<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# OpenShift Container Platform Documentation Index

> IMPORTANT: Prefer retrieval-led reasoning over pre-training-led
> reasoning for OpenShift tasks. Read the referenced files rather
> than relying on training data which may be outdated.

## How to Use This Index

This is a compressed documentation map. Each section lists topic
files using pipe-delimited format: `section/subsection:{file1.md,file2.md}`.
Retrieve the specific file you need rather than reading everything.

Root: ./

## Documentation Map

### Overview

|welcome:{index.md,ocp-overview.md,learn_more_about_openshift.md,kubernetes-overview.md,openshift-editions.md,glossary.md,oke_about.md,providing-feedback-on-red-hat-documentation.md,legal-notice.md}

### Release notes

|release_notes:{ocp-4-20-release-notes.md,addtl-release-notes.md}

### Tutorials

|tutorials:{index.md,dev-app-web-console.md,dev-app-cli.md,additional-tutorials.md}

### Architecture

|architecture:{index.md,architecture.md,architecture-installation.md,ocm-overview-ocp.md,mce-overview-ocp.md,control-plane.md,understanding-development.md,architecture-rhcos.md,admission-plug-ins.md}

### Disconnected environments

|disconnected:{about.md,connected-to-disconnected.md,index.md,installing-mirroring-creating-registry.md,about-installing-oc-mirror-v2.md,oc-mirror-migration-v1-to-v2.md,installing-mirroring-disconnected.md,installing-mirroring-installation-images.md,installing.md,using-olm.md}
|disconnected/updating:{index.md,mirroring-image-repository.md,disconnected-update-osus.md,disconnected-update.md,uninstalling-osus.md}

### Installing

|installing/overview:{index.md,installing-preparing.md,cluster-capabilities.md,installing-fips.md}
|installing/installing_alibaba:{installing-alibaba-assisted-installer.md}
|installing/installing_aws:{preparing-to-install-on-aws.md,installing-aws-account.md,installing-aws-three-node.md,uninstalling-cluster-aws.md,installation-config-parameters-aws.md,aws-compute-edge-zone-tasks.md}
|installing/installing_aws/ipi:{ipi-aws-preparing-to-install.md,installing-aws-default.md,installing-aws-customizations.md,installing-restricted-networks-aws-installer-provisioned.md,installing-aws-vpc.md,installing-aws-private.md,installing-aws-specialized-region.md,installing-aws-localzone.md,installing-aws-wavelength-zone.md,installing-aws-outposts.md,installing-aws-multiarch-support.md}
|installing/installing_aws/upi:{upi-aws-preparing-to-install.md,upi-aws-installation-reqs.md,installing-aws-user-infra.md,installing-restricted-networks-aws.md,installing-aws-multiarch-support-upi.md}
|installing/installing_azure:{preparing-to-install-on-azure.md,installing-azure-account.md,installing-azure-three-node.md,uninstalling-cluster-azure.md,installation-config-parameters-azure.md}
|installing/installing_azure/ipi:{installing-azure-preparing-ipi.md,installing-azure-default.md,installing-azure-customizations.md,installing-restricted-networks-azure-installer-provisioned.md,installing-azure-vnet.md,installing-azure-private.md,installing-azure-government-region.md}
|installing/installing_azure/upi:{installing-azure-preparing-upi.md,installing-restricted-networks-azure-user-provisioned.md,installing-azure-user-infra.md}
|installing/installing_azure_stack_hub:{preparing-to-install-on-azure-stack-hub.md,installing-azure-stack-hub-account.md,installation-config-parameters-ash.md,uninstalling-cluster-azure-stack-hub.md}
|installing/installing_azure_stack_hub/ipi:{ipi-ash-preparing-to-install.md,installing-azure-stack-hub-default.md,installing-azure-stack-hub-network-customizations.md}
|installing/installing_azure_stack_hub/upi:{upi-ash-preparing-to-install.md,installing-azure-stack-hub-user-infra.md}
|installing/installing_gcp:{preparing-to-install-on-gcp.md,installing-gcp-account.md,installing-gcp-default.md,installing-gcp-customizations.md,installing-restricted-networks-gcp-installer-provisioned.md,installing-gcp-vpc.md,installing-gcp-shared-vpc.md,installing-gcp-private.md,installing-gcp-user-infra.md,installing-gcp-user-infra-vpc.md,installing-restricted-networks-gcp.md,installing-gcp-three-node.md,installation-config-parameters-gcp.md,uninstalling-cluster-gcp.md,installing-gcp-multiarch-support.md}
|installing/installing_ibm_cloud:{preparing-to-install-on-ibm-cloud.md,installing-ibm-cloud-account.md,configuring-iam-ibm-cloud.md,user-managed-encryption-ibm-cloud.md,installing-ibm-cloud-customizations.md,installing-ibm-cloud-vpc.md,installing-ibm-cloud-private.md,installing-ibm-cloud-restricted.md,installation-config-parameters-ibm-cloud-vpc.md,uninstalling-cluster-ibm-cloud.md}
|installing/installing_nutanix:{preparing-to-install-on-nutanix.md,nutanix-failure-domains.md,installing-nutanix-installer-provisioned.md,installing-restricted-networks-nutanix-installer-provisioned.md,installing-nutanix-three-node.md,uninstalling-cluster-nutanix.md,installation-config-parameters-nutanix.md}
|installing/installing_on_prem_assisted:{installing-on-prem-assisted.md}
|installing/installing_with_agent_based_installer:{preparing-to-install-with-agent-based-installer.md,understanding-disconnected-installation-mirroring.md,installing-with-agent-basic.md,installing-with-agent-based-installer.md,installing-ove.md,prepare-pxe-assets-agent.md,installing-using-iscsi.md,preparing-an-agent-based-installed-cluster-for-mce.md,installation-config-parameters-agent.md,agent-based-installer-postinstallation.md}
|installing/installing_sno:{install-sno-preparing-to-install-sno.md,install-sno-installing-sno.md}
|installing/installing_two_node_cluster:{about-two-node-arbiter-installation.md}
|installing/installing_two_node_cluster/installing_tnf:{installing-two-node-fencing.md,install-tnf.md,install-post-tnf.md}
|installing/installing_bare_metal:{preparing-to-install-on-bare-metal.md,bare-metal-postinstallation-configuration.md,bare-metal-expanding-the-cluster.md,bare-metal-using-bare-metal-as-a-service.md}
|installing/installing_bare_metal/upi:{installing-bare-metal.md,installing-bare-metal-network-customizations.md,installing-restricted-networks-bare-metal.md,scaling-a-user-provisioned-cluster-with-the-bare-metal-operator.md,installation-config-parameters-bare-metal.md}
|installing/installing_bare_metal/ipi:{ipi-install-overview.md,ipi-install-prerequisites.md,ipi-install-installation-workflow.md,ipi-install-installing-a-cluster.md,ipi-install-troubleshooting.md}
|installing/installing_ibm_cloud_classic:{install-ibm-cloud-prerequisites.md,install-ibm-cloud-installation-workflow.md}
|installing/installing_ibm_z:{preparing-to-install-on-ibm-z.md,installation-config-parameters-ibm-z.md,ibmz-post-install.md}
|installing/installing_ibm_z/upi:{installing-ibm-z-reqs.md,upi-ibm-z-preparing-to-install.md,installing-ibm-z.md,installing-restricted-networks-ibm-z.md,installing-ibm-z-kvm.md,installing-restricted-networks-ibm-z-kvm.md,installing-ibm-z-lpar.md,installing-restricted-networks-ibm-z-lpar.md}
|installing/installing_ibm_power:{preparing-to-install-on-ibm-power.md,installing-ibm-power.md,installing-restricted-networks-ibm-power.md,installation-config-parameters-ibm-power.md}
|installing/installing_ibm_powervs:{preparing-to-install-on-ibm-power-vs.md,installing-ibm-cloud-account-power-vs.md,creating-ibm-power-vs-workspace.md,installing-ibm-power-vs-customizations.md,installing-ibm-powervs-vpc.md,installing-ibm-power-vs-private-cluster.md,installing-restricted-networks-ibm-power-vs.md,uninstalling-cluster-ibm-power-vs.md,installation-config-parameters-ibm-power-vs.md}
|installing/installing_openstack:{preparing-to-install-on-openstack.md,installing-openstack-nfv-preparing.md,installing-openstack-installer-custom.md,installing-openstack-user.md,installing-openstack-installer-restricted.md,installing-openstack-three-node.md,installing-openstack-network-config.md,installing-openstack-cloud-config-reference.md,deploying-openstack-with-rootVolume-etcd-on-local-disk.md,uninstalling-cluster-openstack.md,uninstalling-openstack-user.md,installation-config-parameters-openstack.md}
|installing/installing_oci:{installing-oci-assisted-installer.md,installing-oci-agent-based-installer.md}
|installing/installing_oci_edge:{installing-c3-assisted-installer.md,installing-c3-agent-based-installer.md}
|installing/installing_vsphere:{preparing-to-install-on-vsphere.md,installing-vsphere-assisted-installer.md,installing-vsphere-agent-based-installer.md,installing-vsphere-three-node.md,uninstalling-cluster-vsphere-installer-provisioned.md,using-vsphere-problem-detector-operator.md,installation-config-parameters-vsphere.md,post-install-vsphere-zones-regions-configuration.md,vsphere-post-installation-encryption.md,installing-vsphere-post-installation-configuration.md}
|installing/installing_vsphere/ipi:{ipi-vsphere-installation-reqs.md,ipi-vsphere-preparing-to-install.md,installing-vsphere-installer-provisioned.md,installing-vsphere-installer-provisioned-customizations.md,installing-restricted-networks-installer-provisioned-vsphere.md}
|installing/installing_vsphere/upi:{upi-vsphere-installation-reqs.md,upi-vsphere-preparing-to-install.md,installing-vsphere.md,installing-vsphere-network-customizations.md,installing-restricted-networks-vsphere.md}
|installing/installing_platform_agnostic:{installing-platform-agnostic.md}
|installing/install_config:{installing-customizing.md,configuring-firewall.md}
|installing/validation_and_troubleshooting:{validating-an-installation.md,installing-troubleshooting.md}

