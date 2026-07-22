<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With Oracle® Edge Cloud, you can run applications and middleware by using Oracle® Cloud Infrastructure (OCI) services on high performance cloud infrastructure in your data center.

The following procedures describe a cluster installation on Oracle® Compute Cloud@Customer as an example.

# Supported Oracle Edge Cloud infrastructures

The following table describes the support status of each Oracle® Edge Cloud infrastructure offering:

| Infrastructure type           | Support status       |
|-------------------------------|----------------------|
| Private Cloud Appliance       | General Availability |
| Oracle Compute Cloud@Customer | General Availability |
| Roving Edge                   | Technology Preview   |

Oracle Edge Cloud infrastructure support statuses

# Overview

You can install OpenShift Container Platform on Oracle Edge Cloud by using the Assisted Installer.

For an alternative installation method, see "Installing a cluster on Oracle® Edge Cloud by using the Agent-based Installer".

<div>

<div class="title">

Preinstallation considerations

</div>

- Ensure that your installation meets the prerequisites specified for Oracle. For details, see the "Access and Considerations" section in the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).

- Ensure that your infrastructure is certified and uses a compatible cloud instance type. For details, see [Oracle Cloud Infrastructure](https://catalog.redhat.com/cloud/detail/216977).

- Ensure that you are performing the installation on a virtual machine.

</div>

<div class="formalpara">

<div class="title">

Installation process

</div>

The installation process builds a bastion host within the designated compartment of the OpenShift Container Platform cluster. The bastion host is used to run two Terraform scripts:

</div>

- The first script builds IAM Resources in the OCI Home region of the Oracle® Edge Cloud system (two Dynamic Groups and one Policy).

- The second script builds the infrastructure resources on the Oracle® Edge Cloud system to support the OpenShift Container Platform cluster, including the OpenShift Container Platform VCN, public and private subnets, load balancers, Internet GW, NAT GW, and DNS server. The script includes all the resources needed to activate the control plane nodes and compute nodes that form a cluster.

The bastion host is installed in the designated OpenShift Container Platform Compartment and configured to communicate through a designated Oracle® Edge Cloud DRG Subnet or Internet GW Subnet within the Oracle® Edge Cloud parent tenancy.

The installation process subsequently provisions three control plane (master) nodes and three compute (worker) nodes, together with the external and internal Load Balancers that form the cluster. This is the standard implementation for Oracle Edge Cloud.

<div class="formalpara">

<div class="title">

Main steps

</div>

The main steps of the procedure are as follows:

</div>

1.  Preparing the Oracle® Edge Cloud bastion server.

2.  Running the Terraform script via the Home region.

3.  Preparing the OpenShift Container Platform image for Oracle Edge Cloud.

4.  Running the Terraform script via the Oracle® Edge Cloud region.

5.  Installing the cluster by using the Assisted Installer web console.

# Preparing the OCI bastion server

By implementing a bastion host, you can securely and efficiently manage access to your Oracle Cloud Infrastructure (OCI) resources, ensuring that your private instances remain protected and accessible only through a secure, controlled entry point.

<div>

<div class="title">

Prerequisites

</div>

- See the "Bastion server - prerequisites" section in the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Install the bastion server. For details, see the "Bastion Installation" section in the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).

2.  Install the Terraform application which is used to run the Terraform script. For details, see the "Terraform Installation" section in the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).

3.  Install and configure the OCI command-line interface (CLI). For details, see the "Installing and Configuring the OCI CLI" section in the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).

</div>

<div>

<div class="title">

Additional resources

</div>

- [Quick start - Installing the CLI (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm).

</div>

# Running the Terraform script via the Home region

Copy the Terraform scripts `createInfraResources.tf` and `terraform.tfvars` onto the bastion server. Then run the `createInfraResources.tf` script to create the Dynamic Group Identity resources on your Oracle Cloud Infrastructure (OCI) Home Region. These resources include dynamic groups, policies, and tags.

<div>

<div class="title">

Prerequisites

</div>

- You have tenancy privileges to create Dynamic Groups and Policies. If not, you can manually provision them during this procedure.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Connect to the bastion server via SSH.

2.  Create `OpenShift\createResourceOnHomeRegion` folders.

3.  Copy the `createInfraResources.tf` and `terraform.tfvars` files from the C3_PCA GitHub repository into the `createResourceOnHomeRegion` folder.

4.  Ensure that you have access to the source environment, and that your C3 certificate has been exported.

5.  Run the `createInfraResources.tf` Terraform script.

</div>

For the full procedure, see the "Terraform Script Execution Part-1 (Run Script via Home Region)" section in the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).

# Preparing the OCI image

