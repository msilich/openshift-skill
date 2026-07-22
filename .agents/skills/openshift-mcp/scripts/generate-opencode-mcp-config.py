#!/usr/bin/env python3

import argparse
import datetime
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys


DEFAULT_OPENSHIFT_COMMAND = [
    "{env:OPENSHIFT_MCP_BINARY}",
    "--config",
    "{env:OPENSHIFT_MCP_READ_CONFIG}",
    "--kubeconfig",
    "{env:OPENSHIFT_MCP_READ_KUBECONFIG}",
    "--cluster-provider",
    "disabled",
]

DEFAULT_ARGOCD_COMMAND = [
    "{env:ARGOCD_MCP_NODE}",
    "{env:ARGOCD_MCP_ENTRYPOINT}",
    "stdio",
]


class GeneratorError(Exception):
    pass


def default_config_path():
    base = os.environ.get("XDG_CONFIG_HOME")
    if base:
        return Path(base).expanduser().resolve() / "opencode" / "opencode.json"
    return Path.home().resolve() / ".config" / "opencode" / "opencode.json"


def build_parser():
    parser = argparse.ArgumentParser(
        description=(
            "Preview or merge read-only OpenShift and Argo CD MCP entries into "
            "a plain-JSON OpenCode configuration. No packages are installed."
        ),
        epilog=(
            "For npx commands, include --no-install or --offline inside the JSON "
            "array so OpenCode cannot fetch from a registry at startup. Do not "
            "place secrets in command arrays."
        ),
        allow_abbrev=False,
    )
    parser.add_argument(
        "--profile", required=True, choices=("openshift", "argocd", "both")
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=default_config_path(),
        help="OpenCode JSON config (default: XDG_CONFIG_HOME/opencode/opencode.json)",
    )
    parser.add_argument("--openshift-command-json", help="Exact OpenShift MCP command array")
    parser.add_argument("--argocd-command-json", help="Exact Argo CD MCP command array")
    parser.add_argument("--openshift-name", default="ocp_read")
    parser.add_argument("--argocd-name", default="argocd_read")
    parser.add_argument("--permission", choices=("allow", "ask"), default="allow")
    parser.add_argument(
        "--include-argocd-ca",
        action="store_true",
        help="Add NODE_EXTRA_CA_CERTS as an environment reference",
    )
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Replace a conflicting target-name entry after preview",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Atomically write the reviewed configuration",
    )
    return parser


def parse_command(raw, option_name, fallback):
    if raw is None:
        return list(fallback)
    try:
        command = json.loads(raw)
    except json.JSONDecodeError as error:
        raise GeneratorError(
            "{} must be a valid JSON array: {}".format(option_name, error)
        )
    if not isinstance(command, list) or not command:
        raise GeneratorError("{} must be a non-empty JSON array".format(option_name))
    if any(not isinstance(item, str) or not item for item in command):
        raise GeneratorError(
            "{} entries must be non-empty strings".format(option_name)
        )

    forbidden = re.compile(
        r"(^|[-_])(token|password|passwd|api[-_]?key|authorization)(=|:|$)",
        re.IGNORECASE,
    )
    if any(forbidden.search(item) for item in command):
        raise GeneratorError(
            "{} must not contain token, password, API-key, or authorization arguments".format(
                option_name
            )
        )

    executable = Path(command[0]).name.lower()
    if (
        executable in ("npx", "npx.cmd")
        and "--no-install" not in command
        and "--offline" not in command
    ):
        raise GeneratorError(
            "{} uses npx without --no-install or --offline".format(option_name)
        )
    return command


def parse_config(path):
    if not path.exists():
        return {}
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise GeneratorError(
            "OpenCode configuration must be readable plain JSON; comments are "
            "not rewritten safely: {}".format(error)
        )
    if not isinstance(config, dict):
        raise GeneratorError("OpenCode configuration root must be a JSON object")
    return config


def object_property(config, name):
    if name not in config:
        config[name] = {}
    if not isinstance(config[name], dict):
        raise GeneratorError(
            "OpenCode configuration property {} must be an object".format(name)
        )
    return config[name]


