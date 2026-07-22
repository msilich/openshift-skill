---
name: openshift-api
description: Discover and verify Kubernetes and OpenShift API resources, served group versions, fields, and CRD schemas from the target cluster. Use before creating or reviewing manifests, choosing apiVersion/kind pairs, diagnosing rejected fields, or calling generic oc or MCP resource operations when the exact live API schema matters.
---

# OpenShift API Discovery

Use read-only discovery against the intended cluster. Establish the expected cluster and context first, then pass the same explicit, single-context kubeconfig to every command as `oc --kubeconfig <path> ...`. Never switch context or rely on the ambient `oc` configuration. The command forms below omit that common prefix only for readability. Treat live cluster output as authoritative for what that cluster serves.

## Follow the fixed discovery order

1. Find the canonical resource name, group, kind, scope, and verbs:
   `oc api-resources -o wide`
2. Verify that the selected group/version is served:
   `oc api-versions`
3. Read the resource schema with an explicit version:
   `oc explain <resource> --api-version=<group/version>`
4. Inspect the requested field recursively with the same version:
   `oc explain <resource>.<field> --api-version=<group/version> --recursive`
   When the question concerns the complete resource rather than a field, use `<resource>` as the recursive target.
5. If `explain` is absent or incomplete, inspect the OpenAPI v3 index:
   `oc get --raw /openapi/v3`
   Fetch the exact `serverRelativeURL` advertised for the selected group/version; do not construct or guess it.
6. For a CRD, inspect its matching version schema last:
   `oc get crd <plural>.<group> -o json`
   Use `.spec.versions[]` with the selected version and read `.schema.openAPIV3Schema`.

Do not reorder or skip earlier discovery based on memory. Later sources refine an incomplete result; they do not justify silently changing the resource or API version.

For repeatable evidence collection, run:

```bash
bash <resolved-skill-directory>/scripts/collect-discovery.sh \
  --kubeconfig <explicit-kubeconfig> \
  --resource <resource> \
  --api-version <group/version> \
  [--field <field-path>] \
  [--crd <plural>.<group>]
```

Resolve `<resolved-skill-directory>` from this loaded `SKILL.md`; never assume the process working directory or installation location.

## Evidence rules

- Never invent a resource, version, field, enum, default, or validation rule.
- Stop and report the item as unverified when the target cluster does not provide schema evidence.
- Do not substitute documentation for another OpenShift release or a similar API version without labeling it as non-authoritative context.
- Cite the exact successful command and selected API version for every schema conclusion. For CRDs, also cite the CRD name and `.spec.versions[]` entry.
- Report conflicting sources explicitly. Do not merge incompatible field definitions.
- Keep discovery read-only. Field existence does not imply authorization; verify permission separately with `oc auth can-i` before proposing an operation.
- Never expose Secret values, bearer tokens, client keys, or complete kubeconfigs.

## References

- Read [references/discovery-workflow.md](references/discovery-workflow.md) when resolving ambiguous resource names, OpenAPI paths, or CRD versions.
- Read [references/evidence-reporting.md](references/evidence-reporting.md) when presenting verified fields, unsupported versions, or source conflicts.
