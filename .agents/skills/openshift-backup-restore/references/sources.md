# Procedure sources

Product: OpenShift Container Platform 4.22. Source: openshift/openshift-docs at commit `d8cc5bae880cc93ecd22fecd660c1b3a7f1358ff`.
Read [snapshot provenance](../../openshift-docs/references/ocp-4.22/SOURCE.json) for the source, license and conversion details.

| Procedure | Local chapter | Sections to read |
| --- | --- | --- |
| OADP scope and support | [oadp-intro.md](../../openshift-docs/references/ocp-4.22/backup_and_restore/application_backup_and_restore/oadp-intro.md) | OpenShift API for Data Protection APIs; Support for OpenShift API for Data Protection |
| Backup selection | [oadp-creating-backup-cr.md](../../openshift-docs/references/ocp-4.22/backup_and_restore/application_backup_and_restore/backing_up_and_restoring/oadp-creating-backup-cr.md) | Document introduction and Backup creation procedure |
| Application restore | [restoring-applications.md](../../openshift-docs/references/ocp-4.22/backup_and_restore/application_backup_and_restore/backing_up_and_restoring/restoring-applications.md) | Document introduction and restore procedures |
| etcd backup | [backing-up-etcd.md](../../openshift-docs/references/ocp-4.22/backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.md) | Document introduction and etcd backup procedure |
| Control-plane recovery | [scenario-2-restoring-cluster-state.md](../../openshift-docs/references/ocp-4.22/backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md) | About restoring to a previous cluster state; Restoring to a previous cluster state for a single node |

These workflows are project-authored adaptations of the cited procedures. MCP
selection, bounded diagnostics, target checks, approval handling and offline
routing are project integration decisions, not statements of Red Hat support.
Documentation snippets still require live schema verification.