### Postinstallation configuration

|post_installation_configuration:{index.md,configuring-private-cluster.md,cluster-tasks.md,node-tasks.md,post-install-network-configuration.md,post-install-image-config.md,post-install-storage-configuration.md,preparing-for-users.md,changing-cloud-credentials-configuration.md,configuring-alert-notifications.md,converting-to-disconnected.md}
|post_installation_configuration/configuring-multi-arch-compute-machines:{multi-architecture-configuration.md,creating-multi-arch-compute-nodes-aws.md,creating-multi-arch-compute-nodes-azure.md,creating-multi-arch-compute-nodes-google-cloud.md,creating-multi-arch-compute-nodes-bare-metal.md,creating-multi-arch-compute-nodes-ibm-z.md,creating-multi-arch-compute-nodes-ibm-z-lpar.md,creating-multi-arch-compute-nodes-ibm-z-kvm.md,creating-multi-arch-compute-nodes-ibm-power.md,multi-architecture-compute-managing.md,multiarch-tuning-operator.md,multi-arch-tuning-operator-release-notes.md}
|post_installation_configuration/day_2_core_cnf_clusters:{telco-day-2-welcome.md}
|post_installation_configuration/day_2_core_cnf_clusters/updating:{update-welcome.md,update-api.md,update-ocp-update-prep.md,update-cnf-update-prep.md,update-before-the-update.md,update-completing-the-control-plane-only-update.md,update-completing-the-y-stream-update.md,update-completing-the-z-stream-update.md}
|post_installation_configuration/day_2_core_cnf_clusters/updating:{update-rhacm-talm-overview.md,update-rhacm-talm-preparing-policies.md,update-rhacm-talm-worker-batching.md,update-rhacm-talm-health-checks.md,update-rhacm-talm-worker-management.md,update-rhacm-talm-operator-coordination.md,update-rhacm-talm-z-stream.md,update-rhacm-talm-y-stream.md,update-rhacm-talm-eus.md,update-rhacm-talm-troubleshooting.md}
|post_installation_configuration/day_2_core_cnf_clusters/troubleshooting:{troubleshooting-intro.md,troubleshooting-general-troubleshooting.md,troubleshooting-cluster-maintenance.md,troubleshooting-security.md,troubleshooting-cert-maintenance.md,troubleshooting-mco.md,troubleshooting-bmn-maintenance.md}
|post_installation_configuration/day_2_core_cnf_clusters/observability:{observability.md}
|post_installation_configuration/day_2_core_cnf_clusters/security:{security-basics.md,security-host-sec.md,security-sec-context-constraints.md}

### Updating clusters

|updating/understanding_updates:{intro-to-updates.md,how-updates-work.md,understanding-update-channels-release.md,understanding-openshift-update-duration.md}
|updating/preparing_for_updates:{updating-cluster-prepare.md,preparing-manual-creds-update.md,kmm-preflight-validation.md}
|updating/updating_a_cluster:{updating-cluster-cli.md,updating-cluster-web-console.md,control-plane-only-update.md,update-using-custom-machine-config-pools.md,disconnected-update.md,updating-hardware-on-nodes-running-on-vsphere.md,migrating-to-multi-payload.md,updating-bootloader-rhcos.md}
|updating/troubleshooting_updates:{gathering-data-cluster-update.md}

### Support

|support:{index.md,managing-cluster-resources.md,getting-support.md,gathering-cluster-data.md,summarizing-cluster-specifications.md}
|support/remote_health_monitoring:{about-remote-health-monitoring.md,showing-data-collected-by-remote-health-monitoring.md,remote-health-reporting.md,using-insights-to-identify-issues-with-your-cluster.md,using-insights-operator.md,remote-health-reporting-from-restricted-network.md,insights-operator-simple-access.md}
|support/troubleshooting:{troubleshooting-installations.md,verifying-node-health.md,troubleshooting-crio-issues.md,troubleshooting-operating-system-issues.md,troubleshooting-network-issues.md,troubleshooting-operator-issues.md,investigating-pod-issues.md,troubleshooting-s2i.md,troubleshooting-storage-issues.md,troubleshooting-windows-container-workload-issues.md,investigating-monitoring-issues.md,diagnosing-oc-issues.md}

### Web console

|web_console:{web-console-overview.md,web-console.md,using-dashboard-to-get-cluster-information.md,adding-user-preferences.md,configuring-web-console.md,customizing-the-web-console.md,disabling-web-console.md,creating-quick-start-tutorials.md,capabilities_products-web-console.md}
|web_console/dynamic-plugin:{overview-dynamic-plugin.md,dynamic-plugins-get-started.md,deploy-plugin-cluster.md,content-security-policy.md,dynamic-plugin-example.md,dynamic-plugins-reference.md}
|web_console/web_terminal:{installing-web-terminal.md,configuring-web-terminal.md,odc-using-web-terminal.md,troubleshooting-web-terminal.md,uninstalling-web-terminal.md}

### CLI tools

|cli_reference:{index.md,odo-important-update.md,kn-cli-tools.md,gitops-argocd-cli-tools.md,hcp-cli-ref.md}
|cli_reference/openshift_cli:{getting-started-cli.md,configuring-cli.md,usage-oc-kubectl.md,managing-cli-profiles.md,extending-cli-plugins.md,developer-cli-commands.md,administrator-cli-commands.md}
|cli_reference/cli_manager:{index.md,cli-manager-release-notes.md,cli-manager-install.md,cli-manager-using.md,cli-manager-uninstall.md}
|cli_reference/tkn_cli:{installing-tkn.md,op-configuring-tkn.md,op-tkn-reference.md}
|cli_reference/opm:{cli-opm-install.md,cli-opm-ref.md}

### Security and compliance

|security:{index.md,audit-log-view.md,audit-log-policy-config.md,tls-security-profiles.md,seccomp-profiles.md,allowing-javascript-access-api-server.md,pod-vulnerability-scan.md}
|security/container_security:{security-understanding.md,security-hosts-vms.md,security-hardening.md,security-container-signature.md,security-compliance.md,security-container-content.md,security-registries.md,security-build.md,security-deploy.md,security-platform.md,security-network.md,security-storage.md,security-monitoring.md}
|security/certificates:{replacing-default-ingress-certificate.md,api-server.md,service-serving-certificate.md,updating-ca-bundle.md}
|security/certificate_types_descriptions:{user-provided-certificates-for-api-server.md,proxy-certificates.md,service-ca-certificates.md,node-certificates.md,bootstrap-certificates.md,etcd-certificates.md,olm-certificates.md,aggregated-api-client-certificates.md,machine-config-operator-certificates.md,user-provided-certificates-for-default-ingress.md,ingress-certificates.md,monitoring-and-cluster-logging-operator-component-certificates.md,control-plane-certificates.md}
|security/compliance_operator:{co-overview.md,compliance-operator-release-notes.md,co-support.md}
|security/compliance_operator/co-concepts:{compliance-operator-understanding.md,compliance-operator-crd.md}
|security/compliance_operator/co-management:{compliance-operator-installation.md,compliance-operator-updating.md,compliance-operator-manage.md,compliance-operator-uninstallation.md}
|security/compliance_operator/co-scans:{compliance-operator-supported-profiles.md,compliance-scans.md,compliance-operator-checkresult-custom-metadata.md,compliance-operator-tailor.md,compliance-operator-raw-results.md,compliance-operator-remediation.md,compliance-operator-advanced.md,compliance-operator-troubleshooting.md,oc-compliance-plug-in-using.md}
|security/file_integrity_operator:{fio-overview.md,file-integrity-operator-release-notes.md,fio-support.md,file-integrity-operator-installation.md,file-integrity-operator-updating.md,file-integrity-operator-understanding.md,file-integrity-operator-configuring.md,file-integrity-operator-advanced-usage.md,file-integrity-operator-troubleshooting.md,fio-uninstalling.md}
|security/security_profiles_operator:{spo-overview.md,spo-release-notes.md,spo-support.md,spo-understanding.md,spo-enabling.md,spo-seccomp.md,spo-selinux.md,spo-advanced.md,spo-troubleshooting.md,spo-uninstalling.md}
|security/nbde_tang_server_operator:{nbde-tang-server-operator-overview.md,nbde-tang-server-operator-release-notes.md,nbde-tang-server-operator-understanding.md,nbde-tang-server-operator-installing.md,nbde-tang-server-operator-configuring-managing.md,nbde-tang-server-operator-identifying-url.md}
|security/cert_manager_operator:{index.md,cert-manager-operator-release-notes.md,cert-manager-operator-install.md,cert-manager-operator-proxy.md,cert-manager-customizing-api-fields.md,cert-manager-authenticate.md,cert-manager-operator-issuer-acme.md,cert-manager-creating-certificate.md,cert-manager-securing-routes.md,cert-manager-operator-integrating-istio.md,cert-manager-nw-policy.md,cert-manager-trust-manager.md,cert-manager-monitoring.md,cert-manager-log-levels.md,cert-manager-operator-uninstall.md}
|security/zero_trust_workload_identity_manager:{zero-trust-manager-overview.md,zero-trust-manager-components.md,zero-trust-manager-release-notes.md,zero-trust-manager-install.md,zero-trust-manager-configuration.md,zero-trust-manager-proxy.md,zero-trust-manager-oidc-federation.md,zero-trust-manager-spire-federation.md,zero-trust-manager-spiffe-helper.md,zero-trust-manager-mesh-integration.md,zero-trust-manager-reconciliation.md,zero-trust-manager-plugins.md,zero-trust-manager-monitoring.md,zero-trust-manager-uninstall.md}
|security/external_secrets_operator:{index.md,external-secrets-operator-release-notes.md,external-secrets-operator-install.md,external-secrets-operator-config-net-policy.md,external-secrets-operator-proxy.md,external-secrets-monitoring.md,external-secrets-log-levels.md,external-secrets-operator-uninstall.md,external-secrets-operator-api.md,external-secrets-operator-migrate-downstream-upstream.md}
|security/network_bound_disk_encryption:{nbde-about-disk-encryption-technology.md,nbde-tang-server-installation-considerations.md,nbde-managing-encryption-keys.md,nbde-disaster-recovery-considerations.md}

