<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can remove a cluster that you deployed to IBM Power® Virtual Server.

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

- You have configured the `ccoctl` binary.

- You have installed the IBM Cloud® CLI and installed or updated the VPC infrastructure service plugin. For more information see "Prerequisites" in the [IBM Cloud® CLI documentation](https://cloud.ibm.com/docs/vpc?topic=vpc-infrastructure-cli-plugin-vpc-reference&interface=ui#cli-ref-prereqs).

</div>

<div>

<div class="title">

Procedure

</div>

1.  If the following conditions are met, this step is required:

    - The installer created a resource group as part of the installation process.

    - You or one of your applications created persistent volume claims (PVCs) after the cluster was deployed.

      In which case, the PVCs are not removed when uninstalling the cluster, which might prevent the resource group from being successfully removed. To prevent a failure:

      1.  Log in to the IBM Cloud® using the CLI.

      2.  To list the PVCs, run the following command:

          ``` terminal
          $ ibmcloud is volumes --resource-group-name <infrastructure_id>
          ```

          For more information about listing volumes, see the [IBM Cloud® CLI documentation](https://cloud.ibm.com/docs/vpc?topic=vpc-infrastructure-cli-plugin-vpc-reference&interface=ui#volume-cli).

      3.  To delete the PVCs, run the following command:

          ``` terminal
          $ ibmcloud is volume-delete --force <volume_id>
          ```

          For more information about deleting volumes, see the [IBM Cloud® CLI documentation](https://cloud.ibm.com/docs/vpc?topic=vpc-infrastructure-cli-plugin-vpc-reference&interface=ui#volume-delete).

2.  Export the API key that was created as part of the installation process.

    ``` terminal
    $ export IBMCLOUD_API_KEY=<api_key>
    ```

    > [!NOTE]
    > You must set the variable name exactly as specified. The installation program expects the variable name to be present to remove the service IDs that were created when the cluster was installed.

3.  From the directory that has the installation program on the computer that you used to install the cluster, run the following command:

    ``` terminal
    $ ./openshift-install destroy cluster \
    --dir <installation_directory> --log-level info
    ```

    where:

    `<installation_directory>`
    Specify the path to the directory that you stored the installation files in.

    `--log-level info`
    To view different details, specify `warn`, `debug`, or `error` instead of `info`.

    <div class="note">

    <div class="title">

    </div>

    - You must specify the directory that has the cluster definition files for your cluster. The installation program requires the `metadata.json` file in this directory to delete the cluster.

    - You might have to run the `openshift-install destroy` command up to three times to ensure a proper cleanup.

    </div>

4.  Remove the manual CCO credentials that were created for the cluster:

    ``` terminal
    $ ccoctl ibmcloud delete-service-id \
        --credentials-requests-dir <path_to_credential_requests_directory> \
        --name <cluster_name>
    ```

    > [!NOTE]
    > If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.

5.  Optional: Delete the `<installation_directory>` directory and the OpenShift Container Platform installation program.

</div>
