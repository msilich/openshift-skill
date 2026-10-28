<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the shared cache architecture to reduce Kubernetes API server load and resource consumption in large-scale `flowlogs-pipeline` deployments while maintaining network flow visibility.

# Performance challenges in large-scale deployments

In large-scale deployments, each `flowlogs-pipeline` instance independently queries the Kubernetes API server to enrich flows with metadata, resulting in a linear increase in API queries as instances scale.

The `flowlogs-pipeline` component enriches network flow data with Kubernetes metadata, such as pod names, labels, and namespace information. To retrieve this metadata, each `flowlogs-pipeline` instance independently queries the Kubernetes API server using informers that watch for resource changes.

## API server load at scale

In the default deployment model, the number of API queries increases linearly with the number of `flowlogs-pipeline` instances:

- Each `flowlogs-pipeline` pod maintains separate informers for pods, nodes, services, and other Kubernetes resources.

- Every informer establishes a watch connection to the API server.

- Resource updates are sent independently to each `flowlogs-pipeline` instance.

For example, in a cluster with 10 `flowlogs-pipeline` processor pods, the API server handles 10 times the watch connections and update notifications compared to a single instance. As you scale `flowlogs-pipeline` horizontally to handle increased network traffic, the API server load multiplies accordingly.

## Resource consumption patterns

This architecture creates several performance challenges:

Memory footprint
Each `flowlogs-pipeline` instance maintains a full in-memory cache of all watched Kubernetes resources. In large clusters with thousands of pods and services, this cache can consume significant memory per instance.

CPU utilization
Processing redundant API server updates and maintaining separate caches increases CPU usage across all `flowlogs-pipeline` pods.

API server impact
The cumulative load from multiple `flowlogs-pipeline` instances can degrade API server performance, potentially affecting other cluster components that depend on the API server for critical operations.

Network bandwidth
Duplicate resource updates consume network bandwidth between the API server and `flowlogs-pipeline` instances.

These resource consumption patterns become particularly pronounced in clusters with:

- High pod churn rates where applications frequently scale up and down

- Large numbers of namespaces and services

- Multiple `flowlogs-pipeline` instances deployed to handle high network traffic volumes

# How the shared cache improves cluster stability

The `flowlogs-pipeline` shared cache architecture improves cluster stability and performance in large-scale deployments by centralizing metadata retrieval.

In the default deployment model, each `flowlogs-pipeline` (`flowlogs-pipeline`) instance independently queries the Kubernetes API server to enrich network flows with cluster metadata, such as pod names and labels. At scale, this can result in a high volume of redundant requests that impact the API server performance.

When you enable the shared cache, a centralized component queries the API server and shares the cached metadata with all `flowlogs-pipeline` instances.

## High availability with leader election

The shared cache architecture uses leader election to ensure continuous operation when multiple replicas are deployed. Among the cache replicas, one pod is elected as the active leader that queries the Kubernetes API server and distributes updates. The remaining replicas remain on standby.

If the leader pod fails or is terminated, the remaining replicas automatically elect a new leader, typically within seconds. During this change, flow enrichment continues using cached metadata, though new resource changes might not be reflected until the new leader is established.

The Operator enforces a minimum of 2 replicas to ensure high availability. Deploying only a single replica creates a single point of failure where flow enrichment would be lost if that pod becomes unavailable.

## When to use the shared cache

Enable the shared cache architecture in environments with any of the following characteristics:

- High pod churn rates where applications scale often.

- Large numbers of namespaces and services.

- Many `flowlogs-pipeline` instances deployed to handle high network traffic volumes.

## Considerations

Before modifying the shared cache configuration, consider the following trade-offs:

- Data freshness: There might be a minor delay in flow enrichment updates as metadata propagates from the API server through the cache to the `flowlogs-pipeline` instances.

- Cluster-wide memory: While individual `flowlogs-pipeline` pods consume fewer resources, the addition of shared cache replicas increases the total memory allocated to the network observability namespace.

- Port allocation: The shared cache uses port `9402` for internal gRPC communication between the informer cache proxy and `flowlogs-pipeline` instances.

# Reduce API server load in large clusters

To reduce Kubernetes API server load and optimize resource consumption in large clusters, enable the `flowlogs-pipeline` shared cache. The shared cache is recommended for clusters with more than 3 `flowlogs-pipeline` replicas, especially when API server load becomes a performance concern.

<div>

<div class="title">

Prerequisites

</div>

- The Network Observability Operator is installed.

- Access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, navigate to **Operators** → **Installed Operators**.

2.  Select the **Network Observability Operator**, and then click the **`FlowCollector`** tab.

3.  Click the `cluster` instance, and then click the **YAML** tab.

4.  In the `spec.processor` section, set the `informerCacheProxy` configuration to enable the shared cache by using the following example:

    ``` yaml
    apiVersion: flows.netobserv.io/v1beta2
    kind: FlowCollector
    metadata:
      name: cluster
    spec:
      processor:
        informerCacheProxy:
          enabled: true
          replicas: 2
    ```

    where:

    `spec.processor.informerCacheProxy.enabled`
    Set to `true` to enable the informer cache proxy. The default value is `false`.

    `spec.processor.informerCacheProxy.replicas`
    Specifies the number of replicas. For high availability in production environments, the minimum is `2`. The Operator enforces this requirement with leader election to prevent a single point of failure.

