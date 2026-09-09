<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When installing the Central instance by using the Operator, you can configure optional settings.

<a id="central-configuration-options-operator_install-central-config-options-ocp"></a>

# Central configuration options using the Operator

When you create a Central instance, the Operator lists the following configuration options for the `Central` custom resource.

The following table includes settings for an external PostgreSQL database.

<a id="central-settings_install-central-config-options-ocp"></a>

## Central settings

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
<td style="text-align: left;"><p><code>central.adminPasswordSecret</code></p></td>
<td style="text-align: left;"><p>Specify a secret that contains the administrator password in the <code>password</code> data item. If omitted, the operator autogenerates a password and stores it in the <code>password</code> item in the <code>central-htpasswd</code> secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.defaultTLSSecret</code></p></td>
<td style="text-align: left;"><p>By default, Central only serves an internal TLS certificate, which means that you need to handle TLS termination at the ingress or load balancer level. If you want to terminate TLS in Central and serve a custom server certificate, you can specify a secret containing the certificate and private key.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.adminPasswordGenerationDisabled</code></p></td>
<td style="text-align: left;"><p>Set this parameter to <code>true</code> to disable the automatic administrator password generation. Use this only after you perform the first-time setup of alternative authentication methods. Do not use this for initial installation. Otherwise, you must reinstall the custom resource to log back in.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Central. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.hostAliases</code></p></td>
<td style="text-align: left;"><p>Use this parameter to inject hosts and IP addresses into the pod’s hosts file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.loadBalancer.enabled</code></p></td>
<td style="text-align: left;"><p>Set this to <code>true</code> to expose Central through a load balancer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.loadBalancer.port</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify a custom port for your load balancer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.loadBalancer.ip</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify a static IP address reserved for your load balancer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.enabled</code></p></td>
<td style="text-align: left;"><p>Set this to <code>true</code> to expose Central through a Red Hat OpenShift passthrough route. Disables all route settings if set to <code>false</code>. The default value is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.host</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify a custom hostname to use for Central’s passthrough route. Leave this unset to accept the default value that OpenShift Container Platform provides.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.enabled</code></p></td>
<td style="text-align: left;"><p>Set this to <code>true</code> to expose Central through a Red Hat OpenShift reencrypt route. The default value is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.host</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify a custom hostname to use for Central’s reencrypt route. Leave this unset to accept the default value that OpenShift Container Platform provides.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.tls.caCertificate</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify a PEM-encoded certificate chain that might be used to establish a complete chain of trust. By default, OpenShift Container Platform provides the certificate authority.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.tls.certificate</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify the PEM-encoded certificate that the route serves. The OpenShift Container Platform certificate authority signs the default certificate.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>You must specify both <code>certificate</code> and <code>key</code> together, or omit both. Specifying only one of these parameters causes the Operator to fail with a validation error.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.tls.destinationCACertificate</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify the CA certificate of the final destination, that is of Central. The OpenShift Container Platform router uses this certificate to perform health checks on the secure connection. By default, Central provides the certificate authority.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.tls.key</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify the PEM-encoded private key of the certificate that the route serves. The OpenShift Container Platform certificate authority signs the default certificate.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>You must specify both <code>certificate</code> and <code>key</code> together, or omit both. Specifying only one of these parameters causes the Operator to fail with a validation error.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.nodeport.enabled</code></p></td>
<td style="text-align: left;"><p>Set this to <code>true</code> to expose Central through a node port. The default value is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.nodeport.port</code></p></td>
<td style="text-align: left;"><p>Use this to specify an explicit node port.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.monitoring.exposeEndpoint</code></p></td>
<td style="text-align: left;"><p>Use <code>Enabled</code> to enable monitoring for Central. When you enable monitoring, RHACS creates a new monitoring service on port number <code>9090</code>. The default value is <code>Disabled</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.nodeSelector</code></p></td>
<td style="text-align: left;"><p>If you want this component to only run on specific nodes, you can use this parameter to configure a node selector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.resources.limits</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource limits for the Central.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.resources.requests</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource requests for the Central.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.configAsCode.nodeSelector</code></p></td>
<td style="text-align: left;"><p>If you want the config-controller component to only run on specific nodes, you can use this parameter to configure a node selector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.configAsCode.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for the config-controller component. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.configAsCode.hostAliases</code></p></td>
<td style="text-align: left;"><p>Use this parameter to inject hosts and IP addresses into the hosts file of the config-controller pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.configAsCode.resources.limits</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource limits for the config-controller component.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.configAsCode.resources.requests</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource requests for the config-controller component.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.imagePullSecrets</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify the image pull secrets for the Central image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.passwordSecret.name</code></p></td>
<td style="text-align: left;"><p>Specify a secret that has the database password in the <code>password</code> data item. Only use this parameter if you want to specify a connection string manually. If omitted, the operator auto-generates a password and stores it in the <code>password</code> item in the <code>central-db-password</code> secret.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.connectionString</code></p></td>
<td style="text-align: left;"><p>Setting this parameter will not deploy Central DB, and Central will connect using the specified connection string. If you specify a value for this parameter, you must also specify a value for <code>central.db.passwordSecret.name</code>. This parameter has the following constraints:</p>
<ul>
<li><p>Connection string must be in keyword/value format as described in the PostgreSQL documentation. For more information, see the links in the <strong>Additional resources</strong> section.</p></li>
<li><p>Postgres 15 is the recommended and supported version. Red Hat has deprecated the support for Postgres 13 and will remove it in the newer versions of RHACS.</p></li>
<li><p>Connections through PGBouncer are not supported.</p></li>
<li><p>You must have the following permissions on the database:</p>
<ul>
<li><p>Connection rights to the database.</p></li>
<li><p>Usage and create privileges on the schema.</p></li>
<li><p>Select, insert, update, and delete privileges on all tables.</p></li>
<li><p>Usage privileges on all sequences in the schema.</p></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Central DB. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.hostAliases</code></p></td>
<td style="text-align: left;"><p>Use this parameter to inject hosts and IP addresses into the pod’s hosts file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.persistence.hostPath.path</code></p></td>
<td style="text-align: left;"><p>Specify a host path to store persistent data in a directory on the host. Red Hat does not recommend using this. If you need to use host path, you must use it with a node selector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.persistence.persistentVolumeClaim.claimName</code></p></td>
<td style="text-align: left;"><p>The name of the PVC to manage persistent data. If no PVC with the given name exists, it is created. The default value is <code>central-db</code> if not set. To prevent data loss, the PVC is not removed automatically when Central is deleted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.persistence.persistentVolumeClaim.size</code></p></td>
<td style="text-align: left;"><p>The size of the persistent volume when created through the claim. This is automatically generated by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.persistence.persistentVolumeClaim.storageClassName</code></p></td>
<td style="text-align: left;"><p>The name of the storage class to use for the PVC. If your cluster is not configured with a default storage class, you must provide a value for this parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.connectionPoolSize.minConnections</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default minimum connection pool size between Central and Central DB. The default value is 10.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.connectionPoolSize.maxConnections</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default maximum connection pool size between Central and Central DB. The default value is 90. Ensure that this value does not exceed the maximum number of connections supported by the Central DB:</p>
<ul>
<li><p>An Operator-managed Central DB supports a maximum of 100 connections by default.</p></li>
<li><p>For external PostgreSQL databases, check the database settings or consult your cloud provider for managed databases.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.resources.limits</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource limits for the Central DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.resources.requests</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource requests for the Central DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.nodeSelector</code></p></td>
<td style="text-align: left;"><p>If you want this component to only run on specific nodes, you can use this parameter to configure a node selector.</p></td>
</tr>
</tbody>
</table>

