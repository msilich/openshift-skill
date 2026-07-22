<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can specify a list of IP address ranges for the Ingress Controller. This action restricts access to the load balancer service when you specify the `LoadBalancerService` value for the `endpointPublishingStrategy` parameter.

# Configuring load balancer allowed source ranges

You can enable and configure the `spec.endpointPublishingStrategy.loadBalancer.allowedSourceRanges` parameter. By configuring load balancer allowed source ranges, you can limit the access to the load balancer for the Ingress Controller to a specified list of IP address ranges.

The Ingress Operator reconciles the load balancer Service and sets the `spec.loadBalancerSourceRanges` parameter based on `AllowedSourceRanges`.

> [!NOTE]
> If you have already set the `spec.loadBalancerSourceRanges` parameter or the load balancer service anotation `service.beta.kubernetes.io/load-balancer-source-ranges` in a previous version of OpenShift Container Platform, Ingress Controller starts reporting `Progressing=True` after an upgrade. To fix this, set `AllowedSourceRanges` that overwrites the `spec.loadBalancerSourceRanges` parameter and clears the `service.beta.kubernetes.io/load-balancer-source-ranges` annotation. Ingress Controller starts reporting `Progressing=False` again.

<div>

<div class="title">

Prerequisites

</div>

- You have a deployed Ingress Controller on a running cluster.

</div>

<div>

<div class="title">

Procedure

</div>

- Set the allowed source ranges API for the Ingress Controller by running the following command:

  ``` terminal
  $ oc -n openshift-ingress-operator patch ingresscontroller/default \
      --type=merge --patch='{"spec":{"endpointPublishingStrategy": \
      {"type":"LoadBalancerService", "loadbalancer": \
      {"scope":"External", "allowedSourceRanges":["0.0.0.0/0"]}}}}'
  ```

  where:

  `allowedSourceRanges`
  The example value `0.0.0.0/0` specifies the allowed source range.

</div>

# Migrating to load balancer allowed source ranges

If you have already set the annotation `service.beta.kubernetes.io/load-balancer-source-ranges`, you can migrate to load balancer allowed source ranges. When you set the `AllowedSourceRanges`, the Ingress Controller sets the `spec.loadBalancerSourceRanges` field based on the `AllowedSourceRanges` value and unsets the `service.beta.kubernetes.io/load-balancer-source-ranges` annotation.

> [!NOTE]
> If you have already set the `spec.loadBalancerSourceRanges` parameter or the load balancer service anotation `service.beta.kubernetes.io/load-balancer-source-ranges` in a previous version of OpenShift Container Platform, the Ingress Controller starts reporting `Progressing=True` after an upgrade. To fix this, set `AllowedSourceRanges` that overwrites the `spec.loadBalancerSourceRanges` parameter and clears the `service.beta.kubernetes.io/load-balancer-source-ranges` annotation. The Ingress Controller starts reporting `Progressing=False` again.

<div>

<div class="title">

Prerequisites

</div>

- You have set the `service.beta.kubernetes.io/load-balancer-source-ranges` annotation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check that the `service.beta.kubernetes.io/load-balancer-source-ranges` is set by entering the following command:

    ``` terminal
    $ oc get svc router-default -n openshift-ingress -o yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        service.beta.kubernetes.io/load-balancer-source-ranges: 192.168.0.1/32
    ```

    </div>

2.  Check that the `spec.loadBalancerSourceRanges` parameter is unset by entering the following command:

    ``` terminal
    $ oc get svc router-default -n openshift-ingress -o yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    ...
    spec:
      loadBalancerSourceRanges:
      - 0.0.0.0/0
    ...
    ```

    </div>

3.  Update your cluster to OpenShift Container Platform 4.17.

4.  Set the allowed source ranges API for the `ingresscontroller` by running the following command:

    ``` terminal
    $ oc -n openshift-ingress-operator patch ingresscontroller/default \
        --type=merge --patch='{"spec":{"endpointPublishingStrategy": \
        {"loadBalancer":{"allowedSourceRanges":["0.0.0.0/0"]}}}}'
    ```

    where:

    `allowedSourceRanges`
    The example value `0.0.0.0/0` specifies the allowed source range.

</div>

# Additional resources

- [Introduction to OpenShift updates](../../../updating/understanding_updates/intro-to-updates.md#understanding-openshift-updates)
