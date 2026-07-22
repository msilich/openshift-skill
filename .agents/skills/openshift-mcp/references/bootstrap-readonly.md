# Bootstrap read-only OpenCode access

Use this workflow when the user asks OpenCode to prepare an explicit read-only
OpenShift kubeconfig and configure the local `ocp_read` MCP entry. Run it only
from a trusted operations workspace. Do not install an MCP package; use the
exact command already available in the DevSpace or customer environment.

Use three separate fresh `once` approvals for cluster RBAC, credential
creation, and the local OpenCode configuration write. Skip the first two when
a verified read-only kubeconfig already exists.

## Contents

1. Collect the inputs
2. Perform a read-only preflight
3. Select or provision the OpenShift identity
4. Create the protected kubeconfig
5. Preview the OpenCode configuration
6. Apply the OpenCode configuration
7. Verify the result
8. Report completion

## 1. Collect the inputs

Obtain and restate these values before running a command:

- absolute skill checkout path;
- either an existing dedicated read-only kubeconfig, or an explicit
  administrative kubeconfig used only for provisioning;
- expected OpenShift API URL and expected selected-kubeconfig identity, plus
  the expected administrative identity only when provisioning;
- readable customer API CA PEM bundle and a new output kubeconfig path when
  provisioning;
- desired authorization scope, including whether raw Secret reads are required;
- existing plain-JSON OpenCode config path;
- exact OpenShift MCP command array already installed in the DevSpace and, for
  `both`, the exact installed Argo CD MCP command array; and
- `openshift` or `both` generator profile. For `both`, require an already
  prepared Argo CD token registry, base URL, and optional route CA.

Never ask the user to paste a bearer token, kubeconfig content, private key, or
Secret value into the conversation. Resolve the task-scoped Secret choice from
`safety.md` before provisioning the broad read-all identity because it includes
raw Secret access. Do not infer consent from an earlier task.

## 2. Perform a read-only preflight

Require Python 3.9 or newer, `oc`, OpenCode, and the already installed MCP
command. Require `npx --no-install` or `npx --offline` when the command uses
`npx`; never let OpenCode fetch a package during startup.

Use only the explicitly named kubeconfig. Verify without printing its content:

```text
oc --kubeconfig <admin-or-existing-read-kubeconfig> config current-context
oc --kubeconfig <admin-or-existing-read-kubeconfig> whoami
oc --kubeconfig <admin-or-existing-read-kubeconfig> whoami --show-server
```

When provisioning, validate the supplied CA against the expected API URL:

```text
oc --kubeconfig <admin-kubeconfig> \
  --server=<expected-api-url> \
  --certificate-authority=<customer-api-ca.pem> \
  --insecure-skip-tls-verify=false \
  --request-timeout=8s get --raw /version
```

Stop on any context, identity, server, CA, file, or scope mismatch. Confirm the
displayed target with the user before the first persistent action. Never run
`oc config view --raw`, `oc login`, or `oc config use-context` in this workflow.

## 3. Select or provision the OpenShift identity

If the user supplied an existing read-only kubeconfig, skip all RBAC and token
creation. Verify its expected identity and server, then check representative
permissions:

```text
oc --kubeconfig <read-kubeconfig> auth can-i get namespaces
oc --kubeconfig <read-kubeconfig> auth can-i list pods --all-namespaces
oc --kubeconfig <read-kubeconfig> auth can-i get secrets --all-namespaces
oc --kubeconfig <read-kubeconfig> auth can-i create deployments.apps --all-namespaces
oc --kubeconfig <read-kubeconfig> auth can-i patch deployments.apps --all-namespaces
oc --kubeconfig <read-kubeconfig> auth can-i delete pods --all-namespaces
```

Require `no` for create, patch, and delete. Require the Secret result to match
the user's selected scope. Stop rather than broadening an existing identity.

When provisioning the bundled read-all/write-none identity, inspect the exact
files under `assets/read-all-rbac/`. Preview them with the same admin
kubeconfig. `oc diff` exit code `1` means a difference was found, not a failed
preview:

```text
oc --kubeconfig <admin-kubeconfig> diff \
  -f <skill-root>/.agents/skills/openshift-mcp/assets/read-all-rbac
oc --kubeconfig <admin-kubeconfig> apply --dry-run=server -o name \
  -f <skill-root>/.agents/skills/openshift-mcp/assets/read-all-rbac
```

Explain the exact four objects, cluster-wide read scope, Secret exposure, and
write prohibition. Request a fresh `once` approval for
**Gate 1: cluster RBAC approval**. Do not combine it with credential creation. After approval, apply
only that directory with the explicit admin kubeconfig, then verify the
ServiceAccount through impersonation:

