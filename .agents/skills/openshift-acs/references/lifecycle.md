# Airgap and ACS lifecycle

Read [Offline mode](../../openshift-docs/references/acs-4.11/configuration/enable-offline-mode.md):
deployment steps, downloading images, installation method and Updating Scanner
definitions in offline mode. See [sources](sources.md) and [execution](execution.md).

Separate the connected preparation machine, approved transfer and disconnected
target. Establish component versions, image digests, architecture, internal
registry trust and the applicable Scanner implementation. Plan image/feed/kernel
support content from the matching documented procedure. Validate transfer hashes
and the data's timestamp. Never download content at skill runtime in the airgap.
Feed import modifies Central/Scanner state and needs explicit Day-2 approval.

For upgrades choose the actual installation owner: [Operator upgrade](../../openshift-docs/references/acs-4.11/upgrading/upgrade-operator.md),
[Helm upgrade](../../openshift-docs/references/acs-4.11/upgrading/upgrade-helm.md)
or [roxctl upgrade](../../openshift-docs/references/acs-4.11/upgrading/upgrade-roxctl.md).
Read prerequisites and the upgrade procedure before proposing an order. Verify
installed/target component versions, supported path, storage, backup, mirror
availability and maintenance window. Missing offline compatibility evidence means
unverified, not compatible. Do not infer a supported downgrade from a rollback
wish. Verify Central access, secured-cluster connection, ingestion and new scans.

Read [Backing up ACS](../../openshift-docs/references/acs-4.11/backup_and_restore/backing-up-acs.md)
and [Restoring ACS](../../openshift-docs/references/acs-4.11/backup_and_restore/restore-acs.md),
selecting database, certificates and deployment sections for the installation
method. Record precisely what is backed up, encryption/access requirements,
destination, timestamp, version and retention. Backup files/certificates can
contain credentials: apply the existing Secret choice before examining contents.

ACS Central recovery differs from OADP application restore or etcd recovery; route
those tasks to openshift-backup-restore. Restore is high-risk: confirm destination,
data replacement, version prerequisites and rollback/recovery plan. After fresh
approval verify restored data, user access, secured-cluster reconnection and an
application-relevant security check. A completed backup is not a tested restore.
