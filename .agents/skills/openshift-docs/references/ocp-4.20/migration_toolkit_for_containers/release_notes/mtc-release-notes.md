<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The release notes for Migration Toolkit for Containers (MTC) describe new features and enhancements, deprecated features, and known issues.

The MTC enables you to migrate application workloads between OpenShift Container Platform clusters at the granularity of a namespace.

MTC provides a web console and an API, based on Kubernetes custom resources, to help you control the migration and minimize application downtime.

For information on the support policy for MTC, see [OpenShift Application and Cluster Migration Solutions](https://access.redhat.com/support/policy/updates/openshift#app_migration), part of the *Red Hat OpenShift Container Platform Life Cycle Policy*.

# Migration Toolkit for Containers 1.8.16 release notes

Migration Toolkit for Containers (MTC) 1.8.16 is a Container Grade Only (CGO) release, which is released to refresh the health grades of the containers. No code was changed in the product itself compared to that of MTC 1.8.15. MTC 1.8.16 fixes several Common Vulnerabilities and Exposures (CVEs).

## Resolved issues

Migration Toolkit for Containers (MTC) 1.8.16 fixes the following CVEs
- [CVE-2025-7783](https://access.redhat.com/security/cve/cve-2025-7783)

- [CVE-2025-12816](https://access.redhat.com/security/cve/cve-2025-12816)

- [CVE-2025-13465](https://access.redhat.com/security/cve/cve-2025-13465)

- [CVE-2025-15284](https://access.redhat.com/security/cve/cve-2025-15284)

- [CVE-2025-52881](https://access.redhat.com/security/cve/cve-2025-52881)

- [CVE-2025-58183](https://access.redhat.com/security/cve/cve-2025-58183)

- [CVE-2025-58754](https://access.redhat.com/security/cve/cve-2025-58754)

- [CVE-2025-61726](https://access.redhat.com/security/cve/cve-2025-61726)

- [CVE-2025-61729](https://access.redhat.com/security/cve/cve-2025-61729)

- [CVE-2025-62718](https://access.redhat.com/security/cve/cve-2025-62718)

- [CVE-2025-66031](https://access.redhat.com/security/cve/cve-2025-66031)

- [CVE-2025-66418](https://access.redhat.com/security/cve/cve-2025-66418)

- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)

- [CVE-2025-66506](https://access.redhat.com/security/cve/cve-2025-66506)

- [CVE-2025-68121](https://access.redhat.com/security/cve/cve-2025-68121)

- [CVE-2025-69223](https://access.redhat.com/security/cve/cve-2025-69223)

- [CVE-2025-69227](https://access.redhat.com/security/cve/cve-2025-69227)

- [CVE-2025-69228](https://access.redhat.com/security/cve/cve-2025-69228)

- [CVE-2026-4800](https://access.redhat.com/security/cve/cve-2026-4800)

- [CVE-2026-6322](https://access.redhat.com/security/cve/cve-2026-6322)

- [CVE-2026-9277](https://access.redhat.com/security/cve/cve-2026-9277)

- [CVE-2026-9595](https://access.redhat.com/security/cve/cve-2026-9595)

- [CVE-2026-12143](https://access.redhat.com/security/cve/cve-2026-12143)

- [CVE-2026-13149](https://access.redhat.com/security/cve/cve-2026-13149)

- [CVE-2026-13676](https://access.redhat.com/security/cve/cve-2026-13676)

- [CVE-2026-21441](https://access.redhat.com/security/cve/cve-2026-21441)

- [CVE-2026-22029](https://access.redhat.com/security/cve/cve-2026-22029)

- [CVE-2026-23490](https://access.redhat.com/security/cve/cve-2026-23490)

- [CVE-2026-23745](https://access.redhat.com/security/cve/cve-2026-23745)

- [CVE-2026-25679](https://access.redhat.com/security/cve/cve-2026-25679)

- [CVE-2026-25681](https://access.redhat.com/security/cve/cve-2026-25681)

- [CVE-2026-27136](https://access.redhat.com/security/cve/cve-2026-27136)

- [CVE-2026-27137](https://access.redhat.com/security/cve/cve-2026-27137)

- [CVE-2026-29063](https://access.redhat.com/security/cve/cve-2026-29063)

- [CVE-2026-30922](https://access.redhat.com/security/cve/cve-2026-30922)

- [CVE-2026-32280](https://access.redhat.com/security/cve/cve-2026-32280)

- [CVE-2026-32281](https://access.redhat.com/security/cve/cve-2026-32281)

- [CVE-2026-32283](https://access.redhat.com/security/cve/cve-2026-32283)

- [CVE-2026-33186](https://access.redhat.com/security/cve/cve-2026-33186)

- [CVE-2026-33810](https://access.redhat.com/security/cve/cve-2026-33810)

- [CVE-2026-33811](https://access.redhat.com/security/cve/cve-2026-33811)

- [CVE-2026-34986](https://access.redhat.com/security/cve/cve-2026-34986)

- [CVE-2026-39820](https://access.redhat.com/security/cve/cve-2026-39820)

- [CVE-2026-39821](https://access.redhat.com/security/cve/cve-2026-39821)

- [CVE-2026-40895](https://access.redhat.com/security/cve/cve-2026-40895)

- [CVE-2026-42264](https://access.redhat.com/security/cve/cve-2026-42264)

- [CVE-2026-42338](https://access.redhat.com/security/cve/cve-2026-42338)

- [CVE-2026-42499](https://access.redhat.com/security/cve/cve-2026-42499)

- [CVE-2026-44486](https://access.redhat.com/security/cve/cve-2026-44486)

- [CVE-2026-44487](https://access.redhat.com/security/cve/cve-2026-44487)

- [CVE-2026-44488](https://access.redhat.com/security/cve/cve-2026-44488)

- [CVE-2026-44492](https://access.redhat.com/security/cve/cve-2026-44492)

- [CVE-2026-44494](https://access.redhat.com/security/cve/cve-2026-44494)

- [CVE-2026-44495](https://access.redhat.com/security/cve/cve-2026-44495)

- [CVE-2026-44496](https://access.redhat.com/security/cve/cve-2026-44496)

- [CVE-2026-45736](https://access.redhat.com/security/cve/cve-2026-45736)

- [CVE-2026-45822](https://access.redhat.com/security/cve/cve-2026-45822)

- [CVE-2026-48779](https://access.redhat.com/security/cve/cve-2026-48779)

# Migration Toolkit for Containers 1.8.15 release notes

Migration Toolkit for Containers (MTC) 1.8.15 is a Container Grade Only (CGO) release, which is released to refresh the health grades of the containers. No code was changed in the product itself compared to that of MTC 1.8.14. MTC 1.8.15 fixes several Common Vulnerabilities and Exposures (CVEs).

## Resolved issues

Migration Toolkit for Containers (MTC) 1.8.15 fixes the following CVEs
- [CVE-2026-25639](https://access.redhat.com/security/cve/cve-2026-25639)

- [CVE-2026-40175](https://access.redhat.com/security/cve/cve-2026-40175)

- [CVE-2026-42033](https://access.redhat.com/security/cve/cve-2026-42033)

- [CVE-2026-42035](https://access.redhat.com/security/cve/cve-2026-42035)

- [CVE-2026-42039](https://access.redhat.com/security/cve/cve-2026-42039)

- [CVE-2026-42041](https://access.redhat.com/security/cve/cve-2026-42041)

- [CVE-2026-42043](https://access.redhat.com/security/cve/cve-2026-42043)

- [CVE-2026-42044](https://access.redhat.com/security/cve/cve-2026-42044)

# Migration Toolkit for Containers 1.8.14 release notes

Migration Toolkit for Containers (MTC) 1.8.14 release notes list resolved issues.

MTC 1.8.14 restores full support for OpenShift Container Platform versions 4.12 and 4.13. This release realigns the MTC upgrade path across all supported OpenShift versions, ensuring a stable foundation for future updates.

## Resolved issues

Fixed incompatible Operator versions due to an incorrect OpenShift Container Platform 4.18 catalog update
Before this update, the OpenShift Container Platform 4.18 Operators catalog was accidentally pushed to 4.12 and later versions. As a consequence, clusters on OpenShift Container Platform versions 4.12-4.17 installed incompatible Operator versions. With this release, MTC 1.8 support is extended to OpenShift Container Platform 4.12 and 4.13. As a result, the bug fix updates the MTC Operator to the correct version in OpenShift Container Platform catalogs to provide updates for impacted customers.

If you are on OpenShift Container Platform 4.12 and 4.13, upgrade to MTC 1.8.14 as soon as possible to ensure continued support and access to future security patches.

[MIG-1874](https://issues.redhat.com/browse/MIG-1874)

MTC Operator includes latest `rsync` version
Before this update, the MTC Operator mistakenly included an older version of the `rsync` package. This release updates the MTC Operator to include the latest `rsync` package.

[MIG-1876](https://issues.redhat.com/browse/MIG-1876)

# Migration Toolkit for Containers 1.8.13 release notes

Migration Toolkit for Containers (MTC) 1.8.13 is a Container Grade Only (CGO) release, which is released to refresh the health grades of the containers. No code was changed in the product itself compared to that of MTC 1.8.12.

## Enhancements

MTC 1.8.13 restricts cluster upgrades beyond OpenShift Container Platform 4.20
With this update, MTC prevents OpenShift Container Platform clusters from upgrading to version 4.21 and later to maintain compatibility and stability. To upgrade your cluster beyond version 4.20, uninstall MTC first. For instructions on how to uninstall MTC, see [Uninstalling MTC and deleting resources](../installing-mtc.md#migration-uninstalling-mtc-clean-up_installing-mtc).

[(MIG-1872)](https://redhat.atlassian.net/browse/MIG-1872)

# Migration Toolkit for Containers 1.8.12 release notes

The Migration Toolkit for Containers (MTC) 1.8.12 section lists known and resolved issues.

## Resolved issues

Migration Toolkit for Containers (MTC) 1.8.12 has the following resolved issues:

Live migration of virtual machine instance with RWO configuration works in `MigMigration`
With this release, the live migration of virtual machine instances (VMIs) no longer fails for `MigMigration` when the persistent volume claims (PVC) of VMIs are not shared with the access mode configuration `ReadWriteMany`. The migration plan does not prevent you from migrating the VMIs because of the RWO volumes. As a result, you can migrate VMs with `ReadWriteOnce` volumes.

[(MIG-1770)](https://issues.redhat.com/browse/MIG-1770)

# Migration Toolkit for Containers 1.8.11 release notes

Migration Toolkit for Containers (MTC) 1.8.11 is a Container Grade Only (CGO) release, which is released to refresh the health grades of the containers. No code was changed in the product itself compared to that of MTC 1.8.10.

# Migration Toolkit for Containers 1.8.10 release notes

## Resolved issues

Migration Toolkit for Containers (MTC) 1.8.10 has the following major resolved issues:

<div class="formalpara">

<div class="title">

`migmigration` failed to clean up stale virt-handler pods for stopped VMs

</div>

With this release, `migmigration` object no longer fails to clean up stale `virt-handler` pods for stopped virtual machines (VMs) in an Azure Red Hat OpenShift (ARO) cluster with MTC Operator and Red Hat OpenShift Data Foundation (ODF) storage cluster-CEPH RBD virtualization. This resolution addresses an issue where migration failure occurred due to an attempt to clean up non-existent `virt-handler` pods during live migration when the VM was stopped and no VMI existed. As a result, stopped VMs no longer prevent successful migration. [(MIG-1762)](https://issues.redhat.com/browse/MIG-1762)

</div>

# Migration Toolkit for Containers 1.8.9 release notes

## Resolved issues

Migration Toolkit for Containers (MTC) 1.8.9 has the following major resolved issues:

<div class="formalpara">

<div class="title">

VM restarts migration after the MigPlan deletion

</div>

Before this update, deleting the `MigPlan` triggered unnecessary virtual machine (VM) migrations. This caused the VMs to resume, leading to migration failures. This release introduces a fix that prevents VMs from migrating when the `MigPlan` is actively removed. As a result, VMs no longer unintentionally migrate when MigPlans are deleted, ensuring a stable environment for users. [(MIG-1749)](https://issues.redhat.com/browse/MIG-1749)

</div>

<div class="formalpara">

<div class="title">

Virt-launcher pod remain in pending after migrating the VM from hostpath-csi-basic to hostpath-csi-pvc-block

</div>

Before this update, the `virt-launcher` pod stalled after migrating a VM due to pod anti-affinity conflicts with bound volumes. This resulted in a failed VM migration, causing the virt-launcher pod to get stuck. This release resolves the pod anti-affinity issue, allowing for scheduling on different nodes. As a result, you can now migrate VMs from `hostpath-csi-basic` to `hostpath-csi-pvc-block` without pods getting stuck in a pending state, thereby improving the overall migration process efficiency. [(MIG-1750)](https://issues.redhat.com/browse/MIG-1750)

</div>

<div class="formalpara">

<div class="title">

Migration-controller panics due to LimitRange "NIL" found in source project

</div>

Before this update, the missing `Min` spec in a LimitRange within the `openshift-migration` namespace caused a panic in the migration-controller pod, disrupting the user experience and preventing successful volume migration. With this release, the migration-controller pod no longer crashes when encountering a LimitRange set to `Nil`. As a result, `rsync` pods now comply with the specified limits, improving the migration process stability and eliminating crashloopbacks in source namespaces.

</div>

# Migration Toolkit for Containers 1.8.8 release notes

## Resolved issues

Migration Toolkit for Containers (MTC) 1.8.8 has the following major resolved issues:

<div class="formalpara">

<div class="title">

The detection of storage live migration status failed

</div>

There was an error in detecting the status of storage live migration. This update resolves the issue. [(MIG-1746)](https://issues.redhat.com/browse/MIG-1746)

</div>

# Migration Toolkit for Containers 1.8.7 release notes

## Resolved issues

Migration Toolkit for Containers (MTC) 1.8.7 has the following major resolved issues:

<div class="formalpara">

<div class="title">

MTC migration stuck in a `Prepare` phase on OpenShift Container Platform 4.19 due to incompatible OADP version and outdated DPA specification

</div>

When running migrations use MTC 1.8.7 on OpenShift Container Platform 4.19, the process halts in the `Prepare` phase and the migration plan enters in the `Suspended` phase.

</div>

The root cause is the deployment of an incompatible OADP version, earlier than 1.5.0, whose DataProtectionApplication (DPA) specification format is incompatible with OpenShift Container Platform. [(MIG-1735)](https://issues.redhat.com/browse/MIG-1735)

<div class="formalpara">

<div class="title">

Velero backup fails with a `file already closed` error when using the new AWS plugin in MTC

</div>

During stage or full migrations, the backup process intermittently fails for MTC with OADP on OpenShift Container Platform clusters configured with the new Amazon Web Services (AWS) plugin. You can see the following error in Velero logs:

</div>

``` terminal
error="read |0: file already closed"
```

As a workaround, use the legacy AWS plugin by performing following actions:

1.  Set `velero_use_legacy_aws: true` in the `MigrationController` custom resource (CR).

2.  Restart the MTC Operator to apply changes.

3.  Validate the AWS credentials for the cloud-credentials secret.

[(MIG-1738)](https://issues.redhat.com/browse/MIG-1738)

# Migration Toolkit for Containers 1.8.6 release notes

## Technical changes

<div class="formalpara">

<div class="title">

Multiple migration plans for a namespace is not supported

</div>

MTC version 1.8.6 and later do not support multiple migration plans for a single namespace.

</div>

<div class="formalpara">

<div class="title">

VM storage migration

</div>

VM storage migration feature changes from Technology Preview (TP) status to being Generally Available (GA).

</div>

## Resolved issues

MTC 1.8.6 has the following major resolved issues:

<div class="formalpara">

<div class="title">

UI fails during a namespace search in the migration plan wizard

</div>

When searching for a namespace in the **Select Namespace** step of the migration plan wizard, the user interface (UI) fails and disappears after clicking **Search**. The browser console shows a JavaScript error indicating that an undefined value has been accessed. This issue has been resolved in MTC 1.8.6. [(MIG-1704)](https://issues.redhat.com/browse/MIG-1704)

</div>

<div class="formalpara">

<div class="title">

Unable to create a migration plan due to a reconciliation failure

</div>

In MTC, when creating a migration plan, the UI remains on **Persistent Volumes** and you cannot continue. This issue occurs due to a critical reconciliation failure and returns a 404 API error when you attempt to fetch the migration plan from the backend. These issues cause the migration plan to remain in a **Not Ready** state, and you are prevented from continuing. This issue has been resolved in MTC 1.8.6. [(MIG-1705)](https://issues.redhat.com/browse/MIG-1705)

</div>

<div class="formalpara">

<div class="title">

Migration process becomes fails to complete after the `StageBackup` phase

</div>

When migrating a Django and PostgreSQL application, the migration becomes fails to complete after the `StageBackup` phase. Even though all the pods in the source namespace are healthy before the migration begins, after the migration and when terminating the pods on the source cluster, the Django pod fails with a `CrashLoopBackOff` error. This issue has been resolved in MTC 1.8.6. [(MIG-1707)](https://issues.redhat.com/browse/MIG-1707)

</div>

<div class="formalpara">

<div class="title">

Migration shown as succeeded despite a failed phase due to a misleading UI status

</div>

After running a migration using MTC, the UI incorrectly indicates that the migration was successful, with the status shown as **Migration succeeded**. However, the Direct Volume Migration (DVM) phase failed. This misleading status appears on both the **Migration** and the **Migration Details** pages. This issue has been resolved in MTC 1.8.6. [(MIG-1711)](https://issues.redhat.com/browse/MIG-1711)

</div>

<div class="formalpara">

<div class="title">

Persistent Volumes page hangs indefinitely for namespaces without persistent volume claims

</div>

When a migration plan includes a namespace that does not have any persistent volume claims (PVCs), the **Persistent Volumes** selection page remains indefinitely with the following message shown: `Discovering persistent volumes attached to source projects…​`. The page never completes loading, preventing you from proceeding with the migration. This issue has been resolved in MTC 1.8.6. [(MIG-1713)](https://issues.redhat.com/browse/MIG-1713)

</div>

## Known issues

MTC 1.8.6 has the following known issues:

<div class="formalpara">

<div class="title">

Inconsistent reporting of migration failure status

</div>

There is a discrepancy in the reporting of namespace migration status following a rollback and subsequent re-migration attempt when the migration plan is deliberately faulted. Although the Distributed Volume Migration (DVM) phase correctly registers a failure, this failure is not consistently reflected in the user interface (UI) or the migration plan’s YAML representation.

</div>

This issue is not only limited to unusual or unexpected cases. In certain circumstances, such as when network restrictions are applied that cause the DVM phase to fail, the UI still reports the migration status as successful. This behavior is similar to what was previously observed in [MIG-1711](https://issues.redhat.com/browse/MIG-1711) but occurs under different conditions. [(MIG-1719)](https://issues.redhat.com/browse/MIG-1719)

# Migration Toolkit for Containers 1.8.5 release notes

## Technical changes

Migration Toolkit for Containers (MTC) 1.8.5 has the following technical changes:

<div class="formalpara">

<div class="title">

Federal Information Processing Standard (FIPS)

</div>

FIPS is a set of computer security standards developed by the United States federal government in accordance with the Federal Information Security Management Act (FISMA).

</div>

Starting with version 1.8.5, MTC is designed for FIPS compliance.

## Resolved issues

For more information, see the list of [MTC 1.8.5 resolved issues](https://issues.redhat.com/issues/?filter=12447122) in Jira.

## Known issues

MTC 1.8.5 has the following known issues:

<div class="formalpara">

<div class="title">

The associated SCC for service account cannot be migrated in OpenShift Container Platform 4.12

</div>

The associated Security Context Constraints (SCCs) for service accounts in OpenShift Container Platform 4.12 cannot be migrated. This issue is planned to be resolved in a future release of MTC. [(MIG-1454)](https://issues.redhat.com/browse/MIG-1454)

</div>

<div class="formalpara">

<div class="title">

MTC does not patch `statefulset.spec.volumeClaimTemplates[].spec.storageClassName` on storage class conversion

</div>

While running a Storage Class conversion for a StatefulSet application, MTC updates the persistent volume claims (PVC) references in `.spec.volumeClaimTemplates[].metadata.name` to use the migrated PVC names. MTC does not update `spec.volumeClaimTemplates[].spec.storageClassName`, which causes the application to scale up. Additionally, new replicas consume PVCs created under the old Storage Class instead of the migrated Storage Class. [(MIG-1660)](https://issues.redhat.com/browse/MIG-1660)

</div>

<div class="formalpara">

<div class="title">

Performing a StorageClass conversion triggers the scale-down of all applications in the namespace

</div>

When running a `StorageClass` conversion on more than one application, MTC scales down all the applications in the cutover phase, including those not involved in the migration. [(MIG-1661)](https://issues.redhat.com/browse/MIG-1661)

</div>

<div class="formalpara">

<div class="title">

`MigPlan` cannot be edited to have the same target namespace as the source cluster after it is changed

</div>

After changing the target namespace to something different from the source namespace while creating a `MigPlan` in the MTC UI, you cannot edit the `MigPlan` again to make the target namespace the same as the source namespace. [(MIG-1600)](https://issues.redhat.com/browse/MIG-1600)

</div>

<div class="formalpara">

<div class="title">

Migrated builder pod fails to push to the image registry

</div>

When migrating an application that includes `BuildConfig` from the source to the target cluster, the builder pod encounters an error, failing to push the image to the image registry. [(BZ#2234781)](https://bugzilla.redhat.com/show_bug.cgi?id=2234781)

</div>

<div class="formalpara">

<div class="title">

Conflict condition clears briefly after it is displayed

</div>

When creating a new state migration plan that results in a conflict error, the error is cleared shortly after it is displayed. [(BZ#2144299)](https://bugzilla.redhat.com/show_bug.cgi?id=2144299)

</div>

<div class="formalpara">

<div class="title">

`PvCapacityAdjustmentRequired` warning not displayed after setting `pv_resizing_threshold`

</div>

The `PvCapacityAdjustmentRequired` warning does not appear in the migration plan after the `pv_resizing_threshold` is adjusted. [(BZ#2270160)](https://bugzilla.redhat.com/show_bug.cgi?id=2270160)

</div>

For a complete list of all known issues, see the list of [MTC 1.8.5 known issues](https://issues.redhat.com/issues/?filter=12447121) in Jira.

# Migration Toolkit for Containers 1.8.4 release notes

## Technical changes

Migration Toolkit for Containers (MTC) 1.8.4 has the following technical changes:

- MTC 1.8.4 extends its dependency resolution to include support for using OpenShift API for Data Protection (OADP) 1.4.

<div class="formalpara">

<div class="title">

Support for KubeVirt Virtual Machines with DirectVolumeMigration

</div>

MTC 1.8.4 adds support for KubeVirt Virtual Machines (VMs) with Direct Volume Migration (DVM).

</div>

## Resolved issues

MTC 1.8.4 has the following major resolved issues:

<div class="formalpara">

<div class="title">

Ansible Operator is broken when OpenShift Virtualization is installed

</div>

There is a bug in the `python3-openshift` package that installing OpenShift Virtualization exposes, with an exception, `ValueError: too many values to unpack`, returned during the task. Earlier versions of MTC are impacted, while MTC 1.8.4 has implemented a workaround. Updating to MTC 1.8.4 means you are no longer affected by this issue. [(OCPBUGS-38116)](https://issues.redhat.com/browse/OCPBUGS-38116)

</div>

<div class="formalpara">

<div class="title">

UI stuck at Namespaces while creating a migration plan

</div>

When trying to create a migration plan from the MTC UI, the migration plan wizard becomes stuck at the **Namespaces** step. This issue has been resolved in MTC 1.8.4. [(MIG-1597)](https://issues.redhat.com/browse/MIG-1597)

</div>

<div class="formalpara">

<div class="title">

Migration fails with error of no matches for kind Virtual machine in version kubevirt/v1

</div>

During the migration of an application, all the necessary steps, including the backup, DVM, and restore, are successfully completed. However, the migration is marked as unsuccessful with the error message `no matches for kind Virtual machine in version kubevirt/v1`. [(MIG-1594)](https://issues.redhat.com/browse/MIG-1594)

</div>

<div class="formalpara">

<div class="title">

Direct Volume Migration fails when migrating to a namespace different from the source namespace

</div>

On performing a migration from source cluster to target cluster, with the target namespace different from the source namespace, the DVM fails. [(MIG-1592)](https://issues.redhat.com/browse/MIG-1592)

</div>

<div class="formalpara">

<div class="title">

Direct Image Migration does not respect label selector on migplan

</div>

When using Direct Image Migration (DIM), if a label selector is set on the migration plan, DIM does not respect it and attempts to migrate all imagestreams in the namespace. [(MIG-1533)](https://issues.redhat.com/browse/MIG-1533)

</div>

## Known issues

MTC 1.8.4 has the following known issues:

<div class="formalpara">

<div class="title">

The associated SCC for service account cannot be migrated in OpenShift Container Platform 4.12

</div>

The associated Security Context Constraints (SCCs) for service accounts in OpenShift Container Platform 4.12 cannot be migrated. This issue is planned to be resolved in a future release of MTC. [(MIG-1454)](https://issues.redhat.com/browse/MIG-1454).

</div>

<div class="formalpara">

<div class="title">

Rsync pod fails to start causing the DVM phase to fail

</div>

The DVM phase fails due to the Rsync pod failing to start, because of a permission issue.

</div>

[(BZ#2231403)](https://bugzilla.redhat.com/show_bug.cgi?id=2231403)

<div class="formalpara">

<div class="title">

Migrated builder pod fails to push to image registry

</div>

When migrating an application including `BuildConfig` from source to target cluster, the builder pod results in error, failing to push the image to the image registry.

</div>

[(BZ#2234781)](https://bugzilla.redhat.com/show_bug.cgi?id=2234781)

<div class="formalpara">

<div class="title">

Conflict condition gets cleared briefly after it is created

</div>

When creating a new state migration plan that results in a conflict error, that error is cleared shorty after it is displayed.

</div>

[(BZ#2144299)](https://bugzilla.redhat.com/show_bug.cgi?id=2144299)

<div class="formalpara">

<div class="title">

PvCapacityAdjustmentRequired Warning Not Displayed After Setting pv_resizing_threshold

</div>

The `PvCapacityAdjustmentRequired` warning fails to appear in the migration plan after the `pv_resizing_threshold` is adjusted.

</div>

[(BZ#2270160)](https://bugzilla.redhat.com/show_bug.cgi?id=2270160)

# Migration Toolkit for Containers 1.8.3 release notes

## Technical changes

Migration Toolkit for Containers (MTC) 1.8.3 has the following technical changes:

<div class="formalpara">

<div class="title">

OADP 1.3 is now supported

</div>

MTC 1.8.3 adds support to OpenShift API for Data Protection (OADP) as a dependency of MTC 1.8.z.

</div>

## Resolved issues

MTC 1.8.3 has the following major resolved issues:

<div class="formalpara">

<div class="title">

CVE-2024-24786: Flaw in Golang `protobuf` module causes `unmarshal` function to enter infinite loop

</div>

In previous releases of MTC, a vulnerability was found in Golang’s `protobuf` module, where the `unmarshal` function entered an infinite loop while processing certain invalid inputs. Consequently, an attacker provided carefully constructed invalid inputs, which caused the function to enter an infinite loop.

</div>

With this update, the `unmarshal` function works as expected.

For more information, see [CVE-2024-24786](https://access.redhat.com/security/cve/CVE-2024-24786).

<div class="formalpara">

<div class="title">

CVE-2023-45857: Axios Cross-Site Request Forgery Vulnerability

</div>

In previous releases of MTC, a vulnerability was discovered in Axios 1.5.1 that inadvertently revealed a confidential `XSRF-TOKEN` stored in cookies by including it in the HTTP header `X-XSRF-TOKEN` for every request made to the host, allowing attackers to view sensitive information.

</div>

For more information, see [CVE-2023-45857](https://access.redhat.com/security/cve/CVE-2023-45857).

<div class="formalpara">

<div class="title">

Restic backup does not work properly when the source workload is not quiesced

</div>

In previous releases of MTC, some files did not migrate when deploying an application with a route. The Restic backup did not function as expected when the quiesce option was unchecked for the source workload.

</div>

This issue has been resolved in MTC 1.8.3.

For more information, see [BZ#2242064](https://bugzilla.redhat.com/show_bug.cgi?id=2242064).

<div class="formalpara">

<div class="title">

The `Migration Controller` fails to install due to an unsupported value error in Velero

</div>

The `MigrationController` failed to install due to an unsupported value error in Velero. Updating OADP 1.3.0 to OADP 1.3.1 resolves this problem. For more information, see [BZ#2267018](https://bugzilla.redhat.com/show_bug.cgi?id=2267018).

</div>

This issue has been resolved in MTC 1.8.3.

For a complete list of all resolved issues, see the list of [MTC 1.8.3 resolved issues](https://issues.redhat.com/issues/?filter=12432429) in Jira.

## Known issues

Migration Toolkit for Containers (MTC) 1.8.3 has the following known issues:

<div class="formalpara">

<div class="title">

Ansible Operator is broken when OpenShift Virtualization is installed

</div>

There is a bug in the `python3-openshift` package that installing OpenShift Virtualization exposes, with an exception, `ValueError: too many values to unpack`, returned during the task. MTC 1.8.4 has implemented a workaround. Updating to MTC 1.8.4 means you are no longer affected by this issue. [(OCPBUGS-38116)](https://issues.redhat.com/browse/OCPBUGS-38116)

</div>

<div class="formalpara">

<div class="title">

The associated SCC for service account cannot be migrated in OpenShift Container Platform 4.12

</div>

The associated Security Context Constraints (SCCs) for service accounts in OpenShift Container Platform version 4.12 cannot be migrated. This issue is planned to be resolved in a future release of MTC. [(MIG-1454)](https://issues.redhat.com/browse/MIG-1454).

</div>

For a complete list of all known issues, see the list of [MTC 1.8.3 known issues](https://issues.redhat.com/issues/?filter=12429975) in Jira.

# Migration Toolkit for Containers 1.8.2 release notes

## Resolved issues

This release has the following major resolved issues:

<div class="formalpara">

<div class="title">

Backup phase fails after setting custom CA replication repository

</div>

In previous releases of Migration Toolkit for Containers (MTC), after editing the replication repository, adding a custom CA certificate, successfully connecting the repository, and triggering a migration, a failure occurred during the backup phase.

</div>

<div class="formalpara">

<div class="title">

CVE-2023-26136: tough-cookie package before 4.1.3 are vulnerable to Prototype Pollution

</div>

In previous releases of (MTC), versions before 4.1.3 of the `tough-cookie` package used in MTC were vulnerable to prototype pollution. This vulnerability occurred because CookieJar did not handle cookies properly when the value of the `rejectPublicSuffixes` was set to `false`.

</div>

For more details, see [(CVE-2023-26136)](https://access.redhat.com/security/cve/cve-2023-26136)

<div class="formalpara">

<div class="title">

CVE-2022-25883 openshift-migration-ui-container: nodejs-semver: Regular expression denial of service

</div>

In previous releases of (MTC), versions of the `semver` package before 7.5.2, used in MTC, were vulnerable to Regular Expression Denial of Service (ReDoS) from the function `newRange`, when untrusted user data was provided as a range.

</div>

For more details, see [(CVE-2022-25883)](https://access.redhat.com/security/cve/cve-2022-25883)

## Known issues

MTC 1.8.2 has the following known issues:

<div class="formalpara">

<div class="title">

Ansible Operator is broken when OpenShift Virtualization is installed

</div>

There is a bug in the `python3-openshift` package that installing OpenShift Virtualization exposes, with an exception, `ValueError: too many values to unpack`, returned during the task. MTC 1.8.4 has implemented a workaround. Updating to MTC 1.8.4 means you are no longer affected by this issue. [(OCPBUGS-38116)](https://issues.redhat.com/browse/OCPBUGS-38116)

</div>

# Migration Toolkit for Containers 1.8.1 release notes

## Resolved issues

Migration Toolkit for Containers (MTC) 1.8.1 has the following major resolved issues:

<div class="formalpara">

<div class="title">

CVE-2023-39325: golang: net/http, x/net/http2: rapid stream resets can cause excessive work

</div>

A flaw was found in handling multiplexed streams in the HTTP/2 protocol, which is used by MTC. A client could repeatedly make a request for a new multiplex stream and immediately send an `RST_STREAM` frame to cancel it. This creates additional workload for the server in terms of setting up and dismantling streams, while avoiding any server-side limitations on the maximum number of active streams per connection, resulting in a denial of service due to server resource consumption. [(BZ#2245079)](https://bugzilla.redhat.com/show_bug.cgi?id=2245079)

</div>

It is advised to update to MTC 1.8.1 or later, which resolve this issue.

For more details, see [(CVE-2023-39325)](https://access.redhat.com/security/cve/cve-2023-39325) and [(CVE-2023-44487)](https://access.redhat.com/security/cve/cve-2023-44487)

## Known issues

Migration Toolkit for Containers (MTC) 1.8.1 has the following known issues:

<div class="formalpara">

<div class="title">

Ansible Operator is broken when OpenShift Virtualization is installed

</div>

There is a bug in the `python3-openshift` package that installing OpenShift Virtualization exposes. An exception, `ValueError: too many values to unpack`, is returned during the task. MTC 1.8.4 has implemented a workaround. Updating to MTC 1.8.4 means you are no longer affected by this issue. [(OCPBUGS-38116)](https://issues.redhat.com/browse/OCPBUGS-38116)

</div>

# Migration Toolkit for Containers 1.8.0 release notes

## Resolved issues

Migration Toolkit for Containers (MTC) 1.8.0 has the following resolved issues:

<div class="formalpara">

<div class="title">

Indirect migration is stuck on backup stage

</div>

In previous releases, an indirect migration became stuck at the backup stage, due to `InvalidImageName` error. ([(BZ#2233097)](https://bugzilla.redhat.com/show_bug.cgi?id=2233097))

</div>

<div class="formalpara">

<div class="title">

PodVolumeRestore remain In Progress keeping the migration stuck at Stage Restore

</div>

In previous releases, on performing an indirect migration, the migration became stuck at the `Stage Restore` step, waiting for the `podvolumerestore` to be completed. ([(BZ#2233868)](https://bugzilla.redhat.com/show_bug.cgi?id=2233868))

</div>

<div class="formalpara">

<div class="title">

Migrated application unable to pull image from internal registry on target cluster

</div>

In previous releases, on migrating an application to the target cluster, the migrated application failed to pull the image from the internal image registry resulting in an `application failure`. ([(BZ#2233103)](https://bugzilla.redhat.com/show_bug.cgi?id=2233103))

</div>

<div class="formalpara">

<div class="title">

Migration failing on Azure due to authorization issue

</div>

In previous releases, on an Azure cluster, when backing up to Azure storage, the migration failed at the `Backup` stage. ([(BZ#2238974)](https://bugzilla.redhat.com/show_bug.cgi?id=2238974))

</div>

## Known issues

MTC 1.8.0 has the following known issues:

<div class="formalpara">

<div class="title">

Ansible Operator is broken when OpenShift Virtualization is installed

</div>

There is a bug in the `python3-openshift` package that installing OpenShift Virtualization exposes, with an exception `ValueError: too many values to unpack` returned during the task. MTC 1.8.4 has implemented a workaround. Updating to MTC 1.8.4 means you are no longer affected by this issue. [(OCPBUGS-38116)](https://issues.redhat.com/browse/OCPBUGS-38116)

</div>

<div class="formalpara">

<div class="title">

Old Restic pods are not getting removed on upgrading MTC 1.7.x → 1.8.x

</div>

In this release, on upgrading the MTC Operator from 1.7.x to 1.8.x, the old Restic pods are not being removed. Therefore after the upgrade, both Restic and node-agent pods are visible in the namespace. ([(BZ#2236829)](https://bugzilla.redhat.com/show_bug.cgi?id=2236829))

</div>

<div class="formalpara">

<div class="title">

Migrated builder pod fails to push to image registry

</div>

In this release, on migrating an application including a `BuildConfig` from a source to target cluster, builder pod results in `error`, failing to push the image to the image registry. ([(BZ#2234781)](https://bugzilla.redhat.com/show_bug.cgi?id=2234781))

</div>

<div class="formalpara">

<div class="title">

\[UI\] CA bundle file field is not properly cleared

</div>

In this release, after enabling `Require SSL verification` and adding content to the CA bundle file for an MCG NooBaa bucket in MigStorage, the connection fails as expected. However, when reverting these changes by removing the CA bundle content and clearing `Require SSL verification`, the connection still fails. The issue is only resolved by deleting and re-adding the repository. ([(BZ#2240052)](https://bugzilla.redhat.com/show_bug.cgi?id=2240052))

</div>

<div class="formalpara">

<div class="title">

Backup phase fails after setting custom CA replication repository

</div>

In (MTC), after editing the replication repository, adding a custom CA certificate, successfully connecting the repository, and triggering a migration, a failure occurs during the backup phase.

</div>

This issue is resolved in MTC 1.8.2.

<div class="formalpara">

<div class="title">

CVE-2023-26136: tough-cookie package before 4.1.3 are vulnerable to Prototype Pollution

</div>

Versions before 4.1.3 of the `tough-cookie` package, used in MTC, are vulnerable to prototype pollution. This vulnerability occurs because CookieJar does not handle cookies properly when the value of the `rejectPublicSuffixes` is set to `false`.

</div>

This issue is resolved in MTC 1.8.2.

For more details, see [(CVE-2023-26136)](https://access.redhat.com/security/cve/cve-2023-26136)

<div class="formalpara">

<div class="title">

CVE-2022-25883 openshift-migration-ui-container: nodejs-semver: Regular expression denial of service

</div>

In previous releases of (MTC), versions of the `semver` package before 7.5.2, used in MTC, are vulnerable to Regular Expression Denial of Service (ReDoS) from the function `newRange`, when untrusted user data is provided as a range.

</div>

This issue is resolved in MTC 1.8.2.

For more details, see [(CVE-2022-25883)](https://access.redhat.com/security/cve/cve-2022-25883)

## Technical changes

This release has the following technical changes:

- Migration from OpenShift Container Platform 3 to OpenShift Container Platform 4 requires a legacy Migration Toolkit for Containers Operator and Migration Toolkit for Containers 1.7.x.

- Migration from MTC 1.7.x to MTC 1.8.x is not supported.

- You must use MTC 1.7.x to migrate anything with a source of OpenShift Container Platform 4.9 or earlier.

  - MTC 1.7.x must be used on both source and destination.

- Migration Toolkit for Containers (MTC) 1.8.x only supports migrations from OpenShift Container Platform 4.10 or later to OpenShift Container Platform 4.10 or later. For migrations only involving cluster versions 4.10 and later, either 1.7.x or 1.8.x might be used. However, but it must be the same MTC 1.Y.z on both source and destination.

  - Migration from source MTC 1.7.x to destination MTC 1.8.x is unsupported.

  - Migration from source MTC 1.8.x to destination MTC 1.7.x is unsupported.

  - Migration from source MTC 1.7.x to destination MTC 1.7.x is supported.

  - Migration from source MTC 1.8.x to destination MTC 1.8.x is supported.

- MTC 1.8.x by default installs OADP 1.2.x.

- Upgrading from MTC 1.7.x to MTC 1.8.0, requires manually changing the OADP channel to 1.2. If this is not done, the upgrade of the Operator fails.