### Authentication and authorization

|authentication:{index.md,understanding-authentication.md,configuring-internal-oauth.md,configuring-oauth-clients.md,managing-oauth-access-tokens.md,understanding-identity-provider.md,external-auth.md,using-rbac.md,remove-kubeadmin.md,understanding-and-creating-service-accounts.md,using-service-accounts-in-applications.md,using-service-accounts-as-oauth-client.md,tokens-scoping.md,bound-service-account-tokens.md,managing-security-context-constraints.md,understanding-and-managing-pod-security-admission.md,impersonating-system-admin.md,ldap-syncing.md}
|authentication/identity_providers:{configuring-htpasswd-identity-provider.md,configuring-keystone-identity-provider.md,configuring-ldap-identity-provider.md,configuring-basic-authentication-identity-provider.md,configuring-request-header-identity-provider.md,configuring-github-identity-provider.md,configuring-gitlab-identity-provider.md,configuring-google-identity-provider.md,configuring-oidc-identity-provider.md}
|authentication/managing_cloud_provider_credentials:{about-cloud-credential-operator.md,cco-mode-mint.md,cco-mode-passthrough.md,cco-mode-manual.md,cco-short-term-creds.md}

### Networking

|networking/networking_overview:{understanding-networking.md,accessing-hosts.md,networking-dashboards.md,cidr-range-definitions.md}
|networking/networking_operators:{k8s-nmstate-about-the-k8s-nmstate-operator.md,cluster-network-operator.md,dns-operator.md,ingress-operator.md,ingress-node-firewall-operator.md}
|networking/networking_operators/aws_load_balancer_operator:{aws-load-balancer-operator-release-notes.md,understanding-aws-load-balancer-operator.md,preparing-sts-cluster-for-albo.md,install-aws-load-balancer-operator.md,configuring-aws-load-balancer-operator.md}
|networking/networking_operators/ebpf_manager:{ebpf-manager-operator-about.md,ebpf-manager-operator-install.md,ebpf-manager-operator-deploy.md}
|networking/networking_operators/external_dns_operator:{external-dns-operator-release-notes.md,understanding-external-dns-operator.md,nw-installing-external-dns-operator-on-cloud-providers.md,nw-configuration-parameters.md,nw-creating-dns-records-on-aws.md,nw-creating-dns-records-on-azure.md,nw-creating-dns-records-on-gcp.md,nw-creating-dns-records-on-infoblox.md,nw-configuring-cluster-wide-egress-proxy.md}
|networking/networking_operators/metallb-operator:{about-metallb.md,metallb-operator-install.md,metallb-upgrading-operator.md}
|networking/networking_operators/sr-iov-operator:{installing-sriov-operator.md,configuring-sriov-operator.md,uninstalling-sriov-operator.md}
|networking/networking_operators/dpu-operator:{dpu-operator.md}
|networking/network_observability_operator:{network-observability-operator.md}
|networking/network_security:{network-policy-apis.md,logging-network-security.md,configuring-ipsec-ovn.md,zero-trust-networking.md}
|networking/network_security/AdminNetworkPolicy:{ovn-k-anp.md,ovn-k-banp.md,ovn-k-anp-banp-metrics.md,ovn-k-egress-nodes-networks-peer.md,ovn-k-anp-troubleshooting.md,ovn-k-anp-recommended-practices.md}
|networking/network_security/network_policy:{about-network-policy.md,creating-network-policy.md,viewing-network-policy.md,editing-network-policy.md,deleting-network-policy.md,default-network-policy.md,multitenant-network-policy.md}
|networking/network_security/egress_firewall:{viewing-egress-firewall-ovn.md,editing-egress-firewall-ovn.md,removing-egress-firewall-ovn.md,configuring-egress-firewall-ovn.md}
|networking/multiple_networks:{understanding-multiple-networks.md,use-cases-secondary-network.md,about-virtual-routing-and-forwarding.md,assigning-a-secondary-network-to-a-vrf.md}
|networking/multiple_networks/primary_networks:{about-user-defined-networks.md,about-primary-nwt-nad.md}
|networking/multiple_networks/secondary_networks:{creating-secondary-nwt-ovnk.md,creating-secondary-nwt-other-cni.md,attaching-pod.md,configuring-multi-network-policy.md,removing-pod.md,editing-additional-network.md,configuring-ip-secondary-nwt.md,configuring-master-interface.md,removing-additional-network.md,about-chaining.md}
|networking/hardware_networks:{about-sriov.md,configuring-sriov-device.md,configuring-sriov-net-attach.md,configuring-sriov-ib-attach.md,configuring-namespaced-sriov-resources.md,configuring-sriov-rdma-cni.md,configuring-interface-sysctl-sriov-device.md,configuring-sriov-qinq-support.md,using-sriov-multicast.md,using-dpdk-and-rdma.md,configure-lacp-for-sriov.md,using-pod-level-bonding.md,configuring-hardware-offloading.md,switching-bf2-nic-dpu.md}
|networking/ovn_kubernetes_network_provider:{about-ovn-kubernetes.md,ovn-kubernetes-architecture-assembly.md,ovn-kubernetes-troubleshooting-sources.md,ovn-kubernetes-tracing-using-ovntrace.md,converting-to-dual-stack.md,configure-ovn-kubernetes-subnets.md,configuring-gateway.md,configuring-secondary-external-gateway.md,configuring-egress-ips-ovn.md,configuring-egress-traffic-for-vrf-loadbalancer-services.md,using-an-egress-router-ovn.md,deploying-egress-router-ovn-redirection.md,enabling-multicast.md,disabling-multicast.md,tracking-network-flows.md,configuring-hybrid-networking.md}
|networking/ingress_load_balancing:{load-balancing-openstack.md}
|networking/ingress_load_balancing/routes:{creating-basic-routes.md,securing-routes.md,nw-configuring-routes.md,creating-advanced-routes.md}
|networking/ingress_load_balancing/configuring_ingress_cluster_traffic:{overview-traffic.md,configuring-externalip.md,configuring-ingress-cluster-traffic-ingress-controller.md,nw-configuring-ingress-controller-endpoint-publishing-strategy.md,configuring-ingress-cluster-traffic-load-balancer.md,configuring-ingress-cluster-traffic-aws.md,configuring-ingress-cluster-traffic-service-external-ip.md,configuring-ingress-cluster-traffic-nodeport.md,configuring-ingress-cluster-traffic-load-balancer-allowed-source-ranges.md,configuring-ingress-cluster-patch-fields.md,ingress-controller-dnsmgt.md,ingress-gateway-api.md}
|networking/ingress_load_balancing/metallb:{metallb-configure-address-pools.md,about-advertising-ipaddresspool.md,metallb-configure-bgp-peers.md,metallb-configure-community-alias.md,metallb-configure-bfd-profiles.md,metallb-configure-services.md,metallb-configure-return-traffic.md,metallb-frr-k8s.md,metallb-troubleshoot-support.md}
|networking/configuring_network_settings:{configure-syscontrols-interface-tuning-cni.md,configuring-node-port-service-range.md,configuring-cluster-network-range.md,configuring-ipfailover.md,enable-cluster-wide-proxy.md,configuring-a-custom-pki.md}
|networking/advanced_networking:{verifying-connectivity-endpoint.md,changing-cluster-network-mtu.md,network-bonding-considerations.md,using-sctp.md,associating-secondary-interfaces-metrics-to-network-attachments.md}
|networking/advanced_networking/bgp_routing:{about-bgp-routing.md,enabling-bgp-routing.md,disabling-bgp-routing.md,migrating-frr-k8s-resources.md}
|networking/advanced_networking/route_advertisements:{about-route-advertisements.md,enabling-route-advertisements.md,disabling-route-advertisements.md,example-route-advertisement-setup.md}
|networking/advanced_networking/ptp:{about-ptp.md,configuring-ptp.md,ptp-cloud-events-consumer-dev-reference-v2.md,ptp-events-rest-api-reference-v2.md}
|networking/k8s_nmstate:{k8s-nmstate-updating-node-network-config.md,k8s-nmstate-troubleshooting-node-network.md}

### Storage

