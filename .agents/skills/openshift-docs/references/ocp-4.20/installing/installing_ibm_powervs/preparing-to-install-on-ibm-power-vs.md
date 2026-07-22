<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can install OpenShift Container Platform on IBM Power® Virtual Server using installer-provisioned infrastructure. This process involves using an installation program to provision the underlying infrastructure for your cluster. Installing OpenShift Container Platform on IBM Power® Virtual Server using user-provisioned infrastructure is not supported at this time.

See [Installation process](../../architecture/architecture-installation.md#installation-process_architecture-installation) for more information about installer-provisioned installation processes.

# Installing a cluster on installer-provisioned infrastructure

You can install a cluster on IBM Power® Virtual Server infrastructure that is provisioned by the OpenShift Container Platform installation program by using one of the following methods:

- **[Installing a customized cluster on IBM Power® Virtual Server](installing-ibm-power-vs-customizations.md#installing-ibm-power-vs-customizations)**: You can install a customized cluster on IBM Power® Virtual Server infrastructure that the installation program provisions. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available [post-installation](../../post_installation_configuration/cluster-tasks.md#post-install-cluster-tasks).

- **[Installing a cluster on IBM Power® Virtual Server into an existing VPC](installing-ibm-powervs-vpc.md#installing-ibm-powervs-vpc)**: You can install OpenShift Container Platform on IBM Power® Virtual Server into an existing Virtual Private Cloud (VPC). You can use this installation method if you have constraints set by the guidelines of your company, such as limits when creating new accounts or infrastructure.

- **[Installing a private cluster on IBM Power® Virtual Server](installing-ibm-power-vs-private-cluster.md#installing-ibm-power-vs-private-cluster)**: You can install a private cluster on IBM Power® Virtual Server. You can use this method to deploy OpenShift Container Platform on an internal network that is not visible to the internet.

- **[Installing a cluster on IBM Power® Virtual Server in a restricted network](installing-restricted-networks-ibm-power-vs.md#installing-restricted-networks-ibm-power-vs)**: You can install OpenShift Container Platform on IBM Power® Virtual Server on installer-provisioned infrastructure by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components.

# Configuring the Cloud Credential Operator utility

The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on IBM Power® Virtual Server, you must set the CCO to `manual` mode as part of the installation process.

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

<div id="additional-resources_configuring-ibm-cloud-refreshing-ids">

<div class="title">

Additional resources

</div>

- [Rotating API keys](../../post_installation_configuration/changing-cloud-credentials-configuration.md#refreshing-service-ids-ibm-cloud_changing-cloud-credentials-configuration)

</div>

# Next steps

- [Configuring an IBM Cloud® account](installing-ibm-cloud-account-power-vs.md#installing-ibm-cloud-account-power-vs)
