<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After you install a cluster on IBM Cloud® in a disconnected environment, you must complete the postinstallation configuration steps to prepare the cluster for use.

# Disabling the default software catalog sources

To use only trusted or locally available Operator catalogs, disable the default software catalog sources that OpenShift Container Platform configures during installation. In a restricted network environment, you must disable the default catalogs as a cluster administrator.

<div>

<div class="title">

Procedure

</div>

- Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object:

  ``` terminal
  $ oc patch OperatorHub cluster --type json \
      -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
  ```

  > [!TIP]
  > Or, you can use the web console to manage catalog sources. From the **Administration** → **Cluster Settings** → **Configuration** → **OperatorHub** page, click the **Sources** tab, where you can create, update, delete, disable, and enable individual sources.

</div>

# Installing the policy resources into the cluster

Mirroring the OpenShift Container Platform content using the oc-mirror OpenShift CLI (oc) plugin creates resources, which include `catalogSource-certified-operator-index.yaml` and `imageContentSourcePolicy.yaml`.

- The `ImageContentSourcePolicy` resource associates the mirror registry with the source registry and redirects image pull requests from the online registries to the mirror registry.

- The `CatalogSource` resource is used by Operator Lifecycle Manager (OLM) Classic to retrieve information about the available Operators in the mirror registry, which lets users discover and install Operators.

  > [!NOTE]
  > OLM v1 uses the `ClusterCatalog` resource to retrieve information about the available cluster extensions in the mirror registry.
  >
  > The oc-mirror plugin v1 does not generate `ClusterCatalog` resources automatically; you must manually create them. The oc-mirror plugin v2 does, however, generate `ClusterCatalog` resources automatically.
  >
  > For more information on creating and applying `ClusterCatalog` resources, see "Adding a catalog to a cluster" in "Extensions".

After you install the cluster, you must install these resources into the cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have mirrored the image set to the registry mirror in the disconnected environment.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI as a user with the `cluster-admin` role.

2.  Apply the YAML files from the results directory to the cluster:

    ``` terminal
    $ oc apply -f ./oc-mirror-workspace/results-<id>/
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the `ImageContentSourcePolicy` resources were successfully installed:

    ``` terminal
    $ oc get imagecontentsourcepolicy
    ```

2.  Verify that the `CatalogSource` resources were successfully installed:

    ``` terminal
    $ oc get catalogsource --all-namespaces
    ```

</div>

# Telemetry access for OpenShift Container Platform

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

# Additional resources

- [Customize your cluster](../../post_installation_configuration/cluster-tasks.md#available_cluster_customizations)

- [About remote health monitoring](../../support/remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring)
