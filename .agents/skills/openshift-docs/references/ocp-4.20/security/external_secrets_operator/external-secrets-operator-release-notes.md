<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The External Secrets Operator for Red Hat OpenShift is a cluster-wide service that provides lifecycle management for secrets fetched from external secret management systems.

These release notes track the development of External Secrets Operator.

For more information, see [External Secrets Operator overview](index.md#external-secrets-operator-about).

# Release notes for External Secrets Operator for Red Hat OpenShift 1.2.0

External Secrets Operator for Red Hat OpenShift version 1.2.0 is based on the upstream external-secrets project, version v2.5.0.

Issued: 2026-07-09

The following advisories are available for the External Secrets Operator for Red Hat OpenShift 1.2.0:

- [RHBA-2026:36640](https://access.redhat.com/errata/RHBA-2026:36640)

- [RHBA-2026:36647](https://access.redhat.com/errata/RHBA-2026:36647)

- [RHBA-2026:36650](https://access.redhat.com/errata/RHBA-2026:36650)

- [RHBA-2026:36676](https://access.redhat.com/errata/RHBA-2026:36676)

## New features and enhancements

**Support for user-provided trusted CA bundles on the External Secrets Operator core controller**

With this release, you can configure the External Secrets Operator for Red Hat OpenShift to trust custom Certificate Authority (CA) certificates when the `external-secrets` core controller makes outbound TLS connections to external secret management systems, such as HashiCorp Vault or Amazon Web Services (AWS) Secrets Manager.

To use this feature, create a `ConfigMap` object in the operand namespace containing one or more PEM-encoded CA certificates, and reference it in the `ExternalSecretsConfig` custom resource under the `spec.controllerConfig.trustedCABundle` field. The Operator validates the bundle on every reconcile and mounts it as a volume only on the core controller deployment. The webhook and cert-controller deployments are not affected.

If the referenced `ConfigMap` object is missing or contains invalid data, the Operator sets the `ExternalSecretsConfig` custom resource (CR) status to `Degraded` and emits a warning event describing the problem. The Operator recovers automatically when the `ConfigMap` object is created or corrected, without requiring a spec change.

If the proxy is configured and the `ConfigMap` carries the Cluster Network Operator (CNO) `inject-trusted-cabundle` label, the user bundle mount is skipped because the proxy TLS connections already use the OpenShift Container Platform trusted CA bundle injected by the CNO.

For more information, see [Configuring a trusted CA bundle for the External Secrets Operator for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html-single/security_and_compliance/index#external-secrets-operator-config-trusted-ca).

**Optional feature configuration is available for External Secrets Operator deployments**

With this release, the `ExternalSecretsManager` CR supports a `spec.features` field for toggling optional capabilities across operator-managed deployments. Each entry is identified by name and can be individually set to `Enabled` or `Disabled`.

The first supported feature is `UnsafeAllowGenericTargets`. When enabled, the Operator passes the `--unsafe-allow-generic-targets` flag to the `external-secrets` core controller, allowing `ExternalSecret` resources to sync secrets into Kubernetes resources other than `Secret` objects.

> [!IMPORTANT]
> `UnsafeAllowGenericTargets` is a pre-release feature in the upstream `external-secrets` project. The `UnsafeAllowGenericTargets` feature has the following limitations:
>
> - Only namespaced resources can be targeted, and only by an `ExternalSecret` CR in the same namespace as the target resource.
>
> - Performance is approximately 20% slower than standard `Secret` synchronization.
>
> - Custom resources are not encrypted at rest by Kubernetes. Use this feature only when the target resource does not contain sensitive credentials, or when encryption is provided by other means.

Enabling this feature also requires that the `external-secret` service account has the appropriate role-based access control (RBAC) permissions to create and update the target resource types. Without these permissions, secret synchronization for affected `ExternalSecret` CR resources fails.

**Improved status reporting for invalid user configuration**

With this release, the External Secrets Operator for Red Hat OpenShift distinguishes between Operator-level failures and user configuration errors during reconciliation. When an invalid or incomplete user configuration is detected, such as a missing cert-manager issuer reference or an incomplete Bitwarden TLS setup, the Operator immediately sets the `ExternalSecretsConfig` CR status to `Degraded=True` and `Ready=False` without entering an exponential backoff retry loop.

The Operator recovers automatically when the configuration is corrected. If a referenced object does not yet exist, the Operator requeues periodically until the object is created.

**Automatic proxy egress NetworkPolicy management**

With this release, the External Secrets Operator for Red Hat OpenShift automatically creates, updates, and deletes a proxy egress `NetworkPolicy` named `eso-sys-allow-proxy-egress`, for all `external-secrets` pods when a cluster proxy is configured. The policy allows outbound traffic from operand pods to the configured proxy server port. You can control whether the Operator manages this policy by setting the `networkPolicyProvisioning` field on the proxy configuration to `Managed` or `Unmanaged`. When set to `Unmanaged`, no proxy egress policy is created or deleted by the Operator.

**Standardized NetworkPolicy naming**

With this release, Operator-managed `NetworkPolicies` now use an `eso-sys-` prefix such as `eso-sys-deny-all-traffic`, `eso-sys-allow-to-dns`, and so on. User-configured `NetworkPolicies` defined in the `spec.controllerConfig.networkPolicies` field now use an `eso-user-` prefix when the Kubernetes object is created. This makes it easier to distinguish Operator-managed policies from user-defined ones.

As a result of the `eso-user-` prefix, the maximum length for the name field in `spec.controllerConfig.networkPolicies` entries is reduced from 253 to 243 characters.

**Automatic migration of legacy NetworkPolicy names**

With this release, when upgrading from a version that used unprefixed `NetworkPolicy` names, the Operator automatically detects and deletes the legacy unprefixed `NetworkPolicies` during the first reconciliation after upgrade. This migration runs once per cluster and is gated by the `externalsecretsconfig.operator.openshift.io/skip-np-cleanup-check` annotation so that subsequent reconciliations do not repeat the cleanup scan.

## Fixed issues

- Before this release, if the `app=external-secrets` managed label was externally removed from a resource that the External Secrets Operator for Red Hat OpenShift owns, the resource fell out of the label-filtered informer cache. Subsequent reconciliation attempts to create the resource received an `AlreadyExists` error, causing the controller to enter a permanent error loop. With this release, the controller detects this cache-miss condition and restores the managed labels and annotations directly on the API server by using an uncached client, without interrupting the operand. ([ESO-237](https://issues.redhat.com/browse/ESO-237))

# Release notes for External Secrets Operator for Red Hat OpenShift 1.1.0

External Secrets Operator for Red Hat OpenShift version 1.1.0 is based on the upstream external-secrets project, version v0.20.4.

Issued: 2026-03-17

The following advisories are available for the External Secrets Operator for Red Hat OpenShift 1.1.0:

- [RHBA-2026:5554](https://access.redhat.com/errata/RHBA-2026:5554)

- [RHBA-2026:5555](https://access.redhat.com/errata/RHBA-2026:5555)

- [RHBA-2026:5558](https://access.redhat.com/errata/RHBA-2026:5557)

- [RHBA-2026:5589](https://access.redhat.com/errata/RHBA-2026:5589)

## New features and enhancements

**Customization feature is now available for External Secrets Operator components**

With this release, the Operator API, `externalsecretsconfig.operator.openshift.io` allows users to customize various aspects of the `external-secrets` controllers. The new API allows users to add custom annotations and environment variables, and allows configuring revision history limits for the `external-secrets` deployments.

For more information, see [Customizing the External Secrets Operator for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/security_and_compliance/index#external-secrets-log-levels).

# Release notes for External Secrets Operator for Red Hat OpenShift 1.0.1

External Secrets Operator for Red Hat OpenShift 1.0.1 is based on the upstream external-secrets version 0.19.2.

Issued: 16 July 2026

This release fixes some Common Vulnerabilities and Exposures (CVEs) and provides related Red Hat advisories.

The following advisories are available for the External Secrets Operator for Red Hat OpenShift:

- [RHSA-2026:40924](https://access.redhat.com/errata/RHSA-2026:40924)

- [RHBA-2026:40923](https://access.redhat.com/errata/RHBA-2026:40923)

- [RHBA-2026:40925](https://access.redhat.com/errata/RHBA-2026:40925)

- [RHBA-2026:41014](https://access.redhat.com/errata/RHBA-2026:41014)

## CVEs

- [CVE-2025-61726](https://access.redhat.com/security/cve/cve-2025-61726)

- [CVE-2025-68121](https://access.redhat.com/security/cve/cve-2025-68121)

# Release notes for External Secrets Operator for Red Hat OpenShift 1.0.0 (General Availability)

External Secrets Operator for Red Hat OpenShift version 1.0.0 is based on the upstream external-secrets project, version v0.19.0.

Issued: 2025-11-03

The following advisories are available for the External Secrets Operator for Red Hat OpenShift 1.0.0:

- [RHBA-2025:19416](https://access.redhat.com/errata/RHBA-2025:19416)

- [RHBA-2025:19417](https://access.redhat.com/errata/RHBA-2025:19417)

- [RHBA-2025:19418](https://access.redhat.com/errata/RHBA-2025:19418)

- [RHBA-2025:19463](https://access.redhat.com/errata/RHBA-2025:19463)

## Fixed issues

- Before this release, many of the APIs listed in the console for the External Secrets Operator for Red Hat OpenShift were missing descriptions. With this release, the API descriptions have been added. ([OCPBUGS-61081](https://issues.redhat.com/browse/OCPBUGS-61081))

## New features and enhancements

**Renaming and improvements on the Operator API**

With this release, the Operator API, `externalsecrets.operator.openshift.io` has been renamed to `externalsecretsconfigs.operator.openshift.io` to avoid confusion with the external-secrets provided API that has the same name, but a different purpose. The external-secrets provided API has also been restructured and new features are added.

For more information, see [External Secrets Operator for Red Hat OpenShift APIs](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html-single/security_and_compliance/index#external-secrets-operator-api).

**Support to collect metrics of External Secrets Operator**

With this release, the External Secrets Operator for Red Hat OpenShift supports collecting metrics for both the Operator and operands. This is optional and must be enabled.

For more information, see [Monitoring the External Secrets Operator for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html-single/security_and_compliance/index#external-secrets-monitoring).

**Support to configure proxy for External Secrets Operator**

With this release, the External Secrets Operator for Red Hat OpenShift supports configuring proxy for both the Operator and operand.

For more information, see [About the egress proxy for the External Secrets Operator for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html-single/security_and_compliance/index#external-secrets-operator-proxy).

**Root filesystem is read-only for External Secrets Operator for Red Hat OpenShift containers**

With this release, to improve security, the External Secrets Operator for Red Hat OpenShift and all its operands have the `readOnlyRootFilesystem` security context set to true by default. This enhancement hardens the containers and prevents a potential attacker from modifying the contents of the container’s root file system.

**Network policy hardening is now available for External Secrets Operator components**

With this release, External Secrets Operator for Red Hat OpenShift includes pre-defined `NetworkPolicy` resources designed for enhanced security by governing ingress and egress traffic for operand components. These policies cover essential internal traffic, such as ingress to the metrics and webhook servers, and egress to the OpenShift API server and DNS server. Note that deployment of the `NetworkPolicy` is enabled by default and egress allow policies must be explicitly defined in the `ExternalSecretsConfig` custom resource for the `external-secrets` component to fetch secrets from external providers.

For more information, see [Configuring network policy for the operand](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html-single/security_and_compliance/index#external-secrets-operator-config-net-policy).

# Release notes for External Secrets Operator for Red Hat OpenShift 0.1.0 (Technology Preview)

Version `0.1.0` of the External Secrets Operator for Red Hat OpenShift is based on the upstream external-secrets version `0.14.3`.

Issued: 2025-06-26

The following advisories are available for the External Secrets Operator for Red Hat OpenShift 0.1.0:

- [RHBA-2025:9747](https://access.redhat.com/errata/RHBA-2025:9747)

- [RHBA-2025:9746](https://access.redhat.com/errata/RHBA-2025:9746)

- [RHBA-2025:9757](https://access.redhat.com/errata/RHBA-2025:9757)

- [RHBA-2025:9763](https://access.redhat.com/errata/RHBA-2025:9763)

## New features and enhancements

- This is the initial, Technology Preview release of the External Secrets Operator for Red Hat OpenShift.
