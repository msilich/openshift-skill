# OpenShift Agent Skills for OpenCode

Three portable, English-language agent skills for operating and researching
OpenShift with [OpenCode](https://opencode.ai/):

- `openshift-mcp` — MCP-first diagnosis and controlled Day-2 operations with
  `oc` as a fallback.
- `openshift-api` — live API discovery with `oc api-resources`, `oc explain`,
  OpenAPI v3, and CRD schemas.
- `openshift-docs` — a complete, searchable, offline OpenShift Container
  Platform 4.20 documentation snapshot.

The skills are model-provider independent. An optional OpenAI-compatible Qwen
provider example is included for local and air-gapped deployments.

> [!WARNING]
> The OpenShift MCP server is Developer Preview at the pinned baseline and is
> not recommended for production use by its maintainers. These skills provide
> workflows and guardrails; they do not replace OpenShift RBAC, admission
> policy, process isolation, or human review.

## Repository contents

| Path | Purpose |
| --- | --- |
| `.agents/skills/openshift-mcp/` | MCP operation, safety, and configuration skill |
| `.agents/skills/openshift-mcp/assets/read-all-rbac/` | Optional cluster-wide read-all/write-none RBAC, including Secrets |
| `.agents/skills/openshift-mcp/scripts/` | CA-aware kubeconfig and token bootstrap scripts for Linux and Windows |
| `.agents/skills/openshift-api/` | Live API/schema discovery skill and helper |
| `.agents/skills/openshift-docs/` | Offline OCP 4.20 documentation skill |
| `sources.lock.json` | Exact source and compatibility baselines |
| `tools/docs/` | Reproducible documentation conversion inputs |
| `tests/` | Offline integrity and behavior checks |

## Tested baseline

- OpenCode 1.18.4
- OpenShift CLI and documentation 4.20
- RHEL 9-compatible Linux x86_64 as the primary client target
- `openshift/openshift-mcp-server` commit
  `a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd`

The skills themselves are text assets and can work on other OpenCode platforms.
Revalidate OpenCode permissions, the MCP binary, and tool names after changing
any pinned component.

## Quick start

### 1. Clone the skills

```bash
git clone https://github.com/msilich/openshift-skill.git
cd openshift-skill
```

OpenCode discovers `.agents/skills/*/SKILL.md` when it is started in this
repository. Keeping the full checkout is recommended because it preserves the
offline documentation, tests, and configuration templates.

For a global installation, copy each complete skill directory—not only its
`SKILL.md`—to an OpenCode global skill location such as
`~/.config/opencode/skills/`. When using the supplied restrictive OpenCode
profiles globally, adapt their file-read permissions to the selected global
path.

### 2. Download and build the OpenShift MCP server

The OpenShift fork did not publish GitHub release binaries at the inspected
baseline. Build the native binary from the pinned source instead of assuming
that an upstream `containers/kubernetes-mcp-server` release contains the same
OpenShift downstream features.

Prerequisites on the connected build host:

- Git
- Go 1.26.3, as declared by the pinned `go.mod`
- GNU Make

```bash
git clone https://github.com/openshift/openshift-mcp-server.git
cd openshift-mcp-server

git checkout --detach a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd
test "$(git rev-parse HEAD)" = "a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd"

make build
./kubernetes-mcp-server --help
```

Install it for the local user or system:

```bash
install -d -m 0755 "$HOME/.local/bin"
install -m 0755 kubernetes-mcp-server "$HOME/.local/bin/kubernetes-mcp-server"
```

For a system installation:

```bash
sudo install -m 0755 kubernetes-mcp-server /usr/local/bin/kubernetes-mcp-server
```

#### Air-gapped transfer

Build on a connected host with the same target OS and architecture, then create
and verify a checksum:

```bash
sha256sum kubernetes-mcp-server > kubernetes-mcp-server.sha256
```

Transfer both files through the approved process. On the disconnected target:

```bash
sha256sum --check kubernetes-mcp-server.sha256
install -d -m 0755 "$HOME/.local/bin"
install -m 0755 kubernetes-mcp-server "$HOME/.local/bin/kubernetes-mcp-server"
```

The build downloads Go modules. In a fully disconnected build environment, use
an approved internal Go module mirror or transfer a binary built and verified
on the connected build host.

### 3. Prepare an explicit kubeconfig

Use a minified, single-context kubeconfig and keep it outside the repository
with mode `0600`. Prefer a dedicated, least-privilege ServiceAccount for the
read profile. Use a separate personal kubeconfig for Day-2 work.

Verify the exact target without printing tokens or full kubeconfig contents:

```bash
oc --kubeconfig /secure/path/read-only.kubeconfig config current-context
oc --kubeconfig /secure/path/read-only.kubeconfig whoami
oc --kubeconfig /secure/path/read-only.kubeconfig whoami --show-server
```

#### Optional cluster-wide read-all/write-none identity

> [!CAUTION]
> This optional profile can read every resource in every namespace, including
> raw Secret values and resources from current or future CRDs. Treat its
> kubeconfig, MCP process, model context, and OpenCode session data as
> privileged. Use it only when this broad access is an explicit requirement.

The bundled `read-all-rbac` manifests grant only `get`, `list`, and `watch` on
all API resources, plus `get` on non-resource URLs. They grant no create,
update, patch, or delete verbs. Install them with an explicit admin kubeconfig:

```bash
export OPENSHIFT_SKILL_DIR=/absolute/path/to/openshift-skill

oc --kubeconfig /secure/path/admin.kubeconfig whoami
oc --kubeconfig /secure/path/admin.kubeconfig whoami --show-server
oc --kubeconfig /secure/path/admin.kubeconfig apply \
  -f "$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/assets/read-all-rbac"
```

On the air-gapped Linux client, create a single-context kubeconfig with the
customer's API CA embedded as `certificate-authority-data`:

```bash
chmod 700 \
  "$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/scripts/new-read-all-kubeconfig.sh" \
  "$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/scripts/update-read-all-token.sh"

"$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/scripts/new-read-all-kubeconfig.sh" \
  --admin-kubeconfig /secure/path/admin.kubeconfig \
  --cluster-ca /secure/path/customer-api-ca.pem \
  --output /secure/path/read-all.kubeconfig
```

The creation script validates the supplied CA against the actual API endpoint,
refuses insecure TLS, embeds the exact CA file, sets mode `0600`, verifies the
ServiceAccount identity, confirms Secret read access, and confirms that create
and delete are denied. It never overwrites an existing target. A PEM bundle may
contain the required root and intermediate CAs; for a truly self-signed API
certificate, that certificate itself can be supplied.

The default requested TokenRequest lifetime is `24h`; the API server can cap
it. Refresh the token without replacing the embedded CA:

```bash
"$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/scripts/update-read-all-token.sh" \
  --admin-kubeconfig /secure/path/admin.kubeconfig \
  --target /secure/path/read-all.kubeconfig
```

The updater verifies a protected temporary copy before atomically replacing the
target. Restart OpenCode or its MCP child after refresh. Do not leave the admin
kubeconfig on the MCP host unless the customer's security design explicitly
requires and protects it.

Equivalent PowerShell scripts are included for preparation or testing on
Windows:

```powershell
& "$env:OPENSHIFT_SKILL_DIR\.agents\skills\openshift-mcp\scripts\New-ReadAllKubeconfig.ps1" `
  -AdminKubeconfig C:\Secure\admin.kubeconfig `
  -ClusterCAPath C:\Secure\customer-api-ca.pem `
  -OutputKubeconfig C:\Secure\read-all.kubeconfig

& "$env:OPENSHIFT_SKILL_DIR\.agents\skills\openshift-mcp\scripts\Update-ReadAllToken.ps1" `
  -AdminKubeconfig C:\Secure\admin.kubeconfig `
  -TargetKubeconfig C:\Secure\read-all.kubeconfig
```

Point `OPENSHIFT_MCP_READ_KUBECONFIG` at the resulting read-all kubeconfig when
starting the existing read-only MCP/OpenCode profile. The MCP process remains
read-only; the broader scope comes from cluster RBAC.

### 4. Configure OpenCode read-only mode

The supplied MCP profiles are self-contained in
`.agents/skills/openshift-mcp/assets/`. They intentionally do not select a
model provider; OpenCode continues to use the provider configured by the user
or organization.

OpenCode merges global, custom, and project configuration. Use a trusted
operations workspace and review the effective configuration before adding
credentials; a later project configuration can override an earlier custom
profile.

```bash
export OPENSHIFT_SKILL_DIR=/absolute/path/to/openshift-skill
export OPENSHIFT_MCP_BINARY=/absolute/path/to/kubernetes-mcp-server
export OPENSHIFT_MCP_READ_CONFIG="$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/assets/openshift-mcp.readonly.toml"
export OPENSHIFT_MCP_READ_KUBECONFIG=/secure/path/read-only.kubeconfig
export OPENCODE_CONFIG="$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/assets/opencode.readonly.jsonc"

cd "$OPENSHIFT_SKILL_DIR"
opencode --pure debug skill
opencode mcp list
opencode
```

Expected skills:

```text
openshift-api
openshift-docs
openshift-mcp
```

Safe first prompts:

```text
Use $openshift-docs to find the OCP 4.20 documentation for Routes.
Use $openshift-api to verify the fields of route.spec.tls from the live cluster.
Use $openshift-mcp to confirm the current cluster identity and list namespaces. Read-only only.
```

### Optional: OpenAI-compatible Qwen

Merge
`.agents/skills/openshift-mcp/assets/opencode.qwen-provider.jsonc` into the
normal OpenCode configuration, replace `REPLACE_WITH_QWEN_MODEL_ID`, and set:

```bash
export QWEN_BASE_URL=https://qwen.example.internal/v1
export QWEN_API_KEY=SET_WITH_YOUR_APPROVED_SECRET_MECHANISM
```

Do not commit the API key. Test the exact model ID and tool-calling template
against a disposable cluster before enabling Day-2 operations.

## Day-2 mode

Day-2 is a separate, privileged session. It enables the complete toolset of the
pinned OpenShift downstream build and asks for every MCP or writing `oc` call.

```bash
export OPENSHIFT_SKILL_DIR=/absolute/path/to/openshift-skill
export OPENSHIFT_MCP_BINARY=/absolute/path/to/kubernetes-mcp-server
export OPENSHIFT_MCP_DAY2_CONFIG="$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/assets/openshift-mcp.day2.toml"
export OPENSHIFT_MCP_DAY2_KUBECONFIG=/secure/path/day2.kubeconfig
export OPENCODE_CONFIG="$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/assets/opencode.day2.jsonc"

cd "$OPENSHIFT_SKILL_DIR"
opencode mcp list
opencode
```

Never start Day-2 with `opencode --auto`. Approve mutations only with `once`.
The workflow requires current-state capture, live schema verification, an
explained delta and impact, dry-run or diff when supported, fresh approval,
one bounded change, and post-change verification.

## Secret handling

Before any Secret access, the MCP skill asks the user to choose one task-scoped
mode:

1. metadata and key names only;
2. placeholder-only commands with values entered outside OpenCode;
3. explicitly approved raw processing after a model-context/session-data
   warning; or
4. abort Secret access.

The optional `openshift-mcp.deny-secrets.toml` drop-in can block Secret
resources technically. It is not enabled automatically.

## Offline OCP 4.20 documentation

The `openshift-docs` skill contains 1,746 converted OCP 4.20 topics and requires
no network access at runtime. Provenance, exact commits, licenses, conversion
details, and the content manifest are recorded in
`.agents/skills/openshift-docs/references/ocp-4.20/SOURCE.json`.

When the bundled documentation and a connected cluster disagree about an API,
the API actually served by the cluster is authoritative.

## Validation

Run the offline test suite:

The test suite requires Python 3.11 or newer. Runtime use of the skills does
not require the test environment.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Optional integration variables enable tests against real local binaries:

```bash
OPENCODE_BIN=/absolute/path/to/opencode \
MCP_SERVER_BIN=/absolute/path/to/kubernetes-mcp-server \
PYTHONDONTWRITEBYTECODE=1 \
python3 -m unittest discover -s tests -v
```

The tests use a fake kubeconfig endpoint and do not modify a live cluster.

## Sources and licensing

This project is licensed under the Apache License 2.0. Third-party source and
documentation notices are recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md),
the generated documentation snapshot, and `sources.lock.json`.

No OpenShift MCP server binary or OpenCode binary is redistributed by this
repository.
