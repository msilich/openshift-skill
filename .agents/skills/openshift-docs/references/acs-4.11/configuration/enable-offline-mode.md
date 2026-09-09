<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use Red Hat Advanced Cluster Security for Kubernetes for clusters that are not connected to the internet by enabling the offline mode. In offline mode, Red Hat Advanced Cluster Security for Kubernetes components do not connect to addresses or hosts on the internet.

> [!NOTE]
> Red Hat Advanced Cluster Security for Kubernetes does not find if the user-supplied hostnames, IP addresses, or other resources are on the internet. For example, if you try to integrate with a Docker registry hosted on the internet, Red Hat Advanced Cluster Security for Kubernetes will not block this request.

<a id="enable-offline-mode-deployment-steps_enable-offline-mode"></a>

# Deployment steps for offline mode

To deploy and operate Red Hat Advanced Cluster Security for Kubernetes in offline mode, complete the deployment steps and update procedures.

To deploy and operate Red Hat Advanced Cluster Security for Kubernetes in offline mode:

1.  Download RHACS images and install them in your clusters. If you are using OpenShift Container Platform, you can use Operator Lifecycle Manager (OLM) and the Software Catalog to download images to a workstation that connects to the internet. The workstation then pushes images to a mirror registry that also connects to your secured cluster. For other platforms, you can use a program such as Skopeo or Docker to pull the images from the remote registry and push them to your own private registry, as described in "Downloading images for offline use".

2.  Enable offline mode during installation.

3.  Update the vulnerability list for Scanner by uploading a new definitions file at least once per day.

> [!IMPORTANT]
> You can only enable offline mode during the installation, and not during an upgrade.

<div>

<div class="title">

Additional resources

</div>

