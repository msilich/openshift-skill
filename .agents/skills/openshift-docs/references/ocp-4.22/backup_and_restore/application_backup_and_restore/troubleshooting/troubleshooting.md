<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Troubleshoot OpenShift API for Data Protection (OADP) issues by using diagnostic tools such as the OADP CLI, webhooks, `must-gather` custom resource, and other methods. This helps you identify and resolve problems with backup and restore operations.

You can troubleshoot OADP issues by using the following methods:

- Debug Velero custom resources (CRs) by using the OpenShift CLI tool.

- Debug Velero or Restic pod crashes, which are caused due to a lack of memory or CPU.

- Debug issues with Velero and admission webhooks.

- Check OADP installation issues, OADP Operator issues, backup and restore CR issues, and Restic issues.

- Use the available OADP timeouts to reduce errors, retries, or failures.

- Run the `DataProtectionTest` (DPT) custom resource to verify your backup storage bucket configuration and check the CSI snapshot readiness for persistent volume claims.

- Collect logs and CR information by using the `must-gather` tool.

- Monitor and analyze the workload performance with the help of OADP monitoring.

# Additional resources

- [Debugging with the OpenShift CLI tool](oadp-cli-tool.md#oadp-debugging-oc-cli_oadp-cli-tool)

- [Debugging backups and restores using the OADP CLI](oadp-cli-tool.md#migration-debugging-velero-resources_oadp-cli-tool)

- [Pods crash or restart due to lack of memory or CPU](pods-crash-or-restart-due-to-lack-of-memory-or-cpu.md#pods-crash-or-restart-due-to-lack-of-memory-or-cpu)

- [Restoring workarounds for Velero backups that use admission webhooks](restoring-workarounds-for-velero-backups-that-use-admission-webhooks.md#restoring-workarounds-for-velero-backups-that-use-admission-webhooks)

- [OADP installation issues](oadp-installation-issues.md#oadp-installation-issues)

- [OADP Operator issues](oadp-operator-issues.md#oadp-operator-issues)

- [Backup and restore CR issues](backup-and-restore-cr-issues.md#backup-and-restore-cr-issues)

- [Restic issues](restic-issues.md#restic-issues)

- [OADP timeouts](oadp-timeouts.md#oadp-timeouts)

- [DataProtectionTest custom resource](oadp-data-protection-test.md#oadp-data-protection-test)

- [Using the must-gather tool](using-the-must-gather-tool.md#using-the-must-gather-tool)

- [OADP monitoring](oadp-monitoring.md#oadp-monitoring)
