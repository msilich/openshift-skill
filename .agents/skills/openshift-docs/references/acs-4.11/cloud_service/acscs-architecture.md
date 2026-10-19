<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service) has a cloud-based control plane managed by Red Hat and secured cluster services that you install on your clusters. This section describes the architecture and components.

<a id="acscs-architecture-overview_acscs-architecture"></a>

# Red Hat Advanced Cluster Security Cloud Service architecture overview

Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service) is a Red Hat managed Software-as-a-Service (SaaS) platform you can use to protect your Kubernetes and OpenShift Container Platform clusters and applications throughout the build, deploy, and runtime lifecycles.

The system architecture includes the cloud services, which Red Hat manages, and the secured OpenShift Container Platform or Kubernetes clusters, either on-premise or in the cloud, which you manage.

RHACS Cloud Service includes many built-in DevOps enforcement controls and security-focused best practices based on industry standards such as the Center for Internet Security (CIS) benchmarks and the National Institute of Standards Technology (NIST) guidelines. You can also integrate it with your existing DevOps tools and workflows to improve security and compliance.

The following graphic shows the architecture with the StackRox Scanner and Scanner V4.

<figure>
<img src="../images/acscs-architecture-scannerv4.png" alt="RHACS Cloud Service" />
</figure>

Central services include the user interface (UI), data storage, RHACS application programming interface (API), and image scanning capabilities. You deploy your Central service through the Red Hat Hybrid Cloud Console. When you create a new ACS instance, Red Hat creates your individual control plane for RHACS.

RHACS Cloud Service allows you to secure self-managed clusters that communicate with a Central instance. You manage the clusters that you secure, which are called Secured Clusters. Red Hat does not manage them. Secured Cluster services include optional vulnerability scanning services, admission control services, and data collection services used for runtime monitoring and compliance. You install Secured Cluster services on any OpenShift or Kubernetes cluster you want to secure.

When you install RHACS on OpenShift Container Platform by using the RHACS Operator, or on OpenShift Container Platform or any supported Kubernetes system by using Helm with the `secured-cluster-services` Helm chart, RHACS installs the StackRox Scanner and Scanner V4 components on every secured cluster. This enables the scanning of images in the integrated OpenShift image registry or in any registry that RHACS integrates with when you enable delegated scanning. You can choose to not install the StackRox Scanner or Scanner V4 on the secured clusters and install them only on the cluster where you install Central. For more information, see "Enabling Scanner V4".

<div>

<div class="title">

Additional resources

</div>

