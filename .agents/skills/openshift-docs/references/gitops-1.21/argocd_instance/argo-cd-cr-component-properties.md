<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The `Argo CD` custom resource is a Kubernetes Custom Resource (CRD) that describes the desired state for a given Argo CD cluster and allows you to configure the components which make up an Argo CD cluster.

# Argo CD custom resource properties

The Argo CD Custom Resource consists of the following properties:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Properties</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>aggregatedClusterRoles</code></p></td>
<td style="text-align: left;"><p>Use aggregated cluster roles for the Argo CD Application Controller component of a cluster-scoped instance.</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>applicationInstanceLabelKey</code></p></td>
<td style="text-align: left;"><p>The <code>metadata.label</code> key name where Argo CD injects the app name as a tracking label.</p></td>
<td style="text-align: left;"><p><code>app.kubernetes.io/instance</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>applicationSet</code></p></td>
<td style="text-align: left;"><p>The ApplicationSet Controller configuration options.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>annotations</code> - List of custom annotations to add to pods deployed by the Operator. This field is optional.</p></li>
<li><p><code>enabled</code> - The flag to use to enable the ApplicationSet Controller during the Argo CD installation.</p></li>
<li><p><code>env</code> - Specify the environment for ApplicationSet Controller pods.</p></li>
<li><p><code>extraCommandArgs</code> - List of additional arguments added to the existing arguments set by the Operator for the <code>ApplicationSet</code> workload.</p></li>
<li><p><code>image</code> - The container image for the ApplicationSet Controller. This property overrides the <code>ARGOCD_APPLICATIONSET_IMAGE</code> environment variable.</p></li>
<li><p><code>labels</code> - List of custom labels to add to pods deployed by the Operator. This field is optional.</p></li>
<li><p><code>logLevel</code> - The log level used by the Argo CD Application Controller component. Valid options are <code>debug</code>, <code>info</code>, <code>error</code>, and <code>warn</code>.</p></li>
<li><p><code>logFormat</code> - The log format used by the Argo CD Application Controller component. Valid options are <code>text</code> and <code>json</code>.</p></li>
<li><p><code>parallelismLimit</code> - The kubectl parallelism limit to set for the controller (the <code>--kubectl-parallelism-limit</code> flag).</p></li>
<li><p><code>resources</code> - The container compute resources.</p></li>
<li><p><code>scmProviders</code> - The URLs of the allowed Source Code Manager (SCM) providers.</p></li>
<li><p><code>scmRootCAConfigMap</code> - The name of the config map that stores the Gitlab SCM Provider’s TLS certificate that will be mounted on the Application Set Controller at the "/app/tls/scm/cert" path.</p></li>
<li><p><code>sourceNamespaces</code> - The list of non-control plane namespaces for creating and managing Argo CD <code>ApplicationSet</code> resources in target namespaces.</p></li>
<li><p><code>version</code> - The tag to use with the <code>applicationSet</code> container image.</p></li>
<li><p><code>volumes</code> - List of addition volumes configured for the Argo CD <code>ApplicationSet</code> Controller component. This field is optional.</p></li>
<li><p><code>volumeMounts</code> - List of addition volume mounts configured for the Argo CD <code>ApplicationSet</code> Controller component. This field is optional.</p></li>
<li><p><code>webhookServer</code> - Defines the available options for the ApplicationSet webhook server.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>banner</code></p></td>
<td style="text-align: left;"><p>Adds a UI banner message.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>banner.content</code> - The banner message content. This content is required if a banner is displayed.</p></li>
<li><p><code>banner.url</code> - An optional banner message link URL.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>configManagementPlugins</code></p></td>
<td style="text-align: left;"><p>Adds a configuration management plugin.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>controller</code></p></td>
<td style="text-align: left;"><p>Argo CD Application Controller options.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>annotations</code> - List of custom annotations to add to pods deployed by the Operator. This field is optional.</p></li>
<li><p><code>appSync</code> - AppSync is used to control the sync frequency of Argo CD applications.</p></li>
<li><p><code>env</code> - Environment to set for the application controller workloads.</p></li>
<li><p><code>extraCommandArgs</code> - List of arguments added to the existing arguments set by the Operator.</p></li>
<li><p><code>initContainers</code> - List of <code>init</code> containers for the ArgoCD Application Controller component. This field is optional.</p></li>
<li><p><code>labels</code> - List of custom labels to add to pods deployed by the Operator. This field is optional.</p></li>
<li><p><code>logLevel</code> - The log level used by the Argo CD Application Controller component. Valid options are <code>debug</code>, <code>info</code>, <code>error</code>, and <code>warn</code>.</p></li>
<li><p><code>processors.operation</code> - The number of operation processors.</p></li>
<li><p><code>processors.status</code> - The number of status processors.</p></li>
<li><p><code>resources</code> - The container compute resources.</p></li>
<li><p><code>sidecarContainers</code> - List of <code>sidecar</code> containers for the ArgoCD Application Controller component. This field is optional.</p></li>
<li><p><code>sharding.enabled</code> - Enable sharding on the Argo CD Application Controller component. Use this property to manage a large number of clusters and relieve memory pressure on the controller component.</p></li>
<li><p><code>sharding.replicas</code> - The number of replicas that are used to support sharding of the Argo CD Application Controller.</p></li>
<li><p><code>sharding.dynamicScalingEnabled</code> - Enables the dynamic scaling of the Argo CD Application Controller component. Use this property if you want the Operator to scale the number of replicas based on the number of clusters the controller component is managing. If you set this property to <code>true</code>, it overrides the configuration of the <code>sharding.enabled</code> and <code>sharding.replicas</code> properties.</p></li>
<li><p><code>sharding.minShards</code> - The minimum number of Argo CD Application Controller replicas.</p></li>
<li><p><code>sharding.maxShards</code> - The maximum number of Argo CD Application Controller replicas.</p></li>
<li><p><code>sharding.clustersPerShard</code> - The number of clusters that need to be managed by each shard. When the replica count reaches the <code>maxShards</code>, the shards manage more than one cluster.</p></li>
<li><p><code>volumes</code> - List of addition volumes configured for the Argo CD Application Controller component. This field is optional.</p></li>
<li><p><code>volumeMounts</code> - List of addition volume mounts configured for the Argo CD Application Controller component. This field is optional.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>disableAdmin</code></p></td>
<td style="text-align: left;"><p>Disables the built-in admin user.</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>defaultClusterScopedRoleDisabled</code></p></td>
<td style="text-align: left;"><p>Disables the creation of default cluster roles for a cluster-scoped instance.</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>extraConfig</code></p></td>
<td style="text-align: left;"><p>Add any supplementary Argo CD settings to the <code>argocd-cm</code> config map that cannot be configured directly within the Argo CD custom resource.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gaTrackingID</code></p></td>
<td style="text-align: left;"><p>Use a Google Analytics tracking ID.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gaAnonymizeUsers</code></p></td>
<td style="text-align: left;"><p>Enable hashed usernames sent to Google Analytics.</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ha</code></p></td>
<td style="text-align: left;"><p>High-availability options.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>enabled</code> - Toggle high-availability support globally for Argo CD.</p></li>
<li><p><code>redisProxyImage</code> - The Redis HAProxy container image. This property overrides the <code>ARGOCD_REDIS_HA_PROXY_IMAGE</code> environment variable.</p></li>
<li><p><code>redisProxyVersion</code> - The tag to use for the Redis HAProxy container image.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>helpChatURL</code></p></td>
<td style="text-align: left;"><p>URL for getting chat help (this is typically your Slack channel for support).</p></td>
<td style="text-align: left;"><p><code>https://mycorp.slack.com/argo-cd</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>helpChatText</code></p></td>
<td style="text-align: left;"><p>The text that appears in a text box for getting chat help.</p></td>
<td style="text-align: left;"><p><code>Chat now!</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image</code></p></td>
<td style="text-align: left;"><p>The container image for all Argo CD components. This overrides the <code>ARGOCD_IMAGE</code> environment variable.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>import</code></p></td>
<td style="text-align: left;"><p>Import configuration options for Argo CD.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>name</code> - The name of an <code>ArgoCDExport</code> resource from which data can be imported.</p></li>
<li><p><code>namespace</code> - The namespace for the <code>ArgoCDExport</code> resource referenced by <code>name</code> field. If this field is not set, the namespace of <code>ArgoCDExport</code> resource is set to the same namespace as Argo CD by default.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ingress</code></p></td>
<td style="text-align: left;"><p>Ingress configuration options.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>initialSSHKnownHosts</code></p></td>
<td style="text-align: left;"><p>Defines the initial SSH Known Hosts data for Argo CD to use at cluster creation to connect to Git repositories through SSH.</p></td>
<td style="text-align: left;"><p><code>default_Argo_CD_Known_Hosts</code></p></td>
<td style="text-align: left;"><ul>
<li><p><code>excludedefaulthosts</code> - Indicates whether you want to add the default list of SSH Known Hosts provided by Argo CD.</p></li>
<li><p><code>keys</code> - Describes a custom set of SSH Known Hosts that you want to incorporate into your Argo CD server.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kustomizeBuildOptions</code></p></td>
<td style="text-align: left;"><p>The build options and parameters to use with <code>kustomize build</code>.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kustomizeVersions</code></p></td>
<td style="text-align: left;"><p>Defines a list of <code>Kustomize</code> versions that are configured in the Argo CD repo server container image.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>path</code> - The path of the <code>Kustomize</code> version in the file system of the Argo CD repo server container image.</p></li>
<li><p><code>version</code> - The <code>Kustomize</code> version in the <code>vX.Y.Z</code> format configured in the Argo CD repo server container image.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>monitoring</code></p></td>
<td style="text-align: left;"><p>Defines the workload status monitoring configuration for your instance.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>disableMetrics</code> - Configure this field to enable or disable the collection of metrics for your instance.</p></li>
<li><p><code>enabled</code> - Indicates whether the workload status monitoring is enabled for your instance.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>notifications</code></p></td>
<td style="text-align: left;"><p>Notifications Controller configuration options.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>enabled</code> - The toggle to start the Notifications Controller.</p></li>
<li><p><code>env</code> - The environment to set for the Notifications Controller workloads.</p></li>
<li><p><code>image</code> - The container image for all Argo CD components. This property overrides the <code>ARGOCD_IMAGE</code> environment variable.</p></li>
<li><p><code>logLevel</code> - The log level used by the Argo CD Application Controller component. Valid options are <code>debug</code>, <code>info</code>, <code>error</code>, and <code>warn</code>.</p></li>
<li><p><code>replicas</code> - The number of replicas to be run for the Notifications Controller.</p></li>
<li><p><code>resources</code> - The container compute resources.</p></li>
<li><p><code>version</code> - The tag to use with the Notifications container image.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodePlacement</code></p></td>
<td style="text-align: left;"><p>Defines <code>NodeSelectors</code> and <code>Tolerations</code> for Argo CD workloads.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>nodeSelector</code> - A map of key-value pairs for node selection.</p></li>
<li><p><code>tolerations</code> - Tolerations allow pods to create a schedule for nodes with matching taints.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>oidcConfig</code></p></td>
<td style="text-align: left;"><p>The OIDC configuration as an alternative to Dex.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prometheus</code></p></td>
<td style="text-align: left;"><p>Prometheus configuration options.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>enabled</code> - Toggle Prometheus support globally for Argo CD.</p></li>
<li><p><code>host</code> - The hostname to use for <code>Ingress</code> or <code>Route</code> resources.</p></li>
<li><p><code>ingress</code> - Toggles ingress for Prometheus.</p></li>
<li><p><code>route</code> - Route configuration options.</p></li>
<li><p><code>size</code> - The replica count for the Prometheus <code>StatefulSet</code>.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rbac</code></p></td>
<td style="text-align: left;"><p>RBAC configuration options.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>defaultPolicy</code> - The <code>policy.default</code> property in the <code>argocd-rbac-cm</code> config map. The name of the default role that Argo CD falls back to when authorizing API requests.</p></li>
<li><p><code>policy</code> - The <code>policy.csv</code> property in the <code>argocd-rbac-cm</code> config map. This property includes CSV data about user-defined RBAC policies and role definitions.</p></li>
<li><p><code>policyMatcher</code> - The <code>policy.matchMode</code> property in the <code>argocd-rbac-cm</code> config map. This property has two options: 'glob' for glob matcher and 'regex' for regex matcher.</p></li>
<li><p><code>scopes</code> - The scopes property in the <code>argocd-rbac-cm</code> config map. Controls which OIDC scopes to examine during RBAC enforcement, in addition to sub scope.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>redis</code></p></td>
<td style="text-align: left;"><p>Redis configuration options.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>autotls</code> - Use the provider to create the Redis server’s TLS certificate. Only the <code>openshift</code> value is currently available.</p></li>
<li><p><code>disableTLSVerification</code> - Defines whether the Redis server should be accessed using strict TLS validation.</p></li>
<li><p><code>image</code> - The container image for Redis. This overrides the <code>ARGOCD_REDIS_IMAGE</code> environment variable.</p></li>
<li><p><code>resources</code> - The container compute resources.</p></li>
<li><p><code>version</code> - The tag to use with the Redis container image.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceActions</code></p></td>
<td style="text-align: left;"><p>Customize resource action behavior.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceExclusions</code></p></td>
<td style="text-align: left;"><p>Completely ignore entire classes of resource group.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceInclusions</code></p></td>
<td style="text-align: left;"><p>The configuration to identify which resource group/kinds are applied.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceHealthChecks</code></p></td>
<td style="text-align: left;"><p>Customize resource health check behavior.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceIgnoreDifferences</code></p></td>
<td style="text-align: left;"><p>Customize resource ignore difference behavior.</p></td>
<td style="text-align: left;"><p><em>empty</em></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceTrackingMethod</code></p></td>
<td style="text-align: left;"><p>The field used by Argo CD to monitor its managed resources.</p></td>
<td style="text-align: left;"><p><code>label</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>server</code></p></td>
<td style="text-align: left;"><p>Argo CD Server configuration options.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>annotations</code> - List of custom annotations to add to pods deployed by the Operator. This field is optional.</p></li>
<li><p><code>autoscale</code> - Server autoscale configuration options.</p></li>
<li><p><code>env</code> - Environment to set for the server workloads.</p></li>
<li><p><code>enabled</code> - The flag to enable Argo CD server during the Argo CD installation.</p></li>
<li><p><code>enableRolloutsUI</code> - When the parameter is set to <code>true</code>, the parameter enables the Argo Rollouts UI extension in Argo CD. The default value is set to <code>false</code>.</p></li>
<li><p><code>extraCommandArgs</code> - List of arguments added to the existing arguments set by the Operator.</p></li>
<li><p><code>grpc</code> - gRPC configuration options.</p></li>
<li><p><code>host</code> - The hostname used for <code>Ingress</code> or <code>Route</code> resources.</p></li>
<li><p><code>initContainers</code> - List of <code>init</code> containers for the Argo CD Application Controller component. This field is optional.</p></li>
<li><p><code>ingress</code> - Ingress configuration for the Argo CD server component.</p></li>
<li><p><code>insecure</code> - Toggles the insecure flag for Argo CD server.</p></li>
<li><p><code>labels</code> - List of custom labels to add to pods deployed by the Operator. This field is optional.</p></li>
<li><p><code>logLevel</code> - The log level to be used by the Argo CD server component. Valid options are <code>debug</code>, <code>info</code>, <code>error</code>, and <code>warn</code>.</p></li>
<li><p><code>logFormat</code> - The log format used by the Argo CD server component. Valid options are <code>text</code> and <code>json</code>.</p></li>
<li><p><code>resources</code> - The container compute resources.</p></li>
<li><p><code>replicas</code> - The number of replicas for the Argo CD server. Must be greater than or equal to <code>0</code>. If <code>autoscale</code> is enabled, <code>replicas</code> is ignored.</p></li>
<li><p><code>route</code> - Route configuration options.</p></li>
<li><p><code>service.Type</code> - The <code>serviceType</code> used for the service resource.</p></li>
<li><p><code>sidecarContainers</code> - List of <code>sidecar</code> containers for the Argo CD Application Controller component. This field is optional.</p></li>
<li><p><code>volumes</code> - List of addition volumes configured for the Argo CD Application Controller component. This field is optional.</p></li>
<li><p><code>volumeMounts</code> - List of addition volume mounts configured for the Argo CD Application Controller component. This field is optional.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sourceNamespaces</code></p></td>
<td style="text-align: left;"><p>Specifies the namespaces within which you can create application resources.</p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sso</code></p></td>
<td style="text-align: left;"><p>Single Sign-on options.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>dex</code> - Configuration options for Dex SSO provider.</p></li>
<li><p><code>provider</code> - The name of the provider used to configure Single Sign-on. Currently, the supported option is Dex.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>statusBadgeEnabled</code></p></td>
<td style="text-align: left;"><p>Enable application status badge.</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tls</code></p></td>
<td style="text-align: left;"><p>TLS configuration options.</p></td>
<td style="text-align: left;"><p><em>object</em></p></td>
<td style="text-align: left;"><ul>
<li><p><code>ca.configMapName</code> - The name of the <code>ConfigMap</code> which contains the CA certificate.</p></li>
<li><p><code>ca.secretName</code> - The name of the secret which contains the CA certificate and key.</p></li>
<li><p><code>initialCerts</code> - Initial set of certificates in the <code>argocd-tls-certs-cm</code> config map for connecting Git repositories through HTTPS.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>usersAnonymousEnabled</code></p></td>
<td style="text-align: left;"><p>Enables anonymous user access.</p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>version</code></p></td>
<td style="text-align: left;"><p>The tag to use with the container image for all Argo CD components.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Latest GitOps Version</p></td>
</tr>
</tbody>
</table>

