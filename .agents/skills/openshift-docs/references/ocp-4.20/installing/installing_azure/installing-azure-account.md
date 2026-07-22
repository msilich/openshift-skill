<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you can install OpenShift Container Platform on Microsoft Azure, you must configure an Azure account with the correct identity and permissions before you start the installation.

> [!IMPORTANT]
> All Azure resources that are available through public endpoints are subject to resource name restrictions. For a list of terms that Azure restricts for resource names, see "Resolve errors for reserved resource names".

# Azure account limits

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
<td style="text-align: left;"><p>44</p></td>
<td style="text-align: left;"><p>20 per region</p></td>
<td style="text-align: left;"><p>A default cluster requires 44 vCPUs, so you must increase the account limit.</p>
<p>By default, each cluster creates the following instances:</p>
<ul>
<li><p>One bootstrap machine, which is removed after installation</p></li>
<li><p>Three control plane machines</p></li>
<li><p>Three compute machines</p></li>
</ul>
<p>Because the bootstrap and control plane machines use <code>Standard_D8s_v3</code> virtual machines, which use 8 vCPUs, and the compute machines use <code>Standard_D4s_v3</code> virtual machines, which use 4 vCPUs, a default cluster requires 44 vCPUs. The bootstrap node VM, which uses 8 vCPUs, is used only during installation.</p>
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

