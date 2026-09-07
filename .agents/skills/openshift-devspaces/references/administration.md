# Platform administration

Read the installation, configuration or upgrade chapters listed in [sources.md](sources.md)
for the requested operation; do not perform an installation just to diagnose a workspace.

- Establish the actual installation namespace, CheCluster name, Subscription/CSV,
  installed Dev Spaces version and Dev Workspace Operator version. Discover resource
  names and served versions before querying CRs; do not hardcode a namespace or CR name.
- Read CheCluster status/conditions, relevant Operator workloads and bounded events.
  Distinguish an Operator installation failure from an operand or workspace failure.
- CheCluster is the operator-managed platform's configuration entry point. Inspect
  ownerReferences, managedFields and any GitOps owner before proposing a delta.
  Do not directly edit an Operator-generated Deployment/ConfigMap to make it persist.
  For a Git-managed CR prepare a reviewable Git/manifest change with `openshift-gitops`.
- Treat registry credentials, OAuth client secrets and certificate private keys as
  Secret access under the shared four-choice contract. Even ConfigMaps and logs may
  contain credentials; collect only the relevant, approved fields.
- Installation, upgrade, RBAC, networking and storage are high-risk Day-2 changes.
  Verify live schemas, show the delta and preview when supported, obtain fresh `once`
  approval, execute one scoped change and check observedGeneration/conditions and
  component readiness. Then verify dashboard access and an agreed test workspace.
- An upgrade needs a documented source/target path and compatible Operators/OCP.
  Missing offline support evidence remains unverified; do not improvise downgrades.

Generic resource reads and approved resource changes can use the offered OpenShift
MCP tools. If a needed capability is absent use the allowed `oc --kubeconfig <same-path>`
fallback, not after a permission denial. `dsc` is optional: when unavailable or not
permitted, show reviewed instructions and state they were not executed. Do not add
permissions, download the CLI or route a denied command through pod exec.
