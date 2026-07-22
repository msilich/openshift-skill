<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use machine management to flexibly work with underlying infrastructure such as Amazon Web Services (AWS), Microsoft Azure, Google Cloud, Red Hat OpenStack Platform (RHOSP), and VMware vSphere to manage the OpenShift Container Platform cluster. You can control the cluster and perform auto-scaling, such as scaling up and down the cluster based on specific workload policies.

It is important to have a cluster that adapts to changing workloads. The OpenShift Container Platform cluster can horizontally scale up and down when the load increases or decreases.

Machine management is implemented as a custom resource definition (CRD). A CRD object defines a new unique object `Kind` in the cluster and enables the Kubernetes API server to handle the object’s entire lifecycle.

The Machine API Operator provisions the following resources:

- `MachineSet`

- `Machine`

- `ClusterAutoscaler`

- `MachineAutoscaler`

- `MachineHealthCheck`

# Machine API overview

The Machine API performs all node host provisioning management actions after the cluster installation finishes. Because of this system, OpenShift Container Platform offers an elastic, dynamic provisioning method on top of public or private cloud infrastructure.

The Machine API is a combination of primary resources that are based on the upstream Cluster API project and custom OpenShift Container Platform resources.

The two primary resources are:

Machines
A fundamental unit that describes the host for a node. A machine has a `providerSpec` specification, which describes the types of compute nodes that are offered for different cloud platforms. For example, a machine type for a compute node might define a specific machine type and required metadata.

Machine sets
`MachineSet` resources are groups of compute machines. Compute machine sets are to compute machines as replica sets are to pods. If you need more compute machines or must scale them down, you change the `replicas` field on the `MachineSet` resource to meet your compute need.

> [!WARNING]
> Control plane machines cannot be managed by compute machine sets.
>
> Control plane machine sets provide management capabilities for supported control plane machines that are similar to what compute machine sets provide for compute machines.
>
> For more information, see “Managing control plane machines".

The following custom resources add more capabilities to your cluster:

Machine autoscaler
The `MachineAutoscaler` resource automatically scales compute machines in a cloud. You can set the minimum and maximum scaling boundaries for nodes in a specified compute machine set, and the machine autoscaler maintains that range of nodes.

The `MachineAutoscaler` object takes effect after a `ClusterAutoscaler` object exists. Both `ClusterAutoscaler` and `MachineAutoscaler` resources are made available by the `ClusterAutoscalerOperator` object.

Cluster autoscaler
This resource is based on the upstream cluster autoscaler project. In the OpenShift Container Platform implementation, it is integrated with the Machine API by extending the compute machine set API. You can use the cluster autoscaler to manage your cluster in the following ways:

- Set cluster-wide scaling limits for resources such as cores, nodes, memory, and GPU

- Set the priority so that the cluster prioritizes pods and new nodes are not brought online for less important pods

- Set the scaling policy so that you can scale up nodes but not scale them down

Machine health check
The `MachineHealthCheck` resource detects when a machine is unhealthy, deletes it, and, on supported platforms, makes a new machine.

In OpenShift Container Platform version 3.11, you could not roll out a multi-zone architecture easily because the cluster did not manage machine provisioning. Beginning with OpenShift Container Platform version 4.1, this process is easier. Each compute machine set is scoped to a single zone, so the installation program sends out compute machine sets across availability zones on your behalf. And then because your compute is dynamic, and in the face of a zone failure, you always have a zone for when you must rebalance your machines. In global Azure regions that do not have multiple availability zones, you can use availability sets to ensure high availability. The autoscaler provides best-effort balancing over the life of a cluster.

<div>

<div class="title">

Additional resources

</div>

