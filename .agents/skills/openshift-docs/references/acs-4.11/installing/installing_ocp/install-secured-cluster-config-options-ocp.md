<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When installing Secured Cluster services by using the Operator, you can configure optional settings.

<a id="secured-cluster-configuration-options-operator_install-secured-cluster-config-options-ocp"></a>

# Secured Cluster services configuration options

When you create a Central instance, the Operator lists the following configuration options for the `Central` custom resource.

<a id="required-configuration-settings_install-secured-cluster-config-options-ocp"></a>

## Required configuration settings

| Parameter | Description |
|----|----|
| `centralEndpoint` | The endpoint of Central instance to connect to, including the port number. If using a non-gRPC capable load balancer, use the WebSocket protocol by prefixing the endpoint address with `wss://`. If you do not specify a value for this parameter, Sensor attempts to connect to a Central instance running in the same namespace. |
| `clusterName` | The unique name of this cluster, which shows up in the RHACS portal. After you set the name by using this parameter, you cannot change it again. To change the name, you must delete and re-create the object. |

<a id="admission-controller-settings_install-secured-cluster-config-options-ocp"></a>

## Admission controller settings

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>admissionControl.enforcement</code></p></td>
<td style="text-align: left;"><p>This parameter determines if you configured the admission controller to enforce policies that have enforcement enabled. For a new secured cluster deployed with RHACS 4.9, the default value is <code>Enabled</code>. For secured clusters updating from RHACS versions before 4.9, previous values for the admission controller configuration parameters determine the value of this parameter. Before the update, if either of the <code>admissionControl.listenOnCreates</code> or <code>admissionControl.listenOnUpdates</code> parameters was set to <code>true</code>, the value of this parameter defaults to <code>Enabled</code> after upgrade. If both of these parameters were set to <code>false</code>, the default value becomes <code>Disabled</code> on update.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.listenOnCreates</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated. RHACS checks the value during updates to version 4.9 and is used to set a default value for the new <code>admissionControl.enforcement</code> parameter. On new installations, changing this parameter has no effect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.listenOnEvents</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated. RHACS checks the value during updates to version 4.9 and is used to set a default value for the new <code>admissionControl.enforcement</code> parameter. On new installations, changing this parameter has no effect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.listenOnUpdates</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated and RHACS ignores its value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.nodeSelector</code></p></td>
<td style="text-align: left;"><p>If you want this component to only run on specific nodes, you can configure a node selector using this parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Admission Control. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.hostAliases</code></p></td>
<td style="text-align: left;"><p>Use this parameter to inject hosts and IP addresses into the pod’s hosts file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.resources.limits</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource limits for the admission controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.resources.requests</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource requests for the admission controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.bypass</code></p></td>
<td style="text-align: left;"><p>Use one of the following values to configure whether RHACS allows bypassing the admission controller enforcement:</p>
<ul>
<li><p><code>BreakGlassAnnotation</code> to enable bypassing the admission controller by using the <code>admission.stackrox.io/break-glass</code> annotation.</p></li>
<li><p><code>Disabled</code> to disable the ability to bypass admission controller enforcement for the secured cluster.</p></li>
</ul>
<p>The default value is <code>BreakGlassAnnotation</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.contactImageScanners</code></p></td>
<td style="text-align: left;"><p>This field is deprecated. Setting it has no effect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.failurePolicy</code></p></td>
<td style="text-align: left;"><p>Determines whether the API server request is allowed (fail open) or blocked (fail closed) if an error or timeout happens in the RHACS validating webhook’s evaluation. Valid values are <code>Ignore</code> and <code>Fail</code>. The default value is <code>Ignore</code> to fail open.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.timeoutSeconds</code></p></td>
<td style="text-align: left;"><p>The ability to configure this parameter is deprecated. RHACS uses a preset value for the timeout period and you cannot change it. This parameter is ignored.</p></td>
</tr>
</tbody>
</table>