|storage:{index.md,understanding-ephemeral-storage.md,understanding-persistent-storage.md,generic-ephemeral-vols.md,expanding-persistent-volumes.md,dynamic-provisioning.md,persistent-storage-csi-vol-detach-non-graceful-shutdown.md}
|storage/persistent_storage:{persistent-storage-aws.md,persistent-storage-azure.md,persistent-storage-azure-file.md,persistent-storage-cinder.md,persistent-storage-fibre.md,persistent-storage-flexvolume.md,persistent-storage-gce.md,persistent-storage-iscsi.md,persistent-storage-nfs.md,persistent-storage-ocs.md,persistent-storage-vsphere.md}
|storage/persistent_storage_local:{ways-to-provision-local-storage.md,persistent-storage-local.md,persistent-storage-hostpath.md,persistent-storage-using-lvms.md}
|storage/container_storage_interface:{persistent-storage-csi.md,ephemeral-storage-csi-inline.md,persistent-storage-csi-snapshots.md,persistent-storage-csi-group-snapshots.md,persistent-storage-csi-cloning.md,persistent-storage-csi-vol-populators.md,persistent-storage-csi-sc-manage.md,persistent-storage-csi-migration.md,persistent-storage-csi-ebs.md,persistent-storage-csi-aws-efs.md,persistent-storage-csi-azure.md,persistent-storage-csi-azure-file.md,persistent-storage-csi-azure-stack-hub.md,persistent-storage-csi-gcp-pd.md,persistent-storage-csi-google-cloud-file.md,persistent-storage-csi-ibm-cloud-vpc-block.md,persistent-storage-csi-ibm-powervs-block.md,persistent-storage-csi-cinder.md,persistent-storage-csi-manila.md,persistent-storage-csi-secrets-store.md,persistent-storage-csi-smb-cifs.md,persistent-storage-csi-vsphere.md}

### Registry

|registry:{index.md,configuring-registry-operator.md,accessing-the-registry.md,securing-exposing-registry.md}
|registry/configuring_registry_storage:{configuring-registry-storage-aws-user-infrastructure.md,configuring-registry-storage-gcp-user-infrastructure.md,configuring-registry-storage-openstack-user-infrastructure.md,configuring-registry-storage-azure-user-infrastructure.md,configuring-registry-storage-osp.md,configuring-registry-storage-baremetal.md,configuring-registry-storage-vsphere.md,configuring-registry-storage-rhodf.md,configuring-registry-storage-nutanix.md}

### Operators

|operators:{index.md,operator-reference.md}
|operators/understanding:{olm-what-operators-are.md,olm-packaging-format.md,olm-common-terms.md,olm-understanding-software-catalog.md,olm-rh-catalogs.md,olm-multitenancy.md}
|operators/understanding/olm:{olm-understanding-olm.md,olm-arch.md,olm-workflow.md,olm-understanding-dependency-resolution.md,olm-understanding-operatorgroups.md,olm-colocation.md,olm-operatorconditions.md,olm-understanding-metrics.md,olm-webhooks.md}
|operators/understanding/crds:{crd-extending-api-with-crds.md,crd-managing-resources-from-crds.md}
|operators/user:{olm-creating-apps-from-installed-operators.md,olm-installing-operators-in-namespace.md}
|operators/admin:{olm-adding-operators-to-cluster.md,olm-upgrading-operators.md,olm-deleting-operators-from-cluster.md,olm-config.md,olm-configuring-proxy-support.md,olm-status.md,olm-managing-operatorconditions.md,olm-creating-policy.md,olm-managing-custom-catalogs.md,olm-restricted-networks.md,olm-cs-podsched.md,olm-troubleshooting-operator-issues.md}
|operators/operator_sdk/token_auth:{osdk-token-auth.md,osdk-cco-aws-sts.md,osdk-cco-azure.md,osdk-cco-gcp.md}
|operators/olm_v1:{index.md}

### Extensions

|extensions:{index.md,of-terms.md}
|extensions/arch:{components.md,operator-controller.md,catalogd.md}
|extensions/catalogs:{fbc.md,rh-catalogs.md,managing-catalogs.md,catalog-content-resolution.md,creating-catalogs.md,disconnected-catalogs.md}
|extensions/ce:{managing-ce.md,user-access-resources.md,update-paths.md,crd-upgrade-safety.md}

### CI/CD

|cicd/overview:{index.md}
|cicd/builds_using_shipwright:{overview-openshift-builds.md}
|cicd/builds:{understanding-image-builds.md,understanding-buildconfigs.md,creating-build-inputs.md,managing-build-output.md,build-strategies.md,custom-builds-buildah.md,basic-build-operations.md,triggering-builds-build-hooks.md,advanced-build-operations.md,running-entitled-builds.md,securing-builds-by-strategy.md,build-configuration.md,troubleshooting-builds.md,setting-up-trusted-ca.md}
|cicd/pipelines:{about-pipelines.md}
|cicd/gitops:{about-redhat-openshift-gitops.md}
|cicd/jenkins:{images-other-jenkins.md,images-other-jenkins-agent.md,migrating-from-jenkins-to-openshift-pipelines.md,important-changes-to-openshift-jenkins-images.md}

### Images

|openshift_images:{index.md,configuring-samples-operator.md,samples-operator-alt-registry.md,create-images.md,image-streams-manage.md,using-imagestreams-with-kube-resources.md,triggering-updates-on-imagestream-changes.md,image-configuration.md}
|openshift_images/managing_images:{managing-images-overview.md,tagging-images.md,image-pull-policy.md,using-image-pull-secrets.md}
|openshift_images/using_images:{using-images-overview.md,using-s21-images.md,customizing-s2i-images.md}

### Building applications

|applications:{index.md,odc-viewing-application-composition-using-topology-view.md,odc-exporting-applications.md,config-maps.md,odc-monitoring-project-and-application-metrics-using-developer-perspective.md,application-health.md,odc-editing-applications.md,pruning-objects.md,idling-applications.md,odc-deleting-applications.md,red-hat-marketplace.md}
|applications/projects:{working-with-projects.md,creating-project-other-user.md,configuring-project-creation.md}
|applications/creating_applications:{using-templates.md,odc-creating-applications-using-developer-perspective.md,creating-apps-from-installed-operators.md,creating-applications-using-cli.md,templates-using-ruby-on-rails.md}
|applications/working_with_helm_charts:{understanding-helm.md,installing-helm.md,configuring-custom-helm-chart-repositories.md,odc-working-with-helm-releases.md}
|applications/deployments:{what-deployments-are.md,managing-deployment-processes.md,deployment-strategies.md,route-based-deployment-strategies.md}
|applications/quotas:{quotas-setting-per-project.md,quotas-setting-across-multiple-projects.md}

### Serverless

|serverless/about:{about-serverless.md}

### Machine configuration

|machine_configuration:{index.md,machine-configs-configure.md,machine-config-node-disruption.md,machine-configs-custom.md,machine-config-pin-preload-images-about.md,mco-update-boot-images.md,machine-configs-garbage-collection.md,mco-coreos-layering.md,machine-config-daemon-metrics.md}

### Machine management

|machine_management:{index.md,manually-scaling-machineset.md,modifying-machineset.md,machine-phases-lifecycle.md,deleting-machine.md,applying-autoscaling.md,creating-infrastructure-machinesets.md,deploying-machine-health-checks.md}
|machine_management/creating_machinesets:{creating-machineset-aws.md,creating-machineset-azure.md,creating-machineset-azure-stack-hub.md,creating-machineset-gcp.md,creating-machineset-ibm-cloud.md,creating-machineset-ibm-power-vs.md,creating-machineset-nutanix.md,creating-machineset-osp.md,creating-machineset-vsphere.md,creating-machineset-bare-metal.md}
|machine_management/user_infra:{adding-compute-user-infra-general.md,adding-aws-compute-user-infra.md,adding-vsphere-compute-user-infra.md,adding-bare-metal-compute-user-infra.md}
|machine_management/control_plane_machine_management:{cpmso-about.md,cpmso-getting-started.md,cpmso-managing-machines.md,cpmso-configuration.md,cpmso-resiliency.md,cpmso-troubleshooting.md,cpmso-disabling.md,cpmso-manually-scaling-control-planes.md}
|machine_management/control_plane_machine_management/cpmso_provider_configurations:{cpmso-config-options-aws.md,cpmso-supported-features-aws.md,cpmso-config-options-azure.md,cpmso-supported-features-azure.md,cpmso-config-options-gcp.md,cpmso-supported-features-gcp.md,cpmso-config-options-nutanix.md,cpmso-config-options-openstack.md,cpmso-supported-features-openstack.md,cpmso-config-options-vsphere.md,cpmso-supported-features-vsphere.md}
|machine_management/cluster_api_machine_management:{cluster-api-about.md,cluster-api-getting-started.md,cluster-api-managing-machines.md,cluster-api-troubleshooting.md,cluster-api-disabling.md}
|machine_management/cluster_api_machine_management/cluster_api_provider_configurations:{cluster-api-config-options-aws.md,cluster-api-config-options-gcp.md,cluster-api-config-options-azure.md,cluster-api-config-options-rhosp.md,cluster-api-config-options-vsphere.md,cluster-api-config-options-bare-metal.md}

### etcd

|etcd:{etcd-overview.md,etcd-practices.md,etcd-performance.md,etcd-encrypt.md,etcd-guidance-span.md}
|etcd/etcd-backup-restore:{etcd-backup.md,replace-unhealthy-etcd-member.md,etcd-disaster-recovery.md}

### Hosted control planes

|hosted_control_planes:{hcp-release-notes.md,index.md,hcp-certificates.md,hcp-updating.md,hcp-authentication-authorization.md,hcp-machine-config.md,hcp-using-feature-gates.md,hcp-observability.md,hcp-networking.md,hcp-troubleshooting.md,hcp-import.md}
|hosted_control_planes/hcp-prepare:{hcp-requirements.md,hcp-sizing-guidance.md,hcp-override-resource-util.md,hcp-cli.md,hcp-distribute-workloads.md,hcp-enable-disable.md}
|hosted_control_planes/hcp-deploy:{hcp-deploy-aws.md,hcp-deploy-bm.md,hcp-deploy-virt.md,hcp-deploy-non-bm.md,hcp-deploy-ibmz.md,hcp-deploy-ibm-power.md,hcp-deploy-openstack.md}
|hosted_control_planes/hcp-manage:{hcp-manage-aws.md,hcp-manage-bm.md,hcp-manage-virt.md,hcp-manage-non-bm.md,hcp-manage-ibm-power.md,hcp-manage-openstack.md}
|hosted_control_planes/hcp-disconnected:{hcp-deploy-dc.md,hcp-deploy-dc-virt.md,hcp-deploy-dc-bm.md,disconnected-install-ibmz-hcp.md,hcp-dc-monitor.md}
|hosted_control_planes/hcp_high_availability:{about-hcp-ha.md,hcp-recovering-etcd-cluster.md,hcp-backup-restore-on-premise.md,hcp-backup-restore-aws.md,hcp-backup-restore-virt.md,hcp-disaster-recovery-aws.md,hcp-disaster-recovery-oadp.md,hcp-disaster-recovery-oadp-auto.md}
|hosted_control_planes/hcp-destroy:{hcp-destroy-aws.md,hcp-destroy-bm.md,hcp-destroy-virt.md,hcp-destroy-ibmz.md,hcp-destroy-ibm-power.md,hcp-destroy-openstack.md,hcp-destroy-non-bm.md}

