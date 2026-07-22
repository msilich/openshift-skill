<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform version 4.17, you can install a customized cluster on IBM Cloud® by using installer-provisioned infrastructure with customizations, including network configuration options. In each, you modify parameters in the `install-config.yaml` file before you install the cluster.

By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations.

You must set most of the network configuration parameters during installation, and you can modify only `kubeProxy` configuration parameters in a running cluster.

# Prerequisites

- You reviewed details about the [OpenShift Container Platform installation and update](../../architecture/architecture-installation.md#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../overview/installing-preparing.md#installing-preparing).

- You [configured an IBM Cloud® account](installing-ibm-cloud-account.md#installing-ibm-cloud-account) to host the cluster.

- If you use a firewall, you [configured it to allow the sites](../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall) that your cluster requires access to.

- You configured the `ccoctl` utility before you installed the cluster. For more information, see [Configuring IAM for IBM Cloud®](configuring-iam-ibm-cloud.md#configuring-iam-ibm-cloud).

# Internet access for OpenShift Container Platform

In OpenShift Container Platform 4.17, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

- Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.

- Access Quay.io to obtain the packages that are required to install your cluster.

- Obtain the packages that are required to perform cluster updates.

> [!IMPORTANT]
> If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

# Generating a key pair for cluster node SSH access

During an OpenShift Container Platform installation, you can provide an SSH public key to the installation program. The key is passed to the Red Hat Enterprise Linux CoreOS (RHCOS) nodes through their Ignition config files and is used to authenticate SSH access to the nodes. The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication.

The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication. After the key is passed to the nodes, you can use the key pair to SSH in to the RHCOS nodes as the user `core`. To access the nodes through SSH, the private key identity must be managed by SSH for your local user.

If you want to SSH in to your cluster nodes to perform installation debugging or disaster recovery, you must provide the SSH public key during the installation process. The `./openshift-install gather` command also requires the SSH public key to be in place on the cluster nodes.

> [!IMPORTANT]
> Do not skip this procedure in production environments, where disaster recovery and debugging is required.

> [!NOTE]
> You must use a local key, not one that you configured with platform-specific approaches.

<div>

<div class="title">

Procedure

</div>

1.  If you do not have an existing SSH key pair on your local machine to use for authentication onto your cluster nodes, create one. For example, on a computer that uses a Linux operating system, run the following command:

    ``` terminal
    $ ssh-keygen -t ed25519 -N '' -f <path>/<file_name>
    ```

    Specifies the path and file name, such as `~/.ssh/id_ed25519`, of the new SSH key. If you have an existing key pair, ensure your public key is in the your `~/.ssh` directory.

    > [!NOTE]
    > If you plan to install an OpenShift Container Platform cluster that uses the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the `x86_64`, `ppc64le`, and `s390x` architectures, do not create a key that uses the `ed25519` algorithm. Instead, create a key that uses the `rsa` or `ecdsa` algorithm.

2.  View the public SSH key:

    ``` terminal
    $ cat <path>/<file_name>.pub
    ```

    For example, run the following to view the `~/.ssh/id_ed25519.pub` public key:

    ``` terminal
    $ cat ~/.ssh/id_ed25519.pub
    ```

3.  Add the SSH private key identity to the SSH agent for your local user, if it has not already been added. SSH agent management of the key is required for password-less SSH authentication onto your cluster nodes, or if you want to use the `./openshift-install gather` command.

    > [!NOTE]
    > On some distributions, default SSH private key identities such as `~/.ssh/id_rsa` and `~/.ssh/id_dsa` are managed automatically.

    1.  If the `ssh-agent` process is not already running for your local user, start it as a background task:

        ``` terminal
        $ eval "$(ssh-agent -s)"
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Agent pid 31874
        ```

        </div>

        > [!NOTE]
        > If your cluster is in FIPS mode, only use FIPS-compliant algorithms to generate the SSH key. The key must be either RSA or ECDSA.

4.  Add your SSH private key to the `ssh-agent`:

    ``` terminal
    $ ssh-add <path>/<file_name>
    ```

    Specifies the path and file name for your SSH private key, such as `~/.ssh/id_ed25519`

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Identity added: /home/<you>/<path>/<file_name> (<computer_name>)
    ```

    </div>

</div>

<div>

<div class="title">

Next steps

</div>

- When you install OpenShift Container Platform, provide the SSH public key to the installation program.

</div>

# Obtaining the installation program

Before you install OpenShift Container Platform, download the installation file on the host you are using for installation.

<div>

<div class="title">

Prerequisites

</div>

- You have a computer that runs Linux or macOS, with 500 MB of local disk space.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to the [Cluster Type](https://console.redhat.com/openshift/install) page on the Red Hat Hybrid Cloud Console. If you have a Red Hat account, log in with your credentials. If you do not, create an account.

    > [!TIP]
    > You can also [download the binaries for a specific OpenShift Container Platform release](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/).

2.  Select your infrastructure provider from the **Run it yourself** section of the page.

3.  Select your host operating system and architecture from the dropdown menus under **OpenShift Installer** and click **Download Installer**.

4.  Place the downloaded file in the directory where you want to store the installation configuration files.

    <div class="important">

    <div class="title">

    </div>

    - The installation program creates several files on the computer that you use to install your cluster. You must keep the installation program and the files that the installation program creates after you finish installing the cluster. Both of the files are required to delete the cluster.

    - Deleting the files created by the installation program does not remove your cluster, even if the cluster failed during installation. To remove your cluster, complete the OpenShift Container Platform uninstallation procedures for your specific cloud provider.

    </div>

5.  Extract the installation program. For example, on a computer that uses a Linux operating system, run the following command:

    ``` terminal
    $ tar -xvf openshift-install-linux.tar.gz
    ```

6.  Download your installation [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.

    > [!TIP]
    > Alternatively, you can retrieve the installation program from the [Red Hat Customer Portal](https://access.redhat.com/downloads/content/290/), where you can specify a version of the installation program to download. However, you must have an active subscription to access this page.

</div>

# Exporting the API key

You must set the API key you created as a global variable; the installation program ingests the variable during startup to set the API key.

<div>

<div class="title">

Prerequisites

</div>

- You have created either a user API key or service ID API key for your IBM Cloud® account.

</div>

<div>

<div class="title">

Procedure

</div>

- Export your API key for your account as a global variable:

  ``` terminal
  $ export IC_API_KEY=<api_key>
  ```

</div>

> [!IMPORTANT]
> You must set the variable name exactly as specified; the installation program expects the variable name to be present during startup.

# Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on IBM Cloud®.

<div>

<div class="title">

Prerequisites

</div>

- You have the OpenShift Container Platform installation program and the pull secret for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `install-config.yaml` file.

    1.  Change to the directory that contains the installation program and run the following command:

        ``` terminal
        $ ./openshift-install create install-config --dir <installation_directory>
        ```

        - `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

          When specifying the directory:

        - Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.

        - Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

    2.  At the prompts, provide the configuration details for your cloud:

        1.  Optional: Select an SSH key to use to access your cluster machines.

            > [!NOTE]
            > For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

        2.  Select **ibmcloud** as the platform to target.

        3.  Select the region to deploy the cluster to.

        4.  Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster.

        5.  Enter a descriptive name for your cluster.

2.  Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.

3.  Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

    > [!IMPORTANT]
    > The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installation configuration parameters for IBM Cloud®](installation-config-parameters-ibm-cloud-vpc.md#installation-config-parameters-ibm-cloud-vpc)

</div>

## Minimum resource requirements for cluster installation

Each created cluster must meet minimum requirements so that the cluster runs as expected.

| Machine | Operating System | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
|----|----|----|----|----|----|
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Minimum resource requirements

> [!NOTE]
> For OpenShift Container Platform version 4.19, RHCOS is based on RHEL version 9.6, which updates the micro-architecture requirements. The following list contains the minimum instruction set architectures (ISA) that each architecture requires:
>
> - x86-64 architecture requires x86-64-v2 ISA
>
> - ARM64 architecture requires ARMv8.0-A ISA
>
> - IBM Power architecture requires Power 9 ISA
>
> - s390x architecture requires z14 ISA
>
> For more information, see "Architectures".

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

<div>

<div class="title">

Additional resources

</div>

- [Architectures (RHEL documentation)](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.2_release_notes/index#architectures)

</div>

<div>

<div class="title">

Additional resources

</div>

- [Optimizing storage](../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

</div>

## Tested instance types for IBM Cloud

The following IBM Cloud® instance types have been tested with OpenShift Container Platform.

<div class="example">

<div class="title">

Machine series

</div>

<https://raw.githubusercontent.com/openshift/installer/release-4.20/docs/user/ibmcloud/tested_instance_types_x86_64.md>

</div>

## Sample customized install-config.yaml file for IBM Cloud

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters.

> [!IMPORTANT]
> This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and then modify it.

``` yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    ibmcloud: {}
  replicas: 3
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    ibmcloud: {}
  replicas: 3
metadata:
  name: test-cluster
networking:
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
  ibmcloud:
    region: us-south
credentialsMode: Manual
publish: External
pullSecret: '{"auths": ...}'
fips: false
sshKey: ssh-ed25519 AAAA...
```

- Required. The installation program prompts you for this value.

- If you do not provide these parameters and values, the installation program provides the default value.

- The `controlPlane` section is a single mapping, but the `compute` section is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`, and the first line of the `controlPlane` section must not. Only one control plane pool is used.

- Enables or disables simultaneous multithreading, also known as Hyper-Threading. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

  > [!IMPORTANT]
  > If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance. Use larger machine types, such as `n1-standard-8`, for your machines if you disable simultaneous multithreading.

- The cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

- Enables or disables FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead.

  > [!IMPORTANT]
  > To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Installing the system in FIPS mode](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/security_hardening/assembly_installing-the-system-in-fips-mode_security-hardening).
  >
  > When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures.

- Optional: provide the `sshKey` value that you use to access the machines in your cluster.

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

# Manually creating IAM

Installing the cluster requires that the Cloud Credential Operator (CCO) operate in manual mode. While the installation program configures the CCO for manual mode, you must specify the identity and access management secrets for you cloud provider.

You can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to create the required IBM Cloud® resources.

<div>

<div class="title">

Prerequisites

</div>

- You have configured the `ccoctl` binary.

- You have an existing `install-config.yaml` file.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `install-config.yaml` configuration file so that the file includes the `credentialsMode` parameter set to `Manual`.

    <div class="formalpara">

    <div class="title">

    Example `install-config.yaml` configuration file

    </div>

    ``` yaml
    apiVersion: v1
    baseDomain: cluster1.example.com
    credentialsMode: Manual
    compute:
    - architecture: amd64
      hyperthreading: Enabled
    ```

    </div>

    - `credentialsMode`: Set the `credentialsMode` parameter to `Manual`.

2.  To generate the manifests, run the following command from the directory that includes the installation program:

    ``` terminal
    $ ./openshift-install create manifests --dir <installation_directory>
    ```

3.  From the directory that includes the installation program, set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

4.  Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

    ``` terminal
    $ oc adm release extract \
      --from=$RELEASE_IMAGE \
      --credentials-requests \
      --included \
      --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
      --to=<path_to_directory_for_credentials_requests>
    ```

    - `--included`: Includes only the manifests that your specific cluster configuration requires.

    - `<path_to_directory_with_installation_configuration>`: Specify the location of the `install-config.yaml` file.

    - `<path_to_directory_for_credentials_requests>`: Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

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
          name: openshift-image-registry-ibmcos
          namespace: openshift-cloud-credential-operator
        spec:
          secretRef:
            name: installer-cloud-credentials
            namespace: openshift-image-registry
          providerSpec:
            apiVersion: cloudcredential.openshift.io/v1
            kind: IBMCloudProviderSpec
            policies:
            - attributes:
              - name: serviceName
                value: cloud-object-storage
              roles:
              - crn:v1:bluemix:public:iam::::role:Viewer
              - crn:v1:bluemix:public:iam::::role:Operator
              - crn:v1:bluemix:public:iam::::role:Editor
              - crn:v1:bluemix:public:iam::::serviceRole:Reader
              - crn:v1:bluemix:public:iam::::serviceRole:Writer
            - attributes:
              - name: resourceType
                value: resource-group
              roles:
              - crn:v1:bluemix:public:iam::::role:Viewer
      ```

      </div>

5.  Create the service ID for each credential request, assign the policies defined, create an API key, and generate the secret:

    ``` terminal
    $ ccoctl ibmcloud create-service-id \
      --credentials-requests-dir=<path_to_credential_requests_directory> \
      --name=<cluster_name> \
      --output-dir=<installation_directory> \
      --resource-group-name=<resource_group_name>
    ```

    - `<path_to_credential_requests_directory>`: Specify the directory containing the files for the `CredentialsRequest` objects.

    - `<cluster_name>`: Specify the name of the OpenShift Container Platform cluster.

    - `<installation_directory>`: Optional parameter. Specify the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which you run the commands.

    - `<resource_group_name>`: Optional parameter. Specify the name of the resource group used for scoping the access policies.

      > [!NOTE]
      > If you enabled Technology Preview features by using the `TechPreviewNoUpgrade` feature set for your cluster, you must include the `--enable-tech-preview` parameter in the configuration for the `CredentialsRequest` object.
      >
      > If you provided a wrong resource group name, the installation fails during the bootstrap phase. To find the correct resource group name, run the following command:
      >
      > ``` terminal
      > $ grep resourceGroupName <installation_directory>/manifests/cluster-infrastructure-02-config.yml
      > ```

</div>

<div>

<div class="title">

Verification

</div>

- Check that the appropriate secrets exist in the `manifests` directory of your cluster.

</div>

# Network configuration phases

There are two phases prior to OpenShift Container Platform installation where you can customize the network configuration. Customize settings in the `install-config.yaml` file and in the Cluster Network Operator manifest across two configuration phases.

Phase 1
You can customize the following network-related fields in the `install-config.yaml` file before you create the manifest files:

- `networking.networkType`

- `networking.clusterNetwork`

- `networking.serviceNetwork`

- `networking.machineNetwork`

- `nodeNetworking`

  For more information, see "Installation configuration parameters".

  > [!NOTE]
  > Set the `networking.machineNetwork` to match the Classless Inter-Domain Routing (CIDR) where the preferred subnet is located.

  > [!IMPORTANT]
  > The CIDR range `172.17.0.0/16` is reserved by `libVirt`. You cannot use any other CIDR range that overlaps with the `172.17.0.0/16` CIDR range for networks in your cluster.

Phase 2
After creating the manifest files by running `openshift-install create manifests`, you can define a customized Cluster Network Operator manifest with only the fields you want to modify. You can use the manifest to specify an advanced network configuration.

During phase 2, you cannot override the values that you specified in phase 1 in the `install-config.yaml` file. However, you can customize the network plugin during phase 2.

# Specifying advanced network configuration

To integrate your OpenShift Container Platform cluster with your existing network environment, you can specify advanced network configuration in a manifest before you install the cluster. Advanced network configuration can be configured only during cluster installation.

> [!IMPORTANT]
> Customizing your network configuration by modifying the OpenShift Container Platform manifest files created by the installation program is not supported. Applying a manifest file that you create, as in the following procedure, is supported.

<div>

<div class="title">

Prerequisites

</div>

- You have created the `install-config.yaml` file and completed any modifications to it.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Change to the directory that contains the installation program and create the manifests:

    ``` terminal
    $ ./openshift-install create manifests --dir <installation_directory>
    ```

    The `<installation_directory>` specifies the name of the directory that contains the `install-config.yaml` file for your cluster.

2.  Create a stub manifest file for the advanced network configuration that is named `cluster-network-03-config.yml` in the `<installation_directory>/manifests/` directory:

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: Network
    metadata:
      name: cluster
    spec:
    ```

3.  Specify the advanced network configuration for your cluster in the `cluster-network-03-config.yml` file, such as in the following example:

    <div class="formalpara">

    <div class="title">

    Enable IPsec for the OVN-Kubernetes network provider

    </div>

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: Network
    metadata:
      name: cluster
    spec:
      defaultNetwork:
        ovnKubernetesConfig:
          ipsecConfig:
            mode: Full
    ```

    </div>

4.  Optional: Back up the `manifests/cluster-network-03-config.yml` file. The installation program consumes the `manifests/` directory when you create the Ignition config files.

5.  Remove the Kubernetes manifest files that define the control plane machines and compute `MachineSets`:

    ``` terminal
    $ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml
    ```

    Because you create and manage these resources yourself, you do not have to initialize them.

    - You can preserve the `MachineSet` files to create compute machines by using the machine API, but you must update references to them to match your environment.

</div>

# Cluster Network Operator configuration

To manage cluster networking, configure the Cluster Network Operator (CNO) `Network` custom resource (CR) named `cluster` so the cluster uses the correct IP ranges and network plugin settings for reliable pod and service connectivity. Some settings and fields are inherited at the time of install or by the `default.Network.type` plugin, OVN-Kubernetes.

The CNO configuration inherits the following fields during cluster installation from the `Network` API in the `Network.config.openshift.io` API group:

`clusterNetwork`
IP address pools from which pod IP addresses are allocated.

`serviceNetwork`
IP address pool for services.

`defaultNetwork.type`
Cluster network plugin. `OVNKubernetes` is the only supported plugin during installation.

You can specify the cluster network plugin configuration for your cluster by setting the fields for the `defaultNetwork` object in the CNO object named `cluster`.

## Cluster Network Operator configuration object

The fields for the Cluster Network Operator (CNO) are described in the following table:

<table>
<caption>Cluster Network Operator configuration object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>metadata.name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the CNO object. This name is always <code>cluster</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.clusterNetwork</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>A list specifying the blocks of IP addresses from which pod IP addresses are allocated and the subnet prefix length assigned to each individual node in the cluster. For example:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">spec</span><span class="kw">:</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">clusterNetwork</span><span class="kw">:</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> </span><span class="fu">cidr</span><span class="kw">:</span><span class="at"> 10.128.0.0/19</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">hostPrefix</span><span class="kw">:</span><span class="at"> </span><span class="dv">23</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> </span><span class="fu">cidr</span><span class="kw">:</span><span class="at"> 10.128.32.0/19</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">hostPrefix</span><span class="kw">:</span><span class="at"> </span><span class="dv">23</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.serviceNetwork</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>A block of IP addresses for services. The OVN-Kubernetes network plugin supports only a single IP address block for the service network. For example:</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">spec</span><span class="kw">:</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">serviceNetwork</span><span class="kw">:</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> 172.30.0.0/14</span></span></code></pre></div>
<p>You can customize this field only in the <code>install-config.yaml</code> file before you create the manifests. The value is read-only in the manifest file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.defaultNetwork</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Configures the network plugin for the cluster network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.additionalRoutingCapabilities.providers</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>This setting enables a dynamic routing provider. The FRR routing capability provider is required for the route advertisement feature. The only supported value is <code>FRR</code>.</p>
<ul>
<li><p><code>FRR</code>: The FRR routing provider</p></li>
</ul>
<div class="sourceCode" id="cb3"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="fu">spec</span><span class="kw">:</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">additionalRoutingCapabilities</span><span class="kw">:</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">providers</span><span class="kw">:</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="kw">-</span><span class="at"> FRR</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

> [!IMPORTANT]
> For a cluster that needs to deploy objects across multiple networks, ensure that you specify the same value for the `clusterNetwork.hostPrefix` parameter for each network type that is defined in the `install-config.yaml` file. Setting a different value for each `clusterNetwork.hostPrefix` parameter can impact the OVN-Kubernetes network plugin, where the plugin cannot effectively route object traffic among different nodes.

## defaultNetwork object configuration

The values for the `defaultNetwork` object are defined in the following table:

<table>
<caption><code>defaultNetwork</code> object</caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 20%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p><code>OVNKubernetes</code>. The Red Hat OpenShift Networking network plugin is selected during installation. This value cannot be changed after cluster installation.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>OpenShift Container Platform uses the OVN-Kubernetes network plugin by default.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ovnKubernetesConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>This object is only valid for the OVN-Kubernetes network plugin.</p></td>
</tr>
</tbody>
</table>

## Configuration for the OVN-Kubernetes network plugin

The following table describes the configuration fields for the OVN-Kubernetes network plugin:

<table>
<caption><code>ovnKubernetesConfig</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mtu</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The maximum transmission unit (MTU) for the Geneve (Generic Network Virtualization Encapsulation) overlay network. This is detected automatically based on the MTU of the primary network interface. You do not normally need to override the detected MTU.</p>
<p>If the auto-detected value is not what you expect it to be, confirm that the MTU on the primary network interface on your nodes is correct. You cannot use this option to change the MTU value of the primary network interface on the nodes.</p>
<p>If your cluster requires different MTU values for different nodes, you must set this value to <code>100</code> less than the lowest MTU value in your cluster. For example, if some nodes in your cluster have an MTU of <code>9001</code>, and some have an MTU of <code>1500</code>, you must set this value to <code>1400</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>genevePort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The port to use for all Geneve packets. The default value is <code>6081</code>. This value cannot be changed after cluster installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipsecConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specify a configuration object for customizing the IPsec configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipv4</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specifies a configuration object for IPv4 settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipv6</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specifies a configuration object for IPv6 settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>policyAuditConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Specify a configuration object for customizing network policy audit logging. If unset, the defaults audit log settings are used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>routeAdvertisements</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies whether to advertise cluster network routes. The default value is <code>Disabled</code>.</p>
<ul>
<li><p><code>Enabled</code>: Import routes to the cluster network and advertise cluster network routes as configured in <code>RouteAdvertisements</code> objects.</p></li>
<li><p><code>Disabled</code>: Do not import routes to the cluster network or advertise cluster network routes.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gatewayConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional: Specify a configuration object for customizing how egress traffic is sent to the node gateway. Valid values are <code>Shared</code> and <code>Local</code>. The default value is <code>Shared</code>. In the default setting, the Open vSwitch (OVS) outputs traffic directly to the node IP interface. In the <code>Local</code> setting, it traverses the host network; consequently, it gets applied to the routing table of the host.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>While migrating egress traffic, you can expect some disruption to workloads and service traffic until the Cluster Network Operator (CNO) successfully rolls out the changes.</p>
</div></td>
</tr>
</tbody>
</table>

<table>
<caption><code>ovnKubernetesConfig.ipv4</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>internalTransitSwitchSubnet</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>If your existing network infrastructure overlaps with the <code>100.88.0.0/16</code> IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.</p>
<p>The default value is <code>100.88.0.0/16</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>internalJoinSubnet</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>If your existing network infrastructure overlaps with the <code>100.64.0.0/16</code> IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster. For example, if the <code>clusterNetwork.cidr</code> value is <code>10.128.0.0/14</code> and the <code>clusterNetwork.hostPrefix</code> value is <code>/23</code>, then the maximum number of nodes is <code>2^(23-14)=512</code>.</p>
<p>The default value is <code>100.64.0.0/16</code>.</p></td>
</tr>
</tbody>
</table>

<table>
<caption><code>ovnKubernetesConfig.ipv6</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>internalTransitSwitchSubnet</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>If your existing network infrastructure overlaps with the <code>fd97::/64</code> IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.</p>
<p>The default value is <code>fd97::/64</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>internalJoinSubnet</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>If your existing network infrastructure overlaps with the <code>fd98::/64</code> IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster.</p>
<p>The default value is <code>fd98::/64</code>.</p></td>
</tr>
</tbody>
</table>

<table>
<caption><code>policyAuditConfig</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>rateLimit</code></p></td>
<td style="text-align: left;"><p>integer</p></td>
<td style="text-align: left;"><p>The maximum number of messages to generate every second per node. The default value is <code>20</code> messages per second.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxFileSize</code></p></td>
<td style="text-align: left;"><p>integer</p></td>
<td style="text-align: left;"><p>The maximum size for the audit log in bytes. The default value is <code>50000000</code> or 50 MB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxLogFiles</code></p></td>
<td style="text-align: left;"><p>integer</p></td>
<td style="text-align: left;"><p>The maximum number of log files that are retained.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>destination</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>One of the following additional audit log targets:</p>
<dl>
<dt><code>libc</code></dt>
<dd>
<p>The libc <code>syslog()</code> function of the journald process on the host.</p>
</dd>
<dt><code>udp:&lt;host&gt;:&lt;port&gt;</code></dt>
<dd>
<p>A syslog server. Replace <code>&lt;host&gt;:&lt;port&gt;</code> with the host and port of the syslog server.</p>
</dd>
<dt><code>unix:&lt;file&gt;</code></dt>
<dd>
<p>A Unix Domain Socket file specified by <code>&lt;file&gt;</code>.</p>
</dd>
<dt><code>null</code></dt>
<dd>
<p>Do not send the audit logs to any additional target.</p>
</dd>
</dl></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>syslogFacility</code></p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>The syslog facility, such as <code>kern</code>, as defined by RFC5424. The default value is <code>local0</code>.</p></td>
</tr>
</tbody>
</table>

<table id="gatewayConfig-object_installing-ibm-cloud-customizations">
<caption><code>gatewayConfig</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>routingViaHost</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Set this field to <code>true</code> to send egress traffic from pods to the host networking stack. For highly-specialized installations and applications that rely on manually configured routes in the kernel routing table, you might want to route egress traffic to the host networking stack. By default, egress traffic is processed in OVN to exit the cluster and is not affected by specialized routes in the kernel routing table. The default value is <code>false</code>.</p>
<p>This field has an interaction with the Open vSwitch hardware offloading feature. If you set this field to <code>true</code>, you do not receive the performance benefits of the offloading because egress traffic is processed by the host networking stack.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipForwarding</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>You can control IP forwarding for all traffic on OVN-Kubernetes managed interfaces by using the <code>ipForwarding</code> specification in the <code>Network</code> resource. Specify <code>Restricted</code> to only allow IP forwarding for Kubernetes related traffic. Specify <code>Global</code> to allow forwarding of all IP traffic. For new installations, the default is <code>Restricted</code>. For updates to OpenShift Container Platform 4.14 or later, the default is <code>Global</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>The default value of <code>Restricted</code> sets the IP forwarding to drop.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipv4</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv4 addresses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ipv6</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv6 addresses.</p></td>
</tr>
</tbody>
</table>

<table id="gatewayconfig-ipv4-object_installing-ibm-cloud-customizations">
<caption><code>gatewayConfig.ipv4</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>internalMasqueradeSubnet</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The masquerade IPv4 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is <code>169.254.169.0/29</code>.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>For OpenShift Container Platform 4.17 and later versions, clusters use <code>169.254.0.0/17</code> as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.</p>
</div></td>
</tr>
</tbody>
</table>

<table id="gatewayconfig-ipv6-object_installing-ibm-cloud-customizations">
<caption><code>gatewayConfig.ipv6</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>internalMasqueradeSubnet</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The masquerade IPv6 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is <code>fd69::/125</code>.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>For OpenShift Container Platform 4.17 and later versions, clusters use <code>fd69::/112</code> as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.</p>
</div></td>
</tr>
</tbody>
</table>

<table id="nw-operator-cr-ipsec_installing-ibm-cloud-customizations">
<caption><code>ipsecConfig</code> object</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the behavior of the IPsec implementation. Must be one of the following values:</p>
<ul>
<li><p><code>Disabled</code>: IPsec is not enabled on cluster nodes.</p></li>
<li><p><code>External</code>: IPsec is enabled for network traffic with external hosts.</p></li>
<li><p><code>Full</code>: IPsec is enabled for pod traffic and network traffic with external hosts.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<div class="formalpara">

<div class="title">

Example OVN-Kubernetes configuration with IPSec enabled

</div>

``` yaml
defaultNetwork:
  type: OVNKubernetes
  ovnKubernetesConfig:
    mtu: 1400
    genevePort: 6081
    ipsecConfig:
      mode: Full
```

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

# Installing the OpenShift CLI on Linux

To manage your cluster and deploy applications from the command line on Linux, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the architecture from the **Product Variant** list.

3.  Select the appropriate version from the **Version** list.

4.  Click **Download Now** next to the **OpenShift v4.17 Linux Clients** entry and save the file.

5.  Unpack the archive:

    ``` terminal
    $ tar xvf <file>
    ```

6.  Place the `oc` binary in a directory that is on your `PATH`.

    To check your `PATH`, execute the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- After you install the OpenShift CLI, it is available using the `oc` command:

  ``` terminal
  $ oc <command>
  ```

</div>

# Installing the OpenShift CLI on Windows

To manage your cluster and deploy applications from the command line on Windows, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the appropriate version from the **Version** list.

3.  Click **Download Now** next to the **OpenShift v4.17 Windows Client** entry and save the file.

4.  Extract the archive with a ZIP program.

5.  Move the `oc` binary to a directory that is on your `PATH` variable.

    To check your `PATH` variable, open the command prompt and execute the following command:

    ``` terminal
    C:\> path
    ```

</div>

<div>

<div class="title">

Verification

</div>

- After you install the OpenShift CLI, it is available using the `oc` command:

  ``` terminal
  C:\> oc <command>
  ```

</div>

# Installing the OpenShift CLI on macOS

To manage your cluster and deploy applications from the command line on macOS, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

> [!IMPORTANT]
> If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.
>
> Download and install the new version of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.

2.  Select the architecture from the **Product Variant** list.

3.  Select the appropriate version from the **Version** list.

4.  Click **Download Now** next to the **OpenShift v4.17 macOS Clients** entry and save the file.

    > [!NOTE]
    > For macOS arm64, choose the **OpenShift v4.17 macOS arm64 Client** entry.

5.  Unpack and unzip the archive.

6.  Move the `oc` binary to a directory on your `PATH` variable.

    To check your `PATH` variable, open a terminal and execute the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify your installation by using an `oc` command:

  ``` terminal
  $ oc <command>
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

<div id="additional-resources_installing-ibm-cloud-customizations-console">

<div class="title">

Additional resources

</div>

- [Accessing the web console](../../web_console/web-console.md#web-console)

</div>

# Telemetry access for OpenShift Container Platform

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

<div id="additional-resources_installing-ibm-cloud-customizations-telemetry">

<div class="title">

Additional resources

</div>

- [About remote health monitoring](../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring)

</div>

# Next steps

- [Customize your cluster](../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations).

- If necessary, you can [Remote health reporting](../../support/remote_health_monitoring/remote-health-reporting.md#remote-health-reporting).