# Repo server properties

The following properties are available for configuring the repo server component:

| Name | Default | Description |
|----|----|----|
| `annotations` | *empty* | List of custom annotations to add to pods deployed by the Operator. This field is optional. |
| `autotls` | `""` | Provider to use to set up TLS for the repo-server’s gRPC TLS certificate. Currently, only the `openshift` value is acceptable. |
| `env` | *empty* | The environment to set for the Repo server workloads. |
| `enabled` | *empty* | Flag that enables the Repo server during Argo CD installation. |
| `execTimeout` | `180` | Execution timeout in seconds for rendering tools, for example, Helm or Kustomize. |
| `extraRepoCommandArgs` | `empty` | Passes command-line arguments to the Repo server workload. The command-line arguments are added to the list of arguments set by the Operator. |
| `initContainers` | `empty` | The number of `init` containers in the Argo CD Application Controller component. This field is optional. |
| `image` | `registry.redhat.io` | The container image for Argo CD Repo server. This property overrides the `ARGOCD_REPOSERVER_IMAGE` environment variable. |
| `labels` | `empty` | List of custom labels to add to pods deployed by the Operator. This field is optional. |
| `logLevel` | `info` | The log level used by the Argo CD Repo server. Valid options are `debug`, `info`, `error`, and `warn`. |
| `logFormat` | `text` | The log format to be used by the Argo CD repo server. Valid options are `text` and `json`. |
| `mountsatoken` | `false` | Defines whether the `serviceaccount` token should be mounted to the repo-server pod. |
| `remote` | *empty* | Specifies the remote URL of the Repo server container. |
| `replicas` | *empty* | The number of replicas for the Argo CD Repo server. Must be greater than or equal to `0`. |
| `resources` | *empty* | The container compute resources. |
| `serviceaccount` | `""` | The name of the `serviceaccount` to use with the repo-server pod. |
| `sidecarContainers` | *empty* | The number of `sidecar` containers in the Argo CD Application Controller component. This field is optional. |
| `systemCAtrust` | `empty` | Enables the use of custom CA certificates so that the repo server and its plugins can trust external source hosting sites. |
| `verifytls` | `false` | Defines whether to enforce strict TLS checking on all components when communicating with repo server. |
| `version` | same as `.spec.Version` | The tag to use with the Argo CD Repo server. |
| `volumes` | *empty* | Configures additional volumes used for the Repo server deployment. This field is optional. |
| `volumeMounts` | *empty* | Configures additional volume mounts used for the Repo server deployment. This field is optional. |

