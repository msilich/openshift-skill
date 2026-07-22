# Day-2 operations

## Workflow

1. Restate the expected cluster, identity, namespace, object, desired outcome, and success signal. If the task might access a Secret, resolve the per-task choice from `safety.md` before any Secret operation.
2. Run the context and identity checks from `SKILL.md`; do not continue through a mismatch.
3. Inspect only the relevant objects, recent events, bounded log tails, and health signals.
4. Verify the exact served API version and the schema, field, or subresource used by the mutation. Follow the live-discovery order in the `openshift-api` skill; for CRs, verify the matching CRD version schema. Stop rather than inventing an API version or field.
5. Form a root-cause hypothesis from observed state. Separate facts from inference. Capture the current manifest or relevant fields before mutation and note field ownership when using server-side apply.
6. Explain the exact intended delta, impact radius, success criteria, verification plan, and rollback before executing anything that persists a change.
7. Perform a server-side dry-run or diff when the operation supports one, using the same explicit kubeconfig and intended API version. Show the result. If MCP cannot preview the operation, use a narrowly scoped `oc` fallback; if the API or operation has no preview, state that limitation and added risk explicitly.
8. Let OpenCode request a fresh `once` approval for the actual MCP or `oc` mutation. Never depend on MCP elicitation or reuse an approval from discovery or preview.
9. Execute one bounded change. Avoid parallel writes to related objects.
10. Re-read the changed object and verify rollout, readiness, conditions, events, logs, route/service behavior, and the user's original success signal.
11. If verification fails, stop and present evidence. Obtain a new approval before rollback or another mutation.

## Tool selection

Prefer these MCP paths:

| Goal | MCP tools | Verify with |
| --- | --- | --- |
| Inspect resources | `resources_list`, `resources_get` | conditions, generation, observedGeneration |
| Inspect workloads | `pods_list_in_namespace`, `pods_get`, `pods_log`, `events_list` | readiness, restarts, bounded current/previous logs |
| Apply desired state | `resources_create_or_update` | fetch full object, rollout and dependent objects |
| Scale workload | `resources_scale` | desired/available replicas and pod readiness |
| Restart via pod replacement | `pods_delete` | replacement pod ownership and readiness |
| Delete object | `resources_delete` | absence plus dependent/finalizer behavior |
| Resource pressure | `pods_top`, `nodes_top`, `nodes_stats_summary` | workload/node conditions and events |
| In-container diagnosis | `pods_exec` | exact command result and post-condition |

`resources_create_or_update` uses server-side apply and its input is the complete desired state owned by that field manager. Fetch the existing object first, preserve required fields, and show the meaningful delta. Do not use it as a blind patch.

## `oc` fallback

Use `oc --kubeconfig <same-path> ...` only for an unsupported capability or when exact CLI behavior is materially safer, such as server-side dry-run/diff, rollout status, operator-specific commands, or a narrowly scoped admin diagnostic. Explain why MCP was insufficient. In the read-only profile, use only the explicit read-command allowlist in the OpenCode template; any write fallback requires the Day-2 profile.

Keep fallback commands non-interactive and bounded. Avoid shell pipelines, substitutions, temporary credential files, and broad `-A` output unless essential. Never use `oc login`, `oc config use-context`, or commands that modify the configured identity.

## Risk gates

Treat these as critical operations requiring an explicit target-specific plan and a fresh `once` approval:

- any delete, especially namespace, persistent volume, CRD, webhook, APIService, or operator deletion;
- RBAC, OAuth, identity-provider, admission, or SCC changes;
- Operator lifecycle, subscription, configuration, upgrade, or operand changes;
- storage class, PV/PVC, snapshot, attachment, migration, restore, or data-protection changes;
- network policy, ingress controller, route, proxy, DNS, cluster-network, or other connectivity changes;
- MachineConfig, node debug, host access, drain, reboot, upgrade, or control-plane work;
- certificate rotation or other cluster-wide configuration;
- `pods_exec` into privileged workloads or any command that can reach host or credentials.

For upgrades and recovery, check vendor prerequisites and current cluster health first. Never improvise a version path or continue past a degraded prerequisite.

## Completion evidence

Report the actual context and identity used, changed objects, verification performed, remaining risk, and any rollback artifact. If only the API accepted the request, say that the operation was submitted and continue monitoring until the requested outcome is demonstrated or a concrete blocker is found.
