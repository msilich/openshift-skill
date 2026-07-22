<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As a cluster administrator, you can use cluster capabilities to enable or disable optional components before installation. Additionally, you can enable cluster capabilities at anytime after installation.

> [!NOTE]
> You cannot disable a cluster capability after it is enabled.

# Enabling cluster capabilities

If you are using an installation method that includes customizing your cluster by creating an `install-config.yaml` file, you can select which cluster capabilities you want to make available on the cluster.

> [!NOTE]
> If you customize your cluster by enabling or disabling specific cluster capabilities, you must manually maintain your `install-config.yaml` file. New OpenShift Container Platform updates might declare new capability handles for existing components, or introduce new components altogether. Users who customize their `install-config.yaml` file should consider periodically updating their `install-config.yaml` file as OpenShift Container Platform is updated.

You can use the following configuration parameters to select cluster capabilities:

``` yaml
capabilities:
  baselineCapabilitySet: v4.11
  additionalEnabledCapabilities:
  - CSISnapshot
  - Console
  - Storage
```

`capabilities.baselineCapabilitySet`
Specifies a baseline set of capabilities to install. Valid values are `None`, `vCurrent` and `v4.x`. If you select `None`, all optional capabilities are disabled. The default value is `vCurrent`, which enables all optional capabilities.

> [!NOTE]
> `v4.x` refers to any value up to and including the current cluster version. For example, valid values for a OpenShift Container Platform 4.12 cluster are `v4.11` and `v4.12`.

`capabilities.additionalEnabledCapabilities`
Specifies a list of capabilities to explicitly enable. These capabilities are enabled in addition to the capabilities specified in `baselineCapabilitySet`.

> [!NOTE]
> In this example, the default capability is set to `v4.11`. The `additionalEnabledCapabilities` field enables additional capabilities over the default `v4.11` capability set.

The following table describes the `baselineCapabilitySet` values.

| Value | Description |
|----|----|
| `vCurrent` | Specify this option when you want to automatically add new, default capabilities that are introduced in new releases. |
| `v4.11` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.11. By specifying `v4.11`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.11 are `baremetal`, `MachineAPI`, `marketplace`, and `openshift-samples`. |
| `v4.12` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.12. By specifying `v4.12`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.12 are `baremetal`, `MachineAPI`, `marketplace`, `openshift-samples`, `Console`, `Insights`, `Storage`, and `CSISnapshot`. |
| `v4.13` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.13. By specifying `v4.13`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.13 are `baremetal`, `MachineAPI`, `marketplace`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, and `NodeTuning`. |
| `v4.14` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.14. By specifying `v4.14`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.14 are `baremetal`, `MachineAPI`, `marketplace`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, and `DeploymentConfig`. |
| `v4.15` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.15. By specifying `v4.15`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.15 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, and `DeploymentConfig`. |
| `v4.16` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.16. By specifying `v4.16`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.16 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, `DeploymentConfig`, and `CloudControllerManager`. |
| `v4.17` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.17. By specifying `v4.17`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.17 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, `DeploymentConfig`, and `CloudControllerManager`. |
| `v4.18` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.18. By specifying `v4.18`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.18 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `OperatorLifecycleManagerV1`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, `DeploymentConfig`, and `CloudControllerManager`. |
| `None` | Specify when the other sets are too large, and you do not need any capabilities or want to fine-tune via `additionalEnabledCapabilities`. |

