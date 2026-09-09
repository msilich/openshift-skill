<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) is an enterprise-ready, Kubernetes-native container security solution that protects your vital applications across the build, deploy, and runtime stages of the application lifecycle.

RHACS deploys into your infrastructure and integrates with your DevOps tools and workflows. This integration provides better security and compliance, enabling DevOps and InfoSec teams to operationalize security.

<a id="release-dates-411_release-notes-411"></a>

# Release dates

Review the official release dates and update schedule for RHACS 4.11.

| RHACS version | Released on    |
|---------------|----------------|
| `4.11.0`      | 15 June 2026   |
| `4.11.1`      | 7 July 2026    |
| `4.11.2`      | 30 July 2026   |
| `4.11.3`      | 25 August 2026 |

Release dates

<a id="about-this-release-411_release-notes-411"></a>

# About release 4.11

RHACS 4.11 includes new features, improvements, and updates.

<a id="new-features-411_release-notes-411"></a>

# New features

This release adds new features and enhanced functionality for existing features.

<a id="enhanced-vulnerability-management-reporting_release-notes-411"></a>

## Enhanced vulnerability management reporting

This update includes enhancements in vulnerability management reporting that offer more data, additional filtering options, and scheduling flexibility.

This release includes the following changes:

- Vulnerability reports now include a column showing the current version of each affected component. This eliminates the need to manually cross-reference external inventories when examining and assigning fixable CVEs.

- Administrators can now specify an exact time of hour and minute for scheduled vulnerability report generation, replacing the earlier randomized delivery window. This provides predictable, consistent report delivery aligned with audit, compliance, and operational schedules.

- Scheduled vulnerability reports now use the same filtering options available in the Vulnerability Management workflow views. Using these options, you can now create more granular scheduled reports. You can also begin a new report configuration directly from your active workflow filters, carrying over applied filter criteria without manual re-entry.

<a id="red-hat-hardened-image-scanning_release-notes-411"></a>

## Red Hat hardened image scanning

Red Hat Advanced Cluster Security Clair can scan Red Hat hardened images (Project Hummingbird) and cross-reference findings with Red Hat VEX metadata, supporting validation and ongoing monitoring of hardened image CVE posture.

<a id="known-issue-hummingbird-scan_release-notes-411"></a>

### Known issue as of July 15, 2026

Due to a recently identified data gap in the Red Hat VEX security data feed, RHACS version 4.11 no longer supports vulnerability reporting for Red Hat hardened images (Project Hummingbird). The Red Hat Product Security Team is working to address this data gap so that RHACS can re-introduce support for Red Hat hardened images.

<a id="policy-scope-cluster-namespace-labels_release-notes-411"></a>

## Policy scope support for cluster and namespace labels

This release expands policy scope selection capabilities, allowing you to include clusters by label.

<a id="policy-detection-enforcement-oc-debug-pods-attach_release-notes-411"></a>

## Policy-based detection and enforcement for oc debug and pods attach operations

RHACS policies now cover Kubernetes pod attach requests, including `oc debug` and `oc debug node`, in addition to the existing `pod exec` and `port forward` controls. The default `Kubernetes Actions: Attach to Pod` policy alerts on interactive attach sessions and can block them when you enable enforcement.

<a id="compliance-operator-tailored-profiles-scheduling_release-notes-411"></a>

## Support for Compliance Operator tailored profiles scheduling and maintenance

RHACS now supports seamless integration of existing tailored profiles from Compliance Operator. You can now schedule and manage your custom security configurations directly from the RHACS interface. This update fully accommodates profiles with suppressed rules or multi-profile combinations and profiles that are using the latest `CustomRules` functionality.

<a id="splunk-integration-improvements_release-notes-411"></a>

## Splunk integration improvements

This release updates the Splunk Technology Add On, adding support for File Activity violations and aligning with recent Splunk changes. The new version, 3.0.0, is available for download on SplunkBase.

<div>

<div class="title">

Additional resources

</div>