def stable(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def command_key(entry):
    if not isinstance(entry, dict) or not isinstance(entry.get("command"), list):
        return None
    return stable(entry["command"])


def merge_entry(mcp, name, entry, replace, actions):
    desired_command = command_key(entry)
    for existing_name, existing_entry in mcp.items():
        if existing_name != name and command_key(existing_entry) == desired_command:
            raise GeneratorError(
                "Equivalent MCP command already exists as {}; refusing duplicate {}".format(
                    existing_name, name
                )
            )

    if name not in mcp:
        mcp[name] = entry
        actions.append((name, "add"))
        return
    if stable(mcp[name]) == stable(entry):
        actions.append((name, "unchanged"))
        return
    if not replace:
        raise GeneratorError(
            "MCP entry {} already exists with different settings; preview with "
            "--replace before applying".format(name)
        )
    mcp[name] = entry
    actions.append((name, "replace"))


def validate_name(value, option_name):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", value):
        raise GeneratorError(
            "{} must contain only letters, digits, underscores, and hyphens".format(
                option_name
            )
        )
    return value


def backup_path(path):
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%S%fZ")
    return Path("{}.backup-{}".format(path, timestamp))


def write_atomic(path, config):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path("{}.tmp-{}".format(path, os.getpid()))
    existed = path.exists()
    mode = stat.S_IMODE(path.stat().st_mode) if existed else 0o600
    backup = None
    try:
        if existed:
            backup = backup_path(path)
            shutil.copy2(str(path), str(backup))
            os.chmod(str(backup), mode)
        with temporary.open("x", encoding="utf-8", newline="\n") as stream:
            json.dump(config, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.chmod(str(temporary), mode)
        os.replace(str(temporary), str(path))
    except OSError as error:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise GeneratorError("Could not write OpenCode configuration: {}".format(error))
    return backup


def generate(arguments):
    config_path = arguments.config.expanduser().resolve()
    openshift_name = validate_name(arguments.openshift_name, "--openshift-name")
    argocd_name = validate_name(arguments.argocd_name, "--argocd-name")
    if arguments.profile == "both" and openshift_name == argocd_name:
        raise GeneratorError("OpenShift and Argo CD MCP names must differ")

    openshift_command = parse_command(
        arguments.openshift_command_json,
        "--openshift-command-json",
        DEFAULT_OPENSHIFT_COMMAND,
    )
    argocd_command = parse_command(
        arguments.argocd_command_json,
        "--argocd-command-json",
        DEFAULT_ARGOCD_COMMAND,
    )

    config = parse_config(config_path)
    original_config = stable(config)
    mcp = object_property(config, "mcp")
    permission = object_property(config, "permission")
    actions = []
    selected = []

    if arguments.profile in ("openshift", "both"):
        entry = {"type": "local", "command": openshift_command, "enabled": True}
        merge_entry(mcp, openshift_name, entry, arguments.replace, actions)
        permission["{}_*".format(openshift_name)] = arguments.permission
        selected.append(
            {"name": openshift_name, "entry": entry, "permission": arguments.permission}
        )

    if arguments.profile in ("argocd", "both"):
        environment = {
            "ARGOCD_BASE_URL": "{env:ARGOCD_BASE_URL}",
            "ARGOCD_TOKEN_REGISTRY_PATH": "{env:ARGOCD_TOKEN_REGISTRY_PATH}",
            "MCP_READ_ONLY": "true",
        }
        if arguments.include_argocd_ca:
            environment["NODE_EXTRA_CA_CERTS"] = "{env:NODE_EXTRA_CA_CERTS}"
        entry = {
            "type": "local",
            "command": argocd_command,
            "enabled": True,
            "timeout": 10000,
            "environment": environment,
        }
        merge_entry(mcp, argocd_name, entry, arguments.replace, actions)
        permission["{}_*".format(argocd_name)] = arguments.permission
        selected.append(
            {"name": argocd_name, "entry": entry, "permission": arguments.permission}
        )

    changed = stable(config) != original_config
    print("Mode: {}".format("apply" if arguments.apply else "preview"))
    print("Config: {}".format(config_path))
    for name, action in actions:
        print("MCP {}: {}".format(name, action))
    print("Proposed entries (credential values are environment references only):")
    print(json.dumps(selected, ensure_ascii=False, indent=2))

    if not arguments.apply:
        print("Persistent changes: none (rerun the reviewed command with --apply)")
        return
    if not changed:
        print("Persistent changes: none (configuration already matches)")
        return

    backup = write_atomic(config_path, config)
    print("OpenCode config: {} (updated)".format(config_path))
    if backup is not None:
        print("Backup: {}".format(backup))
    print("Restart OpenCode and run: opencode mcp list")


def main():
    parser = build_parser()
    arguments = parser.parse_args()
    try:
        generate(arguments)
    except GeneratorError as error:
        print("ERROR: {}".format(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