- [Enabling Scanner V4](../operating/examine-images-for-vulnerabilities.md#scannerv4-enabling_examine-images-for-vulnerabilities)

- [Red Hat Hybrid Cloud Console](https://console.redhat.com/)

</div>

<a id="acscs-central_acscs-architecture"></a>

# Central

Red Hat manages Central, the control plane for Red Hat Advanced Cluster Security for Kubernetes (RHACS Cloud Service). These services include the following components:

- **Central**: Central is the RHACS application management interface and services. It handles API interactions and user interface (RHACS Portal) access. You can use the same Central instance to secure many OpenShift Container Platform or Kubernetes clusters.

- **Central DB**: Central DB is the database for RHACS and handles all data persistence. It is currently based on PostgreSQL 13.

- **Scanner V4**: Beginning with version 4.4, RHACS has the Scanner V4 vulnerability scanner for scanning container images. Scanner V4 builds on Claircore, which also powers the Clair scanner. Scanner V4 supports language and OS-specific image components, node, and platform scanning. Scanner V4 has the Indexer, Matcher, and DB components.

  - **Scanner V4 Indexer**: The Scanner V4 Indexer performs image indexing, formerly known as image analysis. Given an image and registry credentials, the Indexer pulls the image from the registry, finds the base operating system, if it exists, and looks for packages. The Indexer then stores and outputs an index report, which has the findings for the given image.

  - **Scanner V4 Matcher**: The Scanner V4 Matcher performs vulnerability matching. If you install the Indexer in Central and it indexed the image, then the Matcher fetches the index report from the Indexer and matches the report with the vulnerabilities stored in the Scanner V4 database. If you install the Indexer in a Secured Cluster and it performed the indexing, then the Matcher uses the index report that the Indexer sent, and then matches against vulnerabilities. The Matcher also fetches vulnerability data and updates the Scanner V4 database with the latest vulnerability data. The Scanner V4 Matcher outputs a vulnerability report, which has the final results of an image.

  - **Scanner V4 DB**: This database stores information for Scanner V4, including all vulnerability data and index reports. You need a persistent volume claim (PVC) for Scanner V4 DB on the cluster where you install Central.

- **StackRox Scanner**: The StackRox Scanner originates from a fork of the Clair v2 open source scanner and was the default scanner for RHACS before Scanner V4.

- **Scanner-DB**: This database has data for the StackRox Scanner.

The RHACS scanner analyzes each image layer to identify the base operating system and identify programming language packages and packages that the operating system package manager installed. It matches the findings against known vulnerabilities from various vulnerability sources. In addition, it identifies vulnerabilities in the node’s operating system and platform.

<div>

<div class="title">

Additional resources

</div>

- [Claircore](https://github.com/quay/claircore)

- [Clair](https://github.com/quay/clair)

</div>

<a id="con-vuln-sources_acscs-architecture"></a>

## Vulnerability data sources

Sources for vulnerabilities depend on the scanner your system uses. RHACS contains two scanners: StackRox Scanner and Scanner V4. The StackRox Scanner is deprecated. Scanner V4 is the default image scanner.

> [!NOTE]
> Although the StackRox Scanner is deprecated, you still must enable it on the cluster where you install Central due to software dependencies.

<a id="scanner-v4-vuln-sources_acscs-architecture"></a>

### Scanner V4 sources

Scanner V4 uses many vulnerability data sources including Red Hat VEX, OSV, NVD, and various Linux distribution security databases.

Scanner V4 uses the following vulnerability sources:

Red Hat VEX  
Use this source with release 4.6 and later. This source offers vulnerability data in Vulnerability Exploitability eXchange (VEX) format. RHACS takes advantage of VEX benefits to significantly decrease the time needed for the initial loading of vulnerability data, and the space needed to store vulnerability data. VEX also offers improved accuracy over OVAL.

RHACS might list a different number of vulnerabilities when you are scanning with a RHACS version that uses OVAL, such as RHACS version 4.5, and a version that uses VEX, such as version 4.6. For example, RHACS no longer displays vulnerabilities with a status of "under investigation," while earlier versions that used OVAL data included these vulnerabilities.

For containers from or built on top of containers from the Red Hat Ecosystem Catalog, RHACS offers an option to show only vulnerabilities from Red Hat’s VEX data. VEX data for Red Hat images is the most exact because the Red Hat security team vets the vulnerabilities in those images and reports the results in VEX. Other vulnerability sources such as OSV can report vulnerabilities that Red Hat has determined are not applicable to the image. This can cause false positives in vulnerability results. Enabling the setting to use only VEX data for Red Hat images minimizes these false positives.

The option to use VEX data for Red Hat containers defaults to disabled. To enable this option, in Scanner V4 Matcher, set the environment variable `ROX_SCANNER_V4_RED_HAT_LAYERS_RED_HAT_VULNS_ONLY` to `true`. Be aware that in rare instances, using this option can cause valid vulnerabilities to not appear in scan results, or false negatives. For example, Red Hat does not track vulnerabilities for products that have reached end of life. Also be aware that Red Hat’s VEX data is missing exact security data for many Middleware products.

For more information about Red Hat security data, including information about the use of OVAL, Common Security Advisory Framework Version 2.0 (CSAF), and VEX, see "The future of Red Hat security data".

OSV  
Use this for language-related vulnerabilities, such as Go, Java, JavaScript, Python, and Ruby. This source might offer vulnerability IDs other than CVE IDs for vulnerabilities, such as a GitHub Security Advisory (GHSA) ID.

> [!NOTE]
> RHACS uses the OSV database available at OSV.dev under the Apache License 2.0.

NVD  
Use this for various purposes such as filling in information gaps when vendors do not offer information. For example, Alpine does not offer a description, CVSS score, severity, or published date.

> [!NOTE]
> This product uses the NVD API but is not endorsed or certified by the NVD.

Additional vulnerability sources  
- Alpine Security Database

- Data tracked in Amazon Linux Security Center

- Debian Security Tracker

- Oracle OVAL

- Photon OVAL

- SUSE OVAL

- Ubuntu OVAL

- StackRox: The upstream StackRox project maintains a set of vulnerabilities that you might not discover due to data formatting from other sources or absence of data.

Scanner V4 Indexer sources  
Scanner V4 indexer uses the following files to index Red Hat containers:

- repository-to-cpe.json: Maps RPM repositories to their related CPEs, which you need for matching vulnerabilities for RHEL-based images.

- container-name-repos-map.json: This matches container names to their corresponding repositories.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat VEX](https://security.access.redhat.com/data/csaf/v2/vex/)

- [Vulnerability Exploitability eXchange (VEX)](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#45-profile-5-vex)

- [Accurate security data for many Middleware products](https://access.redhat.com/security/middleware_security_scanning_problem)

- [The future of Red Hat security data](https://www.redhat.com/en/blog/future-red-hat-security-data)

- [OSV.dev](https://osv.dev/)

- [Apache License 2.0 for OSV database](https://github.com/google/osv.dev/blob/master/LICENSE)

- [NVD](https://nvd.nist.gov/)

- [Alpine Security Database](https://secdb.alpinelinux.org/)

- [Amazon Linux Security Center](https://alas.aws.amazon.com/index.html)

- [Debian Security Tracker](https://security-tracker.debian.org/tracker/data/json)

- [Oracle OVAL](https://linux.oracle.com/security/oval)

- [Photon OVAL](https://packages.vmware.com/photon/photon_oval_definitions/)

- [SUSE OVAL](https://support.novell.com/security/oval/)

- [Ubuntu OVAL](https://security-metadata.canonical.com/oval/)

- [StackRox manual vulnerabilities](https://github.com/stackrox/stackrox/blob/master/scanner/updater/manual/vulns.yaml)

- [repository-to-cpe.json](https://security.access.redhat.com/data/metrics/repository-to-cpe.json)

- [container-name-repos-map.json](https://security.access.redhat.com/data/metrics/container-name-repos-map.json)

</div>

<a id="stackrox-scanner-vuln-sources_acscs-architecture"></a>

### StackRox Scanner sources

StackRox Scanner uses many vulnerability data sources including Red Hat OVAL v2, NVD, and various Linux distribution security databases.

StackRox Scanner uses the following vulnerability sources:

- Red Hat OVAL v2

- Alpine Security Database

- Data tracked in Amazon Linux Security Center

- Debian Security Tracker

- Ubuntu CVE Tracker

- NVD: Use this for various purposes such as filling in information gaps when vendors do not offer information. For example, Alpine does not offer a description, CVSS score, severity, or published date.

  > [!NOTE]
  > This product uses the NVD API but is not endorsed or certified by the NVD.

- Linux manual entries and NVD manual entries: The upstream StackRox project maintains a set of vulnerabilities that you might not discover due to data formatting from other sources or absence of data.

- repository-to-cpe.json: Maps RPM repositories to their related CPEs, which you need for matching vulnerabilities for RHEL-based images.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat OVAL v2](https://access.redhat.com/security/data/oval/v2/)

- [Alpine Security Database](https://secdb.alpinelinux.org/)

- [Amazon Linux Security Center](https://alas.aws.amazon.com/index.html)

- [Debian Security Tracker](https://security-tracker.debian.org/tracker/data/json)

- [Ubuntu CVE Tracker](https://git.launchpad.net/ubuntu-cve-tracker/)

- [NVD](https://nvd.nist.gov/)

- [Linux manual entries](https://github.com/stackrox/scanner/blob/master/ext/vulnsrc/manual/manual.go)

- [NVD manual entries](https://github.com/stackrox/scanner/blob/master/pkg/vulnloader/nvdloader/manual.go)

- [repository-to-cpe.json](https://security.access.redhat.com/data/metrics/repository-to-cpe.json)

</div>

<a id="acs-secured-cluster-services_acscs-architecture"></a>

# Secured cluster services

Install the secured cluster services on each cluster that you want to secure by using Red Hat Advanced Cluster Security Cloud Service.

Secured cluster services include the following components:

- **Sensor**: Sensor is the service responsible for analyzing and monitoring the cluster. Sensor listens to the OpenShift Container Platform or Kubernetes API and Collector events to report the current state of the cluster. Sensor also triggers deploy-time and runtime violations based on RHACS Cloud Service policies. In addition, Sensor is responsible for all cluster interactions, such as applying network policies, initiating reprocessing of RHACS Cloud Service policies, and interacting with the Admission controller.

- **Admission controller**: The Admission controller prevents users from creating workloads that violate security policies in RHACS Cloud Service.

- **Collector**: Collector analyzes and monitors container activity on cluster nodes. It collects container runtime and network activity information and sends the collected data to Sensor.

- **Scanner V4**: Scanner V4 retrieves and scans images and indexes them. It is the default scanner for RHACS and has the following components:

  - **Scanner V4 Indexer**: The Scanner V4 Indexer performs image indexing, formerly known as image analysis. Given an image and registry credentials, the Indexer pulls the image from the registry. The Indexer finds the base operating system, if one exists, and looks for packages. It stores and outputs an index report, which has the findings for the given image.

  - **Scanner V4 DB**: This database stores information for Scanner V4, including index reports. For best performance, configure a persistent volume claim (PVC) for Scanner V4 DB.

- **StackRox Scanner**: In Kubernetes, the secured cluster services include Scanner-slim as an optional component. However, on OpenShift Container Platform, RHACS Cloud Service installs a Scanner-slim version on each secured cluster to scan images in the OpenShift Container Platform integrated registry and optionally other registries.

- **Scanner-DB**: This database has data for the StackRox Scanner.

  > [!NOTE]
  > When you install secured cluster services on the same cluster as Central services and install them in the same namespace, secured cluster services do not deploy Scanner V4 components. Instead, Central services are expected to already include a deployment of Scanner V4.

<div>

<div class="title">

Additional resources

</div>

- [External components](../architecture/acs-architecture.md#external-components_acs-architecture)

</div>

<a id="acscs-data-access-permissions_acscs-architecture"></a>

# Data access and permissions

Red Hat does not have access to the clusters on which you install the secured cluster services. Also, RHACS Cloud Service does not need permission to access the secured clusters. For example, you do not need to create new IAM policies, access roles, or API tokens.

However, RHACS Cloud Service stores the data that secured cluster services send. RHACS Cloud Service encrypts all data. Encrypting the data within the RHACS Cloud Service platform helps to ensure the confidentiality and integrity of the data.

When you install secured cluster services on a cluster, it generates data and transmits it to the RHACS Cloud Service. The RHACS Cloud Service platform keeps this data secure, and only authorized SRE team members and systems can access this data. RHACS Cloud Service uses this data to monitor the security and compliance of your cluster and applications, and to offer valuable insights and analytics that can help you optimize your deployments.
