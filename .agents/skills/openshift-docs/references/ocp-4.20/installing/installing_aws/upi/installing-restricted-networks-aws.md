<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform version 4.20, you can install a cluster on Amazon Web Services (AWS) using infrastructure that you provide and an internal mirror of the installation release content.

> [!IMPORTANT]
> While you can install an OpenShift Container Platform cluster by using mirrored installation release content, your cluster still requires internet access to use the AWS APIs.

One way to create this infrastructure is to use the provided CloudFormation templates. You can change the templates to customize your infrastructure or use the information that they contain to create AWS objects according to your company’s policies.

> [!IMPORTANT]
> The steps for performing a user-provisioned infrastructure installation are an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several CloudFormation templates help you complete these steps or model your own. You are also free to create the required resources through other methods; the templates are just an example.

# Prerequisites

Before you install OpenShift Container Platform on Amazon Web Services (AWS) in a restricted network, ensure that you have prepared your user-provisioned infrastructure, configured mirror registries for disconnected installation, and met all account and networking requirements.

The following list outlines the prerequisites to complete:

- You reviewed details about the OpenShift Container Platform installation and update processes.

- You read the documentation on selecting a cluster installation method and preparing it for users.

- You created a mirror registry on your mirror host and obtained the `imageContentSources` data for your version of OpenShift Container Platform.

  > [!IMPORTANT]
  > Because the installation media is on the mirror host, you can use that computer to complete all installation steps.

- You configured an AWS account to host the cluster.

  > [!IMPORTANT]
  > If you have an AWS profile stored on your computer, it must not use a temporary session token that you generated while using a multi-factor authentication device. The cluster continues to use your current AWS credentials to create AWS resources for the entire life of the cluster, so you must use key-based, long-term credentials. You must generate appropriate keys. You can supply the keys when you run the installation program.

- You prepared the user-provisioned infrastructure.

- You downloaded the AWS CLI and installed it on your computer.

- If you use a firewall and plan to use the Telemetry service, you configured the firewall to allow the sites that your cluster requires access to.

  > [!NOTE]
  > Be sure to also review this site list if you are configuring a proxy.

- If the cloud identity and access management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, you can manually create and maintain long-term credentials.

<div>

<div class="title">

Additional resources

</div>

