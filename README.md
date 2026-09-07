# OpenShift Agent Skills for OpenCode

Nine portable, English-language agent skills for operating and researching
OpenShift with [OpenCode](https://opencode.ai/):

- `openshift-mcp` — MCP-first diagnosis and controlled Day-2 operations with
  `oc` as a fallback.
- `openshift-api` — live API discovery with `oc api-resources`, `oc explain`,
  OpenAPI v3, and CRD schemas.
- `openshift-docs` — a complete, searchable, offline OpenShift Container
  Platform 4.22, OpenShift GitOps 1.21 and Dev Spaces 3.29 documentation snapshots.
- `openshift-troubleshooting` — evidence-led workload, service, storage, node and Operator diagnosis.
- `openshift-disconnected` — oc-mirror v2, internal registries, transfer workflows and image-pull diagnosis.
- `openshift-gitops` — Application/ApplicationSet reconciliation, access, trust and reviewed configuration changes.
- `openshift-upgrade` — update readiness, supported paths, disruption constraints and completion checks.
- `openshift-backup-restore` — OADP coverage and documented application/control-plane recovery.
- `openshift-devspaces` — CheCluster administration, workspaces, devfiles, airgap dependencies and startup/IDE diagnosis.

The skills are model-provider independent. An optional OpenAI-compatible Qwen
provider example is included for local and air-gapped deployments.

This `v4.22` branch bundles the OpenShift Container Platform 4.22 documentation.
The `main` branch retains the 4.20 snapshot.

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
| `.agents/skills/openshift-mcp/assets/argocd-readonly-rbac/` | Optional additive Argo CD account and read-only RBAC patches |
| `.agents/skills/openshift-mcp/scripts/` | CA-aware OpenShift and Argo CD/OpenCode bootstrap scripts |
| `.agents/skills/openshift-api/` | Live API/schema discovery skill and helper |
| `.agents/skills/openshift-docs/` | Offline OCP 4.22, GitOps 1.21 and Dev Spaces 3.29 documentation skill |
| `.agents/skills/openshift-{troubleshooting,disconnected,gitops,upgrade,backup-restore,devspaces}/` | Documentation-based operational workflows |
| `manifests/openshift-gitops-argocd-mcp-readonly/` | Simple reviewed merge-patch YAMLs for an unchanged default OpenShift GitOps instance |
| `sources.lock.json` | Exact source and compatibility baselines |
| `tools/docs/` | Reproducible documentation conversion inputs |
| `tests/` | Offline integrity and behavior checks |

## Tested baseline

- OpenCode 1.18.4
- OpenShift CLI 4.20 (existing runtime baseline); bundled documentation 4.22
- Optional OpenShift GitOps 1.21.1 / Argo CD 3.4.4 integration, validated with
  Argo CD CLI 3.4.5
- RHEL 9-compatible Linux x86_64 as the primary client target
- `openshift/openshift-mcp-server` commit
  `a0a1c370fcce18f76cecdbb2e07d8f4dbafe92dd`
- Optional `argoproj-labs/mcp-for-argocd` commit
  `1bb80b2816f0c8810efedc2fdcf318fd18ce214d`

The skills themselves are text assets and can work on other OpenCode platforms.
Revalidate OpenCode permissions, the MCP binary, and tool names after changing
any pinned component.

The documentation update does not establish live-cluster compatibility with
OCP 4.22. Use the matching `oc` client and validate the existing MCP profiles
against your target cluster before Day-2 use.

## Quick start

### 1. Clone the skills

```bash
git clone --branch v4.22 --single-branch https://github.com/msilich/openshift-skill.git
cd openshift-skill
```

OpenCode discovers `.agents/skills/*/SKILL.md` when it is started in this
repository. Keeping the full checkout is recommended because it preserves the
offline documentation, tests, and configuration templates.

Install all nine complete skill directories as siblings. Domain skills depend
on the shared MCP, API and documentation skills and their relative paths.

For a user-wide installation, run the bundled installer as the user who runs
OpenCode, **without sudo**:

```bash
bash install-skills.sh --dry-run
bash install-skills.sh
```

It copies all nine complete directories, including offline documentation, to
`$HOME/.config/opencode/skills/`, the global location documented by
[OpenCode](https://opencode.ai/docs/skills/#place-files). The source is resolved
relative to the script, so an absolute script path works from any working directory.
The documentation version comes from the current checkout; no download is needed.

Existing skill directories cause a preflight error. To update after reviewing
the source version, use `bash install-skills.sh --replace`. Original directories
are retained at the printed backup path outside OpenCode's skill-discovery tree;
unrelated skills are untouched. Keep OpenCode closed during replacement. Restore
a backup by moving the corresponding new directory aside and moving its original
from the printed `previous/` directory back into `skills/`.

For a customized installation, use `--target-dir /absolute/path/to/skills`.
A non-default `XDG_CONFIG_HOME` requires this explicit selection; match the path
to your OpenCode deployment. No model, MCP or permission configuration is changed.
When using the supplied restrictive profiles globally, adapt their file-read
permissions to the selected path. Restart OpenCode and check discovery from a
directory outside this repository to avoid duplicate project/global skill names.

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

OpenCode can guide and execute steps 3 and 4 when invoked with
`$openshift-mcp`. The skill loads
[bootstrap-readonly.md](.agents/skills/openshift-mcp/references/bootstrap-readonly.md),
previews every persistent delta, and pauses for separate approvals before
cluster RBAC, credential creation, and the local OpenCode config write.

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
update, patch, or delete verbs. Use the deterministic Linux or Windows
bootstrap with an explicit admin kubeconfig, expected identity, and expected
API URL. The scripts never modify the admin kubeconfig and never accept a
login token. Run `oc login` separately before this workflow.

```bash
export OPENSHIFT_SKILL_DIR=/absolute/path/to/openshift-skill
export OPENSHIFT_MCP_SKILL="$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp"

chmod 700 \
  "$OPENSHIFT_MCP_SKILL/scripts/bootstrap-read-all.sh" \
  "$OPENSHIFT_MCP_SKILL/scripts/new-read-all-kubeconfig.sh" \
  "$OPENSHIFT_MCP_SKILL/scripts/update-read-all-token.sh"

"$OPENSHIFT_MCP_SKILL/scripts/bootstrap-read-all.sh" preview \
  --admin-kubeconfig /secure/path/admin.kubeconfig \
  --expected-server https://api.example.test:6443 \
  --expected-admin-identity customer-admin \
  --output /secure/path/read-all.kubeconfig
```

The preview performs `oc diff` and a server-side dry-run without persistent
changes. After a separate RBAC approval, repeat the exact arguments with
`apply-rbac`. After a separate credential approval, repeat them with
`create-kubeconfig`:

```bash
"$OPENSHIFT_MCP_SKILL/scripts/bootstrap-read-all.sh" apply-rbac \
  --admin-kubeconfig /secure/path/admin.kubeconfig \
  --expected-server https://api.example.test:6443 \
  --expected-admin-identity customer-admin \
  --output /secure/path/read-all.kubeconfig

"$OPENSHIFT_MCP_SKILL/scripts/bootstrap-read-all.sh" create-kubeconfig \
  --admin-kubeconfig /secure/path/admin.kubeconfig \
  --expected-server https://api.example.test:6443 \
  --expected-admin-identity customer-admin \
  --output /secure/path/read-all.kubeconfig
```

The bootstrap applies the Namespace, ServiceAccount, ClusterRole, and
ClusterRoleBinding before requesting a TokenRequest credential. By default it
copies the flattened CA field from the already authenticated admin kubeconfig.
Use `--cluster-ca /secure/path/customer-api-ca.pem` in every phase to provide
an explicit CA bundle instead. It validates the selected CA against the
expected API endpoint, refuses insecure TLS, embeds that CA, sets mode `0600`,
verifies the ServiceAccount
identity, confirms cluster-wide reads including Secrets, and confirms that
create, patch, and delete are denied. It never overwrites an existing target.
A PEM bundle may contain the required root and intermediate CAs; for a truly
self-signed API certificate, that certificate itself can be supplied.

The default requested TokenRequest lifetime is `24h`; the API server can cap
it. Refresh the token without replacing the embedded CA:

```bash
"$OPENSHIFT_MCP_SKILL/scripts/update-read-all-token.sh" \
  --admin-kubeconfig /secure/path/admin.kubeconfig \
  --target /secure/path/read-all.kubeconfig
```

The updater verifies a protected temporary copy before atomically replacing the
target. Restart OpenCode or its MCP child after refresh. Do not leave the admin
kubeconfig on the MCP host unless the customer's security design explicitly
requires and protects it.

The deterministic three-phase workflow is also available on Windows. Run the
commands separately so the two approvals and their changes remain explicit:

```powershell
$McpSkill = Join-Path $env:OPENSHIFT_SKILL_DIR ".agents\skills\openshift-mcp"
$BootstrapArgs = @{
  AdminKubeconfig      = "C:\Secure\admin.kubeconfig"
  ExpectedServer       = "https://api.example.test:6443"
  ExpectedAdminIdentity = "customer-admin"
  OutputKubeconfig     = "C:\Secure\read-all.kubeconfig"
}

& "$McpSkill\scripts\Bootstrap-ReadAll.ps1" Preview @BootstrapArgs
& "$McpSkill\scripts\Bootstrap-ReadAll.ps1" ApplyRbac @BootstrapArgs
& "$McpSkill\scripts\Bootstrap-ReadAll.ps1" CreateKubeconfig @BootstrapArgs

& "$McpSkill\scripts\Update-ReadAllToken.ps1" `
  -AdminKubeconfig C:\Secure\admin.kubeconfig `
  -TargetKubeconfig C:\Secure\read-all.kubeconfig
```

By default, the Windows bootstrap copies only the flattened embedded CA from
the authenticated admin kubeconfig. Add `ClusterCAPath =
"C:\Secure\customer-api-ca.pem"` to `$BootstrapArgs` to select an explicit CA
bundle. The output is created through a protected temporary file and moved
into place only after identity, server, TLS, and permission verification.

Point `OPENSHIFT_MCP_READ_KUBECONFIG` at the resulting read-all kubeconfig when
starting the existing read-only MCP/OpenCode profile. The MCP process remains
read-only; the broader scope comes from cluster RBAC.

### 4. Configure OpenCode read-only mode

The supplied MCP profiles are self-contained in
`.agents/skills/openshift-mcp/assets/`. They intentionally do not select a
model provider; OpenCode continues to use the provider configured by the user
or organization.

To merge only the MCP entries into an existing plain-JSON OpenCode config, use
the dependency-free Python 3.9 generator. It installs no package, has no token option,
preserves unrelated configuration, rejects credential arguments and duplicate
commands, and previews by default. Do not place secrets in a command array. Its
built-in commands use the environment-based entry points shown
below. For MCP packages already present in a DevSpace, pass the exact `npx`
commands as JSON arrays and include `--no-install` or `--offline` so OpenCode
cannot fetch from a registry at startup:

```bash
python3 .agents/skills/openshift-mcp/scripts/generate-opencode-mcp-config.py \
  --config "$HOME/.config/opencode/opencode.json" \
  --profile both \
  --openshift-command-json '["npx","--no-install","<openshift-mcp-command>","--config","{env:OPENSHIFT_MCP_READ_CONFIG}","--kubeconfig","{env:OPENSHIFT_MCP_READ_KUBECONFIG}","--cluster-provider","disabled"]' \
  --argocd-command-json '["npx","--no-install","<argocd-mcp-command>","stdio"]' \
  --include-argocd-ca
```

Review the proposed `ocp_read` and `argocd_read` entries, then repeat the same
command with `--apply`. The generator writes atomically, creates a timestamped
backup of an existing config, and is idempotent. It refuses JSONC input rather
than removing comments. Set `ARGOCD_BASE_URL`, `ARGOCD_TOKEN_REGISTRY_PATH`,
and, when requested, `NODE_EXTRA_CA_CERTS` in the DevSpace or shell environment;
their values are not copied into the generated config. Restart OpenCode and run
`opencode mcp list` after applying.

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
openshift-troubleshooting
openshift-disconnected
openshift-gitops
openshift-upgrade
openshift-backup-restore
openshift-devspaces
```

Safe first prompts:

```text
Use $openshift-docs to find the OCP 4.22 documentation for Routes.
Use $openshift-api to verify the fields of route.spec.tls from the live cluster.
Use $openshift-mcp to confirm the current cluster identity and list namespaces. Read-only only.
```

Domain examples (diagnosis alone never authorizes a repair):

```text
Use $openshift-troubleshooting to diagnose Pending pods in namespace payments.
Use $openshift-disconnected to investigate an ImagePullBackOff against our internal mirror.
Use $openshift-gitops to explain why Application shop is OutOfSync after a successful sync.
Use $openshift-upgrade to assess readiness for the target release, including PDBs and mirror content.
Use $openshift-backup-restore to check whether backup orders includes its persistent data.
Use $openshift-devspaces to diagnose why workspace team-a/api is Pending without changing resources.
```

The read-only profile adds only the non-mutating `oc adm upgrade` report and
`oc-mirror --help`. The Day-2 profile also asks for each `oc-mirror --v2 ...`
invocation. Mirror import is a write and must target the explicitly selected
internal registry. Argo CD MCP remains read-only in every supplied profile.

### Optional: Argo CD MCP in read-only mode

This adds a second local MCP server named `argocd_read`. It is independent of
`ocp_read`: the OpenShift server uses its kubeconfig identity, while the Argo CD
server uses a dedicated Argo CD API token. The combined profile uses two layers
of write protection:

1. `MCP_READ_ONLY=true` prevents the Argo CD MCP server from registering its
   create, update, delete, sync, and resource-action tools.
2. The dedicated `opencode-mcp` Argo CD account allows application, project,
   cluster, and workload-log reads and explicitly denies known mutation actions.

The bootstrap expects an installed MCP entry point. On a connected Windows or
Linux workstation, create it from the pinned source:

```bash
git clone https://github.com/argoproj-labs/mcp-for-argocd.git
cd mcp-for-argocd
git checkout --detach 1bb80b2816f0c8810efedc2fdcf318fd18ce214d
test "$(git rev-parse HEAD)" = "1bb80b2816f0c8810efedc2fdcf318fd18ce214d"
corepack pnpm install --frozen-lockfile
corepack pnpm test
corepack pnpm build
corepack pnpm --filter argocd-mcp --legacy deploy --prod "$HOME/.local/share/argocd-mcp"
```

On PowerShell, replace the `test` line with
`if ((git rev-parse HEAD) -ne "1bb80b2816f0c8810efedc2fdcf318fd18ce214d") { throw "revision mismatch" }`.

Review the customer's `policy.default` first. It must not grant write access to
all authenticated users because Argo CD default-policy permissions cannot be
removed by a subject-specific deny rule.

#### Operator-managed OpenShift GitOps

For Red Hat OpenShift GitOps, configure the `ArgoCD` custom resource. Do not
patch `argocd-cm` or `argocd-rbac-cm` directly: they are generated objects and
the Operator can immediately reconcile such changes away.

For an unchanged default instance with no additional local users or custom
policy lines, the small YAML merge patches and exact preview/apply commands in
`manifests/openshift-gitops-argocd-mcp-readonly/` provide the most transparent
customer workflow. Because the CRD treats `localUsers` as a complete list and
`rbac.policy` as one string, those static patches must not be used when custom
entries already exist; use the preserving bootstrap below in that case.

The cross-platform bootstrap requires `oc`, `argocd`, and Node.js. It:

- verifies the exact kubeconfig identity and API server;
- verifies the live `argoproj.io/v1beta1` CRD schema;
- preserves unrelated local users and RBAC rules;
- performs a server dry-run before any persistent change;
- creates an API-only `opencode-mcp` user with a renewable seven-day token;
- reads only `opencode-mcp-local-user.data.apiToken`, without printing it;
- verifies `get=Yes`, `sync=No`, and `delete=No` with the Argo CD CLI;
- tests the Argo CD read API, writes a protected token registry, and updates an
  existing plain-JSON OpenCode configuration with `argocd_read`.

Run it once without `--apply` and review the displayed target and delta:

```bash
export OPENSHIFT_SKILL_DIR=/absolute/path/to/openshift-skill

node "$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/scripts/configure-argocd-mcp-opencode.mjs" \
  --kubeconfig /secure/path/admin.kubeconfig \
  --expected-server https://api.customer.example:6443 \
  --expected-identity kube:admin \
  --namespace openshift-gitops \
  --argocd-name openshift-gitops \
  --base-url https://openshift-gitops-server-openshift-gitops.apps.customer.example \
  --opencode-config "$HOME/.config/opencode/opencode.json" \
  --mcp-entrypoint /opt/argocd-mcp/dist/index.js \
  --registry "$HOME/.config/opencode/secrets/argocd-token-registry.json" \
  --ca /secure/path/customer-argocd-ca.pem \
  --token-lifetime 168h
```

After explicit review and approval, repeat the same command with `--apply`.
The raw-token approval applies only to the named local-user Secret and this
bootstrap run. The script never reads another Secret. Restart OpenCode after a
successful run:

```bash
node "$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/scripts/configure-argocd-mcp-opencode.mjs" \
  --kubeconfig /secure/path/admin.kubeconfig \
  --expected-server https://api.customer.example:6443 \
  --expected-identity kube:admin \
  --namespace openshift-gitops \
  --argocd-name openshift-gitops \
  --base-url https://openshift-gitops-server-openshift-gitops.apps.customer.example \
  --opencode-config "$HOME/.config/opencode/opencode.json" \
  --mcp-entrypoint /opt/argocd-mcp/dist/index.js \
  --registry "$HOME/.config/opencode/secrets/argocd-token-registry.json" \
  --ca /secure/path/customer-argocd-ca.pem \
  --token-lifetime 168h \
  --apply

opencode mcp list
```

On Windows, use the same Node.js script with PowerShell paths:

```powershell
node "$env:OPENSHIFT_SKILL_DIR\.agents\skills\openshift-mcp\scripts\configure-argocd-mcp-opencode.mjs" `
  --kubeconfig "$HOME\.kube\config" `
  --expected-server https://api.customer.example:6443 `
  --expected-identity kube:admin `
  --namespace openshift-gitops `
  --argocd-name openshift-gitops `
  --base-url https://openshift-gitops-server-openshift-gitops.apps.customer.example `
  --opencode-config "$HOME\.config\opencode\opencode.json" `
  --mcp-entrypoint "$HOME\.local\share\argocd-mcp\dist\index.js" `
  --registry "$HOME\.config\opencode\secrets\argocd-token-registry.json" `
  --ca C:\Secure\customer-argocd-ca.pem `
  --token-lifetime 168h `
  --apply
```

Omit `--ca` only when the Argo CD route is already trusted by the operating
system. Rerun the script to copy an automatically renewed Operator token into
the local registry, then restart OpenCode. The script creates a one-time
`opencode.json.backup-before-argocd-mcp` backup and refuses commented JSONC to
avoid silently destroying comments; use the combined profile for JSONC setups.

The JSON merge patches in `assets/argocd-readonly-rbac/` are retained only for
plain, non-operator-managed upstream Argo CD installations. They must not be
applied to ConfigMaps owned by the OpenShift GitOps Operator.

#### Build and transfer for an air-gapped Linux client

Run the pinned builder on a connected Linux host with the same CPU architecture
as the customer system. It requires Git, Node.js 18 or newer, Corepack, tar, and
sha256sum; Node.js 22 or 24 LTS is recommended. The script installs from the
pinned lockfile, runs all upstream tests, builds the server, and packages its
production dependencies:

```bash
chmod 700 "$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/scripts/build-argocd-mcp-airgap-bundle.sh"

"$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/scripts/build-argocd-mcp-airgap-bundle.sh" \
  --output-dir /secure/transfer
```

Transfer the generated `.tar.gz` and `.sha256` files through the approved
process. On the customer Linux system:

```bash
cd /secure/transfer
sha256sum --check argocd-mcp-*.tar.gz.sha256
sudo install -d -m 0755 /opt/argocd-mcp
sudo tar -xzf argocd-mcp-*.tar.gz --strip-components=1 -C /opt/argocd-mcp
```

Node.js itself must also be available from the customer's approved RHEL package
source or be transferred as a separately approved runtime artifact. Transfer a
compatible Argo CD CLI as a separately checksummed artifact as well; the
bootstrap uses it to validate the effective live RBAC policy.

#### Manual token registry for non-operator Argo CD

For a plain upstream Argo CD installation where an administrator generated the
token separately, create a protected registry without exposing that token as a
process argument. The helper verifies the TLS endpoint with the supplied
customer CA and never disables certificate verification:

```bash
chmod 700 "$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/scripts/new-argocd-token-registry.sh"

"$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/scripts/new-argocd-token-registry.sh" \
  --base-url https://argocd.apps.customer.example \
  --token-file /secure/path/opencode-mcp.token \
  --cluster-ca /secure/path/customer-argocd-ca.pem \
  --output /secure/path/argocd-token-registry.json
```

The API CA and Argo CD route CA can be different; use the CA that validates the
actual Argo CD URL. A PEM bundle may include a private root and intermediates.
Do not use `NODE_TLS_REJECT_UNAUTHORIZED=0`.

As an alternative to updating an existing plain-JSON config with the bootstrap,
start OpenCode with the combined profile and environment variables:

```bash
export ARGOCD_MCP_NODE=/usr/bin/node
export ARGOCD_MCP_ENTRYPOINT=/opt/argocd-mcp/dist/index.js
export ARGOCD_BASE_URL=https://argocd.apps.customer.example
export ARGOCD_TOKEN_REGISTRY_PATH=/secure/path/argocd-token-registry.json
export MCP_READ_ONLY=true
export NODE_EXTRA_CA_CERTS=/secure/path/customer-argocd-ca.pem
export OPENCODE_CONFIG="$OPENSHIFT_SKILL_DIR/.agents/skills/openshift-mcp/assets/opencode.readonly-with-argocd.jsonc"

cd "$OPENSHIFT_SKILL_DIR"
opencode mcp list
opencode
```

`NODE_EXTRA_CA_CERTS` is loaded when the Node.js process starts, so restart
OpenCode after changing the CA file. `opencode mcp list` should show at least
`ocp_read` and `argocd_read`. OpenCode merges global, custom, and project
configuration, so additional names indicate MCP entries from another layer.

Argo CD application manifests, resource trees, events, and workload logs can
contain sensitive or attacker-controlled data. Apply the same Secret and
untrusted-output rules used for OpenShift inspection.

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

## Offline OCP 4.22 documentation

The `openshift-docs` skill contains 1,797 converted OCP 4.22 topics and requires
no network access at runtime. Provenance, exact commits, licenses, conversion
details, and the content manifest are recorded in
`.agents/skills/openshift-docs/references/ocp-4.22/SOURCE.json`.

The snapshot is pinned to `openshift/openshift-docs` branch `enterprise-4.22`,
commit `d8cc5bae880cc93ecd22fecd660c1b3a7f1358ff` (September 7, 2026).
The converter includes a small local correction: this source revision's distro
map lacks a 4.22 entry, so the product version is derived from the explicit
`enterprise-4.22` branch instead of silently using the upstream 4.17 fallback.

To rebuild on a connected preparation host with Python 3.12+, PyYAML 6.0.3,
Asciidoctor 2.0.23, and Pandoc 3.7.0.2 installed:

```bash
git clone --branch enterprise-4.22 --single-branch https://github.com/openshift/openshift-docs.git /path/to/openshift-docs
git -C /path/to/openshift-docs checkout --detach d8cc5bae880cc93ecd22fecd660c1b3a7f1358ff
python3 tools/docs/build.py \
  --source-dir /path/to/openshift-docs \
  --output-dir .agents/skills/openshift-docs/references/ocp-4.22
```

The build checks the source revision, converter checksum, topic count, and
complete Markdown content manifest against `tools/docs/build.lock.json`.

## Offline GitOps documentation and procedure sources

Both OCP branches additionally bundle all 56 GitOps 1.21 topics (58 Markdown files)
from `openshift/openshift-docs` at `ca5db8539a097b38e2975980963e0959782d105f`.
GitOps 1.21 is a separate product baseline, not inferred from the OCP version.
Use `search_docs.py "repo server" --product gitops`; the default search remains OCP.
The product's `SOURCE.json`, licenses and navigation files are under the
documentation skill's `references/gitops-1.21/` directory.

Rebuild with the same pinned build dependencies and a clean checkout of that commit:

```bash
python3 tools/docs/build.py --lock tools/docs/gitops.lock.json \
  --source-dir /path/to/gitops-docs \
  --output-dir .agents/skills/openshift-docs/references/gitops-1.21
```

Each domain skill's `references/sources.md` maps its procedures to local chapters,
sections and source revisions. Diagnostic/readiness reasoning also adapts two
`openshift/agentic-skills` workflows at `7aca4bee317cd70a4204795db6b1d7b9eb78f48c`.
MCP mappings and OpenCode permission handling are project adaptations. No upstream
token helpers, online lifecycle/Jira calls or automatic privilege escalation are imported.

When the bundled documentation and a connected cluster disagree about an API,
the API actually served by the cluster is authoritative.

## Offline Dev Spaces 3.29

Both OCP branches include the same official Dev Spaces 3.29 HTML snapshot: all 302
table-of-contents topics and 46 illustrations. Use `$openshift-devspaces` for platform
and workspace operations, or search the documentation without accessing a cluster:

```bash
python3 .agents/skills/openshift-docs/scripts/search_docs.py 'CheCluster' --product devspaces
```

The source is the [official Red Hat portal](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29),
not upstream Eclipse Che or an assumed public product Git branch. The versioned
source archive and [build lock](tools/docs/devspaces.lock.json) preserve the original
document HTML fragments, illustrations, response hashes and retrieval dates.
Website scripts/navigation are excluded. External product/support links and the
duplicate PDF rendition are not bundled. Missing source fragments are mapped to
the local topic; every such adjustment is recorded in the snapshot's `SOURCE.json`.
Bundling this documentation does not certify an installed product combination.

To rebuild the pinned snapshot, install Python 3.9+, Pandoc 3.7.0.2 and the packages
in [requirements-devspaces.lock.txt](tools/docs/requirements-devspaces.lock.txt) on
the preparation host. The build itself needs no network and refuses an existing
output directory:

```bash
python3 tools/docs/import_devspaces.py build --output-dir /path/to/new-devspaces-docs
```

Only maintainers refreshing the source use the connected fetch operation. Use a
fresh cache for a fresh retrieval; the cache resumes interrupted downloads:

```bash
python3 tools/docs/import_devspaces.py fetch \
  --cache-dir /path/to/new-response-cache --archive /path/to/new-devspaces-source.zip
```

A new archive requires explicit review and a new lock checksum; it cannot silently
replace the pinned input. Build and compare two outputs before publishing an update.
Raw response caches are preparation artifacts and are not installed. The installed
skills need neither Pandoc nor the importer dependencies and perform no downloads.

Dev Spaces documentation and the new skill's adapted text use CC BY-SA 3.0, unlike
the Apache-licensed OCP/GitOps snapshots. The complete legal notice, license and
per-topic source URLs are retained; see [third-party notices](THIRD_PARTY_NOTICES.md).

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

See [domain skill evaluation](tests/DOMAIN_EVALUATION.md) for fake MCP/oc scenarios
and optional actual OpenCode/model evaluation. Fixture and integrity checks do
not establish that a model follows the skills. Report missing runtime tests explicitly.

## Sources and licensing

This project is licensed under the Apache License 2.0. Third-party source and
documentation notices are recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md),
the generated documentation snapshot, and `sources.lock.json`.

No OpenShift MCP server binary or OpenCode binary is redistributed by this
repository.
