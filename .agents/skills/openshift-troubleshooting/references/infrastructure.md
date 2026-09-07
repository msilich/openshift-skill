# Storage, nodes and Operators

Use the relevant procedures in [sources.md](sources.md). Keep infrastructure
investigation tied to the reported symptom.

## PVC and attachment problems

Read PVC conditions/events, requested storage class, access mode and capacity.
Discover the referenced PV, StorageClass, CSI controller and VolumeAttachment
only as indicated by those observations. With WaitForFirstConsumer, check
scheduling/topology before concluding that provisioning is broken.
A multi-attach message calls for evidence about the current attachment and pod/node
ownership. Do not remove finalizers, detach volumes or delete PVCs as a generic fix.
After an approved repair verify binding, attachment, pod mount and an application
read/write check agreed with the user.

## Node and Operator problems

Inspect node Ready/pressure conditions, taints, allocatable resources and recent
events. Relate failures to the MachineConfigPool and affected workloads.
For ClusterOperators read condition messages, versions and related objects.
For optional OLM Operators inspect Subscription, InstallPlan, CSV and CatalogSource
only when discovered on the cluster; do not conflate a ClusterOperator with a CSV.

Follow a failing operand to its pod or dependency. Node debug, host logs, drains
and reboots require the normal Day-2 procedure. Do not disable reconciliation or
grant cluster-admin to make a diagnostic check work.

## Alerts and timing

If the installed MCP offers permitted alert/metric queries, inspect the named
alert labels, rule and time range, then correlate by node, namespace or workload.
Otherwise use available conditions, events and bounded logs and report the metric
gap. Do not fetch external runbooks or install Prometheus helpers at runtime.
Compare recent changes with the onset; temporal proximity is a hypothesis, not
proof. Report exact object names and evidence for every causal link.