## Configure TLS trust for the repo server

You can configure the repo server to trust additional certificate authorities (CAs). Inject custom TLS certificates into the repo server container and its Config Management Plugin sidecar containers.

The certificates can be provided through Kubernetes secrets and config maps.

The following example shows how to configure additional trusted certificates in the `Argo CD` custom resource.

``` yaml
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: repo
spec:
  repo:
    systemCATrust:
      secrets:
        - name: my-local-cert-secret
          items:
            - key: key-name-in-the-secret-object
              path: desired-file-name-of-the-certificate.crt
      configMaps:
        - name: my-local-cert-cm
          items: []
```

where:

- `spec.repo`:: Configures settings for the Argo CD repo server component.

- `spec.repo.systemCATrust`:: Defines additional certificate authorities that the repo server trusts.

- `spec.repo.systemCATrust.secrets`:: Specifies kubernetes secrets that contain custom CA certificates.

- `spec.repo.systemCATrust.configMaps`:: References config maps containing CA certificates to trust.

Consider the following behavior and configuration details when using this feature:

- Certificates are not pinned to individual hosts, allowing the use of CA or wildcard certificates.

- The Operator configures the injected certificates inside the container. This configuration supports advanced plugin workflows. For example:

  - Kustomize can invoke Helm charts hosted on different repositories.

  - Kustomize can retrieve resources from other repositories or sources over HTTPS.

  - Config Management Plugins can use TLS-enabled tools in the container image while keeping TLS verification enabled.

