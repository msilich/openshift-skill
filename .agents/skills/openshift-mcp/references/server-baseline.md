# Server and client baseline

## Pinned source

Base these instructions and examples on `openshift/openshift-mcp-server` commit [`a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd`](https://github.com/openshift/openshift-mcp-server/tree/a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd), inspected 2026-07-22. Revalidate flags, tool names, annotations, and defaults before changing the pinned revision.

Primary source points:

- [OpenShift Developer Preview statement and downstream defaults](https://github.com/openshift/openshift-mcp-server/blob/a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd/docs/openshift/user-guide.md)
- [Configuration, tool filtering, denied resources, validation, and confirmation fallback](https://github.com/openshift/openshift-mcp-server/blob/a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd/docs/configuration.md)
- [`configuration_view` tool implementation](https://github.com/openshift/openshift-mcp-server/blob/a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd/pkg/toolsets/config/configuration.go)
- [Core tool implementations and annotations](https://github.com/openshift/openshift-mcp-server/tree/a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd/pkg/toolsets/core)

The repository builds the native binary as `kubernetes-mcp-server`. The OpenShift fork had no GitHub release artifacts at the inspected revision, so build this pinned source rather than presenting an upstream release binary as equivalent. Use the local native binary in air-gapped environments; do not use `npx ...@latest` or an unpinned container pull.

## Download and build

The pinned source declares Go 1.26.3. On a connected build host with Git, Go, and GNU Make:

```text
git clone https://github.com/openshift/openshift-mcp-server.git
cd openshift-mcp-server
git checkout --detach a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd
test "$(git rev-parse HEAD)" = "a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd"
make build
./kubernetes-mcp-server --help
```

Install the resulting native binary in a protected executable path or transfer it to the disconnected target together with a SHA-256 checksum. Build on the target OS and architecture, or cross-compile deliberately; never relabel a binary built for another platform. The build downloads Go modules, so complete it on a connected host or through an approved internal Go module mirror before entering an air-gapped environment.

## Required server controls

- Set an explicit `kubeconfig` path.
- Set `cluster_provider_strategy = "disabled"` to expose only the kubeconfig's current context. Minify the kubeconfig to one context first.
- Keep the read server on `toolsets = ["core"]` with an explicit `enabled_tools` allowlist. Do not trust repository defaults because upstream and downstream defaults differ.
- Make the intentionally privileged Day-2 profile complete by explicitly enabling every toolset registered in the pinned downstream build and enabling target-compatibility filtering. Disable only `configuration_view`. Every resulting tool call must pass OpenCode's `ask` gate; unavailable or unconfigured extension backends may still fail cleanly.
- Set `validation_enabled = true` for schema validation and SelfSubjectAccessReview prechecks. Keep OpenShift RBAC authoritative.
- Set `read_only = true` for the read server. `disable_destructive` alone is insufficient because some creating tools are not annotated destructive.
- Exclude `configuration_view`; the read profile omits `config`, while the complete Day-2 profile disables that tool explicitly.
- Use separate MCP process names and kubeconfigs for read and Day-2 identities.

## Confirmation compatibility

At OpenCode commit [`0317531906d3f3bb01cf33c16319870cfde9170c`](https://github.com/anomalyco/opencode/blob/0317531906d3f3bb01cf33c16319870cfde9170c/packages/opencode/src/mcp/index.ts#L38-L50), MCP elicitation is not advertised. A matching MCP confirmation rule therefore either blocks with fallback `deny` or proceeds silently with fallback `allow`; it cannot provide an interactive OpenCode confirmation.

Use OpenCode's own wildcard permissions for per-call approval. Keep the supplied MCP configs free of `[[confirmation_rules]]`. Re-test this behavior after any OpenCode upgrade.

## Model acceptance gate

Before enabling `ocp_day2`, evaluate the exact model ID, provider, serving stack, context window, and tool-calling template against a disposable cluster. Require correct tool selection, exact namespace/name targeting, valid manifests, refusal on target ambiguity, stable multi-step verification, resistance to instructions in logs, and no Secret exfiltration. Do not assume that a model is safe because another model from the same provider passed.

The read-only and Day-2 OpenCode profiles are provider-independent. For Qwen, optionally merge `assets/opencode.qwen-provider.jsonc`, replace `REPLACE_WITH_QWEN_MODEL_ID` with the exact ID returned by the OpenAI-compatible `/v1/models` endpoint, and keep the provider API key in an environment variable.

## Portable installation

Keep kubeconfigs outside the project with restrictive filesystem permissions. The OpenCode templates under `assets/` take the binary, TOML, and kubeconfig paths from `OPENSHIFT_MCP_*` environment variables and pass the kubeconfig explicitly on the command line. Copy the templates to a protected local configuration directory or point the environment variables at their absolute checked-out paths; do not depend on the caller's current directory.
