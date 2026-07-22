#!/usr/bin/env bash
set -Eeuo pipefail

umask 077

usage() {
  cat <<'EOF'
Usage:
  update-read-all-token.sh [options]

Options:
  --admin-kubeconfig PATH Admin kubeconfig (default: ~/.kube/config)
  --target PATH           Existing read-all/write-none kubeconfig
  --namespace NAME        ServiceAccount namespace (default: openshift-mcp)
  --service-account NAME  ServiceAccount name (default: opencode-admin-readonly)
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
target_kubeconfig="${HOME}/.config/opencode/openshift-mcp/read-all.kubeconfig"
namespace="openshift-mcp"
service_account="opencode-admin-readonly"
duration="24h"

while (($#)); do
  case "$1" in
    --admin-kubeconfig) admin_kubeconfig="${2:?Missing value for --admin-kubeconfig}"; shift 2 ;;
    --target) target_kubeconfig="${2:?Missing value for --target}"; shift 2 ;;
    --namespace) namespace="${2:?Missing value for --namespace}"; shift 2 ;;
    --service-account) service_account="${2:?Missing value for --service-account}"; shift 2 ;;
    --duration) duration="${2:?Missing value for --duration}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) die "Unknown option: $1" ;;
  esac
done

[[ -r "$admin_kubeconfig" ]] || die "Admin kubeconfig is not readable: $admin_kubeconfig"
[[ -r "$target_kubeconfig" ]] || die "Target kubeconfig is not readable: $target_kubeconfig"

for command_name in oc mktemp chmod cp mv rm dirname; do
  require_command "$command_name"
done

read -r context_count cluster_count user_count < <(
  oc --kubeconfig "$target_kubeconfig" config view --raw \
    -o go-template='{{len .contexts}} {{len .clusters}} {{len .users}}{{"\n"}}'
)
[[ "$context_count" == 1 && "$cluster_count" == 1 && "$user_count" == 1 ]] || \
  die "Target kubeconfig is not limited to one context, cluster and user"

target_server="$(oc --kubeconfig "$target_kubeconfig" config view --raw \
  -o jsonpath='{.clusters[0].cluster.server}')"
embedded_ca_data="$(oc --kubeconfig "$target_kubeconfig" config view --raw \
  -o jsonpath='{.clusters[0].cluster.certificate-authority-data}')"
insecure_tls="$(oc --kubeconfig "$target_kubeconfig" config view --raw \
  -o jsonpath='{.clusters[0].cluster.insecure-skip-tls-verify}')"
context_user="$(oc --kubeconfig "$target_kubeconfig" config view --raw --minify \
  -o jsonpath='{.contexts[0].context.user}')"
[[ -n "$target_server" ]] || die "Target kubeconfig has no API server"
[[ -n "$embedded_ca_data" ]] || die "Target kubeconfig has no embedded CA"
[[ "$insecure_tls" != "true" ]] || die "Target kubeconfig disables TLS verification"
[[ "$context_user" == "$service_account" ]] || \
  die "Target context uses unexpected credential entry: $context_user"

admin_server="$(oc --kubeconfig "$admin_kubeconfig" --request-timeout=8s whoami --show-server)"
[[ "$admin_server" == "$target_server" ]] || \
  die "Admin and target kubeconfig point to different clusters: $admin_server != $target_server"

token=""
temporary_kubeconfig=""
cleanup() {
  unset token
  if [[ -n "$temporary_kubeconfig" && -e "$temporary_kubeconfig" ]]; then
    rm -f -- "$temporary_kubeconfig"
  fi
}
trap cleanup EXIT

token="$(oc --kubeconfig "$admin_kubeconfig" --request-timeout=30s \
  create token "$service_account" --namespace "$namespace" --duration="$duration")"
[[ -n "$token" ]] || die "TokenRequest returned an empty token"

temporary_kubeconfig="$(mktemp "$(dirname -- "$target_kubeconfig")/.read-all.kubeconfig.XXXXXX")"
cp -- "$target_kubeconfig" "$temporary_kubeconfig"
chmod 600 -- "$temporary_kubeconfig"
oc config set-credentials "$service_account" \
  --token="$token" \
  --kubeconfig="$temporary_kubeconfig" >/dev/null

expected_identity="system:serviceaccount:${namespace}:${service_account}"
actual_identity="$(oc --kubeconfig "$temporary_kubeconfig" --request-timeout=8s whoami)"
actual_server="$(oc --kubeconfig "$temporary_kubeconfig" --request-timeout=8s whoami --show-server)"
[[ "$actual_identity" == "$expected_identity" ]] || die "Updated token has unexpected identity: $actual_identity"
[[ "$actual_server" == "$target_server" ]] || die "Updated kubeconfig points to an unexpected API server"

can_read_secrets="$(oc --kubeconfig "$temporary_kubeconfig" --request-timeout=8s \
  auth can-i get secrets --all-namespaces)"
can_create="$(oc --kubeconfig "$temporary_kubeconfig" --request-timeout=8s \
  auth can-i create deployments.apps --all-namespaces)"
can_delete="$(oc --kubeconfig "$temporary_kubeconfig" --request-timeout=8s \
  auth can-i delete pods --all-namespaces)"
[[ "$can_read_secrets" == "yes" ]] || die "Read-all check failed after token update"
[[ "$can_create" == "no" && "$can_delete" == "no" ]] || \
  die "Write-none check failed after token update"

mv -- "$temporary_kubeconfig" "$target_kubeconfig"
temporary_kubeconfig=""
chmod 600 -- "$target_kubeconfig"

printf 'Kubeconfig: %s\n' "$target_kubeconfig"
printf 'API server: %s\n' "$actual_server"
printf 'ServiceAccount identity: %s\n' "$actual_identity"
printf 'Embedded CA retained: yes\n'
printf 'Can read Secrets: %s\n' "$can_read_secrets"
printf 'Can create Deployments: %s\n' "$can_create"
printf 'Can delete Pods: %s\n' "$can_delete"
printf 'Requested token lifetime: %s\n' "$duration"