<a id="scanner-configuration-settings_install-secured-cluster-config-options-ocp"></a>

## Scanner configuration settings for the Operator

Use Scanner configuration settings to modify the local cluster scanner for the integrated OpenShift image registry.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.nodeSelector</code></p></td>
<td style="text-align: left;"><p>Specify a node selector label as <code>label-key: label-value</code> to force Scanner to only schedule on nodes with the specified label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Scanner.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.hostAliases</code></p></td>
<td style="text-align: left;"><p>Use this parameter to inject hosts and IP addresses into the pod’s hosts file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.resources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for the Scanner container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.resources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for the Scanner container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.resources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for the Scanner container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.resources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for the Scanner container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.scaling.autoscaling</code></p></td>
<td style="text-align: left;"><p>If you set this option to <code>Disabled</code>, Red Hat Advanced Cluster Security for Kubernetes disables autoscaling on the Scanner deployment. The default value is <code>Enabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.scaling.minReplicas</code></p></td>
<td style="text-align: left;"><p>The minimum number of replicas for autoscaling. The default value is <code>2</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.scaling.maxReplicas</code></p></td>
<td style="text-align: left;"><p>The maximum number of replicas for autoscaling. The default value is <code>5</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.scaling.replicas</code></p></td>
<td style="text-align: left;"><p>The default number of replicas. The default value is <code>3</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.analyzer.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Scanner.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.db.nodeSelector</code></p></td>
<td style="text-align: left;"><p>Specify a node selector label as <code>label-key: label-value</code> to force Scanner DB to only schedule on nodes with the specified label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.db.hostAliases</code></p></td>
<td style="text-align: left;"><p>Use this parameter to inject hosts and IP addresses into the pod’s hosts file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.db.resources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for the Scanner DB container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.db.resources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for the Scanner DB container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.db.resources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for the Scanner DB container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.db.resources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for the Scanner DB container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.db.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Scanner DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.scannerComponent</code></p></td>
<td style="text-align: left;"><p>If you set this option to <code>Disabled</code>, Red Hat Advanced Cluster Security for Kubernetes does not deploy the Scanner deployment. Do not disable the Scanner on OpenShift Container Platform clusters. The default value is <code>AutoSense</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.nodeSelector</code></p></td>
<td style="text-align: left;"><p>If you want this component to only run on specific nodes, you can use this parameter to configure a node selector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Scanner V4 DB. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.resources.limits</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource limits for Scanner V4 DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.resources.requests</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource requests for Scanner V4 DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.persistence.persistentVolumeClaim.claimName</code></p></td>
<td style="text-align: left;"><p>The name of the PVC to manage persistent data for Scanner V4. You can use a PVC, which is the recommended default if a default storage class exists on the cluster. If no default storage class exists and it is not specifically set in the <code>persistentVolumeClaim.storageClassName</code> parameter, ephemeral storage is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.persistence.persistentVolumeClaim.size</code></p></td>
<td style="text-align: left;"><p>The size of the PVC to manage persistent data for Scanner V4.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.persistence.persistentVolumeClaim.storageClassName</code></p></td>
<td style="text-align: left;"><p>The name of the storage class to use for the PVC. If your cluster is not configured with a default storage class, and no value is provided for this parameter, ephemeral storage is used.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.nodeSelector</code></p></td>
<td style="text-align: left;"><p>If you want this component to only run on specific nodes, you can use this parameter to configure a node selector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for the Scanner V4 Indexer. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.resources.limits</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource limits for the Scanner V4 Indexer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.resources.requests</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource requests for the Scanner V4 Indexer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.scaling.autoScaling</code></p></td>
<td style="text-align: left;"><p>When enabled, the number of Scanner V4 Indexer replicas is managed dynamically based on the load, within the limits specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.scaling.maxReplicas</code></p></td>
<td style="text-align: left;"><p>Specifies the maximum replicas to be used in the Scanner V4 Indexer autoscaling configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.scaling.minReplicas</code></p></td>
<td style="text-align: left;"><p>Specifies the minimum replicas to be used in the Scanner V4 Indexer autoscaling configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.scaling.replicas</code></p></td>
<td style="text-align: left;"><p>When autoscaling is disabled for the Scanner V4 Indexer, the number of replicas is always configured to match this value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.monitoring.exposeEndpoint</code></p></td>
<td style="text-align: left;"><p>Configures a monitoring endpoint for Scanner V4. The monitoring endpoint allows other services to collect metrics from Scanner V4, provided in a Prometheus-compatible format. Use <code>Enabled</code> to expose the monitoring endpoint. When you enable monitoring, RHACS creates a new service, <code>monitoring</code>, with port 9090, and a network policy allowing inbound connections to the port. By default, this is not enabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.scannerComponent</code></p></td>
<td style="text-align: left;"><p>Enables Scanner V4. Valid values are:</p>
<p>* <code>Default</code>: Scanner V4 is not enabled and not deployed.</p>
<p>* <code>AutoSense</code>: If Central exists in the same namespace, Scanner V4 is not deployed and the existing Scanner V4 that was installed with Central is used. If there is no Central in this namespace, Scanner V4 is deployed.</p>
<p>* <code>Disabled</code>: Do not deploy Scanner V4.</p></td>
</tr>
</tbody>
</table>

