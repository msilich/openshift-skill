<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
PodTemplate describes a template for creating copies of a predefined pod.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `template` | `object` | PodTemplateSpec describes the data a pod should have when created from a template |

## .template

Description
PodTemplateSpec describes the data a pod should have when created from a template

Type
`object`

| Property | Type | Description |
|----|----|----|
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | PodSpec is a description of a pod. |

## .template.spec

Description
PodSpec is a description of a pod.

Type
`object`

Required
- `containers`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>activeDeadlineSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>affinity</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Affinity is a group of affinity scheduling rules.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>automountServiceAccountToken</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>containers</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>containers[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>A single application container that you want to run within a pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dnsConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dnsPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.</p>
<p>Possible enum values: - <code>"ClusterFirst"</code> indicates that the pod should use cluster DNS first unless hostNetwork is true, if it is available, then fall back on the default (as determined by kubelet) DNS settings. - <code>"ClusterFirstWithHostNet"</code> indicates that the pod should use cluster DNS first, if it is available, then fall back on the default (as determined by kubelet) DNS settings. - <code>"Default"</code> indicates that the pod should use the default (as determined by kubelet) DNS settings. - <code>"None"</code> indicates that the pod should use empty DNS settings. DNS parameters such as nameservers and search paths should be defined via DNSConfig.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enableServiceLinks</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>EnableServiceLinks indicates whether information about services should be injected into pod’s environment variables, matching the syntax of Docker links. Optional: Defaults to true.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ephemeralContainers</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod’s ephemeralcontainers subresource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ephemeralContainers[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.</p>
<p>To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostAliases</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>HostAliases is an optional list of hosts and IPs that will be injected into the pod’s hosts file if specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostAliases[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod’s hosts file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostIPC</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Use the host’s ipc namespace. Optional: Default to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostNetwork</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Host networking requested for this pod. Use the host’s network namespace. If this option is set, the ports that will be used must be specified. Default to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostPID</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Use the host’s pid namespace. Optional: Default to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostUsers</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Use the host’s user namespace. Optional: Default to true. If set to true or not present, the pod will be run in the host user namespace, useful for when the pod needs a feature only available to the host user namespace, such as loading a kernel module with CAP_SYS_MODULE. When set to false, a new userns is created for the pod. Setting false is useful for mitigating container breakout vulnerabilities even allowing users to run their containers as root without actually having root privileges on the host. This field is alpha-level and is only honored by servers that enable the UserNamespacesSupport feature.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostname</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the hostname of the Pod If not specified, the pod’s hostname will be set to a system-defined value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imagePullSecrets</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: <a href="https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod">https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imagePullSecrets[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>initContainers</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: <a href="https://kubernetes.io/docs/concepts/workloads/pods/init-containers/">https://kubernetes.io/docs/concepts/workloads/pods/init-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>initContainers[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>A single application container that you want to run within a pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>NodeName indicates in which node this pod is scheduled. If empty, this pod is a candidate for scheduling by the scheduler defined in schedulerName. Once this field is set, the kubelet for this node becomes responsible for the lifecycle of this pod. This field should not be used to express a desire for the pod to be scheduled on a specific node. <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodename">https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodename</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeSelector</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node’s labels for the pod to be scheduled on that node. More info: <a href="https://kubernetes.io/docs/concepts/configuration/assign-pod-node/">https://kubernetes.io/docs/concepts/configuration/assign-pod-node/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>os</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodOS defines the OS parameters of a pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>overhead</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: <a href="https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md">https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>preemptionPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.</p>
<p>Possible enum values: - <code>"Never"</code> means that pod never preempts other pods with lower priority. - <code>"PreemptLowerPriority"</code> means that pod can preempt other pods with lower priority.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>priority</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>priorityClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If specified, indicates the pod’s priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readinessGates</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: <a href="https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates">https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readinessGates[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodReadinessGate contains the reference to a pod condition</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceClaims</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.</p>
<p>This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.</p>
<p>This field is immutable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceClaims[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodResourceClaim references exactly one ResourceClaim, either directly or by naming a ResourceClaimTemplate which is then turned into a ResourceClaim for the pod.</p>
<p>It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceRequirements describes the compute resource requirements.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>restartPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Restart policy for all containers within the pod. One of Always, OnFailure, Never. In some contexts, only a subset of those values may be permitted. Default to Always. More info: <a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy">https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy</a></p>
<p>Possible enum values: - <code>"Always"</code> - <code>"Never"</code> - <code>"OnFailure"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runtimeClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod. If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: <a href="https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class">https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedulerName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedulingGates</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.</p>
<p>SchedulingGates can only be set at pod creation time, and be removed only afterwards.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedulingGates[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodSchedulingGate is associated to a Pod to guard its scheduling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>securityContext</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext. Field values of container.securityContext take precedence over field values of PodSecurityContext.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serviceAccount</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>DeprecatedServiceAccount is a deprecated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serviceAccountName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: <a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/">https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>setHostnameAsFQDN</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>If true the pod’s hostname will be configured as the pod’s FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>shareProcessNamespace</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subdomain</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If specified, the fully qualified Pod hostname will be "&lt;hostname&gt;.&lt;subdomain&gt;.&lt;pod namespace&gt;.svc.&lt;cluster domain&gt;". If not specified, the pod will not have a domainname at all.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminationGracePeriodSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>If specified, the pod’s tolerations.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerations[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>The pod this Toleration is attached to tolerates any taint that matches the triple &lt;key,value,effect&gt; using the matching operator &lt;operator&gt;.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topologySpreadConstraints</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topologySpreadConstraints[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TopologySpreadConstraint specifies how to spread matching pods among the given topology.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumes</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of volumes that can be mounted by containers belonging to the pod. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes">https://kubernetes.io/docs/concepts/storage/volumes</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumes[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Volume represents a named volume in a pod that may be accessed by any container in the pod.</p></td>
</tr>
</tbody>
</table>

## .template.spec.affinity

Description
Affinity is a group of affinity scheduling rules.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `nodeAffinity` | `object` | Node affinity is a group of node affinity scheduling rules. |
| `podAffinity` | `object` | Pod affinity is a group of inter pod affinity scheduling rules. |
| `podAntiAffinity` | `object` | Pod anti affinity is a group of inter pod anti affinity scheduling rules. |

## .template.spec.affinity.nodeAffinity

Description
Node affinity is a group of node affinity scheduling rules.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `preferredDuringSchedulingIgnoredDuringExecution` | `array` | The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred. |
| `preferredDuringSchedulingIgnoredDuringExecution[]` | `object` | An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it’s a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op). |
| `requiredDuringSchedulingIgnoredDuringExecution` | `object` | A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms. |

## .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution

Description
The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.

Type
`array`

## .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\]

Description
An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it’s a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).

Type
`object`

Required
- `weight`

- `preference`

| Property | Type | Description |
|----|----|----|
| `preference` | `object` | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm. |
| `weight` | `integer` | Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100. |

## .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].preference

Description
A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | A list of node selector requirements by node’s labels. |
| `matchExpressions[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchFields` | `array` | A list of node selector requirements by node’s fields. |
| `matchFields[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |

## .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].preference.matchExpressions

Description
A list of node selector requirements by node’s labels.

Type
`array`

## .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].preference.matchExpressions\[\]

Description
A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The label key that the selector applies to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.</p>
<p>Possible enum values: - <code>"DoesNotExist"</code> - <code>"Exists"</code> - <code>"Gt"</code> - <code>"In"</code> - <code>"Lt"</code> - <code>"NotIn"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>values</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.</p></td>
</tr>
</tbody>
</table>

## .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].preference.matchFields

Description
A list of node selector requirements by node’s fields.

Type
`array`

## .template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].preference.matchFields\[\]

Description
A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The label key that the selector applies to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.</p>
<p>Possible enum values: - <code>"DoesNotExist"</code> - <code>"Exists"</code> - <code>"Gt"</code> - <code>"In"</code> - <code>"Lt"</code> - <code>"NotIn"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>values</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.</p></td>
</tr>
</tbody>
</table>

## .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution

Description
A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms.

Type
`object`

Required
- `nodeSelectorTerms`

| Property | Type | Description |
|----|----|----|
| `nodeSelectorTerms` | `array` | Required. A list of node selector terms. The terms are ORed. |
| `nodeSelectorTerms[]` | `object` | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm. |

## .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms

Description
Required. A list of node selector terms. The terms are ORed.

Type
`array`

## .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms\[\]

Description
A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array` | A list of node selector requirements by node’s labels. |
| `matchExpressions[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |
| `matchFields` | `array` | A list of node selector requirements by node’s fields. |
| `matchFields[]` | `object` | A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. |

## .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms\[\].matchExpressions

Description
A list of node selector requirements by node’s labels.

Type
`array`

## .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms\[\].matchExpressions\[\]

Description
A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The label key that the selector applies to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.</p>
<p>Possible enum values: - <code>"DoesNotExist"</code> - <code>"Exists"</code> - <code>"Gt"</code> - <code>"In"</code> - <code>"Lt"</code> - <code>"NotIn"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>values</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.</p></td>
</tr>
</tbody>
</table>

## .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms\[\].matchFields

Description
A list of node selector requirements by node’s fields.

Type
`array`

## .template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms\[\].matchFields\[\]

Description
A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The label key that the selector applies to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.</p>
<p>Possible enum values: - <code>"DoesNotExist"</code> - <code>"Exists"</code> - <code>"Gt"</code> - <code>"In"</code> - <code>"Lt"</code> - <code>"NotIn"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>values</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.</p></td>
</tr>
</tbody>
</table>

## .template.spec.affinity.podAffinity

Description
Pod affinity is a group of inter pod affinity scheduling rules.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `preferredDuringSchedulingIgnoredDuringExecution` | `array` | The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. |
| `preferredDuringSchedulingIgnoredDuringExecution[]` | `object` | The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s) |
| `requiredDuringSchedulingIgnoredDuringExecution` | `array` | If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. |
| `requiredDuringSchedulingIgnoredDuringExecution[]` | `object` | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running |

## .template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution

Description
The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.

Type
`array`

## .template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\]

Description
The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)

Type
`object`

Required
- `weight`

- `podAffinityTerm`

| Property | Type | Description |
|----|----|----|
| `podAffinityTerm` | `object` | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running |
| `weight` | `integer` | weight associated with matching the corresponding podAffinityTerm, in the range 1-100. |

## .template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm

Description
Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running

Type
`object`

Required
- `topologyKey`

| Property | Type | Description |
|----|----|----|
| `labelSelector` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

## .template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution

Description
If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

Type
`array`

## .template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\]

Description
Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running

Type
`object`

Required
- `topologyKey`

| Property | Type | Description |
|----|----|----|
| `labelSelector` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

## .template.spec.affinity.podAntiAffinity

Description
Pod anti affinity is a group of inter pod anti affinity scheduling rules.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `preferredDuringSchedulingIgnoredDuringExecution` | `array` | The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. |
| `preferredDuringSchedulingIgnoredDuringExecution[]` | `object` | The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s) |
| `requiredDuringSchedulingIgnoredDuringExecution` | `array` | If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. |
| `requiredDuringSchedulingIgnoredDuringExecution[]` | `object` | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running |

## .template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution

Description
The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.

Type
`array`

## .template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\]

Description
The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)

Type
`object`

Required
- `weight`

- `podAffinityTerm`

| Property | Type | Description |
|----|----|----|
| `podAffinityTerm` | `object` | Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running |
| `weight` | `integer` | weight associated with matching the corresponding podAffinityTerm, in the range 1-100. |

## .template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution\[\].podAffinityTerm

Description
Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running

Type
`object`

Required
- `topologyKey`

| Property | Type | Description |
|----|----|----|
| `labelSelector` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

## .template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution

Description
If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.

Type
`array`

## .template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution\[\]

Description
Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key \<topologyKey\> matches that of any node on which a pod of the set of pods is running

Type
`object`

Required
- `topologyKey`

| Property | Type | Description |
|----|----|----|
| `labelSelector` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. |
| `matchLabelKeys` | `array (string)` | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set. |
| `mismatchLabelKeys` | `array (string)` | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set. |
| `namespaceSelector` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. |
| `namespaces` | `array (string)` | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace". |
| `topologyKey` | `string` | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. |

## .template.spec.containers

Description
List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.

Type
`array`

## .template.spec.containers\[\]

Description
A single application container that you want to run within a pod.

Type
`object`

Required
- `name`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>args</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Arguments to the entrypoint. The container image’s CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <a href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>command</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Entrypoint array. Not executed within a shell. The container image’s ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <a href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>env</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of environment variables to set in the container. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>env[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>EnvVar represents an environment variable present in a Container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>envFrom</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>envFrom[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>EnvFromSource represents the source of a set of ConfigMaps or Secrets</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Container image name. More info: <a href="https://kubernetes.io/docs/concepts/containers/images">https://kubernetes.io/docs/concepts/containers/images</a> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imagePullPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: <a href="https://kubernetes.io/docs/concepts/containers/images#updating-images">https://kubernetes.io/docs/concepts/containers/images#updating-images</a></p>
<p>Possible enum values: - <code>"Always"</code> means that kubelet always attempts to pull the latest image. Container will fail If the pull fails. - <code>"IfNotPresent"</code> means that kubelet pulls if the image isn’t present on disk. Container will fail if the image isn’t present and the pull fails. - <code>"Never"</code> means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn’t present</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lifecycle</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>livenessProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ports</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <a href="https://github.com/kubernetes/kubernetes/issues/108255">https://github.com/kubernetes/kubernetes/issues/108255</a>. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ports[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ContainerPort represents a network port in a single container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readinessProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resizePolicy</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Resources resize policy for the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resizePolicy[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ContainerResizePolicy represents resource resize policy for the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceRequirements describes the compute resource requirements.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>restartPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is "Always". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod’s restart policy and the container type. Setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>securityContext</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>startupProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>stdin</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>stdinOnce</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminationMessagePath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: Path at which the file to which the container’s termination message will be written is mounted into the container’s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminationMessagePolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.</p>
<p>Possible enum values: - <code>"FallbackToLogsOnError"</code> will read the most recent contents of the container logs for the container status message when the container exits with an error and the terminationMessagePath has no contents. - <code>"File"</code> is the default behavior and will set the container status message to the contents of the container’s terminationMessagePath when the container exits.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tty</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeDevices</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>volumeDevices is the list of block devices to be used by the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeDevices[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>volumeDevice describes a mapping of a raw block device within a container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMounts</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Pod volumes to mount into the container’s filesystem. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMounts[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>VolumeMount describes a mounting of a Volume within a container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>workingDir</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Container’s working directory. If not specified, the container runtime’s default will be used, which might be configured in the container image. Cannot be updated.</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].env

Description
List of environment variables to set in the container. Cannot be updated.

Type
`array`

## .template.spec.containers\[\].env\[\]

Description
EnvVar represents an environment variable present in a Container.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the environment variable. Must be a C_IDENTIFIER. |
| `value` | `string` | Variable references \$(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single \$, which allows for escaping the \$(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "\$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". |
| `valueFrom` | `object` | EnvVarSource represents a source for the value of an EnvVar. |

## .template.spec.containers\[\].env\[\].valueFrom

Description
EnvVarSource represents a source for the value of an EnvVar.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMapKeyRef` | `object` | Selects a key from a ConfigMap. |
| `fieldRef` | `object` | ObjectFieldSelector selects an APIVersioned field of an object. |
| `resourceFieldRef` | `object` | ResourceFieldSelector represents container resources (cpu, memory) and their output format |
| `secretKeyRef` | `object` | SecretKeySelector selects a key of a Secret. |

## .template.spec.containers\[\].env\[\].valueFrom.configMapKeyRef

Description
Selects a key from a ConfigMap.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .template.spec.containers\[\].env\[\].valueFrom.fieldRef

Description
ObjectFieldSelector selects an APIVersioned field of an object.

Type
`object`

Required
- `fieldPath`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

## .template.spec.containers\[\].env\[\].valueFrom.resourceFieldRef

Description
ResourceFieldSelector represents container resources (cpu, memory) and their output format

Type
`object`

Required
- `resource`

| Property | Type | Description |
|----|----|----|
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | [`Quantity`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

## .template.spec.containers\[\].env\[\].valueFrom.secretKeyRef

Description
SecretKeySelector selects a key of a Secret.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .template.spec.containers\[\].envFrom

Description
List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.

Type
`array`

## .template.spec.containers\[\].envFrom\[\]

Description
EnvFromSource represents the source of a set of ConfigMaps or Secrets

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>configMapRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.</p>
<p>The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prefix</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional text to prepend to the name of each environment variable. Must be a C_IDENTIFIER.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secretRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SecretEnvSource selects a Secret to populate the environment variables with.</p>
<p>The contents of the target Secret’s Data field will represent the key-value pairs as environment variables.</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].envFrom\[\].configMapRef

Description
ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.

The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap must be defined |

## .template.spec.containers\[\].envFrom\[\].secretRef

Description
SecretEnvSource selects a Secret to populate the environment variables with.

The contents of the target Secret’s Data field will represent the key-value pairs as environment variables.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret must be defined |

## .template.spec.containers\[\].lifecycle

Description
Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>postStart</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>preStop</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>stopSignal</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name</p>
<p>Possible enum values: - <code>"SIGABRT"</code> - <code>"SIGALRM"</code> - <code>"SIGBUS"</code> - <code>"SIGCHLD"</code> - <code>"SIGCLD"</code> - <code>"SIGCONT"</code> - <code>"SIGFPE"</code> - <code>"SIGHUP"</code> - <code>"SIGILL"</code> - <code>"SIGINT"</code> - <code>"SIGIO"</code> - <code>"SIGIOT"</code> - <code>"SIGKILL"</code> - <code>"SIGPIPE"</code> - <code>"SIGPOLL"</code> - <code>"SIGPROF"</code> - <code>"SIGPWR"</code> - <code>"SIGQUIT"</code> - <code>"SIGRTMAX"</code> - <code>"SIGRTMAX-1"</code> - <code>"SIGRTMAX-10"</code> - <code>"SIGRTMAX-11"</code> - <code>"SIGRTMAX-12"</code> - <code>"SIGRTMAX-13"</code> - <code>"SIGRTMAX-14"</code> - <code>"SIGRTMAX-2"</code> - <code>"SIGRTMAX-3"</code> - <code>"SIGRTMAX-4"</code> - <code>"SIGRTMAX-5"</code> - <code>"SIGRTMAX-6"</code> - <code>"SIGRTMAX-7"</code> - <code>"SIGRTMAX-8"</code> - <code>"SIGRTMAX-9"</code> - <code>"SIGRTMIN"</code> - <code>"SIGRTMIN+1"</code> - <code>"SIGRTMIN+10"</code> - <code>"SIGRTMIN+11"</code> - <code>"SIGRTMIN+12"</code> - <code>"SIGRTMIN+13"</code> - <code>"SIGRTMIN+14"</code> - <code>"SIGRTMIN+15"</code> - <code>"SIGRTMIN+2"</code> - <code>"SIGRTMIN+3"</code> - <code>"SIGRTMIN+4"</code> - <code>"SIGRTMIN+5"</code> - <code>"SIGRTMIN+6"</code> - <code>"SIGRTMIN+7"</code> - <code>"SIGRTMIN+8"</code> - <code>"SIGRTMIN+9"</code> - <code>"SIGSEGV"</code> - <code>"SIGSTKFLT"</code> - <code>"SIGSTOP"</code> - <code>"SIGSYS"</code> - <code>"SIGTERM"</code> - <code>"SIGTRAP"</code> - <code>"SIGTSTP"</code> - <code>"SIGTTIN"</code> - <code>"SIGTTOU"</code> - <code>"SIGURG"</code> - <code>"SIGUSR1"</code> - <code>"SIGUSR2"</code> - <code>"SIGVTALRM"</code> - <code>"SIGWINCH"</code> - <code>"SIGXCPU"</code> - <code>"SIGXFSZ"</code></p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].lifecycle.postStart

Description
LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

## .template.spec.containers\[\].lifecycle.postStart.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.containers\[\].lifecycle.postStart.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].lifecycle.postStart.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.containers\[\].lifecycle.postStart.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.containers\[\].lifecycle.postStart.sleep

Description
SleepAction describes a "sleep" action.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .template.spec.containers\[\].lifecycle.postStart.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.containers\[\].lifecycle.preStop

Description
LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

## .template.spec.containers\[\].lifecycle.preStop.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.containers\[\].lifecycle.preStop.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].lifecycle.preStop.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.containers\[\].lifecycle.preStop.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.containers\[\].lifecycle.preStop.sleep

Description
SleepAction describes a "sleep" action.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .template.spec.containers\[\].lifecycle.preStop.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.containers\[\].livenessProbe

Description
Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .template.spec.containers\[\].livenessProbe.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.containers\[\].livenessProbe.grpc

Description
GRPCAction specifies an action involving a GRPC service.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].livenessProbe.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].livenessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.containers\[\].livenessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.containers\[\].livenessProbe.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.containers\[\].ports

Description
List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated.

Type
`array`

## .template.spec.containers\[\].ports\[\]

Description
ContainerPort represents a network port in a single container.

Type
`object`

Required
- `containerPort`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>containerPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Number of port to expose on the pod’s IP address. This must be a valid port number, 0 &lt; x &lt; 65536.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostIP</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>What host IP to bind the external port to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Number of port to expose on the host. If specified, this must be a valid port number, 0 &lt; x &lt; 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".</p>
<p>Possible enum values: - <code>"SCTP"</code> is the SCTP protocol. - <code>"TCP"</code> is the TCP protocol. - <code>"UDP"</code> is the UDP protocol.</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].readinessProbe

Description
Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .template.spec.containers\[\].readinessProbe.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.containers\[\].readinessProbe.grpc

Description
GRPCAction specifies an action involving a GRPC service.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].readinessProbe.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].readinessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.containers\[\].readinessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.containers\[\].readinessProbe.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.containers\[\].resizePolicy

