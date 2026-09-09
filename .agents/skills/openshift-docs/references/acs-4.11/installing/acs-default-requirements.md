<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes components have specific default CPU, memory, and storage requirements.

<a id="acs-general-requirements_acs-default-requirements"></a>

# General RHACS requirements

Before you can install RHACS, your system must meet several requirements.

<a id="acs-system-requirements_acs-default-requirements"></a>

## System requirements

System, architecture, processor, memory, and storage requirements for installing RHACS.

> [!WARNING]
> You must not install RHACS on the following systems:
>
> - Amazon Elastic File System (EFS). Use the Amazon Elastic Block Store (EBS) with the default **gp2** volume type instead.
>
> - Older CPUs that do not have the Streaming Single Instruction, Multiple Data (SIMD) Extensions (SSE) 4.2 instruction set. For example, Intel processors older than *Sandy Bridge* and Advanced Micro Devices (AMD) processors older than *Bulldozer*. These processor families became available in 2011.

To install RHACS, you must have one of the following systems:

- OpenShift Container Platform version 4.12 or later, and cluster nodes with a supported operating system of Red Hat Enterprise Linux CoreOS (RHCOS) or Red Hat Enterprise Linux (RHEL)

- A supported managed Kubernetes platform, and cluster nodes with a supported operating system of Amazon Linux, CentOS, Container-Optimized operating system from Google, Red Hat Enterprise Linux CoreOS (RHCOS), Debian, Red Hat Enterprise Linux (RHEL), or Ubuntu

The following minimum requirements and suggestions apply to cluster nodes.

Architecture  
`amd64`, `ppc64le`, or `s390x`

> [!NOTE]
> Starting with RHACS 4.3, both Central and secured cluster services are supported on IBM Power(`ppc64le`), IBM Z(`s390x`), and IBM® LinuxONE(`s390x`) clusters.

Processor  
Requires 3 CPU cores.

Memory  
Requires 6 GiB of RAM.

> [!NOTE]
> See the default memory and CPU requirements for each component and ensure that the node size can support them.

Storage  
Requires a persistent volume claim (PVC) on the cluster where you install Central. Red Hat strongly recommends a PVC on the secured clusters where you enable Scanner V4. Use Solid-State Drives (SSDs) for best performance. However, you can use another storage type if you do not have SSDs available.

> [!IMPORTANT]
> You must not use Ceph FS storage with Red Hat Advanced Cluster Security for Kubernetes. Red Hat recommends using RBD block mode PVCs for Red Hat Advanced Cluster Security for Kubernetes.

<a id="acs-helm-requirements_acs-default-requirements"></a>

## Helm requirements

Requirements for installing RHACS using Helm charts.

If you plan to install RHACS by using Helm charts, you must meet the following requirements:

- You must have Helm command-line interface (CLI) v3.2 or newer, if you are installing or configuring RHACS using Helm charts. Use the `helm version` command to verify the version of Helm you have installed.

- You must have access to the Red Hat Container Registry.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

- [Red Hat Advanced Cluster Security for Kubernetes Support Policy](https://access.redhat.com/support/policy/updates/rhacs)

- [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication)

</div>

<a id="default-requirements-central-services_acs-default-requirements"></a>

# Central services (self-managed)

Central services include Central, Scanner V4, and StackRox Scanner components that require specific CPU, memory, and storage resources.

> [!NOTE]
> If you are using Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service), you do not need to review the requirements for Central services, because Red Hat manages them. You only need to examine the requirements for secured cluster services.

Central services contain the following components:

- Central

- Scanner V4

- StackRox Scanner: Although the StackRox Scanner is deprecated, you still must enable it on the cluster where you install Central due to software dependencies.

<a id="default-requirements-central-services-central_acs-default-requirements"></a>

## Central

A containerized service called Central handles API interactions and RHACS web portal access while a containerized service called Central DB (PostgreSQL 15) handles data persistence.

Central DB requires persistent storage in the cluster where you install Central.

- You can use a persistent volume claim (PVC) for storage.

  > [!NOTE]
  > You can use a hostPath volume for storage only if all your hosts (or a group of hosts) mount a shared file system, such as an NFS share or a storage appliance. Otherwise, your data is only saved on a single node. Red Hat does not recommend using a hostPath volume.

- Use Solid-State Drives (SSDs) for best performance. However, you can use another storage type if you do not have SSDs available.

- If you use a web proxy or firewall, you must configure bypass rules to allow traffic for the `definitions.stackrox.io` domain and enable RHACS to trust your web proxy or firewall. Otherwise, updates for vulnerabilities will fail. You must also ensure that incoming connections from Sensor on secured clusters to Central on port 443 are possible.

  Red Hat Advanced Cluster Security for Kubernetes requires access to:

  - `definitions.stackrox.io` for downloading updated vulnerability data. Vulnerability updates allow Red Hat Advanced Cluster Security for Kubernetes to keep vulnerability data current when the security community discovers new vulnerabilities or adds data sources.

