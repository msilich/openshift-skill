> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/networking/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="networking"></a>

# Networking

Learn about network requirements for both the hub cluster and the managed cluster.

- [Hub cluster network configuration](networking.md#hub-network-config)

- [Managed cluster network configuration](networking.md#managed-network-config)

- [Advanced network configuration](networking.md#adv-network-config)

- [Submariner multicluster networking and service discovery](networking.md#submariner)

<a id="hub-network-config"></a>

## Hub cluster network configuration

**Important:** The trusted CA bundle is available in the Red Hat Advanced Cluster Management namespace, but that enhancement requires changes to your network. The trusted CA bundle ConfigMap uses the default name of `trusted-ca-bundle`. You can change this name by providing it to the operator in an environment variable named `TRUSTED_CA_BUNDLE`. See [Configuring the cluster-wide proxy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/configuring_network_settings/enable-cluster-wide-proxy) in the *Networking* section of Red Hat OpenShift Container Platform for more information.

You can refer to the configuration for your hub cluster network.

| Direction | Protocol | Connection | Port (if specified) | Source address | Destination address |
|----|----|----|----|----|----|
| Outbound to the managed cluster | HTTPS | The `klusterlet-addon-workmgr` service running on the managed cluster dynamically retrieves logs from the search console for the pods | 443 | None | IP address to access managed cluster route |
| Outbound to the managed cluster | HTTPS | Kubernetes API server of the managed cluster that is provisioned during installation to install the klusterlet | 6443 | None | IP of Kubernetes managed cluster API server |
| Outbound to the channel source | HTTPS | The channel source, including GitHub, Object Store, and Helm repository, which is only required when you are using Application lifecycle, OpenShift GitOps, or Argo CD to connect | 443 | None | IP of the channel source |
| Inbound from the managed cluster | HTTPS | Managed cluster to push metrics and alerts that are gathered only for managed clusters that are running on a supported OpenShift Container Platform version | 443 | None | IP address to hub cluster access route |
| Inbound from the managed cluster | HTTPS | Kubernetes API Server of hub cluster that is watched for changes from the managed cluster | 6443 | None | IP address of hub cluster Kubernetes API Server |
| Outbound to the ObjectStore | HTTPS | Sends observability metric data for long term storage when the Cluster Backup Operator is running | 443 | None | IP address of ObjectStore |
| Outbound to the image repository | HTTPS | Access images for OpenShift Container Platform and Red Hat Advanced Cluster Management | 443 | None | IP address of image repository |

Hub cluster network configuration table {#hub-network-table}

<a id="managed-network-config"></a>

## Managed cluster network configuration

You can refer to the configuration for your managed cluster network.

| Direction | Protocol | Connection | Port (if specified) | Source address | Destination address |
|----|----|----|----|----|----|
| Inbound from the hub cluster | HTTPS | Sending of logs dynamically from the search console for the pods of the managed cluster, uses the `klusterlet-addon-workmgr` service that is running on the managed cluster | 443 | None | IP address to access managed cluster route |
| Inbound from the hub cluster | HTTPS | Kubernetes API server of the managed cluster that is provisioned during installation to install the klusterlet | 6443 | None | IP of Kubernetes managed cluster API server |
| Outbound to the image repository | HTTPS | Access images for OpenShift Container Platform and Red Hat Advanced Cluster Management | 443 | None | IP address of image repository |
| Outbound to the hub cluster | HTTPS | Managed cluster to push metrics and alerts that are gathered only for managed clusters that are running on a supported OpenShift Container Platform version | 443 | None | IP address to hub cluster access route |
| Outbound to the hub cluster | HTTPS | Watches the Kubernetes API server of the hub cluster for changes | 6443 | None | IP address of hub cluster Kubernetes API Server |
| Outbound to the channel source | HTTPS | The channel source, including GitHub, Object Store, and Helm repository, which is only required when you are using Application lifecycle, OpenShift GitOps, or Argo CD to connect | 443 | None | IP of the channel source |

Managed cluster network configuration table {#managed-network-table}

<a id="adv-network-config"></a>

## Advanced network configuration

Review the following advanced networking requirements for infrastructure operators, Submariner, Hive, application deployment, and namespace connections.

When you are installing bare metal managed clusters with the Infrastructure Operator, see [Network configuration](clusters.md#mce-network-configuration) in the multicluster engine for Kubernetes operator documentation for additional networking requirements.

Clusters that are using Submariner require three open ports. The following table shows which ports you might use:

| Direction | Protocol | Connection | Port (if specified) |
|----|----|----|----|
| Outbound and inbound | UDP | Each of the managed clusters | 4800 |
| Outbound and inbound | UDP | Each of the managed clusters | 4500, 500, and any other ports that are used for IPSec traffic on the gateway nodes |
| Inbound | TCP | Each of the managed clusters | 8080 |

Submariner networking requirements table

When you are installing bare metal managed clusters with the Hive Operator, which includes using central infrastructure management, you must configure a layer 2 or layer 3 port connection between the hub cluster and the `libvirt` provisioning host. This connection to the provisioning host is required during the creation of a base metal cluster with Hive. See the following table for more information:

| Direction | Protocol | Connection | Port (if specified) |
|----|----|----|----|
| Hub cluster outbound and inbound to the `libvirt` provisioning host | IP | Connects the hub cluster, where the Hive operator is installed, to the `libvirt` provisioning host that serves as a bootstrap when creating the bare metal cluster |  |

Additional networking requirements for Hive table

**Note:** These requirements only apply when installing, and are not required when upgrading clusters that were installed with Infrastructure Operator.

- Application deployment network requirements

  In general, the application deployment communication is one way from a managed cluster to the hub cluster. The connection uses `kubeconfig`, which is configured by the agent on the managed cluster. The application deployment on the managed cluster needs to access the following namespaces on the hub cluster:

  - The namespace of the channel resource

  - The namespace of the managed cluster

- Application lifecycle connections

  - The namespace `open-cluster-management` needs to access the console API on port 4000.

  - The namespace `open-cluster-management` needs to expose the Application UI on port 3001.

- Application lifecycle backend components (pods)

  On the hub cluster, all of the application lifecycle pods are installed in the `open-cluster-management` namespace, including the following pods:

  - multicluster-operators-hub-subscription

  - multicluster-operators-standalone-subscription

  - multicluster-operators-channel

  - multicluster-operators-application

  - multicluster-integrations

  - As a result of these pods being in the `open-cluster-management` namespace:

  - The namespace `open-cluster-management` needs to access the Kube API on port 6443.

  - On the managed cluster, only the `klusterlet-addon-appmgr` application lifecycle pod is installed in the `open-cluster-management-agent-addon` namespace:

  - The namespace `open-cluster-management-agent-addon` needs to access the Kube API on port 6443.

- Governance and risk:

  On the hub cluster, the following access is required:

  - The namespace `open-cluster-management` needs to access the Kube API on port 6443.

  - The namespace `open-cluster-management` needs to access the OpenShift DNS on port 5353.

  - On the managed cluster, the following access is required:

  - The namespace `open-cluster-management-addon` needs to access the Kube API on port 6443.

<a id="submariner"></a>

## Submariner multicluster networking and service discovery

Submariner is an open source tool that you can use with Red Hat Advanced Cluster Management for Kubernetes to provide direct networking and service discovery between two or more managed clusters in your environment, either on-premises or in the cloud. Submariner is compatible with Multi-Cluster Services API ([Kubernetes Enhancements Proposal \#1645](https://github.com/kubernetes/enhancements/tree/master/keps/sig-multicluster/1645-multi-cluster-services-api)). For more information about Submariner, see the [Submariner site](https://submariner.io/).

Submariner is not supported with all of the infrastructure providers that Red Hat Advanced Cluster Management can manage. Refer to the [Red Hat Advanced Cluster Management Support Matrix](https://access.redhat.com/articles/7142376) for more details about the support levels of infrastructure providers, including which providers support [automated console deployments](networking.md#deploying-submariner-console) or require [manual deployment](networking.md#submariner-manual-deployment). See the following topics to learn more about how to use Submariner:

- [Deploying Submariner on disconnected clusters](networking.md#deploying-submariner-disconnected)

- [Preparing to configure Submariner](networking.md#preparing-to-configure-submariner)

- [Submariner ports table](networking.md#submariner-ports)

- [Configuring Submariner for an existing VPC](networking.md#subm-vpc-config)

- [Globalnet](networking.md#submariner-globalnet)

- [Configuring Submariner for a Red Hat OpenShift Container Platform network](networking.md#configuring-submariner-rhos)

- [subctl command utility](networking.md#subctl-command-utility)

- [Deploying Submariner by using the console](networking.md#deploying-submariner-console)

- [Submariner manual deployment](networking.md#submariner-manual-deployment)

- [Customizing Submariner deployments](networking.md#customizing-submariner)

- [Service discovery for Submariner](networking.md#service-discovery-submariner)

- [Uninstalling Submariner](networking.md#uninstalling-submariner)

<a id="deploying-submariner-disconnected"></a>

### Deploying Submariner on disconnected clusters

Deploying Submariner on disconnected clusters can help with security concerns by reducing the risk of external attacks on clusters. To deploy Submariner with Red Hat Advanced Cluster Management for Kubernetes on disconnected clusters, you must first complete the steps outlined in [Installing in disconnected network environments](get_started.md#install-on-disconnected-networks).

After completing the steps in [Installing in disconnected network environments](get_started.md#install-on-disconnected-networks), configure Submariner during the installation to support deployment on disconnected clusters.

<div>

<div class="title">

Procedure

</div>

1.  Mirror the `Submariner Operator bundle` image in the local registry before you deploy Submariner on disconnected clusters.

2.  Choose the Submariner Operator version that is compatible with your Red Hat Advanced Cluster Management version. For instance, use `0.20.0` for Red Hat Advanced Cluster Management version 2.13.

3.  Customize `catalogSource` names. By default, `submariner-addon` searches for a `catalogSource` with the name `redhat-operators`. When you use a `catalogSource` with a different name, you must update the value of the `SubmarinerConfig.Spec.subscriptionConfig.Source` parameter in the `SubmarinerConfig` associated with your managed cluster with the custom name of the `catalogSource`.

4.  Enable `airGappedDeployment` in `SubmarinerConfig`.When installing `submariner-addon` on a managed cluster from the Red Hat Advanced Cluster Management for Kubernetes console, you can select the **Disconnected cluster** option so that Submariner does not make API queries to external servers.

    **Note:** If you are installing Submariner by using the APIs, you must set the `airGappedDeployment` parameter to `true` in the `SubmarinerConfig` associated with your managed cluster.

</div>

<a id="preparing-to-configure-submariner"></a>

### Preparing to configure Submariner

Red Hat Advanced Cluster Management for Kubernetes provides Submariner as an add-on for your hub cluster. To prepare for configuring Submariner, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Ensure that you have a credential to access the hub cluster with `cluster-admin` permissions.

2.  Configure IP connectivity between the gateway nodes. When connecting two clusters, at least one of the clusters must be accessible to the gateway node by using its public or private IP address designated to the gateway node. See *Submariner NAT Traversal* for more information.

3.  If you are using OVN Kubernetes, ensure that your clusters are on a supported version of OpenShift Container Platform.

4.  If your OpenShift Container Platform clusters use OpenShift SDN CNI, configure the firewall across all nodes in each of the managed clusters to allow 4800/UDP in both directions.

5.  Configure the firewall to allow 4500/UDP and 4490/UDP on the gateway nodes for establishing tunnels between the managed clusters.

6.  For OpenShift Container Platform ARM deployments, use the `c6g.large` `instanceType` or any other available instance type.

7.  If the gateway nodes are directly reachable over their private IPs without any NAT in between, configure the firewall to allow the ESP protocol on the gateway nodes.

    **Notes:**

    - This update is configured automatically when your clusters are deployed in an Amazon Web Services, Google Cloud Platform, Microsoft Azure, or Red Hat OpenStack environment. You must manually configure it for clusters on other environments and for the firewalls that protect private clouds.

    - If you do not want to allow the ESP protocol in the firewall, you can force Submariner to encapsulate IPSec traffic in UDP by editing `SubmarinerConfig` and adding `forceUDPEncaps: true` to the `spec` section.

8.  For Red Hat OpenStack Services on OpenShift clusters, select a unique UDP port other than 4500 for IPsec NAT-T. The 4500 port is used by OpenStack services on OpenShift internally.

9.  **Technology Preview:** If Open Virtual Network Internet Protocol Security is enabled, enable `IPSecCertAuthMode` in the `SubmarinerConfig` resource. You can only change this setting during installation.

10. Ensure that the `managedcluster` name follows the DNS label standard as defined in RFC 1123 and meets the following requirements:

    - Contain 63 characters or fewer

    - Contain only lowercase alphanumeric characters or '-'

    - Start with an alphanumeric character

    - End with an alphanumeric character

</div>

<div>

<div class="title">

Next steps

</div>

1.  See the [Submariner ports table](networking.md#submariner-ports) for information about the ports that Submariner uses for communication between clusters.

2.  Go to [Configuring Submariner for an existing VPC](networking.md#subm-vpc-config).

3.  See the [Globalnet](networking.md#submariner-globalnet) documentation.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Submariner documentation](https://submariner.io/)

- [Submariner NAT Traversal](https://submariner.io/operations/nat-traversal)

- [Submariner prerequisites documentation](https://submariner.io/getting-started/#prerequisites)

- [Globalnet controller](https://submariner.io/getting-started/architecture/globalnet/)

</div>

<a id="submariner-ports"></a>

### Submariner ports table

View the following table to see the Submariner ports that you must enable:

| Name               | Default value | Customizable | Optional or required |
|--------------------|---------------|--------------|----------------------|
| IPsec NATT         | 4500/UDP      | Yes          | Required             |
| VXLAN              | 4800/UDP      | No           | Required             |
| NAT discovery port | 4490/UDP      | No           | Required             |

<a id="subm-vpc-config"></a>

### Configuring Submariner for an existing VPC

If you installed your cluster into an existing Amazon Virtual Private Cloud (VPC) on Amazon Web Services (AWS), you must complete the following steps to configure Submariner:

<div>

<div class="title">

Procedure

</div>

1.  Open and edit the `SubmarinerConfig` file by running the following command. Replace values where needed:

    ``` bash
    oc edit submarinerconfig -n <managed-cluster-ns> submariner
    ```

2.  Add the following annotations in the `metadata` field. Replace values where needed. All the IDs you need to add are alphanumeric:

    ``` yaml
    annotations:
      submariner.io/control-plane-sg-id: <control-plane-group-id>
      submariner.io/subnet-id-list: <subnet-id-list>
      submariner.io/vpc-id: <custom-vpc-id>
      submariner.io/worker-sg-id: <worker-security-group-id>
    ```

    - Replace with your control plane security group ID. Typically, you can find the ID from the control plane security group that has a name similar to `<infra-id>-master-sg>`.

    - Replace with a comma-separated list of public subnet IDs in your custom VPC.

    - Replace with your custom VPC ID.

    - Replace with your worker security group ID. Typically, you can find the ID from the worker security group that has a name similar to `<infra-id>-worker-sg`.

</div>

<a id="submariner-globalnet"></a>

### Globalnet

Globalnet is a Submariner add-on feature that allows you to connect clusters with overlapping Classless Inter-Domain Routings (CIDRs), without changing the CIDRs on existing clusters. Globalnet is a cluster set-wide configuration that you can select when you add the first managed cluster to a cluster set.

If you enable Globalnet, every managed cluster receives a global CIDR from the virtual Global Private Network, which is used to facilitate inter-cluster communication.

**Important:** You must enable Globalnet when clusters in a cluster set might have overlapping CIDRs.

The `ClusterAdmin` can enable Globalnet in the console by selecting the option **Enable Globalnet** when enabling the Submariner add-on for clusters in the cluster set. If you want to disable Globalnet after enabling it, you must first remove all managed clusters from your cluster set.

See the following topics to configure Globalnet:

- [Enabling Globalnet by creating the *submariner-broker* object](networking.md#submariner-globalnet-enable)

- [Configuring the number of global IPs](networking.md#subm-globalnet-numperip)

<a id="submariner-globalnet-enable"></a>

### Enabling Globalnet by creating the *submariner-broker* object

When using the Red Hat Advanced Cluster Management APIs, the `ClusterAdmin` can enable Globalnet by creating a `submariner-broker` object in the `<ManagedClusterSet>-broker` namespace.

The `ClusterAdmin` role has the required permissions to create the `submariner-broker` object in the broker namespace. The `ManagedClusterSetAdmin` role, which is sometimes created to act as a proxy administrator for the cluster set, does not have the required permissions.

To provide the required permissions, the `ClusterAdmin` must associate the role permissions for the `access-to-brokers-submariner-crd` to the `ManagedClusterSetAdmin` user.

Complete the following steps to enable Globalnet by creating the `submariner-broker` object:

<div>

<div class="title">

Procedure

</div>

1.  Retrieve the `<broker-namespace>` by running the following command:

    ``` bash
    oc get ManagedClusterSet <cluster-set-name> -o jsonpath="{.metadata.annotations['cluster\.open-cluster-management\.io/submariner-broker-ns']}"
    ```

2.  Create a `submariner-broker` object that specifies the Globalnet configuration by creating a YAML file named `submariner-broker`. Add content that resembles the following lines to the YAML file:

    ``` yaml
    apiVersion: submariner.io/v1alpha1
    kind: Broker
    metadata:
      name: submariner-broker
      namespace: broker-namespace
    spec:
      globalnetEnabled: true-or-false
    ```

    - The name must be `submariner-broker`.

    - Replace `broker-namespace` with the name of your broker namespace.

    - Replace `true-or-false` with `true` to enable Globalnet.

3.  Apply the file by running the following command:

    ``` bash
    oc apply -f submariner-broker.yaml
    ```

</div>

<a id="subm-globalnet-numperip"></a>

### Configuring the number of global IPs

You can assign a configurable number of global IPs by changing the value of the `numberOfIPs` field in the `ClusterGlobalEgressIP` resource. The default value is 8.

<div>

<div class="title">

Procedure

</div>

1.  Create or edit a `ClusterGlobalEgressIP` resource that is similar to the following example:

    ``` yaml
    apiVersion: submariner.io/v1
    kind: ClusterGlobalEgressIP
    metadata:
      name: cluster-egress.submariner.io
    spec:
      numberOfIPs: 8
    ```

</div>

<a id="configuring-submariner-rhos"></a>

### Configuring Submariner for a Red Hat OpenShift Container Platform network

If you installed your cluster into an OpenShift Container Platform network, add the `subnet-names` to the `annotations` field of the `SubmarinerConfig` resource. Add the subnet names as a comma-separated list. This configuration allows Submariner to discover the subnets in your OpenShift Container Platform network.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Open the `SubmarinerConfig` resource for editing. Run the following command. Replace `<managed-cluster-ns>` with the namespace of your managed cluster:

    ``` bash
    oc edit submarinerconfig -n <managed-cluster-ns> submariner
    ```

2.  Add the `subnet-names` for the OpenShift Container Platform network to the `annotations` field. Your `SubmarinerConfig` resource might resemble the following example:

    ``` yaml
    annotations:
      submariner.io/subnet-names: subnet-name1,subnet-name2, subnet-name3
    ```

</div>

<a id="subctl-command-utility"></a>

### subctl command utility

The `subctl` utility is distributed as a container image. See the [Red Hat Ecosystem Catalog `subctl` page](https://catalog.redhat.com/software/containers/rhacm2/subctl-rhel9/65bd43fc6a96e2c53f3159b5) for available image versions.

**Note:** `registry.redhat.io` requires authentication. If not already configured, run `podman login registry.redhat.io` first.

Replace `<version>` in the following examples with the version tag that matches your Submariner deployment, for example `v0.22`.

See the following topics to learn more about installing and using `subctl`:

- [Running subctl in a container](networking.md#run-subctl-in-container)

- [Extracting the subctl binary](networking.md#extract-subctl-binary)

- [subctl commands](networking.md#subctl-commands)

<a id="run-subctl-in-container"></a>

### Running subctl in a container

You can run `subctl` directly from the container image.

<div>

<div class="title">

Procedure

</div>

1.  Run `subctl` from the container image by using a command that resembles the following example. Replace `<version>` with the version tag that matches your Submariner deployment, for example `v0.22`. Replace `<subcommand>` with any `subctl` command, for example `show all` or `diagnose all`:

    ``` bash
    podman run --rm -v ~/.kube:/.kube:z -e KUBECONFIG=/.kube/config \
      registry.redhat.io/rhacm2/subctl-rhel9:<version> <subcommand>
    ```

</div>

<a id="extract-subctl-binary"></a>

### Extracting the subctl binary

If you prefer a local binary, you can extract `subctl` from the container image. The extracted binary requires Red Hat Enterprise Linux 9 or later.

<div>

<div class="title">

Procedure

</div>

1.  Extract `subctl` from the container image by running the following command. Replace `<version>` with the version tag that matches your Submariner deployment, for example `v0.22`:

    ``` bash
    podman cp "$(podman create registry.redhat.io/rhacm2/subctl-rhel9:<version>):/usr/local/bin/subctl" subctl
    ```

    **Notes:** \* Make sure that the `subctl` and Submariner versions match. \* For disconnected environments only, make sure to mirror the `submariner-nettest` image.

</div>

<a id="subctl-commands"></a>

### subctl commands

After adding the utility to your path, view the following table for a brief description of the available commands:

|  |  |
|----|----|
| [`export service`](https://submariner.io/operations/deployment/subctl/#export-service) | Creates a `ServiceExport` resource for the specified service, which enables other clusters in the Submariner deployment to discover the corresponding service. |
| [`unexport service`](https://submariner.io/operations/deployment/subctl/#unexport-service) | Removes the `ServiceExport` resource for the specified service, which prevents other clusters in the Submariner deployment from discovering the corresponding service. |
| [`show`](https://submariner.io/operations/deployment/subctl/#show) | Provides information about Submariner resources. |
| [`verify`](https://submariner.io/operations/deployment/subctl/#verify) | Verifies connectivity, service discovery, and other Submariner features when Submariner is configured across a pair of clusters. |
| [`benchmark`](https://submariner.io/operations/deployment/subctl/#benchmark) | Benchmarks throughput and latency across a pair of clusters that are enabled with Submariner or within a single cluster. |
| [`diagnose`](https://submariner.io/operations/deployment/subctl/#diagnose) | Runs checks to identify issues that prevent the Submariner deployment from working correctly. |
| [`gather`](https://submariner.io/operations/deployment/subctl/#gather) | Collects information from the clusters to help troubleshoot a Submariner deployment. |
| [`version`](https://submariner.io/operations/deployment/subctl/#version) | Displays the version details of the `subctl` binary tool. |

**Note**: The Red Hat build of `subctl` only includes the commands that are relevant to Red Hat Advanced Cluster Management for Kubernetes. For more information about the `subctl` utility and its commands, see [`subctl` in the Submariner documentation](https://submariner.io/operations/deployment/subctl/).

<a id="deploying-submariner-console"></a>

### Deploying Submariner by using the console

Before you deploy Submariner with Red Hat Advanced Cluster Management for Kubernetes, you must prepare the clusters on the hosting environment. You can use the `SubmarinerConfig` API or the Red Hat Advanced Cluster Management for Kubernetes console to automatically prepare Red Hat OpenShift Container Platform clusters on the following providers:

- Amazon Web Services

- Bare Metal with hosted control planes (Technology Preview)

- Google Cloud Platform

- IBM Power Systems Virtual Server

- Red Hat OpenShift on IBM Cloud (Technology Preview)

- Red Hat OpenStack Platform

- Red Hat OpenShift Service on AWS with hosted control planes (Technology Preview)

- Red Hat OpenShift Virtualization (Technology Preview)

- Red Hat OpenShift Virtualization with hosted control planes (Technology Preview)

- Microsoft Azure

- VMware vSphere

- **Important:** Submariner deployments on VMware and vSphere environments that have a VMware NSX enabled are not supported by Red Hat Advanced Cluster Management.

To deploy Submariner on other providers, follow the instructions in [Submariner manual deployment](networking.md#submariner-manual-deployment).

<div>

<div class="title">

Prerequisites

</div>

- You must install the [Calico API server](https://docs.tigera.io/calico/latest/operations/install-apiserver#install-the-api-server) on your cluster if you are using Red Hat OpenShift on IBM Cloud. Alternatively, you can manually create the IP pools required for cross-cluster communication by following the [CALICO CNI](https://submariner.io/operations/deployment/calico/) topic in the Submariner upstream documentation.

</div>

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  From the console, select **Infrastructure** \> **Clusters**.

2.  On the *Clusters* page, select the *Cluster sets* tab. The clusters that you want enable with Submariner must be in the same cluster set.

3.  If the clusters on which you want to deploy Submariner are already in the same cluster set, skip to step 5.

4.  If the clusters on which you want to deploy Submariner are not in the same cluster set, create a cluster set for them by completing the following steps:

    1.  Select **Create cluster set**.

    2.  Name the cluster set, and select **Create**.

    3.  Select **Manage resource assignments** to assign clusters to the cluster set.

    4.  Select the managed clusters that you want to connect with Submariner to add them to the cluster set.

    5.  Select **Review** to view and confirm the clusters that you selected.

    6.  Select **Save** to save the cluster set, and view the resulting cluster set page.

5.  On the cluster set page, select the *Submariner add-ons* tab.

6.  Select **Install Submariner add-ons**.

7.  Select the clusters on which you want to deploy Submariner.

8.  See the fields in the following table and enter the required information in the *Install Submariner add-ons* editor:

    | Field | Notes |
    |----|----|
    | `AWS Access Key ID` | Only visible when you import an AWS cluster. |
    | `AWS Secret Access Key` | Only visible when you import an AWS cluster. |
    | `Base domain resource group name` | Only visible when you import an Azure cluster. |
    | `Client ID` | Only visible when you import an Azure cluster. |
    | `Client secret` | Only visible when you import an Azure cluster. |
    | `Subscription ID` | Only visible when you import an Azure cluster. |
    | `Tenant ID` | Only visible when you import an Azure cluster. |
    | `Google Cloud Platform service account JSON key` | Only visible when you import a Google Cloud Platform cluster. |
    | `Instance type` | The instance type of the gateway node that is created on the managed cluster. |
    | `IPsec NAT-T port` | The default value for the IPsec NAT traversal port is port `4500`. If your managed cluster environment is VMware vSphere, ensure that this port is opened on your firewall. |
    | `Gateway count` | The number of gateway nodes to be deployed on the managed cluster. For AWS, GCP, Azure, and OpenStack clusters, dedicated Gateway nodes are deployed. For VWware clusters, existing worker nodes are tagged as gateway nodes. The default value is `1`. If the value is greater than 1, the Submariner gateway High Availability (HA) is automatically enabled. |
    | `Cable driver` | The Submariner gateway cable engine component that maintains the cross-cluster tunnels. The default value is `Libreswan IPsec`. |
    | `Disconnected cluster` | If enabled, tells Submariner to not access any external servers for public IP resolution. |
    | Globalnet CIDR | Only visible when the Globalnet configuration is selected on the cluster set. The Globalnet CIDR to be used for the managed cluster. If left blank, a CIDR is allocated from the cluster set pool. |

9.  Select **Next** at the end of the editor to move to the editor for the next cluster, and complete the editor for each of the remaining clusters that you selected.

10. Verify your configuration for each managed cluster.

11. Click **Install** to deploy Submariner on the selected managed clusters. It might take several minutes for the installation and configuration to complete. You can check the Submariner status in the list on the *Submariner add-ons* tab. See the following status indicators:

    - `Connection status` indicates how many Submariner connections are established on the managed cluster.

    - `Agent status` indicates whether Submariner is successfully deployed on the managed cluster. The console might report a status of `Degraded` until it is installed and configured.

    - `Gateway nodes labeled` indicates the number of gateway nodes on the managed cluster.

</div>

<a id="submariner-manual-deployment"></a>

### Submariner manual deployment

If your cluster is hosted on a provider that does not support automatic Submariner deployment, see the following sections to prepare the infrastructure manually. Each provider has unique steps for preparation, so make sure to select the correct provider.

**Note:** By default, Submariner uses IP security (IPsec) to establish secure tunnels between the clusters on the gateway nodes. You can either use the default IPsec NATT port, or you can [specify a different port](networking.md#customizing-submariner) that you configure. When you prepare or deploy clusters without specifying an IPsec NATT port, 4500/UDP is used for the connections. See *Customizing Submariner deployments* in the additional resources section to learn more.

**Notes:**

- Before you deploy Submariner with Red Hat Advanced Cluster Management for Kubernetes, you must prepare the clusters on the hosting environment for the connection. See [Deploying Submariner by using the console](networking.md#deploying-submariner-console) to learn how to automatically deploy Submariner on supported clusters by using the console.

- If you are using VMware vSphere or bare metal with hosted control planes, Submariner automatically labels one or more existing worker nodes as gateways during installation. If you want to specify certain nodes as gateways, apply the `submariner.io/gateway=true` label to your nodes.

See the following topics to prepare your environment and deploy Submariner manually:

- [Preparing bare metal for Submariner](networking.md#preparing-bare-metal-submariner)

- [Preparing Microsoft Azure Red Hat OpenShift for Submariner by using the CLI](networking.md#preparing-aro-submariner-cli)

- [Deploying Microsoft Azure Red Hat OpenShift for Submariner by using the API](networking.md#deploy-aro-submariner-api)

- [Preparing Red Hat OpenShift Service on AWS for Submariner by using the CLI](networking.md#preparing-rosa-submariner-cli)

- [Deploying Red Hat OpenShift Service on AWS for Submariner by using the API](networking.md#deploy-rosa-submariner-api)

- [Deploying Red Hat OpenShift on IBM Cloud for Submariner by using the API (Technology Preview)](networking.md#deploy-ocp-ibm-cloud-subm)

- [Deploying Submariner with the ManagedClusterAddOn API](networking.md#deploying-submariner-mcaddon-api)

<div>

<div class="title">

Additional resources

</div>

- [Customizing Submariner deployments](networking.md#customizing-submariner)

</div>

<a id="preparing-bare-metal-submariner"></a>

### Preparing bare metal for Submariner

To prepare bare metal clusters for deploying Submariner, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Ensure that the firewall allows inbound/outbound traffic for external clients on the 4500/UDP and 4490/UDP ports for the Gateway nodes. Also, if the cluster is deployed with OpenShiftSDN CNI, allow inbound/outbound UDP/4800 traffic within the local cluster nodes.

2.  Customize and apply YAML content that is similar to the following example:

    ``` yaml
    apiVersion: submarineraddon.open-cluster-management.io/v1alpha1
    kind: SubmarinerConfig
    metadata:
        name: submariner
        namespace: <managed-cluster-namespace>
    spec:
        gatewayConfig:
          gateways: 1
    ```

    - The name must be `submariner`, as shown in the example.

    - Replace with the name of your managed cluster.

    - This configuration [labels one of the worker nodes as the Submariner gateway](networking.md#number-gateway-nodes) on your bare metal cluster.

3.  Identify the Gateway node configured by Submariner and enable firewall configurations to allow the IPsec NATT (UDP/4500) and NATDiscovery (UDP/4490) ports for external traffic.

</div>

<a id="preparing-aro-submariner-cli"></a>

### Preparing Microsoft Azure Red Hat OpenShift for Submariner by using the CLI

The Microsoft Azure Red Hat OpenShift service combines various tools and resources that you can use to simplify the process of building container-based applications. To prepare Azure Red Hat OpenShift clusters for deploying Submariner by using the command line interface, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Install the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).

2.  From the Azure CLI, run the following command to install the extension. Replace `path-to-extension` with the path to where you downloaded the `.whl` extension file:

    ``` bash
    az extension add --upgrade -s <path-to-extension>
    ```

3.  Run the following command to verify that the CLI extension is being used:

    ``` bash
    az extension list
    ```

    If the extension is being used, the output might resemble the following example:

        "experimental": false,
        "extensionType": "whl",
        "name": "aro",
        "path": "<path-to-extension>",
        "preview": true,
        "version": "1.0.x"

4.  From the Azure CLI, register the preview feature by running the following command:

    ``` bash
    az feature registration create --namespace Microsoft.RedHatOpenShift --name AdminKubeconfig
    ```

5.  Retrieve the administrator `kubeconfig` by running the following command:

    ``` bash
    az aro get-admin-kubeconfig -g <resource group> -n <cluster resource name>
    ```

    **Note:** The `az aro` command saves the `kubeconfig` to the local directory and uses the name `kubeconfig`. To use it, set the environment variable `KUBECONFIG` to match the path of the file. See the following example:

    ``` bash
    export KUBECONFIG=<path-to-kubeconfig>
    oc get nodes
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Cluster import introduction](clusters.md#import-intro)

</div>

<a id="deploy-aro-submariner-api"></a>

### Deploying Microsoft Azure Red Hat OpenShift for Submariner by using the API

The following configuration labels one of the worker nodes as the Submariner gateway on your Azure Red Hat OpenShift cluster.

<div>

<div class="title">

Procedure

</div>

1.  To deploy Azure Red Hat OpenShift clusters for Submariner by using the API, customize and apply YAML content that is similar to the following example:

    ``` yaml
    apiVersion: submarineraddon.open-cluster-management.io/v1alpha1
    kind: SubmarinerConfig
    metadata:
        name: submariner
        namespace: <managed-cluster-namespace>
    spec:
        loadBalancerEnable: true
    ```

    - The name must be `submariner`, as shown in the example.

    - Replace with the name of your managed cluster.

</div>

<a id="preparing-rosa-submariner-cli"></a>

### Preparing Red Hat OpenShift Service on AWS for Submariner by using the CLI

Red Hat OpenShift Service on AWS provides a stable and flexible platform for application development and modernization. To prepare OpenShift Service on AWS clusters for deploying Submariner, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Log in to OpenShift Service on AWS by running the following commands:

    ``` bash
    rosa login
    oc login <rosa-cluster-url>:6443 --username cluster-admin --password <password>
    ```

2.  Create a `kubeconfig` for your OpenShift Service on AWS cluster by running the following command:

    ``` bash
    oc config view --flatten=true > rosa_kube/kubeconfig
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Cluster import introduction](clusters.md#import-intro)

</div>

<a id="deploy-rosa-submariner-api"></a>

### Deploying Red Hat OpenShift Service on AWS for Submariner by using the API

Use the following configuration to deploy Red HatOpenShift Service on AWS clusters for Submariner by using the API.

<div>

<div class="title">

Procedure

</div>

1.  Customize and apply YAML content that is similar to the following example:

    ``` yaml
    apiVersion: submarineraddon.open-cluster-management.io/v1alpha1
    kind: SubmarinerConfig
    metadata:
        name: submariner
        namespace: <managed-cluster-namespace>
    spec:
        loadBalancerEnable: true
    ```

    - The name must be `submariner`, as shown in the example.

    - Replace with the name of your managed cluster.

</div>

<a id="deploy-ocp-ibm-cloud-subm"></a>

### Deploying Red Hat OpenShift on IBM Cloud for Submariner by using the API (Technology Preview)

Use the following configuration to label one of the worker nodes as the Submariner gateway on your Red Hat OpenShift on IBM Cloud cluster.

<div>

<div class="title">

Procedure

</div>

1.  Customize and apply YAML content that is similar to the following example:

    ``` yaml
    apiVersion: submarineraddon.open-cluster-management.io/v1alpha1
    kind: SubmarinerConfig
    metadata:
        name: submariner
        namespace: <managed-cluster-namespace>
    spec:
        gatewayConfig:
          gateways: <num-of-gateways>
        loadBalancerEnable: true
    ```

    - The name must be `submariner`, as shown in the example.

    - Replace with the name of your managed cluster.

    - Set the value higher than `1` if you need Submariner gateway with High Availability (HA).

</div>

<a id="deploying-submariner-mcaddon-api"></a>

### Deploying Submariner with the ManagedClusterAddOn API

After manually preparing your selected hosting environment, you can deploy Submariner with the `ManagedClusterAddOn` API by completing the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Create a `ManagedClusterSet` resource on the hub cluster by using the instructions provided in the [*ManagedClusterSet* overview](clusters.md#creating-a-managedclusterset) documentation. Make sure your entry for the `ManagedClusterSet` resembles the following content:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta2
    kind: ManagedClusterSet
    metadata:
      name: <managed-cluster-set-name>
    ```

    - Replace `managed-cluster-set-name` with a name for the `ManagedClusterSet` that you are creating.

    - **Important:** The maximum character length of a Kubernetes namespace is 63 characters. The maximum character length you can use for the `<managed-cluster-set-name>` is 56 characters. If the character length of `<managed-cluster-set-name>` exceeds 56 characters, the `<managed-cluster-set-name>` is cut off from the head.

    - After the `ManagedClusterSet` is created, the `submariner-addon` creates a namespace called `<managed-cluster-set-name>-broker` and deploys the Submariner broker to it.

2.  Create the `Broker` configuration on the hub cluster in the `<managed-cluster-set-name>-broker` namespace by customizing and applying YAML content that is similar to the following example:

    ``` yaml
    apiVersion: submariner.io/v1alpha1
    kind: Broker
    metadata:
         name: submariner-broker
         namespace: <managed-cluster-set-name>-broker
         labels:
             cluster.open-cluster-management.io/backup: submariner
    spec:
         globalnetEnabled: <true-or-false>
    ```

    - Replace `managed-cluster-set-name` with the name of the managed cluster.

    - Set the value of `globalnetEnabled` to `true` if you want to enable Submariner Globalnet in the `ManagedClusterSet`.

3.  Add one managed cluster to the `ManagedClusterSet` by running the following command:

    ``` bash
    oc label managedclusters <managed-cluster-name> "cluster.open-cluster-management.io/clusterset=<managed-cluster-set-name>" --overwrite
    ```

    - Replace `<managed-cluster-name>` with the name of the managed cluster that you want to add to the `ManagedClusterSet`.

    - Replace `<managed-cluster-set-name>` with the name of the `ManagedClusterSet` to which you want to add the managed cluster.

4.  Customize and apply YAML content that is similar to the following example:

    ``` yaml
    apiVersion: submarineraddon.open-cluster-management.io/v1alpha1
    kind: SubmarinerConfig
    metadata:
        name: submariner
        namespace: <managed-cluster-namespace>
    spec:{}
    ```

    - Replace `managed-cluster-namespace` with the namespace of your managed cluster.

    - **Note:** The name of the `SubmarinerConfig` must be `submariner`, as shown in the example.

5.  Deploy Submariner on the managed cluster by customizing and applying YAML content that is similar to the following example:

    ``` yaml
    apiVersion: addon.open-cluster-management.io/v1alpha1
    kind: ManagedClusterAddOn
    metadata:
         name: submariner
         namespace: <managed-cluster-name>
    spec:
         installNamespace: submariner-operator
    ```

    - Replace `managed-cluster-name` with the name of the managed cluster that you want to use with Submariner.

    - The `installNamespace` field in the spec of the `ManagedClusterAddOn` is the namespace on the managed cluster where it installs Submariner. Currently, Submariner must be installed in the `submariner-operator` namespace.

    - After the `ManagedClusterAddOn` is created, the `submariner-addon` deploys Submariner to the `submariner-operator` namespace on the managed cluster. You can view the deployment status of Submariner from the status of this `ManagedClusterAddOn`.

    - **Notes:**

    - The name of `ManagedClusterAddOn` must be `submariner`.

    - The `spec.installNamespace` field is deprecated.

6.  Repeat steps three, four, and five for all of the managed clusters that you want to enable Submariner on.

7.  After Submariner is deployed on the managed cluster, you can verify the Submariner deployment status by checking the status of submariner `ManagedClusterAddOn` by running the following command:

    ``` bash
    oc -n <managed-cluster-name> get managedclusteraddons submariner -oyaml
    ```

    - Replace `managed-cluster-name` with the name of the managed cluster.

    - In the status of the Submariner `ManagedClusterAddOn`, three conditions indicate the deployment status of Submariner:

    - `SubmarinerGatewayNodesLabeled` condition indicates whether there are labeled Submariner gateway nodes on the managed cluster.

    - `SubmarinerAgentDegraded` condition indicates whether the Submariner is successfully deployed on the managed cluster.

    - `SubmarinerConnectionDegraded` condition indicates how many connections are established on the managed cluster with Submariner.

</div>

<a id="customizing-submariner"></a>

### Customizing Submariner deployments

You can customize some of the settings of your Submariner deployments, including your Network Address Translation-Traversal (NATT) port, number of gateway nodes, and instance type of your gateway nodes. These customizations are consistent across all of the providers.

See the following topics to customize your Submariner deployment:

- [NATT port](networking.md#natt-port-custom)

- [Number of gateway nodes](networking.md#number-gateway-nodes)

- [Instance types of gateway nodes](networking.md#instance-type-gateway-nodes)

- [Cable driver](networking.md#cable-driver)

- [Customized Submariner subscription](networking.md#customized-submariner-subscription)

<a id="natt-port-custom"></a>

### NATT port

You can customize the NATT port for your provider environment.

<div>

<div class="title">

Procedure

</div>

1.  Customize and apply the following YAML content for your provider environment:

    ``` yaml
    apiVersion: submarineraddon.open-cluster-management.io/v1alpha1
    kind: SubmarinerConfig
    metadata:
        name: submariner
        namespace: <managed-cluster-namespace>
    spec:
        credentialsSecret:
          name: <managed-cluster-name>-<provider>-creds
        IPSecNATTPort: <NATTPort>
    ```

    - Replace `managed-cluster-namespace` with the namespace of your managed cluster.

    - Replace `managed-cluster-name` with the name of your managed cluster

      - AWS: Replace `provider` with `aws`. The value of `<managed-cluster-name>-aws-creds` is your AWS credential secret name, which you can find in the cluster namespace of your hub cluster.

      - GCP: Replace `provider` with `gcp`. The value of `<managed-cluster-name>-gcp-creds` is your Google Cloud Platform credential secret name, which you can find in the cluster namespace of your hub cluster.

      - OpenStack: Replace `provider` with `osp`. The value of `<managed-cluster-name>-osp-creds` is your Red Hat OpenStack Platform credential secret name, which you can find in the cluster namespace of your hub cluster.

      - Azure: Replace `provider` with `azure`. The value of `<managed-cluster-name>-azure-creds` is your Microsoft Azure credential secret name, which you can find in the cluster namespace of your hub cluster.

    - Replace `managed-cluster-namespace` with the namespace of your managed cluster.

    - Replace `managed-cluster-name` with the name of your managed cluster. The value of `managed-cluster-name-gcp-creds` is your Google Cloud Platform credential secret name, which you can find in the cluster namespace of your hub cluster.

    - Replace `NATTPort` with the NATT port that you want to use.

      **Note:** The name of the `SubmarinerConfig` must be `submariner`, as shown in the example.

</div>

<a id="number-gateway-nodes"></a>

### Number of gateway nodes

You can customize the number of your gateway nodes by editing the `SubmarinerConfig` resource.

<div>

<div class="title">

Procedure

</div>

1.  Customize and apply YAML content that is similar to the following example:

    ``` yaml
    apiVersion: submarineraddon.open-cluster-management.io/v1alpha1
    kind: SubmarinerConfig
    metadata:
       name: submariner
       namespace: <managed-cluster-namespace>
    spec:
       credentialsSecret:
         name: <managed-cluster-name>-<provider>-creds
      gatewayConfig:
          gateways: <gateways>
    ```

    - Replace `managed-cluster-namespace` with the namespace of your managed cluster.

    - Replace `managed-cluster-name` with the name of your managed cluster.

      - AWS: Replace `provider` with `aws`. The value of `<managed-cluster-name>-aws-creds` is your AWS credential secret name, which you can find in the cluster namespace of your hub cluster.

      - GCP: Replace `provider` with `gcp`. The value of `<managed-cluster-name>-gcp-creds` is your Google Cloud Platform credential secret name, which you can find in the cluster namespace of your hub cluster.

      - OpenStack: Replace `provider` with `osp`. The value of `<managed-cluster-name>-osp-creds` is your Red Hat OpenStack Platform credential secret name, which you can find in the cluster namespace of your hub cluster.

      - Azure: Replace `provider` with `azure`. The value of `<managed-cluster-name>-azure-creds` is your Microsoft Azure credential secret name, which you can find in the cluster namespace of your hub cluster.

    - Replace `gateways` with the number of gateways that you want to use. If the value is greater than 1, the Submariner gateway automatically enables high availability.

      **Note:** The name of the `SubmarinerConfig` must be `submariner`, as shown in the example.

</div>

<a id="instance-type-gateway-nodes"></a>

### Instance types of gateway nodes

You can customize the instance type of your gateway node by editing the `SubmarinerConfig` resource.

<div>

<div class="title">

Procedure

</div>

1.  Customize and apply YAML content that is similar to the following example:

    ``` yaml
    apiVersion: submarineraddon.open-cluster-management.io/v1alpha1
    kind: SubmarinerConfig
    metadata:
       name: submariner
       namespace: <managed-cluster-namespace>
    spec:
       credentialsSecret:
         name: <managed-cluster-name>-<provider>-creds
      gatewayConfig:
          instanceType: <instance-type>
    ```

    - Replace `managed-cluster-namespace` with the namespace of your managed cluster.

    - Replace `managed-cluster-name` with the name of your managed cluster.

      - AWS: Replace `provider` with `aws`. The value of `<managed-cluster-name>-aws-creds` is your AWS credential secret name, which you can find in the cluster namespace of your hub cluster.

      - GCP: Replace `provider` with `gcp`. The value of `<managed-cluster-name>-gcp-creds` is your Google Cloud Platform credential secret name, which you can find in the cluster namespace of your hub cluster.

      - OpenStack: Replace `provider` with `osp`. The value of `<managed-cluster-name>-osp-creds` is your Red Hat OpenStack Platform credential secret name, which you can find in the cluster namespace of your hub cluster.

      - Azure: Replace `provider` with `azure`. The value of `<managed-cluster-name>-azure-creds` is your Microsoft Azure credential secret name, which you can find in the cluster namespace of your hub cluster.

    - Replace `instance-type` with the AWS instance type that you want to use.

      **Note:** The name of the `SubmarinerConfig` must be `submariner`, as shown in the example.

</div>

<a id="cable-driver"></a>

### Cable driver

The Submariner Gateway Engine component creates secure tunnels to other clusters. The cable driver component maintains the tunnels by using a pluggable architecture in the Gateway Engine component. You can use the Libreswan or VXLAN implementations for the `cableDriver` configuration of the cable engine component. See the following example:

``` yaml
apiVersion: submarineraddon.open-cluster-management.io/v1alpha1
kind: SubmarinerConfig
metadata:
   name: submariner
   namespace: <managed-cluster-namespace>
spec:
   cableDriver: vxlan
   credentialsSecret:
     name: <managed-cluster-name>-<provider>-creds
```

**Best practice:** Do not use the VXLAN cable driver on public networks. The VXLAN cable driver is unencrypted. Only use VXLAN to avoid unnecessary double encryption on private networks. For example, some on-premise environments might handle the tunnel’s encryption with a dedicated line-level hardware device.

<a id="customized-submariner-subscription"></a>

### Customized Submariner subscription

The Submariner add-on automatically configures a subscription for Submariner; this ensures that the version of Submariner appropriate for the installed version of Red Hat Advanced Cluster Management is installed and kept up-to-date. If you want to change this behavior, or if you want to manually control Submariner upgrades, you can customize the Submariner subscription.

When you use a customized Submariner subscription, you must complete the following fields:

- **Source:** The catalog source to use for the Submariner subscription. For example, `redhat-operators`.

- **source Namespace:** The namespace of the catalog source. For example, `openshift-marketplace`.

- **Channel:** The channel to follow for the subscription. For example, for Red Hat Advanced Cluster Management 2.12, enter `stable-0.19`.

- **Starting CSV (Optional):** The initial `ClusterServiceVersion`.

- **Install Plan Approval:** The decision to manually or automatically approve install plans.

**Note:** If you want to manually approve the install plan, you must use a customized Submariner subscription.

<a id="service-discovery-submariner"></a>

### Service discovery for Submariner

After Submariner is deployed into the same environment as your managed clusters, the routes are configured for secure IP routing between the pod and services across the clusters in the managed cluster set.

See the following topics to manage service discovery:

- [Enabling service discovery for Submariner](networking.md#enabling-service-discovery-submariner)

- [Disabling service discovery for Submariner](networking.md#disabling-service-discovery-submariner)

<a id="enabling-service-discovery-submariner"></a>

### Enabling service discovery for Submariner

To make a service from a cluster visible and discoverable to other clusters in the managed cluster set, you must create a `ServiceExport` object. After a service is exported with a `ServiceExport` object, you can access the service by the following format: `<service>.<namespace>.svc.clusterset.local`. If multiple clusters export a service with the same name, and from the same namespace, they are recognized by other clusters as a single logical service.

This example uses the `nginx` service in the `default` namespace, but you can discover any Kubernetes `ClusterIP` service or headless service:

<div>

<div class="title">

Procedure

</div>

1.  Apply an instance of the `nginx` service on a managed cluster that is in the `ManagedClusterSet` by entering the following commands:

    ``` bash
    oc -n default create deployment nginx --image=nginxinc/nginx-unprivileged:stable-alpine
    oc -n default expose deployment nginx --port=8080
    ```

2.  Export the service by creating a `ServiceExport` entry by entering a command with the `subctl` tool that is similar to the following command:

    ``` bash
    subctl export service --namespace <service-namespace> <service-name>
    ```

    - Replace `service-namespace` with the name of the namespace where the service is located. In this example, it is `default`.

    - Replace `service-name` with the name of the service that you are exporting. In this example, it is `nginx`.

    - [`export`](https://submariner.io/operations/deployment/subctl/#export)

3.  Run the following command from a different managed cluster to confirm that it can access the `nginx` service:

    ``` bash
    oc -n default run --generator=run-pod/v1 tmp-shell --rm -i --tty --image quay.io/submariner/nettest -- /bin/bash curl nginx.default.svc.clusterset.local:8080
    ```

</div>

<a id="disabling-service-discovery-submariner"></a>

### Disabling service discovery for Submariner

To disable a service from being exported to other clusters complete the following procedure.

<div>

<div class="title">

Procedure

</div>

1.  Enter a command similar to the following example for `nginx`:

    ``` bash
    subctl unexport service --namespace <service-namespace> <service-name>
    ```

2.  Replace `service-namespace` with the name of the namespace where the service is located.

3.  Replace `service-name` with the name of the service that you are exporting.

</div>

<div>

<div class="title">

Additional resources

</div>

- [`unexport`](https://submariner.io/operations/deployment/subctl/#unexport)

</div>

<a id="uninstalling-submariner"></a>

### Uninstalling Submariner

You can uninstall the Submariner components from your clusters using the Red Hat Advanced Cluster Management for Kubernetes console or the command line. For Submariner versions earlier than 0.12, additional steps are needed to completely remove all data plane components. The Submariner uninstall is idempotent, so you can repeat steps without any issues.

<div>

<div class="title">

Procedure

</div>

1.  To uninstall Submariner by using the console, see [Uninstalling Submariner by using the console](networking.md#uninstalling-submariner-console).

2.  To uninstall Submariner by using the CLI, see [Uninstalling Submariner by using the CLI](networking.md#uninstalling-submariner-cli).

3.  To verify Submariner resource removal, see [Verifying Submariner resource removal](networking.md#verifying-subm-resource-removal).

4.  When uninstalling versions of Submariner that are earlier than version 0.12, complete steps 5-8 in the [Manual Uninstall](https://submariner.io/operations/cleanup/#manual-uninstall/) section in the Submariner documentation. After completing those steps, your Submariner components are removed from the cluster.

5.  **Important:** Verify that all of the cloud resources are removed from the cloud provider to avoid additional charges by your cloud provider. See [Verifying Submariner resource removal](networking.md#verifying-subm-resource-removal) for more information.

</div>

<a id="uninstalling-submariner-console"></a>

### Uninstalling Submariner by using the console

If the version of Submariner that you are removing is earlier than version 0.12, continue. If the Submariner version is 0.12 or later, Submariner is removed.

**Important:** Verify that all of the cloud resources are removed from the cloud provider to avoid additional charges by your cloud provider. See [Verifying Submariner resource removal](networking.md#verifying-subm-resource-removal) for more information.

To uninstall Submariner from a cluster by using the console, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  From the console navigation, select **Infrastructure** \> **Clusters**, and select the *Cluster sets* tab.

2.  Select the cluster set that contains the clusters from which you want to remove the Submariner components.

3.  Select the **Submariner Add-ons** tab to view the clusters in the cluster set that have Submariner deployed.

4.  In the *Actions* menu for the cluster that you want to uninstall Submariner, select **Uninstall Add-on**.

5.  In the *Actions* menu for the cluster that you want to uninstall Submariner, select **Delete cluster sets**.

6.  Repeat those steps for other clusters from which you are removing Submariner. You can remove the Submariner add-on from multiple clusters in the same cluster set by selecting multiple clusters and clicking **Actions**. Select **Uninstall Submariner add-ons**.

</div>

<a id="uninstalling-submariner-cli"></a>

### Uninstalling Submariner by using the CLI

To uninstall Submariner by using the command line, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Remove the Submariner deployment for the cluster by running the following command. Replace `managed-cluster-namespace` with the namespace of your managed cluster:

    ``` bash
    oc -n <managed-cluster-namespace> delete managedclusteraddon submariner
    ```

2.  Remove the cloud resources of the cluster by running the following command. Replace `managed-cluster-namespace` with the namespace of your managed cluster:

    ``` bash
    oc -n <managed-cluster-namespace> delete submarinerconfig submariner
    ```

3.  Delete the cluster set to remove the broker details by running the following command. Replace `managedclusterset` with the name of your managed cluster set:

    ``` bash
    oc delete managedclusterset <managedclusterset>
    ```

4.  Verify that all of the cloud resources are removed from the cloud provider to avoid additional charges by your cloud provider. See [Verifying Submariner resource removal](networking.md#verifying-subm-resource-removal) for more information.

</div>

<a id="verifying-subm-resource-removal"></a>

### Verifying Submariner resource removal

After uninstalling Submariner, verify that all of the Submariner resources are removed from your clusters. If they remain on your clusters, some resources continue to collect charges from infrastructure providers.

Ensure that you have no additional Submariner resources on your cluster by completing the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to list any Submariner resources that remain on the cluster. Replace `CLUSTER_NAME` with the name of your cluster:

    ``` bash
    oc get cluster <CLUSTER_NAME> grep submariner
    ```

2.  Remove any resources on the list by entering the following command. Replace `RESOURCE_NAME` with the name of the Submariner resource that you want to remove and `CLUSTER_NAME` with the name of your cluster:

    ``` bash
    oc delete resource <RESOURCE_NAME> cluster <CLUSTER_NAME>
    ```

3.  Repeat steps 1-2 for each of the clusters until your search does not identify any resources.

</div>
