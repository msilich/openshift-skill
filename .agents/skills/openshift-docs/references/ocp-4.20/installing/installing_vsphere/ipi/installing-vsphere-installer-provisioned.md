<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform version 4.17, you can install a cluster on your VMware vSphere instance by using installer-provisioned infrastructure.

# Prerequisites

- You have completed the tasks in "Preparing to install a cluster using installer-provisioned infrastructure".

- You reviewed your VMware platform licenses. Red Hat does not place any restrictions on your VMware licenses, but some VMware infrastructure components require licensing.

- You reviewed details about the OpenShift Container Platform installation and update processes.

- You read the documentation on selecting a cluster installation method and preparing it for users.

- You provisioned persistent storage for your cluster. To deploy a private image registry, your storage must provide `ReadWriteMany` access modes.

- The OpenShift Container Platform installer requires access to port 443 on the vCenter and ESXi hosts. You verified that port 443 is accessible.

- If you use a firewall, you confirmed with the administrator that port 443 is accessible. Control plane nodes must be able to reach vCenter and ESXi hosts on port 443 for the installation to succeed.

- If you use a firewall, you configured it to allow the sites that your cluster requires access to.

  > [!NOTE]
  > Be sure to also review this site list if you are configuring a proxy.

# Internet access for OpenShift Container Platform

In OpenShift Container Platform 4.17, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

- Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.

- Access Quay.io to obtain the packages that are required to install your cluster.

- Obtain the packages that are required to perform cluster updates.

> [!IMPORTANT]
> If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

# Deploying the cluster

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

> [!IMPORTANT]
> You can run the `create cluster` command of the installation program only once, during initial installation.

<div>

<div class="title">

Prerequisites

</div>

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

- You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

- Optional: Before you create the cluster, you configured an external load balancer in place of the default load balancer.

  > [!IMPORTANT]
  > You do not need to specify API and Ingress static addresses for your installation program. If you choose this configuration, you must take additional actions to define network targets that accept an IP address from each referenced vSphere subnet. See the section "Configuring a user-managed load balancer".

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the directory that contains the installation program, initialize the cluster deployment by running the following command:

    ``` terminal
    $ ./openshift-install create cluster --dir <installation_directory> \
        --log-level=info
    ```

    - For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

    - To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

    When specifying the directory:

    - Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.

    - Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

2.  Provide values at the prompts:

    1.  Optional: Select an SSH key to use to access your cluster machines.

        > [!NOTE]
        > For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

    2.  Select **vsphere** as the platform to target.

    3.  Specify the name of your vCenter instance.

    4.  Specify the user name and password for the vCenter account that has the required permissions to create the cluster.

        The installation program connects to your vCenter instance.

        > [!IMPORTANT]
        > Some VMware vCenter Single Sign-On (SSO) environments with Active Directory (AD) integration might primarily require you to use the traditional login method, which requires the `<domain>\` construct.
        >
        > To ensure that vCenter account permission checks complete properly, consider using the User Principal Name (UPN) login method, such as `<username>@<fully_qualified_domainname>`.

    5.  Select the data center in your vCenter instance to connect to.

    6.  Select the default vCenter datastore to use.

        > [!NOTE]
        > Datastore and cluster names cannot exceed 60 characters; therefore, ensure the combined string length does not exceed the 60 character limit.

    7.  Select the vCenter cluster to install the OpenShift Container Platform cluster in. The installation program uses the root resource pool of the vSphere cluster as the default resource pool.

    8.  Select the network in the vCenter instance that contains the virtual IP addresses and DNS records that you configured.

    9.  Enter the virtual IP address that you configured for control plane API access.

    10. Enter the virtual IP address that you configured for cluster ingress.

    11. Enter the base domain. This base domain must be the same one that you used in the DNS records that you configured.

    12. Enter a descriptive name for your cluster. The cluster name must be the same one that you used in the DNS records that you configured.

        > [!NOTE]
        > Datastore and cluster names cannot exceed 60 characters; therefore, ensure the combined string length does not exceed the 60 character limit.

    13. Paste the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret).

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

When the cluster deployment completes successfully:

</div>

- The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.

- Credential information also outputs to `<installation_directory>/.openshift_install.log`.

  > [!IMPORTANT]
  > Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  ...
  INFO Install complete!
  INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
  INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
  INFO Login to the console with user: "kubeadmin", and password: "password"
  INFO Time elapsed: 36m22s
  ```

  </div>

  <div class="important">

  <div class="title">

  </div>

  - The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.

  - It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

  </div>

