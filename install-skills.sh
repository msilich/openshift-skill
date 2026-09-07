#!/usr/bin/env bash
# Install the current checkout's complete skills for the invoking OpenCode user.
# Official path: https://opencode.ai/docs/skills/#place-files
set -euo pipefail
umask 077

usage() {
  printf '%s\n' \
    'Usage: bash install-skills.sh [--dry-run] [--replace] [--target-dir PATH]' \
    '' \
    'Default: $HOME/.config/opencode/skills (run as the intended user, without sudo).' \
    '--dry-run          Show the source and destinations without writing files.' \
    '--replace          Replace existing named skills, retaining a full backup.' \
    '--target-dir PATH  Override the destination with an absolute skill-directory path.' \
    '' \
    'Copies all nine skills and offline docs from this checkout. No downloads,' \
    'OpenCode configuration changes, MCP setup, login, or cluster operations.'
}
fail() { printf 'Error: %s\n' "$*" >&2; exit 1; }

dry_run=false
replace=false
target_dir=''
while (($#)); do
  case "$1" in
    --dry-run) dry_run=true; shift ;;
    --replace) replace=true; shift ;;
    --target-dir)
      (($# >= 2)) || fail '--target-dir needs a path'
      target_dir=$2; shift 2 ;;
    --help|-h) usage; exit 0 ;;
    *) usage >&2; fail "Unknown argument: $1" ;;
  esac
done

[[ -z ${SUDO_USER:-} && -z ${SUDO_UID:-} && $EUID -ne 0 ]] ||
  fail 'Run without sudo, in a login shell of the user who runs OpenCode.'
[[ ${HOME:-} == /* && -d $HOME && -O $HOME ]] ||
  fail 'HOME must be an existing absolute directory owned by the current user.'
if [[ -z $target_dir ]]; then
  # Do not guess how a custom OpenCode/XDG deployment resolves its global paths.
  if [[ -n ${XDG_CONFIG_HOME:-} && $XDG_CONFIG_HOME != "$HOME/.config" ]]; then
    fail 'Custom XDG_CONFIG_HOME detected. Pass --target-dir with the skill path used by your OpenCode installation.'
  fi
  target_dir=$HOME/.config/opencode/skills
fi
[[ $target_dir == /* && $target_dir != / ]] || fail 'Target must be an absolute skill-directory path, not /.'
case "$target_dir/" in
  *'/../'*|*'/./'*|*'//'*) fail 'Use a normalized path without ., .. or repeated slashes.' ;;
esac

# Resolve existing ancestors without creating the destination during a dry-run.
canonical_path() {
  local path=$1 parent
  if [[ -d $path ]]; then
    (cd "$path" && pwd -P)
  else
    [[ ! -e $path && ! -L $path ]] || fail "Not a usable directory: $path"
    parent=$(canonical_path "$(dirname "$path")") || return 1
    printf '%s/%s\n' "${parent%/}" "${path##*/}"
  fi
}
repo_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
source_dir=$repo_dir/.agents/skills
[[ -d $source_dir ]] || fail "Missing bundled skills: $source_dir"
source_dir=$(canonical_path "$source_dir")
target_dir=$(canonical_path "${target_dir%/}")
case "$target_dir/" in "$source_dir/"*) fail 'Target overlaps the source skills.' ;; esac
case "$source_dir/" in "$target_dir/"*) fail 'Target is an ancestor of the source skills.' ;; esac

skills=(openshift-api openshift-docs openshift-mcp openshift-troubleshooting
        openshift-disconnected openshift-gitops openshift-upgrade openshift-backup-restore openshift-devspaces)
printf 'Source: %s\nTarget: %s\n' "$source_dir" "$target_dir"
for skill in "${skills[@]}"; do
  [[ -f $source_dir/$skill/SKILL.md && ! -L $source_dir/$skill ]] ||
    fail "Missing or symlinked source skill: $skill"
  destination=$target_dir/$skill
  [[ ! -L $destination ]] || fail "Refusing a symlink destination: $destination"
  if [[ -e $destination ]]; then
    [[ -d $destination && -f $destination/SKILL.md ]] || fail "Unrecognized existing target: $destination"
    $replace || fail "Already exists: $destination. Review it, then use --replace to back it up and update."
    printf 'Back up and replace: %s\n' "$destination"
  else
    printf 'Install: %s\n' "$destination"
  fi
done
$dry_run && exit 0

parent_dir=$(dirname "$target_dir")
mkdir -p "$parent_dir"
lock_dir=$parent_dir/.openshift-skills-install.lock
mkdir "$lock_dir" 2>/dev/null || fail "Another install may be active: $lock_dir"
stage_dir=''
installed=()
backed_up=()
finished=false
cleanup() {
  local status=$? skill index
  trap - EXIT HUP INT TERM
  set +e
  if ! $finished && [[ -n $stage_dir ]]; then
    # Move failed new copies aside, then restore every original directory.
    for ((index=${#installed[@]}-1; index>=0; index--)); do
      skill=${installed[index]}
      if [[ -e $target_dir/$skill || -L $target_dir/$skill ]]; then
        mv "$target_dir/$skill" "$stage_dir/payload/$skill"
      fi
    done
    for ((index=0; index<${#backed_up[@]}; index++)); do
      skill=${backed_up[index]}
      mv "$stage_dir/previous/$skill" "$target_dir/$skill"
    done
    printf 'Installation failed. Recovery files retained at: %s\n' "$stage_dir" >&2
  fi
  rmdir "$lock_dir"
  exit "$status"
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' HUP TERM
stage_dir=$(mktemp -d "$parent_dir/.openshift-skills-install.XXXXXXXX")
mkdir "$stage_dir/payload" "$stage_dir/previous"
for skill in "${skills[@]}"; do
  cp -R "$source_dir/$skill" "$stage_dir/payload/$skill"
done
mkdir -p "$target_dir"
for skill in "${skills[@]}"; do
  destination=$target_dir/$skill
  [[ ! -L $destination ]] || fail "Destination changed to a symlink: $destination"
  if [[ -e $destination ]]; then
    $replace || fail "Destination appeared during installation: $destination"
    [[ -d $destination && -f $destination/SKILL.md ]] || fail "Destination changed: $destination"
    mv "$destination" "$stage_dir/previous/$skill"
    backed_up+=("$skill")
  fi
  installed+=("$skill")
  mv "$stage_dir/payload/$skill" "$destination"
done
finished=true
rmdir "$stage_dir/payload"
if ((${#backed_up[@]})); then
  printf 'Original skills retained outside discovery paths: %s/previous\n' "$stage_dir"
else
  rmdir "$stage_dir/previous" "$stage_dir"
fi
printf '\nInstalled all nine skills in: %s\n' "$target_dir"
printf '%s\n' \
  'Restart OpenCode. Test from a directory outside this repository to avoid duplicate skill names.' \
  'Existing model, MCP, kubeconfig and permission settings were not changed.' \
  'If your profile restricts skill file reads, allow this destination in that profile.'