Generate the OpenShift Container Platform ISO image in the Assisted Installer on the Red Hat portal. Then, convert the image to an Oracle Edge Cloud compatible image and upload it to the **Custom Images** page of your Oracle Edge Cloud environment.

You can generate, convert and upload the image on your laptop and not on the bastion server or within environments such as Oracle Solution Center.

## Generating the image in the Assisted Installer

Create a cluster and download the discovery ISO image.

<div>

<div class="title">

Procedure

</div>

1.  Log in to [Assisted Installer web console](https://console.redhat.com/) with your credentials.

2.  In the **Red Hat OpenShift** tile, select **OpenShift**.

3.  In the **Red Hat OpenShift Container Platform** tile, select **Create Cluster**.

4.  On the **Cluster Type** page, scroll to the end of the **Cloud** tab, and select **Oracle Cloud Infrastructure (virtual machines)**.

5.  On the **Create an OpenShift Cluster** page, select the **Interactive** tile.

6.  On the **Cluster Details** page, complete the following fields:

    <table>
    <colgroup>
    <col style="width: 25%" />
    <col style="width: 75%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Field</th>
    <th style="text-align: left;">Action required</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p><strong>Cluster name</strong></p></td>
    <td style="text-align: left;"><p>Specify the name of your OpenShift Container Platform cluster. This name is the same name you used to create the resource via the Terraform scripts. The name must be between 1-54 characters. It can use lowercase alphanumeric characters or hyphen (-), but must start and end with a lowercase letter or a number.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><strong>Base domain</strong></p></td>
    <td style="text-align: left;"><p>Specify the base domain of the cluster. This is the value used for the <code>zone_dns</code> variables in the Terraform scripts that run on Oracle® Edge Cloud. Make a note of the value.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><strong>OpenShift version</strong></p></td>
    <td style="text-align: left;"><p>Select <strong>OpenShift 4.16.20</strong>. If it is not immediately visible, scroll to the end of the dropdown menu, select <strong>Show all available versions</strong>, and type the version in the search box.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><strong>Integrate with external partner platforms</strong></p></td>
    <td style="text-align: left;"><p>Select <strong>Oracle Cloud Infrastructure</strong>.</p>
    <p>After you specify this value, the <strong>Include custom manifests</strong> checkbox is selected by default and the <strong>Custom manifests</strong> page is added to the wizard.</p></td>
    </tr>
    </tbody>
    </table>

7.  Leave the default settings for the remaining fields, and click **Next**.

8.  On the **Operators** page, click **Next**.

9.  On the **Host Discovery** page, click **Add hosts** and complete the following steps:

    > [!NOTE]
    > The minimal ISO image is the mandatory **Provisioning type** for the Oracle Edge Cloud, and cannot be changed.

    1.  In the **SSH public key** field, add the SSH public key by copying the output of the following command:

        ``` terminal
        $ cat ~/.ssh/id_rsa.put
        ```

        The SSH public key will be installed on all OpenShift Container Platform control plane and compute nodes.

    2.  Click the **Show proxy settings** checkbox.

    3.  Add the proxy variables from the `/etc/environment` file of the bastion server that you configured earlier:

        ``` terminal
        http_proxy=http://www-proxy.<your_domain>.com:80
        https_proxy=http://www-proxy.<your_domain>.com:80
        no_proxy=localhost,127.0.0.1,1,2,3,4,5,6,7,8,9,0,.<your_domain>.com
        #(ie.oracle.com,.oraclecorp.com)
        ```

    4.  Click **Generate Discovery ISO** to generate the discovery ISO image file.

10. Click **Download Discovery ISO** to save the file to your local system. After you download the ISO file, you can rename it as required, for example `discovery_image_<your_cluster_name>.iso`.

</div>

## Converting and uploading the image to Oracle Edge Cloud

Convert the ISO image to an Oracle Cloud Infrastructure (OCI) image and upload it to your Oracle Edge Cloud system from your OCI Home Region Object Store.

<div>

<div class="title">

Procedure

</div>

1.  Convert the image from ISO to OCI.

2.  Upload the OCI image to an OCI bucket, and generate a Pre-Authenticated Request (PAR) URL.

3.  Import the OCI image to the Oracle® Edge Cloud portal.

4.  Copy the Oracle Cloud Identifier (OCID) of the image for use in the next procedure.

</div>

For the full procedure, see step 6 - 8 in the "OpenShift Image Preparation" section of the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).

# Running the Terraform script via the C3 region

Run the `terraform.tfvars` Terraform script to create all infrastructure resources on Oracle® Edge Cloud. These resources include the OpenShift Container Platform VCN, public and private subnets, load balancers, internet GW, NAT GW, and DNS server.