- [Splunkbase](https://splunkbase.splunk.com/app/5315)

</div>

<a id="performance-operations_release-notes-411"></a>

# Performance and operations

This release includes performance and operational improvements.

<a id="image-data-model-refactoring-technical-details_release-notes-411"></a>

## Image scan accuracy

Images are now uniquely identified by the combination of name and digest, rather than by digest alone. This new data model resolves several long-standing issues when multiple images share the same digest but have different names, for example, different registries or tags.

<a id="lightweight-runtime-data-collection_release-notes-411"></a>

## Lightweight runtime data collection

RHACS now uses a more efficient runtime data collection mechanism that reduces resource consumption while maintaining comprehensive security monitoring capabilities.

<a id="faster-admission-controller_release-notes-411"></a>

## Faster admission controller

This release improves admission controller performance by keeping the image cache warm longer and eliminating image fetches for policies that do not evaluate images. The default memory limit of admission controller pods is now 1 Gi, which has increased from 500 Mi.

<a id="api-list-performance-optimizations_release-notes-411"></a>

## API list performance optimizations

This release improves performance and resource consumption for API list endpoints that return `List<Type>` objects.

<a id="ubi9-minimal-migration_release-notes-411"></a>

## Migration to UBI 9 minimal base images

All RHACS Operator and operand images are now built on UBI 9 Minimal base images. This improves your security posture by shrinking the attack surface and eliminating CVE noise from unnecessary packages.

This migration provides a smaller attack surface, reduced image size, and alignment with the latest Red Hat Universal Base Image standards.

<a id="installation-method-consolidation-operator-based_release-notes-411"></a>

## Installation method consolidation to Operator-based deployment

This release consolidates installation methods to focus on Operator-based deployment as the primary installation approach.

This consolidation simplifies the installation experience and aligns with Kubernetes-native deployment patterns. The RHACS Operator provides a consistent, automated installation and upgrade experience across all supported platforms.

<a id="cluster-registration-secrets-improvements_release-notes-411"></a>

## Cluster registration secrets improvements

Cluster registration secrets (CRSes) were generally available in an earlier release and make the bootstrapping process more secure. In this release, you can configure the CRS maximum expiration time and the maximum number of clusters that can generate and use CRSes through the RHACS web console. This flexibility provides additional hardening and strengthening for CRSes. Credential management is key to the secure functioning of your fleet application and helps prevent exfiltration attacks.

<a id="technology-preview-features_release-notes-411"></a>

# Technology Preview features

This release includes Technology Preview features that offer early access to upcoming product innovations.

> [!IMPORTANT]
> Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features offer early access to upcoming product features, enabling customers to test functionality and give feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see "Technology Preview Features Support Scope".

<div>

<div class="title">

Additional resources

</div>

- [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/)

</div>

<a id="init-container-vulnerability-scanning-technology-preview_release-notes-411"></a>

## Init container vulnerability scanning

RHACS now scans images used by init containers and displays init container information, if it exists, in the deployment details.

This feature is available as a Technology Preview and is disabled by default. To enable init container scanning, set the `ROX_INIT_CONTAINER_SUPPORT` feature flag to `true`.

When enabled, RHACS extracts, scans, and displays init containers in the following RHACS locations:

- Violations Detail view

- Network Graph sidebar

- Risk Deployment details

- Vulnerability Management

Init containers are included in risk scores and compliance checks. However, policies do not evaluate init containers in this Technology Preview release.

> [!NOTE]
> Enabling this feature might increase scanner load, as deployments with init containers might require scanning additional images per deployment. Monitor scanner capacity after enabling this feature.

<a id="dynamic-path-support-for-file-activity-monitoring_release-notes-411"></a>

## Dynamic path support for file activity monitoring

File activity monitoring now supports user-defined path specifications with wildcard patterns, enhanced filtering options, and file rename operation detection.

With this feature, you can define custom paths to monitor using wildcard patterns, filter file activity based on criteria such as process name and ancestor, create policies for file rename operations, and combine process criteria with file access criteria in deployment and node policies.

<div>

<div class="title">

Additional resources

</div>

- [Configuring file activity monitoring](../operating/manage_security_policies/configuring-file-activity-monitoring.md)

</div>

<a id="policy-differentiation-cve-origin-base-application-layers-technology-preview_release-notes-411"></a>

## Policy differentiation for CVE origin from base images or application layers

You can use this Technology Preview feature to experiment with the planned user interface. To use this feature, you must set the feature flag ROX_POLICY_FILTERS_UI to `enabled`.

<a id="technology-preview-to-ga_release-notes-411"></a>

# Technology Preview features promoted to General Availability

The following features were available earlier as Technology Preview and are now Generally Available (GA) in this release.

GA features are fully supported and suitable for production use.

<a id="rhacs-vulnerability-management-openshift-console-plugin-ga_release-notes-411"></a>

## RHACS vulnerability management in OpenShift console plugin

The RHACS vulnerability management integration with the Red Hat OpenShift console plugin is now generally available.

This feature provides vulnerability information directly within the OpenShift Container Platform web console, enabling platform administrators and developers to view and manage security vulnerabilities without leaving their primary workflow interface.

The plugin is supported on OpenShift Container Platform versions 4.19 and later.

<div>

<div class="title">

Additional resources

</div>

- [Accessing vulnerability information in the OpenShift Container Platform web console](../configuration/accessing-vulnerability-information-in-web-console.md)

</div>

<a id="base-image-ga_release-notes-411"></a>

## Standardized base image definition and layer detection

Standardized base image definition and layer detection is now generally available.

<a id="notable-technical-changes-411_release-notes-411"></a>

# Notable technical changes

This release includes notable technical changes.

This release has the following changes:

Update to Patternfly 6  
The RHACS web portal has been upgraded to PatternFly 6. PatternFly 6 provides an improved user experience with enhanced accessibility, better performance, and a modernized visual design.

Security and other enhancements  
- For security purposes, the functionality to export reports to PDF is removed. PDF report generation functionality was replaced with alternative implementations.

- Istio support in RHACS was simplified and the `env.istio` configuration parameter no longer exists. Existing instances of this variable will be ignored and Istio support is always enabled.

<a id="deprecated-and-removed-features-411_release-notes-411"></a>

# Deprecated and removed features

Identify the deprecated and removed features in RHACS 4.11 to ensure your deployment remains secure and fully functional.

Some features available in earlier releases have been deprecated or removed.

Deprecated functionality is still included in RHACS and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments.

For the most recent list of major functionality deprecated and removed, see the following table. Information about additional removed or deprecated functionality is available after the table.

In the table, features are marked with the following statuses:

- GA: General Availability

- TP: Technology Preview

- DEP: Deprecated

- REM: Removed

- NA: Not applicable

<table>
<caption>Deprecated and removed features tracker</caption>
<colgroup>
<col style="width: 57%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Feature</th>
<th style="text-align: left;">RHACS 4.9</th>
<th style="text-align: left;">RHACS 4.10</th>
<th style="text-align: left;">RHACS 4.11</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Admission controller configuration parameters:</p>
<ul>
<li><p><code>admissionControl.contactImageScanners</code></p></li>
<li><p><code>admissionControl.dynamic.enforceOnCreates</code></p></li>
<li><p><code>admissionControl.dynamic.enforceOnUpdates</code></p></li>
<li><p>user configuration ability of <code>admissionControl.dynamic.scanInline</code></p></li>
<li><p>user configuration ability of <code>admissionControl.dynamic.timeout</code></p></li>
<li><p><code>admissionControl.listenOnCreates</code></p></li>
<li><p><code>admissionControl.listenOnEvents</code></p></li>
<li><p><code>admissionControl.listenOnUpdates</code></p></li>
<li><p><code>admissionControl.timeoutSeconds</code></p></li>
</ul></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>API token authentication for Red Hat OpenShift Cluster Manager</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Collections hierarchical implementation</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Compliance dashboard</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>REM</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>definitions.stackrox.io</code></p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Google Container Registry integration</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>GraphQL endpoints</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Kernel support packages and driver download functionality</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Reporting of Istio vulnerabilities</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>roxctl</code> admission controller parameters:</p>
<ul>
<li><p><code>--admission-controller-enforce-on-creates</code></p></li>
<li><p><code>--admission-controller-enforce-on-updates</code></p></li>
<li><p><code>--admission-controller-listen-on-creates</code></p></li>
<li><p><code>--admission-controller-listen-on-updates</code></p></li>
<li><p><code>--admission-controller-listen-on-events</code></p></li>
<li><p><code>--admission-controller-timeout</code></p></li>
</ul></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Scanner V2</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>/v1/clustercves/suppress</code> APIs</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>/v1/clustercves/unsuppress</code> APIs</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>/v1/nodecves/suppress</code> APIs</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>/v1/nodecves/unsuppress</code> APIs</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Vulnerability Management (1.0) menu item</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Vulnerability Report Creator permission</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Init Bundle</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>/v1/cluster-init/init-bundles/revoke</code> API</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>/v1/cluster-init/init-bundles</code> API</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Configuration Management Dashboard and sub-menus</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>OpenShift auth identity provider</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Compliance V1</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Graph view in the Process discovery tab</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Vulnerability reports using attached collections</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Vulnerability Management Dashboard (1.0) and sub-menus</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Install-time Istio integration</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Kubernetes components view</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Manifest install method and the related <code>/v1/clusters</code> API</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Direct Helm chart installations (central-services and secured-cluster-services charts)</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Plain text (non-TLS) endpoints configured by using the <code>ROX-PLAINTEXT_ENDPOINTS</code> environment variable</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>GA</p></td>
<td style="text-align: left;"><p>DEP</p></td>
</tr>
</tbody>
</table>

Deprecated features  
Manifest install method and related API  
The manifest install method and the related `/v1/clusters` API, which deployed and managed clusters, is deprecated and is anticipated to be removed in a future release.

Direct Helm chart installations  
The direct Helm chart installations using the `central-services` and `secured-cluster-services` charts are deprecated and are anticipated to be removed in a future release. You can install RHACS by using the new Operator-based Helm chart, which deploys the RHACS Operator to manage your installation instead.

Init Bundle  
The Init Bundle feature, which registers secured clusters with RHACS Central, is deprecated and is anticipated to be removed in a future release. The associated APIs `/v1/cluster-init/init-bundles/revoke` and `/v1/cluster-init/init-bundles` are also deprecated. You can register new clusters by using the cluster registration secret (CRS) instead.

Configuration Management Dashboard and sub-menus  
The Configuration Management Dashboard and all of its sub-menus, which provided security configuration data, are deprecated and are anticipated to be removed in a future release. API access for Secrets or role-based access control (RBAC) information remains available. Security configuration data integrates directly into risk and policy management workflows to enhance visibility without relying on a standalone dashboard.

OpenShift auth identity provider  
The OpenShift auth identity provider, which served as an identity provider (IdP) for RHACS, is deprecated and is anticipated to be removed in a future release. You can authenticate users by using OpenID Connect (OIDC) IdP integrations instead.

Compliance V1  
The Compliance V1 functionality, including the Compliance Dashboard, compliance APIs, and compliance configuration management board, which provided the earlier compliance implementation, was deprecated in release 4.10. The Compliance Dashboard was removed in release 4.11.

NIST SP 800-190 and HIPAA benchmarks are currently not supported by the Compliance Operator and were only visible in the Compliance Dashboard, which has been removed.

Additionally, Compliance support for non-OpenShift Kubernetes distributions is deprecated and is anticipated to be removed in a future release. If you rely on this functionality, you should prepare for a loss of functionality. For clusters running OpenShift, you can access improved compliance features by using the new compliance version instead.

Graph view in the Process discovery tab  
The **Graph** view, within the **Risk** section of the **Event Timeline** in the **Process discovery** tab, is deprecated and is anticipated to be removed in a future release.

Scanner V2  
Starting with RHACS 4.6, Scanner V2, also known as StackRox Scanner is deprecated and is anticipated to be removed in a future release. To maintain supported vulnerability scanning capabilities and access the latest security features, you should migrate to Scanner V4.

Vulnerability reports by using attached collections  
The vulnerability reports by using attached collections, which provided report scoping through hierarchical relationships, are deprecated and are anticipated to be removed in a future release. You can prepare for future updates to the scoping mechanism by avoiding attached collections.

Vulnerability Management Dashboard (1.0) and sub-menus  
Starting with RHACS 4.3, the Vulnerability Management Dashboard (1.0) and all of its sub-menus, which provided traditional vulnerability management views, are deprecated and is anticipated to be removed in a future release. You can access vulnerability information by using the current Vulnerability Management Dashboard instead.

Install-time Istio integration  
The creation of `networking.istio.io/v1alpha3/DestinationRule` resources by RHACS installation, which automatically generated networking configurations during setup, is deprecated and is anticipated to be removed in a future release. You can manage Istio configurations by creating `DestinationRule` resources out-of-band instead.

Kubernetes components view  
The **Kubernetes components** view available in the RHACS portal at **Vulnerability Management** → **Results** → **More Views** is deprecated and is anticipated to be removed in a future release.

Plain text (non-TLS) endpoints configured by using the `ROX-PLAINTEXT_ENDPOINTS` environment variable  
These are deprecated and will be removed in a future release. Modern load balancers and ingress controllers support TLS passthrough, making plain text endpoints unnecessary.

<a id="known-issues-411_release-notes-411"></a>

# Known issues in version 4.11

The following known issues exist in RHACS 4.11. Review these items before deploying or upgrading to this version.

- Due to a recently identified data gap in the Red Hat VEX security data feed, RHACS version 4.11 no longer supports vulnerability reporting for Red Hat hardened images (Project Hummingbird). See "Red Hat hardened image scanning" for more information.

<a id="bug-fixes-in-version-411_release-notes-411"></a>

# Bug fixes in version 4.11

This release contains bug fixes and enhancements.

- In RHACS release 4.8 through release 4.10, the timestamp for the "Days since CVE was first discovered in system" policy criteria and the "CVE Created Time" search term were not properly maintained and could be reset to a newer timestamp. This release has a fix for this issue and the timestamp will no longer be reset.

<!-- -->

- Starting with RHACS 4.11, the command `roxctl deployment check -f <deployment.yaml> --cluster <cluster name or id>` will evaluate the deployment against the policies as if the deployment is running on the cluster as specified.

<!-- -->

- Fixed an issue where the **Integrations** page tile layout spacing was excessively large when using the Mozilla Firefox browser. The display now uses a more uniform grid layout.

<a id="about-this-release-4111_release-notes-411"></a>

# About release 4.11.1

<a id="bug-fixes-in-version-4111_release-notes-411"></a>

## Bug fixes and security updates in version 4.11.1

This release includes the following bug fixes:

- Before this update, Scanner V4 could report the same vulnerability multiple times for a single component due to multiple entries in the OSV data source. With this release, Scanner V4 implements deduplication logic to ensure that it reports each CVE only once per component, reducing false positives and improving vulnerability report accuracy.

- Before this update, Scanner V4 did not use Red Hat VEX data to filter out packages marked as "not affected" by specific vulnerabilities. With this release, Scanner V4 supports Red Hat CSAF/VEX "not vulnerable" assertions, reducing false positives by not reporting vulnerabilities for packages that are not affected.

- Before this update, loading Compliance Operator profiles on large-scale deployments could cause Central startup to crash due to query timeouts. This release fixes this issue.

- Fixed an issue where under certain circumstances, clusters might not appear in the **OpenShift Coverage** section under the **Compliance** tab. Red Hat has improved compliance scan watcher behavior to prevent this issue.

- Before this update, the RHACS Helm chart versions in the mirror and GitHub repositories showed wrong version strings. This release corrects the Helm charts to display the proper version string.

- Before this update, the Artifactory "test" function always returned `true`, even when authentication failed. The test endpoint did not require authentication, causing confusion about integration status. With this release, the test function now performs an authenticated operation to properly validate credentials before reporting success.

- Images built with erroneous quotes in metadata can now be properly scanned by Scanner V4.

RHACS includes fixes for the following security vulnerabilities:

- Go and golang.org:

  - golang.org/x/crypto/ssh: Unauthorized command execution via discarded SSH permissions ([CVE-2026-39828](https://access.redhat.com/security/cve/CVE-2026-39828))

  - golang.org/x/crypto/ssh: Denial of service via crafted public key with excessive parameters ([CVE-2026-39829](https://access.redhat.com/security/cve/CVE-2026-39829))

  - golang.org/x/crypto/ssh: Denial of service via resource leak from unsolicited SSH responses ([CVE-2026-39830](https://access.redhat.com/security/cve/CVE-2026-39830))

  - golang.org/x/crypto/ssh: Denial of service via crafted SSH certificate ([CVE-2026-39835](https://access.redhat.com/security/cve/CVE-2026-39835))

  - golang.org/x/crypto/ssh: Authorization bypass due to skipped source-address validation ([CVE-2026-46595](https://access.redhat.com/security/cve/CVE-2026-46595))

  - golang.org/x/net/idna: Privilege escalation via incorrect Punycode label processing ([CVE-2026-39821](https://access.redhat.com/security/cve/CVE-2026-39821))

  - golang.org/x/net/html: Arbitrary HTML parsing and rendering can permit cross-site scripting attacks ([CVE-2026-25681](https://access.redhat.com/security/cve/CVE-2026-25681)) and ([CVE-2026-27136](https://access.redhat.com/security/cve/CVE-2026-27136))

  - Go net package: Denial of service via long CNAME response in LookupCNAME ([CVE-2026-33811](https://access.redhat.com/security/cve/CVE-2026-33811))

- Flaw in RHACS potentially could allow excessive resource consumption leading to denial of service ([CVE-2026-9165](https://access.redhat.com/security/cve/CVE-2026-9165))

- Prototype pollution flaw in Axios ([CVE-2026-42264](https://access.redhat.com/security/cve/CVE-2026-42264))

- github.com/containerd: Command execution vulnerability ([CVE-2026-53488](https://access.redhat.com/security/cve/CVE-2026-53488))

<a id="about-this-release-4112_release-notes-411"></a>

# About release 4.11.2

<a id="bug-fixes-in-version-4112_release-notes-411"></a>

## Bug fixes and security updates in version 4.11.2

RHACS includes fixes for the following security vulnerabilities:

- Go and golang.org:

  - Golang MIME: Denial of Service via maliciously-crafted MIME header ([CVE-2026-42504](https://access.redhat.com/security/cve/CVE-2026-42504))

  - Go os.Root: Symlink following vulnerability allows directory traversal ([CVE-2026-39822](https://access.redhat.com/security/cve/CVE-2026-39822))

- Brace-expansion: Denial of service due to exponential-time complexity ([CVE-2026-13149](https://access.redhat.com/security/cve/CVE-2026-13149))

- js-yaml: Denial of service via crafted YAML documents ([CVE-2026-59869](https://access.redhat.com/security/cve/CVE-2026-59869))

- DOMPurify: Cross-site scripting vulnerability allows code execution ([CVE-2026-49978](https://access.redhat.com/security/cve/CVE-2026-49978))

<a id="about-this-release-4113_release-notes-411"></a>

# About release 4.11.3

<a id="bug-fixes-in-version-4113_release-notes-411"></a>

## Bug fixes and security updates in version 4.11.3

This release includes the following bug fixes:

- Before this update, compliance scans that used CEL-scanner profiles, such as the Red Hat OpenShift Virtualization (RHOCPV) profiles, ran successfully but showed no results in the RHACS **Coverage** page. The scan results existed in the database but were not displayed because RHACS could not connect the results to the profile. With this release, CEL-scanner profile results now appear correctly in the **Coverage** view.

<!-- -->

- Before this update, the `NODE_EVENT` event source was missing from the security policy Custom Resource Definition (CRD), preventing you from configuring node-level security policies by using Kubernetes custom resources (CRs). With this release, `NODE_EVENT` is now available as an event source in the policy CRD, and you can configure node-level security policies by using CRs.

<!-- -->

- Before this update, pending view-based reports failed to reschedule automatically when Central restarted. With this release, pending reports now reschedule correctly after a Central restart.

RHACS includes the fix for the following security vulnerability:

- brace-expansion: Denial of service via unbounded intermediate arrays ([CVE-2026-69152](https://access.redhat.com/security/cve/CVE-2026-69152))

<a id="image-versions_release-notes-411"></a>

# Image versions

You can manually pull, retag, and push Red Hat Advanced Cluster Security for Kubernetes (RHACS) images to your registry. The current version includes the following images:

<table>
<caption>Red Hat Advanced Cluster Security for Kubernetes images</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Image</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Current version</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Main</p></td>
<td style="text-align: left;"><p>Includes Central, Sensor, Admission controller, and Compliance components. Also includes <code>roxctl</code> for use in continuous integration (CI) systems.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:4.11.3</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Central DB</p></td>
<td style="text-align: left;"><p>PostgreSQL instance that provides the database storage for Central.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-central-db-rhel9:4.11.3</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Scanner</p></td>
<td style="text-align: left;"><p>Scans images and nodes.</p></td>
<td style="text-align: left;"><ul>
<li><p><code>registry.redhat.io/advanced-cluster-security/rhacs-scanner-rhel9:4.11.3</code></p></li>
<li><p><code>registry.redhat.io/advanced-cluster-security/rhacs-scanner-slim-rhel9:4.11.3</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Scanner DB</p></td>
<td style="text-align: left;"><p>Stores image scan results and vulnerability definitions.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-scanner-db-rhel9:4.11.3</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Scanner V4</p></td>
<td style="text-align: left;"><p>Scans images.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-scanner-v4-rhel9:4.11.3</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Scanner V4 DB</p></td>
<td style="text-align: left;"><p>Stores image scan results and vulnerability definitions for Scanner V4.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-scanner-v4-db-rhel9:4.11.3</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Collector</p></td>
<td style="text-align: left;"><p>Collects runtime activity in Kubernetes or OpenShift Container Platform clusters.</p></td>
<td style="text-align: left;"><p><code>registry.redhat.io/advanced-cluster-security/rhacs-collector-rhel9:4.11.3</code></p></td>
</tr>
</tbody>
</table>
