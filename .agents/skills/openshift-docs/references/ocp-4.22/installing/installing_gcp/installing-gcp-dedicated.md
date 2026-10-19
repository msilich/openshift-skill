<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can install OpenShift Container Platform on Google Cloud Dedicated (GCD), a sovereign cloud platform that provides Google Cloud technology in a fully isolated environment with strict data and operational sovereignty guarantees.

# Prerequisites for installing a cluster on Google Cloud Dedicated

Installing OpenShift Container Platform on GCD requires a configured project with domain-scoped IDs, Workforce Identity Federation credentials, and network access to sovereign cloud API endpoints.

- You reviewed details about the [OpenShift Container Platform installation and update](../../architecture/architecture-installation.md#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../overview/installing-preparing.md#installing-preparing).

- You [configured a Google Cloud project](installing-gcp-account.md#installing-gcp-account) to host the cluster.

- You have a credential file for a GCD service account that includes the `universe_domain` field for your sovereign cloud region.

- If you use a firewall, you [configured access to the sites](../install_config/configuring-firewall.md#configuring-firewall-module_configuring-firewall) that your cluster requires, including the GCD API endpoints for your region.

# Google Cloud Dedicated overview

Google Cloud Dedicated (GCD) is a sovereign cloud platform that provides Google Cloud technology in a fully isolated environment with strict data and operational sovereignty guarantees.

OpenShift Container Platform supports deploying clusters to GCD sovereign cloud regions by using installer-provisioned infrastructure.

> [!NOTE]
> You cannot select a GCD sovereign cloud region by using the guided terminal prompts from the installation program. You must define the region and other GCD-specific parameters manually in the `install-config.yaml` file.

## Sovereign cloud framework

GCD is part of Google’s sovereign cloud strategy, which addresses data residency, administrative access control, and operational sovereignty. Google’s sovereign cloud portfolio includes the following tiers:

- Assured Workloads provides data residency controls within the public cloud.

- Sovereign Controls by Partners adds partner-managed key management and audits.

- GCD provides the highest level of sovereignty with fully isolated infrastructure operated by a regional partner.

Each GCD deployment is operated by a local partner who controls administrative access to the infrastructure. For example, in Germany, the main GCD partner is Thales.

## Key differences from public Google Cloud

GCD regions differ from public Google Cloud in the following ways that affect OpenShift Container Platform installation and operation:

Single region per universe
Each GCD deployment operates as a single region. Multi-region features such as cross-region load balancing and multi-region storage are not available. You must use multiple zones within the single region for high availability.

Different API endpoints
GCD uses API endpoints in the format `<service>.apis-<region-host>.goog` instead of `<service>.googleapis.com`. For example, the Berlin region uses `compute.apis-berlin-build0.goog` instead of `compute.googleapis.com`. Cluster Operators automatically detect the sovereign cloud environment and override standard `googleapis.com` endpoints.

Domain-scoped project IDs
All GCD project IDs carry a mandatory prefix, such as `eu0:`. For example, a project named `my-project` has the project ID `eu0:my-project`. You must include this prefix in all commands and configuration.

Different service account email format
Service account email addresses use GCD-specific domains instead of standard Google Cloud format.

Limited service availability
Only a subset of Google Cloud services is available. Older Compute Engine machine types, ARM-based instances, TPUs, and several other services are not available.

No default VPC
A default VPC network is not automatically created for new projects. You must create or configure a VPC explicitly.

## OpenShift Container Platform constraints on GCD

OpenShift Container Platform on GCD has constraints around machine types, disk types, operating system images, DNS, and endpoint configuration that differ from standard Google Cloud installations.

## Supported GCD regions

The following GCD sovereign cloud regions are supported for OpenShift Container Platform installation:

| Region | Identifier | Zones |
|----|----|----|
| Berlin, Germany | `u-germany-northeast1` | `u-germany-northeast1-a`, `u-germany-northeast1-b`, `u-germany-northeast1-c` |
| Eastern France | `u-france-east1` | `u-france-east1-a`, `u-france-east1-b`, `u-france-east1-c` |

GCD regions

> [!NOTE]
> Additional GCD regions might be supported in future releases. The architectural constraints, such as the single-region design, limited machine types, and different API endpoints, apply to all GCD regions.

# Limitations and considerations for Google Cloud Dedicated

GCD environments have specific constraints for machine types, storage, networking, and identity that differ from standard Google Cloud installations to maintain sovereignty and data isolation requirements.

## Machine types and disk types

GCD has the following limitations for machine types and disk types compared to public Google Cloud:

- Only the C3, M3, and A3 Edge machine series are available. The installation program defaults to `c3-standard-4` for all machine pools. If you specify a machine type from an unavailable series, the installation fails.

- Only the `hyperdisk-balanced` disk type is available. The installation program defaults to `hyperdisk-balanced` for sovereign cloud installations. Other disk types such as `pd-ssd`, `pd-standard`, and Local SSD are not available.

- The installation program validates disk type availability against the GCD API on a per-zone basis. If a disk type is not available in the specified zones, the installation fails with an error indicating the unavailable zones.

- ARM-based (aarch64) machine types and images are not available.

## Storage

GCD has the following storage limitations compared to public Google Cloud:

- You must change the default storage class to use `hyperdisk-balanced` after installation. The default storage class provisioned by the installation program uses `pd-ssd`, which is not available in GCD regions. For more information, see "Changing the default storage class".

- Cloud Storage is available but limited to single-region buckets only. Dual-region, multi-region, and bucket relocation are not available.

- Cloud Storage bucket locations must be set explicitly. There is no default bucket location in GCD.

- Google Cloud Filestore is not available.

## Operating system image

The Red Hat Enterprise Linux CoreOS (RHCOS) image is not pre-published in GCD regions. You must provide a custom operating system image that you uploaded to your GCD project.

In the `install-config.yaml` file, specify the operating system image by using the `platform.gcp.defaultMachinePlatform.osImage` field or the per-machine-pool fields for `osImage`. You must provide both the `name` and `project` fields. If these fields are not set, the installation fails.

<div class="formalpara">

<div class="title">

Example custom operating system image configuration

</div>

``` yaml
platform:
  gcp:
    defaultMachinePlatform:
      osImage:
        name: my-custom-rhcos
        project: eu0:my-image-project
```

</div>

## Networking

GCD has the following networking restrictions:

- Only private DNS zones are supported. Public DNS zones are not available in GCD. You must set the `publish` parameter to `Internal` in the `install-config.yaml` file.

- Private Service Connect (PSC) endpoint overrides are not supported. Do not set the `platform.gcp.endpoint` field in the `install-config.yaml` file. PSC endpoint overrides generate URLs targeting the `googleapis.com` domain, which is not compatible with GCD sovereign cloud environments. Features that depend on PSC endpoints, such as Hive, are not supported.

- A default VPC network is not automatically created for new GCD projects. You must create or specify a VPC network before installation.

## Identity and service accounts

GCD has the following identity and service account limitations compared to public Google Cloud:

- Email addresses for service accounts use a different domain format in GCD. For domain-scoped project IDs, such as `eu0:my-project`, the installation program generates service account emails in the format `<name>@<project-name>.<prefix>.iam.gserviceaccount.com` instead of the standard `<name>@<project-id>.iam.gserviceaccount.com`.

- Google Accounts and Google Groups are not supported for IAM bindings. Use a service account.

- The GCD credential file does not populate the `project_id` field. The installation program reads the project ID from the `platform.gcp.projectID` field in the `install-config.yaml` file instead.

## Encryption and Key Management Service

GCD has the following encryption and Key Management Service requirements:

- When you specify the `defaultMachinePlatform` field in the `install-config.yaml` file, the installation program encrypts both the image registry and the bootstrap ignition by using Key Management Service (KMS). Global KMS keys are not accepted. You must use regional KMS keys that reside in the same GCD region as your cluster.

- You must update Identity and Access Management (IAM) policies to grant the required permissions for your KMS keys before installation.

## Other limitations

GCD has the following additional limitations:

- The installation program automatically detects a GCD sovereign cloud environment based on the domain-scoped project ID prefix (such as `eu0:`) and the region prefix (such as `u-`).

- The universe domain from the GCD credentials is recorded on the cluster’s `Infrastructure` custom resource at `status.platformStatus.gcp.universeDomain`. Cluster components use this value to route API requests to the correct GCD endpoints.

- Multi-project installations that use Shared VPC (XPN) are not supported.

<div>

<div class="title">

Additional resources

</div>

- [Changing the default storage class](../../storage/dynamic-provisioning.md#change-default-storage-class_dynamic-provisioning)

- [GCE PersistentDisk (gcePD) object definition](../../storage/dynamic-provisioning.md#gce-persistentdisk-storage-class_dynamic-provisioning)

</div>

# Preparing your Google Cloud Dedicated environment

To ensure your OpenShift Container Platform cluster can authenticate and communicate with GCD’s isolated infrastructure, you configure project settings, credentials, and networking that comply with sovereignty requirements.

In addition to the standard Google Cloud project configuration, GCD requires configurations described in the following procedure.

<div>

<div class="title">

Prerequisites

</div>

- You have a GCD project with a domain-scoped project ID, such as `eu0:my-project`.

- You have a key file for a service account that contains the universe domain.

- You have a service account with the required permissions for OpenShift Container Platform installation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Confirm the following environment details with your GCD operating partner, such as Thales:

    - The region identifier for your GCD deployment, such as `u-germany-northeast1`.

    - The universe domain for your region, such as `apis-berlin-build0.goog`.

    - Your domain-scoped project ID, such as `eu0:my-project`.

    - Network connectivity requirements for your sovereign cloud region.

2.  Obtain the GCD credential configuration file for your service account. The credential file must include the `universe_domain` field that corresponds to your GCD region.

    Verify that your credential file contains the `universe_domain` field by running the following command:

    ``` terminal
    $ cat <path_to_credentials>/credentials.json | grep universe_domain
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
      "universe_domain": "apis-berlin-build0.goog"
    ```

    </div>

3.  Set the `GOOGLE_CLOUD_UNIVERSE_DOMAIN` environment variable to the universe domain for your GCD region by running the following command:

    ``` terminal
    $ export GOOGLE_CLOUD_UNIVERSE_DOMAIN=<universe_domain>
    ```

    where:

    `<universe_domain>`
    Specifies the universe domain for your GCD region. For the Berlin region, use `apis-berlin-build0.goog`.

4.  Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your GCD credential file by running the following command:

    ``` terminal
    $ export GOOGLE_APPLICATION_CREDENTIALS=<path_to_credentials>/credentials.json
    ```

    where:

    `<path_to_credentials>`
    Specifies the path to the directory that contains your GCD credential file.

5.  Verify that the required APIs are enabled in your GCD project:

    - Compute Engine API (`compute.googleapis.com`)

    - Cloud DNS API (`dns.googleapis.com`)

    - Cloud Storage API (`storage.googleapis.com`)

    - IAM API (`iam.googleapis.com`)

    - Service Usage API (`serviceusage.googleapis.com`)

    - Cloud Resource Manager API (`cloudresourcemanager.googleapis.com`)

    > [!NOTE]
    > GCD uses the same API service names as public Google Cloud for enabling and disabling APIs. The service endpoints, however, use the GCD-specific domain.

6.  Create a VPC network if one does not already exist by running the following command. GCD does not create a default VPC network for new projects.

    ``` terminal
    $ gcloud compute networks create <network_name> \
        --subnet-mode=custom \
        --project=<gcd_project_id>
    ```

    where:

    `<network_name>`
    Specifies the name of the VPC network to create.

    `<gcd_project_id>`
    Specifies your domain-scoped GCD project ID, such as `eu0:my-project`.

7.  Configure a private DNS zone for your cluster’s base domain by running the following command. GCD supports only private DNS zones.

    ``` terminal
    $ gcloud dns managed-zones create <zone_name> \
        --dns-name=<base_domain> \
        --description="Private DNS zone for OpenShift" \
        --visibility=private \
        --networks=<network_name> \
        --project=<gcd_project_id>
    ```

    where:

    `<zone_name>`
    Specifies a name for the DNS zone.

    `<base_domain>`
    Specifies the base domain for your cluster.

    `<network_name>`
    Specifies the name of the VPC network you created.

    `<gcd_project_id>`
    Specifies your domain-scoped GCD project ID, such as `eu0:my-project`.

8.  Prepare a custom Red Hat Enterprise Linux CoreOS (RHCOS) image for your GCD project. The RHCOS image is not pre-published in GCD regions. You must upload your own image:

    1.  Download the RHCOS image for your OpenShift Container Platform version from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/).

        Download the `gcp.x86_64.tar.gz` file for your version.

    2.  Create a Cloud Storage bucket in your GCD project to store the image by running the following command:

        ``` terminal
        $ gcloud storage buckets create gs://<bucket_name> \
            --location=<gcd_region> \
            --project=<gcd_project_id>
        ```

        where:

        `<bucket_name>`
        Specifies a unique name for the storage bucket.

        `<gcd_region>`
        Specifies your GCD region name, such as `u-germany-northeast1`.

        `<gcd_project_id>`
        Specifies your domain-scoped GCD project ID, such as `eu0:my-project`.

        > [!NOTE]
        > Cloud Storage in GCD is limited to single-region buckets. The bucket location must match your cluster region.

    3.  Upload the RHCOS image to your Cloud Storage bucket by running the following command:

        ``` terminal
        $ gcloud storage cp rhcos-<version>-gcp.x86_64.tar.gz \
            gs://<bucket_name>/ \
            --project=<gcd_project_id>
        ```

        Replace `<version>` with the version you downloaded.

    4.  Import the RHCOS image from Cloud Storage to create a Compute Engine image by running the following command:

        ``` terminal
        $ gcloud compute images create <image_name> \
            --source-uri=gs://<bucket_name>/rhcos-<version>-gcp.x86_64.tar.gz \
            --guest-os-features=GVNIC,UEFI_COMPATIBLE,VIRTIO_SCSI_MULTIQUEUE \
            --project=<gcd_project_id>
        ```

        where:

        `<image_name>`
        Specifies a name for the RHCOS image.

        `--source-uri`
        Specifies the Cloud Storage URI (`gs://`) where the image file was uploaded in the previous step. The `gs://` URI must point to the Cloud Storage bucket in your GCD project.

        `--guest-os-features`
        Specifies the guest operating system features required for RHCOS images. You must enable the `GVNIC`, `UEFI_COMPATIBLE`, and `VIRTIO_SCSI_MULTIQUEUE` features for proper network, UEFI boot support, and disk I/O performance.

        `<bucket_name>`
        Specifies the name of the Cloud Storage bucket you created.

        `<version>`
        Specifies the RHCOS version you downloaded.

        `<gcd_project_id>`
        Specifies your domain-scoped GCD project ID, such as `eu0:my-project`.

    5.  Note the image name and project ID. You must specify these values in the `platform.gcp.defaultMachinePlatform.osImage` fields of the `install-config.yaml` file.

</div>

# Internet access for OpenShift Container Platform

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

- Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.

- Access Quay.io to obtain the packages that are required to install your cluster.

- Obtain the packages that are required to perform cluster updates.

> [!IMPORTANT]
> If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

# Generating a key pair for cluster node SSH access

During an OpenShift Container Platform installation, you can provide an SSH public key to the installation program. The key is passed to Red Hat Enterprise Linux CoreOS (RHCOS) nodes through their Ignition config files and is added to `~/.ssh/authorized_keys` for the `core` user on each node.

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

    Specify the path and file name for your SSH private key, such as `~/.ssh/id_ed25519`.

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

Before you install OpenShift Container Platform, download the installation file on the host you are using for installation, so that installation assets exist for deployment in your environment.

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

3.  Back up the `install-config.yaml` file so that you can use it to install many clusters.

    > [!IMPORTANT]
    > Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Additional Google Cloud configuration parameters](installation-config-parameters-gcp.md#installation-configuration-parameters-additional-gcp_installation-config-parameters-gcp)

</div>

## Sample install-config.yaml file for Google Cloud Dedicated

You can configure disk types, encryption keys, and OS images specific to Google Cloud Dedicated (GCD) deployments in the `install-config.yaml` file.

<div class="formalpara">

<div class="title">

Example `install-config.yaml` file for GCD

</div>

``` yaml
apiVersion: v1
baseDomain: example.com
metadata:
  name: gcd-cluster
platform:
  gcp:
    projectID: eu0:my-project-id
    region: u-germany-northeast1
    defaultMachinePlatform:
      osDisk:
        diskType: hyperdisk-balanced
        encryptionKey:
          kmsKey:
            name: my-regional-key
            keyRing: my-key-ring
            location: u-germany-northeast1
            projectID: eu0:my-project-id
      osImage:
        project: eu0:my-project-id
        name: my-rhcos-image
publish: Internal
pullSecret: '{"auths": ...}'
sshKey: 'ssh-rsa AAAA...'
```

</div>

where:

`baseDomain`
Specifies the base domain for your cluster. Use a domain that you control.

`platform.gcp.projectID`
Specifies the Google Cloud project ID for your GCD environment. This value must include the domain-scoped prefix, such as `eu0:my-project-id`.

`platform.gcp.defaultMachinePlatform.osDisk.diskType`
Specifies the disk type for machine storage. For GCD, this value must be `hyperdisk-balanced`.

`platform.gcp.defaultMachinePlatform.osDisk.encryptionKey.kmsKey.name`
Specifies the name of your regional KMS key. In GCD, global keys are not supported.

`platform.gcp.defaultMachinePlatform.osImage.project`
Specifies the Google Cloud project ID where your custom RHCOS image is stored. This value is required. The RHCOS image is not pre-published in GCD regions.

`publish`
Specifies the cluster publishing strategy. For GCD, you must use `Internal`.

`pullSecret`
Specifies your Red Hat pull secret.

`sshKey`
Specifies your SSH public key for accessing cluster nodes.

> [!NOTE]
> Before you use a custom RHCOS image, verify that it is compatible with your OpenShift Container Platform version and has been properly imported into your GCD project.

## Minimum resource requirements for cluster installation

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

| Machine | Operating system | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
|----|----|----|----|----|----|
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Minimum resource requirements

- One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.

- OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance.

- As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines.

> [!NOTE]
> In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA):
>
> - x86-64 architecture requires x86-64-v2 ISA
>
> - ARM64 architecture requires ARMv8.0-A ISA
>
> - ppc64le architecture requires IBM® Power9 ISA
>
> - s390x architecture requires IBM® z14 ISA
>
> For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

<div>

<div class="title">

Additional resources

</div>

- [Optimizing storage](../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

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

# Alternatives to storing administrator-level secrets in the kube-system project

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must manage long-term cloud credentials manually.

## Manually creating long-term credentials

You can put the Cloud Credential Operator (CCO) into manual mode before OpenShift Container Platform installation if the cloud identity and access management (IAM) APIs are not reachable, or if you prefer not to store an administrator-level credential secret in the cluster `kube-system` namespace.

<div>

<div class="title">

Procedure

</div>

1.  Add the following granular permissions to the Google Cloud account that the installation program uses:

    - compute.machineTypes.list

    - compute.regions.list

    - compute.zones.list

    - dns.changes.create

    - dns.changes.get

    - dns.managedZones.create

    - dns.managedZones.delete

    - dns.managedZones.get

    - dns.managedZones.list

    - dns.networks.bindPrivateDNSZone

    - dns.resourceRecordSets.create

    - dns.resourceRecordSets.delete

    - dns.resourceRecordSets.list

2.  If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

    <div class="formalpara">

    <div class="title">

    Sample configuration file snippet

    </div>

    ``` yaml
    apiVersion: v1
    baseDomain: example.com
    credentialsMode: Manual
    # ...
    ```

    </div>

3.  If you have not previously created installation manifest files, do so by running the following command:

    ``` terminal
    $ openshift-install create manifests --dir <installation_directory>
    ```

    where `<installation_directory>` is the directory in which the installation program creates files.

4.  Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

    ``` terminal
    $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
    ```

5.  Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

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
        kind: GCPProviderSpec
        predefinedRoles:
        - roles/storage.admin
        - roles/iam.serviceAccountUser
        skipServiceCheck: true
      ...
    ```

    </div>

6.  Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.

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
      service_account.json: <base64_encoded_gcp_service_account_file>
    ```

    </div>

    > [!IMPORTANT]
    > Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.

</div>

# Installing the cluster

To deploy OpenShift Container Platform in a sovereign cloud environment with strict data isolation, you can install a cluster on Google Cloud Dedicated by configuring and running the installation program.

<div>

<div class="title">

Prerequisites

</div>

- You prepared your GCD environment.

- You obtained the OpenShift Container Platform installation program.

- You obtained the pull secret for your cluster.

- You obtained your GCD region name and custom API endpoints from your local operating partner, such as Thales.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an `install-config.yaml` file. You can generate a template file by running the following command or manually create the file:

    ``` terminal
    $ ./openshift-install create install-config --dir <installation_directory>
    ```

    Replace `<installation_directory>` with the name of the directory that contains the installation files for your cluster.

    > [!NOTE]
    > You cannot select a GCD sovereign cloud region by using the guided terminal prompts. You must manually edit the `install-config.yaml` file to configure GCD-specific parameters.

2.  Edit the `install-config.yaml` file to configure it for your GCD environment:

    > [!NOTE]
    > The installation program automatically detects the GCD sovereign cloud environment based on the region and the domain-scoped project ID in your credential file. You do not need to manually configure API endpoints.

    1.  Specify the GCD region:

        ``` yaml
        platform:
          gcp:
            region: <gcd_region_name>
        ```

    2.  Configure the cluster for private networking:

        ``` yaml
        publish: Internal
        ```

        where:

        `publish`
        Specifies the cluster publishing strategy. For GCD, you must use `Internal`. Public clusters are not supported.

    3.  Optional: If you need to provide a custom Red Hat Enterprise Linux CoreOS (RHCOS) image, add the compute platform image field:

        ``` yaml
        platform:
          gcp:
            defaultMachinePlatform:
              osImage:
                project: <project_id>
                name: <image_name>
        ```

        where:

        `platform.gcp.defaultMachinePlatform.osImage.project`
        Specifies the Google Cloud project ID where your custom RHCOS image is stored.

        `platform.gcp.defaultMachinePlatform.osImage.name`
        Specifies the name of your custom RHCOS image.

        > [!IMPORTANT]
        > You must specify a custom RHCOS image. The RHCOS image is not pre-published in GCD regions. If you do not provide the `osImage.name` and `osImage.project` fields, the installation fails.

    4.  Optional: Configure Customer-Managed Encryption Keys (CMEK) if required for regulatory compliance:

        > [!IMPORTANT]
        > When you use CMEK with GCD, you must use regional keys. Global keys are not supported.

        ``` yaml
        platform:
          gcp:
            defaultMachinePlatform:
              osDisk:
                encryptionKey:
                  kmsKey:
                    name: <regional_key_name>
                    keyRing: <key_ring_name>
                    location: <region_name>
                    projectID: <project_id>
        ```

        where:

        `platform.gcp.defaultMachinePlatform.osDisk.encryptionKey.kmsKey.name`
        Specifies a regional KMS key, not a global key.

    5.  Configure storage to use `hyperdisk-balanced` storage:

        ``` yaml
        platform:
          gcp:
            defaultMachinePlatform:
              osDisk:
                diskType: hyperdisk-balanced
        ```

        where:

        `platform.gcp.defaultMachinePlatform.osDisk.diskType`
        Specifies the disk type for machine storage. GCD supports only `hyperdisk-balanced` storage. Other disk types are not available.

3.  Back up the `install-config.yaml` file by running the following command:

    ``` terminal
    $ cp <installation_directory>/install-config.yaml <installation_directory>/install-config.yaml.backup
    ```

    > [!IMPORTANT]
    > The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up.

4.  Generate the Kubernetes manifests for the cluster by running the following command:

    ``` terminal
    $ ./openshift-install create manifests --dir <installation_directory>
    ```

5.  Deploy the OpenShift Container Platform cluster by running the following command:

    ``` terminal
    $ ./openshift-install create cluster --dir <installation_directory> --log-level=info
    ```

    > [!NOTE]
    > If you provided correct configuration values, the cluster creation process should complete successfully. However, the installation program might fail if it cannot validate your custom API endpoints or if there are connectivity issues with your GCD environment.

    When the cluster deployment is complete, the installation program displays information about accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.

    To verify that the cluster Operators are running, set the `KUBECONFIG` environment variable and check the cluster Operator status by running the following commands:

    ``` terminal
    $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
    ```

    ``` terminal
    $ oc get clusteroperators
    ```

    Verify that all cluster Operators show `AVAILABLE=True`, `PROGRESSING=False`, and `DEGRADED=False`.

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

<div>

<div class="title">

Additional resources

</div>

- [Accessing the web console](../../web_console/web-console.md#web-console)

</div>

# Telemetry access for OpenShift Container Platform

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

<div>

<div class="title">

Additional resources

</div>

- [About remote health monitoring](../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring)

</div>

# Additional resources

- [Customize your cluster](../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations)

- [Opt out of remote health reporting](../../support/remote_health_monitoring/remote-health-reporting.md#remote-health-reporting)