Description
Resources resize policy for the container.

Type
`array`

## .template.spec.containers\[\].resizePolicy\[\]

Description
ContainerResizePolicy represents resource resize policy for the container.

Type
`object`

Required
- `resourceName`

- `restartPolicy`

| Property | Type | Description |
|----|----|----|
| `resourceName` | `string` | Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. |
| `restartPolicy` | `string` | Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. |

## .template.spec.containers\[\].resources

Description
ResourceRequirements describes the compute resource requirements.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>claims</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.</p>
<p>This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.</p>
<p>This field is immutable. It can only be set for containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claims[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceClaim references one entry in PodSpec.ResourceClaims.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>limits</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Limits describes the maximum amount of compute resources allowed. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].resources.claims

Description
Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

This field is immutable. It can only be set for containers.

Type
`array`

## .template.spec.containers\[\].resources.claims\[\]

Description
ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

## .template.spec.containers\[\].securityContext

Description
SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>allowPrivilegeEscalation</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>appArmorProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AppArmorProfile defines a pod or container’s AppArmor settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>capabilities</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Adds and removes POSIX capabilities from running containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>privileged</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>procMount</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.</p>
<p>Possible enum values: - <code>"Default"</code> uses the container runtime defaults for readonly and masked paths for /proc. Most container runtimes mask certain paths in /proc to avoid accidental security exposure of special devices or information. - <code>"Unmasked"</code> bypasses the default masking behavior of the container runtime and ensures the newly created /proc the container stays in tact with no modifications.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnlyRootFilesystem</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsGroup</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsNonRoot</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsUser</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seLinuxOptions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SELinuxOptions are the labels to be applied to the container</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seccompProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>windowsOptions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>WindowsSecurityContextOptions contain Windows-specific options and credentials.</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].securityContext.appArmorProfile

Description
AppArmorProfile defines a pod or container’s AppArmor settings.

Type
`object`

Required
- `type`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement.</p>
<p>Possible enum values: - <code>"Localhost"</code> indicates that a profile pre-loaded on the node should be used. - <code>"RuntimeDefault"</code> indicates that the container runtime’s default AppArmor profile should be used. - <code>"Unconfined"</code> indicates that no AppArmor profile should be enforced.</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].securityContext.capabilities

Description
Adds and removes POSIX capabilities from running containers.

Type
`object`

| Property | Type             | Description          |
|----------|------------------|----------------------|
| `add`    | `array (string)` | Added capabilities   |
| `drop`   | `array (string)` | Removed capabilities |

## .template.spec.containers\[\].securityContext.seLinuxOptions

Description
SELinuxOptions are the labels to be applied to the container

Type
`object`

| Property | Type | Description |
|----|----|----|
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

## .template.spec.containers\[\].securityContext.seccompProfile

Description
SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.

Type
`object`

Required
- `type`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of seccomp profile will be applied. Valid options are:</p>
<p>Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.</p>
<p>Possible enum values: - <code>"Localhost"</code> indicates a profile defined in a file on the node should be used. The file’s location relative to &lt;kubelet-root-dir&gt;/seccomp. - <code>"RuntimeDefault"</code> represents the default container runtime seccomp profile. - <code>"Unconfined"</code> indicates no seccomp profile is applied (A.K.A. unconfined).</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].securityContext.windowsOptions

Description
WindowsSecurityContextOptions contain Windows-specific options and credentials.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

## .template.spec.containers\[\].startupProbe

Description
Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .template.spec.containers\[\].startupProbe.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.containers\[\].startupProbe.grpc

Description
GRPCAction specifies an action involving a GRPC service.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].startupProbe.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.containers\[\].startupProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.containers\[\].startupProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.containers\[\].startupProbe.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.containers\[\].volumeDevices

Description
volumeDevices is the list of block devices to be used by the container.

Type
`array`

