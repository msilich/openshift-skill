> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-con_optimize_overview). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# What you can optimize in OpenShift Dev Spaces

Identify the performance areas you can tune in OpenShift Dev Spaces so that you choose the right optimization strategy for your deployment.

A default OpenShift Dev Spaces installation runs all server components with a single replica and no image pre-caching. This configuration works for small teams but can cause slow workspace starts and limited capacity as usage grows. You can optimize two areas independently:

Workspace startup speed  
When a developer starts a workspace, OpenShift pulls container images from the registry. On a cold node, this can take several minutes. The Kubernetes Image Puller pre-caches images on every node so that workspaces start in seconds. For instructions on deploying and configuring the Image Puller, see Additional resources.

Platform scaling  
By default, each OpenShift Dev Spaces server component runs with one replica. You can increase replicas for high availability and configure cluster autoscaling to add worker nodes when demand exceeds capacity. For instructions on configuring autoscaling, see Additional resources.

<span id="con_optimize-overview_devspaces___when_to_optimize"></span>

## [When to optimize](optimize-con_optimize_overview.md#con_optimize-overview_devspaces___when_to_optimize)

Consider optimization when you observe:

- Workspace startup taking more than 60 seconds on nodes that have not previously run workspaces.
- Dashboard or gateway timeouts during peak usage when many developers start workspaces simultaneously.
- Workspace scheduling failures because of insufficient node resources.

<span id="con_optimize-overview_devspaces___what_affects_workspace_startup_and_platform_capacity"></span>

## [What affects workspace startup and platform capacity](optimize-con_optimize_overview.md#con_optimize-overview_devspaces___what_affects_workspace_startup_and_platform_capacity)

<span id="con_optimize-overview_devspaces___what_affects_workspace_startup_and_platform_capacity__entry__1"></span><span id="con_optimize-overview_devspaces___what_affects_workspace_startup_and_platform_capacity__entry__2"></span><span id="con_optimize-overview_devspaces___what_affects_workspace_startup_and_platform_capacity__entry__3"></span>

| Area | Control | Default |
|----|----|----|
| Image pre-caching | `CheCluster` CR field `spec.components.imagePuller.enable` | `false` (disabled) |
| Server replicas | `CheCluster` CR field `spec.components.<component>.deployment.replicas` | `1` for each component |
| Node autoscaling | `MachineAutoscaler` and `ClusterAutoscaler` custom resources | Not configured |

**Related concepts**  

- [Speed up workspace starts with image caching](optimize-assembly_caching_images_for_faster_workspace_start.md "Speed up workspace starts by deploying the Kubernetes Image Puller to pre-cache container images on cluster nodes so that workspaces start in seconds instead of minutes.")
- [Scale the platform automatically](optimize-assembly_configuring_autoscaling.md "Scale OpenShift Dev Spaces container replicas and cluster nodes automatically so that the platform grows and shrinks with developer demand.")

**Related information**  

- [Monitor OpenShift Dev Spaces platform health](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/observe_monitor/index#monitor-platform-health_observe_monitor)
