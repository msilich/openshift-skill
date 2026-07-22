<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you can install OpenShift Container Platform, you must configure an IBM Cloud® account.

# Prerequisites

- You have an IBM Cloud® account with a subscription. You cannot install OpenShift Container Platform on a free or trial IBM Cloud® account.

# Quotas and limits on IBM Cloud

The OpenShift Container Platform cluster uses a number of IBM Cloud® components, and the default quotas and limits affect your ability to install OpenShift Container Platform clusters. If you use certain cluster configurations, deploy your cluster in certain regions, or run multiple clusters from your account, you might need to request additional resources for your IBM Cloud® account.

For a comprehensive list of the default IBM Cloud® quotas and service limits, see IBM Cloud®'s documentation for [Quotas and service limits](https://cloud.ibm.com/docs/vpc?topic=vpc-quotas).

## Virtual Private Cloud (VPC)

Each OpenShift Container Platform cluster creates its own VPC. The default quota of VPCs per region is 10 and will allow 10 clusters. To have more than 10 clusters in a single region, you must increase this quota.

## Application load balancer

By default, each cluster creates three application load balancers (ALBs):

- Internal load balancer for the master API server

- External load balancer for the master API server

- Load balancer for the router

You can create additional `LoadBalancer` service objects to create additional ALBs. The default quota of VPC ALBs are 50 per region. To have more than 50 ALBs, you must increase this quota.

VPC ALBs are supported. Classic ALBs are not supported for IBM Cloud®.

## Floating IP address

By default, the installation program distributes control plane and compute machines across all availability zones within a region to provision the cluster in a highly available configuration. In each availability zone, a public gateway is created and requires a separate floating IP address.

The default quota for a floating IP address is 20 addresses per availability zone. The default cluster configuration yields three floating IP addresses:

- Two floating IP addresses in the `us-east-1` primary zone. The IP address associated with the bootstrap node is removed after installation.

- One floating IP address in the `us-east-2` secondary zone.

- One floating IP address in the `us-east-3` secondary zone.

IBM Cloud® can support up to 19 clusters per region in an account. If you plan to have more than 19 default clusters, you must increase this quota.

## Virtual Server Instances (VSI)

By default, a cluster creates VSIs using `bx2-4x16` profiles, which includes the following resources by default:

- 4 vCPUs

- 16 GB RAM

The following nodes are created:

- One `bx2-4x16` bootstrap machine, which is removed after the installation is complete

- Three `bx2-4x16` control plane nodes

- Three `bx2-4x16` compute nodes

For more information, see IBM Cloud®'s documentation on [supported profiles](https://cloud.ibm.com/docs/vpc?topic=vpc-profiles).

| VSI component | Default IBM Cloud® quota | Default cluster configuration | Maximum number of clusters |
|----|----|----|----|
| vCPU | 200 vCPUs per region | 28 vCPUs, or 24 vCPUs after bootstrap removal | 8 per region |
| RAM | 1600 GB per region | 112 GB, or 96 GB after bootstrap removal | 16 per region |
| Storage | 18 TB per region | 1050 GB, or 900 GB after bootstrap removal | 19 per region |

VSI component quotas and limits

If you plan to exceed the resources stated in the table, you must increase your IBM Cloud® account quota.

## Block Storage Volumes

For each VPC machine, a block storage device is attached for its boot volume. The default cluster configuration creates seven VPC machines, resulting in seven block storage volumes. Additional Kubernetes persistent volume claims (PVCs) of the IBM Cloud® storage class create additional block storage volumes. The default quota of VPC block storage volumes are 300 per region. To have more than 300 volumes, you must increase this quota.

# Configuring DNS resolution

How you configure DNS resolution depends on the type of OpenShift Container Platform cluster you are installing:

- If you are installing a public cluster, you use IBM Cloud Internet Services (CIS).

- If you are installing a private cluster, you use IBM Cloud® DNS Services (DNS Services)

## Using IBM Cloud Internet Services for DNS resolution

The installation program uses IBM Cloud® Internet Services (CIS) to configure cluster DNS resolution and provide name lookup for a public cluster.

> [!NOTE]
> This offering does not support IPv6, so dual stack or IPv6 environments are not possible.

