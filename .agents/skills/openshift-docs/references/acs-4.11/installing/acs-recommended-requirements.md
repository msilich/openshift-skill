<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To ensure optimal performance for self-managed Red Hat Advanced Cluster Security for Kubernetes (RHACS) components, allocate CPU and memory resources based on the specific scale of your environment. Calculate your infrastructure requirements by analyzing the number of monitored deployments, concurrent users, and unique images across your clusters. Accurate sizing prevents performance bottlenecks and ensures your deployment handles growth effectively.

<a id="resource-requirements-for-scaling-based-on-deployment_acs-recommended-requirements"></a>

# Resource requirements for scaling based on deployment

The recommended resource guidelines were developed by performing a focused test that created the following objects across a given number of namespaces:

- 10 deployments, with 3 pod replicas in a sleep state, mounting 4 secrets, 4 config maps

- 10 services, each one pointing to the TCP/8080 and TCP/8443 ports of one of the previous deployments

- 1 route pointing to the first of the previous services

- 10 secrets containing 2048 random string characters

- 10 config maps containing 2048 random string characters

During the analysis of results, the number of deployments is identified as a primary factor for increasing of used resources. And we are using the number of deployments for the estimation of required resources.

<div>

<div class="title">

Additional resources

</div>

- [Default resource requirements](acs-default-requirements.md#acs-general-requirements_acs-default-requirements)

</div>

<a id="recommended-requirements-central-services_acs-recommended-requirements"></a>

# Central services (self-managed)

> [!NOTE]
> If you are using Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service), you do not need to review the requirements for Central services, because they are managed by Red Hat. You only need to look at the requirements for secured cluster services.

Central services contain the following components:

- Central

- Central DB

- StackRox Scanner

- Scanner V4

<a id="recommended-requirements-central-services-central_acs-recommended-requirements"></a>

## Central

<a id="_memory_and_cpu_requirements"></a>

### Memory and CPU requirements

The following table lists the minimum memory and CPU values required to run Central. To determine sizing, consider the following data:

- The total number of monitored deployments across all secured clusters that are connected to a single Central deployment

- The number of concurrent web portal users

| Deployments | Concurrent web portal users | CPU     | Memory |
|-------------|-----------------------------|---------|--------|
| \< 25,000   | 1 user                      | 2 cores | 8 GiB  |
| \< 25,000   | \< 5 users                  | 2 cores | 8 GiB  |
| \< 50,000   | 1 user                      | 2 cores | 12 GiB |
| \< 50,000   | \< 5 users                  | 6 cores | 16 GiB |

<a id="recommended-requirements-central-db-services-central_acs-recommended-requirements"></a>

## Central DB

<a id="_memory_and_cpu_requirements_2"></a>

### Memory and CPU requirements

The following table lists the minimum memory and CPU values required to run Central DB. To determine sizing, consider the following data:

- The total number of monitored deployments across all secured clusters that are connected to a single Central deployment

- The number of concurrent web portal users

| Deployments | Concurrent web portal users | CPU      | Memory |
|-------------|-----------------------------|----------|--------|
| \< 25,000   | 1 user                      | 12 cores | 32 GiB |
| \< 25,000   | \< 5 users                  | 24 cores | 32 GiB |
| \< 50,000   | 1 user                      | 16 cores | 32 GiB |
| \< 50,000   | \< 5 users                  | 32 cores | 32 GiB |

<a id="recommended-requirements-central-services-scanner-stackrox_acs-recommended-requirements"></a>

## StackRox Scanner

The following table lists the minimum memory and CPU values required for the StackRox Scanner deployment in the Central cluster. The table includes the number of unique images deployed in all secured clusters.

| Number of unique Images | Replicas   | CPU     | Memory  |
|-------------------------|------------|---------|---------|
| \< 100                  | 1 replica  | 1 core  | 1.5 GiB |
| \< 500                  | 1 replica  | 2 cores | 2.5 GiB |
| \< 2000                 | 2 replicas | 2 cores | 2.5 GiB |
| \< 5000                 | 3 replicas | 2 cores | 2.5 GiB |

<a id="recommended-requirements-central-services-scanner-scannerv4_acs-recommended-requirements"></a>