# Logging in to the cluster by using the CLI

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and is created during OpenShift Container Platform installation.

<div>

<div class="title">

Prerequisites

</div>

- You deployed an OpenShift Container Platform cluster.

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Export the `kubeadmin` credentials by running the following command:

    ``` terminal
    $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
    ```

    where:

    `<installation_directory>`
    Specifies the path to the directory that stores the installation files.

2.  Verify you can run `oc` commands successfully using the exported configuration by running the following command:

    ``` terminal
    $ oc whoami
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    system:admin
    ```

    </div>

</div>

<div>

<div class="title">

Next steps

</div>

- "Customize your cluster"

- "Remote health reporting"

</div>

# Image registry removed during installation

On platforms that do not provide shareable object storage, the OpenShift Image Registry Operator bootstraps itself as `Removed`. This allows `openshift-installer` to complete installations on these platform types.

After installation, you must edit the Image Registry Operator configuration to switch the `managementState` from `Removed` to `Managed`. When this has completed, you must configure storage.

# Image registry storage configuration

The Image Registry Operator is not initially available for platforms that do not provide default storage. After installation, you must configure your registry to use storage so that the Registry Operator is made available.

Configure a persistent volume, which is required for production clusters. Where applicable, you can configure an empty directory as the storage location for non-production clusters.

You can also allow the image registry to use block storage types by using the `Recreate` rollout strategy during upgrades.

## Configuring registry storage for VMware vSphere

As a cluster administrator, following installation you must configure your registry to use storage.

<div>

<div class="title">

Prerequisites

</div>

- Cluster administrator permissions.

- A cluster on VMware vSphere.

- Persistent storage provisioned for your cluster, such as Red Hat OpenShift Data Foundation.

  > [!IMPORTANT]
  > OpenShift Container Platform supports `ReadWriteOnce` access for image registry storage when you have only one replica. `ReadWriteOnce` access also requires that the registry uses the `Recreate` rollout strategy. To deploy an image registry that supports high availability with two or more replicas, `ReadWriteMany` access is required.

- Must have "100Gi" capacity.

</div>

> [!IMPORTANT]
> Testing shows issues with using the NFS server on RHEL as storage backend for core services. This includes the OpenShift Container Registry and Quay, Prometheus for monitoring storage, and Elasticsearch for logging storage. Therefore, using RHEL NFS to back PVs used by core services is not recommended.
>
> Other NFS implementations on the marketplace might not have these issues. Contact the individual NFS implementation vendor for more information on any testing that was possibly completed against these OpenShift Container Platform core components.

<div>

<div class="title">

Procedure

</div>

1.  Change the `spec.storage.pvc` field in the `configs.imageregistry/cluster` resource.

    > [!NOTE]
    > When you use shared storage, review your security settings to prevent outside access.

2.  Verify that you do not have a registry pod by running the following command:

    ``` terminal
    $ oc get pod -n openshift-image-registry -l docker-registry=default
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    No resourses found in openshift-image-registry namespace
    ```

    </div>

    > [!NOTE]
    > If you do have a registry pod in your output, you do not need to continue with this procedure.

3.  Check the registry configuration by running the following command:

    ``` terminal
    $ oc edit configs.imageregistry.operator.openshift.io
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    storage:
      pvc:
        claim:
    ```

    </div>

    Leave the `claim` field blank to allow the automatic creation of an `image-registry-storage` persistent volume claim (PVC). The PVC is generated based on the default storage class. However, be aware that the default storage class might provide ReadWriteOnce (RWO) volumes, such as a RADOS Block Device (RBD), which can cause issues when you replicate to more than one replica.