Certificates from secrets or config maps must exist in the same namespace as the Argo CD instance. Use the `items` field to map specific keys. Omit the `items` field to include all keys.

You can mark a trust source as optional. If a required source is missing, the deployment fails.

By default, user-provided certificates are merged with the certificates in the container image. To disable this behavior, set `spec.repo.systemCATrust.dropImageCertificates` to `true`.

# Enabling notifications with an Argo CD instance

With Argo CD notifications, you can send notifications to external services when events occur in your Argo CD instance. For example, you can send notifications to Slack or email when a sync operation fails. By default, notifications are disabled in Argo CD instances.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with `cluster-admin` privileges and are logged in to the web console.

- You have installed the Red Hat OpenShift GitOps Operator on your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the **Operators** → **Installed Operators** page.

2.  From the list of **Installed Operators**, select the Red Hat OpenShift GitOps Operator, and then click the **ArgoCD** tab.

3.  Select the Argo CD instance name you want to enable notifications. For example, `openshift-gitops`.

4.  Click the **YAML** tab, and then edit and set the `spec.notifications.enabled` parameter to `true`:

    **Example:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
    spec:
      notifications:
        enabled: true
    #....
    ```

5.  Click **Save**.

    > [!TIP]
    > Alternatively, you can enable notifications by using the `oc patch` command in the OpenShift CLI. For example:
    >
    > ``` terminal
    > oc patch argocd openshift-gitops -n openshift-gitops --type merge --patch '{"spec": {"notifications": {"enabled": true}}}'
    > ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Argo CD notifications controller](https://argo-cd.readthedocs.io/en/stable/operator-manual/notifications/)

</div>

# Enabling Config Management Plugins in an Argo CD CR

Argo CD provides support for Helm, Jsonnet, and Kustomize as built-in config management tools. To use a different config management tool, or to enable features not provided by the built-in config management tools, you can use the Config Management Plugin (CMP).

In Argo CD, the CMP is specified as a sidecar container for the Argo CD repo server container. For more information, see "Config Management Plugins".

In the Red Hat OpenShift GitOps Operator, you can configure the Config Management plugin as a sidecar container in the Argo CD custom resource (CR). When you configure the sidecar container, you either specify an off-the-shelf or a custom-built container image. If you do not specify an image, the system uses the same image as the repo server for the plugin.

To configure a sidecar container in the Red Hat OpenShift GitOps Operator, add the `.spec.repo.sidecarContainers` key in the Argo CD CR.

**Example Config Management Plugin configuration:**

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
 name: <my_argocd>
spec:
 repo:
   sidecarContainers:
     - name: <my_cmp>
       command: [/var/run/argocd/argocd-cmp-server]
       image: <my_image>
       securityContext:
         runAsNonRoot: <true>
         runAsUser:
       volumeMounts:
         - mountPath: /var/run/argocd
           name: <var_files>
         - mountPath: /home/argocd/cmp-server/plugins
           name: plugins
         - mountPath: /tmp
           name: tmp
         - mountPath: /home/argocd/cmp-server/config/plugin.yaml
           subPath: <plugin.yaml>
           name: <cmp_plugin>
```

where:

`metadata.name`
Specifies the name of an Argo CD CR instance.

`spec.repo.sidecarContainers.name`
Specifies the name of a sidecar container used in the repo server.

`spec.repo.sidecarContainers.volumeMounts`
Specifies the name of volume mounts used in the repo server.

# NotificationsConfiguration custom resource properties

The `NotificationsConfiguration` resource is a Kubernetes custom resource (CR) that manages notifications in a Kubernetes cluster. In Red Hat OpenShift GitOps, you can add templates, triggers, services, and subscription resources to an Argo CD `Notifications` config map by using the `NotificationsConfiguration` CR.

When you create a cluster in Red Hat OpenShift GitOps with notifications enabled, a `NotificationsConfiguration` CR is created by default with the name `default-notifications-configuration`.

Any change made in the existing configuration of the `NotificationsConfiguration` CR is replicated in the Argo CD `Notifications` config map. For example, if the user adds trigger configuration in the `NotificationsConfiguration` resource, this configuration is read, processed, and updated in the Argo CD `Notifications` config map.

> [!IMPORTANT]
> Any configuration changes must be updated in the `default-notifications-configuration` CR. Custom resources created by the users for `NotificationsConfiguration` resource are not supported.
>
> Any modification to the Argo CD `argocd-notifications-cm` config map is overridden by the changes made in the `NotificationsConfiguration` CR.

| **Properties** | **Default** | **Description** |
|----|----|----|
| Templates | `<empty>` | Templates are used to generate the notification template message. |
| Triggers | `<empty>` | Triggers are used to define the condition when a notification is sent to the user and the list of templates required to generate the message. |
| Services | `<empty>` | Services are used to deliver a message. |
| Subscriptions | `<empty>` | Subscriptions contain centrally-managed global application subscriptions. |

`NotificationsConfiguration` custom resource properties

The following examples define how to add templates, triggers, services, and subscription resources to the Argo CD `argocd-notification-cm` config map by using the `default-notifications-configuration` custom resource.

**Example for `templates`:**

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: NotificationsConfiguration
metadata:
 name: default-notifications-configuration
spec:
 templates:
  template.my-custom-template: |
    message: |
     Application details: {{.context.argocdUrl}}/applications/{{.app.metadata.name}}.
```

where:

`metadata.name`
Specifies the default name of the `NotificationsConfiguration` CR in a cluster.

`spec.template.my-custom-template`
Specifies an example custom template configuration for the `NotificationsConfiguration` CR.

**Example for `triggers`:**

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: NotificationsConfiguration
metadata:
 name: default-notifications-configuration
spec:
 triggers:
  trigger.on-sync-status-unknown: |
   - when: app.status.sync.status == 'Unknown'
   send: [my-custom-template]
```

where:

`metadata.name`
Specifies the default name of the `NotificationsConfiguration` CR in a cluster.

`spec.trigger.on-sync-status-unknown`
Specifies an example custom trigger configuration for the `NotificationsConfiguration` CR.

**Example for `services`:**

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: NotificationsConfiguration
metadata:
 name: default-notifications-configuration
spec:
 services:
  service.slack: |
    token: $slack-token
    username: <override-username> # optional username
    icon: <override-icon> # optional icon for the message (supports both emoji and url notation)
```

where:

`metadata.name`
Specifies the default name of the `NotificationsConfiguration` CR in a cluster.

`spec.service.slack`
Specifies an example custom service configuration for the `NotificationsConfiguration` CR.

**Example for `subscriptions`:**

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: NotificationsConfiguration
metadata:
 name: default-notifications-configuration
spec:
 subscriptions:
  subscriptions: |
    # subscription for on-sync-status-unknown trigger notifications
    - recipients:
      - slack:test2
      - email:test@gmail.com
      triggers:
      - on-sync-status-unknown
    # subscription restricted to applications with matching labels only
    - recipients:
      - slack:test3
      selector: test=true
      triggers:
      - on-sync-status-unknown
```

where:

`metadata.name`
Specifies the default name of the `NotificationsConfiguration` CR in a cluster.

`spec.subscriptions`
Specifies an example custom subscription configuration for the `NotificationsConfiguration` CR.

You can configure the `NotificationsConfiguration` CR by using the OpenShift Container Platform web console or the CLI (`oc`).

## Configuring the NotificationsConfiguration CR by using the web console

You can configure the `NotificationsConfiguration` custom resource (CR) by using the web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with `cluster-admin` privileges and are logged in to the web console.

- You have installed the Red Hat OpenShift GitOps Operator on your cluster.

- You have enabled notifications for the Argo CD instance. For more information, see "Enabling notifications with an Argo CD instance".

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the OpenShift Container Platform web console, expand **Operators** → **Installed Operators**.

2.  From the list of **Installed Operators**, select the Red Hat OpenShift GitOps Operator, and then click on the **NotificationsConfiguration** tab.

3.  On the **NotificationsConfigurations** page, click `default-notifications-configuration`.

4.  On the **default-notifications-configuration** page, click **YAML** and add the configuration for any supported resources such as `templates`, `triggers`, `services`, and `subscriptions`. For example, under `templates` in the code, add the following sample configuration:

    **Example template configuration:**

    ``` yaml
      template.my-custom-template: |
        message: |
        Application details: {{.context.argocdUrl}}/applications/{{.app.metadata.name}}.
    ```

5.  Click **Save**.

6.  Verify that the configuration changes made in the `NotificationsConfiguration` CR are reflected in the `argocd-notifications-cm` config map:

    1.  Go to **Workloads** → **ConfigMaps**.

    2.  Click **argocd-notifications-cm** and select the **YAML** tab.

    3.  Scroll through the page in the **YAML** tab to verify the sample configuration added for the supported resources.

</div>

## Configuring the NotificationsConfiguration CR by using the CLI

You can configure the `NotificationsConfiguration` custom resource (CR) by using the CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with `cluster-admin` privileges.

- You have installed the Red Hat OpenShift GitOps Operator on your cluster.

- You have enabled notifications for the Argo CD instance. For more information, see "Enabling notifications with an Argo CD instance".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the default `NotificationsConfiguration` CR in the cluster by running the following command:

    ``` terminal
    $ oc edit notificationsconfiguration default-notifications-configuration -n <namespace>
    ```

    where:

    `default-notifications-configuration`
    Specifies the name of the default `NotificationsConfiguration` CR.

    `<namespace>`
    Specifies the name of the namespace.

2.  Under the `templates` section of the CR, add a configuration similar to the following example:

    **Example template configuration:**

    ``` yaml
      template.my-custom-template: |
        message: |
        Application details: {{.context.argocdUrl}}/applications/{{.app.metadata.name}}.
    ```

3.  Verify the contents of the `argocd-notifications-cm` config map by running the following command:

    ``` terminal
    $ oc edit cm argocd-notifications-cm -n <namespace>
    ```

    The changes made in the existing configuration of the `NotificationsConfiguration` CR are reflected in the `argocd-notifications-cm` config map.

</div>

# Configuring notifications in any Namespace

By default, Argo CD manages notification configuration only within the control plane namespace. With Red Hat OpenShift GitOps Operator, cluster administrators can enable teams to manage notification settings for their applications from additional namespaces.

To enable this functionality, configure the target namespaces in the Argo CD custom resource (CR). The Red Hat OpenShift GitOps Operator reconciles the corresponding notification resources only for namespaces that are explicitly defined in the ArgoCD CR.

> [!NOTE]
> To enable notification configuration in a namespace, you must add the namespace to the following fields in the Argo CD CR:
>
> - `.spec.sourceNamespaces`: Enables the `Apps in Any Namespace` feature for the Application controller.
>
> - `.spec.notifications.sourceNamespaces`: Allows the Notifications controller to read configuration from that namespace.
>
> If a namespace is not included in these fields, notification configuration for that namespace is not processed.

<div>

<div class="title">

Procedure

</div>

1.  List the ArgoCD CRs in the cluster:

    ``` terminal
    $ oc get argocd -A
    ```

2.  Edit the target ArgoCD CR:

    ``` terminal
    $ oc edit argocd <cr_name> -n <namespace>
    ```

3.  Under the `spec` section, add each target namespace to the `sourceNamespaces` and `notifications.sourceNamespaces` fields.

    The following example enables the `example-argocd` instance to manage applications and notification configurations in the `foo` namespace:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ArgoCD
    metadata:
      name: example-argocd
    spec:
      sourceNamespaces:
        - foo
      notifications:
        enabled: true
        sourceNamespaces:
          - foo
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the Argo CD instance recognizes the updated `sourceNamespaces` configuration by checking the settings in the Argo CD CR.

</div>

## Understanding configuration notifications behavior across namespaces

When the Configuring notifications in any namespace feature is enabled, the Red Hat OpenShift GitOps Operator performs additional actions to support delegated notification configuration. For each delegated namespace, the Red Hat OpenShift GitOps Operator automatically creates a `NotificationsConfiguration` custom resource (CR) named `default-notifications-configuration`. Application teams can update this CR to define or modify their notification settings.

The Notifications controller determines which configuration to apply by using the following resolution behavior:

- The controller first checks for the delegated `NotificationsConfiguration` CR or the corresponding config map (`argocd-notifications-cm`) and Secret (`argocd-notification-secret`) in the namespace of the application.

- If no delegated configuration is found, the controller falls back to the central configuration resources (ConfigMap and Secret) defined in the control plane namespace.

To enable this model, the Red Hat OpenShift GitOps Operator creates a `Role` and a `RoleBinding` in each delegated namespace, granting the Notifications controller permission to read `ConfigMaps` and `Secrets`. The Red Hat OpenShift GitOps Operator also applies the `argocd.argoproj.io/notifications-managed-by-cluster-argocd` label to each delegated namespace.

# Enabling annotation-based resource tracking in Argo CD

The Red Hat OpenShift GitOps Operator enhances multi-instance support by improving annotation-based resource tracking in Argo CD. Assign a unique installationID to each Argo CD instance to distinguish resources with identical application names, prevent conflicts and infinite sync loops, and enable multiple instances to operate safely in parallel.

You can perform the following actions by using the OpenShift Container Platform web console:

- Configure multiple Argo CD instances

- Configure annotation-based tracking by associating them with namespaces

- Verify deployments

<div class="note">

<div class="title">

</div>

- Each Argo CD instance must have a unique `installationID` to prevent resource tracking conflicts.

- Ensure that namespaces are labeled accurately because it allows each Argo CD instance to manage only the intended resources.

- If multiple instances have applications with the same name, set resource tracking to `annotation+label`.

- If issues arise, check the **Argo CD Application** status and logs in the OpenShift Container Platform web console.

</div>

## Configuring annotation-based tracking in multiple Argo CD instances

You can configure annotation-based tracking in multiple Argo CD instances.

> [!NOTE]
> This procedure uses the following example values:
>
> - `repoURL`: `https://github.com/redhat-developer/gitops-operator`
>
> - `server`: `https://kubernetes.default.svc`
>
> When you follow these steps, replace the example values with the actual values.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators**.

    - In the **Project** list, create or select the project where you want to install the user-defined Argo CD instance.

3.  Select **Red Hat OpenShift GitOps** from the installed Operators list and click the **Argo CD** tab.

4.  To create two Argo CD instances, click **Create ArgoCD** and create two YAML files similar to the following examples:

    **Example first Argo CD instance with an annotation label:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: argocd-instance-demo-1
      namespace: argocd-test-demo-1
    spec:
      installationID: "instance-demo-1"
      resourceTrackingMethod: "annotation+label"
    ```

    where:

    `metadata.name`
    Specifies the name of the first Argo CD instance.

    `metadata.namespace`
    Specifies the namespace used for the first Argo CD instance.

    `spec.installationID`
    Specifies the name of the `installationID` object for the first Argo CD instance.

    **Example second Argo CD instance with an annotation label:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: argocd-instance-demo-2
      namespace: argocd-test-demo-2
    spec:
      installationID: "instance-demo-2"
      resourceTrackingMethod: "annotation+label"
    ```

    where:

    `metadata.name`
    Specifies the name of the second Argo CD instance.

    `metadata.namespace`
    Specifies the namespace used for the second Argo CD instance.

    `spec.installationID`
    Specifies the name of the `installationID` object for the second Argo CD instance.

5.  Configure and label target namespaces to associate namespaces with their Argo CD instances.

    1.  Navigate to **Administration** → **Namespaces**.

    2.  Create namespaces for application deployments, `app-ns-1` and `app-ns-2`.

    3.  Associate each namespace with their respective Argo CD instance:

        1.  Associate the `app-ns-1` namespace with the `argocd-test-demo-1` Argo CD instance by running the following command:

            **Example command:**

            ``` terminal
            $ oc label namespace app-ns-1 argocd.argoproj.io/managed-by=argocd-test-demo-1
            ```

        2.  Associate the `app-ns-2` namespace with the `argocd-test-demo-2` Argo CD instance by running the following command:

            **Example command:**

            ``` terminal
            $ oc label namespace app-ns-2 argocd.argoproj.io/managed-by=argocd-test-demo-2
            ```

6.  Create two applications in Argo CD.

    1.  In the OpenShift Container Platform web console, go to **Operators** → **Installed Operators** → **OpenShift GitOps Operator**.

    2.  Select **Argo CD** and navigate to the **Applications** tab.

    3.  Click **Create Application**.

    4.  Enter the following YAML snippet to create two applications in Argo CD.

        **Example first application using Argo CD:**

        ``` yaml
        apiVersion: argoproj.io/v1alpha1
        kind: Application
        metadata:
          name: sprint-petclinic
          namespace: argocd-test-demo-1
        spec:
          project: default
          source:
            repoURL: https://github.com/redhat-developer/gitops-operator
            path: test/examples/nginx
            targetRevision: HEAD
          destination:
            server: https://kubernetes.default.svc
            namespace: app-ns-1
          syncPolicy:
            automated: {}
        ```

        where:

        `metadata.name`
        Specifies the name of the first application.

        `metadata.namespace`
        Specifies the namespace used for the first application.

        **Example second application using Argo CD:**

        ``` yaml
        apiVersion: argoproj.io/v1alpha1
        kind: Application
        metadata:
          name: sprint-petclinic
          namespace: argocd-test-demo-2
        spec:
          project: default
          source:
            repoURL: https://github.com/redhat-developer/gitops-operator
            path: test/examples/nginx
            targetRevision: HEAD
          destination:
            server: https://kubernetes.default.svc
            namespace: app-ns-2
          syncPolicy:
            automated: {}
        ```

        where:

        `metadata.name`
        Specifies the name of the second application that is created with the same name as the first application.

        `metadata.namespace`
        Specifies the namespace used for the second application.

</div>

<div>

<div class="title">

Verification

</div>

1.  Navigate to **Workloads** → **Pods** in the OpenShift Container Platform web console.

2.  Ensure that the pods for Argo CD instances `argocd-instance-demo-1` and `argocd-instance-demo-2` are running.

3.  Check the application synchronization status in the **Argo CD Applications** YAML tab.

4.  Navigate to the `argocd-cm` config map in `argocd-test-demo-1` and `argocd-test-demo-2` namespaces and verify that the `installationID` object is configured successfully.

</div>

# Additional resources

- [Installing a user-defined Argo CD instance](setting-up-argocd-instance.md#gitops-argo-cd-installation_setting-up-argocd-instance)

- [Config Management Plugins](https://argo-cd.readthedocs.io/en/stable/operator-manual/config-management-plugins/#config-management-plugins)
