<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can review the release notes to learn about the changes introduced through each release of the Red Hat OpenShift support for Windows Containers and the Windows Machine Config Operator (WMCO).

# Release notes for Red Hat Windows Machine Config Operator 10.22.1

Issued: 28 July 2026

You can review the release notes to learn about the bug fixes and Common Vulnerabilities and Exposures (CVEs) fixes in the Windows Machine Config Operator (WMCO) version 10.22.1.

The components of the WMCO version 10.22.1 were released in [RHSA-2026:47173](https://access.redhat.com/errata/RHSA-2026:47173).

## Bug fixes

- Before this update, the SSH connection between the WMCO and a Windows node would terminate when the WMCO rebooted the node after a configuration update. As a consequence, the WMCO incorrectly treated the SSH disconnection as a reboot failure, preventing the Windows node from completing required reboots. With this release, the reboot validation process is modified to ignore SSH termination errors and instead verify a successful reboot by using explicit node reachability checks and the SSH reconnection. As a result, Windows nodes successfully reboot upon node configuration changes. ([OCPBUGS-98228](https://issues.redhat.com/browse/OCPBUGS-98228))

## CVE fixes

- [CVE-2026-54099](https://access.redhat.com/security/cve/cve-2026-54099)

- [CVE-2026-54100](https://access.redhat.com/security/cve/cve-2026-54100)
