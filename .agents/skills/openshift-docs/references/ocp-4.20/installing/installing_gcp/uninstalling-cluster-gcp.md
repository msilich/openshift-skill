<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can remove a cluster that you deployed to Google Cloud.

# Removing a cluster that uses installer-provisioned infrastructure

To remove an OpenShift Container Platform cluster that uses installer-provisioned infrastructure, you can run the installation program destroy command. Use the installation files from your original deployment to uninstall the cluster from your cloud platform.

> [!NOTE]
> After uninstallation, check your cloud provider for any resources that were not removed properly, especially with user-provisioned infrastructure clusters. Some resources might exist because either the installation program did not create the resource or could not access the resource. For example, some Google Cloud resources require [IAM permissions](https://cloud.google.com/iam/docs/overview#concepts_related_to_access_management) in shared VPC host projects, or there might be unused [health checks that must be deleted](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/delete).

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

# Deleting Google Cloud resources with the Cloud Credential Operator utility

After uninstalling an OpenShift Container Platform cluster that uses short-term credentials managed outside the cluster, you can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to remove the Google Cloud resources that `ccoctl` created during installation.

<div>

<div class="title">

Prerequisites

</div>

- Extract and prepare the `ccoctl` binary.

- Uninstall an OpenShift Container Platform cluster on Google Cloud that uses short-term credentials.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

2.  Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ oc adm release extract \
      --from=$RELEASE_IMAGE \
      --credentials-requests \
      --included \
      --to=<path_to_directory_for_credentials_requests>
    ```

    where:

    `--included`
    The parameter includes only the manifests that your specific cluster configuration requires.

    `<path_to_directory_for_credentials_requests>`
    Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

3.  Delete the Google Cloud resources that `ccoctl` created by running the following command:

    ``` terminal
    $ ccoctl gcp delete \
      --name=<name> \
      --project=<gcp_project_id> \
      --credentials-requests-dir=<path_to_credentials_requests_directory> \
      --force-delete-custom-roles
    ```

    where:

    `<name>`
    Matches the name that was originally used to create and tag the cloud resources.

    `<gcp_project_id>`
    The Google Cloud project ID in which to delete cloud resources.

    `force-delete-custom-roles`
    Optional: This parameter deletes the custom roles that the `ccoctl` utility creates during installation. Google Cloud does not permanently delete custom roles immediately. For more information, see Google Cloud documentation about [deleting a custom role](https://cloud.google.com/iam/docs/creating-custom-roles#deleting-custom-role).

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the resources are deleted, query Google Cloud. For more information, refer to Google Cloud documentation.

</div>
