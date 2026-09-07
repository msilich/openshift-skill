# Evidence-led Dev Spaces diagnosis

Read the relevant troubleshooting chapters in [sources.md](sources.md). Apply the
shared read-only execution, identity and Secret contract before collecting evidence.

| Symptom | Narrow the cause using |
| --- | --- |
| Workspace stays Pending | DevWorkspace conditions, generated pod/init-container state, PVC binding, quota, scheduling and events |
| ImagePullBackOff | Exact effective image, failing registry and event; distinguish missing image, trust, reachability and authorization |
| IDE cannot be reached | Workspace readiness, Service selectors and ready EndpointSlices, Route admission, TLS/proxy and browser error |
| Platform unavailable | CheCluster conditions, Operator reconciliation, operand readiness and bounded component logs |
| Workspace is slow | Time-stamped startup stages, init/image-pull duration, resource pressure and permitted metrics; do not invent universal thresholds |
| OAuth or private Git fails | Configured provider/host, callback route, CA trust and non-secret error details; ask before sensitive data access |

For a Pending PVC correlate its events, requested storage class and access mode,
available provisioner evidence, quota and scheduling constraints. `WaitForFirstConsumer`
can make pod scheduling relevant to binding. Do not equate Pending with lost data or
delete/recreate the claim without a specific approved recovery plan.

For a controller-reverted change identify the owning CR or Git source, generation and
reconciliation evidence. A transient manual edit is not a lasting fix. Prepare the
change at the owning source only when the user requested remediation.

Prefer offered MCP resource, event and bounded log tools. A missing tool can use the
same explicit kubeconfig through permitted `oc`; Forbidden cannot. Limit log scope
before retrieval. Do not invoke broad `dsc` support bundles or debug/exec automatically;
they can expose secrets, execute code or change state.

Separate observed facts, plausible causes and missing evidence. A diagnosis can end
with an unresolved cause; do not present a healthy state when necessary evidence is
unavailable. After an approved fix recheck the original workspace/IDE symptom.
