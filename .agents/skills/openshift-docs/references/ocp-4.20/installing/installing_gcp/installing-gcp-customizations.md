<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform version 4.17, you can install a cluster on Google Cloud by using installer-provisioned infrastructure with customizations, including network configuration options. In each, you modify parameters in the `install-config.yaml` file before you install the cluster.

By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations.

You must set most of the network configuration parameters during installation, and you can modify only `kubeProxy` configuration parameters in a running cluster.

# Prerequisites

- You reviewed details about the [OpenShift Container Platform installation and update](../../architecture/architecture-installation.md#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../overview/installing-preparing.md#installing-preparing).

- You [configured a Google Cloud project](installing-gcp-account.md#installing-gcp-account) to host the cluster.

- If you use a firewall, you [configured it to allow the sites](../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall) that your cluster requires access to.

# Internet access for OpenShift Container Platform

In OpenShift Container Platform 4.17, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

- Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.

- Access Quay.io to obtain the packages that are required to install your cluster.

- Obtain the packages that are required to perform cluster updates.

> [!IMPORTANT]
> If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

# Generating a key pair for cluster node SSH access

During an OpenShift Container Platform installation, you can provide an SSH public key to the installation program. The key is passed to the Red Hat Enterprise Linux CoreOS (RHCOS) nodes through their Ignition config files and is used to authenticate SSH access to the nodes. The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication.

The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication. After the key is passed to the nodes, you can use the key pair to SSH in to the RHCOS nodes as the user `core`. To access the nodes through SSH, the private key identity must be managed by SSH for your local user.

If you want to SSH in to your cluster nodes to perform installation debugging or disaster recovery, you must provide the SSH public key during the installation process. The `./openshift-install gather` command also requires the SSH public key to be in place on the cluster nodes.

> [!IMPORTANT]
> Do not skip this procedure in production environments, where disaster recovery and debugging is required.

> [!NOTE]
> You must use a local key, not one that you configured with platform-specific approaches.

<div>

<div class="title">

Procedure

</div>

1.  If you do not have an existing SSH key pair on your local machine to use for authentication onto your cluster nodes, create one. For example, on a computer that uses a Linux operating system, run the following command:

    ``` terminal
    $ ssh-keygen -t ed25519 -N '' -f <path>/<file_name>
    ```

    Specifies the path and file name, such as `~/.ssh/id_ed25519`, of the new SSH key. If you have an existing key pair, ensure your public key is in the your `~/.ssh` directory.

    > [!NOTE]
    > If you plan to install an OpenShift Container Platform cluster that uses the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the `x86_64`, `ppc64le`, and `s390x` architectures, do not create a key that uses the `ed25519` algorithm. Instead, create a key that uses the `rsa` or `ecdsa` algorithm.

2.  View the public SSH key:

    ``` terminal
    $ cat <path>/<file_name>.pub
    ```

    For example, run the following to view the `~/.ssh/id_ed25519.pub` public key:

    ``` terminal
    $ cat ~/.ssh/id_ed25519.pub
    ```

3.  Add the SSH private key identity to the SSH agent for your local user, if it has not already been added. SSH agent management of the key is required for password-less SSH authentication onto your cluster nodes, or if you want to use the `./openshift-install gather` command.

    > [!NOTE]
    > On some distributions, default SSH private key identities such as `~/.ssh/id_rsa` and `~/.ssh/id_dsa` are managed automatically.

    1.  If the `ssh-agent` process is not already running for your local user, start it as a background task:

        ``` terminal
        $ eval "$(ssh-agent -s)"
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Agent pid 31874
        ```

        </div>

        > [!NOTE]
        > If your cluster is in FIPS mode, only use FIPS-compliant algorithms to generate the SSH key. The key must be either RSA or ECDSA.

4.  Add your SSH private key to the `ssh-agent`:

    ``` terminal
    $ ssh-add <path>/<file_name>
    ```

    Specifies the path and file name for your SSH private key, such as `~/.ssh/id_ed25519`

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Identity added: /home/<you>/<path>/<file_name> (<computer_name>)
    ```

    </div>

</div>

<div>

<div class="title">

Next steps

</div>

- When you install OpenShift Container Platform, provide the SSH public key to the installation program.

</div>

# Obtaining the installation program

Before you install OpenShift Container Platform, download the installation file on the host you are using for installation.

<div>

<div class="title">

Prerequisites

</div>

- You have a computer that runs Linux or macOS, with 500 MB of local disk space.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to the [Cluster Type](https://console.redhat.com/openshift/install) page on the Red Hat Hybrid Cloud Console. If you have a Red Hat account, log in with your credentials. If you do not, create an account.

    > [!TIP]
    > You can also [download the binaries for a specific OpenShift Container Platform release](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/).

2.  Select your infrastructure provider from the **Run it yourself** section of the page.

3.  Select your host operating system and architecture from the dropdown menus under **OpenShift Installer** and click **Download Installer**.

4.  Place the downloaded file in the directory where you want to store the installation configuration files.

    <div class="important">

    <div class="title">

    </div>

    - The installation program creates several files on the computer that you use to install your cluster. You must keep the installation program and the files that the installation program creates after you finish installing the cluster. Both of the files are required to delete the cluster.

    - Deleting the files created by the installation program does not remove your cluster, even if the cluster failed during installation. To remove your cluster, complete the OpenShift Container Platform uninstallation procedures for your specific cloud provider.

    </div>

5.  Extract the installation program. For example, on a computer that uses a Linux operating system, run the following command:

    ``` terminal
    $ tar -xvf openshift-install-linux.tar.gz
    ```

6.  Download your installation [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.

    > [!TIP]
    > Alternatively, you can retrieve the installation program from the [Red Hat Customer Portal](https://access.redhat.com/downloads/content/290/), where you can specify a version of the installation program to download. However, you must have an active subscription to access this page.

</div>

# Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on Google Cloud.

<div>

<div class="title">

Prerequisites

</div>

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

- Configure a Google Cloud account.

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

        2.  Select **gcp** as the platform to target.

        3.  If you have not configured the service account key for your Google Cloud account on your computer, you must obtain it from Google Cloud and paste the contents of the file or enter the absolute path to the file.

        4.  Select the project ID to provision the cluster in. The default value is specified by the service account that you configured.

        5.  Select the region to deploy the cluster to.

        6.  Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster.

        7.  Enter a descriptive name for your cluster.

2.  Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.

    > [!NOTE]
    > If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that the cluster’s control planes are schedulable. For more information, see "Installing a three-node cluster on Google Cloud".

3.  Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

    > [!IMPORTANT]
    > The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for Google Cloud](installation-config-parameters-gcp.md#installation-config-parameters-gcp)

</div>

## Minimum resource requirements for cluster installation

Each created cluster must meet minimum requirements so that the cluster runs as expected.

| Machine | Operating System | vCPU <sup>\[1\]</sup> | Virtual RAM | Storage | Input/Output Per Second (IOPS)<sup>\[2\]</sup> |
|----|----|----|----|----|----|
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Minimum resource requirements

1.  One vCPU is equivalent to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.

2.  OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.

3.  As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Use of RHEL 7 compute machines is deprecated and has been removed in OpenShift Container Platform 4.10 and later.

> [!NOTE]
> For OpenShift Container Platform version 4.19, RHCOS is based on RHEL version 9.6, which updates the micro-architecture requirements. The following list contains the minimum instruction set architectures (ISA) that each architecture requires:
>
> - x86-64 architecture requires x86-64-v2 ISA
>
> - ARM64 architecture requires ARMv8.0-A ISA
>
> - IBM Power architecture requires Power 9 ISA
>
> - s390x architecture requires z14 ISA
>
> For more information, see "Architectures".

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

<div>

<div class="title">

Additional resources

</div>

- [Architectures (RHEL documentation)](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.2_release_notes/index#architectures)

</div>

<div>

<div class="title">

Additional resources

</div>

- [Optimizing storage](../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

</div>

## Tested instance types for Google Cloud

The following Google Cloud instance types have been tested with OpenShift Container Platform.

> [!NOTE]
> Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) (Google documentation).
>
> Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see [machine series support for Hyperdisk](https://cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in *Storage*.

<div class="example">

<div class="title">

Machine series

</div>

<https://raw.githubusercontent.com/openshift/installer/release-4.20/docs/user/gcp/tested_instance_types.md>

</div>

## Tested instance types for Google Cloud on 64-bit ARM infrastructures

The following Google Cloud 64-bit ARM instance types have been tested with OpenShift Container Platform.

<div class="example">

<div class="title">

Machine series for 64-bit ARM machines

</div>

<https://raw.githubusercontent.com/openshift/installer/release-4.20/docs/user/gcp/tested_instance_types_arm.md>

</div>

## Using custom machine types

Using a custom machine type to install a OpenShift Container Platform cluster is supported.

Consider the following when using a custom machine type:

- Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation".

- The name of the custom machine type must adhere to the following syntax:

  `custom-<number_of_cpus>-<amount_of_memory_in_mb>`

  For example, `custom-6-20480`.

As part of the installation process, you specify the custom machine type in the `install-config.yaml` file.

<div class="formalpara">

<div class="title">

Sample `install-config.yaml` file with a custom machine type

</div>

``` yaml
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  platform:
    gcp:
      type: custom-6-20480
  replicas: 2
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform:
    gcp:
      type: custom-6-20480
  replicas: 3
```

</div>

## Enabling Shielded VMs

You can use Shielded VMs when installing your cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. For more information, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).

> [!NOTE]
> Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures.

<div>

<div class="title">

Procedure

</div>

- Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1.  To use shielded VMs for only control plane machines:

      ``` yaml
      controlPlane:
        platform:
          gcp:
             secureBoot: Enabled
      ```

  2.  To use shielded VMs for only compute machines:

      ``` yaml
      compute:
      - platform:
          gcp:
             secureBoot: Enabled
      ```

  3.  To use shielded VMs for all machines:

      ``` yaml
      platform:
        gcp:
          defaultMachinePlatform:
             secureBoot: Enabled
      ```

</div>

## Enabling Confidential VMs

You can use Confidential VMs when installing your cluster. Confidential VMs encrypt data while it is being processed. For more information, see Google’s documentation on [Confidential Computing](https://cloud.google.com/confidential-computing). You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other.

> [!NOTE]
> Confidential VMs are currently not supported on 64-bit ARM architectures.

<div>

<div class="title">

Procedure

</div>

- Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1.  To use confidential VMs for only control plane machines:

      ``` yaml
      controlPlane:
        platform:
          gcp:
             confidentialCompute: AMDEncryptedVirtualizationNestedPaging
             type: n2d-standard-8
             onHostMaintenance: Terminate
      ```

      - Enable confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional Google Cloud configuration parameters".

      - Specify a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see [Supported operating systems and machine types](https://cloud.google.com/compute/confidential-vm/docs/os-and-machine-type#machine-type).

      - Specify the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration.

  2.  To use confidential VMs for only compute machines:

      ``` yaml
      compute:
      - platform:
          gcp:
             confidentialCompute: AMDEncryptedVirtualizationNestedPaging
             type: n2d-standard-8
             onHostMaintenance: Terminate
      ```

  3.  To use confidential VMs for all machines:

      ``` yaml
      platform:
        gcp:
          defaultMachinePlatform:
             confidentialCompute: AMDEncryptedVirtualizationNestedPaging
             type: n2d-standard-8
             onHostMaintenance: Terminate
      ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Additional Google Cloud configuration parameters](installation-config-parameters-gcp.md#installation-configuration-parameters-additional-gcp_installation-config-parameters-gcp)

</div>

## Enabling a user-managed DNS

You can install a cluster with a domain name server (DNS) solution that you manage instead of the default cluster-provisioned DNS solution. As a result, you can manage the API and Ingress DNS records in your own system rather than adding the records to the DNS of the cloud. For example, your organization’s security policies might not allow the use of public DNS services such as Google Cloud DNS. In such scenarios, you can use your own DNS service to bypass the public DNS service and manage your own DNS for the IP addresses of the API and Ingress services.

If you enable user-managed DNS during installation, the installation program provisions DNS records for the API and Ingress services only within the cluster. To ensure access from outside the cluster, you must provision the DNS records in an external DNS service of your choice for the API and Ingress services after installation.

> [!IMPORTANT]
> User-provisioned DNS is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You installed the `jq` package.

</div>

<div>

<div class="title">

Procedure

</div>

- Before you deploy your cluster, use a text editor to open the `install-config.yaml` file and add the following stanza:

  - To enable user-managed DNS:

    ``` yaml
    featureSet: CustomNoUpgrade
    featureGates: ["GCPClusterHostedDNS=true"]

    # ...

    platform:
      gcp:
        userProvisionedDNS: Enabled
    ```

    - Enable DNS management.

</div>

For information about provisioning your DNS records for the API server and the Ingress services, see "Provisioning your own DNS records".

<div>

<div class="title">

Additional resources

</div>

- [Additional Google Cloud configuration parameters](installation-config-parameters-gcp.md#installation-configuration-parameters-additional-gcp_installation-config-parameters-gcp)

</div>

## Sample customized install-config.yaml file for Google Cloud

To specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters, you can customize the `install-config.yaml` file.

> [!IMPORTANT]
> This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it.

``` yaml
apiVersion: v1
baseDomain: example.com
pullSecret: '{"auths": ...}'
controlPlane:
  name: master
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
compute:
- name: worker
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
metadata:
  name: test-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  gcp:
    projectID: sample-project
    region: us-east1
```

where:

`controlPlane`
Specifies parameters that apply to control plane machines.

`compute`
Specifies parameters that apply to compute machines.

`networking`
Specifies parameters that apply to the cluster networking configuration. If you do not provide networking values, the installation program provides default values.

`platform`
Specifies parameters that apply to the infrastructure platform that hosts the cluster.

<div>

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for GCP](installation-config-parameters-gcp.md#installation-config-parameters-gcp)

- [Enabling customer-managed encryption keys for a compute machine set](../../machine_management/creating_machinesets/creating-machineset-gcp.md#machineset-enabling-customer-managed-encryption_creating-machineset-gcp)

</div>

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
    Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations.

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

# Managing user-defined labels and tags for Google Cloud

Google Cloud provides labels and tags that help to identify and organize the resources created for a specific OpenShift Container Platform cluster, making them easier to manage.

You can define labels and tags for each Google Cloud resource only during OpenShift Container Platform cluster installation.

> [!IMPORTANT]
> User-defined labels and tags are not supported for OpenShift Container Platform clusters upgraded to OpenShift Container Platform 4.17.

> [!NOTE]
> You cannot update the tags that are already added. Also, a new tag-supported resource creation fails if the configured tag keys or tag values are deleted.

<div class="formalpara">

<div class="title">

User-defined labels

</div>

User-defined labels and OpenShift Container Platform specific labels are applied only to resources created by OpenShift Container Platform installation program and its core components such as:

</div>

- Google Cloud filestore CSI Driver Operator

- Google Cloud PD CSI Driver Operator

- Image Registry Operator

- Machine API provider for Google Cloud

User-defined labels are not attached to the resources created by any other Operators or the Kubernetes in-tree components.

User-defined labels and OpenShift Container Platform labels are available on the following Google Cloud resources:

- Compute disk

- Compute forwarding rule

- Compute image

- Compute instance

- DNS managed zone

- Filestore backup

- Filestore instance

- Storage bucket

<div>

<div class="title">

Limitations to user-defined labels

</div>

- Labels for `ComputeAddress` are supported in the Google Cloud beta version. OpenShift Container Platform does not add labels to the resource.

</div>

<div class="formalpara">

<div class="title">

User-defined tags

</div>

User-defined tags are applied only to resources created by OpenShift Container Platform installation program and its core components, such as the following resources:

</div>

- Google Cloud FileStore CSI Driver Operator

- Google Cloud PD CSI Driver Operator

- Image Registry Operator

- Machine API provider for Google Cloud

User-defined tags are not attached to the resources created by any other Operators or the Kubernetes in-tree components.

User-defined tags are available on the following Google Cloud resources:

- Compute disk

- Compute instance

- Filestore backup

- Filestore instance

- Storage bucket

<div>

<div class="title">

Limitations to the user-defined tags

</div>

- Tags must not be restricted to particular service accounts, because Operators create and use service accounts with minimal roles.

- OpenShift Container Platform does not create any key and value resources of the tag.

- OpenShift Container Platform specific tags are not added to any resource.

</div>

<div>

<div class="title">

Additional resources

</div>

- For more information about identifying the `OrganizationID`, see: [OrganizationID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id)

- For more information about identifying the `ProjectID`, see: [ProjectID](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)

- For more information about labels, see [Labels Overview](https://cloud.google.com/resource-manager/docs/labels-overview).

- For more information about tags, see [Tags Overview](https://cloud.google.com/resource-manager/docs/tags/tags-overview).

</div>

## Criteria for user-defined labels and tags

Before configuring user-defined labels and tags for Google Cloud, consider the importance of meeting the requirements for these tag and labels to ensure proper resource governance.

The following list details the requirements for user-defined labels:

- A label key and value must have a minimum of 1 character and can have a maximum of 63 characters.

- A label key and value must contain only lowercase letters, numeric characters, an underscore (`_`), and a dash (`-`).

- A label key must start with a lowercase letter.

- You can configure a maximum of 32 labels per resource.

  - Each resource has a maximum of 64 labels, where OpenShift Container Platform reserves 32 labels for internal use.

The following list details the requirements for user-defined tags:

- Tag key and tag value must already exist. OpenShift Container Platform does not create the key and the value.

- A tag `parentID` can be either `OrganizationID` or `ProjectID`:

  - `OrganizationID` must consist of decimal numbers without leading zeros.

  - `ProjectID` must be 6 to 30 characters in length, that includes only lowercase letters, numbers, and hyphens.

  - `ProjectID` must start with a letter, and cannot end with a hyphen.

- A tag key must contain only uppercase and lowercase alphanumeric characters, a hyphen (`-`), an underscore (`_`), and a period (`.`).

- A tag value must contain only uppercase and lowercase alphanumeric characters and any of the following characters:

  - A colon (`:`)

  - A comma (`,`)

  - A curly braces (`{}`)

  - A hyphen (`-`)

  - A parentheses (`()`)

  - A percent sign (`%`)

  - A plus (`+`)

  - A pound sign (`$`)

  - A space.

  - A square braces (`[]`)

  - An ampersand (`&`)

  - An asterisk (`*`)

  - An at sign (`@`)

  - An equals sign (`=`)

  - An underscore (`_`)

  - A period (`.`)

- A tag key and value must begin and end with an alphanumeric character.

- Tag value must be one of the predefined values for the key.

- You can configure a maximum of 50 tags.

- Do not define a tag key with the same value as any of the existing tag keys that get inherited from the parent resource.

## Configuring user-defined labels and tags for Google Cloud

Configuring user-defined labels and tags for Google Cloud means that you can apply key-value pairs to your cloud resources for the purposes of organizing, managing, and automating your infrastructure.

<div>

<div class="title">

Prerequisites

</div>

- The installation program requires that a service account includes a `TagUser` role, so that the program can create the OpenShift Container Platform cluster with defined tags at both organization and project levels.

</div>

<div>

<div class="title">

Procedure

</div>

- Update the `install-config.yaml` file to define the list of required labels and tags.

  > [!NOTE]
  > If you set labels and tags during creation of the `install-config.yaml` configuration file, you cannot create new or update existing labels and tags after creation of the cluster.

  <div class="formalpara">

  <div class="title">

  Sample `install-config.yaml` file

  </div>

  ``` yaml
  apiVersion: v1
  credentialsMode: Passthrough
  platform:
   gcp:
     userLabels:
     - key: <label_key>
       value: <label_value>
     userTags:
     - parentID: <OrganizationID/ProjectID>
       key: <tag_key_short_name>
       value: <tag_value_short_name>
  # ...
  ```

  </div>

  - In passthrough mode, the Cloud Credential Operator (CCO) passes the provided cloud credential to the components that request cloud credentials.

  - Adds keys and values as labels to the resources created on Google Cloud.

  - Defines the label name.

  - Defines the label content.

  - Adds keys and values as tags to the resources created on Google Cloud.

  - The ID of the hierarchical resource where you defined the tags at the organization or the project level.

</div>

## Querying user-defined labels and tags for Google Cloud

After creating the OpenShift Container Platform cluster, you can access the list of the labels and tags defined for the Google Cloud resources in the `infrastructures.config.openshift.io/cluster` object as shown in the following sample `infrastructure.yaml` file.

<div class="formalpara">

<div class="title">

Sample `infrastructure.yaml` file

</div>

``` yaml
apiVersion: config.openshift.io/v1
kind: Infrastructure
metadata:
 name: cluster
spec:
 platformSpec:
   type: GCP
status:
 infrastructureName: <cluster_id>
 platform: GCP
 platformStatus:
   gcp:
     resourceLabels:
     - key: <label_key>
       value: <label_value>
     resourceTags:
     - key: <tag_key_short_name>
       parentID: <OrganizationID/ProjectID>
       value: <tag_value_short_name>
   type: GCP
```

</div>

- The cluster ID that is generated during cluster installation.

Along with the user-defined labels, resources have a label defined by the OpenShift Container Platform. The format of the OpenShift Container Platform labels is `kubernetes-io-cluster-<cluster_id>:owned`.

# Installing the OpenShift CLI on Linux

To manage your cluster and deploy applications from the command line on Linux, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the architecture from the **Product Variant** list.

3.  Select the appropriate version from the **Version** list.

4.  Click **Download Now** next to the **OpenShift v4.17 Linux Clients** entry and save the file.

5.  Unpack the archive:

    ``` terminal
    $ tar xvf <file>
    ```

6.  Place the `oc` binary in a directory that is on your `PATH`.

    To check your `PATH`, execute the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- After you install the OpenShift CLI, it is available using the `oc` command:

  ``` terminal
  $ oc <command>
  ```

</div>

# Installing the OpenShift CLI on Windows

To manage your cluster and deploy applications from the command line on Windows, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the appropriate version from the **Version** list.

3.  Click **Download Now** next to the **OpenShift v4.17 Windows Client** entry and save the file.

4.  Extract the archive with a ZIP program.

5.  Move the `oc` binary to a directory that is on your `PATH` variable.

    To check your `PATH` variable, open the command prompt and execute the following command:

    ``` terminal
    C:\> path
    ```

</div>

<div>

<div class="title">

Verification

</div>

- After you install the OpenShift CLI, it is available using the `oc` command:

  ``` terminal
  C:\> oc <command>
  ```

</div>

# Installing the OpenShift CLI on macOS

To manage your cluster and deploy applications from the command line on macOS, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the architecture from the **Product Variant** list.

3.  Select the appropriate version from the **Version** list.

4.  Click **Download Now** next to the **OpenShift v4.17 macOS Clients** entry and save the file.

    > [!NOTE]
    > For macOS arm64, choose the **OpenShift v4.17 macOS arm64 Client** entry.

5.  Unpack and unzip the archive.

6.  Move the `oc` binary to a directory on your `PATH` variable.

    To check your `PATH` variable, open a terminal and execute the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify your installation by using an `oc` command:

  ``` terminal
  $ oc <command>
  ```

</div>

# Alternatives to storing administrator-level secrets in the kube-system project

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must use one of the following alternatives:

- To manage long-term cloud credentials manually, follow the procedure in [Manually creating long-term credentials](installing-gcp-customizations.md#manually-create-iam_installing-gcp-customizations).

- To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in [Configuring a Google Cloud cluster to use short-term credentials](installing-gcp-customizations.md#installing-gcp-with-short-term-creds_installing-gcp-customizations).

## Manually creating long-term credentials

The Cloud Credential Operator (CCO) can be put into manual mode prior to installation in environments where the cloud identity and access management (IAM) APIs are not reachable, or the administrator prefers not to store an administrator-level credential secret in the cluster `kube-system` namespace.

<div>

<div class="title">

Procedure

</div>

1.  Add the following granular permissions to the Google Cloud account that the installation program uses:

    - compute.machineTypes.list

    - compute.regions.list

    - compute.zones.list

    - dns.changes.create

    - dns.changes.get

    - dns.managedZones.create

    - dns.managedZones.delete

    - dns.managedZones.get

    - dns.managedZones.list

    - dns.networks.bindPrivateDNSZone

    - dns.resourceRecordSets.create

    - dns.resourceRecordSets.delete

    - dns.resourceRecordSets.list

2.  If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

    <div class="formalpara">

    <div class="title">

    Sample configuration file snippet

    </div>

    ``` yaml
    apiVersion: v1
    baseDomain: example.com
    credentialsMode: Manual
    # ...
    ```

    </div>

3.  If you have not previously created installation manifest files, do so by running the following command:

    ``` terminal
    $ openshift-install create manifests --dir <installation_directory>
    ```

    where `<installation_directory>` is the directory in which the installation program creates files.

4.  Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

5.  Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ oc adm release extract \
      --from=$RELEASE_IMAGE \
      --credentials-requests \
      --included \
      --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
      --to=<path_to_directory_for_credentials_requests>
    ```

    where:

    `--included`
    Specifies only the manifests that your specific cluster configuration requires.

    `<path_to_directory_with_installation_configuration>`
    Specifies the location of the `install-config.yaml` file.

    `<path_to_directory_for_credentials_requests>`
    Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

    This command creates a YAML file for each `CredentialsRequest` object.

    <div class="formalpara">

    <div class="title">

    Sample `CredentialsRequest` object

    </div>

    ``` yaml
    apiVersion: cloudcredential.openshift.io/v1
    kind: CredentialsRequest
    metadata:
      name: <component_credentials_request>
      namespace: openshift-cloud-credential-operator
      ...
    spec:
      providerSpec:
        apiVersion: cloudcredential.openshift.io/v1
        kind: GCPProviderSpec
        predefinedRoles:
        - roles/storage.admin
        - roles/iam.serviceAccountUser
        skipServiceCheck: true
      ...
    ```

    </div>

6.  Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.

    <div class="formalpara">

    <div class="title">

    Sample `CredentialsRequest` object with secrets

    </div>

    ``` yaml
    apiVersion: cloudcredential.openshift.io/v1
    kind: CredentialsRequest
    metadata:
      name: <component_credentials_request>
      namespace: openshift-cloud-credential-operator
      ...
    spec:
      providerSpec:
        apiVersion: cloudcredential.openshift.io/v1
          ...
      secretRef:
        name: <component_secret>
        namespace: <component_namespace>
      ...
    ```

    </div>

    <div class="formalpara">

    <div class="title">

    Sample `Secret` object

    </div>

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: <component_secret>
      namespace: <component_namespace>
    data:
      service_account.json: <base64_encoded_gcp_service_account_file>
    ```

    </div>

    > [!IMPORTANT]
    > Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.

</div>

## Configuring a Google Cloud cluster to use short-term credentials

To install a cluster that is configured to use Google Cloud Workload Identity, you must configure the Cloud Credential Operator (CCO) utility and create the required Google Cloud resources for your cluster. Cluster Operators use the credentials created by the CCO. The installation program does not use these credentials.

### Configuring the Cloud Credential Operator utility

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

> [!NOTE]
> The `ccoctl` utility is a Linux binary that must run in a Linux environment.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform account with cluster administrator access.

- You have installed the OpenShift CLI (`oc`).

</div>

- You have added one of the following authentication options to the Google Cloud account that the `ccoctl` utility uses:

  - The **IAM Workload Identity Pool Admin** role

  - The following granular permissions:

    - `compute.projects.get`

    - `iam.googleapis.com/workloadIdentityPoolProviders.create`

    - `iam.googleapis.com/workloadIdentityPoolProviders.get`

    - `iam.googleapis.com/workloadIdentityPools.create`

    - `iam.googleapis.com/workloadIdentityPools.delete`

    - `iam.googleapis.com/workloadIdentityPools.get`

    - `iam.googleapis.com/workloadIdentityPools.undelete`

    - `iam.roles.create`

    - `iam.roles.delete`

    - `iam.roles.list`

    - `iam.roles.undelete`

    - `iam.roles.update`

    - `iam.serviceAccounts.create`

    - `iam.serviceAccounts.delete`

    - `iam.serviceAccounts.getIamPolicy`

    - `iam.serviceAccounts.list`

    - `iam.serviceAccounts.setIamPolicy`

    - `iam.workloadIdentityPoolProviders.get`

    - `iam.workloadIdentityPools.delete`

    - `resourcemanager.projects.get`

    - `resourcemanager.projects.getIamPolicy`

    - `resourcemanager.projects.setIamPolicy`

    - `storage.buckets.create`

    - `storage.buckets.delete`

    - `storage.buckets.get`

    - `storage.buckets.getIamPolicy`

    - `storage.buckets.setIamPolicy`

    - `storage.objects.create`

    - `storage.objects.delete`

    - `storage.objects.list`

<div>

<div class="title">

Procedure

</div>

1.  Set a variable for the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

2.  Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
    ```

    > [!NOTE]
    > Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.

3.  Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ oc image extract $CCO_IMAGE \
      --file="/usr/bin/ccoctl.<rhel_version>" \
      -a ~/.pull-secret
    ```

    For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid:

    - `rhel8`: Specify this value for hosts that use RHEL 8.

    - `rhel9`: Specify this value for hosts that use RHEL 9.

    > [!NOTE]
    > The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.

4.  Change the permissions to make `ccoctl` executable by running the following command:

    ``` terminal
    $ chmod 775 ccoctl
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:

  ``` terminal
  $ ./ccoctl
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  OpenShift credentials provisioning tool

  Usage:
    ccoctl [command]

  Available Commands:
    aws          Manage credentials objects for AWS cloud
    azure        Manage credentials objects for Azure
    gcp          Manage credentials objects for Google cloud
    help         Help about any command
    ibmcloud     Manage credentials objects for IBM Cloud
    nutanix      Manage credentials objects for Nutanix

  Flags:
    -h, --help   help for ccoctl

  Use "ccoctl [command] --help" for more information about a command.
  ```

  </div>

</div>

### Creating Google Cloud resources with the Cloud Credential Operator utility

You can use the `ccoctl gcp create-all` command to automate the creation of Google Cloud resources.

> [!NOTE]
> By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

You must have:

</div>

- Extracted and prepared the `ccoctl` binary.

<div>

<div class="title">

Procedure

</div>

1.  Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

2.  Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ oc adm release extract \
      --from=$RELEASE_IMAGE \
      --credentials-requests \
      --included \
      --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
      --to=<path_to_directory_for_credentials_requests>
    ```

    where:

    `--included`
    Specifies to include only the manifests that your specific cluster configuration requires.

    `<path_to_directory_with_installation_configuration>`
    Specifies the location of the `install-config.yaml` file.

    `<path_to_directory_for_credentials_requests>`
    Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

    > [!NOTE]
    > This command might take a few moments to run.

3.  Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:

    ``` terminal
    $ ccoctl gcp create-all \
      --name=<name> \
      --region=<gcp_region> \
      --project=<gcp_project_id> \
      --credentials-requests-dir=<path_to_credentials_requests_directory> \
      --key-storage-method=<key_storage_method>
    ```

    where:

    `<name>`
    Specifies the user-defined name for all created Google Cloud resources used for tracking. If you plan to install the Google Cloud Filestore Container Storage Interface (CSI) Driver Operator, retain this value.

    `<gcp_region>`
    Specifies the Google Cloud region in which cloud resources will be created.

    `<gcp_project_id>`
    Specifies the Google Cloud project ID in which cloud resources will be created.

    `<path_to_credentials_requests_directory>`
    Specifies the directory containing the files of `CredentialsRequest` manifests to create Google Cloud service accounts.

    > [!NOTE]
    > If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory:

  ``` terminal
  $ ls <path_to_ccoctl_output_dir>/manifests
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` text
  cluster-authentication-02-config.yaml
  openshift-cloud-controller-manager-gcp-ccm-cloud-credentials-credentials.yaml
  openshift-cloud-credential-operator-cloud-credential-operator-gcp-ro-creds-credentials.yaml
  openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
  openshift-cluster-api-capg-manager-bootstrap-credentials-credentials.yaml
  openshift-cluster-csi-drivers-gcp-pd-cloud-credentials-credentials.yaml
  openshift-image-registry-installer-cloud-credentials-credentials.yaml
  openshift-ingress-operator-cloud-credentials-credentials.yaml
  openshift-machine-api-gcp-cloud-credentials-credentials.yaml
  ```

  </div>

  You can verify that the IAM service accounts are created by querying Google Cloud. For more information, refer to Google Cloud documentation on listing IAM service accounts.

</div>

### Incorporating the Cloud Credential Operator utility manifests

To implement short-term security credentials managed outside the cluster for individual components, you must move the manifest files that the Cloud Credential Operator utility (`ccoctl`) created to the correct directories for the installation program.

<div>

<div class="title">

Prerequisites

</div>

- You have configured an account with the cloud platform that hosts your cluster.

- You have configured the Cloud Credential Operator utility (`ccoctl`).

- You have created the cloud provider resources that are required for your cluster with the `ccoctl` utility.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add the following granular permissions to the Google Cloud account that the installation program uses:

    - compute.machineTypes.list

    - compute.regions.list

    - compute.zones.list

    - dns.changes.create

    - dns.changes.get

    - dns.managedZones.create

    - dns.managedZones.delete

    - dns.managedZones.get

    - dns.managedZones.list

    - dns.networks.bindPrivateDNSZone

    - dns.resourceRecordSets.create

    - dns.resourceRecordSets.delete

    - dns.resourceRecordSets.list

2.  If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

    <div class="formalpara">

    <div class="title">

    Sample configuration file snippet

    </div>

    ``` yaml
    apiVersion: v1
    baseDomain: example.com
    credentialsMode: Manual
    # ...
    ```

    </div>

3.  If you have not previously created installation manifest files, do so by running the following command:

    ``` terminal
    $ openshift-install create manifests --dir <installation_directory>
    ```

    where `<installation_directory>` is the directory in which the installation program creates files.

4.  Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command:

    ``` terminal
    $ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
    ```

5.  Copy the `tls` directory that contains the private key to the installation directory:

    ``` terminal
    $ cp -a /<path_to_ccoctl_output_dir>/tls .
    ```

</div>

# Using the Google Cloud Marketplace offering

Using the Google Cloud Marketplace offering lets you deploy an OpenShift Container Platform cluster, which is billed on pay-per-use basis (hourly, per core) through Google Cloud, while still being supported directly by Red Hat.

By default, the installation program downloads and installs the Red Hat Enterprise Linux CoreOS (RHCOS) image that is used to deploy compute machines. To deploy an OpenShift Container Platform cluster using an RHCOS image from the Google Cloud Marketplace, override the default behavior by modifying the `install-config.yaml` file to reference the location of Google Cloud Marketplace offer.

> [!NOTE]
> You should only modify the RHCOS image for compute machines to use a Google Cloud Marketplace image. Control plane machines and infrastructure nodes do not require an OpenShift Container Platform subscription and use the public RHCOS default image by default, which does not incur subscription costs on your Google Cloud bill. Therefore, you should not modify the cluster default boot image or the control plane boot images. Applying the Google Cloud Marketplace image to them will incur additional licensing costs that cannot be recovered.

<div>

<div class="title">

Prerequisites

</div>

- You have an existing `install-config.yaml` file.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `compute.platform.gcp.osImage` parameters to specify the location of the Google Cloud Marketplace image:

    - Set the `project` parameter to `redhat-marketplace-public`

    - Set the `name` parameter to one of the following offers:

      OpenShift Container Platform
      `redhat-coreos-ocp-413-x86-64-202305021736`

      OpenShift Platform Plus
      `redhat-coreos-opp-413-x86-64-202305021736`

      OpenShift Kubernetes Engine
      `redhat-coreos-oke-413-x86-64-202305021736`

2.  Save the file and reference it when deploying the cluster.

</div>

<div class="formalpara">

<div class="title">

Sample `install-config.yaml` file that specifies a Google Cloud Marketplace image for compute machines

</div>

``` yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
# ...
compute:
  platform:
    gcp:
      osImage:
        project: redhat-marketplace-public
        name: redhat-coreos-ocp-413-x86-64-202305021736
# ...
```

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

5.  Remove the Kubernetes manifest files that define the control plane machines and compute `MachineSets`:

    ``` terminal
    $ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml
    ```

    Because you create and manage these resources yourself, you do not have to initialize them.

    - You can preserve the `MachineSet` files to create compute machines by using the machine API, but you must update references to them to match your environment.

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

<table id="gatewayConfig-object_installing-gcp-customizations">
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

<table id="gatewayconfig-ipv4-object_installing-gcp-customizations">
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

<table id="gatewayconfig-ipv6-object_installing-gcp-customizations">
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

<table id="nw-operator-cr-ipsec_installing-gcp-customizations">
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

# Deploying the cluster

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

> [!IMPORTANT]
> You can run the `create cluster` command of the installation program only once, during initial installation.

<div>

<div class="title">

Prerequisites

</div>

- You have configured an account with the cloud platform that hosts your cluster.

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

- You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Remove any existing Google Cloud credentials that do not use the service account key for the Google Cloud account that you configured for your cluster and that are stored in the following locations:

    - The `GOOGLE_CREDENTIALS`, `GOOGLE_CLOUD_KEYFILE_JSON`, or `GCLOUD_KEYFILE_JSON` environment variables

    - The `~/.gcp/osServiceAccount.json` file

    - The `gcloud cli` default credentials

2.  In the directory that contains the installation program, initialize the cluster deployment by running the following command:

    ``` terminal
    $ ./openshift-install create cluster --dir <installation_directory> \
        --log-level=info
    ```

    - For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.

    - To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

3.  Optional: You can reduce the number of permissions for the service account that you used to install the cluster.

    - If you assigned the `Owner` role to your service account, you can remove that role and replace it with the `Viewer` role.

    - If you included the `Service Account Key Admin` role, you can remove it.

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

# Provisioning your own DNS records

Before you use this feature, you must add the `userProvisionedDNS` parameter to the `install-config.yaml` file and enable the parameter. For more information, see "Enabling a user-managed DNS".

Use the IP address of the API server to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. Use the IP address of the Ingress service to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

> [!IMPORTANT]
> User-provisioned DNS is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You installed the `gcloud` CLI tool.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To find the IP address of the API server and then provision the corresponding DNS record, use the `gcloud` CLI to run the following command:

    ``` terminal
    $ gcloud compute forwarding-rules describe --global "${infra_id}-apiserver" --format json | jq -r .IPAddress
    ```

2.  Use the IP address to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

3.  Use the `gcloud` CLI to find the IP address of the Ingress service and then provision the corresponding DNS record.

    1.  To find the forwarding rule for the Ingress service, run the following command:

        ``` terminal
        $ ingress_forwarding_rule=$(gcloud compute target-pools list --format=json --filter="instances[]~${infra_id}" | jq -r .[].name)
        ```

    2.  To use the forwarding rule value to find the IP address of the Ingress service, run the following command:

        ``` terminal
        $ ingress_ip_address=$(gcloud compute forwarding-rules describe --region "${region}" "${ingress_forwarding_rule}" --format json | jq -r .IPAddress)
        ```

4.  Use the IP address to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Additional Google Cloud configuration parameters](installation-config-parameters-gcp.md#installation-configuration-parameters-additional-gcp_installation-config-parameters-gcp)

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

<div>

<div class="title">

Additional resources

</div>

- See [Accessing the web console](../../web_console/web-console.md#web-console) for more details about accessing and understanding the OpenShift Container Platform web console.

</div>

# Telemetry access for OpenShift Container Platform

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

<div>

<div class="title">

Additional resources

</div>

- See [About remote health monitoring](../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring) for more information about the Telemetry service

</div>

# Next steps

- [Customize your cluster](../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations).

- If necessary, you can [Remote health reporting](../../support/remote_health_monitoring/remote-health-reporting.md#remote-health-reporting).
