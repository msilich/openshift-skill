# Workspaces, devfiles and persistence

Use [sources.md](sources.md) to open the local workspace, devfile and storage chapters.

Identify the requested user namespace and DevWorkspace, its associated templates,
devfile source/revision and owner. Inspect only the necessary resource fields;
devfiles, environment variables and repository URLs can contain sensitive values.
Determine whether configuration is owned by the user, CheCluster defaults, a
DevWorkspaceTemplate, or another controller before preparing changes.

For startup follow the dependent resources: DevWorkspace conditions and messages,
generated pod/init containers, image pulls, PVCs, quota, scheduling and events.
For IDE access correlate workspace readiness with Service/EndpointSlice/Route
state and the specific observed browser error. A Ready pod does not prove a
successful authenticated IDE session; request a user check if it cannot be tested
through the permitted access.

For devfile errors compare the supplied devfile version and fields with the local
product guide and the matching devfile schema if available offline. Kubernetes
`oc explain` validates served CR schemas, not an arbitrary devfile specification.
Do not invent a schema or fetch one in the airgap; report missing evidence.

Before stop, restart, delete or storage changes identify persistence strategy,
attached PVCs, uncommitted work, data-retention consequences and the user's intended
outcome. Do not delete a workspace/PVC to resolve an unexplained Pending condition.
Use the shared Day-2 workflow for approved changes; verify workspace startup, IDE
access and an agreed persistence check rather than only successful API submission.