<a id="image-configuration-settings_install-secured-cluster-config-options-ocp"></a>

## Image configuration

Use image configuration settings when you are using a custom registry.

| Parameter | Description |
|----|----|
| `imagePullSecrets.name` | Additional image pull secrets to be taken into account for pulling images. |

<a id="per-node-settings_install-secured-cluster-config-options-ocp"></a>

## Per node settings

Per node settings define the configuration settings for components that run on each node in a cluster to secure the cluster. These components are Collector and Compliance.

| Parameter | Description |
|----|----|
| `perNode.collector.collection` | The method for system-level data collection. The default value is `CORE_BPF`. Red Hat recommends using `CORE_BPF` for data collection. If you select `NoCollection`, Collector does not report any information about the network activity and the process executions. Available options are `NoCollection` and `CORE_BPF`. The `EBPF` option is available only for version 4.4 and earlier. |
| `perNode.collector.imageFlavor` | The image type to use for Collector. You can specify it as `Regular` or `Slim`. This value is deprecated. `Regular` and `Slim` images are identical. |
| `perNode.collector.resources.limits` | Use this parameter to override the default resource limits for Collector. |
| `perNode.collector.resources.requests` | Use this parameter to override the default resource requests for Collector. |
| `perNode.compliance.resources.requests` | Use this parameter to override the default resource requests for Compliance. |
| `perNode.compliance.resources.limits` | Use this parameter to override the default resource limits for Compliance. |
| `perNode.sfa.agent` | Use this parameter to enable file activity monitoring for the secured cluster. Set to `Enabled`. |
| `perNode.taintToleration` | To ensure comprehensive monitoring of your cluster activity, Red Hat Advanced Cluster Security for Kubernetes runs services on every node in the cluster, including tainted nodes by default. If you do not want this behavior, specify `AvoidTaints` for this parameter. The default value is `TolerateTaints`. |

<a id="sensor-configuration-settings_install-secured-cluster-config-options-ocp"></a>

## Sensor configuration

This configuration defines the settings of the Sensor components, which runs on one node in a cluster.

| Parameter | Description |
|----|----|
| `sensor.nodeSelector` | If you want Sensor to only run on specific nodes, you can configure a node selector. |
| `sensor.tolerations` | If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Sensor. This parameter is mainly used for infrastructure nodes. |
| `sensor.hostAliases` | Use this parameter to inject hosts and IP addresses into the pod’s hosts file. |
| `sensor.resources.limits` | Use this parameter to override the default resource limits for Sensor. |
| `sensor.resources.requests` | Use this parameter to override the default resource requests for Sensor. |

