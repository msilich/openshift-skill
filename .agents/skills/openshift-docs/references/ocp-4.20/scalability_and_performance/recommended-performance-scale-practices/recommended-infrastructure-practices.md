<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

This topic provides recommended performance and scalability practices for infrastructure in OpenShift Container Platform.

# Infrastructure node sizing

*Infrastructure nodes* are nodes that are labeled to run pieces of the OpenShift Container Platform environment. The infrastructure node resource requirements depend on the cluster age, nodes, and objects in the cluster, as these factors can lead to an increase in the number of metrics or time series in Prometheus. The following infrastructure node size recommendations are based on the results observed in cluster-density testing detailed in the **Control plane node sizing** section, where the monitoring stack and the default ingress-controller were moved to these nodes.

| Number of worker nodes | Cluster density, or number of namespaces | CPU cores | Memory (GB) |
|----|----|----|----|
| 27 | 500 | 4 | 24 |
| 120 | 1000 | 8 | 48 |
| 252 | 4000 | 16 | 128 |
| 501 | 4000 | 32 | 128 |

In general, three infrastructure nodes are recommended per cluster.

> [!IMPORTANT]
> These sizing recommendations should be used as a guideline. Prometheus is a highly memory intensive application; the resource usage depends on various factors including the number of nodes, objects, the Prometheus metrics scraping interval, metrics or time series, and the age of the cluster. In addition, the router resource usage can also be affected by the number of routes and the amount/type of inbound requests.
>
> These recommendations apply only to infrastructure nodes hosting Monitoring, Ingress and Registry infrastructure components installed during cluster creation.

> [!NOTE]
> In OpenShift Container Platform 4.17, half of a CPU core (500 millicore) is now reserved by the system by default compared to OpenShift Container Platform 3.11 and previous versions. This influences the stated sizing recommendations.

# Scaling the Cluster Monitoring Operator

OpenShift Container Platform exposes metrics that the Cluster Monitoring Operator (CMO) collects and stores in the Prometheus-based monitoring stack. As an administrator, you can view dashboards for system resources, containers, and components metrics in the OpenShift Container Platform web console by navigating to **Observe** → **Dashboards**.

## Prometheus database storage requirements

Red Hat performed various tests for different scale sizes.

<div class="note">

<div class="title">

</div>

- The following Prometheus storage requirements are not prescriptive and should be used as a reference. Higher resource consumption might be observed in your cluster depending on workload activity and resource density, including the number of pods, containers, routes, or other resources exposing metrics collected by Prometheus.

- You can configure the size-based data retention policy to suit your storage requirements.

</div>

| Number of nodes | Number of pods (2 containers per pod) | Prometheus storage growth per day | Prometheus storage growth per 15 days | Network (per tsdb chunk) |
|----|----|----|----|----|
| 50 | 1800 | 6.3 GB | 94 GB | 16 MB |
| 100 | 3600 | 13 GB | 195 GB | 26 MB |
| 150 | 5400 | 19 GB | 283 GB | 36 MB |
| 200 | 7200 | 25 GB | 375 GB | 46 MB |

Prometheus Database storage requirements based on number of nodes/pods in the cluster

Approximately 20 percent of the expected size was added as overhead to ensure that the storage requirements do not exceed the calculated value.

The above calculation is for the default OpenShift Container Platform Cluster Monitoring Operator.

> [!NOTE]
> CPU utilization has minor impact. The ratio is approximately 1 core out of 40 per 50 nodes and 1800 pods.

**Recommendations for OpenShift Container Platform**

- Use at least two infrastructure (infra) nodes.

- Use at least three **openshift-container-storage** nodes with non-volatile memory express (SSD or NVMe) drives.

## Configuring cluster monitoring

You can increase the storage capacity for the Prometheus component in the cluster monitoring stack.

<div>

<div class="title">

Procedure

</div>

1.  To increase the storage capacity for Prometheus, create a YAML configuration file, `cluster-monitoring-config.yaml`, as in the following example:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    data:
      config.yaml: |
        prometheusK8s:
          retention: <prometheus_retention_period>
          nodeSelector:
            node-role.kubernetes.io/infra: ""
          volumeClaimTemplate:
            spec:
              storageClassName: <storage_class>
              resources:
                requests:
                  storage: <prometheus_storage_size>
        alertmanagerMain:
          nodeSelector:
            node-role.kubernetes.io/infra: ""
          volumeClaimTemplate:
            spec:
              storageClassName: <storage_class>
              resources:
                requests:
                  storage: <alertmanager_storage_size>
    metadata:
      name: cluster-monitoring-config
      namespace: openshift-monitoring
    ```

    - `<prometheus_retention_period>` specifies the Prometheus retention period. The default value is `15d`. Units are measured in time using one of these suffixes: s, m, h, d.

    - `<storage_class>` specifies the storage class for your cluster.

    - `<prometheus_storage_size>` specifies the Prometheus storage size. A typical value is `2000Gi`. Storage values can be a plain integer or a fixed-point integer using one of these suffixes: E, P, T, G, M, K. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki.

    - `<alertmanager_storage_size>` specifies the Alertmanager storage size. A typical value is `20Gi`. Storage values can be a plain integer or a fixed-point integer using one of these suffixes: E, P, T, G, M, K. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki.

2.  Add values for the retention period, storage class, and storage sizes.

3.  Save the file.

4.  Apply the changes by running:

    ``` terminal
    $ oc create -f cluster-monitoring-config.yaml
    ```

</div>

# Additional resources

- [Infrastructure Nodes in OpenShift 4](https://access.redhat.com/solutions/5034771)

- [OpenShift Container Platform cluster maximums](../planning-your-environment-according-to-object-maximums.md#planning-your-environment-according-to-object-maximums)

- [Creating infrastructure machine sets](../../machine_management/creating-infrastructure-machinesets.md#creating-infrastructure-machinesets)