<a id="scanner-settings_install-central-config-options-ocp"></a>

## StackRox Scanner settings for the Operator

| Parameter | Description |
|----|----|
| `scanner.analyzer.nodeSelector` | If you want this scanner to only run on specific nodes, you can use this parameter to configure a node selector. |
| `scanner.analyzer.tolerations` | If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for the StackRox Scanner. This parameter is mainly used for infrastructure nodes. |
| `scanner.analyzer.hostAliases` | Use this parameter to inject hosts and IP addresses into the pod’s hosts file. |
| `scanner.analyzer.resources.limits` | Use this parameter to override the default resource limits for the StackRox Scanner. |
| `scanner.analyzer.resources.requests` | Use this parameter to override the default resource requests for the StackRox Scanner. |
| `scanner.analyzer.scaling.autoScaling` | When enabled, the number of analyzer replicas is managed dynamically based on the load, within the limits specified. |
| `scanner.analyzer.scaling.maxReplicas` | Specifies the maximum replicas to be used in the analyzer autoscaling configuration |
| `scanner.analyzer.scaling.minReplicas` | Specifies the minimum replicas to be used in the analyzer autoscaling configuration |
| `scanner.analyzer.scaling.replicas` | When autoscaling is disabled, the number of replicas is always configured to match this value. |
| `scanner.db.nodeSelector` | If you want this component to only run on specific nodes, you can use this parameter to configure a node selector. |
| `scanner.db.tolerations` | If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for the StackRox Scanner DB. This parameter is mainly used for infrastructure nodes. |
| `scanner.db.hostAliases` | Use this parameter to inject hosts and IP addresses into the pod’s hosts file. |
| `scanner.db.resources.limits` | Use this parameter to override the default resource limits for the StackRox Scanner DB. |
| `scanner.db.resources.requests` | Use this parameter to override the default resource requests for the StackRox Scanner DB. |
| `scanner.monitoring.exposeEndpoint` | Use `Enabled` to enable monitoring for the StackRox Scanner. When you enable monitoring, RHACS creates a new monitoring service on port number `9090`. The default value is `Disabled`. |
| `scanner.scannerComponent` | If you do not want to deploy the StackRox Scanner, you can disable it by using this parameter. If you disable the StackRox Scanner, all other settings in this section have no effect. |

