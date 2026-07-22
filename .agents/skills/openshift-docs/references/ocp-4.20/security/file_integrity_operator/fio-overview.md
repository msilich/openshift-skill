<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The File Integrity Operator continually runs file integrity checks on the cluster nodes. It deploys a DaemonSet that initializes and runs privileged [Advanced Intrusion Detection Environment](https://aide.github.io/) (AIDE) containers on each node, providing a log of files that have been modified since the initial run of the DaemonSet pods.

> [!NOTE]
> File Integrity Operator is not supported on HCP clusters.

For the latest updates, see the [File Integrity Operator release notes](file-integrity-operator-release-notes.md#file-integrity-operator-release-notes).

[Installing the File Integrity Operator](file-integrity-operator-installation.md#installing-file-integrity-operator)

[Updating the File Integrity Operator](file-integrity-operator-updating.md#file-integrity-operator-updating)

[Understanding the File Integrity Operator](file-integrity-operator-understanding.md#understanding-file-integrity-operator)

[Configuring the Custom File Integrity Operator](file-integrity-operator-configuring.md#configuring-file-integrity-operator)

[Performing advanced Custom File Integrity Operator tasks](file-integrity-operator-advanced-usage.md#file-integrity-operator-advanced-usage)

[Troubleshooting the File Integrity Operator](file-integrity-operator-troubleshooting.md#troubleshooting-file-integrity-operator)

[Uninstalling the File Integrity Operator](fio-uninstalling.md#fio-uninstalling)