### Nodes

|nodes:{index.md,nodes-dashboard-using.md,nodes-sigstore-using.md}
|nodes/pods:{nodes-pods-using.md,nodes-pods-viewing.md,nodes-pods-configuring.md,nodes-pods-autoscaling.md,nodes-pods-vertical-autoscaler.md,nodes-pods-adjust-resources-in-place.md,nodes-pods-secrets.md,nodes-pods-secrets-store.md,nodes-pods-short-term-auth.md,nodes-pods-configmaps.md,nodes-pods-image-volume.md,nodes-pods-plugins.md,nodes-pods-priority.md,nodes-pods-node-selectors.md,nodes-pods-allocate-dra.md,nodes-pods-user-namespaces.md}
|nodes/pods/run_once_duration_override:{index.md,run-once-duration-override-release-notes.md,run-once-duration-override-install.md,run-once-duration-override-uninstall.md}
|nodes/cma:{nodes-cma-autoscaling-custom.md,nodes-cma-autoscaling-custom-install.md,nodes-cma-autoscaling-custom-trigger.md,nodes-cma-autoscaling-custom-trigger-auth.md,nodes-cma-autoscaling-custom-adding.md,nodes-cma-autoscaling-custom-pausing.md,nodes-cma-autoscaling-custom-audit-log.md,nodes-cma-autoscaling-custom-debugging.md,nodes-cma-autoscaling-custom-metrics.md,nodes-cma-autoscaling-custom-removing.md}
|nodes/cma/nodes-cma-rn:{nodes-cma-autoscaling-custom-rn.md,nodes-cma-autoscaling-custom-rn-past.md}
|nodes/scheduling:{nodes-scheduler-about.md,nodes-scheduler-profiles.md,nodes-scheduler-pod-affinity.md,nodes-scheduler-node-affinity.md,nodes-scheduler-overcommit.md,nodes-scheduler-taints-tolerations.md,nodes-scheduler-node-selectors.md,nodes-scheduler-pod-topology-spread-constraints.md}
|nodes/scheduling/descheduler:{index.md,nodes-descheduler-release-notes.md,nodes-descheduler-configuring.md,nodes-descheduler-uninstalling.md}
|nodes/scheduling/secondary_scheduler:{index.md,nodes-secondary-scheduler-release-notes.md,nodes-secondary-scheduler-configuring.md,nodes-secondary-scheduler-uninstalling.md}
|nodes/jobs:{nodes-pods-daemonsets.md,nodes-nodes-jobs.md}
|nodes/nodes:{nodes-nodes-viewing.md,nodes-nodes-working.md,nodes-nodes-managing.md,nodes-nodes-adding-node-iso.md,nodes-nodes-managing-max-pods.md,nodes-nodes-replace-control-plane.md,nodes-node-tuning-operator.md,nodes-remediating-fencing-maintaining-rhwa.md,nodes-nodes-rebooting.md,nodes-update-boot-images.md,nodes-nodes-garbage-collection.md,nodes-nodes-resources-configuring.md,nodes-nodes-resources-cpus.md,nodes-nodes-tls.md,nodes-nodes-creating-infrastructure-nodes.md}
|nodes/containers:{nodes-containers-using.md,nodes-containers-init.md,nodes-containers-volumes.md,nodes-containers-projected-volumes.md,nodes-containers-downward-api.md,nodes-containers-copying-files.md,nodes-containers-remote-commands.md,nodes-containers-port-forwarding.md,nodes-containers-sysctls.md,nodes-containers-dev-fuse.md}
|nodes/clusters:{nodes-containers-events.md,nodes-cluster-resource-levels.md,nodes-cluster-limit-ranges.md,nodes-cluster-resource-configure.md,nodes-cluster-overcommit.md,nodes-cluster-enabling-features.md,nodes-cluster-worker-latency-profiles.md}
|nodes/edge:{nodes-edge-remote-workers.md}
|nodes/nodes:{nodes-sno-worker-nodes.md}

### Windows Container Support for OpenShift

|windows_containers:{index.md,windows-containers-support.md,understanding-windows-container-workloads.md,enabling-windows-container-workloads.md,scheduling-windows-workloads.md,windows-node-upgrades.md,byoh-windows-instance.md,removing-windows-nodes.md,disabling-windows-container-workloads.md,windows-containers-troubleshooting.md}
|windows_containers/wmco_rn:{windows-containers-release-notes.md,windows-containers-release-notes-past.md,windows-containers-release-notes-prereqs.md,windows-containers-release-notes-limitations.md}
|windows_containers/creating_windows_machinesets:{creating-windows-machineset-aws.md,creating-windows-machineset-azure.md,creating-windows-machineset-gcp.md,creating-windows-machineset-nutanix.md,creating-windows-machineset-vsphere.md}

### OpenShift sandboxed containers

|sandboxed_containers:{about-openshift-sandboxed-containers.md}

### Observability

|observability/overview:{index.md}
|observability/cluster_observability_operator:{cluster-observability-operator-overview.md}
|observability/monitoring:{about-ocp-monitoring.md}
|observability/logging:{about-logging.md}
|observability/distr_tracing:{distr-tracing-tempo-architecture.md}
|observability/otel:{otel-architecture.md}
|observability/network_observability:{network-observability-operator-release-notes.md,network-observability-overview.md,installing-operators.md,network-observability-kafka-operator-scaling-network-flow-collection.md,understanding-network-observability-operator.md,configuring-operator.md,network-observability-per-tenant-model.md,network-observability-network-policy.md,network-observability-dns-resolution-analysis.md,observing-network-traffic.md,network-observability-health-rules.md,network-observability-monitoring-tls-traffic.md,metrics-alerts-dashboards.md,network-observability-operator-monitoring.md,network-observability-scheduling-resources.md,network-observability-secondary-networks.md,flowcollector-api.md,flowmetric-api.md,json-flows-format-reference.md,troubleshooting-network-observability.md}
|observability/network_observability/release_notes_archive:{network-observability-operator-release-notes-archive.md}
|observability/network_observability/netobserv_cli:{netobserv-cli-install.md,netobserv-cli-using.md,netobserv-cli-reference.md}
|observability/power_monitoring:{about-power-monitoring.md}

### Scalability and performance

|scalability_and_performance:{index.md,telco-core-rds.md,telco-ran-du-rds.md,telco-hub-rds.md,planning-your-environment-according-to-object-maximums.md,compute-resource-quotas.md,ibm-z-recommended-host-practices.md,using-node-tuning-operator.md,using-cpu-manager.md,cnf-numa-aware-scheduling.md,managing-bare-metal-hosts.md,what-huge-pages-do-and-how-they-are-consumed-by-apps.md,cnf-understanding-low-latency.md,cnf-tuning-low-latency-nodes-with-perf-profile.md,cnf-tuning-low-latency-hosted-cp-nodes-with-perf-profile.md,cnf-provisioning-low-latency-workloads.md,cnf-debugging-low-latency-tuning-status.md,cnf-performing-platform-verification-latency-tests.md,scaling-worker-latency-profiles.md,enabling-workload-partitioning.md,node-observability-operator.md}
|scalability_and_performance/recommended-performance-scale-practices:{recommended-control-plane-practices.md,increasing-aws-flavor-size.md,recommended-infrastructure-practices.md}
|scalability_and_performance/cluster-compare:{understanding-the-cluster-compare-plugin.md,installing-cluster-compare-plugin.md,using-the-cluster-compare-plugin.md,creating-a-reference-configuration.md,advanced-ref-config-customization.md,troubleshooting-cluster-comparisons.md}
|scalability_and_performance/optimization:{optimizing-storage.md,routing-optimization.md,optimizing-networking.md,optimizing-cpu-usage.md}

### AI workloads

|ai_workloads:{index.md}
|ai_workloads/kueue:{about-kueue.md,release-notes.md,install-kueue.md,install-disconnected.md,integrating-lws.md,integrating-jobset.md,rbac-permissions.md,configuring-quotas.md,managing-workloads.md,monitoring-pending-workloads.md,using-cohorts.md,configuring-fairsharing.md,admission-fair-sharing.md,gangscheduling.md,running-kueue-jobs.md,getting-support.md}
|ai_workloads/leader_worker_set:{index.md,lws-release-notes.md,lws-managing.md,lws-uninstalling.md}
|ai_workloads/jobset_operator:{index.md,jobset-release-notes.md,jobset-install.md,managing-jobset.md,jobset-uninstall.md}

### Edge computing

