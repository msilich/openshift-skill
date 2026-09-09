<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Red Hat Advanced Cluster Security for Kubernetes Documentation Index

> IMPORTANT: Prefer retrieval-led reasoning over pre-training-led
> reasoning for OpenShift tasks. Read the referenced files rather
> than relying on training data which may be outdated.

## How to Use This Index

This is a compressed documentation map. Each section lists topic
files using pipe-delimited format: `section/subsection:{file1.md,file2.md}`.
Retrieve the specific file you need rather than reading everything.

Root: ./

## Documentation Map

### About

|welcome:{index.md}

### Release notes

|release_notes:{411-release-notes.md}

### RHACS Cloud Service

|cloud_service:{rhacs-cloud-service-service-description.md,acs-cloud-responsibility-matrix.md,acscs-architecture.md,getting-started-rhacs-cloud-ocp.md,acscs-default-requirements.md,acscs-recommended-requirements.md}
|cloud_service/installing_cloud_ocp:{cloud-create-instance-ocp.md,cloud-ocp-create-project.md,init-bundle-cloud-ocp-generate.md,init-bundle-cloud-ocp-apply.md,cloud-install-operator.md,install-secured-cluster-cloud-ocp.md,configuring-the-proxy-for-secured-cluster-services-in-rhacs-cloud-service.md,verify-installation-cloud-ocp.md}
|cloud_service/installing_cloud_other:{cloud-create-instance-other.md,init-bundle-cloud-other-generate.md,init-bundle-cloud-other-apply.md,install-secured-cluster-cloud-other.md,verify-installation-cloud-other.md}
|cloud_service/upgrading-cloud:{upgrade-cloudsvc-operator.md,upgrade-cloudsvc-helm.md,upgrade-cloudsvc-roxctl.md}

### Architecture

|architecture:{acs-architecture.md}

### Installing

|installing:{acs-high-level-overview.md,acs-default-requirements.md,acs-recommended-requirements.md,uninstall-acs.md}
|installing/installing_ocp:{install-central-ocp.md,install-central-config-options-ocp.md,init-bundle-ocp.md,install-secured-cluster-ocp.md,install-secured-cluster-config-options-ocp.md,verify-installation-rhacs-ocp.md}
|installing/installing_other:{install-rhacs-other.md,install-central-other.md,init-bundle-other.md,install-secured-cluster-other.md,verify-installation-rhacs-other.md}

### Configuring

|configuration:{add-custom-certificates.md,add-trusted-ca.md,internal-certificate-authority-rotation-for-rhacs.md,reissue-internal-certificates.md,add-security-notices.md,customizing-platform-components.md,enable-offline-mode.md,enable-alert-data-retention.md,expose-portal-over-http.md,configure-automatic-upgrades.md,configure-inactive-cluster-deletion.md,configure-proxy.md,generate-diagnostic-bundle.md,configure-endpoints.md,monitor-acs.md,configure-audit-logging.md,configure-api-token.md,using-rhacs-with-gitops.md,declarative-configuration-using.md,inviting-users-to-your-rhacs-instance.md,managing-preview-features.md,configuring-and-integrating-the-rhacs-plugin-with-red-hat-developer-hub.md,accessing-vulnerability-information-in-web-console.md}

### Operating

