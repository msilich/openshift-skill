<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform version 4.17, you can install a cluster on Microsoft Azure Stack Hub by using infrastructure that you provide.

Several [Azure Resource Manager](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/overview) (ARM) templates are provided to assist in completing these steps or to help model your own.

> [!IMPORTANT]
> The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several ARM templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods; the templates are just an example.

# Prerequisites

- You reviewed details about the [OpenShift Container Platform installation and update](../../../architecture/architecture-installation.md#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../../overview/installing-preparing.md#installing-preparing).

- You have installed Azure Stack Hub version 2008 or later.

- You [configured an Azure Stack Hub account](../installing-azure-stack-hub-account.md#installing-azure-stack-hub-account) to host the cluster.

- You downloaded the Azure CLI and installed it on your computer. See [Install the Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) in the Azure documentation. The documentation below was tested using version `2.28.0` of the Azure CLI. Azure CLI commands might perform differently based on the version you use.

- If you use a firewall and plan to use the Telemetry service, you [configured the firewall to allow the sites](../../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall) that your cluster requires access to.

  > [!NOTE]
  > Be sure to also review this site list if you are configuring a proxy.

# Configuring your Azure Stack Hub project

Before you can install OpenShift Container Platform, you must configure an Azure project to host it.

> [!IMPORTANT]
> All Azure Stack Hub resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure Stack Hub restricts, see [Resolve reserved resource name errors](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-reserved-resource-name) in the Azure documentation.

## Azure Stack Hub account limits

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

- [Optimizing storage](../../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

</div>

## Configuring a DNS zone in Azure Stack Hub

To successfully install OpenShift Container Platform on Azure Stack Hub, you must create DNS records in an Azure Stack Hub DNS zone. The DNS zone must be authoritative for the domain. To delegate a registrar’s DNS zone to Azure Stack Hub, see Microsoft’s documentation for [Azure Stack Hub datacenter DNS integration](https://docs.microsoft.com/en-us/azure-stack/operator/azure-stack-integrate-dns?view=azs-2102).

You can view Azure’s DNS solution by visiting this [example for creating DNS zones](#installation-azure-create-dns-zones_installing-azure-stack-hub-user-infra).

## Certificate signing requests management

On user-provisioned infrastructure, you must provide a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that is requested by using kubelet credentials because it cannot confirm that the correct machine issued the request. You must determine and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

## Required Azure Stack Hub roles

Your Microsoft Azure Stack Hub account must have the following roles for the subscription that you use:

- `Owner`

To set roles on the Azure portal, see the [Manage access to resources in Azure Stack Hub with role-based access control](https://docs.microsoft.com/en-us/azure-stack/user/azure-stack-manage-permissions?view=azs-2102) in the Microsoft documentation.

## Creating a service principal

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

- [About the Cloud Credential Operator](../../../authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.md#about-cloud-credential-operator-modes)

</div>

# Creating the installation files for Azure Stack Hub

To install OpenShift Container Platform on Microsoft Azure Stack Hub using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use. You manually create the `install-config.yaml` file, and then generate and customize the Kubernetes manifests and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.

## Manually creating the installation configuration file

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

    Make the following modifications for Azure Stack Hub:

    1.  Set the `replicas` parameter to `0` for the `compute` pool:

        ``` yaml
        compute:
        - hyperthreading: Enabled
          name: worker
          platform: {}
          replicas: 0
        ```

        - `replicas`: Set to `0`.

          The compute machines will be provisioned manually later.

    2.  Update the `platform.azure` section of the `install-config.yaml` file to configure your Azure Stack Hub configuration:

        ``` yaml
        platform:
          azure:
            armEndpoint: <azurestack_arm_endpoint>
            baseDomainResourceGroupName: <resource_group>
            cloudName: AzureStackCloud
            region: <azurestack_region>
        ```

        where:

        `<azurestack_arm_endpoint>`
        Specifies the Azure Resource Manager endpoint of your Azure Stack Hub environment, like `https://management.local.azurestack.external`.

        `<resource_group>`
        Specifies the name of the resource group that contains the DNS zone for your base domain.

        `cloudName`
        Specifies the Azure Stack Hub environment, which is used to configure the Azure SDK with the appropriate Azure API endpoints.

        `region`
        Specifies the name of your Azure Stack Hub region.

3.  Back up the `install-config.yaml` file so that you can use it to install many clusters.

    > [!IMPORTANT]
    > Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for Azure Stack Hub](../installation-config-parameters-ash.md#installation-config-parameters-ash)

</div>

## Sample customized install-config.yaml file for Azure Stack Hub

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters.

> [!IMPORTANT]
> This sample YAML file is provided for reference only. Use it as a resource to enter parameter values into the installation configuration file that you created manually.

``` yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
  name: master
  platform:
    azure:
      osDisk:
        diskSizeGB: 1024
        diskType: premium_LRS
  replicas: 3
compute:
- name: worker
  platform:
    azure:
      osDisk:
        diskSizeGB: 512
        diskType: premium_LRS
  replicas: 0
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
  azure:
    armEndpoint: azurestack_arm_endpoint
    baseDomainResourceGroupName: resource_group
    region: azure_stack_local_region
    resourceGroupName: existing_resource_group
    outboundType: Loadbalancer
    cloudName: AzureStackCloud
pullSecret: '{"auths": ...}'
fips: false
additionalTrustBundle: |
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
sshKey: ssh-ed25519 AAAA...
```

- The `controlPlane` section is a single mapping, but the `compute` section is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`, and the first line of the `controlPlane` section must not. Only one control plane pool is used.

- You can specify the size of the disk to use in GB. Minimum recommendation for control plane nodes is 1024 GB.

- Specify the name of the cluster.

- The cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

- Specify the Azure Resource Manager endpoint that your Azure Stack Hub operator provides.

- Specify the name of the resource group that contains the DNS zone for your base domain.

- Specify the name of your Azure Stack Hub local region.

- Specify the name of an already existing resource group to install your cluster to. If undefined, a new resource group is created for the cluster.

- Specify the Azure Stack Hub environment as your target platform.

- Specify the pull secret required to authenticate your cluster.

- Whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead.

  > [!IMPORTANT]
  > To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Installing the system in FIPS mode](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/security_hardening/assembly_installing-the-system-in-fips-mode_security-hardening).
  >
  > When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.

- If your Azure Stack Hub environment uses an internal certificate authority (CA), add the necessary certificate bundle in `.pem` format.

- You can optionally provide the `sshKey` value that you use to access the machines in your cluster.

  > [!NOTE]
  > For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

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

You must export a common set of variables that are used with the provided Azure Resource Manager (ARM) templates used to assist in completing a user-provided infrastructure install on Microsoft Azure Stack Hub.

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
    The region to deploy the cluster into. This is the value of the `.platform.azure.region` attribute from the `install-config.yaml` file.

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
    The base domain to deploy the cluster to. The base domain corresponds to the DNS zone that you created for your cluster. This is the value of the `.baseDomain` attribute from the `install-config.yaml` file.

    ``` terminal
    $ export BASE_DOMAIN_RESOURCE_GROUP=<base_domain_resource_group>
    ```

    where:

    `<base_domain_resource_group>`
    The resource group where the DNS zone exists. This is the value of the `.platform.azure.baseDomainResourceGroupName` attribute from the `install-config.yaml` file.

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

7.  Optional: If your Azure Stack Hub environment uses an internal certificate authority (CA), you must update the `.spec.trustedCA.name` field in the `<installation_directory>/manifests/cluster-proxy-01-config.yaml` file to use `user-ca-bundle`:

    ``` yaml
    ...
    spec:
      trustedCA:
        name: user-ca-bundle
    ...
    ```

    Later, you must update your bootstrap ignition to include the CA.

8.  When configuring Azure on user-provisioned infrastructure, you must export some common variables defined in the manifest files to use later in the Azure Resource Manager (ARM) templates:

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

9.  Manually create your cloud credentials.

    1.  From the directory that contains the installation program, obtain details of the OpenShift Container Platform release image that your `openshift-install` binary is built to use:

        ``` terminal
        $ openshift-install version
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` text
        release image quay.io/openshift-release-dev/ocp-release:4.y.z-x86_64
        ```

        </div>

    2.  Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

        ``` terminal
        $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
        ```

    3.  Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

        ``` terminal
        $ oc adm release extract \
          --from=$RELEASE_IMAGE \
          --credentials-requests \
          --included \//
          --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \//
          --to=<path_to_directory_for_credentials_requests>
        ```

        where:

        `--included`
        Specifies to include only the manifests that your specific cluster configuration requires.

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
          labels:
            controller-tools.k8s.io: "1.0"
          name: openshift-image-registry-azure
          namespace: openshift-cloud-credential-operator
        spec:
          secretRef:
            name: installer-cloud-credentials
            namespace: openshift-image-registry
          providerSpec:
            apiVersion: cloudcredential.openshift.io/v1
            kind: AzureProviderSpec
            roleBindings:
            - role: Contributor
        ```

        </div>

    4.  Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object. The format for the secret data varies for each cloud provider.

        <div class="formalpara">

        <div class="title">

        Sample `secrets.yaml` file

        </div>

        ``` yaml
        apiVersion: v1
        kind: Secret
        metadata:
            name: ${secret_name}
            namespace: ${secret_namespace}
        stringData:
          azure_subscription_id: ${subscription_id}
          azure_client_id: ${app_id}
          azure_client_secret: ${client_secret}
          azure_tenant_id: ${tenant_id}
          azure_resource_prefix: ${cluster_name}
          azure_resourcegroup: ${resource_group}
          azure_region: ${azure_region}
        ```

        </div>

    5.  Create a `cco-configmap.yaml` file in the manifests directory with the Cloud Credential Operator (CCO) disabled:

        <div class="formalpara">

        <div class="title">

        Sample `ConfigMap` object

        </div>

        ``` yaml
        apiVersion: v1
        kind: ConfigMap
        metadata:
        name: cloud-credential-operator-config
        namespace: openshift-cloud-credential-operator
          annotations:
            release.openshift.io/create-only: "true"
        data:
          disabled: "true"
        ```

        </div>

10. To create the Ignition configuration files, run the following command from the directory that contains the installation program:

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

<div>

<div class="title">

Additional resources

</div>

- [Manually manage cloud credentials](../ipi/installing-azure-stack-hub-default.md#manually-create-iam_installing-azure-stack-hub-default)

</div>

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

# Creating the Azure resource group

You must create a Microsoft Azure [resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview#resource-groups). This is used during the installation of your OpenShift Container Platform cluster on Azure Stack Hub.

<div>

<div class="title">

Procedure

</div>

- Create the resource group in a supported Azure region:

  ``` terminal
  $ az group create --name ${RESOURCE_GROUP} --location ${AZURE_REGION}
  ```

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
    $ export COMPRESSED_VHD_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.artifacts.azurestack.formats."vhd.gz".disk.location')
    ```

    > [!IMPORTANT]
    > The RHCOS images might not change with every release of OpenShift Container Platform. You must specify an image with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Use the image version that matches your OpenShift Container Platform version if it is available.

4.  Create the storage container for the VHD:

    ``` terminal
    $ az storage container create --name vhd --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY}
    ```

5.  Download the compressed RHCOS VHD file locally:

    ``` terminal
    $ curl -O -L ${COMPRESSED_VHD_URL}
    ```

6.  Decompress the VHD file.

    > [!NOTE]
    > The decompressed VHD file is approximately 16 GB, so be sure that your host system has 16 GB of free space available. You can delete the VHD file after you upload it.

7.  Copy the local VHD to a blob:

    ``` terminal
    $ az storage blob upload --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY} -c vhd -n "rhcos.vhd" -f rhcos-<rhcos_version>-azurestack.x86_64.vhd
    ```

8.  Create a blob storage container and upload the generated `bootstrap.ign` file:

    ``` terminal
    $ az storage container create --name files --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY}
    ```

    ``` terminal
    $ az storage blob upload --account-name ${CLUSTER_NAME}sa --account-key ${ACCOUNT_KEY} -c "files" -f "<installation_directory>/bootstrap.ign" -n "bootstrap.ign"
    ```

</div>

# Example for creating DNS zones

DNS records are required for clusters that use user-provisioned infrastructure. You should choose the DNS strategy that fits your scenario.

For this example, [Azure Stack Hub’s datacenter DNS integration](https://docs.microsoft.com/en-us/azure-stack/operator/azure-stack-integrate-dns?view=azs-2102) is used, so you will create a DNS zone.

> [!NOTE]
> The DNS zone is not required to exist in the same resource group as the cluster deployment and might already exist in your organization for the desired base domain. If that is the case, you can skip creating the DNS zone; be sure the installation config you generated earlier reflects that scenario.

<div>

<div class="title">

Procedure

</div>

- Create the new DNS zone in the resource group exported in the `BASE_DOMAIN_RESOURCE_GROUP` environment variable:

  ``` terminal
  $ az network dns zone create -g ${BASE_DOMAIN_RESOURCE_GROUP} -n ${CLUSTER_NAME}.${BASE_DOMAIN}
  ```

  You can skip this step if you are using a DNS zone that already exists.

</div>

You can learn more about [configuring a DNS zone in Azure Stack Hub](#installation-azure-stack-hub-network-config_installing-azure-stack-hub-user-infra) by visiting that section.

# Creating a VNet in Azure Stack Hub

You must create a virtual network (VNet) in Microsoft Azure Stack Hub for your OpenShift Container Platform cluster to use. You can customize the VNet to meet your requirements. One way to create the VNet is to modify the provided Azure Resource Manager (ARM) template.

> [!NOTE]
> If you do not use the provided ARM template to create your Azure Stack Hub infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

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

</div>

## ARM template for the VNet

You can use the following Azure Resource Manager (ARM) template to deploy the VNet that you need for your OpenShift Container Platform cluster:

<div class="example">

<div class="title">

`01_vnet.json` ARM template

</div>

``` json
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azurestack/01_vnet.json[role=include]
```

</div>

# Deploying the RHCOS cluster image for the Azure Stack Hub infrastructure

You must use a valid Red Hat Enterprise Linux CoreOS (RHCOS) image for Microsoft Azure Stack Hub for your OpenShift Container Platform nodes.

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
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azurestack/02_storage.json[role=include]
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

# Creating networking and load balancing components in Azure Stack Hub

You must configure networking and load balancing in Microsoft Azure Stack Hub for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Azure Resource Manager (ARM) template.

Load balancing requires the following DNS records:

- An `api` DNS record for the API public load balancer in the DNS zone.

- An `api-int` DNS record for the API internal load balancer in the DNS zone.

> [!NOTE]
> If you do not use the provided ARM template to create your Azure Stack Hub infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

<div>

<div class="title">

Prerequisites

</div>

- Create and configure a VNet and associated subnets in Azure Stack Hub.

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
      --parameters baseName="${INFRA_ID}"
    ```

    - The base name to be used in resource names; this is usually the cluster’s infrastructure ID.

3.  Create an `api` DNS record and an `api-int` DNS record. When creating the API DNS records, the `${BASE_DOMAIN_RESOURCE_GROUP}` variable must point to the resource group where the DNS zone exists.

    1.  Export the following variable:

        ``` terminal
        $ export PUBLIC_IP=`az network public-ip list -g ${RESOURCE_GROUP} --query "[?name=='${INFRA_ID}-master-pip'] | [0].ipAddress" -o tsv`
        ```

    2.  Export the following variable:

        ``` terminal
        $ export PRIVATE_IP=`az network lb frontend-ip show -g "$RESOURCE_GROUP" --lb-name "${INFRA_ID}-internal" -n internal-lb-ip --query "privateIpAddress" -o tsv`
        ```

    3.  Create the `api` DNS record in a new DNS zone:

        ``` terminal
        $ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n api -a ${PUBLIC_IP} --ttl 60
        ```

        If you are adding the cluster to an existing DNS zone, you can create the `api` DNS record in it instead:

        ``` terminal
        $ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${BASE_DOMAIN} -n api.${CLUSTER_NAME} -a ${PUBLIC_IP} --ttl 60
        ```

    4.  Create the `api-int` DNS record in a new DNS zone:

        ``` terminal
        $ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z "${CLUSTER_NAME}.${BASE_DOMAIN}" -n api-int -a ${PRIVATE_IP} --ttl 60
        ```

        If you are adding the cluster to an existing DNS zone, you can create the `api-int` DNS record in it instead:

        ``` terminal
        $ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${BASE_DOMAIN} -n api-int.${CLUSTER_NAME} -a ${PRIVATE_IP} --ttl 60
        ```

</div>

## ARM template for the network and load balancers

You can use the following Azure Resource Manager (ARM) template to deploy the networking objects and load balancers that you need for your OpenShift Container Platform cluster:

<div class="example">

<div class="title">

`03_infra.json` ARM template

</div>

``` json
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azurestack/03_infra.json[role=include]
```

</div>

# Creating the bootstrap machine in Azure Stack Hub

You must create the bootstrap machine in Microsoft Azure Stack Hub to use during OpenShift Container Platform cluster initialization. One way to create this machine is to modify the provided Azure Resource Manager (ARM) template.

> [!NOTE]
> If you do not use the provided ARM template to create your bootstrap machine, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

<div>

<div class="title">

Prerequisites

</div>

- Create and configure networking and load balancers in Azure Stack Hub.

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

    1.  If your environment uses a public certificate authority (CA), run this command:

        ``` terminal
        $ export BOOTSTRAP_IGNITION=`jq -rcnM --arg v "3.2.0" --arg url ${BOOTSTRAP_URL} '{ignition:{version:$v,config:{replace:{source:$url}}}}' | base64 | tr -d '\n'`
        ```

    2.  If your environment uses an internal CA, you must add your PEM encoded bundle to the bootstrap ignition stub so that your bootstrap virtual machine can pull the bootstrap ignition from the storage account. Run the following commands, which assume your CA is in a file called `CA.pem`:

        ``` terminal
        $ export CA="data:text/plain;charset=utf-8;base64,$(cat CA.pem |base64 |tr -d '\n')"
        ```

        ``` terminal
        $ export BOOTSTRAP_IGNITION=`jq -rcnM --arg v "3.2.0" --arg url "$BOOTSTRAP_URL" --arg cert "$CA" '{ignition:{version:$v,security:{tls:{certificateAuthorities:[{source:$cert}]}},config:{replace:{source:$url}}}}' | base64 | tr -d '\n'`
        ```

4.  Create the deployment by using the `az` CLI:

    ``` terminal
    $ az deployment group create --verbose -g ${RESOURCE_GROUP} \
      --template-file "<installation_directory>/04_bootstrap.json" \
      --parameters bootstrapIgnition="${BOOTSTRAP_IGNITION}" \
      --parameters baseName="${INFRA_ID}" \
      --parameters diagnosticsStorageAccountName="${CLUSTER_NAME}sa"
    ```

    - The bootstrap Ignition content for the bootstrap cluster.

    - The base name to be used in resource names; this is usually the cluster’s infrastructure ID.

    - The name of the storage account for your cluster.

</div>

## ARM template for the bootstrap machine

You can use the following Azure Resource Manager (ARM) template to deploy the bootstrap machine that you need for your OpenShift Container Platform cluster:

<div class="example">

<div class="title">

`04_bootstrap.json` ARM template

</div>

``` json
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azurestack/04_bootstrap.json[role=include]
```

</div>

# Creating the control plane machines in Azure Stack Hub

You must create the control plane machines in Microsoft Azure Stack Hub for your cluster to use. One way to create these machines is to modify the provided Azure Resource Manager (ARM) template.

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
      --parameters diagnosticsStorageAccountName="${CLUSTER_NAME}sa"
    ```

    - The Ignition content for the control plane nodes (also known as the master nodes).

    - The base name to be used in resource names; this is usually the cluster’s infrastructure ID.

    - The name of the storage account for your cluster.

</div>

## ARM template for control plane machines

You can use the following Azure Resource Manager (ARM) template to deploy the control plane machines that you need for your OpenShift Container Platform cluster:

<div class="example">

<div class="title">

`05_masters.json` ARM template

</div>

``` json
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azurestack/05_masters.json[role=include]
```

</div>

# Wait for bootstrap completion and remove bootstrap resources in Azure Stack Hub

After you create all of the required infrastructure in Microsoft Azure Stack Hub, wait for the bootstrap process to complete on the machines that you provisioned by using the Ignition config files that you generated with the installation program.

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

# Creating additional worker machines in Azure Stack Hub

You can create worker machines in Microsoft Azure Stack Hub for your cluster to use by launching individual instances discretely or by automated processes outside the cluster, such as auto scaling groups. You can also take advantage of the built-in cluster scaling mechanisms and the machine API in OpenShift Container Platform.

In this example, you manually launch one instance by using the Azure Resource Manager (ARM) template. Additional instances can be launched by including additional resources of type `06_workers.json` in the file.

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
      --parameters baseName="${INFRA_ID}"
      --parameters diagnosticsStorageAccountName="${CLUSTER_NAME}sa"
    ```

    - The Ignition content for the worker nodes.

    - The base name to be used in resource names; this is usually the cluster’s infrastructure ID.

    - The name of the storage account for your cluster.

</div>

## ARM template for worker machines

You can use the following Azure Resource Manager (ARM) template to deploy the worker machines that you need for your OpenShift Container Platform cluster:

<div class="example">

<div class="title">

`06_workers.json` ARM template

</div>

``` json
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/azurestack/06_workers.json[role=include]
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

- You deployed an OpenShift Container Platform cluster on Microsoft Azure Stack Hub by using infrastructure that you provisioned.

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

3.  Add a `*.apps` record to the DNS zone.

    1.  If you are adding this cluster to a new DNS zone, run:

        ``` terminal
        $ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${CLUSTER_NAME}.${BASE_DOMAIN} -n *.apps -a ${PUBLIC_IP_ROUTER} --ttl 300
        ```

    2.  If you are adding this cluster to an already existing DNS zone, run:

        ``` terminal
        $ az network dns record-set a add-record -g ${BASE_DOMAIN_RESOURCE_GROUP} -z ${BASE_DOMAIN} -n *.apps.${CLUSTER_NAME} -a ${PUBLIC_IP_ROUTER} --ttl 300
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

# Completing an Azure Stack Hub installation on user-provisioned infrastructure

After you start the OpenShift Container Platform installation on Microsoft Azure Stack Hub user-provisioned infrastructure, you can monitor the cluster events until the cluster is ready.

<div>

<div class="title">

Prerequisites

</div>

- Deploy the bootstrap machine for an OpenShift Container Platform cluster on user-provisioned Azure Stack Hub infrastructure.

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

<div>

<div class="title">

Additional resources

</div>

- [About remote health monitoring](../../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring)

</div>
