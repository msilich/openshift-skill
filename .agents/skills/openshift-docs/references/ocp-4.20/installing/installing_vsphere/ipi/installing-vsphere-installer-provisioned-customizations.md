<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform version 4.17, you can install a cluster on your VMware vSphere instance by using installer-provisioned infrastructure with customizations, including network configuration options. In each, you modify parameters in the `install-config.yaml` file before you install the cluster.

By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations.

You must set most of the network configuration parameters during installation, and you can modify only `kubeProxy` configuration parameters in a running cluster.

# Prerequisites

- You have completed the tasks in [Preparing to install a cluster using installer-provisioned infrastructure](ipi-vsphere-preparing-to-install.md#ipi-vsphere-preparing-to-install).

- You reviewed your vSphere platform licenses. Red Hat does not place any restrictions on your vSphere licenses, but some vSphere infrastructure components require licensing.

- You reviewed details about the [OpenShift Container Platform installation and update](../../../architecture/architecture-installation.md#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../../overview/installing-preparing.md#installing-preparing).

- You provisioned [persistent storage](../../../storage/understanding-persistent-storage.md#understanding-persistent-storage) for your cluster. To deploy a private image registry, your storage must provide `ReadWriteMany` access modes.

- The OpenShift Container Platform installer requires access to port 443 on the vCenter and ESXi hosts. You verified that port 443 is accessible.

- If you use a firewall, you confirmed with the administrator that port 443 is accessible. Control plane nodes must be able to reach vCenter and ESXi hosts on port 443 for the installation to succeed.

- If you use a firewall, you [configured it to allow the sites](../../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall) that your cluster requires access to.

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

# VMware vSphere region and zone enablement

You can deploy an OpenShift Container Platform cluster to multiple vSphere data centers. Each data center can run multiple clusters. This configuration reduces the risk of a hardware failure or network outage that can cause your cluster to fail.

To enable regions and zones, you must define multiple failure domains for your OpenShift Container Platform cluster.

> [!IMPORTANT]
> The VMware vSphere region and zone enablement feature requires the vSphere Container Storage Interface (CSI) driver as the default storage driver in the cluster. As a result, the feature is only available on a newly installed cluster.
>
> For a cluster that was upgraded from a previous release, you must enable CSI automatic migration for the cluster. You can then configure multiple regions and zones for the upgraded cluster.

The default installation configuration deploys a cluster to a single vSphere data center. If you want to deploy a cluster to multiple vSphere data centers, you must create an installation configuration file that enables the region and zone feature.

The default `install-config.yaml` file includes `vcenters` and `failureDomains` fields, where you can specify multiple vSphere data centers and clusters for your OpenShift Container Platform cluster. You can use the default `failureDomains` from `install-config.yaml` if you want to install an OpenShift Container Platform cluster in a vSphere environment that consists of single data center.

The following list describes terms associated with defining zones and regions for your cluster:

- Failure domain: Establishes the relationships between a region and zone. You define a failure domain by using vCenter objects, such as a `datastore` object. A failure domain defines the vCenter location for OpenShift Container Platform cluster nodes.

- Region: Specifies a vCenter data center. You define a region by using a tag from the `openshift-region` tag category.

- Zone: Specifies a vCenter cluster. You define a zone by using a tag from the `openshift-zone` tag category.

> [!NOTE]
> If you plan on specifying more than one failure domain in your `install-config.yaml` file, you must create tag categories, zone tags, and region tags in advance of creating the configuration file.

You must create a vCenter tag for each vCenter data center, which represents a region. Additionally, you must create a vCenter tag for each cluster than runs in a data center, which represents a zone. After you create the tags, you must attach each tag to their respective data centers and clusters.

The following table outlines an example of the relationship among regions, zones, and tags for a configuration with multiple vSphere data centers running in a single VMware vCenter.

| Data center (region) | Cluster (zone) | Tags       |
|----------------------|----------------|------------|
| us-east              | us-east-1      | us-east-1a |
| us-east-1b           |                |            |
| us-east-2            | us-east-2a     |            |
| us-east-2b           |                |            |
| us-west              | us-west-1      | us-west-1a |
| us-west-1b           |                |            |
| us-west-2            | us-west-2a     |            |
| us-west-2b           |                |            |

# VMware vSphere host group enablement

> [!IMPORTANT]
> OpenShift zones support for vSphere host groups is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

When deploying an OpenShift Container Platform cluster to VMware vSphere, you can map your vSphere host groups onto OpenShift Container Platform failure domains. This is useful if you are using a stretched cluster configuration, where ESXi hosts are grouped into host groups by physical location.

To enable this feature, you must meet the following requirements:

- You must arrange your ESXi hosts into host groups.

- You must create a vCenter tag in the `openshift-region` tag category for your cluster. After you create the tag, you must attach the tag to the cluster.

- You must create a vCenter tag in the `openshift-zone` tag category for each host group and then attach the correct tag to each ESXi host.

- You must define multiple failure domains for your OpenShift Container Platform cluster in the `install-config.yaml` file.

- You must grant the `Host.Inventory.EditCluster` privilege on the vSphere vCenter cluster object.

- You must include the following parameters in your `install-config.yaml` file to enable this Technology Preview feature:

  ``` yaml
  featureSet: TechPreviewNoUpgrade
  featureGate:
    - "VSphereHostVMGroupZonal=true"
  ```

  > [!NOTE]
  > For further information on feature gates, see "Enabling features using feature gates".

Review the following key terms, which correspond to parameters in your `install-config.yaml` file that you must configure to enable this feature:

- Failure domain: Specifies the relationships between regions and zones in OpenShift Container Platform, and clusters and host groups in vSphere. You define a failure domain by using vCenter objects, such as a `datastore` object. A failure domain defines the vCenter location for OpenShift Container Platform cluster nodes.

- Region: Specifies a vCenter cluster. You define a region by using a tag from the `openshift-region` tag category.

- Zone: Specifies a vCenter host group. You define a zone by using a tag from the `openshift-zone` tag category.

- Region type: Specifies the `ComputeCluster` region type to enable this feature.

- Zone type: Specifies the `HostGroup` zone type to enable this feature.

<div>

<div class="title">

Additional resources

</div>

- [Additional VMware vSphere configuration parameters](../installation-config-parameters-vsphere.md#installation-configuration-parameters-additional-vsphere_installation-config-parameters-vsphere)

- [Deprecated VMware vSphere configuration parameters](../installation-config-parameters-vsphere.md#deprecated-parameters-vsphere_installation-config-parameters-vsphere)

- [vSphereautomatic migration](../../../storage/container_storage_interface/persistent-storage-csi-migration.md#persistent-storage-csi-migration-sc-vsphere_persistent-storage-csi-migration)

- [VMware vSphere CSI Driver Operator](../../../storage/container_storage_interface/persistent-storage-csi-vsphere.md#persistent-storage-csi-vsphere-top-aware_persistent-storage-csi-vsphere)

- [Enabling features using feature gates](../../../nodes/clusters/nodes-cluster-enabling-features.md#nodes-cluster-enabling-features)

</div>

# Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on VMware vSphere.

<div>

<div class="title">

Prerequisites

</div>

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `install-config.yaml` file.

    1.  Change to the directory that contains the installation program and run the following command:

        ``` terminal
        $ ./openshift-install create install-config --dir <installation_directory>
        ```

        - `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

          When specifying the directory:

        - Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.

        - Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

    2.  At the prompts, provide the configuration details for your cloud:

        1.  Optional: Select an SSH key to use to access your cluster machines.

            > [!NOTE]
            > For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

        2.  Select **vsphere** as the platform to target.

        3.  Specify the name of your vCenter instance.

        4.  Specify the user name and password for the vCenter account that has the required permissions to create the cluster.

            The installation program connects to your vCenter instance.

        5.  Select the data center in your vCenter instance to connect to.

            > [!NOTE]
            > After you create the installation configuration file, you can modify the file to create a multiple vSphere data center environment. This means that you can deploy an OpenShift Container Platform cluster to multiple vSphere data centers. For more information about creating this environment, see the section named *VMware vSphere region and zone enablement*.

        6.  Select the default vCenter datastore to use.

            > [!WARNING]
            > You can specify the path of any datastore that exists in a datastore cluster. By default, Storage Distributed Resource Scheduler (SDRS), which uses Storage vMotion, is automatically enabled for a datastore cluster. Red Hat does not support Storage vMotion, so you must disable Storage DRS to avoid data loss issues for your OpenShift Container Platform cluster.
            >
            > You cannot specify more than one datastore path. If you must specify VMs across multiple datastores, use a `datastore` object to specify a failure domain in your cluster’s `install-config.yaml` configuration file. For more information, see "VMware vSphere region and zone enablement".

        7.  Select the vCenter cluster to install the OpenShift Container Platform cluster in. The installation program uses the root resource pool of the vSphere cluster as the default resource pool.

        8.  Select the network in the vCenter instance that contains the virtual IP addresses and DNS records that you configured.

        9.  Enter the virtual IP address that you configured for control plane API access.

        10. Enter the virtual IP address that you configured for cluster ingress.

        11. Enter the base domain. This base domain must be the same one that you used in the DNS records that you configured.

        12. Enter a descriptive name for your cluster.

            The cluster name you enter must match the cluster name you specified when configuring the DNS records.

2.  Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.

    > [!NOTE]
    > If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that the cluster’s control planes are schedulable. For more information, see "Installing a three-node cluster on vSphere".

3.  Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

    > [!IMPORTANT]
    > The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installation configuration parameters](../installation-config-parameters-vsphere.md#installation-config-parameters-vsphere)

</div>

## Sample install-config.yaml file for a VMware vSphere cluster

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or change the values of the required parameters.

> [!IMPORTANT]
> Carefully review the "Installation configuration parameters for vSphere" page for detailed parameter explanations.

``` yaml
apiVersion: v1
baseDomain: example.com
metadata:
  name: test
sshKey: ssh-ed25519 AAAA...
compute:
- name:  <worker_name>
  platform: {}
  replicas: 3
controlPlane:
  name: <control_plane_name>
  platform: {}
  replicas: 3
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  vsphere:
    apiVIPs:
    - 10.0.0.1
    ingressVIPs:
    - 10.0.0.2
    failureDomains:
    - name: <failure_domain_name>
      region: <default_region_name>
      server: <fully_qualified_domain_name>
      topology:
        computeCluster: "/<data_center>/host/<cluster>"
        datacenter: <data_center>
        datastore: "/<data_center>/datastore/<datastore>"
        networks:
        - <VM_Network_name>
      zone: <default_zone_name>
    vcenters:
    - datacenters:
      - <data_center>
      server: <fully_qualified_domain_name>
      user: administrator@vsphere.local
```

where:

`compute`
Specifes the parameters that apply to compute nodes.

`controlPlane`
Specifies the parameters that apply to control plane nodes.

`networking`
Specifies the parameters that apply to cluster networking configuration.

`platform`
Specifies the parameters that apply to the configuration of the platform hosting the cluster.

## Configuring the cluster-wide proxy during installation

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

<div>

<div class="title">

Prerequisites

</div>

- You have an existing `install-config.yaml` file.

- You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, all cluster egress traffic is proxied, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object’s `spec.noProxy` field to bypass the proxy if necessary.

  > [!NOTE]
  > The `Proxy` object `status.noProxy` field is populated with the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration.
  >
  > For installations on Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Red Hat OpenStack Platform (RHOSP), the `Proxy` object `status.noProxy` field is also populated with the instance metadata endpoint (`169.254.169.254`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit your `install-config.yaml` file and add the proxy settings. For example:

    ``` yaml
    apiVersion: v1
    baseDomain: my.domain.com
    proxy:
      httpProxy: http://<username>:<pswd>@<ip>:<port>
      httpsProxy: https://<username>:<pswd>@<ip>:<port>
      noProxy: example.com
    additionalTrustBundle: |
        -----BEGIN CERTIFICATE-----
        <MY_TRUSTED_CA_CERT>
        -----END CERTIFICATE-----
    additionalTrustBundlePolicy: <policy_to_add_additionalTrustBundle>
    # ...
    ```

    where:

    `proxy.httpProxy`
    Specifies a proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`.

    `proxy.httpsProxy`
    Specifies a proxy URL to use for creating HTTPS connections outside the cluster.

    `proxy.noProxy`
    Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations. You must include vCenter’s IP address and the IP range that you use for its machines.

    `additionalTrustBundle`
    If provided, the installation program generates a config map that is named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you provide `additionalTrustBundle` and at least one proxy setting, the `Proxy` object is configured to reference the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the RHCOS trust bundle. The `additionalTrustBundle` field is required unless the proxy’s identity certificate is signed by an authority from the RHCOS trust bundle.

    `additionalTrustBundlePolicy`
    Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when `http/https` proxy is configured. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter.

    > [!NOTE]
    > The installation program does not support the proxy `readinessEndpoints` field.

    > [!NOTE]
    > If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:
    >
    > ``` terminal
    > $ ./openshift-install wait-for install-complete --log-level debug
    > ```

2.  Save the file and reference it when installing OpenShift Container Platform.

    The installation program creates a cluster-wide proxy that is named `cluster` that uses the proxy settings in the provided `install-config.yaml` file. If no proxy settings are provided, a `cluster` `Proxy` object is still created, but it will have a nil `spec`.

    > [!NOTE]
    > Only the `Proxy` object named `cluster` is supported, and no additional proxies can be created.

</div>

## Deploying with dual-stack networking

For dual-stack networking in OpenShift Container Platform clusters, you can configure IPv4 and IPv6 address endpoints for cluster nodes. To configure IPv4 and IPv6 address endpoints for cluster nodes, edit the `machineNetwork`, `clusterNetwork`, and `serviceNetwork` configuration settings in the `install-config.yaml` file. Each setting must have two CIDR entries each. For a cluster with the IPv4 family as the primary address family, specify the IPv4 setting first. For a cluster with the IPv6 family as the primary address family, specify the IPv6 setting first.

``` yaml
machineNetwork:
- cidr: {{ extcidrnet }}
- cidr: {{ extcidrnet6 }}
clusterNetwork:
- cidr: 10.128.0.0/14
  hostPrefix: 23
- cidr: fd02::/48
  hostPrefix: 64
serviceNetwork:
- 172.30.0.0/16
- fd03::/112
```

> [!IMPORTANT]
> On a bare-metal platform, if you specified an NMState configuration in the `networkConfig` section of your `install-config.yaml` file, add `interfaces.wait-ip: ipv4+ipv6` to the NMState YAML file to resolve an issue that prevents your cluster from deploying on a dual-stack network.
>
> <div class="formalpara">
>
> <div class="title">
>
> Example NMState YAML configuration file that includes the `wait-ip` parameter
>
> </div>
>
> ``` yaml
> networkConfig:
>   nmstate:
>     interfaces:
>     - name: <interface_name>
> # ...
>       wait-ip: ipv4+ipv6
> # ...
> ```
>
> </div>

To provide an interface to the cluster for applications that use IPv4 and IPv6 addresses, configure IPv4 and IPv6 virtual IP (VIP) address endpoints for the Ingress VIP and API VIP services. To configure IPv4 and IPv6 address endpoints, edit the `apiVIPs` and `ingressVIPs` configuration settings in the `install-config.yaml` file . The `apiVIPs` and `ingressVIPs` configuration settings use a list format. The order of the list indicates the primary and secondary VIP address for each service.

``` yaml
platform:
  baremetal:
    apiVIPs:
      - <api_ipv4>
      - <api_ipv6>
    ingressVIPs:
      - <wildcard_ipv4>
      - <wildcard_ipv6>
```

> [!NOTE]
> For a cluster with dual-stack networking configuration, you must assign both IPv4 and IPv6 addresses to the same interface.

## Configuring regions and zones for a VMware vCenter

You can modify the default installation configuration file, so that you can deploy an OpenShift Container Platform cluster to multiple vSphere data centers.

The default `install-config.yaml` file configuration from the previous release of OpenShift Container Platform is deprecated. You can continue to use the deprecated default configuration, but the `openshift-installer` will prompt you with a warning message that indicates the use of deprecated fields in the configuration file.

<div>

<div class="title">

Prerequisites

</div>

- You have an existing `install-config.yaml` installation configuration file.

  > [!IMPORTANT]
  > You must specify at least one failure domain for your OpenShift Container Platform cluster, so that you can provision data center objects for your VMware vCenter server. Consider specifying multiple failure domains if you need to provision virtual machine nodes in different data centers, clusters, datastores, and other components. To enable regions and zones, you must define multiple failure domains for your OpenShift Container Platform cluster.

- You have installed the `govc` command line tool.

  > [!IMPORTANT]
  > The example uses the `govc` command. The `govc` command is an open source command available from VMware; it is not available from Red Hat. The Red Hat support team does not maintain the `govc` command. Instructions for downloading and installing `govc` are found on the VMware documentation website.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `openshift-region` and `openshift-zone` vCenter tag categories by running the following commands:

    > [!IMPORTANT]
    > If you specify different names for the `openshift-region` and `openshift-zone` vCenter tag categories, the installation of the OpenShift Container Platform cluster fails.

    ``` terminal
    $ govc tags.category.create -d "OpenShift region" openshift-region
    ```

    ``` terminal
    $ govc tags.category.create -d "OpenShift zone" openshift-zone
    ```

2.  For each region where you want to deploy your cluster, create a region tag by running the following command:

    ``` terminal
    $ govc tags.create -c <region_tag_category> <region_tag>
    ```

3.  For each zone where you want to deploy your cluster, create a zone tag by running the following command:

    ``` terminal
    $ govc tags.create -c <zone_tag_category> <zone_tag>
    ```

4.  Attach region tags to each vCenter data center object by running the following command:

    ``` terminal
    $ govc tags.attach -c <region_tag_category> <region_tag_1> /<data_center_1>
    ```

5.  Attach the zone tags to each vCenter cluster object by running the following command:

    ``` terminal
    $ govc tags.attach -c <zone_tag_category> <zone_tag_1> /<data_center_1>/host/<cluster1>
    ```

6.  Change to the directory that contains the installation program and initialize the cluster deployment according to your chosen installation requirements.

    <div class="formalpara">

    <div class="title">

    Sample `install-config.yaml` file with multiple data centers defined in a vSphere center

    </div>

    ``` yaml
    # ...
    compute:
    ---
      vsphere:
          zones:
            - "<machine_pool_zone_1>"
            - "<machine_pool_zone_2>"
    # ...
    controlPlane:
    # ...
    vsphere:
          zones:
            - "<machine_pool_zone_1>"
            - "<machine_pool_zone_2>"
    # ...
    platform:
      vsphere:
        vcenters:
    # ...
        datacenters:
          - <data_center_1_name>
          - <data_center_2_name>
        failureDomains:
        - name: <machine_pool_zone_1>
          region: <region_tag_1>
          zone: <zone_tag_1>
          server: <fully_qualified_domain_name>
          topology:
            datacenter: <data_center_1>
            computeCluster: "/<data_center_1>/host/<cluster1>"
            networks:
            - <VM_Network1_name>
            datastore: "/<data_center_1>/datastore/<datastore1>"
            resourcePool: "/<data_center_1>/host/<cluster1>/Resources/<resourcePool1>"
            folder: "/<data_center_1>/vm/<folder1>"
        - name: <machine_pool_zone_2>
          region: <region_tag_2>
          zone: <zone_tag_2>
          server: <fully_qualified_domain_name>
          topology:
            datacenter: <data_center_2>
            computeCluster: "/<data_center_2>/host/<cluster2>"
            networks:
            - <VM_Network2_name>
            datastore: "/<data_center_2>/datastore/<datastore2>"
            resourcePool: "/<data_center_2>/host/<cluster2>/Resources/<resourcePool2>"
            folder: "/<data_center_2>/vm/<folder2>"
    # ...
    ```

    </div>

</div>

## Configuring host groups for a VMware vCenter

> [!IMPORTANT]
> OpenShift zones support for vSphere host groups is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

You can modify the default installation configuration file to deploy an OpenShift Container Platform cluster on a VMware vSphere stretched cluster, where ESXi hosts are grouped into host groups by physical location.

The default `install-config.yaml` file configuration from previous releases of OpenShift Container Platform is deprecated. Though you can still use it, the OpenShift Container Platform installer will display a warning message that indicates the use of deprecated fields in the configuration file.

<div>

<div class="title">

Prerequisites

</div>

- You have an existing `install-config.yaml` installation configuration file.

- You have arranged your ESXi hosts into host groups.

- You have granted the `Host.Inventory.EditCluster` privilege on the vSphere vCenter cluster object.

- You have downloaded and installed the `govc` command line tool. Instructions can be found on the VMware documentation website. Note that `govc` is an open-source tool that is not maintained by the Red Hat support team.

- You have enabled the `TechPreviewNoUpgrade` feature set. For more information, see "Enabling features using feature gates".

  > [!IMPORTANT]
  > To enable host group support, you must define multiple failure domains for your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `openshift-region` and `openshift-zone` vCenter tag categories by running the following commands:

    > [!IMPORTANT]
    > If you specify different names for the `openshift-region` and `openshift-zone` vCenter tag categories, the installation of the OpenShift Container Platform cluster fails.

    ``` terminal
    $ govc tags.category.create -d "OpenShift region" openshift-region
    ```

    ``` terminal
    $ govc tags.category.create -d "OpenShift zone" openshift-zone
    ```

2.  Create a region tag for the vSphere cluster where you want to deploy your OpenShift Container Platform cluster by entering the following command:

    ``` terminal
    $ govc tags.create -c <region_tag_category> <region_tag>
    ```

3.  Create a zone tag for each host group by entering the following command as needed:

    ``` terminal
    $ govc tags.create -c <zone_tag_category> <zone_tag>
    ```

4.  Attach the region tag to the vCenter cluster object by entering the following command:

    ``` terminal
    $ govc tags.attach -c <region_tag_category> <region_tag_1> /<datacenter_1>/host/<cluster_1>
    ```

5.  Use zone tags to associate each ESXi host with its host group, by entering the following command for each ESXi host:

    ``` terminal
    $ govc tags.attach -c <zone_tag_category> <zone_tag_for_host_group_1> /<datacenter_1>/host/<cluster_1>/<esxi_host_in_host_group_1>
    ```

6.  Change to the directory that contains the installation program and initialize the cluster deployment according to your chosen installation requirements.

    <div class="formalpara">

    <div class="title">

    Sample `install-config.yaml` file with multiple host groups

    </div>

    ``` yaml
    featureSet: TechPreviewNoUpgrade
    featureGate:
      - "VSphereHostVMGroupZonal=true"
    # ...
    platform:
      vsphere:
        vcenters:
    # ...
        datacenters:
          - <data_center_1_name>
        failureDomains:
        - name: <host_group_1>
          region: <cluster_1_region_tag>
          zone: <host_group_1_zone_tag>
          regionType: "ComputeCluster"
          zoneType: "HostGroup"
          server: <fully_qualified_domain_name>
          topology:
            datacenter: <data_center_1>
            computeCluster: "/<data_center_1>/host/<cluster_1>"
            networks:
            - <VM_Network1_name>
            hostGroup: <host_group_1_name>
            datastore: "/<data_center_1>/datastore/<datastore_1>"
            resourcePool: "/<data_center_1>/host/<cluster_1>/Resources/<resourcePool_1>"
            folder: "/<data_center_1>/vm/<folder_1>"
        - name: <host_group_2>
          region: <cluster_1_region_tag>
          zone: <host_group_2_zone_tag>
          regionType: "ComputeCluster"
          zoneType: "HostGroup"
          server: <fully_qualified_domain_name>
          topology:
            datacenter: <data_center_1>
            computeCluster: "/<data_center_1>/host/<cluster_1>"
            networks:
            - <VM_Network1_name>
            hostGroup: <host_group_2_name>
            datastore: "/<data_center_1>/datastore/<datastore_1>"
            resourcePool: "/<data_center_1>/host/<cluster_1>/Resources/<resourcePool_1>"
            folder: "/<data_center_1>/vm/<folder_1>"
    ```

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Enabling features using feature gates](../../../nodes/clusters/nodes-cluster-enabling-features.md#nodes-cluster-enabling-features)

</div>

## Configuring multiple NICs

For scenarios requiring multiple network interface controller (NIC), you can configure multiple network adapters per node.

<div>

<div class="title">

Procedure

</div>

1.  Specify the network adapter names in the networks section of `platform.vsphere.failureDomains[*].topology` as shown in the following `install-config.yaml` file:

    ``` yaml
    platform:
      vsphere:
        vcenters:
          ...
        failureDomains:
        - name: <failure_domain_name>
          region: <default_region_name>
          zone: <default_zone_name>
          server: <fully_qualified_domain_name>
          topology:
            datacenter: <data_center>
            computeCluster: "/<data_center>/host/<cluster>"
            networks:
            - <VM_network1_name>
            - <VM_network2_name>
            - ...
            - <VM_network10_name>
    ```

    - Specifies the list of network adapters. You can specify up to 10 network adapters.

2.  Specify at least one of the following configurations in the `install-config.yaml` file:

    - `networking.machineNetwork`

      <div class="formalpara">

      <div class="title">

      Example configuration

      </div>

      ``` yaml
      networking:
        ...
        machineNetwork:
        - cidr: 10.0.0.0/16
        ...
      ```

      </div>

      > [!NOTE]
      > The `networking.machineNetwork.cidr` field must correspond to an address on the first adapter defined in `topology.networks`.

    - Add a `nodeNetworking` object to the `install-config.yaml` file and specify internal and external network subnet CIDR implementations for the object.

      <div class="formalpara">

      <div class="title">

      Example configuration

      </div>

      ``` yaml
      platform:
        vsphere:
          nodeNetworking:
           external:
             networkSubnetCidr:
             - <machine_network_cidr_ipv4>
             - <machine_network_cidr_ipv6>
           internal:
             networkSubnetCidr:
             - <machine_network_cidr_ipv4>
             - <machine_network_cidr_ipv6>
          failureDomains:
          - name: <failure_domain_name>
            region: <default_region_name>
      ```

      </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Network configuration parameters](../installation-config-parameters-vsphere.md#installation-configuration-parameters-network_installation-config-parameters-vsphere)

</div>

# Network configuration phases

There are two phases prior to OpenShift Container Platform installation where you can customize the network configuration. Customize settings in the `install-config.yaml` file and in the Cluster Network Operator manifest across two configuration phases.

Phase 1
You can customize the following network-related fields in the `install-config.yaml` file before you create the manifest files:

- `networking.networkType`

- `networking.clusterNetwork`

- `networking.serviceNetwork`

- `networking.machineNetwork`

- `nodeNetworking`

  For more information, see "Installation configuration parameters".

  > [!NOTE]
  > Set the `networking.machineNetwork` to match the Classless Inter-Domain Routing (CIDR) where the preferred subnet is located.

  > [!IMPORTANT]
  > The CIDR range `172.17.0.0/16` is reserved by `libVirt`. You cannot use any other CIDR range that overlaps with the `172.17.0.0/16` CIDR range for networks in your cluster.

Phase 2
After creating the manifest files by running `openshift-install create manifests`, you can define a customized Cluster Network Operator manifest with only the fields you want to modify. You can use the manifest to specify an advanced network configuration.

During phase 2, you cannot override the values that you specified in phase 1 in the `install-config.yaml` file. However, you can customize the network plugin during phase 2.

# Specifying advanced network configuration

To integrate your OpenShift Container Platform cluster with your existing network environment, you can specify advanced network configuration in a manifest before you install the cluster. Advanced network configuration can be configured only during cluster installation.

> [!IMPORTANT]
> Customizing your network configuration by modifying the OpenShift Container Platform manifest files created by the installation program is not supported. Applying a manifest file that you create, as in the following procedure, is supported.

<div>

<div class="title">

Prerequisites

</div>

- You have created the `install-config.yaml` file and completed any modifications to it.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Change to the directory that contains the installation program and create the manifests:

    ``` terminal
    $ ./openshift-install create manifests --dir <installation_directory>
    ```

    The `<installation_directory>` specifies the name of the directory that contains the `install-config.yaml` file for your cluster.

2.  Create a stub manifest file for the advanced network configuration that is named `cluster-network-03-config.yml` in the `<installation_directory>/manifests/` directory:

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: Network
    metadata:
      name: cluster
    spec:
    ```

3.  Specify the advanced network configuration for your cluster in the `cluster-network-03-config.yml` file, such as in the following example:

    <div class="formalpara">

    <div class="title">

    Enable IPsec for the OVN-Kubernetes network provider

    </div>

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: Network
    metadata:
      name: cluster
    spec:
      defaultNetwork:
        ovnKubernetesConfig:
          ipsecConfig:
            mode: Full
    ```

    </div>

4.  Optional: Back up the `manifests/cluster-network-03-config.yml` file. The installation program consumes the `manifests/` directory when you create the Ignition config files.

</div>

## Specifying multiple subnets for your network

Before you install an OpenShift Container Platform cluster on a vSphere host, you can specify multiple subnets for a networking implementation so that the vSphere cloud controller manager (CCM) can select the appropriate subnet for a given networking situation. vSphere can use the subnet for managing pods and services on your cluster.

For this configuration, you must specify internal and external Classless Inter-Domain Routing (CIDR) implementations in the vSphere CCM configuration. Each CIDR implementation lists an IP address range that the CCM uses to decide what subnets interact with traffic from internal and external networks.

> [!IMPORTANT]
> Failure to configure internal and external CIDR implementations in the vSphere CCM configuration can cause the vSphere CCM to select the wrong subnet. This situation causes the following error:
>
>     ERROR Bootstrap failed to complete: timed out waiting for the condition
>     ERROR Failed to wait for bootstrapping to complete. This error usually happens when there is a problem with control plane hosts that prevents the control plane operators from creating the control plane.
>
> This configuration can cause new nodes that associate with a `MachineSet` object with a single subnet to become unusable as each new node receives the `node.cloudprovider.kubernetes.io/uninitialized` taint. These situations can cause communication issues with the Kubernetes API server that can cause installation of the cluster to fail.

<div>

<div class="title">

Prerequisites

</div>

- You created Kubernetes manifest files for your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the directory where you store your OpenShift Container Platform cluster manifest files, open the `manifests/cluster-infrastructure-02-config.yml` manifest file.

2.  Add a `nodeNetworking` object to the file and specify internal and external network subnet CIDR implementations for the object.

    > [!TIP]
    > For most networking situations, consider setting the standard multiple-subnet configuration. This configuration requires that you set the same IP address ranges in the `nodeNetworking.internal.networkSubnetCidr` and `nodeNetworking.external.networkSubnetCidr` parameters.

    <div class="formalpara">

    <div class="title">

    Example of a configured `cluster-infrastructure-02-config.yml` manifest file

    </div>

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Infrastructure
    metadata:
      name: cluster
    spec:
      cloudConfig:
        key: config
        name: cloud-provider-config
      platformSpec:
        type: VSphere
        vsphere:
          failureDomains:
          - name: generated-failure-domain
          ...
           nodeNetworking:
             external:
               networkSubnetCidr:
               - <machine_network_cidr_ipv4>
               - <machine_network_cidr_ipv6>
             internal:
               networkSubnetCidr:
               - <machine_network_cidr_ipv4>
               - <machine_network_cidr_ipv6>
    # ...
    ```

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [`.spec.platformSpec.vsphere.nodeNetworking`](../../../rest_api/config_apis/infrastructure-config-openshift-io-v1.md#spec-platformspec-vsphere-nodenetworking)

</div>

# Cluster Network Operator configuration

To manage cluster networking, configure the Cluster Network Operator (CNO) `Network` custom resource (CR) named `cluster` so the cluster uses the correct IP ranges and network plugin settings for reliable pod and service connectivity. Some settings and fields are inherited at the time of install or by the `default.Network.type` plugin, OVN-Kubernetes.

The CNO configuration inherits the following fields during cluster installation from the `Network` API in the `Network.config.openshift.io` API group:

`clusterNetwork`
IP address pools from which pod IP addresses are allocated.

`serviceNetwork`
IP address pool for services.

`defaultNetwork.type`
Cluster network plugin. `OVNKubernetes` is the only supported plugin during installation.

You can specify the cluster network plugin configuration for your cluster by setting the fields for the `defaultNetwork` object in the CNO object named `cluster`.

## Cluster Network Operator configuration object

The fields for the Cluster Network Operator (CNO) are described in the following table:

<table>
<caption>Cluster Network Operator configuration object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>metadata.name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the CNO object. This name is always <code>cluster</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.clusterNetwork</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>A list specifying the blocks of IP addresses from which pod IP addresses are allocated and the subnet prefix length assigned to each individual node in the cluster. For example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">spec</span><span class="kw">:</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">clusterNetwork</span><span class="kw">:</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> </span><span class="fu">cidr</span><span class="kw">:</span><span class="at"> 10.128.0.0/19</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">hostPrefix</span><span class="kw">:</span><span class="at"> </span><span class="dv">23</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> </span><span class="fu">cidr</span><span class="kw">:</span><span class="at"> 10.128.32.0/19</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">hostPrefix</span><span class="kw">:</span><span class="at"> </span><span class="dv">23</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.serviceNetwork</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>A block of IP addresses for services. The OVN-Kubernetes network plugin supports only a single IP address block for the service network. For example:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">spec</span><span class="kw">:</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">serviceNetwork</span><span class="kw">:</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> 172.30.0.0/14</span></span></code></pre></div>
<p>You can customize this field only in the <code>install-config.yaml</code> file before you create the manifests. The value is read-only in the manifest file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.defaultNetwork</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Configures the network plugin for the cluster network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.additionalRoutingCapabilities.providers</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>This setting enables a dynamic routing provider. The FRR routing capability provider is required for the route advertisement feature. The only supported value is <code>FRR</code>.</p>
<ul>
<li><p><code>FRR</code>: The FRR routing provider</p></li>
</ul>
<div class="sourceCode" id="cb3"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="fu">spec</span><span class="kw">:</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">additionalRoutingCapabilities</span><span class="kw">:</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">providers</span><span class="kw">:</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="kw">-</span><span class="at"> FRR</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

> [!IMPORTANT]
> For a cluster that needs to deploy objects across multiple networks, ensure that you specify the same value for the `clusterNetwork.hostPrefix` parameter for each network type that is defined in the `install-config.yaml` file. Setting a different value for each `clusterNetwork.hostPrefix` parameter can impact the OVN-Kubernetes network plugin, where the plugin cannot effectively route object traffic among different nodes.

## defaultNetwork object configuration

The values for the `defaultNetwork` object are defined in the following table:

<table>
<caption><code>defaultNetwork</code> object</caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 20%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>OVNKubernetes</code>. The Red Hat OpenShift Networking network plugin is selected during installation. This value cannot be changed after cluster installation.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>OpenShift Container Platform uses the OVN-Kubernetes network plugin by default.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ovnKubernetesConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>This object is only valid for the OVN-Kubernetes network plugin.</p></td>
</tr>
</tbody>
</table>

## Configuration for the OVN-Kubernetes network plugin

The following table describes the configuration fields for the OVN-Kubernetes network plugin:

<table>
<caption><code>ovnKubernetesConfig</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mtu</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The maximum transmission unit (MTU) for the Geneve (Generic Network Virtualization Encapsulation) overlay network. This is detected automatically based on the MTU of the primary network interface. You do not normally need to override the detected MTU.</p>
<p>If the auto-detected value is not what you expect it to be, confirm that the MTU on the primary network interface on your nodes is correct. You cannot use this option to change the MTU value of the primary network interface on the nodes.</p>
<p>If your cluster requires different MTU values for different nodes, you must set this value to <code>100</code> less than the lowest MTU value in your cluster. For example, if some nodes in your cluster have an MTU of <code>9001</code>, and some have an MTU of <code>1500</code>, you must set this value to <code>1400</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>genevePort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The port to use for all Geneve packets. The default value is <code>6081</code>. This value cannot be changed after cluster installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipsecConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specify a configuration object for customizing the IPsec configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipv4</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specifies a configuration object for IPv4 settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipv6</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specifies a configuration object for IPv6 settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>policyAuditConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specify a configuration object for customizing network policy audit logging. If unset, the defaults audit log settings are used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>routeAdvertisements</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies whether to advertise cluster network routes. The default value is <code>Disabled</code>.</p>
<ul>
<li><p><code>Enabled</code>: Import routes to the cluster network and advertise cluster network routes as configured in <code>RouteAdvertisements</code> objects.</p></li>
<li><p><code>Disabled</code>: Do not import routes to the cluster network or advertise cluster network routes.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gatewayConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional: Specify a configuration object for customizing how egress traffic is sent to the node gateway. Valid values are <code>Shared</code> and <code>Local</code>. The default value is <code>Shared</code>. In the default setting, the Open vSwitch (OVS) outputs traffic directly to the node IP interface. In the <code>Local</code> setting, it traverses the host network; consequently, it gets applied to the routing table of the host.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>While migrating egress traffic, you can expect some disruption to workloads and service traffic until the Cluster Network Operator (CNO) successfully rolls out the changes.</p>
</div></td>
</tr>
</tbody>
</table>

<table>
<caption><code>ovnKubernetesConfig.ipv4</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>internalTransitSwitchSubnet</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>If your existing network infrastructure overlaps with the <code>100.88.0.0/16</code> IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.</p>
<p>The default value is <code>100.88.0.0/16</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>internalJoinSubnet</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>If your existing network infrastructure overlaps with the <code>100.64.0.0/16</code> IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster. For example, if the <code>clusterNetwork.cidr</code> value is <code>10.128.0.0/14</code> and the <code>clusterNetwork.hostPrefix</code> value is <code>/23</code>, then the maximum number of nodes is <code>2^(23-14)=512</code>.</p>
<p>The default value is <code>100.64.0.0/16</code>.</p></td>
</tr>
</tbody>
</table>

<table>
<caption><code>ovnKubernetesConfig.ipv6</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>internalTransitSwitchSubnet</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>If your existing network infrastructure overlaps with the <code>fd97::/64</code> IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.</p>
<p>The default value is <code>fd97::/64</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>internalJoinSubnet</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>If your existing network infrastructure overlaps with the <code>fd98::/64</code> IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster.</p>
<p>The default value is <code>fd98::/64</code>.</p></td>
</tr>
</tbody>
</table>

<table>
<caption><code>policyAuditConfig</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>rateLimit</code></p></td>
<td style="text-align: left;"><p>integer</p></td>
<td style="text-align: left;"><p>The maximum number of messages to generate every second per node. The default value is <code>20</code> messages per second.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxFileSize</code></p></td>
<td style="text-align: left;"><p>integer</p></td>
<td style="text-align: left;"><p>The maximum size for the audit log in bytes. The default value is <code>50000000</code> or 50 MB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxLogFiles</code></p></td>
<td style="text-align: left;"><p>integer</p></td>
<td style="text-align: left;"><p>The maximum number of log files that are retained.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>destination</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>One of the following additional audit log targets:</p>
<dl>
<dt><code>libc</code></dt>
<dd>
<p>The libc <code>syslog()</code> function of the journald process on the host.</p>
</dd>
<dt><code>udp:&lt;host&gt;:&lt;port&gt;</code></dt>
<dd>
<p>A syslog server. Replace <code>&lt;host&gt;:&lt;port&gt;</code> with the host and port of the syslog server.</p>
</dd>
<dt><code>unix:&lt;file&gt;</code></dt>
<dd>
<p>A Unix Domain Socket file specified by <code>&lt;file&gt;</code>.</p>
</dd>
<dt><code>null</code></dt>
<dd>
<p>Do not send the audit logs to any additional target.</p>
</dd>
</dl></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>syslogFacility</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>The syslog facility, such as <code>kern</code>, as defined by RFC5424. The default value is <code>local0</code>.</p></td>
</tr>
</tbody>
</table>

<table id="gatewayConfig-object_installing-vsphere-installer-provisioned-customizations">
<caption><code>gatewayConfig</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>routingViaHost</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Set this field to <code>true</code> to send egress traffic from pods to the host networking stack. For highly-specialized installations and applications that rely on manually configured routes in the kernel routing table, you might want to route egress traffic to the host networking stack. By default, egress traffic is processed in OVN to exit the cluster and is not affected by specialized routes in the kernel routing table. The default value is <code>false</code>.</p>
<p>This field has an interaction with the Open vSwitch hardware offloading feature. If you set this field to <code>true</code>, you do not receive the performance benefits of the offloading because egress traffic is processed by the host networking stack.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipForwarding</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>You can control IP forwarding for all traffic on OVN-Kubernetes managed interfaces by using the <code>ipForwarding</code> specification in the <code>Network</code> resource. Specify <code>Restricted</code> to only allow IP forwarding for Kubernetes related traffic. Specify <code>Global</code> to allow forwarding of all IP traffic. For new installations, the default is <code>Restricted</code>. For updates to OpenShift Container Platform 4.14 or later, the default is <code>Global</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>The default value of <code>Restricted</code> sets the IP forwarding to drop.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipv4</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv4 addresses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipv6</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv6 addresses.</p></td>
</tr>
</tbody>
</table>

<table id="gatewayconfig-ipv4-object_installing-vsphere-installer-provisioned-customizations">
<caption><code>gatewayConfig.ipv4</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>internalMasqueradeSubnet</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The masquerade IPv4 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is <code>169.254.169.0/29</code>.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>For OpenShift Container Platform 4.17 and later versions, clusters use <code>169.254.0.0/17</code> as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.</p>
</div></td>
</tr>
</tbody>
</table>

<table id="gatewayconfig-ipv6-object_installing-vsphere-installer-provisioned-customizations">
<caption><code>gatewayConfig.ipv6</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>internalMasqueradeSubnet</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The masquerade IPv6 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is <code>fd69::/125</code>.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>For OpenShift Container Platform 4.17 and later versions, clusters use <code>fd69::/112</code> as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.</p>
</div></td>
</tr>
</tbody>
</table>

<table id="nw-operator-cr-ipsec_installing-vsphere-installer-provisioned-customizations">
<caption><code>ipsecConfig</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the behavior of the IPsec implementation. Must be one of the following values:</p>
<ul>
<li><p><code>Disabled</code>: IPsec is not enabled on cluster nodes.</p></li>
<li><p><code>External</code>: IPsec is enabled for network traffic with external hosts.</p></li>
<li><p><code>Full</code>: IPsec is enabled for pod traffic and network traffic with external hosts.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<div class="formalpara">

<div class="title">

Example OVN-Kubernetes configuration with IPSec enabled

</div>

``` yaml
defaultNetwork:
  type: OVNKubernetes
  ovnKubernetesConfig:
    mtu: 1400
    genevePort: 6081
    ipsecConfig:
      mode: Full
```

</div>

# Services for a user-managed load balancer

You can configure an OpenShift Container Platform cluster to use a user-managed load balancer in place of the default load balancer.

> [!IMPORTANT]
> Configuring a user-managed load balancer depends on your vendor’s load balancer.
>
> The information and examples in this section are for guideline purposes only. Consult the vendor documentation for more specific information about the vendor’s load balancer.

Red Hat supports the following services for a user-managed load balancer:

- Ingress Controller

- OpenShift API

- OpenShift MachineConfig API

You can choose whether you want to configure one or all of these services for a user-managed load balancer. Configuring only the Ingress Controller service is a common configuration option. To better understand each service, view the following diagrams:

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAAN7CAIAAACF/ywBAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAylpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMS1jMDAxIDc5LjE0NjI4OTk3NzcsIDIwMjMvMDYvMjUtMjM6NTc6MTQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNS4wIChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjE4Mzg2QzREOTJENjExRUU5MUQyQjkyOEYzQTYzMTY0IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjE4Mzg2QzRFOTJENjExRUU5MUQyQjkyOEYzQTYzMTY0Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MTgzODZDNEI5MkQ2MTFFRTkxRDJCOTI4RjNBNjMxNjQiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MTgzODZDNEM5MkQ2MTFFRTkxRDJCOTI4RjNBNjMxNjQiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz6q/LYhAADfOklEQVR4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t6empvbq1eunn3665557tBAREZGenj5//vyJEydu2LBh7ty55cqV86Q/goODt23bpi/RgQMHunfv3qFDB43SunXrJk2a1K1btylTpvTo0aOw+3Q0mJ9//vm+fftGjRpV2INsYWFhy5cvf/LJJ3NycrKysooYfD8/P4fDMXjw4CVLlujj2bNnzS14Wq99n3/+eTUmMjKyf//+zZs3V7N13Pfee++1117TfxYmT56sYvx3AABQbJDQAQAUo3/VHI6tW7cOHDhQwaHC0dDQ0HfeeUexX8OGDTt27BgUFEQsB4i+C++9995PP/2kL8uoUaPMTDR+fn4333xz1apVtXLcuHETJ040CR273Z6cnNy3b9+DBw9+8MEHJjfqdrvbtm3bqVOn7t27DxgwoHr16jfccEP+++D0lTx8+PDHH39cr169W265pcCn2NSYPXv29O7d+5prrlGBkydPFtZsm82mL/Xw4cPnzJlz5513/vvf//ZkiLQpKytr/fr1zZo1mzp1qtpj5utp1apV165d+/Tpo12aN29+//33n/MBMQAArIKXOAAAig+Favfdd9/333+/c+fOyZMnb9myZcSIEc8///yXX355zmyOAkJ/f/+gXOahrfxbPY/hmJL5i51Xyf/7lzj3ORGV0d/zmohXhQtrbf5DFFjyfJtaGNVg6s//mJIaqQrzT5uSZ9paT2EzFJJ/KExVpm2eI3rX7BlJdeQiT0phV4jnTJ3va7A8l1YRT3IVfUK9u+BpSZ6eeo6Sv3lmuhzvaufPnx8REfHII49kZmampqZmZGTo63P27NmePXtWr1590aJFp0+fNvUEBwfPnTt348aNTz/9dPfu3ZOTk1NSUrSLCtSuXXvKlClut3v48OFOpzN/s7XvN998k5CQ8PDDD4eGhub/Dqph6enpasaZM2dmzpxZrly5IiZODgsLmz179tixY5944om+fft6b8rJyVH9n+WqWLGiakvNpR5pL/1HQAf67rvvmFELAFCccIcOAKD4UGCpYLhRo0aNGzdeu3at1kRFRcXFxZUuXVoBXhGBtMJOhZEHDx5MTExUJaVKlapUqZJiPzPfhxa09cSJE4oJY2Nj9VElT548WbJkycqVK2t3z40Jvpc0QkJCFHPu3r1bB1K8rUBUh9Zy0TN9qB7tqKMcOnRIcaxprZn/JX8qRyXV9x07dqhh4eHhaoYC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emYDUUkV++yzzzIyMrp06aIYOzMzUyVjYmJUUkF4RESESbhok/ZS7zx5Dd875d0ST/3vvffe77//rkpS/2DuffBkc7RJNYwcOXLdunXDhg0bMGCAlvft2zdkyJASf0y7a57eUoVpfzCzveSZGOUi+d5T7yyAVnbu3Fmn49133zU5DtNNk8Qx2Zz815XZUXWqpIZIR/RMnKxlDb5OpZmE28cTevHd9z59arZJJH377bcaFu87gMz5+u6777RcrVo1z/qHHnpInRo/frwKeAZQDStZsuQXX3yxadOmHj16VKlSxdyOpLM/derUqKgojUCee8RUifZq2rTpbQVp27ZtZGSkxqp58+atW7fWdatrrLCSDRs2LJH7tJpZ1vfIzAN99OjR8PBw7wyjGfwFCxbor+dNagAAkNABAMBKzFytjz/++IwZM8w8NeXLl69YseKSJUt+/fVXhdYKehUNav2///3vEn88EeMJibds2TJ48GDF/wo1VUwr33jjjbFjx9asWbNnz56euzDOWdK8eGvMmDFDhw5NSUlRGR1XfxXVz549W+Vr1Kih2NhM7qPWqs1qudaoqc8884xCVq08cOCAqVyx65u5rrvuus6dO6sZTqfziiuueOGFF5KSknS4FStWqElmmufFixd36NBBQbjJWPnSKRPze7fEzDqsvY4dO/bwww/v2bMn7A8qMGLEiP3795vcgSqcM2fOxIkT4+Li+vXrd+rUqV69et17773ffPONVpoURv369UvkPjujMVENZih0OtavX/+n5DLO9/R500ptUoFRo0ZNnjxZ42C6qYZ99NFHM2fONFP85rmutEY73n///era1KlTX3755dTUVHOWT5w4oY/33HPP6dOnXS6Xjyf0IjNZeU6fKrzxxhtbtWr1r3/9a+TIkeqLDqq2qV9BQUHq1Pjx46+66qo2bdp4XoV266239unT59tvv3366afNFavCqurDDz8cNGhQlSpVBg4caG7P0TivWrVKp09nuUKFCgXeW+TJi+VnnjT0JPW0e2ElzbCYl45pWdfz9u3b77jjju7du+vrrLaZa0ld09aXXnrphx9+0EWoIb3I8QQA4PLBI1cAgP8hivq++OILRaEK9hSvxsTElC5d+pVXXnn44Ydbt26tkNU8X7N48WLzaIaZNMTsm52dfeWVVy5fvvzLL79s0qRJQEDAli1bdu7c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9OnTr7/+ek/ybuvWrYMGDdqwYYMnn6juqyWzZs3SpdK8eXOz3pfLxlwbOlyNGjVUfurUqVoZGhqq9eccPQAAQEIHAAArUXis2Pjbb7/duHGj5wkXp9NZr169OnXqmERDVlaWYvW9e/dOmTJlzZo1kydPHjFixC+//PLaa69pl2bNmg0fPlzFwsLCRo4cad6crWBbgfRLL71Uvnz59PR01ZaZmWnerq3dFd63bt26Z8+epUqVWrFihQL133777Zlnnvn4449VSYncZ3ZCQkJU/q233qpdu/bzzz+vlVFRUWqJInNt0sclS5Y0aNDgs88+UyWrVq2aPn26ovpZs2a1adPmtttu00FLlizZvHnz3bt3a03Dhg3Lli2rZZXXXx1UC08//fQFJ3TUNnXkzTffVHtq1arVtWvXihUr7tq1a/bs2fHx8UOHDo2NjY2Li0tLS/OxGRqTw4cPP/bYYzt27AgMDGzUqJF6ER4evm7duvnz57tcrnM+eGUeoVLh9u3b33jjjVqzfPnyZcuWJSYmPvvss5UrV65fv76G6IKHRee6cePGV111lQa8ZcuW6rVOx3/+85958+ap2okTJ2qlajOnT2df5T///HP1SI1JSkp6//33165de+LECQ3ahx9+aFJC+vjEE09s2bLF4XCoWNu2bbWga2zhwoUHDhxQy809Rz5eNubacLvdqiElJeWpp55SIzUmF5O5AwAAJHQAALhMEzqKdUePHp2Tk+N5pZEC9RdffLFBgwYmDFaErDUDBw5cv379zz//PGPGjPr168+ZM+fQoUPlypUbNWqUAua0tLTg4OBOnToptP7111+XLVsWERHRvn37unXrZmZmmlTRzp07FYTrKM2aNVMlkZGROmiLFi3Kly//0ksvKdr/6quvHnroIc+TSor24+LiJk6caN60pcZ4Uk6qU/H/J598osNpU8uWLYOCgkwvVI/C/hK5r+jq0aPHnXfeWblyZVNn27ZtmzRpopXHjh1bsWLFgAEDLuwtTgEBAbt371ZftFyjRo0PPvigVq1aapu/v79a8vDDDx8/fvztt9++6aab1Cofm6E6Vc+2bdu08MADD7z88ssaT5Xv3bt3mzZtBg8enJSUdM6GqfvDhw9/9NFHzccHH3xQozd+/HjtOzWXDuRLewq8n0XjX7Zs2ffff18nXcOufVVbx44d1ccPP/zw4MGD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rrvuWrFihaboBsBvv/228y7IXl5eskg7c+ZMcnKys4WkpKSMjIySWSFZ4Mm6VKfT7d69++TJk7KqPH36tPxfVpjKejUuLs61/p49eypykxF5+erVq1999dXExERZHMoqes6cOW+88YYsC1u0aHHPPfc4N13xTUibyh1Afv31V4vFIgtO2UfGBhS33nrr3XffbbVaP/zww9mzZyt3CJZvf/7556eeeurIkSOuA77SA/tKjEPpec+ePaWr33777ahRo+Lj43Nzc+WQefPNNzt37qw8beoSfsfV6WR/fXx80tLSHnvssd9//10pl29nzZq1YMECZ2tS88knnzSbzbIL8pIvv/wyMzPz3Llz8pL7779/0KBB8oHg2rJ8LOj1+g8++KBLly42m23JkiXTpk1j4AEArsIvxoQAAKAisob8/vvvV69e7SyRBZXdbpclWePGjWWRppzzonjggQeWLVuWkJDwQJEaNWrs3bt37dq1p06dKnlOQZ06dSIjI2Wxt2vXrjvvvNPX19fb2/vjjz+WQlm2rVy5UlaVKSkpsuaUFeyGDRtkeSydkQXnRVeVsq0JEya8++67sglZXcsCVRaEtWrVmj9/fmBgoNS51E20b99+3rx5sv584YUXFi5cKJWHDx/+9NNPMzygDLkZM2YcOnRo9+7dU6dOlXEVERGRlZW1b98+Gfk7duz4+uuv5Vio4sC+EuNQei4dlp5LV6VBOVTDw8MzMzOTk5Pz8vJmzpx5xx13SM8r3mDHjh0nTpw4efLk7du39+vXr0WLFh4eHvHx8bIJq9UqPZcOKzU7deokeyFbj4uLGzp0qARHr9cnJSXJ1qWmbHfkyJHFGvfz81u8ePGAAQN27tw5Z86cgICAknUAALiiSOgAANRBefB2sUKtVluzZs2GDRv27t370UcfLbbYk/Xq66+/PmvWLFnExsTESElwcPCTTz757bffSkmxZy2bTKbx48cnJiYeP378jz/+kFWccmdlWde9+uqr8u0PP/zwQREp7NGjhywFZSWs3Hi1nG7n5+fLkq9Bgwbz58+XpbLBYPD29paOydKxbdu2/52MDYZL2sRdd9318MMPf/bZZxKQtLQ0u92uXNVlKZKTk1PstilllaP6k1Eq751yt+BSKyg/1fz1ZjoydFetWvXSSy/JUN+9e/fOnTuVBMRtt902evRo5Q5TFR91Mmxk8CijqCLjsKz6ZZW7atSo0VdffSU9X7duXUpKSnJysk6nCwoK6tWrlxQqB/gltf/cc8+FhITI50BcXJzyFHPZ8Tp16vTv379nz56uL3/hhRfCwsLmzZt35MiRXbt2ScA9PDwaN24sARk6dGip7Us7S5YsGThw4P79+yWwnp6ew4YN41lyAAC30fLkCwCAKpw7d06WpsoTuBUyhcnaKTg4uGHDhuXcxUOWhbGxsbLglHVd69atpfKePXvOnDnj7+/fvHnzYleXSOVNmzalp6d7eXk1bdq0Q4cOSsuyltu+ffuBAwdk2XzjjTe2b99eVtqy6pMOyLc1a9Ysud2DBw/eeeedp06devrpp+fOnRsfHy/bzc/Pj4yMbNu2bcmrWi5pE7LvW7ZskQZl1R0aGioLdeUpRampqdLhFi1auD6vp6xyVHMyJOQtlpEv75q8d6UOcnlzZWzLF1Kh5GOwZPzs2LEjMzNTWmjZsmWbNm2KPd+tIqMuNzdXDj3ltLJi9youdRyWVb+cdkqSNqUbciSGh4dLz+VgvGg75bQvh+Hvv/8usZL9lR62a9cuIiKi1O1mZGTExMQol6E1adJENi2fG+W3f+zYsaSkJGlZgiyHNgkdAAAJHQAA1M2Z0PnHP/4xf/58AgIAAIDLiJsiAwAAAAAAqAwJHQAAAAAAAJUhoQMAwBVRkVvAAgAAAJXDPXQAALgiLukWsAAAAMAlIaEDAAAAAACgMlxyBQAAAAAAoDIkdAAAAAAAAFSGhA4AAAAAAIDKkNABAAAAAABQGRI6AABcBnO+T3/o3fiDJ/IJBQAAANyAhA4AAJfBl7vOfPbDieNnCwgFAAAA3ICEDgAAl4GnUacx6/U6LaEAAACAG5DQAQAAwJVltVpjY2N//PFHu93uzu2eOHFi7dq1x44dq7Y9BACg0gyEAAAAQEWOHDny1VdfNWzYsH///q7lmzZtWrFiRWxsrM1mq1OnzsCBAx988EFPT8+SLaSlpf3rX//6/vvv5Qu9Xt+kSZNHH320Z8+eZW0xLy9Ptvjll18mJCRI42FhYXfddVevXr0iIyPL6ef27dvXrFnzyCOP3HTTTadPn+7WrZv0eefOne6M1eLFiydOnPjjjz/WrVu3/JpXq4cAAFQaZ+gAAACow86dOx999NFmzZqNHz9+1apVznKr1Tpu3Lhu3bp9+umner3ebDbv27fvscce6969+5EjR1xbKCgoeOutt6SFsWPHHj58WGrqdLp///vfd91119ChQy0WS8mN7tixo1OnToMGDdq4caN8K+3HxsY+++yzDzzwQE5OTllddTgcTz755Lx58/z9/ZUSrVZbanbpilJOtzEYiv8JMzMzMy8vr1jhVekhAACVRkIHAABAHYYPH/7NN98MHDhQq9UajUZn+SuvvPL6668/8MADBw4ciImJ2b59u3zx9ttv//rrr7179z516pSz5rJly0aNGlW7du0NGzYcPHhQasbGxkrlAQMGLFmy5IUXXii2xZ07d3bv3j0uLu79999XGhfyxSeffDJjxgxvb++yuvrLL7/s2LFj5MiR4eHhSon02f0RK3WjH3/88S233CI7XpHKAABUW1xyBQAAoA6zZs1q2bJlbm7uRx995HA4lMLDhw/PmTOnffv2n3zyiTPL4+3t/dRTT5nN5mHDhk2cOHHhwoVKeY8ePWbMmPH00087T5wRDRs2XL58+YEDB959990xY8bUq1dPKc/JyRkyZEh+fv7PP//cpk0bZ/3g4OC//e1v5Xf1tddeM5lMI0aMqIZhPHLkSEJCQmFhISMKAKBqnKEDAACgDj169KhZs2Z2drZr4fr1661W6+jRo13P2VEMHTq0a9euy5YtS0hIUEoiIiImTJjgms1RmEymAQMGWCwWZ01N0Zkse/funTJlims2pyIOHz78zTff9O/fv2HDhtUwjD4+PvJ/Ly8vRhQAQNU4QwcAAKA6cjgcixcvjomJeeGFFyIiIsqqdvLkSfl/WTf9HTFixObNm3/88ccnnnii/M3l5+drik7tUb612WwLFy4MCgoaNmzYpfb8/ffft1qtI0eOLFau0134U+K2bds+//zz48eP165d+957773jjjtKbWT9+vVr1qw5ceJEjRo17r77bqlZ8pKoI0eObN26VRo8d+6cj49Px44d+/fvHxgYWGqDUkc6lpOTs2XLFvn2nXfe+f777wsLC7t373777bdXsIdKdkyv1zvfI+mVrsjQoUPDwsIYtwAAtyGhAwAAUB1lZGSMGTPm/PnzYWFhL7/8clnVPDw8NEXZilJ/2r59e51OFxMTU35C58yZM8uXL2/Tpk3z5s2VkqNHj+7bt69nz57BwcGaorTRgQMHbDabr69vkyZNyrl7jnR7yZIlHTt27NChg2u5Vqs1GAzz58+fPn16QECA1WpNTk6WbydOnDht2jTXZE1WVtaIESNWrlwpWwkPD09PT3/nnXfuv//+Dz/80PXcohdffHHu3LmFhYX16tUzmUyyC7LdefPmyQulhyU7lpeXt3Tp0hMnTuTm5sq3q1atklfJHkmbSkKnIj2UPvz000/F9ku5/K1v374kdAAA7sQlVwAAANWRv7//ww8/3LRp0+7du5dTTcmbfPLJJ6X+VMrtdntiYmLJH6Wnp+/Zs2f//v2bNm269957jUbjRx99pKSHRFJSUmFhYZcuXbKyskaNGtW4ceOuXbtKT2699dZmzZq98847ygOkSt1iZmbmmDFjip1Q4+np+fvvv//000+bN28+UGTDhg1169adMWPGunXrnNVsNtsjjzyycuXKiRMnHvjTSy+99MUXX0i5/NRZs1WrVrIV6b9UOHjwoPx/6tSp8u2zzz7rWs0pJCRE9lSqjR49Wr6VnVUa/8c//lHxHi5btmz37t17/xQXFzd58mQpl741atSIQQsAcCsHAACosq6vHdI89OumQ+cIBS6vvLy8YiV79+6VX+GGDBmifFtQUHDnnXdKycyZM61Wq7NaRkbG2LFjQ0JCvLy8oqOjS7b8yiuvOH8hbN26dXx8vOtPly5dKuUTJkxo06ZN48aNP/jgg507d+7evfvjjz9u1qyZ/OiZZ54ptbdRUVERERG5ubmu5cqVU1J+/vx51/KVK1dKU4MHD3aWLF++XEqk58VaHjdunJR/8cUX5Yfr1ltvNZvNycnJyrfTp0+XV23atMm1zqxZs6Twp59+qlwPXR05ckRe1aJFizNnzjBWAQBuxhk6AAAA1ZfZbC6/gtFo/PDDDzt06DBhwoRWrVo9//zz06ZNGzJkSJMmTbZu3fr55597enqWvAuy6NOnz8IikyZNslgsvXr12rRpk/OnykOg3njjjR49euzevXv48OEtW7Zs3rz5I4888ttvv919990LFixYvXp1sTbXr18fFxf3zDPPyEaL/aigoKBu3brKDYmdunTpIiXyEmfJ0qVLpbclLzGTTvr6+i5atKj8aMhe5+fnZ2VllVNHOX/HarVWrodOubm5AwYMOH/+/LJlywICAhirAAA34x46AAAA6la3bt3169e/9957y5cvX7Jkid1ur1ev3nPPPTdq1KjExMTTp0/feOONJV/Vqojy9fjx4x988MHevXtv2bJFeaaVn5+fpug5WTNnziz2Qi8vr1dfffXHH3985513+vbt6/qjefPmBQQEDBkypOTmtFptySuhpNBoNCq3Ihbnz5+Pi4uTkn/+85+uCRepJt/m5eXt27evoKDAZDIp5bt27Vq7du0ff/zh7e3dqFEj6b/SVMnbJ1dERXroauTIkTt37vzoo49atGjBIAQAuB8JHQAAANXz8vIaW+T06dN2u71GjRpKuXIH35YtW5b/cl9f33feeefGG2+cMmXKmjVrpKRBgwaaP++4XFJUVFS9evWOHDniml7Zvn37xo0bR40a5dz6RSlnjDu/zc7OtlgshYWF69atcy1XREdHR0ZGOl84Y8aMSZMmBQcH33zzzQaD4Zdffpk/f35+fr6zP5dFsR46vf3224sXLx49evTgwYMZfgCAq4KEDgAAwLVDeSiV0/Lly81mc7du3S76wjp16tSrV2/v3r1KjiYyMlKa+v7771999dWSJ7yUleOQmiNGjKh05/39/WXTst3t27eXX3P9+vWTJk3q16/fwoULnfkj6fywYcNiY2OvdJC3bds2evTojh07zp49myEHALhauIcOAADAtem7777bunXroEGD6tate9HKWVlZmZmZgYGBBsOFP/gFBQUNHjx437590kjJyklJSceOHWvSpInzdBj59vPPP+/Vq9fNN99c6Q57eXl16tTpwIEDv/32W/k1165dqym6D7Tr2UDNmjVr1apVWY/fKqZyl2Vpip7gLpGRQH300UcXvcMRAABXDgkdAACAaurMmTMHDx6s3Gt37Njx97//PTQ01PUGw5999tn999+fmppasv7rr7+emZn5wAMPOO8XM3bs2KCgoKeffjohIcG1pt1unzBhQmFhoevJOEuXLs3LyxszZkwVd3n06NHKM63OnTvnWi6Nnz9/3vmtctPljIyMkhG76CaUjI9er69E92w22+OPP56SkvLFF180bNiQIQoAuIpI6AAAAFRHOTk5/fr1u+WWW/71r3+VX3PDhg2dOnX68MMPd+7c+ccff2zfvn3y5MkdO3bMz8//5JNP6tWr56wZHx+/atWq5s2bz5o1a/fu3SdOnEhLS/v1118HDx48c+bM6OjoUaNGOSvXrVv3/fffT0pK6tChw8KFCw8fPiyVN23adPfdd0sjQ4cO7dWrl1Lz7Nmz7777buvWrbt06VLF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" alt="An image that shows an example network workflow of an Ingress Controller operating in an OpenShift Container Platform environment." />
<figcaption>Example network workflow that shows an Ingress Controller operating in an OpenShift Container Platform environment</figcaption>
</figure>

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAAN7CAIAAACF/ywBAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAylpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMS1jMDAxIDc5LjE0NjI4OTk3NzcsIDIwMjMvMDYvMjUtMjM6NTc6MTQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNS4wIChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjE4Mzg2QzQ5OTJENjExRUU5MUQyQjkyOEYzQTYzMTY0IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjE4Mzg2QzRBOTJENjExRUU5MUQyQjkyOEYzQTYzMTY0Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MTgzODZDNDc5MkQ2MTFFRTkxRDJCOTI4RjNBNjMxNjQiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MTgzODZDNDg5MkQ2MTFFRTkxRDJCOTI4RjNBNjMxNjQiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz5ef6QZAADUqElEQVR4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+ObS+vzzz3VpDRo0SGfHkWflypU66tZbb1XlKhCUjz4WeRuRvpo6deqcOXOeeuqpfv36Fb9utzeF3W534aWU7Xk2btyocdWsWbOYtZYBAMDffngwBQAAeMnPz2/BggUff/xx9+7dhw4dqgg2Jibm7bffHj16dFpa2qOPPmre0aOoNS4uTgF57969IyIi7rvvPnN/xOLFi1evXv3GG2/8+9//VkmF0CdPnjx69GhGRsapnspR7K3AWGH5smXLGjdufNdddwUHB//yyy/qg6p6//33FeSbRhWx5+TkPPDAA+phpUqV7r///qioqL179yqwv/POO9W3Z5991suOnaon6u3AgQNXrVrVvn37Rx55REH4t99+O3PmzC1btsydO1cdy8zM7JRn3rx5L7/88tixY5OTkzVLK1asmDhxYtOmTfv3769wXV1NSEh45plnatWqde+995o1oZcvX75o0SJVpc6o52YaNTnqj8ZSt27dW2+9NT4+ftasWS+++KLKHzx4cOvWrY899lhgYKDqX7hw4W233aYaqlev7s5T4pFqIB988IEaDQkJMU1HR0frLPfp00cHaginOvC0p+Cpp55yuVxentASDz8rK0uXU2xsrI7dt2+fToqa0B61oh5eeeWVOgWffvrpF198oUq0X+dFs3HttdfqwPyL12j4X331lU5ir169Ro4cqW4Xk3Y8o8KeTKXnWbPp06d/8803jz/+uEbqzW1QAABAbP8L73QAAHhPMbAiwDNdVOV/hOJhBdUKOBs0aGDeS6WIdPPmzV27dlV0+uOPP4aFhWnqjhw50qlTp8TExAkTJtx7773mzh3tV7x99913KwJfsmRJjRo1dIgKTJ48+bPPPlP5ItMEQUFBCtpnzpypA59//nk/Pz+163Q6ly9ffvPNNyuKXrp0aaVKlRSiq+Rzzz2nMj169Jg2bVpkZKSCczW9a9euV1999cYbb+zYsWN0dLQ3HVNgX7gnis8VqM+aNUtR95NPPunZr6omTZp0//33v/DCCxqCWUWle/fuW7Zs+fzzz7t163bw4MEuXbqoUVVep04d87iQGt25c6ei9+DgYP0UMSu8jB49Wl1VhcOHD1cfNI3/+te/dEG+8847/fr102Wp2Va1Gou+UhNvv/12aGioJkTHapamT58+YsSI8ePHq6SXp0BNq2Tr1q3VE02p+q8Z3rFjh9qt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qljXrl21oWtsyZIl+/fvV8/NPUdeXjbm2nC73aohJSVlxIgR6qTmpDSZOwAAQEIHAIALNKGjWHfSpEk5OTmeVxopUH/yySebNGliwmBFyNrz8MMPb9iw4eeff3777bcbN268YMGCgwcPVqpUaeLEiQqY09LSAgICevXqpdD6119/XblyZWhoaPfu3Rs1apSZmWlSRTt37lQQrlZat26tSsqWLatG27VrV6VKlaeeekrR/ueffz5kyBDPk0qK9rt16zZ9+nTzpi11xpNyUp2K/+fNm6fm9FX79u39/f3NKFSPwv4yea/ouv3222+66aYaNWqYOrt27dqiRQvtjImJWb169bBhw0r2FidfX9/du3drLNquW7fuu+++W79+ffXNx8dHPbn77ruPHj366quvtmrVSr3yshuqU/Vs375dG3feeeeYMWM0nyo/aNCgLl26PProo0lJSaftmIY/bty4e++913y86667NHtTpkzRsa/nUUPe9KfI+1k0/xUrVnznnXd00jXtOla19ezZU2OcM2fOgQMHtm3bplNpCutblZ8wYcItt9yiFjUzupxuvvlmzZsuA105at3Pz+/DDz/csmWLhty/f3/1PCgoSAfqGnj//fedTmffvn1VyZ49e7y5bDwpm9zcXF05mn9dfuaCUQdI6AAA8E/jblgAAM5DTqdmzZoNGjSo95c6deqEhYXlX11Y8XBISIjic7OsySOPPLJ8+XIF5NpQoG6W1FEoro3U1FQVNokSBdJpeUyyY82aNUePHlX8P2zYsMjISM9TRYMHD27WrJmOWrp0qUqaY1WbwvsHHnhAf5OTk1VJ/jVQ1Le6desGBwebr9RQ+/bt1UN9lZiY6MluqMAll1ziWRBXTdSvX19D0OE68OTJkyV7EsfpdGosMTExOvzee+9VnSdOnFA39Ld169a33HKL9m/bts2kKrzphibn2LFjq1at0oEa16OPPqomUlJSNJmZmZnNmzcvX778aV8mpdo0A+YZpdQ8mrEHH3ywTZs2mlLzPJoaKs20qGTt2rXVijlWfwMCApo2baoD1YROrqekvlIrupbUDTMz1atXv/rqq1XSXCRmyN988425/EaOHGlWv9ZXKtC/f/9+/frpQDPV3l82Jh3ZqVOn66+/XgMxl19pXhYGAAC8/YHEFAAAcC4p1lVo/dJLLyn29mRMTKBe4G3lCrOvvPLKZ5555pFHHjHplYEDByqo9qy2e1pmZVzF7c8///zUqVM9SQEF7bt27VJAfuDAgaSkpKioKLPf19dXfTvVvRXmTUaeDpt6yuQ9d2N26liNbtGiRStWrIiOjlbTDRs2NCkA219KPG9//vmnWixfvrwqzD9Rqrxly5YzZszQ/OzcubN169bedEM9j4mJMQmRVq1aRUREJCcne4ZmFhv2plcFCpu3gKnCH374IT4+PjY2tk6dOqWZFtWmM/XVV19t3rz52LFjlStX1mATEhLUf7VVIA2kbuR/TZXqN0+NeYas/phVkJs2bRoZGWmWIvKM4kwvG/O0lxEYGGjezsZ/4AAAkNABAOCipZC4fPnyUVFR+aNoxeeF72swKQwF0uYrBeHm7dReNmQSRmru+PHjCv7zH1ghj2JylfHs14b391aYnI7no8PhSEtLe+KJJz777LP09HTVHBoaumHDhpkzZ2rDz8+vlJOmfqpvwcHBAQEBBTppKtcwU1JSvO+GK4+OKleu3Fm8o0RVqSHzYJ3ofJ04caJk06KRfvfdd48//nh0dLRK6oLZt2+f6tG2v7+/N3m9/CfIvDPL3FljFr4p5WVTYNRkcwAAOMdI6AAAcB6Y5Wny309RmOJ2BfBPPPFESkqKeWf5jBkzrrrqqg4dOnjurSieeV5GkfaLL75Y4N3V5oktU+1pny3yhno7b968jz/+ODg4ePjw4bfccov2pKWlbdiwQa172eFiREVFORyOmJiYw4cPV69e3TN1drv9wIEDJnmh/Wp04cKFp+2GhlyuXLnQ0NCEhIQtW7aYJ5g8KQnvbyYyb4D6208rp3Pnzp2qsFweffSmP0X8RHM64+PjJ0+erNE1a9Zs7NixtWvXVrePHj367rvvLl68+Ewn0Aw5JCREQ96/f79JZnmGbO7lMVeCl5cNq+QAAHB+sYYOAADngXlteZHMPTjmndyTJk3avn17UFDQ448/Xrly5eTk5DFjxigaL3Bnh+ehGPOyakOHt2jRIiAgwLyJKTQ0tGzZsvoYHBwcHh4eFhamPepGaR6DKmDDhg3qw6WXXjpixIhLLrmkQoUKdevW7devX1RUVPGpq9NStc2aNfP19c3IyPjkk080OZoB/VX/09PTFyxYoAJqzrwmzJtu5OTkVKlSRWU0/LVr165YsUITopnXvGmKyuTdpXLamTH3vGRmZpqzJprSbdu2ffvttya7VLNmTS/7U5hO5YEDBw4ePKhqBw8e3LVrVx2oQ9q1a9e5c+cSzKd6oiFrisy71VetWmWGLOp/amqqri7zdNg5vmwAAAAJHQAALECRsGJmBfkrVqxYWcjy5ctjY2MVYyuEnj179qJFixwOx5133jl69Ojhw4f7+vr++eef48aNK/BSbRNgp6SkqNr09HRF5omJiYr5r7nmmg4dOuTk5Hz44Yfjx49PSEhQtVlZWWpFte3YscMsgnO2qHJ148SJEwcOHPDNo/p3796tzpSyIbNQ8bXXXquxfPbZZxMnToyLi3O5XIcOHRozZsy6deu03b1799q1a2vU3nTD7XZrAvv3769vNWNPPPHE/PnzVSA1NXX9+vVPPfWUOQunPZUZGRljx479/vvvjx8/fvLkSZ3BYcOGHT58WF/169cvPDzcrKpTgmnRKTYldezevXs1A35+ftqjHuoaKMHa0mbIAwcOVD1myB999FFSUpI6tnbt2iFDhgwdOvTo0aPq8Dm+bAAAQMnw7zEAAOc6oZOdnT1y5Mgi121JS0ubPn26QuslS5a88sorKnnttdc++OCDCrxvvfXWX3755YMPPvjqq68uv/zyESNGeB7Yadq06axZsxSoT5gwYd68edrfv39/VaKY/Mknn9yzZ8+2bdumTp26ePHiatWqKYBXTB4fH79582ZF7BEREWdlXBrODTfc8Mknn+zfv//ee+/t0aNHWFiYGvruu+8SExN9fHxKWblG9/TTTx88eHDnzp3Tpk374osv1POjR49qj8lBaELME0NediMjI6Nz586aJU14dHT08OHDa9So4e/vr/p1joKDgz1v7ypGYGCgprFv377169e32+3qTHJysnp72223DRw4MD093dfXt2TTolN/6aWXtmjR4ssvv3znnXdiYmKaNGmSmpq6cuVKXQbm1qQznUYN+brrrtPlpItBV4WGXLNmTYfDceDAAV0VWVlZbdq0GTZsmMvlOmeXDQAAIKEDAIAFZGZmpqWlFV9GQf7u3bsfeeQRxfA1atR47rnnQkJCdJTNZhs9evTvv/++cePGyZMnK9rv0qWLQnTV2aFDh969eyvyV5Bvbl1R5G+32/Wxdu3a77zzjsr/8MMP27dv37Jli8lWtG7d+u677w4NDTVJEAXzKlzkC6e1R/v1beF1cPPvVzfatGnz7LPP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SOafjz/++BtvvCGJ77zzzvvuu4/mAbXJzZ0798CBA3v27Jk9e7a0q+jo6MzMzN9//11a/s6dO7/44gv5LFSwYVdFO5SSS4Gl5FJUyVA+qlFRUenp6UlJSbm5ufPmzRs8eLCUvPwZ9u7de9q0aTNmzNi2bduoUaPat29vsVji4+NlF3a7XUouBVZT9unTR96F7D0uLu6OO+6QyjEYDIcPH5a9S0rZ7wMPPFAk81q1av3nP/8ZO3bsrl27FixYEBISUjwNAABVioAOAEAb1BtvF9moKEp4eHiTJk2GDx9+6623FpnsyXz1hRdeePbZZ2USu337dtkSFhY2adKkr7/+WrYUudey2WyeOnVqYmLin3/++ccff8gsTl1ZWeZ1zz33nPz63XffLSskG6+88kqZCspMWF14tYxi5+XlyZSvcePGixcvlqmy0WgMCAiQgsnUsUuXLv8djI3GC9rFVVddddNNN61atUoqJCUlxel0qld12QplZ2cXWTaltO3wfdJK5dipqwWXmEB9Vvf3xXSk6X766adPPfWUNPU9e/bs2rVLDUD0799/ypQp6gpT5W910myk8aitqDztsLT0pW331KxZs88//1xKvm7dumPHjiUlJen1+tDQ0GHDhslG9QN+Qfk/+uijderUkX4gLi5OvYu5vPEGDRqMHj16yJAhni9//PHHIyMjFy1adOjQod27d0uFWyyWli1bSoXccccdJeYv+Sxfvvz666+PiYmRivXz85swYQL3kgMAeI3CnS8AAJpw5swZmZqqd+BWyRAmc6ewsLAmTZqUsYqHTAt37NghE06Z13Xq1EkS79279/Tp08HBwe3atStydYkk3rhx44kTJ/z9/du0adOzZ081Z5nLbdu2bf/+/TJtbtGiRY8ePWSmLbM+KYD8Gh4eXny/sbGxV1xxRWpq6n333bdw4cL4+HjZb15eXtOmTbt06VL8qpYL2oW89x9//FEylFl3RESETNTVuxQlJydLgdu3b+95v57StsPHSZOQQywtX46aHLsSG7kcXGnb8kASFL8NlrSfnTt3pqenSw4dOnTo3Llzkfu7lafV5eTkyEdPPa2syFrFJbbD0tKXkU9xkqcUQz6JUVFRUnL5MJ43nzLyl4/hr7/+KnUl71dK2L179+jo6BL3m5aWtn37dvUytFatWsmupd8oO/+jR48ePnxYcpZKlo82AR0AAAEdAAC0zR3QueeeexYvXkyFAAAAoBKxKDIAAAAAAIDGENABAAAAAADQGAI6AABUifIsAQsAAABcHNbQAQCgSlzQErAAAADABSGgAwAAAAAAoDFccgUAAAAAAKAxBHQAAAAAAAA0hoAOAAAAAACAxhDQAQAAAAAA0BgCOgAAVIIF3564cWl87PE8qgIAAABeQEAHAIBK8Nnu06u+O/5nRj5VAQAAAC8goAMAQCXwM+l1VoNBr1AVAAAA8AICOgAAAKihYmJivvjiC5vNRlUAADTHSBUAAABozh9//PHhhx9u2LAhOzvbbDZ37Nhx1KhR/fr18/f3L/uFn3zyyd69ewcOHNi/f/+yU544ceKtt96SDCdMmBAUFOT5VEpKiuz922+/lQcGg6FVq1a33nrrkCFDzlvsbdu2rV279uabb77sssuqvQ5tNptUWlZWVmJiIi0KAKA5nKEDAACgJXa7febMme3atZszZ05aWprRaMzMzHz99deHDh26du3asl/77bffjh07dvbs2Rs2bDjvXsaPHz9t2jTZS3Z2tnt7fn7+Sy+91LZt24cffvjgwYNWq1Wv13/88cdXXXXVHXfcUfapLi6Xa9KkSYsWLQoODvaFmpTyOByOgIAAGhUAQIs4QwcAAEBL7r///tdff3306NHTp09v3769oigul2vfvn2bN28ePHhwGS/cv3//TTfdVLt27fT0dLPZXPZepk6dum7dusDAQKvVKrtwb3/nnXcmT57crl271atX9+nTR80nISHh8ccfX758eXBw8KJFi0rLc8uWLTt37nzssceioqJ8pDL1ev66CQDQKsYwAAAAzXjnnXdef/31O++88+OPP+7QoYMaapH/27Vrd99999WpU6e0F2ZmZo4dOzYsLGzJkiXn3YvsYnGhbt265ebmej515ZVXzp07d9OmTQMHDnRHhZo0afLee++1adNm6dKlR44cKS3b559/Xl4yceJEjiMAABVHQAcAAEAbzpw5M3PmzPr16y9YsMDzrJnzcrlcd9xxR0xMzKpVq1q1alV24s2bN99zzz3XXXfdlClT8vPz5bWez0ZHRz/55JPFr5kym81jx4612WwJCQklZnvw4MGvvvpq9OjRTZo08ZH6vKA6BADA13DJFQAAgC9KSkqaP39+ly5d7rjjDjX0sGHDBtk4Z86c0NDQC8rq6aef/vTTT5cvX96xY8cffvihjJQJCQk33HBDhw4dJLH86nA4yr+XvLw8+b+0JWlef/11u93+wAMPuLecPXv2tddeCw8PHz9+/Pfff79ixQqDwTB37lzPC7LWr1+/du3a48eP161bd+jQoddcc03xKMyhQ4c2bdr0888/nzlzJjAwsHfv3qNHj65du3bxMmzduvXbb789ePBgo0aNrr322u7du8se5T2qeS5btkx2NHHixIiIiCIv/OCDD2JiYu699171jcir3E+5XC751el0tm3bVvKk3QIAvMcFAAAqbMDzB3Q3bt144AxVgcry9NNPy1e1oKCgkydPqlumTJmiK7xRlPrrnj171q9fv3Hjxvj4+DLyef/99+VVDz/8sPqrpJdfn3nmmeIpc3Nzu3btWqtWrdjYWHVLz549Q0JCjh8/ft7SpqenN2zYsHPnznl5ecWfTU1NDQ0N7d27t9PpdG9MSUkxmUx9+vRZuXKlFKlevXqSw969e9VnMzIyrr/+ejVCdOmll6q32RozZoxs98z58ccfl0zkqUaNGkmysLAwedy6deuYmBjPZDabbdKkSeq33/DwcDXcM378+Ojo6ObNm8sbd1fv0qVLixRe6l/2LtVy9uzZzZs3l/al+qabbqLRAgC8iUuuAAAAfNGgQYPatGlz0003ua9v2r59uzxu0aLFunXrOnXq1L59+8GDB19++eUtW7YcO3ZsXFxc8Uy2bds2fvz4K6+8csGCBefd45133vnbb7+tWrVKdlGeEp44cWLv3r0xMTEbN2685pprTCbTihUrLBZL8ZTvv/9+enr6Qw895Hl+jTwODQ1NSkpatmzZxx9/vH///t27dzdv3lxXeGbQzTffvHr16mnTpu3/y1NPPfXJJ5/Ids/zhjp27CjZShkkQWxsrPw/e/Zs+fXBBx90J3M6nXfdddfSpUvHjBkjdajm9uWXX8pj2bt7JSBJYzAY5C0UOS/ps88+O3v2rOwlMDBQdrdnz559f5Ed7dixo0mTJvKu77//fhotAMCriGkBAFBxnKGDqqCeOaKy2WzNmjVr3rz5E088ERYWds899/zwww8xMTFbtmx58MEH5UtdRETE7t27PV9+/Pjx6OjoJk2anDhxwr2xtDN01IjPwoULPTeWfYaOeg6RqlOnTqWdKCTvQootJcnJySlSvPr16+v1eilSkZe89957Oo+zitweeeQR2f7JJ5+UXW/dunWzWq1JSUnqr5999pm86rrrrvM8P0hItURGRrrP0HE4HJdffrmiKJ7VKBu7d+9uNBrdZy2VWKTXX3+d5goA8DLO0AEAAPBRVqvV/djhcJhMpsTExM8++2zdunVLly7t379/q1atevXqtWjRoi+//PLEiRP33HNPfn6+ml4e/Otf/5KNH3/8cXh4eNk7Wrt27WOPPTZhwoSHH364/MUbMWLEG4WmT59us9mGDRumRouKWL9+fVxc3P333+/n51fkqZycnI4dOw4YMKDI9rfffjs4OHjmzJlFtsuOgoKC3nzzzbILJtWSl5eXmZmp/vrqq68ajcY5c+YUWX8nNDRUcnOfj6PX66UG5PvxJ5984k6zY8eObdu2XX311SWetfTOO+8sXLjwrrvu4tZdAADvY1FkAAAADTCbzXq93mq1fv7558WDC9dcc82tt966YsWK3377TV2qZurUqT/++OOXX37ZsWNHz5RqVMV9nZGIiYm57bbbBg8eXDxQYjAYFEUpbZ3jjoXUx7K7G264Yfjw4bLTzp07eyZbtGhRSEjI+PHji+fgcrmKX6J19uzZuLg4k8n073//2263u7dLSeTX3Nzc33//PT8/3/0Wdu/eLW/zjz/+kHI2a9ZMyiAVpfvrJlaSm6S/7LLLilea5CYV5bnlyiuvDAsLe++99x577DH1Xb/77rtSSPf6O5527dp11113SQ2U507wAABUOgI6AAAAGmAwGKKjow8dOlRaeGXAgAErVqyIi4vr3bv32rVrX3zxRdk4e/bsGTNmeCY7e/as/L9kyZLVq1d37dr11Vdfvf3220+fPi05d+/evUiAIzY2Njc3t0+fPiaT6bXXXisSqfEUFBQkWbVo0WLWrFmyd/f2bdu2bdiwYfLkyXXr1i3xha6/3xZdZGVl2Wy2goKCdevWFX+2V69eTZs2db927ty506dPDwsLa926tdFo3LJly+LFi/Py8tzhnqxCl156aXluUi6FHDNmzBtvvLF169bBgwdLtXz44YdNmjQpfg5Renr6uHHj/P39V65cWfzMIwAAvICADgAAgDYMHDjwq6+++vXXXxs0aFB2SoPB0L9/f5fLlZOTc95sL7vssoCAADWGUpHiSakaNWq0b98+z9NnXnnlFUVRLuiKpODgYHl5WFjYtm3byk65fv366dOnjxo16o033nAHjKQAEyZM2LFjhzu32rVrp6SkyBssccHmIm677TbJbcWKFYMHD/7mm29SU1MfffRRz2vfVJMmTYqNjV29enXLli1pmQCAakFABwAAQBvGjBnz1FNPLVq0aPTo0cXPN9myZYuucPkY+X94oRIz+fXXX3v06DFlypSpU6eqW1asWFHaHvv27RsTE/PTTz8FBgaet3iZmZnp6enR0dFG43+/YR49evSjjz4aNmxY69aty/82/f39+/Tp8+GHH/7yyy9S1DJSfvnll/L/vHnzPE//adu2bceOHX/77Td3bt27d5diyBbJ1vPlJpNJr9cXOSmpW7du7du3l5xPnTr19ttv+/n5/etf/yqy34ULF65evfqJJ54YO3YszRIAUF1YFBkAAMBHxcbGnj592v1rdHT0Qw89tGXLlmeeeaZIyh9//HH58uU9e/Ys46ooVW5urq5wyeTyFMDhcLhcruzsbPeWVatWjRkzJjk5uXjiF154IT09/brrrlOXsNEVrm0su5MyX+gbnzJlinoDqTNnzhQpvHrJmEq91iktLa3Iyz0rTdx7773yvxSjyPZDhw6dOnXKYDB4bpRfx48fLynnzp27efPm0aNHN2zY0DPBDz/88OSTT44cOXLevHk0UQBANSKgAwAA4Is+/PDDrl27jho1yjOeMm3atEGDBs2YMeOWW27ZunXr8ePHDxw48O9//3vo0KH+/v4vv/yy++yYKhIfH//pp5+2a9fu2Wef3bNnjxQgJSVFSiLlmTdvXq9evSZPnqymzMjIWLp0aadOnfr163ehe+nevfvMmTN//vnnvn37fvbZZ4mJiXFxcfKgd+/e8k7dFXLdddeZTKYJEyZIytxC+/btkwJ8/fXXnqs+DxgwQOpt+/btUrx333137969O3funD9//sCBAzMzMyWHInsfM2ZM7dq1Fy9ebLPZilws9ueff952221SyfKmVqxY8Z+/vPXWW9988w2NFgDgVdy5HQCAihvw/AHdjVs3HjhDVaCyLFy4UL6q1a9f/9SpU57bz5w5M2XKFPW8kpCQEPXaqx49emzbtq082a5fv17Sz5gxozyJO3ToYDKZUlJSPDd+++233bp1U79JSgFq1aqlKzyxZeLEiampqe5k//nPf3SF13OVlrlkK5nLLkpL8MILL6jXUlksFvWsn8jIyLlz52ZnZ7vTvP/++2qaRoWC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u3btqujaXdq6PkR6X7XXuqSuanUNqSKpDoHFL9uW8pM2odinQKlmbVuJiYkKlE899ZRikwbB7hZ52223KaBrDC22WmDS3k2aNOm+++7TyJT7LdMAj4g2WqUDbV2yZ9SIc/TVwowZM/y/nqoFxo8f/9BDD2lk7CxZq85o3b179w4dOlS75n+k1IHk5GT1VkOqzxPEDoC8QF44zvOC0a5pYefXEvvmwuuvv64u2V99e/bsyewGyAvkheMnL6gbertqKOwXBw3UmjVrJk+erJ7be+Dcc8/t1q0bJ/ujRhzNa+js2LHDAofmc7t27fTbst2A0Odzkvc3P/Uh6f/+7/++/fbbpKQkzYGGDRted911mrGff/75okWLNKnUwuOPP/7uu++mpqZ6TyqF/iFDhvTq1WvdunXPP//8/v37NW/1a/n8+fP79eunwPTggw/qvx988IEat/MkFYOUNnJzc1u0aOH9PUnNw4ULFypM/+1vfzvppJM2bNigcKMdCbBjFhGqxM4vveKKK9q0abNy5covvvhCY6LGly9fPm7cuIcffrjc+q52p0GDBjfffPPTTz991llnderUSaFWgezDDz9UgNM+qktTp07t3r27d9bUQHXs2PG5555LSEiYMGHC9OnTtb/q86pVq7Zu3aoB0bi9/PLLS5YsUWsalksvvfSGG27Qtl588UUNpp787LPPpkyZcs0111TypdDKj8gll1wS+IFW39RDdenHH3/U1u3KlJdddlnbtm1Xr149a9YspSLvbKGW169fry1attNxVETWwspVo0ePVscUfJ999tnTTz9decLnW8fcdxYgL5AXyAvldt75PUTLjBkzZtSoUeqDPsdrnDUgfGoHyAvkheMqLxi9unjx4htvvDE2Nlb7Ys/07dtXbyR1oJILdwLuKOh4f2lF7/KDnnUWFha2fft2K8FqHmpqKSiceeaZmtUDBw78y1/+8s0332i6aqLOmzdPAcK7ct+/f//hw4dryfPPP18/NYu8r6qlBrWAguDSpUu1rn0Vs3fv3lpYUabYw2lNc++EE04YO3asApk9r2m8adOmADum2FGlUbJi/5NPPjlgwAAbMcXNhx56SI8VEWbOnDl48ODGjRuXu646r/SjvVCOsVyoqHTaaacprFizitQ+R0S78Oijjyqgq/Pt27df72FXAtOOKxT+/PPPipJaTEPXpUsX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" alt="An image that shows an example network workflow of an OpenShift API operating in an OpenShift Container Platform environment." />
<figcaption>Example network workflow that shows an OpenShift API operating in an OpenShift Container Platform environment</figcaption>
</figure>

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAAN7CAIAAACF/ywBAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAylpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMS1jMDAxIDc5LjE0NjI4OTk3NzcsIDIwMjMvMDYvMjUtMjM6NTc6MTQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNS4wIChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjE4Mzg2QzQ1OTJENjExRUU5MUQyQjkyOEYzQTYzMTY0IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjE4Mzg2QzQ2OTJENjExRUU5MUQyQjkyOEYzQTYzMTY0Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6NjNCQzE4RDQ5MkJCMTFFRTkxRDJCOTI4RjNBNjMxNjQiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MTgzODZDNDQ5MkQ2MTFFRTkxRDJCOTI4RjNBNjMxNjQiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7/yqgJAADYlklEQVR4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yU6dOj311FNqxdwwUgp1fuXKlb179zaDMvUvWbLE9ERx/pYtW7p37z5kyBDzuI3nqGnTpqn8119/7e/vr/2nTp3SpOlY1aDWTYcHDRq0Y8cOFSgyjUePHr355ptVskuXLtdcc82kSZPMi8ZHjRrlmVuV3LZtm2cayznS0odZijJPgZcntPzD//TTTzX8wYMHp6enmxNR/LYp09CGDRu00bhxY0+epcxiqnDFihUq1r9/f32k5oIK0a9Fbjfzsum8AsUza4cPH05JSWnbti3PfgIAUArW0AEA/BfW0CkS5z/44IMffvhhz549W7durdg1Pj7+9ddfT0hIePzxx0eOHKngWeG6InDF2NoICQmJjIxUEG7uaFi4cKE2Xnrppb///e+ekldccUVsbOyqVatKXL1FQa/2KyxfunRpixYtFNgHBwf/+OOP6oMqf/fddxXkmwPNU10PPPDAvHnzqlWr1rt375iYmL179yqwVzCsvo0dO1a1TZgw4bnnnrvsssuOHDmigL9+/fo6xSpz8OBB9fOtt97SGM+0mo+afu+99/75z3+q6TvvvFPd3rdvn4Z/+vRpDWrAgAEZGRka1PDhw+fMmTN69Ojx48enpqaapXOvv/76Vq1affbZZyahs2PHDjVXr149zWStWrXU82XLli1YsEB7NEvquZrT5JiHgOoX0IQnJia+8sor2v/www8fOnRo69at6oY6vHz58vnz59epU0c11K5dOycnR41OnDjRm5EWX0OnzGGeaZ0db06BWvTmhJprozzDnzp16hNPPKEO6FNdhCWeU52Lw4cPd+rUKSws7LvvvtNRJd64VLxYQEBAv379Fi1apJ6rbx9//LHOrLqk/1DoLOvyvvLKK9WNUm6DKr1pk3w0D51pAvv375+UlKTmqlevzouuPFhDBwBAQgcAQELHW2Yl14yMjCZNmpg7DhRNbd68uXv37orAv//++8qVK2uuFHJ37dpVIWhcXNy9995r7tzRfsXbQ4YMUQS+ePFihd/6N9cE7bGxscuWLSsxTaBA99///vesWbN04DPPPOPn56d2FeWq/K233hoSErJkyZJq1aopylXJJ598UmV69eo1bdq06Oho8yroXbt2zZgx44Ybbrj66qt1oEletG3b9tVXXzVLz5pBPfjgg4rJR4wYMWnSpBJ7oqZ37Njxt7/9rWrVqh999NEll1xi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BY0ZM6Z69eqpqanjxo1TNF7kzg7PQzHmZdWGDm/btm1AQIB5E1NoaGhYWJh+DQ4OjoiIqFy5svaoG+V5DKqIDRs2qA8NGzZ86KGHLrrooqioqNjY2L59+8bExJSeuiqTqm3durXT6czKyvroo480OZoB/VT/MzMz582bpwJqzrwmzJtu5OXl1ahRQ2U0/LVr1y5fvlwTopnXvGmKKhXcpVLmzJh7XrKzs81ZE03ptm3bFi1aZLJLdevW9bI/xelUHjx48NChQ6r2rrvu6t69uw7UIZ06dbr22mvPYT7VEw1ZU2Terb5y5UozZFH/09PTdXWZp8PO82UDAABI6AAAYAGKhBUzK8hfvnz5imKWLVuWkJCgGFsh9GuvvbZgwQK73T5o0KDRo0cPHz7c6XT+9ttvEydOLPJSbRNgp6WlqdrMzExF5klJSYr5r7jiimuuuSYvL+/999+fNGnSiRMnVG1OTo5aUW07duwwi+D8UVS5upGSknLw4EFnAdW/e/dudaacDZmFiq+88kqN5ZNPPnnqqaeOHz/ucrkOHz48bty4devWabtnz57169fXqL3phtvt1gQOGDBAn2rGHn300blz56pAenr6+vXrx44da85CmacyKytr/Pjx33777alTp06fPq0zOGzYsCNHjuijvn37RkREmFV1zmFadIpNSR27d+9ezYCfn5/2qIe6Bs5hbWkz5DvuuEP1mCF/8MEHycnJ6tjatWvvueee+++//9ixY+rweb5sAADAueHfYwAAzndCJzc395FHHilx3ZaMjIzp06crtF68ePELL7ygkldeeeXQoUMVePfv3//HH3987733vvjii0suueShhx7yPLDTqlWrV155RYF6XFzcnDlztH/AgAGqRDH5Y489tmfPnm3btj3//PMLFy6sVauWAnjF5ImJiZs3b1bEHhkZ+YeMS8O5/vrrP/roowMHDtx77729evWqXLmyGvrmm2+SkpJ8fX3LWblG9/jjjx86dGjnzp3Tpk377LPP1PNjx45pj8lBaELME0NediMrK+vaa6/VLGnC9+3bN3z48Dp16vj7+6t+naPg4GDP27tKERgYqGns06dP48aNfXx81JnU1FT19rbbbrvjjjsyMzOdTue5TYtOfcOGDdu2bfv555+/8cYb8fHxLVu2TE9PX7FihS4Dc2vS2U6jhnz11VfrctLFoKtC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yt6OHTs2ISHBvT07O7ugoCAuLk7qhAbzN+BwON54443Nmze3aNFixIgRZQZ0li9f/tZbb8mDXr16+SigU1RUdOrUKbPZbLFYvGmH5aX39f74mpQrH7GgoCA/lwsAQHn4wgcA0AaDwRBSLDY2tkOHDu3+EhMTk5eXt2bNmpEjR/7P//zPBed/+PDhIUOGjB8//scffwzwqpg9e/bQoUNffPFFmV6WqCJBU/k7CQ4ODgoKkmZf3glo6rPCd2+9FG00GkvvQHntsLz0vt4fX1PLpU0CAAIHwxIAQEsKCgpGjhw5c+ZMl8ulbsnIyHjvvfc++ugju90+ZcoUk8n0yCOPXEDODodDJmxBxQK8EuRIZSdDQ0M5Ewe0QwAAai0GYACAlrhcLplA1q1bt95fOnTo8Nprr82dO9doNMr0cubMmdu2bStz8nny5MnMzMzyclZPgpD8K/4jfE5OzvHjxwsKCi5s/wsLC8+b5rxFmEwmNZ4VHBxccVanTp0qcfYEapuzZ89Ky3cHQKuxYXvfDm02m2TucDgqteeyMxkZGd58ZLzJX3ZV6kFqw5uiM4vReAAAAY4zdAAAGuN0OktvvPnmm/fs2TN79myr1Tpv3rx3331X3Z6env7LL7+sWrUqKSlJpqyKotSrV2/AgAF33313RESEmuazzz577733ZL5XVFQUFha2cuXKgwcPyuO4uLiXX345KipKpot//vnnd99999tvv0mGMsOUZK1bt77rrrt69+5d3n4eOXLk8ccfz87OvvHGG6+//vq333577dq1ubm5sbGxsmXUqFGe18h4U4RkJRnKFDclJUWelT285557QkJCZN575513utf9kWOUjVu2bHnllVf++OMPo9HYoUOHRx99tGPHjjSeWuX777//6KOP9u/fL60rJiZm8ODBd9xxR3R0dKVaXWletkNhNptl49y5c5ctW3bmzJm6deuOHDny3nvvle0V77nsz8KFC3fs2JGXlxceHi4NWD7gl112WYlkXuZ/4sSJd95558cffzx9+rTJZGrfvv24cePKXNVYMvn444+/+eYbqQ35tUGDBv3797/llluk06hgbydNmrR582b5OD/55JP9+vWj4QEA/McFAIAWbNiwQV0r5OGHHy4zQWpqavPmzUNDQ9u0aSOzTdkis0GZxLrDHMZipmIDBw6U2Z36wunTp+uKF6CRCWH9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pmRt2rSRSZp6zovqhhtu+OCDDw4dOnRDsXr16u3atWvFihUnT54sfU5Bw4YNmzVrJpO97du3X3311eHh4aGhoR999JFslGnb0qVLZVaZmpoqc06Zwa5evVqmx7IzMuE876xSynr66afffPNNKUJm1zJBlQlhQkLCa6+9VqdOHUlT2SJ69uz56quvyvzzySeffOeddyTxXXfd9cADD9A8oDa5mTNn7t27d8eOHdOmTZN2lZiYeObMmT/++ENa/tatW7/++mv5LFSxYfuiHcqeyw7LnsuuSobyUY2Pjz99+nRKSkpBQcGsWbP69+8ve+59hn369Jk0adKUKVM2bdo0YsSITp06BQUFHTx4UIqw2+2y57LDaspLL71UjkJK37dv37hx46RyDAbD4cOHpXRJKeU++OCDJTKPiIh4//33b7zxxm3btr344otRUVGl0wAA4FMEdAAA2qDeeLvERkVR6tev37Rp06FDh952220lJnsyX33llVeef/55mcRu3rxZtsTExNx///3ffvutbClxr2Wz2fzEE08kJycfO3bszz//lFmcurKyzOteeukl+XXVqlXzi8nGAQMGyFRQZsLqwqsV7HZhYaFM+Zo0afLaa6/JVNloNIaGhsqOydSxW7du/x6MjcZKFXHNNdfccsstS5YskQpJT093Op3qVV3WYnl5eSWWTSlvOwKftFJ579TVgstMoD6r++/FdKTpfvHFF5MnT5amvmPHjm3btqkBiMsuu+zhhx9WV5jyvtVJs5HGo7Yib9pheenL2+6pRYsWX331lez5ypUrU1NTU1JS9Hp9dHT0kCFDZKP6Aa9U/o8//njdunWlH9i3b596F3M58IYNG44cOXLgwIGeL3/yySfj4uJeffXVAwcObN++XSo8KCioTZs2UiHjxo0rM3/JZ8GCBaNGjdq9e7dUbHBw8J133sm95AAAfqNw5wsAgCbk5OTI1FS9A7dKhjCZO8XExDRt2rSCVTxkWrhlyxaZcMq8rmvXrpJ4586dWVlZkZGRHTt2LHF1iSRes2bN8ePHQ0JC2rdv36tXLzVnmctt2rRpz549Mm1u1apVz549ZaYtsz7ZAfm1fv36pctNSkq6+uqrT548+cADD8yePfvgwYNSbmFhYbNmzbp161b6qpZKFSHHvm7dOslQZt2xsbEyUVfvUpSWliY73KlTJ8/79ZS3HQFOmoS8xdLy5V2T967MRi5vrrRteSAJSt8GS9rP1q1bT58+LTl07tz54osvLnF/N29aXX5+vnz01NPKSqxVXGY7LC99BfmUJnnKbsgnMT4+XvZcPoznzaeC/OVjuHHjRqkrOV7Zwx49eiQmJpZZ7qlTpzZv3qxehta2bVspWvqNivM/evTo4cOHJWepZPloE9ABABDQAQBA29wBnfvuu++1116jQgAAAFCNWBQZAAAAAABAYwjoAAAAAAAAaAwBHQAAfMKbJWABAACAC8MaOgAA+ESlloAFAAAAKoWADgAAAAAAgMZwyRUAAAAAAIDGENABAAAAAADQGAI6AAAAAAAAGkNABwAAAAAAQGMI6AAAUA1e/P746DcPJmUUUhUAAADwAwI6AABUgy+3Zy1ZlXEs20ZVAAAAwA8I6AAAUA2CTXqdxWDQK1QFAAAA/ICADgAAAGqM3W7fsmXLv/71L6fT6edCV61a5U3ijIyMb7/9NiUlhTcLABBQjFQBAABAAFq9evWSJUu2bt1qtVpjY2OHDBly8803y4MLS6b6888/P/300x9//DEvL89sNnfp0mXEiBH9+vULCQm5sKKXLl0qyQoKCqKiooYOHTp27NiEhISKj8tms82bNy8sLOzOO+/U6/WZmZlXXnll06ZNt23b5re6dRc6YMCA8yZ+//33J02a9K9//SsxMZFmCQAIHJyhAwAAEFiSk5Ovv/76/v37L1q0yOl0BgcH79u3b+LEiX369NmyZUtlk6nsdvuzzz7bsWPH6dOnnzp1ymg0njlz5u233x40aNDy5csrm6dsHDp0qCT78MMPHQ5HSEjIsWPHnnzyya5du65evbrio1u1atWjjz565MgRvf7fX0QVRZGC/FzJZRYqxyKVU2KjeuqQ1BgtEwAQUAjoAAAABJCsrKwBAwZ88cUX06ZN27Nnz9atWzdt2iQP3nvvvcOHD48ZMyYzM9P7ZG4TJkyQlMOHD9+2bZsk+/333+Xnjh075s6d279//0oVfebMmWuvvXbFihXPPvusZ7JPPvkkJydn1KhR8ri8o3O5XK+//npYWNj48ePdGxWlBhafKl2oHP6VV145bty486YEACAQ8KcGAACAABIVFfXkk082bNhw4MCB7o2hoaHjxo3LyMiYNGnS999/f8stt3iZTN3+wQcfvP3223fdddc777zjDk/Ig47FKlt0RETE5MmT5ed1113nTmaxWG6++WabzfaPf/zjvffee/nll8s8OnW5nPHjx8fHxwdazVut1o0bN3bo0IFGCADQBAI6AAAAAURRlDvvvLPMpy6//HL5uX//fu+TiZycnGeffbZBgwYvvvhixSebeF/07bffXmaywYMHh4eH//rrr+UV8c4778jPe+65JwBrPiwsLCQkxGKx0AgBAJpAQAcAAKAmpaSkvPDCC926dRs3blzFAZesrCz5Wa9evYozLJHsxx9/lCKmT58eHR19wTvpZdEOh8Nut0dGRpb5bGpq6scffzxo0CDP04JU6no6v/zyy2effXbs2LEGDRpce+217mvBPKWnpy9ZsuT333+Xx507dx41alTptYrz8vLUU4EOHDjgdDqbN28+bNiwHj16lLfba9asUReKzs/PP3z48NSpU+UoIiIi7r33XvmpprFYLLm5uQsXLvztt9/kbbrkkktuuukm90LR8qoFCxYYDAZ3ni6XS36V0jt06OB5KhMAANWFgA4AAEBNWrhw4VtvvRUeHj5s2LCKIybvvPOOXq9XT5bxPtnatWvlp/sqqp07d548edJgMDRu3Lhp06Ze7qSXRS9evLigoKC8E3A++OADeXbixIkl4lbyq9FofO2112bMmBEVFWW321NSUuTXSZMmTZ8+3TPx0qVLJ0yYIPvfqFEj2Z9PPvlEXjJ//vxRo0a50+zZs2fIkCGHDh2qU6dOdHS00+mUV82aNWvKlCnPPfdcmSGzzZs3z507V1LabLaMjIzXX39dHickJNx2223ugI5k+9hjj0m2siU9Pf3jjz+Wl3z11Vdt27bVFS8mPW3atDKP+pZbbiGgAwDwCRcAAKiyy1/eqxv965q9OVQFKuunn35q3779fffdZ7VaK0i2ePFi+eb24IMPVpxb6WR9+vSJjIw8c+bM999/36VLF/eXQLPZfMMNN+zdu/e8e1hB0Tabbc+ePbt27dq+ffvzzz8fHh7+5JNPlplJdnZ2fHx8x44di4qKPLdnZGQkJCRYLJaRI0dKPpJhfn7+6tWrGzVqJIV+99137pRr1qzR6/UtWrRYt25dbm6uJFu/fn3Lli1lozzlTnb27Nl77733888/P378uORWWFj4+++/t2vXTnL74Ycf3IVGRUX16tVL/TUnJyc9PX3nzp0RERHdunWTF8qv8tNut8uzM2bMkNcmJib+7//+b1ZWlsPhSE1Nfeihh2TjFVdcoR6O7M+OHTt2/WX37t1btmxp2rRpUFDQr7/+SiMHAPgCAR0AAKoBAR1URUFBQcUJNm7caLFYevbsmZeXV6lkVqu1RYsWLVu2fOqpp2JiYu677761a9fu3r17w4YNjzzyiE6ni42N3b59+wUXnZaW5r7sSLz88svl5fPhhx9Kgvfee6/E9oyMjHr16iUmJp49e9Zz+9KlSyX92LFj1V+l9Hbt2kVFRe3fv98zmfwaGRnZuXPnisNh3377reT2+OOPuwv1DOioMjMzZWPv3r1LvFYN6MyZM6fE9q5duyqKsnPnzjJLfOyxx+RVb7/9Ns0bAOAjXHIFAABQwypeiHfPnj1Dhw5t3Ljxp59+GhISUqlkDofDZDLt37//yy+/XLly5cUXX+xO37t37/79+w8ZMuS+++5bt26d2Wy+gKKjoqJeeeWV/Pz8wsLCX3/9dc6cOcnJybKlRG6u4ruVx8bGjhgxonQmNputVatWYWFhnhv79esnW/bt26f+unXr1t27d0+ZMqV58+aeyeTXBx98cMaMGZKgZ8+e5VVOs2bN5Ofx48crqOeioiJ1V8t81rPqVMOGDZNCT548WTrxBx98MHv27Lvvvjswl38GAPw9ENABAAAIXCkpKWoQ5Kuvviq9+u95k5nNZr1eb7FYZHurVq1KvOraa6+97bbbPvzww99//71Pnz4XUHRwcPCYMWPUxxMmTFixYsXQoUPz8vLeffddzxWC161bt3nz5ueee67MhZkVRXE4HKU3mkwmdbFksW3bNvmZlJQ0efJkz8RSypYtW+TBrl273AGds2fPLl++fMOGDadPn27UqFHv3r0TEhIkQ3duF0AN93hSg1al85Rdvfvuu7t06TJnzhwaMADAdwjoAAAABKisrKxhw4YdPXp0w4YNbdq0uYBkBoMhMTHxwIEDoaGhZb728ssv//DDD/ft21cioONl0SUMGTLkgQcemDdv3vjx4y+55BL39ldeeSUoKOiOO+7w/tjVk8ndv54+fVp+7t69+9ChQyVSmkwmOYoGDRqov+7du3f06NHbt29v3769bExOTl68eLEaA6pKQKc0p9NZeqPs55gxY0JCQhYtWhQcHEwbBgD4DgEdAACAQFRQUDBy5MikpKRvvvnGczHjyia78sor5amNGzc2bNiweosuU8+ePefNm7dz5053QEfyWbFixa233tq4ceMLrg01XvP8888PHTq0gmRFRUX333//jh07li1bNmzYMHVjZmbmRx99NHHixPIup6pGUroc79KlS72PggEAcGH0VAEAAECgKSoquu2229auXbt48eL+/ftXJdn1118fHBz86quvlhnO2LBhg/xU771dqaLLo55BU79+ffcWdWHgCRMmVKVCevTooSjK/PnzK06Wmpq6fv36UaNGuaM5IiYmZvjw4bry18epLrNnz166dOlTTz1144030oYBAL5GQAcAAKCGJSUlZWVleW657777Pv/88y+++GLkyJEVvNCbZImJiRMnTtywYYN6tyZP69atW7BgQa9evTxX/D1vnqdOnbr55pvffPPN0k8dOHDgrbfeql+/fvfu3dUtmZmZCxcuvOyyy9xbLky7du2GDx/+9ddfq3fL8uS51LG5mHp9lqfs7Gxd8bo8FRRR4iKvylq7du3TTz8tOzlr1iyaNADAD7jkCgAAoCZ9+umnd999d9euXb/99tvQ0FC73f7MM8+8//77I0aMiI2NXbt2bYn0kqZbt25Op3Py5MkVJ7v44ovVVWMmTZq0cePGKVOm7Nu3b/z48U2aNDlz5szy5cufffbZkJCQuXPnGo3nvhN6U7TkmZOTs2nTJtlt2WHJrXXr1mFhYVlZWZJeijh+/PiiRYvc9zL/6KOPsrOzJ06cWMVakgN5+eWXt2/ffvvtt+/du/fGG2+MiYmRsr788su33npr3rx5o0ePlmTx8fGy84sXL5bKeeCBB+rWrSs7tm7dumnTpunOF9AJKrZnz57vvvuuUaNGhYWF7dq183IdnGPHjv3jH/+QauzXr9+HH34oNalud7lcCQkJgwYNop0DAKofd24HAKDqLn95r270r2v25lAVqKzZs2friteIyczMlF/T09MruDe5iIuLs9vtJ0+ePG+y/Px8dyk5OTkPP/yweuepqKgoNbTRs2fPTZs2udN4U7Sap+zqE088IfmocZCYmBg1ctS6devPPvvMnaEkbtKkScuWLQsKCso7fCnUZDJ17tzZm+1JSUnu4Ih7mecBAwZs2bLFnSYrK0s9tygyMrJZs2ayb7IDakBn9OjRFRf60ksvuQ82IiLi2LFjsnHKlCny6w8//FAisef2lStXlldpHTt2pJEDAHxBcfl+cTgAAP72rpi9b+3m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XnjB5oTPzMxUkNLC2ub5559fVte1SxOdcV8FFyWhN998U+8r/Wjjqs6WLVtUkoceeigjI+Oaa66xKtggsRLDzz//PGfOHAVBBT7FF7WJGlDxWttRm2iDbdq0UeJReRQfbSxZdVd4OuaYYyzPaTs2g70zoqyorRBvI8paVw2uYDRx4kS1g/bofxo5C3lKutqjDug555yTnZ2tMK1mUZRUgO7Xr5/98cR3rbASTmtodVVNNdJr7VqhMMB54KxSWkWn1meffaazpUOHDorXu3fvVtpQ1dQ+5557rh3QwNu8rJZ55513tC81i9ec/AB5gbxAXiAvEAoA8gJ5gbxAXmBAp7Y7ePCgotXZZ5+t6Pz999+rG5x66qnTpk1T+LDhdoUDryClbqAz/pZbbmnbtu15552nGK0OqbA7adKkCRMmqEto9R49etjUXC+//LKis3rdn/70p5tvvjkpKUlhdObMme+///6AAQPq1atnG9fCqampXbp0GTZsmDao/vzpp58qaOpTBdBrr71WPdBPr/a/rgKECqyQoZ0q8irsasnGjRur7ooCWlJdWl398ccf16f79++3vwyo4urGgcyNrx4+b948hX6VpF27dn/7299atWql99WGzz//vKK/Nn7yySfbm04bKuwqZKgBVTYF6Mcee0zLa+H58+ffcMMNKrOCkdrtrbfeeu2117TK0KFDu3btqgCtQvreoqyDpepod0p7WuuSSy657rrrVAUdDm1w3LhxaiKV0/+At5K0ArFeKze0bt1aYUvt2blzZwVoBTjlLct/Xo2vd/bs2WNFsttZV6xYoSpbMujVq5fnXdOBUOMoSSizqhYxMTE6HDpM7777rnah00ktmZCQoNIG2OZ277GflnHurwZAXiAvkBfICwB5gbxAXiAvVJ8QmqA6Bt2vuOIKhU714alTpyrAffLJJ3l5eXZ1ZanTm+lT9Yo777xTP9Vb1EkUanXeN2nSRL1L4UYdTJ1BvUVBX32pZ8+ejzzyiDao/tawYUNF6rFjx6qrKIbaRW76GR0drZCtiKAIrvf79u2rVKEXCv379u3z08nLXVcFUKWmTJmiYjdv3nz48OEqiUKwIuNfSmjjCxcuVCJxnpCnnyq/XQRY7iCxGlAtpiiQmJj4wAMPdOvWza7h7N2791133aUXisVffvml5+2XWviss8669NJLVUiVWaVSwrNrArds2WJP8tOKqpezlspmf1so9TZOfbp48eIlS5ZYBnr44YdbtmwZFRWVnJx800036fiWe/WjtrBo0aLff//dHnmo88FG9Pv06aOPtPqsWbN8W0M11Vq33nrrnYcMGjRIe1dM15mj7Sgxe935XC6teO655w4ZMqRBgwaqslLpPffc069fP+fphipP4G2uhZcuXapTUS1zzjnn+LZMRYsHkBfIC+QF8gJAXiAvkBfIC6gErtCplkH3tm3bqld/9NFHCxYsePPNN1evXq2z+corr6xfv76fqcIVWbZu3aqwroWPOeYYxWid93YPpAKiwo16hTqbeshVV12l5e1CNdtg06ZNPS+rs/tFbcpxZxlt0177v6my3HX1qeKOiqpyqrcrAq5Zs8aJL3bTqUL5+vXr1Q5aJqSEcowKHBsb67/1tPyuXbs2bdqk1507d1bGckZw09PTe/To0aJFi19++WXFihXamudEcTbHm1VNL5TnlL0UVpwGtxnanJho//UzP9nKlSu1gFpbQcfCnLWA3eRcbprRaTB37lztTiXRRubPn6/2VO1UbJ0GquOPP/64fft25VfPA6eGUn1tljs7FvZ4Qi2mBHzDDTdoCwqmFR10t+n6LamoCtrmZZddpoC7e/duRVsF68DbXK26fPlybU2VuvrqqyvaMgB5gbxAXiAvACAvkBfIC2BAp/ZSt9e5O2fOnJSUlDfeeEMnrg23K3A4t1x6jc6quyqUr1q1SjFFnTA5OVmr7N+/X3EnuIQWU7/VT8U4hUuvaxF9b5K0CbE8/2vBKJBnxflfV9FB/VYBNzo6WsVWNb0irMK0arpz5051WqUZxSNFc4WADRs2NGnSxP9VlM7Gta8TTzzRs7Qqg6J/YmKiXisBKJMpPXgW0usQOLPfV+4gqrVVfjW1XUfqtfFyh9uVlZctW6aApaD28MMPW1i0RxjYoyi1fbu803PjiqFdunTp06ePM6Kv5VWG4447TjFabwZyDWqpJ6Rn+2iPSUlJOsd27Nih861Cba7/Hk7LAOQF8gJ5gbwAgLxAXiAvgAGd2kvhqU2bNueff/6UKVNsiNSG27OysnwDtDrzypUr77//foVj9cOrrrpKnUfhTN1bXcJzbNWGM22u9UrHncOnrq74omKrS59++ukXX3yx71Vz6sCtW7fW+1qyW7duiuMq8GeffXbGGWeUOqu5msVm73c2rheqvlc1taJFKJvFvVrDgdKPiqRDpvxa0RFum6tf7RMVFaUU5XntqF0jamFx7ty5OjE8N66PmjVr1rdvX697ZdUyXu8cDvuDgI6Odm0nVeBtblfYVrplAPICeYG8QF4AQF4gL5AXwIBOreYMumdkZBx//PE23F5WZ54+fbqic5MmTZ599tmTTz7ZrrXbt2/f4MGD165d6yzZokULdR51+8WLF3fq1MnZYFhYmDqPutyRefyb9qJko7ijLKIyXHLJJeqltmubgd8CjWphE2Kp7p9++unOnTsXLFjw9ttv33LLLc7lfFZ9dfglS5bMmjVr0KBBqktyiT179ihFqfXsjk0LIlu3bt2yZYt217hx48TExGqtr7V2amrqokWLlG6dAltr++tUYWE6dvPnzw8qufT0mWeeiY+Pd4pq4+7/+te/Vq1atWbNmtWrV3fp0sWreXNKVGU/Lymzs02lDaVMeyRhy5Yt7YAG2OY6sctqGR1K/y0DkBfIC+QF8gIA8gJ5gbyAqsJoWXVxBt11uttwu5+L3+zBeAp5J5xwgla0K+ViYmJ0ujsjtXqne/fujRo1Ut+YNGnSTz/9FBsbq56mn+pXY8eO1UaOTPdQf1ZHPe+881SSX3755fXXX7fH+Fkg2LRpk80rZvXVz4YNGw4YMMAq8uqrr77wwgt79+5VUFbh9TM3N/eLL7546KGHxo8fb89NVDucfvrpWn7dunUTJ0602cjUGtrLW2+9pcoqWJxzzjnVOtarYnfr1q1BgwZ6/cEHHyicOa2tuLZ06VI/e7dpwH777TdVQRvRaZCUlFT/EMXB5s2b2xMZFTFnzpxZ3X88UdxcsWLF5s2brQpxcXE6RqNHj9Zppv/26NFD+VIHNMA218Jdu3a1e6TVMp7nYUpKis4HxuAB8gJ5gbxAXgDIC+QF8gJ54QjgCp1qpJP7sssuW7NmTe/evf1P5X3SSSd99dVXimvqDFpFYS41NVVhS++oq9gy6hiKztdff/2zzz67e/fuf/zjH9qsArpef/3116tXr16yZMnTTz+t/n9k0o+yzrx581auXDlu3LgNGzb06tVLvVT/nTZtWmRkpAJu27Zt7YZJhWBVSnHtjTfeUO99++2358yZo08TEhL0kSKC4oWilbJLenq6DdVfc8018+fPX79+vRpEkcVih6qpQKlPzzrrrAsuuEBlKHXC+SqhvTRp0uS6665TOlEL//3vf1cFmzZtquMya9YsBV/Fr1JXtCskdTRVI7WD0pj95cFzGdVaYVFVS0tLW7hw4a5du7Sv6jtYEREROglvv/12q4J2N3v2bFVBJVQFO3bsqEitIB5gm+usVml1Ho4cOVKBW+ehkk3r1q31/UDJRqsrUtv0ewDIC+QF8gJ5ASAvkBfIC+QFBnRcEIvt+jTPi/p0Nrds2fLf//63IpFnF7X7G21GevvvJZdcop6wbNmyUaNGTZ48WR+pF8XFxdkk505w11rXXnttRkaGutDevXsnTpxo1y4qKGhh9T3912ab99x+WfsN8J1S39dOk5KSVLVHH31UQfnzzz//8ssvVQyrfmJiomJu+/btbV0r0qBBg5Rg3nzzzW3bttlVeXYxoQ0Jq4kUIPr376+gpvjVoEGDxx9//JFHHlm7dq0SleKdNbKCePfu3f/5z38q6NiVe9qCllfZvGbbKut9HQg7Ul730/our9eKX8oZyij79+9/99137c8ISi3nnnvud999pzL4nglKqCtWrFiwYIG2prDleYWhQ+8os3bo0GHGjBkbN2785ptv/vrXvzqnkO98dX7SpFbRjvw/3FFl1rFQAB0zZoz9TUbnic05P3jwYJvJX8sE3ubarwK0WmbChAk6D9977z07xK1atTrjjDMU5bUYs50B5AXyAnmBvACQF8gL5AXyAgM6LojO8fHxPXr00Ov69et7nprqCccff7xnl9On6pw9e/a0C8+sbyjYPfPMM5MmTVqyZElaWpo6z2WXXda3b18F619//VXL22VpWljd6bbbbuvUqdO0adM2bNig/hkdHa00cOGFF3br1s0eWOi1/bL2G8g7Za1rvbRFixYvvvji1KlTFY9SUlL0vhbo0qXLxRdfrL7q+UcGbUGd9sorr1QhZ8+e/f333+/cudMuvFTdO3bs2Lt3b4UzG5zWmxbdlK4+++yzRYsWaeN6U2179tln9+nTR1V2orPK07Vr18zMTJXQafmy3teLxo0b25HSIfO/vLW28krnzp0VrbZv367joqIqR86cOVMJNSYmptTzQclVAVGHrFevXmoQe0qf78D8FVdcYU/727dvn9rKOYU8C+yHtq8Qr7UUWD0vtfWltlJ5brjhBmX01atXq1LHHnvsRRddpMb0/EoRYJs7LaPgrlylHKOWUYrVa0Vtna6W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fVZfenTG20Tu/fv3/+c///nNN9/83//934033uhMdabYoe795Zdfzp49W3Fc6x577LGnnXZanz59mjZtakFTy/z666/6OqUXWvGMM87o16/f1KlTp0yZsmvXrqSkJGWCK664wqKSfjlXr8vMzFTXsovi9PPVV1/99NNPVbzTTz9dXXH58uW2NXXUHj16aGvjxo3T1hRQnnvuuTZt2mgvgRQsQFYAVcFi5bBhw1JTU1X+lStXxsXFaZsqv31r9LMR1U6lXbZs2Q8//LBq1ap9+/apOqq7SnvZZZd16NBBq6tJffelWrz55puLFy/WCy2mA6HY5LkvhTYFqcmTJ3/99ddbtmzR0VQFL7zwQn21tVxbao0CPCJO4qlQe6pIekcLf/fdd7t3727WrJm25plxvYZmlF/VmJ9//rnaJz09PSEhoXPnzgq7LVq0KDW2WkPpy/qAAQPq1as3cOBAzwwHgLxAXjja8oJKpWUef/xx/Y5xzz33dOrUSS2gN3UU7rrrrjlz5qxdu1btsGPHDno3QF4gLxwlvy+omkoBanYdiyFDhtgAkD7SyakqPPHEE0oZKvy2bdvo4HD3gI66kzrSjz/+qH5iT3H7xz/+ceWVV+rUd0bWGzdu/NRTT+n70AUXXGChxFb8/fffH3744ZkzZyo42liyXqinvf32248++qgWtjHjPXv2vPXWW+oz+q+6veKI8oE2otdaXn1eMVffw2wwVZFi69atShI2qq2fWsDGYvXf2267zdmaDQ/r/QceeECL6YU+at++fYAFC/TAlBTAJkJTRIiPj//444+3b99uGeWjjz6aNGmSEoNX3PQNiPfee++aNWu03+BDVCR9y5w4ceJ99903YMAAG8t39lW3bt2OHTsqjCqgK7ppeR2j6dOnv/HGG/qqavuKjIxUW1nutDSgVtViCrWK+yNGjFCBfWN04EfE5hqoUHuqSBs2bFCRFi5caPFXS6rFunfv7nuhu92JrRo9//zzSlrauzZuzfL+++//+9//vvzyy31jtOqu8H3LLbeoiZYuXcrDaAHyAnnhKM8LQSV//W7UqNGoUaO0fFpamr2pU1fNoo/sF8769evTuwHyAnnhKMkL9uyzG264QVuwRKBGtoEeVaq4hKrZrFkz5lZD1Qx819SOrecrMurk1rl+4oknKjqnp6d7ntnqfsccc8z555+vF/a+zn5F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J9O74foBHevtzz//vML0li1bFJTV8Xbs2LF161YLTDrd1StycnLU8U455RS7PG/IkCE//fSTQoOCzvr16/Vfi0c2w7m+LQ0dOrRBgwaV+4VcucFWVBT74YcfvvvuO3X4Bx980Dqw/2QTYMEstlaoVGoEhb9Ro0ZZVFWzaAsKB23btlXk0sadvOKw6wPbtGkzf/58xTilussvv7xdu3b79u1bsmSJc09s5aKnjtf333+/cuVK1VRVHjBggA5Qenq6PTNSYfGFF15Q5DqcMZEKtadOFbXD119/vXPnTiUhtYySq21E1fR6IIJdHnn33Xc/9NBD+nqt/z733HNjx47VR1pRP2+99dYHHnigf//+Wp2xc4C8QF4gL5SVF9TI69ate+mll0JLBJXMufDss896VlMF0yl96qmnqswM6ADkBfLCHzsvqD3VjJ988onKoEMwb968uXPnemYNvWkHReuWe1UXENB4bs3uXuGvW7du77zzziWXXKL+kJmZqY5ntziqGyg06x2d8ePGjbvxxhu1QF5e3vHHHz969OgOHTooIigE2C2a6qLqGwrxI0aMUCSyu9a1qexDPAfgy3pfr//0pz/ZBOnakd2JajFRP8tay1k38IIFeUyJL/6/4elTxZHu3btrg/bsQK2rbWpH2p1z/aRv8fRz4MCBnTp1SktL0+vFixe//vrrii9FJRTXtKQzpVxZ5fF9X7s79thjtWsdODteejM1NdU2q4DoZ7g98CNSofbUwieeeOLIkSObN29ulbXjlZCQoGVsFc896rxSUhk+fLi2qfftpxrE/kyh1i43e3kWmFgMkBfIC0dnXrB7HHJLOKXlAk+AvEBeOGrzgppCVR4/fryKpNRgo0V2ruqFmkXl7NKly5gxY2yuIno3Dl9YbYjRLVq0GDt27Lfffjt16tS1a9eqO6mrhIeHH3fccb169brooouSkpKsK+p9vWjfvv1777338ccfz549e/fu3eoq6rFdu3a97rrr1Hm0gM1Bpf557rnnRkZG2uV2FkrKej+o5OK6unXrvvrqq+pjP/zwg3VdhRsVT327rLU8KxJIwawMHTt2dJ75FxMT4ydG2xzsDz/88MaNGz/77LN9+/apNc4+++wrrrhCL+zW1lIrZX8VnDBhwptvvrlw4UK9r8JoxTPPPFOtrdiqBVQM23Wp5SmrnLaLiRMnqqYzZszY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" alt="An image that shows an example network workflow of an OpenShift `MachineConfig` API operating in an OpenShift Container Platform environment." />
<figcaption>Example network workflow that shows an OpenShift <code>MachineConfig</code> API operating in an OpenShift Container Platform environment</figcaption>
</figure>

The following configuration options are supported for user-managed load balancers:

- Use a node selector to map the Ingress Controller to a specific set of nodes. You must assign a static IP address to each node in this set, or configure each node to receive the same IP address from the Dynamic Host Configuration Protocol (DHCP). Infrastructure nodes commonly receive this type of configuration.

- Target all IP addresses on a subnet. This configuration can reduce the effort required to maintain the load balancer, because you can create and destroy nodes within those networks without reconfiguring the load balancer targets. If you deploy your ingress pods by using a machine set on a smaller network, such as a `/27` or `/28`, you can simplify your load balancer targets.

  > [!TIP]
  > You can list all IP addresses that exist in a network by checking the machine config pool’s resources.

Before you configure a user-managed load balancer for your OpenShift Container Platform cluster, consider the following information:

- For a front-end IP address, you can use the same IP address for the front-end IP address, the Ingress Controller load balancer, and API load balancer. Check the vendor’s documentation for this capability.

- For a back-end IP address, ensure that an IP address for an OpenShift Container Platform control plane node does not change during the lifetime of the user-managed load balancer. You can achieve this by completing one of the following actions:

  - Assign a static IP address to each control plane node.

  - Configure each node to receive the same IP address from the DHCP every time the node requests a DHCP lease. Depending on the vendor, the DHCP lease might be in the form of an IP reservation or a static DHCP assignment.

- Manually define each node that runs the Ingress Controller in the user-managed load balancer for the Ingress Controller back-end service. For example, if the Ingress Controller moves to an undefined node, a connection outage can occur.

## Configuring a user-managed load balancer

You can configure an OpenShift Container Platform cluster to use a user-managed load balancer in place of the default load balancer.

> [!IMPORTANT]
> Before you configure a user-managed load balancer, ensure that you read the "Services for a user-managed load balancer" section.

Read the following prerequisites that apply to the service that you want to configure for your user-managed load balancer.

> [!NOTE]
> MetalLB, which runs on a cluster, functions as a user-managed load balancer.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

The following list details OpenShift API prerequisites:

</div>

- You defined a front-end IP address.

- TCP ports 6443 and 22623 are exposed on the front-end IP address of your load balancer. Check the following items:

  - Port 6443 provides access to the OpenShift API service.

  - Port 22623 can provide ignition startup configurations to nodes.

- The front-end IP address and port 6443 are reachable by all users of your system with a location external to your OpenShift Container Platform cluster.

- The front-end IP address and port 22623 are reachable only by OpenShift Container Platform nodes.

- The load balancer backend can communicate with OpenShift Container Platform control plane nodes on port 6443 and 22623.

The following list details Ingress Controller prerequisites:

- You defined a front-end IP address.

- TCP port 443 and port 80 are exposed on the front-end IP address of your load balancer.

- The front-end IP address, port 80 and port 443 are reachable by all users of your system with a location external to your OpenShift Container Platform cluster.

- The front-end IP address, port 80 and port 443 are reachable by all nodes that operate in your OpenShift Container Platform cluster.

- The load balancer backend can communicate with OpenShift Container Platform nodes that run the Ingress Controller on ports 80, 443, and 1936.

The following list details prerequisites for health check URL specifications:

You can configure most load balancers by setting health check URLs that determine if a service is available or unavailable. OpenShift Container Platform provides these health checks for the OpenShift API, Machine Configuration API, and Ingress Controller backend services.

The following example shows a Kubernetes API health check specification for a backend service:

``` terminal
Path: HTTPS:6443/readyz
Healthy threshold: 2
Unhealthy threshold: 2
Timeout: 10
Interval: 10
```

The following example shows a Machine Config API health check specification for a backend service:

``` terminal
Path: HTTPS:22623/healthz
Healthy threshold: 2
Unhealthy threshold: 2
Timeout: 10
Interval: 10
```

The following example shows a Ingress Controller health check specification for a backend service:

``` terminal
Path: HTTP:1936/healthz/ready
Healthy threshold: 2
Unhealthy threshold: 2
Timeout: 5
Interval: 10
```

<div>

<div class="title">

Procedure

</div>

1.  Configure the HAProxy Ingress Controller, so that you can enable access to the cluster from your load balancer on ports 6443, 22623, 443, and 80. Depending on your needs, you can specify the IP address of a single subnet or IP addresses from multiple subnets in your HAProxy configuration.

    <div class="formalpara">

    <div class="title">

    Example HAProxy configuration with one listed subnet

    </div>

    ``` terminal
    # ...
    listen my-cluster-api-6443
        bind 192.168.1.100:6443
        mode tcp
        balance roundrobin
      option httpchk
      http-check connect
      http-check send meth GET uri /readyz
      http-check expect status 200
        server my-cluster-master-2 192.168.1.101:6443 check inter 10s rise 2 fall 2
        server my-cluster-master-0 192.168.1.102:6443 check inter 10s rise 2 fall 2
        server my-cluster-master-1 192.168.1.103:6443 check inter 10s rise 2 fall 2

    listen my-cluster-machine-config-api-22623
        bind 192.168.1.100:22623
        mode tcp
        balance roundrobin
      option httpchk
      http-check connect
      http-check send meth GET uri /healthz
      http-check expect status 200
        server my-cluster-master-2 192.168.1.101:22623 check inter 10s rise 2 fall 2
        server my-cluster-master-0 192.168.1.102:22623 check inter 10s rise 2 fall 2
        server my-cluster-master-1 192.168.1.103:22623 check inter 10s rise 2 fall 2

    listen my-cluster-apps-443
        bind 192.168.1.100:443
        mode tcp
        balance roundrobin
      option httpchk
      http-check connect
      http-check send meth GET uri /healthz/ready
      http-check expect status 200
        server my-cluster-worker-0 192.168.1.111:443 check port 1936 inter 10s rise 2 fall 2
        server my-cluster-worker-1 192.168.1.112:443 check port 1936 inter 10s rise 2 fall 2
        server my-cluster-worker-2 192.168.1.113:443 check port 1936 inter 10s rise 2 fall 2

    listen my-cluster-apps-80
       bind 192.168.1.100:80
       mode tcp
       balance roundrobin
      option httpchk
      http-check connect
      http-check send meth GET uri /healthz/ready
      http-check expect status 200
        server my-cluster-worker-0 192.168.1.111:80 check port 1936 inter 10s rise 2 fall 2
        server my-cluster-worker-1 192.168.1.112:80 check port 1936 inter 10s rise 2 fall 2
        server my-cluster-worker-2 192.168.1.113:80 check port 1936 inter 10s rise 2 fall 2
    # ...
    ```

    </div>

    <div class="formalpara">

    <div class="title">

    Example HAProxy configuration with multiple listed subnets

    </div>

    ``` terminal
    # ...
    listen api-server-6443
        bind *:6443
        mode tcp
          server master-00 192.168.83.89:6443 check inter 1s
          server master-01 192.168.84.90:6443 check inter 1s
          server master-02 192.168.85.99:6443 check inter 1s
          server bootstrap 192.168.80.89:6443 check inter 1s

    listen machine-config-server-22623
        bind *:22623
        mode tcp
          server master-00 192.168.83.89:22623 check inter 1s
          server master-01 192.168.84.90:22623 check inter 1s
          server master-02 192.168.85.99:22623 check inter 1s
          server bootstrap 192.168.80.89:22623 check inter 1s

    listen ingress-router-80
        bind *:80
        mode tcp
        balance source
          server worker-00 192.168.83.100:80 check inter 1s
          server worker-01 192.168.83.101:80 check inter 1s

    listen ingress-router-443
        bind *:443
        mode tcp
        balance source
          server worker-00 192.168.83.100:443 check inter 1s
          server worker-01 192.168.83.101:443 check inter 1s

    listen ironic-api-6385
        bind *:6385
        mode tcp
        balance source
          server master-00 192.168.83.89:6385 check inter 1s
          server master-01 192.168.84.90:6385 check inter 1s
          server master-02 192.168.85.99:6385 check inter 1s
          server bootstrap 192.168.80.89:6385 check inter 1s

    listen inspector-api-5050
        bind *:5050
        mode tcp
        balance source
          server master-00 192.168.83.89:5050 check inter 1s
          server master-01 192.168.84.90:5050 check inter 1s
          server master-02 192.168.85.99:5050 check inter 1s
          server bootstrap 192.168.80.89:5050 check inter 1s
    # ...
    ```

    </div>

2.  Use the `curl` CLI command to verify that the user-managed load balancer and its resources are operational:

    1.  Verify that the cluster machine configuration API is accessible to the Kubernetes API server resource, by running the following command and observing the response:

        ``` terminal
        $ curl https://<loadbalancer_ip_address>:6443/version --insecure
        ```

        If the configuration is correct, you receive a JSON object in response:

        ``` json
        {
          "major": "1",
          "minor": "11+",
          "gitVersion": "v1.11.0+ad103ed",
          "gitCommit": "ad103ed",
          "gitTreeState": "clean",
          "buildDate": "2019-01-09T06:44:10Z",
          "goVersion": "go1.10.3",
          "compiler": "gc",
          "platform": "linux/amd64"
        }
        ```

    2.  Verify that the cluster machine configuration API is accessible to the Machine config server resource, by running the following command and observing the output:

        ``` terminal
        $ curl -v https://<loadbalancer_ip_address>:22623/healthz --insecure
        ```

        If the configuration is correct, the output from the command shows the following response:

        ``` terminal
        HTTP/1.1 200 OK
        Content-Length: 0
        ```

    3.  Verify that the controller is accessible to the Ingress Controller resource on port 80, by running the following command and observing the output:

        ``` terminal
        $ curl -I -L -H "Host: console-openshift-console.apps.<cluster_name>.<base_domain>" http://<load_balancer_front_end_IP_address>
        ```

        If the configuration is correct, the output from the command shows the following response:

        ``` terminal
        HTTP/1.1 302 Found
        content-length: 0
        location: https://console-openshift-console.apps.ocp4.private.opequon.net/
        cache-control: no-cache
        ```

    4.  Verify that the controller is accessible to the Ingress Controller resource on port 443, by running the following command and observing the output:

        ``` terminal
        $ curl -I -L --insecure --resolve console-openshift-console.apps.<cluster_name>.<base_domain>:443:<Load Balancer Front End IP Address> https://console-openshift-console.apps.<cluster_name>.<base_domain>
        ```

        If the configuration is correct, the output from the command shows the following response:

        ``` terminal
        HTTP/1.1 200 OK
        referrer-policy: strict-origin-when-cross-origin
        set-cookie: csrf-token=UlYWOyQ62LWjw2h003xtYSKlh1a0Py2hhctw0WmV2YEdhJjFyQwWcGBsja261dGLgaYO0nxzVErhiXt6QepA7g==; Path=/; Secure; SameSite=Lax
        x-content-type-options: nosniff
        x-dns-prefetch-control: off
        x-frame-options: DENY
        x-xss-protection: 1; mode=block
        date: Wed, 04 Oct 2023 16:29:38 GMT
        content-type: text/html; charset=utf-8
        set-cookie: 1e2670d92730b515ce3a1bb65da45062=1bf5e9573c9a2760c964ed1659cc1673; path=/; HttpOnly; Secure; SameSite=None
        cache-control: private
        ```

3.  Configure the DNS records for your cluster to target the front-end IP addresses of the user-managed load balancer. You must update records to your DNS server for the cluster API and applications over the load balancer. The following examples shows modified DNS records:

    ``` dns
    <load_balancer_ip_address>  A  api.<cluster_name>.<base_domain>
    A record pointing to Load Balancer Front End
    ```

    ``` dns
    <load_balancer_ip_address>   A apps.<cluster_name>.<base_domain>
    A record pointing to Load Balancer Front End
    ```

    > [!IMPORTANT]
    > DNS propagation might take some time for each DNS record to become available. Ensure that each DNS record propagates before validating each record.

4.  For your OpenShift Container Platform cluster to use the user-managed load balancer, you must specify the following configuration in your cluster’s `install-config.yaml` file:

    ``` yaml
    # ...
    platform:
      vsphere:
        loadBalancer:
          type: <loadBalancer_type>
        apiVIPs:
        - <api_ip>
        ingressVIPs:
        - <ingress_ip>
    # ...
    ```

    where:

    `<loadBalancer_type>`
    Specifies the load balancer type. Set to `UserManaged` to specify a user-managed load balancer for your cluster. The parameter defaults to `OpenShiftManagedDefault`, which denotes the default internal load balancer. For services defined in an `openshift-kni-infra` namespace, a user-managed load balancer can deploy the `coredns` service to pods in your cluster but ignores `keepalived` and `haproxy` services.

    `<api_ip>`
    Specifies the user-managed load balancer’s public IP address for the Kubernetes API. Mandatory parameter.

    `<ingress_ip>`
    Specifies the user-managed load balancer’s public IP address for ingress traffic. Mandatory parameter.

</div>

<div>

<div class="title">

Verification

</div>

1.  Use the `curl` CLI command to verify that the user-managed load balancer and DNS record configuration are operational:

    1.  Verify that you can access the cluster API, by running the following command and observing the output:

        ``` terminal
        $ curl https://api.<cluster_name>.<base_domain>:6443/version --insecure
        ```

        If the configuration is correct, you receive a JSON object in response:

        ``` json
        {
          "major": "1",
          "minor": "11+",
          "gitVersion": "v1.11.0+ad103ed",
          "gitCommit": "ad103ed",
          "gitTreeState": "clean",
          "buildDate": "2019-01-09T06:44:10Z",
          "goVersion": "go1.10.3",
          "compiler": "gc",
          "platform": "linux/amd64"
          }
        ```

    2.  Verify that you can access the cluster machine configuration, by running the following command and observing the output:

        ``` terminal
        $ curl -v https://api.<cluster_name>.<base_domain>:22623/healthz --insecure
        ```

        If the configuration is correct, the output from the command shows the following response:

        ``` terminal
        HTTP/1.1 200 OK
        Content-Length: 0
        ```

    3.  Verify that you can access each cluster application on port 80, by running the following command and observing the output:

        ``` terminal
        $ curl http://console-openshift-console.apps.<cluster_name>.<base_domain> -I -L --insecure
        ```

        If the configuration is correct, the output from the command shows the following response:

        ``` terminal
        HTTP/1.1 302 Found
        content-length: 0
        location: https://console-openshift-console.apps.<cluster-name>.<base domain>/
        cache-control: no-cacheHTTP/1.1 200 OK
        referrer-policy: strict-origin-when-cross-origin
        set-cookie: csrf-token=39HoZgztDnzjJkq/JuLJMeoKNXlfiVv2YgZc09c3TBOBU4NI6kDXaJH1LdicNhN1UsQWzon4Dor9GWGfopaTEQ==; Path=/; Secure
        x-content-type-options: nosniff
        x-dns-prefetch-control: off
        x-frame-options: DENY
        x-xss-protection: 1; mode=block
        date: Tue, 17 Nov 2020 08:42:10 GMT
        content-type: text/html; charset=utf-8
        set-cookie: 1e2670d92730b515ce3a1bb65da45062=9b714eb87e93cf34853e87a92d6894be; path=/; HttpOnly; Secure; SameSite=None
        cache-control: private
        ```

    4.  Verify that you can access each cluster application on port 443, by running the following command and observing the output:

        ``` terminal
        $ curl https://console-openshift-console.apps.<cluster_name>.<base_domain> -I -L --insecure
        ```

        If the configuration is correct, the output from the command shows the following response:

        ``` terminal
        HTTP/1.1 200 OK
        referrer-policy: strict-origin-when-cross-origin
        set-cookie: csrf-token=UlYWOyQ62LWjw2h003xtYSKlh1a0Py2hhctw0WmV2YEdhJjFyQwWcGBsja261dGLgaYO0nxzVErhiXt6QepA7g==; Path=/; Secure; SameSite=Lax
        x-content-type-options: nosniff
        x-dns-prefetch-control: off
        x-frame-options: DENY
        x-xss-protection: 1; mode=block
        date: Wed, 04 Oct 2023 16:29:38 GMT
        content-type: text/html; charset=utf-8
        set-cookie: 1e2670d92730b515ce3a1bb65da45062=1bf5e9573c9a2760c964ed1659cc1673; path=/; HttpOnly; Secure; SameSite=None
        cache-control: private
        ```

</div>

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

- In the directory that contains the installation program, initialize the cluster deployment by running the following command:

  ``` terminal
  $ ./openshift-install create cluster --dir <installation_directory> \
      --log-level=info
  ```

  - For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.

  - To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

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

# Creating registry storage

After you install the cluster, you must create storage for the registry Operator.

## Image registry removed during installation

On platforms that do not provide shareable object storage, the OpenShift Image Registry Operator bootstraps itself as `Removed`. This allows `openshift-installer` to complete installations on these platform types.

After installation, you must edit the Image Registry Operator configuration to switch the `managementState` from `Removed` to `Managed`. When this has completed, you must configure storage.

## Image registry storage configuration

The Image Registry Operator is not initially available for platforms that do not provide default storage. After installation, you must configure your registry to use storage so that the Registry Operator is made available.

Configure a persistent volume, which is required for production clusters. Where applicable, you can configure an empty directory as the storage location for non-production clusters.

You can also allow the image registry to use block storage types by using the `Recreate` rollout strategy during upgrades.

### Configuring registry storage for VMware vSphere

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

### Configuring block registry storage for VMware vSphere

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

For instructions about configuring registry storage so that it references the correct PVC, see [Configuring the registry for vSphere](../../../registry/configuring_registry_storage/configuring-registry-storage-vsphere.md#registry-configuring-storage-vsphere_configuring-registry-storage-vsphere).

# Telemetry access for OpenShift Container Platform

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

<div>

<div class="title">

Additional resources

</div>

- See [About remote health monitoring](../../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring) for more information about the Telemetry service

</div>

# Configuring network components to run on the control plane

You can configure networking components to run exclusively on the control plane nodes. By default, OpenShift Container Platform allows any node in the machine config pool to host the `ingressVIP` virtual IP address. However, some environments deploy compute nodes in separate subnets from the control plane nodes, which requires configuring the `ingressVIP` virtual IP address to run on the control plane nodes.

> [!NOTE]
> You can scale the remote nodes by creating a compute machine set in a separate subnet.

> [!IMPORTANT]
> When deploying remote nodes in separate subnets, you must place the `ingressVIP` virtual IP address exclusively with the control plane nodes.

<figure>
<img src="data:image/png;base64,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juSSudVqNZlMgiAMHDgw24/8/f3nzZs3ceLEPPkWTogKAAAAPNZjX+wqVapE57CmpqY6DwqCsHbt2l69elWtWrVevXqffvrppUuXsn1wx44do0eP3rFjh+vB8+fPf/rpp//9739pLHHu3LmxY8fOmDFDo9EoFIqRI0dOnDhx7NixVquVpnc4HL///nvXrl0rV65cv379r776KiMjI1spH3/8cWRkpCiKs2fPrlKlysCBA2VZzqNTUpQolcrFixfbbDZCyLp161x/JMsyxz1+HDjHca6nS5bladOm6fV6X1/fsWPHPvYj/v7+/v7+7lSJYRg6xj3n7xU4tWvXrnv37iqV6ocffnD+5lOCICxfvrxTp04ajeb111/Pysp6UiYsy4qiyHHcn3/++djf/5xTyV8QogIAAACPJctyztb6mzdv0jcV59Bzi8XStWvXwYMH7927NyEh4datW0uWLKlTp84ff/zh+sFdu3YtXLhw165drgcvXLgwd+7c+fPn06jg/Pnz8+fPP3XqFMdxLMuuWrVq9uzZ8+fPpyVaLJZOnToNGjRo//79ZrP5xo0b06dPr1SpkmsEsmvXrkWLFm3ZsuXrr7+eOHFiYmLikSNHvDMqIIRUrFixbNmyWq128+bNrieB47i4uLj0x4mLi3MNGKxW66lTp+x2+/Dhw59p+anHBh7nz5+PjY0lhJQpU+bFvpmHGzRokNlstlqtV65ccT1usVhCQ0OXLl1qtVqtVuvQoUOflIOPj0/79u1Zlp06dWrXrl1//PHHbdu2JSQkWCyWfKozogIAAACPxXFccnKy4192u/3ChQtDhgxRq9WSJHXu3JkQIsty//79T548qdFovv322/v379++fbtPnz56vb5///6ugxxyzoYkhGg0Gq1WW6xYMdpyOWDAgKysrG+//dZisUiSdP36dZPJlJWV5efnJ8vyq6++eurUqbp16x49ejQ2NvbWrVutW7e22WydOnUymUzOUuiw9a1btx4/fjw+Pv6xI528BMuyHTp0sNvtN27ccG2e12g0GzZsKPk4GzZscH37dzgcVqtVEITq1as/U9Ecx926dcsZbCQkJKxevbpHjx4cxzkcjr59++bZl/REDRo0oH8RMTExrscZhrHb7T4+Pn/++afFYtm6deuWLVsemwPDMH/++Wfjxo2tVmtkZOT777//+uuvly9fvkyZ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zOl/4oknvv/++507d5aUlJw9e3bZsmUbN24sLy/vZlNzWUvmh/Gjbnad9fX106dPnzx58tdff927d++TJ08uXbo0dD3V1dXJZDJsX5A9cje7g9AIv/vuu++8887mzZuvvfbasEX0vn37wmqQ+vr6qVOndvlaQum8F198MawVycvLW7t27bZt2zZs2NC7d+9ffvnllVdeWbNmTXFx8aeffrpixYrwueL1119///33r7766tbW1pqamtbW1lDGtKKiYs6cOUZYoJsu+xSFxsbGhQsXvvHGG2VlZWfOnGlqaiooKCgqKioqKgr7y5w5cyZsAvXoo4+GYsk33XTTypUrw2KpUIyitrY2bC8f7irMnz//0jZ4am5unjlz5tChQ8+ePRv2qzp06FBNTU13nhtqw73wwgszZ848c+ZMmIdaXV0dCs6cOnVqzJgxb775ZqgkfbEnlslkSkpKMpnM/v37a2pqQo91+vTp6667bvny5Z3N4G9sbJw4ceLtt98e7hrv2rVr6dKlixYtWrVq1eHDhy9h24S2R77hhhvWrl1bVlYWJu0cPXq0srKyuro6Pz///Pnz27ZtO3DgwN+sk3NRl7ShoWHmzJmPPfZYOp0OGamhoWHv3r0nT54cPHhwSUlJ20uUyWRaWlqef/75sPA3LHrevXt3VVVVOp0uLCysrKz8/PPPwzS29evXHzx4MNzL+uKLLz788MMwKTadThcVFT355JNd1tju1avXjh073n777TAgN3LkyCVLltx6660LFy4Ms4PCEFd1dXWfPn2effbZ2267LZ1Oh8HFurq6AwcO1NfXh0UODQ0Nc+fOXbx4cdvljBCJvLy8CRMmZL9samoaN25cRUVFiOWZTGby5MnZKS4hM2RHiC5rE93c3NyrV68VK1aEXXeKioqqqqqWL18e/k6709Rc7kLDoUp1d7rOMLDy8ssvp1Kp06dP9+jRI4SHP/74o6CgYMiQIe26m252B8XFxVVVVZs3bw7LsisrK7du3bphw4adO3em0+kzZ87873//mzNnTu5Vv6F+xksvvbR3797CwsKGhoZHHnlk2rRpjz/++OjRo8M2NeHuazKZnD59+tNPP11cXJxOp/Pz8xsaGkKHnkwme/Tocfr06fLy8lCtzggLdNPlvVeQSCTCpMO5c+fefPPNW7du3bFjR01NzcmTJxOJRGlpaXl5+bRp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" alt="Installer-provisioned networking" />
</figure>

<div>

<div class="title">

Procedure

</div>

1.  Change to the directory storing the `install-config.yaml` file:

    ``` terminal
    $ cd ~/clusterconfigs
    ```

2.  Switch to the `manifests` subdirectory:

    ``` terminal
    $ cd manifests
    ```

3.  Create a file named `cluster-network-avoid-workers-99-config.yaml`:

    ``` terminal
    $ touch cluster-network-avoid-workers-99-config.yaml
    ```

4.  Open the `cluster-network-avoid-workers-99-config.yaml` file in an editor and enter a custom resource (CR) that describes the Operator configuration:

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfig
    metadata:
      name: 50-worker-fix-ipi-rwn
      labels:
        machineconfiguration.openshift.io/role: worker
    spec:
      config:
        ignition:
          version: 3.2.0
        storage:
          files:
            - path: /etc/kubernetes/manifests/keepalived.yaml
              mode: 0644
              contents:
                source: data:,
    ```

    This manifest places the `ingressVIP` virtual IP address on the control plane nodes. Additionally, this manifest deploys the following processes on the control plane nodes only:

    - `openshift-ingress-operator`

    - `keepalived`

5.  Save the `cluster-network-avoid-workers-99-config.yaml` file.

6.  Create a `manifests/cluster-ingress-default-ingresscontroller.yaml` file:

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: IngressController
    metadata:
      name: default
      namespace: openshift-ingress-operator
    spec:
      nodePlacement:
        nodeSelector:
          matchLabels:
            node-role.kubernetes.io/master: ""
    ```

7.  Consider backing up the `manifests` directory. The installer deletes the `manifests/` directory when creating the cluster.

8.  Modify the `cluster-scheduler-02-config.yml` manifest to make the control plane nodes schedulable by setting the `mastersSchedulable` field to `true`. Control plane nodes are not schedulable by default. For example:

        $ sed -i "s;mastersSchedulable: false;mastersSchedulable: true;g" clusterconfigs/manifests/cluster-scheduler-02-config.yml

    > [!NOTE]
    > If control plane nodes are not schedulable after completing this procedure, deploying the cluster will fail.

</div>

# Next steps

- [Customize your cluster](../../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations).

- If necessary, you can [Remote health reporting](../../../support/remote_health_monitoring/remote-health-reporting.md#remote-health-reporting).

- [Set up your registry and configure registry storage](../../../registry/configuring_registry_storage/configuring-registry-storage-vsphere.md#configuring-registry-storage-vsphere).

- Optional: [View the events from the vSphere Problem Detector Operator](../using-vsphere-problem-detector-operator.md#vsphere-problem-detector-viewing-events_vsphere-problem-detector) to determine if the cluster has permission or storage configuration issues.