|edge_computing:{ztp-deploying-far-edge-clusters-at-scale.md,ztp-preparing-the-hub-cluster.md,ztp-updating-gitops.md,ztp-deploying-far-edge-sites.md,ztp-manual-install.md,ztp-migrate-clusterinstance.md,ztp-reference-cluster-configuration-for-vdu.md,ztp-vdu-validating-cluster-tuning.md,ztp-advanced-install-ztp.md,ztp-using-hub-cluster-templates.md,cnf-talm-for-cluster-upgrades.md,ztp-sno-additional-worker-node.md,ztp-precaching-tool.md}
|edge_computing/policygenerator_for_ztp:{ztp-configuring-managed-clusters-policygenerator.md,ztp-advanced-policygenerator-config.md,ztp-talm-updating-managed-policies-pg.md}
|edge_computing/policygentemplate_for_ztp:{ztp-configuring-managed-clusters-policies.md,ztp-advanced-policy-config.md,ztp-talm-updating-managed-policies.md}
|edge_computing/image_based_upgrade:{cnf-understanding-image-based-upgrade.md,cnf-image-based-upgrade-base.md,ztp-image-based-upgrade.md}
|edge_computing/image_based_upgrade/preparing_for_image_based_upgrade:{cnf-image-based-upgrade-shared-container-partition.md,cnf-image-based-upgrade-install-operators.md,cnf-image-based-upgrade-generate-seed.md,cnf-image-based-upgrade-prep-resources.md,ztp-image-based-upgrade-prep-resources.md,cnf-image-based-upgrade-auto-image-cleanup.md}
|edge_computing/image_base_install:{ibi-understanding-image-based-install.md,ibi-preparing-for-image-based-install.md,ibi-factory-image-based-install.md}
|edge_computing/image_base_install/ibi_deploying_sno_clusters:{ibi-edge-image-based-install.md,ibi-edge-image-based-install-standalone.md}

### Specialized hardware and driver enablement

|hardware_enablement:{about-hardware-enablement.md,psap-driver-toolkit.md,psap-node-feature-discovery-operator.md,kmm-kernel-module-management.md,kmm-release-notes.md}

### Hardware accelerators

|hardware_accelerators:{about-hardware-accelerators.md,nvidia-gpu-architecture.md,amd-gpu-operator.md,gaudi-ai-accelerator.md,rdma-remote-direct-memory-access.md,das-about-dynamic-accelerator-slicer-operator.md}

### Backup and restore

|backup_and_restore:{index.md,graceful-cluster-shutdown.md,graceful-cluster-restart.md,hibernating-cluster.md}
|backup_and_restore/application_backup_and_restore:{oadp-intro.md,oadp-features-plugins.md,oadp-api.md}
|backup_and_restore/application_backup_and_restore/release-notes:{oadp-1-5-release-notes.md,oadp-upgrade-notes-1-5.md}
|backup_and_restore/application_backup_and_restore/oadp-performance:{oadp-recommended-network-settings.md}
|backup_and_restore/application_backup_and_restore/oadp-use-cases:{oadp-usecase-backup-using-odf.md,oadp-usecase-restore-different-namespace.md,oadp-usecase-enable-ca-cert.md,oadp-usecase-legacy-aws-plugin.md,oadp-rosa-backup-restore.md}
|backup_and_restore/application_backup_and_restore/installing:{about-installing-oadp.md,oadp-installing-operator.md}
|backup_and_restore/application_backup_and_restore/installing:{installing-oadp-aws.md}
|backup_and_restore/application_backup_and_restore/installing:{installing-oadp-ibm-cloud.md}
|backup_and_restore/application_backup_and_restore/installing:{installing-oadp-azure.md}
|backup_and_restore/application_backup_and_restore/installing:{installing-oadp-gcp.md}
|backup_and_restore/application_backup_and_restore/installing:{installing-oadp-mcg.md}
|backup_and_restore/application_backup_and_restore/installing:{installing-oadp-ocs.md}
|backup_and_restore/application_backup_and_restore/installing:{installing-oadp-kubevirt.md}
|backup_and_restore/application_backup_and_restore/installing:{configuring-oadp-multiple-bsl.md}
|backup_and_restore/application_backup_and_restore/installing:{configuring-oadp-multiple-vsl.md}
|backup_and_restore/application_backup_and_restore/installing:{uninstalling-oadp.md}
|backup_and_restore/application_backup_and_restore/backing_up_and_restoring:{backing-up-applications.md,oadp-creating-backup-cr.md,oadp-backing-up-pvs-csi-doc.md,oadp-backing-up-applications-restic-doc.md,oadp-creating-backup-hooks-doc.md,oadp-scheduling-backups-doc.md,oadp-deleting-backups.md,oadp-about-kopia.md}
|backup_and_restore/application_backup_and_restore/backing_up_and_restoring:{restoring-applications.md}
|backup_and_restore/application_backup_and_restore/oadp-self-service:{oadp-self-service.md,oadp-self-service-cluster-admin-use-cases.md,oadp-self-service-namespace-admin-use-cases.md,oadp-self-service-troubleshooting.md}
|backup_and_restore/application_backup_and_restore/oadp-rosa:{oadp-rosa-backing-up-applications.md}
|backup_and_restore/application_backup_and_restore/aws-sts:{oadp-aws-sts.md}
|backup_and_restore/application_backup_and_restore/oadp-3scale:{backing-up-and-restoring-3scale-api-management-by-using-oadp.md,backing-up-3scale-api-management-by-using-oadp.md,restoring-3scale-api-management-by-using-oadp.md}
|backup_and_restore/application_backup_and_restore/installing:{about-oadp-data-mover.md,oadp-backup-restore-csi-snapshots.md,configuring-backup-restore-pvc-datamover.md,overriding-kopia-algorithms.md}
|backup_and_restore/application_backup_and_restore/oadp-advanced-topics:{oadp-different-kubernetes-api-versions.md,oadp-backing-up-data-one-cluster-restoring-another-cluster.md,oadp-storage-class-mapping-main.md}
|backup_and_restore/application_backup_and_restore/troubleshooting:{troubleshooting.md,velero-cli-tool.md,pods-crash-or-restart-due-to-lack-of-memory-or-cpu.md,restoring-workarounds-for-velero-backups-that-use-admission-webhooks.md,oadp-installation-issues.md,oadp-operator-issues.md,oadp-timeouts.md,backup-and-restore-cr-issues.md,restic-issues.md,oadp-data-protection-test.md,using-the-must-gather-tool.md,oadp-monitoring.md}
|backup_and_restore/control_plane_backup_and_restore:{backing-up-etcd.md,replacing-unhealthy-etcd-member.md}
|backup_and_restore/control_plane_backup_and_restore/disaster_recovery:{about-disaster-recovery.md,quorum-restoration.md,scenario-2-restoring-cluster-state.md,scenario-3-expired-certs.md}

### Migrating from version 3 to 4

|migrating_from_ocp_3_to_4:{index.md,about-migrating-from-3-to-4.md,planning-migration-3-4.md,planning-considerations-3-4.md,about-mtc-3-4.md,installing-3-4.md,installing-restricted-3-4.md,upgrading-3-4.md,premigration-checklists-3-4.md,migrating-applications-3-4.md,advanced-migration-options-3-4.md,troubleshooting-3-4.md}

### Migration Toolkit for Containers

|migration_toolkit_for_containers:{about-mtc.md,installing-mtc.md,installing-mtc-restricted.md,upgrading-mtc.md,premigration-checklists-mtc.md,network-considerations-mtc.md,mtc-direct-migration-requirements.md,migrating-applications-with-mtc.md,advanced-migration-options-mtc.md,mtc-migrating-vms.md,troubleshooting-mtc.md}
|migration_toolkit_for_containers/release_notes:{mtc-release-notes.md,mtc-release-notes-1-7.md,mtc-release-notes-1-6.md,mtc-release-notes-1-5.md}

### API reference