5.  Click **Save**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Navigate to **Workloads** → **Pods**.

2.  Ensure that the pods beginning with `flowlogs-pipeline-informers` are in the **Running** state.

3.  Verify that one pod shows as the active leader by checking the pod logs for leader election messages.

4.  Confirm that the `flowlogs-pipeline` pods remain **Running** and show decreased CPU and memory use in the **Metrics** tab.

</div>

# Shared cache configuration parameters

Use the `FlowCollector` informer parameters to configure how the `flowlogs-pipeline` queries metadata from the Kubernetes API server, including cache settings and resource selection.

> [!NOTE]
> The shared cache feature uses centralized Kubernetes informers. Configure this feature in the `spec.processor.informerCacheProxy` field of the `FlowCollector` custom resource.

| Parameter | Type | Default | Description |
|----|----|----|----|
| `enabled` | Boolean | `false` | Enables the shared cache architecture to centralize Kubernetes API metadata retrieval. When enabled, a dedicated `flowlogs-pipeline-informers` deployment queries the Kubernetes API server and distributes cached metadata to all `flowlogs-pipeline` instances through gRPC on port `9402`. |
| `replicas` | Integer | `2` | The number of shared cache pods to deploy. The minimum value is `2` to ensure high availability with leader election. The Operator enforces this requirement. |
| `resources` | Object | See `FlowCollector` API | Configures CPU and memory resource requests and limits for the shared cache pods. Specify `requests.cpu`, `requests.memory`, `limits.cpu`, and `limits.memory` according to your cluster size and performance requirements. |
| `advanced.resyncInterval` | Duration | `60` | The interval, in seconds, at which the informer cache proxy rediscovers `flowlogs-pipeline` processor pods and synchronizes their state. |
| `advanced.batchSize` | Integer | `100` | The number of cache update events to batch together before sending to `flowlogs-pipeline` instances. Larger batches improve efficiency but increase latency for metadata updates. |
| `advanced.sendTimeout` | Duration | `10` | The maximum time to wait when sending cache updates to `flowlogs-pipeline` instances. If a send operation exceeds this timeout, the system retries the update. |
| `advanced.updateBufferSize` | Integer | `100` | The size of the internal buffer queue for cache updates. Increase this value in high-churn environments where Kubernetes resources change often. |

Shared cache parameters

# Resolve shared cache performance issues

Troubleshoot shared cache component failures by verifying pod health, reviewing system logs, and confirming leader election status to restore cluster performance.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Network Observability Operator.

- You have access to the cluster as a user with the `cluster-admin` role.

- The shared cache architecture is enabled in your `FlowCollector` configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check the status of the shared cache pods by running the following command:

    ``` terminal
    $ oc get pods -n netobserv -l app=flowlogs-pipeline-informers
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                             READY   STATUS    RESTARTS   AGE
    flowlogs-pipeline-informers-7d9f8b5c4d-abc12   1/1     Running   0          5m
    flowlogs-pipeline-informers-7d9f8b5c4d-xyz34   1/1     Running   0          5m
    ```

    </div>

    Ensure all pods show `Running` status. If pods are in `CrashLoopBackOff` or `Error` status, proceed to examine the logs.

2.  Identify the current leader pod:

    ``` terminal
    $ oc logs -n netobserv -l app=flowlogs-pipeline-informers --tail=50 | grep -i "leader"
    ```

    Look for log entries indicating leader election status. Ensure that only one pod reports itself as the active leader.

3.  View detailed logs from the leader pod to diagnose issues:

    ``` terminal
    $ oc logs -n netobserv <flowlogs_pipeline_informers_pod_name>
    ```

    Common issues to look for:

    - **API server connection failures**: Error messages indicating inability to connect to the Kubernetes API server suggest network or RBAC permission issues.

    - **gRPC communication errors**: Messages about failed connections on port `9402` indicate `flowlogs-pipeline` instances cannot reach the shared cache.

    - **Leader election conflicts**: If multiple pods claim to be the leader, there might be a configuration issue with leader election.

4.  Verify that `flowlogs-pipeline` instances are receiving cache updates:

    ``` terminal
    $ oc logs -n netobserv -l app=flowlogs-pipeline --tail=100 | grep -i "k8scache"
    ```

    `flowlogs-pipeline` pods show successful connection messages to the shared cache on port `9402`.

5.  Check the shared cache service:

    ``` terminal
    $ oc get svc -n netobserv flowlogs-pipeline-k8scache
    ```

    Verify that the service exists and is routing to the correct pods.

6.  If the shared cache is not functioning correctly, check for RBAC permission issues:

    ``` terminal
    $ oc describe clusterrolebinding netobserv-informers
    ```

    The `ClusterRoleBinding` grants the `flowlogs-pipeline-informers` `ServiceAccount` the necessary permissions to watch Kubernetes resources.

</div>

<div>

<div class="title">

Verification

</div>

1.  After you resolve issues, complete the following verification steps:

    - Confirm all shared cache pods are running and healthy.

    - Verify that one pod shows as the active leader in the logs.

    - Check that `flowlogs-pipeline` pods successfully connect to the shared cache.

    - Monitor flow enrichment in the network observability console to ensure metadata is displayed correctly on network flows.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Kubernetes leader election and leases](https://kubernetes.io/docs/concepts/architecture/leases/)

</div>
