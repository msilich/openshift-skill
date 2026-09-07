<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can view events in OpenShift Container Platform, which are based on events that happen to API objects in an OpenShift Container Platform cluster.

# Understanding events

Review the following information to learn how OpenShift Container Platform uses *events* to record information about real-world events in a resource-agnostic manner. Events also allow developers and administrators to consume information about system components in a unified way.

# Viewing events using the CLI

You can get a list of events in a given project by using the CLI.

<div>

<div class="title">

Procedure

</div>

- View events in a project by using a command similar to the following:

  ``` terminal
  $ oc get events [-n <project>]
  ```

  where:

  `project`
  Specifies the name of the project.

  For example:

  ``` terminal
  $ oc get events -n openshift-config
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  LAST SEEN   TYPE      REASON                   OBJECT                      MESSAGE
  97m         Normal    Scheduled                pod/dapi-env-test-pod       Successfully assigned openshift-config/dapi-env-test-pod to ip-10-0-171-202.ec2.internal
  97m         Normal    Pulling                  pod/dapi-env-test-pod       pulling image "gcr.io/google_containers/busybox"
  97m         Normal    Pulled                   pod/dapi-env-test-pod       Successfully pulled image "gcr.io/google_containers/busybox"
  97m         Normal    Created                  pod/dapi-env-test-pod       Created container
  9m5s        Warning   FailedCreatePodSandBox   pod/dapi-volume-test-pod    Failed create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_dapi-volume-test-pod_openshift-config_6bc60c1f-452e-11e9-9140-0eec59c23068_0(748c7a40db3d08c07fb4f9eba774bd5effe5f0d5090a242432a73eee66ba9e22): Multus: Err adding pod to network "ovn-kubernetes": cannot set "ovn-kubernetes" ifname to "eth0": no netns: failed to Statfs "/proc/33366/ns/net": no such file or directory
  8m31s       Normal    Scheduled                pod/dapi-volume-test-pod    Successfully assigned openshift-config/dapi-volume-test-pod to ip-10-0-171-202.ec2.internal
  #...
  ```

  </div>

- View events in your project from the OpenShift Container Platform console:

  1.  Launch the OpenShift Container Platform console.

  2.  Click **Home** → **Events** and select your project.

  3.  Move to resource that you want to see events. For example: **Home** → **Projects** → \<project-name\> → \<resource-name\>.

      Many objects, such as pods and deployments, also have an **Events** tab, which shows events related to that object.

</div>

# List of events

Review the information in this section to learn about OpenShift Container Platform events.

| Name               | Description                          |
|--------------------|--------------------------------------|
| `FailedValidation` | Failed pod configuration validation. |

Configuration events

| Name | Description |
|----|----|
| `BackOff` | Back-off restarting failed the container. |
| `Created` | Container created. |
| `Failed` | Pull/Create/Start failed. |
| `Killing` | Killing the container. |
| `Started` | Container started. |
| `Preempting` | Preempting other pods. |
| `ExceededGracePeriod` | Container runtime did not stop the pod within specified grace period. |

Container events

| Name        | Description             |
|-------------|-------------------------|
| `Unhealthy` | Container is unhealthy. |

Health events

| Name | Description |
|----|----|
| `BackOff` | Back off Ctr Start, image pull. |
| `ErrImageNeverPull` | The image’s **NeverPull Policy** is violated. |
| `Failed` | Failed to pull the image. |
| `InspectFailed` | Failed to inspect the image. |
| `Pulled` | Successfully pulled the image or the container image is already present on the machine. |
| `Pulling` | Pulling the image. |

Image events

| Name                  | Description             |
|-----------------------|-------------------------|
| `FreeDiskSpaceFailed` | Free disk space failed. |
| `InvalidDiskCapacity` | Invalid disk capacity.  |

Image Manager events

