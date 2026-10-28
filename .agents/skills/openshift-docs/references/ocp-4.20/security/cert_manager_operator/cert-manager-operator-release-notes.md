<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The cert-manager Operator for Red Hat OpenShift is a cluster-wide service that provides application certificate lifecycle management.

These release notes track the development of cert-manager Operator for Red Hat OpenShift.

For more information, see [About the cert-manager Operator for Red Hat OpenShift](index.md#cert-manager-operator-about).

# cert-manager Operator for Red Hat OpenShift 1.20.1

Review the release notes for the cert-manager Operator for Red Hat OpenShift 1.20.1 to learn what is new and updated with this release.

Issued: 28 September 2026

The following advisories are available for the cert-manager Operator for Red Hat OpenShift for OpenShift Container Platform 1.20.1:

- [RHSA-2026:72476](https://access.redhat.com/errata/RHSA-2026:72476)

- [RHSA-2026:72470](https://access.redhat.com/errata/RHSA-2026:72470)

- [RHSA-2026:72475](https://access.redhat.com/errata/RHSA-2026:72475)

- [RHSA-2026:72502](https://access.redhat.com/errata/RHSA-2026:72502)

- [RHBA-2026:72606](https://access.redhat.com/errata/RHBA-2026:72606)

Version `v1.20.1` of the cert-manager Operator for Red Hat OpenShift is based on the upstream cert-manager version `v1.20.4`. For more information, see the [cert-manager project release notes for v1.20.4](https://cert-manager.io/docs/releases/release-notes/release-notes-1.20/#v1.20.4).

## CVEs

- [CVE-2026-84445](https://access.redhat.com/security/cve/CVE-2026-84445)

- [CVE-2026-73500](https://access.redhat.com/security/cve/CVE-2026-73500)

- [CVE-2026-29181](https://access.redhat.com/security/cve/CVE-2026-29181)

- [CVE-2026-46600](https://access.redhat.com/security/cve/CVE-2026-46600)

- [CVE-2026-42508](https://access.redhat.com/security/cve/CVE-2026-42508)

- [CVE-2026-39832](https://access.redhat.com/security/cve/CVE-2026-39832)

- [CVE-2026-33818](https://access.redhat.com/security/cve/CVE-2026-33818)

- [CVE-2026-56862](https://access.redhat.com/security/cve/CVE-2026-56862)

- [CVE-2026-56858](https://access.redhat.com/security/cve/CVE-2026-56858)

- [CVE-2026-56853](https://access.redhat.com/security/cve/CVE-2026-56853)

- [CVE-2026-56859](https://access.redhat.com/security/cve/CVE-2026-56859)

- [CVE-2026-56860](https://access.redhat.com/security/cve/CVE-2026-56860)

- [CVE-2026-41178](https://access.redhat.com/security/cve/CVE-2026-41178)

- [CVE-2026-56852](https://access.redhat.com/security/cve/CVE-2026-56852)

- [CVE-2026-71235](https://access.redhat.com/security/cve/CVE-2026-71235)

# cert-manager Operator for Red Hat OpenShift 1.20.0

Review the release notes for the cert-manager Operator for Red Hat OpenShift 1.20.0 to learn what is new and updated with this release.

Issued: 2 July 2026

The following advisories are available for the cert-manager Operator for Red Hat OpenShift for OpenShift Container Platform 1.20.0:

- [RHBA-2026:34294](https://access.redhat.com/errata/RHBA-2026:34294)

- [RHBA-2026:34309](https://access.redhat.com/errata/RHBA-2026:34309)

- [RHBA-2026:34336](https://access.redhat.com/errata/RHBA-2026:34336)

- [RHBA-2026:34714](https://access.redhat.com/errata/RHBA-2026:34714)

Version `1.20.0` of the cert-manager Operator for Red Hat OpenShift is based on the upstream cert-manager version `v1.20.3`. For more information, see the [cert-manager project release notes for v1.20.3](https://cert-manager.io/docs/releases/release-notes/release-notes-1.20/#v1203).

## New features and enhancements

> [!IMPORTANT]
> TLS adherence for cert-manager operands is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

TrustManager Technology Preview no longer requires a cluster preview FeatureSet
With this release, the cert-manager Operator for Red Hat OpenShift no longer requires the `featuregates.config.openshift.io/cluster` object to use a preview `FeatureSet`, such as `TechPreviewNoUpgrade`, in order to enable the TrustManager Technology Preview operand.

Previously, enabling TrustManager required both of the following conditions to be met:

- The cluster `FeatureSet` must be set to a preview value, such as `TechPreviewNoUpgrade`, `DevPreviewNoUpgrade`, or `CustomNoUpgrade`.

- The Operator subscription must opt in to TrustManager by setting `UNSUPPORTED_ADDON_FEATURES=TrustManager=true`.

  Customers running clusters with the `Default` `FeatureSet` were unable to evaluate TrustManager without first switching the cluster to a preview `FeatureSet`, which is a disruptive, cluster-wide change that prevents upgrades.

  With this update, the cluster `FeatureSet` requirement is removed. Enabling TrustManager now requires only that the Operator subscription includes `UNSUPPORTED_ADDON_FEATURES=TrustManager=true`. TrustManager remains a Technology Preview feature and is disabled by default.

  For more information, see [Enabling the TrustManager Operand](cert-manager-trust-manager.md#cert-manager-trust-manager-install_cert-manager-trust-manager).

New performance-tuning override arguments for the cert-manager controller
With this release, the cert-manager Operator for Red Hat OpenShift supports configuring performance-tuning parameters for the cert-manager controller by using the `overrideArgs` field of the `CertManager` custom resource (CR). Previously, users had to rely on `spec.unsupportedConfigOverrides` to tune these settings.

You can now set the following arguments under `spec.controllerConfig.overrideArgs`:

- `--concurrent-workers`: The number of concurrent workers for each controller. The default value is `5`.

- `--kube-api-qps`: The maximum number of queries per second sent to the Kubernetes API server. The default value is `20`.

- `--kube-api-burst`: The maximum burst of queries per second sent to the Kubernetes API server. Must be greater than or equal to `--kube-api-qps`. The default value is `50`.

- `--max-concurrent-challenges`: The maximum number of ACME challenges that can be scheduled as processing at the same time. The default value is `60`.

  The Operator validates that `--kube-api-burst` is greater than or equal to `--kube-api-qps` when both values are set. If this constraint is not met, the Operator sets the `Degraded` condition on the `CertManager` CR and does not apply the invalid configuration to the controller deployment.

  For more information, see [Overridable arguments for the cert-manager components](cert-manager-customizing-api-fields.md#cert-manager-overridable-arguments_cert-manager-customizing-api-fields).

Cluster TLS security profile applied to cert-manager operands
With this release, the cert-manager Operator for Red Hat OpenShift can read the cluster TLS security profile from the `apiserver.config.openshift.io/cluster` object and automatically apply the corresponding TLS configuration to the cert-manager controller, webhook, and CA injector deployments.

Previously, the TLS configuration for cert-manager operands was not tied to the cluster-wide TLS security profile. Cluster administrators who configured a stricter TLS profile at the cluster level had no automated mechanism to propagate those settings to cert-manager operands, creating a gap in cluster-wide TLS posture enforcement.

With this update, when the `spec.tlsAdherence` field of the `CertManager` custom resource (CR) is set to `StrictAllComponents`, the Operator reads the `spec.tlsSecurityProfile` value from `apiserver.config.openshift.io/cluster` and applies the corresponding TLS arguments to the cert-manager operand deployments. The Operator reconciles the deployments whenever the cluster TLS profile changes.

TLS arguments are applied per operand component as follows:

- `cert-manager-webhook`: serving TLS flags and metrics endpoint TLS flags.

- `cert-manager` (controller): metrics endpoint TLS flags only.

- `cert-manager-cainjector`: metrics endpoint TLS flags only.

  TLS profile enforcement is not yet supported for the IstioCSR and TrustManager operands.

  To support this feature, the Operator now requires `get`, `list`, and `watch` permissions on the `apiservers` resource in the `config.openshift.io` API group.

  This feature is gated by the `TLSAdherence` feature gate. To use this feature, you must enable the `TechPreviewNoUpgrade` feature set. For more information, see [Understanding feature gates](../../nodes/clusters/nodes-cluster-enabling-features.md#nodes-cluster-enabling-features-about_nodes-cluster-enabling).

  > [!NOTE]
  > Elliptic curve preferences are not configurable because cert-manager does not yet support specifying curve preferences upstream.

> [!IMPORTANT]
> {FeatureName} is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

## Fixed issues

- Before this update, the cert-manager Operator for Red Hat OpenShift installation failed on clusters with the Console capability disabled because the `ConsoleYAMLSample` resources were missing the required capability annotation. With this release, the Operator installs successfully on Console-less clusters. ([OCPBUGS-85579](https://redhat.atlassian.net/browse/OCPBUGS-85579))

# cert-manager Operator for Red Hat OpenShift 1.19.2

Review the release notes for the cert-manager Operator for Red Hat OpenShift 1.19.2 to learn what is new and updated with this release.

Issued: 3 September 2026

The following advisories are available for the cert-manager Operator for Red Hat OpenShift for OpenShift Container Platform 1.19.2:

- [RHSA-2026:63135](https://access.redhat.com/errata/RHSA-2026:63135)

- [RHSA-2026:63138](https://access.redhat.com/errata/RHSA-2026:63138)

- [RHSA-2026:63140](https://access.redhat.com/errata/RHSA-2026:63140)

Version `1.19.2` of the cert-manager Operator for Red Hat OpenShift is based on the upstream cert-manager version `v1.19.6`. For more information, see the [cert-manager project release notes for v1.19.6](https://cert-manager.io/docs/releases/release-notes/release-notes-1.19#v1196).

## CVEs

- [CVE-2026-11822](https://access.redhat.com/security/cve/CVE-2026-11822)

- [CVE-2026-11824](https://access.redhat.com/security/cve/CVE-2026-11824)

- [CVE-2026-15588](https://access.redhat.com/security/cve/CVE-2026-15588)

- [CVE-2026-1965](https://access.redhat.com/security/cve/CVE-2026-1965)

- [CVE-2026-29181](https://access.redhat.com/security/cve/CVE-2026-29181)

- [CVE-2026-3783](https://access.redhat.com/security/cve/CVE-2026-3783)

- [CVE-2026-39883](https://access.redhat.com/security/cve/CVE-2026-39883)

- [CVE-2026-46600](https://access.redhat.com/security/cve/CVE-2026-46600)

- [CVE-2026-54371](https://access.redhat.com/security/cve/CVE-2026-54371)

- [CVE-2026-56852](https://access.redhat.com/security/cve/CVE-2026-56852)

- [CVE-2026-58010](https://access.redhat.com/security/cve/CVE-2026-58010)

- [CVE-2026-58011](https://access.redhat.com/security/cve/CVE-2026-58011)

- [CVE-2026-58012](https://access.redhat.com/security/cve/CVE-2026-58012)

- [CVE-2026-58013](https://access.redhat.com/security/cve/CVE-2026-58013)

- [CVE-2026-58014](https://access.redhat.com/security/cve/CVE-2026-58014)

- [CVE-2026-58015](https://access.redhat.com/security/cve/CVE-2026-58015)

- [CVE-2026-58055](https://access.redhat.com/security/cve/CVE-2026-58055)

- [CVE-2026-8286](https://access.redhat.com/security/cve/CVE-2026-8286)

- [CVE-2026-9547](https://access.redhat.com/security/cve/CVE-2026-9547)

# cert-manager Operator for Red Hat OpenShift 1.19.1

Review the release notes for the cert-manager Operator for Red Hat OpenShift 1.19.1 to learn what is new and updated with this release.

Issued: 13 August 2026

The following advisories are available for the cert-manager Operator for Red Hat OpenShift for OpenShift Container Platform 1.19.1:

- [RHSA-2026:54527](https://access.redhat.com/errata/RHSA-2026:54527)

- [RHBA-2026:54529](https://access.redhat.com/errata/RHBA-2026:54529)

- [RHSA-2026:54531](https://access.redhat.com/errata/RHSA-2026:54531)

- [RHBA-2026:54551](https://access.redhat.com/errata/RHBA-2026:54551)

Version `1.19.1` of the cert-manager Operator for Red Hat OpenShift is based on the upstream cert-manager version `v1.19.6`. For more information, see the [cert-manager project release notes for v1.19.6](https://cert-manager.io/docs/releases/release-notes/release-notes-1.19#v1196).

## Fixed issues

- Before this update, the cert-manager Operator for Red Hat OpenShift installation failed on clusters without the console capability because the OLM bundle included `ConsoleYAMLSample` and `ConsoleQuickStart` resources that require the `console.openshift.io` APIs. With this release, the Operator creates the console resources at runtime only when the required APIs are available, ensuring successful installation. ([OCPBUGS-85579](https://redhat.atlassian.net/browse/OCPBUGS-85579))

## CVEs

- [CVE-2026-33186](https://access.redhat.com/security/cve/CVE-2026-33186)

- [CVE-2026-46595](https://access.redhat.com/security/cve/CVE-2026-46595)

- [CVE-2026-39821](https://access.redhat.com/security/cve/CVE-2026-39821)

- [CVE-2026-39828](https://access.redhat.com/security/cve/CVE-2026-39828)

- [CVE-2026-39830](https://access.redhat.com/security/cve/CVE-2026-39830)

- [CVE-2026-42499](https://access.redhat.com/security/cve/CVE-2026-42499)

- [CVE-2026-25681](https://access.redhat.com/security/cve/CVE-2026-25681)

- [CVE-2026-39820](https://access.redhat.com/security/cve/CVE-2026-39820)

- [CVE-2026-46597](https://access.redhat.com/security/cve/CVE-2026-46597)

- [CVE-2026-27145](https://access.redhat.com/security/cve/CVE-2026-27145)

- [CVE-2026-42504](https://access.redhat.com/security/cve/CVE-2026-42504)

- [CVE-2026-27136](https://access.redhat.com/security/cve/CVE-2026-27136)

- [CVE-2026-42502](https://access.redhat.com/security/cve/CVE-2026-42502)

# cert-manager Operator for Red Hat OpenShift 1.19.0

Review the release notes for the cert-manager Operator for Red Hat OpenShift 1.19.0 to learn what is new and updated with this release.

Issued: 20 April 2026

The following advisories are available for the cert-manager Operator for Red Hat OpenShift for OpenShift Container Platform 1.19.0:

- [RHBA-2026:9064](https://access.redhat.com/errata/RHBA-2026:9064)

- [RHBA-2026:9024](https://access.redhat.com/errata/RHBA-2026:9024)

- [RHBA-2026:8953](https://access.redhat.com/errata/RHBA-2026:8953)

- [RHBA-2026:9025](https://access.redhat.com/errata/RHBA-2026:9025)

- [RHBA-2026:8956](https://access.redhat.com/errata/RHBA-2026:8956)

Version `1.19.0` of the cert-manager Operator for Red Hat OpenShift is based on the upstream cert-manager version `v1.19.4`. For more information, see the [cert-manager project release notes for v1.19.4](https://cert-manager.io/docs/releases/release-notes/release-notes-1.19#v1194).

## New features and enhancements

Distribution of trust bundles with the trust manager operand (Technology Preview)
In this release, the cert-manager Operator for Red Hat OpenShift adds support for the trust-manager operand as a Technology Preview feature. You can now install the trust-manager operand to automate the secure distribution of trust bundles, such as certificate authority (CA) certificates, to application namespaces across your cluster. For more information, see [Distributing certificates by using trust-manager operand](cert-manager-trust-manager.md#cert-manager-trust-manager).

Support for configuring the certificate request backoff duration
In this release, the cert-manager Operator for Red Hat OpenShift adds support for the `--certificate-request-minimum-backoff-duration` flag. With this flag, you can configure the minimum backoff period for certificate requests by overriding the default configuration. For more information, see [Overridable arguments for the cert-manager components](cert-manager-customizing-api-fields.md#cert-manager-overridable-arguments_cert-manager-customizing-api-fields).

## Fixed issues

- Before this update, the **ClusterIssuer** form view lacked an option to remove the self-signed field. As a consequence, you could not create issuer types other than self-signed. With this release, the form view sets the certificate authority (CA) as the default issuer type. As a result, you can switch to other issuer types by using the form view. ([OCPBUGS-65620](https://redhat.atlassian.net/browse/OCPBUGS-65620))

# cert-manager Operator for Red Hat OpenShift 1.18.2

Review the release notes for the cert-manager Operator for Red Hat OpenShift 1.18.2 to learn what is new and updated with this release.

Issued: 16 October 2026

The following advisories are available for the cert-manager Operator for Red Hat OpenShift for OpenShift Container Platform 1.18.2:

- [RHSA-2026:82347](https://access.redhat.com/errata/RHSA-2026:82347)

- [RHSA-2026:82354](https://access.redhat.com/errata/RHSA-2026:82354)

- [RHSA-2026:82372](https://access.redhat.com/errata/RHSA-2026:82372)

- [RHSA-2026:82857](https://access.redhat.com/errata/RHSA-2026:82857)

Version `1.18.2` of the cert-manager Operator for Red Hat OpenShift is based on the upstream cert-manager version `v1.18.6`. For more information, see the [cert-manager project release notes for v1.18.6](https://cert-manager.io/docs/releases/release-notes/release-notes-1.18/#v1186).

## CVEs

- [CVE-2024-34459](https://access.redhat.com/security/cve/CVE-2024-34459)

- [CVE-2025-11187](https://access.redhat.com/security/cve/CVE-2025-11187)

- [CVE-2025-13151](https://access.redhat.com/security/cve/CVE-2025-13151)

- [CVE-2025-14087](https://access.redhat.com/security/cve/CVE-2025-14087)

- [CVE-2025-14104](https://access.redhat.com/security/cve/CVE-2025-14104)

- [CVE-2025-14512](https://access.redhat.com/security/cve/CVE-2025-14512)

- [CVE-2025-14831](https://access.redhat.com/security/cve/CVE-2025-14831)

- [CVE-2025-15281](https://access.redhat.com/security/cve/CVE-2025-15281)

- [CVE-2025-15467](https://access.redhat.com/security/cve/CVE-2025-15467)

- [CVE-2025-15468](https://access.redhat.com/security/cve/CVE-2025-15468)

- [CVE-2025-15469](https://access.redhat.com/security/cve/CVE-2025-15469)

- [CVE-2025-5278](https://access.redhat.com/security/cve/CVE-2025-5278)

- [CVE-2025-6170](https://access.redhat.com/security/cve/CVE-2025-6170)

- [CVE-2025-61726](https://access.redhat.com/security/cve/CVE-2025-61726)

- [CVE-2025-61728](https://access.redhat.com/security/cve/CVE-2025-61728)

- [CVE-2025-61730](https://access.redhat.com/security/cve/CVE-2025-61730)

- [CVE-2025-66199](https://access.redhat.com/security/cve/CVE-2025-66199)

- [CVE-2025-68121](https://access.redhat.com/security/cve/CVE-2025-68121)

- [CVE-2025-68160](https://access.redhat.com/security/cve/CVE-2025-68160)

- [CVE-2025-69418](https://access.redhat.com/security/cve/CVE-2025-69418)

- [CVE-2025-69419](https://access.redhat.com/security/cve/CVE-2025-69419)

- [CVE-2025-69420](https://access.redhat.com/security/cve/CVE-2025-69420)

- [CVE-2025-69421](https://access.redhat.com/security/cve/CVE-2025-69421)

- [CVE-2025-9086](https://access.redhat.com/security/cve/CVE-2025-9086)

- [CVE-2025-9820](https://access.redhat.com/security/cve/CVE-2025-9820)

- [CVE-2026-0861](https://access.redhat.com/security/cve/CVE-2026-0861)

- [CVE-2026-0915](https://access.redhat.com/security/cve/CVE-2026-0915)

- [CVE-2026-11822](https://access.redhat.com/security/cve/CVE-2026-11822)

- [CVE-2026-11824](https://access.redhat.com/security/cve/CVE-2026-11824)

- [CVE-2026-11979](https://access.redhat.com/security/cve/CVE-2026-11979)

- [CVE-2026-13757](https://access.redhat.com/security/cve/CVE-2026-13757)

- [CVE-2026-14164](https://access.redhat.com/security/cve/CVE-2026-14164)

- [CVE-2026-15588](https://access.redhat.com/security/cve/CVE-2026-15588)

- [CVE-2026-16118](https://access.redhat.com/security/cve/CVE-2026-16118)

- [CVE-2026-1965](https://access.redhat.com/security/cve/CVE-2026-1965)

- [CVE-2026-2100](https://access.redhat.com/security/cve/CVE-2026-2100)

- [CVE-2026-22795](https://access.redhat.com/security/cve/CVE-2026-22795)

- [CVE-2026-22796](https://access.redhat.com/security/cve/CVE-2026-22796)

- [CVE-2026-25679](https://access.redhat.com/security/cve/CVE-2026-25679)

- [CVE-2026-25681](https://access.redhat.com/security/cve/CVE-2026-25681)

- [CVE-2026-2673](https://access.redhat.com/security/cve/CVE-2026-2673)

- [CVE-2026-27135](https://access.redhat.com/security/cve/CVE-2026-27135)

- [CVE-2026-27145](https://access.redhat.com/security/cve/CVE-2026-27145)

- [CVE-2026-28390](https://access.redhat.com/security/cve/CVE-2026-28390)

- [CVE-2026-29111](https://access.redhat.com/security/cve/CVE-2026-29111)

- [CVE-2026-31790](https://access.redhat.com/security/cve/CVE-2026-31790)

- [CVE-2026-32280](https://access.redhat.com/security/cve/CVE-2026-32280)

- [CVE-2026-32281](https://access.redhat.com/security/cve/CVE-2026-32281)

- [CVE-2026-32283](https://access.redhat.com/security/cve/CVE-2026-32283)

- [CVE-2026-33186](https://access.redhat.com/security/cve/CVE-2026-33186)

- [CVE-2026-33811](https://access.redhat.com/security/cve/CVE-2026-33811)

- [CVE-2026-33814](https://access.redhat.com/security/cve/CVE-2026-33814)

- [CVE-2026-33818](https://access.redhat.com/security/cve/CVE-2026-33818)

- [CVE-2026-33845](https://access.redhat.com/security/cve/CVE-2026-33845)

- [CVE-2026-33846](https://access.redhat.com/security/cve/CVE-2026-33846)

- [CVE-2026-34180](https://access.redhat.com/security/cve/CVE-2026-34180)

- [CVE-2026-34181](https://access.redhat.com/security/cve/CVE-2026-34181)

- [CVE-2026-34182](https://access.redhat.com/security/cve/CVE-2026-34182)

- [CVE-2026-34183](https://access.redhat.com/security/cve/CVE-2026-34183)

- [CVE-2026-34986](https://access.redhat.com/security/cve/CVE-2026-34986)

- [CVE-2026-3783](https://access.redhat.com/security/cve/CVE-2026-3783)

- [CVE-2026-3832](https://access.redhat.com/security/cve/CVE-2026-3832)

- [CVE-2026-3833](https://access.redhat.com/security/cve/CVE-2026-3833)

- [CVE-2026-39820](https://access.redhat.com/security/cve/CVE-2026-39820)

- [CVE-2026-39822](https://access.redhat.com/security/cve/CVE-2026-39822)

- [CVE-2026-40355](https://access.redhat.com/security/cve/CVE-2026-40355)

- [CVE-2026-40356](https://access.redhat.com/security/cve/CVE-2026-40356)

- [CVE-2026-4046](https://access.redhat.com/security/cve/CVE-2026-4046)

- [CVE-2026-4111](https://access.redhat.com/security/cve/CVE-2026-4111)

- [CVE-2026-41989](https://access.redhat.com/security/cve/CVE-2026-41989)

- [CVE-2026-42009](https://access.redhat.com/security/cve/CVE-2026-42009)

- [CVE-2026-42010](https://access.redhat.com/security/cve/CVE-2026-42010)

- [CVE-2026-42011](https://access.redhat.com/security/cve/CVE-2026-42011)

- [CVE-2026-42012](https://access.redhat.com/security/cve/CVE-2026-42012)

- [CVE-2026-42013](https://access.redhat.com/security/cve/CVE-2026-42013)

- [CVE-2026-42014](https://access.redhat.com/security/cve/CVE-2026-42014)

- [CVE-2026-42015](https://access.redhat.com/security/cve/CVE-2026-42015)

- [CVE-2026-42499](https://access.redhat.com/security/cve/CVE-2026-42499)

- [CVE-2026-42504](https://access.redhat.com/security/cve/CVE-2026-42504)

- [CVE-2026-42764](https://access.redhat.com/security/cve/CVE-2026-42764)

- [CVE-2026-42766](https://access.redhat.com/security/cve/CVE-2026-42766)

- [CVE-2026-42767](https://access.redhat.com/security/cve/CVE-2026-42767)

- [CVE-2026-42768](https://access.redhat.com/security/cve/CVE-2026-42768)

- [CVE-2026-42769](https://access.redhat.com/security/cve/CVE-2026-42769)

- [CVE-2026-42770](https://access.redhat.com/security/cve/CVE-2026-42770)

- [CVE-2026-4424](https://access.redhat.com/security/cve/CVE-2026-4424)

- [CVE-2026-4437](https://access.redhat.com/security/cve/CVE-2026-4437)

- [CVE-2026-4438](https://access.redhat.com/security/cve/CVE-2026-4438)

- [CVE-2026-45445](https://access.redhat.com/security/cve/CVE-2026-45445)

- [CVE-2026-45446](https://access.redhat.com/security/cve/CVE-2026-45446)

- [CVE-2026-45447](https://access.redhat.com/security/cve/CVE-2026-45447)

- [CVE-2026-46597](https://access.redhat.com/security/cve/CVE-2026-46597)

- [CVE-2026-4878](https://access.redhat.com/security/cve/CVE-2026-4878)

- [CVE-2026-48864](https://access.redhat.com/security/cve/CVE-2026-48864)

- [CVE-2026-5121](https://access.redhat.com/security/cve/CVE-2026-5121)

- [CVE-2026-5260](https://access.redhat.com/security/cve/CVE-2026-5260)

- [CVE-2026-5419](https://access.redhat.com/security/cve/CVE-2026-5419)

- [CVE-2026-5435](https://access.redhat.com/security/cve/CVE-2026-5435)

- [CVE-2026-54369](https://access.redhat.com/security/cve/CVE-2026-54369)

- [CVE-2026-54370](https://access.redhat.com/security/cve/CVE-2026-54370)

- [CVE-2026-54371](https://access.redhat.com/security/cve/CVE-2026-54371)

- [CVE-2026-5450](https://access.redhat.com/security/cve/CVE-2026-5450)

- [CVE-2026-56858](https://access.redhat.com/security/cve/CVE-2026-56858)

- [CVE-2026-56859](https://access.redhat.com/security/cve/CVE-2026-56859)

- [CVE-2026-56860](https://access.redhat.com/security/cve/CVE-2026-56860)

- [CVE-2026-56862](https://access.redhat.com/security/cve/CVE-2026-56862)

- [CVE-2026-58010](https://access.redhat.com/security/cve/CVE-2026-58010)

- [CVE-2026-58011](https://access.redhat.com/security/cve/CVE-2026-58011)

- [CVE-2026-58012](https://access.redhat.com/security/cve/CVE-2026-58012)

- [CVE-2026-58013](https://access.redhat.com/security/cve/CVE-2026-58013)

- [CVE-2026-58014](https://access.redhat.com/security/cve/CVE-2026-58014)

- [CVE-2026-58015](https://access.redhat.com/security/cve/CVE-2026-58015)

- [CVE-2026-58016](https://access.redhat.com/security/cve/CVE-2026-58016)

- [CVE-2026-58055](https://access.redhat.com/security/cve/CVE-2026-58055)

- [CVE-2026-5928](https://access.redhat.com/security/cve/CVE-2026-5928)

- [CVE-2026-6238](https://access.redhat.com/security/cve/CVE-2026-6238)

- [CVE-2026-6653](https://access.redhat.com/security/cve/CVE-2026-6653)

- [CVE-2026-7383](https://access.redhat.com/security/cve/CVE-2026-7383)

- [CVE-2026-8286](https://access.redhat.com/security/cve/CVE-2026-8286)

- [CVE-2026-9076](https://access.redhat.com/security/cve/CVE-2026-9076)

- [CVE-2026-9547](https://access.redhat.com/security/cve/CVE-2026-9547)

- [CVE-2025-47911](https://access.redhat.com/security/cve/CVE-2025-47911)

- [CVE-2025-47913](https://access.redhat.com/security/cve/CVE-2025-47913)

- [CVE-2025-47914](https://access.redhat.com/security/cve/CVE-2025-47914)

- [CVE-2025-58181](https://access.redhat.com/security/cve/CVE-2025-58181)

- [CVE-2025-58190](https://access.redhat.com/security/cve/CVE-2025-58190)

- [CVE-2026-27136](https://access.redhat.com/security/cve/CVE-2026-27136)

# cert-manager Operator for Red Hat OpenShift 1.17.2

Review the release notes for the cert-manager Operator for Red Hat OpenShift 1.17.2 to learn what is new and updated with this release.

Issued: 16 October 2026

The following advisories are available for the cert-manager Operator for Red Hat OpenShift for OpenShift Container Platform 1.17.2:

- [RHSA-2026:82304](https://access.redhat.com/errata/RHSA-2026:82304)

- [RHSA-2026:82322](https://access.redhat.com/errata/RHSA-2026:82322)

- [RHSA-2026:82336](https://access.redhat.com/errata/RHSA-2026:82336)

- [RHSA-2026:82888](https://access.redhat.com/errata/RHSA-2026:82888)

Version `1.17.2` of the cert-manager Operator for Red Hat OpenShift is based on the upstream cert-manager version `v1.17.4`. For more information, see the [cert-manager project release notes for v1.17.4](https://cert-manager.io/docs/releases/release-notes/release-notes-1.17#v1174).

## CVEs

- [CVE-2022-29458](https://access.redhat.com/security/cve/CVE-2022-29458)

- [CVE-2024-8176](https://access.redhat.com/security/cve/CVE-2024-8176)

- [CVE-2024-12133](https://access.redhat.com/security/cve/CVE-2024-12133)

- [CVE-2024-12243](https://access.redhat.com/security/cve/CVE-2024-12243)

- [CVE-2024-12718](https://access.redhat.com/security/cve/CVE-2024-12718)

- [CVE-2024-34459](https://access.redhat.com/security/cve/CVE-2024-34459)

- [CVE-2024-52533](https://access.redhat.com/security/cve/CVE-2024-52533)

- [CVE-2025-3576](https://access.redhat.com/security/cve/CVE-2025-3576)

- [CVE-2025-4138](https://access.redhat.com/security/cve/CVE-2025-4138)

- [CVE-2025-4330](https://access.redhat.com/security/cve/CVE-2025-4330)

- [CVE-2025-4373](https://access.redhat.com/security/cve/CVE-2025-4373)

- [CVE-2025-4435](https://access.redhat.com/security/cve/CVE-2025-4435)

- [CVE-2025-4517](https://access.redhat.com/security/cve/CVE-2025-4517)

- [CVE-2025-4673](https://access.redhat.com/security/cve/CVE-2025-4673)

- [CVE-2025-4802](https://access.redhat.com/security/cve/CVE-2025-4802)

- [CVE-2025-5278](https://access.redhat.com/security/cve/CVE-2025-5278)

- [CVE-2025-5914](https://access.redhat.com/security/cve/CVE-2025-5914)

- [CVE-2025-6020](https://access.redhat.com/security/cve/CVE-2025-6020)

- [CVE-2025-6021](https://access.redhat.com/security/cve/CVE-2025-6021)

- [CVE-2025-6170](https://access.redhat.com/security/cve/CVE-2025-6170)

- [CVE-2025-6395](https://access.redhat.com/security/cve/CVE-2025-6395)

- [CVE-2025-6965](https://access.redhat.com/security/cve/CVE-2025-6965)

- [CVE-2025-7425](https://access.redhat.com/security/cve/CVE-2025-7425)

- [CVE-2025-8194](https://access.redhat.com/security/cve/CVE-2025-8194)

- [CVE-2025-8941](https://access.redhat.com/security/cve/CVE-2025-8941)

- [CVE-2025-9086](https://access.redhat.com/security/cve/CVE-2025-9086)

- [CVE-2025-9230](https://access.redhat.com/security/cve/CVE-2025-9230)

- [CVE-2025-9714](https://access.redhat.com/security/cve/CVE-2025-9714)

- [CVE-2025-12084](https://access.redhat.com/security/cve/CVE-2025-12084)

- [CVE-2025-13151](https://access.redhat.com/security/cve/CVE-2025-13151)

- [CVE-2025-13601](https://access.redhat.com/security/cve/CVE-2025-13601)

- [CVE-2025-14087](https://access.redhat.com/security/cve/CVE-2025-14087)

- [CVE-2025-14512](https://access.redhat.com/security/cve/CVE-2025-14512)

- [CVE-2025-14831](https://access.redhat.com/security/cve/CVE-2025-14831)

- [CVE-2025-15366](https://access.redhat.com/security/cve/CVE-2025-15366)

- [CVE-2025-15367](https://access.redhat.com/security/cve/CVE-2025-15367)

- [CVE-2025-15467](https://access.redhat.com/security/cve/CVE-2025-15467)

- [CVE-2025-22871](https://access.redhat.com/security/cve/CVE-2025-22871)

- [CVE-2025-22873](https://access.redhat.com/security/cve/CVE-2025-22873)

- [CVE-2025-32414](https://access.redhat.com/security/cve/CVE-2025-32414)

- [CVE-2025-32415](https://access.redhat.com/security/cve/CVE-2025-32415)

- [CVE-2025-32988](https://access.redhat.com/security/cve/CVE-2025-32988)

- [CVE-2025-32989](https://access.redhat.com/security/cve/CVE-2025-32989)

- [CVE-2025-32990](https://access.redhat.com/security/cve/CVE-2025-32990)

- [CVE-2025-45582](https://access.redhat.com/security/cve/CVE-2025-45582)

- [CVE-2025-47273](https://access.redhat.com/security/cve/CVE-2025-47273)

- [CVE-2025-47906](https://access.redhat.com/security/cve/CVE-2025-47906)

- [CVE-2025-47907](https://access.redhat.com/security/cve/CVE-2025-47907)

- [CVE-2025-47911](https://access.redhat.com/security/cve/CVE-2025-47911)

- [CVE-2025-47912](https://access.redhat.com/security/cve/CVE-2025-47912)

- [CVE-2025-47913](https://access.redhat.com/security/cve/CVE-2025-47913)

- [CVE-2025-47914](https://access.redhat.com/security/cve/CVE-2025-47914)

- [CVE-2025-49794](https://access.redhat.com/security/cve/CVE-2025-49794)

- [CVE-2025-49796](https://access.redhat.com/security/cve/CVE-2025-49796)

- [CVE-2025-53905](https://access.redhat.com/security/cve/CVE-2025-53905)

- [CVE-2025-53906](https://access.redhat.com/security/cve/CVE-2025-53906)

- [CVE-2025-58181](https://access.redhat.com/security/cve/CVE-2025-58181)

- [CVE-2025-58183](https://access.redhat.com/security/cve/CVE-2025-58183)

- [CVE-2025-58185](https://access.redhat.com/security/cve/CVE-2025-58185)

- [CVE-2025-58186](https://access.redhat.com/security/cve/CVE-2025-58186)

- [CVE-2025-58187](https://access.redhat.com/security/cve/CVE-2025-58187)

- [CVE-2025-58188](https://access.redhat.com/security/cve/CVE-2025-58188)

- [CVE-2025-58189](https://access.redhat.com/security/cve/CVE-2025-58189)

- [CVE-2025-58190](https://access.redhat.com/security/cve/CVE-2025-58190)

- [CVE-2025-59375](https://access.redhat.com/security/cve/CVE-2025-59375)

- [CVE-2025-61723](https://access.redhat.com/security/cve/CVE-2025-61723)

- [CVE-2025-61724](https://access.redhat.com/security/cve/CVE-2025-61724)

- [CVE-2025-61725](https://access.redhat.com/security/cve/CVE-2025-61725)

- [CVE-2025-61726](https://access.redhat.com/security/cve/CVE-2025-61726)

- [CVE-2025-61727](https://access.redhat.com/security/cve/CVE-2025-61727)

- [CVE-2025-61728](https://access.redhat.com/security/cve/CVE-2025-61728)

- [CVE-2025-61729](https://access.redhat.com/security/cve/CVE-2025-61729)

- [CVE-2025-61730](https://access.redhat.com/security/cve/CVE-2025-61730)

- [CVE-2025-66418](https://access.redhat.com/security/cve/CVE-2025-66418)

- [CVE-2025-66471](https://access.redhat.com/security/cve/CVE-2025-66471)

- [CVE-2025-68121](https://access.redhat.com/security/cve/CVE-2025-68121)

- [CVE-2025-68973](https://access.redhat.com/security/cve/CVE-2025-68973)

- [CVE-2025-69419](https://access.redhat.com/security/cve/CVE-2025-69419)

- [CVE-2026-1299](https://access.redhat.com/security/cve/CVE-2026-1299)

- [CVE-2026-1965](https://access.redhat.com/security/cve/CVE-2026-1965)

- [CVE-2026-2100](https://access.redhat.com/security/cve/CVE-2026-2100)

- [CVE-2026-2673](https://access.redhat.com/security/cve/CVE-2026-2673)

- [CVE-2026-3783](https://access.redhat.com/security/cve/CVE-2026-3783)

- [CVE-2026-3832](https://access.redhat.com/security/cve/CVE-2026-3832)

- [CVE-2026-3833](https://access.redhat.com/security/cve/CVE-2026-3833)

- [CVE-2026-4046](https://access.redhat.com/security/cve/CVE-2026-4046)

- [CVE-2026-4111](https://access.redhat.com/security/cve/CVE-2026-4111)

- [CVE-2026-4424](https://access.redhat.com/security/cve/CVE-2026-4424)

- [CVE-2026-4437](https://access.redhat.com/security/cve/CVE-2026-4437)

- [CVE-2026-4438](https://access.redhat.com/security/cve/CVE-2026-4438)

- [CVE-2026-4519](https://access.redhat.com/security/cve/CVE-2026-4519)

- [CVE-2026-4786](https://access.redhat.com/security/cve/CVE-2026-4786)

- [CVE-2026-4878](https://access.redhat.com/security/cve/CVE-2026-4878)

- [CVE-2026-5121](https://access.redhat.com/security/cve/CVE-2026-5121)

- [CVE-2026-5260](https://access.redhat.com/security/cve/CVE-2026-5260)

- [CVE-2026-5419](https://access.redhat.com/security/cve/CVE-2026-5419)

- [CVE-2026-5435](https://access.redhat.com/security/cve/CVE-2026-5435)

- [CVE-2026-5450](https://access.redhat.com/security/cve/CVE-2026-5450)

- [CVE-2026-5928](https://access.redhat.com/security/cve/CVE-2026-5928)

- [CVE-2026-6100](https://access.redhat.com/security/cve/CVE-2026-6100)

- [CVE-2026-6238](https://access.redhat.com/security/cve/CVE-2026-6238)

- [CVE-2026-6653](https://access.redhat.com/security/cve/CVE-2026-6653)

- [CVE-2026-7383](https://access.redhat.com/security/cve/CVE-2026-7383)

- [CVE-2026-8286](https://access.redhat.com/security/cve/CVE-2026-8286)

- [CVE-2026-9076](https://access.redhat.com/security/cve/CVE-2026-9076)

- [CVE-2026-9547](https://access.redhat.com/security/cve/CVE-2026-9547)

- [CVE-2026-11822](https://access.redhat.com/security/cve/CVE-2026-11822)

- [CVE-2026-11824](https://access.redhat.com/security/cve/CVE-2026-11824)

- [CVE-2026-11979](https://access.redhat.com/security/cve/CVE-2026-11979)

- [CVE-2026-13757](https://access.redhat.com/security/cve/CVE-2026-13757)

- [CVE-2026-14164](https://access.redhat.com/security/cve/CVE-2026-14164)

- [CVE-2026-15588](https://access.redhat.com/security/cve/CVE-2026-15588)

- [CVE-2026-16118](https://access.redhat.com/security/cve/CVE-2026-16118)

- [CVE-2026-21441](https://access.redhat.com/security/cve/CVE-2026-21441)

- [CVE-2026-25679](https://access.redhat.com/security/cve/CVE-2026-25679)

- [CVE-2026-25681](https://access.redhat.com/security/cve/CVE-2026-25681)

- [CVE-2026-25749](https://access.redhat.com/security/cve/CVE-2026-25749)

- [CVE-2026-27135](https://access.redhat.com/security/cve/CVE-2026-27135)

- [CVE-2026-27136](https://access.redhat.com/security/cve/CVE-2026-27136)

- [CVE-2026-27145](https://access.redhat.com/security/cve/CVE-2026-27145)

- [CVE-2026-28390](https://access.redhat.com/security/cve/CVE-2026-28390)

- [CVE-2026-28417](https://access.redhat.com/security/cve/CVE-2026-28417)

- [CVE-2026-28421](https://access.redhat.com/security/cve/CVE-2026-28421)

- [CVE-2026-29111](https://access.redhat.com/security/cve/CVE-2026-29111)

- [CVE-2026-29181](https://access.redhat.com/security/cve/CVE-2026-29181)

- [CVE-2026-31790](https://access.redhat.com/security/cve/CVE-2026-31790)

- [CVE-2026-32280](https://access.redhat.com/security/cve/CVE-2026-32280)

- [CVE-2026-32281](https://access.redhat.com/security/cve/CVE-2026-32281)

- [CVE-2026-32283](https://access.redhat.com/security/cve/CVE-2026-32283)

- [CVE-2026-33186](https://access.redhat.com/security/cve/CVE-2026-33186)

- [CVE-2026-33412](https://access.redhat.com/security/cve/CVE-2026-33412)

- [CVE-2026-33811](https://access.redhat.com/security/cve/CVE-2026-33811)

- [CVE-2026-33814](https://access.redhat.com/security/cve/CVE-2026-33814)

- [CVE-2026-33818](https://access.redhat.com/security/cve/CVE-2026-33818)

- [CVE-2026-33845](https://access.redhat.com/security/cve/CVE-2026-33845)

- [CVE-2026-33846](https://access.redhat.com/security/cve/CVE-2026-33846)

- [CVE-2026-34180](https://access.redhat.com/security/cve/CVE-2026-34180)

- [CVE-2026-34181](https://access.redhat.com/security/cve/CVE-2026-34181)

- [CVE-2026-34182](https://access.redhat.com/security/cve/CVE-2026-34182)

- [CVE-2026-34183](https://access.redhat.com/security/cve/CVE-2026-34183)

- [CVE-2026-34986](https://access.redhat.com/security/cve/CVE-2026-34986)

- [CVE-2026-39820](https://access.redhat.com/security/cve/CVE-2026-39820)

- [CVE-2026-39821](https://access.redhat.com/security/cve/CVE-2026-39821)

- [CVE-2026-39822](https://access.redhat.com/security/cve/CVE-2026-39822)

- [CVE-2026-39829](https://access.redhat.com/security/cve/CVE-2026-39829)

- [CVE-2026-39832](https://access.redhat.com/security/cve/CVE-2026-39832)

- [CVE-2026-40355](https://access.redhat.com/security/cve/CVE-2026-40355)

- [CVE-2026-40356](https://access.redhat.com/security/cve/CVE-2026-40356)

- [CVE-2026-41989](https://access.redhat.com/security/cve/CVE-2026-41989)

- [CVE-2026-42009](https://access.redhat.com/security/cve/CVE-2026-42009)

- [CVE-2026-42010](https://access.redhat.com/security/cve/CVE-2026-42010)

- [CVE-2026-42011](https://access.redhat.com/security/cve/CVE-2026-42011)

- [CVE-2026-42012](https://access.redhat.com/security/cve/CVE-2026-42012)

- [CVE-2026-42013](https://access.redhat.com/security/cve/CVE-2026-42013)

- [CVE-2026-42014](https://access.redhat.com/security/cve/CVE-2026-42014)

- [CVE-2026-42015](https://access.redhat.com/security/cve/CVE-2026-42015)

- [CVE-2026-42499](https://access.redhat.com/security/cve/CVE-2026-42499)

- [CVE-2026-42504](https://access.redhat.com/security/cve/CVE-2026-42504)

- [CVE-2026-42764](https://access.redhat.com/security/cve/CVE-2026-42764)

- [CVE-2026-42766](https://access.redhat.com/security/cve/CVE-2026-42766)

- [CVE-2026-42767](https://access.redhat.com/security/cve/CVE-2026-42767)

- [CVE-2026-42768](https://access.redhat.com/security/cve/CVE-2026-42768)

- [CVE-2026-42769](https://access.redhat.com/security/cve/CVE-2026-42769)

- [CVE-2026-42770](https://access.redhat.com/security/cve/CVE-2026-42770)

- [CVE-2026-45445](https://access.redhat.com/security/cve/CVE-2026-45445)

- [CVE-2026-45446](https://access.redhat.com/security/cve/CVE-2026-45446)

- [CVE-2026-45447](https://access.redhat.com/security/cve/CVE-2026-45447)

- [CVE-2026-46597](https://access.redhat.com/security/cve/CVE-2026-46597)

- [CVE-2026-48864](https://access.redhat.com/security/cve/CVE-2026-48864)

- [CVE-2026-54369](https://access.redhat.com/security/cve/CVE-2026-54369)

- [CVE-2026-54370](https://access.redhat.com/security/cve/CVE-2026-54370)

- [CVE-2026-54371](https://access.redhat.com/security/cve/CVE-2026-54371)

- [CVE-2026-56858](https://access.redhat.com/security/cve/CVE-2026-56858)

- [CVE-2026-56859](https://access.redhat.com/security/cve/CVE-2026-56859)

- [CVE-2026-56860](https://access.redhat.com/security/cve/CVE-2026-56860)

- [CVE-2026-56862](https://access.redhat.com/security/cve/CVE-2026-56862)

- [CVE-2026-58010](https://access.redhat.com/security/cve/CVE-2026-58010)

- [CVE-2026-58011](https://access.redhat.com/security/cve/CVE-2026-58011)

- [CVE-2026-58012](https://access.redhat.com/security/cve/CVE-2026-58012)

- [CVE-2026-58013](https://access.redhat.com/security/cve/CVE-2026-58013)

- [CVE-2026-58014](https://access.redhat.com/security/cve/CVE-2026-58014)

- [CVE-2026-58015](https://access.redhat.com/security/cve/CVE-2026-58015)

- [CVE-2026-58016](https://access.redhat.com/security/cve/CVE-2026-58016)

- [CVE-2026-58055](https://access.redhat.com/security/cve/CVE-2026-58055)
