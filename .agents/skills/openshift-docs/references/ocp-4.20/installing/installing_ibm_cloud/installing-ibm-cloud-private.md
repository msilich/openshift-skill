<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform version 4.20, you can install a private cluster into an existing Virtual Private Cloud (VPC) on IBM Cloud®. The installation program provisions the rest of the required infrastructure, which you can further customize.

# Prerequisites for installing a cluster on IBM Cloud®

Before installing an OpenShift Container Platform cluster on IBM Cloud® by using installer-provisioned infrastructure, ensure that you have configured your IBM Cloud® account, firewall, and the `ccoctl` utility.

- You reviewed details about the OpenShift Container Platform installation and update processes.

- You read the documentation on selecting a cluster installation method and preparing it for users.

- You configured an IBM Cloud® account to host the cluster.

- If you use a firewall, you configured it to allow the sites that your cluster requires access to.

- You configured the `ccoctl` utility before you installed the cluster.

<div>

<div class="title">

Additional resources

</div>

- [OpenShift Container Platform installation and update](../../architecture/architecture-installation.md#architecture-installation)

- [Selecting a cluster installation method and preparing it for users](../overview/installing-preparing.md#installing-preparing)

- [Configuring an IBM Cloud® account](installing-ibm-cloud-account.md#installing-ibm-cloud-account)

- [Configuring your firewall](../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall)

- [Configuring IAM for IBM Cloud®](configuring-iam-ibm-cloud.md#configuring-iam-ibm-cloud)

</div>

# Private clusters

You can deploy a private OpenShift Container Platform cluster that does not expose external endpoints. Private clusters are accessible from only an internal network and are not visible to the internet.

By default, OpenShift Container Platform is provisioned to use publicly-accessible DNS and endpoints. A private cluster sets the DNS, Ingress Controller, and API server to private when you deploy your cluster. This means that the cluster resources are only accessible from your internal network and are not visible to the internet.

> [!IMPORTANT]
> If the cluster has any public subnets, load balancer services created by administrators might be publicly accessible. To ensure cluster security, verify that these services are explicitly annotated as private.

To deploy a private cluster, you must:

- Use existing networking that meets your requirements. Your cluster resources might be shared between other clusters on the network.

- Create a DNS zone using IBM Cloud® DNS Services and specify it as the base domain of the cluster. For more information, see "Using IBM Cloud® DNS Services to configure DNS resolution".

- Deploy from a machine that has access to:

  - The API services for the cloud to which you provision.

  - The hosts on the network that you provision.

  - The internet to obtain installation media.

# Private clusters in IBM Cloud

To create a private cluster on IBM Cloud®, you must provide an existing private VPC and subnets. The installation program must also resolve the DNS records that the cluster requires, and configures the Ingress Operator and API server for only internal traffic.

The cluster still requires access to internet to access the IBM Cloud® APIs.

The following items are not required or created when you install a private cluster:

- Public subnets

- Public network load balancers, which support public ingress

- A public DNS zone that matches the `baseDomain` for the cluster

The installation program does use the `baseDomain` that you specify to create a private DNS zone and the required records for the cluster. The cluster is configured so that the Operators do not create public records for the cluster and all cluster machines are placed in the private subnets that you specify.

## Limitations

Private clusters on IBM Cloud® are subject only to the limitations associated with the existing VPC that was used for cluster deployment.

# About using a custom VPC

You can deploy OpenShift Container Platform into the subnets of an existing IBM® Virtual Private Cloud (VPC) to avoid account limit constraints or comply with your company’s infrastructure guidelines.

Because the installation program cannot know what other components are in your existing subnets, it cannot choose subnet CIDRs and so forth. You must configure networking for the subnets to which you will install the cluster.

## Requirements for using your VPC

You must correctly configure the existing VPC and its subnets before you install the cluster. The installation program does not create the following components:

- NAT gateways

- Subnets

- Route tables

- VPC network

The installation program cannot:

- Subdivide network ranges for the cluster to use

- Set route tables for the subnets

- Set VPC options like DHCP

> [!NOTE]
> The installation program requires that you use the cloud-provided DNS server. Using a custom DNS server is not supported and causes the installation to fail.

## VPC validation

The VPC and all of the subnets must be in an existing resource group. The cluster is deployed to the existing VPC.

As part of the installation, specify the following in the `install-config.yaml` file:

- The name of the existing resource group that contains the VPC and subnets (`networkResourceGroupName`)

- The name of the existing VPC (`vpcName`)

- The subnets that were created for control plane machines and compute machines (`controlPlaneSubnets` and `computeSubnets`)

> [!NOTE]
> Additional installer-provisioned cluster resources are deployed to a separate resource group (`resourceGroupName`). You can specify this resource group before installing the cluster. If undefined, a new resource group is created for the cluster.

To ensure that the subnets that you provide are suitable, the installation program confirms the following:

- All of the subnets that you specify exist.

- For each availability zone in the region, you specify:

  - One subnet for control plane machines.

  - One subnet for compute machines.

- The machine CIDR that you specified contains the subnets for the compute machines and control plane machines.

> [!NOTE]
> Subnet IDs are not supported.

## Isolation between clusters

If you deploy OpenShift Container Platform to an existing network, the isolation of cluster services is reduced in the following ways:

- You can install multiple OpenShift Container Platform clusters in the same VPC.

- ICMP ingress is allowed to the entire network.

- TCP port 22 ingress (SSH) is allowed to the entire network.

- Control plane TCP 6443 ingress (Kubernetes API) is allowed to the entire network.

- Control plane TCP 22623 ingress (MCS) is allowed to the entire network.

# Internet access for OpenShift Container Platform

In OpenShift Container Platform 4.20, you require access to the internet to install your cluster.

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

    Specify the path and file name for your SSH private key, such as `~/.ssh/id_ed25519`.

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

Before you install OpenShift Container Platform, download the installation file on a bastion host on your cloud network or a machine that has access to the network through a VPN. This ensures that installation assets exist for deployment in your environment.

For more information about private cluster installation requirements, see "Private clusters".

<div>

<div class="title">

Prerequisites

</div>

- You have a machine that runs Linux, for example Red Hat Enterprise Linux 8, with 500 MB of local disk space.

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

# Exporting the API key

You must set the API key you created as a global variable; the installation program ingests the variable during startup to set the API key.

<div>

<div class="title">

Prerequisites

</div>

- You have created either a user API key or service ID API key for your IBM Cloud® account.

</div>

<div>

<div class="title">

Procedure

</div>

- Export your API key for your account as a global variable:

  ``` terminal
  $ export IC_API_KEY=<api_key>
  ```

</div>

> [!IMPORTANT]
> You must set the variable name exactly as specified; the installation program expects the variable name to be present during startup.

# Manually creating the installation configuration file

Installing the cluster requires that you manually create the installation configuration file.

<div>

<div class="title">

Prerequisites

</div>

- You have an SSH public key on your local machine for use with the installation program. You can use the key for SSH authentication onto your cluster nodes for debugging and disaster recovery.

- You have obtained the OpenShift Container Platform installation program and the pull secret for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an installation directory to store your required installation assets in:

    ``` terminal
    $ mkdir <installation_directory>
    ```

    > [!IMPORTANT]
    > You must create a directory. Some installation assets, such as bootstrap X.509 certificates have short expiration intervals, so you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

2.  Customize the provided sample `install-config.yaml` file template and save the file in the `<installation_directory>`.

    > [!NOTE]
    > You must name this configuration file `install-config.yaml`.

3.  Back up the `install-config.yaml` file so that you can use it to install many clusters.

    > [!IMPORTANT]
    > Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for IBM Cloud®](installation-config-parameters-ibm-cloud-vpc.md#installation-config-parameters-ibm-cloud-vpc)

</div>

## Minimum resource requirements for cluster installation

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

| Machine | Operating system | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
|----|----|----|----|----|----|
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Minimum resource requirements

> [!NOTE]
> In OpenShift Container Platform version 4.19, RHCOS uses RHEL version 9.6, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA):
>
> - x86-64 architecture requires x86-64-v2 ISA
>
> - ARM64 architecture requires ARMv8.0-A ISA
>
> - ppc64le architecture requires IBM® Power9 ISA
>
> - s390x architecture requires IBM® z14 ISA
>
> For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

<div>

<div class="title">

Additional resources

</div>

- [Optimizing storage](../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

</div>

## Tested instance types for IBM Cloud

Use these tested IBM Cloud® instance types to ensure compatibility when selecting machine types for your OpenShift Container Platform cluster.

See the following machine series:

<https://raw.githubusercontent.com/openshift/installer/release-4.20/docs/user/ibmcloud/tested_instance_types_x86_64.md>

## Sample customized install-config.yaml file for IBM Cloud

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or change the values of the required parameters.

> [!IMPORTANT]
> This sample YAML file is for reference only. You must obtain your `install-config.yaml` file by using the installation program and then change it.

``` yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    ibmcloud: {}
  replicas: 3
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    ibmcloud: {}
  replicas: 3
metadata:
  name: test-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  ibmcloud:
    region: eu-gb
    resourceGroupName: eu-gb-example-cluster-rg
    networkResourceGroupName: eu-gb-example-existing-network-rg
    vpcName: eu-gb-example-network-1
    controlPlaneSubnets:
      - eu-gb-example-network-1-cp-eu-gb-1
      - eu-gb-example-network-1-cp-eu-gb-2
      - eu-gb-example-network-1-cp-eu-gb-3
    computeSubnets:
      - eu-gb-example-network-1-compute-eu-gb-1
      - eu-gb-example-network-1-compute-eu-gb-2
      - eu-gb-example-network-1-compute-eu-gb-3
credentialsMode: Manual
publish: Internal
pullSecret: '{"auths": ...}'
fips: false
sshKey: ssh-ed25519 AAAA...
```

where:

`baseDomain`
Specifies the base domain of your cluster. This value is required.

`metadata.name`
Specifies the name of your cluster. This value is required.

`platform.ibmcloud.region`
Specifies the IBM Cloud® region to deploy the cluster to. This value is required.

`pullSecret`
Specifies your pull secret. This value is required.

`compute`
Specifies parameters where, if you do not supply values, the installation program uses the default value. The first line of the `compute` section must begin with a hyphen, `-`. Both sections currently define a single machine pool.

`compute.hyperthreading`
Specifies whether to enable or disable simultaneous multithreading, also known as Hyper-Threading. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

`controlPlane`
Specifies parameters where, if you do not supply values, the installation program uses the default value. The `controlPlane` section is a single mapping, and its first line must not begin with a hyphen. Only one control plane pool is used.

`controlPlane.hyperthreading`
Specifies whether to enable or disable simultaneous multithreading, also known as Hyper-Threading. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

> [!IMPORTANT]
> If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance. Use larger machine types, such as `n1-standard-8`, for your machines if you disable simultaneous multithreading.

`networking.clusterNetwork.cidr`
Specifies the CIDR. The machine CIDR must contain the subnets for the compute machines and control plane machines.

`networking.machineNetwork.cidr`
Specifies the CIDR. The CIDR must contain the subnets defined in `platform.ibmcloud.controlPlaneSubnets` and `platform.ibmcloud.computeSubnets`.

`networking.networkType`
Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

`platform.ibmcloud.resourceGroupName`
Specifies the name of an existing resource group. All installer-provisioned cluster resources are deployed to this resource group. If undefined, a new resource group is created for the cluster.

`platform.ibmcloud.networkResourceGroupName`
Specifies the name of the resource group that contains the existing virtual private cloud (VPC). The existing VPC and subnets must be in this resource group. The cluster is installed to this VPC.

`platform.ibmcloud.vpcName`
Specifies the name of an existing VPC.

`platform.ibmcloud.controlPlaneSubnets`
Specifies the name of the existing subnets to which to deploy the control plane machines. The subnets must belong to the VPC that you specified. Specify a subnet for each availability zone in the region.

`platform.ibmcloud.computeSubnets`
Specifies the name of the existing subnets to which to deploy the compute machines. The subnets must belong to the VPC that you specified. Specify a subnet for each availability zone in the region.

`publish`
Specifies how to publish the user-facing endpoints of your cluster. Set `publish` to `Internal` to deploy a private cluster. The default value is `External`.

`fips`
Specifies whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead.

> [!IMPORTANT]
> When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.

`sshKey`
Specifies the SSH key to use to access the machines in your cluster. This value is optional.

> [!NOTE]
> For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

## Configuring the cluster-wide proxy during installation

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

<div>

<div class="title">

Prerequisites

</div>

- You have an existing `install-config.yaml` file.

- You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, the proxy handles all cluster egress traffic, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object’s `spec.noProxy` field to bypass the proxy if necessary.

  > [!NOTE]
  > The `Proxy` object `status.noProxy` field includes the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration.
  >
  > For installations on Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Red Hat OpenStack Platform (RHOSP), the `Proxy` object `status.noProxy` field also includes the instance metadata endpoint (`169.254.169.254`).

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
    If you specify this value, the installation program generates a config map named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you specify `additionalTrustBundle` and at least one proxy setting, the `Proxy` object references the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the RHCOS trust bundle. You must set the `additionalTrustBundle` field unless an authority from the RHCOS trust bundle signs the proxy’s identity certificate.

    `additionalTrustBundlePolicy`
    Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when you configure an `http/https` proxy. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter.

    > [!NOTE]
    > The installation program does not support the proxy `readinessEndpoints` field.

    > [!NOTE]
    > If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:
    >
    > ``` terminal
    > $ ./openshift-install wait-for install-complete --log-level debug
    > ```

2.  Save the file and reference it when installing OpenShift Container Platform.

    The installation program creates a cluster-wide proxy named `cluster` that uses the proxy settings in the `install-config.yaml` file. If you do not give proxy settings, the installation program still creates a `cluster` `Proxy` object, but it has a nil `spec`.

    > [!NOTE]
    > Only the `Proxy` object named `cluster` is supported, and you cannot create additional proxies.

</div>

# Manually creating IAM

To install OpenShift Container Platform, the Cloud Credential Operator (CCO) must operate in manual mode. While the installation program configures the CCO for manual mode, you must specify the identity and access management secrets for your cloud provider.

You can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to create the required IBM Cloud® resources.

<div>

<div class="title">

Prerequisites

</div>

- You have configured the `ccoctl` binary.

- You have an existing `install-config.yaml` file.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `install-config.yaml` configuration file so that the file includes the `credentialsMode` parameter set to `Manual`.

    <div class="formalpara">

    <div class="title">

    Example `install-config.yaml` configuration file

    </div>

    ``` yaml
    apiVersion: v1
    baseDomain: cluster1.example.com
    credentialsMode: Manual
    compute:
    - architecture: amd64
      hyperthreading: Enabled
    ```

    </div>

    where:

    `credentialsMode`
    Specifies the CCO credentials mode. Set the value to `Manual`.

2.  To generate the manifests, run the following command from the directory that includes the installation program:

    ``` terminal
    $ ./openshift-install create manifests --dir <installation_directory>
    ```

3.  From the directory that includes the installation program, set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

4.  Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

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
    Specifies that only the manifests that your specific cluster configuration requires are included.

    `--install-config`
    Specifies the location of the `install-config.yaml` file.

    `--to`
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
        labels:
          controller-tools.k8s.io: "1.0"
        name: openshift-image-registry-ibmcos
        namespace: openshift-cloud-credential-operator
      spec:
        secretRef:
          name: installer-cloud-credentials
          namespace: openshift-image-registry
        providerSpec:
          apiVersion: cloudcredential.openshift.io/v1
          kind: IBMCloudProviderSpec
          policies:
          - attributes:
            - name: serviceName
              value: cloud-object-storage
            roles:
            - crn:v1:bluemix:public:iam::::role:Viewer
            - crn:v1:bluemix:public:iam::::role:Operator
            - crn:v1:bluemix:public:iam::::role:Editor
            - crn:v1:bluemix:public:iam::::serviceRole:Reader
            - crn:v1:bluemix:public:iam::::serviceRole:Writer
          - attributes:
            - name: resourceType
              value: resource-group
            roles:
            - crn:v1:bluemix:public:iam::::role:Viewer
    ```

    </div>

5.  Create the service ID for each credential request, assign the policies defined, create an API key, and generate the secret:

    ``` terminal
    $ ccoctl ibmcloud create-service-id \
      --credentials-requests-dir=<path_to_credential_requests_directory> \
      --name=<cluster_name> \
      --output-dir=<installation_directory> \
      --resource-group-name=<resource_group_name>
    ```

    where:

    `<path_to_credential_requests_directory>`
    Specifies the directory that has the files for the `CredentialsRequest` objects.

    `<cluster_name>`
    Specifies the name of the OpenShift Container Platform cluster.

    `<installation_directory>`
    Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which you run the commands. This parameter is optional.

    `<resource_group_name>`
    Specifies the name of the resource group used for scoping the access policies. This parameter is optional.

    > [!NOTE]
    > If you enabled Technology Preview features by using the `TechPreviewNoUpgrade` feature set for your cluster, you must include the `--enable-tech-preview` parameter in the configuration for the `CredentialsRequest` object.
    >
    > If you provided a wrong resource group name, the installation fails during the bootstrap phase. To find the correct resource group name, run the following command:
    >
    > ``` terminal
    > $ grep resourceGroupName <installation_directory>/manifests/cluster-infrastructure-02-config.yml
    > ```

</div>

<div>

<div class="title">

Verification

</div>

- Check that the appropriate secrets exist in the `manifests` directory of your cluster.

</div>

# Deploying the cluster

To deploy your OpenShift Container Platform cluster, you initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions the required infrastructure and completes the cluster setup.

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

- In the directory that contains the installation program, initialize the cluster deployment by running the following command:

  ``` terminal
  $ ./openshift-install create cluster --dir <installation_directory> \
      --log-level=info
  ```

  where:

  - `<installation_directory>`: Specifies the location of your customized `./install-config.yaml` file.

  - `--log-level`: Specifies the log level. To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

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

  The following example shows the expected output:

  ``` terminal
  ...
  INFO Install complete!
  INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
  INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
  INFO Login to the console with user: "kubeadmin", and password: "password"
  INFO Time elapsed: 36m22s
  ```

  <div class="important">

  <div class="title">

  </div>

  - The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.

  - It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

  </div>

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

4.  Click **Download Now** next to the **OpenShift v4.20 Linux Clients** entry and save the file.

5.  Unpack the archive:

    ``` terminal
    $ tar xvf <file>
    ```

6.  Place the `oc` binary in a directory that is on your `PATH`.

    To check your `PATH`, run the following command:

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

3.  Click **Download Now** next to the **OpenShift v4.20 Windows Client** entry and save the file.

4.  Extract the archive with a ZIP program.

5.  Move the `oc` binary to a directory that is on your `PATH` variable.

    To check your `PATH` variable, open the Command Prompt and run the following command:

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

4.  Click **Download Now** next to the **OpenShift v4.20 macOS Clients** entry and save the file.

    > [!NOTE]
    > For macOS arm64, choose the **OpenShift v4.20 macOS arm64 Client** entry.

5.  Extract the archive.

6.  Move the `oc` binary to a directory on your `PATH` variable.

    To check your `PATH` variable, open a terminal and run the following command:

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

# Logging in to the cluster by using the CLI

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and OpenShift Container Platform generates it during installation.

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

<div id="additional-resources_installing-ibm-cloud-private-console">

<div class="title">

Additional resources

</div>

- [Accessing the web console](../../web_console/web-console.md#web-console)

</div>

# Telemetry access for OpenShift Container Platform

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

# Additional resources

- [Customize your cluster](../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations)

- [About remote health monitoring](../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring)
