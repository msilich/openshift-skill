<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Troubleshoot OpenShift API for Data Protection (OADP) issues by using diagnostic tools such as the Velero CLI, webhooks, `must-gather` custom resource, and other methods. This helps you identify and resolve problems with backup and restore operations.

You can troubleshoot OADP issues by using the following methods:

- Debug Velero custom resources (CRs) by using the [OpenShift CLI tool](velero-cli-tool.md#oadp-debugging-oc-cli_velero-cli-tool) or the [Velero CLI tool](velero-cli-tool.md#migration-debugging-velero-resources_velero-cli-tool). The Velero CLI tool provides more detailed logs and information.

- Debug Velero or Restic pod crashes, which are caused due to a lack of memory or CPU by using [Pods crash or restart due to lack of memory or CPU](pods-crash-or-restart-due-to-lack-of-memory-or-cpu.md#pods-crash-or-restart-due-to-lack-of-memory-or-cpu).

- Debug issues with Velero and admission webhooks by using [Restoring workarounds for Velero backups that use admission webhooks](restoring-workarounds-for-velero-backups-that-use-admission-webhooks.md#restoring-workarounds-for-velero-backups-that-use-admission-webhooks).

- Check [OADP installation issues](oadp-installation-issues.md#oadp-installation-issues), [OADP Operator issues](oadp-operator-issues.md#oadp-operator-issues), [backup and restore CR issues](backup-and-restore-cr-issues.md#backup-and-restore-cr-issues), and [Restic issues](restic-issues.md#restic-issues).

- Use the available [OADP timeouts](oadp-timeouts.md#oadp-timeouts) to reduce errors, retries, or failures.

- Run the [`DataProtectionTest` (DPT)](oadp-data-protection-test.md#oadp-data-protection-test) custom resource to verify your backup storage bucket configuration and check the CSI snapshot readiness for persistent volume claims.

- Collect logs and CR information by using the [`must-gather` tool](using-the-must-gather-tool.md#using-the-must-gather-tool).

- Monitor and analyze the workload performance with the help of [OADP monitoring](oadp-monitoring.md#oadp-monitoring).
