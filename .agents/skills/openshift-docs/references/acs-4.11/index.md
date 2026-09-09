<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Red Hat Advanced Cluster Security for Kubernetes Documentation

> Auto-generated Markdown conversion of [openshift/openshift-docs](https://github.com/openshift/openshift-docs).
> Designed for offline AI-agent retrieval. Pinned to the source revision recorded in SOURCE.json.

## Table of Contents

### About

- [Welcome](welcome/index.md)

### Release notes

- [Red Hat Advanced Cluster Security for Kubernetes 4.11](release_notes/411-release-notes.md)

### RHACS Cloud Service

- [Service description](cloud_service/rhacs-cloud-service-service-description.md)
- [Overview of responsibilities for RHACS Cloud Service](cloud_service/acs-cloud-responsibility-matrix.md)
- [RHACS Cloud Service architecture](cloud_service/acscs-architecture.md)
- [Getting started with RHACS Cloud Service](cloud_service/getting-started-rhacs-cloud-ocp.md)
- [Default resource requirements for RHACS Cloud Service](cloud_service/acscs-default-requirements.md)
- [Recommended resource requirements for RHACS Cloud Service](cloud_service/acscs-recommended-requirements.md)
- **Setting up RHACS Cloud Service with Red Hat OpenShift secured clusters**
  - [Creating a RHACS Cloud Service instance on Red Hat Cloud](cloud_service/installing_cloud_ocp/cloud-create-instance-ocp.md)
  - [Creating a project on your Red Hat OpenShift secured cluster](cloud_service/installing_cloud_ocp/cloud-ocp-create-project.md)
  - [Generating a cluster registration secret or init bundle for secured clusters](cloud_service/installing_cloud_ocp/init-bundle-cloud-ocp-generate.md)
  - [Applying a cluster registration secret or init bundle for secured clusters](cloud_service/installing_cloud_ocp/init-bundle-cloud-ocp-apply.md)
  - [Installing the RHACS Operator for RHACS Cloud Service](cloud_service/installing_cloud_ocp/cloud-install-operator.md)
  - [Installing secured cluster services from RHACS Cloud Service](cloud_service/installing_cloud_ocp/install-secured-cluster-cloud-ocp.md)
  - [Configuring the proxy for secured cluster services in RHACS Cloud Service](cloud_service/installing_cloud_ocp/configuring-the-proxy-for-secured-cluster-services-in-rhacs-cloud-service.md)
  - [Verifying installation of secured clusters](cloud_service/installing_cloud_ocp/verify-installation-cloud-ocp.md)
- **Setting up RHACS Cloud Service with Kubernetes secured clusters**
  - [Creating a RHACS Cloud Service instance for Kubernetes clusters](cloud_service/installing_cloud_other/cloud-create-instance-other.md)
  - [Generating a cluster registration secret or init bundle for Kubernetes secured clusters](cloud_service/installing_cloud_other/init-bundle-cloud-other-generate.md)
  - [Applying a cluster registration secret or init bundle for Kubernetes secured clusters](cloud_service/installing_cloud_other/init-bundle-cloud-other-apply.md)
  - [Installing secured cluster services from RHACS Cloud Service on Kubernetes clusters](cloud_service/installing_cloud_other/install-secured-cluster-cloud-other.md)
  - [Verifying installation of secured clusters](cloud_service/installing_cloud_other/verify-installation-cloud-other.md)
- **Upgrading RHACS Cloud Service**
  - [Upgrading secured clusters in RHACS Cloud Service by using the Operator](cloud_service/upgrading-cloud/upgrade-cloudsvc-operator.md)
  - [Upgrading secured clusters in RHACS Cloud Service by using Helm charts](cloud_service/upgrading-cloud/upgrade-cloudsvc-helm.md)
  - [Upgrading secured clusters in RHACS Cloud Service by using the roxctl CLI](cloud_service/upgrading-cloud/upgrade-cloudsvc-roxctl.md)

### Architecture

- [RHACS architecture](architecture/acs-architecture.md)

### Installing

- [High-level RHACS installation overview](installing/acs-high-level-overview.md)
- [Default resource requirements for RHACS](installing/acs-default-requirements.md)
- [Recommended resource requirements for RHACS](installing/acs-recommended-requirements.md)
- **Installing RHACS on Red Hat OpenShift**
  - [Installing Central services for RHACS on Red Hat OpenShift](installing/installing_ocp/install-central-ocp.md)
  - [Configuring Central configuration options for RHACS using the Operator](installing/installing_ocp/install-central-config-options-ocp.md)
  - [Generating and applying a cluster registration secret or init bundle for RHACS on Red Hat OpenShift](installing/installing_ocp/init-bundle-ocp.md)
  - [Installing Secured Cluster services for RHACS on Red Hat OpenShift](installing/installing_ocp/install-secured-cluster-ocp.md)
  - [Configuring Secured Cluster services options for RHACS using the Operator](installing/installing_ocp/install-secured-cluster-config-options-ocp.md)
  - [Verifying installation of RHACS on Red Hat OpenShift](installing/installing_ocp/verify-installation-rhacs-ocp.md)
- **Installing RHACS on other platforms**
  - [High-level overview of installing RHACS on other platforms](installing/installing_other/install-rhacs-other.md)
  - [Installing Central services for RHACS on other platforms](installing/installing_other/install-central-other.md)
  - [Generating and applying a cluster registration secret or init bundle for RHACS on other platforms](installing/installing_other/init-bundle-other.md)
  - [Installing Secured Cluster services for RHACS on other platforms](installing/installing_other/install-secured-cluster-other.md)
  - [Verifying installation of RHACS on other platforms](installing/installing_other/verify-installation-rhacs-other.md)
- [Uninstalling Red Hat Advanced Cluster Security for Kubernetes](installing/uninstall-acs.md)

### Configuring

- [Adding custom certificates](configuration/add-custom-certificates.md)
- [Adding trusted certificate authorities](configuration/add-trusted-ca.md)
- [Internal certificate authority rotation for RHACS](configuration/internal-certificate-authority-rotation-for-rhacs.md)
- [Reissuing internal certificates](configuration/reissue-internal-certificates.md)
- [Adding security notices](configuration/add-security-notices.md)
- [Customizing platform components](configuration/customizing-platform-components.md)
- [Enabling offline mode](configuration/enable-offline-mode.md)
- [Enabling alert data retention](configuration/enable-alert-data-retention.md)
- [Exposing the RHACS portal over HTTP](configuration/expose-portal-over-http.md)
- [Configuring automatic upgrades for manifest-installed secured clusters](configuration/configure-automatic-upgrades.md)
- [Configuring automatic removal of nonactive clusters](configuration/configure-inactive-cluster-deletion.md)
- [Configuring a proxy for external network access](configuration/configure-proxy.md)
- [Generating a diagnostic bundle](configuration/generate-diagnostic-bundle.md)
- [Configuring endpoints](configuration/configure-endpoints.md)
- [Monitoring](configuration/monitor-acs.md)
- [Enabling audit logging](configuration/configure-audit-logging.md)
- [Configuring API tokens](configuration/configure-api-token.md)
- [Using RHACS with GitOps](configuration/using-rhacs-with-gitops.md)
- [Using declarative configuration](configuration/declarative-configuration-using.md)
- [Inviting users to your RHACS instance](configuration/inviting-users-to-your-rhacs-instance.md)
- [Managing preview features](configuration/managing-preview-features.md)
- [Configuring and integrating the RHACS plugin with Red Hat Developer Hub](configuration/configuring-and-integrating-the-rhacs-plugin-with-red-hat-developer-hub.md)
- [Accessing vulnerability information in the OpenShift Container Platform web console](configuration/accessing-vulnerability-information-in-web-console.md)

### Operating

- [Viewing the dashboard](operating/view-dashboard.md)
- [Using Compliance Operator with RHACS](operating/compliance-operator-rhacs.md)
- **Managing compliance**
  - [Compliance feature overview](operating/manage-compliance/compliance-feature-overview.md)
  - [Using OpenShift compliance](operating/manage-compliance/using-openshift-compliance.md)
- [Evaluating security risks](operating/evaluate-security-risks.md)
- **Using policies to provide security**
  - [About policies in RHACS](operating/manage_security_policies/about-security-policies.md)
  - [Using admission controller enforcement](operating/manage_security_policies/use-admission-controller-enforcement.md)
  - [Configuring file activity monitoring](operating/manage_security_policies/configuring-file-activity-monitoring.md)
  - [Creating and modifying security policies](operating/manage_security_policies/custom-security-policies.md)
  - [Managing policies as code](operating/manage_security_policies/managing-policies-as-code.md)
  - [Security policy reference](operating/manage_security_policies/security-policy-reference.md)
- [Managing network policies](operating/manage-network-policies.md)
- [Build-time network policy tools](operating/build-time-network-policy-tools.md)
- [Visualizing external entities](operating/visualizing-external-entities.md)
- [Using Collector runtime configuration](operating/using-collector-runtime-configuration.md)
- [Auditing listening endpoints](operating/audit-listening-endpoints.md)
- [Reviewing cluster configuration](operating/review-cluster-configuration.md)
- [Examining images for vulnerabilities](operating/examine-images-for-vulnerabilities.md)
- [Verifying image signatures](operating/verify-image-signatures.md)
- **Managing vulnerabilities**
  - [Vulnerability management overview](operating/manage-vulnerabilities/vulnerability-management.md)
  - [Viewing and addressing vulnerabilities](operating/manage-vulnerabilities/common-vuln-management-tasks.md)
  - [Vulnerability reporting](operating/manage-vulnerabilities/vulnerability-reporting.md)
  - [Using the vulnerability management dashboard (deprecated)](operating/manage-vulnerabilities/vulnerability-management-dashboard.md)
  - [Scanning RHCOS node hosts](operating/manage-vulnerabilities/scan-rhcos-node-host.md)
  - [Generating SBOMs from scanned images](operating/manage-vulnerabilities/scanner-generate-sbom.md)
- [Responding to violations](operating/respond-to-violations.md)
- [Using deployment collections](operating/create-use-collections.md)
- [Searching and filtering](operating/search-filter.md)
- **Managing user access**
  - [Managing RBAC in Red Hat Advanced Cluster Security for Kubernetes](operating/manage-user-access/manage-role-based-access-control-3630.md)
  - [Enabling PKI authentication](operating/manage-user-access/enable-pki-authentication.md)
  - [Understanding authentication providers](operating/manage-user-access/understanding-authentication-providers.md)
  - **Configuring identity providers**
    - [Configuring Okta Identity Cloud as a SAML 2.0 identity provider](operating/manage-user-access/configuring-identity-providers/configure-okta-identity-cloud.md)
    - [Configuring Google Workspace as an OIDC identity provider](operating/manage-user-access/configuring-identity-providers/configure-google-workspace-identity.md)
    - [Configuring OpenShift Container Platform OAuth server as an identity provider](operating/manage-user-access/configuring-identity-providers/configure-ocp-oauth.md)
    - [Connecting Azure AD to RHACS using SSO configuration](operating/manage-user-access/configuring-identity-providers/connecting-azure-ad-to-rhacs-using-sso-configuration.md)
  - [Removing the admin user](operating/manage-user-access/remove-admin-user.md)
  - [Configuring short-lived access](operating/manage-user-access/configure-short-lived-access.md)
  - [Understanding multi-tenancy](operating/manage-user-access/understanding-multi-tenancy.md)
- [Using the system health dashboard](operating/use-system-health-dashboard.md)
- [Using the administration events page](operating/using-the-administration-events-page.md)

### Integrating

- [Integrating with image registries](integration/integrate-with-image-registries.md)
- [Integrating with CI systems](integration/integrate-with-ci-systems.md)
- [Integrating with PagerDuty](integration/integrate-with-pagerduty.md)
- [Integrating with Slack](integration/integrate-with-slack.md)
- [Integrating by using generic webhooks](integration/integrate-using-generic-webhooks.md)
- [Integrating with QRadar](integration/integrate-with-qradar.md)
- [Integrating with ServiceNow](integration/integrate-with-servicenow.md)
- [Integrating with Sumo Logic](integration/integrate-with-sumologic.md)
- [Integrating with Google Cloud Storage](integration/integrate-with-google-cloud-storage.md)
- [Integrating by using the syslog protocol](integration/integrate-using-syslog-protocol.md)
- [Integrating with Amazon S3](integration/integrate-with-amazon-s3.md)
- [Integrating with S3 API compatible services](integration/integrate-with-s3-api-compatible-services.md)
- [Integrating with Google Cloud Security Command Center](integration/integrate-with-google-cloud-scc.md)
- [Integrating with Splunk](integration/integrate-with-splunk.md)
- [Integrating with image vulnerability scanners](integration/integrate-with-image-vulnerability-scanners.md)
- [Integrating with Jira](integration/integrate-with-jira.md)
- [Integrating with email](integration/integrate-with-email.md)
- [Integrating with cloud management platforms](integration/integrate-with-cloud-management-platforms.md)
- [Integrating using short-lived tokens](integration/integrate-using-short-lived-tokens.md)
- [Integrating with Microsoft Sentinel notifier](integration/integrating-with-microsoft-sentinel-notifier.md)

### Backup and restore

- [Backing up Red Hat Advanced Cluster Security for Kubernetes](backup_and_restore/backing-up-acs.md)
- [Restoring from a backup](backup_and_restore/restore-acs.md)

### Upgrading

- [Upgrading using the Operator](upgrading/upgrade-operator.md)
- [Upgrading using Helm charts](upgrading/upgrade-helm.md)
- [Upgrading using the roxctl CLI](upgrading/upgrade-roxctl.md)

### roxctl CLI

- [Installing the roxctl CLI](cli/installing-the-roxctl-cli.md)
- [Using the roxctl CLI](cli/using-the-roxctl-cli.md)
- [Managing secured clusters](cli/managing-secured-clusters.md)
- [Checking policy compliance](cli/checking-policy-compliance.md)
- [Debugging issues](cli/debugging-issues.md)
- [Image scanning by using the roxctl CLI](cli/image-scanning-by-using-the-roxctl-cli.md)
- **roxctl CLI command reference**
  - [roxctl](cli/command-reference/roxctl.md)
  - [roxctl central](cli/command-reference/roxctl-central.md)
  - [roxctl cluster](cli/command-reference/roxctl-cluster.md)
  - [roxctl collector](cli/command-reference/roxctl-collector.md)
  - [roxctl completion](cli/command-reference/roxctl-completion.md)
  - [roxctl declarative-config](cli/command-reference/roxctl-declarative-config.md)
  - [roxctl deployment](cli/command-reference/roxctl-deployment.md)
  - [roxctl helm](cli/command-reference/roxctl-helm.md)
  - [roxctl image](cli/command-reference/roxctl-image.md)
  - [roxctl netpol](cli/command-reference/roxctl-netpol.md)
  - [roxctl scanner](cli/command-reference/roxctl-scanner.md)
  - [roxctl sensor](cli/command-reference/roxctl-sensor.md)
  - [roxctl version](cli/command-reference/roxctl-version.md)

### Troubleshooting Collector

- [Retrieving and analyzing the Collector logs and pod status](troubleshooting/retrieving-and-analyzing-the-collector-logs-and-pod-status.md)
- [Commonly occurring error conditions](troubleshooting/commonly-occurring-error-conditions.md)

### Troubleshooting Central

- [Backing up Central database by using the roxctl CLI](troubleshooting_central/backing-up-central-database-by-using-the-roxctl-cli.md)
- [Restoring Central database by using the roxctl CLI](troubleshooting_central/restoring-central-database-by-using-the-roxctl-cli.md)

### Telemetry

- [About Telemetry](telemetry/about-telemetry.md)
- [Opting out of Telemetry](telemetry/opting-out-of-telemetry.md)

### Support

- [Getting support for Red Hat Advanced Cluster Security for Kubernetes](support/getting-support.md)

### API reference

- **Administration Event Service**
  - [Administration Event Service](rest_api/AdministrationEventService/AdministrationEventService.md)
- **Administration Usage Service**
  - [Administration Usage Service](rest_api/AdministrationUsageService/AdministrationUsageService.md)
- **Alert Service**
  - [Alert Service](rest_api/AlertService/AlertService.md)
- **APIToken Service**
  - [A P I Token Service](rest_api/APITokenService/APITokenService.md)
- **Auth Provider Service**
  - [Auth Provider Service](rest_api/AuthProviderService/AuthProviderService.md)
- **Auth Service**
  - [Auth Service](rest_api/AuthService/AuthService.md)
- **Base Image Service V2**
  - [Base Image Service V2](rest_api/BaseImageServiceV2/BaseImageServiceV2.md)
- **Central Health Service**
  - [Central Health Service](rest_api/CentralHealthService/CentralHealthService.md)
- **Cloud Sources Service**
  - [Cloud Sources Service](rest_api/CloudSourcesService/CloudSourcesService.md)
- **Cluster CVEService**
  - [Cluster C V E Service](rest_api/ClusterCVEService/ClusterCVEService.md)
- **Cluster Init Service**
  - [Cluster Init Service](rest_api/ClusterInitService/ClusterInitService.md)
- **Clusters Service**
  - [Clusters Service](rest_api/ClustersService/ClustersService.md)
- **Collection Service**
  - [Collection Service](rest_api/CollectionService/CollectionService.md)
- **Compliance Integration Service**
  - [Compliance Integration Service](rest_api/ComplianceIntegrationService/ComplianceIntegrationService.md)
- **Compliance Management Service**
  - [Compliance Management Service](rest_api/ComplianceManagementService/ComplianceManagementService.md)
- **Compliance Profile Service**
  - [Compliance Profile Service](rest_api/ComplianceProfileService/ComplianceProfileService.md)
- **Compliance Results Service**
  - [Compliance Results Service](rest_api/ComplianceResultsService/ComplianceResultsService.md)
- **Compliance Results Stats Service**
  - [Compliance Results Stats Service](rest_api/ComplianceResultsStatsService/ComplianceResultsStatsService.md)
- **Compliance Rule Service**
  - [Compliance Rule Service](rest_api/ComplianceRuleService/ComplianceRuleService.md)
- **Compliance Scan Configuration Service**
  - [Compliance Scan Configuration Service](rest_api/ComplianceScanConfigurationService/ComplianceScanConfigurationService.md)
- **Compliance Service**
  - [Compliance Service](rest_api/ComplianceService/ComplianceService.md)
- **Config Service**
  - [Config Service](rest_api/ConfigService/ConfigService.md)
- **Credential Expiry Service**
  - [Credential Expiry Service](rest_api/CredentialExpiryService/CredentialExpiryService.md)
- **DBService**
  - [D B Service](rest_api/DBService/DBService.md)
- **Debug Service**
  - [Debug Service](rest_api/DebugService/DebugService.md)
- **Declarative Config Health Service**
  - [Declarative Config Health Service](rest_api/DeclarativeConfigHealthService/DeclarativeConfigHealthService.md)
- **Delegated Registry Config Service**
  - [Delegated Registry Config Service](rest_api/DelegatedRegistryConfigService/DelegatedRegistryConfigService.md)
- **Deployment Service**
  - [Deployment Service](rest_api/DeploymentService/DeploymentService.md)
- **Detection Service**
  - [Detection Service](rest_api/DetectionService/DetectionService.md)
- **Discovered Clusters Service**
  - [Discovered Clusters Service](rest_api/DiscoveredClustersService/DiscoveredClustersService.md)
- **External Backup Service**
  - [External Backup Service](rest_api/ExternalBackupService/ExternalBackupService.md)
- **Feature Flag Service**
  - [Feature Flag Service](rest_api/FeatureFlagService/FeatureFlagService.md)
- **Group Service**
  - [Group Service](rest_api/GroupService/GroupService.md)
- **GRPCPreferences Service**
  - [G R P C Preferences Service](rest_api/GRPCPreferencesService/GRPCPreferencesService.md)
- **Image Integration Service**
  - [Image Integration Service](rest_api/ImageIntegrationService/ImageIntegrationService.md)
- **Image Service**
  - [Image Service](rest_api/ImageService/ImageService.md)
- **Integration Health Service**
  - [Integration Health Service](rest_api/IntegrationHealthService/IntegrationHealthService.md)
- **Listening Endpoints Service**
  - [Listening Endpoints Service](rest_api/ListeningEndpointsService/ListeningEndpointsService.md)
- **Metadata Service**
  - [Metadata Service](rest_api/MetadataService/MetadataService.md)
- **Mitre Attack Service**
  - [Mitre Attack Service](rest_api/MitreAttackService/MitreAttackService.md)
- **Namespace Service**
  - [Namespace Service](rest_api/NamespaceService/NamespaceService.md)
- **Network Baseline Service**
  - [Network Baseline Service](rest_api/NetworkBaselineService/NetworkBaselineService.md)
- **Network Graph Service**
  - [Network Graph Service](rest_api/NetworkGraphService/NetworkGraphService.md)
- **Network Policy Service**
  - [Network Policy Service](rest_api/NetworkPolicyService/NetworkPolicyService.md)
- **Node CVEService**
  - [Node C V E Service](rest_api/NodeCVEService/NodeCVEService.md)
- **Node Service**
  - [Node Service](rest_api/NodeService/NodeService.md)
- **Notifier Service**
  - [Notifier Service](rest_api/NotifierService/NotifierService.md)
- **Ping Service**
  - [Ping Service](rest_api/PingService/PingService.md)
- **Pod Service**
  - [Pod Service](rest_api/PodService/PodService.md)
- **Policy Category Service**
  - [Policy Category Service](rest_api/PolicyCategoryService/PolicyCategoryService.md)
- **Policy Service**
  - [Policy Service](rest_api/PolicyService/PolicyService.md)
- **Probe Upload Service**
  - [Probe Upload Service](rest_api/ProbeUploadService/ProbeUploadService.md)
- **Process Baseline Service**
  - [Process Baseline Service](rest_api/ProcessBaselineService/ProcessBaselineService.md)
- **Process Service**
  - [Process Service](rest_api/ProcessService/ProcessService.md)
- **Rbac Service**
  - [Rbac Service](rest_api/RbacService/RbacService.md)
- **Report Configuration Service**
  - [Report Configuration Service](rest_api/ReportConfigurationService/ReportConfigurationService.md)
- **Report Service**
  - [Report Service](rest_api/ReportService/ReportService.md)
- **Role Service**
  - [Role Service](rest_api/RoleService/RoleService.md)
- **Search Service**
  - [Search Service](rest_api/SearchService/SearchService.md)
- **Secret Service**
  - [Secret Service](rest_api/SecretService/SecretService.md)
- **Sensor Upgrade Service**
  - [Sensor Upgrade Service](rest_api/SensorUpgradeService/SensorUpgradeService.md)
- **Service Account Service**
  - [Service Account Service](rest_api/ServiceAccountService/ServiceAccountService.md)
- **Service Identity Service**
  - [Service Identity Service](rest_api/ServiceIdentityService/ServiceIdentityService.md)
- **Signature Integration Service**
  - [Signature Integration Service](rest_api/SignatureIntegrationService/SignatureIntegrationService.md)
- **Telemetry Service**
  - [Telemetry Service](rest_api/TelemetryService/TelemetryService.md)
- **User Service**
  - [User Service](rest_api/UserService/UserService.md)
- **Virtual Machine Service**
  - [Virtual Machine Service](rest_api/VirtualMachineService/VirtualMachineService.md)
- **Virtual Machine V2Service**
  - [Virtual Machine V2 Service](rest_api/VirtualMachineV2Service/VirtualMachineV2Service.md)
- **Vulnerability Exception Service**
  - [Vulnerability Exception Service](rest_api/VulnerabilityExceptionService/VulnerabilityExceptionService.md)
- **Vuln Mgmt Service**
  - [Vuln Mgmt Service](rest_api/VulnMgmtService/VulnMgmtService.md)
- **Common Object Reference**
  - [Common Object Reference](rest_api/CommonObjectReference/CommonObjectReference.md)