|rest_api/overview:{understanding-api-support-tiers.md,understanding-compatibility-guidelines.md,editing-kubelet-log-level-verbosity.md,index.md}
|rest_api/objects:{index.md}
|rest_api/authorization_apis:{authorization-apis-index.md,localresourceaccessreview-authorization-openshift-io-v1.md,localsubjectaccessreview-authorization-openshift-io-v1.md,resourceaccessreview-authorization-openshift-io-v1.md,selfsubjectrulesreview-authorization-openshift-io-v1.md,subjectaccessreview-authorization-openshift-io-v1.md,subjectrulesreview-authorization-openshift-io-v1.md,selfsubjectreview-authentication-k8s-io-v1.md,tokenrequest-authentication-k8s-io-v1.md,tokenreview-authentication-k8s-io-v1.md,localsubjectaccessreview-authorization-k8s-io-v1.md,selfsubjectaccessreview-authorization-k8s-io-v1.md,selfsubjectrulesreview-authorization-k8s-io-v1.md,subjectaccessreview-authorization-k8s-io-v1.md}
|rest_api/autoscale_apis:{autoscale-apis-index.md,clusterautoscaler-autoscaling-openshift-io-v1.md,machineautoscaler-autoscaling-openshift-io-v1beta1.md,horizontalpodautoscaler-autoscaling-v2.md,scale-autoscaling-v1.md}
|rest_api/cluster_apis:{cluster-apis-index.md,ipaddress-ipam-cluster-x-k8s-io-v1beta1.md,ipaddressclaim-ipam-cluster-x-k8s-io-v1beta1.md}
|rest_api/config_apis:{config-apis-index.md,apiserver-config-openshift-io-v1.md,authentication-config-openshift-io-v1.md,build-config-openshift-io-v1.md,clusterimagepolicy-config-openshift-io-v1.md,clusteroperator-config-openshift-io-v1.md,clusterversion-config-openshift-io-v1.md,console-config-openshift-io-v1.md,dns-config-openshift-io-v1.md,featuregate-config-openshift-io-v1.md,helmchartrepository-helm-openshift-io-v1beta1.md,image-config-openshift-io-v1.md,imagedigestmirrorset-config-openshift-io-v1.md,imagecontentpolicy-config-openshift-io-v1.md,imagepolicy-config-openshift-io-v1.md,imagetagmirrorset-config-openshift-io-v1.md,infrastructure-config-openshift-io-v1.md,ingress-config-openshift-io-v1.md,network-config-openshift-io-v1.md,node-config-openshift-io-v1.md,oauth-config-openshift-io-v1.md,operatorhub-config-openshift-io-v1.md,project-config-openshift-io-v1.md,projecthelmchartrepository-helm-openshift-io-v1beta1.md,proxy-config-openshift-io-v1.md,scheduler-config-openshift-io-v1.md}
|rest_api/console_apis:{console-apis-index.md,consoleclidownload-console-openshift-io-v1.md,consoleexternalloglink-console-openshift-io-v1.md,consolelink-console-openshift-io-v1.md,consolenotification-console-openshift-io-v1.md,consoleplugin-console-openshift-io-v1.md,consolequickstart-console-openshift-io-v1.md,consolesample-console-openshift-io-v1.md,consoleyamlsample-console-openshift-io-v1.md}
|rest_api/extension_apis:{extension-apis-index.md,apiservice-apiregistration-k8s-io-v1.md,customresourcedefinition-apiextensions-k8s-io-v1.md,mutatingwebhookconfiguration-admissionregistration-k8s-io-v1.md,validatingadmissionpolicy-admissionregistration-k8s-io-v1.md,validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md,validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md}
|rest_api/image_apis:{image-apis-index.md,image-image-openshift-io-v1.md,imagesignature-image-openshift-io-v1.md,imagestreamimage-image-openshift-io-v1.md,imagestreamimport-image-openshift-io-v1.md,imagestreamlayers-image-openshift-io-v1.md,imagestreammapping-image-openshift-io-v1.md,imagestream-image-openshift-io-v1.md,imagestreamtag-image-openshift-io-v1.md,imagetag-image-openshift-io-v1.md,secretlist-image-openshift-io-v1.md}
|rest_api/machine_apis:{machine-apis-index.md,containerruntimeconfig-machineconfiguration-openshift-io-v1.md,controllerconfig-machineconfiguration-openshift-io-v1.md,controlplanemachineset-machine-openshift-io-v1.md,kubeletconfig-machineconfiguration-openshift-io-v1.md,machineconfig-machineconfiguration-openshift-io-v1.md,machineconfigpool-machineconfiguration-openshift-io-v1.md,machinehealthcheck-machine-openshift-io-v1beta1.md,machine-machine-openshift-io-v1beta1.md,machineset-machine-openshift-io-v1beta1.md,machineconfignode-machineconfiguration-openshift-io-v1.md,machineosbuild-machineconfiguration-openshift-io-v1.md,machineosconfig-machineconfiguration-openshift-io-v1.md,pinnedimageset-machineconfiguration-openshift-io-v1.md}
|rest_api/metadata_apis:{metadata-apis-index.md,apirequestcount-apiserver-openshift-io-v1.md,binding-v1.md,componentstatus-v1.md,configmap-v1.md,controllerrevision-apps-v1.md,event-events-k8s-io-v1.md,event-v1.md,lease-coordination-k8s-io-v1.md,namespace-v1.md}
|rest_api/monitoring_apis:{monitoring-apis-index.md,alertmanager-monitoring-coreos-com-v1.md,alertmanagerconfig-monitoring-coreos-com-v1beta1.md,alertrelabelconfig-monitoring-openshift-io-v1.md,alertingrule-monitoring-openshift-io-v1.md,podmonitor-monitoring-coreos-com-v1.md,probe-monitoring-coreos-com-v1.md,prometheus-monitoring-coreos-com-v1.md,prometheusrule-monitoring-coreos-com-v1.md,servicemonitor-monitoring-coreos-com-v1.md,thanosruler-monitoring-coreos-com-v1.md,nodemetrics-metrics-k8s-io-v1beta1.md,podmetrics-metrics-k8s-io-v1beta1.md}
|rest_api/network_apis:{network-apis-index.md,clusteruserdefinednetwork-k8s-ovn-org-v1.md,adminnetworkpolicy-policy-networking-k8s-io-v1alpha1.md,adminpolicybasedexternalroute-k8s-ovn-org-v1.md,baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1.md,cloudprivateipconfig-cloud-network-openshift-io-v1.md,egressfirewall-k8s-ovn-org-v1.md,egressip-k8s-ovn-org-v1.md,egressqos-k8s-ovn-org-v1.md,egressservice-k8s-ovn-org-v1.md,endpoints-v1.md,endpointslice-discovery-k8s-io-v1.md,egressrouter-network-operator-openshift-io-v1.md,grpcroute-gateway-networking-k8s-io-v1.md,gateway-gateway-networking-k8s-io-v1.md,gatewayclass-gateway-networking-k8s-io-v1.md,httproute-gateway-networking-k8s-io-v1.md,ingress-networking-k8s-io-v1.md,ingressclass-networking-k8s-io-v1.md,ipaddress-networking-k8s-io-v1.md,ipamclaim-k8s-cni-cncf-io-v1alpha1.md,ippool-whereabouts-cni-cncf-io-v1alpha1.md,multinetworkpolicy-k8s-cni-cncf-io-v1beta1.md,networkattachmentdefinition-k8s-cni-cncf-io-v1.md,networkpolicy-networking-k8s-io-v1.md,nodeslicepool-whereabouts-cni-cncf-io-v1alpha1.md,overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1.md,podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1.md,referencegrant-gateway-networking-k8s-io-v1beta1.md,route-route-openshift-io-v1.md,service-v1.md,servicecidr-networking-k8s-io-v1.md,ipaddressclaim-ipam-cluster-x-k8s-io-v1beta1.md,userdefinednetwork-k8s-ovn-org-v1.md}
|rest_api/node_apis:{node-apis-index.md,node-v1.md,performanceprofile-performance-openshift-io-v2.md,profile-tuned-openshift-io-v1.md,runtimeclass-node-k8s-io-v1.md,tuned-tuned-openshift-io-v1.md}
|rest_api/oauth_apis:{oauth-apis-index.md,oauthaccesstoken-oauth-openshift-io-v1.md,oauthauthorizetoken-oauth-openshift-io-v1.md,oauthclientauthorization-oauth-openshift-io-v1.md,oauthclient-oauth-openshift-io-v1.md,useroauthaccesstoken-oauth-openshift-io-v1.md}
|rest_api/operator_apis:{operator-apis-index.md,authentication-operator-openshift-io-v1.md,cloudcredential-operator-openshift-io-v1.md,clustercsidriver-operator-openshift-io-v1.md,console-operator-openshift-io-v1.md,config-operator-openshift-io-v1.md,config-imageregistry-operator-openshift-io-v1.md,config-samples-operator-openshift-io-v1.md,csisnapshotcontroller-operator-openshift-io-v1.md,dns-operator-openshift-io-v1.md,dnsrecord-ingress-operator-openshift-io-v1.md,etcd-operator-openshift-io-v1.md,imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md,imagepruner-imageregistry-operator-openshift-io-v1.md,ingresscontroller-operator-openshift-io-v1.md,insightsoperator-operator-openshift-io-v1.md,kubeapiserver-operator-openshift-io-v1.md,kubecontrollermanager-operator-openshift-io-v1.md,kubescheduler-operator-openshift-io-v1.md,kubestorageversionmigrator-operator-openshift-io-v1.md,machineconfiguration-operator-openshift-io-v1.md,network-operator-openshift-io-v1.md,openshiftapiserver-operator-openshift-io-v1.md,openshiftcontrollermanager-operator-openshift-io-v1.md,operatorpki-network-operator-openshift-io-v1.md,serviceca-operator-openshift-io-v1.md,storage-operator-openshift-io-v1.md}
|rest_api/operatorhub_apis:{operatorhub-apis-index.md,catalogsource-operators-coreos-com-v1alpha1.md,clustercatalog-olm-operatorframework-io-v1.md,clusterextension-olm-operatorframework-io-v1.md,clusterserviceversion-operators-coreos-com-v1alpha1.md,installplan-operators-coreos-com-v1alpha1.md,olmconfig-operators-coreos-com-v1.md,operator-operators-coreos-com-v1.md,operatorcondition-operators-coreos-com-v2.md,operatorgroup-operators-coreos-com-v1.md,packagemanifest-packages-operators-coreos-com-v1.md,subscription-operators-coreos-com-v1alpha1.md}
|rest_api/policy_apis:{policy-apis-index.md,eviction-policy-v1.md,poddisruptionbudget-policy-v1.md}
|rest_api/project_apis:{project-apis-index.md,project-project-openshift-io-v1.md,projectrequest-project-openshift-io-v1.md}
|rest_api/provisioning_apis:{provisioning-apis-index.md,bmceventsubscription-metal3-io-v1alpha1.md,baremetalhost-metal3-io-v1alpha1.md,dataimage-metal3-io-v1alpha1.md,firmwareschema-metal3-io-v1alpha1.md,hardwaredata-metal3-io-v1alpha1.md,hostfirmwarecomponents-metal3-io-v1alpha1.md,hostfirmwaresettings-metal3-io-v1alpha1.md,hostupdatepolicy-metal3-io-v1alpha1.md,metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md,metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1.md,preprovisioningimage-metal3-io-v1alpha1.md,provisioning-metal3-io-v1alpha1.md}
|rest_api/rbac_apis:{rbac-apis-index.md,clusterrolebinding-rbac-authorization-k8s-io-v1.md,clusterrole-rbac-authorization-k8s-io-v1.md,rolebinding-rbac-authorization-k8s-io-v1.md,role-rbac-authorization-k8s-io-v1.md}
|rest_api/role_apis:{role-apis-index.md,clusterrolebinding-authorization-openshift-io-v1.md,clusterrole-authorization-openshift-io-v1.md,rolebindingrestriction-authorization-openshift-io-v1.md,rolebinding-authorization-openshift-io-v1.md,role-authorization-openshift-io-v1.md}
|rest_api/schedule_and_quota_apis:{schedule-and-quota-apis-index.md,appliedclusterresourcequota-quota-openshift-io-v1.md,clusterresourcequota-quota-openshift-io-v1.md,flowschema-flowcontrol-apiserver-k8s-io-v1.md,limitrange-v1.md,priorityclass-scheduling-k8s-io-v1.md,prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1.md,resourcequota-v1.md}
|rest_api/security_apis:{security-apis-index.md,certificatesigningrequest-certificates-k8s-io-v1.md,credentialsrequest-cloudcredential-openshift-io-v1.md,podsecuritypolicyreview-security-openshift-io-v1.md,podsecuritypolicyselfsubjectreview-security-openshift-io-v1.md,podsecuritypolicysubjectreview-security-openshift-io-v1.md,rangeallocation-security-openshift-io-v1.md,secret-v1.md,securitycontextconstraints-security-openshift-io-v1.md,serviceaccount-v1.md}
|rest_api/storage_apis:{storage-apis-index.md,csidriver-storage-k8s-io-v1.md,csinode-storage-k8s-io-v1.md,csistoragecapacity-storage-k8s-io-v1.md,persistentvolume-v1.md,persistentvolumeclaim-v1.md,storageclass-storage-k8s-io-v1.md,storagestate-migration-k8s-io-v1alpha1.md,storageversionmigration-migration-k8s-io-v1alpha1.md,volumeattachment-storage-k8s-io-v1.md,volumepopulator-populator-storage-k8s-io-v1beta1.md,volumesnapshot-snapshot-storage-k8s-io-v1.md,volumesnapshotclass-snapshot-storage-k8s-io-v1.md,volumesnapshotcontent-snapshot-storage-k8s-io-v1.md}
|rest_api/template_apis:{template-apis-index.md,brokertemplateinstance-template-openshift-io-v1.md,podtemplate-v1.md,template-template-openshift-io-v1.md,templateinstance-template-openshift-io-v1.md}
|rest_api/user_and_group_apis:{user-and-group-apis-index.md,group-user-openshift-io-v1.md,identity-user-openshift-io-v1.md,useridentitymapping-user-openshift-io-v1.md,user-user-openshift-io-v1.md}
|rest_api/workloads_apis:{workloads-apis-index.md,buildconfig-build-openshift-io-v1.md,build-build-openshift-io-v1.md,buildlog-build-openshift-io-v1.md,buildrequest-build-openshift-io-v1.md,cronjob-batch-v1.md,daemonset-apps-v1.md,deployment-apps-v1.md,deploymentconfig-apps-openshift-io-v1.md,deploymentconfigrollback-apps-openshift-io-v1.md,deploymentlog-apps-openshift-io-v1.md,deploymentrequest-apps-openshift-io-v1.md,job-batch-v1.md,pod-v1.md,replicationcontroller-v1.md,replicaset-apps-v1.md,statefulset-apps-v1.md}