## .template.spec.containers\[\].volumeDevices\[\]

Description
volumeDevice describes a mapping of a raw block device within a container.

Type
`object`

Required
- `name`

- `devicePath`

| Property | Type | Description |
|----|----|----|
| `devicePath` | `string` | devicePath is the path inside of the container that the device will be mapped to. |
| `name` | `string` | name must match the name of a persistentVolumeClaim in the pod |

## .template.spec.containers\[\].volumeMounts

Description
Pod volumes to mount into the container’s filesystem. Cannot be updated.

Type
`array`

## .template.spec.containers\[\].volumeMounts\[\]

Description
VolumeMount describes a mounting of a Volume within a container.

Type
`object`

Required
- `name`

- `mountPath`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mountPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the container at which the volume should be mounted. Must not contain ':'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mountPropagation</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).</p>
<p>Possible enum values: - <code>"Bidirectional"</code> means that the volume in a container will receive new mounts from the host or other containers, and its own mounts will be propagated from the container to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rshared" in Linux terminology). - <code>"HostToContainer"</code> means that the volume in a container will receive new mounts from the host or other containers, but filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rslave" in Linux terminology). - <code>"None"</code> means that the volume in a container will not receive new mounts from the host or other containers, and filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode corresponds to "private" in Linux terminology.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>This must match the Name of a Volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnly</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>recursiveReadOnly</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>RecursiveReadOnly specifies whether read-only mounts should be handled recursively.</p>
<p>If ReadOnly is false, this field has no meaning and must be unspecified.</p>
<p>If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.</p>
<p>If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).</p>
<p>If this field is not specified, it is treated as an equivalent of Disabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPathExpr</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive.</p></td>
</tr>
</tbody>
</table>

## .template.spec.dnsConfig

Description
PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `nameservers` | `array (string)` | A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed. |
| `options` | `array` | A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy. |
| `options[]` | `object` | PodDNSConfigOption defines DNS resolver options of a pod. |
| `searches` | `array (string)` | A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed. |

## .template.spec.dnsConfig.options

Description
A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.

Type
`array`

## .template.spec.dnsConfig.options\[\]

Description
PodDNSConfigOption defines DNS resolver options of a pod.

Type
`object`

| Property | Type     | Description                                        |
|----------|----------|----------------------------------------------------|
| `name`   | `string` | Name is this DNS resolver option’s name. Required. |
| `value`  | `string` | Value is this DNS resolver option’s value.         |

## .template.spec.ephemeralContainers

Description
List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod’s ephemeralcontainers subresource.

Type
`array`

## .template.spec.ephemeralContainers\[\]

Description
An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.

To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted.

Type
`object`

