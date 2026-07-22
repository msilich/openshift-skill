<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When you no longer need an OpenShift Container Platform cluster on Microsoft Azure, you can uninstall the cluster and remove related cloud resources. Complete uninstallation so you avoid ongoing costs and leave no orphaned infrastructure.

# Removing a cluster that uses installer-provisioned infrastructure

To remove an OpenShift Container Platform cluster that uses installer-provisioned infrastructure, you can run the installation program destroy command. Use the installation files from your original deployment to uninstall the cluster from your cloud platform.

> [!NOTE]
> After uninstallation, check your cloud provider for any resources that were not removed properly, especially with user-provisioned infrastructure clusters. Some resources might exist because either the installation program did not create the resource or could not access the resource.

<div>

<div class="title">

Prerequisites

</div>

- You have a copy of the installation program that you used to deploy the cluster.

- You have the files that the installation program generated when you created your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the directory that has the installation program on the computer that you used to install the cluster, run the following command:

    ``` terminal
    $ ./openshift-install destroy cluster \
    --dir <installation_directory> --log-level info
    ```

    where:

    `<installation_directory>`
    Specify the path to the directory that you stored the installation files in.

    `--log-level info`
    To view different details, specify `warn`, `debug`, or `error` instead of `info`.

    > [!NOTE]
    > You must specify the directory that includes the cluster definition files for your cluster. The installation program requires the `metadata.json` file in this directory to delete the cluster.

2.  Optional: Delete the `<installation_directory>` directory and the OpenShift Container Platform installation program.

</div>

# Deleting Microsoft Azure resources with the Cloud Credential Operator utility

After uninstalling an OpenShift Container Platform cluster that uses short-term credentials managed outside the cluster, you can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to remove the Microsoft Azure resources that `ccoctl` created during installation.

<div>

<div class="title">

Prerequisites

</div>

- Extract and prepare the `ccoctl` binary.

- Uninstall an OpenShift Container Platform cluster on Azure that uses short-term credentials.

</div>

<div>

<div class="title">

Procedure

</div>

- Delete the Azure resources that `ccoctl` created by running the following command:

  ``` terminal
  $ ccoctl azure delete \
    --name=<name> \
    --region=<azure_region> \
    --subscription-id=<azure_subscription_id> \
    --delete-oidc-resource-group
  ```

  where:

  `<name>`
  Matches the name that was originally used to create and tag the cloud resources.

  `<azure_region>`
  is the Azure region in which to delete cloud resources.

  `<azure_subscription_id>`
  is the Azure subscription ID for which to delete cloud resources.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the resources are deleted, query Azure. For more information, refer to Azure documentation.

</div>