### OpenShift Lightspeed

|lightspeed/about:{ols-openshift-lightspeed-overview.md}

### Service Mesh

|service_mesh/v3x:{ossm-service-mesh-3-0-overview.md}
|service_mesh/v2x:{ossm-about.md,servicemesh-release-notes.md,upgrading-ossm.md,ossm-architecture.md,ossm-deployment-models.md,ossm-vs-community.md,preparing-ossm-installation.md,installing-ossm.md,ossm-create-smcp.md,ossm-create-mesh.md,prepare-to-deploy-applications-ossm.md,ossm-profiles-users.md,ossm-security.md,ossm-traffic-manage.md,ossm-gateway-migration.md,ossm-route-migration.md,ossm-observability.md,ossm-performance-scalability.md,ossm-deploy-production.md,ossm-federation.md,ossm-extensions.md,ossm-kiali-ossmc-plugin.md,ossm-threescale-webassembly-module.md,threescale-adapter.md,ossm-troubleshooting-istio.md,ossm-reference-smcp.md,ossm-reference-kiali.md,removing-ossm.md}

### Virtualization

|virt/about_virt:{about-virt.md,virt-supported-limits.md,virt-security-policies.md,virt-architecture.md}
|virt/release_notes:{virt-4-20-release-notes.md}
|virt/getting_started:{virt-getting-started.md,virt-using-the-cli-tools.md}
|virt/install:{preparing-cluster-for-virt.md,virt-requirements.md,installing-virt.md,uninstalling-virt.md}
|virt/post_installation_configuration:{virt-post-install-config.md,virt-node-placement-virt-components.md,virt-post-install-network-config.md,virt-post-install-storage-config.md,virt-physical-cores-allocation-vms.md,virt-configuring-higher-vm-workload-density.md,virt-configuring-certificate-rotation.md}
|virt/updating:{upgrading-virt.md}
|virt/creating_vm:{virt-creating-vms-from-instance-types.md,virt-creating-vms-from-templates.md,virt-configuring-ibm-secure-execution-vms-ibm-z.md,virt-creating-vms-aws-li-windows.md}
|virt/creating_vms_advanced:{virt-creating-vms-from-rh-images-overview.md,virt-golden-image-heterogeneous-clusters.md,virt-creating-vms-from-web-images.md,virt-creating-vms-uploading-images.md,virt-cloning-vms.md,virt-creating-vms-from-cli.md,virt-creating-vms-from-container-disks.md,virt-creating-vms-by-cloning-pvcs.md}
|virt/managing_vms:{virt-list-vms.md,virt-installing-qemu-guest-agent.md,virt-install-virtio-drivers-on-windows-vms.md,virt-update-virtio-drivers.md,virt-accessing-vm-consoles.md,virt-edit-vms.md,virt-edit-boot-order.md,virt-delete-vms.md,virt-enabling-disabling-vm-delete-protection.md,virt-exporting-vms.md,virt-manage-vmis.md,virt-controlling-vm-states.md,virt-using-vtpm-devices.md,virt-managing-vms-openshift-pipelines.md,virt-migrating-vms-in-single-cluster-to-different-storage-class.md}
|virt/managing_vms/ssh:{virt-accessing-vm-ssh.md,virt-using-virtctl-ssh.md,virt-using-secondary-networks-ssh.md,virt-using-services.md}
|virt/managing_vms/advanced_vm_management:{virt-working-with-resource-quotas-for-vms.md,virt-understanding-aaq-operator.md,virt-specifying-nodes-for-vms.md,virt-configuring-default-cpu-model.md,virt-uefi-mode-for-vms.md,virt-configuring-pxe-booting.md,virt-using-huge-pages-with-vms.md,virt-dedicated-resources-vm.md,virt-schedule-vms.md,virt-configuring-pci-passthrough.md,virt-configuring-virtual-gpus.md,virt-configuring-usb-host-passthrough.md,virt-enabling-descheduler-evictions.md,virt-high-availability-for-vms.md,virt-vm-control-plane-tuning.md,virt-assigning-compute-resources.md,virt-about-multi-queue.md,virt-managing-virtual-machines-by-using-openshift-gitops.md,virt-NUMA-topology.md}
|virt/managing_vms/virtual_disks:{virt-hot-plugging-virtual-disks.md,virt-expanding-vm-disks.md,virt-configuring-shared-volumes-for-vms.md,virt-migrating-storage-class.md,virt-inserting-cd-roms-in-virtual-machines.md}
|virt/vm_networking:{virt-networking-overview.md,virt-connecting-vm-to-default-pod-network.md,virt-connecting-vm-to-primary-udn.md,virt-connecting-vm-to-secondary-udn.md,virt-exposing-vm-with-service.md,virt-accessing-vm-internal-fqdn.md,virt-connecting-vm-to-linux-bridge.md,virt-connecting-vm-to-sriov.md,virt-using-dpdk-with-sriov.md,virt-connecting-vm-to-ovn-secondary-network.md,virt-hot-plugging-network-interfaces.md,virt-setting-interface-link-state.md,virt-connecting-vm-to-service-mesh.md,virt-dedicated-network-live-migration.md,virt-configuring-viewing-ips-for-vms.md,virt-accessing-vm-secondary-network-fqdn.md,virt-using-mac-address-pool-for-vms.md}
|virt/storage:{virt-storage-config-overview.md,virt-configuring-storage-profile.md,virt-automatic-bootsource-updates.md,virt-reserving-pvc-space-fs-overhead.md,virt-configuring-local-storage-with-hpp.md,virt-enabling-user-permissions-to-clone-datavolumes.md,virt-configuring-cdi-for-namespace-resourcequota.md,virt-preparing-cdi-scratch-space.md,virt-using-preallocation-for-datavolumes.md,virt-managing-data-volume-annotations.md,virt-storage-with-csi-paradigm.md,install-configure-fusion-access-san.md}
|virt/live_migration:{virt-about-live-migration.md,virt-configuring-live-migration.md,virt-initiating-live-migration.md,virt-enabling-cclm-for-vms.md,virt-configuring-cross-cluster-live-migration-network.md,virt-about-mtv-providers.md}
|virt/nodes:{virt-node-maintenance.md,virt-eviction-strategies.md,virt-managing-node-labeling-obsolete-cpu-models.md,virt-preventing-node-reconciliation.md,virt-activating-ksm.md}
|virt/monitoring:{virt-monitoring-overview.md,virt-running-cluster-checkups.md,virt-prometheus-queries.md,virt-exposing-custom-metrics-for-vms.md,virt-exposing-downward-metrics.md,virt-monitoring-vm-health.md,virt-runbooks.md}
|virt/support:{virt-support-overview.md,virt-collecting-virt-data.md,virt-troubleshooting.md}
|virt/backup_restore:{virt-backup-restore-snapshots.md,virt-backup-restore-overview.md,virt-disaster-recovery.md}

