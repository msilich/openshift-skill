#!/usr/bin/env bash
set -Eeuo pipefail

umask 077

usage() {
  cat <<'EOF'
Usage:
  new-argocd-token-registry.sh --base-url URL --token-file PATH \
    --cluster-ca PATH --output PATH

Create a protected token registry for one Argo CD instance without printing
the token or placing it in a command-line argument. The customer CA is tested
against the Argo CD endpoint before the registry is written.

Required:
  --base-url URL    HTTPS URL of the Argo CD API
  --token-file PATH File containing the dedicated Argo CD API token
  --cluster-ca PATH PEM CA certificate or CA bundle for Argo CD
  --output PATH     New registry JSON file (must not already exist)
  -h, --help        Show this help
EOF
}

die() {
  printf 'ERROR: %s\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || die "Required command not found: $1"
}

base_url=""
token_file=""
cluster_ca=""
output_file=""

while (($#)); do
  case "$1" in
    --base-url) base_url="${2:?Missing value for --base-url}"; shift 2 ;;
    --token-file) token_file="${2:?Missing value for --token-file}"; shift 2 ;;
    --cluster-ca) cluster_ca="${2:?Missing value for --cluster-ca}"; shift 2 ;;
    --output) output_file="${2:?Missing value for --output}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) die "Unknown option: $1" ;;
  esac
done

[[ -n "$base_url" && -n "$token_file" && -n "$cluster_ca" && -n "$output_file" ]] || {
  usage >&2
  die "All required options must be provided"
}

for command_name in node curl grep mkdir dirname chmod; do
  require_command "$command_name"
done

[[ -r "$token_file" ]] || die "Token file is not readable: $token_file"
[[ -r "$cluster_ca" ]] || die "CA file is not readable: $cluster_ca"
[[ ! -e "$output_file" ]] || die "Output already exists: $output_file"
grep -q -- '-----BEGIN CERTIFICATE-----' "$cluster_ca" || \
  die "CA file is not a PEM certificate or PEM CA bundle: $cluster_ca"

node -e '
  const url = new URL(process.argv[1]);
  if (url.protocol !== "https:") throw new Error("Argo CD URL must use HTTPS");
  if (url.username || url.password || url.search || url.hash) {
    throw new Error("Argo CD URL must not contain credentials, query, or fragment");
  }
' "$base_url"

# Any HTTP response is sufficient here; curl must still complete a verified TLS
# handshake with the supplied CA. Do not add --insecure.
curl --silent --show-error --output /dev/null \
  --cacert "$cluster_ca" \
  --connect-timeout 8 \
  --max-time 20 \
  "${base_url%/}/"

mkdir -p -- "$(dirname -- "$output_file")"
node -e '
  const fs = require("node:fs");
  const [baseUrl, tokenPath, outputPath] = process.argv.slice(1);
  const token = fs.readFileSync(tokenPath, "utf8").trim();
  if (!token) throw new Error("Token file is empty");
  if (/\s/.test(token)) throw new Error("Token file must contain exactly one token");
  const payload = JSON.stringify([{ baseUrl, token }], null, 2) + "\n";
  const fd = fs.openSync(outputPath, "wx", 0o600);
  try { fs.writeFileSync(fd, payload, { encoding: "utf8" }); }
  finally { fs.closeSync(fd); }
' "$base_url" "$token_file" "$output_file"
chmod 0400 -- "$output_file"

printf 'Token registry: %s\n' "$output_file"
printf 'Argo CD base URL: %s\n' "$base_url"
printf 'Customer CA validation: passed\n'
printf 'Token printed: no\n'
