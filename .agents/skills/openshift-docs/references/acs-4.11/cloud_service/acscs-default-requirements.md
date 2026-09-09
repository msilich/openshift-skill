<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

This document describes the default CPU, memory, and storage requirements for Red Hat Advanced Cluster Security Cloud Service components.

<a id="acs-cloud-requirements_acscs-default-requirements"></a>

# General requirements for RHACS Cloud Service

Before you can install Red Hat Advanced Cluster Security Cloud Service, your system must meet several requirements.

<a id="acscs-system-requirements_acscs-default-requirements"></a>

## System requirements

System, architecture, processor, memory, and storage requirements for installing RHACS Cloud Service.

> [!WARNING]
> You must not install RHACS Cloud Service on:
>
> - Amazon Elastic File System (Amazon EFS). Use the Amazon Elastic Block Store (Amazon EBS) with the default **gp2** volume type instead.
>
> - Older CPUs that do not have the Streaming SIMD Extensions (SSE) 4.2 instruction set. For example, Intel processors older than *Sandy Bridge* and AMD processors older than *Bulldozer*. These processor families became available in 2011.

To install RHACS Cloud Service, you must have one of the following systems:

- OpenShift Container Platform version 4.12 or later, and cluster nodes with a supported operating system of Red Hat Enterprise Linux CoreOS (RHCOS) or Red Hat Enterprise Linux (RHEL)

- A supported managed Kubernetes platform, and cluster nodes with a supported operating system of Amazon Linux, CentOS, Container-Optimized operating system from Google, Red Hat Enterprise Linux CoreOS (RHCOS), Debian, Red Hat Enterprise Linux (RHEL), or Ubuntu

For information about supported platforms and architecture, see the "Red Hat Advanced Cluster Security for Kubernetes Support Matrix".

The following minimum requirements and suggestions apply to cluster nodes.

Architecture  
Supported architectures are `amd64`, `ppc64le`, or `s390x`.

> [!NOTE]
> Secured cluster services are supported on IBM Power (`ppc64le`), IBM Z (`s390x`), and IBM® LinuxONE (`s390x`) clusters.

Processor  
Requires 3 CPU cores.

Memory  
Requires 6 GiB of RAM.

> [!NOTE]
> See the default memory and CPU requirements for each component and ensure that the node size can support them.

Storage  
For RHACS Cloud Service, a persistent volume claim (PVC) is not required. However, a PVC is strongly recommended if you have secured clusters with Scanner V4 enabled. Use Solid-State Drives (SSDs) for best performance. However, you can use another storage type if you do not have SSDs available.

> [!IMPORTANT]
> You must not use Ceph FS storage with RHACS Cloud Service. Red Hat recommends using RBD block mode PVCs for RHACS Cloud Service.

<a id="acscs-helm-requirements_acscs-default-requirements"></a>

## Helm requirements

Requirements for installing RHACS Cloud Service using Helm charts.

If you plan to install RHACS Cloud Service by using Helm charts, you must meet the following requirements:

- You must have Helm command-line interface (CLI) v3.2 or newer, if you are installing or configuring RHACS Cloud Service using Helm charts. Use the `helm version` command to verify the version of Helm you have installed.

- You must have access to the Red Hat Container Registry. For information about downloading images from `registry.redhat.io`, see "Red Hat Container Registry Authentication".

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

- [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication)

</div>

<a id="default-requirements-secured-cluster-services_acscs-default-requirements"></a>

# Secured cluster services

Secured cluster services include Sensor, Admission controller, Collector, and optional Scanner components that run on your Kubernetes and OpenShift Container Platform clusters.

Secured cluster services contain the following components:

- Sensor

- Admission controller

- Collector

- Scanner (optional)

- Scanner V4 (optional)

If you use a web proxy or firewall, you must ensure that secured clusters and Central can communicate on HTTPS port 443.

<div>

<div class="title">

Additional resources

</div>

- [Admission controller settings for the Operator](../installing/installing_ocp/install-secured-cluster-config-options-ocp.md#admission-controller-settings_install-secured-cluster-config-options-ocp)

- [Configuration parameters for Helm](../installing/installing_ocp/install-secured-cluster-ocp.md#secured-cluster-services-config_install-secured-cluster-ocp)

</div>
