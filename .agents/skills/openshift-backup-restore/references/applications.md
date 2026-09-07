# OADP application and data protection

Start with [sources.md](sources.md). Record the OCP/OADP versions, namespace,
selected resources, application consistency requirements, storage method,
backup target, retention requirements and intended restore destination.
Check the locally available compatibility matrix. Do not assume that an OADP
version supported on one OCP release is supported on another.

Discover the served OADP/Velero and snapshot APIs before inspecting the relevant
DataProtectionApplication, Backup, Restore, Schedule, BackupStorageLocation and
VolumeSnapshotLocation objects. Use generic MCP resource reads if dedicated
tools are absent. Object existence is not evidence that backups are usable.

## Backup coverage and failures

Inspect the named backup's phase, warnings/errors, selection/exclusions, volume
backup or snapshot/data-mover results, hooks and storage-location availability.
Do not equate snapshots alone with an independently recoverable off-cluster copy.
A PartiallyFailed backup, missing volume data or unavailable location must be
reported as incomplete protection, even if Kubernetes metadata was backed up.

Inspect only bounded relevant controller logs. Backup files and credential
objects may contain Secret values; resolve the existing user choice before any
content access. Never list or download an entire backup bucket as a routine check.

## Restore plan and verification

Select an exact backup and target namespace/cluster. Read the applicable
cross-cluster, storage-class and API-version restrictions. State what already
exists at the target and how the documented restore procedure handles it.
Restore can overwrite or conflict with application state; show the scoped change
and obtain the existing Day-2 approval before creating the Restore request.

After execution inspect restore errors/warnings, resource reconciliation, PVC
binding, volumes and pod readiness. Perform the user-agreed application/data
integrity check. Backup completion or a Completed Restore alone does not prove
business-data recovery. Report RPO/RTO evidence only when measured; do not infer
it from the schedule. Do not delete backups or change retention as part of diagnosis.