- [Optimizing storage](../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

- [Azure subscription and service limits, quotas, and constraints (Azure documentation)](https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits)

</div>

# Configuring a public DNS zone in Azure

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

# Recording the subscription and tenant IDs

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

# Supported identities to access Azure resources

An OpenShift Container Platform cluster requires an Azure identity to create and manage Azure resources. You need a service principal, a system-assigned managed identity, or a user-assigned managed identity to complete the installation.

- A service principal

- A system-assigned managed identity

- A user-assigned managed identity

For more information on Azure identities, see "Managed identity types".

<div>

<div class="title">

Additional resources

</div>

- [Managed identity types (Azure documentation)](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview#managed-identity-types)

</div>

## Required Azure roles

Before you create the identity for an OpenShift Container Platform cluster on Azure, verify that your environment meets the role and permission requirements for the identity type you plan to use.

The following requirements must be met:

- The Azure account that you use to create the identity is assigned the `User Access Administrator` and `Contributor` roles. These roles are required when:

  - Creating a service principal or user-assigned managed identity.

  - Enabling a system-assigned managed identity on a virtual machine.

- If you are going to use a service principal to complete the installation, verify that the Azure account that you use to create the identity is assigned the `microsoft.directory/servicePrincipals/createAsOwner` permission in Microsoft Entra ID.

<div>

<div class="title">

Additional resources

</div>

- [Assign Azure roles using the Azure portal (Azure documentation)](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)

</div>

### Required Azure permissions for installer-provisioned infrastructure

The installation program requires access to a Microsoft Azure service principal or managed identity with the necessary permissions to deploy the cluster and to maintain its daily operation. These permissions must be granted to the Azure subscription that is associated with the identity.

The following options are available to you:

- You can assign the identity the `Contributor` and `User Access Administrator` roles, which grant all of the required permissions.

  If you set `identity.type` to `None` in the `install-config.yaml` file, you do not need to assign the `User Access Administrator` role to the service principal.

  For more information about assigning roles, see the Azure documentation for [managing access to Azure resources using the Azure portal](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).

- If the security policies of your organization require a more restrictive set of permissions, you can create a [custom role](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles) with the necessary permissions.

The following permissions are required for creating an OpenShift Container Platform cluster on Microsoft Azure.

Required permissions for creating authorization resources
- `Microsoft.Authorization/policies/audit/action`

- `Microsoft.Authorization/policies/auditIfNotExists/action`

- `Microsoft.Authorization/roleAssignments/read`

- `Microsoft.Authorization/roleAssignments/write`

> [!IMPORTANT]
> The following permissions are not required if you set `identity.type` to `None` in the `install-config.yaml` file:
>
> - `Microsoft.Authorization/roleAssignments/read`
>
> - `Microsoft.Authorization/roleAssignments/write`
>
> - `Microsoft.ManagedIdentity/userAssignedIdentities/assign/action`
>
> - `Microsoft.ManagedIdentity/userAssignedIdentities/read`
>
> - `Microsoft.ManagedIdentity/userAssignedIdentities/write`
>
> - `Microsoft.Authorization/roleAssignments/delete`
>
> The following permissions are not required if you set `identity.type` to `UserAssigned` in the `install-config.yaml` file and provide a user-assigned identity:
>
> - `Microsoft.Authorization/roleAssignments/read`
>
> - `Microsoft.Authorization/roleAssignments/write`
>
> - `Microsoft.ManagedIdentity/userAssignedIdentities/write`
>
> - `Microsoft.Authorization/roleAssignments/delete`

Required permissions for creating compute resources
- `Microsoft.Compute/availabilitySets/read`

- `Microsoft.Compute/availabilitySets/write`

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

Required permissions for creating identity management resources
- `Microsoft.ManagedIdentity/userAssignedIdentities/assign/action`

- `Microsoft.ManagedIdentity/userAssignedIdentities/read`

- `Microsoft.ManagedIdentity/userAssignedIdentities/write`

Required permissions for creating network resources
- `Microsoft.Network/dnsZones/A/write`

- `Microsoft.Network/dnsZones/CNAME/write`

- `Microsoft.Network/dnszones/CNAME/read`

- `Microsoft.Network/dnszones/read`

- `Microsoft.Network/loadBalancers/backendAddressPools/join/action`

- `Microsoft.Network/loadBalancers/backendAddressPools/read`

- `Microsoft.Network/loadBalancers/backendAddressPools/write`

- `Microsoft.Network/loadBalancers/read`

- `Microsoft.Network/loadBalancers/write`

- `Microsoft.Network/loadBalancers/inboundNatRules/read`

- `Microsoft.Network/loadBalancers/inboundNatRules/write`

- `Microsoft.Network/loadBalancers/inboundNatRules/join/action`

- `Microsoft.Network/loadBalancers/inboundNatRules/delete`

- `Microsoft.Network/routeTables/read`

- `Microsoft.Network/routeTables/write`

- `Microsoft.Network/routeTables/join/action`

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

- `Microsoft.Network/virtualNetworks/checkIpAddressAvailability/read`

- `Microsoft.Network/virtualNetworks/join/action`

- `Microsoft.Network/virtualNetworks/read`

- `Microsoft.Network/virtualNetworks/subnets/join/action`

- `Microsoft.Network/virtualNetworks/subnets/read`

- `Microsoft.Network/virtualNetworks/subnets/write`

- `Microsoft.Network/virtualNetworks/write`

> [!NOTE]
> The following permissions are not required to create the private OpenShift Container Platform cluster on Azure.
>
> - `Microsoft.Network/dnsZones/A/write`
>
> - `Microsoft.Network/dnsZones/CNAME/write`
>
> - `Microsoft.Network/dnszones/CNAME/read`
>
> - `Microsoft.Network/dnszones/read`

Required permissions for checking the health of resources
- `Microsoft.Resourcehealth/healthevent/Activated/action`

- `Microsoft.Resourcehealth/healthevent/InProgress/action`

- `Microsoft.Resourcehealth/healthevent/Pending/action`

- `Microsoft.Resourcehealth/healthevent/Resolved/action`

- `Microsoft.Resourcehealth/healthevent/Updated/action`

Required permissions for creating a resource group
- `Microsoft.Resources/subscriptions/resourceGroups/read`

- `Microsoft.Resources/subscriptions/resourcegroups/write`

Optional permissions for attaching an existing user-assigned identity to a node
- `Microsoft.ManagedIdentity/userAssignedIdentities/assign/action`

- `Microsoft.ManagedIdentity/userAssignedIdentities/read`

Required permissions for creating resource tags
- `Microsoft.Resources/tags/write`

Required permissions for creating storage resources
- `Microsoft.Storage/storageAccounts/blobServices/read`

- `Microsoft.Storage/storageAccounts/blobServices/containers/write`

- `Microsoft.Storage/storageAccounts/fileServices/read`

- `Microsoft.Storage/storageAccounts/fileServices/shares/read`

- `Microsoft.Storage/storageAccounts/fileServices/shares/write`

- `Microsoft.Storage/storageAccounts/fileServices/shares/delete`

- `Microsoft.Storage/storageAccounts/listKeys/action`

- `Microsoft.Storage/storageAccounts/read`

- `Microsoft.Storage/storageAccounts/write`

Optional permissions for creating a private storage endpoint for the image registry
- `Microsoft.Network/privateEndpoints/write`

- `Microsoft.Network/privateEndpoints/read`

- `Microsoft.Network/privateEndpoints/privateDnsZoneGroups/write`

- `Microsoft.Network/privateEndpoints/privateDnsZoneGroups/read`

- `Microsoft.Network/privateDnsZones/join/action`

- `Microsoft.Storage/storageAccounts/PrivateEndpointConnectionsApproval/action`

Optional permissions for creating marketplace virtual machine resources
- `Microsoft.MarketplaceOrdering/offertypes/publishers/offers/plans/agreements/read`

- `Microsoft.MarketplaceOrdering/offertypes/publishers/offers/plans/agreements/write`

Optional permissions for creating compute resources
- `Microsoft.Compute/availabilitySets/delete`

- `Microsoft.Compute/images/read`

- `Microsoft.Compute/images/write`

- `Microsoft.Compute/images/delete`

Optional permissions for enabling user-managed encryption
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

Optional permissions for installing a cluster using the `NatGateway` outbound type
- `Microsoft.Network/natGateways/read`

- `Microsoft.Network/natGateways/write`

Optional permissions for installing a private cluster with Azure Network Address Translation (NAT)
- `Microsoft.Network/natGateways/join/action`

- `Microsoft.Network/natGateways/read`

- `Microsoft.Network/natGateways/write`

Optional permissions for installing a private cluster with Azure firewall
- `Microsoft.Network/azureFirewalls/applicationRuleCollections/write`

- `Microsoft.Network/azureFirewalls/read`

- `Microsoft.Network/azureFirewalls/write`

- `Microsoft.Network/routeTables/join/action`

- `Microsoft.Network/routeTables/read`

- `Microsoft.Network/routeTables/routes/read`

- `Microsoft.Network/routeTables/routes/write`

- `Microsoft.Network/routeTables/write`

- `Microsoft.Network/virtualNetworks/peer/action`

- `Microsoft.Network/virtualNetworks/virtualNetworkPeerings/read`

- `Microsoft.Network/virtualNetworks/virtualNetworkPeerings/write`

Optional permission for running gather bootstrap
- `Microsoft.Compute/virtualMachines/retrieveBootDiagnosticsData/action`

The following permissions are required for deleting an OpenShift Container Platform cluster on Microsoft Azure. You can use the same permissions to delete a private OpenShift Container Platform cluster on Azure.

Required permissions for deleting authorization resources
- `Microsoft.Authorization/roleAssignments/delete`

Required permissions for deleting compute resources
- `Microsoft.Compute/disks/delete`

- `Microsoft.Compute/galleries/delete`

- `Microsoft.Compute/galleries/images/delete`

- `Microsoft.Compute/galleries/images/versions/delete`

- `Microsoft.Compute/virtualMachines/delete`

Required permissions for deleting identity management resources
- `Microsoft.ManagedIdentity/userAssignedIdentities/delete`

Required permissions for deleting network resources
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

> [!NOTE]
> The following permissions are not required to delete a private OpenShift Container Platform cluster on Azure.
>
> - `Microsoft.Network/dnszones/read`
>
> - `Microsoft.Network/dnsZones/A/read`
>
> - `Microsoft.Network/dnsZones/A/delete`
>
> - `Microsoft.Network/dnsZones/CNAME/read`
>
> - `Microsoft.Network/dnsZones/CNAME/delete`

Required permissions for checking the health of resources
- `Microsoft.Resourcehealth/healthevent/Activated/action`

- `Microsoft.Resourcehealth/healthevent/Resolved/action`

- `Microsoft.Resourcehealth/healthevent/Updated/action`

Required permissions for deleting a resource group
- `Microsoft.Resources/subscriptions/resourcegroups/delete`

Required permissions for deleting storage resources
- `Microsoft.Storage/storageAccounts/delete`

- `Microsoft.Storage/storageAccounts/listKeys/action`

> [!NOTE]
> To install OpenShift Container Platform on Azure, you must scope the permissions to your subscription. You can re-scope these permissions to the resource group created by installation program. If the public DNS zone is present in a different resource group, then the network DNS zone related permissions must always be applied to your subscription. By default, the OpenShift Container Platform installation program assigns the Azure identity the `Contributor` role.
>
> You can scope all the permissions to your subscription when deleting an OpenShift Container Platform cluster.

<div>

<div class="title">

Additional resources

</div>

- [Managing access to Azure resources using the Azure portal (Azure documentation)](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)

- [Custom roles (Azure documentation)](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles)

</div>

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

<div>

<div class="title">

Additional resources

</div>

- [List user-assigned managed identities (Azure documentation)](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-manage-user-assigned-managed-identities?pivots=identity-mi-methods-azp#list-user-assigned-managed-identities)

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

- [About the Cloud Credential Operator](../../authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.md#about-cloud-credential-operator-modes)

</div>

# Supported Azure Marketplace regions

Installing a cluster by using the Azure Marketplace image is available to customers who purchase the offer in North America and EMEA.

While the offer must be purchased in North America or EMEA, you can deploy the cluster to any of the Azure public partitions that OpenShift Container Platform supports.

> [!NOTE]
> Deploying a cluster using the Azure Marketplace image is not supported for the Azure Government regions.

# Supported Azure regions

Base on your subscription, the installation program dynamically generates the list of available Microsoft Azure public regions.

## Supported Azure public regions

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

## Supported Azure Government regions

Support for the following Microsoft Azure Government (MAG) regions was added in OpenShift Container Platform version 4.6:

- `usgovtexas` (US Gov Texas)

- `usgovvirginia` (US Gov Virginia)

You can reference all available MAG regions in the [Azure documentation](https://azure.microsoft.com/en-us/global-infrastructure/geographies/#geographies). Other provided MAG regions are expected to work with OpenShift Container Platform, but have not been tested.

# Additional resources

- [Resolve errors for reserved resource names (Azure documentation)](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-reserved-resource-name)

- [Install a customized cluster on Azure](ipi/installing-azure-customizations.md#installing-azure-customizations)

- [Quickly install a cluster on Azure with default options](ipi/installing-azure-default.md#installing-azure-default)
