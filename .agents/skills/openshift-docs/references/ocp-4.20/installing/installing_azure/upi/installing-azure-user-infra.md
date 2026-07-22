<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform version 4.17, you can install a cluster on Microsoft Azure by using infrastructure that you provide.

Several [Azure Resource Manager](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/overview) (ARM) templates are provided to assist in completing these steps or to help model your own.

> [!IMPORTANT]
> The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several ARM templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods; the templates are just an example.

# Prerequisites

- You reviewed details about the [OpenShift Container Platform installation and update](../../../architecture/architecture-installation.md#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../../overview/installing-preparing.md#installing-preparing).

- You [configured an Azure account](../installing-azure-account.md#installing-azure-account) to host the cluster.

- You downloaded the Azure CLI and installed it on your computer. See [Install the Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) in the Azure documentation. The following documentation was last tested using version `2.49.0` of the Azure CLI. Azure CLI commands might perform differently based on the version you use.

- If the cloud identity and access management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, see [Alternatives to storing administrator-level secrets in the kube-system project](../ipi/installing-azure-customizations.md#installing-azure-manual-modes_installing-azure-customizations).

- If you use a firewall and plan to use the Telemetry service, you [configured the firewall to allow the sites](../../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall) that your cluster requires access to.

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

# Configuring your Azure project

Before you can install OpenShift Container Platform, you must configure an Azure project to host it.

> [!IMPORTANT]
> All Azure resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure restricts, see [Resolve reserved resource name errors](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-reserved-resource-name) in the Azure documentation.

## Azure account limits

The OpenShift Container Platform cluster uses a number of Microsoft Azure components. Default subscription and service limits, quotas, and constraints can affect your ability to install OpenShift Container Platform clusters.

For more information on Azure subscription and service limits, see "Azure subscription and service limits, quotas, and constraints".

> [!IMPORTANT]
> Default limits vary by offer category types, such as Free Trial and Pay-As-You-Go, and by series, such as Dv2, F, and G. For example, the default for Enterprise Agreement subscriptions is 350 cores.
>
> Check the limits for your subscription type and if necessary, increase quota limits for your account before you install a default cluster on Azure.

The following table summarizes the Azure components whose limits can impact your ability to install and run OpenShift Container Platform clusters.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Component</th>
<th style="text-align: left;">Number of components required by default</th>
<th style="text-align: left;">Default Azure limit</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>vCPU</p></td>
<td style="text-align: left;"><p>40</p></td>
<td style="text-align: left;"><p>20 per region</p></td>
<td style="text-align: left;"><p>A default cluster requires 40 vCPUs, so you must increase the account limit.</p>
<p>By default, each cluster creates the following instances:</p>
<ul>
<li><p>One bootstrap machine, which is removed after installation</p></li>
<li><p>Three control plane machines</p></li>
<li><p>Three compute machines</p></li>
</ul>
<p>Because the bootstrap machine uses <code>Standard_D4s_v3</code> machines, which use 4 vCPUs, the control plane machines use <code>Standard_D8s_v3</code> virtual machines, which use 8 vCPUs, and the worker machines use <code>Standard_D4s_v3</code> virtual machines, which use 4 vCPUs, a default cluster requires 40 vCPUs. The bootstrap node VM, which uses 4 vCPUs, is used only during installation.</p>
<p>To deploy more worker nodes, enable autoscaling, deploy large workloads, or use a different instance type, you must further increase the vCPU limit for your account to ensure that your cluster can deploy the machines that you require.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>OS Disk</p></td>
<td style="text-align: left;"><p>7</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Each cluster machine must have a minimum of 100 GB of storage and 300 IOPS.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Faster storage is recommended for production clusters and clusters with intensive workloads. For more information about optimizing storage for performance, see the page titled "Optimizing storage" in the "Scalability and performance" section.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p>VNet</p></td>
<td style="text-align: left;"><p>1</p></td>
<td style="text-align: left;"><p>1000 per region</p></td>
<td style="text-align: left;"><p>Each default cluster requires one Virtual Network (VNet), which contains two subnets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Network interfaces</p></td>
<td style="text-align: left;"><p>7</p></td>
<td style="text-align: left;"><p>65,536 per region</p></td>
<td style="text-align: left;"><p>Each default cluster requires seven network interfaces. If you create more machines or your deployed workloads create load balancers, your cluster uses more network interfaces.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Network security groups</p></td>
<td style="text-align: left;"><p>2</p></td>
<td style="text-align: left;"><p>5000</p></td>
<td style="text-align: left;"><p>Each cluster creates network security groups for each subnet in the VNet. The default cluster creates network security groups for the control plane and for the compute node subnets:</p>
<table data-custom-style="horizontal">
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<tbody>
<tr>
<td><p><code>controlplane</code></p></td>
<td><p>Allows the control plane machines to be reached on port 6443 from anywhere</p></td>
</tr>
<tr>
<td><p><code>node</code></p></td>
<td><p>Allows worker nodes to be reached from the internet on ports 80 and 443</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td style="text-align: left;"><p>Network load balancers</p></td>
<td style="text-align: left;"><p>3</p></td>
<td style="text-align: left;"><p>1000 per region</p></td>
<td style="text-align: left;"><p>Each cluster creates the following <a href="https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview">load balancers</a>:</p>
<table data-custom-style="horizontal">
<colgroup>
<col style="width: 15%" />
<col style="width: 85%" />
</colgroup>
<tbody>
<tr>
<td><p><code>default</code></p></td>
<td><p>Public IP address that load balances requests to ports 80 and 443 across worker machines</p></td>
</tr>
<tr>
<td><p><code>internal</code></p></td>
<td><p>Private IP address that load balances requests to ports 6443 and 22623 across control plane machines</p></td>
</tr>
<tr>
<td><p><code>external</code></p></td>
<td><p>Public IP address that load balances requests to port 6443 across control plane machines</p></td>
</tr>
</tbody>
</table>
<p>If your applications create more Kubernetes <code>LoadBalancer</code> service objects, your cluster uses more load balancers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Public IP addresses</p></td>
<td style="text-align: left;"><p>3</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Each of the two public load balancers uses a public IP address. The bootstrap machine also uses a public IP address so that you can SSH into the machine to troubleshoot issues during installation. The IP address for the bootstrap node is used only during installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Private IP addresses</p></td>
<td style="text-align: left;"><p>7</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The internal load balancer, each of the three control plane machines, and each of the three worker machines each use a private IP address.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Spot VM vCPUs (optional)</p></td>
<td style="text-align: left;"><p>0</p>
<p>If you configure spot VMs, your cluster must have two spot VM vCPUs for every compute node.</p></td>
<td style="text-align: left;"><p>20 per region</p></td>
<td style="text-align: left;"><p>This is an optional component. To use spot VMs, you must increase the Azure default limit to at least twice the number of compute nodes in your cluster.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Using spot VMs for control plane nodes is not recommended.</p>
</div></td>
</tr>
</tbody>
</table>

To increase an account limit, file a support request on the Azure portal. For more information, see [Request a quota limit increase for Azure Deployment Environments resources](https://learn.microsoft.com/en-us/azure/deployment-environments/how-to-request-quota-increase).

<div>

<div class="title">

Additional resources

</div>

- [Optimizing storage](../../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

- [Azure subscription and service limits, quotas, and constraints (Azure documentation)](https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits)

</div>

## Configuring a public DNS zone in Azure

To install OpenShift Container Platform, the Microsoft Azure account you use must have a dedicated public hosted DNS zone in your account that is authoritative for the domain. This zone provides cluster DNS resolution and name lookup for external connections to the cluster.

<div>

<div class="title">

Procedure

</div>

1.  Identify your domain, or subdomain, and registrar. You can transfer an existing domain and registrar or obtain a new one through Azure or another source.

    - To purchase a new domain through Azure, see [Buy a custom domain name for Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/manage-custom-dns-buy-domain).

    - If you are using an existing domain and registrar, migrate its DNS to Azure. For more information, see [Migrate an active DNS name to Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/manage-custom-dns-migrate-domain) in the Azure documentation.

2.  Configure DNS for your domain, which includes creating a public hosted zone for your domain or subdomain, extracting the new authoritative name servers, and updating the registrar records for the name servers that your domain uses. For more information, see [Tutorial: Host your domain in Azure DNS](https://docs.microsoft.com/en-us/azure/dns/dns-delegate-domain-azure-dns).

    Use an appropriate root domain, such as `openshiftcorp.com`, or subdomain, such as `clusters.openshiftcorp.com`.

3.  If you use a subdomain, follow your organization’s procedures to add its delegation records to the parent domain.

</div>

You can view Azure’s DNS solution by visiting this [example for creating DNS zones](#installation-azure-create-dns-zones_installing-azure-user-infra).

## Certificate signing requests management

On user-provisioned infrastructure, you must provide a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that is requested by using kubelet credentials because it cannot confirm that the correct machine issued the request. You must determine and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

## Recording the subscription and tenant IDs

To record the subscription and tenant IDs that the installation program requires for your Azure account, you can use the Azure CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have installed or updated the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-yum?view=azure-cli-latest).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the Azure CLI by running the following command:

    ``` terminal
    $ az login
    ```

2.  Ensure that you are using the right subscription:

    1.  View a list of available subscriptions by running the following command:

        ``` terminal
        $ az account list --refresh
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        [
          {
            "cloudName": "AzureCloud",
            "id": "8xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "isDefault": true,
            "name": "Subscription Name 1",
            "state": "Enabled",
            "tenantId": "6xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "user": {
              "name": "you@example.com",
              "type": "user"
            }
          },
          {
            "cloudName": "AzureCloud",
            "id": "9xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "isDefault": false,
            "name": "Subscription Name 2",
            "state": "Enabled",
            "tenantId": "7xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "user": {
              "name": "you2@example.com",
              "type": "user"
            }
          }
        ]
        ```

        </div>

    2.  View the details of the active account, and confirm that this is the subscription you want to use, by running the following command:

        ``` terminal
        $ az account show
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        {
          "environmentName": "AzureCloud",
          "id": "8xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "isDefault": true,
          "name": "Subscription Name 1",
          "state": "Enabled",
          "tenantId": "6xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "user": {
            "name": "you@example.com",
            "type": "user"
          }
        }
        ```

        </div>

3.  If you are not using the right subscription:

    1.  Change the active subscription by running the following command:

        ``` terminal
        $ az account set -s <subscription_id>
        ```

    2.  Verify that you are using the subscription you need by running the following command:

        ``` terminal
        $ az account show
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        {
          "environmentName": "AzureCloud",
          "id": "9xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "isDefault": true,
          "name": "Subscription Name 2",
          "state": "Enabled",
          "tenantId": "7xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "user": {
            "name": "you2@example.com",
            "type": "user"
          }
        }
        ```

        </div>

4.  Record the `id` and `tenantId` parameter values from the output. You require these values to install an OpenShift Container Platform cluster.

</div>

## Supported identities to access Azure resources

An OpenShift Container Platform cluster requires an Azure identity to create and manage Azure resources. You need a service principal, a system-assigned managed identity, or a user-assigned managed identity to complete the installation.

- A service principal

- A system-assigned managed identity

- A user-assigned managed identity

For more information on Azure identities, see "Managed identity types".

## Required Azure permissions for user-provisioned infrastructure

The installation program requires access to an Azure service principal or managed identity with the necessary permissions to deploy the cluster and to maintain its daily operation. These permissions must be granted to the Azure subscription that is associated with the identity.

The following options are available to you:

- You can assign the identity the `Contributor` and `User Access Administrator` roles. Assigning these roles is the quickest way to grant all of the required permissions.

  For more information about assigning roles, see the Azure documentation for [managing access to Azure resources using the Azure portal](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).

- If your organization’s security policies require a more restrictive set of permissions, you can create a [custom role](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles) with the necessary permissions.

The following permissions are required for creating an OpenShift Container Platform cluster on Microsoft Azure.

<div class="example">

<div class="title">

Required permissions for creating authorization resources

</div>

- `Microsoft.Authorization/policies/audit/action`

- `Microsoft.Authorization/policies/auditIfNotExists/action`

- `Microsoft.Authorization/roleAssignments/read`

- `Microsoft.Authorization/roleAssignments/write`

</div>

<div class="example">

<div class="title">

Required permissions for creating compute resources

</div>

- `Microsoft.Compute/images/read`

- `Microsoft.Compute/images/write`

- `Microsoft.Compute/images/delete`

- `Microsoft.Compute/availabilitySets/read`

- `Microsoft.Compute/disks/beginGetAccess/action`

- `Microsoft.Compute/disks/delete`

- `Microsoft.Compute/disks/read`

- `Microsoft.Compute/disks/write`

- `Microsoft.Compute/galleries/images/read`

- `Microsoft.Compute/galleries/images/versions/read`

- `Microsoft.Compute/galleries/images/versions/write`

- `Microsoft.Compute/galleries/images/write`

- `Microsoft.Compute/galleries/read`

- `Microsoft.Compute/galleries/write`

- `Microsoft.Compute/snapshots/read`

- `Microsoft.Compute/snapshots/write`

- `Microsoft.Compute/snapshots/delete`

- `Microsoft.Compute/virtualMachines/delete`

- `Microsoft.Compute/virtualMachines/powerOff/action`

- `Microsoft.Compute/virtualMachines/read`

- `Microsoft.Compute/virtualMachines/write`

- `Microsoft.Compute/virtualMachines/deallocate/action`

</div>

<div class="example">

<div class="title">

Required permissions for creating identity management resources

</div>

- `Microsoft.ManagedIdentity/userAssignedIdentities/assign/action`

- `Microsoft.ManagedIdentity/userAssignedIdentities/read`

- `Microsoft.ManagedIdentity/userAssignedIdentities/write`

</div>

<div class="example">

<div class="title">

Required permissions for creating network resources

</div>

- `Microsoft.Network/dnsZones/A/write`

- `Microsoft.Network/dnsZones/CNAME/write`

- `Microsoft.Network/dnszones/CNAME/read`

- `Microsoft.Network/dnszones/read`

- `Microsoft.Network/loadBalancers/backendAddressPools/join/action`

- `Microsoft.Network/loadBalancers/backendAddressPools/read`

- `Microsoft.Network/loadBalancers/backendAddressPools/write`

- `Microsoft.Network/loadBalancers/read`

- `Microsoft.Network/loadBalancers/write`

- `Microsoft.Network/networkInterfaces/delete`

- `Microsoft.Network/networkInterfaces/join/action`

- `Microsoft.Network/networkInterfaces/read`

- `Microsoft.Network/networkInterfaces/write`

- `Microsoft.Network/networkSecurityGroups/join/action`

- `Microsoft.Network/networkSecurityGroups/read`

- `Microsoft.Network/networkSecurityGroups/securityRules/delete`

- `Microsoft.Network/networkSecurityGroups/securityRules/read`

- `Microsoft.Network/networkSecurityGroups/securityRules/write`

- `Microsoft.Network/networkSecurityGroups/write`

- `Microsoft.Network/privateDnsZones/A/read`

- `Microsoft.Network/privateDnsZones/A/write`

- `Microsoft.Network/privateDnsZones/A/delete`

- `Microsoft.Network/privateDnsZones/SOA/read`

- `Microsoft.Network/privateDnsZones/read`

- `Microsoft.Network/privateDnsZones/virtualNetworkLinks/read`

- `Microsoft.Network/privateDnsZones/virtualNetworkLinks/write`

- `Microsoft.Network/privateDnsZones/write`

- `Microsoft.Network/publicIPAddresses/delete`

- `Microsoft.Network/publicIPAddresses/join/action`

- `Microsoft.Network/publicIPAddresses/read`

- `Microsoft.Network/publicIPAddresses/write`

- `Microsoft.Network/virtualNetworks/join/action`

- `Microsoft.Network/virtualNetworks/read`

- `Microsoft.Network/virtualNetworks/subnets/join/action`

- `Microsoft.Network/virtualNetworks/subnets/read`

- `Microsoft.Network/virtualNetworks/subnets/write`

- `Microsoft.Network/virtualNetworks/write`

</div>

<div class="example">

<div class="title">

Required permissions for checking the health of resources

</div>

- `Microsoft.Resourcehealth/healthevent/Activated/action`

- `Microsoft.Resourcehealth/healthevent/InProgress/action`

- `Microsoft.Resourcehealth/healthevent/Pending/action`

- `Microsoft.Resourcehealth/healthevent/Resolved/action`

- `Microsoft.Resourcehealth/healthevent/Updated/action`

</div>

<div class="example">

<div class="title">

Required permissions for creating a resource group

</div>

- `Microsoft.Resources/subscriptions/resourceGroups/read`

- `Microsoft.Resources/subscriptions/resourcegroups/write`

</div>

<div class="example">

<div class="title">

Required permissions for creating resource tags

</div>

- `Microsoft.Resources/tags/write`

</div>

<div class="example">

<div class="title">

Required permissions for creating storage resources

</div>

- `Microsoft.Storage/storageAccounts/blobServices/read`

- `Microsoft.Storage/storageAccounts/blobServices/containers/write`

- `Microsoft.Storage/storageAccounts/fileServices/read`

- `Microsoft.Storage/storageAccounts/fileServices/shares/read`

- `Microsoft.Storage/storageAccounts/fileServices/shares/write`

- `Microsoft.Storage/storageAccounts/fileServices/shares/delete`

- `Microsoft.Storage/storageAccounts/listKeys/action`

- `Microsoft.Storage/storageAccounts/read`

- `Microsoft.Storage/storageAccounts/write`

</div>

<div class="example">

<div class="title">

Required permissions for creating deployments

</div>

- `Microsoft.Resources/deployments/read`

- `Microsoft.Resources/deployments/write`

- `Microsoft.Resources/deployments/validate/action`

- `Microsoft.Resources/deployments/operationstatuses/read`

</div>

<div class="example">

<div class="title">

Optional permissions for creating compute resources

</div>

- `Microsoft.Compute/availabilitySets/delete`

- `Microsoft.Compute/availabilitySets/write`

</div>

<div class="example">

<div class="title">

Optional permissions for creating marketplace virtual machine resources

</div>

- `Microsoft.MarketplaceOrdering/offertypes/publishers/offers/plans/agreements/read`

- `Microsoft.MarketplaceOrdering/offertypes/publishers/offers/plans/agreements/write`

</div>

<div class="example">

<div class="title">

Optional permissions for enabling user-managed encryption

</div>

- `Microsoft.Compute/diskEncryptionSets/read`

- `Microsoft.Compute/diskEncryptionSets/write`

- `Microsoft.Compute/diskEncryptionSets/delete`

- `Microsoft.KeyVault/vaults/read`

- `Microsoft.KeyVault/vaults/write`

- `Microsoft.KeyVault/vaults/delete`

- `Microsoft.KeyVault/vaults/deploy/action`

- `Microsoft.KeyVault/vaults/keys/read`

- `Microsoft.KeyVault/vaults/keys/write`

- `Microsoft.Features/providers/features/register/action`

</div>

The following permissions are required for deleting an OpenShift Container Platform cluster on Microsoft Azure.

<div class="example">

<div class="title">

Required permissions for deleting authorization resources

</div>

- `Microsoft.Authorization/roleAssignments/delete`

</div>

<div class="example">

<div class="title">

Required permissions for deleting compute resources

</div>

- `Microsoft.Compute/disks/delete`

- `Microsoft.Compute/galleries/delete`

- `Microsoft.Compute/galleries/images/delete`

- `Microsoft.Compute/galleries/images/versions/delete`

- `Microsoft.Compute/virtualMachines/delete`

- `Microsoft.Compute/images/delete`

</div>

<div class="example">

<div class="title">

Required permissions for deleting identity management resources

</div>

- `Microsoft.ManagedIdentity/userAssignedIdentities/delete`

</div>

<div class="example">

<div class="title">

Required permissions for deleting network resources

</div>

- `Microsoft.Network/dnszones/read`

- `Microsoft.Network/dnsZones/A/read`

- `Microsoft.Network/dnsZones/A/delete`

- `Microsoft.Network/dnsZones/CNAME/read`

- `Microsoft.Network/dnsZones/CNAME/delete`

- `Microsoft.Network/loadBalancers/delete`

- `Microsoft.Network/networkInterfaces/delete`

- `Microsoft.Network/networkSecurityGroups/delete`

- `Microsoft.Network/privateDnsZones/read`

- `Microsoft.Network/privateDnsZones/A/read`

- `Microsoft.Network/privateDnsZones/delete`

- `Microsoft.Network/privateDnsZones/virtualNetworkLinks/delete`

- `Microsoft.Network/publicIPAddresses/delete`

- `Microsoft.Network/virtualNetworks/delete`

</div>

<div class="example">

<div class="title">

Required permissions for checking the health of resources

</div>

- `Microsoft.Resourcehealth/healthevent/Activated/action`

- `Microsoft.Resourcehealth/healthevent/Resolved/action`

- `Microsoft.Resourcehealth/healthevent/Updated/action`

</div>

<div class="example">

<div class="title">

Required permissions for deleting a resource group

</div>

- `Microsoft.Resources/subscriptions/resourcegroups/delete`

</div>

<div class="example">

<div class="title">

Required permissions for deleting storage resources

</div>

- `Microsoft.Storage/storageAccounts/delete`

- `Microsoft.Storage/storageAccounts/listKeys/action`

</div>

> [!NOTE]
> To install OpenShift Container Platform on Azure, you must scope the permissions related to resource group creation to your subscription. After the resource group is created, you can scope the rest of the permissions to the created resource group. If the public DNS zone is present in a different resource group, then the network DNS zone related permissions must always be applied to your subscription.
>
> You can scope all the permissions to your subscription when deleting an OpenShift Container Platform cluster.

## Using Azure managed identities

To provide the identity that the installation program requires on Azure, you can use a system-assigned or user-assigned managed identity.

If you are unable to use a managed identity, you can use a service principal.

<div>

<div class="title">

Procedure

</div>

1.  If you are using a system-assigned managed identity, enable it on the virtual machine that you will run the installation program from.

2.  If you are using a user-assigned managed identity:

    1.  Assign it to the virtual machine that you will run the installation program from.

    2.  Record its client ID. You require this value when installing the cluster.

3.  Verify that the required permissions are assigned to the managed identity.

</div>

## Creating a service principal

To provide the identity that the installation program requires on Azure, you can create a service principal.

If you are unable to use a service principal, you can use a managed identity.

<div>

<div class="title">

Prerequisites

</div>

- You have installed or updated the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-yum?view=azure-cli-latest).

- You have an Azure subscription ID.

- If you are not assigning the `Contributor` and `User Administrator Access` roles to the service principal, you have created a custom role with the required Azure permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the service principal for your account by running the following command:

    ``` terminal
    $ az ad sp create-for-rbac --role <role_name> \
         --name <service_principal> \
         --scopes /subscriptions/<subscription_id>
    ```

    where:

    `<role_name>`
    Specifies the role name. You can use the `Contributor` role, or you can specify a custom role which contains the necessary permissions.

    `<service_principal>`
    Specifies the service principal name.

    `<subscription_id>`
    Specifies the subscription ID.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Creating 'Contributor' role assignment under scope '/subscriptions/<subscription_id>'
    The output includes credentials that you must protect. Be sure that you do not
    include these credentials in your code or check the credentials into your source
    control. For more information, see https://aka.ms/azadsp-cli
    {
      "appId": "axxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "displayName": <service_principal>",
      "password": "00000000-0000-0000-0000-000000000000",
      "tenantId": "8xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
    ```

    </div>

    Record the values of the `appId` and `password` parameters from the output. You require these values when installing the cluster.

2.  If you assigned the `Contributor` role to your service principal, assign the `User Administrator Access` role by running the following command:

    ``` terminal
    $ az role assignment create --role "User Access Administrator" \
      --assignee-object-id $(az ad sp show --id <appId> --query id -o tsv) \
      --scope /subscriptions/<subscription_id>
    ```

    where:

    `<appId>`
    Specifies the `appId` parameter value for your service principal.

    `<subscription_id>`
    Specifies the subscription ID.

</div>

<div>

<div class="title">

Additional resources

</div>

- For more information about CCO modes, see [About the Cloud Credential Operator](../../../authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.md#about-cloud-credential-operator-modes).

</div>

## Supported Azure regions

Base on your subscription, the installation program dynamically generates the list of available Microsoft Azure public regions.

### Supported Azure public regions

- `australiacentral` (Australia Central)

- `australiaeast` (Australia East)

- `australiasoutheast` (Australia South East)

- `austriaeast` (Austria East)

- `belgiumcentral` (Belgium Central)

- `brazilsouth` (Brazil South)

- `canadacentral` (Canada Central)

- `canadaeast` (Canada East)

- `centralindia` (Central India)

- `centralus` (Central US)

- `chilecentral` (Chile Central)

- `eastasia` (East Asia)

- `eastus` (East US)

- `eastus2` (East US 2)

- `francecentral` (France Central)

- `germanywestcentral` (Germany West Central)

- `indonesiacentral` (Indonesia Central)

- `israelcentral` (Israel Central)

- `italynorth` (Italy North)

- `japaneast` (Japan East)

- `japanwest` (Japan West)

- `koreacentral` (Korea Central)

- `koreasouth` (Korea South)

- `malaysiawest` (Malaysia West)

- `mexicocentral` (Mexico Central)

- `newzealandnorth` (New Zealand North)

- `northcentralus` (North Central US)

- `northeurope` (North Europe)

- `norwayeast` (Norway East)

- `polandcentral` (Poland Central)

- `qatarcentral` (Qatar Central)

- `southafricanorth` (South Africa North)

- `southcentralus` (South Central US)

- `southeastasia` (Southeast Asia)

- `southindia` (South India)

- `spaincentral` (Spain Central)

- `swedencentral` (Sweden Central)

- `switzerlandnorth` (Switzerland North)

- `uaenorth` (UAE North)

- `uksouth` (UK South)

- `ukwest` (UK West)

- `westcentralus` (West Central US)

- `westeurope` (West Europe)

- `westindia` (West India)

- `westus` (West US)

- `westus2` (West US 2)

- `westus3` (West US 3)

### Supported Azure Government regions

Support for the following Microsoft Azure Government (MAG) regions was added in OpenShift Container Platform version 4.6:

- `usgovtexas` (US Gov Texas)

- `usgovvirginia` (US Gov Virginia)

You can reference all available MAG regions in the [Azure documentation](https://azure.microsoft.com/en-us/global-infrastructure/geographies/#geographies). Other provided MAG regions are expected to work with OpenShift Container Platform, but have not been tested.

# Requirements for a cluster with user-provisioned infrastructure

For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

This section describes the requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

## Required machines for cluster installation

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails.

The smallest OpenShift Container Platform clusters require the following hosts:

> [!IMPORTANT]
> For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

| Hosts | Description |
|----|----|
| One temporary bootstrap machine | The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster. |
| Three control plane machines | The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane. |
| At least two compute machines, which are also known as worker machines. | The workloads requested by OpenShift Container Platform users run on the compute machines. |

Minimum required hosts

> [!IMPORTANT]
> To maintain high availability of your cluster, use separate physical hosts for these cluster machines.

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. However, the compute machines can choose between Red Hat Enterprise Linux CoreOS (RHCOS), Red Hat Enterprise Linux (RHEL) 8.6 and later.

Note that RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.2 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits).

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

> [!IMPORTANT]
> You are required to use Azure virtual machines that have the `premiumIO` parameter set to `true`.

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

## Tested instance types for Azure

There are several Microsoft Azure instance types tested with OpenShift Container Platform. Choose a listed instance type when you install a cluster on 64-bit x86 infrastructure.

<div class="example">

<div class="title">

Machine types based on 64-bit x86 architecture

</div>

<https://raw.githubusercontent.com/openshift/installer/release-4.20/docs/user/azure/tested_instance_types_x86_64.md>

</div>

## Tested instance types for Azure on 64-bit ARM infrastructures

There are several Microsoft Azure ARM64 instance types tested with OpenShift Container Platform. Choose a listed instance type when you install a cluster on 64-bit ARM infrastructure.

<div class="example">

<div class="title">

Machine types based on 64-bit ARM architecture

</div>

<https://raw.githubusercontent.com/openshift/installer/release-4.20/docs/user/azure/tested_instance_types_aarch64.md>

</div>

# Using the Azure Marketplace offering

You can use the Azure Marketplace offering to deploy an OpenShift Container Platform cluster, which is billed on pay-per-use basis (hourly, per core) through Azure, while still being supported directly by Red Hat.

To deploy an OpenShift Container Platform cluster using the Azure Marketplace offering, you must first obtain the Azure Marketplace image. The installation program uses this image to deploy worker or control plane nodes. When obtaining your image, consider the following:

- While the images are the same, the Azure Marketplace publisher is different depending on your region. If you are located in North America, specify `redhat` as the publisher. If you are located in EMEA, specify `redhat-limited` as the publisher.

- The offer includes a `rh-ocp-worker` SKU and a `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker` SKU represents a Hyper-V generation version 2 VM image. The default instance types used in OpenShift Container Platform are version 2 compatible. If you plan to use an instance type that is only version 1 compatible, use the image associated with the `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker-gen1` SKU represents a Hyper-V version 1 VM image.

> [!IMPORTANT]
> Installing images with the Azure marketplace is not supported on clusters with 64-bit ARM instances.
>
> You should only modify the RHCOS image for compute machines to use an Azure Marketplace image. Control plane machines and infrastructure nodes do not require an OpenShift Container Platform subscription and use the public RHCOS default image by default, which does not incur subscription costs on your Azure bill. Therefore, you should not modify the cluster default boot image or the control plane boot images. Applying the Azure Marketplace image to them will incur additional licensing costs that cannot be recovered.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Azure CLI client `(az)`.

- Your Azure account is entitled for the offer and you have logged into this account with the Azure CLI client.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Display all of the available OpenShift Container Platform images by running one of the following commands:

    - North America:

      ``` terminal
      $  az vm image list --all --offer rh-ocp-worker --publisher redhat -o table
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      Offer          Publisher       Sku                 Urn                                                             Version
      -------------  --------------  ------------------  --------------------------------------------------------------  -----------------
      rh-ocp-worker  RedHat          rh-ocp-worker       RedHat:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
      rh-ocp-worker  RedHat          rh-ocp-worker-gen1  RedHat:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
      ```

      </div>

    - EMEA:

      ``` terminal
      $  az vm image list --all --offer rh-ocp-worker --publisher redhat-limited -o table
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      Offer          Publisher       Sku                 Urn                                                                     Version
      -------------  --------------  ------------------  --------------------------------------------------------------          -----------------
      rh-ocp-worker  redhat-limited  rh-ocp-worker       redhat-limited:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
      rh-ocp-worker  redhat-limited  rh-ocp-worker-gen1  redhat-limited:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
      ```

      </div>

    > [!NOTE]
    > Use the latest image that is available for compute and control plane nodes. If required, your VMs are automatically upgraded as part of the installation process.

2.  Inspect the image for your offer by running one of the following commands:

    - North America:

      ``` terminal
      $ az vm image show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
      ```

    - EMEA:

      ``` terminal
      $ az vm image show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
      ```

3.  Review the terms of the offer by running one of the following commands:

    - North America:

      ``` terminal
      $ az vm image terms show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
      ```

    - EMEA:

      ``` terminal
      $ az vm image terms show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
      ```

4.  Accept the terms of the offering by running one of the following commands:

    - North America:

      ``` terminal
      $ az vm image terms accept --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
      ```

    - EMEA:

      ``` terminal
      $ az vm image terms accept --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
      ```

5.  Record the image details of your offer. If you use the Azure Resource Manager (ARM) template to deploy your compute nodes:

    1.  Update `storageProfile.imageReference` by deleting the `id` parameter and adding the `offer`, `publisher`, `sku`, and `version` parameters by using the values from your offer.

    2.  Specify a `plan` for the virtual machines (VMs).

        <div class="formalpara">

        <div class="title">

        Example `06_workers.json` ARM template with an updated `storageProfile.imageReference` object and a specified `plan`

        </div>

        ``` json
        ...
          "plan" : {
            "name": "rh-ocp-worker",
            "product": "rh-ocp-worker",
            "publisher": "redhat"
          },
          "dependsOn" : [
            "[concat('Microsoft.Network/networkInterfaces/', concat(variables('vmNames')[copyIndex()], '-nic'))]"
          ],
          "properties" : {
        ...
          "storageProfile": {
            "imageReference": {
            "offer": "rh-ocp-worker",
            "publisher": "redhat",
            "sku": "rh-ocp-worker",
            "version": "413.92.2023101700"
            }
            ...
           }
        ...
          }
        ```

        </div>

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

- When you install OpenShift Container Platform, provide the SSH public key to the installation program. If you install a cluster on infrastructure that you provision, you must provide the key to the installation program.

</div>

# Creating the installation files for Azure

To install OpenShift Container Platform on Microsoft Azure using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use. You generate and customize the `install-config.yaml` file, Kubernetes manifests, and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.

## Optional: Creating a separate `/var` partition

It is recommended that disk partitioning for OpenShift Container Platform be left to the installer. However, there are cases where you might want to create separate partitions in a part of the filesystem that you expect to grow.

OpenShift Container Platform supports the addition of a single partition to attach storage to either the `/var` partition or a subdirectory of `/var`. For example:

- `/var/lib/containers`: Holds container-related content that can grow as more images and containers are added to a system.

- `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage.

- `/var`: Holds data that you might want to keep separate for purposes such as auditing.

Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date and keep that data intact. With this method, you will not have to pull all your containers again, nor will you have to copy massive log files when you update systems.

Because `/var` must be in place before a fresh installation of Red Hat Enterprise Linux CoreOS (RHCOS), the following procedure sets up the separate `/var` partition by creating a machine config manifest that is inserted during the `openshift-install` preparation phases of an OpenShift Container Platform installation.

> [!IMPORTANT]
> If you follow the steps to create a separate `/var` partition in this procedure, it is not necessary to create the Kubernetes manifest and Ignition config files again as described later in this section.

<div>

<div class="title">

Procedure

</div>

1.  Create a directory to hold the OpenShift Container Platform installation files:

    ``` terminal
    $ mkdir $HOME/clusterconfig
    ```

2.  Run `openshift-install` to create a set of files in the `manifest` and `openshift` subdirectories. Answer the system questions as you are prompted:

    ``` terminal
    $ openshift-install create manifests --dir $HOME/clusterconfig
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ? SSH Public Key ...
    INFO Credentials loaded from the "myprofile" profile in file "/home/myuser/.aws/credentials"
    INFO Consuming Install Config from target directory
    INFO Manifests created in: $HOME/clusterconfig/manifests and $HOME/clusterconfig/openshift
    ```

    </div>

3.  Optional: Confirm that the installation program created manifests in the `clusterconfig/openshift` directory:

    ``` terminal
    $ ls $HOME/clusterconfig/openshift/
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    99_kubeadmin-password-secret.yaml
    99_openshift-cluster-api_master-machines-0.yaml
    99_openshift-cluster-api_master-machines-1.yaml
    99_openshift-cluster-api_master-machines-2.yaml
    ...
    ```

    </div>

4.  Create a Butane config that configures the additional partition. For example, name the file `$HOME/clusterconfig/98-var-partition.bu`, change the disk device name to the name of the storage device on the `worker` systems, and set the storage size as appropriate. This example places the `/var` directory on a separate partition:

    ``` yaml
    variant: openshift
    version: 4.17.0
    metadata:
      labels:
        machineconfiguration.openshift.io/role: worker
      name: 98-var-partition
    storage:
      disks:
      - device: /dev/disk/by-id/<device_name>
        partitions:
        - label: var
          start_mib: <partition_start_offset>
          size_mib: <partition_size>
          number: 5
      filesystems:
        - device: /dev/disk/by-partlabel/var
          path: /var
          format: xfs
          mount_options: [defaults, prjquota]
          with_mount_unit: true
    ```

    - The storage device name of the disk that you want to partition.

    - When adding a data partition to the boot disk, a minimum value of 25000 MiB (Mebibytes) is recommended. The root file system is automatically resized to fill all available space up to the specified offset. If no value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of RHCOS might overwrite the beginning of the data partition.

    - The size of the data partition in mebibytes.

    - The `prjquota` mount option must be enabled for filesystems used for container storage.

      > [!NOTE]
      > When creating a separate `/var` partition, you cannot use different instance types for worker nodes, if the different instance types do not have the same device name.

5.  Create a manifest from the Butane config and save it to the `clusterconfig/openshift` directory. For example, run the following command:

    ``` terminal
    $ butane $HOME/clusterconfig/98-var-partition.bu -o $HOME/clusterconfig/openshift/98-var-partition.yaml
    ```

6.  Run `openshift-install` again to create Ignition configs from a set of files in the `manifest` and `openshift` subdirectories:

    ``` terminal
    $ openshift-install create ignition-configs --dir $HOME/clusterconfig
    ```

    ``` terminal
    $ ls $HOME/clusterconfig/
    auth  bootstrap.ign  master.ign  metadata.json  worker.ign
    ```

    You can now use the Ignition config files as input to the installation procedures to install Red Hat Enterprise Linux CoreOS (RHCOS) systems.

</div>

## Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on Microsoft Azure.

> [!IMPORTANT]
> Do not specify `windows`, `microsoft`, or other variants of these words in the `metadata.name` parameter of the `install-config.yaml` file. Specifying one of these words for the cluster name causes the installation program to generate an error message like the following example message:
>
> ``` terminal
> The resource name 'windows-xxxx-identity' or a part of the name is a trademarked or reserved word.
> ```
>
> Additionally, specifying `login` at the beginning of the name in the `metadata.name` parameter of the `install-config.yaml` file results in the generation of an error message. You can specify `login` in the middle or end of the name.

<div>

<div class="title">

Prerequisites

</div>

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

- You have an Azure subscription ID and tenant ID.

- If you are installing the cluster using a service principal, you have its application ID and password.

- If you are installing the cluster using a system-assigned managed identity, you have enabled it on the virtual machine that you will run the installation program from.

- If you are installing the cluster using a user-assigned managed identity, you have met these prerequisites:

  - You have its client ID.

  - You have assigned it to the virtual machine that you will run the installation program from.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Optional: If you have run the installation program on this computer before, and want to use an alternative service principal or managed identity, go to the `~/.azure/` directory and delete the `osServicePrincipal.json` configuration file.

    Deleting this file prevents the installation program from automatically reusing subscription and authentication values from a previous installation.

2.  Create the `install-config.yaml` file.

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

        2.  Select **azure** as the platform to target.

            If the installation program cannot locate the `osServicePrincipal.json` configuration file from a previous installation, you are prompted for Azure subscription and authentication values.

        3.  Enter the following Azure parameter values for your subscription:

            - **azure subscription id**: Enter the subscription ID to use for the cluster.

            - **azure tenant id**: Enter the tenant ID.

        4.  Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the **azure service principal client id**:

            - If you are using a service principal, enter its application ID.

            - If you are using a system-assigned managed identity, leave this value blank.

            - If you are using a user-assigned managed identity, specify its client ID.

        5.  Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the **azure service principal client secret**:

            - If you are using a service principal, enter its password.

            - If you are using a system-assigned managed identity, leave this value blank.

            - If you are using a user-assigned managed identity, leave this value blank.

        6.  Select the region to deploy the cluster to.

        7.  Select the base domain to deploy the cluster to. The base domain corresponds to the Azure DNS Zone that you created for your cluster.

        8.  Enter a descriptive name for your cluster.

            > [!IMPORTANT]
            > All Azure resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure restricts, see [Resolve reserved resource name errors](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-reserved-resource-name) in the Azure documentation.

3.  Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.

    > [!NOTE]
    > If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that the cluster’s control planes are schedulable. For more information, see "Installing a three-node cluster on Azure".

4.  Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

    > [!IMPORTANT]
    > The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

    If previously not detected, the installation program creates an `osServicePrincipal.json` configuration file and stores this file in the `~/.azure/` directory on your computer. This ensures that the installation program can load the profile when it is creating an OpenShift Container Platform cluster on the target platform.

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

## Exporting common variables for ARM templates

You must export a common set of variables that are used with the provided Azure Resource Manager (ARM) templates used to assist in completing a user-provided infrastructure install on Microsoft Azure.

> [!NOTE]
> Specific ARM templates can also require additional exported variables, which are detailed in their related procedures.

<div>

<div class="title">

Prerequisites

</div>

- Obtain the OpenShift Container Platform installation program and the pull secret for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Export common variables found in the `install-config.yaml` to be used by the provided ARM templates:

    ``` terminal
    $ export CLUSTER_NAME=<cluster_name>
    ```

    where:

    `<cluster_name>`
    The value of the `.metadata.name` attribute from the `install-config.yaml` file.

    ``` terminal
    $ export AZURE_REGION=<azure_region>
    ```

    where:

    `<azure_region>`
    The region to deploy the cluster into, for example `centralus`. This is the value of the `.platform.azure.region` attribute from the `install-config.yaml` file.

    ``` terminal
    $ export SSH_KEY=<ssh_key>
    ```

    where:

    `<ssh_key>`
    The SSH RSA public key file as a string. You must enclose the SSH key in quotes since it contains spaces. This is the value of the `.sshKey` attribute from the `install-config.yaml` file.

    ``` terminal
    $ export BASE_DOMAIN=<base_domain>
    ```

    where:

    `<base_domain>`
    The base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster. This is the value of the `.baseDomain` attribute from the `install-config.yaml` file.

    ``` terminal
    $ export BASE_DOMAIN_RESOURCE_GROUP=<base_domain_resource_group>
    ```

    where:

    `<base_domain_resource_group>`
    The resource group where the public DNS zone exists. This is the value of the `.platform.azure.baseDomainResourceGroupName` attribute from the `install-config.yaml` file.

    For example:

    ``` terminal
    $ export CLUSTER_NAME=test-cluster
    ```

    ``` terminal
    $ export AZURE_REGION=centralus
    ```

    ``` terminal
    $ export SSH_KEY="ssh-rsa xxx/xxx/xxx= user@email.com"
    ```

    ``` terminal
    $ export BASE_DOMAIN=example.com
    ```

    ``` terminal
    $ export BASE_DOMAIN_RESOURCE_GROUP=ocp-cluster
    ```

2.  Export the kubeadmin credentials:

    ``` terminal
    $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
    ```

    where:

    `<installation_directory>`
    Specify the path to the directory that you stored the installation files in.

</div>

## Creating the Kubernetes manifest and Ignition config files

To customize cluster definitions and manually start machines, generate the Kubernetes manifest and Ignition config files.

The installation configuration file transforms into the Kubernetes manifests. The manifests wrap into the Ignition configuration files, which are later used to configure the cluster machines.

<div class="important">

<div class="title">

</div>

- The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.

- It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You obtained the OpenShift Container Platform installation program.

- You created the `install-config.yaml` installation configuration file.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:

    ``` terminal
    $ ./openshift-install create manifests --dir <installation_directory>
    ```

    where

    `<installation_directory>`
    Specifies the installation directory that contains the `install-config.yaml` file you created.

2.  Remove the Kubernetes manifest files that define the control plane machines:

    ``` terminal
    $ rm -f <installation_directory>/openshift/99_openshift-cluster-api_master-machines-*.yaml
    ```

    By removing these files, you prevent the cluster from automatically generating control plane machines.

3.  Remove the Kubernetes manifest files that define the control plane machine set:

    ``` terminal
    $ rm -f <installation_directory>/openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
    ```

4.  Remove the Kubernetes manifest files that define the worker machines:

    ``` terminal
    $ rm -f <installation_directory>/openshift/99_openshift-cluster-api_worker-machineset-*.yaml
    ```

    > [!IMPORTANT]
    > If you disabled the `MachineAPI` capability when installing a cluster on user-provisioned infrastructure, you must remove the Kubernetes manifest files that define the worker machines. Otherwise, your cluster fails to install.

    Because you create and manage the worker machines yourself, you do not need to initialize these machines.

    > [!WARNING]
    > If you are installing a three-node cluster, skip the following step to allow the control plane nodes to be schedulable.

    > [!IMPORTANT]
    > When you configure control plane nodes from the default unschedulable to schedulable, additional subscriptions are required. This is because control plane nodes then become compute nodes.

5.  Check that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:

    1.  Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.

    2.  Locate the `mastersSchedulable` parameter and ensure that it is set to `false`.

    3.  Save and exit the file.

6.  Optional: If you do not want [the Ingress Operator](https://github.com/openshift/cluster-ingress-operator) to create DNS records on your behalf, remove the `privateZone` and `publicZone` sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: DNS
    metadata:
      creationTimestamp: null
      name: cluster
    spec:
      baseDomain: example.openshift.com
      privateZone:
        id: mycluster-100419-private-zone
      publicZone:
        id: example.openshift.com
    status: {}
    ```

    `spec.privateZone`: Remove this section completely.

    If you do so, you must add ingress DNS records manually in a later step.

7.  When configuring Azure on user-provisioned infrastructure, you must export some common variables defined in the manifest files to use later in the Azure Resource Manager (ARM) templates:

    1.  Export the infrastructure ID by using the following command:

        ``` terminal
        $ export INFRA_ID=<infra_id>
        ```

        where:

        `<infra_id>`
        Specifies that the OpenShift Container Platform cluster has been assigned an identifier (`INFRA_ID`) in the form of `<cluster_name>-<random_string>`. This identifier is used as the base name for most resources created using the provided ARM templates. This is the value of the `.status.infrastructureName` attribute from the `manifests/cluster-infrastructure-02-config.yml` file.

    2.  Export the resource group by using the following command:

        ``` terminal
        $ export RESOURCE_GROUP=<resource_group>
        ```

        where:

        `<resource_group>`
        All resources created in this Azure deployment exists as part of a [resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview#resource-groups). The resource group name is also based on the `INFRA_ID`, in the form of `<cluster_name>-<random_string>-rg`. This is the value of the `.status.platformStatus.azure.resourceGroupName` attribute from the `manifests/cluster-infrastructure-02-config.yml` file.

8.  To create the Ignition configuration files, run the following command from the directory that contains the installation program:

    ``` terminal
    $ ./openshift-install create ignition-configs --dir <installation_directory>
    ```

    where:

    `<installation_directory>`
    Specifies the same installation directory.

    Ignition config files are created for the bootstrap, control plane, and compute nodes in the installation directory. The `kubeadmin-password` and `kubeconfig` files are created in the `./<installation_directory>/auth` directory:

        .
        ├── auth
        │   ├── kubeadmin-password
        │   └── kubeconfig
        ├── bootstrap.ign
        ├── master.ign
        ├── metadata.json
        └── worker.ign

</div>

# Creating the Azure resource group

You must create a Microsoft Azure [resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview#resource-groups) and an identity for that resource group. These are both used during the installation of your OpenShift Container Platform cluster on Azure.

<div>

<div class="title">

Procedure

</div>

1.  Create the resource group in a supported Azure region:

    ``` terminal
    $ az group create --name ${RESOURCE_GROUP} --location ${AZURE_REGION}
    ```

2.  Create an Azure identity for the resource group:

    ``` terminal
    $ az identity create -g ${RESOURCE_GROUP} -n ${INFRA_ID}-identity
    ```

    This is used to grant the required access to Operators in your cluster. For example, this allows the Ingress Operator to create a public IP and its load balancer. You must assign the Azure identity to a role.

3.  Grant the Contributor role to the Azure identity:

    1.  Export the following variables required by the Azure role assignment:

        ``` terminal
        $ export PRINCIPAL_ID=`az identity show -g ${RESOURCE_GROUP} -n ${INFRA_ID}-identity --query principalId --out tsv`
        ```

        ``` terminal
        $ export RESOURCE_GROUP_ID=`az group show -g ${RESOURCE_GROUP} --query id --out tsv`
        ```

    2.  Assign the Contributor role to the identity:

        ``` terminal
        $ az role assignment create --assignee "${PRINCIPAL_ID}" --role 'Contributor' --scope "${RESOURCE_GROUP_ID}"
        ```

        > [!NOTE]
        > If you want to assign a custom role with all the required permissions to the identity, run the following command:
        >
        > ``` terminal
        > $ az role assignment create --assignee "${PRINCIPAL_ID}" --role <custom_role> \
        > --scope "${RESOURCE_GROUP_ID}"
        > ```
        >
        > - Specifies the custom role name.

</div>

# Uploading the RHCOS cluster image and bootstrap Ignition config file

The Azure client does not support deployments based on files existing locally. You must copy and store the RHCOS virtual hard disk (VHD) cluster image and bootstrap Ignition config file in a storage container so they are accessible during deployment.

<div>

<div class="title">

Prerequisites

</div>

- Generate the Ignition config files for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an Azure storage account to store the VHD cluster image:

    ``` terminal
    $ az storage account create -g ${RESOURCE_GROUP} --location ${AZURE_REGION} --name ${CLUSTER_NAME}sa --kind Storage --sku Standard_LRS
    ```

    > [!WARNING]
    > The Azure storage account name must be between 3 and 24 characters in length and use numbers and lower-case letters only. If your `CLUSTER_NAME` variable does not follow these restrictions, you must manually define the Azure storage account name. For more information on Azure storage account name restrictions, see [Resolve errors for storage account names](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/error-storage-account-name) in the Azure documentation.

2.  Export the storage account key as an environment variable:

    ``` terminal
    $ export ACCOUNT_KEY=`az storage account keys list -g ${RESOURCE_GROUP} --account-name ${CLUSTER_NAME}sa --query "[0].value" -o tsv`
    ```

3.  Export the URL of the RHCOS VHD to an environment variable:

    ``` terminal
    $ export VHD_URL=`openshift-install coreos print-stream-json | jq -r '.architectures.<architecture>."rhel-coreos-extensions"."azure-disk".url'`
    ```

    where:

    `<architecture>`
    Specifies the architecture, valid values include `x86_64` or `aarch64`.

    > [!IMPORTANT]
    > The RHCOS images might not change with every release of OpenShift Container Platform. You must specify an image with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Use the image version that matches your OpenShift Container Platform version if it is available.

4.  Create the storage container for the VHD:

    ``` terminal
    $ az storage container create --name vhd --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY}
    ```

5.  Copy the local VHD to a blob:

    ``` terminal
    $ az storage blob copy start --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY} --destination-blob "rhcos.vhd" --destination-container vhd --source-uri "${VHD_URL}"
    ```

6.  Create a blob storage container and upload the generated `bootstrap.ign` file:

    ``` terminal
    $ az storage container create --name files --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY}
    ```

    ``` terminal
    $ az storage blob upload --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY} -c "files" -f "<installation_directory>/bootstrap.ign" -n "bootstrap.ign"
    ```

</div>

# Example for creating DNS zones

DNS records are required for clusters that use user-provisioned infrastructure. You should choose the DNS strategy that fits your scenario.

For this example, [Azure’s DNS solution](https://docs.microsoft.com/en-us/azure/dns/dns-overview) is used, so you will create a new public DNS zone for external (internet) visibility and a private DNS zone for internal cluster resolution.

> [!NOTE]
> The public DNS zone is not required to exist in the same resource group as the cluster deployment and might already exist in your organization for the desired base domain. If that is the case, you can skip creating the public DNS zone; be sure the installation config you generated earlier reflects that scenario.

<div>

<div class="title">

Procedure

</div>

1.  Create the new public DNS zone in the resource group exported in the `BASE_DOMAIN_RESOURCE_GROUP` environment variable:

    ``` terminal
    $ az network dns zone create -g ${BASE_DOMAIN_RESOURCE_GROUP} -n ${CLUSTER_NAME}.${BASE_DOMAIN}
    ```

    You can skip this step if you are using a public DNS zone that already exists.

2.  Create the private DNS zone in the same resource group as the rest of this deployment:

    ``` terminal
    $ az network private-dns zone create -g ${RESOURCE_GROUP} -n ${CLUSTER_NAME}.${BASE_DOMAIN}
    ```

</div>

You can learn more about [configuring a public DNS zone in Azure](#installation-azure-network-config_installing-azure-user-infra) by visiting that section.

# Creating a VNet in Azure

You must create a virtual network (VNet) in Microsoft Azure for your OpenShift Container Platform cluster to use. You can customize the VNet to meet your requirements. One way to create the VNet is to modify the provided Azure Resource Manager (ARM) template.

> [!NOTE]
> If you do not use the provided ARM template to create your Azure infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

<div>

<div class="title">

Procedure

</div>

1.  Copy the template from the **ARM template for the VNet** section of this topic and save it as `01_vnet.json` in your cluster’s installation directory. This template describes the VNet that your cluster requires.

2.  Create the deployment by using the `az` CLI:

    ``` terminal
    $ az deployment group create -g ${RESOURCE_GROUP} \
      --template-file "<installation_directory>/01_vnet.json" \
      --parameters baseName="${INFRA_ID}"
    ```

    - The base name to be used in resource names; this is usually the cluster’s infrastructure ID.

3.  Link the VNet template to the private DNS zone:

    ``` terminal
    $ az network private-dns link vnet create -g ${RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n ${INFRA_ID}-network-link -v "${INFRA_ID}-vnet" -e false
    ```

</div>

## ARM template for the VNet

You can use the following Azure Resource Manager (ARM) template to deploy the VNet that you need for your OpenShift Container Platform cluster:

<div class="example">

<div class="title">

`01_vnet.json` ARM template

</div>

``` json
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azure/01_vnet.json[role=include]
```

</div>

# Deploying the RHCOS cluster image for the Azure infrastructure

You must use a valid Red Hat Enterprise Linux CoreOS (RHCOS) image for Microsoft Azure for your OpenShift Container Platform nodes.

<div>

<div class="title">

Prerequisites

</div>

- Store the RHCOS virtual hard disk (VHD) cluster image in an Azure storage container.

- Store the bootstrap Ignition config file in an Azure storage container.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Copy the template from the **ARM template for image storage** section of this topic and save it as `02_storage.json` in your cluster’s installation directory. This template describes the image storage that your cluster requires.

2.  Export the RHCOS VHD blob URL as a variable:

    ``` terminal
    $ export VHD_BLOB_URL=`az storage blob url --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY} -c vhd -n "rhcos.vhd" -o tsv`
    ```

3.  Deploy the cluster image:

    ``` terminal
    $ az deployment group create -g ${RESOURCE_GROUP} \
      --template-file "<installation_directory>/02_storage.json" \
      --parameters vhdBlobURL="${VHD_BLOB_URL}" \
      --parameters baseName="${INFRA_ID}" \
      --parameters storageAccount="${CLUSTER_NAME}sa" \
      --parameters architecture="<architecture>"
    ```

    - The blob URL of the RHCOS VHD to be used to create master and worker machines.

    - The base name to be used in resource names; this is usually the cluster’s infrastructure ID.

    - The name of your Azure storage account.

    - Specify the system architecture. Valid values are `x64` (default) or `Arm64`.

</div>

## ARM template for image storage

You can use the following Azure Resource Manager (ARM) template to deploy the stored Red Hat Enterprise Linux CoreOS (RHCOS) image that you need for your OpenShift Container Platform cluster:

<div class="example">

<div class="title">

`02_storage.json` ARM template

</div>

``` json
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azure/02_storage.json[role=include]
```

</div>

# Networking requirements for user-provisioned infrastructure

You must configure networking for all the Red Hat Enterprise Linux CoreOS (RHCOS) machines in `initramfs` during boot, so that they can fetch their Ignition config files.

## Network connectivity requirements

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster.

This section provides details about the ports that are required.

> [!IMPORTANT]
> In connected OpenShift Container Platform environments, all nodes are required to have internet access to pull images for platform containers and provide telemetry data to Red Hat.

| Protocol | Port | Description |
|----|----|----|
| ICMP | N/A | Network reachability tests |
| TCP | `1936` | Metrics |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101` and the Cluster Version Operator on port `9099`. |  |
| `10250`-`10259` | The default ports that Kubernetes reserves |  |
| `22623` | The port handles traffic from the Machine Config Server and directs the traffic to the control plane machines. |  |
| UDP | `6081` | Geneve |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101`. |  |
| `500` | IPsec IKE packets |  |
| `4500` | IPsec NAT-T packets |  |
| `123` | Network Time Protocol (NTP) on UDP port `123`. If an external NTP time server is configured, you must open UDP port `123`. |  |
| TCP/UDP | `30000`-`32767` |  |
| Kubernetes node port | ESP | N/A |

Ports used for all-machine to all-machine communications

| Protocol | Port   | Description    |
|----------|--------|----------------|
| TCP      | `6443` | Kubernetes API |

Ports used for all-machine to control plane communications

| Protocol | Port          | Description                |
|----------|---------------|----------------------------|
| TCP      | `2379`-`2380` | etcd server and peer ports |

Ports used for control plane machine to control plane machine communications

# Creating networking and load balancing components in Azure

You must configure networking and load balancing in Microsoft Azure for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Azure Resource Manager (ARM) template.

> [!NOTE]
> If you do not use the provided ARM template to create your Azure infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

<div>

<div class="title">

Prerequisites

</div>

- Create and configure a VNet and associated subnets in Azure.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Copy the template from the **ARM template for the network and load balancers** section of this topic and save it as `03_infra.json` in your cluster’s installation directory. This template describes the networking and load balancing objects that your cluster requires.

2.  Create the deployment by using the `az` CLI:

    ``` terminal
    $ az deployment group create -g ${RESOURCE_GROUP} \
      --template-file "<installation_directory>/03_infra.json" \
      --parameters privateDNSZoneName="${CLUSTER_NAME}.${BASE_DOMAIN}" \
      --parameters baseName="${INFRA_ID}"
    ```

    - The name of the private DNS zone.

    - The base name to be used in resource names; this is usually the cluster’s infrastructure ID.

3.  Create an `api` DNS record in the public zone for the API public load balancer. The `${BASE_DOMAIN_RESOURCE_GROUP}` variable must point to the resource group where the public DNS zone exists.

    1.  Export the following variable:

        ``` terminal
        $ export PUBLIC_IP=`az network public-ip list -g ${RESOURCE_GROUP} --query "[?name=='${INFRA_ID}-master-pip'] | [0].ipAddress" -o tsv`
        ```

    2.  Create the `api` DNS record in a new public zone:

        ``` terminal
        $ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n api -a ${PUBLIC_IP} --ttl 60
        ```

        If you are adding the cluster to an existing public zone, you can create the `api` DNS record in it instead:

        ``` terminal
        $ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${BASE_DOMAIN} -n api.${CLUSTER_NAME} -a ${PUBLIC_IP} --ttl 60
        ```

</div>

## ARM template for the network and load balancers

You can use the following Azure Resource Manager (ARM) template to deploy the networking objects and load balancers that you need for your OpenShift Container Platform cluster:

<div class="example">

<div class="title">

`03_infra.json` ARM template

</div>

``` json
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azure/03_infra.json[role=include]
```

</div>

# Creating the bootstrap machine in Azure

You must create the bootstrap machine in Microsoft Azure to use during OpenShift Container Platform cluster initialization. One way to create this machine is to modify the provided Azure Resource Manager (ARM) template.

> [!NOTE]
> If you do not use the provided ARM template to create your bootstrap machine, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

<div>

<div class="title">

Prerequisites

</div>

- Create and configure networking and load balancers in Azure.

- Create the Azure identity and grant the appropriate roles.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Copy the template from the **ARM template for the bootstrap machine** section of this topic and save it as `04_bootstrap.json` in your cluster’s installation directory. This template describes the bootstrap machine that your cluster requires.

2.  Export the bootstrap URL variable:

    ``` terminal
    $ bootstrap_url_expiry=`date -u -d "10 hours" '+%Y-%m-%dT%H:%MZ'`
    ```

    ``` terminal
    $ export BOOTSTRAP_URL=`az storage blob generate-sas -c 'files' -n 'bootstrap.ign' --https-only --full-uri --permissions r --expiry $bootstrap_url_expiry --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY} -o tsv`
    ```

3.  Export the bootstrap ignition variable:

    ``` terminal
    $ export BOOTSTRAP_IGNITION=`jq -rcnM --arg v "3.2.0" --arg url ${BOOTSTRAP_URL} '{ignition:{version:$v,config:{replace:{source:$url}}}}' | base64 | tr -d '\n'`
    ```

4.  Create the deployment by using the `az` CLI:

    ``` terminal
    $ az deployment group create -g ${RESOURCE_GROUP} \
      --template-file "<installation_directory>/04_bootstrap.json" \
      --parameters bootstrapIgnition="${BOOTSTRAP_IGNITION}" \
      --parameters baseName="${INFRA_ID}" \
      --parameter bootstrapVMSize="Standard_D4s_v3"
    ```

    - The bootstrap Ignition content for the bootstrap cluster.

    - The base name to be used in resource names; this is usually the cluster’s infrastructure ID.

    - Optional: Specify the size of the bootstrap VM. Use a VM size compatible with your specified architecture. If this value is not defined, the default value from the template is set.

</div>

## ARM template for the bootstrap machine

You can use the following Azure Resource Manager (ARM) template to deploy the bootstrap machine that you need for your OpenShift Container Platform cluster:

<div class="example">

<div class="title">

`04_bootstrap.json` ARM template

</div>

``` json
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azure/04_bootstrap.json[role=include]
```

</div>

# Creating the control plane machines in Azure

You must create the control plane machines in Microsoft Azure for your cluster to use. One way to create these machines is to modify the provided Azure Resource Manager (ARM) template.

> [!NOTE]
> By default, Microsoft Azure places control plane machines and compute machines in a pre-set availability zone. You can manually set an availability zone for a compute node or control plane node. To do this, modify a vendor’s Azure Resource Manager (ARM) template by specifying each of your availability zones in the `zones` parameter of the virtual machine resource.

If you do not use the provided ARM template to create your control plane machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, consider contacting Red Hat support with your installation logs.

<div>

<div class="title">

Prerequisites

</div>

- Create the bootstrap machine.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Copy the template from the **ARM template for control plane machines** section of this topic and save it as `05_masters.json` in your cluster’s installation directory. This template describes the control plane machines that your cluster requires.

2.  Export the following variable needed by the control plane machine deployment:

    ``` terminal
    $ export MASTER_IGNITION=`cat <installation_directory>/master.ign | base64 | tr -d '\n'`
    ```

3.  Create the deployment by using the `az` CLI:

    ``` terminal
    $ az deployment group create -g ${RESOURCE_GROUP} \
      --template-file "<installation_directory>/05_masters.json" \
      --parameters masterIgnition="${MASTER_IGNITION}" \
      --parameters baseName="${INFRA_ID}" \
      --parameters masterVMSize="Standard_D8s_v3"
    ```

    - The Ignition content for the control plane nodes.

    - The base name to be used in resource names; this is usually the cluster’s infrastructure ID.

    - Optional: Specify the size of the Control Plane VM. Use a VM size compatible with your specified architecture. If this value is not defined, the default value from the template is set.

</div>

## ARM template for control plane machines

You can use the following Azure Resource Manager (ARM) template to deploy the control plane machines that you need for your OpenShift Container Platform cluster:

<div class="example">

<div class="title">

`05_masters.json` ARM template

</div>

``` json
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azure/05_masters.json[role=include]
```

</div>

# Wait for bootstrap completion and remove bootstrap resources in Azure

After you create all of the required infrastructure in Microsoft Azure, wait for the bootstrap process to complete on the machines that you provisioned by using the Ignition config files that you generated with the installation program.

<div>

<div class="title">

Prerequisites

</div>

- Create the control plane machines.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Change to the directory that contains the installation program and run the following command:

    ``` terminal
    $ ./openshift-install wait-for bootstrap-complete --dir <installation_directory> \
        --log-level info
    ```

    - For `<installation_directory>`, specify the path to the directory that you stored the installation files in.

    - To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

      If the command exits without a `FATAL` warning, your production control plane has initialized.

2.  Delete the bootstrap resources:

    ``` terminal
    $ az network nsg rule delete -g ${RESOURCE_GROUP} --nsg-name ${INFRA_ID}-nsg --name bootstrap_ssh_in
    ```

    ``` terminal
    $ az vm stop -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap
    ```

    ``` terminal
    $ az vm deallocate -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap
    ```

    ``` terminal
    $ az vm delete -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap --yes
    ```

    ``` terminal
    $ az disk delete -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap_OSDisk --no-wait --yes
    ```

    ``` terminal
    $ az network nic delete -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap-nic --no-wait
    ```

    ``` terminal
    $ az storage blob delete --account-key ${ACCOUNT_KEY} --account-name ${CLUSTER_NAME}sa --container-name files --name bootstrap.ign
    ```

    ``` terminal
    $ az network public-ip delete -g ${RESOURCE_GROUP} --name ${INFRA_ID}-bootstrap-ssh-pip
    ```

    > [!NOTE]
    > If you do not delete the bootstrap server, installation may not succeed due to API traffic being routed to the bootstrap server.

</div>

# Creating additional worker machines in Azure

You can create worker machines in Microsoft Azure for your cluster to use by launching individual instances discretely or by automated processes outside the cluster, such as auto scaling groups. You can also take advantage of the built-in cluster scaling mechanisms and the machine API in OpenShift Container Platform.

> [!NOTE]
> If you are installing a three-node cluster, skip this step. A three-node cluster consists of three control plane machines, which also act as compute machines.

In this example, you manually launch one instance by using the Azure Resource Manager (ARM) template. Additional instances can be launched by including additional resources of type `06_workers.json` in the file.

> [!NOTE]
> By default, Microsoft Azure places control plane machines and compute machines in a pre-set availability zone. You can manually set an availability zone for a compute node or control plane node. To do this, modify a vendor’s ARM template by specifying each of your availability zones in the `zones` parameter of the virtual machine resource.

If you do not use the provided ARM template to create your control plane machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, consider contacting Red Hat support with your installation logs.

<div>

<div class="title">

Procedure

</div>

1.  Copy the template from the **ARM template for worker machines** section of this topic and save it as `06_workers.json` in your cluster’s installation directory. This template describes the worker machines that your cluster requires.

2.  Export the following variable needed by the worker machine deployment:

    ``` terminal
    $ export WORKER_IGNITION=`cat <installation_directory>/worker.ign | base64 | tr -d '\n'`
    ```

3.  Create the deployment by using the `az` CLI:

    ``` terminal
    $ az deployment group create -g ${RESOURCE_GROUP} \
      --template-file "<installation_directory>/06_workers.json" \
      --parameters workerIgnition="${WORKER_IGNITION}" \
      --parameters baseName="${INFRA_ID}" \
      --parameters nodeVMSize="Standard_D4s_v3"
    ```

    - The Ignition content for the worker nodes.

    - The base name to be used in resource names; this is usually the cluster’s infrastructure ID.

    - Optional: Specify the size of the compute node VM. Use a VM size compatible with your specified architecture. If this value is not defined, the default value from the template is set.

</div>

## ARM template for worker machines

You can use the following Azure Resource Manager (ARM) template to deploy the worker machines that you need for your OpenShift Container Platform cluster:

<div class="example">

<div class="title">

`06_workers.json` ARM template

</div>

``` json
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azure/06_workers.json[role=include]
```

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

# Approving the certificate signing requests for your machines

When you add machines to a cluster, two pending certificate signing requests (CSRs) are generated for each machine that you added. You must confirm that these CSRs are approved or, if necessary, approve them yourself. The client requests must be approved first, followed by the server requests.

<div>

<div class="title">

Prerequisites

</div>

- You added machines to your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Confirm that the cluster recognizes the machines:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME      STATUS    ROLES   AGE  VERSION
    master-0  Ready     master  63m  v1.33.4
    master-1  Ready     master  63m  v1.33.4
    master-2  Ready     master  64m  v1.33.4
    ```

    </div>

    The output lists all of the machines that you created.

    > [!NOTE]
    > The preceding output might not include the compute nodes until some CSRs are approved.

2.  Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster:

    ``` terminal
    $ oc get csr
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        AGE     REQUESTOR                                                                   CONDITION
    csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
    csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
    ...
    ```

    </div>

    In this example, two machines are joining the cluster. You might see more approved CSRs in the list.

3.  If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines:

    > [!NOTE]
    > You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates will rotate, and more than two certificates will be present for each node. You must approve all of these certificates. After the client CSR is approved, the Kubelet creates a secondary CSR for the serving certificate, which requires manual approval. The subsequent serving certificate renewal requests are then automatically approved by the `machine-approver` if the Kubelet requests a new certificate with identical parameters.

    > [!NOTE]
    > For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If a request is not approved, then the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because a serving certificate is required when the API server connects to the kubelet. Any operation that contacts the Kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the CSR was submitted by the `node-bootstrapper` service account in the `system:node` or `system:admin` groups, and confirm the identity of the node.

    - To approve them individually, run the following command for each valid CSR:

      ``` terminal
      $ oc adm certificate approve <csr_name>
      ```

      where:

      `<csr_name>`
      Specifies the name of a CSR from the list of current CSRs.

    - To approve all pending CSRs, run the following command:

      ``` terminal
      $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
      ```

      > [!NOTE]
      > Some Operators might not become available until some CSRs are approved.

4.  Now that your client requests are approved, you must review the server requests for each machine that you added to the cluster:

    ``` terminal
    $ oc get csr
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        AGE     REQUESTOR                                                                   CONDITION
    csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
    csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
    ...
    ```

    </div>

5.  If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines:

    - To approve them individually, run the following command for each valid CSR:

      ``` terminal
      $ oc adm certificate approve <csr_name>
      ```

      where:

      `<csr_name>`
      Specifies the name of a CSR from the list of current CSRs.

    - To approve all pending CSRs, run the following command:

      ``` terminal
      $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
      ```

6.  After all client and server CSRs have been approved, the machines have the `Ready` status. Verify this by running the following command:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME      STATUS    ROLES   AGE  VERSION
    master-0  Ready     master  73m  v1.33.4
    master-1  Ready     master  73m  v1.33.4
    master-2  Ready     master  74m  v1.33.4
    worker-0  Ready     worker  11m  v1.33.4
    worker-1  Ready     worker  11m  v1.33.4
    ```

    </div>

    > [!NOTE]
    > You might need to wait a few minutes after approval of the server CSRs for the machines to transition to the `Ready` status.

</div>

# Adding the Ingress DNS records

If you removed the DNS Zone configuration when creating Kubernetes manifests and generating Ignition configs, you must manually create DNS records that point at the Ingress load balancer. You can create either a wildcard `*.apps.{baseDomain}.` or specific records. You can use A, CNAME, and other records per your requirements.

<div>

<div class="title">

Prerequisites

</div>

- You deployed an OpenShift Container Platform cluster on Microsoft Azure by using infrastructure that you provisioned.

- Install the OpenShift CLI (`oc`).

- Install or update the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-yum?view=azure-cli-latest).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Confirm the Ingress router has created a load balancer and populated the `EXTERNAL-IP` field:

    ``` terminal
    $ oc -n openshift-ingress get service router-default
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME             TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
    router-default   LoadBalancer   172.30.20.10   35.130.120.110   80:32288/TCP,443:31215/TCP   20
    ```

    </div>

2.  Export the Ingress router IP as a variable:

    ``` terminal
    $ export PUBLIC_IP_ROUTER=`oc -n openshift-ingress get service router-default --no-headers | awk '{print $4}'`
    ```

3.  Add a `*.apps` record to the public DNS zone.

    1.  If you are adding this cluster to a new public zone, run:

        ``` terminal
        $ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n *.apps -a ${PUBLIC_IP_ROUTER} --ttl 300
        ```

    2.  If you are adding this cluster to an already existing public zone, run:

        ``` terminal
        $ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${BASE_DOMAIN} -n *.apps.${CLUSTER_NAME} -a ${PUBLIC_IP_ROUTER} --ttl 300
        ```

4.  Add a `*.apps` record to the private DNS zone:

    1.  Create a `*.apps` record by using the following command:

        ``` terminal
        $ az network private-dns record-set a create -g ${RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n *.apps --ttl 300
        ```

    2.  Add the `*.apps` record to the private DNS zone by using the following command:

        ``` terminal
        $ az network private-dns record-set a add-record -g ${RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n *.apps -a ${PUBLIC_IP_ROUTER}
        ```

</div>

If you prefer to add explicit domains instead of using a wildcard, you can create entries for each of the cluster’s current routes:

``` terminal
$ oc get --all-namespaces -o jsonpath='{range .items[*]}{range .status.ingress[*]}{"\n"}{end}{end}' routes
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
oauth-openshift.apps.cluster.basedomain.com
console-openshift-console.apps.cluster.basedomain.com
downloads-openshift-console.apps.cluster.basedomain.com
alertmanager-main-openshift-monitoring.apps.cluster.basedomain.com
prometheus-k8s-openshift-monitoring.apps.cluster.basedomain.com
```

</div>

# Completing an Azure installation on user-provisioned infrastructure

After you start the OpenShift Container Platform installation on Microsoft Azure user-provisioned infrastructure, you can monitor the cluster events until the cluster is ready.

<div>

<div class="title">

Prerequisites

</div>

- Deploy the bootstrap machine for an OpenShift Container Platform cluster on user-provisioned Azure infrastructure.

- Install the `oc` CLI and log in.

</div>

<div>

<div class="title">

Procedure

</div>

- Complete the cluster installation:

  ``` terminal
  $ ./openshift-install --dir <installation_directory> wait-for install-complete
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  INFO Waiting up to 30m0s for the cluster to initialize...
  ```

  </div>

  - For `<installation_directory>`, specify the path to the directory that you stored the installation files in.

    <div class="important">

    <div class="title">

    </div>

    - The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.

    - It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

    </div>

</div>

# Telemetry access for OpenShift Container Platform

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

<div>

<div class="title">

Additional resources

</div>

- See [About remote health monitoring](../../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring) for more information about the Telemetry service

</div>