<a id="general-and-miscellaneous-settings-secured-cluster_install-secured-cluster-config-options-ocp"></a>

## General and miscellaneous settings

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>customize.annotations</code></p></td>
<td style="text-align: left;"><p>Allows specifying custom annotations for the Central deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>customize.envVars</code></p></td>
<td style="text-align: left;"><p>Advanced settings to configure environment variables.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>customize.deploymentDefaults.pinToNodes</code></p></td>
<td style="text-align: left;"><p>Automates the placement of all deployment-based components onto specific node types. Set to <code>InfraRole</code> to target OpenShift infrastructure nodes. You cannot use this parameter simultaneously with <code>nodeSelector</code> or <code>tolerations</code>. The default value is <code>None</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>If you configure a specific node selector or tolerations settings for individual components, such as <code>central.nodeSelector</code> or <code>admissionControl.nodeSelector</code>, those settings override the global values defined in <code>customize.deploymentDefaults.pinToNodes</code>.</p>
<p>Setting <code>pinToNodes</code> to <code>InfraRole</code> is a simple alternative to manually configuring node selectors and tolerations when you want to pin deployments to infrastructure nodes.</p>
<p>It is the exact equivalent of applying the following configuration:</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="co"># ...</span></span>
<span id="cb1-2"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="fu">nodeSelector</span><span class="kw">:</span></span>
<span id="cb1-3"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">node-role.kubernetes.io/infra</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;&quot;</span></span>
<span id="cb1-4"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="fu">tolerations</span><span class="kw">:</span></span>
<span id="cb1-5"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="fu">key</span><span class="kw">:</span><span class="at"> node-role.kubernetes.io/infra</span></span>
<span id="cb1-6"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">value</span><span class="kw">:</span><span class="at"> reserved</span></span>
<span id="cb1-7"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">effect</span><span class="kw">:</span><span class="at"> NoSchedule</span></span>
<span id="cb1-8"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="fu">key</span><span class="kw">:</span><span class="at"> node-role.kubernetes.io/infra</span></span>
<span id="cb1-9"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">value</span><span class="kw">:</span><span class="at"> reserved</span></span>
<span id="cb1-10"><a data-unavailable-reference="true" aria-hidden="true" tabindex="-1"></a><span class="co"># ...</span></span></code></pre></div>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>customize.deploymentDefaults.nodeSelector</code></p></td>
<td style="text-align: left;"><p>Applies a default <code>nodeSelector</code> to all deployment-based components. You cannot use this parameter simultaneously with <code>pinToNodes</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<ul>
<li><p>If you configure specific <code>nodeSelector</code> settings for individual components, such as <code>admissionControl.nodeSelector</code>, <code>scanner.analyzer.nodeSelector</code>, <code>scanner.db.nodeSelector</code>, <code>scannerV4.db.nodeSelector</code>, <code>scannerV4.indexer.nodeSelector</code>, or <code>sensor.nodeSelector</code>, those settings override the global values defined in <code>customize.deploymentDefaults.nodeSelector</code>.</p></li>
<li><p>You can use this setting to define global node selectors and tolerations that are automatically inherited by all resources to reduce repetitive configuration and simplify scheduling.</p></li>
</ul>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>customize.deploymentDefaults.tolerations</code></p></td>
<td style="text-align: left;"><p>Applies default tolerations to all deployment-based components. You cannot use this parameter simultaneously with <code>pinToNodes</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<ul>
<li><p>If you configure specific <code>tolerations</code> settings for individual components, such as <code>admissionControl.tolerations</code>, <code>scanner.analyzer.tolerations</code>, <code>scanner.analyzer.tolerations</code>, <code>scanner.db.tolerations</code>, <code>scannerV4.db.tolerations</code>, <code>scannerV4.indexer.tolerations</code>, or <code>sensor.tolerations</code>, those settings override the global values defined in <code>customize.deploymentDefaults.tolerations</code>.</p></li>
<li><p>You can use this setting to define global node selectors and tolerations that are automatically inherited by all resources to reduce repetitive configuration and simplify scheduling.</p></li>
</ul>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>egress.connectivityPolicy</code></p></td>
<td style="text-align: left;"><p>Configures whether Red Hat Advanced Cluster Security for Kubernetes should run in online or offline mode. In offline mode, automatic updates of vulnerability definitions and kernel modules are disabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>misc.createSCCs</code></p></td>
<td style="text-align: left;"><p>Set this to <code>true</code> to create SCCs for Central. It may cause issues in some environments.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>network.policies</code></p></td>
<td style="text-align: left;"><p>To provide security at the network level, RHACS creates default <code>NetworkPolicy</code> resources in the namespace where secured cluster resources are installed. These network policies allow ingress to specific components on specific ports. If you do not want RHACS to create these policies, set this parameter to <code>Disabled</code>. The default value is <code>Enabled</code>.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>Disabling creation of default network policies can break communication between RHACS components. If you disable creation of default policies, you must create your own network policies to allow this communication.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>overlays</code></p></td>
<td style="text-align: left;"><p>See "Customizing the installation using the Operator with overlays".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tls.additionalCAs</code></p></td>
<td style="text-align: left;"><p>Additional trusted CA certificates for the secured cluster. These certificates are used when integrating with services using a private certificate authority.</p></td>
</tr>
</tbody>
</table>

