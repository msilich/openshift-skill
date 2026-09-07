> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-ref_troubleshooting_workspace_startup_failures). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Diagnose workspace startup failures

Diagnose and resolve common workspace startup failures based on error symptoms and root causes. The OpenShift Dev Spaces dashboard and the Dev Workspace Operator emit error messages that indicate pod scheduling, image pull, DevWorkspace, and resource quota issues.

<span id="ref_troubleshooting-workspace-startup-failures_devspaces___pod_scheduling_errors"></span>

## [Pod scheduling errors](troubleshoot-ref_troubleshooting_workspace_startup_failures.md#ref_troubleshooting-workspace-startup-failures_devspaces___pod_scheduling_errors)

<span id="ref_troubleshooting-workspace-startup-failures_devspaces___pod_scheduling_errors__entry__1"></span><span id="ref_troubleshooting-workspace-startup-failures_devspaces___pod_scheduling_errors__entry__2"></span>

| Error message | Resolution |
|----|----|
| `FailedScheduling: 0/N nodes are available: insufficient cpu` or `insufficient memory` | The cluster does not have enough resources to schedule the workspace Pod. Free resources by stopping idle workspaces, or add nodes to the cluster. |
| `FailedScheduling: 0/N nodes are available: pod has unbound immediate PersistentVolumeClaims` | A PersistentVolumeClaim (PVC) cannot be bound. Verify that a StorageClass is configured and that the cluster has available persistent volumes. |
| `node(s) didn’t match Pod’s node affinity/selector` | The workspace Pod has a `nodeSelector` or node affinity that does not match any available node. Verify the `nodeSelector` configuration in the `CheCluster` Custom Resource. |

Table 1. Pod scheduling error messages and resolutions

<span id="ref_troubleshooting-workspace-startup-failures_devspaces___image_pull_errors"></span>

## [Image pull errors](troubleshoot-ref_troubleshooting_workspace_startup_failures.md#ref_troubleshooting-workspace-startup-failures_devspaces___image_pull_errors)

<span id="ref_troubleshooting-workspace-startup-failures_devspaces___image_pull_errors__entry__1"></span><span id="ref_troubleshooting-workspace-startup-failures_devspaces___image_pull_errors__entry__2"></span>

| Error message | Resolution |
|----|----|
| `ErrImagePull` or `ImagePullBackOff` | The container runtime cannot pull the workspace image. Verify that the image exists, the image name is correct in the devfile, and that image pull secrets are configured if the image is in a private registry. |
| `x509: certificate signed by unknown authority` | The container runtime does not trust the TLS certificate of the container registry. Import the registry Certificate Authority (CA) certificate into OpenShift Dev Spaces. |

Table 2. Image pull error messages and resolutions

<span id="ref_troubleshooting-workspace-startup-failures_devspaces___devworkspace_errors"></span>

## [DevWorkspace errors](troubleshoot-ref_troubleshooting_workspace_startup_failures.md#ref_troubleshooting-workspace-startup-failures_devspaces___devworkspace_errors)

<span id="ref_troubleshooting-workspace-startup-failures_devspaces___devworkspace_errors__entry__1"></span><span id="ref_troubleshooting-workspace-startup-failures_devspaces___devworkspace_errors__entry__2"></span>

| Error message | Resolution |
|----|----|
| `DevWorkspace failed to start: timed out waiting for DevWorkspace to be ready` | The workspace did not reach the `Running` phase within the configured timeout. Increase `startTimeoutSeconds` in the `CheCluster` Custom Resource or investigate Pod events for resource or scheduling issues. |
| `Failed to create DevWorkspace: admission webhook denied the request` | The Dev Workspace Operator webhook rejected the DevWorkspace. Verify that the Dev Workspace Operator is running and that CRDs are up to date. |
| `BadRequest` or `InfrastructureFailure` | An infrastructure-level error prevented workspace creation. Check the Dev Workspace Operator logs for details. |

Table 3. DevWorkspace error messages and resolutions

<span id="ref_troubleshooting-workspace-startup-failures_devspaces___resource_quota_errors"></span>

## [Resource quota errors](troubleshoot-ref_troubleshooting_workspace_startup_failures.md#ref_troubleshooting-workspace-startup-failures_devspaces___resource_quota_errors)

<span id="ref_troubleshooting-workspace-startup-failures_devspaces___resource_quota_errors__entry__1"></span><span id="ref_troubleshooting-workspace-startup-failures_devspaces___resource_quota_errors__entry__2"></span>

| Error message | Resolution |
|----|----|
| `exceeded quota` or `forbidden: exceeded quota` | The user namespace has a ResourceQuota that prevents creating the workspace Pod or PVC. Increase the quota or reduce the workspace resource requests in the devfile. |
| `OOMKilled` | The workspace container exceeded its memory limit and was terminated. Increase the memory limit in the devfile `components` section or in the `CheCluster` Custom Resource defaults. |

Table 4. Resource quota error messages and resolutions

**Related information**  

- [View Dev Workspace Operator metrics dashboard](observe-proc_viewing_devworkspace_operator_from_openshift_dashboard.md)
- [View OpenShift Dev Spaces server metrics dashboard](observe-proc_viewing_devspaces_server_from_openshift_dashboard.md)
- [Configure machine autoscaling](optimize-proc_configuring_machine_autoscaling.md)
- [Calculate OpenShift Dev Spaces resource requirements](plan-proc_calculating_resource_requirements.md)
