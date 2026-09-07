# Image-pull and trust diagnosis

Read [sources.md](sources.md), then establish the affected pod/container,
exact image reference and observed pull error using the shared domain contract.

| Observed error | Evidence to collect before a change |
| --- | --- |
| manifest unknown / not found | Exact tag/digest and repository; compare against the selected/imported image set and generated mirrors. |
| unauthorized / denied | Referenced pull-secret name, service account and registry host; inspect values only after the user's Secret decision. |
| x509 / unknown authority | Registry hostname, certificate chain and configured trust source; do not disable TLS verification. |
| timeout / name resolution | Reachability and DNS from the affected node's path, registry availability and proxy/noProxy configuration. |
| Public registry attempted | Image reference, matching IDMS/ITMS scope, digest-versus-tag semantics and configured source fallback; do not assume the mirror is applied. |

Inspect the installed image configuration and discover the served mirror API before
proposing changes. Local workstation access does not prove node access.
Use API evidence first; active registry/node tests require an explicit target and
permitted command. Do not tunnel tests through a privileged pod to bypass access limits.

After an approved correction confirm the affected workload can pull the intended
image and reaches readiness. If a restart/redeployment is needed, request it as a
separate mutation through openshift-mcp. Do not infer success just because a mirror
object was accepted.
