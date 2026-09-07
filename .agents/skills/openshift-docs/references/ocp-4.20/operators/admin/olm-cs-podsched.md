<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When a `grpc` type catalog source defines the `spec.image` field, the Catalog Operator creates a pod to serve that image.

By default, the pod specification configures the following default settings:

- Node selector: `kubernetes.io/os=linux`

- Priority class name: `system-cluster-critical`

- Tolerations: None

As an administrator, you can override these defaults by configuring fields in the optional `spec.grpcPodConfig` section of the `CatalogSource` object.

> [!IMPORTANT]
> The Marketplace Operator, `openshift-marketplace`, manages the default `OperatorHub` custom resource’s (CR). This CR manages `CatalogSource` objects. If you attempt to modify fields in the `CatalogSource` object’s `spec.grpcPodConfig` section, the Marketplace Operator automatically reverts these modifications. By default, if you modify fields in the `spec.grpcPodConfig` section of the `CatalogSource` object, the Marketplace Operator automatically reverts these changes.
>
> To apply persistent changes to `CatalogSource` object, you must first disable a default `CatalogSource` object.

<div>

<div class="title">

Additional resources

</div>

- [OLM concepts and resources → Catalog source](../understanding/olm/olm-understanding-olm.md#olm-catalogsource_olm-understanding-olm)

</div>

# Disabling default CatalogSource objects at a local level

You can make persistent local changes to a `CatalogSource` object by disabling the default `CatalogSource` object. Otherwise, the Marketplace Operator automatically reverts any manual modifications to fields in the `spec.grpcPodConfig` section.

The Marketplace Operator, `openshift-marketplace`, manages the default custom resources (CRs) of the `OperatorHub`. The `OperatorHub` manages `CatalogSource` objects.

To apply persistent changes to `CatalogSource` object, you must first disable a default `CatalogSource` object.

<div>

<div class="title">

Procedure

</div>

- To disable all the default `CatalogSource` objects at a local level, enter the following command:

  ``` terminal
  $ oc patch operatorhub cluster -p '{"spec": {"disableAllDefaultSources": true}}' --type=merge
  ```

  > [!NOTE]
  > You can also configure the default `OperatorHub` CR to either disable all `CatalogSource` objects or disable a specific object.

</div>

<div>

<div class="title">

Additional resources

</div>

- [OperatorHub custom resource](../understanding/olm-understanding-software-catalog.md#olm-software-catalog-arch-operatorhub-crd_olm-understanding-software-catalog)

- [Disabling the default OperatorHub catalog sources](../../disconnected/using-olm.md#olm-restricted-networks-operatorhub_olm-restricted-networks)

</div>

# Overriding the node selector for catalog source pods

To control which nodes run catalog source pods, you can override the default node selector in the `spec.grpcPodConfig` section of the `CatalogSource` object.

<div>

<div class="title">

Prerequisites

</div>

- A `CatalogSource` object of source type `grpc` with `spec.image` is defined.

</div>

<div>

<div class="title">

Procedure

</div>

- Edit the `CatalogSource` object and add or modify the `spec.grpcPodConfig` section to include the following:

  ``` yaml
    grpcPodConfig:
      nodeSelector:
        custom_label: <label>
  ```

  where `<label>` is the label for the node selector that you want catalog source pods to use for scheduling.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Placing pods on specific nodes using node selectors](../../nodes/scheduling/nodes-scheduler-node-selectors.md#nodes-scheduler-node-selectors)

</div>

# Overriding the priority class name for catalog source pods

To control the scheduling priority of catalog source pods, you can override the default priority class name in the `spec.grpcPodConfig` section of the `CatalogSource` object.

<div>

<div class="title">

Prerequisites

</div>

- A `CatalogSource` object of source type `grpc` with a defined `spec.image`.

</div>

<div>

<div class="title">

Procedure

</div>

- Edit the `CatalogSource` object and configure the `spec.grpcPodConfig` section, similar to the following example:

  ``` yaml
    grpcPodConfig:
      priorityClassName: <priority_class>
  ```

  where:

  `<priority_class>`
  Specifies one of the following priority classes:

  - A default Kubernetes priority class, such as `system-cluster-critical` or `system-node-critical`

  - An empty string (`""`) to assign the default priority

  - A custom, pre-existing priority class name

  > [!NOTE]
  > Previously, the only pod scheduling parameter that could be overriden was `priorityClassName`. This was done by adding the `operatorframework.io/priorityclass` annotation to the `CatalogSource` object. For example:
  >
  > ``` yaml
  > apiVersion: operators.coreos.com/v1alpha1
  > kind: CatalogSource
  > metadata:
  >   name: example-catalog
  >   namespace: openshift-marketplace
  >   annotations:
  >     operatorframework.io/priorityclass: system-cluster-critical
  > ```
  >
  > If a `CatalogSource` object defines both the annotation and `spec.grpcPodConfig.priorityClassName`, the annotation takes precedence over the configuration parameter.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Pod priority classes](../../nodes/pods/nodes-pods-priority.md#admin-guide-priority-preemption-priority-class_nodes-pods-priority)

</div>

# Overriding tolerations for catalog source pods

To allow catalog source pods to schedule onto nodes with matching taints, you can override the default tolerations in the `spec.grpcPodConfig` section of the `CatalogSource` object.

<div>

<div class="title">

Prerequisites

</div>

- A `CatalogSource` object of source type `grpc` with `spec.image` is defined.

</div>

<div>

<div class="title">

Procedure

</div>

- Edit the `CatalogSource` object and add or modify the `spec.grpcPodConfig` section to include the following:

  ``` yaml
    grpcPodConfig:
      tolerations:
        - key: "<key_name>"
          operator: "<operator_type>"
          value: "<value>"
          effect: "<effect>"
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Understanding taints and tolerations](../../nodes/scheduling/nodes-scheduler-taints-tolerations.md#nodes-scheduler-taints-tolerations-about_nodes-scheduler-taints-tolerations)

</div>