|operating:{view-dashboard.md,compliance-operator-rhacs.md,evaluate-security-risks.md,manage-network-policies.md,build-time-network-policy-tools.md,visualizing-external-entities.md,using-collector-runtime-configuration.md,audit-listening-endpoints.md,review-cluster-configuration.md,examine-images-for-vulnerabilities.md,verify-image-signatures.md,respond-to-violations.md,create-use-collections.md,search-filter.md,use-system-health-dashboard.md,using-the-administration-events-page.md}
|operating/manage-compliance:{compliance-feature-overview.md,using-openshift-compliance.md}
|operating/manage_security_policies:{about-security-policies.md,use-admission-controller-enforcement.md,configuring-file-activity-monitoring.md,custom-security-policies.md,managing-policies-as-code.md,security-policy-reference.md}
|operating/manage-vulnerabilities:{vulnerability-management.md,common-vuln-management-tasks.md,vulnerability-reporting.md,vulnerability-management-dashboard.md,scan-rhcos-node-host.md,scanner-generate-sbom.md}
|operating/manage-user-access:{manage-role-based-access-control-3630.md,enable-pki-authentication.md,understanding-authentication-providers.md,remove-admin-user.md,configure-short-lived-access.md,understanding-multi-tenancy.md}
|operating/manage-user-access/configuring-identity-providers:{configure-okta-identity-cloud.md,configure-google-workspace-identity.md,configure-ocp-oauth.md,connecting-azure-ad-to-rhacs-using-sso-configuration.md}

### Integrating

|integration:{integrate-with-image-registries.md,integrate-with-ci-systems.md,integrate-with-pagerduty.md,integrate-with-slack.md,integrate-using-generic-webhooks.md,integrate-with-qradar.md,integrate-with-servicenow.md,integrate-with-sumologic.md,integrate-with-google-cloud-storage.md,integrate-using-syslog-protocol.md,integrate-with-amazon-s3.md,integrate-with-s3-api-compatible-services.md,integrate-with-google-cloud-scc.md,integrate-with-splunk.md,integrate-with-image-vulnerability-scanners.md,integrate-with-jira.md,integrate-with-email.md,integrate-with-cloud-management-platforms.md,integrate-using-short-lived-tokens.md,integrating-with-microsoft-sentinel-notifier.md}

### Backup and restore

|backup_and_restore:{backing-up-acs.md,restore-acs.md}

### Upgrading

|upgrading:{upgrade-operator.md,upgrade-helm.md,upgrade-roxctl.md}

### roxctl CLI

|cli:{installing-the-roxctl-cli.md,using-the-roxctl-cli.md,managing-secured-clusters.md,checking-policy-compliance.md,debugging-issues.md,image-scanning-by-using-the-roxctl-cli.md}
|cli/command-reference:{roxctl.md,roxctl-central.md,roxctl-cluster.md,roxctl-collector.md,roxctl-completion.md,roxctl-declarative-config.md,roxctl-deployment.md,roxctl-helm.md,roxctl-image.md,roxctl-netpol.md,roxctl-scanner.md,roxctl-sensor.md,roxctl-version.md}

### Troubleshooting Collector

|troubleshooting:{retrieving-and-analyzing-the-collector-logs-and-pod-status.md,commonly-occurring-error-conditions.md}

### Troubleshooting Central

|troubleshooting_central:{backing-up-central-database-by-using-the-roxctl-cli.md,restoring-central-database-by-using-the-roxctl-cli.md}

### Telemetry

|telemetry:{about-telemetry.md,opting-out-of-telemetry.md}

### Support

|support:{getting-support.md}

### API reference