<a id="customize-installation-operator-overlays_install-secured-cluster-config-options-ocp"></a>

# Customizing the installation using the Operator with overlays

Learn how to tailor the installation of RHACS using the Operator method with overlays.

<a id="overlays_install-secured-cluster-config-options-ocp"></a>

## Overlays

When `Central` or `SecuredCluster` custom resources don’t expose certain low-level configuration options as parameters, you can use the `.spec.overlays` field for adjustments. Use this field to amend the Kubernetes resources generated by these custom resources.

The `.spec.overlays` field comprises a sequence of patches, applied in their listed order. These patches are processed by the Operator on the Kubernetes resources before deployment to the cluster.

> [!WARNING]
> The `.spec.overlays` field in both `Central` and `SecuredCluster` allows users to modify low-level Kubernetes resources in arbitrary ways. Use this feature only when the desired customization is not available through the `SecuredCluster` or `Central` custom resources.
>
> Support for the `.spec.overlays` feature is limited primarily because it grants the ability to make intricate and highly specific modifications to Kubernetes resources, which can vary significantly from one implementation to another. This level of customization introduces a complexity that goes beyond standard usage scenarios, making it challenging to provide broad support. Each modification can be unique, potentially interacting with the Kubernetes system in unpredictable ways across different versions and configurations of the product. This variability means that troubleshooting and guaranteeing the stability of these customizations require a level of expertise and understanding specific to each individual’s setup. Consequently, while this feature empowers tailoring Kubernetes resources to meet precise needs, greater responsibility must also assumed to ensure the compatibility and stability of configurations, especially during upgrades or changes to the underlying product.

The following example shows the structure of an overlay:

``` yaml
overlays:
- apiVersion: v1         #
  kind: ExampleKind      #
  name: my-resource      #
  patches:
    - path: .some.field  #
      value: |           #
        key1: data2
        key2: data2
```

where:

`overlays.apiVersion`  
Specifies the targeted Kubernetes resource ApiVersion, for example, `apps/v1`, `v1`, `networking.k8s.io/v1`.

`overlays.kind`  
Specifies the resource type, for example,`Deployment`, `ConfigMap`, `NetworkPolicy`.

`overlays.name`  
Specifies the name of the resource, for example, `my-resource`.

`overlays.patches.path`  
Specifies the JSON path expression to the field, for example, `spec.template.spec.containers[name:central].env[-1]`.

