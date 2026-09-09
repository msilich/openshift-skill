# Optional read-only StackRox MCP

The [upstream server](https://github.com/stackrox/stackrox-mcp/tree/57264356341b0f5a6aa3cb3b31da33dcb3307104)
is **Developer Preview**, pinned to `57264356341b0f5a6aa3cb3b31da33dcb3307104`.
No binary is bundled or built when loading a skill. OpenShift MCP remains a
separate server. Central administration is not added to this MCP.

## Connected preparation, then transfer

On an approved connected Linux x86_64 build machine, provision Git, make and an
approved Go toolchain compatible with the pinned `go.mod` (`go 1.25.0`). Review
upstream source and dependencies under your software intake policy. These are
preparation commands, not airgap runtime actions:

```bash
git clone https://github.com/stackrox/stackrox-mcp.git
cd stackrox-mcp
git checkout --detach 57264356341b0f5a6aa3cb3b31da33dcb3307104
git rev-parse HEAD
go mod download
go mod verify
GOOS=linux GOARCH=amd64 CGO_ENABLED=0 make build
file stackrox-mcp
sha256sum stackrox-mcp > stackrox-mcp.sha256
```

Record the Go version, source revision, dependency verification and binary hash.
Transfer the binary, checksum, upstream LICENSE, approved CA and skill bundle
through the customer's approved mechanism. A self-generated checksum detects
transfer changes, not publisher authenticity; verify the recorded hash through
the approved intake record. On the disconnected machine run
`sha256sum --check stackrox-mcp.sha256` and validate the binary on RHEL 9-compatible
Linux x86_64 before use. Choose installation paths yourself; nothing is installed
or started automatically by this repository. Do not use an unpinned `latest` image.

## OpenCode configuration

Use [the read profile](../assets/opencode.acs-readonly.jsonc) or
[the Day-2 profile](../assets/opencode.acs-day2.jsonc) as reviewed examples.
They include the existing OpenShift MCP configuration and an `acs_read` local
process. Both keep StackRox read-only; Day-2 adds only narrow Central HTTP patterns.
Do not merge over customer configuration without reviewing effective permissions.
For installed skills adjust `permission.read` to the actual common skills path,
as described in the repository installation guide. Keep the existing Qwen provider.

Set `ACS_MCP_BINARY`, `ACS_CENTRAL_HOST` and `ACS_CA_FILE` to approved nonsecret
values. Provision `ACS_READ_TOKEN` outside OpenCode through the customer's chosen
secret-management mechanism; do not paste or echo it. The profile forwards it as
`STACKROX_MCP__CENTRAL__API_TOKEN`, never in command arguments. Protect the parent
environment and OpenCode session files; environment substitution is not secret
isolation. Do not inspect a resolved config because it may contain credentials.

Both profiles explicitly set `server.type=stdio`, `central.auth_type=static`,
`global.read_only_tools=true`, `central.insecure_skip_tls_verify=false`,
`central.ca_cert_path` and both supported toolsets. The env spelling is
`STACKROX_MCP__SECTION__KEY`; values override upstream defaults. Automatic server
retries are disabled so the skill can control one bounded transient read retry.
Use a dedicated Central identity with only the required read permissions and
access scope. Inspect the local RHACS RBAC chapter for Cluster, Deployment, Node
and vulnerability access; do not create an administrator token for this example.

## Exact tool inventory at the pin

| Allowed OpenCode tool | Use and limits |
| --- | --- |
| `acs_read_list_secured_clusters` | IDs/names/types; choose finite offset/limit. Pagination is client-side after an upstream cluster list, not a server-side scope boundary. |
| `acs_read_get_deployments_for_cve` | CVE/advisory deployment groups; verified `filterClusterId`, optional namespace, follow bounded cursors only when needed. |
| `acs_read_get_nodes_for_cve` | Aggregated node groups; verified `filterClusterId`. Do not report group counts as individual node counts. |
| `acs_read_get_clusters_with_orchestrator_cve` | Orchestrator findings only; verified `filterClusterId`. Not an inventory of every vulnerable workload. |

Read the actual advertised schemas before calls. Prefer ID filters; never pass
both name and ID or infer IDs from names. No other `acs_read_*` tool is allowed.
New tools at another revision require review and explicit allowlist updates.

Validate `opencode mcp list` and offered tool names without exposing configuration
or tokens. Then, against an explicitly authorized target only, test one bounded
cluster read and a scoped known CVE. Compare Central/cluster mapping and permissions.
A connection test does not prove every tool or Qwen workflow. Forbidden stops
the access; TLS failure does not authorize disabling verification.

Source mapping: upstream `internal/config/config.go`, `internal/toolsets/config/tools.go`,
`internal/toolsets/vulnerability/{deployments,nodes,clusters}.go`, `Makefile` and
`go.mod` at the pin above. Configuration examples, identity mapping and OpenCode
approval rules are project-authored adaptations, not upstream support guarantees.