- [Installation and update](../../../architecture/architecture-installation.md#architecture-installation)

- [Selecting a cluster installation method and preparing it for users](../../overview/installing-preparing.md#installing-preparing)

- [Mirroring images for a disconnected installation](../../../disconnected/installing-mirroring-installation-images.md#installing-mirroring-installation-images)

- [Configuring an AWS account](../installing-aws-account.md#installing-aws-account)

- [Managing access keys for IAM users (AWS documentation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)

- [Requirements for a cluster with user-provisioned infrastructure on AWS](upi-aws-installation-reqs.md#upi-aws-installation-reqs)

- [Install the AWS CLI Using the Bundled Installer (Linux, macOS, or UNIX) (AWS documentation)](https://docs.aws.amazon.com/cli/latest/userguide/install-bundle.html)

- [Configuring your firewall](../../install_config/configuring-firewall.md#configuring-firewall)

- [Manually creating long-term credentials](../ipi/installing-aws-customizations.md#manually-create-iam_installing-aws-customizations)

</div>

# About installations in restricted networks

You can install OpenShift Container Platform 4.20 in a restricted network without an active internet connection to obtain software components. Restricted network installations can use installer-provisioned or user-provisioned infrastructure, depending on the cloud platform to which you are installing the cluster.

If you choose to perform a restricted network installation on a cloud platform, you still require access to its cloud APIs. Some cloud functions, such as Amazon Web Service’s Route 53 DNS and IAM services, require internet access. Depending on your network, you might require less internet access for an installation on bare-metal hardware, Nutanix, or on VMware vSphere.

To complete a restricted network installation, you must create a registry that mirrors the contents of the OpenShift image registry and contains the installation media. You can create this registry on a mirror host, which can access both the internet and your closed network, or by using other methods that meet your restrictions.

> [!IMPORTANT]
> Because of the complexity of the configuration for user-provisioned installations, consider completing a standard user-provisioned infrastructure installation before you try a restricted network installation using user-provisioned infrastructure. Completing this test installation might make it easier to isolate and troubleshoot any issues that might arise during your installation in a restricted network.

## Additional limits

Clusters in restricted networks have the following additional limitations and restrictions:

- The `ClusterVersion` status includes an `Unable to retrieve available updates` error.

- By default, you cannot use the contents of the Developer Catalog because you cannot access the required image stream tags.

# Creating the installation files for AWS

To install OpenShift Container Platform on Amazon Web Services by using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use.

You generate and customize the `install-config.yaml` file, Kubernetes manifests, and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.

## Creating a separate `/var` partition

To isolate growing storage for containers, etcd, or logs, you can optionally create a separate `/var` partition on worker nodes before you generate Ignition configs.

It is recommended that disk partitioning for OpenShift Container Platform be left to the installation program. However, there are cases where you might want to create separate partitions in a part of the filesystem that you expect to grow.

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
    version: 4.20.0
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

    where:

    `<device_name>`
    Specifies the storage device name of the disk that you want to partition.

    `<partition_start_offset>`
    Specifies the `start_mib` parameter. When adding a data partition to the boot disk, a minimum value of 25000 MiB (Mebibytes) is recommended. The root file system is automatically resized to fill all available space up to the specified offset. If no value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of RHCOS might overwrite the beginning of the data partition.

    `<partition_size>`
    Specifies the size of the data partition in mebibytes.

    `storage.filesystems.mount_options`
    The `prjquota` mount option must be enabled for filesystems used for container storage.

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

## Creating the installation configuration file

Generate and customize the installation configuration file that the installation program needs to deploy your cluster.

<div>

<div class="title">

Prerequisites

</div>

- You obtained the OpenShift Container Platform installation program for user-provisioned infrastructure and the pull secret for your cluster. For a restricted network installation, these files are on your mirror host.

- You checked that you are deploying your cluster to an Amazon Web Services (AWS) Region with an accompanying Red Hat Enterprise Linux CoreOS (RHCOS) AMI published by Red Hat. If you are deploying to an AWS Region that requires a custom AMI, such as an AWS GovCloud Region, you must create the `install-config.yaml` file manually.

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

        For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

        > [!IMPORTANT]
        > Specify an empty directory. Some installation assets, such as bootstrap X.509 certificates have short expiration intervals, so you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.

    2.  At the prompts, provide the configuration details for your cloud:

        1.  Optional: Select an SSH key to use to access your cluster machines.

            > [!NOTE]
            > For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

        2.  Select **aws** as the platform to target.

        3.  If you do not have an AWS profile stored on your computer, enter the AWS access key ID and secret access key for the user that you configured to run the installation program.

            > [!NOTE]
            > The AWS access key ID and secret access key are stored in `~/.aws/credentials` in the home directory of the current user on the installation host. You are prompted for the credentials by the installation program if the credentials for the exported profile are not present in the file. Any credentials that you provide to the installation program are stored in the file.

        4.  Select the AWS Region to deploy the cluster to.

        5.  Select the base domain for the Route 53 service that you configured for your cluster.

        6.  Enter a descriptive name for your cluster.

        7.  Paste the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret).

2.  Edit the `install-config.yaml` file to give the additional information that is required for an installation in a restricted network.

    1.  Update the `pullSecret` value to contain the authentication information for your registry:

        ``` yaml
        pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
        ```

        For `<local_registry>`, specify the registry domain name, and optionally the port, that your mirror registry uses to serve content. For example `registry.example.com` or `registry.example.com:5000`. For `<credentials>`, specify the base64-encoded user name and password for your mirror registry.

    2.  Add the `additionalTrustBundle` parameter and value. The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry.

        ``` yaml
        additionalTrustBundle: |
          -----BEGIN CERTIFICATE-----
          ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
          -----END CERTIFICATE-----
        ```

    3.  Add the image content resources:

        ``` yaml
        imageContentSources:
        - mirrors:
          - <local_registry>/<local_repository_name>/release
          source: quay.io/openshift-release-dev/ocp-release
        - mirrors:
          - <local_registry>/<local_repository_name>/release
          source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
        ```

        Use the `imageContentSources` section from the output of the command to mirror the repository or the values that you used when you mirrored the content from the media that you brought into your restricted network.

    4.  Optional: Set the publishing strategy to `Internal`:

        ``` yaml
        publish: Internal
        ```

        By setting this option, you create an internal Ingress Controller and a private load balancer.

3.  Optional: Back up the `install-config.yaml` file.

    > [!IMPORTANT]
    > The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuration and credential file settings (AWS documentation)](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

</div>

## Configuring the cluster-wide proxy during installation

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

<div>

<div class="title">

Prerequisites

</div>

- You have an existing `install-config.yaml` file.

- You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, the proxy handles all cluster egress traffic, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object’s `spec.noProxy` field to bypass the proxy if necessary.

  > [!NOTE]
  > The `Proxy` object `status.noProxy` field includes the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration.
  >
  > For installations on Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Red Hat OpenStack Platform (RHOSP), the `Proxy` object `status.noProxy` field also includes the instance metadata endpoint (`169.254.169.254`).

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
      noProxy: ec2.<aws_region>.amazonaws.com,elasticloadbalancing.<aws_region>.amazonaws.com,s3.<aws_region>.amazonaws.com
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
    Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations. If you have added the Amazon `EC2`, `Elastic Load Balancing`, and `S3` VPC endpoints to your VPC, you must add these endpoints to the `noProxy` field.

    `additionalTrustBundle`
    If you specify this value, the installation program generates a config map named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you specify `additionalTrustBundle` and at least one proxy setting, the `Proxy` object references the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the RHCOS trust bundle. You must set the `additionalTrustBundle` field unless an authority from the RHCOS trust bundle signs the proxy’s identity certificate.

    `additionalTrustBundlePolicy`
    Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when you configure an `http/https` proxy. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter.

    > [!NOTE]
    > The installation program does not support the proxy `readinessEndpoints` field.

    > [!NOTE]
    > If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:
    >
    > ``` terminal
    > $ ./openshift-install wait-for install-complete --log-level debug
    > ```

2.  Save the file and reference it when installing OpenShift Container Platform.

    The installation program creates a cluster-wide proxy named `cluster` that uses the proxy settings in the `install-config.yaml` file. If you do not give proxy settings, the installation program still creates a `cluster` `Proxy` object, but it has a nil `spec`.

    > [!NOTE]
    > Only the `Proxy` object named `cluster` is supported, and you cannot create additional proxies.

</div>

## Creating the Kubernetes manifest and Ignition config files

Because you manually provision infrastructure, you must generate the Kubernetes manifest and Ignition config files that the cluster requires.

The installation program converts the installation configuration into Kubernetes manifests and then wraps them into Ignition configuration files. You use these Ignition files to configure the cluster machines.

<div class="important">

<div class="title">

</div>

- The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which the system then renews. If you shut down the cluster before the system renews the certificates and you later restart the cluster after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.

- Use Ignition config files within 12 hours after you generate them, because the 24-hour certificate rotates from 16 to 22 hours after you install the cluster. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You obtained the OpenShift Container Platform installation program. For a restricted network installation, these files are on your mirror host.

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

    where:

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

5.  Verify that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:

    1.  Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.

    2.  Locate the `mastersSchedulable` parameter and verify that it is set to `false`.

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

7.  To create the Ignition configuration files, run the following command from the directory that contains the installation program:

    ``` terminal
    $ ./openshift-install create ignition-configs --dir <installation_directory>
    ```

    where:

    `<installation_directory>`
    Specifies the same installation directory.

    The installation program creates Ignition config files for the bootstrap, control plane, and compute nodes in the installation directory. The program also creates the `kubeadmin-password` and `kubeconfig` files in the `./<installation_directory>/auth` directory:

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

- [Manually creating long-term credentials](../ipi/installing-restricted-networks-aws-installer-provisioned.md#manually-create-iam_installing-restricted-networks-aws-installer-provisioned)

</div>

# Extracting the infrastructure name

To identify your cluster resources in Amazon Web Services, extract the unique infrastructure name from the Ignition config files.

The Ignition config files contain a unique cluster identifier that you can use to uniquely identify your cluster in Amazon Web Services. The infrastructure name is also used to locate the appropriate AWS resources during an OpenShift Container Platform installation. The provided CloudFormation templates contain references to this infrastructure name, so you must extract it.

<div>

<div class="title">

Prerequisites

</div>

- You obtained the OpenShift Container Platform installation program and the pull secret for your cluster.

- You generated the Ignition config files for your cluster.

- You installed the `jq` package.

</div>

<div>

<div class="title">

Procedure

</div>

- To extract and view the infrastructure name from the Ignition config file metadata, run the following command:

  ``` terminal
  $ jq -r .infraID <installation_directory>/metadata.json
  ```

  where `<installation_directory>` is the path to the directory that you stored the installation files in.

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  openshift-vw9j6
  ```

  </div>

  The output of this command is your cluster name and a random string.

</div>

# Creating a VPC in AWS

To provide the network foundation for your OpenShift Container Platform cluster, create a Virtual Private Cloud (VPC) in Amazon Web Services (AWS) by using the provided CloudFormation template.

You can customize the VPC to meet your requirements, including VPN and route tables. You can use the provided CloudFormation template and a custom parameter file to create a stack of AWS resources that represent the VPC.

> [!NOTE]
> If you do not use the provided CloudFormation template to create your AWS infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

<div>

<div class="title">

Prerequisites

</div>

- You added your AWS keys and region to your local AWS profile by running `aws configure`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a JSON file that contains the parameter values that the template requires:

    ``` json
    [
      {
        "ParameterKey": "VpcCidr",
        "ParameterValue": "10.0.0.0/16"
      },
      {
        "ParameterKey": "AvailabilityZoneCount",
        "ParameterValue": "1"
      },
      {
        "ParameterKey": "SubnetBits",
        "ParameterValue": "12"
      }
    ]
    ```

    where:

    `VpcCidr`
    Specifies the CIDR block for the VPC in the format `x.x.x.x/16-24`.

    `AvailabilityZoneCount`
    Specifies the number of availability zones to deploy the VPC in. Set the value to an integer between `1` and `3`.

    `SubnetBits`
    Specifies the size of each subnet in each availability zone. Set the value to an integer between `5` and `13`, where `5` is `/27` and `13` is `/19`.

2.  Copy the template from the **CloudFormation template for the VPC** section of this topic and save it as a YAML file on your computer. This template describes the VPC that your cluster requires.

3.  Launch the CloudFormation template to create a stack of AWS resources that represent the VPC:

    > [!IMPORTANT]
    > You must enter the command on a single line.

    ``` terminal
    $ aws cloudformation create-stack --stack-name <name> \
         --template-body file://<template>.yaml \
         --parameters file://<parameters>.json
    ```

    where:

    `<name>`
    Specifies the name for the CloudFormation stack, such as `cluster-vpc`. You need the name of this stack if you remove the cluster.

    `<template>`
    Specifies the relative path to and name of the CloudFormation template YAML file that you saved.

    `<parameters>`
    Specifies the relative path to and name of the CloudFormation parameters JSON file.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-vpc/dbedae40-2fd3-11eb-820e-12a48460849f
    ```

    </div>

4.  Confirm that the template components exist:

    ``` terminal
    $ aws cloudformation describe-stacks --stack-name <name>
    ```

    After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values for the following parameters. You must provide these parameter values to the other CloudFormation templates that you run to create your cluster:

    |                    |                                     |
    |--------------------|-------------------------------------|
    | `VpcId`            | The ID of your VPC.                 |
    | `PublicSubnetIds`  | The IDs of the new public subnets.  |
    | `PrivateSubnetIds` | The IDs of the new private subnets. |

</div>

## CloudFormation template for the VPC

The VPC `CloudFormation` template creates the Amazon Web Services (AWS) networking infrastructure, including the public and private subnets, that your OpenShift Container Platform cluster requires.

<div class="formalpara">

<div class="title">

CloudFormation template for the VPC

</div>

``` yaml
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/aws/cloudformation/01_vpc.yaml[role=include]
```

</div>

# Creating networking and load balancing components in AWS

To route traffic to your OpenShift Container Platform cluster, configure the networking and load balancing components in Amazon Web Services (AWS) by using the provided `CloudFormation` template.

You can use the provided `CloudFormation` template and a custom parameter file to create a stack of AWS resources. The stack represents the networking and load balancing components that your OpenShift Container Platform cluster requires. The template also creates a hosted zone and subnet tags.

You can run the template many times within a single Virtual Private Cloud (VPC).

> [!NOTE]
> If you do not use the provided `CloudFormation` template to create your AWS infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

<div>

<div class="title">

Prerequisites

</div>

- You created and configured a VPC and associated subnets in AWS.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Obtain the hosted zone ID for the Route 53 base domain that you specified in the `install-config.yaml` file for your cluster. You can obtain details about your hosted zone by running the following command:

    ``` terminal
    $ aws route53 list-hosted-zones-by-name --dns-name <route53_domain>
    ```

    where `<route53_domain>` is the Route 53 base domain that you used when you generated the `install-config.yaml` file for the cluster.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    mycluster.example.com.   False   100
    HOSTEDZONES 65F8F38E-2268-B835-E15C-AB55336FCBFA    /hostedzone/Z21IXYZABCZ2A4  mycluster.example.com.  10
    ```

    </div>

    In the example output, the hosted zone ID is `Z21IXYZABCZ2A4`.

2.  Create a JSON file that has the parameter values that the template requires:

    ``` json
    [
      {
        "ParameterKey": "ClusterName",
        "ParameterValue": "mycluster"
      },
      {
        "ParameterKey": "InfrastructureName",
        "ParameterValue": "mycluster-<random_string>"
      },
      {
        "ParameterKey": "HostedZoneId",
        "ParameterValue": "<random_string>"
      },
      {
        "ParameterKey": "HostedZoneName",
        "ParameterValue": "example.com"
      },
      {
        "ParameterKey": "PublicSubnets",
        "ParameterValue": "subnet-<random_string>"
      },
      {
        "ParameterKey": "PrivateSubnets",
        "ParameterValue": "subnet-<random_string>"
      },
      {
        "ParameterKey": "VpcId",
        "ParameterValue": "vpc-<random_string>"
      }
    ]
    ```

    where:

    `ClusterName`
    Specifies a short, representative cluster name to use for hostnames, and so on. Set the value to the cluster name that you used when you generated the `install-config.yaml` file for the cluster.

    `InfrastructureName`
    Specifies the name for your cluster infrastructure that your Ignition config files encode for the cluster. Set the value to the infrastructure name that you extracted from the Ignition config file metadata, which has the format `<cluster_name>-<random_string>`.

    `HostedZoneId`
    Specifies the Route 53 public zone ID to register the targets with. Set the value to the Route 53 public zone ID, which has a format similar to `Z21IXYZABCZ2A4`. You can obtain this value from the AWS console.

    `HostedZoneName`
    Specifies the Route 53 zone to register the targets with. Set the value to the Route 53 base domain that you used when you generated the `install-config.yaml` file for the cluster. Do not include the trailing period (.) that is displayed in the AWS console.

    `PublicSubnets`
    Specifies the public subnets that you created for your VPC. Set the value to the `PublicSubnetIds` value from the output of the `CloudFormation` template for the VPC.

    `PrivateSubnets`
    Specifies the private subnets that you created for your VPC. Set the value to the `PrivateSubnetIds` value from the output of the `CloudFormation` template for the VPC.

    `VpcId`
    Specifies the VPC that you created for the cluster. Set the value to the `VpcId` value from the output of the `CloudFormation` template for the VPC.

3.  Copy the template from the **`CloudFormation` template for the network and load balancers** section and save it as a YAML file on your computer. This template describes the networking and load balancing objects that your cluster requires.

    > [!IMPORTANT]
    > If you are deploying your cluster to an AWS government or secret region, you must update the `InternalApiServerRecord` in the `CloudFormation` template to use `CNAME` records. Records of type `ALIAS` are not supported for AWS government regions.

4.  Launch the `CloudFormation` template to create a stack of AWS resources for the networking and load balancing components:

    > [!IMPORTANT]
    > You must enter the command on a single line.

    ``` terminal
    $ aws cloudformation create-stack --stack-name <name> \
         --template-body file://<template>.yaml \
         --parameters file://<parameters>.json \
         --capabilities CAPABILITY_NAMED_IAM
    ```

    where:

    `<name>`
    Specifies the name for the `CloudFormation` stack, such as `cluster-dns`. You need the name of this stack if you remove the cluster.

    `<template>`
    Specifies the relative path to and name of the `CloudFormation` template YAML file that you saved.

    `<parameters>`
    Specifies the relative path to and name of the `CloudFormation` parameters JSON file.

    `CAPABILITY_NAMED_IAM`
    You must explicitly declare this capability because the provided template creates some `AWS::IAM::Role` resources.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-dns/cd3e5de0-2fd4-11eb-5cf0-12be5c33a183
    ```

    </div>

5.  Confirm that the template components exist:

    ``` terminal
    $ aws cloudformation describe-stacks --stack-name <name>
    ```

    After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values for the following parameters. You must give these parameter values to the other `CloudFormation` templates that you run to create your cluster:

    |  |  |
    |----|----|
    | `PrivateHostedZoneId` | Hosted zone ID for the private DNS. |
    | `ExternalApiLoadBalancerName` | Full name of the external API load balancer. |
    | `InternalApiLoadBalancerName` | Full name of the internal API load balancer. |
    | `ApiServerDnsName` | Full hostname of the API server. |
    | `RegisterNlbIpTargetsLambda` | Lambda ARN useful to help register and unregister IP targets for these load balancers. |
    | `ExternalApiTargetGroupArn` | ARN of external API target group. |
    | `InternalApiTargetGroupArn` | ARN of internal API target group. |
    | `InternalServiceTargetGroupArn` | ARN of internal service target group. |

</div>

## CloudFormation template for the network and load balancers

The networking `CloudFormation` template creates the Route 53 DNS entries and load balancers on Amazon Web Services (AWS) that route traffic to your OpenShift Container Platform control plane and applications.

<div class="formalpara">

<div class="title">

CloudFormation template for the network and load balancers

</div>

``` yaml
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/aws/cloudformation/02_cluster_infra.yaml[role=include]
```

</div>

> [!IMPORTANT]
> If you are deploying your cluster to an AWS government or secret region, you must update the `InternalApiServerRecord` to use `CNAME` records. Records of type `ALIAS` are not supported for AWS government regions. For example:
>
> ``` yaml
> Type: CNAME
> TTL: 10
> ResourceRecords:
> - !GetAtt IntApiElb.DNSName
> ```

<div>

<div class="title">

Additional resources

</div>

- [Listing public hosted zones(AWS documentation)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ListInfoOnHostedZone.html)

</div>

# Creating security group and roles in AWS

To control access to your OpenShift Container Platform cluster resources, create the required security groups and IAM roles in Amazon Web Services (AWS) by using the provided `CloudFormation` template.

You can use the provided `CloudFormation` template and a custom parameter file to create a stack of AWS resources. The stack represents the security groups and roles that your OpenShift Container Platform cluster requires.

> [!NOTE]
> If you do not use the provided `CloudFormation` template to create your AWS infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

<div>

<div class="title">

Procedure

</div>

1.  Create a JSON file that has the parameter values that the template requires:

    ``` json
    [
      {
        "ParameterKey": "InfrastructureName",
        "ParameterValue": "mycluster-<random_string>"
      },
      {
        "ParameterKey": "VpcCidr",
        "ParameterValue": "10.0.0.0/16"
      },
      {
        "ParameterKey": "PrivateSubnets",
        "ParameterValue": "subnet-<random_string>"
      },
      {
        "ParameterKey": "VpcId",
        "ParameterValue": "vpc-<random_string>"
      }
    ]
    ```

    where:

    `InfrastructureName`
    Specifies the name for your cluster infrastructure that your Ignition config files encode for the cluster. Set the value to the infrastructure name that you extracted from the Ignition config file metadata, which has the format `<cluster_name>-<random_string>`.

    `VpcCidr`
    Specifies the CIDR block for the VPC. Set the value to the CIDR block parameter that you used for the VPC that you defined in the form `x.x.x.x/16-24`.

    `PrivateSubnets`
    Specifies the private subnets that you created for your VPC. Set the value to the `PrivateSubnetIds` value from the output of the `CloudFormation` template for the VPC.

    `VpcId`
    Specifies the VPC that you created for the cluster. Set the value to the `VpcId` value from the output of the `CloudFormation` template for the VPC.

2.  Copy the template from the **`CloudFormation` template for security objects** section and save it as a YAML file on your computer. This template describes the security groups and roles that your cluster requires.

3.  Launch the `CloudFormation` template to create a stack of AWS resources that represent the security groups and roles:

    > [!IMPORTANT]
    > You must enter the command on a single line.

    ``` terminal
    $ aws cloudformation create-stack --stack-name <name> \
         --template-body file://<template>.yaml \
         --parameters file://<parameters>.json \
         --capabilities CAPABILITY_NAMED_IAM
    ```

    where:

    `<name>`
    Specifies the name for the `CloudFormation` stack, such as `cluster-sec`. You need the name of this stack if you remove the cluster.

    `<template>`
    Specifies the relative path to and name of the `CloudFormation` template YAML file that you saved.

    `<parameters>`
    Specifies the relative path to and name of the `CloudFormation` parameters JSON file.

    `CAPABILITY_NAMED_IAM`
    You must explicitly declare this capability because the provided template creates some `AWS::IAM::Role` and `AWS::IAM::InstanceProfile` resources.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-sec/03bd4210-2ed7-11eb-6d7a-13fc0b61e9db
    ```

    </div>

4.  Confirm that the template components exist:

    ``` terminal
    $ aws cloudformation describe-stacks --stack-name <name>
    ```

    After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values for the following parameters. You must give these parameter values to the other `CloudFormation` templates that you run to create your cluster:

    |                         |                                    |
    |-------------------------|------------------------------------|
    | `MasterSecurityGroupId` | Control plane security group ID    |
    | `WorkerSecurityGroupId` | Worker security group ID           |
    | `MasterInstanceProfile` | Control plane IAM instance profile |
    | `WorkerInstanceProfile` | Worker IAM instance profile        |

</div>

## CloudFormation template for security objects

The security `CloudFormation` template creates the IAM roles and security groups on Amazon Web Services (AWS) that control access to your OpenShift Container Platform cluster resources.

<div class="formalpara">

<div class="title">

CloudFormation template for security objects

</div>

``` yaml
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/aws/cloudformation/03_cluster_security.yaml[role=include]
```

</div>

# Accessing RHCOS AMIs with stream metadata

To find the correct RHCOS boot image for your cluster, you can use stream metadata, which provides standardized information about RHCOS in the JSON format.

You can use the `coreos print-stream-json` subcommand of `openshift-install` to access information about the boot images in the stream metadata format. This command provides a method for printing stream metadata in a scriptable, machine-readable format.

For user-provisioned installations, the `openshift-install` binary has references to the version of RHCOS boot images that are tested for use with OpenShift Container Platform, such as the Amazon Web Services (AWS) AMI.

To parse the stream metadata, use one of the following methods:

<div>

<div class="title">

Procedure

</div>

- From a Go program, use the official `stream-metadata-go` library at <https://github.com/coreos/stream-metadata-go>. You can also view example code in the library.

- From another programming language, such as Python or Ruby, use the JSON library of your preferred programming language.

- From a command-line utility that handles JSON data, such as `jq`, print the current `x86_64` or `aarch64` AMI for an AWS region, such as `us-west-1`:

  <div class="formalpara">

  <div class="title">

  For x86_64

  </div>

  ``` terminal
  $ openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.aws.regions["us-west-1"].image'
  ```

  </div>

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  ami-0d3e625f84626bbda
  ```

  </div>

  <div class="formalpara">

  <div class="title">

  For aarch64

  </div>

  ``` terminal
  $ openshift-install coreos print-stream-json | jq -r '.architectures.aarch64.images.aws.regions["us-west-1"].image'
  ```

  </div>

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  ami-0af1d3b7fa5be2131
  ```

  </div>

  The output of this command is the AWS AMI ID for your designated architecture and the `us-west-1` region. The AMI must belong to the same region as the cluster.

</div>

# RHCOS AMIs for the AWS infrastructure

To deploy OpenShift Container Platform nodes on Amazon Web Services (AWS), select from the valid Red Hat Enterprise Linux CoreOS (RHCOS) AMIs for your region and instance architecture.

> [!NOTE]
> By importing your own AMI, you can also install to regions that do not have a published RHCOS AMI.

| AWS zone         | AWS AMI                 |
|------------------|-------------------------|
| `af-south-1`     | `ami-03ec26381f6a347be` |
| `ap-east-1`      | `ami-04332931a972c8398` |
| `ap-east-2`      | `ami-0ac916d2813a7b18a` |
| `ap-northeast-1` | `ami-0a3254abafd41cbda` |
| `ap-northeast-2` | `ami-001d35f0b7a38999e` |
| `ap-northeast-3` | `ami-012a97b7293096c47` |
| `ap-south-1`     | `ami-021b5ab76f755886f` |
| `ap-south-2`     | `ami-038f598890a52f3c9` |
| `ap-southeast-1` | `ami-0d191a1bffd735ebe` |
| `ap-southeast-2` | `ami-007439e088223214a` |
| `ap-southeast-3` | `ami-0e024a0bbbdf621da` |
| `ap-southeast-4` | `ami-0929268b6d28ba1e9` |
| `ap-southeast-5` | `ami-0a9461ac20d4691fe` |
| `ap-southeast-7` | `ami-0ae438f9ab8af4459` |
| `ca-central-1`   | `ami-07079826624ddc0d3` |
| `ca-west-1`      | `ami-0e0a89efe9e4aebd8` |
| `eu-central-1`   | `ami-0b9392304b25a1be6` |
| `eu-central-2`   | `ami-004899c1b1392a416` |
| `eu-north-1`     | `ami-04db8de6d2660d477` |
| `eu-south-1`     | `ami-03f6525889efe953b` |
| `eu-south-2`     | `ami-0214e803d8564e890` |
| `eu-west-1`      | `ami-04ca111133e8458c6` |
| `eu-west-2`      | `ami-089d8892ef8f88156` |
| `eu-west-3`      | `ami-0cebb38e071808759` |
| `il-central-1`   | `ami-08ff4ee35db1e8b29` |
| `me-central-1`   | `ami-0467b2b1a131cb070` |
| `me-south-1`     | `ami-09fe6bcfb3cab07a7` |
| `mx-central-1`   | `ami-0a7e97cb28cbb8354` |
| `sa-east-1`      | `ami-0ff7e5fea2302529b` |
| `us-east-1`      | `ami-09d23adad19cdb25c` |
| `us-east-2`      | `ami-082a55a580d5538ed` |
| `us-gov-east-1`  | `ami-06eb65026809257f2` |
| `us-gov-west-1`  | `ami-02d89c98e7cb51709` |
| `us-west-1`      | `ami-0788e768db7ced74d` |
| `us-west-2`      | `ami-000b42519a25cacc5` |

x86_64 RHCOS AMIs

| AWS zone         | AWS AMI                 |
|------------------|-------------------------|
| `af-south-1`     | `ami-0148286cf26e84d1d` |
| `ap-east-1`      | `ami-020178428baa4d29d` |
| `ap-east-2`      | `ami-0dc346212bfae9a5a` |
| `ap-northeast-1` | `ami-04cd61839a245df4e` |
| `ap-northeast-2` | `ami-09f756251f513af27` |
| `ap-northeast-3` | `ami-0d2f277e312013de9` |
| `ap-south-1`     | `ami-0bc01c2ad16fef268` |
| `ap-south-2`     | `ami-0961ddf05f99aa1ac` |
| `ap-southeast-1` | `ami-086c5fdb20edc12c7` |
| `ap-southeast-2` | `ami-0cd7e64385588d5af` |
| `ap-southeast-3` | `ami-09a4ec979ba4d8804` |
| `ap-southeast-4` | `ami-030445ba8507a3ec6` |
| `ap-southeast-5` | `ami-013bd53f7db86068d` |
| `ap-southeast-7` | `ami-026b8f665827ffda4` |
| `ca-central-1`   | `ami-0dd67b8ff235b962c` |
| `ca-west-1`      | `ami-09469dfe86edf2a39` |
| `eu-central-1`   | `ami-00bd76511738f7c79` |
| `eu-central-2`   | `ami-0e72cf40ed8ca51f3` |
| `eu-north-1`     | `ami-06ce6706d18914e38` |
| `eu-south-1`     | `ami-0d3c5dedab43b8daa` |
| `eu-south-2`     | `ami-06c0dd7efd3688e89` |
| `eu-west-1`      | `ami-0ba6941055f037421` |
| `eu-west-2`      | `ami-0934f6e7344143299` |
| `eu-west-3`      | `ami-0faeee552170fef71` |
| `il-central-1`   | `ami-0f6dbbdd757912184` |
| `me-central-1`   | `ami-0f9afa7909fa8890b` |
| `me-south-1`     | `ami-0f7e06ef6b630d78c` |
| `mx-central-1`   | `ami-08956a7d43f06c11a` |
| `sa-east-1`      | `ami-0774d29f6ed96935b` |
| `us-east-1`      | `ami-05834415546b16278` |
| `us-east-2`      | `ami-0c59bfd7b7a7cc3e7` |
| `us-gov-east-1`  | `ami-04c3ea90e1fec5a29` |
| `us-gov-west-1`  | `ami-05fce4dea56fdf75f` |
| `us-west-1`      | `ami-0104db843a42a4455` |
| `us-west-2`      | `ami-0b745e03468dc48d2` |

aarch64 RHCOS AMIs

# Creating the bootstrap node in AWS

To initialize the OpenShift Container Platform control plane, create the bootstrap node in Amazon Web Services (AWS) by uploading the Ignition config to an S3 bucket and launching the `CloudFormation` template.

- Providing a location to serve the `bootstrap.ign` Ignition config file to your cluster. This file is in your installation directory. The provided `CloudFormation` template assumes that you serve the Ignition config files for your cluster from an S3 bucket. If you choose to serve the files from another location, you must change the templates.

- Using the provided `CloudFormation` template and a custom parameter file to create a stack of AWS resources. The stack represents the bootstrap node that your OpenShift Container Platform installation requires.

> [!NOTE]
> If you do not use the provided `CloudFormation` template to create your bootstrap node, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

<div>

<div class="title">

Prerequisites

</div>

- You created and configured DNS, load balancers, and listeners in AWS.

- You created the security groups and roles required for your cluster in AWS.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the bucket by running the following command:

    ``` terminal
    $ aws s3 mb s3://<cluster_name>-infra
    ```

    where `<cluster_name>-infra` is the bucket name. When creating the `install-config.yaml` file, replace `<cluster_name>` with the name specified for the cluster.

    You must use a presigned URL for your S3 bucket, instead of the `s3://` schema, if you are:

    - Deploying to a region that has endpoints that differ from the AWS SDK.

    - Deploying a proxy.

    - Providing your own custom endpoints.

2.  Upload the `bootstrap.ign` Ignition config file to the bucket by running the following command:

    ``` terminal
    $ aws s3 cp <installation_directory>/bootstrap.ign s3://<cluster_name>-infra/bootstrap.ign
    ```

    where `<installation_directory>` is the path to the directory that you stored the installation files in.

3.  Verify that the file uploaded by running the following command:

    ``` terminal
    $ aws s3 ls s3://<cluster_name>-infra/
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    2019-04-03 16:15:16     314878 bootstrap.ign
    ```

    </div>

    > [!NOTE]
    > The bootstrap Ignition config file does have secrets, such as X.509 keys. The following steps give basic security for the S3 bucket. To give additional security, you can enable an S3 bucket policy to allow only certain users, such as the OpenShift IAM user, to access objects that the bucket has. You can avoid S3 entirely and serve your bootstrap Ignition config file from any address that the bootstrap machine can reach.

4.  Create a JSON file that has the parameter values that the template requires:

    ``` json
    [
      {
        "ParameterKey": "InfrastructureName",
        "ParameterValue": "mycluster-<random_string>"
      },
      {
        "ParameterKey": "RhcosAmi",
        "ParameterValue": "ami-<random_string>"
      },
      {
        "ParameterKey": "AllowedBootstrapSshCidr",
        "ParameterValue": "0.0.0.0/0"
      },
      {
        "ParameterKey": "PublicSubnet",
        "ParameterValue": "subnet-<random_string>"
      },
      {
        "ParameterKey": "MasterSecurityGroupId",
        "ParameterValue": "sg-<random_string>"
      },
      {
        "ParameterKey": "VpcId",
        "ParameterValue": "vpc-<random_string>"
      },
      {
        "ParameterKey": "BootstrapIgnitionLocation",
        "ParameterValue": "s3://<bucket_name>/bootstrap.ign"
      },
      {
        "ParameterKey": "AutoRegisterELB",
        "ParameterValue": "yes"
      },
      {
        "ParameterKey": "RegisterNlbIpTargetsLambdaArn",
        "ParameterValue": "arn:aws:lambda:<aws_region>:<account_number>:function:<dns_stack_name>-RegisterNlbIpTargets-<random_string>"
      },
      {
        "ParameterKey": "ExternalApiTargetGroupArn",
        "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Exter-<random_string>"
      },
      {
        "ParameterKey": "InternalApiTargetGroupArn",
        "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Inter-<random_string>"
      },
      {
        "ParameterKey": "InternalServiceTargetGroupArn",
        "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Inter-<random_string>"
      }
    ]
    ```

    where:

    `InfrastructureName`
    Specifies the name for your cluster infrastructure that your Ignition config files encode for the cluster. Specify the infrastructure name that you extracted from the Ignition config file metadata, which has the format `<cluster_name>-<random_string>`.

    `RhcosAmi`
    Specifies the current Red Hat Enterprise Linux CoreOS (RHCOS) AMI to use for the bootstrap node based on your selected architecture. Specify a valid `AWS::EC2::Image::Id` value.

    `AllowedBootstrapSshCidr`
    Specifies the CIDR block to allow SSH access to the bootstrap node. Specify a CIDR block in the format `x.x.x.x/16-24`.

    `PublicSubnet`
    Specifies the public subnet in your VPC to launch the bootstrap node into. Specify the `PublicSubnetIds` value from the output of the `CloudFormation` template for the VPC.

    `MasterSecurityGroupId`
    Specifies the control plane security group ID for registering temporary rules. Specify the `MasterSecurityGroupId` value from the output of the `CloudFormation` template for the security group and roles.

    `VpcId`
    Specifies the VPC that the created resources will belong to. Specify the `VpcId` value from the output of the `CloudFormation` template for the VPC.

    `BootstrapIgnitionLocation`
    Specifies the location to fetch the bootstrap Ignition config file from. Specify the S3 bucket and file name in the form `s3://<bucket_name>/bootstrap.ign`.

    `AutoRegisterELB`
    Specifies whether to register a network load balancer (NLB). Specify `yes` or `no`. If you specify `yes`, you must give a Lambda Amazon Resource Name (ARN) value.

    `RegisterNlbIpTargetsLambdaArn`
    Specifies the ARN for NLB IP target registration lambda group. Specify the `RegisterNlbIpTargetsLambda` value from the output of the `CloudFormation` template for DNS and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS `GovCloud` region.

    `ExternalApiTargetGroupArn`
    Specifies the ARN for external API load balancer target group. Specify the `ExternalApiTargetGroupArn` value from the output of the `CloudFormation` template for DNS and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS `GovCloud` region.

    `InternalApiTargetGroupArn`
    Specifies the ARN for internal API load balancer target group. Specify the `InternalApiTargetGroupArn` value from the output of the `CloudFormation` template for DNS and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS `GovCloud` region.

    `InternalServiceTargetGroupArn`
    Specifies the ARN for internal service load balancer target group. Specify the `InternalServiceTargetGroupArn` value from the output of the `CloudFormation` template for DNS and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS `GovCloud` region.

5.  Copy the template from the **`CloudFormation` template for the bootstrap machine** section and save it as a YAML file on your computer. This template describes the bootstrap machine that your cluster requires.

6.  Optional: If you are deploying the cluster with a proxy, you must update the ignition in the template to add the `ignition.config.proxy` fields. Additionally, If you have added the Amazon EC2, Elastic Load Balancing, and S3 VPC endpoints to your VPC, you must add these endpoints to the `noProxy` field.

7.  Launch the `CloudFormation` template to create a stack of AWS resources that represent the bootstrap node:

    > [!IMPORTANT]
    > You must enter the command on a single line.

    ``` terminal
    $ aws cloudformation create-stack --stack-name <name> \
         --template-body file://<template>.yaml \
         --parameters file://<parameters>.json \
         --capabilities CAPABILITY_NAMED_IAM
    ```

    where:

    `<name>`
    Specifies the name for the `CloudFormation` stack, such as `cluster-bootstrap`. You need the name of this stack if you remove the cluster.

    `<template>`
    Specifies the relative path to and name of the `CloudFormation` template YAML file that you saved.

    `<parameters>`
    Specifies the relative path to and name of the `CloudFormation` parameters JSON file.

    `CAPABILITY_NAMED_IAM`
    You must explicitly declare this capability because the provided template creates some `AWS::IAM::Role` and `AWS::IAM::InstanceProfile` resources.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-bootstrap/12944486-2add-11eb-9dee-12dace8e3a83
    ```

    </div>

8.  Confirm that the template components exist:

    ``` terminal
    $ aws cloudformation describe-stacks --stack-name <name>
    ```

    After the `StackStatus` displays `CREATE_COMPLETE`, the output displays values for the following parameters. You must give these parameter values to the other `CloudFormation` templates that you run to create your cluster:

    |                       |                                        |
    |-----------------------|----------------------------------------|
    | `BootstrapInstanceId` | The bootstrap Instance ID.             |
    | `BootstrapPublicIp`   | The bootstrap node public IP address.  |
    | `BootstrapPrivateIp`  | The bootstrap node private IP address. |

</div>

## CloudFormation template for the bootstrap machine

The bootstrap machine `CloudFormation` template creates the temporary Amazon Web Services (AWS) resources that the OpenShift Container Platform bootstrap process requires to initialize the control plane.

<div class="formalpara">

<div class="title">

CloudFormation template for the bootstrap machine

</div>

``` yaml
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/aws/cloudformation/04_cluster_bootstrap.yaml[role=include]
```

</div>

<div>

<div class="title">

Additional resources

</div>

- [RHCOS AMIs for the AWS infrastructure (AWS documentation)](installing-aws-user-infra.md#installation-aws-user-infra-rhcos-ami_installing-aws-user-infra)

</div>

## Creating the control plane machines in AWS

To run the OpenShift Container Platform control plane, create the three control plane machines in Amazon Web Services (AWS) by using the provided `CloudFormation` template and a custom parameter file.

> [!IMPORTANT]
> The `CloudFormation` template creates a stack that represents three control plane nodes.

> [!NOTE]
> If you do not use the provided `CloudFormation` template to create your control plane nodes, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

<div>

<div class="title">

Prerequisites

</div>

- You created the bootstrap machine.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a JSON file that has the parameter values that the template requires:

    ``` json
    [
      {
        "ParameterKey": "InfrastructureName",
        "ParameterValue": "mycluster-<random_string>"
      },
      {
        "ParameterKey": "RhcosAmi",
        "ParameterValue": "ami-<random_string>"
      },
      {
        "ParameterKey": "AutoRegisterDNS",
        "ParameterValue": "yes"
      },
      {
        "ParameterKey": "PrivateHostedZoneId",
        "ParameterValue": "<random_string>"
      },
      {
        "ParameterKey": "PrivateHostedZoneName",
        "ParameterValue": "mycluster.example.com"
      },
      {
        "ParameterKey": "Master0Subnet",
        "ParameterValue": "subnet-<random_string>"
      },
      {
        "ParameterKey": "Master1Subnet",
        "ParameterValue": "subnet-<random_string>"
      },
      {
        "ParameterKey": "Master2Subnet",
        "ParameterValue": "subnet-<random_string>"
      },
      {
        "ParameterKey": "MasterSecurityGroupId",
        "ParameterValue": "sg-<random_string>"
      },
      {
        "ParameterKey": "IgnitionLocation",
        "ParameterValue": "https://api-int.<cluster_name>.<domain_name>:22623/config/master"
      },
      {
        "ParameterKey": "CertificateAuthorities",
        "ParameterValue": "data:text/plain;charset=utf-8;base64,ABC...xYz=="
      },
      {
        "ParameterKey": "MasterInstanceProfileName",
        "ParameterValue": "<roles_stack>-MasterInstanceProfile-<random_string>"
      },
      {
        "ParameterKey": "MasterInstanceType",
        "ParameterValue": ""
      },
      {
        "ParameterKey": "AutoRegisterELB",
        "ParameterValue": "yes"
      },
      {
        "ParameterKey": "RegisterNlbIpTargetsLambdaArn",
        "ParameterValue": "arn:aws:lambda:<aws_region>:<account_number>:function:<dns_stack_name>-RegisterNlbIpTargets-<random_string>"
      },
      {
        "ParameterKey": "ExternalApiTargetGroupArn",
        "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Exter-<random_string>"
      },
      {
        "ParameterKey": "InternalApiTargetGroupArn",
        "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Inter-<random_string>"
      },
      {
        "ParameterKey": "InternalServiceTargetGroupArn",
        "ParameterValue": "arn:aws:elasticloadbalancing:<aws_region>:<account_number>:targetgroup/<dns_stack_name>-Inter-<random_string>"
      }
    ]
    ```

    where:

    `InfrastructureName`
    Specifies the name for your cluster infrastructure that your Ignition config files encode for the cluster. Specify the infrastructure name that you extracted from the Ignition config file metadata, which has the format `<cluster_name>-<random_string>`.

    `RhcosAmi`
    Specifies the current Red Hat Enterprise Linux CoreOS (RHCOS) AMI to use for the control plane machines based on your selected architecture. Specify an `AWS::EC2::Image::Id` value.

    `AutoRegisterDNS`
    Specifies whether to perform DNS etcd registration. Specify `yes` or `no`. If you specify `yes`, you must give hosted zone information.

    `PrivateHostedZoneId`
    Specifies the Route 53 private zone ID to register the etcd targets with. Specify the `PrivateHostedZoneId` value from the output of the `CloudFormation` template for DNS and load balancing.

    `PrivateHostedZoneName`
    Specifies the Route 53 zone to register the targets with. Specify `<cluster_name>.<domain_name>` where `<domain_name>` is the Route 53 base domain that you used when you generated the `install-config.yaml` file for the cluster. Do not include the trailing period (.) that is displayed in the AWS console.

    `Master0Subnet`, `Master1Subnet`, `Master2Subnet`
    Specifies a subnet, preferably private, to launch the control plane machines on. Specify a subnet from the `PrivateSubnets` value from the output of the `CloudFormation` template for DNS and load balancing.

    `MasterSecurityGroupId`
    Specifies the control plane security group ID to associate with control plane nodes. Specify the `MasterSecurityGroupId` value from the output of the `CloudFormation` template for the security group and roles.

    `IgnitionLocation`
    Specifies the location to fetch the control plane Ignition config file from. Specify the generated Ignition config file location, `https://api-int.<cluster_name>.<domain_name>:22623/config/master`.

    `CertificateAuthorities`
    Specifies the base64 encoded certificate authority string to use. Specify the value from the `master.ign` file that is in the installation directory. This value is the long string with the format `data:text/plain;charset=utf-8;base64,ABC…​xYz==`.

    `MasterInstanceProfileName`
    Specifies the IAM profile to associate with control plane nodes. Specify the `MasterInstanceProfile` parameter value from the output of the `CloudFormation` template for the security group and roles.

    `MasterInstanceType`
    Specifies the type of AWS instance to use for the control plane machines based on your selected architecture. The instance type value corresponds to the minimum resource requirements for control plane machines. For example `m6i.xlarge` is a type for AMD64 and `m6g.xlarge` is a type for ARM64.

    `AutoRegisterELB`
    Specifies whether to register a network load balancer (NLB). Specify `yes` or `no`. If you specify `yes`, you must give a Lambda Amazon Resource Name (ARN) value.

    `RegisterNlbIpTargetsLambdaArn`
    Specifies the ARN for NLB IP target registration lambda group. Specify the `RegisterNlbIpTargetsLambda` value from the output of the `CloudFormation` template for DNS and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS `GovCloud` region.

    `ExternalApiTargetGroupArn`
    Specifies the ARN for external API load balancer target group. Specify the `ExternalApiTargetGroupArn` value from the output of the `CloudFormation` template for DNS and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS `GovCloud` region.

    `InternalApiTargetGroupArn`
    Specifies the ARN for internal API load balancer target group. Specify the `InternalApiTargetGroupArn` value from the output of the `CloudFormation` template for DNS and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS `GovCloud` region.

    `InternalServiceTargetGroupArn`
    Specifies the ARN for internal service load balancer target group. Specify the `InternalServiceTargetGroupArn` value from the output of the `CloudFormation` template for DNS and load balancing. Use `arn:aws-us-gov` if deploying the cluster to an AWS `GovCloud` region.

2.  Copy the template from the **`CloudFormation` template for control plane machines** section and save it as a YAML file on your computer. This template describes the control plane machines that your cluster requires.

3.  If you specified an `m5` instance type as the value for `MasterInstanceType`, add that instance type to the `MasterInstanceType.AllowedValues` parameter in the `CloudFormation` template.

4.  Launch the `CloudFormation` template to create a stack of AWS resources that represent the control plane nodes:

    > [!IMPORTANT]
    > You must enter the command on a single line.

    ``` terminal
    $ aws cloudformation create-stack --stack-name <name> \
         --template-body file://<template>.yaml \
         --parameters file://<parameters>.json
    ```

    where:

    `<name>`
    Specifies the name for the `CloudFormation` stack, such as `cluster-control-plane`. You need the name of this stack if you remove the cluster.

    `<template>`
    Specifies the relative path to and name of the `CloudFormation` template YAML file that you saved.

    `<parameters>`
    Specifies the relative path to and name of the `CloudFormation` parameters JSON file.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-control-plane/21c7e2b0-2ee2-11eb-c6f6-0aa34627df4b
    ```

    </div>

    > [!NOTE]
    > The `CloudFormation` template creates a stack that represents three control plane nodes.

5.  Confirm that the template components exist:

    ``` terminal
    $ aws cloudformation describe-stacks --stack-name <name>
    ```

</div>

## CloudFormation template for control plane machines

The control plane `CloudFormation` template creates the Amazon Web Services (AWS) resources for the three control plane machines that manage your OpenShift Container Platform cluster.

<div class="formalpara">

<div class="title">

CloudFormation template for control plane machines

</div>

``` yaml
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/aws/cloudformation/05_cluster_master_nodes.yaml[role=include]
```

</div>

# Creating the worker nodes in AWS

To run application workloads on your OpenShift Container Platform cluster, create worker nodes in Amazon Web Services (AWS) by using the provided CloudFormation template.

You can use the provided CloudFormation template and a custom parameter file to create a stack of AWS resources that represent a worker node.

> [!IMPORTANT]
> The CloudFormation template creates a stack that represents one worker node. You must create a stack for each worker node.

> [!NOTE]
> If you do not use the provided CloudFormation template to create your worker nodes, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

<div>

<div class="title">

Prerequisites

</div>

- You created the control plane machines.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a JSON file that contains the parameter values that the CloudFormation template requires:

    ``` json
    [
      {
        "ParameterKey": "InfrastructureName",
        "ParameterValue": "mycluster-<random_string>"
      },
      {
        "ParameterKey": "RhcosAmi",
        "ParameterValue": "ami-<random_string>"
      },
      {
        "ParameterKey": "Subnet",
        "ParameterValue": "subnet-<random_string>"
      },
      {
        "ParameterKey": "WorkerSecurityGroupId",
        "ParameterValue": "sg-<random_string>"
      },
      {
        "ParameterKey": "IgnitionLocation",
        "ParameterValue": "https://api-int.<cluster_name>.<domain_name>:22623/config/worker"
      },
      {
        "ParameterKey": "CertificateAuthorities",
        "ParameterValue": "data:text/plain;charset=utf-8;base64,ABC...xYz=="
      },
      {
        "ParameterKey": "WorkerInstanceProfileName",
        "ParameterValue": "<roles_stack>-WorkerInstanceProfile-<random_string>"
      },
      {
        "ParameterKey": "WorkerInstanceType",
        "ParameterValue": ""
      }
    ]
    ```

    where:

    `InfrastructureName`
    Specifies the name for your cluster infrastructure that is encoded in your Ignition config files for the cluster. Set the value to the infrastructure name that you extracted from the Ignition config file metadata, which has the format `<cluster-name>-<random-string>`.

    `RhcosAmi`
    Specifies the current Red Hat Enterprise Linux CoreOS (RHCOS) AMI to use for the worker nodes based on your selected architecture. Set the value to a valid `AWS::EC2::Image::Id` value.

    `Subnet`
    Specifies a subnet, preferably private, to start the worker nodes on. Set the value to a subnet from the `PrivateSubnets` value from the output of the CloudFormation template for DNS and load balancing.

    `WorkerSecurityGroupId`
    Specifies the worker security group ID to associate with worker nodes. Set the value to the `WorkerSecurityGroupId` value from the output of the CloudFormation template for the security group and roles.

    `IgnitionLocation`
    Specifies the location to fetch the bootstrap Ignition config file from. Set the value to the generated Ignition config location, `https://api-int.<cluster_name>.<domain_name>:22623/config/worker`.

    `CertificateAuthorities`
    Specifies the base64 encoded certificate authority string to use. Set the value to the value from the `worker.ign` file that is in the installation directory. This value is the long string with the format `data:text/plain;charset=utf-8;base64,ABC…​xYz==`.

    `WorkerInstanceProfileName`
    Specifies the IAM profile to associate with worker nodes. Set the value to the `WorkerInstanceProfile` parameter value from the output of the CloudFormation template for the security group and roles.

    `WorkerInstanceType`
    Specifies the type of AWS instance to use for the compute machines based on your selected architecture. The instance type value corresponds to the minimum resource requirements for compute machines. For example `m6i.large` is a type for AMD64 and `m6g.large` is a type for ARM64.

2.  Copy the template from the **CloudFormation template for compute machines** section of this topic and save it as a YAML file on your computer. This template describes the compute machines that your cluster requires.

3.  Optional: If you specified an `m5` instance type as the value for `WorkerInstanceType`, add that instance type to the `WorkerInstanceType.AllowedValues` parameter in the CloudFormation template.

4.  Optional: If you are deploying with an AWS Marketplace image, update the `Worker0.type.properties.ImageID` parameter with the AMI ID that you obtained from your subscription.

5.  Use the CloudFormation template to create a stack of AWS resources that represent a worker node:

    > [!IMPORTANT]
    > You must enter the command on a single line.

    ``` terminal
    $ aws cloudformation create-stack --stack-name <name> \
         --template-body file://<template>.yaml \
         --parameters file://<parameters>.json
    ```

    where:

    `<name>`
    Specifies the name for the CloudFormation stack, such as `cluster-worker-1`. You need the name of this stack if you remove the cluster.

    `<template>`
    Specifies the relative path to and name of the CloudFormation template YAML file that you saved.

    `<parameters>`
    Specifies the relative path to and name of the CloudFormation parameters JSON file.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-worker-1/729ee301-1c2a-11eb-348f-sd9888c65b59
    ```

    </div>

    > [!NOTE]
    > The CloudFormation template creates a stack that represents one worker node.

6.  Confirm that the template components exist:

    ``` terminal
    $ aws cloudformation describe-stacks --stack-name <name>
    ```

7.  Continue to create worker stacks until you have created enough worker machines for your cluster. You can create additional worker stacks by referencing the same template and parameter files and specifying a different stack name.

    > [!IMPORTANT]
    > You must create at least two worker machines, so you must create at least two stacks that use this CloudFormation template.

</div>

## CloudFormation template for compute machines

The compute machine `CloudFormation` template creates the Amazon Web Services (AWS) resources for the worker nodes that run your OpenShift Container Platform application workloads.

<div class="formalpara">

<div class="title">

CloudFormation template for compute machines

</div>

``` yaml
link:https://raw.githubusercontent.com/openshift/installer/release-4.20/upi/aws/cloudformation/06_cluster_worker_node.yaml[role=include]
```

</div>

## Creating the CloudFormation stack for compute machines

You can create a stack of Amazon Web Services (AWS) resources for the compute machines by using the provided `CloudFormation` template.

> [!IMPORTANT]
> When you use the `CloudFormation` template for the control plane machines, the template provisions all three control plane machines with a single stack; however, when you use the `CloudFormation` template to deploy the compute machines, you must create the number of stacks based on the number that you defined in the `install-config.yaml` file. You provision each stack once for each machine. To provision a new compute machine, you must change the stack name.

<div>

<div class="title">

Procedure

</div>

- To create the `CloudFormation` stack for compute machines, run the following command:

  ``` terminal
  $ aws cloudformation create-stack --stack-name <name> \
       --template-body file://<template>.yaml \
       --parameters file://<parameters>.json
  ```

  where:

  `<name>`
  Specifies the `<name>` with the name for the `CloudFormation` stack, such as `cluster-worker-1`. You need the name of this stack if you remove the cluster.

  `<template>`
  Specifies the relative path and the name of the `CloudFormation` template YAML file that you saved.

  `<parameters>`
  Specifies the relative path and the name of the JSON file for the `CloudFormation` parameters.

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  arn:aws:cloudformation:us-east-1:269333783861:stack/cluster-worker-1/729ee301-1c2a-11eb-348f-sd9888c65b59
  ```

  </div>

</div>

# Initializing the bootstrap sequence on AWS with user-provisioned infrastructure

After creating all required infrastructure in AWS, you can start the bootstrap sequence that initializes the OpenShift Container Platform control plane. Run the installation program to monitor the bootstrap process until the control plane is ready.

<div>

<div class="title">

Prerequisites

</div>

- You created the worker nodes.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Change to the directory that has the installation program and start the bootstrap process that initializes the OpenShift Container Platform control plane:

    ``` terminal
    $ ./openshift-install wait-for bootstrap-complete --dir <installation_directory> \
        --log-level=info
    ```

    - For `<installation_directory>`, specify the path to the directory that you stored the installation files in.

    - To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      INFO Waiting up to 20m0s for the Kubernetes API at https://api.mycluster.example.com:6443...
      INFO API v1.33.4 up
      INFO Waiting up to 45m0s for bootstrapping to complete...
      INFO It is now safe to remove the bootstrap resources
      INFO Time elapsed: 1s
      ```

      </div>

      The bootstrapping completion wait time varies per platform.

      If the command exits without a `FATAL` warning, your OpenShift Container Platform control plane has initialized.

      > [!NOTE]
      > After the control plane initializes, it sets up the compute nodes and installs additional services in the form of Operators.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Monitoring installation progress](../../../support/troubleshooting/troubleshooting-installations.md#monitoring-installation-progress_troubleshooting-installations)

- [Gathering bootstrap node diagnostic data](../../../support/troubleshooting/troubleshooting-installations.md#gathering-bootstrap-diagnostic-data_troubleshooting-installations)

</div>

# Approving the certificate signing requests for your machines

To allow newly added machines to join your OpenShift Container Platform cluster, confirm that the cluster approves pending certificate signing requests (CSRs), or approve them yourself. Approve client requests first, then server requests.

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
    > The preceding output might not include the compute nodes until you approve some CSRs.

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
    > You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates rotate, and more than two certificates are present for each node. You must approve all of these certificates. After you approve the client CSR, the kubelet creates a secondary CSR for the serving certificate, which requires manual approval. The `machine-approver` then automatically approves later serving certificate renewal requests if the kubelet requests a new certificate with the same parameters.

    > [!NOTE]
    > For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If you do not approve a request, the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because the API server requires a serving certificate when it connects to the kubelet. Any operation that contacts the kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the `node-bootstrapper` service account in the `system:node` or `system:admin` groups submitted the CSR, and confirm the identity of the node.

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
      > Some Operators might not become available until you approve some CSRs.

4.  After you approve your client requests, review the server requests for each machine that you added to the cluster:

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

6.  After you approve all client and server CSRs, the machines have the `Ready` status. Verify this by running the following command:

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
    > You might need to wait a few minutes after approval of the server CSRs for the machines to reach the `Ready` status.

</div>

# Initial Operator configuration

After the control plane initializes, you must immediately configure some Operators so that they all become available.

<div>

<div class="title">

Prerequisites

</div>

- Your control plane has initialized.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Watch the cluster components come online:

    ``` terminal
    $ watch -n5 oc get clusteroperators
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
    authentication                             4.20.0    True        False         False      19m
    baremetal                                  4.20.0    True        False         False      37m
    cloud-credential                           4.20.0    True        False         False      40m
    cluster-autoscaler                         4.20.0    True        False         False      37m
    config-operator                            4.20.0    True        False         False      38m
    console                                    4.20.0    True        False         False      26m
    csi-snapshot-controller                    4.20.0    True        False         False      37m
    dns                                        4.20.0    True        False         False      37m
    etcd                                       4.20.0    True        False         False      36m
    image-registry                             4.20.0    True        False         False      31m
    ingress                                    4.20.0    True        False         False      30m
    insights                                   4.20.0    True        False         False      31m
    kube-apiserver                             4.20.0    True        False         False      26m
    kube-controller-manager                    4.20.0    True        False         False      36m
    kube-scheduler                             4.20.0    True        False         False      36m
    kube-storage-version-migrator              4.20.0    True        False         False      37m
    machine-api                                4.20.0    True        False         False      29m
    machine-approver                           4.20.0    True        False         False      37m
    machine-config                             4.20.0    True        False         False      36m
    marketplace                                4.20.0    True        False         False      37m
    monitoring                                 4.20.0    True        False         False      29m
    network                                    4.20.0    True        False         False      38m
    node-tuning                                4.20.0    True        False         False      37m
    openshift-apiserver                        4.20.0    True        False         False      32m
    openshift-controller-manager               4.20.0    True        False         False      30m
    openshift-samples                          4.20.0    True        False         False      32m
    operator-lifecycle-manager                 4.20.0    True        False         False      37m
    operator-lifecycle-manager-catalog         4.20.0    True        False         False      37m
    operator-lifecycle-manager-packageserver   4.20.0    True        False         False      32m
    service-ca                                 4.20.0    True        False         False      38m
    storage                                    4.20.0    True        False         False      37m
    ```

    </div>

2.  Configure the Operators that are not available.

</div>

## Disabling the default software catalog sources

To use only trusted or locally available Operator catalogs, disable the default software catalog sources that OpenShift Container Platform configures during installation. In a restricted network environment, you must disable the default catalogs as a cluster administrator.

<div>

<div class="title">

Procedure

</div>

- Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object:

  ``` terminal
  $ oc patch OperatorHub cluster --type json \
      -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
  ```

  > [!TIP]
  > Or, you can use the web console to manage catalog sources. From the **Administration** → **Cluster Settings** → **Configuration** → **OperatorHub** page, click the **Sources** tab, where you can create, update, delete, disable, and enable individual sources.

</div>

## Image registry storage configuration

Amazon Web Services provides default storage, which means the Image Registry Operator is available after installation. However, if the Registry Operator cannot create an S3 bucket and automatically configure storage, you must manually configure registry storage.

Configure a persistent volume, which is required for production clusters. Where applicable, you can configure an empty directory as the storage location for non-production clusters.

You can also allow the image registry to use block storage types by using the `Recreate` rollout strategy during upgrades.

### Configuring registry storage for AWS with user-provisioned infrastructure

If the Registry Operator cannot automatically create and configure an Amazon S3 bucket during installation, you must manually configure registry storage for your cluster.

> [!WARNING]
> To secure your registry images in Amazon Web Services (AWS), [block public access](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html) to the S3 bucket.

<div>

<div class="title">

Prerequisites

</div>

- You have a cluster on AWS with user-provisioned infrastructure.

- For Amazon S3 storage, the secret must contain two keys:

  - `REGISTRY_STORAGE_S3_ACCESSKEY`

  - `REGISTRY_STORAGE_S3_SECRETKEY`

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set up a [Bucket Lifecycle Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config) to cancel incomplete multipart uploads that are one day old.

2.  Enter the storage configuration in `configs.imageregistry.operator.openshift.io/cluster`:

    ``` terminal
    $ oc edit configs.imageregistry.operator.openshift.io/cluster
    ```

    <div class="formalpara">

    <div class="title">

    Example configuration

    </div>

    ``` yaml
    apiVersion: imageregistry.operator.openshift.io/v1
    kind: Config
    metadata:
      name: cluster
    spec:
      storage:
        s3:
          bucket: <bucket_name>
          region: <region_name>
    ```

    </div>

</div>

### Configuring storage for the image registry in non-production clusters

You must configure storage for the Image Registry Operator. For non-production clusters, you can set the image registry to an empty directory, but you lose all images if you restart the registry.

<div>

<div class="title">

Procedure

</div>

- To set the image registry storage to an empty directory:

  ``` terminal
  $ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"storage":{"emptyDir":{}}}}'
  ```

  > [!WARNING]
  > Configure this option only for non-production clusters.

  If you run this command before the Image Registry Operator initializes its components, the `oc patch` command fails with the following error:

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Error from server (NotFound): configs.imageregistry.operator.openshift.io "cluster" not found
  ```

  </div>

  Wait a few minutes and run the command again.

</div>

# Deleting the bootstrap resources

After completing the initial Operator configuration for your OpenShift Container Platform cluster, you can delete the bootstrap resources from AWS to free up capacity and reduce costs.

<div>

<div class="title">

Prerequisites

</div>

- You completed the initial Operator configuration for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Delete the bootstrap resources. If you used the `CloudFormation` template, [delete its stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html):

    - Delete the stack by using the AWS CLI:

      ``` terminal
      $ aws cloudformation delete-stack --stack-name <name>
      ```

      `<name>` is the name of your bootstrap stack.

    - Delete the stack by using the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

</div>

# Creating the Ingress DNS records

If you removed the DNS zone configuration during installation, you must manually create DNS records that point to the Ingress load balancer so that your OpenShift Container Platform cluster routes are reachable.

You can create either a wildcard record or specific records. While the following procedure uses A records, you can use other record types that you require, such as CNAME or alias.

<div>

<div class="title">

Prerequisites

</div>

- You deployed an OpenShift Container Platform cluster on Amazon Web Services (AWS) that uses infrastructure that you provisioned.

- You installed the OpenShift CLI (`oc`).

- You installed the `jq` package.

- You downloaded the AWS CLI and installed it on your computer. See [Install the AWS CLI Using the Bundled Installer (Linux, macOS, or Unix)](https://docs.aws.amazon.com/cli/latest/userguide/install-bundle.html).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Find the routes to create.

    - To create a wildcard record, use `*.apps.<cluster_name>.<domain_name>`, where `<cluster_name>` is your cluster name, and `<domain_name>` is the Route 53 base domain for your OpenShift Container Platform cluster.

    - To create specific records, you must create a record for each route that your cluster uses, as shown in the output of the following command:

      ``` terminal
      $ oc get --all-namespaces -o jsonpath='{range .items[*]}{range .status.ingress[*]}{"\n"}{end}{end}' routes
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      oauth-openshift.apps.<cluster_name>.<domain_name>
      console-openshift-console.apps.<cluster_name>.<domain_name>
      downloads-openshift-console.apps.<cluster_name>.<domain_name>
      alertmanager-main-openshift-monitoring.apps.<cluster_name>.<domain_name>
      prometheus-k8s-openshift-monitoring.apps.<cluster_name>.<domain_name>
      ```

      </div>

2.  Retrieve the Ingress Operator load balancer status and note the value of the external IP address that it uses, which the `EXTERNAL-IP` column displays:

    ``` terminal
    $ oc -n openshift-ingress get service router-default
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME             TYPE           CLUSTER-IP      EXTERNAL-IP                            PORT(S)                      AGE
    router-default   LoadBalancer   172.30.62.215   ab3...28.us-east-2.elb.amazonaws.com   80:31499/TCP,443:30693/TCP   5m
    ```

    </div>

3.  Locate the hosted zone ID for the load balancer:

    ``` terminal
    $ aws elb describe-load-balancers | jq -r '.LoadBalancerDescriptions[] | select(.DNSName == "<external_ip>").CanonicalHostedZoneNameID'
    ```

    For `<external_ip>`, specify the value of the external IP address of the Ingress Operator load balancer that you obtained.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Z3AADJGX6KTTL2
    ```

    </div>

    The output of this command is the load balancer hosted zone ID.

4.  Obtain the public hosted zone ID for your cluster’s domain:

    ``` terminal
    $ aws route53 list-hosted-zones-by-name \
                --dns-name "<domain_name>" \
                --query 'HostedZones[? Config.PrivateZone != `true` && Name == `<domain_name>.`].Id'
                --output text
    ```

    For `<domain_name>`, specify the Route 53 base domain for your OpenShift Container Platform cluster.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    /hostedzone/Z3URY6TWQ91KVV
    ```

    </div>

    The command output displays the public hosted zone ID for your domain. In this example, it is `Z3URY6TWQ91KVV`.

5.  Add the alias records to your private zone:

    ``` terminal
    $ aws route53 change-resource-record-sets --hosted-zone-id "<private_hosted_zone_id>" --change-batch '{
    >   "Changes": [
    >     {
    >       "Action": "CREATE",
    >       "ResourceRecordSet": {
    >         "Name": "\\052.apps.<cluster_domain>",
    >         "Type": "A",
    >         "AliasTarget":{
    >           "HostedZoneId": "<hosted_zone_id>",
    >           "DNSName": "<external_ip>.",
    >           "EvaluateTargetHealth": false
    >         }
    >       }
    >     }
    >   ]
    > }'
    ```

    where:

    `<private_hosted_zone_id>`
    Specifies the value from the output of the CloudFormation template for DNS and load balancing.

    `<cluster_domain>`
    Specifies the domain or subdomain that you use with your OpenShift Container Platform cluster.

    `<hosted_zone_id>`
    Specifies the public hosted zone ID for the load balancer that you obtained.

    `<external_ip>`
    Specifies the value of the external IP address of the Ingress Operator load balancer. Ensure that you include the trailing period (`.`) in this parameter value.

6.  Add the records to your public zone:

    ``` terminal
    $ aws route53 change-resource-record-sets --hosted-zone-id "<public_hosted_zone_id>"" --change-batch '{
    >   "Changes": [
    >     {
    >       "Action": "CREATE",
    >       "ResourceRecordSet": {
    >         "Name": "\\052.apps.<cluster_domain>",
    >         "Type": "A",
    >         "AliasTarget":{
    >           "HostedZoneId": "<hosted_zone_id>",
    >           "DNSName": "<external_ip>.",
    >           "EvaluateTargetHealth": false
    >         }
    >       }
    >     }
    >   ]
    > }'
    ```

    where: `<public_hosted_zone_id>`:: Specifies the public hosted zone for your domain. `<cluster_domain>`:: Specifies the domain or subdomain that you use with your OpenShift Container Platform cluster. `<hosted_zone_id>`:: Specifies the public hosted zone ID for the load balancer that you obtained. `<external_ip>`:: Specifies the value of the external IP address of the Ingress Operator load balancer. Ensure that you include the trailing period (`.`) in this parameter value.

</div>

# Completing an AWS installation on user-provisioned infrastructure

To finish installing OpenShift Container Platform on user-provisioned AWS infrastructure, monitor the deployment until it completes successfully.

<div>

<div class="title">

Prerequisites

</div>

- You removed the bootstrap node for an OpenShift Container Platform cluster on user-provisioned AWS infrastructure.

- You installed the `oc` CLI.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the directory that has the installation program, complete the cluster installation:

    ``` terminal
    $ ./openshift-install --dir <installation_directory> wait-for install-complete
    ```

    For `<installation_directory>`, specify the path to the directory that you stored the installation files in.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    INFO Waiting up to 40m0s for the cluster at https://api.mycluster.example.com:6443 to initialize...
    INFO Waiting up to 10m0s for the openshift-console route to be created...
    INFO Install complete!
    INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
    INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
    INFO Login to the console with user: "kubeadmin", and password: "password"
    INFO Time elapsed: 1s
    ```

    </div>

    <div class="important">

    <div class="title">

    </div>

    - The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If you shut down the cluster before renewing the certificates and later restart it after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.

    - Use Ignition config files within 12 hours after the installation program generates them because the 24-hour certificate rotates from 16 to 22 hours after you install the cluster. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

    </div>

2.  Register your cluster on the [Cluster registration](https://console.redhat.com/openshift/register) page.

</div>

# Logging in to the cluster by using the CLI

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and OpenShift Container Platform generates it during installation.

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

To verify that your cluster deployed successfully and access its features, log in to the OpenShift Container Platform web console as the `kubeadmin` user.

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
    > Or, you can obtain the `kubeadmin` password from the `<installation_directory>/.openshift_install.log` log file on the installation host.

2.  List the OpenShift Container Platform web console route:

    ``` terminal
    $ oc get routes -n openshift-console | grep 'console-openshift'
    ```

    > [!NOTE]
    > Or, you can obtain the OpenShift Container Platform route from the `<installation_directory>/.openshift_install.log` log file on the installation host.

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

<div>

<div class="title">

Additional resources

</div>

- [Accessing the web console](../../../web_console/web-console.md#web-console)

- [About remote health monitoring](../../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring)

- [Managing AWS resources as a single unit with CloudFormation stacks (AWS documentation)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html)

- [Validating an installation](../../validation_and_troubleshooting/validating-an-installation.md#validating-an-installation)

- [Customizing your cluster](../../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations)

- [Configuring image streams](../../../post_installation_configuration/cluster-tasks.md#post-install-must-gather-disconnected)

- [Using Operator Lifecycle Manager in disconnected environments](../../../disconnected/using-olm.md#olm-restricted-networks)

- [Image configuration resources](../../../openshift_images/image-configuration.md#images-configuration-cas_image-configuration)

- [Remote health reporting](../../../support/remote_health_monitoring/remote-health-reporting.md#remote-health-reporting)

- [Changing the cloud provider credentials configuration](../../../post_installation_configuration/changing-cloud-credentials-configuration.md#manually-removing-cloud-creds_changing-cloud-credentials-configuration)

</div>