4.  Check the `clusteroperator` status by running the following command:

    ``` terminal
    $ oc get clusteroperator image-registry
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME             VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
    image-registry   4.7       True        False         False      6h50m
    ```

    </div>

</div>

## Configuring block registry storage for VMware vSphere

To allow the image registry to use block storage types such as vSphere Virtual Machine Disk (VMDK) during upgrades as a cluster administrator, you can use the `Recreate` rollout strategy.

> [!IMPORTANT]
> Block storage volumes are supported but not recommended for use with image registry on production clusters. An installation where the registry is configured on block storage is not highly available because the registry cannot have more than one replica.

<div>

<div class="title">

Procedure

</div>

1.  Enter the following command to set the image registry storage as a block storage type, patch the registry so that it uses the `Recreate` rollout strategy, and runs with only `1` replica:

    ``` terminal
    $ oc patch config.imageregistry.operator.openshift.io/cluster --type=merge -p '{"spec":{"rolloutStrategy":"Recreate","replicas":1}}'
    ```

2.  Provision the persistent volume (PV) for the block storage device, and create a persistent volume claim (PVC) for that volume. The requested block volume uses the ReadWriteOnce (RWO) access mode.

    1.  Create a `pvc.yaml` file with the following contents to define a VMware vSphere `PersistentVolumeClaim` object:

        ``` yaml
        kind: PersistentVolumeClaim
        apiVersion: v1
        metadata:
          name: image-registry-storage
          namespace: openshift-image-registry
        spec:
          accessModes:
          - ReadWriteOnce
          resources:
            requests:
              storage: 100Gi
        ```

        where:

</div>

`metadata.name`
Specifies a unique name that represents the `PersistentVolumeClaim` object.

`metadata.namespace`
Specifies the `namespace` for the `PersistentVolumeClaim` object, which is `openshift-image-registry`.

`spec.accessModes`
Specifies the access mode of the persistent volume claim. With `ReadWriteOnce`, the volume can be mounted with read and write permissions by a single node.

`spec.resources.requests.storage`
Specifies the size of the persistent volume claim.

1.  Enter the following command to create the `PersistentVolumeClaim` object from the file:

    ``` terminal
    $ oc create -f pvc.yaml -n openshift-image-registry
    ```

    1.  Enter the following command to edit the registry configuration so that it references the correct PVC:

        ``` terminal
        $ oc edit config.imageregistry.operator.openshift.io -o yaml
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` yaml
        storage:
          pvc:
            claim:
        ```

        </div>

        By creating a custom PVC, you can leave the `claim` field blank for the default automatic creation of an `image-registry-storage` PVC.

<div>

<div class="title">

Additional resources

</div>

- [Configuring the registry for vSphere](../../../registry/configuring_registry_storage/configuring-registry-storage-vsphere.md#registry-configuring-storage-vsphere_configuring-registry-storage-vsphere)

</div>

# Telemetry access for OpenShift Container Platform

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

<div>

<div class="title">

Additional resources

</div>

- [Preparing to install a cluster using installer-provisioned infrastructure](ipi-vsphere-preparing-to-install.md#ipi-vsphere-preparing-to-install)

- [OpenShift Container Platform installation and update processes](../../../architecture/architecture-installation.md#architecture-installation)

- [Selecting a cluster installation method and preparing it for users](../../overview/installing-preparing.md#installing-preparing)

- [Persistent storage](../../../storage/understanding-persistent-storage.md#understanding-persistent-storage)

- [Configuring your firewall to allow required sites](../../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall)

- [About remote health monitoring](../../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring)

- [Customize your cluster](../../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations)

- [Remote health reporting](../../../support/remote_health_monitoring/remote-health-reporting.md#remote-health-reporting)

- [Set up your registry and configure registry storage](../../../registry/configuring_registry_storage/configuring-registry-storage-vsphere.md#configuring-registry-storage-vsphere)

- [View the events from the vSphere Problem Detector Operator to determine if the cluster has permission or storage configuration issues](../using-vsphere-problem-detector-operator.md#vsphere-problem-detector-viewing-events_vsphere-problem-detector)

</div>
