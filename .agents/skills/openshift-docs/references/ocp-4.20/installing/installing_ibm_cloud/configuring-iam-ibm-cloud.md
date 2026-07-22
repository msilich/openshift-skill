<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In environments where the cloud identity and access management (IAM) APIs are not reachable, you must put the Cloud Credential Operator (CCO) into manual mode before you install the cluster.

# Alternatives to storing administrator-level secrets in the kube-system project

The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). You can configure the CCO to suit the security requirements of your organization by setting different values for the `credentialsMode` parameter in the `install-config.yaml` file.

Storing an administrator-level credential secret in the cluster `kube-system` project is not supported for IBM Cloud®; therefore, you must set the `credentialsMode` parameter for the CCO to `Manual` when installing OpenShift Container Platform and manage your cloud credentials manually.

Using manual mode allows each cluster component to have only the permissions it requires, without storing an administrator-level credential in the cluster. You can also use this mode if your environment does not have connectivity to the cloud provider public IAM endpoint. However, you must manually reconcile permissions with new release images for every upgrade. You must also manually supply credentials for every component that requests them.

<div id="additional-resources_configuring-iam-ibm-cloud-about-cco">

<div class="title">

Additional resources

</div>

- [About the Cloud Credential Operator](../../authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.md#about-cloud-credential-operator)

</div>

# Configuring the Cloud Credential Operator utility

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

> [!NOTE]
> The `ccoctl` utility is a Linux binary that must run in a Linux environment.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform account with cluster administrator access.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set a variable for the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

2.  Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
    ```

    > [!NOTE]
    > Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.

3.  Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ oc image extract $CCO_IMAGE \
      --file="/usr/bin/ccoctl.<rhel_version>" \
      -a ~/.pull-secret
    ```

    For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid:

    - `rhel8`: Specify this value for hosts that use RHEL 8.

    - `rhel9`: Specify this value for hosts that use RHEL 9.

    > [!NOTE]
    > The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.

4.  Change the permissions to make `ccoctl` executable by running the following command:

    ``` terminal
    $ chmod 775 ccoctl
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:

  ``` terminal
  $ ./ccoctl
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  OpenShift credentials provisioning tool

  Usage:
    ccoctl [command]

  Available Commands:
    aws          Manage credentials objects for AWS cloud
    azure        Manage credentials objects for Azure
    gcp          Manage credentials objects for Google cloud
    help         Help about any command
    ibmcloud     Manage credentials objects for IBM Cloud
    nutanix      Manage credentials objects for Nutanix

  Flags:
    -h, --help   help for ccoctl

  Use "ccoctl [command] --help" for more information about a command.
  ```

  </div>

</div>

<div id="additional-resources_configuring-iam-ibm-cloud-refreshing-ids">

<div class="title">

Additional resources

</div>

- [Rotating API keys for IBM Cloud®](../../post_installation_configuration/changing-cloud-credentials-configuration.md#refreshing-service-ids-ibm-cloud_changing-cloud-credentials-configuration)

</div>

# Next steps

- [Installing a cluster on IBM Cloud® with customizations](installing-ibm-cloud-customizations.md#installing-ibm-cloud-customizations)

# Additional resources

- [Preparing to update a cluster with manually maintained credentials](../../updating/preparing_for_updates/preparing-manual-creds-update.md#preparing-manual-creds-update)
