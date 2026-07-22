<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform version 4.17, you can install a cluster on Microsoft Azure Stack Hub with an installer-provisioned infrastructure. However, you must manually configure the `install-config.yaml` file to specify values that are specific to Azure Stack Hub.

> [!NOTE]
> While you can select `azure` when using the installation program to deploy a cluster using installer-provisioned infrastructure, this option is only supported for the Azure Public Cloud.

# Prerequisites

- You reviewed details about the [OpenShift Container Platform installation and update](../../../architecture/architecture-installation.md#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../../overview/installing-preparing.md#installing-preparing).

- You have installed Azure Stack Hub version 2008 or later.

- You [configured an Azure Stack Hub account](../installing-azure-stack-hub-account.md#installing-azure-stack-hub-account) to host the cluster.

- If you use a firewall, you [configured it to allow the sites](../../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall) that your cluster requires access to.

- You verified that you have approximately 16 GB of local disk space. Installing the cluster requires that you download the RHCOS virtual hard drive (VHD) cluster image and upload it to your Azure Stack Hub environment so that it is accessible during deployment. Decompressing the VHD files requires this amount of local disk space.

# Uploading the RHCOS cluster image

You must download the RHCOS virtual hard disk (VHD) cluster image and upload it to your Azure Stack Hub environment so that it is accessible during deployment.

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

1.  Obtain the RHCOS VHD cluster image:

    1.  Export the URL of the RHCOS VHD to an environment variable.

        ``` terminal
        $ export COMPRESSED_VHD_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.artifacts.azurestack.formats."vhd.gz".disk.location')
        ```

    2.  Download the compressed RHCOS VHD file locally.

        ``` terminal
        $ curl -O -L ${COMPRESSED_VHD_URL}
        ```

2.  Decompress the VHD file.

    > [!NOTE]
    > The decompressed VHD file is approximately 16 GB, so be sure that your host system has 16 GB of free space available. The VHD file can be deleted once you have uploaded it.

3.  Upload the local VHD to the Azure Stack Hub environment, making sure that the blob is publicly available. For example, you can upload the VHD to a blob using the `az` cli or the web portal.

</div>

# Manually creating the installation configuration file

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

    Make the following modifications:

    1.  Specify the required installation parameters.

    2.  Update the `platform.azure` section to specify the parameters that are specific to Azure Stack Hub.

    3.  Optional: Update one or more of the default configuration parameters to customize the installation.

        For more information about the parameters, see "Installation configuration parameters".

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
credentialsMode: Manual
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
  replicas: 3
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
    clusterOSimage: https://vhdsa.blob.example.example.com/vhd/rhcos-410.84.202112040202-0-azurestack.x86_64.vhd
pullSecret: '{"auths": ...}'
fips: false
sshKey: ssh-ed25519 AAAA...
additionalTrustBundle: |
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
```

- Required.

- If you do not provide these parameters and values, the installation program provides the default value.

- The `controlPlane` section is a single mapping, but the `compute` section is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`, and the first line of the `controlPlane` section must not. Although both sections currently define a single machine pool, it is possible that future versions of OpenShift Container Platform will support defining multiple compute pools during installation. Only one control plane pool is used.

- You can specify the size of the disk to use in GB. Minimum recommendation for control plane nodes is 1024 GB.

- The name of the cluster.

- The cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

- The Azure Resource Manager endpoint that your Azure Stack Hub operator provides.

- The name of the resource group that contains the DNS zone for your base domain.

- The name of your Azure Stack Hub local region.

- The name of an existing resource group to install your cluster to. If undefined, a new resource group is created for the cluster.

- The URL of a storage blob in the Azure Stack environment that contains an RHCOS VHD.

- The pull secret required to authenticate your cluster.

- Whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead.

  > [!IMPORTANT]
  > When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.

- You can optionally provide the `sshKey` value that you use to access the machines in your cluster.

  > [!NOTE]
  > For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

- If the Azure Stack Hub environment is using an internal Certificate Authority (CA), adding the CA certificate is required.

# Manually manage cloud credentials

The Cloud Credential Operator (CCO) only supports your cloud provider in manual mode. As a result, you must specify the identity and access management (IAM) secrets for your cloud provider.

<div>

<div class="title">

Procedure

</div>

1.  If you have not previously created installation manifest files, do so by running the following command:

    ``` terminal
    $ openshift-install create manifests --dir <installation_directory>
    ```

    where `<installation_directory>` is the directory in which the installation program creates files.

2.  Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

3.  Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ oc adm release extract \
      --from=$RELEASE_IMAGE \
      --credentials-requests \
      --included \
      --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
      --to=<path_to_directory_for_credentials_requests>
    ```

    where:

    `--included`
    Specifies only the manifests that your specific cluster configuration requires.

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
      name: <component_credentials_request>
      namespace: openshift-cloud-credential-operator
      ...
    spec:
      providerSpec:
        apiVersion: cloudcredential.openshift.io/v1
        kind: AzureProviderSpec
        roleBindings:
        - role: Contributor
      ...
    ```

    </div>

4.  Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.

    <div class="formalpara">

    <div class="title">

    Sample `CredentialsRequest` object with secrets

    </div>

    ``` yaml
    apiVersion: cloudcredential.openshift.io/v1
    kind: CredentialsRequest
    metadata:
      name: <component_credentials_request>
      namespace: openshift-cloud-credential-operator
      ...
    spec:
      providerSpec:
        apiVersion: cloudcredential.openshift.io/v1
        kind: AzureProviderSpec
        roleBindings:
        - role: Contributor
          ...
      secretRef:
        name: <component_secret>
        namespace: <component_namespace>
      ...
    ```

    </div>

    <div class="formalpara">

    <div class="title">

    Sample `Secret` object

    </div>

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: <component_secret>
      namespace: <component_namespace>
    data:
      azure_subscription_id: <base64_encoded_azure_subscription_id>
      azure_client_id: <base64_encoded_azure_client_id>
      azure_client_secret: <base64_encoded_azure_client_secret>
      azure_tenant_id: <base64_encoded_azure_tenant_id>
      azure_resource_prefix: <base64_encoded_azure_resource_prefix>
      azure_resourcegroup: <base64_encoded_azure_resourcegroup>
      azure_region: <base64_encoded_azure_region>
    ```

    </div>

    > [!IMPORTANT]
    > Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.

</div>

<div id="additional-resources_installing-azure-stack-hub-default-cco">

<div class="title">

Additional resources

</div>

- [Updating cloud provider resources with manually maintained credentials](../../../updating/preparing_for_updates/preparing-manual-creds-update.md#manually-maintained-credentials-upgrade_preparing-manual-creds-update)

</div>

# Configuring the cluster to use an internal CA

If the Azure Stack Hub environment is using an internal Certificate Authority (CA), update the `cluster-proxy-01-config.yaml file` to configure the cluster to use the internal CA.

<div>

<div class="title">

Prerequisites

</div>

- Create the `install-config.yaml` file and specify the certificate trust bundle in `.pem` format.

- Create the cluster manifests.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the directory in which the installation program creates files, go to the `manifests` directory.

2.  Add `user-ca-bundle` to the `spec.trustedCA.name` field.

    <div class="formalpara">

    <div class="title">

    Example `cluster-proxy-01-config.yaml` file

    </div>

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Proxy
    metadata:
      creationTimestamp: null
      name: cluster
    spec:
      trustedCA:
        name: user-ca-bundle
    status: {}
    ```

    </div>

3.  Optional: Back up the `manifests/ cluster-proxy-01-config.yaml` file. The installation program consumes the `manifests/` directory when you deploy the cluster.

</div>

# Deploying the cluster

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

> [!IMPORTANT]
> You can run the `create cluster` command of the installation program only once, during initial installation.

<div>

<div class="title">

Prerequisites

</div>

- You have configured an account with the cloud platform that hosts your cluster.

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

- You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

</div>

<div>

<div class="title">

Procedure

</div>

- In the directory that contains the installation program, initialize the cluster deployment by running the following command:

  ``` terminal
  $ ./openshift-install create cluster --dir <installation_directory> \
      --log-level=info
  ```

  - For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.

  - To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

When the cluster deployment completes successfully:

</div>

- The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.

- Credential information also outputs to `<installation_directory>/.openshift_install.log`.

  > [!IMPORTANT]
  > Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  ...
  INFO Install complete!
  INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
  INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
  INFO Login to the console with user: "kubeadmin", and password: "password"
  INFO Time elapsed: 36m22s
  ```

  </div>

  <div class="important">

  <div class="title">

  </div>

  - The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.

  - It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

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

# Logging in to the cluster by using the web console

The `kubeadmin` user exists by default after an OpenShift Container Platform installation. You can log in to your cluster as the `kubeadmin` user by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the installation host.

- You completed a cluster installation and all cluster Operators are available.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Obtain the password for the `kubeadmin` user from the `kubeadmin-password` file on the installation host:

    ``` terminal
    $ cat <installation_directory>/auth/kubeadmin-password
    ```

    > [!NOTE]
    > Alternatively, you can obtain the `kubeadmin` password from the `<installation_directory>/.openshift_install.log` log file on the installation host.

2.  List the OpenShift Container Platform web console route:

    ``` terminal
    $ oc get routes -n openshift-console | grep 'console-openshift'
    ```

    > [!NOTE]
    > Alternatively, you can obtain the OpenShift Container Platform route from the `<installation_directory>/.openshift_install.log` log file on the installation host.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    console     console-openshift-console.apps.<cluster_name>.<base_domain>            console     https   reencrypt/Redirect   None
    ```

    </div>

3.  Navigate to the route detailed in the output of the preceding command in a web browser and log in as the `kubeadmin` user.

</div>

<div id="additional-resources_installing-azure-stack-hub-default-console">

<div class="title">

Additional resources

</div>

- [Accessing the web console](../../../web_console/web-console.md#web-console)

</div>

# Next steps

- [Validating an installation](../../validation_and_troubleshooting/validating-an-installation.md#validating-an-installation)

- [Customize your cluster](../../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations)

- Optional: [Remote health reporting](../../../support/remote_health_monitoring/remote-health-reporting.md#remote-health-reporting)

- Optional: [Remove cloud provider credentials](../../../post_installation_configuration/changing-cloud-credentials-configuration.md#manually-removing-cloud-creds_changing-cloud-credentials-configuration)