## Scanner V4

The following table lists the minimum memory and CPU values required for the Scanner V4 deployment in the Central cluster. The table includes the number of unique images deployed in all secured clusters.

<a id="_scanner_v4_indexer"></a>

### Scanner V4 Indexer

| Number of unique images | Replicas | CPU     | Memory  |
|-------------------------|----------|---------|---------|
| \< 100                  | 1        | 2 cores | 0.5 GiB |
| \< 500                  | 1        | 2 cores | 0.5 GiB |
| \< 2000                 | 2        | 3 cores | 1 GiB   |
| \< 5000                 | 2        | 5 cores | 1 GiB   |
| \< 10000                | 3        | 6 cores | 1.5 GiB |

<a id="_scanner_v4_matcher"></a>

### Scanner V4 Matcher

| Number of unique images | Replicas | CPU     | Memory  |
|-------------------------|----------|---------|---------|
| \< 100                  | 1        | 1 core  | 1.3 GiB |
| \< 500                  | 1        | 1 core  | 1.4 GiB |
| \< 2000                 | 2        | 3 cores | 1.5 GiB |
| \< 5000                 | 2        | 3 cores | 1.6 GiB |
| \< 10000                | 3        | 3 cores | 1.7 GiB |

<a id="_scanner_v4_db"></a>

### Scanner V4 DB

| Number of unique images | Replicas | CPU     | Memory  |
|-------------------------|----------|---------|---------|
| \< 100                  | 1        | 1 core  | 4.5 GiB |
| \< 500                  | 1        | 3 cores | 5 GiB   |
| \< 2000                 | 1        | 6 cores | 6 GiB   |
| \< 5000                 | 1        | 6 cores | 6 GiB   |
| \< 10000                | 1        | 8 cores | 6 GiB   |

<div>

<div class="title">

Additional resources

</div>