This procedure deploys a cluster consisting of three control plane (master) and three compute (worker) nodes. After deployment, you must rename and reboot the nodes. This process temporarily duplicates nodes, requiring manual cleanup in the next procedure.

<div>

<div class="title">

Procedure

</div>

1.  Connect to the bastion server via SSH.

2.  Set the C3 Certificate location and export the certificate.

3.  Run the `terraform.tfvars` script to create three control plane nodes and three compute nodes.

4.  Update the labels for the control plane and compute nodes.

5.  Stop and restart the instances one by one on the Oracle® Edge Cloud portal.

</div>

For the full procedure, see the "Terraform Script Execution - Part 2" section in the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).

# Completing the installation by using the Assisted Installer web console

After you configure the infrastructure, the instances are now running and are ready to be registered with Red Hat.

## Assigning node roles

If the Terraform scripts completed successfully, twelve hosts are now listed for the cluster. Three control plane hosts and three compute hosts have the status "Disconnected". Three control plane hosts and three compute hosts have the status "Insufficient".

Delete the disconnected hosts and assign roles to the remaining hosts.

<div>

<div class="title">

Procedure

</div>

1.  From the [Assisted Installer web console](https://console.redhat.com/openshift/assisted-installer/clusters), select the cluster and navigate to the **Host discovery** page.

2.  Delete the six hosts with a "Disconnected" status, by clicking the option button for each host and selecting **Remove host**. The status of the remaining hosts changes from "Insufficient" to "Ready". This process can take up to three minutes.

3.  From the **Role** column, assign the **Control plane** role to the three nodes with a boot size of 1.10 TB. Assign the **Worker** role to the three nodes with boot size of 100 GB.

4.  Rename any hosts with a name shorter than 63 characters, by clicking the option button for the host and selecting **Change hostname**. Otherwise the cluster installation will fail.

5.  Click **Next**.

6.  On the **Storage** page, click **Next**.

</div>

## Configuring networking

On the **Networking** page, add the NTP sources for any hosts that display the `Some validations failed` status.

<div>

<div class="title">

Procedure

</div>

1.  In the **Host inventory** table, click the **Some validations failed** link for each host displaying this status.

2.  Click **Add NTP sources**, and then add the IP address `169.254.169.254` for one of the nodes.

3.  Wait for 2 - 3 minutes until all the **Some validations failed** indicators disappear.

4.  Select **Next**.

</div>

## Adding custom manifests

Create, modify, and upload the four mandatory custom manifests provided by Oracle.

- In the `C3/custom_manifests_C3/manifests` folder, the following manifests are mandatory:

  - `oci-ccm.yml`

  - `oci-csi.yml`

- In the `C3/custom_manifests_C3/openshift` folder, the following manifests are mandatory:

  - `machineconfig-ccm.yml`

  - `machineconfig-csi.yml`

<div>

<div class="title">

Prerequisites

</div>

- Prepare the custom manifests. For details, see step 8 in the "Install the Cluster using the RH Assisted Installer UI" section of the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the **Custom manifests** page.

2.  Upload and save the `oci-ccm.yml` and `oci-csi.yml` manifest files:

    1.  In the **Folder** field, select **manifests**.

    2.  In the **File name** field, enter `oci-ccm.yml`.

    3.  In the **Content** section, click **Browse**.

    4.  Select the **oci-ccm.yml** file from the `C3/custom_ manifest_C3/manifests` folder.

    5.  Click **Add another manifest** and repeat the previous substeps for the `oci-csi.yml` file.

3.  Upload and save the `machineconfig-ccm.yml` and `machineconfig-csi.yml` manifest files:

    1.  Click **Add another manifest**.

    2.  In the **Folder** field, select **openshift**.

    3.  In the **File name** field, enter `machineconfig-ccm.yml`.

    4.  In the **Content** section, click **Browse**.

    5.  Select the **machineconfig-ccm.yml** file from the `C3/custom_ manifest_C3/openshift` folder.

    6.  Click **Add another manifest** and repeat the previous substeps for the `machineconfig-csi.yml` file.

4.  Click **Next** to save the custom manifests.

5.  From the **Review and create** page, click **Install cluster** to create your OpenShift Container Platform cluster. This process takes approximately thirty minutes.

</div>

# Opening OpenShift Container Platform from the Oracle Edge Cloud web console

For instructions to access the OpenShift Container Platform console from Oracle Edge Cloud, see steps 15 - 17 in the "Install the Cluster using the RH Assisted Installer UI" section of the [Oracle documentation](https://www.oracle.com/a/otn/docs/compute_cloud_at_customer_assisted_installer.pdf?source=:em:nl:mt::::PCATP).
