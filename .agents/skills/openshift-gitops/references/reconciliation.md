# Reconciliation and resource ownership

The bundled GitOps source is 1.21, independently of the OCP version. Inspect the
installed GitOps/Argo CD version and consult [sources.md](sources.md).
Do not copy example apiVersion values without live discovery.

## Establish the two views

Identify the Argo CD instance namespace, Application name, destination cluster
and namespace, repository URL, path/chart and resolved revision. Avoid printing
credential-bearing URLs. For multiple sources record each applicable revision.
For ApplicationSets inspect generator/template and ownership before inspecting a
generated Application. A change to generated output may be overwritten.

Use only the read operations actually advertised by `argocd_read`. If it is
unavailable, use permitted OpenShift reads of served Application/ApplicationSet
CRs and workload objects; report any missing rendered-desired-state or diff data.
Never invent an Argo CD tool name or log in automatically.

## Sync and health

Read sync status, health status, conditions, operation state and per-resource
differences separately. Synced does not prove application health.
Follow Degraded to the named workload and use openshift-troubleshooting.

For an OutOfSync resource compare the reported desired and live fields with
owner references, managedFields and recent controller activity. A field being
rewritten is evidence to investigate the owning controller, webhook, HPA or
Operator. Do not repeatedly sync, force-apply, or add ignoreDifferences merely to
hide the discrepancy. If desired manifests are unavailable, report the drift
cause as unverified rather than reconstructing Git contents from memory.

Before suggesting sync, prune, replace or an ApplicationSet template change,
describe the actual affected resources and deletion/recreation implications.
The configured Argo CD MCP is read-only: do not invoke these writes through it.
