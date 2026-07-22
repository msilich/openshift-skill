# Simple OpenShift GitOps Argo CD MCP read-only patches

These small YAML merge patches target the default Red Hat OpenShift GitOps
instance. They create the operator-managed API token for `opencode-mcp` and
configure its global Argo CD read-only policy.

## Exact preconditions

Use these static YAMLs only when all of the following are true:

- the `ArgoCD` resource is `openshift-gitops/openshift-gitops`;
- `.spec.localUsers` is absent, empty, or already contains only the supplied
  `opencode-mcp` entry;
- `.spec.rbac.policy` is empty, contains only the two standard OpenShift
  cluster-admin mappings shown in `02-readonly-policy.merge.yaml`, or already
  matches the supplied file; and
- `.spec.rbac.defaultPolicy` does not grant write access to authenticated users;
- the live CRD serves `argoproj.io/v1beta1` with `spec.localUsers` and
  `spec.rbac.policy`.

The live CRD does not declare `localUsers` as a mergeable map-list, and the RBAC
policy is one scalar string. A merge patch therefore replaces those two fields.
If the customer has any additional local user or custom policy line, stop and
use `configure-argocd-mcp-opencode.mjs`; it preserves unrelated entries.

These files contain no token. The Operator creates the token in the named
Secret `opencode-mcp-local-user` after the first patch.

## Inspect and preview

Set one explicit administrative kubeconfig and verify the exact target:

```bash
export KUBECONFIG_ADMIN=/secure/path/admin.kubeconfig

oc --kubeconfig "$KUBECONFIG_ADMIN" config current-context
oc --kubeconfig "$KUBECONFIG_ADMIN" whoami
oc --kubeconfig "$KUBECONFIG_ADMIN" whoami --show-server

oc --kubeconfig "$KUBECONFIG_ADMIN" -n openshift-gitops \
  get argocd openshift-gitops \
  -o jsonpath='{.spec.localUsers}{"\n"}{.spec.rbac.defaultPolicy}{"\n"}{.spec.rbac.policy}{"\n"}'
```

Review the two YAML files, then perform server-side dry-runs. These commands do
not persist a change:

```bash
oc --kubeconfig "$KUBECONFIG_ADMIN" -n openshift-gitops \
  patch argocd openshift-gitops --type merge \
  --patch-file 01-api-user.merge.yaml --dry-run=server -o name

oc --kubeconfig "$KUBECONFIG_ADMIN" -n openshift-gitops \
  patch argocd openshift-gitops --type merge \
  --patch-file 02-readonly-policy.merge.yaml --dry-run=server -o name
```

## Apply in order

After customer approval, apply exactly one patch at a time and verify it before
continuing:

```bash
oc --kubeconfig "$KUBECONFIG_ADMIN" -n openshift-gitops \
  patch argocd openshift-gitops --type merge \
  --patch-file 01-api-user.merge.yaml

oc --kubeconfig "$KUBECONFIG_ADMIN" -n openshift-gitops \
  get secret opencode-mcp-local-user \
  -o custom-columns='NAME:.metadata.name,MANAGED-BY:.metadata.labels.app\.kubernetes\.io/managed-by'

oc --kubeconfig "$KUBECONFIG_ADMIN" -n openshift-gitops \
  patch argocd openshift-gitops --type merge \
  --patch-file 02-readonly-policy.merge.yaml

argocd admin settings rbac validate \
  --kubeconfig "$KUBECONFIG_ADMIN" --namespace openshift-gitops
argocd admin settings rbac can opencode-mcp get applications '*' \
  --kubeconfig "$KUBECONFIG_ADMIN" --namespace openshift-gitops
argocd admin settings rbac can opencode-mcp sync applications '*' \
  --kubeconfig "$KUBECONFIG_ADMIN" --namespace openshift-gitops
argocd admin settings rbac can opencode-mcp delete applications '*' \
  --kubeconfig "$KUBECONFIG_ADMIN" --namespace openshift-gitops
```

Expected RBAC results are `Yes`, `No`, and `No`. The last two commands return a
non-zero exit status because access is denied; that is the intended result.

Do not run `oc apply -f .`. These are merge-patch documents, not complete
resources. Do not read or decode the token Secret until the task-scoped Secret
handling mode has been explicitly selected.

## Rollback

The `rollback/` patches restore the same assumed default state. They also
replace the complete `localUsers` and `rbac.policy` fields. Use them only if the
exact preconditions above still hold, preview them with `--dry-run=server`, and
apply them one at a time with `oc patch --type merge --patch-file ...`.
