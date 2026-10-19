<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Understanding the interactions between your cluster and external entities is essential for incident response and network policy management. With the Visualizing external entities feature, you can view the external IP addresses that interact with your cluster.

<a id="visualizing-external-entities-overview_visualizing-external-entities"></a>

# Visualizing external entities overview

You can view external entities in the Network Graph or query them by using the API.

To view external entities in the Network Graph, select the **External Entities** graph node or check the deployment flows tab.

> [!NOTE]
> Visualizing external entities is an opt-in feature that the product disables by default. To enable this feature, you must enable external IP collection in secured clusters.

<a id="enabling-external-ip-collection-secured-clusters_visualizing-external-entities"></a>

# Enabling external IP collection in secured clusters

To enable external IP collection in secured clusters, you must individually configure each secured cluster’s runtime configuration.

You can have some clusters with the functionality enabled while others remain disabled. In this case, external IP information is only available for the clusters where you have enabled the feature.

You can use a `ConfigMap` object to enable the external IP collection in secured clusters.

<div>

<div class="title">

Procedure

</div>

- Create a `ConfigMap` object called `collector-config` with the following content:

  ``` yaml
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: collector-config
    namespace: stackrox
  data:
    runtime_config.yaml: |
      networking:
        externalIps:
          enabled: ENABLED
  ```

  where:

  `data.runtime_config.yaml`  
  Specifies the runtime configuration file. RHACS mounts this file at `/etc/stackrox/runtime_config.yaml`.

  `data.runtime_config.yaml.networking.externalIps.enabled`  
  Specifies whether to enable or disable external IPs for networking. You can set this parameter to `ENABLED` or `DISABLED`. When you create or update the `ConfigMap` object, the collector refreshes the runtime configuration. When you delete the `ConfigMap` object, the settings revert to the default runtime configuration values. For more information, see [Using Collector runtime configuration](using-collector-runtime-configuration.md).

</div>

<a id="querying-external-entities-using-api_visualizing-external-entities"></a>

# Querying external IP addresses by using the API

You can get information about the external IP addresses associated with a specific cluster by using the following endpoints:

- `/v1/networkgraph/cluster/{clusterId}/externalentities`: This endpoint returns a list of external entities for a given cluster ID. Each entity includes the following information:

  - **Name**: The name of the external entity.

  - **CIDR block**: The CIDR block associated with the entity.

  - **Default entity**: Indicates that the entity is a CIDR-block definition provided by the system.

  - **Discovered**: If `true`, indicates that the external IP address does not match any specified CIDR block.

- `/v1/networkgraph/cluster/{clusterId}/externalentities/{entityId}/flows`: This endpoint reports the flows to and from an external entity for a given cluster ID and entity ID. Use this endpoint to analyze network traffic patterns and gain insights into the interactions between your cluster and external entities.

- `/v1/networkgraph/cluster/{clusterId}/externalentities/metadata`: This endpoint reports statistics about the external flows for a given cluster ID. It reports details about each entity and the number of flows associated with it.

<a id="visualizing-external-entities-known-limitations_visualizing-external-entities"></a>

# Known limitations

The following are some known limitations of the Visualizing external entities feature:

- You cannot see external IP addresses if they are part of CIDR blocks.

- When you enable external IP collection for a cluster, the Collector in those clusters reports more information to Sensor and Central. Enabling external IP collection might create scalability issues if the workload in the cluster communicates with a large number of distinct external peers. Red Hat recommends that you turn off this feature on clusters with communication patterns involving more than 10,000 distinct external entities. However, if the pattern is mostly ingress or egress, you can overcome the scaling issue by enabling external IPs only in the opposite direction. For more information, see "Using Collector runtime configuration".

<a id="additional-resources_visualizing-external-entities"></a>

# Additional resources

- [Using Collector runtime configuration](using-collector-runtime-configuration.md)
