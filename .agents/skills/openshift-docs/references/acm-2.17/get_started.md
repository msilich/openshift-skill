> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/get_started/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="get-started-acm"></a>

# Get started with Red Hat Advanced Cluster Management

Install Red Hat Advanced Cluster Management through Operator Lifecycle Manager, which manages the installation, update, and removal of the components that encompass the Red Hat Advanced Cluster Management hub cluster. You can also find information about updating, uninstalling, and cleaning up artifacts before reinstalling. See advanced configuration information for Red Hat Advanced Cluster Management and discover APIs from the console or command line. After you create the `MultiClusterHub` resource during installation, the Red Hat Advanced Cluster Management operator automatically installs the multicluster engine operator and creates the `MultiClusterEngine` resource.

You must have a supported version of OpenShift Container Platform to install Red Hat Advanced Cluster Management. Review the required hardware and system configuration for each product. You can install online on Linux with a supported version of OpenShift Container Platform.

For full support information, see the [Red Hat Advanced Cluster Management Support Matrix](https://access.redhat.com/articles/7142376) and the [Lifecycle and update policies for Red Hat Advanced Cluster Management for Kubernetes](https://access.redhat.com/support/policy/updates/advanced-cluster-management).

**Deprecated:** Red Hat Advanced Cluster Management 2.9 and earlier versions are no longer supported. The documentation might remain available, but without any errata releases for fixed issues or other updates.

- [Preparing for Red Hat Advanced Cluster Management installation](get_started.md#prepare-install-acm)

- [Installing from the console](get_started.md#install-console-acm)

- [Installing from the command-line interface](get_started.md#install-command-line-acm)

- [Install on disconnected networks](get_started.md#install-on-disconnected-networks)

- [Configuring infrastructure nodes for Red Hat Advanced Cluster Management](get_started.md#config-infra-node-acm)

- [MultiClusterHub advanced configuration](get_started.md#advanced-config-hub)

- [Cluster sizing](get_started.md#cluster-sizing)

- [Performance and scalability overview](get_started.md#performance-and-scalability)

- [Resource requests for components](get_started.md#component-resource-requests)

- [Update considerations for your hub cluster](get_started.md#update-considerations)

- [Updating your hub cluster](get_started.md#updating-hub)

- [Updating in a disconnected network environment](get_started.md#updating-disconnected)

- [Uninstalling](get_started.md#uninstalling)

- [Cleaning up artifacts before reinstalling](get_started.md#cleanup-reinstall)

- [APIs](get_started.md#apis)

- [Discover APIs from the console](get_started.md#discover-apis-console-acm)

- [Discover APIs from the command line](get_started.md#discover-apis-command-line-acm)

<a id="prepare-install-acm"></a>

## Preparing for Red Hat Advanced Cluster Management installation

Install Red Hat Advanced Cluster Management through Operator Lifecycle Manager, which manages the installation, upgrade, and removal of the components that encompass the Red Hat Advanced Cluster Management hub cluster.

- Because Red Hat Advanced Cluster Management depends on and uses the multicluster engine operator, after you create the `MultiClusterHub` resource during installation, the Red Hat Advanced Cluster Management operator automatically installs the multicluster engine operator and creates the `MultiClusterEngine` resource.

- You must have an Internet connection to access the dependencies for the operator.

- To import, you must use the `stable-2.0` channel of the klusterlet operator for 2.17.

- **Required access:** Cluster administrator

- **OpenShift Container Platform Dedicated environment required access:** You need `cluster-admin` permissions. By default the `dedicated-admin` role does not have the required permissions to create namespaces in the OpenShift Container Platform Dedicated environment.

- For full support information, see the [Red Hat Advanced Cluster Management Support Matrix](https://access.redhat.com/articles/7142376) and the [Lifecycle and update policies for Red Hat Advanced Cluster Management](https://access.redhat.com/support/policy/updates/advanced-cluster-management).

- By default, the hub cluster components are installed on worker nodes of your OpenShift Container Platform cluster without any additional configuration. You can install the hub cluster on worker nodes by using the Red Hat OpenShift Software Catalog console, or by using the OpenShift Container Platform command-line interface.

- If you have configured your OpenShift Container Platform cluster with infrastructure nodes, you can install the hub cluster on those infrastructure nodes by using the OpenShift Container Platform command-line interface with additional resource parameters. See the *Installing the Red Hat Advanced Cluster Management hub cluster on infrastructure node* section for more details.

- If you plan to import Kubernetes clusters that are not OpenShift Container Platform or Red Hat Advanced Cluster Management clusters, you need to configure an image pull secret.

- For information on how to configure advanced configurations, see options in the [MultiClusterHub advanced configuration](get_started.md#advanced-config-hub) section of the documentation.

- If you previously installed Red Hat Advanced Cluster Management on a cluster, then uninstalled, you need to follow the clean up procedure to remove artifacts. See [Cleaning up artifacts before reinstalling](get_started.md#cleanup-reinstall) and follow the procedure.

- If you plan to configure TLS, go to the OpenShift Container Platform [Configuring TLS security profiles](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/tls-security-profiles) section of the documentation and review the requirements for TLS security profiles.

<div>

<div class="title">

Procedure

</div>

1.  Ensure that your Red Hat OpenShift Container Platform cluster can access the Red Hat Advanced Cluster Management operator in the Red Hat OpenShift Software Catalog console.

2.  Ensure that your OpenShift Container Platform cluster is supported by your current Red Hat Advanced Cluster Management version.

3.  Access the catalog at [catalog.redhat.com](https://catalog.redhat.com/software/containers/search?p=1&application_categories_list=Container%20Platform%20%2F%20Management).

4.  Install a supported version of OpenShift Container Platform and the OpenShift Container Platform command-line interface. See [OpenShift Container Platform installing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installation_overview/index).

5.  Configure to run `oc` commands. See [Getting started with the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started) for information.

6.  Ensure that your permissions allow you to create a namespace. Without a namespace, installation fails.

7.  **Optional:** Install in a OpenShift Container Platform Dedicated environment. You must have the OpenShift Container Platform Dedicated environment configured and running and you must have `cluster-admin` authority to the OpenShift Container Platform Dedicated environment where you are installing the hub cluster.

8.  Confirm your installation. Verify that a Red Hat Advanced Cluster Management hub cluster is not already installed on your OpenShift Container Platform cluster. You cannot have more than one hub cluster. You can only have one single Red Hat Advanced Cluster Management hub cluster installation on each OpenShift Container Platform cluster. Continue with the following steps if there is no Red Hat Advanced Cluster Management hub cluster installed:

9.  To ensure that the OpenShift Container Platform cluster is set up correctly, access the OpenShift Container Platform web console with the following command:

    ``` bash
    oc -n openshift-console get route
    ```

    See the following example output:

    ``` bash
    openshift-console console console-openshift-console.apps.new-coral.purple-chesterfield.com
    console   https   reencrypt/Redirect     None
    ```

10. Open the URL in your browser and check the result. If the console URL displays `console-openshift-console.router.default.svc.cluster.local`, set the value for `openshift_master_default_subdomain` when you install OpenShift Container Platform. See the following example of a URL: `https://console-openshift-console.apps.new-coral.purple-chesterfield.com`.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

You can proceed to install Red Hat Advanced Cluster Management from the [console](get_started.md#install-console-acm) or the [command-line interface](get_started.md#install-command-line-acm). **Note:** For installing the Red Hat Advanced Cluster Management hub cluster on infrastructure nodes, see *Configuring infrastructure nodes for Red Hat Advanced Cluster Management*.

</div>

<a id="install-console-acm"></a>

## Installing from the console

Install Red Hat Advanced Cluster Management for Kubernetes from the Red Hat OpenShift Software Catalog console by using Operator Lifecycle Manager, which manages the installation, upgrade, and removal of the components that encompass the Red Hat Advanced Cluster Management hub cluster. Because Red Hat Advanced Cluster Management depends on and uses the multicluster engine operator, after you create the `MultiClusterHub` resource during installation, the Red Hat Advanced Cluster Management operator automatically installs the multicluster engine operator and creates the `MultiClusterEngine` resource.

<div>

<div class="title">

Prerequisites

</div>

- Before you install Red Hat Advanced Cluster Management, ensure that your cluster is prepared and meets the prerequisites. See [Preparing for Red Hat Advanced Cluster Management installation](get_started.md#prepare-install-acm).

- By default, the Red Hat OpenShift Software Catalog console installation process creates a namespace that is titled `open-cluster-management`. Continue to use the `open-cluster-management` namespace if it is available for the installation process.

- If there is already a namespace named `open-cluster-management`, choose a different namespace for the installation.

- From the *Administrator* view in your console, you need to install the console interface that is provided with OpenShift Container Platform.

- **Important:** For security reasons, do not give access to the `<your-local-cluster-name>` namespace to any user that is not a `cluster-administrator`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to your OpenShift Container Platform cluster console.

2.  Go to **Ecosystem** \> **Software Catalog**.

3.  Find the *Advanced Cluster Management for Kubernetes* operator and choose the options for your installation:

    Channel  
    The channel that you select corresponds to the release that you are installing. When you select the channel, it installs the identified release, and establishes that the future errata updates within that release are obtained.

    Namespace information  
    The Red Hat Advanced Cluster Management hub cluster must be installed in its own namespace, or project.

    Approval strategy for updates  
    The approval strategy identifies the human interaction that is required for applying updates to the channel or release to which you subscribed.

4.  Select **Automatic** to ensure any updates within that release are automatically applied.

5.  Select **Manual** to receive a notification when an update is available. If you have concerns about when the updates are applied, this might be best practice for you.

    **Important:** To upgrade to the next minor release, you must return to the *Red Hat OpenShift Software Catalog* page and select a new channel for a more recent release.

6.  Select **Install** to apply your changes and create the operator.

7.  Create the *MultiClusterHub* custom resource.

    1.  In the OpenShift Container Platform console navigation, select **Installed Operators** \> **Advanced Cluster Management for Kubernetes**.

    2.  Select the **MultiClusterHub** tab.

    3.  Select **Create MultiClusterHub**.

    4.  Update the default values in the YAML file. See options in the *MultiClusterHub advanced configuration* section of the documentation.

8.  Click the *MultiClusterHub* tab to see the list of resources where your operator is listed. The following example shows the default template from the YAML view. Confirm that `namespace` is your project namespace. See the sample:

    ``` yaml
    apiVersion: operator.open-cluster-management.io/v1
    kind: MultiClusterHub
    metadata:
      name: multiclusterhub
      namespace: <namespace>
    ```

9.  Select **Create** to initialize the custom resource. It can take up to 10 minutes for the Red Hat Advanced Cluster Management hub cluster to build and deploy components. After the Red Hat Advanced Cluster Management hub cluster is created, the `MultiClusterHub` resource status displays *Running* from the *MultiClusterHub* tab of the Red Hat Advanced Cluster Management operator details.

10. Gain access to the console. See the *Access your console* topic in *Additional resources*.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

You can now configure your OpenShift Container Platform cluster to contain infrastructure nodes to run approved management components. Running components on infrastructure nodes avoids allocating OpenShift Container Platform subscription quota for the nodes that are running those management components. See [Configuring infrastructure nodes for Red Hat Advanced Cluster Management](get_started.md#config-infra-node-acm) for that procedure.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Access your console](console.md#accessing-your-console)

- [MultiClusterHub advanced configuration](get_started.md#advanced-config-hub)

- [Installing from the command-line interface](get_started.md#install-command-line-acm)

</div>

<a id="install-command-line-acm"></a>

## Installing from the command-line interface

Install Red Hat Advanced Cluster Management for Kubernetes from the OpenShift Container Platform command-line interface by using Operator Lifecycle Manager, which manages the installation, upgrade, and removal of the components that encompass the Red Hat Advanced Cluster Management hub cluster. Because Red Hat Advanced Cluster Management depends on and uses the multicluster engine operator, after you create the `MultiClusterHub` resource during installation, the Red Hat Advanced Cluster Management operator automatically installs the multicluster engine operator and creates the `MultiClusterEngine` resource.

<div>

<div class="title">

Prerequisites

</div>

- Before you install Red Hat Advanced Cluster Management, ensure that your cluster is prepared and meets the prerequisites. See [Preparing for Red Hat Advanced Cluster Management installation](get_started.md#prepare-install-acm).

- You must be logged in with the command-line interface. See [Getting started with the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started) for information.

- Continue to use the `open-cluster-management` namespace if it is available for the installation process.

- If there is already a namespace named `open-cluster-management`, choose a different namespace for the installation.

- **Important:** For security reasons, do not give access to the `<your-local-cluster-name>` namespace to any user that is not a `cluster-administrator`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a Red Hat Advanced Cluster Management hub cluster namespace where the operator requirements are contained. Run the following command, where `namespace` is the name for your Red Hat Advanced Cluster Management hub cluster namespace. The value for `namespace` might be referred to as *Project* in the OpenShift Container Platform environment:

    ``` bash
    oc create namespace <namespace>
    ```

2.  Switch your project namespace to the one that you created. Replace `namespace` with the name of the Red Hat Advanced Cluster Management hub cluster namespace that you created in step 1.

    ``` bash
    oc project <namespace>
    ```

3.  Create a YAML file to configure an `OperatorGroup` resource. Each namespace can have only one operator group:

    ``` yaml
    apiVersion: operators.coreos.com/v1
    kind: OperatorGroup
    metadata:
      name: <default>
      namespace: <namespace>
    spec:
      targetNamespaces:
      - <namespace>
    ```

    - Replace `<default>` with the name of your operator group.

    - Replace `<namespace>` with the name of your project namespace.

4.  Run the following command to create the `OperatorGroup` resource. Replace `operator-group` with the name of the operator group YAML file that you created:

    ``` bash
    oc apply -f <path-to-file>/<operator-group>.yaml
    ```

5.  Create a YAML file to configure an OpenShift Container Platform subscription to choose the version that you want to install. Your file is similar to the following sample, replacing `release-<2.x>` with the selected release:

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: acm-operator-subscription
    spec:
      sourceNamespace: openshift-marketplace
      source: redhat-operators
      channel: release-<2.x>
      installPlanApproval: Automatic
      name: advanced-cluster-management
    ```

6.  Run the following command to apply the file and create the OpenShift Container Platform subscription. Replace `subscription` with the name of the subscription file that you created:

    ``` bash
    oc apply -f <path-to-file>/<subscription>.yaml
    ```

7.  Create a YAML file to configure the `MultiClusterHub` custom resource. Your default template should look similar to the following example. Replace `namespace` with your project namespace:

    ``` yaml
    apiVersion: operator.open-cluster-management.io/v1
    kind: MultiClusterHub
    metadata:
      name: multiclusterhub
      namespace: <namespace>
    spec: {}
    ```

8.  Run the following command to apply the file and create the `MultiClusterHub` custom resource. Replace `custom-resource` with the name of your custom resource file:

    ``` bash
    oc apply -f <path-to-file>/<custom-resource>.yaml
    ```

    **Note:** If you receive the following error, the resource process is still running. Run the `oc apply` command again in a few minutes when the resources are created:

    ``` bash
    error: unable to recognize "./mch.yaml": no matches for kind "MultiClusterHub" in version "operator.open-cluster-management.io/v1"
    ```

9.  Run the following command to get the custom resource. It can take up to 10 minutes for the `MultiClusterHub` custom resource status to display as `Running`:

    ``` bash
    oc get mch -o yaml
    ```

    **Notes:**

    - A `ServiceAccount` with a `ClusterRoleBinding` automatically gives cluster administrator privileges to Red Hat Advanced Cluster Management and to any user credentials with access to the namespace where you install Red Hat Advanced Cluster Management.

    - A namespace called `<your-local-cluster-name>` is reserved for the Red Hat Advanced Cluster Management hub cluster when it is self-managed. This is the only `local-cluster` namespace that can exist in the product.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

You can now configure your OpenShift Container Platform cluster to contain infrastructure nodes to run approved management components. Running components on infrastructure nodes avoids allocating OpenShift Container Platform subscription quota for the nodes that are running those management components. See [Configuring infrastructure nodes for Red Hat Advanced Cluster Management](get_started.md#config-infra-node-acm) for that procedure.

</div>

<div>

<div class="title">

Additional resources

</div>

- [MultiClusterHub advanced configuration](get_started.md#advanced-config-hub)

- [Installing from the console](get_started.md#install-console-acm)

- [Access your console](console.md#accessing-your-console)

</div>

<a id="config-infra-node-acm"></a>

## Configuring infrastructure nodes for Red Hat Advanced Cluster Management

Configure your OpenShift Container Platform cluster to contain infrastructure nodes to run approved Red Hat Advanced Cluster Management management components. Running components on infrastructure nodes avoids allocating OpenShift Container Platform subscription quota for the nodes that are running Red Hat Advanced Cluster Management management components.

After adding infrastructure nodes to your OpenShift Container Platform cluster, follow the [Installing from the command-line interface](get_started.md#install-command-line-acm) instructions and add configurations to the Operator Lifecycle Manager subscription and `MultiClusterHub` custom resource.

Follow the procedures that are described in [Creating infrastructure machine sets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/machine_management/creating-infrastructure-machinesets) in the OpenShift Container Platform documentation. Infrastructure nodes are configured with a Kubernetes `taints` and `labels` to keep non-management workloads from running on them.

<div>

<div class="title">

Procedure

</div>

1.  To be compatible with the infrastructure node enablement provided by Red Hat Advanced Cluster Management, ensure your infrastructure nodes have the following `taints` and `labels` applied:

    ``` yaml
    metadata:
      labels:
        node-role.kubernetes.io/infra: ""
    spec:
      taints:
      - effect: NoSchedule
        key: node-role.kubernetes.io/infra
    ```

2.  Add the following additional configuration before applying the Operator Lifecycle Manager Subscription:

    ``` yaml
    spec:
      config:
        nodeSelector:
          node-role.kubernetes.io/infra: ""
        tolerations:
        - key: node-role.kubernetes.io/infra
          effect: NoSchedule
          operator: Exists
    ```

3.  Add the following additional configuration before you apply the `MultiClusterHub` custom resource:

    ``` yaml
    spec:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
    ```

4.  Update any add-ons to include the following node selectors and tolerations. You need to use the instructions [Set up the *AddOnDeploymentConfig* to configure klusterlet add-ons](add-ons.md#setting-addondeploymentconfig-klusterlet-addons):

    ``` yaml
        nodeSelector:
          node-role.kubernetes.io/infra: ""
        tolerations:
        - key: node-role.kubernetes.io/infra
          effect: NoSchedule
          operator: Exists
    ```

5.  If you used Red Hat OpenShift Data Foundation as a storage provisioner, make sure *Container Storage Interface* pods can run on infrastructure nodes. Learn more at [Managing container storage interface (CSI) component placements](https://docs.redhat.com/it/documentation/red_hat_openshift_data_foundation/4.18/html/managing_and_allocating_storage_resources/managing-container-storage-interface-component-placements_rhodf#managing-container-storage-interface-component-placements_rhodf) in the Red Hat OpenShift Data Foundation documentation.

</div>

<a id="install-on-disconnected-networks"></a>

## Installing in disconnected network environments

You might need to install Red Hat Advanced Cluster Management on disconnected OpenShift Container Platform clusters. To install on a disconnected hub cluster, perform the following steps in addition to the usual install or update steps that are for the connected network environment.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Before you install Red Hat Advanced Cluster Management, ensure that your cluster is prepared and meets the prerequisites. See [Preparing for Red Hat Advanced Cluster Management installation](get_started.md#prepare-install-acm).

- Since you are installing in a disconnected network environment, you need access to a local image registry to store mirrored Operator Lifecycle Manager catalogs and operator images. You probably already set up a local image registry when installing the OpenShift Container Platform cluster in this environment, so you should be able to use the same local image registry.

- You must have a workstation that has access to both the Internet and your local mirror registry.

- You need a supported OpenShift Container Platform version that aligns with your Red Hat Advanced Cluster Management version deployed in your environment.

- You must be logged in with the command-line interface. See the [OpenShift Container Platform install documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installation_overview/index) for information on installing OpenShift Container Platform. See [Getting started with the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started) for information.

- Review [Cluster sizing](get_started.md#cluster-sizing) to learn about setting up capacity for your hub cluster.

- If you previously installed Red Hat Advanced Cluster Management on a cluster, then uninstalled, you need to follow the clean up procedure to remove artifacts. See [Cleaning up artifacts before reinstalling](get_started.md#cleanup-reinstall) and follow the procedure.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Confirm your OpenShift Container Platform installation while you are connected. Verify that a Red Hat Advanced Cluster Management hub cluster is not already installed on your OpenShift Container Platform cluster. You can only have one single Red Hat Advanced Cluster Management hub cluster installation on each OpenShift Container Platform cluster.

    1.  Access the OpenShift Container Platform web console with the following command:

        ``` bash
        oc -n openshift-console get route
        ```

    2.  See the following example output:

    ``` bash
    openshift-console console console-openshift-console.apps.new-coral.purple-chesterfield.com
    console   https   reencrypt/Redirect     None
    ```

    1.  Open the URL in your browser and check the result. If the console URL displays `console-openshift-console.router.default.svc.cluster.local`, set the value for `openshift_master_default_subdomain` when you install OpenShift Container Platform.

2.  Confirm availability of a local image registry. **Best practice:** Use your existing mirror registry for the Operator Lifecycle Manager operator related content.

    Installing Red Hat Advanced Cluster Management in a disconnected environment involves the use of a local mirror image registry. Because you already completed the installation of the OpenShift Container Platform cluster in your disconnected environment, you already set up a mirror registry for use during the OpenShift Container Platform cluster installation.

    If you do not already have a local image registry, create one by completing the procedure that is described in [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/disconnected_environments/mirroring-in-disconnected-environments#mirroring-images-disconnected-install) of the Red Hat OpenShift Container Platform documentation.

3.  Configure Operator Lifecycle Manager. Red Hat Advanced Cluster Management is packaged as an operator, so you install by using Operator Lifecycle Manager.

    In disconnected environments, Operator Lifecycle Manager cannot access the standard operator sources that Red Hat provided operators can because they are hosted on image registries that are not accessible from a disconnected cluster. Instead, a cluster administrator can enable the installation and update of operators in a disconnected environment by using mirrored image registries and operator catalogs.

    To prepare your disconnected cluster for installing Red Hat Advanced Cluster Management, follow the procedure that is described in [Using Operator Lifecycle Manager on restricted networks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/operators/index#olm-restricted-networks) in the OpenShift Container Platform documentation.

4.  Include operator packages in your mirror catalog.

    Red Hat provides the Red Hat Advanced Cluster Management operator in the Red Hat operators catalog, which is delivered by the `registry.redhat.io/redhat/redhat-operator-index` index image. When you prepare your mirror of this catalog index image, you can choose to either mirror the entire catalog as provided by Red Hat, or you can mirror a subset that contains only the operator packages that you intend to use.

    If you are creating a full mirror catalog, no special considerations are needed as all of the packages required to install Red Hat Advanced Cluster Management are included. However, if you are creating a partial or filtered mirrored catalog, for which you identify particular packages to be included, you need to include the following package names in your list:

    - `advanced-cluster-management`

    - `multicluster-engine`

5.  Use one of the following two mirroring procedures:

    - If you are creating the mirrored catalog or registry by using the OPM utility, `opm index prune`, include the following package names in the value of the `-p` option as displayed in the following example, with the current version replacing `4.x`:

      ``` bash
      opm index prune \
         -f registry.redhat.io/redhat/redhat-operator-index:v4.x \
         -p advanced-cluster-management,multicluster-engine \
         -t myregistry.example.com:5000/mirror/my-operator-index:v4.x
      ```

    - If you are populating the mirrored catalog or registry by using the `oc-mirror` plug-in instead, include the following package names in the packages list section of your `ImageSetConfiguration`, as displayed in the following example, with the current version replacing `4.x`:

    ``` yaml
    kind: ImageSetConfiguration
    apiVersion: mirror.openshift.io/v1alpha2
    storageConfig:
      registry:
         imageURL: myregistry.example.com:5000/mirror/oc-mirror-metadata
    mirror:
      platform:
        channels:
        - name: stable-4.x
          type: ocp
      operators:
      - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.11
        packages:
        - name: advanced-cluster-management
        - name: multicluster-engine
      additionalImages: []
      helm: {}
    ```

6.  Configure to use your mirror registry.

    When you have populated a local mirror registry with the earlier packages that are required for installing Red Hat Advanced Cluster Management, complete the steps that are described in [Using Operator Lifecycle Manager on restricted networks](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.20/html-single/operators/index#olm-restricted-networks) to make your mirror registry and catalog available on your disconnected cluster, which includes the following procedures:

    - [Disabling the default OperatorHub sources](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.20/html-single/operators/index#olm-restricted-networks-operatorhub_olm-restricted-networks)

    - [Mirroring the Operator catalog](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.20/html-single/operators/index#olm-mirror-catalog_olm-restricted-networks)

    - [Adding a catalog source for your mirrored catalog](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.20/html-single/operators/index#olm-creating-catalog-from-index_olm-restricted-networks)

7.  Add a `CatalogSource` resource to your disconnected cluster by following the OpenShift Container Platform documentation. **Important:** Take note of the value of the `metadata.name` field, which you will need later.

8.  Add the `CatalogSource` resource into the `openshift-marketplace` namespace by using a YAML file similar to the following example, replacing `4.x` with the current version:

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: CatalogSource
    metadata:
      name: my-mirror-catalog-source
      namespace: openshift-marketplace
    spec:
      image: myregistry.example.com:5000/mirror/my-operator-index:v4.x
      sourceType: grpc
    ```

    You need the `metadata.name` field value for the annotation in the `MultiClusterHub` resource that you will create later.

9.  Verify that the required packages are available.

    Operator Lifecycle Manager polls catalog sources for available packages on a regular timed interval. After Operator Lifecycle Manager polls the catalog source for your mirrored catalog, you can verify that the required packages are available from on your disconnected cluster by querying the available `PackageManifest` resources.

    Run the following command, directed at your disconnected cluster:

    ``` bash
    oc -n openshift-marketplace get packagemanifests
    ```

    The list that is displayed should include entries showing that the following packages are supplied by the catalog source for your mirror catalog:

    - `advanced-cluster-management`

    - `multicluster-engine`

10. Configure image content source policies.

    To have your cluster obtain container images for the Red Hat Advanced Cluster Management for Kubernetes operator from your mirror registry, rather than from the internet-hosted registries, you must configure an `ImageContentSourcePolicy` on your disconnected cluster to redirect image references to your mirror registry.

    If you mirrored your catalog using the `oc adm catalog mirror` command, the needed image content source policy configuration is in the `imageContentSourcePolicy.yaml` file inside of the `manifests-*` directory that is created by that command.

    If you used the oc-mirror plug-in to mirror your catalog instead, the `imageContentSourcePolicy.yaml` file is within the `oc-mirror-workspace/results-*` directory create by the oc-mirror plug-in.

    Apply the policies to your disconnected command using an `oc apply` or `oc replace`. See the following command:

    ``` bash
    oc replace -f ./<path>/imageContentSourcePolicy.yaml
    ```

    The required image content source policy statements can vary based on how you created your mirror registry, but are similar to the following example:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ImageContentSourcePolicy
    metadata:
      labels:
        operators.openshift.org/catalog: "true"
      name: operator-0
    spec:
      repositoryDigestMirrors:
      - mirrors:
        - myregistry.example.com:5000/rhacm2
        source: registry.redhat.io/rhacm2
      - mirrors:
        - myregistry.example.com:5000/multicluster-engine
        source: registry.redhat.io/multicluster-engine
      - mirrors:
        - myregistry.example.com:5000/openshift4
        source: registry.redhat.io/openshift4
      - mirrors:
        - myregistry.example.com:5000/redhat
        source: registry.redhat.io/redhat
    ```

11. Install the Red Hat Advanced Cluster Management operator and hub cluster.

    After you have configured Operator Lifecycle Manager and OpenShift Container Platform, you can install Red Hat Advanced Cluster Management by using the Red Hat OpenShift Software Catalog console or the command-line interface. For directions, see [Installing from the console](get_started.md#install-console-acm) or [Installing from the command-line interface](get_started.md#install-command-line-acm).

    Creating the `MulticlusterHub` resource is the beginning of the installation process of your hub cluster.

    Because operator installation on a cluster requires the use of a non-default catalog source for the mirror catalog, a special annotation is needed in the `MulticlusterHub` resource to provide the name of the mirror catalog source to the operator. The following example displays the required `mce-subscription-spec` annotation:

    ``` yaml
    apiVersion: operator.open-cluster-management.io/v1
    kind: MultiClusterHub
    metadata:
       namespace: open-cluster-management
       name: hub
       annotations:
          installer.open-cluster-management.io/mce-subscription-spec: '{"source": "my-mirror-catalog-source"}'
    spec: {}
    ```

    The `mce-subscription-spec` annotation is required because multicluster engine operator is automatically installed during the Red Hat Advanced Cluster Management installation. If you are creating the resource with a command-line interface, include the `mce-subscription-spec` annotation in the YAML that you apply with the `oc apply` command to create the `MultiClusterHub` resource.

    If you create the resource by using the console, switch to the *YAML view* and insert the annotation as previously displayed. **Important:** There is no field in the OperatorHub console for the annotation in the *Field view* panel to create the `MultiClusterHub` resource.

12. Learn about `CatalogSource` priority. When the `MultiClusterHub` resource prepares to install the multicluster engine operator, it implements `CatalogSource` priority as criteria.

    The Red Hat Advanced Cluster Management `MultiClusterHub` resource seeks the `CatalogSource` that contains the desired multicluster engine operator version that is compatible with the current Red Hat Advanced Cluster Management version.

    If there are multiple `CatalogSource` resources available, the `MultiClusterHub` resource selects the catalog source with the highest `spec.priority` value that is set within the resource instances. If a custom `CatalogSource` is created without a priority level, it is set to `0` and used as the target `CatalogSource`. By default, the `redhat-operators` priority is set to `-100`, as displayed in the following example `CatalogSource`:

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: CatalogSource
    metadata:
      name: redhat-operators
      namespace: openshift-marketplace
    spec:
       displayName: Red Hat Operators
       priority: -100
    ```

</div>

<a id="advanced-config-hub"></a>

## *MultiClusterHub* advanced configuration

Red Hat Advanced Cluster Management for Kubernetes is installed by using the `MultiClusterHub` operator, which deploys all of the required components. Some of the listed components are enabled by default. If a component is *disabled*, that resource is not deployed to the cluster until it is enabled.

- Deployed components

|  |  |  |
|----|----|----|
| Name | Description | Enabled |
| app-lifecycle | Unifies and simplifies options for constructing and deploying applications and application updates. | True |
| cluster-backup | Provides backup and restore support for all hub cluster resources such as managed clusters, applications, and policies. | False |
| cluster-lifecycle | Provides cluster management capabilities for OpenShift Container Platform and Red Hat Advanced Cluster Management hub clusters. | True |
| cluster-permission | Automatically distributes RBAC resources to managed clusters and manage the lifecycle of those resources. | True |
| cnv-mtv-integrations | Provide related resources for virtual machine live migration. | False |
| console | Enables Red Hat Advanced Cluster Management web console plug-in. | True |
| fine-grained-rbac | Enables fine-grained role-based access control for virtual machine resources across clusters. | False |
| grc | Enables the security enhancement for you to define policies for your clusters. | True |
| insights | Identifies existing or potential problems in your clusters. | True |
| multicluster-observability | Enables monitoring to gain further insights into the health of your managed clusters. | True |
| search | Provides visibility into your Kubernetes resources across all of your clusters. | True |
| siteconfig | Enables provisioning clusters at scale by using templates and a unified front-end API. | False |
| submariner-addon | Enables direct networking and service discovery between two or more managed clusters in your environment, either on-premises or in the cloud. | True |
| volsync | Supports asynchronous replication of persistent volumes within a cluster, or across clusters with storage types that are not otherwise compatible for replication. | True |

Table list of the deployed components

When you install Red Hat Advanced Cluster Management on to the cluster, not all of the listed components are enabled by default.

You can further configure Red Hat Advanced Cluster Management during or after installation by adding one or more attributes to the `MultiClusterHub` custom resource. Continue reading for information about the attributes that you can add.

- Console and component configuration

The following example displays the `spec.overrides` default template that you can use to enable or disable the component:

``` yaml
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterHub
metadata:
  name: multiclusterhub
  namespace: <namespace>
spec:
  overrides:
    components:
    - name: <name>
      enabled: true
```

- Replace `namespace` with the name of your project.

- Replace `name` with the name of the component.

Alternatively, you can run the following command. Replace `namespace` with the name of your project and `name` with the name of the component:

    oc patch MultiClusterHub multiclusterhub -n <namespace> --type=json -p='[{"op": "add", "path": "/spec/overrides/components/-","value":{"name":"<name>","enabled":true}}]'

**Note:** When the `console` component is disabled, the Red Hat OpenShift Container Platform console is disabled.

Custom Image Pull Secret  
If you plan to import Kubernetes clusters that were not created by OpenShift Container Platform or Red Hat Advanced Cluster Management, generate a secret that has your OpenShift Container Platform pull secret information to access the entitled content from the distribution registry.

The secret requirements for OpenShift Container Platform clusters are automatically resolved by OpenShift Container Platform and Red Hat Advanced Cluster Management, so you do not have to create the secret if you are not importing other types of Kubernetes clusters to be managed. Your OpenShift Container Platform pull secret is associated with your Red Hat Customer Portal ID, and is the same across all Kubernetes providers.

**Important:** These secrets are namespace-specific, so make sure that you are in the namespace that you use for your hub cluster.

See [cloud.redhat.com/openshift/install/pull-secret](https://console.redhat.com/openshift/install/pull-secret) to download the OpenShift Container Platform pull secret file. Click **Download pull secret**. Run the following command to create your secret:

``` bash
oc create secret generic <secret> -n <namespace> --from-file=.dockerconfigjson=<path-to-pull-secret> --type=kubernetes.io/dockerconfigjson
```

- Replace `secret` with the name of the secret that you want to create.

- Replace `namespace` with your project namespace, as the secrets are namespace-specific.

- Replace `path-to-pull-secret` with the path to your OpenShift Container Platform pull secret that you downloaded.

The following example displays the `spec.imagePullSecret` template to use if you want to use a custom pull secret. Replace secret with the name of your pull secret:

``` yaml
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterHub
metadata:
  name: multiclusterhub
  namespace: <namespace>
spec:
  imagePullSecret: <secret>
```

availabilityConfig  
The Red Hat Advanced Cluster Management hub cluster has two availabilities: `High` and `Basic`. By default, the hub cluster has an availability of `High`, which gives hub cluster components a `replicaCount` of `2`. This provides better support in cases of failover but consumes more resources than the `Basic` availability, which gives components a `replicaCount` of `1`.

**Important:** Set `spec.availabilityConfig` to `Basic` if you are using multicluster engine operator on a single-node OpenShift cluster.

The following example shows the `spec.availabilityConfig` template with `Basic` availability:

``` yaml
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterHub
metadata:
  name: multiclusterhub
  namespace: <namespace>
spec:
  availabilityConfig: "Basic"
```

nodeSelector  
You can define a set of node selectors in the Red Hat Advanced Cluster Management hub cluster to install to specific nodes on your cluster. The following example shows `spec.nodeSelector` to assign Red Hat Advanced Cluster Management pods to nodes with the label `node-role.kubernetes.io/infra`:

``` yaml
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterHub
metadata:
  name: multiclusterhub
  namespace: <namespace>
spec:
  nodeSelector:
    node-role.kubernetes.io/infra: ""
```

To define a set of node selectors for the multicluster engine operator cluster, see [Advanced configuration multicluster engine operator](clusters.md#advanced-config-engine) in the multicluster engine operator documentation.

tolerations  
You can define a list of tolerations to allow the Red Hat Advanced Cluster Management hub cluster to tolerate specific taints defined on the cluster.

The following example shows a `spec.tolerations` that matches a `node-role.kubernetes.io/infra` taint:

``` yaml
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterHub
metadata:
  name: multiclusterhub
  namespace: <namespace>
spec:
  tolerations:
  - key: node-role.kubernetes.io/infra
    effect: NoSchedule
    operator: Exists
```

The previous infra-node toleration is set on pods by default without specifying any tolerations in the configuration. Customizing tolerations in the configuration replaces this default.

To define a list of tolerations for the multicluster engine operator hub cluster, see [Advanced configuration multicluster engine operator](clusters.md#advanced-config-engine) in the multicluster engine operator documentation.

disableHubSelfManagement  
By default, the Red Hat Advanced Cluster Management hub cluster is automatically imported and the hub cluster manages itself. A hub cluster that manages itself is designated as the `local-cluster`.

You can change the `spec.localClusterName` name if the `disableHubSelfManagement` field is set to `true`, which disables the local cluster feature.

The `local-cluster` cannot be renamed if the `disableHubSelfManagement` field is set to `false`, which enables the local cluster.

You must use 34 or fewer characters for the `<your-local-cluster-name>` value. The `local-cluster` resource and the namespaces reflects the change.

If you do not want the Red Hat Advanced Cluster Management hub cluster to manage itself, you need change the setting for `spec.disableHubSelfManagement` from `false` to `true`.

See the following YAML sample with `disableHubSelfManagement:true`, which disables the `local-cluster` setting. Replace `namespace` with the name of your project:

``` yaml
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterHub
metadata:
  name: multiclusterhub
  namespace: <namespace>
spec:
  disableHubSelfManagement: true
  localClusterName: local-cluster
```

To enable the default `local-cluster`, return the setting to `false`. You can also remove this setting to return to default behavior, which is the hub cluster managing itself as a local cluster.

Setting the `disableHubSelfManagement` option to `true` and attempting to manage the hub cluster manually leads to unexpected behavior.

On a Red Hat Advanced Cluster Management hub cluster that is managing a multicluster engine operator cluster, any earlier manual configurations are replaced by new configuration.

disableUpdateClusterImageSets  
If you want to ensure that you use the same release image for all of your clusters, you can create your own custom list of release images that are available when you create a cluster.

See the following instructions in [Maintain a custom list of release images when connected](clusters.md#release-images-connected) to manage your available release images and to set the `spec.disableUpdateClusterImageSets` attribute, which stops the custom image list from being overwritten.

The following example shows the default template that disables updates to the cluster image set. Replace `namespace` with the name of your project:

``` yaml
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterHub
metadata:
  name: multiclusterhub
  namespace: <namespace>
spec:
  disableUpdateClusterImageSets: true
```

customCAConfigmap (Deprecated)  
By default, Red Hat OpenShift Container Platform uses the Ingress Operator to create an internal CA.

The following example shows the default template used to provide a customized OpenShift Container Platform default ingress CA certificate to Red Hat Advanced Cluster Management. Replace `namespace` with the name of your project. Replace the `spec.customCAConfigmap` value with the name of your `ConfigMap`:

``` yaml
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterHub
metadata:
  name: multiclusterhub
  namespace: <namespace>
spec:
  customCAConfigmap: <configmap>
```

sslCiphers (Deprecated)  
By default, the Red Hat Advanced Cluster Management hub cluster includes the full list of supported SSL ciphers.

The following example shows the default `spec.ingress.sslCiphers` template that is used to list `sslCiphers` for the management ingress. Replace `namespace` with the name of your project:

``` yaml
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterHub
metadata:
  name: multiclusterhub
  namespace: <namespace>
spec:
  ingress:
    sslCiphers:
    - "ECDHE-ECDSA-AES128-GCM-SHA256"
    - "ECDHE-RSA-AES128-GCM-SHA256"
```

ClusterBackup  
The `enableClusterBackup` field is no longer supported and is replaced by this component.

The following example shows the `spec.overrides` default template used to enable `ClusterBackup`. Replace `namespace` with the name of your project:

``` yaml
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterHub
metadata:
  name: multiclusterhub
  namespace: <namespace>
spec:
  overrides:
    components:
    - name: cluster-backup
      enabled: true
```

Alternatively, you can run the following command. Replace `namespace` with the name of your project.

``` bash
oc patch MultiClusterHub multiclusterhub -n <namespace> --type=json -p='[{"op": "add", "path": "/spec/overrides/components/-","value":{"name":"cluster-backup","enabled":true}}]'
```

cnv-mtv-integrations  
The `cnv-mtv-integrations` component requires the `local-cluster` to be enabled on the hub cluster. The `local-cluster` feature allows the hub cluster to manage itself and is enabled by default. You must have Cluster Administrator access to use the `cnv-mtv-integrations` component, and the `local-cluster` must be enabled.

- If you plan to use `cnv-mtv-integrations`, do not set `disableHubSelfManagement: true` in the `MultiClusterHub` custom resource. If `disableHubSelfManagement` is set to `true`, `cnv-mtv-integrations` does not function correctly.

- Do not disable `local-cluster` in the `MultiClusterEngine` custom resource.

- You cannot disable the `local-cluster` while `cnv-mtv-integrations` is enabled. To disable the `local-cluster`, you must first disable the `cnv-mtv-integrations` component.

- Verify that the local-cluster is enabled. Run the following command to confirm that the `local-cluster` exists and status is `Available=True`:

``` bash
oc get managedcluster local-cluster
```

<a id="cluster-sizing"></a>

## Cluster sizing

The following guidelines give sample deployment sizes for your cluster, which are classified by size and purpose. Red Hat Advanced Cluster Management applies the following dimensions for sizing and placement of supporting services:

Availability zones  
Availability zones isolate potential fault domains across the cluster. Typical clusters have near-equal worker node capacity in three or more availability zones.

vCPU reservations and limits  
vCPU reservations and limits establish vCPU capacity on a worker node to assign to a container. A vCPU is equal to a Kubernetes compute unit. See the Kubernetes [Meaning of CPU](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/#meaning-of-cpu) topic to learn about Kubernetes compute units.

Memory reservations and limits  
Memory reservations and limits establish memory capacity on a worker node to assign to a container.

Persistent data  
Persistent data is managed by the product and stored in the etcd cluster that is used by Kubernetes.

Single node OpenShift Container Platform clusters  
*Availability zones* isolate potential fault domains across the cluster. High Availability is not supported in single-node OpenShift clusters. **Important:** For an Red Hat Advanced Cluster Management hub cluster that is running on OpenShift Container Platform, distribute the master nodes of the cluster across three availability zones.

**Important:** For OpenShift Container Platform, distribute the master nodes of the cluster across three availability zones.

The following requirements are *not* minimum requirements for the environment:

| Node type | Availability zones | etcd | Total reserved memory | Total reserved CPU |
|----|----|----|----|----|
| Master | 3 | 3 | Per OpenShift Container Platform sizing guidelines | Per OpenShift Container Platform sizing guidelines |
| Worker or infrastructure | 3 | 1 | 12 GB | 6 |

Product environment

Additionally, the OpenShift Container Platform cluster runs more services to support cluster features. See the following table for information about OpenShift Container Platform on additional services. *Availability zones* isolate potential fault domains across the cluster:

| Service | Node count | Availability zones | Instance size | vCPU | Memory | Storage size | Resources |
|----|----|----|----|----|----|----|----|
| OpenShift Container Platform on Amazon Web Services | 3 | 3 | m5.xlarge | 4 | 16 GB | 120 GB | See *Installing on AWS* in the OpenShift Container Platform product documentation for more information. Also learn more about *machine types* in the AWS documentation. See the related links in *Additional resources*. |
| OpenShift Container Platform on Google Cloud Platform | 3 | 3 | N1-standard-4 (0.95–6.5 GB) | 4 | 15 GB | 120 GB | See the *View and manage quotas* for more information about quotas. Also learn more about *Google Machine families resource and comparisons*. See the related links. |
| OpenShift Container Platform on Microsoft Azure | 3 | 3 | Standard_D4_v3 | 4 | 16 GB | 120 GB | See *Configuring an Azure* account in the OpenShift Container Platform documentation for more details. |
| OpenShift Container Platform on VMware vSphere | 3 | 3 |  | 4 (2 cores per socket) | 16 GB | 120 GB | See *Installing on VMware vSphere* in the OpenShift Container Platform documentation for more details. |
| OpenShift Container Platform on IBM Z systems | 3 | 3 |  | 10 | 16 GB | 100 GB | See *Installing a cluster on IBM Z systems* in the OpenShift Container Platform documentation for more information. IBM Z systems provide the ability to configure simultaneous multithreading (SMT), which extends the number of vCPUs that can run on each core. If you configured SMT, One physical core (IFL) provides two logical cores (threads). The hypervisor can provide two or more vCPUs. One vCPU is equal to one physical core when simultaneous multithreading (SMT), or hyper-threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs. For more information about SMT, see *Simultaneous multithreading*. |
| OpenShift Container Platform on IBM Power systems | 3 | 3 |  | 16 | 16 GB | 120 GB | See *Installing a cluster on Power systems* in the OpenShift Container Platform documentation for more information. IBM Power systems provide the ability to configure simultaneous multithreading (SMT), which extends the number of vCPUs that can run on each core. If you configured SMT, your SMT level determines how you satisfy the 16 vCPU requirement. The most common configurations are: Two cores running on SMT-8 (the default configuration for systems that are running IBM Power VM) that provide the required 16 vCPUs, and four cores running on SMT-4 that provide the required 16 vCPUs. For more information about SMT, see *Simultaneous multithreading*. |
| OpenShift Container Platform on-premises | 3 |  |  | 4 | 16 GB | 120 GB | See *Configuring a three-node cluster* in the OpenShift Container Platform documentation for more details. An Red Hat Advanced Cluster Management hub cluster can be installed and supported on OpenShift Container Platform bare metal. The hub cluster can run on a compact bare metal topology, in which there are 3 schedulable control plane nodes, and 0 additional workers. |

Additional services

See example requirements for creating and managing 3500 single node OpenShift Container Platform clusters. See the minimum requirements for using Red Hat Advanced Cluster Management to create single-node OpenShift clusters (230 and more provisioned at the same time), and manage those single-node OpenShift clusters with a hub cluster:

| Node count | Memory (peak cluster usage) | Memory (single node min-max) | CPU (peak cluster usage) | CPU (single node min-max) |
|----|----|----|----|----|
| 3 | 447 GB | 113 GB-205 GB | 114 | 31-62 |

Master (schedulable)

<div>

<div class="title">

Additional resources

</div>

- [Installing on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_aws/index)

- [machine types](https://aws.amazon.com/ec2/instance-types/m5/)

- [Configuring an Azure account](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_azure/installing-azure-account)

- [Installing on VMware vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_vmware_vsphere/preparing-to-install-on-vsphere)

- [Installing a cluster on IBM Z systems](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_ibm_z_and_ibm_linuxone/index)

- [Simultaneous multithreading](https://www.ibm.com/docs/en/aix/7.2.0?topic=concepts-simultaneous-multithreading)

- [Installing a cluster on Power systems](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_ibm_power/index)

- [Configuring a three-node cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_openstack/installing-openstack-three-node#installation-three-node-cluster_installing-openstack-three-node)

- [Installing on a single node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_on_a_single_node/index)

</div>

<a id="performance-and-scalability"></a>

## Performance and scalability overview

Red Hat Advanced Cluster Management for Kubernetes is tested to determine certain scalability and performance data. The major areas that are tested are cluster scalability and search performance. Use this information as you plan your environment.

**Note:** Data is based on the results from a lab environment at the time of testing.

Red Hat Advanced Cluster Management is tested by using a three node hub cluster on bare metal machines. At testing, there is a sufficient amount of resource capacity (CPU, memory, and disk) to find software component limits. Your results might vary, depending on your environment, network speed, and changes to the product.

Maximum number of managed clusters  
The maximum number of clusters that Red Hat Advanced Cluster Management can manage varies based on the following factors:

- The number of resources in the cluster, which depends on factors such as the number of policies and applications that are deployed.

- The configuration of the hub cluster, such as how many pods are used for scaling.

- The managed clusters are single-node OpenShift virtual machines that are hosted on Red Hat Enterprise Linux hypervisors.

- Virtual machines are used to achieve high-density counts of clusters per single bare metal machine in the testbed.

- Sushy-emulator is used with libvirt for virtual machines to have an accessible bare metal cluster by using Redfish APIs.

- The following operators are a part of the test installation, Topology Aware Lifecycle Manager, Local Storage Operator, and Red Hat OpenShift GitOps.

The following table shows the lab environment scaling information:

| Node | Count | Operating system | Hardware | CPU cores | Memory | Disks |
|----|----|----|----|----|----|----|
| Hub cluster control plane | 3 | OpenShift Container Platform | Bare metal | 112 | 512 GiB | 446 GB SSD, 2.9 TB NVMe, 2 x 1.8 TB SSD |
| Managed cluster | 3500 | single-node OpenShift | Virtual machine | 8 | 18 GiB | 120 GB |

Table for environment scaling

- Search scalability

The scalability of the search component depends on the performance of the data store. The query run time is an important variable when analyzing the search performance.

There are some things that can affect the time that it takes to run and return results from a query. Consider the following items when planning and configuring your environment:

- Searching for a keyword is not efficient.

  If you search for `RedHat` and you manage a large number of clusters, it might take a longer time to receive search results.

- The first search takes longer than later searches because it takes additional time to gather user role-based access control rules.

- The length of time to complete a request is proportional to the number of namespaces and resources the user is authorized to access.

  **Note:** If you save and share a search query with another user, returned results depend on access level for that user. For more information on role access, see [Using RBAC to define and apply permissions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/authentication_and_authorization/using-rbac) in the OpenShift Container Platform documentation.

- The worst performance is observed for a request by a non-administrator user with access to all of the namespaces, or all of the managed clusters.

  - Observability scalability

You need to plan your environment if you want to enable and use the observability service. The resource consumption later is for the OpenShift Container Platform project, where observability components are installed. Values that you plan to use are sums for all observability components.

**Note:** Data is based on the results from a lab environment at the time of testing. Your results might vary, depending on your environment, network speed, and changes to the product.

- Sample observability environment

  In the sample environment, hub clusters and managed clusters are located in Amazon Web Services cloud platform and have the following topology and configuration:

  | Node        | Flavor     | vCPU | RAM (GiB) | Disk type | Disk size (GiB) | Count | Region    |
  |-------------|------------|------|-----------|-----------|-----------------|-------|-----------|
  | Master node | m5.4xlarge | 16   | 64        | gp2       | 100             | 3     | sa-east-1 |
  | Worker node | m5.4xlarge | 16   | 64        | gp2       | 100             | 3     | sa-east-1 |

  Table for sample observability environment

The observability deployment is configured for high availability environments. With a high availability environment, each Kubernetes deployment has two instances, and each StatefulSet has three instances.

- Write throughput

  During the sample test, a different number of managed clusters are simulated to push metrics, and each test lasts for 24 hours. See the following throughput:

  | Pods | Interval (minute) | Time series per min |
  |------|-------------------|---------------------|
  | 400  | 1                 | 83000               |

  Table for write throughput

- CPU usage (millicores)

  See the following CPU usage during testing:

  | Size        | CPU Usage |
  |-------------|-----------|
  | 10 clusters | 400       |
  | 20 clusters | 800       |

  Table for CPU usage (millicores)

- RSS and working set memory

  - **Memory usage RSS:** From the metrics `container_memory_rss` and remains stable during the test.

  - **Memory usage working set:** From the metrics `container_memory_working_set_bytes`, increases along with the test.

    The following results are from a 24-hour test:

  | Size        | Memory usage RSS | Memory usage working set |
  |-------------|------------------|--------------------------|
  | 10 clusters | 9.84             | 4.93                     |
  | 20 clusters | 13.10            | 8.76                     |

  Table for RSS and working set memory

- Persistent Volume for the `thanos-receive` component

  **Important:** Metrics are stored in `thanos-receive` until retention time (four days) is reached. Other components do not require as much volume as `thanos-receive` components.

  Disk usage increases along with the test. Data represents disk usage after one day, so the final disk usage is multiplied by four.

  | Size        | Disk usage (GiB) |
  |-------------|------------------|
  | 10 clusters | 2                |
  | 20 clusters | 3                |

  Table of disk usage

- Network transfer

  During tests, network transfer provides stability. See the sizes and network transfer values:

  | Size        | Inbound network transfer | Outbound network transfer |
  |-------------|--------------------------|---------------------------|
  | 10 clusters | 6.55 MBs per second      | 5.80 MBs per second       |
  | 20 clusters | 13.08 MBs per second     | 10.9 MBs per second       |

  Table Network transfer

- Amazon Simple Storage Service (S3)

  Total usage in Amazon Simple Storage Service (S3) increases. The metrics data is stored in S3 until default retention time (five days) is reached. See the following disk usages:

  | Size        | Disk usage (GiB) |
  |-------------|------------------|
  | 10 clusters | 16.2             |
  | 20 clusters | 23.8             |

  Table for Amazon Simple Storage Service (S3)

- Backup and restore scalability

The tests performed on large scaled environment show the following data for backup and restore:

| Backups          | Duration | Number of resources | Backup memory        |
|------------------|----------|---------------------|----------------------|
| credentials      | 2m5s     | 18272 resources     | 55MiB backups size   |
| managed clusters | 3m22s    | 58655 resources     | 38MiB backups size   |
| resources        | 1m34s    | 1190 resources      | 1.7MiB backups size  |
| generic/user     | 2m56s    | 0 resources         | 16.5KiB backups size |

Table of run times for managed cluster backups

The total backup time is `10m`.

| Backups             | Duration | Number of resources |
|---------------------|----------|---------------------|
| redentials          | 47m8s    | 18272 resources     |
| resources           | 3m10s    | 1190 resources      |
| generic/user backup | 0m       | 0 resources         |

Table of run time for restoring passive hub cluster

Total restore time is `50m18s`.

The number of backup file are pruned using the `veleroTtl` parameter option set when the `BackupSchedule` is created. Any backups with a creation time older than the specified TTL (time to live) are expired and automatically deleted from the storage location by Velero.

``` yaml
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: BackupSchedule
 metadata:
 name:schedule-acm
 namespace:open-cluster-management-backup
spec:
veleroSchedule:0 */1 * * *
veleroTtl:120h
```

<a id="component-resource-requests"></a>

## Resource requests for components

On the hub cluster, the deployment of each component has resource requests that are based on the number of clusters that you manage with Red Hat Advanced Cluster Management. Setting resource requests helps ensure that hub cluster components have sufficient resources to operate effectively.

See the following table for details on the resource requests for each component:

| Namespace | Deployment | CPU Request | Memory Request |
|----|----|----|----|
| `ocm` | `klusterlet-addon-controller-v2` | 50m | 96Mi |
| `multicluster-engine` | `clusterlifecycle-state-metrics-v2` | 25m | 32Mi |
| `multicluster-engine` | `cluster-manager` | 2m | 16Mi |
| `open-cluster-management-hub` | `cluster-manager-addon-manager-controller` | 2m | 16Mi |
| `open-cluster-management-hub` | `cluster-manager-placement-controller` | 2m | 16Mi |
| `open-cluster-management-hub` | `cluster-manager-registration-controller` | 2m | 16Mi |
| `open-cluster-management-hub` | `cluster-manager-registration-webhook` | 2m | 16Mi |
| `open-cluster-management-hub` | `cluster-manager-work-webhook` | 2m | 16Mi |
| `multicluster-engine` | `cluster-proxy-addon-manager` | 25m | 128Mi |
| `multicluster-engine` | `cluster-proxy-addon-user` | 25m | 256Mi |
| `multicluster-engine` | `managedcluster-import-controller-v2` | 50m | 96Mi |
| `multicluster-engine` | `ocm-controller` | 100m | 256Mi |
| `multicluster-engine` | `ocm-proxyserver` | 100m | 256Mi |
| `multicluster-engine` | `ocm-webhook` | 50m | 128Mi |

Table list of component requests

The resource requests that are listed result from the following environment variables:

- Each cluster belongs to one cluster set.

- Each cluster has 10 add-ons and 30 `ManifestWorks` with 50kb installed.

- See the CPU usage calculation: `50m + 0.05m` `*` `CLUSTER_NUMBER`.

- See the memory usage calculation: `1000Mi + 10Mi` `*` `CLUSTER_NUMBER`.

For example, for 50 clusters, the following formulas are used:

- CPU usage is calculated with the following formula: `50m + 0.05m x 50 = 52.5m`.

- Memory usage is calculated with the following formula: `1000Mi + 10Mi x 50 = 1500Mi.`

For example, for 100 clusters, the following formulas are used:

- CPU usage is calculated with the following formula: `50m + 0.05m x 100 = 55m`.

- Memory usage is is calculated with the following formula: `1000Mi + 10Mi x 100 = 2000Mi`

<a id="update-considerations"></a>

## Update considerations for your hub cluster

Before you update your Red Hat Advanced Cluster Management for Kubernetes hub cluster, see the following information about the update process and requirements, then proceed to [Updating your hub cluster](get_started.md#updating-hub) for instructions about how to update your hub cluster.

**Required access:** OpenShift Container Platform administrator

- Plan to update both Red Hat Advanced Cluster Management and multicluster engine operator. Do not attempt to update multicluster engine operator separately from Red Hat Advanced Cluster Management update because this action can cause issues with your cluster.

- If you attempt to update to an unsupported OpenShift Container Platform version, you receive an error message. If you force the update to an *unsupported* version, your Red Hat Advanced Cluster Management hub cluster does not function correctly.

- When you update Red Hat Advanced Cluster Management, multicluster engine operator automatically updates to the required version. The `MultiClusterHub` `mceVersionCompliance` resource status is `isCompliant: true`.

- Updates are always supported from the immediate previous version. You can update to the next available feature release.

- If you are on a version with *Extended Update Support* (EUS), you can update to the next version, or you can skip to the next EUS version. You can perform skip-level updates from `<2.x>` to `<2.x+2>` on *odd* number versions of Red Hat Advanced Cluster Management. For instance, when you update Red Hat Advanced Cluster Management 2.13, which is an EUS version, you can choose to update to version 2.15, which is also an EUS version.

- Downgrading a version is not supported. You cannot revert to an earlier version after updating to a later version in the channel selection. You must uninstall the operator and reinstall it with the earlier version to use a previous version.

- The Operator Lifecycle Manager `operatorcondition` helps control how versions are updated. When you initially deploy Red Hat Advanced Cluster Management by using the operator, you make the following selections:

  Channel  
  Channel corresponds to the version of the product that you are installing. The initial channel setting is often the most current channel that was available at the time of installation.

  Approval  
  Approval specifies whether approval is required for updates within the channel, or if they are done automatically.

- If set to `Automatic`, then minor release updates in the selected channel are deployed without administrator intervention.

  - If set to `Manual`, then each update to the minor release within the channel requires an administrator to approve the update.

    You also use these settings when you update to the latest version of Red Hat Advanced Cluster Management by using the operator.

Continue to [Updating your hub cluster](get_started.md#updating-hub) to complete the steps to update your operator.

- Component considerations

  - If you are [Cluster pools (Technology Preview)](clusters.md#managing-cluster-pools), you need further configuration to stop automatic management of these cluster pools after update. Set `cluster.open-cluster-management.io/createmanagedcluster: "false"` in the `ClusterClaim` `metadata.annotations`.

  - If you use OpenShift GitOps, verify that the `managedserviceaccount` component is enabled in multicluster engine operator before you update. OpenShift GitOps uses short-lived tokens that require this component. If the component is disabled, OpenShift GitOps loses connectivity to managed clusters and Argo CD applications show as `Unknown`. See [ManagedServiceAccount add-on](clusters.md#advanced-config-engine) and [Register managed clusters to the Red Hat OpenShift GitOps operator](gitops.md#gitops-push-register).

<a id="updating-hub"></a>

## Updating your hub cluster

You control your Red Hat Advanced Cluster Management for Kubernetes updates by using the operator subscription settings in the Red Hat OpenShift Container Platform console.

**Required access:** OpenShift Container Platform administrator

<div>

<div class="title">

Prerequisites

</div>

- Before you update, see [Update considerations for your hub cluster](get_started.md#update-considerations) to understand the update requirements, limitations, and the potential impacts of an update.

- Before you update OpenShift Container Platform on your Red Hat Advanced Cluster Management hub cluster, ensure that you choose the OpenShift Container Platform version that is supported by your current Red Hat Advanced Cluster Management version. See the Support Matrix in [Red Hat Advanced Cluster Management Support Matrix](https://access.redhat.com/articles/7142376) for more information about the required OpenShift Container Platform versions for each Red Hat Advanced Cluster Management version.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to your Red Hat OpenShift Software Catalog.

2.  In the OpenShift Container Platform navigation, select **Ecosystem** \> **Installed operators**.

3.  Select the **Red Hat Advanced Cluster Management for Kubernetes** operator.

4.  Select the *Subscription* tab to edit the subscription settings.

5.  Ensure that the *Update Status* is labeled *Up to date*. This status indicates that the operator is at the latest level that is available in the selected channel. If the *Update Status* indicates that there is an update pending, complete the following steps to update it to the latest minor release that is available in the channel:

    1.  Click the **Manual** setting in the *Approval* field to edit the value.

    2.  Select **Automatic** to enable automatic updates.

    3.  Select **Save** to commit your change.

    4.  Wait for the automatic updates to be applied to the operator. The updates automatically add the required updates to the latest version in the selected channel. When all of the updated updates are complete, the *Update Status* field indicates an `Up to date` status.

        **Note:** It can take up to 10 minutes for the `MultiClusterHub` custom resource to finish updating. You can check whether the update is still in process by entering the following command:

        ``` bash
        oc get mch
        ```

    While it is updating, the `Status` field shows the `Updating` status. After the update is complete, the `Status` field shows the `Running` status.

6.  When the *Update Status* is `Up to date`, click the value in the *Channel* field to edit the channel.

7.  Select the channel for the next available feature release, but do not attempt to skip a channel.

    **Important:** The Operator Lifecycle Manager `operatorcondition` resource checks for previous updates during the current update process and prevents skipping versions. You can check that same resource status to see if the upgradable status is `true` or `false`.

8.  Click **Save** to save your changes.

9.  Wait for the automatic update to complete. After the update to the next feature release completes, the updates to the latest patch releases within the channel are deployed.

10. If you have to update to a later feature release, repeat steps 7-9 until your operator is at the latest level of the desired channel. Make sure that all of the patch releases are deployed for your final channel.

11. **Optional:** You can set your *Approval* setting to **Manual**, if you want your future updates within the channel to require manual approvals.

12. If you performed a skip-level update, see the following sub steps to verify your update:

    1.  Verify that the `csv` version from the previous release, for instance, `2.13` (EUS), is replaced with the updated version, for instance, `2.15` (EUS).

    2.  Verify that the `MultiClusterHub` instance `status.currentVersion` specification value is set at `2.15` and matches the `desiredVersion` status, which is also set at `2.15`.

13. **Optional:** If you are [Cluster pools (Technology Preview)](clusters.md#managing-cluster-pools), you need further configuration to stop automatic management of these cluster pools.

14. Set `cluster.open-cluster-management.io/createmanagedcluster: "false"` in the `ClusterClaim` `metadata.annotations`.

</div>

<div class="formalpara">

<div class="title">

Results

</div>

All existing cluster claims are automatically imported when the product is updated unless you change this setting.

</div>

<div class="formalpara">

<div class="title">

Additional resources

</div>

[Operators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/operators/index) in the OpenShift Container Platform documentation.

</div>

<a id="updating-disconnected"></a>

## Updating in a disconnected network environment

See the steps and information to update Red Hat Advanced Cluster Management in a disconnected network environment. This information follows the updating procedure in [Updating your hub cluster](get_started.md#updating-hub).

- The process starts by changing the update channel in your Operator Lifecycle Manager subscription for Red Hat Advanced Cluster Management for Kubernetes to the channel for the new release.

- Because of the special characteristics of the disconnected environment, you need to address the mirroring requirements before changing the update channel to start the update process.

- You might encounter important information that is related to the interdependency between the Red Hat Advanced Cluster Management and multicluster engine operator. See [Installing in disconnected network environments](get_started.md#install-on-disconnected-networks) for consideration during install or update.

<div>

<div class="title">

Procedure

</div>

1.  Ensure that required packages are updated in your mirror catalog.

    1.  Update your mirror catalog and registry to pick up the updated versions of the operator packages.During installation, or during a previous update, you created a mirror catalog and a registry that contains operator packages and images that are needed to install Red Hat Advanced Cluster Management in a disconnected network environment.

    2.  Ensure that your mirror catalog and registry include the following operator packages in the list of operators to be included or updated:

        - `advanced-cluster-manager`

        - `multicluster-engine`

2.  Verify your `MutliclusterHub` resource instance. During installation or a previous update, you created an instance of the `MulticlusterHub` resource, and due to the disconnected environment, you added a `mce-subscription-spec` annotation to that resource.

    If you updated your mirror catalog and registry and got an updated catalog on the OpenShift Container Platform cluster through a `CatalogSource` with the same name as the one that you previously used, you do not need to update your `MulticlusterHub` resource to update the `mce-subscriptino-spec` annotation.

    If your mirrored catalog and registry resulted in a newly named `CatalogSource` being created, update the `mce-subscription-spec` annotation in your `MulticlusterHub` resource to reflect the new catalog source name.

3.  Update with catalog mirroring

    Red Hat Advanced Cluster Management uses the related multicluster engine operator functionality to provide foundational services that were delivered as part of the product. Red Hat Advanced Cluster Management automatically installs and manages the required multicluster engine operator and `MulticlusterEngine` resource instance as part of the hub cluster installation and update.

    In connected network environments, the cluster administrator can install or update Red Hat Advanced Cluster Management without special mirror catalogs and catalog sources. However, because installation of any Operator Lifecycle Manager operator in a disconnected environment involves the use of special mirror catalogs and catalog sources, as described in the earlier sections, some additional steps are necessary after installation.

4.  Update your procedures for populating the mirror catalog.

    If when installing Red Hat Advanced Cluster Management mirroring procedures created a full copy of the Red Hat Operators catalog, no special mirroring updates are required. Refresh your catalog to pick up the updated content for the new operator releases.

    If your procedures populated mirror catalog that is a *filtered* catalog, you need to update your mirroring procedures to ensure that the `multcluster-engine` operator package is included in the mirror catalog, in addition to the `advanced-cluster-management` package.

    See the *Install in disconnected network environments* topic for examples of the options to use when populating the mirror catalog. Update the operator-package lists that are used in your procedures to match these new requirements.

5.  Update your `MutliclusterHub` resource instance. You need a new annotation on the `MulticlusterHub` resource when the hub cluster is installed or updated in a disconnected environment.

    **Best practice:** Update your `MulticlusterHub` resource instance to include the required annotation before you change the Operator Lifecycle Manager update channel in your Operator Lifecycle Manager subscription to the `advanced-cluster-management` operator package to start the update. This update allows the update to proceed without delay.

6.  Run the `oc edit` command to update your `Multiclusterub` resource to add the `mce-subscription-spec` annotation as displayed in the following example. Replace `<my-mirror-catalog-source>` from the example with the name of the `CatalogSource` resource located in the `openshift-marketplace` namespace for your mirror catalog:

    ``` yaml
    metadata:
       annotations:
          installer.open-cluster-management.io/mce-subscription-spec: '{"source": "<my-mirror-catalog-source>"}'
    ```

    **Important:** If you begin an update before you add the annotation, the update begins but stalls when the operator attempts to install a subscription to `multicluster-engine` in the background. The status of the `MulticlusterHub` resource continues to display `upgrading` during this time. To resolve this issue, run `oc edit` to add the `mce-subscription-spec` annotation as shown previously.

</div>

<div class="formalpara">

<div class="title">

Additional resources

</div>

[Installing in disconnected network environments](get_started.md#install-on-disconnected-networks)

</div>

<a id="uninstalling"></a>

## Uninstalling Red Hat Advanced Cluster Management

When you uninstall Red Hat Advanced Cluster Management for Kubernetes, you see two different levels of the uninstall process: A *custom resource removal* and a *complete operator uninstall*. The uninstall process can take up to 20 minutes and the process includes removing resources.

Custom resource removal  
The first and most basic type of uninstall that removes the custom resource of the `MultiClusterHub` instance, but leaves other required operator resources. This level of uninstall is helpful if you plan to reinstall with the same settings and components.

Complete operator uninstall  
The second level process that removes most operator components, excluding components such as custom resource definitions. When you continue with this step, it removes all of the components and subscriptions that were not removed with the custom resource removal. After this uninstall, you must reinstall the operator before reinstalling the custom resource.

<div>

<div class="title">

Prerequisites

</div>

- If you have managed clusters attached, you need to detach them. **Note:** This does not include the `local-cluster`, which is your self-managed hub cluster. For more information about detaching clusters, see the *Cluster removal overview* section in [Creating clusters](clusters.md#create-intro).

- If you use Discovery, you need to disable the function. From the console, go to the *Discovered Clusters* table and click **Disable cluster discovery**. Confirm that you want to remove the service. You can also use the terminal to disable Discovery with the following command:

  ``` bash
  oc delete discoveryconfigs --all --all-namespaces
  ```

- If you use Agent Service Configuration, you need to disable and remove the `AgentServiceConfig` resource. Complete the following steps:

  1.  Log in to your hub cluster.

  2.  Delete the `AgentServiceConfig` custom resource by entering the following command:

  ``` bash
  oc delete agentserviceconfig --all
  ```

- If you use observability, disable and remove the `MultiClusterObservability` custom resource. **Note:** Your object storage is not affected after you remove the observability service. See the following procedure:

  1.  Log in to your hub cluster.

  2.  Delete the `MultiClusterObservability` custom resource by entering the following command:

      ``` bash
      oc delete mco observability
      ```

  3.  To remove `MultiClusterObservability` custom resource with the console, see the following procedure:

      1.  If the `MultiClusterObservability` custom resource is installed, select the tab for *MultiClusterObservability*.

      2.  Select the **Options** menu for the `MultiClusterObservability` custom resource.

      3.  Select **Delete MultiClusterObservability**.

  When you delete the resource, the pods in the `open-cluster-management-observability` namespace on Red Hat Advanced Cluster Management hub cluster, and the pods in `open-cluster-management-addon-observability` namespace on all managed clusters are removed.

</div>

<div>

<div class="title">

Procedure

</div>

- Delete *MultiClusterHub* and resources with the terminal

  1.  If you have not already, ensure that your OpenShift Container Platform command-line tool is configured to run `oc` commands. See [Getting started with the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started) in the OpenShift Container Platform documentation for more information about how to configure the `oc` commands.

  2.  Change to your project namespace by entering the following command. Replace *namespace* with the your project namespace:

      ``` bash
      oc project <namespace>
      ```

  3.  Run the following command to delete the `MultiClusterHub` custom resource:

      ``` bash
      oc delete multiclusterhub --all
      ```

  4.  To view the progress, run the following command:

      ``` bash
      oc get mch -o yaml
      ```

  5.  Uninstall the `MultiClusterHub` operator. **Note:** If you plan to reinstall the same Red Hat Advanced Cluster Management version, you do not need to uninstall the operator.

  6.  Run the following commands to delete the `ClusterServiceVersion` and `Subscription` in the namespace where it is installed. Replace the `2.x.0` value with the selected release:

      ``` bash
      oc get csv
      NAME                                 DISPLAY                                      VERSION   REPLACES   PHASE
      advanced-cluster-management.v2.x.0   Advanced Cluster Management for Kubernetes   2.x.0                Succeeded

      oc delete clusterserviceversion advanced-cluster-management.v2.x.0

      oc get sub
      NAME                        PACKAGE                       SOURCE                CHANNEL
      acm-operator-subscription   advanced-cluster-management   acm-custom-registry   release-2.x

      oc delete sub acm-operator-subscription
      ```

  **Note:** The name of the subscription and version of the CSV might differ.

- Delete the components by using the console

  1.  In the OpenShift Container Platform console navigation, select **Operators** \> **Installed Operators** \> **Advanced Cluster Manager for Kubernetes**.

      **Note:** When you use the OpenShift Container Platform console to uninstall, you remove the `MultiClusterHub` resource to delete the object. Wait for the status, then uninstall the operator. Complete the following steps to uninstall by using the console:

  2.  Remove the `MultiClusterHub` custom resource.

      1.  Select the tab for *Multiclusterhub*.

      2.  Select the *Options* menu for the `MultiClusterHub` custom resource.

      3.  Select **Delete MultiClusterHub**.

  3.  Navigate to **Installed Operators**.

  4.  Remove the *Red Hat Advanced Cluster Management* operator by selecting the *Options* menu and selecting **Uninstall operator**.

</div>

<a id="cleanup-reinstall"></a>

## Cleaning up artifacts before reinstalling

Before you reinstall Red Hat Advanced Cluster Management for Kubernetes on a cluster where a previous version was installed and then deleted, you need to remove all artifacts that remain by running the clean-up script. You need to clean up artifacts if you plan to reinstall Red Hat Advanced Cluster Management with an older version of Red Hat Advanced Cluster Management on the same cluster.

**Required access:** Cluster administrator

**OpenShift Container Platform Dedicated environment required access:** You must have `cluster-admin` permissions.

<div>

<div class="title">

Procedure

</div>

1.  Ensure that your Red Hat OpenShift Container Platform CLI is configured to run `oc` commands. See [Getting started with the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started) in the OpenShift Container Platform documentation for more information about how to configure the `oc` commands.

2.  Copy the following script into a file, replacing the `<namespace>` value in the script with the name of the namespace where you previously installed Red Hat Advanced Cluster Management.

    **Important:** Ensure that you specify the correct namespace because the namespace is also cleaned out and deleted when you run the script:

    ``` bash
    ACM_NAMESPACE=<namespace>
    oc delete mch --all -n $ACM_NAMESPACE
    oc delete apiservice v1.admission.cluster.open-cluster-management.io v1.admission.work.open-cluster-management.io
    oc delete clusterimageset --all
    oc delete clusterrole open-cluster-management:cert-policy-controller open-cluster-management:cluster-manager-admin open-cluster-management:config-policy-controller open-cluster-management:endpoint-observability-operator open-cluster-management:governance-policy-framework open-cluster-management:governance-policy-framework-kube-rbac-proxy multiclusterengines.multicluster.openshift.io-v1-admin multiclusterengines.multicluster.openshift.io-v1-crdview multiclusterengines.multicluster.openshift.io-v1-edit multiclusterengines.multicluster.openshift.io-v1-view open-cluster-management:addons:application-manager open-cluster-management:admin-aggregate open-cluster-management:cert-policy-controller-hub open-cluster-management:cluster-manager-admin-aggregate open-cluster-management:config-policy-controller-hub open-cluster-management:edit-aggregate open-cluster-management:policy-framework-hub open-cluster-management:view-aggregate
    oc delete crd klusterletaddonconfigs.agent.open-cluster-management.io placementbindings.policy.open-cluster-management.io policies.policy.open-cluster-management.io userpreferences.console.open-cluster-management.io discoveredclusters.discovery.open-cluster-management.io discoveryconfigs.discovery.open-cluster-management.io
    oc delete mutatingwebhookconfiguration ocm-mutating-webhook managedclustermutators.admission.cluster.open-cluster-management.io multicluster-observability-operator
    oc delete validatingwebhookconfiguration channels.apps.open.cluster.management.webhook.validator application-webhook-validator multiclusterhub-operator-validating-webhook ocm-validating-webhook multicluster-observability-operator multiclusterengines.multicluster.openshift.io
    ```

3.  Run the script. When you receive a message that no resources were found, then you can proceed with the installation.

</div>

<a id="apis"></a>

# APIs

You can use the Search API to query information from Red Hat Advanced Cluster Management. For other APIs, use the *API Explorer* in the console, or an `oc` command, to view current and supported APIs.

**User required access:** You can only perform actions that your role is assigned. Learn about access requirements from the [Role-based access control](secure_clusters.md) documentation.

You can also access Kubernetes APIs from the integrated console. Select the **Administrator** perspective, then navigate to **Home** \> **API Explorer** to explore API groups.

**Note:** For Red Hat OpenShift Container Platform versions earlier than version 4.20, select **local-cluster** from the cluster switcher. Then select **Home** \> **API Explorer** to explore API groups.

For more information, review the following API documentation:

- [Discover APIs from the console](get_started.md#discover-apis-console-acm)

- [Discover APIs from the command line](get_started.md#discover-apis-command-line-acm)

- [Search API](search.md#search-api)

<a id="discover-apis-console-acm"></a>

## Discover APIs from the console

You can view Red Hat Advanced Cluster Management custom resources definitions in the integrated console. List available APIs and display API details for your hub cluster and managed clusters.

**Required access:** Cluster administrator, or a role with permission to list and get custom resources definitions

<div>

<div class="title">

Prerequisites

</div>

- You installed a supported version of OpenShift Container Platform on your hub cluster. See [Installing OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/installation_overview/index).

- You installed Red Hat Advanced Cluster Management on the hub cluster. See [Preparing for Red Hat Advanced Cluster Management installation](get_started.md#prepare-install-acm).

- multicluster engine operator is installed on the hub cluster. If you installed Red Hat Advanced Cluster Management, multicluster engine operator is installed automatically. See [Preparing to install multicluster engine operator](clusters.md#preparing-to-install-mce).

- You configured the OpenShift Container Platform CLI (`oc`) or the Kubernetes CLI (`kubectl`) on your workstation and can run commands against the hub cluster. See [Getting started with the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/cli_tools/openshift-cli-oc#cli-getting-started).

- You are logged in to the hub cluster with credentials that can access API resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform console, choose the **Core platform** view.

2.  Click **Home** \> **API Explorer** in the navigation menu.

3.  From the **API Explorer** page, sort by groups, versions, scope, and kind to view the available APIs and *Resource details* for your hub cluster and managed clusters. You can also change the amount of information that is displayed by selecting the number `per page` from the drop-down menu.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Advanced Cluster Management API documentation](https://github.com/stolostron/api-documentation)

</div>

<a id="discover-apis-command-line-acm"></a>

## Discover APIs from the command line

You can view Red Hat Advanced Cluster Management custom resources definitions from the command line by using the Kubernetes CLI (`kubectl`). List available APIs and display API details for your hub cluster and managed clusters.

**Required access:** Cluster administrator, or a role with permission to list and get custom resources definitions

<div>

<div class="title">

Prerequisites

</div>

- You installed a supported version of OpenShift Container Platform on your hub cluster. See [Installing OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installation_overview/index).

- You installed Red Hat Advanced Cluster Management on the hub cluster. See [Preparing for Red Hat Advanced Cluster Management installation](get_started.md#prepare-install-acm).

- multicluster engine operator is installed on the hub cluster. If you installed Red Hat Advanced Cluster Management, multicluster engine operator is installed automatically. See [Preparing to install multicluster engine operator](clusters.md#preparing-to-install-mce).

- You configured the OpenShift Container Platform CLI (`oc`) or the Kubernetes CLI (`kubectl`) on your workstation and can run commands against the hub cluster. See [Getting started with the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started).

- You are logged in to the hub cluster with credentials that can access API resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  List the APIs that are available on the hub cluster. Run the following command:

    ``` bash
    kubectl get crds
    ```

2.  To view details for a specific `crd`, run the following command. Replace `<name>` with the `crd` name from the previous step:

    ``` bash
    kubectl describe crd <name>
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Advanced Cluster Management API documentation](https://github.com/stolostron/api-documentation)

</div>
