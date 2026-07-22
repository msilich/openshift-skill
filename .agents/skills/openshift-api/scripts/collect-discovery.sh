#!/usr/bin/env bash

set -uo pipefail

usage() {
  printf 'Usage: %s --kubeconfig PATH --resource RESOURCE --api-version VERSION [--field FIELD_PATH] [--crd CRD_NAME]\n' "$0" >&2
}

kubeconfig=''
resource=''
api_version=''
field=''
crd=''

while (($#)); do
  case "$1" in
    --kubeconfig)
      [[ $# -ge 2 ]] || { usage; exit 64; }
      kubeconfig=$2
      shift 2
      ;;
    --resource)
      [[ $# -ge 2 ]] || { usage; exit 64; }
      resource=$2
      shift 2
      ;;
    --api-version)
      [[ $# -ge 2 ]] || { usage; exit 64; }
      api_version=$2
      shift 2
      ;;
    --field)
      [[ $# -ge 2 ]] || { usage; exit 64; }
      field=$2
      shift 2
      ;;
    --crd)
      [[ $# -ge 2 ]] || { usage; exit 64; }
      crd=$2
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown argument: %s\n' "$1" >&2
      usage
      exit 64
      ;;
  esac
done

if [[ -z "$kubeconfig" || -z "$resource" || -z "$api_version" ]]; then
  usage
  exit 64
fi

oc_bin=${OC_BIN:-oc}
python_bin=${PYTHON_BIN:-python3}
oc_prefix=(--kubeconfig "$kubeconfig")
schema_sources=0

show_source() {
  printf 'Source command: oc'
  printf ' %q' "${oc_prefix[@]}"
  printf ' %q' "$@"
  printf '\n'
}

run_required() {
  local label=$1
  shift
  printf '\n## %s\n' "$label"
  show_source "$@"
  if "$oc_bin" "${oc_prefix[@]}" "$@"; then
    return 0
  fi
  printf 'Discovery stopped: required stage failed: %s. Do not infer API data.\n' "$label" >&2
  return 1
}

run_schema_source() {
  local label=$1
  shift
  printf '\n## %s\n' "$label"
  show_source "$@"
  if "$oc_bin" "${oc_prefix[@]}" "$@"; then
    schema_sources=$((schema_sources + 1))
    return 0
  fi
  printf 'Schema source unavailable: %s. Continue to the next source; do not infer fields.\n' "$label" >&2
  return 0
}

run_openapi_source() {
  local index relative_url expected_key
  printf '\n## OpenAPI v3 index\n'
  show_source get --raw /openapi/v3
  if ! index=$("$oc_bin" "${oc_prefix[@]}" get --raw /openapi/v3); then
    printf 'Optional discovery source unavailable: OpenAPI v3 index.\n' >&2
    return 0
  fi

  if [[ "$api_version" == */* ]]; then
    expected_key="apis/$api_version"
  else
    expected_key="api/$api_version"
  fi

  relative_url=$(printf '%s' "$index" | "$python_bin" -c '
import json
import sys

expected = sys.argv[1]
try:
    paths = json.load(sys.stdin).get("paths", {})
except (AttributeError, json.JSONDecodeError):
    raise SystemExit(2)
entry = paths.get(expected) or paths.get("/" + expected)
url = entry.get("serverRelativeURL") if isinstance(entry, dict) else None
if not isinstance(url, str) or not url.startswith("/openapi/v3/"):
    raise SystemExit(3)
sys.stdout.write(url)
' "$expected_key") || {
    printf 'The OpenAPI v3 index did not advertise a safe document for %s; do not guess its URL.\n' "$api_version" >&2
    return 0
  }

  printf 'Advertised serverRelativeURL: %s\n' "$relative_url"
  run_schema_source 'Advertised OpenAPI v3 document' get --raw "$relative_url"
}

run_required 'API resources' api-resources -o wide || exit 1
run_required 'API versions' api-versions || exit 1
run_schema_source 'Versioned resource explanation' explain "$resource" "--api-version=$api_version"
recursive_target=$resource
if [[ -n "$field" ]]; then
  recursive_target="$resource.$field"
fi
run_schema_source 'Recursive versioned field' explain "$recursive_target" "--api-version=$api_version" --recursive
run_openapi_source

if [[ -n "$crd" ]]; then
  run_schema_source 'CRD schema source' get crd "$crd" -o json
fi

if ((schema_sources == 0)); then
  printf 'No field-bearing schema source succeeded. Fetch the advertised OpenAPI v3 document or provide the CRD schema. Never invent schema.\n' >&2
  exit 2
fi

printf '\nEvidence collection complete. Cite the exact successful source command and API version in the result.\n'