| Name | Description |
|----|----|
| `FailedMount` | Volume mount failed. |
| `HostNetworkNotSupported` | Host network not supported. |
| `HostPortConflict` | Host/port conflict. |
| `KubeletSetupFailed` | Kubelet setup failed. |
| `NilShaper` | Undefined shaper. |
| `NodeNotReady` | Node is not ready. |
| `NodeNotSchedulable` | Node is not schedulable. |
| `NodeReady` | Node is ready. |
| `NodeSchedulable` | Node is schedulable. |
| `NodeSelectorMismatching` | Node selector mismatch. |
| `OutOfDisk` | Out of disk. |
| `Rebooted` | Node rebooted. |
| `Starting` | Starting kubelet. |
| `FailedAttachVolume` | Failed to attach volume. |
| `FailedDetachVolume` | Failed to detach volume. |
| `VolumeResizeFailed` | Failed to expand/reduce volume. |
| `VolumeResizeSuccessful` | Successfully expanded/reduced volume. |
| `FileSystemResizeFailed` | Failed to expand/reduce file system. |
| `FileSystemResizeSuccessful` | Successfully expanded/reduced file system. |
| `FailedUnMount` | Failed to unmount volume. |
| `FailedMapVolume` | Failed to map a volume. |
| `FailedUnmapDevice` | Failed unmaped device. |
| `AlreadyMountedVolume` | Volume is already mounted. |
| `SuccessfulDetachVolume` | Volume is successfully detached. |
| `SuccessfulMountVolume` | Volume is successfully mounted. |
| `SuccessfulUnMountVolume` | Volume is successfully unmounted. |
| `ContainerGCFailed` | Container garbage collection failed. |
| `ImageGCFailed` | Image garbage collection failed. |
| `FailedNodeAllocatableEnforcement` | Failed to enforce System Reserved Cgroup limit. |
| `NodeAllocatableEnforced` | Enforced System Reserved Cgroup limit. |
| `UnsupportedMountOption` | Unsupported mount option. |
| `SandboxChanged` | Pod sandbox changed. |
| `FailedCreatePodSandBox` | Failed to create pod sandbox. |
| `FailedPodSandBoxStatus` | Failed pod sandbox status. |

Node events

| Name         | Description      |
|--------------|------------------|
| `FailedSync` | Pod sync failed. |

Pod worker events

| Name        | Description                                               |
|-------------|-----------------------------------------------------------|
| `SystemOOM` | There is an OOM (out of memory) situation on the cluster. |

System Events

| Name                       | Description                          |
|----------------------------|--------------------------------------|
| `FailedKillPod`            | Failed to stop a pod.                |
| `FailedCreatePodContainer` | Failed to create a pod container.    |
| `Failed`                   | Failed to make pod data directories. |
| `NetworkNotReady`          | Network is not ready.                |
| `FailedCreate`             | Error creating: `<error-msg>`.       |
| `SuccessfulCreate`         | Created pod: `<pod-name>`.           |
| `FailedDelete`             | Error deleting: `<error-msg>`.       |
| `SuccessfulDelete`         | Deleted pod: `<pod-id>`.             |

Pod events

| Name | Description |
|----|----|
| SelectorRequired | Selector is required. |
| `InvalidSelector` | Could not convert selector into a corresponding internal selector object. |
| `FailedGetObjectMetric` | HPA was unable to compute the replica count. |
| `InvalidMetricSourceType` | Unknown metric source type. |
| `ValidMetricFound` | HPA was able to successfully calculate a replica count. |
| `FailedConvertHPA` | Failed to convert the given HPA. |
| `FailedGetScale` | HPA controller was unable to get the target’s current scale. |
| `SucceededGetScale` | HPA controller was able to get the target’s current scale. |
| `FailedComputeMetricsReplicas` | Failed to compute desired number of replicas based on listed metrics. |
| `FailedRescale` | New size: `<size>`; reason: `<msg>`; error: `<error-msg>`. |
| `SuccessfulRescale` | New size: `<size>`; reason: `<msg>`. |
| `FailedUpdateStatus` | Failed to update status. |

