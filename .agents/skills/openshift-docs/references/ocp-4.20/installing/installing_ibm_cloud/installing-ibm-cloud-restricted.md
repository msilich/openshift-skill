<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform 4.17, you can install a cluster in a restricted network by creating an internal mirror of the installation release content that is accessible to an existing Virtual Private Cloud (VPC) on IBM Cloud®.

# Prerequisites

- You reviewed details about the [OpenShift Container Platform installation and update](../../architecture/architecture-installation.md#architecture-installation) processes.

- You [configured an IBM Cloud account](installing-ibm-cloud-account.md#installing-ibm-cloud-account) to host the cluster.

- You have a container image registry that is accessible to the internet and your restricted network. The container image registry should mirror the contents of the OpenShift image registry and contain the installation media. For more information, see [Mirroring images for a disconnected installation by using the oc-mirror plugin v2](../../disconnected/about-installing-oc-mirror-v2.md#about-installing-oc-mirror-v2).

- You have an existing VPC on IBM Cloud® that meets the following requirements:

  - The VPC contains the mirror registry or has firewall rules or a peering connection to access the mirror registry that is hosted elsewhere.

  - The VPC can access IBM Cloud® service endpoints using a public endpoint. If network restrictions limit access to public service endpoints, evaluate those services for alternate endpoints that might be available. For more information see [Access to IBM service endpoints](installing-ibm-cloud-restricted.md#access-to-ibm-service-endpoints_installing-ibm-cloud-restricted).

  You cannot use the VPC that the installation program provisions by default.

- If you plan on configuring endpoint gateways to use IBM Cloud® Virtual Private Endpoints, consider the following requirements:

  - Endpoint gateway support is currently limited to the `us-east` and `us-south` regions.

  - The VPC must allow traffic to and from the endpoint gateways. You can use the VPC’s default security group, or a new security group, to allow traffic on port 443. For more information, see [Allowing endpoint gateway traffic](installing-ibm-cloud-restricted.md#installation-ibm-cloud-configure-vpc-for-endpoint-gateways_installing-ibm-cloud-restricted).

- If you use a firewall, you [configured it to allow the sites](../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall) that your cluster requires access to.

- You configured the `ccoctl` utility before you installed the cluster. For more information, see [Configuring IAM for IBM Cloud](configuring-iam-ibm-cloud.md#configuring-iam-ibm-cloud).

# About installations in restricted networks

In OpenShift Container Platform 4.17, you can install a cluster in a restricted network without an active internet connection to obtain software components.

Depending on the cloud platform where you install the cluster, you can complete a restricted network installation by using either installer-provisioned infrastructure or user-provisioned infrastructure.

## Required internet access and an installation host

You complete the installation using a bastion host or portable device that can access both the internet and your closed network. You must use a host with internet access to:

- Download the installation program, the OpenShift CLI (`oc`), and the CCO utility (`ccoctl`).

- Use the installation program to locate the Red Hat Enterprise Linux CoreOS (RHCOS) image and create the installation configuration file.

- Use `oc` to extract `ccoctl` from the CCO container image.

- Use `oc` and `ccoctl` to configure IAM for IBM Cloud®.

## Access to a mirror registry

To complete a restricted network installation, you must create a registry that mirrors the contents of the OpenShift image registry and contains the installation media.

You can create this registry on a mirror host, which can access both the internet and your restricted network, or by using other methods that meet your organization’s security restrictions.

For more information on mirroring images for a disconnected installation, see "Additional resources".

## Access to IBM service endpoints

The installation program requires access to the following IBM Cloud® service endpoints:

- Cloud Object Storage

- DNS Services

- Global Search

- Global Tagging

- Identity Services

- Resource Controller

- Resource Manager

- VPC

> [!NOTE]
> If you are specifying an IBM® Key Protect for IBM Cloud® root key as part of the installation process, the service endpoint for Key Protect is also required.

By default, the public endpoint is used to access the service. If network restrictions limit access to public service endpoints, you can override the default behavior.

Before deploying the cluster, you can update the installation configuration file (`install-config.yaml`) to specify the URI of an alternate service endpoint. For more information on usage, see "Additional resources".

## Additional limits

Clusters in restricted networks have the following additional limitations and restrictions:

- The `ClusterVersion` status includes an `Unable to retrieve available updates` error.

- By default, you cannot use the contents of the Developer Catalog because you cannot access the required image stream tags.

<div>

<div class="title">

Additional resources

</div>

- [Mirroring images for a disconnected installation by using the oc-mirror plugin v2](../../disconnected/about-installing-oc-mirror-v2.md#about-installing-oc-mirror-v2)

- [Additional IBM Cloud configuration parameters](installation-config-parameters-ibm-cloud-vpc.md#installation-configuration-parameters-additional-ibm-cloud_installation-config-parameters-ibm-cloud-vpc)

</div>

# About using a custom VPC

In OpenShift Container Platform 4.17, you can deploy a cluster into the subnets of an existing IBM® Virtual Private Cloud (VPC). Deploying OpenShift Container Platform into an existing VPC can help you avoid limit constraints in new accounts or more easily abide by the operational constraints that your company’s guidelines set. If you cannot obtain the infrastructure creation permissions that are required to create the VPC yourself, use this installation option.

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

## Allowing endpoint gateway traffic

If you are using IBM Cloud® Virtual Private endpoints, your Virtual Private Cloud (VPC) must be configured to allow traffic to and from the endpoint gateways.

A VPC’s default security group is configured to allow all outbound traffic to endpoint gateways. Therefore, the simplest way to allow traffic between your VPC and endpoint gateways is to modify the default security group to allow inbound traffic on port 443.

> [!NOTE]
> If you choose to configure a new security group, the security group must be configured to allow both inbound and outbound traffic.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the IBM Cloud® Command Line Interface utility (`ibmcloud`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Obtain the identifier for the default security group by running the following command:

    ``` terminal
    $ DEFAULT_SG=$(ibmcloud is vpc <your_vpc_name> --output JSON | jq -r '.default_security_group.id')
    ```

2.  Add a rule that allows inbound traffic on port 443 by running the following command:

    ``` terminal
    $ ibmcloud is security-group-rule-add $DEFAULT_SG inbound tcp --remote 0.0.0.0/0 --port-min 443 --port-max 443
    ```

</div>

> [!NOTE]
> Be sure that your endpoint gateways are configured to use this security group.

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

# Downloading the RHCOS cluster image

The installation program requires the Red Hat Enterprise Linux CoreOS (RHCOS) image to install the cluster. While optional, downloading the Red Hat Enterprise Linux CoreOS (RHCOS) before deploying removes the need for internet access when creating the cluster.

Use the installation program to locate and download the Red Hat Enterprise Linux CoreOS (RHCOS) image.

<div>

<div class="title">

Prerequisites

</div>

- The host running the installation program has internet access.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Change to the directory that contains the installation program and run the following command:

    ``` terminal
    $ ./openshift-install coreos print-stream-json
    ```

2.  Use the output of the command to find the location of the IBM Cloud® image.

    ``` terminal
    .Example output
    ----
      "release": "415.92.202311241643-0",
      "formats": {
        "qcow2.gz": {
          "disk": {
            "location": "https://rhcos.mirror.openshift.com/art/storage/prod/streams/4.15-9.2/builds/415.92.202311241643-0/x86_64/rhcos-415.92.202311241643-0-ibmcloud.x86_64.qcow2.gz",
            "sha256": "6b562dee8431bec3b93adeac1cfefcd5e812d41e3b7d78d3e28319870ffc9eae",
            "uncompressed-sha256": "5a0f9479505e525a30367b6a6a6547c86a8f03136f453c1da035f3aa5daa8bc9"
    ----
    ```

3.  Download and extract the image archive. Make the image available on the host that the installation program uses to create the cluster.

</div>

# Manually creating the installation configuration file

Installing the cluster requires that you manually create the installation configuration file.

<div>

<div class="title">

Prerequisites

</div>

- You have obtained the OpenShift Container Platform installation program and the pull secret for your cluster.

- You have the `imageContentSourcePolicy.yaml` file that was created when you mirrored your registry.

- You have obtained the contents of the certificate for your mirror registry.

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

    When customizing the sample template, be sure to provide the information that is required for an installation in a restricted network:

    1.  Update the `pullSecret` value to contain the authentication information for your registry:

        ``` yaml
        pullSecret: '{"auths":{"<mirror_host_name>:5000": {"auth": "<credentials>","email": "you@example.com"}}}'
        ```

        For `<mirror_host_name>`, specify the registry domain name that you specified in the certificate for your mirror registry, and for `<credentials>`, specify the base64-encoded user name and password for your mirror registry.

    2.  Add the `additionalTrustBundle` parameter and value.

        ``` yaml
        additionalTrustBundle: |
          -----BEGIN CERTIFICATE-----
          ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
          -----END CERTIFICATE-----
        ```

        The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority, or the self-signed certificate that you generated for the mirror registry.

    3.  Define the network and subnets for the VPC to install the cluster in under the parent `platform.ibmcloud` field:

        ``` yaml
        vpcName: <existing_vpc>
        controlPlaneSubnets: <control_plane_subnet>
        computeSubnets: <compute_subnet>
        ```

        For `platform.ibmcloud.vpcName`, specify the name for the existing IBM Cloud Virtual Private Cloud (VPC) network. For `platform.ibmcloud.controlPlaneSubnets` and `platform.ibmcloud.computeSubnets`, specify the existing subnets to deploy the control plane machines and compute machines, respectively.

    4.  Add the image content resources, which resemble the following YAML excerpt:

        ``` yaml
        imageContentSources:
        - mirrors:
          - <mirror_host_name>:5000/<repo_name>/release
          source: quay.io/openshift-release-dev/ocp-release
        - mirrors:
          - <mirror_host_name>:5000/<repo_name>/release
          source: registry.redhat.io/ocp/release
        ```

        For these values, use the `imageContentSourcePolicy.yaml` file that was created when you mirrored the registry.

    5.  If network restrictions limit the use of public endpoints to access the required IBM Cloud® services, add the `serviceEndpoints` stanza to `platform.ibmcloud` to specify an alternate service endpoint.

        > [!NOTE]
        > You can specify only one alternate service endpoint for each service.

        <div class="formalpara">

        <div class="title">

        Example of using alternate services endpoints

        </div>

        ``` yaml
        # ...
        serviceEndpoints:
          - name: IAM
            url: <iam_alternate_endpoint_url>
          - name: VPC
            url: <vpc_alternate_endpoint_url>
          - name: ResourceController
            url: <resource_controller_alternate_endpoint_url>
          - name: ResourceManager
            url: <resource_manager_alternate_endpoint_url>
          - name: DNSServices
            url: <dns_services_alternate_endpoint_url>
          - name: COS
            url: <cos_alternate_endpoint_url>
          - name: GlobalSearch
            url: <global_search_alternate_endpoint_url>
          - name: GlobalTagging
            url: <global_tagging_alternate_endpoint_url>
        # ...
        ```

        </div>

    6.  Optional: Set the publishing strategy to `Internal`:

        ``` yaml
        publish: Internal
        ```

        By setting this option, you create an internal Ingress Controller and a private load balancer.

        > [!NOTE]
        > If you use the default value of `External`, your network must be able to access the public endpoint for IBM Cloud® Internet Services (CIS). CIS is not enabled for Virtual Private Endpoints.

3.  Back up the `install-config.yaml` file so that you can use it to install many clusters.

    > [!IMPORTANT]
    > Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step.

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

<div>

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for IBM Cloud®](installation-config-parameters-ibm-cloud-vpc.md#installation-config-parameters-ibm-cloud-vpc)

</div>

## Minimum resource requirements for cluster installation

Each created cluster must meet minimum requirements so that the cluster runs as expected.

| Machine | Operating System | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
|----|----|----|----|----|----|
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Minimum resource requirements

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

## Tested instance types for IBM Cloud

The following IBM Cloud® instance types have been tested with OpenShift Container Platform.

<div class="example">

<div class="title">

Machine series

</div>

<https://raw.githubusercontent.com/openshift/installer/release-4.20/docs/user/ibmcloud/tested_instance_types_x86_64.md>

</div>

## Sample customized install-config.yaml file for IBM Cloud

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters.

> [!IMPORTANT]
> This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and then modify it.

``` yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    ibm-cloud: {}
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
    region: us-east
    resourceGroupName: us-east-example-cluster-rg
    serviceEndpoints:
      - name: IAM
        url: https://private.us-east.iam.cloud.ibm.com
      - name: VPC
        url: https://us-east.private.iaas.cloud.ibm.com/v1
      - name: ResourceController
        url: https://private.us-east.resource-controller.cloud.ibm.com
      - name: ResourceManager
        url: https://private.us-east.resource-controller.cloud.ibm.com
      - name: DNSServices
        url: https://api.private.dns-svcs.cloud.ibm.com/v1
      - name: COS
        url: https://s3.direct.us-east.cloud-object-storage.appdomain.cloud
      - name: GlobalSearch
        url: https://api.private.global-search-tagging.cloud.ibm.com
      - name: GlobalTagging
        url: https://tags.private.global-search-tagging.cloud.ibm.com
    networkResourceGroupName: us-east-example-existing-network-rg
    vpcName: us-east-example-network-1
    controlPlaneSubnets:
      - us-east-example-network-1-cp-us-east-1
      - us-east-example-network-1-cp-us-east-2
      - us-east-example-network-1-cp-us-east-3
    computeSubnets:
      - us-east-example-network-1-compute-us-east-1
      - us-east-example-network-1-compute-us-east-2
      - us-east-example-network-1-compute-us-east-3
credentialsMode: Manual
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
fips: false
sshKey: ssh-ed25519 AAAA...
additionalTrustBundle: |
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
imageContentSources:
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
```

- Required.

- If you do not provide these parameters and values, the installation program provides the default value.

- The `controlPlane` section is a single mapping, but the `compute` section is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`, and the first line of the `controlPlane` section must not. Only one control plane pool is used.

- Enables or disables simultaneous multithreading, also known as Hyper-Threading. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

  > [!IMPORTANT]
  > If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance. Use larger machine types, such as `n1-standard-8`, for your machines if you disable simultaneous multithreading.

- The machine CIDR must contain the subnets for the compute machines and control plane machines.

- The CIDR must contain the subnets defined in `platform.ibmcloud.controlPlaneSubnets` and `platform.ibmcloud.computeSubnets`.

- The cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

- The name of an existing resource group. All installer-provisioned cluster resources are deployed to this resource group. If undefined, a new resource group is created for the cluster.

- Based on the network restrictions of the VPC, specify alternate service endpoints as needed. This overrides the default public endpoint for the service.

- Specify the name of the resource group that contains the existing virtual private cloud (VPC). The existing VPC and subnets should be in this resource group. The cluster will be installed to this VPC.

- Specify the name of an existing VPC.

- Specify the name of the existing subnets to which to deploy the control plane machines. The subnets must belong to the VPC that you specified. Specify a subnet for each availability zone in the region.

- Specify the name of the existing subnets to which to deploy the compute machines. The subnets must belong to the VPC that you specified. Specify a subnet for each availability zone in the region.

- For `<local_registry>`, specify the registry domain name, and optionally the port, that your mirror registry uses to serve content. For example, registry.example.com or registry.example.com:5000. For `<credentials>`, specify the base64-encoded user name and password for your mirror registry.

- Enables or disables FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead.

  > [!IMPORTANT]
  > The use of FIPS Validated or Modules in Process cryptographic libraries is only supported on OpenShift Container Platform deployments on the `x86_64` architecture.

- Optional: provide the `sshKey` value that you use to access the machines in your cluster.

- Provide the contents of the certificate file that you used for your mirror registry.

- Provide these values from the `metadata.name: release-0` section of the `imageContentSourcePolicy.yaml` file that was created when you mirrored the registry.

  > [!NOTE]
  > For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

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

# Manually creating IAM

Installing the cluster requires that the Cloud Credential Operator (CCO) operate in manual mode. While the installation program configures the CCO for manual mode, you must specify the identity and access management secrets for you cloud provider.

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

    - `credentialsMode`: Set the `credentialsMode` parameter to `Manual`.

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

    - `--included`: Includes only the manifests that your specific cluster configuration requires.

    - `<path_to_directory_with_installation_configuration>`: Specify the location of the `install-config.yaml` file.

    - `<path_to_directory_for_credentials_requests>`: Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

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

    - `<path_to_credential_requests_directory>`: Specify the directory containing the files for the `CredentialsRequest` objects.

    - `<cluster_name>`: Specify the name of the OpenShift Container Platform cluster.

    - `<installation_directory>`: Optional parameter. Specify the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which you run the commands.

    - `<resource_group_name>`: Optional parameter. Specify the name of the resource group used for scoping the access policies.

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

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

> [!IMPORTANT]
> You can run the `create cluster` command of the installation program only once, during initial installation.

<div>

<div class="title">

Prerequisites

</div>

- You have configured an account with the cloud platform that hosts your cluster.

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

  If the Red Hat Enterprise Linux CoreOS (RHCOS) image is available locally, the host running the installation program does not require internet access.

- You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Export the `OPENSHIFT_INSTALL_OS_IMAGE_OVERRIDE` variable to specify the location of the Red Hat Enterprise Linux CoreOS (RHCOS) image by running the following command:

    ``` terminal
    $ export OPENSHIFT_INSTALL_OS_IMAGE_OVERRIDE="<path_to_image>/rhcos-<image_version>-ibmcloud.x86_64.qcow2.gz"
    ```

2.  In the directory that contains the installation program, initialize the cluster deployment by running the following command:

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

<div id="additional-resources_installing-ibm-cloud-restricted-console">

<div class="title">

Additional resources

</div>

- [Accessing the web console](../../web_console/web-console.md#web-console)

</div>

# Post installation

Complete the following steps to complete the configuration of your cluster.

## Disabling the default software catalog sources

In a restricted network environment, you must disable the default catalogs as a cluster administrator.

Operator catalogs that source content provided by Red Hat and community projects are configured for the software catalog by default during an OpenShift Container Platform installation.

<div>

<div class="title">

Procedure

</div>

- Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object:

  ``` terminal
  $ oc patch OperatorHub cluster --type json \
      -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
  ```

  > [!TIP]
  > Alternatively, you can use the web console to manage catalog sources. From the **Administration** → **Cluster Settings** → **Configuration** → **OperatorHub** page, click the **Sources** tab, where you can create, update, delete, disable, and enable individual sources.

</div>

## Installing the policy resources into the cluster

Mirroring the OpenShift Container Platform content using the oc-mirror OpenShift CLI (oc) plugin creates resources, which include `catalogSource-certified-operator-index.yaml` and `imageContentSourcePolicy.yaml`.

- The `ImageContentSourcePolicy` resource associates the mirror registry with the source registry and redirects image pull requests from the online registries to the mirror registry.

- The `CatalogSource` resource is used by Operator Lifecycle Manager (OLM) Classic to retrieve information about the available Operators in the mirror registry, which lets users discover and install Operators.

  > [!NOTE]
  > OLM v1 uses the `ClusterCatalog` resource to retrieve information about the available cluster extensions in the mirror registry.
  >
  > The oc-mirror plugin v1 does not generate `ClusterCatalog` resources automatically; you must manually create them. The oc-mirror plugin v2 does, however, generate `ClusterCatalog` resources automatically.
  >
  > For more information on creating and applying `ClusterCatalog` resources, see "Adding a catalog to a cluster" in "Extensions".

After you install the cluster, you must install these resources into the cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have mirrored the image set to the registry mirror in the disconnected environment.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI as a user with the `cluster-admin` role.

2.  Apply the YAML files from the results directory to the cluster:

    ``` terminal
    $ oc apply -f ./oc-mirror-workspace/results-<id>/
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the `ImageContentSourcePolicy` resources were successfully installed:

    ``` terminal
    $ oc get imagecontentsourcepolicy
    ```

2.  Verify that the `CatalogSource` resources were successfully installed:

    ``` terminal
    $ oc get catalogsource --all-namespaces
    ```

</div>

# Telemetry access for OpenShift Container Platform

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

<div id="additional-resources_installing-ibm-cloud-restricted-telemetry">

<div class="title">

Additional resources

</div>

- [About remote health monitoring](../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring)

</div>

# Next steps

- [Customize your cluster](../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations).

- Optional: [Remote health reporting](../../support/remote_health_monitoring/remote-health-reporting.md#remote-health-reporting).