- [Operator Lifecycle Manager (OLM)](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.21/html/operators/understanding-operators#operator-lifecycle-manager-olm)

- [Downloading images for offline use](enable-offline-mode.md#downloading-images-offline-overview_enable-offline-mode)

</div>

<a id="downloading-images-offline-overview_enable-offline-mode"></a>

# Downloading images for offline use

Before you can use RHACS in offline mode, you must download the required container images and make them available in your environment. The method you use depends on your platform and infrastructure.

If you are using OpenShift Container Platform, you can use Operator Lifecycle Manager (OLM) and the Software Catalog to download images to a workstation that connects to the internet. The workstation then pushes images to a mirror registry that also connects to your secured cluster.

For other platforms, you can use a program such as Skopeo or Docker to pull the images from the remote registry and push them to your own private registry.

<a id="image-versions_enable-offline-mode"></a>

## Image versions

You can manually pull, retag, and push Red Hat Advanced Cluster Security for Kubernetes (RHACS) images to your registry. The current version includes the following images:

<table>
<caption>Red Hat Advanced Cluster Security for Kubernetes images</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Image</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Current version</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Main</p></td>
<td style="text-align: left;"><p>Includes Central, Sensor, Admission controller, and Compliance components. Also includes <code>roxctl</code> for use in continuous integration (CI) systems.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:4.11.3</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Central DB</p></td>
<td style="text-align: left;"><p>PostgreSQL instance that provides the database storage for Central.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-central-db-rhel9:4.11.3</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Scanner</p></td>
<td style="text-align: left;"><p>Scans images and nodes.</p></td>
<td style="text-align: left;"><ul>
<li><p><code>registry.redhat.io/advanced-cluster-security/rhacs-scanner-rhel9:4.11.3</code></p></li>
<li><p><code>registry.redhat.io/advanced-cluster-security/rhacs-scanner-slim-rhel9:4.11.3</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Scanner DB</p></td>
<td style="text-align: left;"><p>Stores image scan results and vulnerability definitions.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-scanner-db-rhel9:4.11.3</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Scanner V4</p></td>
<td style="text-align: left;"><p>Scans images.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-scanner-v4-rhel9:4.11.3</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Scanner V4 DB</p></td>
<td style="text-align: left;"><p>Stores image scan results and vulnerability definitions for Scanner V4.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-scanner-v4-db-rhel9:4.11.3</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Collector</p></td>
<td style="text-align: left;"><p>Collects runtime activity in Kubernetes or OpenShift Container Platform clusters.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-collector-rhel9:4.11.3</code></p></td>
</tr>
</tbody>
</table>

<a id="topic-name_enable-offline-mode"></a>

### Retagging images

You can download and retag images using the Docker command-line interface.

> [!IMPORTANT]
> When you retag an image, you must maintain the name of the image and the tag. For example, use:
>
> ``` terminal
> $ docker tag registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:4.11.3 <your_registry>/rhacs-main-rhel9:4.11.3
> ```
>
> and do not retag like the following example:
>
> ``` terminal
> $ docker tag registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:4.11.3 <your_registry>/other-name:latest
> ```

<div>

<div class="title">

Procedure

</div>

1.  Log in to the registry:

    ``` terminal
    $ docker login registry.redhat.io
    ```

2.  Pull the image:

    ``` terminal
    $ docker pull <image>
    ```

3.  Retag the image:

    ``` terminal
    $ docker tag <image> <new_image>
    ```

4.  Push the updated image to your registry:

    ``` terminal
    $ docker push <new_image>
    ```

</div>

<a id="enabling-offline-mode-installation-overview_enable-offline-mode"></a>

# Enabling offline mode during installation

You can enable offline mode during the installation of Red Hat Advanced Cluster Security for Kubernetes. After offline mode is enabled, RHACS components do not connect to addresses or hosts on the internet.

<a id="enable-offline-mode-operator_enable-offline-mode"></a>

## Enabling offline mode when installing by using the Operator

You can enable offline mode when installing Red Hat Advanced Cluster Security for Kubernetes (RHACS) by using the Operator method. In offline mode, RHACS components do not connect to addresses or hosts on the internet.

<div>

<div class="title">

Prerequisites

</div>

- You have configured a private container or mirror registry with the required RHACS images. See "Using Operator Lifecycle Manager in disconnected environments".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Install the Red Hat Advanced Cluster Security for Kubernetes Operator following the instructions in "Installing the Red Hat Advanced Cluster Security for Kubernetes Operator".

2.  On the OpenShift Container Platform web console, go to the **Ecosystem** → **Installed Operators** page.

3.  Select the Red Hat Advanced Cluster Security for Kubernetes Operator from the list of installed Operators.

4.  If you have installed the Operator in the recommended namespace, OpenShift Container Platform lists the project as `rhacs-operator`. Select **Project: rhacs-operator** → **Create project**.

    > [!NOTE]
    > If you installed the Operator in a different namespace, OpenShift Container Platform lists the name of that namespace instead of `rhacs-operator`.

5.  Enter the new project name (for example, `stackrox`), and click **Create**. Red Hat recommends that you use `stackrox` as the project name.

6.  Under the **Provided APIs** section, select **Central**. Click **Create Central**.

7.  Take one of the following actions to configure offline mode. In this mode, RHACS does not automatically download or update vulnerability definitions or other data. You must manually download these and provide them to RHACS if you have configured it to run in offline mode.

    - To configure offline mode by using the portal, select **Form view** in the **Configure via** field.

      1.  Locate the **Egress** setting. This setting indicates if the system allows outgoing network traffic.

      2.  In the **Connectivity Policy** field, select **Offline** to indicate that RHACS should run in offline (disconnected) mode.

    - To configure offline mode by editing the YAML CR, select **YAML view** in the **Configure via** field.

      1.  Add `egress.connectivityPolicy: Offline` to the file as shown in the following example:

          ``` yaml
          apiVersion: platform.stackrox.io/v1alpha1
          kind: Central
          metadata:
            name: stackrox-central-services
            namespace: stackrox
          spec:
            egress:
              connectivityPolicy: Offline
          ```

8.  Click **Create**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Using Operator Lifecycle Manager in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/operators/administrator-tasks#olm-restricted-networks)

- [Installing the Red Hat Advanced Cluster Security for Kubernetes Operator](../installing/installing_ocp/install-central-ocp.md#install-acs-operator_install-central-ocp)

</div>

<a id="enable-offline-mode-helm_enable-offline-mode"></a>

## Enabling offline mode by using Helm configuration

You can enable offline mode during the installation when you are installing Red Hat Advanced Cluster Security for Kubernetes by using a Helm chart.

<div>

<div class="title">

Procedure

</div>

1.  When installing the central-services Helm chart, set the value of the `env.offlineMode` environmental variable to `true` in the `values-public.yaml` configuration file.

2.  When installing the secured-cluster-services Helm chart, set the value of the `config.offlineMode` parameter to `true` in the `values-public.yaml` configuration file.

</div>

<a id="enable-offline-mode-roxctl_enable-offline-mode"></a>

## Enabling offline mode by using the roxctl CLI

You can enable offline mode when you are installing Red Hat Advanced Cluster Security for Kubernetes by using the `roxctl` CLI.

<div>

<div class="title">

Procedure

</div>

1.  If you are using a registry other than the default internet-connected registry (`registry.redhat.io`), provide the locations where you have pushed the Red Hat Advanced Cluster Security for Kubernetes images when answering the `image to use` prompts:

    ``` terminal
    Enter main image to use (if unset, the default will be used): <your_registry>/rhacs-main-rhel9:4.11.3
    ```

    > [!NOTE]
    > The default image depends on your answer for the prompt `Enter default container images settings:`. If you entered `rhacs`, the default option, the default image will be `registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:4.11.3`.

    ``` terminal
    Enter Scanner DB image to use (if unset, the default will be used): <your_registry>/rhacs-scanner-db-rhel9:4.11.3
    ```

    ``` terminal
    Enter Scanner image to use (if unset, the default will be used): <your_registry>/rhacs-scanner-rhel9:4.11.3
    ```

2.  To enable the offline mode, enter `true` when answering the `Enter whether to run StackRox in offline mode` prompt:

    ``` terminal
    Enter whether to run StackRox in offline mode, which avoids reaching out to the internet (default: "false"): true
    ```

3.  Later, when you add Sensor to a remote cluster in the **Platform Configuration** → **Clusters** view in the RHACS portal, you must specify your the Collector image name in the **Collector Image Repository** field.

</div>

<a id="updating-scanner-definitions-offline-overview_enable-offline-mode"></a>

# Updating Scanner definitions in offline mode

Scanner maintains a database of vulnerabilities. When Red Hat Advanced Cluster Security for Kubernetes (RHACS) runs in normal mode, Central retrieves the latest vulnerability data from the internet, and Scanner retrieves vulnerability data from Central.

However, if you are using RHACS in offline mode, you must manually update the vulnerability data. To manually update the vulnerability data, you must upload a definitions file to Central, and Scanner then retrieves the vulnerability data from Central.

In both online and offline mode, Scanner checks for new data from Central every 5 minutes by default. In online mode, Central also checks for new data from the internet approximately every 5-20 minutes.

The offline data source is updated approximately every 3 hours. After the data has been uploaded to Central, Scanner downloads the data and updates its local vulnerability database.

To update the definitions in offline mode, you must download the definitions and then upload them to Central.

<a id="download-scanner-definitions_enable-offline-mode"></a>

## Downloading Scanner definitions

If you are running Red Hat Advanced Cluster Security for Kubernetes in offline mode, you can download the vulnerability definitions database that Scanner uses and then upload it to Central.

<div>

<div class="title">

Prerequisites

</div>

- To download Scanner definitions, you need a system with internet access.

</div>

<div>

<div class="title">

Procedure

</div>

- To download the definitions, perform one of the following actions:

  - Recommended: Beginning with RHACS version 4.4, use the `roxctl scanner download-db --scanner-db-file scanner-vuln-updates.zip` command to download the definitions.

  - Go to the "Scanner vulnerability definitions database" to download the definitions.

</div>

<div>

<div class="title">

Additional resources

</div>

- [roxctl scanner download-db](../cli/command-reference/roxctl-scanner.md#roxctl-scanner-download-db_roxctl-scanner)

- [Scanner vulnerability definitions database](https://install.stackrox.io/scanner/scanner-vuln-updates.zip)

</div>

<a id="uploading-scanner-definitions-overview_enable-offline-mode"></a>

## Uploading definitions to Central

To upload Scanner definitions to Central, you can either use an API token or your administrator password. Red Hat recommends using an authentication token in a production environment because each token is assigned specific access control permissions.

<a id="upload-definitions-to-central-api-token_enable-offline-mode"></a>

### Uploading definitions to Central by using an API token

You can upload the vulnerability definitions database that Scanner uses to Central by using an API token.

<div>

<div class="title">

Prerequisites

</div>

- You must have an API token with the administrator role.

- You must have installed the `roxctl` command-line interface (CLI).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the `ROX_API_TOKEN` and the `ROX_CENTRAL_ADDRESS` environment variables:

    ``` terminal
    $ export ROX_API_TOKEN=<api_token>
    ```

    ``` terminal
    $ export ROX_CENTRAL_ADDRESS=<address>:<port_number>
    ```

2.  Run the following command to upload the definitions file:

    ``` terminal
    $ roxctl scanner upload-db \
      -e "$ROX_CENTRAL_ADDRESS" \
      --scanner-db-file=<compressed_scanner_definitions.zip>
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Authenticating by using the roxctl CLI](../cli/using-the-roxctl-cli.md#authenticating-by-using-the-roxctl-cli_using-roxctl-cli)

</div>

<a id="upload-definitions-to-central-admin-pass_enable-offline-mode"></a>

### Uploading definitions to Central by using the administrator password

You can upload the vulnerability definitions database that Scanner uses to Central by using your Red Hat Advanced Cluster Security for Kubernetes administrator password.

<div>

<div class="title">

Prerequisites

</div>

- You must have the administrator password.

- You must have installed the `roxctl` command-line interface (CLI).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the `ROX_CENTRAL_ADDRESS` environment variable:

    ``` terminal
    $ export ROX_CENTRAL_ADDRESS=<address>:<port_number>
    ```

2.  Run the following command to upload the definitions file:

    ``` terminal
    $ roxctl scanner upload-db \
      -p <your_administrator_password> \
      -e "$ROX_CENTRAL_ADDRESS" \
      --scanner-db-file=<compressed_scanner_definitions.zip>
    ```

</div>

<a id="update-kernel-support-packages_enable-offline-mode"></a>

# Updating kernel support packages in offline mode

In offline mode, you can manually download and upload kernel support packages containing probes for Linux kernel versions to Central. Collectors then download these probes from Central.

> [!NOTE]
> Support packages are deprecated and have no effect on secured clusters running version 4.5 or later. Support package uploads only affect secured clusters on version 4.4 and earlier.

Collector monitors the runtime activity for each node in your secured clusters. To monitor the activities, Collector requires probes in the form of eBPF programs.

With the `CORE_BPF` collection method, the probe is not specific to any kernel version, and can still be used after the underlying kernel has been updated. This collection method does not require you to provide or update a support package.

Instead, when you use the collection method `EBPF`, the probes are specific to the Linux kernel version installed on the host. The Collector image contains a set of built-in probes for the kernels supported at release time. However, later kernels will require newer probes.

When Red Hat Advanced Cluster Security for Kubernetes runs in normal mode (connected to the internet), Collector automatically downloads a new probe if the required probe is not built in.

In offline mode, you can manually download packages containing probes for all recent and supported Linux kernel versions and upload them to Central. Collectors then download these probes from Central.

Collector checks for the new probes in the following order. It checks:

1.  The existing Collector image.

2.  The kernel support package (if you have uploaded one to Central).

3.  A Red Hat-operated server available on the internet. Collector uses Central’s network connection to check and download the probes.

If Collector does not get new probes after checking, it reports a `CrashLoopBackoff` event.

If your network configuration restricts outbound traffic, you can manually download packages containing probes for all recent and supported Linux kernel versions and upload them to Central. Collectors then download these probes from Central, thus avoiding any outbound internet access.

<a id="download-kernel-support-package_enable-offline-mode"></a>

## Downloading kernel support packages

If you are running Red Hat Advanced Cluster Security for Kubernetes in offline mode, you can download packages containing probes for all recent and supported Linux kernel versions and then upload them to Central.

> [!NOTE]
> Support packages are deprecated and have no effect on secured clusters running version 4.5 or later. Support package uploads only affect secured clusters on version 4.4 and earlier.

<div>

<div class="title">

Procedure

</div>

- View and download available support packages from the "Kernel support packages index page". The kernel support packages list categorizes support packages based on Red Hat Advanced Cluster Security for Kubernetes version.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Kernel support packages index page](https://install.stackrox.io/collector/support-packages/index.html)

</div>

<a id="upload-kernel-support-package-to-central_enable-offline-mode"></a>

## Uploading kernel support packages to Central

You can upload the kernel support packages containing probes for all recent and supported Linux kernel versions to Central.

When uploading packages, consider the following guidance:

- When you upload a new support package that includes content uploaded to Central before, the upload only includes new files.

- When you upload a new support package that has files with the same name but different contents than those present on the Central, `roxctl` shows a warning message and does not overwrite files.

- You can use the `--overwrite` option with the upload command to overwrite the files.

- When you upload a support package that has a required probe, Central does not make any outbound requests to the internet for downloading this probe. Central uses the probe from the support package.

<div>

<div class="title">

Prerequisites

</div>

- You must have an API token with the administrator role.

- You must have installed the `roxctl` command-line interface (CLI).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the `ROX_API_TOKEN` and the `ROX_CENTRAL_ADDRESS` environment variables:

    ``` terminal
    $ export ROX_API_TOKEN=<api_token>
    ```

    ``` terminal
    $ export ROX_CENTRAL_ADDRESS=<address>:<port_number>
    ```

2.  Run the following command to upload the kernel support packages:

    ``` terminal
    $ roxctl collector support-packages upload <package_file> \
      -e "$ROX_CENTRAL_ADDRESS"
    ```

</div>
