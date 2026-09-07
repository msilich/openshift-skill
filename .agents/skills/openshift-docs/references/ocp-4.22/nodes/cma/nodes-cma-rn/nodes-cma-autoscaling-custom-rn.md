<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can review the following release notes to learn about changes in the Custom Metrics Autoscaler Operator version 2.19.0-3. The release notes for the Custom Metrics Autoscaler Operator for Red Hat OpenShift describe new features and enhancements, deprecated features, and known issues.

The Custom Metrics Autoscaler Operator uses the Kubernetes-based Event Driven Autoscaler (KEDA) and is built on top of the OpenShift Container Platform horizontal pod autoscaler (HPA).

> [!NOTE]
> The Custom Metrics Autoscaler Operator for Red Hat OpenShift is provided as an installable component, with a distinct release cycle from the core OpenShift Container Platform. The [Red Hat OpenShift Container Platform Life Cycle Policy](https://access.redhat.com/support/policy/updates/openshift#cma) outlines release compatibility.

# Supported versions

The following table defines the Custom Metrics Autoscaler Operator versions for each OpenShift Container Platform version.

| Version  | OpenShift Container Platform version | General availability |
|----------|--------------------------------------|----------------------|
| 2.19.0-3 | 4.21                                 | General availability |
| 2.19.0-3 | 4.20                                 | General availability |
| 2.19.0-3 | 4.19                                 | General availability |
| 2.19.0-3 | 4.18                                 | General availability |
| 2.19.0-3 | 4.17                                 | General availability |
| 2.19.0-3 | 4.16                                 | General availability |
| 2.19.0-3 | 4.15                                 | General availability |
| 2.19.0-3 | 4.14                                 | General availability |
| 2.19.0-3 | 4.13                                 | General availability |
| 2.19.0-3 | 4.12                                 | General availability |

# Custom Metrics Autoscaler Operator 2.19.0-3 release notes

Issued: 03 September 2026

You can review the following release notes to learn about the bug fixes provided in this release of the Custom Metrics Autoscaler Operator.

The following advisory is available for the Custom Metrics Autoscaler Operator:

- [RHSA-2026:62866](https://access.redhat.com/errata/RHSA-2026:62866)

> [!IMPORTANT]
> Before installing this version of the Custom Metrics Autoscaler Operator, remove any previously installed Technology Preview versions or the community-supported version of Kubernetes-based Event Driven Autoscaler (KEDA).

Bug fixes
- Before this update, the `default` scaling strategy for scaled jobs was missing. With this fix, the `default` strategy has been added back to the `scaledjobs` custom resource. As a result, you can select the default strategy with scaled jobs. ([OCPBUGS-98657](https://redhat.atlassian.net/browse/OCPBUGS-98657))

- Before this update, the `installAdmissionWebhooks` function was incorrectly using `Operator.Volumes` and `Operator.VolumeMounts` parameters instead of the `AdmissionWebhooks.Volumes` and `AdmissionWebhooks.VolumeMounts` parameters. This caused user-configured volumes for admission webhooks to not be applied correctly, because the Operator’s volumes were used instead. With the fix, the Custom Metrics Autoscaler Operator correctly configures admission webhooks, ensuring the proper deployment of user-defined volumes and volume mounts. ([OCPBUGS-84045](https://redhat.atlassian.net/browse/OCPBUGS-84045))
