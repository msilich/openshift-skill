<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Optimizing storage helps to minimize storage use across all resources. As an administrator, you can optimize storage to ensure that existing storage resources are working in an efficient manner.

# Available persistent storage options

To optimize your OpenShift Container Platform environment, review the available persistent storage options. By understanding these choices, you can select the appropriate storage configuration to meet your specific workload requirements.

<table>
<caption>Available storage options</caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 50%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Storage type</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Examples</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Block</p></td>
<td style="text-align: left;"><ul>
<li><p>Presented to the operating system (OS) as a block device</p></li>
<li><p>Suitable for applications that need full control of storage and operate at a low level on files bypassing the file system.</p></li>
<li><p>Also referred to as a Storage Area Network (SAN).</p></li>
<li><p>Non-shareable, which means that only one client at a time can mount an endpoint of this type.</p></li>
</ul></td>
<td style="text-align: left;"><p>AWS EBS and VMware vSphere support dynamic persistent volume (PV) provisioning natively in OpenShift Container Platform.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>File</p></td>
<td style="text-align: left;"><ul>
<li><p>Presented to the OS as a file system export to be mounted</p></li>
<li><p>Also referred to as Network Attached Storage (NAS).</p></li>
<li><p>Concurrency, latency, file locking mechanisms, and other capabilities vary widely between protocols, implementations, vendors, and scales.</p></li>
</ul></td>
<td style="text-align: left;"><p>RHEL NFS, NetApp NFS, and Vendor NFS.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Object</p></td>
<td style="text-align: left;"><ul>
<li><p>Accessible through a REST API endpoint.</p></li>
<li><p>Configurable for use in the OpenShift image registry</p></li>
<li><p>Applications must build their drivers into the application and/or container.</p></li>
</ul></td>
<td style="text-align: left;"><p>AWS S3.</p></td>
</tr>
</tbody>
</table>

- `File`: NetApp NFS supports dynamic PV provisioning when using the Trident plugin.

# Recommended configurable storage technology

Review the recommended and configurable storage technologies for the given OpenShift Container Platform cluster application.

| Storage type          | Block            | File             | Object           |
|-----------------------|------------------|------------------|------------------|
| ROX                   | Yes              | Yes              | Yes              |
| RWX                   | No               | Yes              | Yes              |
| Registry              | Configurable     | Configurable     | Recommended      |
| Scaled registry       | Not configurable | Configurable     | Recommended      |
| Metrics               | Recommended      | Configurable     | Not configurable |
| Elasticsearch Logging | Recommended      | Configurable     | Not supported    |
| Loki Logging          | Not configurable | Not configurable | Recommended      |
| Apps                  | Recommended      | Recommended      | Not configurable |

Recommended and configurable storage technology

where:

`ROX`
Specifies `ReadOnlyMany` access mode.

`ROX.Yes`
Specifies that this access mode

`RWX`
Specifies `ReadWriteMany` access mode.

`Metrics`
Specifies Prometheus as the underlying technology used for metrics.

`Metrics.Configurable`
For metrics, using file storage with the `ReadWriteMany` (RWX) access mode is unreliable. If you use file storage, do not configure the RWX access mode on any persistent volume claims (PVCs) that are configured for use with metrics.

`Elasticsearch Logging.Configurable`
For logging, review the recommended storage solution in Configuring persistent storage for the log store section. Using NFS storage as a persistent volume or through NAS, such as Gluster, can corrupt the data. Therefore, NFS is not supported for Elasticsearch storage and LokiStack log store in OpenShift Container Platform Logging. You must use one persistent volume type per log store.

`Apps.Not configurable`
Specifies that object storage is not consumed through PVs or PVCs of OpenShift Container Platform. Apps must integrate with the object storage REST API.

> [!NOTE]
> A scaled registry is an OpenShift image registry where two or more pod replicas are running.

## Specific application storage recommendations

Review the specific storage recommendations for registries, scaled registries, metrics, logs, and applications to better understand the storage requirements for each of these entities.

> [!IMPORTANT]
> Testing shows issues with using the NFS server on Red Hat Enterprise Linux (RHEL) as a storage backend for core services. This includes the OpenShift Container Registry and Quay, Prometheus for monitoring storage, and Elasticsearch for logging storage. Therefore, using RHEL NFS to back PVs used by core services is not recommended.
>
> Other NFS implementations in the marketplace might not have these issues. Contact the individual NFS implementation vendor for more information on any testing that was possibly completed against these OpenShift Container Platform core components.

Registry
In a non-scaled/high-availability (HA) OpenShift image registry cluster deployment:

- The storage technology does not have to support RWX access mode.

- The storage technology must ensure read-after-write consistency.

- The preferred storage technology is object storage followed by block storage.

- File storage is not recommended for OpenShift image registry cluster deployment with production workloads.

Scaled registry
In a scaled/HA OpenShift image registry cluster deployment:

- The storage technology must support RWX access mode.

- The storage technology must ensure read-after-write consistency.

- The preferred storage technology is object storage.

- Red Hat OpenShift Data Foundation, Amazon Simple Storage Service (Amazon S3), Google Cloud Storage (GCS), Microsoft Azure Blob Storage, and OpenStack Swift are supported.

- Object storage should be S3 or Swift compliant.

- For non-cloud platforms, such as vSphere and bare-metal installations, the only configurable technology is file storage.

- Block storage is not configurable.