<a id="scannerv4-settings_install-central-config-options-ocp"></a>

## Scanner V4 settings for the Operator

| Parameter | Description |
|----|----|
| `scannerV4.db.nodeSelector` | If you want this component to only run on specific nodes, you can use this parameter to configure a node selector. |
| `scannerV4.db.tolerations` | If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Scanner V4 DB. This parameter is mainly used for infrastructure nodes. |
| `scannerV4.db.hostAliases` | Use this parameter to inject hosts and IP addresses into the pod’s hosts file. |
| `scannerV4.db.resources.limits` | Use this parameter to override the default resource limits for Scanner V4 DB. |
| `scannerV4.db.resources.requests` | Use this parameter to override the default resource requests for Scanner V4 DB. |
| `scannerV4.db.persistence.persistentVolumeClaim.claimName` | The name of the PVC to manage persistent data for Scanner V4. The default value is `scanner-v4-db`. |
| `scannerV4.db.persistence.persistentVolumeClaim.size` | The size of the PVC to manage persistent data for Scanner V4. |
| `scannerV4.db.persistence.persistentVolumeClaim.storageClassName` | The name of the storage class to use for the PVC. If your cluster is not configured with a default storage class, you must provide a value for this parameter. |
| `scannerV4.indexer.nodeSelector` | If you want this component to only run on specific nodes, you can use this parameter to configure a node selector. |
| `scannerV4.indexer.tolerations` | If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for the Scanner V4 Indexer. This parameter is mainly used for infrastructure nodes. |
| `scannerV4.indexer.hostAliases` | Use this parameter to inject hosts and IP addresses into the pod’s hosts file. |
| `scannerV4.indexer.resources.limits` | Use this parameter to override the default resource limits for the Scanner V4 Indexer. |
| `scannerV4.indexer.resources.requests` | Use this parameter to override the default resource requests for the Scanner V4 Indexer. |
| `scannerV4.indexer.scaling.autoScaling` | When enabled, the number of Scanner V4 Indexer replicas is managed dynamically based on the load, within the limits specified. |
| `scannerV4.indexer.scaling.maxReplicas` | Specifies the maximum replicas to be used in the Scanner V4 Indexer autoscaling configuration. |
| `scannerV4.indexer.scaling.minReplicas` | Specifies the minimum replicas to be used in the Scanner V4 Indexer autoscaling configuration. |
| `scannerV4.indexer.scaling.replicas` | When autoscaling is disabled for the Scanner V4 Indexer, the number of replicas is always configured to match this value. |
| `scannerV4.matcher.nodeSelector` | If you want this component to only run on specific nodes, you can use this parameter to configure a node selector. |
| `scannerV4.matcher.tolerations` | If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for the Scanner V4 Matcher. This parameter is mainly used for infrastructure nodes. |
| `scannerV4.matcher.hostAliases` | Use this parameter to inject hosts and IP addresses into the pod’s hosts file. |
| `scannerV4.matcher.resources.limits` | Use this parameter to override the default resource limits for the Scanner V4 Matcher. |
| `scannerV4.matcher.resources.requests` | Use this parameter to override the default resource requests for the Scanner V4 Matcher. |
| `scannerV4.matcher.scaling.autoScaling` | When enabled, the number of Scanner V4 Matcher replicas is managed dynamically based on the load, within the limits specified. |
| `scannerV4.matcher.scaling.maxReplicas` | Specifies the maximum replicas to be used in the Scanner V4 Matcher autoscaling configuration. |
| `scannerV4.matcher.scaling.minReplicas` | Specifies the minimum replicas to be used in the Scanner V4 Matcher autoscaling configuration. |
| `scannerV4.matcher.scaling.replicas` | When autoscaling is disabled for the Scanner V4 Matcher, the number of replicas is always configured to match this value. |
| `scannerV4.monitoring.exposeEndpoint` | Configures a monitoring endpoint for Scanner V4. The monitoring endpoint allows other services to collect metrics from Scanner V4, provided in a Prometheus-compatible format. Use `Enabled` to expose the monitoring endpoint. When you enable monitoring, RHACS creates a new service, `monitoring`, with port 9090, and a network policy allowing inbound connections to the port. By default, this is not enabled. |
| `scannerV4.scannerComponent` | If this setting is not specified, Scanner V4 is enabled for new installations, by default. For updates from an earlier release, Scanner V4 will not be enabled in the upgrade by default, if it was not previously enabled. To disable Scanner V4, set to `Disabled`. Disabling Scanner V4 negatively impacts the ability of RHACS to provide thorough and accurate scanning results. |

