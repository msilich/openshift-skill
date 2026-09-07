<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Operator Lifecycle Manager (OLM) uses Operator conditions to communicate additional lifecycle information about an Operator that OLM cannot infer on its own.

# About Operator conditions

Operator Lifecycle Manager (OLM) infers Operator state from Kubernetes resources, but some conditions require explicit communication. You can use the `OperatorCondition` custom resource definition (CRD) to tell OLM about supported conditions that affect lifecycle management.

> [!NOTE]
> By default, the `Spec.Conditions` array is not present in an `OperatorCondition` object until it is either added by a user or as a result of custom Operator logic.

# Supported conditions

Operator Lifecycle Manager (OLM) supports a specific set of Operator conditions that communicate the state of an Operator.

## Upgradeable condition

The `Upgradeable` Operator condition prevents an existing cluster service version (CSV) from being replaced by a newer version of the CSV. This condition is useful when:

- An Operator is about to start a critical process and should not be upgraded until the process is completed.

- An Operator is performing a migration of custom resources (CRs) that must be completed before the Operator is ready to be upgraded.

> [!IMPORTANT]
> Setting the `Upgradeable` Operator condition to the `False` value does not avoid pod disruption. If you must ensure your pods are not disrupted, see "Using pod disruption budgets to specify the number of pods that must be up" and "Graceful termination" in the "Additional resources" section.

<div class="formalpara">

<div class="title">

Example `Upgradeable` Operator condition

</div>

``` yaml
apiVersion: operators.coreos.com/v1
kind: OperatorCondition
metadata:
  name: my-operator
  namespace: operators
spec:
  conditions:
  - type: Upgradeable
    status: "False"
    reason: "migration"
    message: "The Operator is performing a migration."
    lastTransitionTime: "2020-08-24T23:15:55Z"
```

</div>

- The `type` field sets the name of the condition.

- A `False` value in the `status` field indicates the Operator is not ready to be upgraded. OLM prevents a CSV that replaces the existing CSV of the Operator from leaving the `Pending` phase. A `False` value does not block cluster upgrades.

# Additional resources

- [Managing Operator conditions](../../admin/olm-managing-operatorconditions.md#olm-operatorconditions)

- [Understanding how to use pod disruption budgets to specify the number of pods that must be up](../../../nodes/pods/nodes-pods-configuring.md#nodes-pods-pod-disruption-about_nodes-pods-configuring)

- [Graceful termination](../../../applications/deployments/route-based-deployment-strategies.md#deployments-graceful-termination_route-based-deployment-strategies)
