<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Container Platform is a cloud-based Kubernetes container platform. The foundation of OpenShift Container Platform is based on Kubernetes and therefore shares the same technology. To learn more about OpenShift Container Platform and Kubernetes, see [product architecture](architecture.md#architecture).

# Glossary of common terms for OpenShift Container Platform architecture

This glossary defines common terms that are used in the architecture content.

access policies
A set of roles that dictate how users, applications, and entities within a cluster interact with one another. An access policy increases cluster security.

admission plugins
Admission plugins enforce security policies, resource limitations, or configuration requirements.

authentication
To control access to an OpenShift Container Platform cluster, a cluster administrator can configure user authentication to ensure only approved users access the cluster. To interact with an OpenShift Container Platform cluster, you must authenticate with the OpenShift Container Platform API. You can authenticate by providing an OAuth access token or an X.509 client certificate in your requests to the OpenShift Container Platform API.

bootstrap
A temporary machine that runs minimal Kubernetes and deploys the OpenShift Container Platform control plane.

certificate signing requests (CSRs)
A resource requests a denoted signer to sign a certificate. This request might get approved or denied.

Cluster Version Operator (CVO)
An Operator that checks with the OpenShift Container Platform Update Service to see the valid updates and update paths based on current component versions and information in the graph.

compute nodes
Nodes that are responsible for executing workloads for cluster users. Compute nodes are also known as worker nodes.

configuration drift
A situation where the configuration on a node does not match what the machine config specifies.

containers
Lightweight and executable images that consist of software and all of its dependencies. Because containers virtualize the operating system, you can run containers anywhere, such as data centers, public or private clouds, and local hosts.

container orchestration engine
Software that automates the deployment, management, scaling, and networking of containers.

container workloads
Applications that are packaged and deployed in containers.

control groups (cgroups)
Partitions sets of processes into groups to manage and limit the resources processes consume.

control plane
A container orchestration layer that exposes the API and interfaces to define, deploy, and manage the life cycle of containers. Control planes are also known as control plane machines.

CRI-O
A Kubernetes native container runtime implementation that integrates with the operating system to deliver an efficient Kubernetes experience.

deployment
A Kubernetes resource object that maintains the life cycle of an application.

Dockerfile
A text file that contains the user commands to perform on a terminal to assemble the image.

hosted control planes
A OpenShift Container Platform feature that enables hosting a control plane on the OpenShift Container Platform cluster from its data plane and workers. This model performs the following actions:

- Optimize infrastructure costs required for the control planes.

- Improve the cluster creation time.

- Enable hosting the control plane using the Kubernetes native high level primitives. For example, deployments and stateful sets.

- Allow a strong network segmentation between the control plane and workloads.

hybrid cloud deployments
Deployments that deliver a consistent platform across bare metal, virtual, private, and public cloud environments. This offers speed, agility, and portability.

Ignition
A utility that RHCOS uses to manipulate disks during initial configuration. It completes common disk tasks, including partitioning disks, formatting partitions, writing files, and configuring users.

installer-provisioned infrastructure
The installation program deploys and configures the infrastructure that the cluster runs on.

kubelet
A primary node agent that runs on each node in the cluster to ensure that containers are running in a pod.

kubernetes manifest
Specifications of a Kubernetes API object in a JSON or YAML format. A configuration file can include deployments, config maps, secrets, daemon sets.

Machine Config Daemon (MCD)
A daemon that regularly checks the nodes for configuration drift.

Machine Config Operator (MCO)
An Operator that applies the new configuration to your cluster machines.

machine config pools (MCP)
A group of machines, such as control plane components or user workloads, that are based on the resources that they handle.

metadata
Additional information about cluster deployment artifacts.

microservices
An approach to writing software. Applications can be separated into the smallest components, independent from each other by using microservices.

mirror registry
A registry that holds the mirror of OpenShift Container Platform images.

monolithic applications
Applications that are self-contained, built, and packaged as a single piece.

namespaces
A namespace isolates specific system resources that are visible to all processes. Inside a namespace, only processes that are members of that namespace can see those resources.

networking
Network information of OpenShift Container Platform cluster.

node
A worker machine in the OpenShift Container Platform cluster. A node is either a virtual machine (VM) or a physical machine.

OpenShift CLI (`oc`)
A command-line tool to run OpenShift Container Platform commands on the terminal.

OpenShift Dedicated
A managed RHEL OpenShift Container Platform offering on Amazon Web Services (AWS) and Google Cloud. OpenShift Dedicated focuses on building and scaling applications.

OpenShift Update Service (OSUS)
For clusters with internet access, Red Hat Enterprise Linux (RHEL) provides over-the-air updates by using an OpenShift update service as a hosted service located behind public APIs.

OpenShift image registry
A registry provided by OpenShift Container Platform to manage images.

Operator
The preferred method of packaging, deploying, and managing a Kubernetes application in an OpenShift Container Platform cluster. An Operator takes human operational knowledge and encodes it into software that is packaged and shared with customers.

OperatorHub
A platform that contains various OpenShift Container Platform Operators to install.

Operator Lifecycle Manager (OLM)
OLM helps you to install, update, and manage the lifecycle of Kubernetes native applications. OLM is an open source toolkit designed to manage Operators in an effective, automated, and scalable way.

OSTree
An upgrade system for Linux-based operating systems that performs atomic upgrades of complete file system trees. OSTree tracks meaningful changes to the file system tree using an addressable object store, and is designed to complement existing package management systems.

over-the-air (OTA) updates
The OpenShift Container Platform Update Service (OSUS) provides over-the-air updates to OpenShift Container Platform, including Red Hat Enterprise Linux CoreOS (RHCOS).

pod
One or more containers with shared resources, such as volume and IP addresses, running in your OpenShift Container Platform cluster. A pod is the smallest compute unit defined, deployed, and managed.

private registry
OpenShift Container Platform can use any server implementing the container image registry API as a source of the image which allows the developers to push and pull their private container images.

public registry
OpenShift Container Platform can use any server implementing the container image registry API as a source of the image which allows the developers to push and pull their public container images.

RHEL OpenShift Container Platform Cluster Manager
A managed service where you can install, modify, operate, and upgrade your OpenShift Container Platform clusters.

RHEL Quay Container Registry
A Quay.io container registry that serves most of the container images and Operators to OpenShift Container Platform clusters.

replication controllers
An asset that indicates how many pod replicas are required to run at a time.

role-based access control (RBAC)
A key security control to ensure that cluster users and workloads have only access to resources required to execute their roles.

route
Routes expose a service to allow for network access to pods from users and applications outside the OpenShift Container Platform instance.

scaling
The increasing or decreasing of resource capacity.

service
A service exposes a running application on a set of pods.

Source-to-Image (S2I) image
An image created based on the programming language of the application source code in OpenShift Container Platform to deploy applications.

storage
OpenShift Container Platform supports many types of storage, both for on-premise and cloud providers. You can manage container storage for persistent and non-persistent data in an OpenShift Container Platform cluster.

Telemetry
A component to collect information such as size, health, and status of OpenShift Container Platform.

template
A template describes a set of objects that can be parameterized and processed to produce a list of objects for creation by OpenShift Container Platform.

user-provisioned infrastructure
You can install OpenShift Container Platform on the infrastructure that you provide. You can use the installation program to generate the assets required to provision the cluster infrastructure, create the cluster infrastructure, and then deploy the cluster to the infrastructure that you provided.

web console
A user interface (UI) to manage OpenShift Container Platform.

worker node
Nodes that are responsible for executing workloads for cluster users. Worker nodes are also known as compute nodes.

<div>

<div class="title">

Additional resources

</div>

- For more information on networking, see [OpenShift Container Platform networking](../networking/networking_overview/understanding-networking.md#understanding-networking).

- For more information on storage, see [OpenShift Container Platform storage](../storage/index.md#index).

- For more information on authentication, see [OpenShift Container Platform authentication](../authentication/index.md#index).

- For more information on Operator Lifecycle Manager (OLM), see [OLM](../operators/understanding/olm/olm-understanding-olm.md#olm-understanding-olm).

- For more information on over-the-air (OTA) updates, see [Introduction to OpenShift updates](../updating/understanding_updates/intro-to-updates.md#understanding-openshift-updates).

</div>

# About installation and updates

As a cluster administrator, you can use the OpenShift Container Platform [installation program](architecture-installation.md#architecture-installation) to install and deploy a cluster by using one of the following methods:

- Installer-provisioned infrastructure

- User-provisioned infrastructure

# About the control plane

The [control plane](control-plane.md#control-plane) manages the worker nodes and the pods in your cluster. You can configure nodes with the use of machine config pools (MCPs). MCPs are groups of machines, such as control plane components or user workloads, that are based on the resources that they handle. OpenShift Container Platform assigns different roles to hosts. These roles define the function of a machine in a cluster. The cluster contains definitions for the standard control plane and worker role types.

You can use Operators to package, deploy, and manage services on the control plane. Operators are important components in OpenShift Container Platform because they provide the following services:

- Perform health checks

- Provide ways to watch applications

- Manage over-the-air updates

- Ensure applications stay in the specified state

<div>

<div class="title">

Additional resources

</div>

- [Hosted control planes overview](../hosted_control_planes/index.md#hcp-overview)

</div>

# About containerized applications for developers

As a developer, you can use different tools, methods, and formats to [develop your containerized application](understanding-development.md#understanding-development) based on your unique requirements, for example:

- Use various build-tool, base-image, and registry options to build a simple container application.

- Use supporting components such as the software catalog and templates to develop your application.

- Package and deploy your application as an Operator.

You can also create a Kubernetes manifest and store it in a Git repository. Kubernetes works on basic units called pods. A pod is a single instance of a running process in your cluster. Pods can contain one or more containers. You can create a service by grouping a set of pods and their access policies. Services provide permanent internal IP addresses and host names for other applications to use as pods are created and destroyed. Kubernetes defines workloads based on the type of your application.

# About Red Hat Enterprise Linux CoreOS (RHCOS) and Ignition

As a cluster administrator, you can perform the following Red Hat Enterprise Linux CoreOS (RHCOS) tasks:

- Learn about the next generation of [single-purpose container operating system technology](architecture-rhcos.md#architecture-rhcos).

- Choose how to configure Red Hat Enterprise Linux CoreOS (RHCOS)

- Choose how to deploy Red Hat Enterprise Linux CoreOS (RHCOS):

  - Installer-provisioned deployment

  - User-provisioned deployment

The OpenShift Container Platform installation program creates the Ignition configuration files that you need to deploy your cluster. Red Hat Enterprise Linux CoreOS (RHCOS) uses Ignition during the initial configuration to perform common disk tasks, such as partitioning, formatting, writing files, and configuring users. During the first boot, Ignition reads its configuration from the installation media or the location that you specify and applies the configuration to the machines.

You can learn how [Ignition works](architecture-rhcos.md#architecture-rhcos), the process for a Red Hat Enterprise Linux CoreOS (RHCOS) machine in an OpenShift Container Platform cluster, view Ignition configuration files, and change Ignition configuration after an installation.

# About admission plugins

You can use [admission plugins](admission-plug-ins.md#admission-plug-ins) to regulate how OpenShift Container Platform functions. After a resource request is authenticated and authorized, admission plugins intercept the resource request to the master API to validate resource requests and to ensure that scaling policies are adhered to. Admission plugins are used to enforce security policies, resource limitations, configuration requirements, and other settings.

# About Linux cgroup version 2

OpenShift Container Platform uses [Linux control group version 2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html) (cgroup v2) in your cluster.

cgroup v2 offers several improvements over cgroup v1, including a unified hierarchy, safer sub-tree delegation, features such as [Pressure Stall Information](https://www.kernel.org/doc/html/latest/accounting/psi.html), and enhanced resource management and isolation. However, cgroup v2 has different CPU, memory, and I/O management characteristics than cgroup v1. Therefore, some workloads might experience slight differences in memory or CPU usage on clusters that run cgroup v2.

<div class="note">

<div class="title">

</div>

- If you run third-party monitoring and security agents that depend on the cgroup file system, update the agents to a version that supports cgroup v2.

- If you have configured cgroup v2 and run cAdvisor as a stand-alone daemon set for monitoring pods and containers, update cAdvisor to v0.43.0 or later.

- If you deploy Java applications, use versions that fully support cgroup v2, such as the following packages:

  - OpenJDK / HotSpot: jdk8u372, 11.0.16, 15 and later

  - NodeJs 20.3.0 and later

  - IBM Semeru Runtimes: jdk8u345-b01, 11.0.16.0, 17.0.4.0, 18.0.2.0 and later

  - IBM SDK Java Technology Edition Version (IBM Java): 8.0.7.15 and later

</div>