Horizontal Pod AutoScaler events

| Name | Description |
|----|----|
| `FailedBinding` | There are no persistent volumes available and no storage class is set. |
| `VolumeMismatch` | Volume size or class is different from what is requested in claim. |
| `VolumeFailedRecycle` | Error creating recycler pod. |
| `VolumeRecycled` | Occurs when volume is recycled. |
| `RecyclerPod` | Occurs when pod is recycled. |
| `VolumeDelete` | Occurs when volume is deleted. |
| `VolumeFailedDelete` | Error when deleting the volume. |
| `ExternalProvisioning` | Occurs when volume for the claim is provisioned either manually or via external software. |
| `ProvisioningFailed` | Failed to provision volume. |
| `ProvisioningCleanupFailed` | Error cleaning provisioned volume. |
| `ProvisioningSucceeded` | Occurs when the volume is provisioned successfully. |
| `WaitForFirstConsumer` | Delay binding until pod scheduling. |

Volume events

| Name                    | Description                   |
|-------------------------|-------------------------------|
| `FailedPostStartHook`   | Handler failed for pod start. |
| `FailedPreStopHook`     | Handler failed for pre-stop.  |
| `UnfinishedPreStopHook` | Pre-stop hook unfinished.     |

Lifecycle hooks

| Name | Description |
|----|----|
| `DeploymentCancellationFailed` | Failed to cancel deployment. |
| `DeploymentCancelled` | Canceled deployment. |
| `DeploymentCreated` | Created new replication controller. |
| `IngressIPRangeFull` | No available Ingress IP to allocate to service. |

Deployments

| Name | Description |
|----|----|
| `FailedScheduling` | Failed to schedule pod: `<pod-namespace>/<pod-name>`. This event is raised for multiple reasons, for example: `AssumePodVolumes` failed, Binding rejected etc. |
| `Preempted` | By `<preemptor-namespace>/<preemptor-name>` on node `<node-name>`. |
| `Scheduled` | Successfully assigned `<pod-name>` to `<node-name>`. |

Scheduler events

| Name | Description |
|----|----|
| `SelectingAll` | This daemon set is selecting all pods. A non-empty selector is required. |
| `FailedPlacement` | Failed to place pod on `<node-name>`. |
| `FailedDaemonPod` | Found failed daemon pod `<pod-name>` on node `<node-name>`, will try to kill it. |

Daemon set events

| Name | Description |
|----|----|
| `CreatingLoadBalancerFailed` | Error creating load balancer. |
| `DeletingLoadBalancer` | Deleting load balancer. |
| `EnsuringLoadBalancer` | Ensuring load balancer. |
| `EnsuredLoadBalancer` | Ensured load balancer. |
| `UnAvailableLoadBalancer` | There are no available nodes for `LoadBalancer` service. |
| `LoadBalancerSourceRanges` | Lists the new `LoadBalancerSourceRanges`. For example, `<old-source-range> → <new-source-range>`. |
| `LoadbalancerIP` | Lists the new IP address. For example, `<old-ip> → <new-ip>`. |
| `ExternalIP` | Lists external IP address. For example, `Added: <external-ip>`. |
| `UID` | Lists the new UID. For example, `<old-service-uid> → <new-service-uid>`. |
| `ExternalTrafficPolicy` | Lists the new `ExternalTrafficPolicy`. For example, `<old-policy> → <new-policy>`. |
| `HealthCheckNodePort` | Lists the new `HealthCheckNodePort`. For example, `<old-node-port> → new-node-port>`. |
| `UpdatedLoadBalancer` | Updated load balancer with new hosts. |
| `LoadBalancerUpdateFailed` | Error updating load balancer with new hosts. |
| `DeletingLoadBalancer` | Deleting load balancer. |
| `DeletingLoadBalancerFailed` | Error deleting load balancer. |
| `DeletedLoadBalancer` | Deleted load balancer. |

LoadBalancer service events