Required
- `name`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>args</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Arguments to the entrypoint. The image’s CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <a href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>command</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Entrypoint array. Not executed within a shell. The image’s ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <a href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>env</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of environment variables to set in the container. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>env[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>EnvVar represents an environment variable present in a Container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>envFrom</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>envFrom[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>EnvFromSource represents the source of a set of ConfigMaps or Secrets</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Container image name. More info: <a href="https://kubernetes.io/docs/concepts/containers/images">https://kubernetes.io/docs/concepts/containers/images</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imagePullPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: <a href="https://kubernetes.io/docs/concepts/containers/images#updating-images">https://kubernetes.io/docs/concepts/containers/images#updating-images</a></p>
<p>Possible enum values: - <code>"Always"</code> means that kubelet always attempts to pull the latest image. Container will fail If the pull fails. - <code>"IfNotPresent"</code> means that kubelet pulls if the image isn’t present on disk. Container will fail if the image isn’t present and the pull fails. - <code>"Never"</code> means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn’t present</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lifecycle</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>livenessProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ports</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Ports are not allowed for ephemeral containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ports[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ContainerPort represents a network port in a single container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readinessProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resizePolicy</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Resources resize policy for the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resizePolicy[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ContainerResizePolicy represents resource resize policy for the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceRequirements describes the compute resource requirements.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>restartPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Restart policy for the container to manage the restart behavior of each container within a pod. This may only be set for init containers. You cannot set this field on ephemeral containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>securityContext</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>startupProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>stdin</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>stdinOnce</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetContainerName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container uses the namespaces configured in the Pod spec.</p>
<p>The container runtime must implement support for this feature. If the runtime does not support namespace targeting then the result of setting this field is undefined.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminationMessagePath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: Path at which the file to which the container’s termination message will be written is mounted into the container’s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminationMessagePolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.</p>
<p>Possible enum values: - <code>"FallbackToLogsOnError"</code> will read the most recent contents of the container logs for the container status message when the container exits with an error and the terminationMessagePath has no contents. - <code>"File"</code> is the default behavior and will set the container status message to the contents of the container’s terminationMessagePath when the container exits.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tty</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeDevices</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>volumeDevices is the list of block devices to be used by the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeDevices[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>volumeDevice describes a mapping of a raw block device within a container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMounts</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Pod volumes to mount into the container’s filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMounts[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>VolumeMount describes a mounting of a Volume within a container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>workingDir</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Container’s working directory. If not specified, the container runtime’s default will be used, which might be configured in the container image. Cannot be updated.</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].env

Description
List of environment variables to set in the container. Cannot be updated.

Type
`array`

## .template.spec.ephemeralContainers\[\].env\[\]

Description
EnvVar represents an environment variable present in a Container.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the environment variable. Must be a C_IDENTIFIER. |
| `value` | `string` | Variable references \$(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single \$, which allows for escaping the \$(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "\$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". |
| `valueFrom` | `object` | EnvVarSource represents a source for the value of an EnvVar. |

## .template.spec.ephemeralContainers\[\].env\[\].valueFrom

Description
EnvVarSource represents a source for the value of an EnvVar.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMapKeyRef` | `object` | Selects a key from a ConfigMap. |
| `fieldRef` | `object` | ObjectFieldSelector selects an APIVersioned field of an object. |
| `resourceFieldRef` | `object` | ResourceFieldSelector represents container resources (cpu, memory) and their output format |
| `secretKeyRef` | `object` | SecretKeySelector selects a key of a Secret. |

## .template.spec.ephemeralContainers\[\].env\[\].valueFrom.configMapKeyRef

Description
Selects a key from a ConfigMap.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .template.spec.ephemeralContainers\[\].env\[\].valueFrom.fieldRef

Description
ObjectFieldSelector selects an APIVersioned field of an object.

Type
`object`

Required
- `fieldPath`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

## .template.spec.ephemeralContainers\[\].env\[\].valueFrom.resourceFieldRef

Description
ResourceFieldSelector represents container resources (cpu, memory) and their output format

Type
`object`

Required
- `resource`

| Property | Type | Description |
|----|----|----|
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | [`Quantity`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

## .template.spec.ephemeralContainers\[\].env\[\].valueFrom.secretKeyRef

Description
SecretKeySelector selects a key of a Secret.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .template.spec.ephemeralContainers\[\].envFrom

Description
List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.

Type
`array`

## .template.spec.ephemeralContainers\[\].envFrom\[\]

Description
EnvFromSource represents the source of a set of ConfigMaps or Secrets

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>configMapRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.</p>
<p>The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prefix</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional text to prepend to the name of each environment variable. Must be a C_IDENTIFIER.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secretRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SecretEnvSource selects a Secret to populate the environment variables with.</p>
<p>The contents of the target Secret’s Data field will represent the key-value pairs as environment variables.</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].envFrom\[\].configMapRef

Description
ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.

The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap must be defined |

## .template.spec.ephemeralContainers\[\].envFrom\[\].secretRef

Description
SecretEnvSource selects a Secret to populate the environment variables with.

The contents of the target Secret’s Data field will represent the key-value pairs as environment variables.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret must be defined |

## .template.spec.ephemeralContainers\[\].lifecycle

Description
Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>postStart</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>preStop</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>stopSignal</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name</p>
<p>Possible enum values: - <code>"SIGABRT"</code> - <code>"SIGALRM"</code> - <code>"SIGBUS"</code> - <code>"SIGCHLD"</code> - <code>"SIGCLD"</code> - <code>"SIGCONT"</code> - <code>"SIGFPE"</code> - <code>"SIGHUP"</code> - <code>"SIGILL"</code> - <code>"SIGINT"</code> - <code>"SIGIO"</code> - <code>"SIGIOT"</code> - <code>"SIGKILL"</code> - <code>"SIGPIPE"</code> - <code>"SIGPOLL"</code> - <code>"SIGPROF"</code> - <code>"SIGPWR"</code> - <code>"SIGQUIT"</code> - <code>"SIGRTMAX"</code> - <code>"SIGRTMAX-1"</code> - <code>"SIGRTMAX-10"</code> - <code>"SIGRTMAX-11"</code> - <code>"SIGRTMAX-12"</code> - <code>"SIGRTMAX-13"</code> - <code>"SIGRTMAX-14"</code> - <code>"SIGRTMAX-2"</code> - <code>"SIGRTMAX-3"</code> - <code>"SIGRTMAX-4"</code> - <code>"SIGRTMAX-5"</code> - <code>"SIGRTMAX-6"</code> - <code>"SIGRTMAX-7"</code> - <code>"SIGRTMAX-8"</code> - <code>"SIGRTMAX-9"</code> - <code>"SIGRTMIN"</code> - <code>"SIGRTMIN+1"</code> - <code>"SIGRTMIN+10"</code> - <code>"SIGRTMIN+11"</code> - <code>"SIGRTMIN+12"</code> - <code>"SIGRTMIN+13"</code> - <code>"SIGRTMIN+14"</code> - <code>"SIGRTMIN+15"</code> - <code>"SIGRTMIN+2"</code> - <code>"SIGRTMIN+3"</code> - <code>"SIGRTMIN+4"</code> - <code>"SIGRTMIN+5"</code> - <code>"SIGRTMIN+6"</code> - <code>"SIGRTMIN+7"</code> - <code>"SIGRTMIN+8"</code> - <code>"SIGRTMIN+9"</code> - <code>"SIGSEGV"</code> - <code>"SIGSTKFLT"</code> - <code>"SIGSTOP"</code> - <code>"SIGSYS"</code> - <code>"SIGTERM"</code> - <code>"SIGTRAP"</code> - <code>"SIGTSTP"</code> - <code>"SIGTTIN"</code> - <code>"SIGTTOU"</code> - <code>"SIGURG"</code> - <code>"SIGUSR1"</code> - <code>"SIGUSR2"</code> - <code>"SIGVTALRM"</code> - <code>"SIGWINCH"</code> - <code>"SIGXCPU"</code> - <code>"SIGXFSZ"</code></p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].lifecycle.postStart

Description
LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

## .template.spec.ephemeralContainers\[\].lifecycle.postStart.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.ephemeralContainers\[\].lifecycle.postStart.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].lifecycle.postStart.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.ephemeralContainers\[\].lifecycle.postStart.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.ephemeralContainers\[\].lifecycle.postStart.sleep

Description
SleepAction describes a "sleep" action.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .template.spec.ephemeralContainers\[\].lifecycle.postStart.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.ephemeralContainers\[\].lifecycle.preStop

Description
LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

## .template.spec.ephemeralContainers\[\].lifecycle.preStop.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.ephemeralContainers\[\].lifecycle.preStop.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].lifecycle.preStop.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.ephemeralContainers\[\].lifecycle.preStop.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.ephemeralContainers\[\].lifecycle.preStop.sleep

Description
SleepAction describes a "sleep" action.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .template.spec.ephemeralContainers\[\].lifecycle.preStop.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.ephemeralContainers\[\].livenessProbe

Description
Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .template.spec.ephemeralContainers\[\].livenessProbe.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.ephemeralContainers\[\].livenessProbe.grpc

Description
GRPCAction specifies an action involving a GRPC service.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].livenessProbe.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].livenessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.ephemeralContainers\[\].livenessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.ephemeralContainers\[\].livenessProbe.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.ephemeralContainers\[\].ports

Description
Ports are not allowed for ephemeral containers.

Type
`array`

## .template.spec.ephemeralContainers\[\].ports\[\]

Description
ContainerPort represents a network port in a single container.

Type
`object`

Required
- `containerPort`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>containerPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Number of port to expose on the pod’s IP address. This must be a valid port number, 0 &lt; x &lt; 65536.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostIP</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>What host IP to bind the external port to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Number of port to expose on the host. If specified, this must be a valid port number, 0 &lt; x &lt; 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".</p>
<p>Possible enum values: - <code>"SCTP"</code> is the SCTP protocol. - <code>"TCP"</code> is the TCP protocol. - <code>"UDP"</code> is the UDP protocol.</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].readinessProbe

Description
Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .template.spec.ephemeralContainers\[\].readinessProbe.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.ephemeralContainers\[\].readinessProbe.grpc

Description
GRPCAction specifies an action involving a GRPC service.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].readinessProbe.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].readinessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.ephemeralContainers\[\].readinessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.ephemeralContainers\[\].readinessProbe.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.ephemeralContainers\[\].resizePolicy

Description
Resources resize policy for the container.

Type
`array`

## .template.spec.ephemeralContainers\[\].resizePolicy\[\]

Description
ContainerResizePolicy represents resource resize policy for the container.

Type
`object`

Required
- `resourceName`

- `restartPolicy`

| Property | Type | Description |
|----|----|----|
| `resourceName` | `string` | Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. |
| `restartPolicy` | `string` | Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. |

## .template.spec.ephemeralContainers\[\].resources

Description
ResourceRequirements describes the compute resource requirements.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>claims</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.</p>
<p>This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.</p>
<p>This field is immutable. It can only be set for containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claims[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceClaim references one entry in PodSpec.ResourceClaims.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>limits</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Limits describes the maximum amount of compute resources allowed. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].resources.claims

Description
Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

This field is immutable. It can only be set for containers.

Type
`array`

## .template.spec.ephemeralContainers\[\].resources.claims\[\]

Description
ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

## .template.spec.ephemeralContainers\[\].securityContext

Description
SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>allowPrivilegeEscalation</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>appArmorProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AppArmorProfile defines a pod or container’s AppArmor settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>capabilities</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Adds and removes POSIX capabilities from running containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>privileged</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>procMount</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.</p>
<p>Possible enum values: - <code>"Default"</code> uses the container runtime defaults for readonly and masked paths for /proc. Most container runtimes mask certain paths in /proc to avoid accidental security exposure of special devices or information. - <code>"Unmasked"</code> bypasses the default masking behavior of the container runtime and ensures the newly created /proc the container stays in tact with no modifications.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnlyRootFilesystem</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsGroup</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsNonRoot</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsUser</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seLinuxOptions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SELinuxOptions are the labels to be applied to the container</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seccompProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>windowsOptions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>WindowsSecurityContextOptions contain Windows-specific options and credentials.</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].securityContext.appArmorProfile

Description
AppArmorProfile defines a pod or container’s AppArmor settings.

Type
`object`

Required
- `type`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement.</p>
<p>Possible enum values: - <code>"Localhost"</code> indicates that a profile pre-loaded on the node should be used. - <code>"RuntimeDefault"</code> indicates that the container runtime’s default AppArmor profile should be used. - <code>"Unconfined"</code> indicates that no AppArmor profile should be enforced.</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].securityContext.capabilities

Description
Adds and removes POSIX capabilities from running containers.

Type
`object`

| Property | Type             | Description          |
|----------|------------------|----------------------|
| `add`    | `array (string)` | Added capabilities   |
| `drop`   | `array (string)` | Removed capabilities |

## .template.spec.ephemeralContainers\[\].securityContext.seLinuxOptions

Description
SELinuxOptions are the labels to be applied to the container

Type
`object`

| Property | Type | Description |
|----|----|----|
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

## .template.spec.ephemeralContainers\[\].securityContext.seccompProfile

Description
SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.

Type
`object`

Required
- `type`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of seccomp profile will be applied. Valid options are:</p>
<p>Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.</p>
<p>Possible enum values: - <code>"Localhost"</code> indicates a profile defined in a file on the node should be used. The file’s location relative to &lt;kubelet-root-dir&gt;/seccomp. - <code>"RuntimeDefault"</code> represents the default container runtime seccomp profile. - <code>"Unconfined"</code> indicates no seccomp profile is applied (A.K.A. unconfined).</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].securityContext.windowsOptions

Description
WindowsSecurityContextOptions contain Windows-specific options and credentials.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

## .template.spec.ephemeralContainers\[\].startupProbe

Description
Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .template.spec.ephemeralContainers\[\].startupProbe.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.ephemeralContainers\[\].startupProbe.grpc

Description
GRPCAction specifies an action involving a GRPC service.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].startupProbe.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.ephemeralContainers\[\].startupProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.ephemeralContainers\[\].startupProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.ephemeralContainers\[\].startupProbe.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.ephemeralContainers\[\].volumeDevices

Description
volumeDevices is the list of block devices to be used by the container.

Type
`array`

## .template.spec.ephemeralContainers\[\].volumeDevices\[\]

Description
volumeDevice describes a mapping of a raw block device within a container.

Type
`object`

Required
- `name`

- `devicePath`

| Property | Type | Description |
|----|----|----|
| `devicePath` | `string` | devicePath is the path inside of the container that the device will be mapped to. |
| `name` | `string` | name must match the name of a persistentVolumeClaim in the pod |

## .template.spec.ephemeralContainers\[\].volumeMounts

Description
Pod volumes to mount into the container’s filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated.

Type
`array`

## .template.spec.ephemeralContainers\[\].volumeMounts\[\]

Description
VolumeMount describes a mounting of a Volume within a container.

Type
`object`

Required
- `name`

- `mountPath`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mountPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the container at which the volume should be mounted. Must not contain ':'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mountPropagation</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).</p>
<p>Possible enum values: - <code>"Bidirectional"</code> means that the volume in a container will receive new mounts from the host or other containers, and its own mounts will be propagated from the container to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rshared" in Linux terminology). - <code>"HostToContainer"</code> means that the volume in a container will receive new mounts from the host or other containers, but filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rslave" in Linux terminology). - <code>"None"</code> means that the volume in a container will not receive new mounts from the host or other containers, and filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode corresponds to "private" in Linux terminology.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>This must match the Name of a Volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnly</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>recursiveReadOnly</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>RecursiveReadOnly specifies whether read-only mounts should be handled recursively.</p>
<p>If ReadOnly is false, this field has no meaning and must be unspecified.</p>
<p>If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.</p>
<p>If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).</p>
<p>If this field is not specified, it is treated as an equivalent of Disabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPathExpr</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive.</p></td>
</tr>
</tbody>
</table>

## .template.spec.hostAliases

Description
HostAliases is an optional list of hosts and IPs that will be injected into the pod’s hosts file if specified.

Type
`array`

## .template.spec.hostAliases\[\]

Description
HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod’s hosts file.

Type
`object`

Required
- `ip`

| Property    | Type             | Description                         |
|-------------|------------------|-------------------------------------|
| `hostnames` | `array (string)` | Hostnames for the above IP address. |
| `ip`        | `string`         | IP address of the host file entry.  |

## .template.spec.imagePullSecrets

Description
ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: <https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod>

Type
`array`

## .template.spec.imagePullSecrets\[\]

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .template.spec.initContainers

Description
List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/>

Type
`array`

## .template.spec.initContainers\[\]

Description
A single application container that you want to run within a pod.

Type
`object`

Required
- `name`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>args</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Arguments to the entrypoint. The container image’s CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <a href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>command</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Entrypoint array. Not executed within a shell. The container image’s ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <a href="https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell">https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>env</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of environment variables to set in the container. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>env[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>EnvVar represents an environment variable present in a Container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>envFrom</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>envFrom[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>EnvFromSource represents the source of a set of ConfigMaps or Secrets</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Container image name. More info: <a href="https://kubernetes.io/docs/concepts/containers/images">https://kubernetes.io/docs/concepts/containers/images</a> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imagePullPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: <a href="https://kubernetes.io/docs/concepts/containers/images#updating-images">https://kubernetes.io/docs/concepts/containers/images#updating-images</a></p>
<p>Possible enum values: - <code>"Always"</code> means that kubelet always attempts to pull the latest image. Container will fail If the pull fails. - <code>"IfNotPresent"</code> means that kubelet pulls if the image isn’t present on disk. Container will fail if the image isn’t present and the pull fails. - <code>"Never"</code> means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn’t present</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>lifecycle</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>livenessProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ports</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <a href="https://github.com/kubernetes/kubernetes/issues/108255">https://github.com/kubernetes/kubernetes/issues/108255</a>. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ports[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ContainerPort represents a network port in a single container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readinessProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resizePolicy</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Resources resize policy for the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resizePolicy[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ContainerResizePolicy represents resource resize policy for the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceRequirements describes the compute resource requirements.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>restartPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is "Always". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod’s restart policy and the container type. Setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>securityContext</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>startupProbe</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>stdin</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>stdinOnce</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminationMessagePath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: Path at which the file to which the container’s termination message will be written is mounted into the container’s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>terminationMessagePolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.</p>
<p>Possible enum values: - <code>"FallbackToLogsOnError"</code> will read the most recent contents of the container logs for the container status message when the container exits with an error and the terminationMessagePath has no contents. - <code>"File"</code> is the default behavior and will set the container status message to the contents of the container’s terminationMessagePath when the container exits.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tty</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeDevices</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>volumeDevices is the list of block devices to be used by the container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeDevices[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>volumeDevice describes a mapping of a raw block device within a container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMounts</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Pod volumes to mount into the container’s filesystem. Cannot be updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMounts[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>VolumeMount describes a mounting of a Volume within a container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>workingDir</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Container’s working directory. If not specified, the container runtime’s default will be used, which might be configured in the container image. Cannot be updated.</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].env

Description
List of environment variables to set in the container. Cannot be updated.

Type
`array`

## .template.spec.initContainers\[\].env\[\]

Description
EnvVar represents an environment variable present in a Container.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the environment variable. Must be a C_IDENTIFIER. |
| `value` | `string` | Variable references \$(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single \$, which allows for escaping the \$(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "\$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". |
| `valueFrom` | `object` | EnvVarSource represents a source for the value of an EnvVar. |

## .template.spec.initContainers\[\].env\[\].valueFrom

Description
EnvVarSource represents a source for the value of an EnvVar.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `configMapKeyRef` | `object` | Selects a key from a ConfigMap. |
| `fieldRef` | `object` | ObjectFieldSelector selects an APIVersioned field of an object. |
| `resourceFieldRef` | `object` | ResourceFieldSelector represents container resources (cpu, memory) and their output format |
| `secretKeyRef` | `object` | SecretKeySelector selects a key of a Secret. |

## .template.spec.initContainers\[\].env\[\].valueFrom.configMapKeyRef

Description
Selects a key from a ConfigMap.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key to select. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap or its key must be defined |

## .template.spec.initContainers\[\].env\[\].valueFrom.fieldRef

Description
ObjectFieldSelector selects an APIVersioned field of an object.

Type
`object`

Required
- `fieldPath`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

## .template.spec.initContainers\[\].env\[\].valueFrom.resourceFieldRef

Description
ResourceFieldSelector represents container resources (cpu, memory) and their output format

Type
`object`

Required
- `resource`

| Property | Type | Description |
|----|----|----|
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | [`Quantity`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

## .template.spec.initContainers\[\].env\[\].valueFrom.secretKeyRef

Description
SecretKeySelector selects a key of a Secret.

Type
`object`

Required
- `key`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | The key of the secret to select from. Must be a valid secret key. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret or its key must be defined |

## .template.spec.initContainers\[\].envFrom

Description
List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.

Type
`array`

## .template.spec.initContainers\[\].envFrom\[\]

Description
EnvFromSource represents the source of a set of ConfigMaps or Secrets

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>configMapRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.</p>
<p>The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>prefix</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional text to prepend to the name of each environment variable. Must be a C_IDENTIFIER.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secretRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SecretEnvSource selects a Secret to populate the environment variables with.</p>
<p>The contents of the target Secret’s Data field will represent the key-value pairs as environment variables.</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].envFrom\[\].configMapRef

Description
ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.

The contents of the target ConfigMap’s Data field will represent the key-value pairs as environment variables.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the ConfigMap must be defined |

## .template.spec.initContainers\[\].envFrom\[\].secretRef

Description
SecretEnvSource selects a Secret to populate the environment variables with.

The contents of the target Secret’s Data field will represent the key-value pairs as environment variables.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | Specify whether the Secret must be defined |

## .template.spec.initContainers\[\].lifecycle

Description
Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>postStart</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>preStop</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>stopSignal</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name</p>
<p>Possible enum values: - <code>"SIGABRT"</code> - <code>"SIGALRM"</code> - <code>"SIGBUS"</code> - <code>"SIGCHLD"</code> - <code>"SIGCLD"</code> - <code>"SIGCONT"</code> - <code>"SIGFPE"</code> - <code>"SIGHUP"</code> - <code>"SIGILL"</code> - <code>"SIGINT"</code> - <code>"SIGIO"</code> - <code>"SIGIOT"</code> - <code>"SIGKILL"</code> - <code>"SIGPIPE"</code> - <code>"SIGPOLL"</code> - <code>"SIGPROF"</code> - <code>"SIGPWR"</code> - <code>"SIGQUIT"</code> - <code>"SIGRTMAX"</code> - <code>"SIGRTMAX-1"</code> - <code>"SIGRTMAX-10"</code> - <code>"SIGRTMAX-11"</code> - <code>"SIGRTMAX-12"</code> - <code>"SIGRTMAX-13"</code> - <code>"SIGRTMAX-14"</code> - <code>"SIGRTMAX-2"</code> - <code>"SIGRTMAX-3"</code> - <code>"SIGRTMAX-4"</code> - <code>"SIGRTMAX-5"</code> - <code>"SIGRTMAX-6"</code> - <code>"SIGRTMAX-7"</code> - <code>"SIGRTMAX-8"</code> - <code>"SIGRTMAX-9"</code> - <code>"SIGRTMIN"</code> - <code>"SIGRTMIN+1"</code> - <code>"SIGRTMIN+10"</code> - <code>"SIGRTMIN+11"</code> - <code>"SIGRTMIN+12"</code> - <code>"SIGRTMIN+13"</code> - <code>"SIGRTMIN+14"</code> - <code>"SIGRTMIN+15"</code> - <code>"SIGRTMIN+2"</code> - <code>"SIGRTMIN+3"</code> - <code>"SIGRTMIN+4"</code> - <code>"SIGRTMIN+5"</code> - <code>"SIGRTMIN+6"</code> - <code>"SIGRTMIN+7"</code> - <code>"SIGRTMIN+8"</code> - <code>"SIGRTMIN+9"</code> - <code>"SIGSEGV"</code> - <code>"SIGSTKFLT"</code> - <code>"SIGSTOP"</code> - <code>"SIGSYS"</code> - <code>"SIGTERM"</code> - <code>"SIGTRAP"</code> - <code>"SIGTSTP"</code> - <code>"SIGTTIN"</code> - <code>"SIGTTOU"</code> - <code>"SIGURG"</code> - <code>"SIGUSR1"</code> - <code>"SIGUSR2"</code> - <code>"SIGVTALRM"</code> - <code>"SIGWINCH"</code> - <code>"SIGXCPU"</code> - <code>"SIGXFSZ"</code></p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].lifecycle.postStart

Description
LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

## .template.spec.initContainers\[\].lifecycle.postStart.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.initContainers\[\].lifecycle.postStart.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].lifecycle.postStart.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.initContainers\[\].lifecycle.postStart.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.initContainers\[\].lifecycle.postStart.sleep

Description
SleepAction describes a "sleep" action.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .template.spec.initContainers\[\].lifecycle.postStart.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.initContainers\[\].lifecycle.preStop

Description
LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `sleep` | `object` | SleepAction describes a "sleep" action. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |

## .template.spec.initContainers\[\].lifecycle.preStop.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.initContainers\[\].lifecycle.preStop.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].lifecycle.preStop.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.initContainers\[\].lifecycle.preStop.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.initContainers\[\].lifecycle.preStop.sleep

Description
SleepAction describes a "sleep" action.

Type
`object`

Required
- `seconds`

| Property  | Type      | Description                                |
|-----------|-----------|--------------------------------------------|
| `seconds` | `integer` | Seconds is the number of seconds to sleep. |

## .template.spec.initContainers\[\].lifecycle.preStop.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.initContainers\[\].livenessProbe

Description
Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .template.spec.initContainers\[\].livenessProbe.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.initContainers\[\].livenessProbe.grpc

Description
GRPCAction specifies an action involving a GRPC service.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].livenessProbe.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].livenessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.initContainers\[\].livenessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.initContainers\[\].livenessProbe.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.initContainers\[\].ports

Description
List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated.

Type
`array`

## .template.spec.initContainers\[\].ports\[\]

Description
ContainerPort represents a network port in a single container.

Type
`object`

Required
- `containerPort`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>containerPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Number of port to expose on the pod’s IP address. This must be a valid port number, 0 &lt; x &lt; 65536.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostIP</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>What host IP to bind the external port to.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostPort</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Number of port to expose on the host. If specified, this must be a valid port number, 0 &lt; x &lt; 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>protocol</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".</p>
<p>Possible enum values: - <code>"SCTP"</code> is the SCTP protocol. - <code>"TCP"</code> is the TCP protocol. - <code>"UDP"</code> is the UDP protocol.</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].readinessProbe

Description
Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .template.spec.initContainers\[\].readinessProbe.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.initContainers\[\].readinessProbe.grpc

Description
GRPCAction specifies an action involving a GRPC service.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].readinessProbe.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].readinessProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.initContainers\[\].readinessProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.initContainers\[\].readinessProbe.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.initContainers\[\].resizePolicy

Description
Resources resize policy for the container.

Type
`array`

## .template.spec.initContainers\[\].resizePolicy\[\]

Description
ContainerResizePolicy represents resource resize policy for the container.

Type
`object`

Required
- `resourceName`

- `restartPolicy`

| Property | Type | Description |
|----|----|----|
| `resourceName` | `string` | Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. |
| `restartPolicy` | `string` | Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. |

## .template.spec.initContainers\[\].resources

Description
ResourceRequirements describes the compute resource requirements.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>claims</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.</p>
<p>This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.</p>
<p>This field is immutable. It can only be set for containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claims[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceClaim references one entry in PodSpec.ResourceClaims.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>limits</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Limits describes the maximum amount of compute resources allowed. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].resources.claims

Description
Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

This field is immutable. It can only be set for containers.

Type
`array`

## .template.spec.initContainers\[\].resources.claims\[\]

Description
ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

## .template.spec.initContainers\[\].securityContext

Description
SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext. When both are set, the values in SecurityContext take precedence.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>allowPrivilegeEscalation</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>appArmorProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AppArmorProfile defines a pod or container’s AppArmor settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>capabilities</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Adds and removes POSIX capabilities from running containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>privileged</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>procMount</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.</p>
<p>Possible enum values: - <code>"Default"</code> uses the container runtime defaults for readonly and masked paths for /proc. Most container runtimes mask certain paths in /proc to avoid accidental security exposure of special devices or information. - <code>"Unmasked"</code> bypasses the default masking behavior of the container runtime and ensures the newly created /proc the container stays in tact with no modifications.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnlyRootFilesystem</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsGroup</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsNonRoot</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsUser</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seLinuxOptions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SELinuxOptions are the labels to be applied to the container</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seccompProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>windowsOptions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>WindowsSecurityContextOptions contain Windows-specific options and credentials.</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].securityContext.appArmorProfile

Description
AppArmorProfile defines a pod or container’s AppArmor settings.

Type
`object`

Required
- `type`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement.</p>
<p>Possible enum values: - <code>"Localhost"</code> indicates that a profile pre-loaded on the node should be used. - <code>"RuntimeDefault"</code> indicates that the container runtime’s default AppArmor profile should be used. - <code>"Unconfined"</code> indicates that no AppArmor profile should be enforced.</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].securityContext.capabilities

Description
Adds and removes POSIX capabilities from running containers.

Type
`object`

| Property | Type             | Description          |
|----------|------------------|----------------------|
| `add`    | `array (string)` | Added capabilities   |
| `drop`   | `array (string)` | Removed capabilities |

## .template.spec.initContainers\[\].securityContext.seLinuxOptions

Description
SELinuxOptions are the labels to be applied to the container

Type
`object`

| Property | Type | Description |
|----|----|----|
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

## .template.spec.initContainers\[\].securityContext.seccompProfile

Description
SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.

Type
`object`

Required
- `type`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of seccomp profile will be applied. Valid options are:</p>
<p>Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.</p>
<p>Possible enum values: - <code>"Localhost"</code> indicates a profile defined in a file on the node should be used. The file’s location relative to &lt;kubelet-root-dir&gt;/seccomp. - <code>"RuntimeDefault"</code> represents the default container runtime seccomp profile. - <code>"Unconfined"</code> indicates no seccomp profile is applied (A.K.A. unconfined).</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].securityContext.windowsOptions

Description
WindowsSecurityContextOptions contain Windows-specific options and credentials.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

## .template.spec.initContainers\[\].startupProbe

Description
Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `exec` | `object` | ExecAction describes a "run in container" action. |
| `failureThreshold` | `integer` | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. |
| `grpc` | `object` | GRPCAction specifies an action involving a GRPC service. |
| `httpGet` | `object` | HTTPGetAction describes an action based on HTTP Get requests. |
| `initialDelaySeconds` | `integer` | Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |
| `periodSeconds` | `integer` | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. |
| `successThreshold` | `integer` | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |
| `tcpSocket` | `object` | TCPSocketAction describes an action based on opening a socket |
| `terminationGracePeriodSeconds` | `integer` | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |
| `timeoutSeconds` | `integer` | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes> |

## .template.spec.initContainers\[\].startupProbe.exec

Description
ExecAction describes a "run in container" action.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `command` | `array (string)` | Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('\|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. |

## .template.spec.initContainers\[\].startupProbe.grpc

Description
GRPCAction specifies an action involving a GRPC service.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Port number of the gRPC service. Number must be in the range 1 to 65535.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>service</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Service is the name of the service to place in the gRPC HealthCheckRequest (see <a href="https://github.com/grpc/grpc/blob/master/doc/health-checking.md">https://github.com/grpc/grpc/blob/master/doc/health-checking.md</a>).</p>
<p>If this is not specified, the default behavior is defined by gRPC.</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].startupProbe.httpGet

Description
HTTPGetAction describes an action based on HTTP Get requests.

Type
`object`

Required
- `port`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>host</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Custom headers to set in the request. HTTP allows repeated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpHeaders[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>HTTPHeader describes a custom header to be used in HTTP probes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to access on the HTTP server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>port</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-util-intstr-IntOrString"><code>IntOrString</code></a></p></td>
<td style="text-align: left;"><p>Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scheme</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Scheme to use for connecting to the host. Defaults to HTTP.</p>
<p>Possible enum values: - <code>"HTTP"</code> means that the scheme used will be http:// - <code>"HTTPS"</code> means that the scheme used will be https://</p></td>
</tr>
</tbody>
</table>

## .template.spec.initContainers\[\].startupProbe.httpGet.httpHeaders

Description
Custom headers to set in the request. HTTP allows repeated headers.

Type
`array`

## .template.spec.initContainers\[\].startupProbe.httpGet.httpHeaders\[\]

Description
HTTPHeader describes a custom header to be used in HTTP probes

Type
`object`

Required
- `name`

- `value`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. |
| `value` | `string` | The header field value |

## .template.spec.initContainers\[\].startupProbe.tcpSocket

Description
TCPSocketAction describes an action based on opening a socket

Type
`object`

Required
- `port`

| Property | Type | Description |
|----|----|----|
| `host` | `string` | Optional: Host name to connect to, defaults to the pod IP. |
| `port` | [`IntOrString`](../objects/index.md#io-k8s-apimachinery-pkg-util-intstr-IntOrString) | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. |

## .template.spec.initContainers\[\].volumeDevices

Description
volumeDevices is the list of block devices to be used by the container.

Type
`array`

## .template.spec.initContainers\[\].volumeDevices\[\]

Description
volumeDevice describes a mapping of a raw block device within a container.

Type
`object`

Required
- `name`

- `devicePath`

| Property | Type | Description |
|----|----|----|
| `devicePath` | `string` | devicePath is the path inside of the container that the device will be mapped to. |
| `name` | `string` | name must match the name of a persistentVolumeClaim in the pod |

## .template.spec.initContainers\[\].volumeMounts

Description
Pod volumes to mount into the container’s filesystem. Cannot be updated.

Type
`array`

## .template.spec.initContainers\[\].volumeMounts\[\]

Description
VolumeMount describes a mounting of a Volume within a container.

Type
`object`

Required
- `name`

- `mountPath`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mountPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the container at which the volume should be mounted. Must not contain ':'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mountPropagation</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).</p>
<p>Possible enum values: - <code>"Bidirectional"</code> means that the volume in a container will receive new mounts from the host or other containers, and its own mounts will be propagated from the container to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rshared" in Linux terminology). - <code>"HostToContainer"</code> means that the volume in a container will receive new mounts from the host or other containers, but filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode is recursively applied to all mounts in the volume ("rslave" in Linux terminology). - <code>"None"</code> means that the volume in a container will not receive new mounts from the host or other containers, and filesystems mounted inside the container won’t be propagated to the host or other containers. Note that this mode corresponds to "private" in Linux terminology.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>This must match the Name of a Volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnly</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>recursiveReadOnly</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>RecursiveReadOnly specifies whether read-only mounts should be handled recursively.</p>
<p>If ReadOnly is false, this field has no meaning and must be unspecified.</p>
<p>If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.</p>
<p>If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).</p>
<p>If this field is not specified, it is treated as an equivalent of Disabled.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPath</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>subPathExpr</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive.</p></td>
</tr>
</tbody>
</table>

## .template.spec.os

Description
PodOS defines the OS parameters of a pod.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name is the name of the operating system. The currently supported values are linux and windows. Additional value may be defined in future and can be one of: <https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-configuration> Clients should expect to handle additional values and treat unrecognized values in this field as os: null |

## .template.spec.readinessGates

Description
If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: <https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates>

Type
`array`

## .template.spec.readinessGates\[\]

Description
PodReadinessGate contains the reference to a pod condition

Type
`object`

Required
- `conditionType`

| Property | Type | Description |
|----|----|----|
| `conditionType` | `string` | ConditionType refers to a condition in the pod’s condition list with matching type. |

## .template.spec.resourceClaims

Description
ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.

This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

This field is immutable.

Type
`array`

## .template.spec.resourceClaims\[\]

Description
PodResourceClaim references exactly one ResourceClaim, either directly or by naming a ResourceClaimTemplate which is then turned into a ResourceClaim for the pod.

It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name.

Type
`object`

Required
- `name`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceClaimName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod.</p>
<p>Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceClaimTemplateName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.</p>
<p>The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.</p>
<p>This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.</p>
<p>Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set.</p></td>
</tr>
</tbody>
</table>

## .template.spec.resources

Description
ResourceRequirements describes the compute resource requirements.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>claims</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.</p>
<p>This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.</p>
<p>This field is immutable. It can only be set for containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claims[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ResourceClaim references one entry in PodSpec.ResourceClaims.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>limits</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Limits describes the maximum amount of compute resources allowed. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
</tbody>
</table>

## .template.spec.resources.claims

Description
Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.

This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.

This field is immutable. It can only be set for containers.

Type
`array`

## .template.spec.resources.claims\[\]

Description
ResourceClaim references one entry in PodSpec.ResourceClaims.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. |
| `request` | `string` | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. |

## .template.spec.schedulingGates

Description
SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.

SchedulingGates can only be set at pod creation time, and be removed only afterwards.

Type
`array`

## .template.spec.schedulingGates\[\]

Description
PodSchedulingGate is associated to a Pod to guard its scheduling.

Type
`object`

Required
- `name`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the scheduling gate. Each scheduling gate must have a unique name field. |

## .template.spec.securityContext

Description
PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext. Field values of container.securityContext take precedence over field values of PodSecurityContext.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>appArmorProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AppArmorProfile defines a pod or container’s AppArmor settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fsGroup</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:</p>
<p>1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR’d with rw-rw----</p>
<p>If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fsGroupChangePolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows.</p>
<p>Possible enum values: - <code>"Always"</code> indicates that volume’s ownership and permissions should always be changed whenever volume is mounted inside a Pod. This the default behavior. - <code>"OnRootMismatch"</code> indicates that volume’s ownership and permissions will be changed only when permission and ownership of root directory does not match with expected permissions on the volume. This can help shorten the time it takes to change ownership and permissions of a volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsGroup</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsNonRoot</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>runAsUser</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seLinuxChangePolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>seLinuxChangePolicy defines how the container’s SELinux label is applied to all volumes used by the Pod. It has no effect on nodes that do not support SELinux or to volumes does not support SELinux. Valid values are "MountOption" and "Recursive".</p>
<p>"Recursive" means relabeling of all files on all Pod volumes by the container runtime. This may be slow for large volumes, but allows mixing privileged and unprivileged Pods sharing the same volume on the same node.</p>
<p>"MountOption" mounts all eligible Pod volumes with <code>-o context</code> mount option. This requires all Pods that share the same volume to use the same SELinux label. It is not possible to share the same volume among privileged and unprivileged Pods. Eligible volumes are in-tree FibreChannel and iSCSI volumes, and all CSI volumes whose CSI driver announces SELinux support by setting spec.seLinuxMount: true in their CSIDriver instance. Other volumes are always re-labelled recursively. "MountOption" value is allowed only when SELinuxMount feature gate is enabled.</p>
<p>If not specified and SELinuxMount feature gate is enabled, "MountOption" is used. If not specified and SELinuxMount feature gate is disabled, "MountOption" is used for ReadWriteOncePod volumes and "Recursive" for all other volumes.</p>
<p>This field affects only Pods that have SELinux label set, either in PodSecurityContext or in SecurityContext of all containers.</p>
<p>All Pods that use the same volume should use the same seLinuxChangePolicy, otherwise some pods can get stuck in ContainerCreating state. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seLinuxOptions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SELinuxOptions are the labels to be applied to the container</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>seccompProfile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>supplementalGroups</code></p></td>
<td style="text-align: left;"><p><code>array (integer)</code></p></td>
<td style="text-align: left;"><p>A list of groups applied to the first process run in each container, in addition to the container’s primary GID and fsGroup (if specified). If the SupplementalGroupsPolicy feature is enabled, the supplementalGroupsPolicy field determines whether these are in addition to or instead of any group memberships defined in the container image. If unspecified, no additional groups are added, though group memberships defined in the container image may still be used, depending on the supplementalGroupsPolicy field. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>supplementalGroupsPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Defines how supplemental groups of the first container processes are calculated. Valid values are "Merge" and "Strict". If not specified, "Merge" is used. (Alpha) Using the field requires the SupplementalGroupsPolicy feature gate to be enabled and the container runtime must implement support for this feature. Note that this field cannot be set when spec.os.name is windows.</p>
<p>Possible enum values: - <code>"Merge"</code> means that the container’s provided SupplementalGroups and FsGroup (specified in SecurityContext) will be merged with the primary user’s groups as defined in the container image (in /etc/group). - <code>"Strict"</code> means that the container’s provided SupplementalGroups and FsGroup (specified in SecurityContext) will be used instead of any groups defined in the container image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sysctls</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sysctls[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Sysctl defines a kernel parameter to be set</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>windowsOptions</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>WindowsSecurityContextOptions contain Windows-specific options and credentials.</p></td>
</tr>
</tbody>
</table>

## .template.spec.securityContext.appArmorProfile

Description
AppArmorProfile defines a pod or container’s AppArmor settings.

Type
`object`

Required
- `type`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement.</p>
<p>Possible enum values: - <code>"Localhost"</code> indicates that a profile pre-loaded on the node should be used. - <code>"RuntimeDefault"</code> indicates that the container runtime’s default AppArmor profile should be used. - <code>"Unconfined"</code> indicates that no AppArmor profile should be enforced.</p></td>
</tr>
</tbody>
</table>

## .template.spec.securityContext.seLinuxOptions

Description
SELinuxOptions are the labels to be applied to the container

Type
`object`

| Property | Type | Description |
|----|----|----|
| `level` | `string` | Level is SELinux level label that applies to the container. |
| `role` | `string` | Role is a SELinux role label that applies to the container. |
| `type` | `string` | Type is a SELinux type label that applies to the container. |
| `user` | `string` | User is a SELinux user label that applies to the container. |

## .template.spec.securityContext.seccompProfile

Description
SeccompProfile defines a pod/container’s seccomp profile settings. Only one profile source may be set.

Type
`object`

Required
- `type`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>localhostProfile</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type indicates which kind of seccomp profile will be applied. Valid options are:</p>
<p>Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.</p>
<p>Possible enum values: - <code>"Localhost"</code> indicates a profile defined in a file on the node should be used. The file’s location relative to &lt;kubelet-root-dir&gt;/seccomp. - <code>"RuntimeDefault"</code> represents the default container runtime seccomp profile. - <code>"Unconfined"</code> indicates no seccomp profile is applied (A.K.A. unconfined).</p></td>
</tr>
</tbody>
</table>

## .template.spec.securityContext.sysctls

Description
Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.

Type
`array`

## .template.spec.securityContext.sysctls\[\]

Description
Sysctl defines a kernel parameter to be set

Type
`object`

Required
- `name`

- `value`

| Property | Type     | Description                |
|----------|----------|----------------------------|
| `name`   | `string` | Name of a property to set  |
| `value`  | `string` | Value of a property to set |

## .template.spec.securityContext.windowsOptions

Description
WindowsSecurityContextOptions contain Windows-specific options and credentials.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `gmsaCredentialSpec` | `string` | GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. |
| `gmsaCredentialSpecName` | `string` | GMSACredentialSpecName is the name of the GMSA credential spec to use. |
| `hostProcess` | `boolean` | HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. |
| `runAsUserName` | `string` | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. |

## .template.spec.tolerations

Description
If specified, the pod’s tolerations.

Type
`array`

## .template.spec.tolerations\[\]

Description
The pod this Toleration is attached to tolerates any taint that matches the triple \<key,value,effect\> using the matching operator \<operator\>.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>effect</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.</p>
<p>Possible enum values: - <code>"NoExecute"</code> Evict any already-running pods that do not tolerate the taint. Currently enforced by NodeController. - <code>"NoSchedule"</code> Do not allow new pods to schedule onto the node unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. Enforced by the scheduler. - <code>"PreferNoSchedule"</code> Like TaintEffectNoSchedule, but the scheduler tries not to schedule new pods onto the node, rather than prohibiting new pods from scheduling onto the node entirely. Enforced by the scheduler.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.</p>
<p>Possible enum values: - <code>"Equal"</code> - <code>"Exists"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerationSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.</p></td>
</tr>
</tbody>
</table>

## .template.spec.topologySpreadConstraints

Description
TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed.

Type
`array`

## .template.spec.topologySpreadConstraints\[\]

Description
TopologySpreadConstraint specifies how to spread matching pods among the given topology.

Type
`object`

Required
- `maxSkew`

- `topologyKey`

- `whenUnsatisfiable`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>labelSelector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector"><code>LabelSelector</code></a></p></td>
<td style="text-align: left;"><p>LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>matchLabelKeys</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn’t set. Keys that don’t exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.</p>
<p>This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxSkew</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>MaxSkew describes the degree to which pods may be unevenly distributed. When <code>whenUnsatisfiable=DoNotSchedule</code>, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | | P P | P P | P | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When <code>whenUnsatisfiable=ScheduleAnyway</code>, it is used to give higher precedence to topologies that satisfy it. It’s a required field. Default value is 1 and 0 is not allowed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minDomains</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats "global minimum" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won’t schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.</p>
<p>For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | | P P | P P | P P | The number of domains is less than 5(MinDomains), so "global minimum" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeAffinityPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>NodeAffinityPolicy indicates how we will treat Pod’s nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.</p>
<p>If this value is nil, the behavior is equivalent to the Honor policy.</p>
<p>Possible enum values: - <code>"Honor"</code> means use this scheduling directive when calculating pod topology spread skew. - <code>"Ignore"</code> means ignore this scheduling directive when calculating pod topology spread skew.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeTaintsPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.</p>
<p>If this value is nil, the behavior is equivalent to the Ignore policy.</p>
<p>Possible enum values: - <code>"Honor"</code> means use this scheduling directive when calculating pod topology spread skew. - <code>"Ignore"</code> means ignore this scheduling directive when calculating pod topology spread skew.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topologyKey</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each &lt;key, value&gt; as a "bucket", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is "kubernetes.io/hostname", each Node is a domain of that topology. And, if TopologyKey is "topology.kubernetes.io/zone", each zone is a domain of that topology. It’s a required field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>whenUnsatisfiable</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>WhenUnsatisfiable indicates how to deal with a pod if it doesn’t satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location, but giving higher precedence to topologies that would help reduce the skew. A constraint is considered "Unsatisfiable" for an incoming pod if and only if every possible node assignment for that pod would violate "MaxSkew" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P | P | P | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won’t make it <strong>more</strong> imbalanced. It’s a required field.</p>
<p>Possible enum values: - <code>"DoNotSchedule"</code> instructs the scheduler not to schedule the pod when constraints are not satisfied. - <code>"ScheduleAnyway"</code> instructs the scheduler to schedule the pod even if constraints are not satisfied.</p></td>
</tr>
</tbody>
</table>

## .template.spec.volumes

Description
List of volumes that can be mounted by containers belonging to the pod. More info: <https://kubernetes.io/docs/concepts/storage/volumes>

Type
`array`

## .template.spec.volumes\[\]

Description
Volume represents a named volume in a pod that may be accessed by any container in the pod.

Type
`object`

Required
- `name`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>awsElasticBlockStore</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Persistent Disk resource in AWS.</p>
<p>An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>azureDisk</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>azureFile</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>AzureFile represents an Azure File Service mount on the host and bind mount to the pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cephfs</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cinder</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>configMap</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Adapts a ConfigMap into a volume.</p>
<p>The contents of the target ConfigMap’s Data field will be presented in a volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>csi</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a source location of a volume to mount, managed by an external CSI driver</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>downwardAPI</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>DownwardAPIVolumeSource represents a volume containing downward API info. Downward API volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>emptyDir</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ephemeral</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents an ephemeral volume that is handled by a normal storage driver.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fc</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>flexVolume</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>flocker</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gcePersistentDisk</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Persistent Disk resource in Google Compute Engine.</p>
<p>A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gitRepo</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a volume that is populated with the contents of a git repository. Git repo volumes do not support ownership management. Git repo volumes support SELinux relabeling.</p>
<p>DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod’s container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>glusterfs</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostPath</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ImageVolumeSource represents a image volume resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>iscsi</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>name of the volume. Must be a DNS_LABEL and unique within the pod. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names">https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nfs</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>persistentVolumeClaim</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PersistentVolumeClaimVolumeSource references the user’s PVC in the same namespace. This volume finds the bound PV and mounts that volume for the pod. A PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another type of volume that is owned by someone else (the system).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>photonPersistentDisk</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Photon Controller persistent disk resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>portworxVolume</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PortworxVolumeSource represents a Portworx volume resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>projected</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a projected volume source</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>quobyte</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rbd</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scaleIO</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ScaleIOVolumeSource represents a persistent ScaleIO volume</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Adapts a Secret into a volume.</p>
<p>The contents of the target Secret’s Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>storageos</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a StorageOS persistent volume resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>vsphereVolume</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents a vSphere volume resource.</p></td>
</tr>
</tbody>
</table>

## .template.spec.volumes\[\].awsElasticBlockStore

Description
Represents a Persistent Disk resource in AWS.

An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.

Type
`object`

Required
- `volumeID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |
| `partition` | `integer` | partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). |
| `readOnly` | `boolean` | readOnly value true will force the readOnly setting in VolumeMounts. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |
| `volumeID` | `string` | volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore> |

## .template.spec.volumes\[\].azureDisk

Description
AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

Type
`object`

Required
- `diskName`

- `diskURI`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>cachingMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>cachingMode is the Host Caching mode: None, Read Only, Read Write.</p>
<p>Possible enum values: - <code>"None"</code> - <code>"ReadOnly"</code> - <code>"ReadWrite"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>diskName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>diskName is the Name of the data disk in the blob storage</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>diskURI</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>diskURI is the URI of data disk in the blob storage</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fsType</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>kind</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>kind expected values are Shared: multiple blob disks per storage account Dedicated: single blob disk per storage account Managed: azure managed data disk (only in managed availability set). defaults to shared</p>
<p>Possible enum values: - <code>"Dedicated"</code> - <code>"Managed"</code> - <code>"Shared"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnly</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.</p></td>
</tr>
</tbody>
</table>

## .template.spec.volumes\[\].azureFile

Description
AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

Type
`object`

Required
- `secretName`

- `shareName`

| Property | Type | Description |
|----|----|----|
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretName` | `string` | secretName is the name of secret that contains Azure Storage Account Name and Key |
| `shareName` | `string` | shareName is the azure share Name |

## .template.spec.volumes\[\].cephfs

Description
Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.

Type
`object`

Required
- `monitors`

| Property | Type | Description |
|----|----|----|
| `monitors` | `array (string)` | monitors is Required: Monitors is a collection of Ceph monitors More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `path` | `string` | path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / |
| `readOnly` | `boolean` | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `secretFile` | `string` | secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `user` | `string` | user is optional: User is the rados user name, default is admin More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it> |

## .template.spec.volumes\[\].cephfs.secretRef

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .template.spec.volumes\[\].cinder

Description
Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.

Type
`object`

Required
- `volumeID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `volumeID` | `string` | volumeID used to identify the volume in cinder. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md> |

## .template.spec.volumes\[\].cinder.secretRef

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .template.spec.volumes\[\].configMap

Description
Adapts a ConfigMap into a volume.

The contents of the target ConfigMap’s Data field will be presented in a volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and SELinux relabeling.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `defaultMode` | `integer` | defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array` | items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | optional specify whether the ConfigMap or its keys must be defined |

## .template.spec.volumes\[\].configMap.items

Description
items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
`array`

## .template.spec.volumes\[\].configMap.items\[\]

Description
Maps a string key to a path within a volume.

Type
`object`

Required
- `key`

- `path`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

## .template.spec.volumes\[\].csi

Description
Represents a source location of a volume to mount, managed by an external CSI driver

Type
`object`

Required
- `driver`

| Property | Type | Description |
|----|----|----|
| `driver` | `string` | driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. |
| `fsType` | `string` | fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. |
| `nodePublishSecretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `readOnly` | `boolean` | readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). |
| `volumeAttributes` | `object (string)` | volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver’s documentation for supported values. |

## .template.spec.volumes\[\].csi.nodePublishSecretRef

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .template.spec.volumes\[\].downwardAPI

Description
DownwardAPIVolumeSource represents a volume containing downward API info. Downward API volumes support ownership management and SELinux relabeling.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `defaultMode` | `integer` | Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array` | Items is a list of downward API volume file |
| `items[]` | `object` | DownwardAPIVolumeFile represents information to create the file containing the pod field |

## .template.spec.volumes\[\].downwardAPI.items

Description
Items is a list of downward API volume file

Type
`array`

## .template.spec.volumes\[\].downwardAPI.items\[\]

Description
DownwardAPIVolumeFile represents information to create the file containing the pod field

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `fieldRef` | `object` | ObjectFieldSelector selects an APIVersioned field of an object. |
| `mode` | `integer` | Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | Required: Path is the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..' |
| `resourceFieldRef` | `object` | ResourceFieldSelector represents container resources (cpu, memory) and their output format |

## .template.spec.volumes\[\].downwardAPI.items\[\].fieldRef

Description
ObjectFieldSelector selects an APIVersioned field of an object.

Type
`object`

Required
- `fieldPath`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

## .template.spec.volumes\[\].downwardAPI.items\[\].resourceFieldRef

Description
ResourceFieldSelector represents container resources (cpu, memory) and their output format

Type
`object`

Required
- `resource`

| Property | Type | Description |
|----|----|----|
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | [`Quantity`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

## .template.spec.volumes\[\].emptyDir

Description
Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `medium` | `string` | medium represents what type of storage medium should back this directory. The default is "" which means to use the node’s default medium. Must be an empty string (default) or Memory. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir> |
| `sizeLimit` | [`Quantity`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir> |

## .template.spec.volumes\[\].ephemeral

Description
Represents an ephemeral volume that is handled by a normal storage driver.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `volumeClaimTemplate` | `object` | PersistentVolumeClaimTemplate is used to produce PersistentVolumeClaim objects as part of an EphemeralVolumeSource. |

## .template.spec.volumes\[\].ephemeral.volumeClaimTemplate

Description
PersistentVolumeClaimTemplate is used to produce PersistentVolumeClaim objects as part of an EphemeralVolumeSource.

Type
`object`

Required
- `spec`

| Property | Type | Description |
|----|----|----|
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. |
| `spec` | `object` | PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes |

## .template.spec.volumes\[\].ephemeral.volumeClaimTemplate.spec

Description
PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>accessModes</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>accessModes contains the desired access modes the volume should have. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1">https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dataSource</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dataSourceRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TypedObjectReference contains enough information to let you locate the typed referenced object</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>VolumeResourceRequirements describes the storage resource requirements for a volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector"><code>LabelSelector</code></a></p></td>
<td style="text-align: left;"><p>selector is a label query over volumes to consider for binding.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>storageClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>storageClassName is the name of the StorageClass required by the claim. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1">https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeAttributesClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it’s not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: <a href="https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/">https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/</a> (Beta) Using this field requires the VolumeAttributesClass feature gate to be enabled (off by default).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.</p>
<p>Possible enum values: - <code>"Block"</code> means the volume will not be formatted with a filesystem and will remain a raw block device. - <code>"Filesystem"</code> means the volume will be or is formatted with a filesystem.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeName is the binding reference to the PersistentVolume backing this claim.</p></td>
</tr>
</tbody>
</table>

## .template.spec.volumes\[\].ephemeral.volumeClaimTemplate.spec.dataSource

Description
TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |

## .template.spec.volumes\[\].ephemeral.volumeClaimTemplate.spec.dataSourceRef

Description
TypedObjectReference contains enough information to let you locate the typed referenced object

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |
| `namespace` | `string` | Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. |

## .template.spec.volumes\[\].ephemeral.volumeClaimTemplate.spec.resources

Description
VolumeResourceRequirements describes the storage resource requirements for a volume.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `limits` | [`object (Quantity)`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | [`object (Quantity)`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

## .template.spec.volumes\[\].fc

Description
Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `lun` | `integer` | lun is Optional: FC target lun number |
| `readOnly` | `boolean` | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `targetWWNs` | `array (string)` | targetWWNs is Optional: FC target worldwide names (WWNs) |
| `wwids` | `array (string)` | wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously. |

## .template.spec.volumes\[\].flexVolume

Description
FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.

Type
`object`

Required
- `driver`

| Property | Type | Description |
|----|----|----|
| `driver` | `string` | driver is the name of the driver to use for this volume. |
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. |
| `options` | `object (string)` | options is Optional: this field holds extra command options if any. |
| `readOnly` | `boolean` | readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |

## .template.spec.volumes\[\].flexVolume.secretRef

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .template.spec.volumes\[\].flocker

Description
Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `datasetName` | `string` | datasetName is Name of the dataset stored as metadata → name on the dataset for Flocker should be considered as deprecated |
| `datasetUUID` | `string` | datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset |

## .template.spec.volumes\[\].gcePersistentDisk

Description
Represents a Persistent Disk resource in Google Compute Engine.

A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling.

Type
`object`

Required
- `pdName`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `partition` | `integer` | partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `pdName` | `string` | pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk> |

## .template.spec.volumes\[\].gitRepo

Description
Represents a volume that is populated with the contents of a git repository. Git repo volumes do not support ownership management. Git repo volumes support SELinux relabeling.

DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod’s container.

Type
`object`

Required
- `repository`

| Property | Type | Description |
|----|----|----|
| `directory` | `string` | directory is the target directory name. Must not contain or start with '..'. If '.' is supplied, the volume directory will be the git repository. Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name. |
| `repository` | `string` | repository is the URL |
| `revision` | `string` | revision is the commit hash for the specified revision. |

## .template.spec.volumes\[\].glusterfs

Description
Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.

Type
`object`

Required
- `endpoints`

- `path`

| Property | Type | Description |
|----|----|----|
| `endpoints` | `string` | endpoints is the endpoint name that details Glusterfs topology. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |
| `path` | `string` | path is the Glusterfs volume path. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |
| `readOnly` | `boolean` | readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod> |

## .template.spec.volumes\[\].hostPath

Description
Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling.

Type
`object`

Required
- `path`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#hostpath">https://kubernetes.io/docs/concepts/storage/volumes#hostpath</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>type for HostPath Volume Defaults to "" More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#hostpath">https://kubernetes.io/docs/concepts/storage/volumes#hostpath</a></p>
<p>Possible enum values: - <code>""</code> For backwards compatible, leave it empty if unset - <code>"BlockDevice"</code> A block device must exist at the given path - <code>"CharDevice"</code> A character device must exist at the given path - <code>"Directory"</code> A directory must exist at the given path - <code>"DirectoryOrCreate"</code> If nothing exists at the given path, an empty directory will be created there as needed with file mode 0755, having the same group and ownership with Kubelet. - <code>"File"</code> A file must exist at the given path - <code>"FileOrCreate"</code> If nothing exists at the given path, an empty file will be created there as needed with file mode 0644, having the same group and ownership with Kubelet. - <code>"Socket"</code> A UNIX socket must exist at the given path</p></td>
</tr>
</tbody>
</table>

## .template.spec.volumes\[\].image

Description
ImageVolumeSource represents a image volume resource.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>pullPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Policy for pulling OCI objects. Possible values are: Always: the kubelet always attempts to pull the reference. Container creation will fail If the pull fails. Never: the kubelet never pulls the reference and only uses a local image or artifact. Container creation will fail if the reference isn’t present. IfNotPresent: the kubelet pulls if the reference isn’t already present on disk. Container creation will fail if the reference isn’t present and the pull fails. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise.</p>
<p>Possible enum values: - <code>"Always"</code> means that kubelet always attempts to pull the latest image. Container will fail If the pull fails. - <code>"IfNotPresent"</code> means that kubelet pulls if the image isn’t present on disk. Container will fail if the image isn’t present and the pull fails. - <code>"Never"</code> means that kubelet never pulls an image, but only uses a local image. Container will fail if the image isn’t present</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>reference</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Required: Image or artifact reference to be used. Behaves in the same way as pod.spec.containers[*].image. Pull secrets will be assembled in the same way as for the container image by looking up node credentials, SA image pull secrets, and pod spec image pull secrets. More info: <a href="https://kubernetes.io/docs/concepts/containers/images">https://kubernetes.io/docs/concepts/containers/images</a> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.</p></td>
</tr>
</tbody>
</table>

## .template.spec.volumes\[\].iscsi

Description
Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.

Type
`object`

Required
- `targetPortal`

- `iqn`

- `lun`

| Property | Type | Description |
|----|----|----|
| `chapAuthDiscovery` | `boolean` | chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication |
| `chapAuthSession` | `boolean` | chapAuthSession defines whether support iSCSI Session CHAP authentication |
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#iscsi> |
| `initiatorName` | `string` | initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface \<target portal\>:\<volume name\> will be created for the connection. |
| `iqn` | `string` | iqn is the target iSCSI Qualified Name. |
| `iscsiInterface` | `string` | iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). |
| `lun` | `integer` | lun represents iSCSI Target Lun number. |
| `portals` | `array (string)` | portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `targetPortal` | `string` | targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). |

## .template.spec.volumes\[\].iscsi.secretRef

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .template.spec.volumes\[\].nfs

Description
Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling.

Type
`object`

Required
- `server`

- `path`

| Property | Type | Description |
|----|----|----|
| `path` | `string` | path that is exported by the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |
| `readOnly` | `boolean` | readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |
| `server` | `string` | server is the hostname or IP address of the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs> |

## .template.spec.volumes\[\].persistentVolumeClaim

Description
PersistentVolumeClaimVolumeSource references the user’s PVC in the same namespace. This volume finds the bound PV and mounts that volume for the pod. A PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another type of volume that is owned by someone else (the system).

Type
`object`

Required
- `claimName`

| Property | Type | Description |
|----|----|----|
| `claimName` | `string` | claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims> |
| `readOnly` | `boolean` | readOnly Will force the ReadOnly setting in VolumeMounts. Default false. |

## .template.spec.volumes\[\].photonPersistentDisk

Description
Represents a Photon Controller persistent disk resource.

Type
`object`

Required
- `pdID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `pdID` | `string` | pdID is the ID that identifies Photon Controller persistent disk |

## .template.spec.volumes\[\].portworxVolume

Description
PortworxVolumeSource represents a Portworx volume resource.

Type
`object`

Required
- `volumeID`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified. |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `volumeID` | `string` | volumeID uniquely identifies a Portworx volume |

## .template.spec.volumes\[\].projected

Description
Represents a projected volume source

Type
`object`

| Property | Type | Description |
|----|----|----|
| `defaultMode` | `integer` | defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `sources` | `array` | sources is the list of volume projections. Each entry in this list handles one source. |
| `sources[]` | `object` | Projection that may be projected along with other supported volume types. Exactly one of these fields must be set. |

## .template.spec.volumes\[\].projected.sources

Description
sources is the list of volume projections. Each entry in this list handles one source.

Type
`array`

## .template.spec.volumes\[\].projected.sources\[\]

Description
Projection that may be projected along with other supported volume types. Exactly one of these fields must be set.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>clusterTrustBundle</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ClusterTrustBundleProjection describes how to select a set of ClusterTrustBundle objects and project their contents into the pod filesystem.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>configMap</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Adapts a ConfigMap into a projected volume.</p>
<p>The contents of the target ConfigMap’s Data field will be presented in a projected volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. Note that this is identical to a configmap volume source without the default mode.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>downwardAPI</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Represents downward API info for projecting into a projected volume. Note that this is identical to a downwardAPI volume source without the default mode.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>secret</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Adapts a secret into a projected volume.</p>
<p>The contents of the target Secret’s Data field will be presented in a projected volume as files using the keys in the Data field as the file names. Note that this is identical to a secret volume source without the default mode.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serviceAccountToken</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ServiceAccountTokenProjection represents a projected service account token volume. This projection can be used to insert a service account token into the pods runtime filesystem for use against APIs (Kubernetes API Server or otherwise).</p></td>
</tr>
</tbody>
</table>

## .template.spec.volumes\[\].projected.sources\[\].clusterTrustBundle

Description
ClusterTrustBundleProjection describes how to select a set of ClusterTrustBundle objects and project their contents into the pod filesystem.

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `labelSelector` | [`LabelSelector`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) | Select all ClusterTrustBundles that match this label selector. Only has effect if signerName is set. Mutually-exclusive with name. If unset, interpreted as "match nothing". If set but empty, interpreted as "match everything". |
| `name` | `string` | Select a single ClusterTrustBundle by object name. Mutually-exclusive with signerName and labelSelector. |
| `optional` | `boolean` | If true, don’t block pod startup if the referenced ClusterTrustBundle(s) aren’t available. If using name, then the named ClusterTrustBundle is allowed not to exist. If using signerName, then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles. |
| `path` | `string` | Relative path from the volume root to write the bundle. |
| `signerName` | `string` | Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name. The contents of all selected ClusterTrustBundles will be unified and deduplicated. |

## .template.spec.volumes\[\].projected.sources\[\].configMap

Description
Adapts a ConfigMap into a projected volume.

The contents of the target ConfigMap’s Data field will be presented in a projected volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. Note that this is identical to a configmap volume source without the default mode.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `items` | `array` | items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | optional specify whether the ConfigMap or its keys must be defined |

## .template.spec.volumes\[\].projected.sources\[\].configMap.items

Description
items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
`array`

## .template.spec.volumes\[\].projected.sources\[\].configMap.items\[\]

Description
Maps a string key to a path within a volume.

Type
`object`

Required
- `key`

- `path`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

## .template.spec.volumes\[\].projected.sources\[\].downwardAPI

Description
Represents downward API info for projecting into a projected volume. Note that this is identical to a downwardAPI volume source without the default mode.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `items` | `array` | Items is a list of DownwardAPIVolume file |
| `items[]` | `object` | DownwardAPIVolumeFile represents information to create the file containing the pod field |

## .template.spec.volumes\[\].projected.sources\[\].downwardAPI.items

Description
Items is a list of DownwardAPIVolume file

Type
`array`

## .template.spec.volumes\[\].projected.sources\[\].downwardAPI.items\[\]

Description
DownwardAPIVolumeFile represents information to create the file containing the pod field

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `fieldRef` | `object` | ObjectFieldSelector selects an APIVersioned field of an object. |
| `mode` | `integer` | Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | Required: Path is the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..' |
| `resourceFieldRef` | `object` | ResourceFieldSelector represents container resources (cpu, memory) and their output format |

## .template.spec.volumes\[\].projected.sources\[\].downwardAPI.items\[\].fieldRef

Description
ObjectFieldSelector selects an APIVersioned field of an object.

Type
`object`

Required
- `fieldPath`

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | Version of the schema the FieldPath is written in terms of, defaults to "v1". |
| `fieldPath` | `string` | Path of the field to select in the specified API version. |

## .template.spec.volumes\[\].projected.sources\[\].downwardAPI.items\[\].resourceFieldRef

Description
ResourceFieldSelector represents container resources (cpu, memory) and their output format

Type
`object`

Required
- `resource`

| Property | Type | Description |
|----|----|----|
| `containerName` | `string` | Container name: required for volumes, optional for env vars |
| `divisor` | [`Quantity`](../objects/index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Specifies the output format of the exposed resources, defaults to "1" |
| `resource` | `string` | Required: resource to select |

## .template.spec.volumes\[\].projected.sources\[\].secret

Description
Adapts a secret into a projected volume.

The contents of the target Secret’s Data field will be presented in a projected volume as files using the keys in the Data field as the file names. Note that this is identical to a secret volume source without the default mode.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `items` | `array` | items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | optional field specify whether the Secret or its key must be defined |

## .template.spec.volumes\[\].projected.sources\[\].secret.items

Description
items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
`array`

## .template.spec.volumes\[\].projected.sources\[\].secret.items\[\]

Description
Maps a string key to a path within a volume.

Type
`object`

Required
- `key`

- `path`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

## .template.spec.volumes\[\].projected.sources\[\].serviceAccountToken

Description
ServiceAccountTokenProjection represents a projected service account token volume. This projection can be used to insert a service account token into the pods runtime filesystem for use against APIs (Kubernetes API Server or otherwise).

Type
`object`

Required
- `path`

| Property | Type | Description |
|----|----|----|
| `audience` | `string` | audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver. |
| `expirationSeconds` | `integer` | expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes. |
| `path` | `string` | path is the path relative to the mount point of the file to project the token into. |

## .template.spec.volumes\[\].quobyte

Description
Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling.

Type
`object`

Required
- `registry`

- `volume`

| Property | Type | Description |
|----|----|----|
| `group` | `string` | group to map volume access to Default is no group |
| `readOnly` | `boolean` | readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false. |
| `registry` | `string` | registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes |
| `tenant` | `string` | tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin |
| `user` | `string` | user to map volume access to Defaults to serivceaccount user |
| `volume` | `string` | volume is a string that references an already created Quobyte volume by name. |

## .template.spec.volumes\[\].rbd

Description
Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling.

Type
`object`

Required
- `monitors`

- `image`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#rbd> |
| `image` | `string` | image is the rados image name. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `keyring` | `string` | keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `monitors` | `array (string)` | monitors is a collection of Ceph monitors. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `pool` | `string` | pool is the rados pool name. Default is rbd. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `readOnly` | `boolean` | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `user` | `string` | user is the rados user name. Default is admin. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it> |

## .template.spec.volumes\[\].rbd.secretRef

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .template.spec.volumes\[\].scaleIO

Description
ScaleIOVolumeSource represents a persistent ScaleIO volume

Type
`object`

Required
- `gateway`

- `system`

- `secretRef`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs". |
| `gateway` | `string` | gateway is the host address of the ScaleIO API Gateway. |
| `protectionDomain` | `string` | protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. |
| `readOnly` | `boolean` | readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `sslEnabled` | `boolean` | sslEnabled Flag enable/disable SSL communication with Gateway, default false |
| `storageMode` | `string` | storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. |
| `storagePool` | `string` | storagePool is the ScaleIO Storage Pool associated with the protection domain. |
| `system` | `string` | system is the name of the storage system as configured in ScaleIO. |
| `volumeName` | `string` | volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. |

## .template.spec.volumes\[\].scaleIO.secretRef

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .template.spec.volumes\[\].secret

Description
Adapts a Secret into a volume.

The contents of the target Secret’s Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `defaultMode` | `integer` | defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array` | items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `items[]` | `object` | Maps a string key to a path within a volume. |
| `optional` | `boolean` | optional field specify whether the Secret or its keys must be defined |
| `secretName` | `string` | secretName is the name of the secret in the pod’s namespace to use. More info: <https://kubernetes.io/docs/concepts/storage/volumes#secret> |

## .template.spec.volumes\[\].secret.items

Description
items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

Type
`array`

## .template.spec.volumes\[\].secret.items\[\]

Description
Maps a string key to a path within a volume.

Type
`object`

Required
- `key`

- `path`

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the key to project. |
| `mode` | `integer` | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `path` | `string` | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. |

## .template.spec.volumes\[\].storageos

Description
Represents a StorageOS persistent volume resource.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `readOnly` | `boolean` | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. |
| `secretRef` | `object` | LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. |
| `volumeName` | `string` | volumeName is the human-readable name of the StorageOS volume. Volume names are only unique within a namespace. |
| `volumeNamespace` | `string` | volumeNamespace specifies the scope of the volume within StorageOS. If no namespace is specified then the Pod’s namespace will be used. This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. |

## .template.spec.volumes\[\].storageos.secretRef

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

## .template.spec.volumes\[\].vsphereVolume

Description
Represents a vSphere volume resource.

Type
`object`

Required
- `volumePath`

| Property | Type | Description |
|----|----|----|
| `fsType` | `string` | fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |
| `storagePolicyID` | `string` | storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName. |
| `storagePolicyName` | `string` | storagePolicyName is the storage Policy Based Management (SPBM) profile name. |
| `volumePath` | `string` | volumePath is the path that identifies vSphere volume vmdk |

# API endpoints

The following API endpoints are available:

- `/api/v1/podtemplates`

  - `GET`: list or watch objects of kind PodTemplate

- `/api/v1/watch/podtemplates`

  - `GET`: watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.

- `/api/v1/namespaces/{namespace}/podtemplates`

  - `DELETE`: delete collection of PodTemplate

  - `GET`: list or watch objects of kind PodTemplate

  - `POST`: create a PodTemplate

- `/api/v1/watch/namespaces/{namespace}/podtemplates`

  - `GET`: watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.

- `/api/v1/namespaces/{namespace}/podtemplates/{name}`

  - `DELETE`: delete a PodTemplate

  - `GET`: read the specified PodTemplate

  - `PATCH`: partially update the specified PodTemplate

  - `PUT`: replace the specified PodTemplate

- `/api/v1/watch/namespaces/{namespace}/podtemplates/{name}`

  - `GET`: watch changes to an object of kind PodTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

## /api/v1/podtemplates

HTTP method
`GET`

Description
list or watch objects of kind PodTemplate

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PodTemplateList`](../objects/index.md#io-k8s-api-core-v1-PodTemplateList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/podtemplates

HTTP method
`GET`

Description
watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{namespace}/podtemplates

HTTP method
`DELETE`

Description
delete collection of PodTemplate

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list or watch objects of kind PodTemplate

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PodTemplateList`](../objects/index.md#io-k8s-api-core-v1-PodTemplateList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a PodTemplate

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |
| 201 - Created | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |
| 202 - Accepted | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/namespaces/{namespace}/podtemplates

HTTP method
`GET`

Description
watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/namespaces/{namespace}/podtemplates/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the PodTemplate |

Global path parameters

HTTP method
`DELETE`

Description
delete a PodTemplate

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |
| 202 - Accepted | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified PodTemplate

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified PodTemplate

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |
| 201 - Created | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified PodTemplate

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |
| 201 - Created | [`PodTemplate`](podtemplate-v1.md#podtemplate-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /api/v1/watch/namespaces/{namespace}/podtemplates/{name}

| Parameter | Type     | Description             |
|-----------|----------|-------------------------|
| `name`    | `string` | name of the PodTemplate |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind PodTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses
