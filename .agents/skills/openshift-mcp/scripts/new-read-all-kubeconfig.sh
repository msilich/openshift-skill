#!/usr/bin/env bash
set -Eeuo pipefail

umask 077

usage() {
  cat <<'EOF'
Usage:
  new-read-all-kubeconfig.sh --cluster-ca PATH [options]

Required:
  --cluster-ca PATH       PEM CA certificate or CA bundle for the API server

Options:
  --admin-kubeconfig PATH Admin kubeconfig (default: ~/.kube/config)
  --output PATH           New read-all/write-none kubeconfig
  --namespace NAME        ServiceAccount namespace (default: openshift-mcp)
  --service-account NAME  ServiceAccount name (default: opencode-admin-readonly)
  --context NAME          Context name (default: opencode-admin-readonly)
  --default-namespace NS  Context namespace (default: default)
  --duration DURATION     Requested token lifetime (default: 24h)
  -h, --help              Show this help
EOF
}

die() {
  printf 'ERROR: %s\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || die "Required command not found: $1"
}

admin_kubeconfig="${HOME}/.kube/config"
output_kubeconfig="${HOME}/.config/opencode/openshift-mcp/read-all.kubeconfig"
cluster_ca=""
namespace="openshift-mcp"
service_account="opencode-admin-readonly"
context_name="opencode-admin-readonly"
default_namespace="default"
duration="24h"

while (($#)); do
  case "$1" in
    --cluster-ca) cluster_ca="${2:?Missing value for --cluster-ca}"; shift 2 ;;
    --admin-kubeconfig) admin_kubeconfig="${2:?Missing value for --admin-kubeconfig}"; shift 2 ;;
    --output) output_kubeconfig="${2:?Missing value for --output}"; shift 2 ;;
    --namespace) namespace="${2:?Missing value for --namespace}"; shift 2 ;;
    --service-account) service_account="${2:?Missing value for --service-account}"; shift 2 ;;
    --context) context_name="${2:?Missing value for --context}"; shift 2 ;;
    --default-namespace) default_namespace="${2:?Missing value for --default-namespace}"; shift 2 ;;
    --duration) duration="${2:?Missing value for --duration}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) die "Unknown option: $1" ;;
  esac
done

[[ -n "$cluster_ca" ]] || { usage >&2; die "--cluster-ca is required"; }
[[ -r "$admin_kubeconfig" ]] || die "Admin kubeconfig is not readable: $admin_kubeconfig"
[[ -r "$cluster_ca" ]] || die "CA file is not readable: $cluster_ca"
[[ ! -e "$output_kubeconfig" ]] || die "Output already exists; use the token update script: $output_kubeconfig"

for command_name in oc grep base64 cmp mktemp chmod mkdir dirname rm; do
  require_command "$command_name"
done

grep -q -- '-----BEGIN CERTIFICATE-----' "$cluster_ca" || \
  die "CA file is not a PEM certificate or PEM CA bundle: $cluster_ca"

api_server="$(oc --kubeconfig "$admin_kubeconfig" config view --raw --minify --flatten \
  -o jsonpath='{.clusters[0].cluster.server}')"
[[ -n "$api_server" ]] || die "No API server found in the admin kubeconfig"

admin_identity="$(oc --kubeconfig "$admin_kubeconfig" --request-timeout=8s whoami)"
admin_server="$(oc --kubeconfig "$admin_kubeconfig" --request-timeout=8s whoami --show-server)"
[[ "$admin_server" == "$api_server" ]] || \
  die "Admin context and selected API server differ: $admin_server != $api_server"

# Force validation with the customer CA. Never inherit an insecure TLS setting.
oc --kubeconfig "$admin_kubeconfig" \
  --server="$api_server" \
  --certificate-authority="$cluster_ca" \
  --insecure-skip-tls-verify=false \
  --request-timeout=8s \
  get --raw /version >/dev/null

oc --kubeconfig "$admin_kubeconfig" --request-timeout=8s \
  get serviceaccount "$service_account" --namespace "$namespace" -o name >/dev/null

token=""
created_output=0
success=0
embedded_ca_file=""
cleanup() {
  unset token
  if [[ -n "$embedded_ca_file" && -e "$embedded_ca_file" ]]; then
    rm -f -- "$embedded_ca_file"
  fi
  if [[ "$success" -ne 1 && "$created_output" -eq 1 && -e "$output_kubeconfig" ]]; then
    rm -f -- "$output_kubeconfig"
  fi
}
trap cleanup EXIT

