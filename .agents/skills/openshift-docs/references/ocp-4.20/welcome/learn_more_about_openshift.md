<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To better use OpenShift Container Platform, you should first learn about and better understand how OpenShift Container Platform functions.

You can use the following sections to find content to help you learn about OpenShift Container Platform.

Learning and support
| Learn about OpenShift Container Platform | Optional additional resources |
|----|----|
| [What’s new in OpenShift Container Platform](https://www.openshift.com/learn/whats-new) | [OpenShift blog](https://www.openshift.com/blog?hsLang=en-us) |
| [OpenShift Container Platform Life Cycle Policy](https://access.redhat.com/support/policy/updates/openshift) | [OpenShift Container Platform life cycle](https://access.redhat.com/support/policy/updates/openshift#ocp4_phases) |
| [OpenShift Interactive Learning Portal](https://learn.openshift.com/?extIdCarryOver=true&sc_cid=701f2000001Css5AAC) | [OpenShift Knowledgebase articles](https://access.redhat.com/articles/4217411) |
| [Getting Support](../support/getting-support.md#getting-support) | [Gathering data about your cluster](../support/gathering-cluster-data.md#gathering-data) |

Architecture
| Learn about OpenShift Container Platform | Optional additional resources |
|----|----|
| [Enterprise Kubernetes with OpenShift](https://www.openshift.com/blog/enterprise-kubernetes-with-openshift-part-one?extIdCarryOver=true&sc_cid=701f2000001Css5AAC) | [Tested platforms](https://access.redhat.com/articles/4128421) |
| [Architecture](../architecture/architecture.md#architecture) | [Security and compliance](../security/container_security/security-understanding.md#understanding-security) |
| [Networking](../networking/networking_overview/understanding-networking.md#understanding-networking) | [OVN-Kubernetes architecture](../networking/ovn_kubernetes_network_provider/ovn-kubernetes-architecture-assembly.md#ovn-kubernetes-architecture-con) |
| [Backup and restore](../backup_and_restore/index.md#backup-restore-overview) | [Restoring to a previous cluster state](../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md#scenario-2-restoring-cluster-state) |

Installation
Explore the following OpenShift Container Platform installation tasks:

| Learn about installation on OpenShift Container Platform | Optional additional resources |
|----|----|
| [OpenShift Container Platform installation overview](../installing/overview/index.md#ocp-installation-overview) | [Selecting a cluster installation method and preparing it for users](../installing/overview/installing-preparing.md#installing-preparing) |
| [Installing a cluster in FIPS mode](../installing/overview/installing-fips.md#installing-fips-mode_installing-fips) | [About FIPS compliance](../installing/installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.md#agent-installer-fips-compliance_preparing-to-install-with-agent-based-installer) |

Other cluster installer tasks
| Learn about other installer tasks on OpenShift Container Platform | Optional additional resources |
|----|----|
| [Troubleshooting installation issues](../installing/validation_and_troubleshooting/installing-troubleshooting.md#installing-troubleshooting) | [Validating an installation](../installing/validation_and_troubleshooting/validating-an-installation.md#validating-an-installation) |
| [Install Red Hat OpenShift Data Foundation](../storage/persistent_storage/persistent-storage-ocs.md#red-hat-openshift-data-foundation) | [image mode for OpenShift](../machine_configuration/mco-coreos-layering.md#mco-coreos-layering) |

Install a cluster in a restricted network
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Learn about installing in a restricted network</th>
<th style="text-align: left;">Optional additional resources</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><a href="../disconnected/index.xml#index">About disconnected installation mirroring</a></p></td>
<td style="text-align: left;"><p>If your cluster uses user-provisioned infrastructure, and the cluster does not have full access to the internet, you must mirror the OpenShift Container Platform installation images.</p>
<ul>
<li><p><a href="../installing/installing_aws/upi/installing-restricted-networks-aws.xml#installing-restricted-networks-aws">Amazon Web Services (AWS)</a></p></li>
<li><p><a href="../installing/installing_gcp/installing-restricted-networks-gcp.xml#installing-restricted-networks-gcp">Google Cloud</a></p></li>
<li><p><a href="../installing/installing_vsphere/upi/installing-restricted-networks-vsphere.xml#installing-restricted-networks-vsphere">vSphere</a></p></li>
<li><p><a href="../installing/installing_ibm_cloud/installing-ibm-cloud-restricted.xml#installing-ibm-cloud-restricted">IBM Cloud®</a></p></li>
<li><p><a href="../installing/installing_ibm_z/preparing-to-install-on-ibm-z.xml#preparing-to-install-on-ibm-z">IBM Z® and IBM® LinuxONE</a></p></li>
<li><p><a href="../installing/installing_ibm_power/installing-restricted-networks-ibm-power.xml#installing-restricted-networks-ibm-power">IBM Power®</a></p></li>
<li><p><a href="../installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.xml#installing-restricted-networks-bare-metal">bare metal</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

Install a cluster in an existing network
| Learn about installing in a restricted network | Optional additional resources |
|----|----|
| If you use an existing Virtual Private Cloud (VPC) in [Amazon Web Services (AWS)](../installing/installing_aws/ipi/installing-aws-vpc.md#installing-aws-vpc) or [Google Cloud](../installing/installing_gcp/installing-gcp-vpc.md#installing-gcp-vpc) or an existing [VNet](../installing/installing_azure/ipi/installing-azure-vnet.md#installing-azure-vnet) on Microsoft Azure, you can install a cluster | [Installing a cluster on Google Cloud into a shared VPC](../installing/installing_gcp/installing-gcp-shared-vpc.md#installation-gcp-shared-vpc-prerequisites_installing-gcp-shared-vpc) |

Cluster administration
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Learn about OpenShift Container Platform cluster activities</th>
<th style="text-align: left;">Optional additional resources</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><a href="../architecture/architecture.xml#architecture-overview-architecture">Understand OpenShift Container Platform management</a></p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../machine_management/index.xml#machine-api-overview_overview-of-machine-management">Machine API</a></p></li>
<li><p><a href="../architecture/control-plane.xml#operators-overview_control-plane">Operators</a></p></li>
<li><p>* <a href="../etcd/etcd-overview.xml#etc-overview">etcd</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../installing/overview/cluster-capabilities.xml#enabling-cluster-capabilities_cluster-capabilities">Enable cluster capabilities</a></p></td>
<td style="text-align: left;"><p><a href="../installing/overview/cluster-capabilities.xml#explanation_of_capabilities_cluster-capabilities">Optional cluster capabilities in OpenShift Container Platform 4.17</a></p></td>
</tr>
</tbody>
</table>

Managing cluster components
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Learn about managing cluster components</th>
<th style="text-align: left;">Optional additional resources</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Manage <a href="../machine_management/index.xml#machine-mgmt-intro-managing-compute_overview-of-machine-management">compute</a> and <a href="../machine_management/index.xml#machine-mgmt-intro-managing-control-plane_overview-of-machine-management">control plane</a> machines with machine sets</p></td>
<td style="text-align: left;"><p><a href="../machine_management/deploying-machine-health-checks.xml#deploying-machine-health-checks">Deploy machine health checks</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../machine_management/applying-autoscaling.xml#applying-autoscaling">Apply autoscaling to an OpenShift Container Platform cluster</a></p></td>
<td style="text-align: left;"><p><a href="../nodes/pods/nodes-pods-priority.xml#nodes-pods-priority">Including pod priority in pod scheduling decisions</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../registry/index.xml#registry-overview">Manage container registries</a></p></td>
<td style="text-align: left;"><p><a href="https://access.redhat.com/documentation/en-us/red_hat_quay/">Red Hat Quay</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../authentication/understanding-authentication.xml#understanding-authentication">Manage users and groups</a></p></td>
<td style="text-align: left;"><p><a href="../authentication/impersonating-system-admin.xml#impersonating-system-admin">Impersonating the system:admin user</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../authentication/understanding-authentication.xml#understanding-authentication">Manage authentication</a></p></td>
<td style="text-align: left;"><p><a href="../authentication/understanding-identity-provider.xml#supported-identity-providers_understanding-identity-provider">Supported identity providers</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Manage <a href="../security/certificates/replacing-default-ingress-certificate.xml#replacing-default-ingress">Ingress</a>, <a href="../security/certificates/api-server.xml#api-server-certificates">API server</a>, and <a href="../security/certificates/service-serving-certificate.xml#add-service-serving">Service</a> certificates</p></td>
<td style="text-align: left;"><p><a href="../networking/network_security/network-policy-apis.xml#network-policy-apis">Network security</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../networking/networking_overview/understanding-networking.xml#understanding-networking">Manage networking</a></p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../networking/networking_operators/cluster-network-operator.xml#nw-cluster-network-operator_cluster-network-operator">Cluster Network Operator</a></p></li>
<li><p><a href="../networking/multiple_networks/understanding-multiple-networks.xml#understanding-multiple-networks">Multiple network interfaces</a></p></li>
<li><p><a href="../networking/network_security/network_policy/about-network-policy.xml#about-network-policy">Network policy</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../operators/understanding/olm-understanding-software-catalog.xml#olm-understanding-software-catalog">Manage Operators</a></p></td>
<td style="text-align: left;"><p><a href="../operators/user/olm-creating-apps-from-installed-operators.xml#olm-creating-apps-from-installed-operators">Creating applications from installed Operators</a></p></td>
</tr>
</tbody>
</table>

<!-- -->

Changing cluster components
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Learn more about changing cluster components</th>
<th style="text-align: left;">Optional additional resources</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><a href="../updating/understanding_updates/intro-to-updates.xml#intro-to-updates">Introduction to OpenShift updates</a></p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../updating/updating_a_cluster/updating-cluster-web-console.xml#updating-cluster-web-console">Updating a cluster using the web console</a></p></li>
<li><p><a href="../updating/updating_a_cluster/updating-cluster-cli.xml#updating-cluster-cli">Updating using the CLI</a></p></li>
<li><p><a href="../disconnected/updating/index.xml#about-disconnected-updates">Using the OpenShift Update Service in a disconnected environment</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../operators/understanding/crds/crd-extending-api-with-crds.xml#crd-extending-api-with-crds">Use custom resource definitions (CRDs) to modify the cluster</a></p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../operators/understanding/crds/crd-extending-api-with-crds.xml#crd-creating-custom-resources-definition_crd-extending-api-with-crds">Create a CRD</a></p></li>
<li><p><a href="../operators/understanding/crds/crd-managing-resources-from-crds.xml#crd-managing-resources-from-crds">Manage resources from CRDs</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../applications/quotas/quotas-setting-per-project.xml#quotas-setting-per-project">Set resource quotas</a></p></td>
<td style="text-align: left;"><p><a href="../applications/quotas/quotas-setting-across-multiple-projects.xml#quotas-setting-across-multiple-projects">Resource quotas across multiple projects</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../applications/pruning-objects.xml#pruning-objects">Prune and reclaim resources</a></p></td>
<td style="text-align: left;"><p><a href="../cicd/builds/advanced-build-operations.xml#builds-build-pruning-advanced-build-operations">Performing advanced builds</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../scalability_and_performance/recommended-performance-scale-practices/recommended-infrastructure-practices.xml#scaling-cluster-monitoring-operator">Scale</a> and <a href="../scalability_and_performance/using-node-tuning-operator.xml#using-node-tuning-operator">tune</a> clusters</p></td>
<td style="text-align: left;"><p><a href="../scalability_and_performance/index.xml#scalability-and-performance-overview">OpenShift Container Platform scalability and performance</a></p></td>
</tr>
</tbody>
</table>

Observe a cluster
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Learn about OpenShift Container Platform</th>
<th style="text-align: left;">Optional additional resources</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><a href="https://docs.redhat.com/en/documentation/red_hat_openshift_distributed_tracing_platform/latest/html/release_notes_for_the_distributed_tracing_platform/distr-tracing-rn">Release notes for the Red Hat OpenShift Distributed Tracing Platform</a></p></td>
<td style="text-align: left;"><p><a href="https://docs.redhat.com/en/documentation/red_hat_openshift_distributed_tracing_platform/latest">Red Hat OpenShift Distributed Tracing Platform</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://docs.redhat.com/en/documentation/red_hat_build_of_opentelemetry/latest/html/installing_red_hat_build_of_opentelemetry/install-otel">Red Hat build of OpenTelemetry</a></p></td>
<td style="text-align: left;"><p><a href="https://docs.redhat.com/en/documentation/red_hat_build_of_opentelemetry/latest/html/receiving_telemetry_data/otel-receiving-telemetry-data">Receiving telemetry data from multiple clusters</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../observability/network_observability/network-observability-overview.xml#network-observability-overview">About Network Observability</a></p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../observability/network_observability/metrics-alerts-dashboards.xml#metrics-alerts-dashboards_metrics-alerts-dashboards">Using metrics with dashboards and alerts</a></p></li>
<li><p><a href="../observability/network_observability/observing-network-traffic.xml#network-observability-trafficflow_nw-observe-network-traffic">Observing the network traffic from the Traffic flows view</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/about_monitoring/about-ocp-monitoring">About OpenShift Container Platform monitoring</a></p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../support/remote_health_monitoring/about-remote-health-monitoring.xml#about-remote-health-monitoring_about-remote-health-monitoring">Remote health monitoring</a></p></li>
<li><p><a href="https://docs.redhat.com/en/documentation/power_monitoring_for_red_hat_openshift/latest/html/about_power_monitoring/about-power-monitoring">Power monitoring for Red Hat OpenShift (Technology Preview)</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

Storage activities
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Learn about OpenShift Container Platform</th>
<th style="text-align: left;">Optional additional resources</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><a href="../storage/index.xml#storage-types">Storage types</a></p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../storage/understanding-persistent-storage.xml#understanding-persistent-storage">Persistent storage</a></p></li>
<li><p><a href="../storage/understanding-ephemeral-storage.xml#understanding-ephemeral-storage">Ephemeral storage</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

Application Site Reliability Engineer (App SRE)
| Learn about OpenShift Container Platform | Optional additional resources |
|----|----|
| [Building applications overview](../applications/index.md#building-applications-overview) | [Projects](../applications/projects/working-with-projects.md#working-with-projects) |
| [Operators](../operators/understanding/olm-what-operators-are.md#olm-what-operators-are) | [Cluster Operator reference](../operators/operator-reference.md#cluster-operator-reference) |

Developing applications
OpenShift Container Platform is a platform for developing and deploying containerized applications. Read the following OpenShift Container Platform documentation, so that you can better understand OpenShift Container Platform functions:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Learn about application development in OpenShift Container Platform</th>
<th style="text-align: left;">Optional additional resources</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><a href="https://developers.redhat.com/products/openshift/getting-started#assembly-field-sections-13455">Getting started with OpenShift for developers (interactive tutorial)</a></p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../architecture/understanding-development.xml#understanding-development">Understanding OpenShift Container Platform development</a></p></li>
<li><p><a href="../applications/projects/working-with-projects.xml#working-with-projects">Working with projects</a></p></li>
<li><p><a href="../applications/deployments/what-deployments-are.xml#what-deployments-are">Create deployments</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://developers.redhat.com/">Red Hat Developers site</a></p></td>
<td style="text-align: left;"><p><a href="../cicd/builds/understanding-image-builds.xml#understanding-image-builds">Understanding image builds</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://developers.redhat.com/products/openshift-dev-spaces/overview">Red Hat OpenShift Dev Spaces (formerly Red Hat CodeReady Workspaces)</a></p></td>
<td style="text-align: left;"><p><a href="../operators/understanding/olm-what-operators-are.xml#olm-what-operators-are">Operators</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../openshift_images/index.xml#overview-of-images">Create container images</a></p></td>
<td style="text-align: left;"><p><a href="../openshift_images/managing_images/managing-images-overview.xml#managing-images-overview">Managing images overview</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://odo.dev/docs/introduction/"><code>odo</code></a></p></td>
<td style="text-align: left;"><p><a href="../cli_reference/odo-important-update.xml#odo-important_update">Developer-focused CLI</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../applications/odc-viewing-application-composition-using-topology-view.xml#odc-viewing-application-topology_viewing-application-composition-using-topology-view">Viewing application composition using the Topology view</a></p></td>
<td style="text-align: left;"><p><a href="../applications/odc-exporting-applications.xml#odc-exporting-applications">Exporting applications</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://docs.openshift.com/pipelines/1.15/about/understanding-openshift-pipelines.html">Understanding OpenShift Pipelines</a></p></td>
<td style="text-align: left;"><p><a href="https://docs.openshift.com/pipelines/latest/create/creating-applications-with-cicd-pipelines.html">Create CI/CD Pipelines</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="https://docs.openshift.com/gitops/latest/declarative_clusterconfig/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.html">Configuring an OpenShift cluster by deploying an application with cluster configurations</a></p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../nodes/scheduling/nodes-scheduler-taints-tolerations.xml#nodes-scheduler-taints-tolerations">Controlling pod placement using node taints</a></p></li>
<li><p><a href="../machine_management/creating-infrastructure-machinesets.xml#creating-infrastructure-machinesets">Creating infrastructure machine sets</a></p></li>
</ul></td>
</tr>
</tbody>
</table>

Hosted control planes
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Learn about hosted control planes</th>
<th style="text-align: left;">Optional additional resources</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><a href="../hosted_control_planes/index.xml#hosted-control-planes-overview">Hosted control planes overview</a></p></td>
<td style="text-align: left;"><p><a href="../hosted_control_planes/index.xml#hosted-control-planes-version-support_hcp-overview">Versioning for hosted control planes</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Preparing to deploy</p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../hosted_control_planes/hcp-prepare/hcp-requirements.xml#hcp-requirements">Requirements for hosted control planes</a></p></li>
<li><p><a href="../hosted_control_planes/hcp-prepare/hcp-sizing-guidance.xml#hcp-sizing-guidance">Sizing guidance for hosted control planes</a></p></li>
<li><p><a href="../hosted_control_planes/hcp-prepare/hcp-override-resource-util.xml#hcp-override-resource-util">Overriding resource utilization measurements</a></p></li>
<li><p><a href="../hosted_control_planes/hcp-prepare/hcp-cli.xml#hcp-cli">Installing the hosted control planes command-line interface</a></p></li>
<li><p><a href="../hosted_control_planes/hcp-prepare/hcp-distribute-workloads.xml#hcp-distribute-workloads">Distributing hosted cluster workloads</a></p></li>
<li><p><a href="../hosted_control_planes/hcp-prepare/hcp-enable-disable.xml#hcp-enable-disable">Enabling or disabling the hosted control planes feature</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Deploying hosted control planes</p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../hosted_control_planes/hcp-deploy/hcp-deploy-virt.xml#hcp-deploy-virt">Deploying hosted control planes on OpenShift Virtualization</a></p></li>
<li><p><a href="../hosted_control_planes/hcp-deploy/hcp-deploy-aws.xml#hcp-deploy-aws">Deploying hosted control planes on AWS</a></p></li>
<li><p><a href="../hosted_control_planes/hcp-deploy/hcp-deploy-bm.xml#hcp-deploy-bm">Deploying hosted control planes on bare metal</a></p></li>
<li><p><a href="../hosted_control_planes/hcp-deploy/hcp-deploy-non-bm.xml#hcp-deploy-non-bm">Deploying hosted control planes on non-bare-metal agent machines</a></p></li>
<li><p><a href="../hosted_control_planes/hcp-deploy/hcp-deploy-ibmz.xml#hcp-deploy-ibmz">Deploying hosted control planes on IBM Z</a></p></li>
<li><p><a href="../hosted_control_planes/hcp-deploy/hcp-deploy-ibm-power.xml#hcp-deploy-ibm-power">Deploying hosted control planes on IBM Power</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Deploying hosted control planes in a disconnected environment</p></td>
<td style="text-align: left;"><ul>
<li><p><a href="../hosted_control_planes/hcp-disconnected/hcp-deploy-dc-bm.xml#hcp-deploy-dc-bm">Deploying hosted control planes on bare metal in a disconnected environment</a></p></li>
<li><p><a href="../hosted_control_planes/hcp-disconnected/hcp-deploy-dc-virt.xml#hcp-deploy-dc-virt">Deploying hosted control planes on OpenShift Virtualization in a disconnected environment</a></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><a href="../hosted_control_planes/hcp-troubleshooting.xml#hcp-troubleshooting">Troubleshooting hosted control planes</a></p></td>
<td style="text-align: left;"><p><a href="../hosted_control_planes/hcp-troubleshooting.xml#hosted-control-planes-troubleshooting_hcp-troubleshooting">Gathering information to troubleshoot hosted control planes</a></p></td>
</tr>
</tbody>
</table>
