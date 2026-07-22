<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use the Agent-based Installer to install a cluster on Oracle® Edge Cloud, so that you can run cluster workloads on on-premise infrastructure while still using Oracle® Cloud Infrastructure (OCI) services.

The following procedures describe a cluster installation on Oracle® Compute Cloud@Customer as an example.

# Supported Oracle Edge Cloud infrastructures

The following table describes the support status of each Oracle® Edge Cloud infrastructure offering:

| Infrastructure type           | Support status       |
|-------------------------------|----------------------|
| Private Cloud Appliance       | General Availability |
| Oracle Compute Cloud@Customer | General Availability |
| Roving Edge                   | Technology Preview   |

Oracle Edge Cloud infrastructure support statuses

# Installation process workflow

The following workflow describes a high-level outline for the process of installing an OpenShift Container Platform cluster on Oracle Edge Cloud using the Agent-based Installer:

1.  Create Oracle Cloud Infrastructure (OCI) resources and services (Oracle).

2.  Prepare configuration files for the Agent-based Installer (Red Hat).

3.  Generate the agent ISO image (Red Hat).

4.  Convert the ISO image to an OCI image, upload it to an OCI Home Region Bucket, and then import the uploaded image to the Oracle Edge Cloud system (Oracle).

5.  Disconnected environments: Prepare a web server that is accessible by Oracle Edge Cloud instances (Red Hat).

6.  Disconnected environments: Upload the rootfs image to the web server (Red Hat).

7.  Configure your firewall for OpenShift Container Platform (Red Hat).

8.  Create control plane nodes and configure load balancers (Oracle).

9.  Create compute nodes and configure load balancers (Oracle).

10. Verify that your cluster runs on Oracle Edge Cloud (Oracle).

# Creating OCI infrastructure resources and services

You must create an Oracle Edge Cloud environment on your virtual machine (VM) shape. By creating this environment, you can install OpenShift Container Platform and deploy a cluster on an infrastructure that supports a wide range of cloud options and strong security policies. Having prior knowledge of Oracle Cloud Infrastructure (OCI) components can help you with understanding the concept of OCI resources and how you can configure them to meet your organizational needs.

> [!IMPORTANT]
> To ensure compatibility with OpenShift Container Platform, you must set `A` as the record type for each DNS record and name records as follows:
>
> - `api.<cluster_name>.<base_domain>`, which targets the `apiVIP` parameter of the API load balancer
>
> - `api-int.<cluster_name>.<base_domain>`, which targets the `apiVIP` parameter of the API load balancer
>
> - `*.apps.<cluster_name>.<base_domain>`, which targets the `ingressVIP` parameter of the Ingress load balancer
>
> The `api.*` and `api-int.*` DNS records relate to control plane machines, so you must ensure that all nodes in your installed OpenShift Container Platform cluster can access these DNS records.

<div>

<div class="title">

Prerequisites

</div>

- You configured an OCI account to host the OpenShift Container Platform cluster. See "Access and Considerations" in [OpenShift Cluster Setup with Agent Based Installer on Compute Cloud@Customer](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_agent_based_installation.pdf?source=:em:nl:mt::::PCATP) (Oracle documentation).

</div>

<div>

<div class="title">

Procedure

</div>

- Create the required OCI resources and services.

  For more information, see "Terraform Script Execution" in [OpenShift Cluster Setup with Agent Based Installer on Compute Cloud@Customer](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_agent_based_installation.pdf?source=:em:nl:mt::::PCATP) (Oracle documentation).

</div>

<div>

<div class="title">

Additional resources

</div>

