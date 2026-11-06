> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/global_hub/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="multicluster-global-hub"></a>

# multicluster global hub

The multicluster global hub is a set of components that enable you to import one or more hub clusters and manage them from a single hub cluster.

After importing the hub clusters as managed hub clusters, you can use multicluster global hub to complete the following tasks across all of the managed hub clusters:

- Report the policy compliance status and trend

- Inventory all managed hubs and managed clusters on the overview page

- Detect and alert in cases of irregular policy behavior

The multicluster global hub is useful when a single hub cluster cannot manage the large number of clusters in a high-scale environment. When this happens, you divide the clusters into smaller groups of clusters and configure a hub cluster for each group.

It is often inconvenient to view the data on multiple hub clusters for the managed clusters that are managed by that hub cluster. The multicluster global hub provides an easier way to view information from multiple hubs by designating multiple hub clusters as managed hub clusters. The multicluster global hub cluster manages the other hub clusters and gathers summarized information from the managed hub clusters.

Enable the observability service on your multicluster global hub to view the health and utilization of your managed hub clusters in Grafana dashboards. View metrics from your multicluster global hub and hub cluster. For more information about observability, see [Observability service](observability.md#observing-environments-intro) documentation.

To learn about how you can use the multicluster global hub, see the following sections:

- [multicluster global hub architecture](global_hub.md#global-hub-architecture)

- [Networking requirements for multicluster global hub](global_hub.md#global-hub-networking-requirements)

- [Supported components for multicluster global hub](global_hub.md#global-hub-supported-components)

- [Installing Multicluster Global Hub in a connected environment](global_hub.md#global-hub-install-connected)

- [Installing Multicluster Global Hub in a disconnected environment](global_hub.md#global-hub-install-disconnected)

- [Installing multicluster global hub on an existing Red Hat Advanced Cluster Management hub cluster](global_hub.md#global-hub-install-acm)

- [Integrating an existing version of Kafka](global_hub.md#global-hub-integrating-kafka)

- [Integrating an existing version of PostgreSQL](global_hub.md#global-hub-integrating-postgres)

- [Integrating an existing version of Grafana](global_hub.md#global-hub-integrating-grafana)

- [Importing a managed hub cluster in the default mode](global_hub.md#global-hub-importing-managed-hub-in-default-mode)

- [Importing a managed hub cluster in the hosted mode](global_hub.md#global-hub-importing-in-hosted-mode)

- [Access the Grafana data](global_hub.md#global-hub-accessing-grafana-data)

- [Grafana alerts (Technology Preview)](global_hub.md#global-hub-grafana-alerts)

- [Customize Grafana alerting resources](global_hub.md#global-hub-customize-grafana-alert)

- [Delete Grafana alert rules](global_hub.md#global-hub-delete-grafana-rule)

- [multicluster global hub managed cluster migration](global_hub.md#migration-intro)

- [Zero Touch Provisioning migration overview](global_hub.md#ztp-migration-overview)

- [Preparing the hub clusters for migration](global_hub.md#preparing-hubs-for-migration)

- [Verifying the source hub cluster status for migration](global_hub.md#ztp-migration-verify-hub)

- [Applying policy to the target hub cluster for migration](global_hub.md#ztp-apply-policy-hub)

- [Creating a *ManagedClusterMigration* resource to migrate a static list](global_hub.md#ztp-create-resource-static)

- [Creating a *ManagedClusterMigration* resource to migrate a dynamic placement](global_hub.md#ztp-create-resource-dynamic)

- [Verifying the migration resource status](global_hub.md#ztp-create-resource-verify)

- [Monitoring migration progress](global_hub.md#ztp-monitor-migration)

- [Applying *ClusterInstance* applications to the target hub cluster](global_hub.md#ztp-monitor-migration)

- [Cleaning up the source hub cluster](global_hub.md#ztp-clean-up-source-hub)

- [Rolling back cluster migration](global_hub.md#rolling-back-migration)

- [multicluster global hub cron job settings](global_hub.md#global-hub-configuring-cronjobs)

- [Running the summarization process manually](global_hub.md#global-hub-compliance-manual)

- [Backup for multicluster global hub(Technology Preview)](global_hub.md#global-hub-backup)

- [multicluster global hub search (Technology Preview)](global_hub.md#global-search)

- [Migrating managed clusters with multicluster global hub (Technology Preview)](global_hub.md#global-hub-migrate)

- [Managed cluster migration process](global_hub.md#global-hub-migrate-process)

- [Preparing your multicluster global hub environment for migration](global_hub.md#global-hub-migrate-prep)

- [Migrating managed clusters](global_hub.md#global-hub-migrate-clusters)

- [Tracking the migration status](global_hub.md#global-hub-migrate-status)

- [Recovering data from the updated built-in PostgreSQL (Deprecated)](global_hub.md#global-hub-update-postgres)

- [Deleting legacy built-in Postgres data](global_hub.md#global-hub-update-postgres-delete-legacy)

<a id="global-hub-architecture"></a>

## multicluster global hub architecture

The multicluster global hub consists of the following components that are used to access and manage your hub clusters:

- A server component called the *global hub cluster* where the management tools and the console run

- A client component that is installed on Red Hat Advanced Cluster Management, named the *managed hub*, which can be managed by the global hub cluster. The managed hub also manages other clusters. You do not have to use a dedicated cluster for your multicluster global hub cluster.

Learn more about the architecture in the following sections:

See the following high-level multicluster terms and components:

<a id="_the_multicluster_global_hub_operator"></a>

### The multicluster global hub operator

The multicluster global hub operator contains the components of multicluster global hub. The operator deploys all of the required components for global multicluster management. The components include `multicluster-global-hub-manager`, `multicluster-global-hub-grafana`, and provided versions of `Kafka` and `PostgreSQL` in the multicluster global hub cluster and `multicluster-global-hub-agent` in the managed hub clusters.

<a id="_the_multicluster_global_hub_manager"></a>

### The multicluster global hub manager

The multicluster global hub manager is used to persist the data into the `postgreSQL` database. The data is from Kafka transport. The manager also posts the data to the Kafka transport, so it can be synchronized with the data on the managed hub clusters.

<a id="_the_multicluster_global_hub_agent"></a>

### The multicluster global hub agent

The multicluster global hub agent runs on the managed hub clusters. It synchronizes the data between the multicluster global hub cluster and the managed hub clusters. For example, the agent synchronizes the information of the managed clusters from the managed hub clusters to the multicluster global hub cluster and synchronizes the policy or application from the multicluster global hub cluster to the managed hub clusters.

<a id="_the_multicluster_global_hub_visualizations"></a>

### The multicluster global hub visualizations

Grafana runs on the multicluster global hub cluster as the main service for multicluster global hub visualizations. The PostgreSQL data collected by the Global Hub Manager is its default DataSource. By exposing the service using the route called `multicluster-global-hub-grafana`, you can access the multicluster global hub Grafana dashboards by accessing the console.

<a id="global-hub-networking-requirements"></a>

## Networking requirements for multicluster global hub

Learn about the multicluster global hub requirements and review the components and environments that are supported by multicluster global hub.

**Required access:** Cluster administrator

**OpenShift Container Platform Dedicated environment required access:** You must have `cluster-admin` permissions. By default `dedicated-admin` role does not have the required permissions to create namespaces in the OpenShift Container Platform Dedicated environment.

- The managed hub cluster is also a multicluster global hub managed cluster in Red Hat Advanced Cluster Management. You must configure the network component in Red Hat Advanced Cluster Management. For Red Hat Advanced Cluster Management networking details, see [Networking](networking.md#networking).

- To review the multicluster global hub network information, see the following table:

  | Direction | Protocol | Connection | Port that is specified | Source address | Destination address |  |
  |----|----|----|----|----|----|----|
  | Inbound from the browser | HTTPS | Access the Grafana dashboard | 443 | Browser | Grafana route IP address |  |
  | Outbound to Kafka Cluster | HTTPS | The multicluster global hub manager needs to receive data from Kafka cluster | 443 | `multicluster-global-hub-manager-xxx` pod | Kafka route host |  |
  | Outbound to PostgreSQL database | HTTPS | The multicluster global hub needs to contribute data to the PostgreSQL database | 443 | `multicluster-global-hub-manager-xxx` pod | PostgreSQL database IP address |  |

  Global hub network information

- To review the managed hub network information, see the following table:

  | Direction | Protocol | Connection | Port that is specified | Source address | Destination address |  |
  |----|----|----|----|----|----|----|
  | Outbound to Kafka Cluster | HTTPS | The multicluster global hub agent needs to sync cluster and policy information to Kafka cluster | 443 | `multicluster-global-hub-agent` pod | Kafka route host |  |

  Managed hub cluster network information

For sizing guidelines, see [Sizing your Red Hat Advanced Cluster Management cluster](get_started.md).

<div>

<div class="title">

Additional resources

</div>

- [Installing Multicluster Global Hub in a connected environment](global_hub.md#global-hub-install-connected)

- [Installing Multicluster Global Hub in a disconnected environment](global_hub.md#global-hub-install-disconnected)

</div>

<a id="global-hub-supported-components"></a>

## Supported components for multicluster global hub

Learn about the multicluster global hub requirements and review the components and environments that are supported by multicluster global hub.

**Required access:** Cluster administrator

**OpenShift Container Platform Dedicated environment required access:** You must have `cluster-admin` permissions. By default `dedicated-admin` role does not have the required permissions to create namespaces in the OpenShift Container Platform Dedicated environment.

- The multicluster global hub and OpenShift Container Platform console share an integrated console, so they support the same browser. For information about supported browsers and versions, see [Accessing the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html-single/web_console/index#web-console) in the Red Hat OpenShift Container Platform documentation

- Supported components:

The multicluster global hub and OpenShift Container Platform console share an integrated console, so they support the same browser. For information about supported browsers and versions, see [Accessing the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/web_console/index#web-console) in the Red Hat OpenShift Container Platform documentation. See the following table of supported platforms for the multicluster global hub cluster:

| Platform | Supported for global hub cluster | Supported for managed hub cluster |
|----|----|----|
| Red Hat Advanced Cluster Management 2.17, and later 2.17.x releases | Yes | Yes |
| Red Hat Advanced Cluster Management 2.16, and later 2.16.x releases | Yes | Yes |
| Red Hat Advanced Cluster Management 2.15, and later 2.15.x releases | Yes | Yes |
| Red Hat Advanced Cluster Management on Arm | Yes | Yes |
| Red Hat Advanced Cluster Management on IBM Z | Yes | Yes |
| Red Hat Advanced Cluster Management on IBM Power Systems | Yes | Yes |

multicluster global hub supports middleware, such as Kafka, PostgreSQL, and Grafana. See the following table for a list of supported middleware and built-in versions:

| Middleware               | Built-in version |
|--------------------------|------------------|
| Streams for Apache Kafka | 3.1.x            |
| Kafka                    | 4.1.0            |
| PostgreSQL               | 16               |
| Grafana                  | 12.4.0           |

<div>

<div class="title">

Additional resources

</div>

- [Installing Multicluster Global Hub in a connected environment](global_hub.md#global-hub-install-connected)

- [Installing Multicluster Global Hub in a disconnected environment](global_hub.md#global-hub-install-disconnected)

</div>

<a id="global-hub-install-connected"></a>

## Installing multicluster global hub in a connected environment

The multicluster global hub is installed through Operator Lifecycle Manager, which manages the installation, update, and removal of the components that comprise the operator.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- For the OpenShift Container Platform Dedicated environment, you must have `cluster-admin` permissions to access the environment. By default `dedicated-admin` role does not have the required permissions to create namespaces in the OpenShift Container Platform Dedicated environment.

- You must install and configure Red Hat Advanced Cluster Management for Kubernetes. For more details, see [Get started with Red Hat Advanced Cluster Management](get_started.md#get-started-acm).

- You must configure the Red Hat Advanced Cluster Management network. The managed hub cluster is also a managed cluster of multicluster global hub in Red Hat Advanced Cluster Management. For more details, see [Hub cluster network configuration](networking.md#hub-network-config).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform console as a user with the `cluster-admin` role.

2.  From the navigation menu, select **Operators** \> the **OperatorHub** icon.

3.  Locate and select the **Multicluster global hub operator**.

4.  Click **Install** to start the installation.

5.  After the installation completes, check the status on the *Installed Operators* page.

6.  Click **Multicluster global hub operator** to go to the *Operator* page.

7.  Click the **Multicluster global hub** tab to see the `Multicluster Global Hub` instance.

8.  Click **Create Multicluster Global Hub** to create the `Multicluster Global Hub` instance.

9.  Enter the required information and click **Create** to create the `Multicluster Global Hub` instance.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Mirroring an Operator catalog](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/operators/index#olm-mirror-catalog_olm-restricted-networks)

- [Accessing images for Operators from private registries](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/operators/index#olm-accessing-images-private-registries_olm-managing-custom-catalogs)

- [Adding a catalog source to a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/operators/index#olm-creating-catalog-from-index_olm-restricted-networks)

- [Installing in disconnected network environments](get_started.md#install-on-disconnected-networks)

- [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html-single/disconnected_environments/mirroring-in-disconnected-environments)

- [Operator SDK Integration with Operator Lifecycle Manager](https://sdk.operatorframework.io/docs/olm-integration/)

</div>

<a id="global-hub-install-disconnected"></a>

## Installing multicluster global hub in a disconnected environment

If your cluster is in a restricted network, you can deploy the multicluster global hub operator in the disconnected environment.

**Required access:** Cluster administrator

<div class="formalpara">

<div class="title">

Prerequisites

</div>

You must meet the following requirements before you install multicluster global hub in a disconnected environment:

</div>

- An image registry and a bastion host must have access to both the internet and to your mirror registry.

- Install the Operator Lifecycle Manager on your cluster. See [Operator Lifecycle Manager (OLM)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/operators/index#operator-lifecycle-manager-olm).

- Install Red Hat Advanced Cluster Management for Kubernetes.

- Install the OpenShift Container Platform command line. See [Getting started with the OpenShift Container Platform CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started).

- Install the `opm` command line. See [Installing the opm CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/opm-cli#cli-opm-install).

- Install the `oc-mirror` plugin. See [Mirroring images for a disconnected installation by using the oc-mirror plugin v2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/disconnected_environments/mirroring-in-disconnected-environments#about-installing-oc-mirror-v2).

- You have set up a mirror registry during the OpenShift Container Platform cluster installation. Installing multicluster global hub in a disconnected environment involves the use of a local mirror image registry.

<div>

<div class="title">

Procedure

</div>

1.  Configure a mirror registry by creating operator packages in the mirror catalog with the `oc-mirror` plug-in. See the following substeps:

    **Notes:** Red Hat provides the multicluster global hub and AMQ Streams operators in the Red Hat operators catalog, which are delivered by the `registry.redhat.io/redhat/redhat-operator-index` index image. When you prepare your mirror of this catalog index image, you can choose to either mirror the entire catalog as provided by Red Hat, or you can mirror a subset that contains only the operator packages that you intend to use.

    If you are creating a full mirror catalog, no special considerations are needed as all of the packages required to install multicluster global hub and AMQ Streams are included. However, if you are creating a partial or filtered mirrored catalog, for which you identify particular packages to be included, you must to include the `multicluster-global-hub-operator-rh` and `amq-streams` package names in your list.

    1.  Create a local mirror registry of the `multicluster-global-hub-operator-rh` and `amq-streams` packages. You need a `ImageSetConfiguration` YAML file to configure and add the operator image. Your YAML file might resemble the following content, with the current version replacing `4.x`:

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
          - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.x
            packages:
            - name: multicluster-global-hub-operator-rh
            - name: amq-streams
          additionalImages: []
          helm: {}
        ```

    2.  Mirror the image set directly to the target mirror registry. Run the following command:

    ``` bash
    oc mirror --config=./imageset-config.yaml docker://myregistry.example.com:5000
    ```

    1.  Mirror the image set in a fully disconnected environment. For more details, see [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/disconnected_environments/mirroring-in-disconnected-environments#installing-mirroring-installation-images).

2.  Add the registry and catalog to your disconnected cluster to make your mirror registry and catalog available on your disconnected cluster. Complete the following substeps:

    1.  Disable the default catalog sources of Operator Hub. Run the following command to update the `OperatorHub` resource:

        ``` bash
        oc patch OperatorHub cluster --type json \
        -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
        ```

    2.  Mirror the Operator catalog by completing the procedure, [Mirroring the Operator catalog](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/operators/index#olm-mirror-catalog_olm-restricted-networks).

    3.  Add the `CatalogSource` resource for your mirrored catalog into the `openshift-marketplace` namespace. Your `CatalogSource` YAML file might be similar to the following example, with `4.x` set as the supported version. Take note of the value of the `metadata.name` field:

        ``` yaml
        apiVersion: operators.coreos.com/v1alpha1
        kind: CatalogSource
        metadata:
          name: my-mirror-catalog-source
          namespace: openshift-marketplace
        spec:
          image: myregistry.example.com:5000/mirror/my-operator-index:v4.x
          sourceType: grpc
          secrets:
          - <global-hub-secret>
        ```

    4.  Save the updated file.

    5.  Query the available `PackageManifest` resource to verify that the required packages are available from your disconnected cluster. Run the following command:

        ``` bash
        oc -n openshift-marketplace get packagemanifests
        ```

    6.  Ensure that the displayed list includes entries showing the `multicluster-global-hub-operator-rh` and `amq-streams` packages. Verify that the catalog source for your mirror catalog supplies these packages.

    7.  To change the build in the `amq-strimzi` catalog source, create a multicluster global hub annotation. Apply the following YAML resource:

    ``` yaml
    apiVersion: operator.open-cluster-management.io/v1alpha4
    kind: MulticlusterGlobalHub
    metadata:
      annotations:
        global-hub.open-cluster-management.io/strimzi-catalog-source-name: redhat-operators
        global-hub.open-cluster-management.io/strimzi-catalog-source-namespace: openshift-marketplace
        global-hub.open-cluster-management.io/strimzi-subscription-package-name: amq-streams
        global-hub.open-cluster-management.io/strimzi-subscription-channel: amq-streams-3.1.x
      name: multiclusterglobalhub
    spec:
      ......
    ```

3.  Configure the image registry. In order to have your cluster obtain container images for the multicluster global hub operator from your local mirror registry, rather than from the internet-hosted registries, you must configure an `ImageContentSourcePolicy` resource on your disconnected cluster to redirect image references to your mirror registry. The `ImageContentSourcePolicy` only support the image mirror with image **digest**.

    **Notes:**

    If you mirrored your catalog using the `oc adm catalog mirror` command, the image content source policy configuration is in the `imageContentSourcePolicy.yaml` file inside the `manifests-` directory that is created by that command.

    If you used the `oc-mirror` plug-in to mirror your catalog instead, the `imageContentSourcePolicy.yaml` file is within the `oc-mirror-workspace/results-` directory created by the `oc-mirror` plug-in.

    In either case, you can apply the policies to your disconnected command using an `oc apply` or `oc replace` command such as `oc replace -f ./<path>/imageContentSourcePolicy.yaml`. The image content source policy statements can vary based on how you created your mirror registry, but are similar to the following example:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ImageContentSourcePolicy
    metadata:
      labels:
        operators.openshift.org/catalog: "true"
      name: global-hub-operator-icsp
    spec:
      repositoryDigestMirrors:
      - mirrors:
        - myregistry.example.com:5000/multicluster-globalhub
        source: registry.redhat.io/multicluster-globalhub
      - mirrors:
        - myregistry.example.com:5000/openshift4
        source: registry.redhat.io/openshift4
      - mirrors:
        - myregistry.example.com:5000/redhat
        source: registry.redhat.io/redhat
      - mirrors:
        - myregistry.example.com:5000/rhel9
        source: registry.redhat.io/rhel9
      - mirrors:
        - myregistry.example.com:5000/amq-streams
        source: registry.redhat.io/amq-streams
    ```

    **Note:** You can configure different image registries for different managed hubs with the `ManagedClusterImageRegistry`. See [Importing a cluster that has a ManagedClusterImageRegistry](clusters.md#import-cluster-managedclusterimageregistry) to use the `ManagedClusterImageRegistry` API to replace the agent image. The following `Label` and `Annotation` are added to the selected `ManagedCluster` resource. The agent image in the cluster is replaced with the mirror image:

    - Label: `multicluster-global-hub.io/image-registry=<namespace.managedclusterimageregistry-name>`

    - Annotation: `multicluster-global-hub.io/image-registries: <image-registry-info>`

4.  Configure the multicluster global hub image pull secret in an OpenShift Container Platform cluster. If the Operator or Operand images that are referenced by a subscribed Operator require access to a private registry, you can go to [Adding a catalog source to a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/operators/index#olm-creating-catalog-from-index_olm-managing-custom-catalogs) for more information. You can configure the image pull secret in an existing OpenShift Container Platform cluster.

    **Note:** Applying the image pull secret on a pre-existing cluster causes a rolling restart of all of the nodes.

    1.  Configure the pull secret by exporting the user name and password. Run the following command:

        ``` bash
        export USER=<the-registry-user>
        ```

    2.  Export the password from the pull secret. Run the following command:

        ``` bash
        export PASSWORD=<the-registry-password>
        ```

    3.  Copy the pull secret. Run the following command:

        ``` bash
        oc get secret/pull-secret -n openshift-config --template='{{index .data ".dockerconfigjson" | base64decode}}' > pull_secret.yaml
        ```

    4.  Log in using the pull secret. Run the following command:

        ``` bash
        oc registry login --registry=${REGISTRY} --auth-basic="$USER:$PASSWORD" --to=pull_secret.yaml
        ```

    5.  Specify the multicluster global hub image pull secret. Run the following command:

        ``` bash
        oc set data secret/pull-secret -n openshift-config --from-file=.dockerconfigjson=pull_secret.yaml
        ```

    6.  Remove the old pull secret, then run the following command:

        ``` bash
        rm pull_secret.yaml
        ```

    7.  Configure the multicluster global hub image pull secret to an individual namespace. You can configure the image pull secret to an individual namespace. Create the secret in the tenant namespace by running the following command:

        ``` bash
        oc create secret generic <secret_name> -n <tenant_namespace> \
        --from-file=.dockerconfigjson=<path/to/registry/credentials> \
        --type=kubernetes.io/dockerconfigjson
        ```

    8.  Link the secret to the service account for your operator or operand:

    ``` bash
    oc secrets link <operator_sa> -n <tenant_namespace> <secret_name> --for=pull
    ```

5.  Install the multicluster global hub Operator. You can install and subscribe an Operator from the Red Hat OpenShift Software Catalog. See [Adding Operators to a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/operators/administrator-tasks#olm-adding-operators-to-a-cluster) for the procedure. After adding the Operator, you can check the status of the multicluster global hub Operator by running the following command:

    ``` bash
    oc get pods -n multicluster-global-hub
    NAME                                                READY   STATUS    RESTARTS   AGE
    multicluster-global-hub-operator-687584cb7c-fnftj   1/1     Running   0          2m12s
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Create a mirror registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/disconnected_environments/mirroring-in-disconnected-environments#creating-mirror-registry)

- [Mirroring in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/disconnected_environments/mirroring-in-disconnected-environments)

- [Mirroring an Operator catalog](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/operators/index#olm-mirror-catalog_olm-restricted-networks)

</div>

<a id="global-hub-install-acm"></a>

## Installing multicluster global hub on an existing Red Hat Advanced Cluster Management hub cluster

You can install multicluster global hub in an existing Red Hat Advanced Cluster Management hub cluster and enable the multicluster global hub agent in Red Hat Advanced Cluster Management. The multicluster global hub agent is automatically installed on an existing Red Hat Advanced Cluster Management hub cluster. Learn about the following capabilities:

- When you install multicluster global hub in an Red Hat Advanced Cluster Management hub cluster, Kafka receives the information from the multicluster global hub operator and stores it in the multicluster global hub database, giving you access to the clusters, policies, and events.

- Kafka stores the multicluster global hub operator information, so as a Kafka consumer, you can access other components. For example, you can integrate with Red Hat Advanced Cluster Security and Red Hat Event-Driven Ansible.

- Your data is stored in the multicluster global hub database so you can view the cluster and policy information in the Grafana dashboards.

<div>

<div class="title">

Procedure

</div>

1.  To install multicluster global hub on an existing Red Hat Advanced Cluster Management hub cluster, set the `installAgentOnLocal` field to `true` by applying the following YAML sample:

    ``` yaml
    apiVersion: operator.open-cluster-management.io/v1alpha4
    kind: MulticlusterGlobalHub
    metadata:
      name: multiclusterglobalhub
      namespace: multicluster-global-hub
    spec:
      enableMetrics: true
      installAgentOnLocal: true
      dataLayer:
        kafka:
          topics:
            specTopic: gh-spec
            statusTopic: gh-status
          consumerGroupPrefix: org1_
        postgres:
          retention: 18m
      availabilityConfig: High
    ```

    - `installAgentOnLocal`: Deploys multicluster global hub on the multicluster global hub cluster. If you set the value to `true`, the multicluster global hub operator installs the agent on the multicluster global hub cluster.

    - `specTopic`: Distributes workloads from multicluster global hub to managed hub clusters. The default value is `gh-spec`.

    - `statusTopic`: Reports events and status updates to the multicluster global hub manager. When a topic ends with an asterisk, the topic is intended for the individual managed hub clusters. The default value for all managed hub clusters is `gh-status`.

    - `consumerGroupPrefix`: Specifies the prefix for Kafka consumer groups. The final consumer group identification for multicluster global hub is `<prefix> + "global_hub"`, and for managed hub clusters it is `<prefix> + <managed-hub-name>`. In the final group identification, all hyphens, get changed to underscores. If you do not specify a value, the default consumer group is the name of the hubs without any prefix.

    - `availabilityConfig`: Specifies the replication of deployments to improve their availability. For the values of the replications, you have the options of `Basic` and `High`. For the `High` value, the `availabilityConfig` creates one replica for the multicluster global hub manager and Grafana. It creates two replicas for the Kafka broker, which is a separate component in multicluster global hub. The default value is `High`.

2.  Create a `MultiClusterGlobalHub` custom resource by completing the following procedures. If you enabled the `MultiClusterObservability` custom resource in the Red Hat Advanced Cluster Management after you installed multicluster global hub, then any new update for the `MultiClusterObservability` custom resource does not take effect:

    - [Installing Multicluster Global Hub in a connected environment](global_hub.md#global-hub-install-connected)

    - [Installing Multicluster Global Hub in a disconnected environment](global_hub.md#global-hub-install-disconnected)

</div>

<a id="global-hub-integrating-kafka"></a>

## Integrating an existing version of Kafka

If you have your own instance of Kafka, you can use it as the transport for multicluster global hub.

<div>

<div class="title">

Procedure

</div>

1.  If you do not have a persistent volume for your Kafka instance, create one.

2.  Create a secret that is named `multicluster-global-hub-transport` in the `multicluster-global-hub` namespace.

    1.  Extract the information in the following required fields:

        - `bootstrap.servers`: Specifies the Kafka bootstrap servers.

        - `ca.crt`: Required if you use the `KafkaUser` custom resource to configure authentication credentials. See [User authentication](https://strimzi.io/docs/operators/latest/deploying.html#con-securing-client-authentication-str) in the Strimzi documentation for the required steps to extract the `ca.crt` certificate from the secret.

        - `client.crt`: Required. See [User authentication](https://strimzi.io/docs/operators/latest/deploying.html#con-securing-client-authentication-str) in the Strimzi documentation for the steps to extract the `user.crt` certificate from the secret.

        - `client.key`: Required. See [User authentication](https://strimzi.io/docs/operators/latest/deploying.html#con-securing-client-authentication-str) in the Strimzi documentation for the steps to extract the `user.key` from the secret.

    2.  Create the secret by running the following command, replacing the values with your extracted values where necessary:

    ``` bash
    oc create secret generic multicluster-global-hub-transport -n multicluster-global-hub \
        --from-literal=bootstrap_server=<kafka-bootstrap-server-address> \
        --from-file=ca.crt=<CA-cert-for-kafka-server> \
        --from-file=client.crt=<Client-cert-for-kafka-server> \
        --from-file=client.key=<Client-key-for-kafka-server>
    ```

3.  If automatic topic creation is configured on your Kafka instance, skip this step. If it is not configured, create the `spec` and `status` topics manually.

4.  Ensure that the multicluster global hub user that accesses Kafka has permission to read data from the topics and write data to the topics.

</div>

<a id="global-hub-integrating-postgres"></a>

## Integrating an existing version of PostgreSQL

If you have your own PostgreSQL relational database, you can use it as the storage for multicluster global hub. The minimum required storage size is 20 GB. This amount can store three managed hubs with 250 managed clusters and 50 policies per managed hub for 18 months.

<div>

<div class="title">

Prerequisites

</div>

- Create a secret that is named `multicluster-global-hub-storage` in the `multicluster-global-hub` namespace. The secret must contain the following fields:

  - `database_uri`: Used to create the database and insert data. Your value must resemble the following format: `postgres://<user>:<password>@<host>:<port>/<database>?sslmode=<mode>`.

  - `database_uri_with_readonlyuser`: Used to query data by the instance of Grafana that is used by multicluster global hub. This value is optional. Your value must resemble the following format: `postgres://<user>:<password>@<host>:<port>/<database>?sslmode=<mode>`.

  - `ca.crt`: Optional, based on the `sslmode` value.

- Verify that your cluster has the minimum required storage size of 20 GB.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the secret by running the following command:

    ``` bash
    oc create secret generic multicluster-global-hub-storage -n multicluster-global-hub \
        --from-literal=database_uri=<postgresql-uri> \
        --from-literal=database_uri_with_readonlyuser=<postgresql-uri-with-readonlyuser> \
        --from-file=ca.crt=<CA-for-postgres-server>
    ```

    The host must be accessible from the multicluster global hub cluster. If your PostgreSQL database is in a Kubernetes cluster, consider using the service type with `nodePort` or `LoadBalancer` to expose the database. For more information, see [Accessing the provisioned PostgreSQL database for troubleshooting](troubleshooting.md).

</div>

<a id="global-hub-integrating-grafana"></a>

## Integrating an existing version of Grafana

Using an existing Grafana instance might work with multicluster global hub if you rely on your own Grafana to get metrics from multiple sources, such as Prometheus, from different clusters and you aggregate the metrics yourself. To get multicluster global hub data into your own Grafana, configure the data source and import the dashboards.

<div>

<div class="title">

Procedure

</div>

1.  Collect the PostgreSQL connection information from the multicluster global hub Grafana `datasource` secret by running the following command:

    ``` bash
    oc get secret multicluster-global-hub-grafana-datasources -n multicluster-global-hub -ojsonpath='{.data.datasources\.yaml}' | base64 -d
    ```

    The output resembles the following example:

    ``` yaml
    apiVersion: 1
    datasources:
    - access: proxy
      isDefault: true
      name: Global-Hub-DataSource
      type: postgres
      url: postgres-primary.multicluster-global-hub.svc:5432
      database: hoh
      user: guest
      jsonData:
        sslmode: verify-ca
        tlsAuth: true
        tlsAuthWithCACert: true
        tlsConfigurationMethod: file-content
        tlsSkipVerify: true
        queryTimeout: 300s
        timeInterval: 30s
      secureJsonData:
        password: xxxxx
        tlsCACert: xxxxx
    ```

2.  Configure the `datasource` in your own Grafana instance by adding a source, such as PostgreSQL, and complete the required fields with the information that you previously extracted.

    See the following required fields:

    - Name

    - Host

    - Database

    - User

    - Password

    - TLS/SSL Mode

    - TLS/SSL Method

    - CA Cert

3.  If your Grafana is not in the multicluster global hub cluster, expose PostgreSQL by using the `LoadBalancer` so that PostgreSQL can be accessed from outside. Add the following value into the `PostgresCluster` operand:

    ``` yaml
    service:
      type: LoadBalancer
    ```

    After you add that content, get the `EXTERNAL-IP` from the `postgres-ha` service. See the following example:

    ``` bash
    oc get svc postgres-ha -n multicluster-global-hub
    NAME          TYPE           CLUSTER-IP      EXTERNAL-IP                        PORT(S)          AGE
    postgres-ha   LoadBalancer   172.30.227.58   xxxx.us-east-1.elb.amazonaws.com   5432:31442/TCP   128m
    ```

    After running that command, you can use `xxxx.us-east-1.elb.amazonaws.com:5432` as the PostgreSQL connection host.

4.  Import the existing dashboards.

    1.  Follow the steps in [Export and import dashboards](https://grafana.com/docs/grafana/latest/dashboards/manage-dashboards/#export-and-import-dashboards) in the official Grafana documentation to export the dashboard from the existing Grafana instance.

    2.  Follow the steps in [Export and import dashboards](https://grafana.com/docs/grafana/latest/dashboards/manage-dashboards/#export-and-import-dashboards) in the official Grafana documentation to import a dashboard into the multicluster global hub Grafana instance.

</div>

<a id="global-hub-importing-managed-hub-in-default-mode"></a>

## Importing a managed hub cluster in the default mode

Import an existing hub cluster as a managed hub cluster to help you control your different environments when you develop and deploy your applications.

<div>

<div class="title">

Prerequisites

</div>

- Disable the cluster self-management setting in the existing hub cluster by setting the `disableHubSelfManagement` setting to `true` in the `multiclusterhub` custom resource. This setting disables the automatic import of the hub cluster as a managed cluster.

  1.  Import the managed hub cluster by completing the steps in [Cluster import introduction](clusters.md#import-intro).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the label `global-hub.open-cluster-management.io/deploy-mode=default` to the `managedcluster` when you import the managed hub cluster.

2.  Check the multicluster global hub agent status to ensure that the agent is running in the managed hub cluster. Run the following command:

    ``` bash
    oc get managedclusteraddon multicluster-global-hub-controller -n <managed_hub_cluster_name>
    ```

3.  If you upgrade multicluster global hub, manually add the label `global-hub.open-cluster-management.io/deploy-mode=default` to all the managed hub clusters.

</div>

<a id="global-hub-importing-in-hosted-mode"></a>

## Importing a managed hub cluster in the hosted mode

To enable `local-cluster` on your managed hub cluster, you must import it in the hosted mode.

When you import an existing managed hub cluster in the hosted mode, you only get support for imported managed hub clusters that use a `kubeconfig` file. Red Hat Advanced Cluster Management for Kubernetes uses this `kubeconfig` file to generate the `auto-import-secret` which connects to your managed hub cluster. In the hosted mode, multicluster global hub does not support backup and restore.

<div>

<div class="title">

Prerequisites

</div>

- Enable the `local-cluster` in the multicluster global hub cluster.

- Install the latest Red Hat Advanced Cluster Management version.

- Make sure this `kubeconfig` file is always usable. If it expires, regenerate the `auto-import-secret` in the managed hub cluster namespace with the following command:

  ``` bash
  oc create secret generic auto-import-secret --from-file=kubeconfig=./managedClusterKubeconfig -n <Managedhub Namespace>
  ```

</div>

<div>

<div class="title">

Procedure

</div>

- Import your managed hub cluster by setting the label `global-hub.open-cluster-management.io/deploy-mode=hosted` to `managedcluster`. With this label, multicluster global hub does the following actions:

- Imports the new managed hub cluster in the hosted mode.

- Installs the multicluster global hub agent in the new managed hub cluster that uses the hosted mode.

- Disables the following `addons` in the new managed hub cluster namespaces: `applicationManager`, `certPolicyController`, and `policyController`.

- Changes the following managed hub clusters `addons` that are related to the new namespace: `work-manager`,`cluster-proxy`, and `managed-serviceaccount`.

- Changes these namespaces to `open-cluster-management-global-hub-agent-addon`.

</div>

<a id="global-hub-accessing-grafana-data"></a>

## Access the Grafana data

The Grafana data is exposed through the route. The authentication method of this URL is same as authenticating to the Red Hat OpenShift Container Platform console. You can run the following command to display the login URL and then learn about ways to use the Grafana dashboards:

``` bash
oc get route multicluster-global-hub-grafana -n <the-namespace-of-multicluster-global-hub-instance>
```

- View policy status with Grafana dashboards

  After accessing the global hub Grafana data, you can monitor the policies that were configured through the hub cluster environments that are managed.

  From the multicluster global hub dashboard, you can identify the compliance status of the policies of the system over a selected time range. The policy compliance status is updated daily, so the dashboard does not display the status of the current day until the following day.

  To navigate the multicluster global hub dashboards, you can observe and filter the policy data by grouping them by `policy` or by `cluster`.

  If you prefer to examine the policy data by using the `policy` grouping, start from the and the dashboard called `Global Hub - Policy Group Compliancy Overview`.

  This dashboard allows you to filter the policy data based on `standard`, `category`, and `control`. After selecting a specific point in time on the graph, you are directed to the `Global Hub - Offending Policies` dashboard. The `Global Hub - Offending Policies` dashboard lists the non-compliant or unknown policies at that time. After selecting a target policy, you can view related events and see what has changed by accessing the `Global Hub - What’s Changed / Policies` dashboard.

  Similarly, if you want to examine the policy data by `cluster` grouping, begin by using the `Global Hub - Cluster Group Compliancy Overview` dashboard. The navigation flow is identical to the `policy` grouping flow, but you select filters that are related to the cluster, such as managed cluster `labels` and `values`. Instead of viewing policy events for all clusters, after reaching the `Global Hub - What’s Changed / Clusters` dashboard, you can view policy events related to an individual cluster.

- View Strimzi information with Grafana dashboards

  To understand the health and performance of your Kafka deployment and Postgres database, collect their metrics. When you check the metrics, you can identify issues before they become critical and make informed decisions about resource allocation and capacity planning. If you do not collect and check the metrics, you might have limited visibility into the behavior of your Kafka deployment, making troubleshooting more difficult.

  You can check the dashboards and their metrics in the multicluster global hub Grafana. In the Strimzi folder, you can view the following dashboards:

  - multicluster global hub - Strimzi Operator

  - multicluster global hub - Strimzi Kafka

  - multicluster global hub - Strimzi Kraft

- View Postgres information with Grafana dashboards (Technology Preview)

  To understand the health and performance of your Postgres config, collect and check the Postgres metrics in the Grafana dashboard. In the Postgres folder, you can view the following dashboard: multicluster global hub - PostgresSQL Database

- View cluster information with Grafana dashboards

  To filter your managed clusters and to view their details and events, use the Grafana dashboards. With the Grafana dashboard, you can filter your managed clusters based on: `hub`, `labels` and `name`. Additionally, you can view the distribution of your managed clusters based on: `hub`, `status`, `cloud`, and `version`.

  In the Cluster folder, you can view the multicluster global hub *Cluster Overview* dashboard.

<a id="global-hub-grafana-alerts"></a>

## Grafana alerts (Technology Preview)

You can configure three Grafana alerts, which are stored in the `multicluster-global-hub-default-alerting` config map. These alerts notify you of suspicious policies, suspicious clusters compliance status change, and failed cron jobs.

See the following descriptions of the alerts:

Suspicious policy change  
This alert rule watches the suspicious policies change. If the following events occur more than five times in one hour, it creates notifications.

- A policy was enabled or disabled.

- A policy was updated.

Suspicious cluster compliance status change  
This alert rule watches the cluster compliance status and policy events for a cluster. There are two rules in this alert:

- Cluster compliance status changes frequently: If a cluster compliance status changes from `compliance` to `non-compliance` more than three times in one hour, it creates notifications.

- Too many policy events in a cluster: For a policy in a cluster, if there are more than 20 events in five minutes, it creates notifications. If this alert is always firing, the data in the `event.local_policies` table increases too fast.

Cron Job failed  
This alert watches the cron jobs that are described in [multicluster global hub cron job settings](global_hub.md#global-hub-configuring-cronjobs) for failed events. There are two rules in this alert:

- Local compliance job failed: If this alert rule creates notifications, it means the local compliance status synchronization job failed. It might cause the data in the `history.local_compliance` table to be lost. Run the job manually, if necessary.

- Data retention job failed: If this alert rule starts creating notifications, it means the data retention job failed. You can run it manually.

<a id="global-hub-customize-grafana-alert"></a>

## Customize Grafana alerting resources

The multicluster global hub supports creating custom Grafana alerts. Complete the following steps to customize your Grafana alerts and Grafana alerting resources. See [Create and manage alerting resources using file provisioning](https://grafana.com/docs/grafana/v10.1/alerting/set-up/provision-alerting-resources/file-provisioning/) in the Grafana documentation.

<div>

<div class="title">

Procedure

</div>

1.  To customize your `grafana.ini` file, create a secret that is named `multicluster-global-hub-custom-grafana-config` in the namespace where you installed your multicluster global hub operator. The secret data key is `grafana.ini`, as seen in the following example. Replace the required information with your own credentials:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: multicluster-global-hub-custom-grafana-config
      namespace: multicluster-global-hub
    type: Opaque
    stringData:
      grafana.ini: |
        [smtp]
        enabled = true
        host = smtp.google.com:465
        user = <example@google.com>
        password = <password>
        ;cert_file =
        ;key_file =
        skip_verify = true
        from_address = <example@google.com>
        from_name = Grafana
        ;ehlo_identity = dashboard.example.com
    ```

    - The `ehlo_identity` in the `SMTP` dialog defaults to `instance_name`.

    - You cannot configure the section that already contains the `multicluster-global-hub-default-grafana-config` secret.

2.  Customize the alerting resources. Create a config map that is named `multicluster-global-hub-custom-alerting` in the `multicluster-global-hub` namespace. The config map data key is `alerting.yaml`, as in the following example:

    ``` yaml
    apiVersion: v1
    data:
      alerting.yaml: |
        contactPoints:
          - orgId: 1
            name: globalhub_policy
            receivers:
              - uid: globalhub_policy_alert_email
                type: email
                settings:
                  addresses: <example@redhat.com>
                  singleEmail: false
              - uid: globalhub_policy_alert_slack
                type: slack
                settings:
                  url: <Slack-webhook-URL>
                  title: |
                    {{ template "globalhub.policy.title" . }}
                  text: |
                    {{ template "globalhub.policy.message" . }}
        policies:
          - orgId: 1
            receiver: globalhub_policy
            group_by: ['grafana_folder', 'alertname']
            matchers:
              - grafana_folder = Policy
            repeat_interval: 1d
        deleteRules:
          - orgId: 1
            uid: [Alert Rule Uid]
        muteTimes:
          - orgId: 1
            name: mti_1
            time_intervals:
              - times:
                  - start_time: '06:00'
                    end_time: '23:59'
                    location: 'UTC'
                weekdays: ['monday:wednesday', 'saturday', 'sunday']
                months: ['1:3', 'may:august', 'december']
                years: ['2020:2022', '2030']
                days_of_month: ['1:5', '-3:-1']
    kind: ConfigMap
    metadata:
      name: multicluster-global-hub-custom-alerting
      namespace: multicluster-global-hub
    ```

</div>

<a id="global-hub-delete-grafana-rule"></a>

## Delete Grafana alert rules

If the default Grafana alert rules do not provide useful information, you can delete the Grafana alert rule by including a `deleteRules` section in the `multicluster-global-hub-custom-alerting` config map. See [Customize Grafana alerting resources](global_hub.md#global-hub-customize-grafana-alert) for more information about the `multicluster-global-hub-custom-alerting` config map.

To delete all of the default alerts, the `deleteRules` configuration section should resemble the following example:

        deleteRules:
          - orgId: 1
            uid: globalhub_suspicious_policy_change
          - orgId: 1
            uid: globalhub_cluster_compliance_status_change_frequently
          - orgId: 1
            uid: globalhub_high_number_of_policy_events
          - orgId: 1
            uid: globalhub_data_retention_job
          - orgId: 1
            uid: globalhub_local_compliance_job

<a id="migration-intro"></a>

## multicluster global hub managed cluster migration

Cluster migration enables you to move managed clusters from one Red Hat Advanced Cluster Management hub cluster to another, providing an alternative to in-place upgrades. You can gradually migrate managed clusters and validate each status before decommissioning the original hub cluster. Zero Touch Provisioning (ZTP) migration facilitates the transfer of fully provisioned, bare-metal clusters, while maintaining cluster state, configuration, and OpenShift GitOps management throughout the transition.

**Required access:** Cluster administrator

- [Zero Touch Provisioning migration overview](global_hub.md#ztp-migration-overview)

- [Preparing the hub clusters for migration](global_hub.md#preparing-hubs-for-migration)

- [Verifying the source hub cluster status for migration](global_hub.md#ztp-migration-verify-hub)

- [Applying policy to the target hub cluster for migration](global_hub.md#ztp-apply-policy-hub)

- [Creating a *ManagedClusterMigration* resource to migrate a static list](global_hub.md#ztp-create-resource-static)

- [Creating a *ManagedClusterMigration* resource to migrate a dynamic placement](global_hub.md#ztp-create-resource-dynamic)

- [Verifying the migration resource status](global_hub.md#ztp-create-resource-verify)

- [Monitoring migration progress](global_hub.md#ztp-monitor-migration)

- [Applying *ClusterInstance* applications to the target hub cluster](global_hub.md#ztp-monitor-migration)

- [Cleaning up the source hub cluster](global_hub.md#ztp-clean-up-source-hub)

- [Rolling back cluster migration](global_hub.md#rolling-back-migration)

<a id="ztp-migration-overview"></a>

## Zero Touch Provisioning migration overview

Zero Touch Provisioning (ZTP) migration facilitates the transfer of fully provisioned, bare-metal clusters, such as single-node OpenShift, from a *source* Red Hat Advanced Cluster Management hub cluster to a *target* hub cluster. Migration maintains the cluster state, configuration, and OpenShift GitOps management throughout the transition.

The ZTP migration procedure automatically transfers several resource categories from the source hub cluster to the target hub cluster to ensure continuity with the following processes:

Pre-migration verification  
Verify the clusters on the source hub cluster to ensure migration readiness.

Apply policy applications  
Manually apply policy applications from the source hub cluster to the target hub cluster.

Create migration resource  
Manually create the migration resource on the global hub cluster to initiate the process.

Migration execution  
The multicluster global hub cluster automatically transfers resources and registers clusters to the target hub cluster.

Apply `ClusterInstance` applications  
Manually apply the `ClusterInstance` applications to the target hub cluster.

Verify migration  
On the target hub cluster, verify that all clusters are available, test cluster operations, and confirm policy compliance.

Cleanup source hub cluster  
Manually delete the OpenShift GitOps applications and the `ClusterInstance` resources from the source hub cluster.

- Supported versions of Red Hat Advanced Cluster Management and OpenShift Container Platform for migration

See the following version compatibility for migration:

| Component | Source hub cluster | Target hub cluster | Notes |
|----|----|----|----|
| Red Hat Advanced Cluster Management | Version `N` | Version `N to N+1`, and EUS version support | None |
| OpenShift Container Platform | Version `4.x` | Version `4.x` | Compatible with Red Hat Advanced Cluster Management version |
| multicluster global hub | None | Latest stable | Installed on the target hub cluster only |

Version requirements for hub cluster components

- Core resources that are included

The following resources are included in the migration process:

`ManagedCluster`  
Facilitates cluster registration and management.

`KlusterletAddonConfig`  
Defines add-on configurations for managed clusters.

- Deployment resources that are included

The following deployment resources are included in the migration:

`ClusterDeployment`  
Contains Hive deployment configuration while preserving status.

`ImageClusterInstall`  
Manages image-based installation configuration while preserving status.

- Secrets that are included

The following secrets are included in the migration:

| Secret type | Description |
|----|----|
| Administrative credentials | The `<cluster-name>-admin-password` secret. |
| Administrative Kubeconfig | The `<cluster-name>-admin-kubeconfig` secret. |
| Metadata | The `<cluster-name>-metadata-json` secret. |
| Seed reconfiguration | The `<cluster-name>-seed-reconfiguration` secret. |
| Network secrets | Secrets that contain the `siteconfig.open-cluster-management.io/sync-wave` annotation. |
| BMC credentials | Secrets referenced in the `BareMetalHost.spec.bmc.credentialsName` field. |
| Pull secrets | Secrets that are referenced in the `ClusterDeployment.spec.pullSecretRef.name` field. |

Secrets that are included in the migration

- Config maps that are included

The following config maps are included in the migration:

Extra Manifests  
Config maps that are referenced in `ImageClusterInstall.spec.extraManifestsRefs`

- Bare metal resources that are included

The following bare metal resources with status preserved are included in the migration:

`BareMetalHost`  
Physical server inventory and state

`HostFirmwareSettings`  
BIOS and firmware configurations

`FirmwareSchema`  
Firmware setting schemas

`HostFirmwareComponents`  
Individual firmware components

- Resources that are *not* included in the migration

`ClusterInstance` Resources  
Resources that are managed by Argo CD. Manually apply OpenShift GitOps applications to the target hub cluster after cluster migration.

`Policy Resources`  
Resources that are used for polices. Use OpenShift GitOps applications to re-deploy on the target hub cluster.

`Application Resources`  
Configuration for OpenShift GitOps applications managing clusters.

See [Preparing the hub clusters for migration](global_hub.md#preparing-hubs-for-migration) for more information about preparing the hub clusters for migration.

<a id="preparing-hubs-for-migration"></a>

## Preparing the hub clusters for migration

To migrate managed clusters between hub clusters, you must configure the target hub cluster to match the source hub cluster environment and establish connectivity through the multicluster global hub.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Ensure all managed clusters are connected by network to the target hub cluster.

- Verify version compatibility. See [Zero Touch Provisioning migration overview](global_hub.md#ztp-migration-overview) for supported versions of Red Hat Advanced Cluster Management and OpenShift Container Platform.

- Install the Red Hat Advanced Cluster Management operator on the target hub cluster. See [Get started with Red Hat Advanced Cluster Management](get_started.md#get-started-acm).

- Become familiar with the `siteconfig` operator. See *SiteConfig operator* in the *Additional resources* section.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file to enable the `siteconfig` operator as you see in the following example where `siteconfig` is set to `enabled: true`:

    ``` yaml
    apiVersion: operator.open-cluster-management.io/v1
    kind: MultiClusterHub
    metadata:
      name: multiclusterhub
      namespace: open-cluster-management
    spec:
      overrides:
        components:
          - name: siteconfig
            enabled: true
    ```

2.  Apply the file to your cluster. Run the following command:

    ``` bash
    oc apply -f mch-siteconfig.yaml
    ```

3.  Verify that the `siteconfig-controller-manager` deployment is in the `available` status. Run the following command:

    ``` bash
    oc get deployment -n open-cluster-management siteconfig-controller-manager
    ```

4.  Prepare the target hub cluster for Zero Touch Provisioning (ZTP). See the [Enable the SiteConfig operator](mce_acm_integration.md#enable-sco) documentation.

5.  **Optional:** If the observability feature is enabled on the source hub cluster, configure it on the target hub cluster. See *Enabling the observability service* in the *Additional resources* section.

6.  Install the multicluster global hub operator on the target hub cluster. See the [multicluster global hub](global_hub.md#multicluster-global-hub) documentation for directions.

7.  Create a YAML file to enable the `ManagedServiceAccount` component. See the following example where `managedserviceaccount` component is set to `enabled: true`:

    ``` yaml
    apiVersion: multicluster.openshift.io/v1
    kind: MultiClusterEngine
    metadata:
      name: multiclusterengine
    spec:
      overrides:
        components:
          - name: managedserviceaccount
            enabled: true
    ```

8.  Apply the file to your cluster. Run the following command:

    ``` bash
    oc apply -f mce-msa.yaml
    ```

9.  Import the source hub cluster as a managed hub cluster to the multicluster global hub. **Important:** You must include the `global-hub.open-cluster-management.io/deploy-mode: hosted` label during the import process for the migration to function. For detailed instructions, see [Cluster import](clusters.md#import-intro).

</div>

<div>

<div class="title">

Additional resources

</div>

- [SiteConfig operator](mce_acm_integration.md#siteconfig)

- [multicluster global hub](global_hub.md#multicluster-global-hub)

</div>

<a id="ztp-migration-verify-hub"></a>

## Verifying the source hub cluster status for migration

Before you initiate the ZTP cluster migration process, verify the current state and resource health of the managed clusters on the source hub cluster to ensure eligibility for transfer.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Configure OpenShift Container Platform to run `oc` commands. See [Getting started with the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started) for information about installing and configuring the command-line tool.

</div>

<div>

<div class="title">

Procedure

</div>

1.  List the managed clusters to identify the candidates for migration by running the following command:

    ``` bash
    oc get managedcluster
    ```

2.  Verify that the output displays `True` for the `JOINED` and `AVAILABLE` columns for all clusters you intend to migrate as you see in the following example for `sno1`, `sno2`, `sno1`:

    ``` bash
    NAME   HUB ACCEPTED   MANAGED CLUSTER URLS   JOINED   AVAILABLE   AGE
    sno1   true                                  True     True        30d
    sno2   true                                  True     True        25d
    sno3   true                                  True     True        20d
    ```

3.  Check the status of the `ClusterInstance` resources to ensure provisioning is complete. Run the following command:

    ``` bash
    oc get clusterinstance -A
    ```

4.  See the following output example to check for a `completed` status on all clusters. **Important:** You can only migrate clusters that display `Completed` in the `PROVISIONSTATUS` column. If a cluster is still provisioning, wait for the process to complete before proceeding:

    ``` bash
    NAMESPACE   NAME   PAUSED   PROVISIONSTATUS   PROVISIONDETAILS         AGE
    sno1        sno1            Completed         Provisioning completed   30d
    ```

5.  Verify the `ImageClusterInstall` resources to ensure the installation requirements are met. Run the following command:

    ``` bash
    oc get imageclusterinstall -A
    ```

6.  Confirm that each cluster shows `ClusterInstallationSucceeded` in the `COMPLETED` column and `HostValidationSucceeded` in the `REQUIREMENTSMET` column. Other states indicate that the installation is incomplete or has encountered errors. See the following output:

    ``` bash
    NAMESPACE   NAME   REQUIREMENTSMET           COMPLETED                      BAREMETALHOSTREF
    sno1        sno1   HostValidationSucceeded   ClusterInstallationSucceeded   sno1
    sno2        sno2   HostValidationSucceeded   ClusterInstallationSucceeded   sno2
    sno3        sno3   HostValidationSucceeded   ClusterInstallationSucceeded   sno3
    ```

7.  Check the `ClusterDeployment` resources to confirm the operational state of the clusters:

    ``` bash
    oc get clusterdeployment -A
    ```

8.  Verify that the `PROVISIONSTATUS` value is `Provisioned` and the `POWERSTATE` is `Running` in the output. This status indicates that the cluster deployment is successful and the cluster is ready for migration. See the following example output:

    ``` bash
    NAMESPACE   NAME   INFRAID       PLATFORM        REGION   VERSION   CLUSTERTYPE   PROVISIONSTATUS   POWERSTATE   AGE
    sno1        sno1   sno1-abc123   none-platform            4.x.x                   Provisioned       Running      30d
    sno2        sno2   sno2-def456   none-platform            4.x.x                   Provisioned       Running      25d
    sno3        sno3   sno3-ghi789   none-platform            4.x.x                   Provisioned       Running      20d
    ```

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

See [Applying policy to the target hub cluster for migration](global_hub.md#ztp-apply-policy-hub) for information about the next steps in the migration process.

</div>

<a id="ztp-apply-policy-hub"></a>

## Applying a policy to the target hub cluster for migration

In Zero Touch Provisioning (ZTP) deployments, Red Hat Advanced Cluster Management policies are managed through Argo CD applications. These policies control cluster configuration, compliance, and governance. You must apply policy applications to the target hub cluster before you create the migration resource. This sequence ensures that policies are ready to apply to clusters as soon as the migration completes.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You have access to the source hub cluster and the target hub cluster by using the OpenShift Container Platform command-line tool (`oc`).

- The `openshift-gitops` operator is installed on both hub clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On the source hub cluster, export the policy applications by running the following command:

    ``` bash
    oc get application -n openshift-gitops -l app=policies -o yaml > policies-app.yaml
    ```

2.  Switch your command-line to the target hub cluster and apply the policy applications to the target hub cluster. Run the following command:

    ``` bash
    oc apply -f policies-app.yaml
    ```

3.  Verify that the policy applications are synchronized and the policies are created. Run the following commands to check that policy applications are created and synced. Wait for all policy applications to show a healthy state before you proceed to the next migration process. This process might take one or two minutes:

    ``` bash
    oc get application -n openshift-gitops -l app=policies

    oc get policy -A
    ```

    **Important:** Do not create the migration resource until the policy applications are fully synchronized. If policies are missing during migration, the clusters might fail to reach a compliant state.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

See [Creating a *ManagedClusterMigration* resource to migrate a static list](global_hub.md#ztp-create-resource-static) or [Creating a *ManagedClusterMigration* resource to migrate a dynamic placement](global_hub.md#ztp-create-resource-dynamic) for the next steps.

</div>

<a id="ztp-create-resource-static"></a>

## Creating a *ManagedClusterMigration* resource to migrate a static list

To start the multicluster global hub ZTP cluster migration, you must create a `ManagedClusterMigration` custom resource. You can define the clusters to migrate by using a *static* list, or by using a *dynamic* placement resource. If you have a *static* list of managed clusters to migrate, use this procedure to create the migration resource.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create a file that is named `migration-static.yaml` with the following content where the `local-cluster` and the `hub2` represents the source cluster and target clusters:

    ``` yaml
    apiVersion: global-hub.open-cluster-management.io/v1alpha1
    kind: ManagedClusterMigration
    metadata:
      name: ztp-sno-migration
      namespace: multicluster-global-hub
    spec:
      to: local-cluster
      from: hub2
      includedManagedClusters:
        - sno1
        - sno2
        - sno3
      supportedConfigs:
        stageTimeout: 15m
    ```

2.  Apply the resource to the multicluster global hub by running the following command:

    ``` bash
    oc apply -f migration-static.yaml
    ```

</div>

<div>

<div class="title">

Next steps

</div>

1.  Proceed to [Verifying the migration resource status](global_hub.md#ztp-create-resource-verify).

</div>

<a id="ztp-create-resource-dynamic"></a>

## Creating a *ManagedClusterMigration* resource to migrate a dynamic placement

To start the multicluster global hub ZTP cluster migration, you must create a `ManagedClusterMigration` custom resource. You can define the clusters to migrate by using a *static* list, or by using a *dynamic* placement resource. Use this procedure to select clusters that are based on labels and dynamic placement rules.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create a file that is named `migration-placement.yaml` with the following content to define the `clusterSet` binding and `Placement` in the multicluster global hub agent namespace, `multicluster-global-hub-agent`, on the source hub cluster:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta2
    kind: ManagedClusterSetBinding
    metadata:
      name: global
      namespace: multicluster-global-hub-agent
    spec:
      clusterSet: global
    ---
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: migration-50
      namespace: multicluster-global-hub-agent
    spec:
      numberOfClusters: 50
      clusterSets:
        - global
      predicates:
        - requiredClusterSelector:
            labelSelector:
              matchExpressions:
                - key: local-cluster
                  operator: NotIn
                  values:
                    - "true"
    ```

2.  Apply the placement resources to the source hub cluster by running the following command:

    ``` bash
    oc apply -f migration-placement.yaml
    ```

3.  Create a file named `migration-resource.yaml` with the following content to initiate the migration on the multicluster global hub:

    ``` yaml
    apiVersion: global-hub.open-cluster-management.io/v1alpha1
    kind: ManagedClusterMigration
    metadata:
      name: ztp-sno-migration
      namespace: multicluster-global-hub
    spec:
      to: local-cluster
      from: hub2
      includedManagedClustersPlacementRef: migration-50
      supportedConfigs:
        stageTimeout: 15m
    ```

4.  Apply the migration resource to the multicluster global hub by running the following command:

    ``` bash
    oc apply -f migration-resource.yaml
    ```

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

Continue to [Verifying the migration resource status](global_hub.md#ztp-create-resource-verify).

</div>

<a id="ztp-create-resource-verify"></a>

## Verifying the migration resource status

After you apply the migration resource, verify the progress of the migration.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Check the status of the `ManagedClusterMigration` resource by running the following command:

    ``` bash
    oc get managedclustermigration ztp-sno-migration -n multicluster-global-hub -o yaml
    ```

2.  Review the `status` section of the output. The migration is complete when the status indicates that all clusters have reached the `Completed` stage.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

See [Monitoring migration progress](global_hub.md#ztp-monitor-migration) to check the migration status.

</div>

<a id="ztp-monitor-migration"></a>

## Monitoring migration progress

After you start a cluster migration, you can monitor the progress by checking the migration phase and the status of individual clusters. The migration progresses through several distinct phases. You can view the current phase of the migration resource to understand the overall state of the operation.

The migration controller creates a `ConfigMap` to track the status of each cluster involved in the migration. Use this resource to identify which clusters succeeded and which require investigation.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Check the current migration phase by running the following command:

    ``` bash
    oc get managedclustermigration ztp-sno-migration -n multicluster-global-hub
    ```

2.  Review the `PHASE` column in the output. The following table describes the possible migration phases:

    |  |  |
    |----|----|
    | Phase | Description |
    | `Initializing` | The system is preparing the required resources for migration. |
    | `Deploying` | The system is transferring resources to the target hub cluster. |
    | `Registering` | The clusters are registering with the target hub cluster. |
    | `Completed` | The migration finished successfully. |
    | `RollingBack` | An automatic rollback is in progress because of a detected failure. See *Rolling back cluster migration* in *Additional resources*. |
    | `Failed` | The migration failed and requires manual intervention. |

    Migration phases

3.  View the migration tracking `configmap` by running the following command:

    ``` bash
    oc get configmap ztp-sno-migration -n multicluster-global-hub -o yaml
    ```

4.  Locate the `data` section in the output to see the list of successful and failed clusters. See the following example, where `"sno1","sno3"` clusters migrated successfully and the `"sno2"` cluster failed to migrate and requires further investigation.

    ``` yaml
    data:
      success: '["sno1","sno3"]'
      failure: '["sno2"]'
    ```

5.  See [Applying *ClusterInstance* applications to the target hub cluster](global_hub.md#ztp-monitor-migration) for information about how to proceed with the successful clusters. You might need to investigate the failed clusters. See *Rolling back cluster migration* in *Additional resources* for information about how to proceed if you encounter failures during migration.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Cleaning up the source hub cluster](global_hub.md#ztp-clean-up-source-hub)

- [Rolling back cluster migration](global_hub.md#rolling-back-migration)

</div>

<a id="ztp-apply-clusterinstance-hub"></a>

## Applying *ClusterInstance* applications to the target hub cluster

After the migration completes successfully, you must apply the `ClusterInstance` applications to the target hub cluster. `ClusterInstance` resources are managed by OpenShift GitOps and are not automatically migrated. `ClusterInstance` applications manage the declarative configuration of your Zero Touch Provisioning (ZTP) clusters, including `ClusterInstance` custom resources, cluster-specific secrets, and infrastructure configurations.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Ensure that the status for your migration is in the `Completed` phase before you attempt to apply `ClusterInstance` applications. Verify the status by running the following command:

  ``` bash
  oc get managedclustermigration -n multicluster-global-hub
  ```

</div>

<div>

<div class="title">

Procedure

</div>

1.  Export the applications that manage your `ClusterInstance` resources, secrets, and configurations. On the source hub cluster, export the `ClusterInstance` applications by running the following command:

    ``` bash
    oc get application -n openshift-gitops <clusterinstance-sno-clusters> -o yaml > clusterinstance-app.yaml
    ```

2.  Modify `ClusterInstance` resources in the Git repository to suppress the rendering of `BareMetalHost` and `ImageClusterInstall` manifests, which are migrated with their status preserved. You receive conflicts if you re-render these resources on the target hub cluster.

    1.  In your Git repository, locate the `ClusterInstance` definitions.

    2.  Add the `suppressedManifests` field to the `spec` section of each `ClusterInstance` resource. See the following example:

        ``` yaml
        apiVersion: siteconfig.open-cluster-management.io/v1alpha1
        kind: ClusterInstance
        metadata:
          name: sno1
          namespace: sno1
        spec:
          suppressedManifests:
            - BareMetalHost
            - ImageClusterInstall
        ```

    3.  Add and commit your changes to your Git repository. Run the following commands:

        ``` bash
        git add clusterinstance/*.yaml

        git commit -m "Add suppressedManifests to prevent re-rendering migrated resources"
        ```

    4.  Commit your changes with the following command:

    ``` bash
    git push origin main
    ```

3.  Apply the exported applications to the target hub cluster. Run the following command on the hub cluster:

    ``` bash
    oc apply -f clusterinstance-app.yaml
    ```

4.  Verify that the resources are reconciled and compliant. Check the status of the `ClusterInstance` resources by running the following command:

    ``` bash
    oc get clusterinstance -A
    ```

5.  From the output, ensure that the `PROVISIONSTATUS` is in the `Completed` phase, and that the `PROVISIONDETAILS` displays the `Provisioning completed`.

6.  Verify that the Red Hat Advanced Cluster Management policies are applied and compliant. Run the following command:

    ``` bash
    oc get policy -A
    ```

7.  Verify that the migrated managed clusters are available on the target hub cluster. Run the following command:

    ``` bash
    oc get managedcluster sno1,sno2,sno3
    ```

</div>

<a id="ztp-clean-up-source-hub"></a>

## Cleaning up the source hub cluster

After you verify that the clusters migrated successfully and are fully operational on the target hub cluster, you must remove the migration-related resources from the source hub cluster.

**Important:** The cleanup process is destructive and irreversible because it permanently deletes all `ManagedCluster` resources from the source hub cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Verify that common cluster operations, such as policy application and monitoring, are functioning correctly on the target hub cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On the source hub cluster, delete the `ClusterInstance` applications by running the following command. Deleting `ClusterInstance` resources initiates the `siteconfig` operator to clean up related resources, including `ClusterDeployment`, `ImageClusterInstall`, `BareMetalHost`, secrets, and the cluster namespace.

    ``` bash
    oc delete application clusterinstance-sno-clusters -n openshift-gitops
    ```

    **Important:** For clusters that migrated successfully, the multicluster global hub adds `pause` annotations to the `ClusterDeployment` and `ImageClusterInstall` resources to prevent the deletion of these resources from affecting the actual running clusters.

2.  On the source hub cluster, delete the `ClusterInstance` resources by running the following command:

    ``` bash
    oc delete clusterinstance <cluster_name> -n <cluster_namespace> --wait=false
    ```

3.  **Optional:** To delete multiple clusters simultaneously, run a loop script similar to the following example:

    ``` bash
    for cluster in sno1 sno2 sno3; do
      echo "Deleting ClusterInstance: ${cluster}"
      oc delete clusterinstance ${cluster} -n ${cluster} --wait=false
    done
    ```

4.  Verify that the namespaces and related resources that are associated with the migrated clusters are removed from the source hub cluster. Run the following command. If the cleanup is successful, the command returns no results for the specified clusters:

    ``` bash
    oc get namespace -A | grep -E 'sno1|sno2|sno3'
    ```

</div>

<a id="rolling-back-migration"></a>

## Rolling back cluster migration

For any problems with your cluster migration, the multicluster global hub attempts an *automatic* rollback to restore clusters to the source hub cluster. If an automatic rollback fails as a result of environmental issues, such as power outages or network disconnections, you can initiate a *manual* rollback after the environment recovers.

**Required access:** Cluster administrator

**Notes:**

- Rollback only affects clusters that failed the migration process. Clusters that migrated successfully remain on the target hub cluster and are not rolled back.

- During an automatic rollback, resources on the target hub cluster are removed, and the clusters remain managed by the source hub cluster. You can check the status of the automated rollback. You can also initiate a manual rollback by adding a specific annotation to the `ManagedClusterMigration` resource.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

There are no requirements for automatic rollback. However, before you initiate a manual rollback, ensure the following conditions are true:

</div>

- The source hub cluster is healthy and accessible.

- The target multicluster global hub cluster is healthy and accessible.

- All managed clusters are connected to both the source hub cluster and target hub cluster.

- The connection between the multicluster global hub and Kafka is healthy.

<div>

<div class="title">

Procedure

</div>

1.  Monitor the status of an automatic rollback by running the following command:

    ``` bash
    oc get managedclustermigration ztp-sno-migration -n multicluster-global-hub
    ```

2.  Check for a successful rollback. The migration resource enters the `Failed` phase, indicating the migration did not complete but the environment was restored.

3.  If you need to rollback manually, initiate a rollback by adding the `migration-request` annotation to the `ManagedClusterMigration` resource. Run the following command:

    ``` bash
    oc annotate managedclustermigration ztp-sno-migration -n multicluster-global-hub \
      global-hub.open-cluster-management.io/migration-request=rollback
    ```

4.  Monitor the progress and view the detailed status of the rollback by running the following commands:

    ``` bash
    oc get managedclustermigration ztp-sno-migration -n multicluster-global-hub

    oc describe managedclustermigration ztp-sno-migration -n multicluster-global-hub
    ```

5.  Verify the rollback success by checking the resource conditions. Run the following command:

    ``` bash
    oc get managedclustermigration ztp-sno-migration -n multicluster-global-hub -o yaml
    ```

6.  Check the output for a successful rollback, which contains the `ResourceRolledBack` and `ResourceCleaned` types with a status of `True`. See the following YAML example:

    ``` yaml
    status:
      conditions:
        - message: Registering rollback completed
          reason: ResourceRolledBack
          status: "True"
          type: ResourceRolledBack
        - message: Resources have been successfully cleaned up from the hub clusters
          reason: ResourceCleaned
          status: "True"
          type: ResourceCleaned
    ```

7.  In the terminal, switch to the source hub cluster and verify that the managed clusters are available. Run the following command:

    ``` bash
    oc get managedcluster <cluster_name>
    ```

</div>

<a id="global-hub-configuring-cronjobs"></a>

## multicluster global hub cron job settings

Learn about cron job settings of the multicluster global hub. After you install the multicluster global hub operand, the multicluster global hub manager runs and displays a job scheduler for you to schedule the following cron jobs:

Local compliance status sync job  
This cron job runs at midnight every day based on the policy status and events collected by the manager on the previous day. Run this job to summarize the compliance status and the change frequency of the policy on the cluster, and store them to the `history.local_compliance` table as the data source of the Grafana dashboards.

Data retention job  
Some data tables in multicluster global hub continue to grow over time, which normally can cause problems when the tables get too large. The following two actions help to minimize the issues that result from tables that are too large:

- Delete older data that is no longer needed.

- Enable partitioning on the large table to run queries and deletions on faster.

For event tables, such as the `event.local_policies` and the `history.local_compliance` that increase in size daily, range partitioning divides the large tables into smaller partitions. This process also creates the partition tables for the next month each time it is run.

For the policy and cluster tables, such as `local_spec.policies` and `status.managed_clusters`, the `deleted_at` indexes on the tables to improve performance when you delete.

You can change the duration of time that the data is retained by changing the `retention` setting on the multicluster global hub operand. The recommended minimum value is `1 month`, and the default value is `18 months`. The run interval of this job should be less than one month.

The listed cron jobs run every time the multicluster global hub manager starts. The local compliance status sync job is run once a day and can be run multiple times within the day without changing the result.

The data retention job is run once a week and also can be run many times per month without a change in the results.

The status of these jobs are are saved in the `multicluster_global_hub_jobs_status` metrics, which can be viewed from the console of the Red Hat OpenShift Container Platform cluster. A value of `0` indicates that the job ran successfully, while a value of `1` indicates failure.

<a id="global-hub-compliance-manual"></a>

## Running the summarization process manually

You can manually run the summarization process to restore the initial compliance state of the day when the job is not triggered or has not failed running. To manually run the summarization process, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Use the earlier compliance history from the day as the initial state for the recovery day history.

2.  Connect to the database. You can use clients such as `pgAdmin` and `tablePlush` to connect to the multicluster global hub database. Or, you can directly connect to the database on the cluster by running the following command:

    ``` bash
    oc exec -it multicluster-global-hub-postgresql-0 -n multicluster-global-hub -- psql -d hoh
    ```

3.  Decide the date when you want the summarization process to run, for example: `2023-07-06`. Find the local compliance job failure information from the dashboard metrics or the `history.local_compliance_job_log` table. In the example, the date is, `2023-07-06`, so you know that `2023-07-06` is the date when you need to manually run the summary processes.

4.  Recover the initial compliance of `2023-07-06` by running the following SQL:

    ``` bash
    -- call the func to generate the initial data of '2023-07-06' by inheriting '2023-07-05'
    CALL history.generate_local_compliance('2024-07-06');
    ```

</div>

<a id="global-hub-backup"></a>

## Backup for multicluster global hub (Technology Preview)

Use multicluster global hub with Red Hat Advanced Cluster Management backup and restore features for recovery solutions and to access basic resources. To learn more about how these features help you, see [backup and restore](business_continuity.md#backup-intro).

multicluster global hub also supports backup `postgres pvc` by using the `acm-hub-pvc-backup`. To ensure your multicluster global hub can support the backup `postgres pvc`, you must have the current version of VolySync and Red Hat Advanced Cluster Management. For detailed steps on backing up your data, see [acm-hub-pvc-backup](https://github.com/open-cluster-management-io/policy-collection/tree/main/community/CM-Configuration-Management/acm-hub-pvc-backup).

If you need to restore your multicluster global hub cluster, see [Backup and restore](business_continuity.md#backup-intro). Install the multicluster global hub operator but do not create the multicluster global hub custom resource (CR) because the CR is automatically restored.

<a id="global-search"></a>

## multicluster global hub search (Technology Preview)

Global search expands the search capabilities when you use multicluster global hub to manage your environment.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

You need to enable multicluster global hub.

</div>

<a id="_enabling_global_search"></a>

### Enabling global search

To enable global search, add the `global-search-preview=true` annotation to the `search-v2-operator` resource by running the following command:

``` bash
oc annotate search search-v2-operator -n open-cluster-management global-search-preview=true
```

The search operator is updated with the following status condition:

``` yaml
status:
  conditions:
    - lastTransitionTime: '2024-05-31T19:49:37Z'
      message: None
      reason: None
      status: 'True'
      type: GlobalSearchReady
```

<div>

<div class="title">

Additional resources

</div>

- [multicluster global hub overview](global_hub.md#multicluster-global-hub)

- [Search service](search.md#search-service)

</div>

<a id="global-hub-migrate"></a>

## Migrating managed clusters with multicluster global hub

**Technology Preview:** You can access the Managed Cluster Migration feature in multicluster global hub 1.5. You can migrate managed clusters from one Red Hat Advanced Cluster Management hub cluster to another and across versions, for example, from Red Hat Advanced Cluster Management 2.13 to Red Hat Advanced Cluster Management 2.14.

**Required access:** Cluster administrator

- [Managed cluster migration process](global_hub.md#global-hub-migrate-process)

- [Preparing your multicluster global hub environment for migration](global_hub.md#global-hub-migrate-prep)

- [Migrating managed clusters](global_hub.md#global-hub-migrate-clusters)

- [Tracking the migration status](global_hub.md#global-hub-migrate-status)

<a id="global-hub-migrate-process"></a>

## Managed cluster migration process

By using multicluster global hub to migrate your managed clusters, you have a unified process that helps you reorganize workloads, move clusters and their resources together, automate cluster registration and cleanup, and track individual steps with detailed status updates. To migrate your managed clusters, you need the following components:

- The multicluster global hub operator to organize the migration workflow.

- The `source` Red Hat Advanced Cluster Management hub cluster to manage the clusters and the associated resources.

- The `target` Red Hat Advanced Cluster Management hub cluster to receive the migrated clusters and the associated resources.

With multicluster global hub, you can manage large fleets of clusters by implementing the event-driven architecture of multicluster global hub. multicluster global hub connects itself to your managed hub clusters. With the multicluster global hub event-based design, you can enable multicluster global hub to communicate, organize, synchronize, and transfer resources and cluster states among all your hub clusters.

The managed cluster migration process requires coordination between a `source` and `target` Red Hat Advanced Cluster Management hub cluster. The `multicluster-global-hub-agent` performs the migration tasks on the `source` and `target` hub clusters. The `multicluster-global-hub-manager` controls the flow of the migration between the `source` and `target` hub clusters and manages the `ManagedClusterMigration` resources.

During the managed cluster migration, the `source` and `target` hub clusters go through different phases. These phases and their conditions help track the status changes of the hub clusters throughout the migration process. See the following table for an outline of each phase and its condition:

| Phase | Condition |
|----|----|
| `Pending` | Performs one migration at a time. Other migrations remain `Pending`. |
| `Validating` | Verifies that the clusters and hub clusters are valid. |
| `Initializing` | Prepares the `target` and `source` hub cluster. |
| `Deploying` | Migrates selected clusters and their resources. |
| `Registering` | Restarts the registration of the cluster to the `target` hub cluster. |
| `Cleaning` | Cleans the resources from both `target` and `source` hub cluster and manages the `rollback` if needed. |
| `Completed` | Confirms the migrations are successfully completed. |
| `Failed` | Confirms that the migration has failed and includes this failure message in the `status`. |

Phase and condition

See the following table for the supported versions and the corresponding multicluster global hub `source`, and `target` hub versions:

| multicluster global hub version for migration | `source` hub version | `target` hub version |
|----|----|----|
| multicluster global hub 1.5 | Red Hat Advanced Cluster Management 2.14 | Red Hat Advanced Cluster Management 2.14 |
| multicluster global hub 1.5 | Red Hat Advanced Cluster Management 2.13 | Red Hat Advanced Cluster Management 2.14 |

Supported versions

To fully migrate your managed clusters, you need to complete the following procedures:

- [Preparing your multicluster global hub environment for migration](global_hub.md#global-hub-migrate-prep)

- [Migrating managed clusters](global_hub.md#global-hub-migrate-clusters)

- [Tracking the migration status](global_hub.md#global-hub-migrate-status)

<div>

<div class="title">

Additional resources

</div>

- [Importing a managed hub cluster in the default mode](global_hub.md#global-hub-importing-managed-hub-in-default-mode)

- [Importing a managed hub cluster in the hosted mode](global_hub.md#global-hub-importing-in-hosted-mode)

</div>

<a id="global-hub-migrate-prep"></a>

## Preparing your multicluster global hub environment for migration

To prepare your multicluster global hub environment for migration, you can create a Brownfield environment by deploying the multicluster global hub control plane directly into the `source` hub cluster. Then, you can import the `target` hub cluster into the multicluster global hub environment that is in the `Hosted` mode.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- The multicluster global hub operator to organize the migration workflow.

- The `source` Red Hat Advanced Cluster Management hub cluster to manage the clusters and the associated resources.

- The `target` Red Hat Advanced Cluster Management hub cluster to receive the migrated clusters and the associated resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Install the multicluster global hub operator in the `source` Red Hat Advanced Cluster Management hub cluster.

2.  Enable the `local-cluster` in the multicluster global hub custom operator that is running in the `source` hub cluster.

3.  Apply the following YAML to create the multicluster global hub operand and enable the multicluster global hub agent to run locally:

    ``` yaml
    apiVersion: operator.open-cluster-management.io/v1alpha4
    kind: MulticlusterGlobalHub
    metadata:
      name: multiclusterglobalhub
      namespace: multicluster-global-hub
    spec:
      availabilityConfig: High
      installAgentOnLocal: true
    ```

4.  Import the target hub cluster into multicluster global hub that is in the `Hosted` mode. Add the following label to the managed hub cluster:

    ``` bash
    global-hub.open-cluster-management.io/deploy-mode=hosted
    ```

</div>

<a id="global-hub-migrate-clusters"></a>

## Migrating managed clusters

After you configure your multicluster global hub migration environment, migrate your managed clusters. You can create a `ManagedClusterMigration` resource in the multicluster global hub migration environment by directly selecting your managed clusters by name or by using a `Placement` resource. To migrate the `cluster1` sample and the associated resources from `hub1` to `hub2` hub clusters, see the following procedure.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Complete [Preparing your multicluster global hub environment for migration](global_hub.md#global-hub-migrate-prep).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to your multicluster global hub namespace.

2.  Apply the following YAML file:

    ``` yaml
    apiVersion: global-hub.open-cluster-management.io/v1alpha1
    kind: ManagedClusterMigration
    metadata:
      name: migration-sample
    spec:
      from: local-cluster
      includedManagedClusters:
        - cluster1
        - cluster2
      to: hub2
    ```

    - The `source` hub cluster is a `local-cluster` that multicluster global hub installed in `hub1` hub cluster.

    - The managed clusters that are being migrated to `hub2` hub cluster. The managed cluster in `hub1` and `hub2` hub clusters must be different from one another.

    - The `target` hub cluster is `hub2`.

3.  To migrate your managed clusters with the `Placement` resource, go to your multicluster global hub namespace.

4.  Select clusters based on labels, cluster properties, or other criteria defined in your `Placement` resource.

5.  Apply the following YAML file:

    ``` yaml
    apiVersion: global-hub.open-cluster-management.io/v1alpha1
    kind: ManagedClusterMigration
    metadata:
      name: migration-placement-sample
    spec:
      from: local-cluster
      includedManagedClustersPlacementRef: production-clusters
      to: hub2
    ```

    - The `source` hub cluster is a `local-cluster` that multicluster global hub installed in `hub1` hub cluster.

    - The `Placement` resource that has the name `production-clusters` and that defines which clusters get migrated. You must define the `Placement` resource in the multicluster global hub agent namespace of the source hub cluster. For example, you can name the `Placement` resource `multicluster-global-hub` or `multicluster-global-hub-agent`.

    - The `target` hub cluster is `hub2`.

6.  Specify the `includedManagedClusters` or `includedManagedClustersPlacementRef` cluster type to include in your migration. Include only one of these cluster types in your migration because they cannot exist together.

</div>

<a id="global-hub-migrate-status"></a>

## Tracking the migration status

During the migration process, you can track the statuses of your managed clusters by using the multicluster global hub `ConfigMap` or the migration custom resource. multicluster global hub automatically creates a `ConfigMap` which gives you a detailed cluster list, telling you if the cluster migration fails or succeeds. The migration custom resource gives you the status of the entire migration process.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  View the migration status from the `ConfigMap` by running the following command:

    ``` bash
    oc get configmap <migration-name> -n <global-hub-namespace> -o yaml
    ```

2.  Ensure that the `ConfigMap` that you see resembles the following sample:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: migration-sample
      namespace: multicluster-global-hub
    data:
      success: '["cluster1","cluster3"]'
      failure: '["cluster2"]'
    ```

3.  To view the tracking status from the migration custom resource, verify that its migration status is `True`, and that it resembles the following sample:

    ``` yaml
    status:
      conditions:
        - type: ResourceValidated
          status: "True"
          message: Migration resources have been validated
        - type: ResourceInitialized
          status: "True"
          message: All source and target hubs have been initialized
        - type: ResourceDeployed
          status: "True"
          message: Resources have been successfully deployed to the target hub cluster
        - type: ClusterRegistered
          status: "True"
          message: All migrated clusters have been successfully registered
        - type: ResourceCleaned
          status: "True"
          message: Resources have been successfully cleaned up from the hub clusters
      phase: Completed
    ```

</div>

<a id="global-hub-update-postgres"></a>

## Recovering data from the updated built-in PostgreSQL (Deprecated)

Starting with multicluster global hub version 1.4.0, the built-in PostgreSQL database is updated to version 16. This update replaces the earlier `multicluster-global-hub-postgres` instance with the new `multicluster-global-hub-postgressql` instance.

By default, this update automatically re-syncs real-time data, such as `policies` and `clusters`, to the new Postgres instance. Historical data, such as `event` and `history` tables, are not automatically recovered.

When the multicluster global hub update to version 1.4.0 removes your historical data, recover your data by completing the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Clone the Red Hat Advanced Cluster Management for Kubernetes Git repository to access the shell script that you need to recover your data by running the following command:

    ``` bash
    git clone -b release-2.13 https://github.com/stolostron/multicluster-global-hub.git
    ```

2.  Restore your history tables by completing the following steps. Use the multicluster global hub that you installed:

    1.  If the default namespace is `multicluster-global-hub`, run the following shell script:

        ``` bash
        ./doc/upgrade/restore_history_tables.sh
        ```

    2.  If the namespace is not specified as `multicluster-global-hub`, set the multicluster global hub namespace when you run the following shell script:

    ``` bash
    ./doc/upgrade/restore_history_tables.sh
    ```

3.  Restore your event tables by completing the following steps:

    1.  If the default namespace is `multicluster-global-hub`, run the following shell script:

        ``` bash
        ./doc/upgrade/restore_event_tables.sh
        ```

    2.  If the namespace is not specified as `multicluster-global-hub`, set the multicluster global hub namespace when you run the following shell script:

    ``` bash
    ./doc/upgrade/restore_event_tables.sh
    ```

</div>

<a id="global-hub-update-postgres-delete-legacy"></a>

## Deleting legacy built-in Postgres data

Starting with multicluster global hub version 1.4.0, the built-in PostgreSQL database is updated to version 16. This update replaces the earlier `multicluster-global-hub-postgres` instance with the new `multicluster-global-hub-postgressql` instance.

By default, this update automatically re-syncs real-time data, such as `policies` and `clusters`, to the new Postgres instance. Historical data, such as `event` and `history` tables, are not automatically recovered.

After multicluster global hub updates to version 1.4.0, it switches to the new built-in Postgres instance. The global hub operator does not automatically delete resources associated with the legacy Postgres instance. To delete the legacy Postgres resources, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  If the default namespace is `multicluster-global-hub`, run the following shell script:

    ``` bash
    ./doc/upgrade/cleanup_legacy_postgres.sh
    ```

2.  If the namespace is not specified as `multicluster-global-hub`, set the multicluster global hub namespace when you run the following shell script:

    ``` bash
    ./doc/upgrade/cleanup_legacy_postgres.sh
    ```

</div>
