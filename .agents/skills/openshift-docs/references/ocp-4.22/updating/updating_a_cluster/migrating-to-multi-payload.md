<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can migrate your current cluster with single-architecture compute machines to a cluster with multi-architecture compute machines by updating to a multi-architecture, manifest-listed payload. This allows you to add mixed architecture compute nodes to your cluster.

For information about configuring your multi-architecture compute machines, see "Configuring multi-architecture compute machines on an OpenShift Container Platform cluster".

Before migrating your single-architecture cluster to a cluster with multi-architecture compute machines, it is recommended to install the Multiarch Tuning Operator, and deploy a `ClusterPodPlacementConfig` custom resource. For more information, see [Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator](../../post_installation_configuration/configuring-multi-arch-compute-machines/multiarch-tuning-operator.md#multiarch-tuning-operator).

> [!IMPORTANT]
> Migration from a multi-architecture payload to a single-architecture payload is not supported. Once a cluster has transitioned to using a multi-architecture payload, it can no longer accept a single-architecture update payload.

# Migrating to a cluster with multi-architecture compute machines using the CLI

You can use the OpenShift CLI (`oc`) to migrate to a cluster with multi-architecture compute machines.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- Your OpenShift Container Platform version is 4.13.0 or later.

  For more information on how to update your cluster version, see "Updating a cluster using the web console" or "Updating a cluster using the CLI".

- You have installed the OpenShift CLI (`oc`) that matches the version for your current cluster.

- Your `oc` client is updated to version 4.13.0 or later.

- Your OpenShift Container Platform cluster is installed on AWS, Azure, Google Cloud, bare metal, or IBM P/Z platforms.

  For more information on selecting a supported platform for your cluster installation, see "Selecting a cluster installation type".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the `RetrievedUpdates` condition is `True` in the Cluster Version Operator (CVO) by running the following command:

    ``` terminal
    $ oc get clusterversion/version -o=jsonpath="{.status.conditions[?(.type=='RetrievedUpdates')].status}"
    ```

    If the `RetrievedUpates` condition is `False`, you can find supplemental information regarding the failure by using the following command:

    ``` terminal
    $ oc adm upgrade
    ```

    For more information about cluster version condition types, see "Understanding cluster version condition types".

2.  If the condition `RetrievedUpdates` is `False`, change the channel to `stable-<4.y>` or `fast-<4.y>` by running the following command:

    ``` terminal
    $ oc adm upgrade channel <channel>
    ```

    After setting the channel, verify if `RetrievedUpdates` is `True`.

    For more information about channels, see "Understanding update channels and releases".

3.  Migrate to the multi-architecture payload by running the following command:

    ``` terminal
    $ oc adm upgrade --to-multi-arch
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Monitor the migration by running the following command:

  ``` terminal
  $ oc adm upgrade
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  working towards ${VERSION}: 106 of 841 done (12% complete), waiting on machine-config
  ```

  </div>

  > [!IMPORTANT]
  > Machine launches may fail as the cluster settles into the new state. To notice and recover when machines fail to launch, it is recommended that you deploy machine health checks. For more information about machine health checks and how to deploy them, see "About machine health checks".

  1.  Optional: Retrieve more detailed information about the status of your update and monitor the migration by running the following command:

      ``` terminal
      $ oc adm upgrade status
      ```

      For more information about how to use the `oc adm upgrade status` command, see "Gathering cluster update status using oc adm upgrade status (Technology Preview)".

</div>

The migrations must be complete and all the cluster operators must be stable before you can add compute machine sets with different architectures to your cluster.

<div>

<div class="title">

Additional resources

</div>

- [Configuring multi-architecture compute machines on an OpenShift Container Platform cluster](../../post_installation_configuration/configuring-multi-arch-compute-machines/multi-architecture-configuration.md#multi-architecture-configuration)

- [Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator](../../post_installation_configuration/configuring-multi-arch-compute-machines/multiarch-tuning-operator.md#multiarch-tuning-operator)

- [Updating a cluster using the web console](updating-cluster-web-console.md#updating-cluster-web-console)

- [Updating a cluster using the CLI](updating-cluster-cli.md#updating-cluster-cli)

- [Understanding cluster version condition types](../understanding_updates/intro-to-updates.md#understanding-clusterversion-conditiontypes_understanding-openshift-updates)

- [Understanding update channels and releases](../understanding_updates/understanding-update-channels-release.md#understanding-update-channels-releases)

- [Selecting a cluster installation type](../../installing/overview/installing-preparing.md#installing-preparing-selecting-cluster-type_installing-preparing)

- [About machine health checks](../../machine_management/deploying-machine-health-checks.md#machine-health-checks-about_deploying-machine-health-checks)

</div>

# Migrating the x86 control plane to arm64 architecture on Amazon Web Services

You can migrate the control plane in your cluster from `x86` to `arm64` architecture on Amazon Web Services (AWS).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You logged in to `oc` as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check the architecture of the control plane nodes by running the following command:

    ``` terminal
    $ oc get nodes -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                          STATUS   ROLES                  AGE    VERSION   INTERNAL-IP EXTERNAL-IP   OS-IMAGE                                         KERNEL-VERSION                 CONTAINER-RUNTIME
    worker-001.example.com        Ready    worker                 100d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
    worker-002.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
    worker-003.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
    master-001.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
    master-002.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
    master-003.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
    ```

    </div>

    The `KERNEL-VERSION` field in the output indicates the architecture of the nodes.

2.  Check that your cluster uses the multi payload by running the following command:

    ``` terminal
    $ oc adm release info -o jsonpath="{ .metadata.metadata}"
    ```

    If you see the following output, the cluster is multi-architecture compatible.

    ``` terminal
    {
     "release.openshift.io/architecture": "multi",
     "url": "https://access.redhat.com/errata/<errata_version>"
    }
    ```

    If the cluster is not using the multi payload, migrate the cluster to a multi-architecture cluster. For more information, see "Migrating to a cluster with multi-architecture compute machines using the CLI".

3.  Update your image stream from single-architecture to multi-architecture by running the following command:

    ``` terminal
    $ oc import-image <multiarch_image_stream_tag>  --from=<registry>/<project_name>/<image_name> \
    --import-mode='PreserveOriginal'
    ```

4.  Get the `arm64` compatible Amazon Machine Image (AMI) for configuring the control plane machine set by running the following command:

    ``` terminal
    $ oc get configmap/coreos-bootimages -n openshift-machine-config-operator -o jsonpath='{.data.stream}' | jq -r '.architectures.aarch64.images.aws.regions."<aws_region>".image'
    ```

    Replace `<aws_region>` with the AWS region where the current cluster is installed. You can get the AWS region for the installed cluster by running the following command:

    ``` terminal
    $ oc get infrastructure cluster -o jsonpath='{.status.platformStatus.aws.region}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ami-xxxxxxx
    ```

    </div>

5.  Update the control plane machine set to support the `arm64` architecture by running the following command:

    ``` terminal
    $ oc edit controlplanemachineset.machine.openshift.io cluster -n openshift-machine-api
    ```

    1.  Update the `instanceType` field to a type that supports the `arm64` architecture, and set the `ami.id` field to an AMI that is compatible with the `arm64` architecture. For information about supported instance types, see "Tested instance types for AWS on 64-bit ARM infrastructures".

        For more information about configuring the control plane machine set for AWS, see "Control plane configuration options for Amazon Web Services".

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the control plane nodes are now running on the `arm64` architecture by running the following command:

  ``` terminal
  $ oc get nodes -o wide
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                          STATUS   ROLES                  AGE    VERSION   INTERNAL-IP EXTERNAL-IP   OS-IMAGE                                         KERNEL-VERSION                 CONTAINER-RUNTIME
  worker-001.example.com        Ready    worker                 100d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
  worker-002.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
  worker-003.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
  master-001.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.aarch64   cri-o://1.30.x
  master-002.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.aarch64   cri-o://1.30.x
  master-003.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.aarch64   cri-o://1.30.x
  ```

  </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Control plane configuration options for Amazon Web Services](../../machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.md#cpmso-config-options-aws)

- [Tested instance types for AWS on 64-bit ARM infrastructures](../../installing/installing_aws/upi/upi-aws-installation-reqs.md#installation-aws-arm-tested-machine-types_upi-aws-installation-reqs)

- [Migrating to a cluster with multi-architecture compute machines using the CLI](migrating-to-multi-payload.md#migrating-to-multi-arch-cli_updating-clusters-overview)

</div>

# Migrating control plane or infra machine sets between architectures on Google Cloud

You can migrate the control plane or infra machine sets in your Google Cloud cluster between `x86` and `arm64` architectures.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You logged in to `oc` as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check the architecture of the control plane or infra nodes by running the following command:

    ``` terminal
    $ oc get nodes -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                          STATUS   ROLES                  AGE    VERSION   INTERNAL-IP EXTERNAL-IP   OS-IMAGE                                         KERNEL-VERSION                 CONTAINER-RUNTIME
    worker-001.example.com        Ready    infra                  100d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
    master-001.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
    ```

    </div>

    The `KERNEL-VERSION` field in the output indicates the architecture of the nodes.

2.  Check that your cluster uses the multi payload by running the following command:

    ``` terminal
    $ oc adm release info -o jsonpath="{ .metadata.metadata}"
    ```

    If you see the following output, the cluster is multi-architecture compatible.

    ``` terminal
    {
     "release.openshift.io/architecture": "multi",
     "url": "https://access.redhat.com/errata/<errata_version>"
    }
    ```

    If the cluster is not using the multi payload, migrate the cluster to a multi-architecture cluster. For more information, see "Migrating to a cluster with multi-architecture compute machines".

3.  If you use any custom image streams, update them from single-architecture to multi-architecture by running the following command for each image stream:

    ``` terminal
    $ oc import-image <multiarch_image_stream_tag>  --from=<registry>/<project_name>/<image_name> \
    --import-mode='PreserveOriginal'
    ```

4.  Select an instance type that matches the target architecture from [General-purpose machine family for Compute engine](https://cloud.google.com/compute/docs/general-purpose-machines) (Google documentation). Check the [Available regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) table (Google documentation) to verify that the instance type is supported in your zone.

5.  Select a supported disk type for the instance type that you selected from the "Supported disk types" section of [General-purpose machine family for Compute engine](https://cloud.google.com/compute/docs/general-purpose-machines) (Google documentation).

6.  Determine the Google Cloud image that the machine set uses after migration by running the following command:

    ``` terminal
    $ oc get configmap/coreos-bootimages \
      -n openshift-machine-config-operator \
      -o jsonpath='{.data.stream}' | jq \
      -r '.architectures.aarch64.images.gcp'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    "gcp": {
        "release": "415.92.202309142014-0",
        "project": "rhcos-cloud",
        "name": "rhcos-415-92-202309142014-0-gcp-aarch64"
      }
    ```

    </div>

    Use the `project` and `name` parameters from the output to form the `image` parameter in the following format: `projects/<project>/global/images/<name>`.

7.  To migrate the control plane to another architecture, run the following command:

    ``` terminal
    $ oc edit controlplanemachineset.machine.openshift.io cluster -n openshift-machine-api
    ```

    1.  Replace the `disks.type` parameter with the disk type that you selected.

    2.  Replace the `disks.image` parameter with the `image` parameter that you formed previously.

    3.  Replace the `machineType` parameter with the instance type that you selected.

8.  To migrate an infra machine set to another architecture, run the following command using the ID of an infra machine set:

    ``` terminal
    $ oc edit machineset <infra-machine-set_id> -n openshift-machine-api
    ```

    1.  Replace the `disks.type` parameter with the disk type that you selected.

    2.  Replace the `disks.image` parameter with the `image` parameter that you formed previously.

    3.  Replace the `machineType` parameter with the instance type that you selected.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Tested instance types for Google Cloud on 64-bit ARM infrastructures](../../installing/installing_gcp/installing-gcp-customizations.md#installation-gcp-tested-machine-types-arm_installing-gcp-customizations)

- [Migrating to a cluster with multi-architecture compute machines using the CLI](migrating-to-multi-payload.md#migrating-to-multi-arch-cli_updating-clusters-overview)

</div>
