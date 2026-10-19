<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can review the following release notes to learn about changes in the Windows Machine Config Operator (WMCO) version 10.20.2.

# Release notes for Red Hat Windows Machine Config Operator 10.20.2

Issued: 13 October 2026

You can review the following release notes to learn about the bug fixes provided in this release of the Windows Machine Config Operator (WMCO).

The components of the Red Hat Windows Machine Config Operator (WMCO) 10.20.2 were released in [RHSA-2026:82440](https://access.redhat.com/errata/RHSA-2026:82440).

## Bug fixes

- Before this update, if a Windows node or Windows Instance Config Daemon (WICD) daemon submitted a certificate signing request (CSR), the WMCO only checked that the expected organization, such as `system:nodes` or `system:wicd-nodes`, was present in the CSR subject. The validation did not require that organization to be the only one listed. As a result, a CSR could include the required organization plus additional organizations and still pass validation. WMCO approved and signed those CSRs, issuing certificates that did not strictly match the expected node identity constraints. With this release, the validation now requires that the CSR subject contain exactly one organization, and the CSR must match the expected group for the certificate type, such as `WICD`, `kubelet client`, or `kubelet serving`. As a result, CSRs with extra, missing, or incorrect organizations are rejected. ([OCPBUGS-88347](https://issues.redhat.com/browse/OCPBUGS-88347))

- Before this update, the SSH connection between the WMCO and a Windows node would terminate when the WMCO rebooted the node after a configuration update. As a consequence, the WMCO incorrectly treated the SSH disconnection as a reboot failure, preventing the Windows node from completing required reboots. With this release, the reboot validation process is modified to ignore SSH termination errors and instead verify a successful reboot by using explicit node reachability checks and the SSH reconnection. As a result, Windows nodes successfully reboot upon node configuration changes. ([OCPBUGS-98230](https://issues.redhat.com/browse/OCPBUGS-98230))
