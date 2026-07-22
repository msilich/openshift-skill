<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can review the following release notes to learn about changes in the Custom Metrics Autoscaler Operator version 2.19.0-2. The release notes for the Custom Metrics Autoscaler Operator for Red Hat OpenShift describe new features and enhancements, deprecated features, and known issues.

The Custom Metrics Autoscaler Operator uses the Kubernetes-based Event Driven Autoscaler (KEDA) and is built on top of the OpenShift Container Platform horizontal pod autoscaler (HPA).

> [!NOTE]
> The Custom Metrics Autoscaler Operator for Red Hat OpenShift is provided as an installable component, with a distinct release cycle from the core OpenShift Container Platform. The [Red Hat OpenShift Container Platform Life Cycle Policy](https://access.redhat.com/support/policy/updates/openshift#cma) outlines release compatibility.

# Supported versions

The following table defines the Custom Metrics Autoscaler Operator versions for each OpenShift Container Platform version.

| Version  | OpenShift Container Platform version | General availability |
|----------|--------------------------------------|----------------------|
| 2.19.0-2 | 4.21                                 | General availability |
| 2.19.0-2 | 4.20                                 | General availability |
| 2.19.0-2 | 4.19                                 | General availability |
| 2.19.0-2 | 4.18                                 | General availability |
| 2.19.0-2 | 4.17                                 | General availability |
| 2.19.0-2 | 4.16                                 | General availability |
| 2.19.0-2 | 4.15                                 | General availability |
| 2.19.0-2 | 4.14                                 | General availability |
| 2.19.0-2 | 4.13                                 | General availability |
| 2.19.0-2 | 4.12                                 | General availability |

# Custom Metrics Autoscaler Operator 2.19.0-2 release notes

Issued: 09 July 2026

You can review the following release notes to learn about the bug fixes provided in this release of the Custom Metrics Autoscaler Operator.

The following advisory is available for the Custom Metrics Autoscaler Operator:

- [RHBA-2026:37467](https://access.redhat.com/errata/RHBA-2026:37467)

> [!IMPORTANT]
> Before installing this version of the Custom Metrics Autoscaler Operator, remove any previously installed Technology Preview versions or the community-supported version of Kubernetes-based Event Driven Autoscaler (KEDA).

Bug fixes
- Before this update, the addition of an immutable label in the deployment selector that was not compatible with the existing deployment was causing automatic upgrades from Custom Metrics Autoscaler Operator version 2.18.1-2 to version 2.19.0-1 to fail. With the fix, automatic upgrades from version 2.18.1-2 to version 2.19.0-2 succeed without manual intervention. ([OCPBUGS-91950](https://redhat.atlassian.net/browse/OCPBUGS-91950))