> [!NOTE]
> For security reasons, you should deploy Central in a cluster with limited administrative access.

<a id="central-resource-requirements_acs-default-requirements"></a>

## CPU, memory, and storage requirements

CPU, memory, and storage requirements for Central and Central DB.

The following table lists the minimum CPU and memory values required to install and run Central.

| Central     | CPU       | Memory |
|-------------|-----------|--------|
| **Request** | 1.5 cores | 4 GiB  |
| **Limit**   | 4 cores   | 8 GiB  |

Central requires Central DB to store data. The following table lists the minimum CPU, memory, and storage values required to install and run Central DB.

| Central DB  | CPU     | Memory | Storage |
|-------------|---------|--------|---------|
| **Request** | 4 cores | 8 GiB  | 100 GiB |
| **Limit**   | 8 cores | 16 GiB | 100 GiB |

<a id="default-requirements-central-services-scanner_acs-default-requirements"></a>

## Scanner

Scanner is responsible for scanning images, nodes, and the platform for vulnerabilities.

RHACS includes two image vulnerability scanners: StackRox Scanner and Scanner V4. The StackRox Scanner is deprecated. Scanner V4 became available in release 4.4 and as of release 4.8 is the default image scanner.

<a id="stackrox-scanner-requirements_acs-default-requirements"></a>

## StackRox Scanner

CPU and memory requirements for StackRox Scanner and Scanner DB.

The following table lists the minimum CPU and memory values required to install and run StackRox Scanner. This table assumes the default of 3 replicas.

| StackRox Scanner | CPU     | Memory   |
|------------------|---------|----------|
| **Request**      | 3 cores | 4500 MiB |
| **Limit**        | 6 cores | 12 GiB   |

The StackRox Scanner requires Scanner DB (PostgreSQL 15) to store data. This data is not persisted. The following table lists the minimum CPU and memory values required to install and run Scanner DB.

| Scanner DB  | CPU       | Memory  |
|-------------|-----------|---------|
| **Request** | 0.2 cores | 512 MiB |
| **Limit**   | 2 cores   | 4 GiB   |

<a id="default-requirements-central-services-scanner-v4_acs-default-requirements"></a>

## Scanner V4 Indexer

CPU and memory requirements for Scanner V4 Indexer.

This table assumes the default of 3 replicas.

| Scanner V4 Indexer | CPU       | Memory   |
|--------------------|-----------|----------|
| **Request**        | 4.5 cores | 1536 MiB |
| **Limit**          | 12 cores  | 9 GiB    |

<a id="scanner-v4-matcher-requirements_acs-default-requirements"></a>

## Scanner V4 Matcher

CPU and memory requirements for Scanner V4 Matcher.

This table assumes the default of 2 replicas.

| Scanner V4 Matcher | CPU     | Memory |
|--------------------|---------|--------|
| **Request**        | 1 core  | 3 GiB  |
| **Limit**          | 2 cores | 6 GiB  |

<a id="scanner-v4-db-requirements_acs-default-requirements"></a>

## Scanner V4 DB

CPU, memory, and storage requirements for Scanner V4 DB.

Scanner V4 requires Scanner V4 DB (PostgreSQL 15) to store data. The following table lists the minimum CPU, memory, and storage values required to install and run Scanner V4 DB. For Scanner V4 DB, a PVC is not required, but it is strongly recommended because it ensures optimal performance.

| Scanner V4 DB | CPU     | Memory | Storage |
|---------------|---------|--------|---------|
| **Request**   | 1 core  | 4 GiB  | 50 GiB  |
| **Limit**     | 4 cores | 8 GiB  | 50 GiB  |

<a id="default-requirements-secured-cluster-services_acs-default-requirements"></a>

# Secured cluster services

Secured cluster services include Sensor, Admission controller, Collector, and optional Scanner components that run on your Kubernetes and OpenShift Container Platform clusters.

Secured cluster services contain the following components:

- Sensor

- Admission controller

- Collector

- Scanner (optional)

- Scanner V4 (optional)

If you use a web proxy or firewall, you must ensure that secured clusters and Central can communicate on HTTPS port 443.

<a id="default-requirements-secured-cluster-services-sensor_acs-default-requirements"></a>

## Sensor

Sensor monitors your Kubernetes and OpenShift Container Platform clusters and coordinates with other Red Hat Advanced Cluster Security for Kubernetes components.

Sensor services currently deploy in a single deployment, which handles interactions with the Kubernetes API and coordinates with the other Red Hat Advanced Cluster Security for Kubernetes components.