```text
oc --kubeconfig <admin-kubeconfig> apply \
  -f <skill-root>/.agents/skills/openshift-mcp/assets/read-all-rbac
oc --kubeconfig <admin-kubeconfig> auth can-i get secrets --all-namespaces \
  --as=system:serviceaccount:openshift-mcp:opencode-admin-readonly
oc --kubeconfig <admin-kubeconfig> auth can-i create deployments.apps --all-namespaces \
  --as=system:serviceaccount:openshift-mcp:opencode-admin-readonly
oc --kubeconfig <admin-kubeconfig> auth can-i patch deployments.apps --all-namespaces \
  --as=system:serviceaccount:openshift-mcp:opencode-admin-readonly
oc --kubeconfig <admin-kubeconfig> auth can-i delete pods --all-namespaces \
  --as=system:serviceaccount:openshift-mcp:opencode-admin-readonly
```

Require `yes`, `no`, `no`, and `no` in that order.

## 4. Create the protected kubeconfig

Skip this section for an existing read-only kubeconfig. Refuse to overwrite an
existing output path. Explain that the next script requests a short-lived
ServiceAccount token, embeds the named CA, writes mode `0600`, and does not
print the token. Request a fresh `once` approval for
**Gate 2: credential creation approval**. Do not reuse Gate 1.

After approval, run exactly:

```text
<skill-root>/.agents/skills/openshift-mcp/scripts/new-read-all-kubeconfig.sh \
  --admin-kubeconfig <admin-kubeconfig> \
  --cluster-ca <customer-api-ca.pem> \
  --output <new-read-kubeconfig>
```

Do not enable shell tracing. Do not capture, print, decode, or return the token.
Use only the script's non-sensitive summary. Re-run the context, identity,
server, TLS, and representative permission checks against the new kubeconfig.

## 5. Preview the OpenCode configuration

Require an absolute plain-JSON OpenCode config path. Do not print the complete
existing config because it can contain provider credentials. Build the exact
command arrays without tokens. For a DevSpace `npx` command, use a reviewed
array like this, replacing the package command and path placeholders. Prefer
absolute non-secret paths here so no shell profile needs modification:

```json
["npx","--no-install","<openshift-mcp-command>","--config","<skill-root>/.agents/skills/openshift-mcp/assets/openshift-mcp.readonly.toml","--kubeconfig","<absolute-read-kubeconfig>","--cluster-provider","disabled"]
```

Run the Python 3.9 generator without `--apply`:

```text
python3 <skill-root>/.agents/skills/openshift-mcp/scripts/generate-opencode-mcp-config.py \
  --config <opencode.json> \
  --profile openshift \
  --openshift-command-json '<reviewed-json-array>'
```

For `both`, change the profile and add the separately reviewed
`--argocd-command-json` array plus `--include-argocd-ca` when the customer route
requires its private CA. Do not continue unless the Argo CD token registry and
environment values were already prepared through the approved customer
mechanism.

Show the generator's selected-entry preview. If it reports a conflicting name
or equivalent command, stop. Use `--replace` only after showing the conflict
and receiving explicit direction; never silently create a second OpenShift MCP
identity.

## 6. Apply the OpenCode configuration

Request a fresh `once` approval for **Gate 3: configuration write approval**.
Do not reuse either cluster approval. After approval, repeat the exact reviewed
generator command with `--apply`. The generator preserves unrelated JSON,
writes atomically, and creates a timestamped backup when the config exists.

Validate JSON without displaying it:

```text
python3 -m json.tool <opencode.json> >/dev/null
```

Repeat the generator preview with the same arguments and require `unchanged`.
Never add a raw token or password to the OpenCode configuration.

## 7. Verify the result

When the reviewed OpenShift command deliberately uses environment references,
set `OPENSHIFT_MCP_READ_CONFIG` and `OPENSHIFT_MCP_READ_KUBECONFIG` through the
approved DevSpace mechanism before restart. No OpenShift environment change is
needed when the command contains the reviewed absolute paths. For optional Argo
CD, the environment includes
`ARGOCD_BASE_URL`, `ARGOCD_TOKEN_REGISTRY_PATH`, and, when required,
`NODE_EXTRA_CA_CERTS`; never set `NODE_TLS_REJECT_UNAUTHORIZED=0`.

OpenCode must start a new process to load changed MCP configuration and Node CA
variables. Do not claim that the current process reloaded them. Ask the user to
restart OpenCode, then run `opencode mcp list` and require exactly one intended
`ocp_read` entry plus any explicitly selected `argocd_read` entry. Perform one
harmless namespace or project list and re-check the exact kubeconfig identity
and server.

If verification fails, stop and report evidence. Offer the timestamped OpenCode
backup as the local rollback. Do not remove cluster RBAC or revoke credentials
without a new, explicit request and approval.

## 8. Report completion

Report the verified API URL, ServiceAccount identity, kubeconfig path,
customer-CA validation, effective read/write checks, OpenCode config path,
configured MCP names, backup path, and restart status. Never include tokens,
Secret values, full kubeconfig content, or provider credentials.

## Stop conditions

Stop without mutation on a target or CA mismatch, unresolved Secret scope,
missing dependency, existing output kubeconfig, JSONC input, unreviewed config
replacement, `npx` without offline protection, any effective write permission,
or a failed dry-run. Preserve all existing customer files and report the exact
blocking check.