- The use of Network File System (NFS) storage with OpenShift Container Platform is supported. However, the use of NFS storage with a scaled registry can cause known issues. For more information, see the "Is NFS supported for OpenShift cluster internal components in Production?" Red Hat Knowledgebase solution.

Metrics
In an OpenShift Container Platform hosted metrics cluster deployment:

- The preferred storage technology is block storage.

- Object storage is not configurable.

> [!IMPORTANT]
> It is not recommended to use file storage for a hosted metrics cluster deployment with production workloads.

Logging
In an OpenShift Container Platform hosted logging cluster deployment:

- Loki Operator:

  - The preferred storage technology is S3 compatible Object storage.

  - Block storage is not configurable.

- OpenShift Elasticsearch Operator:

  - The preferred storage technology is block storage.

  - Object storage is not supported.

> [!NOTE]
> As of logging version 5.4.3 the OpenShift Elasticsearch Operator is deprecated and is planned to be removed in a future release. Red Hat will provide bug fixes and support for this feature during the current release lifecycle, but this feature will no longer receive enhancements and will be removed. As an alternative to using the OpenShift Elasticsearch Operator to manage the default log storage, you can use the Loki Operator.

Applications
Application use cases vary from application to application, as described in the following examples:

- Storage technologies that support dynamic PV provisioning have low mount time latencies, and are not tied to nodes to support a healthy cluster.

- Application developers are responsible for knowing and understanding the storage requirements for their application, and how it works with the provided storage to ensure that issues do not occur when an application scales or interacts with the storage layer.

Other specific application storage recommendations

> [!IMPORTANT]
> Red Hat does not recommend using RAID configurations on `Write` intensive workloads, such as `etcd`. If you are running `etcd` with a RAID configuration, you might be at risk of encountering performance issues with your workloads.

- Red Hat OpenStack Platform (RHOSP) Cinder: RHOSP Cinder tends to be adept at ROX access mode use cases.

- Databases: Databases (RDBMSs, NoSQL DBs, etc.) tend to perform best with dedicated block storage.

- The etcd database must have enough storage and adequate performance capacity to enable a large cluster. Information about monitoring and benchmarking tools to establish ample storage and a high-performance environment is described in *Recommended etcd practices*.

# Additional resources

- [Is NFS supported for OpenShift cluster internal components in Production?](https://access.redhat.com/solutions/3428661)

# Data storage management

To effectively manage data storage in OpenShift Container Platform, review the main directories where components write data.

The following table summarizes the main directories that OpenShift Container Platform components write data to.

<table>
<caption>Main directories for storing OpenShift Container Platform data</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Directory</th>
<th style="text-align: left;">Notes</th>
<th style="text-align: left;">Sizing</th>
<th style="text-align: left;">Expected growth</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><strong><em>/var/lib/etcd</em></strong></p></td>
<td style="text-align: left;"><p>Used for etcd storage when storing the database.</p></td>
<td style="text-align: left;"><p>Less than 20 GB.</p>
<p>Database can grow up to 8 GB.</p></td>
<td style="text-align: left;"><p>Will grow slowly with the environment. Only storing metadata.</p>
<p>Additional 20-25 GB for every additional 8 GB of memory.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong><em>/var/lib/containers</em></strong></p></td>
<td style="text-align: left;"><p>This is the mount point for the CRI-O runtime. Storage used for active container runtimes, including pods, and storage of local images. Not used for registry storage.</p></td>
<td style="text-align: left;"><p>50 GB for a node with 16 GB memory. Note that this sizing should not be used to determine minimum cluster requirements.</p>
<p>Additional 20-25 GB for every additional 8 GB of memory.</p></td>
<td style="text-align: left;"><p>Growth is limited by capacity for running containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong><em>/var/lib/kubelet</em></strong></p></td>
<td style="text-align: left;"><p>Ephemeral volume storage for pods. This includes anything external that is mounted into a container at runtime. Includes environment variables, kube secrets, and data volumes not backed by persistent volumes.</p></td>
<td style="text-align: left;"><p>Varies</p></td>
<td style="text-align: left;"><p>Minimal if pods requiring storage are using persistent volumes. If using ephemeral storage, this can grow quickly.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong><em>/var/log</em></strong></p></td>
<td style="text-align: left;"><p>Log files for all components.</p></td>
<td style="text-align: left;"><p>10 to 30 GB.</p></td>
<td style="text-align: left;"><p>Log files can grow quickly; size can be managed by growing disks or by using log rotate.</p></td>
</tr>
</tbody>
</table>

# Optimizing storage performance for Microsoft Azure

To ensure optimal cluster performance on Microsoft Azure, configure faster storage for OpenShift Container Platform and Kubernetes. Red Hat recommends faster storage, particularly for etcd on the control plane nodes.

For production Azure clusters and clusters with intensive workloads, the virtual machine operating system disk for control plane machines should be able to sustain a tested and recommended minimum throughput of 5000 IOPS / 200 MBps. This throughput can be provided by having a minimum of 1 TiB Premium SSD (P30). In Azure and Azure Stack Hub, disk performance is directly dependent on SSD disk sizes. To achieve the throughput supported by a `Standard_D8s_v3` virtual machine, or other similar machine types, and the target of 5000 IOPS, at least a P30 disk is required.

Host caching must be set to `ReadOnly` for low latency and high IOPS and throughput when reading data. Reading data from the cache, which is present either in the VM memory or in the local SSD disk, is much faster than reading from the disk, which is in the blob storage.