|rest_api/AdministrationEventService:{AdministrationEventService.md}
|rest_api/AdministrationUsageService:{AdministrationUsageService.md}
|rest_api/AlertService:{AlertService.md}
|rest_api/APITokenService:{APITokenService.md}
|rest_api/AuthProviderService:{AuthProviderService.md}
|rest_api/AuthService:{AuthService.md}
|rest_api/BaseImageServiceV2:{BaseImageServiceV2.md}
|rest_api/CentralHealthService:{CentralHealthService.md}
|rest_api/CloudSourcesService:{CloudSourcesService.md}
|rest_api/ClusterCVEService:{ClusterCVEService.md}
|rest_api/ClusterInitService:{ClusterInitService.md}
|rest_api/ClustersService:{ClustersService.md}
|rest_api/CollectionService:{CollectionService.md}
|rest_api/ComplianceIntegrationService:{ComplianceIntegrationService.md}
|rest_api/ComplianceManagementService:{ComplianceManagementService.md}
|rest_api/ComplianceProfileService:{ComplianceProfileService.md}
|rest_api/ComplianceResultsService:{ComplianceResultsService.md}
|rest_api/ComplianceResultsStatsService:{ComplianceResultsStatsService.md}
|rest_api/ComplianceRuleService:{ComplianceRuleService.md}
|rest_api/ComplianceScanConfigurationService:{ComplianceScanConfigurationService.md}
|rest_api/ComplianceService:{ComplianceService.md}
|rest_api/ConfigService:{ConfigService.md}
|rest_api/CredentialExpiryService:{CredentialExpiryService.md}
|rest_api/DBService:{DBService.md}
|rest_api/DebugService:{DebugService.md}
|rest_api/DeclarativeConfigHealthService:{DeclarativeConfigHealthService.md}
|rest_api/DelegatedRegistryConfigService:{DelegatedRegistryConfigService.md}
|rest_api/DeploymentService:{DeploymentService.md}
|rest_api/DetectionService:{DetectionService.md}
|rest_api/DiscoveredClustersService:{DiscoveredClustersService.md}
|rest_api/ExternalBackupService:{ExternalBackupService.md}
|rest_api/FeatureFlagService:{FeatureFlagService.md}
|rest_api/GroupService:{GroupService.md}
|rest_api/GRPCPreferencesService:{GRPCPreferencesService.md}
|rest_api/ImageIntegrationService:{ImageIntegrationService.md}
|rest_api/ImageService:{ImageService.md}
|rest_api/IntegrationHealthService:{IntegrationHealthService.md}
|rest_api/ListeningEndpointsService:{ListeningEndpointsService.md}
|rest_api/MetadataService:{MetadataService.md}
|rest_api/MitreAttackService:{MitreAttackService.md}
|rest_api/NamespaceService:{NamespaceService.md}
|rest_api/NetworkBaselineService:{NetworkBaselineService.md}
|rest_api/NetworkGraphService:{NetworkGraphService.md}
|rest_api/NetworkPolicyService:{NetworkPolicyService.md}
|rest_api/NodeCVEService:{NodeCVEService.md}
|rest_api/NodeService:{NodeService.md}
|rest_api/NotifierService:{NotifierService.md}
|rest_api/PingService:{PingService.md}
|rest_api/PodService:{PodService.md}
|rest_api/PolicyCategoryService:{PolicyCategoryService.md}
|rest_api/PolicyService:{PolicyService.md}
|rest_api/ProbeUploadService:{ProbeUploadService.md}
|rest_api/ProcessBaselineService:{ProcessBaselineService.md}
|rest_api/ProcessService:{ProcessService.md}
|rest_api/RbacService:{RbacService.md}
|rest_api/ReportConfigurationService:{ReportConfigurationService.md}
|rest_api/ReportService:{ReportService.md}
|rest_api/RoleService:{RoleService.md}
|rest_api/SearchService:{SearchService.md}
|rest_api/SecretService:{SecretService.md}
|rest_api/SensorUpgradeService:{SensorUpgradeService.md}
|rest_api/ServiceAccountService:{ServiceAccountService.md}
|rest_api/ServiceIdentityService:{ServiceIdentityService.md}
|rest_api/SignatureIntegrationService:{SignatureIntegrationService.md}
|rest_api/TelemetryService:{TelemetryService.md}
|rest_api/UserService:{UserService.md}
|rest_api/VirtualMachineService:{VirtualMachineService.md}
|rest_api/VirtualMachineV2Service:{VirtualMachineV2Service.md}
|rest_api/VulnerabilityExceptionService:{VulnerabilityExceptionService.md}
|rest_api/VulnMgmtService:{VulnMgmtService.md}
|rest_api/CommonObjectReference:{CommonObjectReference.md}

