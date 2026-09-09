<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With Red Hat Advanced Cluster Security for Kubernetes, you can analyze images for vulnerabilities by using the RHACS Scanner V4, or you can [configure an integration](../integration/integrate-with-image-vulnerability-scanners.md) to use another supported scanner.

<a id="scanning-about_examine-images-for-vulnerabilities"></a>

# Scanning in RHACS

RHACS scanners analyze each image layer to find packages and match them against known vulnerabilities by comparing them with a vulnerability database populated from different sources. These sources include Red Hat Vulnerability Exchange (VEX), the National Vulnerability Database (NVD), the Open Source Vulnerabilities (OSV) database, and operating system vulnerability feeds.

> [!NOTE]
> RHACS uses the OSV database available at [OSV.dev](https://osv.dev/) under [Apache License 2.0](https://github.com/google/osv.dev/blob/master/LICENSE).

RHACS contains two scanners: Scanner V4 and the StackRox Scanner.

Scanner V4, built on Claircore, is the default scanner as of release 4.8. The StackRox Scanner, which originates from a fork of the Clair v2 open source scanner, is deprecated. Although the StackRox Scanner is deprecated, it still must be enabled on the cluster where Central is installed due to software dependencies.

> [!NOTE]
> When this documentation uses the term "RHACS scanner" or "Scanner", it refers to Scanner V4.

When the RHACS scanner finds any vulnerabilities, it performs the following actions:

- Shows them in the [**Vulnerability Management**](manage-vulnerabilities/common-vuln-management-tasks.md) view for detailed analysis

- Ranks vulnerabilities according to risk and highlights them in the RHACS portal for risk assessment

- Checks them against enabled [security policies](manage_security_policies/about-security-policies.md)

The RHACS scanner inspects the images and identifies the installed components based on the files in the images. It might fail to identify installed components or vulnerabilities if the final images are modified to remove the following files:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Components</th>
<th style="text-align: left;">Files</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Package managers</p></td>
<td style="text-align: left;"><ul>
<li><p><code>/etc/alpine-release</code></p></li>
<li><p><code>/etc/lsb-release</code></p></li>
<li><p><code>/etc/os-release</code> or <code>/usr/lib/os-release</code></p></li>
<li><p><code>/etc/oracle-release</code>, <code>/etc/centos-release</code>, <code>/etc/redhat-release</code>, or <code>/etc/system-release</code></p></li>
<li><p>Other similar system files.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Language-level dependencies</p></td>
<td style="text-align: left;"><ul>
<li><p><code>package.json</code> for JavaScript.</p></li>
<li><p><code>dist-info</code> or <code>egg-info</code> for Python.</p></li>
<li><p><code>MANIFEST.MF</code> in Java Archive (JAR) for Java.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Application-level dependencies</p></td>
<td style="text-align: left;"><ul>
<li><p><code>dotnet/shared/Microsoft.AspNetCore.App/</code></p></li>
<li><p><code>dotnet/shared/Microsoft.NETCore.App/</code></p></li>
</ul></td>
</tr>
</tbody>
</table>

<a id="about-scanner-v4_examine-images-for-vulnerabilities"></a>

# About Scanner V4

RHACS provides its own scanner, Scanner V4, or you can configure an integration to use RHACS with another vulnerability scanner.

Built on [Claircore](https://github.com/quay/claircore), Scanner V4 provides scanning for language and operating system-specific image components and scanning Red Hat Enterprise Linux CoreOS (RHCOS).

> [!NOTE]
> Beginning with release 4.6, due to changes in vulnerability sources used, Scanner V4 only considers vulnerabilities affecting Red Hat products dated back to 2014. Previously, when reading Red Hat’s OVAL data, the vulnerabilities dated back to before 2000.

<a id="scannerv4-enabling_examine-images-for-vulnerabilities"></a>

# Enabling Scanner V4

Scanner V4 is enabled by default when RHACS is newly installed. However, if you have not previously enabled Scanner V4 and are upgrading from version 4.7 or earlier, you must enable it explicitly during the upgrade to use it.

You can enable Scanner V4 after installation by using the Operator or Helm.

<a id="enabling-scanner-v4-after-operator-installation-central_examine-images-for-vulnerabilities"></a>

## Enabling RHACS Scanner V4 for Central after Operator installation

If Scanner V4 was not enabled during installation, you can enable it after installation.

<div>

<div class="title">

Procedure

</div>

1.  In the cluster where Central is installed, in the console, click **Ecosystem** → **Installed Operators** and select the RHACS Operator.

2.  Click **Central** in the menu bar.

3.  Click the name of the cluster where Central was installed. The default value is **stackrox-central-services**.

4.  Click the **YAML** tab.

5.  Edit the YAML file as shown in the following example:

    ``` yaml
      scannerV4:
        scannerComponent: Enabled
    ```

</div>

<a id="enabling-scanner-v4-after-operator-installation-secured-cluster_examine-images-for-vulnerabilities"></a>

## Enabling RHACS Scanner V4 on the secured cluster after Operator installation

You can enable Scanner V4 after installation.

<div>

<div class="title">

Prerequisite

</div>

- You set up Central and the secured cluster by using a CRS or an init bundle so that they can communicate with each other.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the secured cluster, click **Ecosystem** → **Installed Operators** and select the RHACS Operator.

2.  Click **Secured Cluster** in the menu bar.

3.  Click the default cluster name, **stackrox-secured-cluster-services**, or the name that you entered during installation.

4.  Click the **YAML** tab.

5.  Edit the YAML file as shown in the following example:

    ``` yaml
      scannerV4:
        scannerComponent: AutoSense
    ```

</div>

<a id="enabling-scanner-v4-after-helm-installation-central_examine-images-for-vulnerabilities"></a>

## Enabling RHACS Scanner V4 for Central when upgrading by using Helm

You can enable Scanner V4 when upgrading by using Helm by enabling setting the `scannerV4.disable` parameter to `false`.

<div>

<div class="title">

Procedure

</div>

1.  On the cluster where Central is installed, run the following command, using the instructions in "Changing configuration options after deploying the central-services Helm chart" if you need more information:

    ``` terminal
    $ helm upgrade -n stackrox \
        stackrox-central-services rhacs/central-services \
        --reuse-values \
        -f <path_to_values_public.yaml> \
        -f <path_to_generated-values.yaml> \
        --set scannerV4.disable=false
    ```

    where:

    \<path_to_generated-values.yaml\>  
    Specifies the path to the generated values YAML file. When updating the system and installing a new component, you must provide the internal CA. See "Retrieving the automatically generated certificate authority".

</div>

<a id="enabling-scanner-v4-after-helm-installation-secured-cluster_examine-images-for-vulnerabilities"></a>

## Enabling RHACS Scanner V4 on the secured cluster when upgrading by using Helm

You can enable Scanner V4 when upgrading by using Helm.

<div>

<div class="title">

Prerequisites

</div>

- You set up Central and the secured cluster by using a CRS or an init bundle so that they can communicate with each other.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On the secured cluster, run the following command, using the instructions in "Configuring the secured-cluster-services Helm chart with customizations" if you need more information:

    ``` terminal
    $ helm upgrade -n stackrox \
        stackrox-central-services rhacs/secured-cluster-services \
        --reuse-values \
        -f <path_to_values_public.yaml> \
        -f <path_to_generated-values.yaml> \
        --set scannerV4.disable=false
    ```

    where:

    \<path_to_generated-values.yaml\>  
    Specifies the path to the generated values YAML file. When updating the system and installing a new component, you must provide the internal CA. See "Retrieving the automatically generated certificate authority".

</div>

<div>

<div class="title">

Additional resources

</div>

- [Changing configuration options after deploying the central-services Helm chart](../installing/installing_ocp/install-central-ocp.md#change-config-options-after-deployment-central-services_install-central-ocp)

- [Retrieving the automatically generated certificate authority](../installing/installing_ocp/install-central-ocp.md#automatically-generated-ca_install-central-ocp)

- [Upgrading using Helm charts](../upgrading/upgrade-helm.md)

</div>

<a id="scanning-images_examine-images-for-vulnerabilities"></a>

# Scanning images

Scanner V4 is the default scanner for RHACS. When scanning, it performs the following actions:

- Central requests the Scanner V4 Indexer to download and index (analyze) given images.

- Scanner V4 Indexer pulls image metadata from registries to determine the layers of the image, and downloads each previously unindexed layer.

- Scanner V4 Indexer requests mapping files from Central that assist the indexing process. Scanner V4 Indexer produces in an index report.

- Central requests that Scanner V4 Matcher match given images to known vulnerabilities. This process results in the final scan result: a vulnerability report. Scanner V4 Matcher requests the latest vulnerabilities from Central.

- Scanner V4 Matcher requests the results of the image indexing, the index report, from Scanner V4 Indexer. It then uses the report to determine relevant vulnerabilities. This interaction occurs only when the image is indexed in the Central cluster. This interaction does not occur when Scanner V4 is matching vulnerabilities for images indexed in secured clusters.

- The Indexer stores data in the Scanner V4 DB that is related to the indexing results to ensure that image layers are only downloaded and indexed once. This prevents unnecessary network traffic and other resource utilization.

- When secured cluster scanning is enabled, Sensor requests Scanner V4 to index images. Scanner V4 Indexer requests mapping files from Sensor that assist the indexing process unless Central exists in the same namespace. In that case, Central is contacted instead.

<a id="common-scanner-warning-messages_examine-images-for-vulnerabilities"></a>

## Understanding and addressing common Scanner warning messages

When scanning images with Red Hat Advanced Cluster Security for Kubernetes (RHACS), you might see the `CVE DATA MAY BE INACCURATE` warning message. Scanner displays this message when it cannot retrieve complete information about the operating system or other packages in the image.

The following table shows some common Scanner warning messages:

<table>
<caption>Warning messages</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Message</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>Unable to retrieve the OS CVE data, only Language CVE data is available</code></p></td>
<td style="text-align: left;"><p>Indicates that Scanner does not officially support the base operating system of the image; therefore, it cannot retrieve CVE data for the operating system-level packages.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Stale OS CVE data</code></p></td>
<td style="text-align: left;"><p>Indicates that the base operating system of the image has reached end-of-life, which means the vulnerability data is outdated. For example, Debian 8 and 9.</p>
<p>For more information about the files needed to identify the components in the images, see <a href="examine-images-for-vulnerabilities.md">Examining images for vulnerabilities</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Failed to get the base OS information</code></p></td>
<td style="text-align: left;"><p>Indicates that Scanner scanned the image, but was unable to determine the base operating system used for the image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Failed to retrieve metadata from the registry</code></p></td>
<td style="text-align: left;"><p>Indicates that the target registry is unreachable on the network. The cause could be a firewall blocking <code>docker.io</code>, or an authentication issue preventing access.</p>
<p>To analyze the root cause, create a special registry integration for private registries or repositories to get the pod logs for RHACS Central. For instructions on how to do this, see <a href="../integration/integrate-with-image-registries.md">Integrating with image registries</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Image out of scope for Red Hat Vulnerability Scanner Certification</code></p></td>
<td style="text-align: left;"><p>Indicates that Scanner scanned the image, but the image is old and does not fall within the scope of Red Hat Scanner Certification. For more information, see <a href="https://redhat-connect.gitbook.io/partner-guide-red-hat-vulnerability-scanner-cert/">Partner Guide for Red Hat Vulnerability Scanner Certification</a>.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>If you are using a Red Hat <a href="https://catalog.redhat.com/software/containers/explore">container image</a>, consider using a base image newer than June 2020.</p>
</div></td>
</tr>
</tbody>
</table>

<a id="supported-operating-systems_examine-images-for-vulnerabilities"></a>

## Supported operating systems

The supported platforms listed in this section are the distributions in which Scanner identifies vulnerabilities, and it is different from the supported platforms on which you can install Red Hat Advanced Cluster Security for Kubernetes.

Scanner identifies vulnerabilities in images that contain the following Linux distributions. For more information about the vulnerability databases used, see "Vulnerability sources" in "RHACS Architecture".

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Distribution</th>
<th style="text-align: left;">Version</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><a href="https://www.alpinelinux.org/">Alpine Linux</a></p></td>
<td style="text-align: left;"><p><code>alpine:3.2</code><sup>[1]</sup>,<code>alpine:3.3</code>, <code>alpine:3.4</code>, <code>alpine:3.5</code>, <code>alpine:3.6</code>, <code>alpine:3.7</code>, <code>alpine:3.8</code>, <code>alpine:3.9</code>, <code>alpine:3.10</code>, <code>alpine:3.11</code>, <code>alpine:3.12</code>, <code>alpine:3.13</code>, <code>alpine:3.14</code>, <code>alpine:3.15</code>, <code>alpine:3.16</code>, <code>alpine:3.17</code>, <code>alpine:3.18</code>, <code>alpine:3.19</code>, <code>alpine:3.20</code>, <code>alpine:3.21</code><sup>[2]</sup>, <code>alpine:3.22</code><sup>[2]</sup>, <code>alpine:edge</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://aws.amazon.com/amazon-linux-ami">Amazon Linux</a></p></td>
<td style="text-align: left;"><p><code>amzn:2018.03</code>, <code>amzn:2</code>, <code>amzn:2023</code><sup>[2]</sup></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>CentOS</p></td>
<td style="text-align: left;"><p><code>centos:6</code><sup>[1]</sup>, <code>centos:7</code><sup>[1]</sup>, <code>centos:8</code><sup>[1]</sup></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://www.debian.org/releases/">Debian</a></p></td>
<td style="text-align: left;"><p><code>debian:11</code>, <code>debian:12</code>, <code>debian:13</code><sup>[2]</sup>, <code>debian:unstable</code><sup>[1]</sup>, <a href="https://github.com/GoogleContainerTools/distroless"><code>Distroless</code></a></p>
<p>The following vulnerability sources are not updated by the vendor: <code>debian:8</code><sup>[1]</sup>, <code>debian:9</code><sup>[1]</sup>, <code>debian:10</code><sup>[1]</sup></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://www.oracle.com/linux/">Oracle Linux</a></p></td>
<td style="text-align: left;"><p><code>ol:5</code><sup>[2]</sup>, <code>ol:6</code><sup>[2]</sup>, <code>ol:7</code><sup>[2]</sup>, <code>ol:8</code><sup>[2]</sup>, <code>ol:9</code><sup>[2]</sup></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://vmware.github.io/photon/assets/files/html/3.0/Introduction.html">Photon OS</a></p></td>
<td style="text-align: left;"><p><code>photon:1.0</code><sup>[2]</sup>, <code>photon:2.0</code><sup>[2]</sup>, <code>photon:3.0</code><sup>[2]</sup></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux">Red Hat Enterprise Linux (RHEL)</a></p></td>
<td style="text-align: left;"><p><code>rhel:6</code><sup>[3]</sup>, <code>rhel:7</code><sup>[3]</sup>, <code>rhel:8</code><sup>[3]</sup>, <code>rhel:9</code>, <code>rhel:10</code><sup>[2]</sup></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://www.suse.com/">SUSE</a></p></td>
<td style="text-align: left;"><p><code>sles:11</code><sup>[2]</sup>, <code>sles:12</code><sup>[2]</sup>, <code>sles:15</code><sup>[2]</sup>, <code>opensuse-leap:15.5</code><sup>[2]</sup>, <code>opensuse-leap:15.6</code><sup>[2]</sup></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="http://releases.ubuntu.com/">Ubuntu</a></p></td>
<td style="text-align: left;"><p><code>ubuntu:14.04</code>, <code>ubuntu:16.04</code>, <code>ubuntu:18.04</code>, <code>ubuntu:20.04</code>, <code>ubuntu:22.04</code>, <code>ubuntu:24.04</code>, ubuntu:25.04`<sup>[2]</sup></p>
<p>The following vulnerability sources are not updated by the vendor: <code>ubuntu:12.04</code><sup>[1]</sup>, <code>ubuntu:12.10</code><sup>[1]</sup>, <code>ubuntu:13.04</code><sup>[1]</sup>, <code>ubuntu:14.10</code><sup>[1]</sup>, <code>ubuntu:15.04</code><sup>[1]</sup>, <code>ubuntu::15.10</code><sup>[1]</sup>, <code>ubuntu::16.10</code><sup>[1]</sup>, <code>ubuntu:17.04</code><sup>[1]</sup>, <code>ubuntu:17.10</code><sup>[1]</sup>, <code>ubuntu:18.10</code><sup>[1]</sup>, <code>ubuntu:19.04</code><sup>[1]</sup>, <code>ubuntu:19.10</code><sup>[1]</sup>, <code>ubuntu:20.10</code><sup>[1]</sup>, <code>ubuntu:21.04</code><sup>[1]</sup>, <code>ubuntu:21.10</code><sup>[1]</sup>, <code>ubuntu:22.10</code><sup>[1]</sup>, <code>ubuntu:23.04</code><sup>[1]</sup>, <code>ubuntu:23.10</code><sup>[1]</sup>, <code>ubuntu:24.10</code><sup>[1]</sup></p></td>
</tr>
</tbody>
</table>

1.  Only supported in the StackRox Scanner.

2.  Only supported in Scanner V4.

3.  Images older than June 2020 are not supported in Scanner V4.

> [!NOTE]
> Scanner does not support the Fedora operating system because Fedora does not maintain a vulnerability database. However, Scanner still detects language-specific vulnerabilities in Fedora-based images.

<a id="supported-package-formats_examine-images-for-vulnerabilities"></a>

## Supported package formats

Scanner can check for vulnerabilities in images that use the following package formats:

| Package format | Package managers        |
|----------------|-------------------------|
| apk            | apk                     |
| dpkg           | apt, dpkg               |
| rpm            | dnf, microdnf, rpm, yum |

<a id="supported-programming-languages_examine-images-for-vulnerabilities"></a>

## Supported programming languages

Scanner can check for vulnerabilities in dependencies for the following programming languages:

| Programming language | Package format |
|----|----|
| Go<sup>\[1\]</sup> | Binaries: The standard library version used to build the binary is analyzed. If the binaries are built with module support (go.mod), then the dependencies are also analyzed. |
| Java | JAR, WAR, EAR, JPI, HPI |
| JavaScript | package.json |
| Python | egg, wheel |
| Ruby | gem |

1.  Only supported in Scanner V4.

<a id="supported-layer-compression-formats_examine-images-for-vulnerabilities"></a>

## Supported layer compression formats

Container image layers are `.tar` file archives that might be compressed or uncompressed. StackRox Scanner and Scanner V4 support different formats as shown in the following table:

| Format         | StackRox Scanner Support | Scanner V4 Support |
|----------------|--------------------------|--------------------|
| No compression | Yes                      | Yes                |
| bzip2          | Yes                      | Yes                |
| gzip           | Yes                      | Yes                |
| xz             | Yes                      | No                 |
| zstd           | No                       | Yes                |

<a id="supported-runtimes-frameworks_examine-images-for-vulnerabilities"></a>

## Supported runtimes and frameworks

Beginning from Red Hat Advanced Cluster Security for Kubernetes 3.0.50 (Scanner version 2.5.0), the StackRox Scanner identifies vulnerabilities in the following developer platforms:

- .NET Core

- ASP.NET Core

These are not supported by Scanner V4.

<div>

<div class="title">

Additional resources

</div>

- [Vulnerability sources](../architecture/acs-architecture.md)

- [Integrating with image vulnerability scanners](../integration/integrate-with-image-vulnerability-scanners.md)

</div>

<a id="scanning-virtual-machines_examine-images-for-vulnerabilities"></a>

# Scanning virtual machines

You can use Red Hat Advanced Cluster Security for Kubernetes (RHACS) to scan virtual machine (VM) workloads running on Red Hat OpenShift Virtualization (RHOCPV) to identify security vulnerabilities in packages installed on VMs. RHACS creates index reports of installed packages and matches them against known vulnerabilities to provide comprehensive security assessment of VM workloads.

> [!IMPORTANT]
> Vulnerability management in RHACS for virtual machines running on OpenShift Virtualization is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

RHACS uses the following components to collect, process, and analyze VM package data:

- `roxagent`: A binary executable that runs inside VMs and scans for installed packages, creates index reports, and sends them to the relay component

- Relay: The node-level RHACS component that receives index reports from `roxagent` and forwards them to Sensor

- Sensor: The cluster-level RHACS component that collects data from relay components and sends it to Central

- Central: The main component that stores virtual machine information and finds vulnerabilities based on the reported packages

The VM scanning process follows this data flow:

1.  The `roxagent` binary running inside a VM scans the filesystem for installed packages and package managers such as Red Hat Package Manager (RPM) and DNF.

2.  `roxagent` creates index reports based on discovered packages.

3.  `roxagent` sends the index reports to the host by using the virtual socket (vsock) protocol.

4.  The relay component in the Collector daemonset receives the index reports.

5.  Relay forwards the reports to Sensor for processing.

6.  Sensor aggregates VM data with Kubernetes API information.

7.  Sensor sends the combined data to Central.

8.  Central stores the VM information and requests Scanner V4 to match packages against known CVEs.

9.  Central provides access to VM vulnerability data through the RHACS portal and the API.

To use RHACS to scan VMs, you must configure a feature flag in RHACS. Additionally, you must ensure that your system meets specific hardware and software requirements. For more information about requirements, see "Resource requirements for virtual machine scanning".

<div>

<div class="title">

Additional resources

</div>

- [Resource requirements for virtual machine scanning](../installing/acs-recommended-requirements.md#recommended-requirements-vm-scanning_acs-recommended-requirements)

</div>

<a id="vm-scanning-requirements_examine-images-for-vulnerabilities"></a>

## Requirements for virtual machine scanning

To use Red Hat Advanced Cluster Security for Kubernetes (RHACS) to scan virtual machines (VMs), you must meet specific requirements.

Red Hat OpenShift Virtualization (RHOCPV) must meet the following requirements:

- The RHOCPV Operator is installed in the cluster you want to scan.

- The HyperConverged resource is patched to enable virtual socket (vsock) support.

VMs must meet the following requirements:

- VM resources include vsock support with the setting `spec.domain.devices.autoattachVSOCK: true`.

- VMs are running Red Hat Enterprise Linux (RHEL). You must register any host where the scan agent is installed with Red Hat Subscription Manager and have an active RHEL subscription.

- VMs have internet access to download repository-to-Common Platform Enumeration (CPE) mappings.

- DNF is installed.

RHACS must meet the following requirements:

- Scanner V4 is deployed and available.

For resource requirements, such as CPU and memory resource allocation, see "Resource requirements for virtual machine scanning".

<div>

<div class="title">

Additional resources

</div>

- [Resource requirements for virtual machine scanning](../installing/acs-recommended-requirements.md#recommended-requirements-vm-scanning_acs-recommended-requirements)

</div>

<a id="vm-scanning-limitations_examine-images-for-vulnerabilities"></a>

## Limitations for virtual machine scanning

Scanning virtual machines (VMs) with Red Hat Advanced Cluster Security for Kubernetes has some limitations.

Scanning VMs has the following limitations:

- Currently, RHACS can only scan VMs that are running RHEL.

- RHEL must be activated with a valid subscription.

- Only RHEL packages indexed by DNF with valid repository links can be scanned.

- Scanning requires sudo privileges for `roxagent` to scan package databases and communicate over vsock.

- Only packages managed by Red Hat Package Manager (RPM) and DNF are detected.

- Internet connectivity is required for repository-to-CPE mapping downloads unless a local mapping file is configured.

<a id="configuring-vm-scanning_examine-images-for-vulnerabilities"></a>

## Configuring the virtual machine feature flag

To use Red Hat Advanced Cluster Security for Kubernetes (RHACS) to scan virtual machines (VMs), you must configure a feature flag. You must also configure virtual socket (vsock) support in RHOCPV.

<div>

<div class="title">

Procedure

</div>

1.  Set the VM feature flag environment variable `ROX_VIRTUAL_MACHINES=true` on the following components:

    - Central container in the Central pod

    - Sensor container in the Sensor pod

    - Compliance container in the Collector pod

2.  Enable vsock support in RHOCPV by adding the following annotation:

    ``` yaml
    metadata:
     annotations:
       kubevirt.kubevirt.io/jsonpatch: |-
         [
           {
             "op":"add",
             "path":"/spec/configuration/developerConfiguration/featureGates/-",
             "value":"VSOCK"
           }
         ]
    ```

    You can add the annotation by editing the CR manually. For example, you can apply a JSON patch by entering the following command:

    ``` terminal
    $ cat << EOF | kubectl apply -f -
    apiVersion: hco.kubevirt.io/v1beta1
    kind: HyperConverged
    metadata:
      name: kubevirt-hyperconverged
      namespace: openshift-cnv
      annotations:
        kubevirt.kubevirt.io/jsonpatch: |-
          [
            {
              "op":"add",
              "path":"/spec/configuration/developerConfiguration/featureGates/-",
              "value":"VSOCK"
            }
          ]
    spec: {}
    EOF
    ```

</div>

<a id="advanced-vm-scanning_examine-images-for-vulnerabilities"></a>

### Advanced virtual machine scanning configuration

Depending on your system needs, you might need to set some advanced configuration parameters to scan virtual machines.

<div>

<div class="title">

Procedure

</div>

- In the Collector pod in the Compliance container, you can configure the following environment variables:

  - ROX_VIRTUAL_MACHINES_VSOCK_PORT: Port for virtual socket (vsock) connections. The default value is `818`.

  - ROX_VIRTUAL_MACHINES_MAX_CONCURRENT_VSOCK_CONNECTIONS: Maximum number of VMs that can send index reports concurrently. The default value is `50`.

  - ROX_VIRTUAL_MACHINES_VSOCK_CONN_MAX_SIZE_KB: Maximum connection size in KB. The default value is `16384`.

  - ROX_VIRTUAL_MACHINES_VSOCK_CONCURRENCY_TIMEOUT: Timeout for acquiring a vsock connection semaphore slot. Increase this value if VMs are timing out while waiting for a connection slot. The default value is `5s`.

  - ROX_VIRTUAL_MACHINES_INDEX_REPORTS_BUFFER_SIZE: Buffer size for index reports awaiting processing in Sensor. Increase this value in high-latency environments where reports queue up in Sensor before being forwarded to Central. The default value is `100`.

  - ROX_VIRTUAL_MACHINES_RELAY_ENABLED_ON_MASTER_NODES: Allow the relay to run on control-plane nodes. Enable this in small clusters where master nodes also host VMs. The default value is `false`.

  - ROX_VM_RELAY_MAX_REPORTS_PER_MINUTE: Maximum number of VM index reports per minute that the relay forwards to Sensor for each VM connection. This setting supports fractional values. Set the value to `0` to disable relay-side rate limiting. The default value is `1.0`. This setting helps prevent a single VM from sending bursts of reports that can consume relay capacity and interfere with report processing for other VMs.

  - ROX_VM_RELAY_STALE_ACK_THRESHOLD: Maximum time that the relay waits for an acknowledgment (ACK) confirming successful processing of a previously forwarded VM index report. If the last ACK is older than this threshold or no ACK was received, a stale-ACK event is recorded in logs and metrics. Set a non-positive value to disable this behavior. The default value is `4h`.

- In the Central pod, you can configure the following environment variables:

  - ROX_VM_INDEX_REPORT_RATE_LIMIT: Maximum number of index reports per second that Central accepts. Each secured cluster gets an equal share (1/N) of this global capacity. The default value is `0.3`.

  - ROX_VM_INDEX_REPORT_BUCKET_CAPACITY: Maximum number of requests that can be accepted in a burst before rate limiting happens. The default value is `200`.

</div>

<a id="deploy-roxagent_examine-images-for-vulnerabilities"></a>

## Deploying roxagent

To use Red Hat Advanced Cluster Security for Kubernetes (RHACS) to scan virtual machines (VMs), you must run `roxagent`, a binary executable. It runs inside VMs, scans for installed packages, and creates index reports.

Deploy `roxagent` as a systemd-managed container service by using Podman Quadlet. This deployment method uses container images from a validated build pipeline, runs `roxagent` periodically by using a systemd timer, and manages the container lifecycle automatically.

<a id="deploy-roxagent-quadlet_examine-images-for-vulnerabilities"></a>

### Deploying roxagent by using Podman Quadlet

You can deploy `roxagent` as a systemd-managed container service by using Podman Quadlet. This deployment method uses container images from a validated build pipeline, runs `roxagent` periodically by using a systemd timer, and manages the container lifecycle automatically.

<div>

<div class="title">

Prerequisites

</div>

- You have a Red Hat Enterprise Linux (RHEL) 8, 9, or 10 virtual machine running on RHOCPV with virtual socket (vsock) enabled.

- You have installed Podman on the VM.

- You have deployed RHACS with VM scanning enabled by setting `ROX_VIRTUAL_MACHINES=true`.

- The VM has network access to pull the RHACS main image from your container registry.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that vsock is available:

    ``` terminal
    $ ls -la /dev/vsock
    ```

2.  Create the Quadlet directory:

    ``` terminal
    $ sudo mkdir -p /etc/containers/systemd/
    ```

3.  Create the `tmpfiles.d` configuration for the `roxagent` lock directory by copying the following content to `/etc/tmpfiles.d/roxagent.conf`:

    ``` text
    d /run/lock/roxagent 0755 root root -
    ```

    Apply the configuration:

    ``` terminal
    $ sudo systemd-tmpfiles --create
    ```

4.  Copy the following content to `/etc/systemd/system/roxagent-prep.service`:

    ``` ini
    [Unit]
    Description=Prepare RPM database for StackRox VM Agent
    # Copy the RPM database to a writable location because SQLite WAL mode
    # requires write access even for read-only queries

    [Service]
    Type=oneshot
    RemainAfterExit=yes
    ExecStartPre=/bin/mkdir -p /run/lock/roxagent
    ExecStart=/bin/rm -rf /tmp/roxagent-rpm
    ExecStart=/bin/cp -a /var/lib/rpm /tmp/roxagent-rpm
    ExecStart=/bin/chmod -R 755 /tmp/roxagent-rpm
    ```

5.  Copy the following content to `/etc/systemd/system/roxagent.timer`:

    ``` ini
    [Unit]
    Description=Run StackRox VM Agent periodically

    [Timer]
    OnBootSec=5min
    OnUnitActiveSec=3h40m
    RandomizedDelaySec=40min
    Persistent=true

    [Install]
    WantedBy=timers.target
    ```

6.  Copy the following content to `/etc/containers/systemd/roxagent.container`:

    ``` ini
    [Unit]
    Description=StackRox VM Agent Container
    # Copy RPM database before starting (SQLite WAL requires writable access)
    Requires=roxagent-prep.service
    After=roxagent-prep.service

    [Container]
    # Replace with your StackRox main image tag
    Image=registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:<rhacs-version>
    Exec=--host-path /host
    Network=host

    # Privileged for vsock access
    # Use PodmanArgs for entrypoint (RHEL 8 Quadlet doesn't support Entrypoint key)
    # Run as root since image defaults to non-root user
    SecurityLabelDisable=true
    PodmanArgs=--privileged --user root --entrypoint /stackrox/bin/roxagent --device /dev/vsock

    # Mount copied RPM database (writable for SQLite WAL) and host config files (read-only)
    Volume=/tmp/roxagent-rpm:/host/var/lib/rpm:rw
    Volume=/etc/yum.repos.d:/host/etc/yum.repos.d:ro
    Volume=/etc/os-release:/host/etc/os-release:ro
    Volume=/etc/redhat-release:/host/etc/redhat-release:ro
    Volume=/etc/system-release-cpe:/host/etc/system-release-cpe:ro
    # DNF cache and state for repo-to-package mapping
    Volume=/var/cache/dnf:/host/var/cache/dnf:ro
    Volume=/var/lib/dnf:/host/var/lib/dnf:ro
    # Shared lock directory for single-instance enforcement
    Volume=/run/lock/roxagent:/run/lock/roxagent:rw

    [Service]
    Type=oneshot
    TimeoutStartSec=600

    [Install]
    WantedBy=
    ```

    Where:

    \<rhacs-version\>  
    The version of your RHACS deployment, for example, 4.11.3.

7.  If SELinux is enabled, restore the SELinux contexts by entering the following commands:

    ``` terminal
    $ sudo restorecon -Rv /etc/containers/systemd/
    ```

    ``` terminal
    $ sudo restorecon -Rv /etc/systemd/system/roxagent.timer /etc/systemd/system/roxagent-prep.service
    ```

8.  Reload systemd and enable the timer by entering the following commands:

    ``` terminal
    $ sudo systemctl daemon-reload
    ```

    ``` terminal
    $ sudo systemctl enable --now roxagent.timer
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the timer is active by entering the following command:

  ``` terminal
  $ sudo systemctl list-timers roxagent.timer
  ```

- Optional: Run a scan immediately by entering the following command:

  ``` terminal
  $ sudo systemctl start roxagent.service
  ```

- View the scan logs by entering the following command:

  ``` terminal
  $ sudo journalctl -u roxagent.service -f
  ```

</div>

<a id="troubleshooting-vm-scanning_examine-images-for-vulnerabilities"></a>

## Troubleshooting virtual machine scanning

If you have problems when viewing vulnerability results for VMs, you can try some common troubleshooting steps. You can try different steps depending on the type of issue you are having, for example, connectivity or performance issues. You can also make sure your system meets the recommended requirements. See "Resource requirements for virtual machine scanning".

<div>

<div class="title">

Procedure

</div>

- If `roxagent` cannot connect to the host, try these steps:

  - Verify that virtual socket (vsock) is enabled in the VM configuration.

  - Check that the relay is running on the host node. The relay runs inside the Compliance container in the Collector pod, not as a standalone process.

  - Verify that the relay is expected to run on the node hosting the VM. The relay does not start on master or control-plane nodes unless `ROX_VIRTUAL_MACHINES_RELAY_ENABLED_ON_MASTER_NODES` is explicitly set to `true`.

  - Ensure that the vsock kernel modules are loaded.

  - Verify that port configuration matches between the `roxagent` and relay.

- If the scan finds no packages, try these steps:

  - Verify that `--host-path` points to the correct filesystem location.

  - Verify that RPM and DNF databases exist and are readable by `roxagent`.

  - Use the `--verbose` flag to examine index reports.

  - Confirm that the roxagent has root privileges.

- If vulnerability data does not appear in RHACS, try these steps:

  - Verify that the feature flag is enabled on all components.

  - Check Central logs for enrichment processing.

  - Ensure that the VM has a valid RHEL subscription.

  - Confirm repository-to-CPE mapping downloads are successful. If downloads are not successful, the "error updating mapping file" message occurs in the logs. The likely cause of an unsuccessful download is a failed internet connection. In air-gapped environments, configure `roxagent` with the `--repo-cpe-url` flag to point to a local mapping file.

- If there is a network connectivity problem:

  - Verify that the VM has internet access.

  - Check the firewall rules for repository access.

  - Validate DNS resolution from within the VM.

- If you observe performance issues, such as large memory usage, try these steps:

  - Monitor relay resource consumption and set `ROX_VIRTUAL_MACHINES_MAX_CONCURRENT_VSOCK_CONNECTIONS` to a lower number if needed.

  - Consider reducing scan frequency in daemon mode.

- If you notice slow scan times, try these steps:

  - Verify that metal nodes are used for VM hosting.

  - Check network latency for repository downloads.

  - Monitor disk I/O during package database reads.

- If you see that some VMs are not scanned for vulnerabilities, try these steps:

  - Check for a RHACS Administration Events warning that "VM index reports are being rate limited". If you see this warning, you might need to adjust the following items based on your workloads:

    - `ROX_VM_INDEX_REPORT_RATE_LIMIT`: For more information, see "Advanced virtual machine scanning configuration".

    - `ROX_VM_INDEX_REPORT_BUCKET_CAPACITY`: For more information, see "Advanced virtual machine scanning configuration".

    - Scanner V4 resources. For more information, see "Resource requirements for virtual machine scanning".

  - Check the logs of the Compliance container in the Collector pod for instances of the "Could not acquire semaphore, too many concurrent connections" message. If you see this message, you can increase the number of connections in `ROX_VIRTUAL_MACHINES_MAX_CONCURRENT_VSOCK_CONNECTIONS` to allow RHACS to process more VMs in parallel. You might also need to increase the Compliance container memory limit.

  - Check the logs of the Compliance container in the Collector pod for instances of the "data size exceeds the limit" message. If you see this message, you can increase the maximum vsock connection size in `ROX_VIRTUAL_MACHINES_VSOCK_CONN_MAX_SIZE_KB` to allow processing of larger index reports. You might also need to increase the Compliance container memory limit.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Viewing vulnerabilities in virtual machines](manage-vulnerabilities/common-vuln-management-tasks.md#vview-vms-cves_vms)

- [Resource requirements for virtual machine scanning](../installing/acs-recommended-requirements.md#recommended-requirements-vm-scanning_acs-recommended-requirements)

</div>

<a id="redirecting-image-pulls-from-a-source-registry-to-a-mirrored-registry_examine-images-for-vulnerabilities"></a>

# Redirecting image pulls from a source registry to a mirrored registry

Red Hat Advanced Cluster Security for Kubernetes (RHACS) supports scanning images from registry mirrors that you have configured by using one of the following OpenShift Container Platform custom resources (CRs):

- `ImageContentSourcePolicy` (ICSP)

- `ImageDigestMirrorSet` (IDMS)

- `ImageTagMirrorSet` (ITMS)

For more information about how to configure image registry repository mirroring, see "Configuring image registry repository mirroring".

> [!IMPORTANT]
> To scan images from registry mirrors, you must configure delegated image scanning.

For more information about how to configure delegated image scanning, see "Accessing delegated image scanning".

<div>

<div class="title">

Additional resources

</div>

- [Configuring image registry repository mirroring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/images/image-configuration#images-configuration-registry-mirror-configuring_image-configuration)

- [Accessing delegated image scanning](examine-images-for-vulnerabilities.md#accessing-delegated-image-scanning_examine-images-for-vulnerabilities)

- [Scanning images by using secured clusters](examine-images-for-vulnerabilities.md#scanning-images-by-using-secured-clusters_examine-images-for-vulnerabilities)

</div>

<a id="accessing-delegated-image-scanning_examine-images-for-vulnerabilities"></a>

# Accessing delegated image scanning

If you have isolated container image registries that are accessible from your secured clusters, you can use delegated image scanning to scan them.

<a id="enhancing-image-scanning-by-accessing-delegated-image-scanning_examine-images-for-vulnerabilities"></a>

## Enhancing image scanning by accessing delegated image scanning

Currently, by default, Central Services Scanner performs both indexing (identification of components) and vulnerability matching (enrichment of components with vulnerability data) for images observed in your secured clusters, with the exception of images from the OpenShift Container Platform integrated registry.

For images from the OpenShift Container Platform integrated registry, Scanner-slim installed in your secured cluster performs the indexing, and the Central Services Scanner performs the vulnerability matching.

The delegated image scanning feature extends scanning functionality by allowing Scanner-slim to index images from any registry and then send them to Central for vulnerability matching. To use this feature, ensure that Scanner-slim is installed in your secured clusters. If Scanner-slim is not present, scan requests are sent directly to Central.

<a id="scanning-images-by-using-secured-clusters_examine-images-for-vulnerabilities"></a>

## Scanning images by using secured clusters

To scan images by using the secured clusters instead of the Central services, you can use the delegated image scanning feature.

A new delegated scanning configuration specifies the registries from which you can delegate image scans. For images that Sensor observes, you can use the delegated registry configuration to delegate scans from no registries, all registries, or specific registries.

To enable delegation of scans by using the `roxctl` CLI, Jenkins plugin, or API, you must also specify a destination cluster and source registry.

<div>

<div class="title">

Prerequisites

</div>

- You have installed Scanner in the secured cluster to scan images.

  > [!NOTE]
  > Enabling Scanner is supported on OpenShift Container Platform and Kubernetes secured clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Platform Configuration → Clusters**.

2.  In the **Clusters** view header, click **Delegated scanning**.

3.  In the **Delegated Image Scanning** page, provide the following information:

    - **Delegate scanning for**: To choose the scope of the image delegation, select one of the following options:

      - **None**: The default option. This option specifies that the secured clusters do *not* scan any images, except for images from the integrated OpenShift image registry.

      - **All registries**: This option indicates that the secured clusters scan all the images.

      - **Specified registries**: This option specifies the images that secured clusters should scan based on the registries list.

    - **Select default cluster to delegate to**: From the drop-down list, select the name of the default cluster. The default cluster processes the scan requests coming from the command-line interface (CLI) and API. This is optional and you can select `None` if required.

    - Optional: To specify the source registry and destination cluster details, click **Add registry**.

      For example, specify the source registry as `example.com`, and select `remote` from the drop-down list for the destination cluster. You can add more than one source registry and destination cluster if required.

      > [!IMPORTANT]
      > You can select the destination cluster as `None` if the scan requests are not coming from the CLI and API.

4.  Click **Save**.

</div>

Image integrations are now synchronized between Central and Sensor, and Sensor captures pull secrets from each namespace. Sensor then uses these credentials to authenticate to the image registries.

<div>

<div class="title">

Additional resources

</div>

- [Redirecting image pulls from a source registry to a mirrored registry](examine-images-for-vulnerabilities.md#redirecting-image-pulls-from-a-source-registry-to-a-mirrored-registry_examine-images-for-vulnerabilities)

</div>

<a id="installing-scanner-slim_examine-images-for-vulnerabilities"></a>

## Installing and configuring Scanner-slim on secured clusters

If you are using the StackRox scanner, Scanner-slim is the lightweight version of that scanner that runs on your secured clusters instead of the cluster where Central is installed. You can install Scanner-slim by using the Operator or by using Helm. Scanner V4 does not use Scanner-slim.

<a id="installing-scanner-slim-operator_examine-images-for-vulnerabilities"></a>

## Using the Operator

The RHACS Operator installs a Scanner-slim version on each secured cluster to scan images in the OpenShift Container Platform integrated registry and optionally other registries.

For more information, see [Installing RHACS on secured clusters by using the Operator](../installing/installing_ocp/install-secured-cluster-ocp.md).

<a id="installing-scanner-slim-helm_examine-images-for-vulnerabilities"></a>

## Using Helm

The secured cluster services Helm chart (`secured-cluster-services`) installs a Scanner-slim version on each secured cluster. In Kubernetes, the secured cluster services include Scanner-slim. On OpenShift Container Platform, however, RHACS installs a Scanner-slim version on each secured cluster to scan images in the OpenShift Container Platform integrated registry and optionally other registries.

- For OpenShift Container Platform installations, see [Installing the secured-cluster-services Helm chart without customization](../installing/installing_ocp/install-secured-cluster-ocp.md#installing-secured-cluster-services-quickly_install-secured-cluster-ocp).

- For non-OpenShift Container Platform installations, such as Amazon Elastic Kubernetes Service (Amazon EKS), Google Kubernetes Engine (Google GKE), and Microsoft Azure Kubernetes Service (Microsoft AKS), see [Installing the secured-cluster-services Helm chart without customization](../installing/installing_other/install-secured-cluster-other.md#installing-secured-cluster-services-quickly_install-secured-cluster-other).

<a id="verifying-scanner-installation_examine-images-for-vulnerabilities"></a>

# Verifying scanner installation

After installation, use the portal to make sure that the scanner is installed and working.

<div>

<div class="title">

Procedure

</div>

- Verify that the status of the secured cluster indicates that scanner is present and healthy:

  1.  In the RHACS portal, go to **Platform Configuration → Clusters**.

  2.  In the **Clusters** view, select a cluster to view its details.

  3.  In the **Health Status** card, ensure that **Scanner** is present and is marked as **Healthy.**

</div>

<a id="using-image-scanning_examine-images-for-vulnerabilities"></a>

# Using image scanning

You can scan images stored in a cluster specific OpenShift Container Platform integrated image registry by using `roxctl` CLI, Jenkins, and API. You can specify the appropriate cluster in the delegated scanning configuration or use the cluster parameter available in `roxctl` CLI, Jenkins, and API.

For more information about how to scan images by using the `roxctl` CLI, see [Image scanning by using the roxctl CLI](../cli/image-scanning-by-using-the-roxctl-cli.md).

<a id="setting-up-scanning_examine-images-for-vulnerabilities"></a>

## Setting up scanning

Red Hat Advanced Cluster Security for Kubernetes automatically scans active images. You can configure additional settings for scanning, such as automatic scanning of inactive images and scanning of virtual images.

<a id="periodic-scanning-of-images_examine-images-for-vulnerabilities"></a>

## Automatic scanning of active images

Red Hat Advanced Cluster Security for Kubernetes periodically scans all active images and updates the image scan results to reflect the latest vulnerability definitions. Active images are the images you have deployed in your environment.

> [!NOTE]
> From Red Hat Advanced Cluster Security for Kubernetes 3.0.57, you can enable automatic scanning of inactive images by configuring the **Watch** setting for images.

Central fetches the image scan results for all active images from Scanner or other integrated image scanners that you use and updates the results every 4 hours.

You can also use the `roxctl` CLI to check the image scan results on demand.

<a id="scan-inactive-images_examine-images-for-vulnerabilities"></a>

## Scanning inactive images

Red Hat Advanced Cluster Security for Kubernetes (RHACS) scans all active (deployed) images every 4 hours and updates the image scan results to reflect the latest vulnerability definitions.

You can also configure RHACS to scan inactive (not deployed) images automatically.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Vulnerability Management** → **Results**.

2.  Click **More Views** → **Inactive images**.

3.  Optional: Choose the appropriate method to view the component and advisory data associated with a CVE:

    - To view the component and advisory data associated with a CVE from the list of CVEs, complete the following steps:

      1.  Click the **\<number\> CVEs** tab.

      2.  In the list of CVEs, click a CVE to do any of the following tasks:

          - To view the component and advisory data associated with an image:

            1.  Click the **\<number\> Images** tab.

            2.  Expand the image.

                You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

          - To view the component and advisory data associated with a deployment:

            1.  Click the **\<number\> Deployments** tab.

            2.  Expand the deployment.

                You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

    - To view the component and advisory data associated with a CVE from the list of images, complete the following steps:

      1.  Click the **\<number\> Images** tab.

      2.  In the list of images, click an image.

      3.  To view the component and advisory data associated with a CVE, expand the CVE.

          You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

    - To view the component and advisory data associated with a CVE from the list of deployments, complete the following steps:

      1.  Click the **\<number\> Deployments** tab.

      2.  In the list of deployments, click a deployment.

      3.  To view the component and advisory data associated with a CVE, expand the CVE.

          You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

4.  Click **Manage watched images**.

5.  In the **Image name** field, enter the fully-qualified image name that begins with the registry and ends with the image tag, for example, `docker.io/library/nginx:latest`.

6.  Click **Add image to watch list**.

7.  Optional: To remove a watched image, locate the image in the **Manage watched images** window, and click **Remove watch**.

    > [!IMPORTANT]
    > In the RHACS portal, click **Platform Configuration** → **System Configuration** to view the data retention configuration.
    >
    > All the data related to the image removed from the watched image list continues to appear in the RHACS portal for the number of days mentioned on the **System Configuration** page and is only removed after that period is over.

8.  Click **Close** to return to the **Inactive images** page.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing the roxctl CLI](../cli/installing-the-roxctl-cli.md)

</div>

<a id="about-vulnerabilities_examine-images-for-vulnerabilities"></a>

# Vulnerabilities

Red Hat Advanced Cluster Security for Kubernetes (RHACS) fetches vulnerability definitions and updates from many vulnerability feeds. These feeds are both general in nature, such as the National Vulnerability Database (NVD), or distribution-specific, such as Alpine, Debian, and Ubuntu.

For more information about viewing and addressing vulnerabilities that RHACS finds, see "Vulnerability management".

<a id="fetching-vulnerability-definitions_examine-images-for-vulnerabilities"></a>

## Fetching vulnerability definitions

In online mode, Central fetches the vulnerability definitions every 5 minutes from a single feed. This feed combines vulnerability definitions from upstream sources, and it refreshes every 3 hours. The address of the feed is `https://definitions.stackrox.io`.

You can change the frequency of the default query from Central to the `definitions.stackrox.io` feed by setting the `ROX_SCANNER_VULN_UPDATE_INTERVAL` environment variable. Run the following command:

``` terminal
$ oc -n stackrox set env deploy/central ROX_SCANNER_VULN_UPDATE_INTERVAL=<value>
```

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

This variable applies to the connection between Central and the `definitions.stackrox.io` feed. Both the StackRox Scanner and Scanner V4 use vulnerability data from Central that is obtained from this feed. The StackRox Scanner’s config map still has an `updater.interval` parameter for configuring the scanner’s updating frequency, but it no longer includes the `fetchFromCentral` parameter.

For more information about the vulnerability sources that RHACS uses, see "Vulnerability sources" in "Red Hat Advanced Cluster Security for Kubernetes architecture".

<div>

<div class="title">

Additional resources

</div>

- [Vulnerability sources](../architecture/acs-architecture.md)

</div>

<a id="understanding-understanding-vulnerability-scores_examine-images-for-vulnerabilities"></a>

## Understanding vulnerability scores in the dashboard

The vulnerability management dashboard in the Red Hat Advanced Cluster Security for Kubernetes portal shows a single Common Vulnerability Scoring System (CVSS) base score for each vulnerability. RHACS shows the CVSS score based on the following criteria:

- If a CVSS v3 score is available, RHACS shows the score and lists `v3` along with it. For example, `6.5 (v3)`.

  > [!NOTE]
  > CVSS v3 scores are only available if you are using the StackRox Scanner version 1.3.5 and later or Scanner V4.

- If a CVSS v3 score is not available, RHACS might show only the CVSS v2 score. For example, `6.5`.

You can use the API to get the CVSS scores. If CVSS v3 information is available for a vulnerability, the response might include both CVSS v3 and CVSS v2 information.

<a id="disable-language-specific-vulnerability-scanning_examine-images-for-vulnerabilities"></a>

# Disabling language-specific vulnerability scanning

Scanner identifies the vulnerabilities in the programming language-specific dependencies by default. You can disable the language-specific dependency scanning.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

- To disable language-specific vulnerability scanning, run the following command:

  ``` terminal
  $ oc -n stackrox set env deploy/scanner \
    ROX_LANGUAGE_VULNS=false
  ```

  If you are using Red Hat Advanced Cluster Security for Kubernetes version 3.0.47 or older, replace the environment variable name `ROX_LANGUAGE_VULNS` with `LANGUAGE_VULNS`.

</div>

<a id="base-images_examine-images-for-vulnerabilities"></a>

# Defining base images used in application development

Red Hat Advanced Cluster Security for Kubernetes (RHACS) lets DevSecOps engineers in your organization to identify base images that are used in the container applications that your developers build. RHACS can then provide information about vulnerabilities that exist in base image layers so that application developers can address these vulnerabilities and use trusted, secure images when building applications. Developers can also focus on fixing vulnerabilities in application layers instead of vulnerabilities in the base layers.

When you configure a list of base images, RHACS pulls information about those images from the repositories and stores it in a database. When you scan images, RHACS tries to match the container images against the images in that database. RHACS then provides information about the base image layer in the RHACS portal.

> [!NOTE]
> You can configure RHACS to pull multiple tags for an image by using a wildcard. However, to prevent undue system resource use, RHACS only tracks information for the most recent 100 tags.

<a id="define-base-images_examine-images-for-vulnerabilities"></a>

## Defining base images by using the RHACS portal

You can set up a list of base images in Red Hat Advanced Cluster Security for Kubernetes (RHACS) that are used in the applications that your DevOps users build. RHACS then uses this list to identify those base images in the images that it scans. Using this information, you can separate vulnerabilities contained in the base image layer from vulnerabilities contained in the application layers.

<div>

<div class="title">

Prerequisites

</div>

- To define base images, you must be logged in as a user with the `ImageAdministration` permission; for example, as the `Admin` or `Analyst` user.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Select **Platform Configuration** → **Base Images** and click **Add base image**.

2.  Enter the path to the base image repository, including the repository address and the image tag, in the format `<hostname>/<project-id>/<repository-name>:<tag>.` You can include a pattern to filter the tag, including using `*` to match any sequence of nonseparator characters or `?` to match any single nonseparator character. For more filtering syntax information, see the [Go filepath match](https://pkg.go.dev/path/filepath#Match) documentation. For example, `registry.redhat.io/ubi9:9.*` would add Red Hat Universal Base Image 9 images with tags starting with `9`.

    > [!NOTE]
    > To prevent undue system resource use, RHACS only tracks information for the most recent 100 tags.

3.  Click **Save**. The list of base images is compared against the repository and tags are updated every 4 hours.

</div>

<div>

<div class="title">

Additional resources

</div>

- [System permission sets](manage-user-access/manage-role-based-access-control-3630.md#rbac-permission-sets_manage-role-based-access-control)

- [Viewing vulnerabilities in base images](manage-vulnerabilities/common-vuln-management-tasks.md#base-image-vulnerabilities_other)

</div>

<a id="base-images-api_examine-images-for-vulnerabilities"></a>

### Configuring base images by using the API

You can use the API to set up a list of base images, add new base images, delete base images, and modify the tag pattern for a base image.

<div>

<div class="title">

Prerequisites

</div>

- You must be logged in as a user whose role has a permission set that includes the `ImageAdministration` permission; for example, the `Admin` and `Analyst` permission sets have this permission.

</div>

<div>

<div class="title">

Procedure

</div>

1.  You can take the following actions by using the Base Image Service in the v2 API:

    - Get a list of base images: Use `GetBaseImageReferences`.

    - Add a new base image: Use `CreateBaseImageReference`.

    - Delete a base image: Use `DeleteBaseImageReference`.

    - Update the tag pattern for a base image: Use `UpdateBaseImageTagPattern`.

      For more information about schema and valid values, see the API Reference.

</div>

<div>

<div class="title">

Additional resources

</div>

- [System permission sets](manage-user-access/manage-role-based-access-control-3630.md#rbac-permission-sets_manage-role-based-access-control)

- [Viewing vulnerabilities in base images](manage-vulnerabilities/common-vuln-management-tasks.md#base-image-vulnerabilities_other)

</div>

<a id="additional-resources_examine-images-for-vulnerabilities"></a>

# Additional resources

- [Red Hat CVE Database](https://access.redhat.com/security/cve)
