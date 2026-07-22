#!/usr/bin/env bash
set -Eeuo pipefail

umask 077

readonly upstream_url="https://github.com/argoproj-labs/mcp-for-argocd.git"
readonly upstream_revision="1bb80b2816f0c8810efedc2fdcf318fd18ce214d"

usage() {
  cat <<'EOF'
Usage:
  build-argocd-mcp-airgap-bundle.sh [--output-dir PATH]

Build and test the pinned Argo CD MCP server on a connected Linux host, then
create a production dependency bundle and SHA-256 checksum for air-gapped
transfer. Build on the same Linux architecture as the disconnected target.

Options:
  --output-dir PATH  Destination for archive and checksum (default: ./dist-airgap)
  -h, --help         Show this help
EOF
}

die() {
  printf 'ERROR: %s\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || die "Required command not found: $1"
}

output_dir="${PWD}/dist-airgap"

while (($#)); do
  case "$1" in
    --output-dir) output_dir="${2:?Missing value for --output-dir}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) die "Unknown option: $1" ;;
  esac
done

[[ "$(uname -s)" == "Linux" ]] || \
  die "Build this bundle on a connected Linux host matching the target architecture"

for command_name in git node corepack tar sha256sum mktemp mkdir chmod uname rm; do
  require_command "$command_name"
done

node_major="$(node -p 'Number(process.versions.node.split(".")[0])')"
[[ "$node_major" =~ ^[0-9]+$ && "$node_major" -ge 18 ]] || \
  die "Node.js 18 or newer is required; Node.js 22 or 24 LTS is recommended"

mkdir -p -- "$output_dir"
output_dir="$(cd -- "$output_dir" && pwd -P)"
architecture="$(uname -m)"
archive_name="argocd-mcp-${upstream_revision:0:12}-linux-${architecture}.tar.gz"
archive_path="${output_dir}/${archive_name}"
checksum_path="${archive_path}.sha256"

[[ ! -e "$archive_path" && ! -e "$checksum_path" ]] || \
  die "Output already exists: $archive_path or $checksum_path"

temporary_root="$(mktemp -d)"
success=0
cleanup() {
  rm -rf -- "$temporary_root"
  if [[ "$success" -ne 1 ]]; then
    rm -f -- "$archive_path" "$checksum_path"
  fi
}
trap cleanup EXIT

source_dir="${temporary_root}/source"
bundle_dir="${temporary_root}/argocd-mcp"

git clone --quiet "$upstream_url" "$source_dir"
git -C "$source_dir" checkout --quiet --detach "$upstream_revision"
actual_revision="$(git -C "$source_dir" rev-parse HEAD)"
[[ "$actual_revision" == "$upstream_revision" ]] || \
  die "Unexpected source revision: $actual_revision"

(
  cd -- "$source_dir"
  corepack pnpm install --frozen-lockfile
  corepack pnpm test
  corepack pnpm build
  corepack pnpm --filter argocd-mcp --legacy deploy --prod "$bundle_dir"
)

[[ -f "${bundle_dir}/dist/index.js" ]] || die "Production entry point is missing"
[[ -f "${bundle_dir}/LICENSE" ]] || die "Upstream license is missing from bundle"

tar -C "$temporary_root" -czf "$archive_path" argocd-mcp
(
  cd -- "$output_dir"
  sha256sum "$archive_name" >"${archive_name}.sha256"
)
chmod 0644 -- "$archive_path" "$checksum_path"
success=1

printf 'Source revision: %s\n' "$actual_revision"
printf 'Node.js: %s\n' "$(node --version)"
printf 'Bundle: %s\n' "$archive_path"
printf 'Checksum: %s\n' "$checksum_path"
