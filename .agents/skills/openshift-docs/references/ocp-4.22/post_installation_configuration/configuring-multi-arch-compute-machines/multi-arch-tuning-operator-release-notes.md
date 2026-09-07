<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Multiarch Tuning Operator (MTO) optimizes workload management within multi-architecture clusters and in single-architecture clusters transitioning to multi-architecture environments. Use the release notes to track the development of the Multiarch Tuning Operator.

# Additional resources

- [Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator](multiarch-tuning-operator.md#multiarch-tuning-operator)

# Release notes for the Multiarch Tuning Operator 1.3.3

The release notes for the Multiarch Tuning Operator 1.3.3 summarize all new features and enhancements, notable technical changes, major corrections from the previous version, and any known bugs upon general availability.

Issued: 28 July 2026

## Enhancements

- MTO has been updated to use `go` version 1.26.4.

# Release notes for the Multiarch Tuning Operator 1.3.2

The release notes for the Multiarch Tuning Operator 1.3.2 summarize all new features and enhancements, notable technical changes, major corrections from the previous version, and any known bugs upon general availability.

Issued: 13 July 2026

## Bug fixes

- Previously, when deleting a `ClusterPodPlacementConfig` with the `execFormatErrorMonitor` plugin enabled, the MTO could get stuck in a `Deleting` state because some resources were not deleted. With this update, all relevant resources are removed so that the deletion is successful. [(MULTIARCH-6186)](https://redhat.atlassian.net/browse/MULTIARCH-6186)

- Previously, a race condition between the `eNoExecEvent` daemon and the handler controller caused the `ENoExecEvent` CR to be rolled back before its status could be set, preventing any exec format errors from being recorded. With this update the conflict so events are captured successfully. [(MULTIARCH-6207)](https://redhat.atlassian.net/browse/MULTIARCH-6207)

- Previously, deleting a `ClusterPodPlacementConfig` object could tear down the webhook and operand resources while `PodPlacementConfigs` still existed, orphaning them without the resources they depend on. The deletion is now properly gated and blocks if any `PodPlacementConfig` objects remain. [(MULTIARCH-6236)](https://redhat.atlassian.net/browse/MULTIARCH-6236)

## Enhancements

- MTO has been updated to use `go` version 1.26.3.

- When the MTO is unable to connect to an image registry, the resulting error message has been improved to better explain the error. [(MULTIARCH-5541)](https://redhat.atlassian.net/browse/MULTIARCH-5541)

- The MTO API has been updated to use `runtime.NewSchemeBuilder` instead of the deprecated `scheme.Builder`. [(MULTIARCH-6272)](https://redhat.atlassian.net/browse/MULTIARCH-6272)

# Release notes for the Multiarch Tuning Operator 1.3.1

The release notes for the Multiarch Tuning Operator 1.3.1 summarize all new features and enhancements, notable technical changes, major corrections from the previous version, and any known bugs upon general availability.

Issued: 1 July 2026

## Enhancements

- MTO has been updated to use `go` version 1.25.9.

# Release notes for the Multiarch Tuning Operator 1.3.0

The release notes for the Multiarch Tuning Operator 1.3.0 summarize all new features and enhancements, notable technical changes, major corrections from the previous version, and any known bugs upon general availability.

Issued: 6 April 2026

## New features and enhancements

- With this release, after you create a `ClusterPodPlacementConfig` object, you can create namespace-scoped `PodPlacementConfig` objects for the purposes of configuring pod placement at the namespace level. `PodPlacementConfig` objects modify the behavior of the pod placement controller at the namespace level, and take precedence over the `ClusterPodPlacementConfig` object. For more information, see [Creating the namespace-scoped PodPlacementConfig object](multiarch-tuning-operator.md#multi-arch-creating-namespace-podplacement-config_multiarch-tuning-operator).

- With this release, you can specify a fallback architecture where pods are scheduled if the image inspector cannot determine the architecture of the image. For more information, see [Creating the ClusterPodPlacementConfig object](multiarch-tuning-operator.md#multi-architecture-creating-podplacement-config_multiarch-tuning-operator).

## Bug fixes

- Previously, an error could occur that led to an `ENoExecEvent` custom resource (CR) failing to be deleted. This leftover CR resulted in the failure to uninstall the `execFormatErrorMonitor` plugin. With this update, the `execFormatErrorMonitor` plugin can be uninstalled if there are leftover `ENoExecEvent` CRs. Deleting the `ClusterPodPlacementConfig` object removes all remaining CRs regardless of their state. ([MULTIARCH-5642](https://redhat.atlassian.net/browse/MULTIARCH-5642))

- Previously, the Multiarch Tuning Operator (MTO) processed images that contained attestation manifests, leading to the incorrect creation of an "unknown" architecture. Pods could fail to be scheduled when they tried to target the "unknown" architecture. With this update, the MTO does not process attestation manifests, and the "unknown" architecture is not created. ([MULTIARCH-5800](https://redhat.atlassian.net/browse/MULTIARCH-5800))

## Enhancements

- MTO has been updated to use `go` version 1.25.7.

# Release notes for the Multiarch Tuning Operator 1.2.2

The release notes for the Multiarch Tuning Operator 1.2.2 summarize all new features and enhancements, notable technical changes, major corrections from the previous version, and any known bugs upon general availability.

Issued: 6 February 2026

## Enhancements

- With this update, MTO uses the Red Hat Universal Base Image (UBI) 9 minimal image. This change improves compatibility with OpenShift Container Platform ecosystems.

- MTO has been updated to use `go` version 1.25.3, `k8s` version 1.34.1, and Operator SDK v4 version 1.33.

- The `ENoExecEvent.Status.Command` field has been removed from the `ENoExecEvent` custom resource. This field was not in use.

# Release notes for the Multiarch Tuning Operator 1.2.1

The release notes for the Multiarch Tuning Operator 1.2.1 summarize all new features and enhancements, notable technical changes, major corrections from the previous version, and any known bugs upon general availability.

Issued: 15 December 2025

## Bug fixes

- Previously, the Multiarch Tuning Operator image inspector incorrectly processed images whose registry address included a digest, tag, and port number. The port portion of the registry was incorrectly interpreted as an image tag and was trimmed, causing the inspector to construct an invalid image reference. With this update, image references that contain a digest, tag, and registry port are now correctly parsed and handled. ([MULTIARCH-5767](https://issues.redhat.com/browse/MULTIARCH-5767))

# Release notes for the Multiarch Tuning Operator 1.2.0

The release notes for the Multiarch Tuning Operator 1.2.0 summarize all new features and enhancements, notable technical changes, major corrections from the previous version, and any known bugs upon general availability.

Issued: 22 October 2025

## New features and enhancements

- With this release, you can enable the `exec format error monitor` plugin for the Multiarch Tuning Operator. This plugin detects `ENOEXEC` errors, which occur when a pod attempts to execute a binary incompatible with the node’s architecture. You enable this plugin by setting the `plugins.execFormatErrorMonitor.enabled` parameter to `true` in the `ClusterPodPlacementConfig` object. For more information, see [Creating the ClusterPodPlacementConfig object](multiarch-tuning-operator.md#multi-architecture-creating-podplacement-config_multiarch-tuning-operator).

## Bug fixes

- Previously, the Multiarch Tuning Operator incorrectly handled the Operator bundle image inspector, restricting the inspector to a single architecture, which could cause OLM to fail when installing Operators. With this update, MTO now sets the bundle image to support all architectures, allowing Operators to be successfully installed on single-architecture clusters when the Multiarch Tuning Operator is deployed. ([MULTIARCH-5546](https://issues.redhat.com/browse/MULTIARCH-5546))

- Previously, when a cluster global pull secret was changed, stale authentication information could remain in the Multiarch Tuning Operator cache. With this update, the cache is cleared whenever a cluster global pull secret is changed. ([MULTIARCH-5538](https://issues.redhat.com/browse/MULTIARCH-5538))

- Previously, the Multiarch Tuning Operator failed to process pods if an image reference contained both a tag and a digest. With this update, the image inspector prioritizes the digest if both are present. ([MULTIARCH-5584](https://issues.redhat.com/browse/MULTIARCH-5584))

- Previously, the Multiarch Tuning Operator did not respect the `.spec.registrySources.containerRuntimeSearchRegistries` field in the `config.openshift.io/Image` custom resource when a workload image did not specify a registry URL. With this update, the Operator can now handle this case, allowing workload images without an explicit registry URL to be pulled successfully. ([MULTIARCH-5611](https://issues.redhat.com/browse/MULTIARCH-5611))

- Previously, if the `ClusterPodPlacementConfig` object was deleted less than 1 second after its creation, some finalizers were not removed in time, causing certain resources to remain. With this update, all finalizers are properly deleted when the `ClusterPodPlacementConfig` object is deleted. ([MULTIARCH-5372](https://issues.redhat.com/browse/MULTIARCH-5372))

# Release notes for the Multiarch Tuning Operator 1.1.1

The release notes for the Multiarch Tuning Operator 1.1.1 summarize all new features and enhancements, notable technical changes, major corrections from the previous version, and any known bugs upon general availability.

Issued: 27 May 2025

## Bug fixes

- Previously, the pod placement operand did not support authenticating registries using wildcard entries in the hostname of their pull secret. This caused inconsistent behavior with Kubelet when pulling images, because Kubelet supported wildcard entries while the operand required exact hostname matches. As a result, image pulls could fail unexpectedly when registries used wildcard hostnames.

  With this release, the pod placement operand supports pull secrets that include wildcard hostnames, ensuring consistent and reliable image authentication and pulling.

- Previously, when image inspection failed after all retries and the `nodeAffinityScoring` plugin was enabled, the pod placement operand applied incorrect `nodeAffinityScoring` labels.

  With this release, the operand sets `nodeAffinityScoring` labels correctly, even when image inspection fails. The operand now applies these labels independently of the required affinity process to ensure accurate and consistent scheduling.

# Release notes for the Multiarch Tuning Operator 1.1.0

The release notes for the Multiarch Tuning Operator 1.1.0 summarize all new features and enhancements, notable technical changes, major corrections from the previous version, and any known bugs upon general availability.

Issued: 18 March 2024

## New features and enhancements

- The Multiarch Tuning Operator is now supported on managed offerings, including ROSA with Hosted Control Planes (HCP) and other HCP environments.

- With this release, you can configure architecture-aware workload scheduling by using the new `plugins` field in the `ClusterPodPlacementConfig` object. You can use the `plugins.nodeAffinityScoring` field to set architecture preferences for pod placement. If you enable the `nodeAffinityScoring` plugin, the scheduler first filters out nodes that do not meet the pod requirements. The scheduler then prioritizes the remaining nodes based on the architecture scores defined in the `nodeAffinityScoring.platforms` field.

## Bug fixes

- With this release, the Multiarch Tuning Operator does not update the `nodeAffinity` field for pods that are managed by a daemon set. ([OCPBUGS-45885](https://issues.redhat.com/browse/OCPBUGS-45885))

# Release notes for the Multiarch Tuning Operator 1.0.0

The release notes for the Multiarch Tuning Operator 1.0.0 summarize all new features and enhancements, notable technical changes, major corrections from the previous version, and any known bugs upon general availability.

Issued: 31 October 2024

## New features and enhancements

- With this release, the Multiarch Tuning Operator supports custom network scenarios and cluster-wide custom registries configurations.

- With this release, you can identify pods based on their architecture compatibility by using the pod labels that the Multiarch Tuning Operator adds to newly created pods.

- With this release, you can monitor the behavior of the Multiarch Tuning Operator by using the metrics and alerts that are registered in the Cluster Monitoring Operator.
