> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/whats_new-ref_patch_releases). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Patch releases

The following release notes detail the updates for the Red Hat OpenShift Dev Spaces patch releases.

Security, bug fixes, and enhancements for Red Hat OpenShift Dev Spaces are released as asynchronous erratas. All Red Hat OpenShift Dev Spaces erratas are available on the [Red Hat package browser](https://access.redhat.com/downloads/content/package-browser).

As a Red Hat Customer Portal user, you can enable errata notifications in the account settings for Red Hat Subscription Management (RHSM). When errata notifications are enabled, you receive notifications through email whenever new erratas relevant to your registered systems are released.

Note

Red Hat Customer Portal user accounts must have systems registered and consuming Red Hat OpenShift Dev Spaces entitlements for errata notification emails to generate.

## Red Hat OpenShift Dev Spaces 3.29.1

This patch release for Red Hat OpenShift Dev Spaces 3.29 addresses security vulnerabilities across multiple container images and resolves a plugin registry startup failure on ARM architectures.

## Bug fixes

**Plugin registry pod no longer reports permission errors during startup:** Before this update, the plugin registry pod logged `chmod: Permission denied` errors in the PostgreSQL data directory during startup. On ARM architectures, a stricter file permission on `replorigin_checkpoint` caused the pod to enter a CrashLoopBackOff state and fail to start. With this update, file permissions in the plugin registry container image are set correctly. As a result, the plugin registry pod starts successfully without permission errors. ([CRW-11943](https://redhat.atlassian.net/browse/CRW-11943))

## CVEs

The following CVEs are addressed in this release:

**code-rhel9**

- [CVE-2026-6734](https://access.redhat.com/security/cve/CVE-2026-6734): `undici` -- Information disclosure and data integrity issues due to incorrect Socks5ProxyAgent connection routing. ([CRW-11311](https://redhat.atlassian.net/browse/CRW-11311))
- [CVE-2026-9697](https://access.redhat.com/security/cve/CVE-2026-9697): `undici` -- Man-in-the-Middle attack via ignored TLS options with SOCKS5 proxy. ([CRW-11339](https://redhat.atlassian.net/browse/CRW-11339))
- [CVE-2026-12151](https://access.redhat.com/security/cve/CVE-2026-12151): `undici` -- Denial of Service due to unbounded memory growth via WebSocket frames. ([CRW-11356](https://redhat.atlassian.net/browse/CRW-11356))
- [CVE-2026-12143](https://access.redhat.com/security/cve/CVE-2026-12143): `form-data` -- Form field override via CRLF injection. ([CRW-11377](https://redhat.atlassian.net/browse/CRW-11377))
- [CVE-2026-45149](https://access.redhat.com/security/cve/CVE-2026-45149): `brace-expansion` -- Denial of Service due to excessive memory allocation when expanding large numeric ranges. ([CRW-11453](https://redhat.atlassian.net/browse/CRW-11453))

**dashboard-rhel9**

- [CVE-2026-12143](https://access.redhat.com/security/cve/CVE-2026-12143): `form-data` -- Form field override via CRLF injection. ([CRW-11376](https://redhat.atlassian.net/browse/CRW-11376))
- [CVE-2026-13149](https://access.redhat.com/security/cve/CVE-2026-13149): `brace-expansion` -- Denial of Service due to exponential-time complexity. ([CRW-11663](https://redhat.atlassian.net/browse/CRW-11663))
- [CVE-2026-13676](https://access.redhat.com/security/cve/CVE-2026-13676): `fast-uri` -- Security policy bypass due to improper Unicode hostname canonicalization. ([CRW-11535](https://redhat.atlassian.net/browse/CRW-11535))
- [CVE-2026-44990](https://access.redhat.com/security/cve/CVE-2026-44990): `sanitize-html` -- Stored Cross-Site Scripting via HTML sanitizer bypass. ([CRW-11484](https://redhat.atlassian.net/browse/CRW-11484))
- [CVE-2026-45149](https://access.redhat.com/security/cve/CVE-2026-45149): `brace-expansion` -- Denial of Service due to excessive memory allocation when expanding large numeric ranges. ([CRW-11450](https://redhat.atlassian.net/browse/CRW-11450))
- [CVE-2026-59869](https://access.redhat.com/security/cve/CVE-2026-59869): `js-yaml` -- Denial of Service via crafted YAML documents. ([CRW-11823](https://redhat.atlassian.net/browse/CRW-11823))
- [CVE-2026-59873](https://access.redhat.com/security/cve/CVE-2026-59873): `node-tar` -- Denial of Service via crafted gzip bomb. ([CRW-11758](https://redhat.atlassian.net/browse/CRW-11758))
- [CVE-2026-59874](https://access.redhat.com/security/cve/CVE-2026-59874): `node-tar` -- Denial of Service via malformed tar archive header. ([CRW-11761](https://redhat.atlassian.net/browse/CRW-11761))

**jetbrains-ide-rhel9**

- [CVE-2026-13149](https://access.redhat.com/security/cve/CVE-2026-13149): `brace-expansion` -- Denial of Service due to exponential-time complexity. ([CRW-11662](https://redhat.atlassian.net/browse/CRW-11662))
- [CVE-2026-44249](https://access.redhat.com/security/cve/CVE-2026-44249): `netty-handler` -- IPv6 subnet rule bypass due to incorrect masking operation. ([CRW-11401](https://redhat.atlassian.net/browse/CRW-11401))
- [CVE-2026-48043](https://access.redhat.com/security/cve/CVE-2026-48043): `netty-codec-http2` -- Denial of Service due to resource leak. ([CRW-11271](https://redhat.atlassian.net/browse/CRW-11271))

**server-rhel9**

- [CVE-2026-50193](https://access.redhat.com/security/cve/CVE-2026-50193): `jackson-databind` -- Denial of Service via deeply nested JSON processing. ([CRW-11567](https://redhat.atlassian.net/browse/CRW-11567))
- [CVE-2026-54512](https://access.redhat.com/security/cve/CVE-2026-54512): `jackson-databind` -- Arbitrary code execution via PolymorphicTypeValidator bypass. ([CRW-11557](https://redhat.atlassian.net/browse/CRW-11557))

**Related information**  

- [What is a CVE?](https://www.redhat.com/en/topics/security/what-is-cve)
- [Red Hat CVE Database](https://access.redhat.com/security/security-updates/cve)
