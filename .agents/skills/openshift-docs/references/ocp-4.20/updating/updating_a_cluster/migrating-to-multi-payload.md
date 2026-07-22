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

- [Selecting a cluster installation type](../../installing/overview/installing-preparing.md#installing-preparing-selecting-cluster-type)

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

# Migrating the x86 control plane to arm64 architecture on Microsoft Azure

You can migrate the control plane in your cluster from `x86` to `arm64` architecture on Microsoft Azure. Migrating to `arm64` control plane nodes can reduce cloud infrastructure costs and improve energy efficiency while maintaining the same cluster functionality.

Azure requires you to manually create a gallery image from the `arm64` Red Hat Enterprise Linux CoreOS (RHCOS) VHD before updating the control plane machine set.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You logged in to `oc` as a user with `cluster-admin` privileges.

- You have installed the Azure CLI (`az`).

- You are logged in to the Azure CLI with an account that has permissions to create resources in the cluster’s resource group.

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
    master-001.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
    master-002.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
    master-003.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
    ```

    </div>

    The `KERNEL-VERSION` field in the output indicates the architecture of the nodes.

2.  Check that your cluster is multi-architecture compatible by running the following command:

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

    If the value of the `release.openshift.io/architecture` field is not `multi`, migrate the cluster to a multi-architecture cluster. For more information, see "Migrating to a cluster with multi-architecture compute machines using the CLI".

3.  Update your image stream from single-architecture to multi-architecture by running the following command:

    ``` terminal
    $ oc import-image <multiarch_image_stream_tag>  --from=<registry>/<project_name>/<image_name> \
    --import-mode='PreserveOriginal'
    ```

4.  Set the infrastructure ID environment variable by running the following command:

    ``` terminal
    $ INFRA_ID=$(oc get infrastructure cluster -o jsonpath='{.status.infrastructureName}')
    ```

5.  Set the region environment variable by running the following command:

    ``` terminal
    $ REGION=$(oc get machines -n openshift-machine-api -o jsonpath='{.items[0].spec.providerSpec.value.location}')
    ```

6.  Set the resource group environment variable by running the following command:

    ``` terminal
    $ RESOURCE_GROUP="${INFRA_ID}-rg"
    ```

7.  Set the storage account name environment variable by running the following command:

    ``` terminal
    $ STORAGE_ACCOUNT_NAME=$(az storage account list --resource-group ${RESOURCE_GROUP} --query "[?ends_with(name, 'sa')].name" -o tsv)
    ```

8.  Set the gallery name environment variable by running the following command:

    ``` terminal
    $ GALLERY_NAME=$(az sig list --resource-group ${RESOURCE_GROUP} --query "[].name" -o tsv)
    ```

9.  Set the `arm64` RHCOS VHD URL environment variable by running the following command:

    ``` terminal
    $ VHD_URL=$(oc -n openshift-machine-config-operator get configmap/coreos-bootimages \
      -o jsonpath='{.data.stream}' | jq -r \
      '.architectures.aarch64."rhel-coreos-extensions"."azure-disk".url')
    ```

10. Set the VHD release environment variable by running the following command:

    ``` terminal
    $ VHD_RELEASE=$(oc -n openshift-machine-config-operator get configmap/coreos-bootimages \
      -o jsonpath='{.data.stream}' | jq -r \
      '.architectures.aarch64."rhel-coreos-extensions"."azure-disk".release')
    ```

11. Set the blob name environment variable by running the following command:

    ``` terminal
    $ BLOB_NAME="rhcos-${VHD_RELEASE}-azure.aarch64.vhd"
    ```

12. Set the storage account key environment variable by running the following command:

    ``` terminal
    $ ACCOUNT_KEY=$(az storage account keys list \
      -g ${RESOURCE_GROUP} \
      --account-name ${STORAGE_ACCOUNT_NAME} \
      --query "[0].value" -o tsv)
    ```

13. Copy the `arm64` RHCOS VHD to the cluster’s storage account by running the following command:

    ``` terminal
    $ az storage blob copy start \
      --account-name ${STORAGE_ACCOUNT_NAME} \
      --account-key "${ACCOUNT_KEY}" \
      --source-uri "${VHD_URL}" \
      --destination-blob "${BLOB_NAME}" \
      --destination-container vhd
    ```

14. Monitor the copy progress by running the following command:

    ``` terminal
    $ az storage blob show \
      -c vhd -n "${BLOB_NAME}" \
      --account-name ${STORAGE_ACCOUNT_NAME} \
      --account-key "${ACCOUNT_KEY}" \
      --query "{status:properties.copy.status, progress:properties.copy.progress}" \
      -o table
    ```

    Wait until the status shows `success`. The VHD is approximately 17 GB and the copy typically takes about 5 minutes.

15. Set the image definition name environment variable by running the following command:

    ``` terminal
    $ IMAGE_DEFINITION_NAME=$(az sig image-definition list \
      --resource-group ${RESOURCE_GROUP} \
      --gallery-name ${GALLERY_NAME} \
      --query "[?contains(name,'-gen2')].name" -o tsv \
      | sed 's/-gen2/-aarch64-gen2/')
    ```

16. Create an `arm64` image definition in the cluster’s shared image gallery by running the following command:

    ``` terminal
    $ az sig image-definition create \
      --resource-group ${RESOURCE_GROUP} \
      --gallery-name ${GALLERY_NAME} \
      --gallery-image-definition ${IMAGE_DEFINITION_NAME} \
      --publisher RedHat-gen2 \
      --offer rhcos-aarch64-gen2 \
      --sku gen2 \
      --os-type Linux \
      --architecture Arm64 \
      --hyper-v-generation V2 \
      -l ${REGION}
    ```

17. Set the RHCOS VHD URL environment variable for the copied blob by running the following command:

    ``` terminal
    $ RHCOS_VHD_URL=$(az storage blob url \
      --account-name ${STORAGE_ACCOUNT_NAME} \
      -c vhd -n "${BLOB_NAME}" -o tsv)
    ```

18. Create a gallery image version from the copied VHD by running the following command:

    ``` terminal
    $ az sig image-version create \
      --resource-group ${RESOURCE_GROUP} \
      --gallery-name ${GALLERY_NAME} \
      --gallery-image-definition ${IMAGE_DEFINITION_NAME} \
      --gallery-image-version 1.0.0 \
      --os-vhd-storage-account ${STORAGE_ACCOUNT_NAME} \
      --os-vhd-uri ${RHCOS_VHD_URL} \
      -l ${REGION}
    ```

19. Set the resource ID environment variable for the newly created image version by running the following command:

    ``` terminal
    $ RESOURCE_ID="/$(az sig image-version show \
      --resource-group ${RESOURCE_GROUP} \
      --gallery-name ${GALLERY_NAME} \
      --gallery-image-definition ${IMAGE_DEFINITION_NAME} \
      --gallery-image-version 1.0.0 \
      --query id -o tsv | cut -d'/' -f4-)"
    ```

20. Update the control plane machine set to use the `arm64` image and an ARM-compatible VM size by running the following command:

    ``` terminal
    $ oc patch controlplanemachineset.machine.openshift.io cluster \
      --type=json \
      -p "[
        {\"op\": \"replace\", \"path\": \"/spec/template/machines_v1beta1_machine_openshift_io/spec/providerSpec/value/image/resourceID\", \"value\": \"${RESOURCE_ID}\"},
        {\"op\": \"replace\", \"path\": \"/spec/template/machines_v1beta1_machine_openshift_io/spec/providerSpec/value/vmSize\", \"value\": \"<arm64_vm_size>\"}
      ]" \
      -n openshift-machine-api
    ```

    Replace `<arm64_vm_size>` with an ARM-compatible VM size, such as `Standard_D8ps_v6`. The `ps` suffix in Azure VM sizes denotes Ampere Arm-based processors. For information about supported instance types, see "Tested instance types for Azure on 64-bit ARM infrastructures".

    For clusters that use the default `RollingUpdate` update strategy, the control plane machine set propagates changes to your control plane configuration automatically. The full rollout typically takes approximately 55 minutes for a 3-node control plane. During the rollout, `etcd` may report transient `Degraded` or `Progressing` conditions, which resolve after all control plane nodes are replaced.

    For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

    > [!NOTE]
    > If a replacement machine fails with an "instance missing" error, delete the failed machine to allow the control plane machine set to retry the replacement.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the control plane nodes are running on the `arm64` architecture by running the following command:

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

- [Control plane configuration options for Microsoft Azure](../../machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.md#cpmso-config-options-azure)

- [Tested instance types for Azure on 64-bit ARM infrastructures](../../installing/installing_azure/ipi/installing-azure-customizations.md#installation-azure-arm-tested-machine-types_installing-azure-customizations)

- [Migrating to a cluster with multi-architecture compute machines using the CLI](migrating-to-multi-payload.md#migrating-to-multi-arch-cli_updating-clusters-overview)

</div>
