<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Many factors, including hosted cluster workload and worker node count, affect how many hosted control planes can fit within a certain number of worker nodes.

Use this sizing guide to help with hosted cluster capacity planning.

This guidance assumes a highly available hosted control planes topology. The load-based sizing examples were measured on a bare-metal cluster. Cloud-based instances might have different limiting factors, such as memory size.

You can override the following resource utilization sizing measurements and disable the metric service monitoring.

See the following highly available hosted control planes requirements, which were tested with OpenShift Container Platform version 4.12.9 and later:

- 78 pods

- Three 8 GiB PVs for etcd

- Minimum vCPU: approximately 5.5 cores

- Minimum memory: approximately 19 GiB

<div>

<div class="title">

Additional resources

</div>

- [Overriding resource utilization measurements](hcp-override-resource-util.md#hcp-override-resource-util)

- [Distributing hosted cluster workloads](hcp-distribute-workloads.md#hcp-distribute-workloads)

</div>

# Pod limits

The `maxPods` setting for each node affects how many hosted clusters can fit in a control-plane node. It is important to note the `maxPods` value on all control-plane nodes. Plan for about 75 pods for each highly available hosted control plane.

For bare-metal nodes, the default `maxPods` setting of 250 is likely to be a limiting factor because roughly three hosted control planes fit for each node given the pod requirements, even if the machine has plenty of resources to spare. Setting the `maxPods` value to 500 by configuring the `KubeletConfig` value allows for greater hosted control plane density, which can help you take advantage of additional compute resources.

<div>

<div class="title">

Additional resources

</div>

- [Configuring the maximum number of pods per node](../../nodes/nodes/nodes-nodes-managing-max-pods.md#nodes-nodes-managing-max-pods-proc_nodes-nodes-managing-max-pods)

</div>

# Request-based resource limit

The maximum number of hosted control planes that the cluster can host is calculated based on the hosted control plane CPU and memory requests from the pods.

A highly available hosted control plane consists of 78 pods that request 5 vCPUs and 18 GiB memory. These baseline numbers are compared to the cluster worker node resource capacities to estimate the maximum number of hosted control planes.

# Load-based limit

As you plan your deployment, consider the maximum number of hosted control planes that the cluster can host. That number is calculated based on the hosted control plane pods CPU and memory utilizations when some workload is put on the hosted control plane Kubernetes API server.

The following method is used to measure the hosted control plane resource utilizations as the workload increases:

- A hosted cluster with 9 workers that use 8 vCPU and 32 GiB each, while using the KubeVirt platform

- The workload test profile that is configured to focus on API control-plane stress, based on the following definition:

  - Created objects for each namespace, scaling up to 100 namespaces total

  - Additional API stress with continuous object deletion and creation

  - Workload queries-per-second (QPS) and Burst settings set high to remove any client-side throttling

As the load increases by 1000 QPS, the hosted control plane resource utilization increases by 9 vCPUs and 2.5 GB memory.

For general sizing purposes, consider the 1000 QPS API rate that is a *medium* hosted cluster load, and a 2000 QPS API that is a *heavy* hosted cluster load.

> [!NOTE]
> This test provides an estimation factor to increase the compute resource utilization based on the expected API load. Exact utilization rates can vary based on the type and pace of the cluster workload.

The following example shows hosted control plane resource scaling for the workload and API rate definitions:

| QPS (API rate)              | vCPU usage | Memory usage (GiB) |
|-----------------------------|------------|--------------------|
| Low load (Less than 50 QPS) | 2.9        | 11.1               |
| Medium load (1000 QPS)      | 11.9       | 13.6               |
| High load (2000 QPS)        | 20.9       | 16.1               |

API rate table

The hosted control plane sizing is about control-plane load and workloads that cause heavy API activity, etcd activity, or both. Hosted pod workloads that focus on data-plane loads, such as running a database, might not result in high API rates.

# Sizing calculation example

Review an example of how to size a deployment of hosted control planes.

This example provides sizing guidance for the following scenario:

- Three bare-metal workers that are labeled as `hypershift.openshift.io/control-plane` nodes

- `maxPods` value set to 500

- The expected API rate is medium or about 1000, according to the load-based limits

| Limit description                                 | Server 1 | Server 2 |
|---------------------------------------------------|----------|----------|
| Number of vCPUs on worker node                    | 64       | 128      |
| Memory on worker node (GiB)                       | 128      | 256      |
| Maximum pods per worker                           | 500      | 500      |
| Number of workers used to host control planes     | 3        | 3        |
| Maximum QPS target rate (API requests per second) | 1000     | 1000     |

Limit inputs

|  |  |  |  |
|----|----|----|----|
| Calculated values based on worker node size and API rate | Server 1 | Server 2 | Calculation notes |
| Maximum hosted control planes per worker based on vCPU requests | 12.8 | 25.6 | Number of worker vCPUs ÷ 5 total vCPU requests per hosted control plane |
| Maximum hosted control planes per worker based on vCPU usage | 5.4 | 10.7 | Number of vCPUS ÷ (2.9 measured idle vCPU usage + (QPS target rate ÷ 1000) × 9.0 measured vCPU usage per 1000 QPS increase) |
| Maximum hosted control planes per worker based on memory requests | 7.1 | 14.2 | Worker memory GiB ÷ 18 GiB total memory request per hosted control plane |
| Maximum hosted control planes per worker based on memory usage | 9.4 | 18.8 | Worker memory GiB ÷ (11.1 measured idle memory usage + (QPS target rate ÷ 1000) × 2.5 measured memory usage per 1000 QPS increase) |
| Maximum hosted control planes per worker based on per node pod limit | 6.7 | 6.7 | 500 `maxPods` ÷ 75 pods per hosted control plane |
| Minimum of previously mentioned maximums | 5.4 | 6.7 |  |
|  | vCPU limiting factor | `maxPods` limiting factor |  |
| Maximum number of hosted control planes within a management cluster | 16 | 20 | Minimum of previously mentioned maximums × 3 control-plane workers |

Sizing calculation example

|  |  |
|----|----|
| Name | Description |
| `mce_hs_addon_request_based_hcp_capacity_gauge` | Estimated maximum number of hosted control planes the cluster can host based on a highly available hosted control planes resource request. |
| `mce_hs_addon_low_qps_based_hcp_capacity_gauge` | Estimated maximum number of hosted control planes the cluster can host if all hosted control planes make around 50 QPS to the clusters Kube API server. |
| `mce_hs_addon_medium_qps_based_hcp_capacity_gauge` | Estimated maximum number of hosted control planes the cluster can host if all hosted control planes make around 1000 QPS to the clusters Kube API server. |
| `mce_hs_addon_high_qps_based_hcp_capacity_gauge` | Estimated maximum number of hosted control planes the cluster can host if all hosted control planes make around 2000 QPS to the clusters Kube API server. |
| `mce_hs_addon_average_qps_based_hcp_capacity_gauge` | Estimated maximum number of hosted control planes the cluster can host based on the existing average QPS of hosted control planes. If you do not have an active hosted control planes, you can expect low QPS. |

Hosted control planes capacity metrics

# Shared infrastructure between hosted and standalone control planes

As a service provider, you can more effectively use your resources by sharing infrastructure between a standalone OpenShift Container Platform control plane and hosted control planes. A 3-node OpenShift Container Platform cluster can be a management cluster for a hosted cluster.

Sharing infrastructure can be beneficial in constrained environments, such as in small-scale deployments where you need resource efficiency.

Before you share infrastructure, ensure that your infrastructure has enough resources to support hosted control planes. On the OpenShift Container Platform management cluster, nothing else can be deployed except hosted control planes. Ensure that the management cluster has enough CPU, memory, storage, and network resources to handle the combined load of the hosted clusters. Workload must not be demanding, and it must fall within a low queries-per-second (QPS) profile. For more information about resources and workload, see "Sizing guidance for hosted control planes".

<div>

<div class="title">

Additional resources

</div>

- [Sizing guidance for hosted control planes](hcp-sizing-guidance.md#hcp-sizing-guidance)

</div>
