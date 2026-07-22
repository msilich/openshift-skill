<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you can install OpenShift Container Platform, you must configure a Microsoft Azure account.

> [!IMPORTANT]
> All Azure resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure restricts, see [Resolve reserved resource name errors](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-reserved-resource-name) in the Azure documentation.

# Azure Stack Hub account limits

The OpenShift Container Platform cluster uses a number of Microsoft Azure Stack Hub components, and the default [Quota types in Azure Stack Hub](https://docs.microsoft.com/en-us/azure-stack/operator/azure-stack-quota-types?view=azs-2102) affect your ability to install OpenShift Container Platform clusters.

The following table summarizes the Azure Stack Hub components whose limits can impact your ability to install and run OpenShift Container Platform clusters.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 23%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Component</th>
<th style="text-align: left;">Number of components required by default</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>vCPU</p></td>
<td style="text-align: left;"><p>56</p></td>
<td style="text-align: left;"><p>A default cluster requires 56 vCPUs, so you must increase the account limit.</p>
<p>By default, each cluster creates the following instances:</p>
<ul>
<li><p>One bootstrap machine, which is removed after installation</p></li>
<li><p>Three control plane machines</p></li>
<li><p>Three compute machines</p></li>
</ul>
<p>Because the bootstrap, control plane, and worker machines use <code>Standard_DS4_v2</code> virtual machines, which use 8 vCPUs, a default cluster requires 56 vCPUs. The bootstrap node VM is used only during installation.</p>
<p>To deploy more worker nodes, enable autoscaling, deploy large workloads, or use a different instance type, you must further increase the vCPU limit for your account to ensure that your cluster can deploy the machines that you require.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>VNet</p></td>
<td style="text-align: left;"><p>1</p></td>
<td style="text-align: left;"><p>Each default cluster requires one Virtual Network (VNet), which contains two subnets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Network interfaces</p></td>
<td style="text-align: left;"><p>7</p></td>
<td style="text-align: left;"><p>Each default cluster requires seven network interfaces. If you create more machines or your deployed workloads create load balancers, your cluster uses more network interfaces.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Network security groups</p></td>
<td style="text-align: left;"><p>2</p></td>
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
<td style="text-align: left;"><p>2</p></td>
<td style="text-align: left;"><p>The public load balancer uses a public IP address. The bootstrap machine also uses a public IP address so that you can SSH into the machine to troubleshoot issues during installation. The IP address for the bootstrap node is used only during installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Private IP addresses</p></td>
<td style="text-align: left;"><p>7</p></td>
<td style="text-align: left;"><p>The internal load balancer, each of the three control plane machines, and each of the three worker machines each use a private IP address.</p></td>
</tr>
</tbody>
</table>

To increase an account limit, file a support request on the Azure portal. For more information, see [Request a quota limit increase for Azure Deployment Environments resources](https://learn.microsoft.com/en-us/azure/deployment-environments/how-to-request-quota-increase).

<div>

<div class="title">

Additional resources

</div>

- [Optimizing storage](../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

</div>

# Configuring a DNS zone in Azure Stack Hub

To successfully install OpenShift Container Platform on Azure Stack Hub, you must create DNS records in an Azure Stack Hub DNS zone. The DNS zone must be authoritative for the domain. To delegate a registrar’s DNS zone to Azure Stack Hub, see Microsoft’s documentation for [Azure Stack Hub datacenter DNS integration](https://docs.microsoft.com/en-us/azure-stack/operator/azure-stack-integrate-dns?view=azs-2102).

# Required Azure Stack Hub roles

Your Microsoft Azure Stack Hub account must have the following roles for the subscription that you use:

- `Owner`

To set roles on the Azure portal, see the [Manage access to resources in Azure Stack Hub with role-based access control](https://docs.microsoft.com/en-us/azure-stack/user/azure-stack-manage-permissions?view=azs-2102) in the Microsoft documentation.

# Creating a service principal

Because OpenShift Container Platform and its installation program create Microsoft Azure resources by using the Azure Resource Manager, you must create a service principal to represent it.

<div>

<div class="title">

Prerequisites

</div>

- Install or update the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-yum?view=azure-cli-latest).

- Your Azure account has the required roles for the subscription that you use.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Register your environment:

    ``` terminal
    $ az cloud register -n AzureStackCloud --endpoint-resource-manager <endpoint>
    ```

    - Specify the Azure Resource Manager endpoint, \`https://management.\<region\>.\<fqdn\>/\`.

      See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure-stack/mdc/azure-stack-version-profiles-azurecli-2-tzl#connect-to-azure-stack-hub) for details.

2.  Set the active environment:

    ``` terminal
    $ az cloud set -n AzureStackCloud
    ```

3.  Update your environment configuration to use the specific API version for Azure Stack Hub:

    ``` terminal
    $ az cloud update --profile 2019-03-01-hybrid
    ```

4.  Log in to the Azure CLI:

    ``` terminal
    $ az login
    ```

    If you are in a multitenant environment, you must also supply the tenant ID.

5.  If your Azure account uses subscriptions, ensure that you are using the right subscription:

    1.  View the list of available accounts and record the `tenantId` value for the subscription you want to use for your cluster:

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
            "cloudName": AzureStackCloud",
            "id": "9bab1460-96d5-40b3-a78e-17b15e978a80",
            "isDefault": true,
            "name": "Subscription Name",
            "state": "Enabled",
            "tenantId": "6057c7e9-b3ae-489d-a54e-de3f6bf6a8ee",
            "user": {
              "name": "you@example.com",
              "type": "user"
            }
          }
        ]
        ```

        </div>

    2.  View your active account details and confirm that the `tenantId` value matches the subscription you want to use:

        ``` terminal
        $ az account show
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        {
          "environmentName": AzureStackCloud",
          "id": "9bab1460-96d5-40b3-a78e-17b15e978a80",
          "isDefault": true,
          "name": "Subscription Name",
          "state": "Enabled",
          "tenantId": "6057c7e9-b3ae-489d-a54e-de3f6bf6a8ee",
          "user": {
            "name": "you@example.com",
            "type": "user"
          }
        }
        ```

        </div>

        - Ensure that the value of the `tenantId` parameter is the correct subscription ID.

    3.  If you are not using the right subscription, change the active subscription:

        ``` terminal
        $ az account set -s <subscription_id>
        ```

        - Specify the subscription ID.

    4.  Verify the subscription ID update:

        ``` terminal
        $ az account show
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        {
          "environmentName": AzureStackCloud",
          "id": "33212d16-bdf6-45cb-b038-f6565b61edda",
          "isDefault": true,
          "name": "Subscription Name",
          "state": "Enabled",
          "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee",
          "user": {
            "name": "you@example.com",
            "type": "user"
          }
        }
        ```

        </div>

6.  Record the `tenantId` and `id` parameter values from the output. You need these values during the OpenShift Container Platform installation.

7.  Create the service principal for your account:

    ``` terminal
    $ az ad sp create-for-rbac --role Contributor --name <service_principal> \
      --scopes /subscriptions/<subscription_id>
      --years <years>
    ```

    - Specify the service principal name.

    - Specify the subscription ID.

    - Specify the number of years. By default, a service principal expires in one year. By using the `--years` option you can extend the validity of your service principal.

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
        "appId": "ac461d78-bf4b-4387-ad16-7e32e328aec6",
        "displayName": <service_principal>",
        "password": "00000000-0000-0000-0000-000000000000",
        "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee"
      }
      ```

      </div>

8.  Record the values of the `appId` and `password` parameters from the previous output. You need these values during OpenShift Container Platform installation.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the Cloud Credential Operator](../../authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.md#about-cloud-credential-operator-modes)

</div>

# Next steps

- Install an OpenShift Container Platform cluster:

  - [Installing a cluster on Azure Stack Hub with customizations](ipi/installing-azure-stack-hub-default.md#installing-azure-stack-hub-default)

  - Install an OpenShift Container Platform cluster on Azure Stack Hub with user-provisioned infrastructure by following [Installing a cluster on Azure Stack Hub using ARM templates](upi/installing-azure-stack-hub-user-infra.md#installing-azure-stack-hub-user-infra).
