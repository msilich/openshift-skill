<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you can install OpenShift Container Platform, you must configure an IBM Cloud® account.

# Prerequisites

- You have an IBM Cloud® account with a subscription. You cannot install OpenShift Container Platform on a free or on a trial IBM Cloud® account.

# Quotas and limits on IBM Power Virtual Server

The OpenShift Container Platform cluster uses several IBM Cloud® and IBM Power® Virtual Server components, and the default quotas and limits affect your ability to install OpenShift Container Platform clusters. If you use certain cluster configurations, deploy your cluster in certain regions, or run multiple clusters from your account, you might need to request additional resources for your IBM Cloud® account.

For a comprehensive list of the default IBM Cloud® quotas and service limits, see the IBM Cloud® documentation for [Quotas and service limits](https://cloud.ibm.com/docs/vpc?topic=vpc-quotas).

## Virtual Private Cloud

Each OpenShift Container Platform cluster creates its own Virtual Private Cloud (VPC). The default quota of VPCs per region is 10. If you have 10 VPCs created, you will need to increase your quota before attempting an installation.

## Application load balancer

By default, each cluster creates two application load balancers (ALBs):

- Internal load balancer for the control plane API server

- External load balancer for the control plane API server

You can create additional `LoadBalancer` service objects to create additional ALBs. The default quota of VPC ALBs are 50 per region. To have more than 50 ALBs, you must increase this quota.

VPC ALBs are supported. Classic ALBs are not supported for IBM Power® Virtual Server.

## Transit Gateways

Each OpenShift Container Platform cluster creates its own Transit Gateway to enable communication with a VPC. The default quota of transit gateways per account is 10. If you have 10 transit gateways created, you will need to increase your quota before attempting an installation.

## Dynamic Host Configuration Protocol Service

There is a limit of one Dynamic Host Configuration Protocol (DHCP) service per IBM Power® Virtual Server instance.

## Virtual Server Instances

By default, a cluster creates server instances with the following resources :

- 0.5 CPUs

- 32 GB RAM

- System Type: `s922`

- Processor Type: `uncapped`, `shared`

- Storage Tier: `Tier-3`

The following nodes are created:

- One bootstrap machine, which is removed after the installation is complete

- Three control plane nodes

- Three compute nodes

For more information, see [Creating a Power Systems Virtual Server](https://cloud.ibm.com/docs/power-iaas?topic=power-iaas-creating-power-virtual-server) in the IBM Cloud® documentation.

# Configuring DNS resolution

How you configure DNS resolution depends on the type of OpenShift Container Platform cluster you are installing:

- If you are installing a public cluster, you use IBM Cloud® Internet Services (CIS).

- If you are installing a private cluster, you use IBM Cloud® DNS Services (DNS Services).

# Using IBM Cloud Internet Services for DNS resolution

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

    2.  Log in to IBM Cloud® by using the CLI:

        ``` terminal
        $ ibmcloud login
        ```

    3.  Create the CIS instance:

        ``` terminal
        $ ibmcloud cis instance-create <instance_name> standard-next
        ```

        - At a minimum, you require a `Standard Next` plan for CIS to manage the cluster subdomain and its DNS records.

          > [!NOTE]
          > After you have configured your registrar or DNS provider, it can take up to 24 hours for the changes to take effect.

2.  Connect an existing domain to your CIS instance:

    1.  Set the context instance for CIS:

        ``` terminal
        $ ibmcloud cis instance-set <instance_CRN>
        ```

        - The instance CRN (Cloud Resource Name). For example: `ibmcloud cis instance-set crn:v1:bluemix:public:power-iaas:osa21:a/65b64c1f1c29460d8c2e4bbfbd893c2c:c09233ac-48a5-4ccb-a051-d1cfb3fc7eb5::`

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

# IBM Cloud IAM Policies and API Key

To install OpenShift Container Platform into your IBM Cloud® account, the installation program requires an IAM API key, which provides authentication and authorization to access IBM Cloud® service APIs. You can use an existing IAM API key that contains the required policies or create a new one.

For an IBM Cloud® IAM overview, see the IBM Cloud® [documentation](https://cloud.ibm.com/docs/account?topic=account-iamoverview).

## Pre-requisite permissions

| Role | Access |
|----|----|
| Viewer, Operator, Editor, Administrator, Reader, Writer, Manager | Internet Services service in \<resource_group\> resource group |
| Viewer, Operator, Editor, Administrator, User API key creator, Service ID creator | IAM Identity Service service |
| Viewer, Operator, Administrator, Editor, Reader, Writer, Manager, Console Administrator | VPC Infrastructure Services service in \<resource_group\> resource group |
| Viewer | Resource Group: Access to view the resource group itself. The resource type should equal `Resource group`, with a value of \<your_resource_group_name\>. |

Pre-requisite permissions

## Cluster-creation permissions

| Role | Access |
|----|----|
| Viewer | \<resource_group\> (Resource Group Created for Your Team) |
| Viewer, Operator, Editor, Reader, Writer, Manager | All Identity and IAM enabled services in Default resource group |
| Viewer, Reader | Internet Services service |
| Viewer, Operator, Reader, Writer, Manager, Content Reader, Object Reader, Object Writer, Editor | Cloud Object Storage service |
| Viewer | Default resource group: The resource type should equal `Resource group`, with a value of `Default`. If your account administrator changed your account’s default resource group to something other than Default, use that value instead. |
| Viewer, Operator, Editor, Reader, Manager | Workspace for IBM Power® Virtual Server service in \<resource_group\> resource group |
| Viewer, Operator, Editor, Reader, Writer, Manager, Administrator | Internet Services service in \<resource_group\> resource group: CIS functional scope string equals reliability |
| Viewer, Operator, Editor | Transit Gateway service |
| Viewer, Operator, Editor, Administrator, Reader, Writer, Manager, Console Administrator | VPC Infrastructure Services service \<resource_group\> resource group |

Cluster-creation permissions

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

# Supported IBM Power Virtual Server regions and zones

You can deploy an OpenShift Container Platform cluster to the following regions:

- `tor` (Toronto, Canada)

  - `tor01`

- `dal` (Dallas, USA)

  - `dal10`

  - `dal12`

- `eu-de` (Frankfurt, Germany)

  - `eu-de-1`

  - `eu-de-2`

- `lon` (London, UK)

  - `lon04`

  - `lon06`

- `mad` (Madrid, Spain)

  - `mad02`

  - `mad04`

- `osa` (Osaka, Japan)

  - `osa21`

- `sao` (Sao Paulo, Brazil)

  - `sao01`

  - `sao04`

- `syd` (Sydney, Australia)

  - `syd04`

  - `syd05`

- `wdc` (Washington DC, USA)

  - `wdc06`

  - `wdc07`

- `us-east` (Washington DC, United States)

  - `us-east`

- `us-south` (Dallas, United States)

  - `us-south`

You might optionally specify the IBM Cloud® region in which the installation program creates any VPC components.

> [!NOTE]
> If you do not specify the region, the installation program selects the region closest to IBM Power Virtual Server zone you are deploying to.

IBM Cloud® supports the following regions:

- `us-east`

- `us-south`

- `eu-de`

- `eu-es`

- `eu-gb`

- `jp-osa`

- `au-syd`

- `br-sao`

- `ca-tor`

- `jp-tok`

# Next steps

- [Creating an IBM Power® Virtual Server workspace](creating-ibm-power-vs-workspace.md#creating-ibm-power-vs-workspace)
