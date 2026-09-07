# Workloads and service reachability

Read the matching chapter in [sources.md](sources.md), then follow the shared domain contract.

## Pod startup and scheduling

Discover the workload and its owner references or label selector. Inspect a small
representative set of affected pods, including init containers, waiting and last
termination reasons, readiness, restarts, and the first relevant events.

| Evidence | Next check |
| --- | --- |
| ImagePullBackOff / ErrImagePull | Read the actual pull error and exact image digest/tag. Distinguish missing image, authentication, registry trust and connectivity; use openshift-disconnected when a mirror is involved. |
| CrashLoopBackOff | Read bounded previous-container logs and termination details. Check OOMKilled, limits, probes and recent rollout changes. The backoff status alone does not establish the cause. |
| Pending / Unschedulable | Follow the scheduler message to requests, node capacity, taints/tolerations, affinity, quota or an unbound PVC. |
| Init container waiting | Inspect that init container's dependency and logs before the main container. |

MCP resource reads, pod logs and events are the preferred evidence path.
An equivalent fallback is `oc --kubeconfig <verified-path> logs <pod> -n <namespace>
-c <container> --previous --tail=100`; use it only when the MCP
cannot request previous logs and the command is permitted.

Do not restart or delete the pod as a diagnostic first step. A repair must address
the observed cause and preserve the owning controller's intended configuration.

## Service and Route failures

Trace the requested hostname/port through Route admission and TLS settings,
Service selector and port mapping, EndpointSlices, and target pod readiness.
Zero ready endpoints directs investigation toward selectors/readiness, not an
assumed router restart. With ready endpoints, inspect the affected network
policies and DNS/ingress conditions before proposing active network probes.

A curl/exec/debug test can contact a service or create a pod. Show its target and
command and use the existing permission gates; do not classify it as a passive API
read. Preserve private CA verification. A successful rollout is insufficient:
verify the user's original service path, or explicitly report that it remains untested.
