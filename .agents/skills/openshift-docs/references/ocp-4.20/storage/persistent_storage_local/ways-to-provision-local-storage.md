<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use any of the following solutions to provision local storage:

- HostPath Provisioner (HPP)

- Local Storage Operator (LSO)

- Logical Volume Manager (LVM) Storage

> [!WARNING]
> These solutions support provisioning only node-local storage. The workloads are bound to the nodes that provide the storage. If the node becomes unavailable, the workload also becomes unavailable. To maintain workload availability despite node failures, you must ensure storage data replication through active or passive replication mechanisms.

# Overview of HostPath Provisioner functionality

You can perform the following actions using HostPath Provisioner (HPP):

- Map the host filesystem paths to storage classes for provisioning local storage.

- Statically create storage classes to configure filesystem paths on a node for storage consumption.

- Statically provision Persistent Volumes (PVs) based on the storage class.

- Create workloads and PersistentVolumeClaims (PVCs) while being aware of the underlying storage topology.

> [!NOTE]
> HPP is available in upstream Kubernetes. However, it is not recommended to use HPP from upstream Kubernetes.

# Overview of Local Storage Operator functionality

You can perform the following actions using Local Storage Operator (LSO):

- Assign the storage devices (disks or partitions) to the storage classes without modifying the device configuration.

- Statically provision PVs and storage classes by configuring the `LocalVolume` custom resource (CR).

- Create workloads and PVCs while being aware of the underlying storage topology.

> [!NOTE]
> LSO is developed and delivered by Red Hat.

# Overview of LVM Storage functionality

You can perform the following actions using Logical Volume Manager (LVM) Storage:

- Configure storage devices (disks or partitions) as lvm2 volume groups and expose the volume groups as storage classes.

- Create workloads and request storage by using PVCs without considering the node topology.

LVM Storage uses the TopoLVM CSI driver to dynamically allocate storage space to the nodes in the topology and provision PVs.

> [!NOTE]
> LVM Storage is developed and maintained by Red Hat. The CSI driver provided with LVM Storage is the upstream project "topolvm".

# Comparison of LVM Storage, LSO, and HPP

The following sections compare the functionalities provided by LVM Storage, Local Storage Operator (LSO), and HostPath Provisioner (HPP) to provision local storage.

## Comparison of the support for storage types and filesystems

The following table compares the support for storage types and filesystems provided by LVM Storage, Local Storage Operator (LSO), and HostPath Provisioner (HPP) to provision local storage:

| Functionality | LVM Storage | LSO | HPP |
|----|----|----|----|
| Support for block storage | Yes | Yes | No |
| Support for file storage | Yes | Yes | Yes |
| Support for object storage <sup>\[1\]</sup> | No | No | No |
| Available filesystems | `ext4`, `xfs` | `ext4`, `xfs` | Any mounted system available on the node is supported. |

Comparison of the support for storage types and filesystems

1.  None of the solutions (LVM Storage, LSO, and HPP) provide support for object storage. Therefore, if you want to use object storage, you need an S3 object storage solution, such as `MultiClusterGateway` from the Red Hat OpenShift Data Foundation. All of the solutions can serve as underlying storage providers for the S3 object storage solutions.

## Comparison of the support for core functionalities

The following table compares how LVM Storage, Local Storage Operator (LSO), and HostPath Provisioner (HPP) support core functionalities for provisioning local storage:

<table style="width:100%;">
<caption>Comparison of the support for core functionalities</caption>
<colgroup>
<col style="width: 28%" />
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Functionality</th>
<th style="text-align: left;">LVM Storage</th>
<th style="text-align: left;">LSO</th>
<th style="text-align: left;">HPP</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Support for automatic file system formatting</p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for dynamic provisioning</p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for using software Redundant Array of Independent Disks (RAID) arrays</p></td>
<td style="text-align: left;"><p>Yes</p>
<p>Supported on 4.15 and later.</p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for transparent disk encryption</p></td>
<td style="text-align: left;"><p>Yes</p>
<p>Supported on 4.16 and later.</p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for volume based disk encryption</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for disconnected installation</p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for PVC expansion</p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for volume snapshots and volume clones</p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for thin provisioning</p></td>
<td style="text-align: left;"><p>Yes</p>
<p>Devices are thin-provisioned by default.</p></td>
<td style="text-align: left;"><p>Yes</p>
<p>You can configure the devices to point to the thin-provisioned volumes</p></td>
<td style="text-align: left;"><p>Yes</p>
<p>You can configure a path to point to the thin-provisioned volumes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for automatic disk discovery and setup</p></td>
<td style="text-align: left;"><p>Yes</p>
<p>Automatic disk discovery is available during installation and runtime. You can also dynamically add the disks to the <code>LVMCluster</code> custom resource (CR) to increase the storage capacity of the existing storage classes.</p></td>
<td style="text-align: left;"><p>Technology Preview</p>
<p>Automatic disk discovery is available during installation.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
</tbody>
</table>

## Comparison of performance and isolation capabilities

The following table compares the performance and isolation capabilities of LVM Storage, Local Storage Operator (LSO), and HostPath Provisioner (HPP) in provisioning local storage.

<table>
<caption>Comparison of performance and isolation capabilities</caption>
<colgroup>
<col style="width: 21%" />
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Functionality</th>
<th style="text-align: left;">LVM Storage</th>
<th style="text-align: left;">LSO</th>
<th style="text-align: left;">HPP</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Performance</p></td>
<td style="text-align: left;"><p>I/O speed is shared for all workloads that use the same storage class.</p>
<p>Block storage allows direct I/O operations.</p>
<p>Thin provisioning can affect the performance.</p></td>
<td style="text-align: left;"><p>I/O depends on the LSO configuration.</p>
<p>Block storage allows direct I/O operations.</p></td>
<td style="text-align: left;"><p>I/O speed is shared for all workloads that use the same storage class.</p>
<p>The restrictions imposed by the underlying filesystem can affect the I/O speed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Isolation boundary <sup>[1]</sup></p></td>
<td style="text-align: left;"><p>LVM Logical Volume (LV)</p>
<p>It provides higher level of isolation compared to HPP.</p></td>
<td style="text-align: left;"><p>LVM Logical Volume (LV)</p>
<p>It provides higher level of isolation compared to HPP</p></td>
<td style="text-align: left;"><p>Filesystem path</p>
<p>It provides lower level of isolation compared to LSO and LVM Storage.</p></td>
</tr>
</tbody>
</table>

1.  Isolation boundary refers to the level of separation between different workloads or applications that use local storage resources.

## Comparison of the support for additional functionalities

The following table compares the additional features provided by LVM Storage, Local Storage Operator (LSO), and HostPath Provisioner (HPP) to provision local storage:

<table style="width:100%;">
<caption>Comparison of the support for additional functionalities</caption>
<colgroup>
<col style="width: 28%" />
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Functionality</th>
<th style="text-align: left;">LVM Storage</th>
<th style="text-align: left;">LSO</th>
<th style="text-align: left;">HPP</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Support for generic ephemeral volumes</p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for CSI inline ephemeral volumes</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for storage topology</p></td>
<td style="text-align: left;"><p>Yes</p>
<p>Supports CSI node topology</p></td>
<td style="text-align: left;"><p>Yes</p>
<p>LSO provides partial support for storage topology through node tolerations.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Support for <code>ReadWriteMany</code> (RWX) access mode <sup>[1]</sup></p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
</tbody>
</table>

1.  All of the solutions (LVM Storage, LSO, and HPP) have the `ReadWriteOnce` (RWO) access mode. RWO access mode allows access from multiple pods on the same node.