- [Machine phases and lifecycle](machine-phases-lifecycle.md#machine-phases-lifecycle)

</div>

# Compute machine management

As a cluster administrator, you can manage the compute machines in your OpenShift Container Platform cluster.

For example, you can perform the following actions:

- Create a compute machine set for the following cloud providers:

  - [AWS](creating_machinesets/creating-machineset-aws.md#creating-machineset-aws)

  - [Azure](creating_machinesets/creating-machineset-azure.md#creating-machineset-azure)

  - [Azure Stack Hub](creating_machinesets/creating-machineset-azure-stack-hub.md#creating-machineset-azure-stack-hub)

  - [Google Cloud](creating_machinesets/creating-machineset-gcp.md#creating-machineset-gcp)

  - [IBM Cloud](creating_machinesets/creating-machineset-ibm-cloud.md#creating-machineset-ibm-cloud)

  - [IBM Power Virtual Server](creating_machinesets/creating-machineset-ibm-power-vs.md#creating-machineset-ibm-power-vs)

  - [Nutanix](creating_machinesets/creating-machineset-nutanix.md#creating-machineset-nutanix)

  - [RHOSP](creating_machinesets/creating-machineset-osp.md#creating-machineset-osp)

  - [vSphere](creating_machinesets/creating-machineset-vsphere.md#creating-machineset-vsphere)

- Create a machine set for a bare metal deployment: [Creating a compute machine set on bare metal](creating_machinesets/creating-machineset-bare-metal.md#creating-machineset-bare-metal)

- [Manually scale a compute machine set](manually-scaling-machineset.md#manually-scaling-machineset) by adding or removing a machine from the compute machine set.

- [Modify a compute machine set](modifying-machineset.md#modifying-machineset) through the `MachineSet` YAML configuration file.

- [Delete](deleting-machine.md#deleting-machine) a machine.

- [Create infrastructure compute machine sets](creating-infrastructure-machinesets.md#creating-infrastructure-machinesets).

- Configure and deploy a [machine health check](deploying-machine-health-checks.md#deploying-machine-health-checks) to automatically fix damaged machines in a machine pool.

# Control plane machine management

As a cluster administrator, you can manage the control plane machines in your OpenShift Container Platform cluster.

For example, you can perform the following actions:

- [Update your control plane configuration](control_plane_machine_management/cpmso-managing-machines.md#cpmso-feat-config-update_cpmso-managing-machines) with a control plane machine set for the following cloud providers:

  - [Amazon Web Services](control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-aws.md#cpmso-config-options-aws)

  - [Google Cloud](control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-gcp.md#cpmso-config-options-gcp)

  - [Microsoft Azure](control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-azure.md#cpmso-config-options-azure)

  - [Nutanix](control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-nutanix.md#cpmso-config-options-nutanix)

  - [Red Hat OpenStack Platform (RHOSP)](control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-openstack.md#cpmso-config-options-openstack)

  - [VMware vSphere](control_plane_machine_management/cpmso_provider_configurations/cpmso-config-options-vsphere.md#cpmso-config-options-vsphere)

- Configure and deploy a [machine health check](deploying-machine-health-checks.md#deploying-machine-health-checks) to automatically recover unhealthy control plane machines.

# Cluster autoscaling

You can automatically scale your OpenShift Container Platform cluster to ensure flexibility for changing workloads.

To [autoscale](applying-autoscaling.md#applying-autoscaling) your cluster, you must first deploy a cluster autoscaler, and then deploy a machine autoscaler for each compute machine set.

- The [*cluster autoscaler*](applying-autoscaling.md#cluster-autoscaler-about_applying-autoscaling) increases and decreases the size of the cluster based on deployment needs.

- The [*machine autoscaler*](applying-autoscaling.md#machine-autoscaler-about_applying-autoscaling) adjusts the number of machines in the compute machine sets that you deploy in your OpenShift Container Platform cluster.

# Compute machine creation on user-provisioned infrastructure

User-provisioned infrastructure is an environment where you can deploy infrastructure such as compute, network, and storage resources that host the OpenShift Container Platform. You can add compute machines to a cluster on user-provisioned infrastructure during or after the installation process.

<div>

<div class="title">

Additional resources

</div>

- [Adding compute machines to clusters with user-provisioned infrastructure manually](user_infra/adding-compute-user-infra-general.md#adding-compute-user-infra-general)

</div>
