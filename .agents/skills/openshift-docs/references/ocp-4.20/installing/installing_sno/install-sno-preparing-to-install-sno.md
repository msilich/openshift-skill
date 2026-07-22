<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Review the different requirements for installing OpenShift Container Platform on a single node and prepare your environment for installation.

Ensure you have reviewed the following documentation before preparing for a single node installation:

- "OpenShift Container Platform installation and update"

- "Selecting a cluster installation method and preparing it for users"

# About OpenShift on a single node

You can create a single-node cluster with standard installation methods. OpenShift Container Platform on a single node is a specialized installation that requires the creation of a special Ignition configuration file.

The primary use case is for edge computing workloads, including intermittent connectivity, portable clouds, and 5G radio access networks (RAN) close to a base station. The major tradeoff with an installation on a single node is the lack of high availability.

> [!IMPORTANT]
> The use of OpenShiftSDN with single-node OpenShift is not supported. OVN-Kubernetes is the default network plugin for single-node OpenShift deployments.

# Requirements for installing OpenShift on a single node

Installing OpenShift Container Platform on a single node alleviates some of the requirements for high availability and large scale clusters. However, you must still address several requirements.

The following requirements must be met:

- **Administration host:** You must have a computer to prepare the ISO, to create the USB boot drive, and to monitor the installation.

  > [!NOTE]
  > For the `ppc64le` platform, the host should prepare the ISO, but does not need to create the USB boot drive. The ISO can be mounted to PowerVM directly.

  > [!NOTE]
  > ISO is not required for IBM Z® installations.

- **CPU Architecture:** Installing OpenShift Container Platform on a single node supports `x86_64`, `arm64`,`ppc64le`, and `s390x` CPU architectures.

- **Supported platforms:** Installing OpenShift Container Platform on a single node is supported on bare metal and Certified third-party hypervisors. See "Certified Hypervisors and Guest Operating Systems" for more information. In most cases, you must specify the `platform.none: {}` parameter in the `install-config.yaml` configuration file. The following list shows the only exceptions and the corresponding parameter to specify in the `install-config.yaml` configuration file:

  - Amazon Web Services (AWS), where you use `platform=aws`

  - Google Cloud, where you use `platform=gcp`

  - Microsoft Azure, where you use `platform=azure`

- **Production-grade server:** Installing OpenShift Container Platform on a single node requires a server with sufficient resources to run OpenShift Container Platform services and a production workload.

  | Profile | Compute | Memory       | Storage |
  |---------|---------|--------------|---------|
  | Minimum | 8 vCPUs | 16 GB of RAM | 120 GB  |

  Minimum resource requirements

  > [!NOTE]
  > One vCPU generally equals one physical core. However, if you enable simultaneous multithreading (SMT), or Hyper-Threading, each CPU thread counts as a vCPU.
  >
  > Adding Operators during the installation process might increase the minimum resource requirements.

  The server must have a Baseboard Management Controller (BMC) when booting with virtual media.

  > [!NOTE]
  > BMC is not supported on IBM Z® and IBM Power®.

- **Networking:** The server must have access to the internet or access to a local registry if it is not connected to a routable network. The server must have a DHCP reservation or a static IP address for the Kubernetes API, ingress route, and cluster node domain names. You must configure the DNS to resolve the IP address to each of the following fully qualified domain names (FQDN):

  | Usage | FQDN | Description |
  |----|----|----|
  | Kubernetes API | `api.<cluster_name>.<base_domain>` | Add a DNS A/AAAA or CNAME record. This record must be resolvable by both clients external to the cluster and within the cluster. |
  | Internal API | `api-int.<cluster_name>.<base_domain>` | Add a DNS A/AAAA or CNAME record when creating the ISO manually. This record must be resolvable by nodes within the cluster. |
  | Ingress route | `*.apps.<cluster_name>.<base_domain>` | Add a wildcard DNS A/AAAA or CNAME record that targets the node. This record must be resolvable by both clients external to the cluster and within the cluster. |

  Required DNS records

  > [!IMPORTANT]
  > Without persistent IP addresses, communications between the `apiserver` and `etcd` might fail.

<div>

<div class="title">

Additional resources

</div>

- [Certified Hypervisors and Guest Operating Systems (Red Hat Knowledgebase article)](https://access.redhat.com/articles/973163)

</div>

# Additional resources

- [OpenShift Container Platform installation and update](../../architecture/architecture-installation.md#architecture-installation)

- [Selecting a cluster installation method and preparing it for users](../overview/installing-preparing.md#installing-preparing)