<a id="sensor-resource-requirements_acs-default-requirements"></a>

## CPU and memory requirements

CPU and memory requirements for Sensor on secured clusters.

The following table lists the minimum CPU and memory values required to install and run sensor on secured clusters.

| Sensor      | CPU     | Memory |
|-------------|---------|--------|
| **Request** | 2 cores | 4 GiB  |
| **Limit**   | 4 cores | 8 GiB  |

<a id="default-requirements-secured-cluster-services-admission-controller_acs-default-requirements"></a>

## Admission controller

The Admission controller prevents users from creating workloads that violate policies you configure.

<a id="admission-controller-resource-requirements_acs-default-requirements"></a>

## CPU and memory requirements

CPU and memory requirements for the Admission controller.

By default, the admission control service runs 3 replicas. The following table lists the request and limits for each replica.

| Admission controller | CPU        | Memory  |
|----------------------|------------|---------|
| **Request**          | 0.05 cores | 100 MiB |
| **Limit**            | 0.5 cores  | 500 MiB |

> [!NOTE]
> When you enable admission controller policy enforcement, the system automatically increases the memory limit to 1 GiB per replica to support image scan data caching requirements. If you specify a custom memory limit override, the custom value takes priority. For more information, see "Admission controller settings for the Operator" and "Configuration parameters for Helm".

<a id="default-requirements-secured-cluster-services-collector_acs-default-requirements"></a>

## Collector

Collector monitors runtime activity on each node in your secured clusters as a DaemonSet.

It connects to Sensor to report this information. The collector pod has three containers. The first container is collector, which monitors and reports the runtime activity on the node. The other two are compliance and node-inventory.

<a id="collector-collection-requirements_acs-default-requirements"></a>

## Collection requirements

Requirements for using the CORE_BPF collection method with Collector.

To use the `CORE_BPF` collection method, the base kernel must support Berkeley Packet Filter (BPF) Type Format (BTF), and the BTF file must be available to collector. In general, the kernel version must be later than 5.8 (4.18 for RHEL nodes) and you must set the `CONFIG_DEBUG_INFO_BTF` configuration option.

Collector looks for the BTF file in the following standard locations:

<div class="formalpara">

<div class="title">

Example file paths

</div>

``` terminal
/sys/kernel/btf/vmlinux
/boot/vmlinux-<kernel_version>
/lib/modules/<kernel_version>/vmlinux-<kernel_version>
/lib/modules/<kernel_version>/build/vmlinux
/usr/lib/modules/<kernel_version>/kernel/vmlinux
/usr/lib/debug/boot/vmlinux-<kernel_version>
/usr/lib/debug/boot/vmlinux-<kernel_version>.debug
/usr/lib/debug/lib/modules/<kernel_version>/vmlinux
```

</div>

If any of these files exists, it is likely that the kernel has BTF support and `CORE_BPF` is configurable.

<a id="collector-cpu-memory-requirements_acs-default-requirements"></a>

## CPU and memory requirements

By default, the collector pod runs 3 containers. The following tables list the CPU and memory requirements for each container and the total for each collector pod.

<a id="collector-container-requirements_acs-default-requirements"></a>

## Collector container

CPU and memory requirements for the collector container.

| Type        | CPU        | Memory   |
|-------------|------------|----------|
| **Request** | 0.06 cores | 320 MiB  |
| **Limit**   | 0.9 cores  | 1000 MiB |

<a id="compliance-container-requirements_acs-default-requirements"></a>

## Compliance container

CPU and memory requirements for the compliance container.

| Type        | CPU        | Memory   |
|-------------|------------|----------|
| **Request** | 0.01 cores | 10 MiB   |
| **Limit**   | 1 core     | 2000 MiB |

<a id="node-inventory-container-requirements_acs-default-requirements"></a>

## Node-inventory container

CPU and memory requirements for the node-inventory container.

| Type        | CPU        | Memory  |
|-------------|------------|---------|
| **Request** | 0.01 cores | 10 MiB  |
| **Limit**   | 1 core     | 500 MiB |

<a id="collector-total-requirements_acs-default-requirements"></a>

## Total collector pod requirements

Total CPU and memory requirements for the entire collector pod.

| Type        | CPU        | Memory   |
|-------------|------------|----------|
| **Request** | 0.07 cores | 340 MiB  |
| **Limit**   | 2.75 cores | 3500 MiB |

<a id="default-requirements-secured-cluster-services-scanner_acs-default-requirements"></a>

## Scanner

CPU and memory requirements for StackRox Scanner and Scanner DB on secured clusters.

This table assumes the default of 3 replicas.

