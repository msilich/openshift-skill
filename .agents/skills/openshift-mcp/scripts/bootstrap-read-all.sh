#!/usr/bin/env bash
set -Eeuo pipefail

umask 077

usage() {
  cat <<'EOF'
Usage:
  bootstrap-read-all.sh COMMAND --admin-kubeconfig PATH \
    --expected-server URL --expected-admin-identity NAME --output PATH [options]

Commands:
  preview             Validate the target and preview the bundled RBAC
  apply-rbac          Revalidate, apply RBAC, and verify read-all/write-none
  create-kubeconfig   Revalidate RBAC, request a token, and write the kubeconfig

Required:
  --admin-kubeconfig PATH       Existing administrative kubeconfig
  --expected-server URL         Exact expected OpenShift API URL
  --expected-admin-identity ID  Exact expected result of `oc whoami`
  --output PATH                 New read-all/write-none kubeconfig

Options:
  --cluster-ca PATH             Explicit PEM CA bundle; otherwise copy the CA
                                embedded in the admin kubeconfig
  --duration DURATION           Requested token lifetime (default: 24h)
  -h, --help                    Show this help

Run the three commands in order. The first is read-only. Obtain a separate
approval before apply-rbac and another approval before create-kubeconfig.
EOF
}

die() {
  printf 'ERROR: %s\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || die "Required command not found: $1"
}