token="$(oc --kubeconfig "$admin_kubeconfig" --request-timeout=30s \
  create token "$service_account" --namespace "$namespace" --duration="$duration")"
[[ -n "$token" ]] || die "TokenRequest returned an empty token"

mkdir -p -- "$(dirname -- "$output_kubeconfig")"
created_output=1
oc config set-cluster openshift-mcp-cluster \
  --server="$api_server" \
  --certificate-authority="$cluster_ca" \
  --embed-certs=true \
  --kubeconfig="$output_kubeconfig" >/dev/null
oc config set-credentials "$service_account" \
  --token="$token" \
  --kubeconfig="$output_kubeconfig" >/dev/null
chmod 600 -- "$output_kubeconfig"
oc config set-context "$context_name" \
  --cluster=openshift-mcp-cluster \
  --user="$service_account" \
  --namespace="$default_namespace" \
  --kubeconfig="$output_kubeconfig" >/dev/null
oc config use-context "$context_name" --kubeconfig="$output_kubeconfig" >/dev/null

read -r context_count cluster_count user_count < <(
  oc --kubeconfig "$output_kubeconfig" config view --raw \
    -o go-template='{{len .contexts}} {{len .clusters}} {{len .users}}{{"\n"}}'
)
[[ "$context_count" == 1 && "$cluster_count" == 1 && "$user_count" == 1 ]] || \
  die "Generated kubeconfig is not limited to one context, cluster and user"

embedded_ca_data="$(oc --kubeconfig "$output_kubeconfig" config view --raw \
  -o jsonpath='{.clusters[0].cluster.certificate-authority-data}')"
insecure_tls="$(oc --kubeconfig "$output_kubeconfig" config view --raw \
  -o jsonpath='{.clusters[0].cluster.insecure-skip-tls-verify}')"
[[ -n "$embedded_ca_data" ]] || die "Customer CA was not embedded"
[[ "$insecure_tls" != "true" ]] || die "Generated kubeconfig disables TLS verification"

embedded_ca_file="$(mktemp)"
printf '%s' "$embedded_ca_data" | base64 --decode >"$embedded_ca_file"
cmp -s -- "$cluster_ca" "$embedded_ca_file" || die "Embedded CA differs from the supplied CA file"

expected_identity="system:serviceaccount:${namespace}:${service_account}"
actual_identity="$(oc --kubeconfig "$output_kubeconfig" --request-timeout=8s whoami)"
actual_server="$(oc --kubeconfig "$output_kubeconfig" --request-timeout=8s whoami --show-server)"
[[ "$actual_identity" == "$expected_identity" ]] || die "Unexpected ServiceAccount identity: $actual_identity"
[[ "$actual_server" == "$api_server" ]] || die "Generated kubeconfig points to an unexpected API server"

can_read_secrets="$(oc --kubeconfig "$output_kubeconfig" --request-timeout=8s \
  auth can-i get secrets --all-namespaces)"
can_create="$(oc --kubeconfig "$output_kubeconfig" --request-timeout=8s \
  auth can-i create deployments.apps --all-namespaces)"
can_delete="$(oc --kubeconfig "$output_kubeconfig" --request-timeout=8s \
  auth can-i delete pods --all-namespaces)"
[[ "$can_read_secrets" == "yes" ]] || die "Read-all check failed: cannot read Secrets"
[[ "$can_create" == "no" && "$can_delete" == "no" ]] || \
  die "Write-none check failed: create or delete is unexpectedly allowed"

success=1
printf 'Kubeconfig: %s\n' "$output_kubeconfig"
printf 'API server: %s\n' "$actual_server"
printf 'Admin identity used for TokenRequest: %s\n' "$admin_identity"
printf 'ServiceAccount identity: %s\n' "$actual_identity"
printf 'Customer CA embedded: yes\n'
printf 'TLS verification disabled: no\n'
printf 'Can read Secrets: %s\n' "$can_read_secrets"
printf 'Can create Deployments: %s\n' "$can_create"
printf 'Can delete Pods: %s\n' "$can_delete"
printf 'Requested token lifetime: %s\n' "$duration"