<a id="general-and-miscellaneous-settings_install-central-config-options-ocp"></a>

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
<td style="text-align: left;"><p>Advanced settings to configure environment variables. Use this to set custom environment variables for Central components.</p>
<p>For example, you can set <code>ROX_REPORT_MAX_ROWS</code> to increase the row limit for vulnerability reports from the default value of 1,000,000 rows.</p>
<p>For more information, see "Configuring the vulnerability report row limit".</p></td>
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
<li><p>If you configure specific <code>nodeSelector</code> settings for individual components, such as <code>central.nodeSelector</code> or <code>central.db.nodeSelector</code>, those settings override the global values defined in <code>customize.deploymentDefaults.nodeSelector</code>.</p></li>
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
<li><p>If you configure specific <code>tolerations</code> settings for individual components, such as <code>central.tolerations</code> or <code>central.db.tolerations</code>, those settings override the global values defined in <code>customize.deploymentDefaults.tolerations</code>.</p></li>
<li><p>You can use this setting to define global node selectors and tolerations that are automatically inherited by all resources to reduce repetitive configuration and simplify scheduling.</p></li>
</ul>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>egress.connectivityPolicy</code></p></td>
<td style="text-align: left;"><p>Configures whether RHACS should run in online or offline mode. In offline mode, automatic updates of vulnerability definitions and kernel modules are disabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>misc.createSCCs</code></p></td>
<td style="text-align: left;"><p>Specify <code>true</code> to create <code>SecurityContextConstraints</code> (SCCs) for Central. Setting to <code>true</code> might cause issues in some environments.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>monitoring.openshift.enabled</code></p></td>
<td style="text-align: left;"><p>If you set this option to <code>false</code>, Red Hat Advanced Cluster Security for Kubernetes will not set up Red Hat OpenShift monitoring. Defaults to <code>true</code> on Red Hat OpenShift 4.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>network.policies</code></p></td>
<td style="text-align: left;"><p>To provide security at the network level, RHACS creates default <code>NetworkPolicy</code> resources in the namespace where Central is installed. These network policies allow ingress to specific components on specific ports. If you do not want RHACS to create these policies, set this parameter to <code>Disabled</code>. The default value is <code>Enabled</code>.</p>
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
<td style="text-align: left;"><p>Additional Trusted CA certificates for the secured cluster to trust. These certificates are typically used when integrating with services using a private certificate authority.</p></td>
</tr>
</tbody>
</table>

<div>

<div class="title">

Additional resources

</div>

- [Configuring the vulnerability report row limit](../../operating/manage-vulnerabilities/vulnerability-reporting.md#configure-vulnerability-report-row-limit_vulnerability-reporting)

</div>

<a id="customize-installation-operator-overlays_install-central-config-options-ocp"></a>

# Customizing the installation using the Operator with overlays

Learn how to tailor the installation of RHACS using the Operator method with overlays.

<a id="overlays_install-central-config-options-ocp"></a>

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

<a id="adding-an-overlay_install-central-config-options-ocp"></a>

### Adding an overlay

For customizations, you can add overlays to `Central` or `SecuredCluster` custom resources. Use the OpenShift CLI (`oc`) or the OpenShift Container Platform web console for modifications.

If overlays do not take effect as expected, check the RHACS Operator logs for any syntax errors or issues logged.

<a id="examples_install-central-config-options-ocp"></a>

## Overlay examples

<a id="adding-eks-role-arn-annotation_install-central-config-options-ocp"></a>

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

<a id="adding-an-environment-variable-to-a-deployment_install-central-config-options-ocp"></a>

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

<a id="adding-an-ingress-to-a-network-policy_install-central-config-options-ocp"></a>

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

<a id="changing-configmap-data_install-central-config-options-ocp"></a>

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

<a id="adding-a-container-to-a-deployment_install-central-config-options-ocp"></a>

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

<div>

<div class="title">

Additional resources

</div>

- [Connection Strings - PostgreSQL Docs](https://www.postgresql.org/docs/15/libpq-connect.html#LIBPQ-CONNSTRING)

- [Parameter Interaction via the Configuration File - PostgreSQL Docs](https://www.postgresql.org/docs/15/config-setting.html#CONFIG-SETTING-CONFIGURATION-FILE)

- [The pg_hba.conf File - PostgreSQL Docs](https://www.postgresql.org/docs/15/auth-pg-hba-conf.html)

</div>
