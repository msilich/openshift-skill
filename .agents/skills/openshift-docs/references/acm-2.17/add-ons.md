> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/add-ons/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="acm-managed-adv-config"></a>

# Managed cluster advanced configuration

With Red Hat Advanced Cluster Management for Kubernetes klusterlet add-ons, you can further configure your managed clusters to improve performance and add functionality to your applications.

In Red Hat Advanced Cluster Management, you can configure the following klusterlet add-ons to improve the performance and functionality of your managed clusters:

- application-manager

- cert-policy-controller

- cluster-proxy

- config-policy-controller

- governance-policy-framework

- hypershift-addon

- managed-serviceaccount

- multicluster-observability-addon

- search-collector

- submariner

- volsync

- work-manager

<div>

<div class="title">

Additional resources

</div>

- [Enable klusterlet add-ons on clusters for cluster management](add-ons.md#add-ons-klusterlet)

- [Set up the *AddOnDeploymentConfig* to configure klusterlet add-ons](add-ons.md#setting-addondeploymentconfig-klusterlet-addons)

- [Configure a klusterlet add-on for all managed clusters](add-ons.md#configuring-klusterlet-addons-all-managedclusters)

- [Configure a klusterlet add-on for a single managed cluster](add-ons.md#configuring-klusterlet-addons-single-managedclusters)

- [Enable cluster-wide proxy on existing cluster add-ons](add-ons.md#enable-cluster-wide-proxy-addon)

- [Modify the klusterlet add-ons settings of your cluster](add-ons.md#modify-klusterlet-add-ons)

</div>

<a id="add-ons-klusterlet"></a>

## Enable klusterlet add-ons on clusters for cluster management

Enable the klusterlet add-ons for managed clusters after you install Red Hat Advanced Cluster Management for Kubernetes and create or import clusters with multicluster engine operator. The klusterlet add-ons are not enabled by default if you created or imported clusters unless you create or import with the Red Hat Advanced Cluster Management console.

See the following available klusterlet add-ons:

- application-manager

- cert-policy-controller

- config-policy-controller

- governance-policy-framework

- search-collector

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file that is similar to the following `KlusterletAddonConfig`, with the `spec` value that represents the add-ons:

    ``` yaml
    apiVersion: agent.open-cluster-management.io/v1
    kind: KlusterletAddonConfig
    metadata:
      name: <cluster_name>
      namespace: <cluster_name>
    spec:
      applicationManager:
        enabled: true
      certPolicyController:
        enabled: true
      policyController:
        enabled: true
      searchCollector:
        enabled: true
    ```

    - The `policy-controller` add-on is divided into two add-ons: The `governance-policy-framework` and the `config-policy-controller`. As a result, the `policyController` controls the `governance-policy-framework` and the `config-policy-controller` `managedClusterAddons`.

2.  Save the file as `klusterlet-addon-config.yaml`.

3.  Apply the YAML by running the following command on the hub cluster:

    ``` bash
    oc apply -f klusterlet-addon-config.yaml
    ```

4.  To verify whether the enabled `managedClusterAddons` are created after the `KlusterletAddonConfig` is created, run the following command:

    ``` bash
    oc get managedclusteraddons -n <cluster namespace>
    ```

</div>

<div>

<div class="title">

Next steps

</div>

- [Set up the *AddOnDeploymentConfig* to configure klusterlet add-ons](add-ons.md#setting-addondeploymentconfig-klusterlet-addons)

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster advanced configuration](add-ons.md#acm-managed-adv-config)

</div>

<a id="setting-addondeploymentconfig-klusterlet-addons"></a>

## Set up the *AddOnDeploymentConfig* to configure klusterlet add-ons

Set up the `AddOnDeploymentConfig` resource and apply specifications to any of the klusterlet add-ons on each of your managed clusters, such as the `nodeSelector` and `tolerations`.

<div>

<div class="title">

Procedure

</div>

1.  Use the `AddonDeploymentConfig` API to create an add-on configuration in any namespace on the hub cluster.

2.  Create a file named `addondeploymentconfig.yaml` with the following template:

    ``` yaml
    apiVersion: addon.open-cluster-management.io/v1alpha1
    kind: AddOnDeploymentConfig
    metadata:
      name: config-name
      namespace: config-namespace
    spec:
      nodePlacement:
        nodeSelector: {<node-selector>}
        tolerations: {<tolerations>}
      resourceRequirements:
      - containerID: "<workload-kind>:<workload-name>:<container-name>"
        resources:
          requests:
            memory: 75Mi
          limits:
            memory: 150Mi
    ```

    - Replace `config-name` with the name of the `AddonDeploymentConfig` that you created.

    - Replace `config-namespace` with the namespace of the `AddonDeploymentConfig` that you created.

    - Replace `<node-selector>` with your node selector.

    - Replace `<tolerations>` with your tolerations.

    - List resource requirements here to override the `resources` of the add-on workload containers. If an add-on container matches more than one of the items in the list, the last matching configuration is applied.

    - Replace `<workload-kind>` with the kind of workload, for example: `deployment`. Replace `<workload-name>` with the name of the workload. Replace `<container-name>` with the name of the container.

      **Note:** For any of these values, you can use the `*` attribute to apply the configuration to all objects managed by the add-on. For example, if you used the `*:*:*` attribute, it would apply the configuration to every container of every workload kind in any add-on the configuration is attached to.

      A completed `AddOnDeploymentConfig` resembles the following example:

    ``` yaml
    apiVersion: addon.open-cluster-management.io/v1alpha1
    kind: AddOnDeploymentConfig
    metadata:
      name: deploy-config
      namespace: open-cluster-management-hub
    spec:
      nodePlacement:
        nodeSelector:
          "node-dedicated": "acm-addon"
        tolerations:
          - effect: NoSchedule
            key: node-dedicated
            value: acm-addon
            operator: Equal
    ```

</div>

<div>

<div class="title">

Next steps

</div>

- [Configure a klusterlet add-on for all managed clusters](add-ons.md#configuring-klusterlet-addons-all-managedclusters)

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster advanced configuration](add-ons.md#acm-managed-adv-config)

- [Configure a klusterlet add-on for all managed clusters](add-ons.md#configuring-klusterlet-addons-all-managedclusters)

- [Configure a klusterlet add-on for a single managed cluster](add-ons.md#configuring-klusterlet-addons-single-managedclusters)

</div>

<a id="configuring-klusterlet-addons-all-managedclusters"></a>

## Configure a klusterlet add-on for all managed clusters

Configure a klusterlet add-on for all managed clusters by applying the `AddOnDeploymentConfig` with the `ClusterManagementAddOn`, which applies this add-on configuration to all your managed clusters that are attached to the hub cluster.

<div>

<div class="title">

Prerequisites

</div>

- You set up the `AddOnDeploymentConfig`. See [Set up the *AddOnDeploymentConfig* to configure klusterlet add-ons](add-ons.md#setting-addondeploymentconfig-klusterlet-addons).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Apply the `AddOnDeploymentConfig` file to your klusterlet add-on by running the following command:

    ``` bash
    oc apply -f addondeploymentconfig.yaml
    ```

2.  Connect the new configuration that you created to an add-on for all of your managed clusters by patching the `ClusterManagementAddOn` resource. Run the following command to patch the `spec.supportedConfigs` parameter in the `ClusterManagementAddOn` to point to the new configuration:

    ``` bash
    oc patch clustermanagementaddons.v1alpha1.addon.open-cluster-management.io <addon-name> --type='json' -p='[{
      "op":"add",
      "path":"/spec/supportedConfigs",
      "value":[{
        "group":"addon.open-cluster-management.io",
        "resource":"addondeploymentconfigs",
        "defaultConfig":{"name":"<config-name>","namespace":"<config-namespace>"}
      }]
    }]'
    ```

    - Replace `<addon-name>` with your add-on name.

    - Replace `<config-name>` with the name of the `AddonDeploymentConfig` that you created.

    - Replace `<config-namespace>` with the namespace of the `AddonDeploymentConfig` that you created.

</div>

<div>

<div class="title">

Next steps

</div>

- To override the configuration for one managed cluster, see [Configure a klusterlet add-on for a single managed cluster](add-ons.md#configuring-klusterlet-addons-single-managedclusters).

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster advanced configuration](add-ons.md#acm-managed-adv-config)

- [Set up the *AddOnDeploymentConfig* to configure klusterlet add-ons](add-ons.md#setting-addondeploymentconfig-klusterlet-addons)

</div>

<a id="configuring-klusterlet-addons-single-managedclusters"></a>

## Configure a klusterlet add-on for a single managed cluster

Configure a klusterlet add-on for a single managed cluster. Override the global default `AddonDeploymentConfig` configuration for your add-on on a certain managed cluster. The add-on configuration only applies to the particular managed cluster attached to that namespace of the hub cluster.

The new configuration that you reference in the `ManagedClusterAddOn` add-on overrides the global default configuration that you defined earlier in the `ClusterManagementAddOn` add-on.

<div>

<div class="title">

Prerequisites

</div>

- You set up the `AddOnDeploymentConfig`. See [Set up the *AddOnDeploymentConfig* to configure klusterlet add-ons](add-ons.md#setting-addondeploymentconfig-klusterlet-addons).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Use the `AddonDeploymentConfig` API to create another configuration to specify the `nodeSelector` and `tolerations` on the hub cluster.

2.  Connect the new configuration that you created to your `ManagedClusterAddOn` add-on on the hub cluster in the managed cluster namespace. Run the following command to patch the `spec.configs` parameter in the `ManagedClusterAddOn` to point to the new configuration:

    ``` bash
    oc -n <managed-cluster> patch managedclusteraddons.v1alpha1.addon.open-cluster-management.io <addon-name> --type='json' -p='[{
      "op":"add",
      "path":"/spec/configs",
      "value":[{
        "group":"addon.open-cluster-management.io",
        "resource":"addondeploymentconfigs",
        "namespace":"<config-namespace>",
        "name":"<config-name>"
      }]
    }]'
    ```

    - Replace `managed-cluster` with your managed cluster name.

    - Replace `addon-name` with your add-on name.

    - Replace `config-namespace` with the namespace of the `AddonDeploymentConfig` that you created.

    - Replace `config-name` with the name of the `AddonDeploymentConfig` that you created.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster advanced configuration](add-ons.md#acm-managed-adv-config)

- [Configure the klusterlet to run on specific nodes](clusters.md#config-klusterlet-nodes)

</div>

<a id="enable-cluster-wide-proxy-addon"></a>

## Enable cluster-wide proxy on existing cluster add-ons

Enable cluster cluster-wide proxy by configuring the `KlusterletAddonConfig` in the cluster namespace to add the proxy environment variables to all the klusterlet add-on pods of the managed Red Hat OpenShift Container Platform clusters.

<div>

<div class="title">

Procedure

</div>

1.  Edit the `KlusterletAddonConfig` file that is in the namespace of the cluster that needs the proxy. You can use the console to find the resource, or you can edit from the terminal with the following command:

    ``` bash
    oc -n <my-cluster-name> edit klusterletaddonconfig <my-cluster-name>
    ```

    **Note:** If you are working with only one cluster, you do not need `<my-cluster-name>` at the end of your command. See the following command:

    ``` bash
    oc -n <my-cluster-name> edit klusterletaddonconfig
    ```

2.  Edit the `.spec.proxyConfig` section of the file so it resembles the following example. The `spec.proxyConfig` is an optional section:

    ``` yaml
    spec:
      proxyConfig:
        httpProxy: "<proxy_not_secure>"
        httpsProxy: "<proxy_secure>"
        noProxy: "<no_proxy>"
    ```

    - Replace `proxy_not_secure` with the address of the proxy server for `http` requests. For example, use `http://192.168.123.145:3128`.

    - Replace `proxy_secure` with the address of the proxy server for `https` requests. For example, use `https://192.168.123.145:3128`.

    - Replace `no_proxy` with a comma delimited list of IP addresses, hostnames, and domain names where traffic is not routed through the proxy. For example, use `.cluster.local,.svc,10.128.0.0/14,example.com`.

      If the OpenShift Container Platform cluster is created with cluster wide proxy configured on the hub cluster, the cluster wide proxy configuration values are added to the pods of the klusterlet add-ons as environment variables when the following conditions are met:

    - The `.spec.policyController.proxyPolicy` in the `addon` section is enabled and set to `OCPGlobalProxy`.

    - The `.spec.applicationManager.proxyPolicy` is enabled and set to `CustomProxy`.

      **Note:** The default value of `proxyPolicy` in the `addon` section is `Disabled`.

      See the following examples of `proxyPolicy` entries:

      ``` yaml
      apiVersion: agent.open-cluster-management.io/v1
          kind: KlusterletAddonConfig
          metadata:
            name: clusterName
            namespace: clusterName
          spec:
            proxyConfig:
              httpProxy: http://pxuser:12345@10.0.81.15:3128
              httpsProxy: http://pxuser:12345@10.0.81.15:3128
              noProxy: .cluster.local,.svc,10.128.0.0/14, example.com
            applicationManager:
              enabled: true
              proxyPolicy: CustomProxy
            policyController:
              enabled: true
              proxyPolicy: OCPGlobalProxy
            searchCollector:
              enabled: true
              proxyPolicy: Disabled
            certPolicyController:
              enabled: true
              proxyPolicy: Disabled
      ```

      **Important:** Global proxy settings do not impact alert forwarding.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

To set up alert forwarding for Red Hat Advanced Cluster Management hub clusters with a cluster-wide proxy, see [Forward your alerts](observability.md#obs-forward-alerts) for more details.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster advanced configuration](add-ons.md#acm-managed-adv-config)

</div>

<a id="modify-klusterlet-add-ons"></a>

## Modify the klusterlet add-ons settings of your cluster

Modify the settings of `KlusterletAddonConfig` to change your configuration by using the hub cluster.

The `KlusterletAddonConfig` controller manages the functions that are enabled and disabled according to the settings in the `klusterletaddonconfigs.agent.open-cluster-management.io` Kubernetes resource. View the following example of the `KlusterletAddonConfig`, where the value for `<2.x.0>` is replaced with the supported version you are using:

``` yaml
apiVersion: agent.open-cluster-management.io/v1
kind: KlusterletAddonConfig
metadata:
  name: <cluster-name>
  namespace: <cluster-name>
spec:
  clusterName: <cluster-name>
  clusterNamespace: <cluster-name>
  clusterLabels:
    cloud: auto-detect
    vendor: auto-detect
  applicationManager:
    enabled: true
  certPolicyController:
    enabled: true
  policyController:
    enabled: true
  searchCollector:
    enabled: false
  version: <2.x.0>
```

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster advanced configuration](add-ons.md#acm-managed-adv-config)

- [Klusterlet add-ons settings](add-ons.md#description-of-settings)

- [Modify klusterlet add-ons settings by using the console](add-ons.md#modify-using-the-console-on-the-hub-cluster)

- [Modify klusterlet add-ons settings by using the command line](add-ons.md#modify-using-the-command-line-on-the-hub-cluster)

</div>

<a id="description-of-settings"></a>

## Klusterlet add-ons settings

There are settings that you can update in the `klusterletaddonconfigs.agent.open-cluster-management.io` Kubernetes resource.

| Setting name | Value | Description |
|----|----|----|
| applicationmanager | `true` or `false` | This controller manages the application subscription lifecycle on the managed cluster. |
| certPolicyController | `true` or `false` | This controller enforces certificate-based policies on the managed cluster. |
| policyController | `true` or `false` | This controller enforces all other policy rules on the managed cluster. |
| searchCollector | `true` or `false` | This controller is used to periodically push the resource index data back to the hub cluster. |

Table list of klusterlet add-ons settings

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster advanced configuration](add-ons.md#acm-managed-adv-config)

- [Modify the klusterlet add-ons settings of your cluster](add-ons.md#modify-klusterlet-add-ons)

</div>

<a id="modify-using-the-console-on-the-hub-cluster"></a>

## Modify klusterlet add-ons settings by using the console

Modify the settings of the `klusterletaddonconfigs.agent.open-cluster-management.io` resource by using the hub cluster console.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the Red Hat Advanced Cluster Management for Kubernetes console of the hub cluster.

2.  From the header menu of the hub cluster console, select the **Search** icon.

3.  In the search parameters, enter the following value: `kind:klusterletaddonconfigs`

4.  Select the endpoint resource that you want to update.

5.  Find the `spec` section and select **Edit** to edit the content.

6.  Modify your settings.

7.  Select **Save** to apply your changes.

</div>

<div>

<div class="title">

Next steps

</div>

- [Managed cluster advanced configuration](add-ons.md#acm-managed-adv-config)

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster advanced configuration](add-ons.md#acm-managed-adv-config)

- [Modify the klusterlet add-ons settings of your cluster](add-ons.md#modify-klusterlet-add-ons)

- [Klusterlet add-ons settings](add-ons.md#description-of-settings)

- [Modify klusterlet add-ons settings by using the command line](add-ons.md#modify-using-the-command-line-on-the-hub-cluster)

</div>

<a id="modify-using-the-command-line-on-the-hub-cluster"></a>

## Modify klusterlet add-ons settings by using the command line

Modify your `KlusterletAddonConfig` settings by using the command line on the hub cluster. You must have access to the `cluster-name` namespace.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the hub cluster.

2.  Enter the following command to edit the resource:

        kubectl edit klusterletaddonconfigs.agent.open-cluster-management.io <cluster-name> -n <cluster-name>

3.  Find the `spec` section.

4.  Modify your settings, as necessary.

</div>

<div>

<div class="title">

Next steps

</div>

- [Managed cluster advanced configuration](add-ons.md#acm-managed-adv-config)

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managed cluster advanced configuration](add-ons.md#acm-managed-adv-config)

- [Modify the klusterlet add-ons settings of your cluster](add-ons.md#modify-klusterlet-add-ons)

- [Klusterlet add-ons settings](add-ons.md#description-of-settings)

- [Modify klusterlet add-ons settings by using the console](add-ons.md#modify-using-the-console-on-the-hub-cluster)

</div>