`overlays.patches.value`  
Specifies the YAML string for the new field value. If you do not want to use YAML parsing, you can use the `verbatim` key as shown in the following ConfigMap example.

<a id="adding-an-overlay_install-secured-cluster-config-options-ocp"></a>

### Adding an overlay

For customizations, you can add overlays to `Central` or `SecuredCluster` custom resources. Use the OpenShift CLI (`oc`) or the OpenShift Container Platform web console for modifications.

If overlays do not take effect as expected, check the RHACS Operator logs for any syntax errors or issues logged.

<a id="examples_install-secured-cluster-config-options-ocp"></a>

## Overlay examples

<a id="adding-eks-role-arn-annotation_install-secured-cluster-config-options-ocp"></a>

### Specifying an EKS pod role ARN for the Central ServiceAccount

Add an Amazon Elastic Kubernetes Service (EKS) pod role Amazon Resource Name (ARN) annotation to the `central` ServiceAccount as shown in the following example:

``` yaml
apiVersion: platform.stackrox.io
kind: Central
metadata:
  name: central
spec:
  # ...
  overlays:
  - apiVersion: v1
    kind: ServiceAccount
    name: central
    patches:
      - path: metadata.annotations.eks\.amazonaws\.com/role-arn
        value: "\"arn:aws:iam:1234:role\""
```

<a id="adding-an-environment-variable-to-a-deployment_install-secured-cluster-config-options-ocp"></a>

### Injecting an environment variable into the Central deployment

Inject an environment variable into the `central` deployment as shown in the following example:

``` yaml
apiVersion: platform.stackrox.io
kind: Central
metadata:
  name: central
spec:
  # ...
  overlays:
  - apiVersion: apps/v1
    kind: Deployment
    name: central
    patches:
    - path: spec.template.spec.containers[name:central].env[-1]
      value: |
        name: MY_ENV_VAR
        value: value
```

<a id="adding-an-ingress-to-a-network-policy_install-secured-cluster-config-options-ocp"></a>

### Extending network policy with an ingress rule

Add an ingress rule to the `allow-ext-to-central` network policy for port 999 traffic as shown in the following example:

``` yaml
apiVersion: platform.stackrox.io
kind: Central
metadata:
  name: central
spec:
    # ...
    overlays:
    - apiVersion: networking.k8s.io/v1
      kind: NetworkPolicy
      name: allow-ext-to-central
      patches:
        - path: spec.ingress[-1]
          value: |
            ports:
            - port: 999
              protocol: TCP
```

<a id="changing-configmap-data_install-secured-cluster-config-options-ocp"></a>

### Modifying ConfigMap data

Modify the `central-endpoints` ConfigMap data as shown in the following example:

``` yaml
apiVersion: platform.stackrox.io
kind: Central
metadata:
  name: central
spec:
    # ...
    overlays:
    - apiVersion: v1
      kind: ConfigMap
      name: central-endpoints
      patches:
      - path: data.endpoints\.yaml
        verbatim: |
          disableDefault: false
          # another line
```

This example shows how to override only a single item (file) under `data`.

Follow this example by taking these steps:

- Use the `verbatim` key, rather than `value`. This helps pass through characters such as newlines or quotes so that they are unaffected.

- You must escape the dot in the filename in the `path` key as shown, or you can write the path as `data["endpoints.yaml"]`.

<a id="adding-a-container-to-a-deployment_install-secured-cluster-config-options-ocp"></a>

### Adding a container to the `Central` deployment

Add a new container to the `central` deployment as shown in the following example:.

``` yaml
apiVersion: platform.stackrox.io
kind: Central
metadata:
  name: central
spec:
    # ...
    overlays:
    - apiVersion: apps/v1
      kind: Deployment
      name: central
      patches:
        - path: spec.template.spec.containers[-1]
      value: |
        name: nginx
        image: nginx
        ports:
          - containerPort: 8000
            name: http
            protocol: TCP
```
