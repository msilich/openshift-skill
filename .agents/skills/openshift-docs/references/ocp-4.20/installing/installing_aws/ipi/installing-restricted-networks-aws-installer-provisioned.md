<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform version 4.17, you can install a cluster on Amazon Web Services (AWS) in a restricted network by creating an internal mirror of the installation release content on an existing Amazon Virtual Private Cloud (VPC).

# Prerequisites

- You reviewed details about the [OpenShift Container Platform installation and update](../../../architecture/architecture-installation.md#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../../overview/installing-preparing.md#installing-preparing).

- You [mirrored the images for a disconnected installation](../../../disconnected/installing-mirroring-installation-images.md#installation-about-mirror-registry_installing-mirroring-installation-images) to your registry and obtained the `imageContentSources` data for your version of OpenShift Container Platform.

  > [!IMPORTANT]
  > Because the installation media is on the mirror host, you can use that computer to complete all installation steps.

- You have an existing VPC in AWS. When installing to a restricted network using installer-provisioned infrastructure, you cannot use the installer-provisioned VPC. You must use a user-provisioned VPC that satisfies one of the following requirements:

  - Contains the mirror registry

  - Has firewall rules or a peering connection to access the mirror registry hosted elsewhere

- You [configured an AWS account](../installing-aws-account.md#installing-aws-account) to host the cluster.

  > [!IMPORTANT]
  > If you have an AWS profile stored on your computer, it must not use a temporary session token that you generated while using a multi-factor authentication device. The cluster continues to use your current AWS credentials to create AWS resources for the entire life of the cluster, so you must use key-based, long-term credentials. To generate appropriate keys, see [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the AWS documentation. You can supply the keys when you run the installation program.

- You downloaded the AWS CLI and installed it on your computer. See [Install the AWS CLI Using the Bundled Installer (Linux, macOS, or UNIX)](https://docs.aws.amazon.com/cli/latest/userguide/install-bundle.html) in the AWS documentation.

- If you use a firewall and plan to use the Telemetry service, you [configured the firewall to allow the sites](../../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall) that your cluster requires access to.

  > [!NOTE]
  > If you are configuring a proxy, be sure to also review this site list.

# About installations in restricted networks

In OpenShift Container Platform 4.17, you can install a cluster in a restricted network without an active internet connection to obtain software components.

Depending on the cloud platform where you install the cluster, you can complete a restricted network installation by using either installer-provisioned infrastructure or user-provisioned infrastructure.

If you choose to perform a restricted network installation on a cloud platform, you still require access to its cloud APIs. Some cloud functions, like Amazon Web Service’s Route 53 DNS and IAM services, require internet access. Depending on your network, you might require less internet access for an installation on bare metal hardware, Nutanix, or on VMware vSphere.

To complete a restricted network installation, you must create a registry that mirrors the contents of the OpenShift image registry and contains the installation media. You can create this registry on a mirror host, which can access both the internet and your closed network, or by using other methods that meet your restrictions.

## Additional limits

Clusters in restricted networks have the following additional limitations and restrictions:

- The `ClusterVersion` status includes an `Unable to retrieve available updates` error.

- By default, you cannot use the contents of the Developer Catalog because you cannot access the required image stream tags.

# About using a custom VPC

In OpenShift Container Platform 4.17, you can deploy a cluster into existing subnets in an existing Amazon Virtual Private Cloud (VPC) in Amazon Web Services (AWS). By deploying OpenShift Container Platform into an existing AWS VPC, you might be able to avoid limit constraints in new accounts or more easily abide by the operational constraints that your company’s guidelines set. If you cannot obtain the infrastructure creation permissions that are required to create the VPC yourself, use this installation option.

Because the installation program cannot know what other components are also in your existing subnets, it cannot choose subnet CIDRs and so forth on your behalf. You must configure networking for the subnets that you install your cluster to yourself.

## Requirements for using your VPC

The installation program no longer creates the following components:

- Internet gateways

- NAT gateways

- Subnets

- Route tables

- VPCs

- VPC DHCP options

- VPC endpoints

> [!NOTE]
> The installation program requires that you use the cloud-provided DNS server. Using a custom DNS server is not supported and causes the installation to fail.

If you use a custom VPC, you must correctly configure it and its subnets for the installation program and the cluster to use. See [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html) in the Amazon Web Services documentation for more information about AWS VPC console wizard configurations and creating and managing an AWS VPC.

The installation program cannot:

- Subdivide network ranges for the cluster to use.

- Set route tables for the subnets.

- Set VPC options like DHCP.

You must complete these tasks before you install the cluster. See [VPC networking components](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Networking.html) and [Route tables for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) for more information on configuring networking in an AWS VPC.

Your VPC must meet the following characteristics:

- The VPC must not use the `kubernetes.io/cluster/.*: owned`, `Name`, and `openshift.io/cluster` tags.

  The installation program modifies your subnets to add the `kubernetes.io/cluster/.*: shared` tag, so your subnets must have at least one free tag slot available for it. See [Tag Restrictions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-restrictions) in the AWS documentation to confirm that the installation program can add a tag to each subnet that you specify. You cannot use a `Name` tag, because it overlaps with the EC2 `Name` field and the installation fails.

- If you want to extend your OpenShift Container Platform cluster into an AWS Outpost and have an existing Outpost subnet, the existing subnet must use the `kubernetes.io/cluster/unmanaged: true` tag. If you do not apply this tag, the installation might fail due to the Cloud Controller Manager creating a service load balancer in the Outpost subnet, which is an unsupported configuration.

- You must enable the `enableDnsSupport` and `enableDnsHostnames` attributes in your VPC, so that the cluster can use the Route 53 zones that are attached to the VPC to resolve cluster’s internal DNS records. See [DNS Support in Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support) in the AWS documentation.

  If you prefer to use your own Route 53 hosted private zone, you must associate the existing hosted zone with your VPC prior to installing a cluster. You can define your hosted zone using the `platform.aws.hostedZone` and `platform.aws.hostedZoneRole` fields in the `install-config.yaml` file. You can use a private hosted zone from another account by sharing it with the account where you install the cluster. If you use a private hosted zone from another account, you must use the `Passthrough` or `Manual` credentials mode.

If you are working in a disconnected environment, you are unable to reach the public IP addresses for EC2, ELB, and S3 endpoints. Depending on the level to which you want to restrict internet traffic during the installation, the following configuration options are available:

### Option 1: Create VPC endpoints

Create a VPC endpoint and attach it to the subnets that the clusters are using. Name the endpoints as follows:

- `ec2.<aws_region>.amazonaws.com`

- `elasticloadbalancing.<aws_region>.amazonaws.com`

- `s3.<aws_region>.amazonaws.com`

With this option, network traffic remains private between your VPC and the required AWS services.

### Option 2: Create a proxy without VPC endpoints

As part of the installation process, you can configure an HTTP or HTTPS proxy. With this option, internet traffic goes through the proxy to reach the required AWS services.

### Option 3: Create a proxy with VPC endpoints

As part of the installation process, you can configure an HTTP or HTTPS proxy with VPC endpoints. Create a VPC endpoint and attach it to the subnets that the clusters are using. Name the endpoints as follows:

- `ec2.<aws_region>.amazonaws.com`

- `elasticloadbalancing.<aws_region>.amazonaws.com`

- `s3.<aws_region>.amazonaws.com`

When configuring the proxy in the `install-config.yaml` file, add these endpoints to the `noProxy` field. With this option, the proxy prevents the cluster from accessing the internet directly. However, network traffic remains private between your VPC and the required AWS services.

<div class="formalpara">

<div class="title">

Required VPC components

</div>

You must provide a suitable VPC and subnets that allow communication to your machines.

</div>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 46%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Component</th>
<th style="text-align: left;">AWS type</th>
<th colspan="2" style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>VPC</p></td>
<td style="text-align: left;"><ul>
<li><p><code>AWS::EC2::VPC</code></p></li>
<li><p><code>AWS::EC2::VPCEndpoint</code></p></li>
</ul></td>
<td colspan="2" style="text-align: left;"><p>You must provide a public VPC for the cluster to use. The VPC uses an endpoint that references the route tables for each subnet to improve communication with the registry that is hosted in S3.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Public subnets</p></td>
<td style="text-align: left;"><ul>
<li><p><code>AWS::EC2::Subnet</code></p></li>
<li><p><code>AWS::EC2::SubnetNetworkAclAssociation</code></p></li>
</ul></td>
<td colspan="2" style="text-align: left;"><p>Your VPC must have public subnets for between 1 and 3 availability zones and associate them with appropriate Ingress rules.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Internet gateway</p></td>
<td style="text-align: left;"><ul>
<li><p><code>AWS::EC2::InternetGateway</code></p></li>
<li><p><code>AWS::EC2::VPCGatewayAttachment</code></p></li>
<li><p><code>AWS::EC2::RouteTable</code></p></li>
<li><p><code>AWS::EC2::Route</code></p></li>
<li><p><code>AWS::EC2::SubnetRouteTableAssociation</code></p></li>
<li><p><code>AWS::EC2::NatGateway</code></p></li>
<li><p><code>AWS::EC2::EIP</code></p></li>
</ul></td>
<td colspan="2" style="text-align: left;"><p>You must have a public internet gateway, with public routes, attached to the VPC. In the provided templates, each public subnet has a NAT gateway with an EIP address. These NAT gateways allow cluster resources, like private subnet instances, to reach the internet and are not required for some restricted network or proxy scenarios.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Network access control</p></td>
<td style="text-align: left;"><ul>
<li><p><code>AWS::EC2::NetworkAcl</code></p></li>
<li><p><code>AWS::EC2::NetworkAclEntry</code></p></li>
</ul></td>
<td colspan="2" style="text-align: left;"><p>You must allow the VPC to access the following ports:</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>Port</strong></p></td>
<td style="text-align: left;"><p><strong>Reason</strong></p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>80</code></p></td>
<td style="text-align: left;"><p>Inbound HTTP traffic</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>443</code></p></td>
<td style="text-align: left;"><p>Inbound HTTPS traffic</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>22</code></p></td>
<td style="text-align: left;"><p>Inbound SSH traffic</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>1024</code> - <code>65535</code></p></td>
<td style="text-align: left;"><p>Inbound ephemeral traffic</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>0</code> - <code>65535</code></p></td>
<td style="text-align: left;"><p>Outbound ephemeral traffic</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p>Private subnets</p></td>
<td style="text-align: left;"><ul>
<li><p><code>AWS::EC2::Subnet</code></p></li>
<li><p><code>AWS::EC2::RouteTable</code></p></li>
<li><p><code>AWS::EC2::SubnetRouteTableAssociation</code></p></li>
</ul></td>
<td colspan="2" style="text-align: left;"><p>Your VPC can have private subnets. The provided CloudFormation templates can create private subnets for between 1 and 3 availability zones. If you use private subnets, you must provide appropriate routes and tables for them.</p></td>
</tr>
</tbody>
</table>

## VPC validation

To ensure that the subnets that you provide are suitable, the installation program confirms the following data:

- All the subnets that you specify exist.

- You provide private subnets.

- The subnet CIDRs belong to the machine CIDR that you specified.

- You provide subnets for each availability zone. Each availability zone contains no more than one public and one private subnet. If you use a private cluster, provide only a private subnet for each availability zone. Otherwise, provide exactly one public and private subnet for each availability zone.

- You provide a public subnet for each private subnet availability zone. Machines are not provisioned in availability zones that you do not provide private subnets for.

If you destroy a cluster that uses an existing VPC, the VPC is not deleted. When you remove the OpenShift Container Platform cluster from a VPC, the `kubernetes.io/cluster/.*: shared` tag is removed from the subnets that it used.

## Division of permissions

Starting with OpenShift Container Platform 4.3, you do not need all of the permissions that are required for an installation program-provisioned infrastructure cluster to deploy a cluster. This change mimics the division of permissions that you might have at your company: some individuals can create different resource in your clouds than others. For example, you might be able to create application-specific items, like instances, buckets, and load balancers, but not networking-related components such as VPCs, subnets, or ingress rules.

The AWS credentials that you use when you create your cluster do not need the networking permissions that are required to make VPCs and core networking components within the VPC, such as subnets, routing tables, internet gateways, NAT, and VPN. You still need permission to make the application resources that the machines within the cluster require, such as ELBs, security groups, S3 buckets, and nodes.

## Isolation between clusters

If you deploy OpenShift Container Platform to an existing network, the isolation of cluster services is reduced in the following ways:

- You can install multiple OpenShift Container Platform clusters in the same VPC.

- ICMP ingress is allowed from the entire network.

- TCP 22 ingress (SSH) is allowed to the entire network.

- Control plane TCP 6443 ingress (Kubernetes API) is allowed to the entire network.

- Control plane TCP 22623 ingress (MCS) is allowed to the entire network.

# Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on Amazon Web Services (AWS).

<div>

<div class="title">

Prerequisites

</div>

- You have the OpenShift Container Platform installation program and the pull secret for your cluster. For a restricted network installation, these files are on your mirror host.

- You have the `imageContentSources` values that were generated during mirror registry creation.

- You have obtained the contents of the certificate for your mirror registry.

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

        2.  Select **AWS** as the platform to target.

        3.  If you do not have an Amazon Web Services (AWS) profile stored on your computer, enter the AWS access key ID and secret access key for the user that you configured to run the installation program.

        4.  Select the AWS region to deploy the cluster to.

        5.  Select the base domain for the Route 53 service that you configured for your cluster.

        6.  Enter a descriptive name for your cluster.

2.  Edit the `install-config.yaml` file to give the additional information that is required for an installation in a restricted network.

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

    3.  Define the subnets for the VPC to install the cluster in, as in the following example:

        ``` yaml
        platform:
          aws:
            vpc:
              subnets:
                - id: subnet-<id_1>
                - id: subnet-<id_2>
                - id: subnet-<id_3>
        ```

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

        For these values, use the `imageContentSources` that you recorded during mirror registry creation.

    5.  Optionally, set the publishing strategy to `Internal`:

        ``` yaml
        publish: Internal
        ```

        By setting this option, you create an internal Ingress Controller and a private load balancer.

3.  Make any other modifications to the `install-config.yaml` file that you require.

    For more information about the parameters, see "Installation configuration parameters".

4.  Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

    > [!IMPORTANT]
    > The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for AWS](../installation-config-parameters-aws.md#installation-config-parameters-aws)

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

- [Optimizing storage](../../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

</div>

## Sample customized install-config.yaml file for AWS

You can customize the installation configuration file (`install-config.yaml`) to specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters.

> [!IMPORTANT]
> This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it. For a full list and description of all installation configuration parameters, see *Installation configuration parameters for AWS*.

<div class="formalpara">

<div class="title">

Sample `install-config.yaml` file for AWS

</div>

``` yaml
apiVersion: v1
baseDomain: example.com
sshKey: ssh-ed25519 AAAA...
pullSecret: '{"auths": ...}'
metadata:
  name: example-cluster
controlPlane:
  name: master
  platform:
    aws:
      type: m6i.xlarge
  replicas: 3
compute:
-  name: worker
  platform:
    aws:
      type: c5.4xlarge
  replicas: 3
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  aws:
    region: us-west-2
```

</div>

- Parameters at the first level of indentation apply to the cluster globally.

- The `controlPlane` stanza applies to control plane machines.

- The `compute` stanza applies to compute machines.

- The `networking` stanza applies to the cluster networking configuration. If you do not provide networking values, the installation program provides default values.

- The `platform` stanza applies to the infrastructure platform that hosts the cluster.

<div>

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for AWS](../installation-config-parameters-aws.md#installation-config-parameters-aws)

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
      noProxy: ec2.<aws_region>.amazonaws.com,elasticloadbalancing.<aws_region>.amazonaws.com,s3.<aws_region>.amazonaws.com
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
    Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations. If you have added the Amazon `EC2`, `Elastic Load Balancing`, and `S3` VPC endpoints to your VPC, you must add these endpoints to the `noProxy` field.

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

# Alternatives to storing administrator-level secrets in the kube-system project

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must use one of the following alternatives:

- To manage long-term cloud credentials manually, follow the procedure in [Manually creating long-term credentials](installing-restricted-networks-aws-installer-provisioned.md#manually-create-iam_installing-restricted-networks-aws-installer-provisioned).

- To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in [Configuring an AWS cluster to use short-term credentials](installing-restricted-networks-aws-installer-provisioned.md#installing-aws-with-short-term-creds_installing-restricted-networks-aws-installer-provisioned).

## Manually creating long-term credentials

The Cloud Credential Operator (CCO) can be put into manual mode prior to installation in environments where the cloud identity and access management (IAM) APIs are not reachable, or the administrator prefers not to store an administrator-level credential secret in the cluster `kube-system` namespace.

<div>

<div class="title">

Procedure

</div>

1.  If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

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

2.  If you have not previously created installation manifest files, do so by running the following command:

    ``` terminal
    $ openshift-install create manifests --dir <installation_directory>
    ```

    where `<installation_directory>` is the directory in which the installation program creates files.

3.  Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

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
        kind: AWSProviderSpec
        statementEntries:
        - effect: Allow
          action:
          - iam:GetUser
          - iam:GetUserPolicy
          - iam:ListAccessKeys
          resource: "*"
      ...
    ```

    </div>

5.  Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.

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
        kind: AWSProviderSpec
        statementEntries:
        - effect: Allow
          action:
          - s3:CreateBucket
          - s3:DeleteBucket
          resource: "*"
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
      aws_access_key_id: <base64_encoded_aws_access_key_id>
      aws_secret_access_key: <base64_encoded_aws_secret_access_key>
    ```

    </div>

    > [!IMPORTANT]
    > Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.

</div>

## Configuring an AWS cluster to use short-term credentials

To install a cluster that is configured to use the AWS Security Token Service (STS), you must configure the CCO utility and create the required AWS resources for your cluster.

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

- You have created an AWS account for the `ccoctl` utility to use with the following permissions:

  **Required `iam` permissions**

  - `iam:CreateOpenIDConnectProvider`

  - `iam:CreateRole`

  - `iam:DeleteOpenIDConnectProvider`

  - `iam:DeleteRole`

  - `iam:DeleteRolePolicy`

  - `iam:GetOpenIDConnectProvider`

  - `iam:GetRole`

  - `iam:GetUser`

  - `iam:ListOpenIDConnectProviders`

  - `iam:ListRolePolicies`

  - `iam:ListRoles`

  - `iam:PutRolePolicy`

  - `iam:TagOpenIDConnectProvider`

  - `iam:TagRole`

  **Required `s3` permissions**

  - `s3:CreateBucket`

  - `s3:DeleteBucket`

  - `s3:DeleteObject`

  - `s3:GetBucketAcl`

  - `s3:GetBucketTagging`

  - `s3:GetObject`

  - `s3:GetObjectAcl`

  - `s3:GetObjectTagging`

  - `s3:ListBucket`

  - `s3:PutBucketAcl`

  - `s3:PutBucketPolicy`

  - `s3:PutBucketPublicAccessBlock`

  - `s3:PutBucketTagging`

  - `s3:PutObject`

  - `s3:PutObjectAcl`

  - `s3:PutObjectTagging`

  **Required `cloudfront` permissions**

  - `cloudfront:ListCloudFrontOriginAccessIdentities`

  - `cloudfront:ListDistributions`

  - `cloudfront:ListTagsForResource`

- If you plan to store the OIDC configuration in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL, the AWS account that runs the `ccoctl` utility requires the following additional permissions:

  - `cloudfront:CreateCloudFrontOriginAccessIdentity`

  - `cloudfront:CreateDistribution`

  - `cloudfront:DeleteCloudFrontOriginAccessIdentity`

  - `cloudfront:DeleteDistribution`

  - `cloudfront:GetCloudFrontOriginAccessIdentity`

  - `cloudfront:GetCloudFrontOriginAccessIdentityConfig`

  - `cloudfront:GetDistribution`

  - `cloudfront:TagResource`

  - `cloudfront:UpdateDistribution`

  > [!NOTE]
  > These additional permissions support the use of the `--create-private-s3-bucket` option when processing credentials requests with the `ccoctl aws create-all` command.

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

### Creating AWS resources with the Cloud Credential Operator utility

You have the following options when creating AWS resources:

- You can use the `ccoctl aws create-all` command to create the AWS resources automatically. This is the quickest way to create the resources. See [Creating AWS resources with a single command](installing-restricted-networks-aws-installer-provisioned.md#cco-ccoctl-creating-at-once_installing-restricted-networks-aws-installer-provisioned).

- If you need to review the JSON files that the `ccoctl` tool creates before modifying AWS resources, or if the process the `ccoctl` tool uses to create AWS resources automatically does not meet the requirements of your organization, you can create the AWS resources individually. See [Creating AWS resources individually](installing-restricted-networks-aws-installer-provisioned.md#cco-ccoctl-creating-individually_installing-restricted-networks-aws-installer-provisioned).

#### Creating AWS resources with a single command

If the process the `ccoctl` tool uses to create AWS resources automatically meets the requirements of your organization, you can use the `ccoctl aws create-all` command to automate the creation of AWS resources.

Otherwise, you can create the AWS resources individually. For more information, see "Creating AWS resources individually".

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
    $ ccoctl aws create-all \
      --name=<name> \
      --region=<aws_region> \
      --credentials-requests-dir=<path_to_credentials_requests_directory> \
      --output-dir=<path_to_ccoctl_output_dir> \
      --create-private-s3-bucket
    ```

    where:

    `<name>`
    Specifies the name used to tag any cloud resources that are created for tracking.

    `<aws_region>`
    Specifies the AWS region in which cloud resources will be created.

    `<path_to_credentials_requests_directory>`
    Specifies the directory containing the files for the component `CredentialsRequest` objects.

    `<path_to_ccoctl_output_dir>`
    Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run. This parameter is optional.

    `--create-private-s3-bucket`
    Specifies that the OpenID Connect (OIDC) configuration files should be stored in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL. Note that by default, the `ccoctl` utility stores the OIDC configuration files in a public S3 bucket and uses the S3 URL as the public OIDC endpoint. This parameter is optional.

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
  openshift-cloud-credential-operator-cloud-credential-operator-iam-ro-creds-credentials.yaml
  openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
  openshift-cluster-api-capa-manager-bootstrap-credentials-credentials.yaml
  openshift-cluster-csi-drivers-ebs-cloud-credentials-credentials.yaml
  openshift-image-registry-installer-cloud-credentials-credentials.yaml
  openshift-ingress-operator-cloud-credentials-credentials.yaml
  openshift-machine-api-aws-cloud-credentials-credentials.yaml
  ```

  </div>

  You can verify that the IAM roles are created by querying AWS. For more information, refer to AWS documentation on listing IAM roles.

</div>

#### Creating AWS resources individually

You can use the `ccoctl` tool to create AWS resources individually. This option might be useful for an organization that shares the responsibility for creating these resources among different users or departments.

Otherwise, you can use the `ccoctl aws create-all` command to create the AWS resources automatically. For more information, see "Creating AWS resources with a single command".

> [!NOTE]
> By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory.
>
> Some `ccoctl` commands make AWS API calls to create or modify AWS resources. You can use the `--dry-run` flag to avoid making API calls. Using this flag creates JSON files on the local file system instead. You can review and modify the JSON files and then apply them with the AWS CLI tool using the `--cli-input-json` parameters.

<div>

<div class="title">

Prerequisites

</div>

- Extract and prepare the `ccoctl` binary.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Generate the public and private RSA key files that are used to set up the OpenID Connect provider for the cluster by running the following command:

    ``` terminal
    $ ccoctl aws create-key-pair
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    2021/04/13 11:01:02 Generating RSA keypair
    2021/04/13 11:01:03 Writing private key to /<path_to_ccoctl_output_dir>/serviceaccount-signer.private
    2021/04/13 11:01:03 Writing public key to /<path_to_ccoctl_output_dir>/serviceaccount-signer.public
    2021/04/13 11:01:03 Copying signing key for use by installer
    ```

    </div>

    where `serviceaccount-signer.private` and `serviceaccount-signer.public` are the generated key files.

    This command also creates a private key that the cluster requires during installation in `/<path_to_ccoctl_output_dir>/tls/bound-service-account-signing-key.key`.

2.  Create an OpenID Connect identity provider and S3 bucket on AWS by running the following command:

    ``` terminal
    $ ccoctl aws create-identity-provider \
      --name=<name> \
      --region=<aws_region> \
      --public-key-file=<path_to_ccoctl_output_dir>/serviceaccount-signer.public
    ```

    - `<name>` is the name used to tag any cloud resources that are created for tracking.

    - `<aws-region>` is the AWS region in which cloud resources will be created.

    - `<path_to_ccoctl_output_dir>` is the path to the public key file that the `ccoctl aws create-key-pair` command generated.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` text
      2021/04/13 11:16:09 Bucket <name>-oidc created
      2021/04/13 11:16:10 OpenID Connect discovery document in the S3 bucket <name>-oidc at .well-known/openid-configuration updated
      2021/04/13 11:16:10 Reading public key
      2021/04/13 11:16:10 JSON web key set (JWKS) in the S3 bucket <name>-oidc at keys.json updated
      2021/04/13 11:16:18 Identity Provider created with ARN: arn:aws:iam::<aws_account_id>:oidc-provider/<name>-oidc.s3.<aws_region>.amazonaws.com
      ```

      </div>

      where `openid-configuration` is a discovery document and `keys.json` is a JSON web key set file.

      This command also creates a YAML configuration file in `/<path_to_ccoctl_output_dir>/manifests/cluster-authentication-02-config.yaml`. This file sets the issuer URL field for the service account tokens that the cluster generates, so that the AWS IAM identity provider trusts the tokens.

3.  Create IAM roles for each component in the cluster:

    1.  Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

        ``` terminal
        $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
        ```

    2.  Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image:

        ``` terminal
        $ oc adm release extract \
          --from=$RELEASE_IMAGE \
          --credentials-requests \
          --included \
          --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
          --to=<path_to_directory_for_credentials_requests>
        ```

        - The `--included` parameter includes only the manifests that your specific cluster configuration requires.

        - Specify the location of the `install-config.yaml` file.

        - Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

    3.  Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:

        ``` terminal
        $ ccoctl aws create-iam-roles \
          --name=<name> \
          --region=<aws_region> \
          --credentials-requests-dir=<path_to_credentials_requests_directory> \
          --identity-provider-arn=arn:aws:iam::<aws_account_id>:oidc-provider/<name>-oidc.s3.<aws_region>.amazonaws.com
        ```

        > [!NOTE]
        > For AWS environments that use alternative IAM API endpoints, such as GovCloud, you must also specify your region with the `--region` parameter.
        >
        > If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.

        For each `CredentialsRequest` object, `ccoctl` creates an IAM role with a trust policy that is tied to the specified OIDC identity provider, and a permissions policy as defined in each `CredentialsRequest` object from the OpenShift Container Platform release image.

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
  openshift-cloud-credential-operator-cloud-credential-operator-iam-ro-creds-credentials.yaml
  openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
  openshift-cluster-api-capa-manager-bootstrap-credentials-credentials.yaml
  openshift-cluster-csi-drivers-ebs-cloud-credentials-credentials.yaml
  openshift-image-registry-installer-cloud-credentials-credentials.yaml
  openshift-ingress-operator-cloud-credentials-credentials.yaml
  openshift-machine-api-aws-cloud-credentials-credentials.yaml
  ```

  </div>

  You can verify that the IAM roles are created by querying AWS. For more information, refer to AWS documentation on listing IAM roles.

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

1.  If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

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

2.  If you have not previously created installation manifest files, do so by running the following command:

    ``` terminal
    $ openshift-install create manifests --dir <installation_directory>
    ```

    where `<installation_directory>` is the directory in which the installation program creates files.

3.  Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command:

    ``` terminal
    $ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
    ```

4.  Copy the `tls` directory that contains the private key to the installation directory:

    ``` terminal
    $ cp -a /<path_to_ccoctl_output_dir>/tls .
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

1.  In the directory that contains the installation program, initialize the cluster deployment by running the following command:

    ``` terminal
    $ ./openshift-install create cluster --dir <installation_directory> \
        --log-level=info
    ```

    - For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.

    - To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

2.  Optional: Remove or disable the `AdministratorAccess` policy from the IAM account that you used to install the cluster.

    > [!NOTE]
    > The elevated permissions provided by the `AdministratorAccess` policy are required only during installation.

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

# Disabling the default software catalog sources

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

# Next steps

- [Validate an installation](../../validation_and_troubleshooting/validating-an-installation.md#validating-an-installation).

- [Customize your cluster](../../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations).

- [Configure image streams](../../../post_installation_configuration/cluster-tasks.md#post-install-must-gather-disconnected) for the Cluster Samples Operator and the `must-gather` tool.

- Learn how to [use Operator Lifecycle Manager in disconnected environments](../../../disconnected/using-olm.md#olm-restricted-networks).

- If the mirror registry that you used to install your cluster has a trusted CA, add it to the cluster by [configuring additional trust stores](../../../openshift_images/image-configuration.md#images-configuration-cas_image-configuration).

- If necessary, you can [Remote health reporting](../../../support/remote_health_monitoring/remote-health-reporting.md#remote-health-reporting).
