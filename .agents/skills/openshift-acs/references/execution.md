# Execution and approval contract

This is project-authored integration guidance. Read the unchanged
[Secret choice and approval policy](../../openshift-mcp/references/safety.md)
and [OpenShift Day-2 workflow](../../openshift-mcp/references/operations.md).

## Separate the two control planes

Record Central's configured TLS endpoint and trusted CA, the ACS cluster ID and
the OpenShift API endpoint/context from a single-context kubeconfig. Match the
registration using approved inventory and Sensor/operator metadata. Duplicate
names, another Central's ID, or an ambiguous match stop cross-plane operations.
Kubernetes RBAC and RHACS permission sets/access scopes are independent. A token
that can read clusters does not necessarily read deployments, nodes or policies.

Inspect offered tools and their input/output schemas. OpenShift MCP handles
Kubernetes resources, with the same explicit-identity `oc` fallback when a tool
is missing. StackRox MCP handles only the reads in [its setup guide](stackrox-mcp.md).
For missing Central functions select a method from the local RHACS REST or roxctl
reference. `oc explain` cannot validate Central REST objects. Forbidden means
stop, not fallback, alternate identity, broader role or retry. A transient read
may be retried at most once in total, including server retries.

## Central schema and mutations

Read the appropriate service in the [API map](../../openshift-docs/references/acs-4.11/AGENTS.md)
and linked [Common object reference](../../openshift-docs/references/acs-4.11/rest_api/CommonObjectReference/CommonObjectReference.md).
Check Central's observed version and, when provided through an approved endpoint,
its offered API description. Do not guess a Swagger URL or import schemas from
the internet. An undocumented or mismatched field remains unknown.

For every explicitly requested mutation:

1. Read current state, object ID, ownership and the desired outcome. For managed
   objects identify the Operator CR, Git repository or declarative configuration.
2. Verify the method, request model and installed version. Read prerequisites and
   RHACS permissions separately from Kubernetes schema/RBAC.
3. Show a reviewed payload/manifest diff, affected scope, risk and rollback.
   Use a supported preview; state clearly when no server preview exists. A local
   diff is not a server validation. Treat job-creating dry runs/scans as writes.
4. Obtain a fresh OpenCode `once` approval for that exact command and payload.
   Approval for a preview is not approval for the final write. No `--auto`, `always`
   or automatic switch from the read-only profile.
5. Execute once. After a timeout or unclear response, read current state before
   deciding whether any retry is safe; obtain fresh approval for another write.
6. Read back the object and verify the original symptom, controller reconciliation
   and relevant health/enforcement/application behavior. A 2xx is submission
   evidence, not proof of completion. Report unverified checks.

Policy disablement, enforcement changes, exceptions, deletes, rights, integrations,
certificates and restoration are high-risk. Preserve a recoverable prior state
using approved protected storage; do not expose credentials in a rollback file.

## Narrow HTTP/CLI examples

The optional profiles permit a deliberately small **Policy Service** example,
not arbitrary Central API access. Other procedures remain documented but require
reviewed, endpoint-specific permission entries before execution. Never work around
a deny with shell wrappers, pod exec, redirects or another binary.

Configure these values outside the model session:

- `ACS_CENTRAL_HOST`: exact `hostname:port`, no scheme, path or shell syntax.
- `ACS_CA_FILE`: absolute PEM CA path; TLS verification remains on.
- `ACS_READ_HEADER_FILE` / `ACS_DAY2_HEADER_FILE`: separate protected files containing
  the Authorization header, prepared by the user outside OpenCode. No token values
  in commands, examples, model text or logs. The read identity must have no writes.
- `ACS_POLICY_ID`: one verified policy ID, no wildcard or path separator.
- `ACS_POLICY_BODY_FILE`: absolute path to the reviewed request body; not a credential file.
- `ACS_DRYRUN_BODY_FILE`: separately reviewed DryRunPolicy request body.
- `ACS_ROXCTL_BINARY`: absolute path to a trusted, version-matched CLI.

Example command shape (substitute nonsecret paths/IDs from the reviewed configuration):

```bash
curl -q --silent --show-error --fail-with-body --proto =https --max-redirs 0 --connect-timeout 10 --max-time 60 --write-out %{http_code} --cacert /configured/central-ca.pem --header @/protected/acs-read.header --request GET --url https://central.example.invalid:443/v1/policies/verified-policy-id
```

`-q` must be first to ignore curlrc. Do not use `-L`, `--location`, `--location-trusted`,
`-k`, `--insecure`, proxy overrides, `--retry`, extra URLs or commands. Do not
forward authentication to redirects. Treat every 3xx as failure even if curl's
exit code is zero. Do not print headers or use verbose/trace flags. Before use,
read the final three-digit HTTP status appended by `--write-out` separately from
the response body; a missing/000 status is not success. For these exact patterns
use paths without whitespace or shell metacharacters; otherwise review an exactly
quoted command and its matching permission entry before use. Before execution,
verify local curl supports these options and the configured host/path is exact.

In Day-2, the example allows a single ID's `PUT /v1/policies/{id}` with JSON content
type and `--data-binary @<reviewed-body-file>`. Read **PutPolicy** and
**PolicyServicePutPolicyBody** first: a GET response is not automatically the PUT
body. A separate approved `POST /v1/policies/dryrun` uses its own request model
and payload file; it is never granted by the read-only profile. The examples do
not grant async dryrunjob, reassess, delete, exceptions or restore automatically.

Only `roxctl version` and `roxctl --help` are initially allowed as CLI discovery.
Select additional exact CLI operations from the [command reference](../../openshift-docs/references/acs-4.11/cli/command-reference/roxctl.md),
check local help, and review narrowly scoped `ask` patterns with the configured
`--endpoint` and `--ca`. roxctl supports a protected token file or `ROX_API_TOKEN`;
the user provisions authentication outside OpenCode. Do not use the read MCP token
for writes. Backup/scan/upload commands are not implicitly read-only.

OpenCode patterns are approval routing, **not a shell sandbox**. Wildcards and a
privileged shared process are not endpoint or credential isolation. Review each
full command; use OS isolation, RHACS scopes and network egress policy for hard
enforcement. Do not add broad `curl *` or `roxctl *` permissions.

Before reading Secret contents or credential-bearing Central objects offer the
existing four choices: metadata/key names; placeholders with manual input outside
OpenCode; explicitly approved named raw processing; abort. Warn before raw
processing that values can enter model context and local OpenCode session data.
The selection is task-local unless the user explicitly chooses session-wide.
Externally provisioned authentication does not authorize displaying its value.