- [Learn About Oracle Cloud Basics (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/concepts.htm)

</div>

# Creating configuration files for installing a cluster on Oracle Edge Cloud

You must create the `install-config.yaml` and the `agent-config.yaml` configuration files so that you can use the Agent-based Installer to generate a bootable ISO image. The Agent-based installation comprises a bootable ISO that has the Assisted discovery agent and the Assisted Service. Both of these components are required to perform the cluster installation, but the latter component runs on only one of the hosts.

> [!NOTE]
> You can also use the Agent-based Installer to generate or accept Zero Touch Provisioning (ZTP) custom resources.

<div>

<div class="title">

Prerequisites

</div>

- You reviewed details about the OpenShift Container Platform installation and update processes.

- You read the documentation on selecting a cluster installation method and preparing the method for users.

- You have read the "Preparing to install with the Agent-based Installer" documentation.

- You downloaded the Agent-Based Installer and the command-line interface (CLI) from the [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift/install/metal/agent-based).

- If you are installing in a disconnected environment, you have prepared a mirror registry in your environment and mirrored release images to the registry.

  > [!IMPORTANT]
  > Check that your `openshift-install` binary version relates to your local image container registry and not a shared registry, such as Red Hat Quay, by running the following command:
  >
  > ``` terminal
  > $ ./openshift-install version
  > ```
  >
  > <div class="formalpara">
  >
  > <div class="title">
  >
  > Example output for a shared registry binary
  >
  > </div>
  >
  > ``` terminal
  > ./openshift-install 4.20.0
  > built from commit ae7977b7d1ca908674a0d45c5c243c766fa4b2ca
  > release image registry.ci.openshift.org/origin/release:4.20ocp-release@sha256:0da6316466d60a3a4535d5fed3589feb0391989982fba59d47d4c729912d6363
  > release architecture amd64
  > ```
  >
  > </div>

- You have logged in to the OpenShift Container Platform with administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an installation directory to store configuration files in by running the following command:

    ``` terminal
    $ mkdir ~/<directory_name>
    ```

2.  Configure the `install-config.yaml` configuration file to meet the needs of your organization and save the file in the directory you created.

    <div class="formalpara">

    <div class="title">

    `install-config.yaml` file that sets an external platform

    </div>

    ``` yaml
    # install-config.yaml
    apiVersion: v1
    baseDomain: <base_domain>
    networking:
      clusterNetwork:
      - cidr: 10.128.0.0/14
        hostPrefix: 23
      network type: OVNKubernetes
      machineNetwork:
      - cidr: <ip_address_from_cidr>
      serviceNetwork:
      - 172.30.0.0/16
    compute:
      - architecture: amd64
      hyperthreading: Enabled
      name: worker
      replicas: 0
    controlPlane:
      architecture: amd64
      hyperthreading: Enabled
      name: master
      replicas: 3
    platform:
       external:
        platformName: oci
        cloudControllerManager: External
    sshKey: <public_ssh_key>
    pullSecret: '<pull_secret>'
    # ...
    ```

    </div>

    - The base domain of your cloud provider.

    - The IP address from the virtual cloud network (VCN) that the CIDR allocates to resources and components that operate on your network.

    - Depending on your infrastructure, you can select either `arm64` or `amd64`.

    - Set `OCI` as the external platform, so that OpenShift Container Platform can integrate with OCI.

    - Specify your SSH public key.

    - The pull secret that you need for authenticate purposes when downloading container images for OpenShift Container Platform components and services, such as Quay.io. See [Install OpenShift Container Platform 4](https://console.redhat.com/openshift/install/pull-secret) from the Red Hat Hybrid Cloud Console.

3.  Create a directory on your local system named `openshift`. This must be a subdirectory of the installation directory.

    > [!IMPORTANT]
    > Do not move the `install-config.yaml` or `agent-config.yaml` configuration files to the `openshift` directory.

4.  Configure the Oracle custom manifest files.

    1.  Go to "Prepare the OpenShift Master Images" in [OpenShift Cluster Setup with Agent Based Installer on Compute Cloud@Customer](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_agent_based_installation.pdf?source=:em:nl:mt::::PCATP) (Oracle documentation).

    2.  Copy and paste the `oci-ccm.yml`, `oci-csi.yml`, and `machineconfig-ccm.yml` files into your `openshift` directory.

    3.  Edit the `oci-ccm.yml` and `oci-csi.yml` files to specify the compartment Oracle® Cloud Identifier (OCID), VCN OCID, subnet OCID from the load balancer, the security lists OCID, and the `c3-cert.pem` section.

5.  Configure the `agent-config.yaml` configuration file to meet your organization’s requirements.

    <div class="formalpara">

    <div class="title">

    Sample `agent-config.yaml` file for an IPv4 network.

    </div>

    ``` yaml
    apiVersion: v1beta1
    metadata:
      name: <cluster_name>
      namespace: <cluster_namespace>
    rendezvousIP: <ip_address_from_CIDR>
    bootArtifactsBaseURL: <server_URL>
    # ...
    ```

    </div>

    - The cluster name that you specified in your DNS record.

    - The namespace of your cluster on OpenShift Container Platform.

    - If you use IPv4 as the network IP address format, ensure that you set the `rendezvousIP` parameter to an IPv4 address that the VCN’s Classless Inter-Domain Routing (CIDR) method allocates on your network. Also ensure that at least one instance from the pool of instances that you booted with the ISO matches the IP address value you set for the `rendezvousIP` parameter.

    - The URL of the server where you want to upload the rootfs image. This parameter is required only for disconnected environments.

6.  Generate a minimal ISO image, which excludes the rootfs image, by entering the following command in your installation directory:

    ``` terminal
    $ ./openshift-install agent create image --log-level debug
    ```

    The command also completes the following actions:

    - Creates a subdirectory, `./<installation_directory>/auth directory:`, and places `kubeadmin-password` and `kubeconfig` files in the subdirectory.

    - Creates a `rendezvousIP` file based on the IP address that you specified in the `agent-config.yaml` configuration file.

    - Optional: Any modifications you made to `agent-config.yaml` and `install-config.yaml` configuration files get imported to the Zero Touch Provisioning (ZTP) custom resources.

      > [!IMPORTANT]
      > The Agent-based Installer uses Red Hat Enterprise Linux CoreOS (RHCOS). The rootfs image, which is mentioned in a later step, is required for booting, recovering, and repairing your operating system.

7.  Disconnected environments only: Upload the rootfs image to a web server.

    1.  Go to the `./<installation_directory>/boot-artifacts` directory that was generated when you created the minimal ISO image.

    2.  Use your preferred web server, such as any Hypertext Transfer Protocol daemon (`httpd`), to upload the rootfs image to the location specified in the `bootArtifactsBaseURL` parameter of the `agent-config.yaml` file.

        For example, if the `bootArtifactsBaseURL` parameter states `http://192.168.122.20`, you would upload the generated rootfs image to this location so that the Agent-based installer can access the image from `http://192.168.122.20/agent.x86_64-rootfs.img`. After the Agent-based installer boots the minimal ISO for the external platform, the Agent-based Installer downloads the rootfs image from the `http://192.168.122.20/agent.x86_64-rootfs.img` location into the system memory.

        > [!NOTE]
        > The Agent-based Installer also adds the value of the `bootArtifactsBaseURL` to the minimal ISO Image’s configuration, so that when the Operator boots a cluster’s node, the Agent-based Installer downloads the rootfs image into system memory.

        > [!IMPORTANT]
        > Consider that the full ISO image, which is in excess of `1` GB, includes the rootfs image. The image is larger than the minimal ISO Image, which is typically less than `150` MB.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About OpenShift Container Platform installation](../../architecture/architecture-installation.md#installation-overview_architecture-installation)

- [Selecting a cluster installation type](../overview/installing-preparing.md#installing-preparing-selecting-cluster-type)

- [Preparing to install with the Agent-based Installer](../installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.md#preparing-to-install-with-agent-based-installer)

- [Downloading the Agent-based Installer](../installing_with_agent_based_installer/installing-with-agent-based-installer.md#installing-ocp-agent-retrieve_installing-with-agent-based-installer)

- [Creating a mirror registry with mirror registry for Red Hat OpenShift](../../disconnected/installing-mirroring-creating-registry.md#installing-mirroring-creating-registry)

- [Mirroring the OpenShift Container Platform image repository](../../disconnected/installing-mirroring-installation-images.md#installation-mirror-repository_installing-mirroring-installation-images)

- [Optional: Using ZTP manifests](../installing_with_agent_based_installer/installing-with-agent-based-installer.md#installing-ocp-agent-ztp_installing-with-agent-based-installer)

</div>

# Configuring your firewall for OpenShift Container Platform

Before you install OpenShift Container Platform, you must configure your firewall to grant access to the sites that OpenShift Container Platform requires.

There are no special configuration considerations for services running on only controller nodes compared to compute nodes.

> [!NOTE]
> If your environment has a dedicated load balancer in front of your OpenShift Container Platform cluster, review the allowlists between your firewall and load balancer to prevent unwanted network restrictions to your cluster.

<div>

<div class="title">

Procedure

</div>

1.  Allowlist the following container registry URLs for cluster installation and upgrades:

    | URL | Port | Function |
    |----|----|----|
    | `registry.redhat.io` | 443 | Provides core container images |
    | `access.redhat.com` | 443 | Hosts a signature store that a container client requires for verifying images pulled from `registry.access.redhat.com`. In a firewall environment, ensure that this resource is on the allowlist. |
    | `registry.access.redhat.com` | 443 | Hosts all the container images that are stored on the Red Hat Ecosystem Catalog, including core container images. |
    | `quay.io` | 443 | Provides core container images |
    | `cdn.quay.io` | 443 | Provides core container images |
    | `cdn01.quay.io` | 443 | Provides core container images |
    | `cdn02.quay.io` | 443 | Provides core container images |
    | `cdn03.quay.io` | 443 | Provides core container images |
    | `cdn04.quay.io` | 443 | Provides core container images |
    | `cdn05.quay.io` | 443 | Provides core container images |
    | `cdn06.quay.io` | 443 | Provides core container images |
    | `icr.io` | 443 | Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks. |
    | `cp.icr.io` | 443 | Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks. |

    - You can use the wildcard `*.quay.io` instead of `cdn.quay.io` and `cdn0[1-6].quay.io` in your allowlist.

    - You can use the wildcard `*.access.redhat.com` to simplify the configuration and ensure that all subdomains, including `registry.access.redhat.com`, are allowed.

    - When adding a site such as `quay.io` to your allowlist, do not add a wildcard entry such as `*.quay.io` to your denylist. In most cases, image registries use a content delivery network (CDN) to serve images. If a firewall blocks access, image downloads are denied when the initial download request redirects to a hostname such as `cdn01.quay.io`.

2.  Allowlist the following URLs to enable cluster access, authentication, and updates:

    | URL | Port | Function |
    |----|----|----|
    | `*.apps.<cluster_name>.<base_domain>` | 443 | Allowlist these URLs to enable cluster access, authentication, and updates. |
    | `api.openshift.com` | 443 | API endpoint for cluster tokens and update checks. |
    | `console.redhat.com` | 443 | Authentication service for cluster tokens. |
    | `sso.redhat.com` | 443 | The `https://console.redhat.com` site uses authentication from `sso.redhat.com` |

    For egress traffic, Operators require route access to perform health checks to establish a connection for reaching endpoints. The authentication and web console Operators connect to two routes to verify functionality. Cluster administrators who do not want to allow `*.apps.<cluster_name>.<base_domain>`, must allow the following routes:

    - `oauth-openshift.apps.<cluster_name>.<base_domain>`

    - `canary-openshift-ingress-canary.apps.<cluster_name>.<base_domain>`

    - `console-openshift-console.apps.<cluster_name>.<base_domain>`, or the hostname that is specified in the `spec.route.hostname` field of the `consoles.operator/cluster` object if the field is not empty.

3.  Allowlist the following registry URLs that host related artifacts for cluster installation and upgrades, such as installation content, release images, and client tools:

    | URL | Port | Function |
    |----|----|----|
    | `mirror.openshift.com` | 443 | Required to access mirrored installation content and images. This site is also a source of release image signatures, although the Cluster Version Operator needs only a single functioning source. |
    | `quayio-production-s3.s3.amazonaws.com` | 443 | Required to access Quay image content in AWS. |
    | `rhcos.mirror.openshift.com` | 443 | Required to download Red Hat Enterprise Linux CoreOS (RHCOS) images. |
    | `storage.googleapis.com/openshift-release` | 443 | A source of release image signatures, although the Cluster Version Operator needs only a single functioning source. |

4.  Set your firewall’s allowlist to include any site that provides resources for a language or framework that your builds require.

5.  If you do not disable Telemetry, you must grant access to the following URLs to access Telemetry and Red Hat Lightspeed:

    | URL | Port | Function |
    |----|----|----|
    | `cert-api.access.redhat.com` | 443 | Required for Telemetry |
    | `api.access.redhat.com` | 443 | Required for Telemetry |
    | `infogw.api.openshift.com` | 443 | Required for Telemetry |
    | `console.redhat.com` | 443 | Required for Telemetry and for `insights-operator` |

6.  If you use Alibaba Cloud, Amazon Web Services (AWS), Microsoft Azure, or Google Cloud to host your cluster, you must grant access to the URLs that offer the cloud provider API and DNS for that cloud:

    <table>
    <colgroup>
    <col style="width: 10%" />
    <col style="width: 40%" />
    <col style="width: 10%" />
    <col style="width: 40%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Cloud</th>
    <th style="text-align: left;">URL</th>
    <th style="text-align: left;">Port</th>
    <th style="text-align: left;">Function</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p>Alibaba</p></td>
    <td style="text-align: left;"><p><code>*.aliyuncs.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access Alibaba Cloud services and resources. Review the <a href="https://github.com/aliyun/alibaba-cloud-sdk-go/blob/master/sdk/endpoints/endpoints_config.go?spm=a2c4g.11186623.0.0.47875873ciGnC8&amp;file=endpoints_config.go">Alibaba endpoints_config.go file</a> to find the exact endpoints to allow for the regions that you use.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>AWS</p></td>
    <td style="text-align: left;"><p><code>aws.amazon.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.amazonaws.com</code></p>
    <p>Alternatively, if you choose to not use a wildcard for AWS APIs, you must include the following URLs in your allowlist:</p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access AWS services and resources. Review the <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html">AWS Service Endpoints</a> in the AWS documentation to find the exact endpoints to allow for the regions that you use.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>ec2.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>events.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>iam.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>route53.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.s3.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.s3.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.s3.dualstack.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>sts.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>sts.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>tagging.us-east-1.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment. This endpoint is always <code>us-east-1</code>, regardless of the region the cluster is deployed in.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>ec2.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>elasticloadbalancing.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>servicequotas.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required. Used to confirm quotas for deploying the service.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>tagging.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Allows the assignment of metadata about AWS resources in the form of tags.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.cloudfront.net</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to provide access to CloudFront. If you use the AWS Security Token Service (STS) and the private S3 bucket, you must provide access to CloudFront.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>GCP</p></td>
    <td style="text-align: left;"><p><code>*.googleapis.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access Google Cloud services and resources. Review <a href="https://cloud.google.com/endpoints/">Cloud Endpoints</a> in the Google Cloud documentation to find the endpoints to allow for your APIs.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>accounts.google.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access your Google Cloud account.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Microsoft Azure</p></td>
    <td style="text-align: left;"><p><code>management.azure.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access Microsoft Azure services and resources. Review the <a href="https://docs.microsoft.com/en-us/rest/api/azure/">Microsoft Azure REST API reference</a> in the Microsoft Azure documentation to find the endpoints to allow for your APIs.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.blob.core.windows.net</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to download Ignition files.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>login.microsoftonline.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access Microsoft Azure services and resources. Review the <a href="https://docs.microsoft.com/en-us/rest/api/azure/">Azure REST API reference</a> in the Microsoft Azure documentation to find the endpoints to allow for your APIs.</p></td>
    <td></td>
    </tr>
    </tbody>
    </table>

7.  Allowlist the following URL for optional third-party content:

    | URL | Port | Function |
    |----|----|----|
    | `registry.connect.redhat.com` | 443 | Required for all third-party images and certified operators. |

8.  If you use a default Red Hat Network Time Protocol (NTP) server, allow the following URLs. NTP operates on User Datagram Protocol (UDP) port 123, so this port must be opened on the firewall.

    | URL                   | Port | Function                                        |
    |-----------------------|------|-------------------------------------------------|
    | `1.rhel.pool.ntp.org` | 123  | Provides NTP services for time synchronization. |
    | `2.rhel.pool.ntp.org` | 123  | Provides NTP services for time synchronization. |
    | `3.rhel.pool.ntp.org` | 123  | Provides NTP services for time synchronization. |

    > [!NOTE]
    > If you do not use a default Red Hat NTP server, verify the NTP server for your platform and allow it in your firewall.

</div>

# Running a cluster on Oracle Edge Cloud

To run a cluster on Oracle® Edge Cloud, you must first convert your generated Agent ISO image into an OCI image, upload it to an OCI Home Region Bucket, and then import the uploaded image to the Oracle Edge Cloud system.

> [!NOTE]
> Oracle Edge Cloud supports the following OpenShift Container Platform cluster topologies:
>
> - Installing an OpenShift Container Platform cluster on a single node.
>
> - A highly available cluster that has a minimum of three control plane instances and two compute instances.
>
> - A compact three-node cluster that has a minimum of three control plane instances.

<div>

<div class="title">

Prerequisites

</div>

- You generated an Agent ISO image. See the "Creating configuration files for installing a cluster on Oracle Edge Cloud" section.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Convert the agent ISO image to an OCI image, upload it to an OCI Home Region Bucket, and then import the uploaded image to the Oracle Edge Cloud system. See "Prepare the OpenShift Master Images" in [OpenShift Cluster Setup with Agent Based Installer on Compute Cloud@Customer (Oracle documentation)](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_agent_based_installation.pdf?source=:em:nl:mt::::PCATP) for instructions.

2.  Create control plane instances on Oracle Edge Cloud. See "Create control plane instances on C3 and Master Node LB Backend Sets" in [OpenShift Cluster Setup with Agent Based Installer on Compute Cloud@Customer (Oracle documentation)](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_agent_based_installation.pdf?source=:em:nl:mt::::PCATP) for instructions.

3.  Create a compute instance from the supplied base image for your cluster topology. See "Add worker nodes" in [OpenShift Cluster Setup with Agent Based Installer on Compute Cloud@Customer (Oracle documentation)](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_agent_based_installation.pdf?source=:em:nl:mt::::PCATP) for instructions.

    > [!IMPORTANT]
    > Before you create the compute instance, check that you have enough memory and disk resources for your cluster. Additionally, ensure that at least one compute instance has the same IP address as the address stated under `rendezvousIP` in the `agent-config.yaml` file.

</div>

# Verifying that your Agent-based cluster installation runs on Oracle Edge Cloud

Verify that your cluster was installed and is running effectively on Oracle Edge Cloud.

<div>

<div class="title">

Prerequisites

</div>

- You created all the required Oracle Cloud Infrastructure (OCI) resources and services. See the "Creating OCI infrastructure resources and services" section.

- You created `install-config.yaml` and `agent-config.yaml` configuration files. See the "Creating configuration files for installing a cluster on Oracle Edge Cloud" section.

- You uploaded the agent ISO image to a default Oracle Object Storage bucket, and you created a compute instance on Oracle Edge Cloud. For more information, see "Running a cluster on Oracle Edge Cloud".

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

After you deploy the compute instance on a self-managed node in your OpenShift Container Platform cluster, you can monitor the cluster’s status by choosing one of the following options:

</div>

- From the OpenShift Container Platform CLI, enter the following command:

  ``` terminal
  $ ./openshift-install agent wait-for install-complete --log-level debug
  ```

  Check the status of the `rendezvous` host node that runs the bootstrap node. After the host reboots, the host forms part of the cluster.

- Use the `kubeconfig` API to check the status of various OpenShift Container Platform components. For the `KUBECONFIG` environment variable, set the relative path of the cluster’s `kubeconfig` configuration file:

  ``` terminal
  $  export KUBECONFIG=~/auth/kubeconfig
  ```

  Check the status of each of the cluster’s self-managed nodes. CCM applies a label to each node to designate the node as running in a cluster on OCI.

  ``` terminal
  $ oc get nodes -A
  ```

  <div class="formalpara">

  <div class="title">

  Output example

  </div>

  ``` terminal
  NAME                                   STATUS ROLES                 AGE VERSION
  main-0.private.agenttest.oraclevcn.com Ready  control-plane, master 7m  v1.27.4+6eeca63
  main-1.private.agenttest.oraclevcn.com Ready  control-plane, master 15m v1.27.4+d7fa83f
  main-2.private.agenttest.oraclevcn.com Ready  control-plane, master 15m v1.27.4+d7fa83f
  ```

  </div>

  Check the status of each of the cluster’s Operators, with the CCM Operator status being a good indicator that your cluster is running.

  ``` terminal
  $ oc get co
  ```

  <div class="formalpara">

  <div class="title">

  Truncated output example

  </div>

  ``` terminal
  NAME           VERSION     AVAILABLE  PROGRESSING    DEGRADED   SINCE   MESSAGE
  authentication 4.20.0-0    True       False          False      6m18s
  baremetal      4.20.0-0    True       False          False      2m42s
  network        4.20.0-0    True       True           False      5m58s  Progressing: …
      …
  ```

  </div>

# Additional resources

- [Gathering log data from a failed Agent-based installation](../installing_with_agent_based_installer/installing-with-agent-based-installer.md#installing-ocp-agent-gather-log_installing-with-agent-based-installer)

- [Adding worker nodes to an on-premise cluster](../../nodes/nodes/nodes-nodes-adding-node-iso.md#adding-node-iso)
