<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

An OpenShift Container Platform cluster with multi-architecture compute machines supports compute machines with different architectures.

> [!NOTE]
> When you have nodes with multiple architectures in your cluster, the architecture of your image must be consistent with the architecture of the node. You must ensure that the pod is assigned to the node with the appropriate architecture and that it matches the image architecture. For more information on assigning pods to nodes, see [Scheduling workloads on clusters with multi-architecture compute machines](../../../post_installation_configuration/configuring-multi-arch-compute-machines/multi-architecture-compute-managing.md#scheduling-workloads-on-clusters-with-multi-architecture-compute-machines).

You can install an AWS cluster with the support for configuring multi-architecture compute machines. After installing the AWS cluster, you can add multi-architecture compute machines to the cluster in the following ways:

- Adding 64-bit x86 compute machines to a cluster that uses 64-bit ARM control plane machines and already includes 64-bit ARM compute machines. In this case, 64-bit x86 is considered the secondary architecture.

- Adding 64-bit ARM compute machines to a cluster that uses 64-bit x86 control plane machines and already includes 64-bit x86 compute machines. In this case, 64-bit ARM is considered the secondary architecture.

> [!NOTE]
> Before adding a secondary architecture node to your cluster, it is recommended to install the Multiarch Tuning Operator, and deploy a `ClusterPodPlacementConfig` custom resource. For more information, see "Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator".

# Installing a cluster with multi-architecture support

You can install a cluster with multi-architecture support to use compute machines with different Central Processing Unit (CPU) architectures. Modifying your configuration file helps ensure your control plane and worker nodes deploy with the correct architecture.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- You have the OpenShift Container Platform installation program.

- You downloaded the pull secret for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check that the `openshift-install` binary is using the `multi` payload by running the following command:

    ``` terminal
    $ ./openshift-install version
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ./openshift-install 4.20.0
    built from commit abc123etc
    release image quay.io/openshift-release-dev/ocp-release@sha256:abc123wxyzetc
    release architecture multi
    default architecture amd64
    ```

    </div>

    The output must contain `release architecture multi` to indicate that the `openshift-install` binary is using the `multi` payload.

2.  Update the `install-config.yaml` file to configure the architecture for the nodes.

    <div class="formalpara">

    <div class="title">

    Sample `install-config.yaml` file with multi-architecture configuration

    </div>

    ``` yaml
    apiVersion: v1
    baseDomain: example.openshift.com
    compute:
    - architecture: amd64
      hyperthreading: Enabled
      name: worker
      platform: {}
      replicas: 3
    controlPlane:
      architecture: arm64
      name: master
      platform: {}
      replicas: 3
    # ...
    ```

    </div>

    where:

    `compute.architecture`
    Specifies the architecture of the worker node. You can set this field to either `arm64` or `amd64`.

    `controlPlane.architecture`
    Specifies the control plane node architecture. You can set this field to either `arm64` or `amd64`.

</div>

<div>

<div class="title">

Next steps

</div>

- [Deploying the cluster](../ipi/installing-aws-localzone.md#installation-launching-installer_installing-aws-localzone)

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator](../../../post_installation_configuration/configuring-multi-arch-compute-machines/multiarch-tuning-operator.md#multiarch-tuning-operator)

</div>