You must create a domain zone in CIS in the same account as your cluster. You must also ensure the zone is authoritative for the domain. You can do this using a root domain or subdomain.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the [IBM Cloud® CLI](https://www.ibm.com/cloud/cli).

- You have an existing domain and registrar. For more information, see the IBM® [documentation](https://cloud.ibm.com/docs/dns?topic=dns-getting-started).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a CIS instance to use with your cluster:

    1.  Install the CIS plugin:

        ``` terminal
        $ ibmcloud plugin install cis
        ```

    2.  Create the CIS instance:

        ``` terminal
        $ ibmcloud cis instance-create <instance_name> standard-next
        ```

        - At a minimum, you require a `Standard Next` plan for CIS to manage the cluster subdomain and its DNS records.

          > [!NOTE]
          > After you have configured your registrar or DNS provider, it can take up to 24 hours for the changes to take effect.

2.  Connect an existing domain to your CIS instance:

    1.  Set the context instance for CIS:

        ``` terminal
        $ ibmcloud cis instance-set <instance_name>
        ```

        - The instance cloud resource name.

    2.  Add the domain for CIS:

        ``` terminal
        $ ibmcloud cis domain-add <domain_name>
        ```

        - The fully qualified domain name. You can use either the root domain or subdomain value as the domain name, depending on which you plan to configure.

          > [!NOTE]
          > A root domain uses the form `openshiftcorp.com`. A subdomain uses the form `clusters.openshiftcorp.com`.

3.  Open the [CIS web console](https://cloud.ibm.com/catalog/services/internet-services), navigate to the **Overview** page, and note your CIS name servers. These name servers will be used in the next step.

4.  Configure the name servers for your domains or subdomains at the domain’s registrar or DNS provider. For more information, see the IBM Cloud® [documentation](https://cloud.ibm.com/docs/cis?topic=cis-getting-started#configure-your-name-servers-with-the-registrar-or-existing-dns-provider).

</div>

## Using IBM Cloud DNS Services for DNS resolution

The installation program uses IBM Cloud® DNS Services to configure cluster DNS resolution and provide name lookup for a private cluster.

You configure DNS resolution by creating a DNS services instance for the cluster, and then adding a DNS zone to the DNS Services instance. Ensure that the zone is authoritative for the domain. You can do this using a root domain or subdomain.

> [!NOTE]
> IBM Cloud® does not support IPv6, so dual stack or IPv6 environments are not possible.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the [IBM Cloud® CLI](https://www.ibm.com/cloud/cli).

- You have an existing domain and registrar. For more information, see the IBM® [documentation](https://cloud.ibm.com/docs/dns?topic=dns-getting-started).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a DNS Services instance to use with your cluster:

    1.  Install the DNS Services plugin by running the following command:

        ``` terminal
        $ ibmcloud plugin install cloud-dns-services
        ```

    2.  Create the DNS Services instance by running the following command:

        ``` terminal
        $ ibmcloud dns instance-create <instance-name> standard-dns
        ```

        - At a minimum, you require a `Standard DNS` plan for DNS Services to manage the cluster subdomain and its DNS records.

          > [!NOTE]
          > After you have configured your registrar or DNS provider, it can take up to 24 hours for the changes to take effect.

2.  Create a DNS zone for the DNS Services instance:

    1.  Set the target operating DNS Services instance by running the following command:

        ``` terminal
        $ ibmcloud dns instance-target <instance-name>
        ```

    2.  Add the DNS zone to the DNS Services instance by running the following command:

        ``` terminal
        $ ibmcloud dns zone-create <zone-name>
        ```

        - The fully qualified zone name. You can use either the root domain or subdomain value as the zone name, depending on which you plan to configure. A root domain uses the form `openshiftcorp.com`. A subdomain uses the form `clusters.openshiftcorp.com`.

3.  Record the name of the DNS zone you have created. As part of the installation process, you must update the `install-config.yaml` file before deploying the cluster. Use the name of the DNS zone as the value for the `baseDomain` parameter.

</div>

> [!NOTE]
> You do not have to manage permitted networks or configure an "A" DNS resource record. As required, the installation program configures these resources automatically.

# IBM Cloud IAM Policies and API Key

To install OpenShift Container Platform into your IBM Cloud® account, the installation program requires an IAM API key, which provides authentication and authorization to access IBM Cloud® service APIs. You can use an existing IAM API key that contains the required policies or create a new one.

For an IBM Cloud® IAM overview, see the IBM Cloud® [documentation](https://cloud.ibm.com/docs/account?topic=account-iamoverview).

## Required access policies

You must assign the required access policies to your IBM Cloud® account.

| Service type | Service | Access policy scope | Platform access | Service access |
|----|----|----|----|----|
| Account management | IAM Identity Service | All resources or a subset of resources <sup>\[1\]</sup> | Editor, Operator, Viewer, Administrator | Service ID creator |
| Account management <sup>\[2\]</sup> | Identity and Access Management | All resources | Editor, Operator, Viewer, Administrator |  |
| Account management | Resource group only | All resource groups in the account | Administrator |  |
| IAM services | Cloud Object Storage | All resources or a subset of resources <sup>\[1\]</sup> | Editor, Operator, Viewer, Administrator | Reader, Writer, Manager, Content Reader, Object Reader, Object Writer |
| IAM services | Internet Services | All resources or a subset of resources <sup>\[1\]</sup> | Editor, Operator, Viewer, Administrator | Reader, Writer, Manager |
| IAM services | DNS Services | All resources or a subset of resources <sup>\[1\]</sup> | Editor, Operator, Viewer, Administrator | Reader, Writer, Manager |
| IAM services | VPC Infrastructure Services | All resources or a subset of resources <sup>\[1\]</sup> | Editor, Operator, Viewer, Administrator | Reader, Writer, Manager |

Required access policies

1.  The policy access scope should be set based on how granular you want to assign access. The scope can be set to **All resources** or **Resources based on selected attributes**.

2.  Optional: This access policy is only required if you want the installation program to create a resource group. For more information about resource groups, see the IBM® [documentation](https://cloud.ibm.com/docs/account?topic=account-rgs).

## Access policy assignment

In IBM Cloud® IAM, access policies can be attached to different subjects:

- Access group (Recommended)

- Service ID

- User

> [!NOTE]
> The recommended method is to define IAM access policies in an [access group](https://cloud.ibm.com/docs/account?topic=account-groups). This helps organize all the access required for OpenShift Container Platform and enables you to onboard users and service IDs to this group. You can also assign access to [users and service IDs](https://cloud.ibm.com/docs/account?topic=account-assign-access-resources) directly, if desired.

## Creating an API key

You must create a user API key or a service ID API key for your IBM Cloud® account.

<div>

<div class="title">

Prerequisites

</div>

- You have assigned the required access policies to your IBM Cloud® account.

- You have attached you IAM access policies to an access group, or other appropriate resource.

</div>

<div>

<div class="title">

Procedure

</div>

- Create an API key, depending on how you defined your IAM access policies.

  For example, if you assigned your access policies to a user, you must create a [user API key](https://cloud.ibm.com/docs/account?topic=account-userapikey). If you assigned your access policies to a service ID, you must create a [service ID API key](https://cloud.ibm.com/docs/account?topic=account-serviceidapikeys). If your access policies are assigned to an access group, you can use either API key type. For more information on IBM Cloud® API keys, see [Understanding API keys](https://cloud.ibm.com/docs/account?topic=account-manapikey&interface=ui).

</div>

# Supported IBM Cloud regions

You can deploy an OpenShift Container Platform cluster to the following regions:

- `au-syd` (Sydney, Australia)

- `br-sao` (Sao Paulo, Brazil)

- `ca-tor` (Toronto, Canada)

- `eu-de` (Frankfurt, Germany)

- `eu-gb` (London, United Kingdom)

- `eu-es` (Madrid, Spain)

- `jp-osa` (Osaka, Japan)

- `jp-tok` (Tokyo, Japan)

- `us-east` (Washington DC, United States)

- `us-south` (Dallas, United States)

> [!NOTE]
> Deploying your cluster in the `eu-es` (Madrid, Spain) region is not supported for OpenShift Container Platform 4.14.6 and earlier versions.

# Next steps

- [Configuring IAM for IBM Cloud®](configuring-iam-ibm-cloud.md#configuring-iam-ibm-cloud)