| StackRox Scanner | CPU     | Memory   |
|------------------|---------|----------|
| **Request**      | 3 cores | 4500 MiB |
| **Limit**        | 6 cores | 12 GiB   |

The StackRox Scanner requires Scanner DB (PostgreSQL 15) to store data. The following table lists the minimum memory and storage values required to install and run Scanner DB.

| Scanner DB  | CPU       | Memory  |
|-------------|-----------|---------|
| **Request** | 0.2 cores | 512 MiB |
| **Limit**   | 2 cores   | 4 GiB   |

<a id="default-requirements-secured-cluster-services-scanner-v4_acs-default-requirements"></a>

## Scanner V4 Indexer

CPU and memory requirements for Scanner V4 Indexer on secured clusters.

Scanner V4 is optional. If you install Scanner V4 on secured clusters, the following requirements apply.

This table assumes the default of 2 replicas.

| Scanner V4 Indexer | CPU     | Memory   |
|--------------------|---------|----------|
| **Request**        | 2 cores | 3000 MiB |
| **Limit**          | 4 cores | 6 GiB    |

<a id="secured-cluster-scanner-v4-db-requirements_acs-default-requirements"></a>

## Scanner V4 DB

CPU, memory, and storage requirements for Scanner V4 DB on secured clusters.

Scanner V4 requires Scanner V4 DB (PostgreSQL 15) to store data. The following table lists the minimum CPU, memory, and storage values required to install and run Scanner V4 DB. For Scanner V4 DB, a PVC is not required, but it is strongly recommended because it ensures optimal performance.

| Scanner V4 DB | CPU       | Memory | Storage |
|---------------|-----------|--------|---------|
| **Request**   | 0.2 cores | 2 GiB  | 10 GiB  |
| **Limit**     | 2 cores   | 4 GiB  | 10 GiB  |

<div>

<div class="title">

Additional resources

</div>

- [Admission controller settings for the Operator](installing_ocp/install-secured-cluster-config-options-ocp.md#admission-controller-settings_install-secured-cluster-config-options-ocp)

- [Configuration parameters for Helm](installing_ocp/install-secured-cluster-ocp.md#secured-cluster-services-config_install-secured-cluster-ocp)

</div>

<a id="external-db-req_acs-default-requirements"></a>

# Requirements for using an external database

You can configure Red Hat Advanced Cluster Security for Kubernetes Central services to use an external PostgreSQL-compatible database for data persistence instead of deploying its own database pod.

> [!IMPORTANT]
> When you use an external database, note the following guidance:
>
> - The database infrastructure manages persistent storage for Central DB. Therefore, do not configure persistence settings for the Central DB within the RHACS installation configuration.
>
> - Red Hat supports the configuration and operation of RHACS Central connected to that database. However, support for database-specific operations such as backup and restore, performance diagnosis and potential tuning, software and version upgrades, and high availability/disaster recovery operation falls under third-party support. Manually upgrading or customizing your database outside of a full platform upgrade also limits supportability.

If you select an external database, your database instance and the user connecting to it must meet the requirements listed in the following sections.

<a id="external-db-type-version_acs-default-requirements"></a>

## Database type and version

Database type and version requirements for using an external database.

The database must be a PostgreSQL-compatible database that supports PostgreSQL 13 or later.

<a id="external-db-user-permissions_acs-default-requirements"></a>

## User permissions

User permissions required for connecting to an external database.

The user account that Central uses to connect to the database must be a `superuser` account with connection rights to the database and the following permissions:

- `Usage` and `Create` permissions on the schema.

- `Select`, `Insert`, `Update`, and `Delete` permissions on all tables in the schema.

- `Usage` permissions on all sequences in the schema.

- The ability to create and delete databases as a `superuser`.

<a id="external-db-connection-string_acs-default-requirements"></a>

## Connection string

Connection string format for connecting to an external database.

Central connects to the external database by using a connection string, which must be in `keyword=value` format. The connection string should specify details such as the host, port, database name, user, and SSL/TLS mode. For example, `host=<host> port=5432 database=stackrox user=stackrox sslmode=verify-ca`.

> [!NOTE]
> Connections through **PgBouncer** are not supported.

<a id="external-db-ca-certificates_acs-default-requirements"></a>

## CA certificates

CA certificate requirements for connecting to an external database with untrusted certificates.

If your external database uses a certificate issued by a private or untrusted Certificate Authority (CA), you might need to specify the CA certificate so that Central trusts the database certificate. You can add this by using a TLS block in the Central custom resource configuration.

<div>

<div class="title">

Additional resources

</div>

- Provisioning a database in your PostgreSQL instance (unavailable upstream reference: `../installing/installing-rhacs-on-red-hat-openshift.xml#provision-postgresql-database_install-central-ocp`)

</div>
