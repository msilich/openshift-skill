<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Learn about the installation methods, requirements, and process for deploying an OpenShift Container Platform cluster.

# The OpenShift Container Platform installation

The OpenShift Container Platform installation program offers four methods for deploying a cluster. Each method has unique characteristics so that you can choose a method that meets your needs.

The following list details these methods:

- **Interactive**: You can deploy a cluster with the web-based Assisted Installer. This is an ideal approach for clusters with networks connected to the internet. The Assisted Installer is the easiest way to install OpenShift Container Platform. Assisted Installer provides smart defaults and performs pre-flight validations before installing the cluster. Assisted Installer also provides a RESTful API for automation and advanced configuration scenarios.

- **Local Agent-based**: You can deploy a cluster locally with the Agent-based Installer for disconnected environments or restricted networks. The Local Agent-based installer provides many of the benefits of the Assisted Installer, but you must download and configure the Agent-based Installer first. Configuration is done with a command-line interface. This approach is ideal for disconnected environments.

  - Additionally, you can deploy a cluster without an external registry, using self-contained installation media that also provides a simplified user interface similar to the Assisted Installer during on-premise installations. For more information, see "Installing a cluster without an external registry".

- **Automated**: You can deploy a cluster on installer-provisioned infrastructure. The installation program uses each cluster host’s baseboard management controller (BMC) for provisioning. You can deploy clusters in connected or disconnected environments.

- **Full control**: You can deploy a cluster on infrastructure that you prepare and maintain, which provides maximum customizability. You can deploy clusters in connected or disconnected environments.

Each method deploys a cluster with the following characteristics:

- Highly available infrastructure with no single points of failure, which is available by default.

