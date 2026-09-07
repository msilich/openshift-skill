<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure application pods to ensure workload availability during OpenShift Container Platform updates. For example, use deployment strategies, pod disruption budgets, anti-affinity rules, and health probes to maintain high availability and prevent service disruption. In the telecommunications industry, most containerized network function (CNF) vendors follow the guidance in Red Hat best practices for Kubernetes to ensure that the cluster can schedule pods properly during an upgrade.

> [!IMPORTANT]
> Always deploy pods in groups by using `Deployment` resources. `Deployment` resources spread the workload across all of the available pods ensuring there is no single point of failure. When a pod that is managed by a `Deployment` resource is deleted, a new pod takes its place automatically.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat best practices for Kubernetes](https://redhat-best-practices-for-k8s.github.io/guide/)

</div>

# Ensuring that workloads run uninterrupted with pod disruption budgets

To prevent interruption of upgrading worker nodes, configure the pod disruption budget properly. For more information, see *Additional resources*.

<div>

<div class="title">

Additional resources

</div>

- [Specifying the number of pods that must be up with pod disruption budgets](../../cluster-tasks.md#nodes-pods-pod-disruption-configuring_post-install-cluster-tasks)

- [Configuring an OpenShift Container Platform cluster for pods](../../../nodes/pods/nodes-pods-configuring.md#nodes-pods-pod-disruption-configuring_nodes-pods-configuring)

- [Pod preemption and other scheduler settings](../../../nodes/pods/nodes-pods-priority.md#priority-preemption-other_nodes-pods-priority)

</div>

# Ensuring that pods do not run on the same cluster node

High availability in Kubernetes requires duplicate processes to be running on separate nodes in the cluster. This ensures that the application continues to run even if one node becomes unavailable. In OpenShift Container Platform, processes can be automatically duplicated in separate pods in a deployment. You configure anti-affinity in the `Pod` resource to ensure that the pods in a deployment do not run on the same cluster node.

During an update, setting pod anti-affinity ensures that pods are distributed evenly across nodes in the cluster. This means that node reboots are easier during an update. For example, if there are 4 pods from a single deployment on a node, and the pod disruption budget is set to only allow 1 pod to be deleted at a time, then it will take 4 times as long for that node to reboot. Setting pod anti-affinity spreads pods across the cluster to prevent such occurrences.

<div>

<div class="title">

Additional resources

</div>

- [Configuring a pod affinity rule](../../../nodes/scheduling/nodes-scheduler-pod-affinity.md#nodes-scheduler-pod-affinity-configuring_nodes-scheduler-pod-affinity)

</div>

# Application liveness, readiness, and startup probes

You can use liveness, readiness and startup probes to check the health of your live application containers before you schedule an update. These are very useful tools to use with pods that are dependent upon keeping state for their application containers.

Liveness health check
Determines if a container is running. If the liveness probe fails for a container, the pod responds based on the restart policy.

Readiness probe
Determines if a container is ready to accept service requests. If the readiness probe fails for a container, the kubelet removes the container from the list of available service endpoints.

Startup probe
A startup probe indicates whether the application within a container is started. All other probes are disabled until the startup succeeds. If the startup probe does not succeed, the kubelet stops the container, and the container is subject to the pod `restartPolicy` setting.

<div>

<div class="title">

Additional resources

</div>

- [Understanding health checks](../../../applications/application-health.md#application-health-about_application-health)

</div>
