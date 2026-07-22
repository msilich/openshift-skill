<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Refer to tested object maximums when planning your environment for your specific use case, and consider all factors that can impact cluster scaling. For information options that impact performance, see the "OpenShift Virtualization - Tuning & Scaling Guide" in the Red Hat Knowledgebase.

# Tested maximums for OpenShift Virtualization

Maximums are based on a single cluster of the largest possible size for a OpenShift Virtualization 4.x environment. Approaching the maximum values can reduce performance and increase latency. Consider using multiple smaller clusters if possible to improve performance.

## Virtual machine maximums

Maximums apply to virtual machines (VMs) running on OpenShift Virtualization and are subject to the limits specified in "Virtualization limits for Red Hat Enterprise Linux with KVM".

| Objective (per VM)  | Tested limit | Theoretical limit |
|---------------------|--------------|-------------------|
| Virtual CPUs        | 216 vCPUs    | 255 vCPUs         |
| Memory              | 6 TB         | 16 TB             |
| Single disk size    | 100 TB       | 100 TB            |
| Hot-pluggable disks | 255 disks    | N/A               |

> [!NOTE]
> Each VM must have at least 512 MB of memory. The `fstype` in the guest operating system (OS) must support the maximum limits. Do not use preallocation in data volumes that are larger than 99 TB.

## Host maximums

The following maximums apply to the OpenShift Container Platform hosts used for OpenShift Virtualization.

| Objective (per host) | Tested limit | Theoretical limit |
|----|----|----|
| Logical CPU cores or threads | Same as Red Hat Enterprise Linux (RHEL) | N/A |
| RAM | Same as RHEL | N/A |
| Simultaneous live migrations | Defaults to 2 outbound migrations per node, and 5 concurrent migrations per cluster | Depends on NIC bandwidth |
| Live migration bandwidth | No default limit | Depends on NIC bandwidth |

## Cluster maximums

The following maximums apply to objects defined in OpenShift Virtualization.

| Objective (per cluster) | Tested limit | Theoretical limit |
|----|----|----|
| Number of attached PVs per node | N/A | CSI storage provider dependent |
| Maximum PV size | N/A | CSI storage provider dependent |
| Hosts | 500 hosts (100 or fewer recommended) <sup>\[1\]</sup> | Same as OpenShift Container Platform |
| Defined VMs | 10,000 VMs <sup>\[2\]</sup> | Same as OpenShift Container Platform |

1.  If you use more than 100 nodes, consider using Red Hat Advanced Cluster Management (RHACM) to manage multiple clusters instead of scaling out a single control plane. Larger clusters add complexity, require longer updates, and depending on node size and total object density, they can increase control plane stress.

    Using multiple clusters can be beneficial in areas like per-cluster isolation and high availability.

2.  The maximum number of VMs per node depends on the host hardware and resource capacity. It is also limited by the following parameters:

    - Settings that limit the number of pods that can be scheduled to a node. For example: `maxPods`.

    - The default number of KVM devices. For example: `devices.kubevirt.io/kvm: 1k`.

# Additional resources

- [OpenShift Virtualization - Tuning & Scaling Guide](https://access.redhat.com/articles/6994974)

- [Virtualization limits for Red Hat Enterprise Linux with KVM](https://access.redhat.com/articles/rhel-kvm-limits)

- [Planning your environment according to object maximums](../../scalability_and_performance/planning-your-environment-according-to-object-maximums.md#planning-your-environment-according-to-object-maximums)

- [Managing the maximum number of pods per node](../../nodes/nodes/nodes-nodes-managing-max-pods.md#nodes-nodes-managing-max-pods)

- [Red Hat Advanced Cluster Management documentation](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes)