- Administrators can control what updates are applied and when.

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster without an external registry](../installing_with_agent_based_installer/installing-ove.md#installing-ove)

</div>

## Glossary of common terms for OpenShift Container Platform installing

The glossary defines common terms that relate to the installation content. Read the following list of terms to better understand the installation process.

Assisted Installer
An installer hosted at [console.redhat.com](https://console.redhat.com/openshift/assisted-installer/clusters/~new) that provides a web-based user interface or a RESTful API for creating a cluster configuration. The [Assisted Installer](https://access.redhat.com/documentation/en-us/assisted_installer_for_openshift_container_platform) generates a discovery image. Cluster machines boot with the discovery image, which installs RHCOS and an agent. Together, the Assisted Installer and agent provide preinstallation validation and installation for the cluster.

Agent-based Installer
An installer similar to the Assisted Installer, but you must download the [Agent-based Installer](https://console.redhat.com/openshift/install/metal/agent-based) first. The Agent-based Installer is ideal for disconnected environments.

Bootstrap node
A temporary machine that runs a minimal Kubernetes configuration required to deploy the OpenShift Container Platform control plane.

Control plane
A container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers. Also known as control plane machines.

Compute node
Nodes that are responsible for executing workloads for cluster users. Also known as worker nodes.

Disconnected installation
In some situations, parts of a data center might not have access to the internet, even through proxy servers. You can still install the OpenShift Container Platform in these environments, but you must download the required software and images and make them available to the disconnected environment.

The OpenShift Container Platform installation program
A program that provisions the infrastructure and deploys a cluster.

Installer-provisioned infrastructure
The installation program deploys and configures the infrastructure that the cluster runs on.

Ignition config files
A file that the Ignition tool uses to configure Red Hat Enterprise Linux CoreOS (RHCOS) during operating system initialization. The installation program generates different Ignition configuration files to initialize bootstrap, control plane, and worker nodes.

Kubernetes manifests
Specifications of a Kubernetes API object in a JSON or YAML format. A configuration file can include deployments, config maps, secrets, daemonsets, and so on.

kubelet
A primary node agent that runs on each node in the cluster to ensure that containers are running in a pod.

Load balancers
A load balancer serves as the single point of contact for clients. Load balancers for the API distribute incoming traffic across control plane nodes.

Machine Config Operator
An Operator that manages and applies configurations and updates of the base operating system and container runtime, including everything between the kernel and kubelet, for the nodes in the cluster.

Operators
The preferred method of packaging, deploying, and managing a Kubernetes application in an OpenShift Container Platform cluster. An operator takes human operational knowledge and encodes it into software that is easily packaged and shared with customers.

User-provisioned infrastructure
You can install OpenShift Container Platform on infrastructure that you provide. You can use the installation program to generate the assets required to provision the cluster infrastructure, create the cluster infrastructure, and then deploy the cluster to the infrastructure that you provided.

## Installation process

The OpenShift Container Platform installation program transforms a set of assets into a running cluster, using an installation process that varies depending on your installation method.

Except for the Assisted Installer, when you install an OpenShift Container Platform cluster, you must download the installation program from the appropriate **Cluster Type** page on the OpenShift Cluster Manager Hybrid Cloud Console. This console manages:

- REST API for accounts.

- Registry tokens, which are the pull secrets that you use to obtain the required components.

- Cluster registration, which associates the cluster identity to your Red Hat account to facilitate the gathering of usage metrics.

In OpenShift Container Platform 4.20, the installation program is a Go binary file that performs a series of file transformations on a set of assets. The way you interact with the installation program differs depending on your installation type. Consider the following installation use cases:

- To deploy a cluster with the Assisted Installer, you must configure the cluster settings by using the Assisted Installer. There is no installation program to download and configure. After you finish setting the cluster configuration, you download a discovery ISO and then boot cluster machines with that image. You can install clusters with the Assisted Installer on Nutanix, vSphere, and bare metal with full integration, and other platforms without integration. If you install on bare metal, you must provide all of the cluster infrastructure and resources, including the networking, load balancing, storage, and individual cluster machines.

- To deploy clusters with the Agent-based Installer, you can download the Agent-based Installer first. You can then configure the cluster and generate a discovery image. You boot cluster machines with the discovery image, which installs an agent that communicates with the installation program and handles the provisioning for you instead of you interacting with the installation program or setting up a provisioner machine yourself. You must provide all of the cluster infrastructure and resources, including the networking, load balancing, storage, and individual cluster machines. This approach is ideal for disconnected environments.

- For clusters with installer-provisioned infrastructure, you delegate the infrastructure bootstrapping and provisioning to the installation program instead of doing it yourself. The installation program creates all of the networking, machines, and operating systems that are required to support the cluster, except if you install on bare metal. If you install on bare metal, you must provide all of the cluster infrastructure and resources, including the bootstrap machine, networking, load balancing, storage, and individual cluster machines.

- If you provision and manage the infrastructure for your cluster, you must provide all of the cluster infrastructure and resources, including the bootstrap machine, networking, load balancing, storage, and individual cluster machines.

The installation program uses three sets of files during installation: an installation configuration file that is named `install-config.yaml`, Kubernetes manifests, and Ignition config files for your machine types.

> [!IMPORTANT]
> You can modify Kubernetes and the Ignition config files that control the underlying RHCOS operating system during installation. However, no validation is available to confirm the suitability of any modifications that you make to these objects. If you modify these objects, you might render your cluster non-functional. Because of this risk, modifying Kubernetes and Ignition config files is not supported unless you are following documented procedures or are instructed to do so by Red Hat support.

The installation configuration file is transformed into Kubernetes manifests, and then the manifests are wrapped into Ignition config files. The installation program uses these Ignition config files to create the cluster.

The installation configuration files are all pruned when you run the installation program, ensure you back up all the configuration files that you want to use again.

> [!IMPORTANT]
> You cannot modify the parameters that you set during installation, but you can modify many cluster attributes after installation.

The installation process with the Assisted Installer
Installation with the Assisted Installer involves creating a cluster configuration interactively by using the web-based user interface or the RESTful API. The Assisted Installer user interface prompts you for required values and provides reasonable default values for the remaining parameters, unless you change them in the user interface or with the API. The Assisted Installer generates a discovery image, which you download and use to boot the cluster machines. The image installs RHCOS and an agent, and the agent handles the provisioning for you. You can install OpenShift Container Platform with the Assisted Installer and full integration on Nutanix, vSphere, and bare metal. Additionally, you can install OpenShift Container Platform with the Assisted Installer on other platforms without integration.

OpenShift Container Platform manages all aspects of the cluster, including the operating system itself. Each machine boots with a configuration that references resources hosted in the cluster that it joins. This configuration allows the cluster to manage itself as updates are applied.

If possible, use the Assisted Installer feature to avoid having to download and configure the Agent-based Installer.

The installation process with Agent-based infrastructure
Agent-based installation is similar to using the Assisted Installer, except that you must initially download and install the Agent-based Installer. An Agent-based installation is useful when you want the convenience of the Assisted Installer, but you need to install a cluster in a disconnected environment.

If possible, use the Agent-based installation feature to avoid having to create a provisioner machine with a bootstrap VM, and then provision and maintain the cluster infrastructure.

The installation process with installer-provisioned infrastructure
The default installation type uses installer-provisioned infrastructure. By default, the installation program acts as an installation wizard, prompting you for values that it cannot determine on its own and providing reasonable default values for the remaining parameters. You can also customize the installation process to support advanced infrastructure scenarios. The installation program provisions the underlying infrastructure for the cluster.

You can install either a standard cluster or a customized cluster. With a standard cluster, you provide minimum details that are required to install the cluster. With a customized cluster, you can specify more details about the platform, such as the number of machines that the control plane uses, the type of virtual machine that the cluster deploys, or the CIDR range for the Kubernetes service network.

If possible, use this feature to avoid having to provision and maintain the cluster infrastructure. In all other environments, you use the installation program to generate the assets that you require to provision your cluster infrastructure.

With installer-provisioned infrastructure clusters, OpenShift Container Platform manages all aspects of the cluster, including the operating system itself. Each machine boots with a configuration that references resources hosted in the cluster that it joins. This configuration allows the cluster to manage itself as updates are applied.

The installation process with user-provisioned infrastructure
You can also install OpenShift Container Platform on infrastructure that you provide. You use the installation program to generate the assets that you require to provision the cluster infrastructure, create the cluster infrastructure, and then deploy the cluster to the infrastructure that you provided.

If you do not use infrastructure that the installation program provisioned, you must manage and maintain the cluster resources yourself. The following list details some of these self-managed resources:

- The underlying infrastructure for the control plane and compute machines that make up the cluster

- Load balancers

- Cluster networking, including the DNS records and required subnets

- Storage for the cluster infrastructure and applications

  If your cluster uses user-provisioned infrastructure, you have the option of adding RHEL compute machines to your cluster.

<div>

<div class="title">

Additional resources

</div>

- [Recommended etcd practices](../../etcd/etcd-practices.md#recommended-etcd-practices)

- [Control plane node sizing](../../scalability_and_performance/recommended-performance-scale-practices/recommended-control-plane-practices.md#master-node-sizing_recommended-control-plane-practices)

- [Red Hat OpenShift Network Calculator](https://access.redhat.com/labs/ocpnc/)

</div>

## Verifying node state after installation

The OpenShift Container Platform installation completes when the following installation health checks are successful:

- The provisioner can access the OpenShift Container Platform web console.

- All control plane nodes are ready.

- All cluster Operators are available.

> [!NOTE]
> After the installation completes, the specific cluster Operators responsible for the worker nodes continuously attempt to provision all worker nodes. Some time is required before all worker nodes report as `READY`. For installations on bare metal, wait a minimum of 60 minutes before troubleshooting a worker node. For installations on all other platforms, wait a minimum of 40 minutes before troubleshooting a worker node. A `DEGRADED` state for the cluster Operators responsible for the worker nodes depends on the Operators' own resources and not on the state of the nodes.

After your installation completes, you can continue to monitor the condition of the nodes in your cluster.

<div>

<div class="title">

Prerequisites

</div>

- The installation program resolves successfully in the terminal.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Show the status of all worker nodes:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                           STATUS   ROLES    AGE   VERSION
    example-compute1.example.com   Ready    worker   13m   v1.21.6+bb8d50a
    example-compute2.example.com   Ready    worker   13m   v1.21.6+bb8d50a
    example-compute4.example.com   Ready    worker   14m   v1.21.6+bb8d50a
    example-control1.example.com   Ready    master   52m   v1.21.6+bb8d50a
    example-control2.example.com   Ready    master   55m   v1.21.6+bb8d50a
    example-control3.example.com   Ready    master   55m   v1.21.6+bb8d50a
    ```

    </div>

2.  Show the phase of all worker machine nodes:

    ``` terminal
    $ oc get machines -A
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAMESPACE               NAME                           PHASE         TYPE   REGION   ZONE   AGE
    openshift-machine-api   example-zbbt6-master-0         Running                              95m
    openshift-machine-api   example-zbbt6-master-1         Running                              95m
    openshift-machine-api   example-zbbt6-master-2         Running                              95m
    openshift-machine-api   example-zbbt6-worker-0-25bhp   Running                              49m
    openshift-machine-api   example-zbbt6-worker-0-8b4c2   Running                              49m
    openshift-machine-api   example-zbbt6-worker-0-jkbqt   Running                              49m
    openshift-machine-api   example-zbbt6-worker-0-qrl5b   Running                              49m
    ```

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Getting the BareMetalHost resource](../installing_bare_metal/bare-metal-postinstallation-configuration.md#bmo-getting-the-baremetalhost-resource_bare-metal-postinstallation-configuration)

- [Following the progress of the installation](../installing_bare_metal/ipi/ipi-install-installing-a-cluster.md#ipi-install-following-the-progress-of-the-installation_ipi-install-installing-a-cluster)

- [Validating an installation](../validation_and_troubleshooting/validating-an-installation.md#validating-an-installation)

- [Agent-based Installer](../installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.md#preparing-to-install-with-agent-based-installer)

- [Assisted Installer for OpenShift Container Platform](https://access.redhat.com/documentation/en-us/assisted_installer_for_openshift_container_platform)

</div>

## Installation scope

The scope of the OpenShift Container Platform installation program is intentionally narrow. It is designed for simplicity and ensured success. You can complete many more configuration tasks after installation completes.

<div>

<div class="title">

Additional resources

</div>

- [Available cluster customizations](../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations)

</div>

## OpenShift Local overview

OpenShift Local supports rapid application development to get started building OpenShift Container Platform clusters. OpenShift Local is designed to run on a local computer to simplify setup and testing, and to emulate the cloud development environment locally with all of the tools needed to develop container-based applications.

Regardless of the programming language you use, OpenShift Local hosts your application and brings a minimal, preconfigured Red Hat OpenShift Container Platform cluster to your local PC without the need for a server-based infrastructure.

On a hosted environment, OpenShift Local can create microservices, convert them into images, and run them in Kubernetes-hosted containers directly on your laptop or desktop running Linux, macOS, or Windows 10 or later.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat OpenShift Local Overview](https://developers.redhat.com/products/openshift-local/overview)

</div>

# Supported platforms for OpenShift Container Platform clusters

Review the platform support matrix to choose the installation method that meets your requirements.

| Platform | Installer-provisioned infrastructure <sup>\[1\]</sup> | User-provisioned infrastructure <sup>\[2\]</sup> | Agent-based Installer | Assisted Installer |
|----|----|----|----|----|
| **Amazon Web Services (AWS)** | X | X |  |  |
| **Bare metal** | X | X | X | X |
| **External** |  |  | X | X |
| **Google Cloud** | X | X |  |  |
| **IBM Cloud® Classic** | X |  |  |  |
| **IBM Cloud® Virtual Private Cloud (VPC)** | X |  |  |  |
| **IBM Power®** |  | X | X | X |
| **IBM Z® or IBM® LinuxONE** |  | X | X | X |
| **Microsoft Azure** | X | X |  |  |
| **Microsoft Azure Stack Hub** | X | X |  |  |
| **None** |  |  | X | X |
| **Nutanix** | X |  |  | X |
| **Oracle Cloud Infrastructure (OCI)** |  |  | X | X |
| **Red Hat OpenStack Platform (RHOSP) <sup>\[3\]</sup>** | X | X |  |  |
| **VMware vSphere** | X | X | X | X |

Supported platforms

The following list describes three different deployment pathways and their prerequisites:

- For installer-provisioned infrastructure: All machines, including the computer that you run the installation process on, must have direct internet access to pull images for platform containers and provide telemetry data to Red Hat.

  > [!IMPORTANT]
  > After installation, the following changes are not supported:
  >
  > - Mixing cloud provider platforms.
  >
  > - Mixing cloud provider components. For example, using a persistent storage framework from another platform on the platform where you installed the cluster.

- For user-provisioned infrastructure: Depending on the supported cases for the platform, you can perform installations on user-provisioned infrastructure so that you can run machines with full internet access, place your cluster behind a proxy, or perform a disconnected installation.

  In a disconnected installation, you can download the images that are required to install a cluster, place them in a mirror registry, and use that data to install your cluster. While you require internet access to pull images for platform containers, with a disconnected installation on vSphere or bare-metal infrastructure, your cluster machines do not require direct internet access.

- For Red Hat OpenStack Platform (RHOSP): The latest OpenShift Container Platform release supports both the latest RHOSP long-life release and intermediate release. For complete RHOSP release compatibility, see "OpenShift Container Platform on RHOSP support matrix". See "OpenShift Container Platform 4.x Tested Integrations" for details about integration testing for different platforms.

<div>

<div class="title">

Additional resources

</div>

- [Supported installation methods for different platforms](installing-preparing.md#installing-preparing-supported-installation-methods-reference_installing-preparing)

- [Selecting a cluster installation method and preparing it for users](installing-preparing.md#installing-preparing)

- [Red Hat OpenShift Network Calculator](https://access.redhat.com/labs/ocpnc/)

</div>
