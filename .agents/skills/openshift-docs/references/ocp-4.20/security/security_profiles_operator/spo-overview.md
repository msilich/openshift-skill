<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Container Platform Security Profiles Operator (SPO) provides a way to define secure computing ([seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/)) profiles and SELinux profiles as custom resources, synchronizing profiles to every node in a given namespace. For the latest updates, see the [release notes](spo-release-notes.md#spo-release-notes).

The SPO can distribute custom resources to each node while a reconciliation loop ensures that the profiles stay up-to-date. See [Understanding the Security Profiles Operator](spo-understanding.md#spo-understanding).

The SPO manages SELinux policies and seccomp profiles for namespaced workloads. For more information, see [Enabling the Security Profiles Operator](spo-enabling.md#spo-enabling).

You can create [seccomp](spo-seccomp.md#spo-seccomp) and [SELinux](spo-selinux.md#spo-selinux) profiles, bind policies to pods, record workloads, and synchronize all worker nodes in a namespace.

Use [Advanced Security Profile Operator tasks](spo-advanced.md#spo-advanced) to enable the log enricher, configure webhooks and metrics, or restrict profiles to a single namespace.

[Troubleshoot the Security Profiles Operator](spo-troubleshooting.md#spo-inspecting-seccomp-profiles_spo-troubleshooting) as needed, or engage [Red Hat support](https://access.redhat.com/support/).

You can [Uninstall the Security Profiles Operator](spo-uninstalling.md#spo-uninstalling) by removing the profiles before removing the Operator.
