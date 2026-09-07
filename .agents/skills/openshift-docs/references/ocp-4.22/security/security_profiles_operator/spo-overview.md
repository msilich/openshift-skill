<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With the OpenShift Container Platform Security Profiles Operator (SPO), you can define seccomp and SELinux profiles as custom resources and keep them synchronized across every node in a namespace.

The SPO distributes seccomp and SELinux profile custom resources to each node and keeps them up to date when profiles change. You can also bind policies to pods and record workloads. See Additional resources for advanced tasks such as enabling the log enricher, configuring webhooks and metrics, or restricting profiles to a single namespace, and for advanced audit logging that correlates cluster users with actions during `oc exec`, `oc rsh`, and `oc debug` sessions.

# Additional resources

- [Security Profiles Operator release notes](spo-release-notes.md#spo-release-notes)

- [Security Profiles Operator support](spo-support.md#spo-support)

- [Understanding the Security Profiles Operator](spo-understanding.md#spo-understanding)

- [Enabling the Security Profiles Operator](spo-enabling.md#spo-enabling)

- [Managing seccomp profiles](spo-seccomp.md#spo-seccomp)

- [Managing SELinux profiles](spo-selinux.md#spo-selinux)

- [Advanced Security Profiles Operator tasks](spo-advanced.md#spo-advanced)

- [Advanced Audit Logging Framework](spo-logging.md#spo-audit-logging)

- [Troubleshooting the Security Profiles Operator](spo-troubleshooting.md#spo-inspecting-seccomp-profiles_spo-troubleshooting)

- [Uninstalling the Security Profiles Operator](spo-uninstalling.md#spo-uninstalling)

- [seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/)
