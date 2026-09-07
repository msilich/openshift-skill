# Repository access and reviewed changes

Use [sources.md](sources.md) for the GitOps custom resource, repo-server trust and
RBAC procedures. Read-only inspection uses the shared domain contract.

For repository errors inspect Application conditions and bounded repo-server logs.
Distinguish DNS/route, TLS trust, authentication, repository/ref/path and manifest
rendering failures. An accessible Git repository does not prove that Helm
dependencies or plugins are available in the air gap. Do not download missing
dependencies or run arbitrary repository scripts.

Resolve the user's Secret mode before reading repository credential Secrets,
tokens or manifests that could contain values. Argo CD authorization and
Kubernetes RBAC are separate checks; one success does not prove the other.
Do not disable TLS verification or change the configured Argo CD identity.

## Select the authoritative change location

- Git-managed desired state: prepare a scoped Git/manifest diff for the requested
  repository/path. Persist it only when local edit permissions allow it. Do not
  commit, push, sync or prune without that requested action.
- Operator-managed Argo CD configuration: verify the live ArgoCD CR schema and
  change the CR through the approved OpenShift Day-2 path. Do not patch generated
  argocd-cm or argocd-rbac-cm ConfigMaps.
- Generated ApplicationSet applications: change the owning template or source,
  not the generated child, unless a documented, explicitly requested exception applies.

Show impact, preview and fresh approval through openshift-mcp for cluster writes.
If no supported preview exists, explain that before approval. Keep
`argocd_read` and `MCP_READ_ONLY=true` unchanged; do not create a write MCP profile.

After the requested action verify reconciliation, sync and health, the resolved
revision and the application's actual service behavior. A prepared patch is not
an applied repair. Report pending Git publication/sync or unavailable checks explicitly.