- [Default resource requirements](acs-default-requirements.md#acs-general-requirements_acs-default-requirements)

</div>

<a id="recommended-requirements-secured-cluster-services_acs-recommended-requirements"></a>

# Secured cluster services

Secured cluster services contain the following components:

- Sensor

- Admission controller

- Collector

  > [!NOTE]
  > Information about the resource requirements for the Collector component is included in the Default resource requirements section.

<a id="recommended-requirements-vm-scanning_acs-recommended-requirements"></a>

# Resource requirements for virtual machine scanning

When using Red Hat Advanced Cluster Security for Kubernetes (RHACS) to scan virtual machines (VMs) for vulnerabilities, you might need to adjust CPU and memory resource allocations for certain components to match the scale of your environment. Scanner V4 might require modified resources depending on the number of VMs and frequency of scans.

For more information about configuring VM scanning, see "Scanning virtual machines".

The following guidelines were developed by running tests that deployed large numbers of VMs and identifying the resources that determine the overall system throughput. The tests identified the number of VMs and the frequency of their scans as the primary driver of resource usage. These tests showed that you can achieve higher throughput by modifying Scanner V4 resources.

The following settings impact throughput when allocating resources at the OpenShift Container Platform level:

- Scanner V4 Matcher replicas: These are controlled by the Scanner V4 Matcher Horizontal Pod Autoscaler (HPA).

- Scanner V4 Matcher CPU limit

- Scanner V4 DB CPU limit

When calculating infrastructure requirements, use the standard guidance for the rest of the system, and adjust Scanner V4 resources according to the recommendations in the following table:

| Number of VMs | Scanner V4 Matcher HPA maximum replicas | Scanner V4 Matcher CPU limit | Scanner V4 DB CPU limit |
|----|----|----|----|
| \< 4500 | 3 | 1 core | 4 cores |
| \< 14000 | 3 | 1 core | 8 cores |
| \< 25000 | 3 | 1 core | 16 cores |
| \< 40000 | 3 | 2 cores | 32 cores |
| \< 50000 | 6 | 2 cores | 32 cores |

<a id="_factors_affecting_throughput"></a>

## Factors affecting throughput

While Scanner V4 resources constrain throughput, other factors are relevant when determining the number of VMs that a specific RHACS deployment supports. Consider the following factors:

- VM scan interval: System throughput is measured in VM scans per unit of time, and therefore scan interval, a configuration parameter of `roxagent`, directly impacts the number of VMs that RHACS can handle. The figures in the previous table were calculated for a scan interval of 4 hours, the default setting. A scan interval of 2 hours would result in halved numbers of VMs, and an interval of 8 hours would result in doubled numbers of VMs.

- VM index report rate limiter: RHACS is protected against excessive load by a rate limiter, which rejects index reports sent by VMs when their rate exceeds the maximum value. If you see administration events indicating that VM index reports are being rate limited and you have increased system resources, adjust the rate limit by using the `ROX_VM_INDEX_REPORT_RATE_LIMIT` environment variable. The rate limiter allows bursts according to the `ROX_VM_INDEX_REPORT_BUCKET_CAPACITY` environment variable, which can be increased to allow larger bursts if the Central pod has enough available memory. For more information, see "Advanced virtual machine scanning configuration" in "Scanning virtual machines".

- Number of packages installed in each VM: Increased numbers of packages result in increased scan times, and therefore reduce throughput.

- Vulnerabilities in installed packages: Greater numbers of overall vulnerabilities found in VMs result in longer scan times, reducing throughput.

- Other workloads: While RHACS processes VMs, RHACS components keep processing the rest of the usual workloads. These components include Scanner V4, and therefore such workloads reduce the VM scanning throughput.

  To account for these factors and their variability, the suggested capacity for each deployment type includes a headroom of at least 100%. Therefore, even if the processing time doubles due to an increased number of packages or vulnerabilities, RHACS can handle the specified number of VMs.

<a id="compliance-relay-concurrency_acs-recommended-requirements"></a>

## Compliance relay concurrency and buffer sizing

The Compliance relay, which runs in the Compliance container of the Collector pod, manages the vsock connections from VMs and buffers index reports before forwarding them to Sensor. The following parameters affect relay capacity:

- `ROX_VIRTUAL_MACHINES_MAX_CONCURRENT_VSOCK_CONNECTIONS`: Controls how many VMs can send index reports simultaneously to a single node. Do not change this value unless a single node handles many VMs and you observe performance problems in the Compliance container. Increasing this value increases the load on the Compliance container, and you must ensure that sufficient CPU and memory are allocated to the container.

- `ROX_VIRTUAL_MACHINES_INDEX_REPORTS_BUFFER_SIZE`: Controls the number of index reports buffered in Sensor before they are forwarded to Central. Increase this value only if Central is slow to process reports while Sensor is operating normally. Increasing this buffer causes Sensor to hold more index reports in memory, which can lead to Sensor running out of memory. Before changing this value, investigate the resource allocation for Central and Scanner V4 Matcher.

- `ROX_VM_RELAY_MAX_REPORTS_PER_MINUTE`: Controls relay-side rate limiting for forwarding reports to Sensor per VM connection. Only increase this value if specific VMs are reporting infrequently, for example, once every one or two days instead of every four hours, which can indicate those VMs are being starved by the rate limiter. In that case, a modest increase, for example, from `1.0` to `2.0`, might help. Do not increase this value significantly unless the Scanner V4 Matcher has enough resources to handle the additional load.

<a id="central-enrichment-throughput_acs-recommended-requirements"></a>

## Central enrichment throughput

Central processes incoming VM index reports by enriching them with vulnerability data from Scanner V4. At scale, this enrichment adds CPU and memory load to the Central pod. Consider the following:

- Each VM index report triggers a vulnerability matching request to Scanner V4. The Central pod CPU usage increases linearly with the rate of incoming reports.

- Central memory usage increases with the number of active VMs because vulnerability results are cached. For deployments exceeding 10,000 VMs, monitor Central memory usage and increase limits if necessary.

- If Central is overloaded, the rate limiter (`ROX_VM_INDEX_REPORT_RATE_LIMIT`) rejects excess reports, which delays vulnerability data freshness but protects system stability.

<div>

<div class="title">

Additional resources

</div>

- [Scanning virtual machines](../operating/examine-images-for-vulnerabilities.md#scanning-virtual-machines_examine-images-for-vulnerabilities)

</div>