Cluster capabilities `baselineCapabilitySet` values description

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on AWS with customizations](../installing_aws/ipi/installing-aws-customizations.md#installing-aws-customizations)

- [Installing a cluster on Google Cloud with customizations](../installing_gcp/installing-gcp-customizations.md#installing-gcp-customizations)

</div>

# Optional cluster capabilities in OpenShift Container Platform 4.17

Currently, cluster Operators provide the features for these optional capabilities.

The following sections summarize the features provided by each capability and what functionality you lose if you disable a functionality.

<div>

<div class="title">

Additional resources

</div>

- [Cluster Operators reference](../../operators/operator-reference.md#cluster-operator-reference)

</div>

## Bare-metal capability

The Cluster Baremetal Operator provides the features for the `baremetal` capability.

The Cluster Baremetal Operator (CBO) deploys all the components necessary to take a bare-metal server to a fully functioning worker node ready to run OpenShift Container Platform compute nodes. The CBO ensures that the metal3 deployment, which consists of the Bare Metal Operator (BMO) and Ironic containers, runs on one of the control plane nodes within the OpenShift Container Platform cluster. The CBO also listens for OpenShift Container Platform updates to resources that it watches and takes appropriate action.

The bare-metal capability is required for deployments using installer-provisioned infrastructure. Disabling the bare-metal capability can result in unexpected problems with these deployments.

> [!IMPORTANT]
> If the bare-metal capability is disabled, the cluster cannot provision or manage bare-metal nodes. Only disable the capability if there are no `BareMetalHost` resources in your deployment. The `baremetal` capability depends on the `MachineAPI` capability. If you enable the `baremetal` capability, you must also enable `MachineAPI`.

> [!NOTE]
> Red Hat recommends that cluster administrators only disable the bare-metal capability during installations with user-provisioned infrastructure that do not have any `BareMetalHost` resources in the cluster.

<div>

<div class="title">

Additional resources

</div>

- [Deploying installer-provisioned clusters on bare metal](../installing_bare_metal/ipi/ipi-install-overview.md#ipi-install-overview)

- [Preparing for bare metal cluster installation](../installing_bare_metal/preparing-to-install-on-bare-metal.md#preparing-to-install-on-bare-metal)

- [Configuration using the Bare Metal Operator](../installing_bare_metal/bare-metal-postinstallation-configuration.md#bmo-config-using-bare-metal-operator_bare-metal-postinstallation-configuration)

</div>

## Build capability

The `Build` capability enables the `Build` API. The `Build` API manages the lifecycle of `Build` and `BuildConfig` objects.

> [!IMPORTANT]
> If you disable the `Build` capability, the following resources will not be available in the cluster:
>
> - `Build` and `BuildConfig` resources
>
> - The `builder` service account
>
> Disable the `Build` capability only if you do not require `Build` and `BuildConfig` resources or the `builder` service account in the cluster.

## Cloud controller manager capability

The Cloud Controller Manager Operator provides features for the `CloudControllerManager` capability.

> [!NOTE]
> Currently, disabling the `CloudControllerManager` capability is not supported on all platforms.

You can determine if your cluster supports disabling the `CloudControllerManager` capability by checking values in the installation configuration (`install-config.yaml`) file for your cluster.

In the `install-config.yaml` file, locate the `platform` parameter.

- If the value of the `platform` parameter is `Baremetal` or `None`, you can disable the `CloudControllerManager` capability on your cluster.

- If the value of the `platform` parameter is `External`, locate the `platform.external.cloudControllerManager` parameter. If the value of the `platform.external.cloudControllerManager` parameter is `None`, you can disable the `CloudControllerManager` capability on your cluster.

> [!IMPORTANT]
> If these parameters contain any other values than those listed, you cannot disable the `CloudControllerManager` capability on your cluster.

> [!NOTE]
> The status of this Operator is General Availability for Amazon Web Services (AWS), Google Cloud, IBM Cloud®, global Microsoft Azure, Microsoft Azure Stack Hub, Nutanix, Red Hat OpenStack Platform (RHOSP), and VMware vSphere.
>
> The Operator is available as a Technology Preview for IBM Power® Virtual Server.

The Cloud Controller Manager Operator manages and updates the cloud controller managers deployed on top of OpenShift Container Platform. The Operator is based on the Kubebuilder framework and `controller-runtime` libraries. You can install the Cloud Controller Manager Operator by using the Cluster Version Operator (CVO).

The Cloud Controller Manager Operator includes the following components:

- Operator

- Cloud configuration observer

By default, the Operator exposes Prometheus metrics through the `metrics` service.

<div>

<div class="title">

Additional resources

</div>

- [Technology Preview](https://access.redhat.com/support/offerings/techpreview)

- [`cluster-cloud-controller-manager-operator`](https://github.com/openshift/cluster-cloud-controller-manager-operator)

</div>

## Cloud credential capability

The Cloud Credential Operator provides features for the `CloudCredential` capability.

> [!NOTE]
> Currently, disabling the `CloudCredential` capability is only supported for bare-metal clusters.

The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). The CCO syncs on `CredentialsRequest` custom resources (CRs) to allow OpenShift Container Platform components to request cloud provider credentials with the specific permissions that are required for the cluster to run.

By setting different values for the `credentialsMode` parameter in the `install-config.yaml` file, the CCO can be configured to operate in several different modes. If no mode is specified, or the `credentialsMode` parameter is set to an empty string (`""`), the CCO operates in its default mode.

<div>

<div class="title">

Additional resources

</div>

- [About the Cloud Credential Operator](../../authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.md#about-cloud-credential-operator)

- [`openshift-cloud-credential-operator`](https://github.com/openshift/cloud-credential-operator)

</div>

## Cluster Image Registry capability

The Cluster Image Registry Operator provides features for the `ImageRegistry` capability.

The Cluster Image Registry Operator manages a singleton instance of the OpenShift image registry. It manages all configuration of the registry, including creating storage.

On initial start up, the Operator creates a default `image-registry` resource instance based on the configuration detected in the cluster. This indicates what cloud storage type to use based on the cloud provider.

If insufficient information is available to define a complete `image-registry` resource, then an incomplete resource is defined and the Operator updates the resource status with information about what is missing.

The Cluster Image Registry Operator runs in the `openshift-image-registry` namespace and it also manages the registry instance in that location. All configuration and workload resources for the registry reside in that namespace.

In order to integrate the image registry into the cluster’s user authentication and authorization system, an image pull secret is generated for each service account in the cluster.

> [!IMPORTANT]
> If you disable the `ImageRegistry` capability or if you disable the integrated OpenShift image registry in the Cluster Image Registry Operator’s configuration, the image pull secret is not generated for each service account.

If you disable the `ImageRegistry` capability, you can reduce the overall resource footprint of OpenShift Container Platform in Telco environments. Depending on your deployment, you can disable this component if you do not need it.

Project
See "cluster-image-registry-operator".

<div>

<div class="title">

Additional resources

</div>

- [Image Registry Operator in OpenShift Container Platform](../../registry/configuring-registry-operator.md#configuring-registry-operator)

- [Automatically generated secrets](../../nodes/pods/nodes-pods-secrets.md#auto-generated-sa-token-secrets_nodes-pods-secrets)

- [cluster-image-registry-operator](https://github.com/openshift/cluster-image-registry-operator)

</div>

## Cluster storage capability

The Cluster Storage Operator provides the features for the `Storage` capability.

The Cluster Storage Operator sets OpenShift Container Platform cluster-wide storage defaults. It ensures a default `storageclass` exists for OpenShift Container Platform clusters. It also installs Container Storage Interface (CSI) drivers which enable your cluster to use various storage backends.

> [!IMPORTANT]
> If the cluster storage capability is disabled, the cluster will not have a default `storageclass` or any CSI drivers. Users with administrator privileges can create a default `storageclass` and manually install CSI drivers if the cluster storage capability is disabled.

Notes
The storage class that the Operator creates can be made non-default by editing its annotation, but this storage class cannot be deleted as long as the Operator runs.

<div>

<div class="title">

Additional resources

</div>

- [cluster-storage-operator](https://github.com/openshift/cluster-storage-operator)

</div>

## Console capability

The Console Operator provides the features for the `Console` capability.

The Console Operator installs and maintains the OpenShift Container Platform web console on a cluster. The Console Operator is installed by default and automatically maintains a console.

<div>

<div class="title">

Additional resources

</div>

- [Web console overview](../../web_console/web-console-overview.md#web-console-overview)

- [console-operator](https://github.com/openshift/console-operator)

</div>

## CSI snapshot controller capability

The Cluster CSI Snapshot Controller Operator provides the features for the `CSISnapshot` capability.

The Cluster CSI Snapshot Controller Operator installs and maintains the CSI Snapshot Controller. The CSI Snapshot Controller is responsible for watching the `VolumeSnapshot` CRD objects and manages the creation and deletion lifecycle of volume snapshots.

<div>

<div class="title">

Additional resources

</div>

- [CSI volume snapshots](../../storage/container_storage_interface/persistent-storage-csi-snapshots.md#persistent-storage-csi-snapshots)

- [cluster-csi-snapshot-controller-operator](https://github.com/openshift/cluster-csi-snapshot-controller-operator)

</div>

## DeploymentConfig capability

The `DeploymentConfig` capability enables and manages the `DeploymentConfig` API.

> [!IMPORTANT]
> If you disable the `DeploymentConfig` capability, the following resources will not be available in the cluster:
>
> - `DeploymentConfig` resources
>
> - The `deployer` service account
>
> Disable the `DeploymentConfig` capability only if you do not require `DeploymentConfig` resources and the `deployer` service account in the cluster.

## Ingress Capability

The Ingress Operator provides the features for the `Ingress` capability.

The Ingress Operator configures and manages the OpenShift Container Platform router.

Project
`openshift-ingress-operator`

CRDs
- `clusteringresses.ingress.openshift.io`

  - Scope: Namespaced

  - CR: `clusteringresses`

  - Validation: No

Configuration objects
- Cluster config

  - Type Name: `clusteringresses.ingress.openshift.io`

  - Instance Name: `default`

  - View Command:

    ``` terminal
    $ oc get clusteringresses.ingress.openshift.io -n openshift-ingress-operator default -o yaml
    ```

Notes
The Ingress Operator sets up the router in the `openshift-ingress` project and creates the deployment for the router:

``` terminal
$ oc get deployment -n openshift-ingress
```

The Ingress Operator uses the `clusterNetwork[].cidr` from the `network/cluster` status to determine what mode (IPv4, IPv6, or dual stack) the managed Ingress Controller (router) should operate in. For example, if `clusterNetwork` contains only a v6 `cidr`, then the Ingress Controller operates in IPv6-only mode.

In the following example, Ingress Controllers managed by the Ingress Operator will run in IPv4-only mode because only one cluster network exists and the network is an IPv4 `cidr`:

``` terminal
$ oc get network/cluster -o jsonpath='{.status.clusterNetwork[*]}'
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
map[cidr:10.128.0.0/14 hostPrefix:23]
```

</div>

<div>

<div class="title">

Additional resources

</div>

- [openshift-ingress-operator](https://github.com/openshift/cluster-ingress-operator)

</div>

## Insights capability

The Insights Operator provides the features for the `Insights` capability.

The Insights Operator gathers OpenShift Container Platform configuration data and sends it to Red Hat. The data is used to produce proactive insights recommendations about potential issues that a cluster might be exposed to. These insights are communicated to cluster administrators through the Red Hat Lightspeed advisor service on [console.redhat.com](https://console.redhat.com/).

Notes
Insights Operator complements OpenShift Container Platform Telemetry.

<div>

<div class="title">

Additional resources

</div>

- [Using Insights Operator](../../support/remote_health_monitoring/using-insights-operator.md#using-insights-operator)

- [Red Hat Hybrid Cloud Console](https://console.redhat.com/)

- [insights-operator](https://github.com/openshift/insights-operator)

</div>

## Machine API capability

The `machine-api-operator`, `cluster-autoscaler-operator`, and `cluster-control-plane-machine-set-operator` Operators provide the features for the `MachineAPI` capability. You can disable this capability only if you install a cluster with user-provisioned infrastructure.

The Machine API capability is responsible for all machine configuration and management in the cluster. If you disable the Machine API capability during installation, you need to manage all machine-related tasks manually.

<div>

<div class="title">

Additional resources

</div>

- [Overview of machine management](../../machine_management/index.md#index)

- [Machine API Operator](../../operators/operator-reference.md#machine-api-operator_operator-reference)

- [Cluster Autoscaler Operator](../../operators/operator-reference.md#cluster-autoscaler-operator_operator-reference)

- [Control Plane Machine Set Operator](../../operators/operator-reference.md#control-plane-machine-set-operator_operator-reference)

</div>

## Marketplace capability

The Marketplace Operator provides the features for the `marketplace` capability.

The Marketplace Operator simplifies the process for bringing off-cluster Operators to your cluster by using a set of default Operator Lifecycle Manager (OLM) catalogs on the cluster. When the Marketplace Operator is installed, it creates the `openshift-marketplace` namespace. OLM ensures catalog sources installed in the `openshift-marketplace` namespace are available for all namespaces on the cluster.

If you disable the `marketplace` capability, the Marketplace Operator does not create the `openshift-marketplace` namespace. Catalog sources can still be configured and managed on the cluster manually, but OLM depends on the `openshift-marketplace` namespace in order to make catalogs available to all namespaces on the cluster. Users with elevated permissions to create namespaces prefixed with `openshift-`, such as system or cluster administrators, can manually create the `openshift-marketplace` namespace.

If you enable the `marketplace` capability, you can enable and disable individual catalogs by configuring the Marketplace Operator.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat-provided Operator catalogs](../../operators/understanding/olm-rh-catalogs.md#olm-rh-catalogs)

- [operator-marketplace](https://github.com/operator-framework/operator-marketplace)

</div>

## Node Tuning capability

The Node Tuning Operator provides features for the `NodeTuning` capability.

The Node Tuning Operator helps you manage node-level tuning by orchestrating the TuneD daemon and achieves low latency performance by using the Performance Profile controller. The majority of high-performance applications require some level of kernel tuning. The Node Tuning Operator provides a unified management interface to users of node-level sysctls and more flexibility to add custom tuning specified by user needs.

If you disable the NodeTuning capability, some default tuning settings will not be applied to the control-plane nodes. This might limit the scalability and performance of large clusters with over 900 nodes or 900 routes.

<div>

<div class="title">

Additional resources

</div>

- [Using the Node Tuning Operator](../../scalability_and_performance/using-node-tuning-operator.md#using-node-tuning-operator)

- [cluster-node-tuning-operator](https://github.com/openshift/cluster-node-tuning-operator)

</div>

## OpenShift samples capability

The Cluster Samples Operator provides the features for the `openshift-samples` capability.

The Cluster Samples Operator manages the sample image streams and templates stored in the `openshift` namespace.

On initial start up, the Operator creates the default samples configuration resource to initiate the creation of the image streams and templates. The configuration object is a cluster scoped object with the key `cluster` and type `configs.samples`.

The image streams are the Red Hat Enterprise Linux CoreOS (RHCOS)-based OpenShift Container Platform image streams pointing to images on `registry.redhat.io`. Similarly, the templates are those categorized as OpenShift Container Platform templates.

If you disable the samples capability, users cannot access the image streams, samples, and templates it provides. Depending on your deployment, you might want to disable this component if you do not need it.

<div>

<div class="title">

Additional resources

</div>

- [Configuring the Cluster Samples Operator](../../openshift_images/configuring-samples-operator.md#configuring-samples-operator)

- [cluster-samples-operator](https://github.com/openshift/cluster-samples-operator)

</div>

## Operator Lifecycle Manager (OLM) Classic capability

OLM (Classic) provides the features for the `OperatorLifecycleManager` capability.

Operator Lifecycle Manager (OLM) Classic helps users install, update, and manage the lifecycle of Kubernetes native applications (Operators) and their associated services running across their OpenShift Container Platform clusters. Operator Lifecycle Manager (OLM) Classic forms part of the Operator Framework, an open source toolkit designed to manage Operators in an effective, automated, and scalable way.

If an Operator requires any of the following APIs, then you must enable the `OperatorLifecycleManager` capability:

- `ClusterServiceVersion`

- `CatalogSource`

- `Subscription`

- `InstallPlan`

- `OperatorGroup`

> [!IMPORTANT]
> The `marketplace` capability depends on the `OperatorLifecycleManager` capability. You cannot disable the `OperatorLifecycleManager` capability and enable the `marketplace` capability.

<div>

<div class="title">

Additional resources

</div>

- [Operator Lifecycle Manager concepts and resources](../../operators/understanding/olm/olm-understanding-olm.md#olm-understanding-olm)

- [Operator Framework](https://operatorframework.io/)

</div>

## Operator Lifecycle Manager (OLM) v1 capability

OLM v1 provides the features for the `OperatorLifecycleManagerV1` capability.

Starting in OpenShift Container Platform 4.18, OLM v1 is enabled by default alongside OLM (Classic). This next-generation iteration provides an updated framework that evolves many of OLM (Classic) concepts that enable cluster administrators to extend capabilities for their users.

OLM v1 manages the lifecycle of the new `ClusterExtension` object, which includes Operators via the `registry+v1` bundle format, and controls installation, upgrade, and role-based access control (RBAC) of extensions within a cluster.

In OpenShift Container Platform, OLM v1 is provided by the `olm` cluster Operator.

> [!NOTE]
> The `olm` cluster Operator informs cluster administrators if there are any installed extensions blocking cluster upgrade, based on their `olm.maxOpenShiftVersion` properties. For more information, see "Compatibility with OpenShift Container Platform versions".

Operator Lifecycle Manager (OLM) v1 comprises the following component projects:

- Operator Controller: The central component of OLM v1 that extends Kubernetes with an API through which users can install and manage the lifecycle of Operators and extensions. It consumes information from catalogd.

- Catalogd: A Kubernetes extension that unpacks file-based catalog (FBC) content packaged and shipped in container images for consumption by on-cluster clients. As a component of the OLM v1 microservices architecture, catalogd hosts metadata for Kubernetes extensions packaged by the authors of the extensions, and as a result helps users discover installable content.

- CRDs:

  - `clusterextension.olm.operatorframework.io`

    - Scope: Cluster

    - CR: `ClusterExtension`

  - `clustercatalog.olm.operatorframework.io`

    - Scope: Cluster

    - CR: `ClusterCatalog`

- See the following projects in the *Additional resources* section:

  - `operator-framework/operator-controller`

  - `operator-framework/catalogd`

<div>

<div class="title">

Additional resources

</div>

- [Extensions overview](../../extensions/index.md#olmv1-about)

- [operator-framework/operator-controller](https://github.com/operator-framework/operator-controller)

- [operator-framework/catalogd](https://github.com/operator-framework/catalogd)

</div>

# Viewing the cluster capabilities

As a cluster administrator, you can view the capabilities by using the `clusterversion` resource status.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- To view the status of the cluster capabilities, run the following command:

  ``` terminal
  $ oc get clusterversion version -o jsonpath='{.spec.capabilities}{"\n"}{.status.capabilities}{"\n"}'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  {"additionalEnabledCapabilities":["openshift-samples"],"baselineCapabilitySet":"None"}
  {"enabledCapabilities":["openshift-samples"],"knownCapabilities":["CSISnapshot","Console","Insights","Storage","baremetal","marketplace","openshift-samples"]}
  ```

  </div>

</div>

# Enabling the cluster capabilities by setting baseline capability set

As a cluster administrator, you can enable cluster capabilities any time after a OpenShift Container Platform installation by setting the `baselineCapabilitySet` configuration parameter.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- To set the `baselineCapabilitySet` configuration parameter, run the following command:

  ``` terminal
  $ oc patch clusterversion version --type merge -p '{"spec":{"capabilities":{"baselineCapabilitySet":"vCurrent"}}}'
  ```

  For `baselineCapabilitySet` you can specify `vCurrent`, `v4.17`, or `None`.

</div>

# Enabling the cluster capabilities by setting additional enabled capabilities

As a cluster administrator, you can enable cluster capabilities any time after a OpenShift Container Platform installation by setting the `additionalEnabledCapabilities` configuration parameter.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  View the additional enabled capabilities by running the following command:

    ``` terminal
    $ oc get clusterversion version -o jsonpath='{.spec.capabilities.additionalEnabledCapabilities}{"\n"}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ["openshift-samples"]
    ```

    </div>

2.  To set the `additionalEnabledCapabilities` configuration parameter, run the following command:

    ``` terminal
    $ oc patch clusterversion/version --type merge -p '{"spec":{"capabilities":{"additionalEnabledCapabilities":["openshift-samples", "marketplace"]}}}'
    ```

    > [!IMPORTANT]
    > You cannot disable a capability that is already enabled in a cluster. The cluster version Operator (CVO) continues to reconcile the capability which is already enabled in the cluster.

    If you try to disable a capability, then CVO shows the divergent spec:

    ``` terminal
    $ oc get clusterversion version -o jsonpath='{.status.conditions[?(@.type=="ImplicitlyEnabledCapabilities")]}{"\n"}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    {"lastTransitionTime":"2022-07-22T03:14:35Z","message":"The following capabilities could not be disabled: openshift-samples","reason":"CapabilitiesImplicitlyEnabled","status":"True","type":"ImplicitlyEnabledCapabilities"}
    ```

    </div>

    > [!NOTE]
    > During the cluster upgrades, it is possible that a given capability could be implicitly enabled. If a resource was already running on the cluster before the upgrade, then any capabilities that is part of the resource will be enabled. For example, during a cluster upgrade, a resource that is already running on the cluster has been changed to be part of the `marketplace` capability by the system. Even if a cluster administrator does not explicitly enabled the `marketplace` capability, it is implicitly enabled by the system.

</div>