require_absolute_path() {
  local label="$1"
  local path="$2"
  [[ "$path" == /* ]] || die "$label must be an absolute path: $path"
}

run_oc() {
  oc --kubeconfig "$admin_kubeconfig" "$@"
}

can_i_as_read_identity() {
  run_oc --request-timeout=8s auth can-i "$@" \
    --as="system:serviceaccount:openshift-mcp:opencode-admin-readonly"
}

verify_read_all_write_none() {
  local can_get_namespaces can_list_pods can_get_secrets
  local can_create can_patch can_delete

  run_oc --request-timeout=8s get serviceaccount opencode-admin-readonly \
    --namespace openshift-mcp -o name >/dev/null

  can_get_namespaces="$(can_i_as_read_identity get namespaces)"
  can_list_pods="$(can_i_as_read_identity list pods --all-namespaces)"
  can_get_secrets="$(can_i_as_read_identity get secrets --all-namespaces)"
  can_create="$(can_i_as_read_identity create deployments.apps --all-namespaces)"
  can_patch="$(can_i_as_read_identity patch deployments.apps --all-namespaces)"
  can_delete="$(can_i_as_read_identity delete pods --all-namespaces)"

  [[ "$can_get_namespaces" == "yes" ]] || die "Read check failed: cannot get namespaces"
  [[ "$can_list_pods" == "yes" ]] || die "Read check failed: cannot list pods cluster-wide"
  [[ "$can_get_secrets" == "yes" ]] || die "Read check failed: cannot get Secrets cluster-wide"
  [[ "$can_create" == "no" ]] || die "Write check failed: can create Deployments"
  [[ "$can_patch" == "no" ]] || die "Write check failed: can patch Deployments"
  [[ "$can_delete" == "no" ]] || die "Write check failed: can delete Pods"

  printf 'Can get namespaces: %s\n' "$can_get_namespaces"
  printf 'Can list Pods cluster-wide: %s\n' "$can_list_pods"
  printf 'Can get Secrets cluster-wide: %s\n' "$can_get_secrets"
  printf 'Can create Deployments: %s\n' "$can_create"
  printf 'Can patch Deployments: %s\n' "$can_patch"
  printf 'Can delete Pods: %s\n' "$can_delete"
}

preview_rbac() {
  local diff_status

  set +e
  run_oc diff -f "$rbac_dir"
  diff_status=$?
  set -e
  [[ "$diff_status" -eq 0 || "$diff_status" -eq 1 ]] || \
    die "oc diff failed with exit code $diff_status"

  run_oc apply --dry-run=server -o name -f "$rbac_dir"
}

[[ $# -gt 0 ]] || { usage >&2; exit 2; }

command_name="$1"
shift

case "$command_name" in
  preview|apply-rbac|create-kubeconfig) ;;
  -h|--help) usage; exit 0 ;;
  *) usage >&2; die "Unknown command: $command_name" ;;
esac

admin_kubeconfig=""
cluster_ca=""
expected_server=""
expected_admin_identity=""
output_kubeconfig=""
duration="24h"

while (($#)); do
  case "$1" in
    --admin-kubeconfig) admin_kubeconfig="${2:?Missing value for --admin-kubeconfig}"; shift 2 ;;
    --cluster-ca) cluster_ca="${2:?Missing value for --cluster-ca}"; shift 2 ;;
    --expected-server) expected_server="${2:?Missing value for --expected-server}"; shift 2 ;;
    --expected-admin-identity) expected_admin_identity="${2:?Missing value for --expected-admin-identity}"; shift 2 ;;
    --output) output_kubeconfig="${2:?Missing value for --output}"; shift 2 ;;
    --duration) duration="${2:?Missing value for --duration}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) die "Unknown option: $1" ;;
  esac
done

[[ -n "$admin_kubeconfig" ]] || die "--admin-kubeconfig is required"
[[ -n "$expected_server" ]] || die "--expected-server is required"
[[ -n "$expected_admin_identity" ]] || die "--expected-admin-identity is required"
[[ -n "$output_kubeconfig" ]] || die "--output is required"

require_absolute_path "Admin kubeconfig" "$admin_kubeconfig"
require_absolute_path "Output kubeconfig" "$output_kubeconfig"

[[ -r "$admin_kubeconfig" ]] || die "Admin kubeconfig is not readable: $admin_kubeconfig"
[[ ! -e "$output_kubeconfig" && ! -L "$output_kubeconfig" ]] || \
  die "Output already exists; refusing to overwrite: $output_kubeconfig"

for command_dependency in oc grep base64 chmod dirname mktemp rm; do
  require_command "$command_dependency"
done

script_dir="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
skill_dir="$(dirname -- "$script_dir")"
rbac_dir="$skill_dir/assets/read-all-rbac"
create_kubeconfig_script="$script_dir/new-read-all-kubeconfig.sh"

[[ -d "$rbac_dir" ]] || die "Bundled RBAC directory is missing: $rbac_dir"
[[ -x "$create_kubeconfig_script" ]] || \
  die "Kubeconfig creation script is not executable: $create_kubeconfig_script"

temporary_ca=""
cleanup() {
  if [[ -n "$temporary_ca" && -e "$temporary_ca" ]]; then
    rm -f -- "$temporary_ca"
  fi
}
trap cleanup EXIT

actual_context="$(run_oc config current-context)"
actual_admin_identity="$(run_oc --request-timeout=8s whoami)"
actual_server="$(run_oc --request-timeout=8s whoami --show-server)"

[[ "$actual_admin_identity" == "$expected_admin_identity" ]] || \
  die "Admin identity mismatch: $actual_admin_identity != $expected_admin_identity"
[[ "$actual_server" == "$expected_server" ]] || \
  die "API server mismatch: $actual_server != $expected_server"

if [[ -n "$cluster_ca" ]]; then
  require_absolute_path "Cluster CA" "$cluster_ca"
  [[ -r "$cluster_ca" ]] || die "CA file is not readable: $cluster_ca"
  ca_source="$cluster_ca"
else
  admin_insecure_tls="$(run_oc config view --raw --minify --flatten \
    -o jsonpath='{.clusters[0].cluster.insecure-skip-tls-verify}')"
  [[ "$admin_insecure_tls" != "true" ]] || \
    die "Admin kubeconfig disables TLS verification; refusing to copy its trust settings"

  admin_ca_data="$(run_oc config view --raw --minify --flatten \
    -o jsonpath='{.clusters[0].cluster.certificate-authority-data}')"
  [[ -n "$admin_ca_data" ]] || \
    die "Admin kubeconfig has no embedded CA; provide --cluster-ca explicitly"

  temporary_ca="$(mktemp)"
  printf '%s' "$admin_ca_data" | base64 --decode >"$temporary_ca"
  chmod 600 -- "$temporary_ca"
  cluster_ca="$temporary_ca"
  ca_source="embedded CA from admin kubeconfig"
fi

grep -q -- '-----BEGIN CERTIFICATE-----' "$cluster_ca" || \
  die "Selected CA is not a PEM certificate or PEM CA bundle"

run_oc \
  --server="$expected_server" \
  --certificate-authority="$cluster_ca" \
  --insecure-skip-tls-verify=false \
  --request-timeout=8s \
  get --raw /version >/dev/null

printf 'Command: %s\n' "$command_name"
printf 'Admin context: %s\n' "$actual_context"
printf 'Admin identity: %s\n' "$actual_admin_identity"
printf 'API server: %s\n' "$actual_server"
printf 'Customer CA validation: success\n'
printf 'Customer CA source: %s\n' "$ca_source"
printf 'RBAC directory: %s\n' "$rbac_dir"
printf 'Output kubeconfig: %s\n' "$output_kubeconfig"

case "$command_name" in
  preview)
    preview_rbac
    printf 'Persistent changes: none\n'
    printf 'Next command after Gate 1 approval: apply-rbac\n'
    ;;
  apply-rbac)
    preview_rbac
    run_oc apply -f "$rbac_dir"
    verify_read_all_write_none
    printf 'Credential created: no\n'
    printf 'Next command after Gate 2 approval: create-kubeconfig\n'
    ;;
  create-kubeconfig)
    verify_read_all_write_none
    "$create_kubeconfig_script" \
      --admin-kubeconfig "$admin_kubeconfig" \
      --cluster-ca "$cluster_ca" \
      --output "$output_kubeconfig" \
      --duration "$duration"

    actual_read_identity="$(oc --kubeconfig "$output_kubeconfig" --request-timeout=8s whoami)"
    actual_read_server="$(oc --kubeconfig "$output_kubeconfig" --request-timeout=8s whoami --show-server)"
    [[ "$actual_read_identity" == "system:serviceaccount:openshift-mcp:opencode-admin-readonly" ]] || \
      die "Generated kubeconfig has an unexpected identity: $actual_read_identity"
    [[ "$actual_read_server" == "$expected_server" ]] || \
      die "Generated kubeconfig has an unexpected API server: $actual_read_server"

    printf 'Bootstrap completed: yes\n'
    ;;
esac
