> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/mce_acm_integration/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="mce-acm-integration"></a>

# multicluster engine operator with Red Hat Advanced Cluster Management integration

If you are using multicluster engine operator and then you install Red Hat Advanced Cluster Management, you can access more multicluster management features, such as *observability* and *policy*. For integrated capability, see the following requirements:

- You need to install Red Hat Advanced Cluster Management. See the Red Hat Advanced Cluster Management [Get started with Red Hat Advanced Cluster Management](get_started.md#get-started-acm) documentation.

- See [MultiClusterHub advanced configuration](get_started.md#advanced-config-hub) for details about Red Hat Advanced Cluster Management after you install.

<div>

<div class="title">

Additional resources

</div>

- [Integrated hosted control plane fleet management architecture pattern](mce_acm_integration.md#hosted-pattern)

- [multicluster engine operator hosted cluster discovery in Red Hat Advanced Cluster Management](mce_acm_integration.md#discover-hosted-acm)

- [Automated import for discovered hosted clusters](mce_acm_integration.md#auto-import-hcp)

- [Automated import for discovered Red Hat OpenShift Service on AWS (classic) clusters](mce_acm_integration.md#import-discover-rosa)

- [Label propagation for hosted clusters between Red Hat Advanced Cluster Management and multicluster engine operator hub clusters](mce_acm_integration.md#propagate-hosted-labels)

- [Observability integration](mce_acm_integration.md#mce-acm-observability)

- [SiteConfig operator](mce_acm_integration.md#siteconfig)

</div>

<a id="hosted-acm"></a>

# Hosted clusters with Red Hat Advanced Cluster Management

If you have multicluster engine operator clusters that are hosting multiple *hosted clusters*, you can bring those hosted clusters to a Red Hat Advanced Cluster Management hub cluster to manage with Red Hat Advanced Cluster Management components, such as *Application lifecycle* and *Governance*.

Begin with learning from the [About hosted control planes with multicluster engine operator](clusters.md#mce-hcp-overview) documentation.

- [Integrated hosted control plane fleet management architecture pattern](mce_acm_integration.md#hosted-pattern)

- [multicluster engine operator hosted cluster discovery in Red Hat Advanced Cluster Management](mce_acm_integration.md#discover-hosted-acm)

  - [Configure Red Hat Advanced Cluster Management to import multicluster engine operator clusters](mce_acm_integration.md#hosted-import-config)

  - [Import multicluster engine operator manually](mce_acm_integration.md#hosted-import-mce)

  - [Discover hosted clusters](mce_acm_integration.md#hosted-discover)

- [Automated import for discovered hosted clusters](mce_acm_integration.md#auto-import-hcp)

  - [Configure settings for automatic import](mce_acm_integration.md#config-hcp-autoimport)

  - [Create the hosted control plane placement definition](mce_acm_integration.md#create-hcp-placement)

  - [Bind the import policy to a hosted control plane placement definition](mce_acm_integration.md#bind-hcp-placement)

- [Automated import for discovered Red Hat OpenShift Service on AWS (classic) clusters](mce_acm_integration.md#import-discover-rosa)

  - [Create the automatic import policy](mce_acm_integration.md#creating-rosa-policy)

  - [Create the Red Hat OpenShift Service on AWS (classic) placement definition](mce_acm_integration.md#create-rosa-placement)

  - [Bind the import policy to a Red Hat OpenShift Service on AWS (classic) placement definition](mce_acm_integration.md#bind-rosa-placement)

- [Label propagation for hosted clusters between Red Hat Advanced Cluster Management and multicluster engine operator hub clusters](mce_acm_integration.md#propagate-hosted-labels)

  - [Propagating HostedCluster labels to ManagedCluster resources](mce_acm_integration.md#propagate-labels-hc)

  - [Propagating labels from Red Hat Advanced Cluster Management hub cluster to multicluster engine operator ManagedCluster resources](mce_acm_integration.md#propagate-labels-hub)

- [Observability integration](mce_acm_integration.md#mce-acm-observability)

<a id="hosted-pattern"></a>

## Integrated hosted control plane fleet management architecture pattern

As your Red Hat Advanced Cluster Management for Kubernetes and multicluster engine for Kubernetes operator hosted control plane deployment scales, you can strategically manage resource requirements and maintain centralized visibility across your fleet.

Consider the following guidance for an architecture pattern for managing hosted control plane clusters at scale.

Red Hat Advanced Cluster Management for Kubernetes or multicluster engine for Kubernetes operator enables hosted control plane capabilities. While deployments often begin with a single hub cluster, scaling the number of hosted control plane clusters introduces several challenges.

Resource consumption  
Resource requirements grow proportionally with the number of planes.

Scaling complexity  
You must choose between scaling existing clusters or provisioning new ones.

Management overhead  
Managing multiple hosting clusters individually becomes complex.

Visibility gaps  
Maintaining centralized visibility and governance across disparate clusters is difficult.

To address these challenges, implement a *hierarchical management pattern*, which is an architecture that separates the management logic from the hosting infrastructure. Learn more about this pattern in the sections that follow.

Learn about the benefits of this architecture pattern in the following table:

| Benefit | Description |
|----|----|
| Centralized management | Provides a single pane of glass for the entire fleet. |
| Scalability | Allows you to add multicluster engine operator clusters as needed to increase capacity. |
| Resource optimization | Focuses multicluster engine operator clusters on hosting and the Red Hat Advanced Cluster Management hub cluster on management. |
| Operational efficiency | Enables unified policy management and governance. |
| Cost effectiveness | Allows you to right-size each component for a specific role. |

Advantages of the hierarchical management pattern

- Central Red Hat Advanced Cluster Management hub cluster

  The central Red Hat Advanced Cluster Management hub cluster serves as the primary management and visibility layer for the following functions:

  - Provides a single console for end-to-end fleet management

  - Manages operational policies across the entire infrastructure

  - Enables comprehensive monitoring and governance capabilities

- multicluster engine operator hosting infrastructure

  Deploy multiple multicluster engine operator clusters to serve as the physical hosting infrastructure for control planes. See the following functions of the multicluster engine operator hosting cluster:

  - Provides hosted control plane components with a smaller footprint than a full Red Hat Advanced Cluster Management installation.

  - Includes the management console and BareMetal infrastructure operators.

  - Optimizes for hosting workloads rather than high-level fleet management.

- Implementation considerations

  Learn about the process and gather other important information for fleet management architecture.

  - The central Red Hat Advanced Cluster Management hub cluster manages both the multicluster engine operator clusters and the attached hosted control plane clusters

  - Policies and governance are applied consistently across the entire infrastructure.

  - Monitoring and alerting are centralized while hosting capacity remains distributed.

    See the following process overview:

  - **Deploy the central Red Hat Advanced Cluster Management hub cluster:** Establish this cluster as your primary management interface.

  - **Deploy multicluster engine operator clusters:** Use these as the hosting infrastructure for your control planes.

  - **Configure discovery:** Ensure the Red Hat Advanced Cluster Management hub cluster can manage both the multicluster engine operator clusters and the attached hosted control plane clusters.

    **Important:** A Red Hat Advanced Cluster Management cluster cannot manage another Red Hat Advanced Cluster Management cluster.

    If you have already deployed multiple Red Hat Advanced Cluster Management hub clusters to host control planes, use the following process for this pattern architecture:

  - **Convert Red Hat Advanced Cluster Management hosting clusters to multicluster engine operator:** Uninstall Red Hat Advanced Cluster Management and install multicluster engine operator on the clusters that are designated for hosting infrastructure.

  - **Preserve hosted control plane clusters:** Ensure the conversion process does not disrupt existing hosted control plane clusters.

  - **Designate the hub cluster:** Select one Red Hat Advanced Cluster Management cluster to serve as the central management hub cluster.

<div>

<div class="title">

Additional resources

</div>

- [multicluster engine operator hosted cluster discovery in Red Hat Advanced Cluster Management](mce_acm_integration.md#discover-hosted-acm)

- [Uninstalling](get_started.md#uninstalling)

- [Get started with multicluster engine operator](clusters.md#get-started-mce)

</div>

<a id="discover-hosted-acm"></a>

## multicluster engine operator hosted cluster discovery in Red Hat Advanced Cluster Management

If you have multicluster engine operator clusters that are hosting multiple *hosted clusters*, you can bring those hosted clusters to a Red Hat Advanced Cluster Management hub cluster to manage with Red Hat Advanced Cluster Management components, such as *Application lifecycle* and *Governance*.

Those hosted clusters can be automatically discovered and imported as managed clusters.

**Note:** Since the hosted control planes run on the managed multicluster engine operator cluster nodes, the number of hosted control planes that the cluster can host is determined by the resource availability of managed multicluster engine operator cluster nodes, as well as the number of managed multicluster engine operator clusters. You can add more nodes or managed clusters to host more hosted control planes.

<div>

<div class="title">

Additional resources

</div>

- [Configure Red Hat Advanced Cluster Management to import multicluster engine operator clusters](mce_acm_integration.md#hosted-import-config)

- [Import multicluster engine operator manually](mce_acm_integration.md#hosted-import-mce)

- [Discover hosted clusters](mce_acm_integration.md#hosted-discover)

- [Automated import for discovered hosted clusters](mce_acm_integration.md#auto-import-hcp)

</div>

<a id="hosted-import-config"></a>

### Configure Red Hat Advanced Cluster Management to import multicluster engine operator clusters

Configure add-ons and install those add-ons in a different multicluster engine operator namespace so that the multicluster engine operator can self-manage with the `local-cluster` add-ons while Red Hat Advanced Cluster Management manages multicluster engine operator at the same time. multicluster engine operator has a `local-cluster`, which is a hub cluster that is managed.

The following default add-ons are enabled for this `local-cluster` in the `open-cluster-management-agent-addon` namespace:

- `cluster-proxy`

- `managed-serviceaccount`

- `work-manager`

      When your {mce-short} is imported into {acm-short}, {acm-short} enables the same set of add-ons to manage the {mce-short}.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You need one or more multicluster engine operator clusters that are not currently managed by any Red Hat Advanced Cluster Management cluster. You cannot install multicluster engine operator in a managed cluster.

- You need a Red Hat Advanced Cluster Management cluster that is set as your hub cluster.

- Install the `clusteradm` CLI by running the following command:

  ``` bash
  curl -L https://raw.githubusercontent.com/open-cluster-management-io/clusteradm/main/install.sh | bash
  ```

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to your Red Hat Advanced Cluster Management with the CLI.

2.  Update the `hypershift-addon-deploy-config` install add-ons in the `open-cluster-management-agent-addon-discovery` namespace. Run the following command:

    ``` bash
    oc patch addondeploymentconfig hypershift-addon-deploy-config -n multicluster-engine --type=merge -p '{"spec":{"customizedVariables":[{"name":"configureMceImport","value":"true"}]}}'
    ```

3.  Run the following command to verify that the add-ons for the Red Hat Advanced Cluster Management `local-cluster` are re-installed into the namespace that you specified:

    ``` bash
    oc get deployment -n open-cluster-management-agent-addon-discovery
    ```

    See the following output example:

    ``` bash
    NAME                                                  READY   STATUS    RESTARTS   AGE
    application-manager-6b7f74b8f7-7sd25                  1/1     Running   0          1d15h
    cluster-proxy-proxy-agent-7985ddfdb6-kng5p            3/3     Running   0          1d15h
    klusterlet-addon-workmgr-55fd575b4b-rs5vz             1/1     Running   0          1d15h
    managed-serviceaccount-addon-agent-54bd989b94-g6gz9   1/1     Running   0          1d15h
    ```

4.  Run the following command to check the status of your configuration:

    ``` bash
    oc get configmap hypershift-addon-deploy-config-info -n multicluster-engine -o yaml
    ```

</div>

<a id="hosted-import-mce"></a>

### Import multicluster engine operator manually

Import multicluster engine operator clusters after you configure Red Hat Advanced Cluster Management add-ons to install in a different namespace than multicluster engine operator add-ons. To manually import an multicluster engine operator cluster from your Red Hat Advanced Cluster Management cluster, complete the following procedure.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  From your Red Hat Advanced Cluster Management cluster, create a `ManagedCluster` resource manually to import an multicluster engine operator cluster. See the following file example:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1
    kind: ManagedCluster
    metadata:
      annotations:
        agent.open-cluster-management.io/klusterlet-config: mce-import-klusterlet-config
      labels:
        cloud: auto-detect
        vendor: auto-detect
      name: <name>
    spec:
      hubAcceptsClient: true
      leaseDurationSeconds: 60
    ```

    - The `mce-import-klusterlet-config` annotation references the `KlusterletConfig` resource that you created in the previous step to install the Red Hat Advanced Cluster Management klusterlet with a different name in multicluster engine operator.

    - Replace `<name>` with your cluster name.

2.  Run `oc apply -f <filename>.yaml` to apply the file.

3.  **Optional:** Create a `KlusterletAddonConfig` resource for each multicluster engine operator cluster to enable additional Red Hat Advanced Cluster Management add-ons. Use the following example:

    ``` yaml
    apiVersion: agent.open-cluster-management.io/v1
    kind: KlusterletAddonConfig
    metadata:
      name: <host-name>  # Must match your ManagedCluster name
      namespace: <host-namespace>  # Must match your ManagedCluster name
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

    - Replace `<host-name>` with your managed cluster name.

    - Replace `<host-namespace>` with your managed cluster namespace.

4.  Run `oc apply -f <filename>.yaml` to apply the file.

5.  Create the `auto-import-secret` secret that references the `kubeconfig` of the multicluster engine operator cluster. Go to [Import a cluster by using the auto import secret](clusters.md#importing-clusters-auto-import-secret) to add the auto import secret to complete the multicluster engine operator auto-import process.

    After you create the auto import secret in the multicluster engine operator managed cluster namespace in the Red Hat Advanced Cluster Management cluster, the managed cluster is registered.

6.  Alternatively, extract the import manifest for your multicluster engine operator cluster. Run the following command. Replace `<name>` with the name of your multicluster engine operator cluster:

    ``` bash
    oc get secret mce-hosting-east-import -n <name> -o jsonpath={.data.import\\.yaml} | base64 --decode > import.yaml
    ```

7.  Apply the `import.yaml` file to your multicluster engine operator cluster. Run the following command:

    ``` bash
    oc apply -f import.yaml
    ```

8.  Run the following command to get the status:

    ``` bash
    oc get managedcluster
    ```

    See following example output with the status and example URLs of managed clusters:

    ``` bash
    NAME           HUB ACCEPTED   MANAGED CLUSTER URLS            JOINED   AVAILABLE   AGE
    local-cluster  true           https://<api.acm-hub.com:port>  True     True        44h
    mce-a          true           https://<api.mce-a.com:port>    True     True        27s
    ```

    **Important:** Do not enable any other Red Hat Advanced Cluster Management add-ons for the imported multicluster engine operator.

</div>

<a id="hosted-discover"></a>

### Discover hosted clusters

Discover hosted clusters by enabling the `hypershift-addon` for managed multicluster engine operator clusters after you import all multicluster engine operator clusters into Red Hat Advanced Cluster Management. Default add-ons are installed into a different namespace in the previous procedures. Similarly, you install the `hypershift-addon` into a different namespace in multicluster engine operator so that the add-ons agent for multicluster engine operator local-cluster and the agent for Red Hat Advanced Cluster Management can work in multicluster engine operator.

**Required access:** Cluster administrator

**Important:** For all the following commands, replace `<managed-cluster-names>` with comma-separated managed cluster names for multicluster engine operator.

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to set the `agentInstallNamespace` namespace of the add-on to `open-cluster-management-agent-addon-discovery`:

    ``` bash
    oc patch addondeploymentconfig hypershift-addon-deploy-config -n multicluster-engine --type=merge -p '{"spec":{"agentInstallNamespace":"open-cluster-management-agent-addon-discovery"}}'
    ```

2.  Run the following command to disable metrics and to disable the HyperShift operator management:

    ``` bash
    oc patch addondeploymentconfig hypershift-addon-deploy-config -n multicluster-engine --type=merge -p '{"spec":{"customizedVariables":[{"name":"disableMetrics","value": "true"},{"name":"disableHOManagement","value": "true"}]}}'
    ```

3.  **Optional:** Configure your customized naming convention. By default, imported hosted clusters use the `<mce-cluster-name>-<hosted-cluster-name>` naming pattern, but you can change the name with the following steps:

    1.  Remove the default prefix by running the following command:

        ``` bash
        oc patch addondeploymentconfig hypershift-addon-deploy-config \
          -n multicluster-engine \
          --type=merge \
          -p '{"spec":{"customizedVariables":[{"name":"disableMetrics","value":"true"},{"name":"disableHOManagement","value":"true"},{"name":"discoveryPrefix","value":"custom-prefix"}]}}'
        ```

    2.  Change `custom-prefix` to your new prefix. The hosted cluster names are created with the `<custom-prefix>-<hosted-cluster-name>` pattern. Run the following command:

        ``` bash
        oc patch addondeploymentconfig hypershift-addon-deploy-config \
          -n multicluster-engine \
          --type=merge \
          -p '{"spec":{"customizedVariables":[{"name":"disableMetrics","value":"true"},{"name":"disableHOManagement","value":"true"},{"name":"discoveryPrefix","value":"custom-prefix"}]}}'
        ```

    3.  If you need to remove the discovery prefix entirely, first ensure all hosted clusters are detached from the respective clusters. **Important:** Using an empty string as the custom prefix can cause klusterlet naming collisions within the multicluster engine operator cluster. Run the following command:

    ``` bash
    oc patch addondeploymentconfig hypershift-addon-deploy-config \
       -n multicluster-engine \
       --type=json \
       -p='[{"op":"add","path":"/spec/customizedVariables/-","value":{"name":"autoImportDisabled","value":"true"}}]'
    ```

4.  Run the following command to enable the `hypershift-addon` for multicluster engine operator:

    ``` bash
    clusteradm addon enable --names hypershift-addon --clusters <managed-cluster-names>
    ```

5.  Get the multicluster engine operator managed cluster names by running the following command in Red Hat Advanced Cluster Management.

    ``` bash
    oc get managedcluster
    ```

6.  Log in to multicluster engine operator clusters and verify that the `hypershift-addon` is installed in the namespace that you specified. Run the following command:

    ``` bash
    oc get deployment -n open-cluster-management-agent-addon-discovery
    ```

    See the following example output that lists the add-ons:

    ``` bash
    NAME                                READY   UP-TO-DATE   AVAILABLE   AGE
    cluster-proxy-proxy-agent           1/1     1            1           24h
    klusterlet-addon-workmgr            1/1     1            1           24h
    hypershift-addon-agent              1/1     1            1           24h
    managed-serviceaccount-addon-agent  1/1     1            1           24h
    ```

    Red Hat Advanced Cluster Management deploys the `hypershift-addon`, which is the discovery agent that discovers hosted clusters from multicluster engine operator. The agent creates the corresponding `DiscoveredCluster` custom resource in the multicluster engine operator managed cluster namespace in the Red Hat Advanced Cluster Management hub cluster when the hosted cluster `kube-apiserver` becomes available.

7.  View your discovered clusters in the console. Log in to hub cluster console and click **Fleet Management** \> **Infrastructure** \> **Clusters**.

    **Note:** For OpenShift Container Platform versions earlier than version 4.20, select **All Clusters** from the cluster switcher.

8.  Find the *Discovered clusters* tab to view all discovered hosted clusters from multicluster engine operator with type `MultiClusterEngineHCP`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Automated import for discovered hosted clusters](mce_acm_integration.md#auto-import-hcp)

</div>

<a id="auto-import-hcp"></a>

## Automated import for discovered hosted clusters

Automated import of hosted clusters uses the `DiscoveredCluster` resource for faster cluster management, without manually importing individual clusters.

Automatic import of a discovered hosted cluster into Red Hat Advanced Cluster Management enables all Red Hat Advanced Cluster Management add-ons so that you can start managing the hosted clusters with the available management tools.

The hosted cluster is also *auto-imported* into multicluster engine operator. Through the multicluster engine operator console, you can manage the hosted cluster lifecycle. However, you cannot manage the hosted cluster lifecycle from the Red Hat Advanced Cluster Management console.

**Required access:** Cluster administrator

<div>

<div class="title">

Additional resources

</div>

- [Configure settings for automatic import](mce_acm_integration.md#config-hcp-autoimport)

- [Create the hosted control plane placement definition](mce_acm_integration.md#create-hcp-placement)

- [Bind the import policy to a hosted control plane placement definition](mce_acm_integration.md#bind-hcp-placement)

</div>

<a id="config-hcp-autoimport"></a>

### Configure settings for automatic import

Configure a Red Hat Advanced Cluster Management policy to automatically set the `spec.importAsManagedCluster` field from the default `false` setting to the `true` setting for all `type.MultiClusterEngineHCP` resources within `DiscoveredCluster` resources. With this change, discovered hosted clusters are immediately and automatically imported into Red Hat Advanced Cluster Management. Discovered hosted clusters from managed multicluster engine operator clusters are represented in `DiscoveredCluster` custom resources, which are located in the managed multicluster engine operator cluster namespace in Red Hat Advanced Cluster Management.

See the following `DiscoveredCluster` resource and namespace example:

``` yaml
apiVersion: discovery.open-cluster-management.io/v1
kind: DiscoveredCluster
metadata:
  creationTimestamp: "2024-05-30T23:05:39Z"
  generation: 1
  labels:
    hypershift.open-cluster-management.io/hc-name: hosted-cluster-1
    hypershift.open-cluster-management.io/hc-namespace: clusters
  name: hosted-cluster-1
  namespace: mce-1
  resourceVersion: "1740725"
  uid: b4c36dca-a0c4-49f9-9673-f561e601d837
spec:
  apiUrl: https://a43e6fe6dcef244f8b72c30426fb6ae3-ea3fec7b113c88da.elb.us-west-1.amazonaws.com:6443
  cloudProvider: aws
  creationTimestamp: "2024-05-30T23:02:45Z"
  credential: {}
  displayName: mce-1-hosted-cluster-1
  importAsManagedCluster: false
  isManagedCluster: false
  name: hosted-cluster-1
  openshiftVersion: 0.0.0
  status: Active
  type: MultiClusterEngineHCP
```

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You need Red Hat Advanced Cluster Management installed. See the Red Hat Advanced Cluster Management [Get started with Red Hat Advanced Cluster Management](get_started.md#get-started-acm) documentation.

- You need to learn about *Policies*. See the introduction to [Governance](governance.md#governance) in the Red Hat Advanced Cluster Management documentation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to your hub cluster from the CLI.

2.  Create a YAML file for your `DiscoveredCluster` custom resource and edit the configuration that is referenced in the following example:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: policy-mce-hcp-autoimport
      namespace: open-cluster-management-global-set
      annotations:
        policy.open-cluster-management.io/standards: NIST SP 800-53
        policy.open-cluster-management.io/categories: CM Configuration Management
        policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
        policy.open-cluster-management.io/description: Discovered clusters that are of
          type MultiClusterEngineHCP can be automatically imported into ACM as managed clusters.
          This policy configure those discovered clusters so they are automatically imported.
          Fine tuning MultiClusterEngineHCP clusters to be automatically imported
          can be done by configure filters at the configMap or add annotation to the discoverd cluster.
    spec:
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: mce-hcp-autoimport-config
            spec:
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: v1
                    kind: ConfigMap
                    metadata:
                      name: discovery-config
                      namespace: open-cluster-management-global-set
                    data:
                      rosa-filter: ""
              remediationAction: enforce
              severity: low
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: policy-mce-hcp-autoimport
            spec:
              remediationAction: enforce
              severity: low
              object-templates-raw: |
                {{- /* find the MultiClusterEngineHCP DiscoveredClusters */ -}}
                {{- range $dc := (lookup "discovery.open-cluster-management.io/v1" "DiscoveredCluster" "" "").items }}
                  {{- /* Check for the flag that indicates the import should be skipped */ -}}
                  {{- $skip := "false" -}}
                  {{- range $key, $value := $dc.metadata.annotations }}
                    {{- if and (eq $key "discovery.open-cluster-management.io/previously-auto-imported")
                               (eq $value "true") }}
                      {{- $skip = "true" }}
                    {{- end }}
                  {{- end }}
                  {{- /* if the type is MultiClusterEngineHCP and the status is Active */ -}}
                  {{- if and (eq $dc.spec.status "Active")
                             (contains (fromConfigMap "open-cluster-management-global-set" "discovery-config" "mce-hcp-filter") $dc.spec.displayName)
                             (eq $dc.spec.type "MultiClusterEngineHCP")
                             (eq $skip "false") }}
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: discovery.open-cluster-management.io/v1
                    kind: DiscoveredCluster
                    metadata:
                      name: {{ $dc.metadata.name }}
                      namespace: {{ $dc.metadata.namespace }}
                    spec:
                      importAsManagedCluster: true
                  {{- end }}
                {{- end }}
    ```

3.  Enable automatic import. Change the `spec.remediationAction` to `enforce`.

4.  Enable automatic import. Change `spec.importAsManagedCluster` to `true`.

5.  Run `oc apply -f <filename>.yaml -n <namespace>` to apply the file.

</div>

<a id="create-hcp-placement"></a>

### Create the hosted control plane placement definition

Create a placement definition that specifies the managed cluster for the policy deployment. Complete the following procedure.

<div>

<div class="title">

Procedure

</div>

1.  Create the `Placement` definition that selects only the `local-cluster`, which is a hub cluster that is managed. Use the following YAML sample:

2.  Create the `Placement` definition that selects only the `local-cluster`, which is a hub cluster that is managed. Use the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: policy-mce-hcp-autoimport-placement
      namespace: open-cluster-management-global-set
    spec:
      tolerations:
        - key: cluster.open-cluster-management.io/unreachable
          operator: Exists
        - key: cluster.open-cluster-management.io/unavailable
          operator: Exists
      clusterSets:
        - global
      predicates:
        - requiredClusterSelector:
            labelSelector:
              matchExpressions:
                - key: local-cluster
                  operator: In
                  values:
                    - "true"
    ```

3.  Run `oc apply -f placement.yaml -n <namespace>`, where `namespace` matches the namespace that you used for the policy that you previously created.

</div>

<a id="bind-hcp-placement"></a>

### Bind the import policy to a hosted control plane placement definition

Bind the policy to the placement after you create both resources. Complete the following steps.

<div>

<div class="title">

Procedure

</div>

1.  Connect the resources by using a `PlacementBinding` resource. See the following example where `placementRef` references the `Placement` that you created, and `subjects` references the `Policy` that you created:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: PlacementBinding
    metadata:
      name: policy-mce-hcp-autoimport-placement-binding
      namespace: open-cluster-management-global-set
    placementRef:
      name: policy-mce-hcp-autoimport-placement
      apiGroup: cluster.open-cluster-management.io
      kind: Placement
    subjects:
      - name: policy-mce-hcp-autoimport
        apiGroup: policy.open-cluster-management.io
        kind: Policy
    ```

2.  To verify, run the following command:

    ``` bash
    oc get policies.policy.open-cluster-management.io policy-mce-hcp-autoimport -n <namespace>
    ```

    **Important:** You can *detach* a hosted cluster from Red Hat Advanced Cluster Management by using the **Detach** option in the Red Hat Advanced Cluster Management console, or by removing the corresponding `ManagedCluster` custom resource from the command line. For best results, detach the managed hosted cluster before *destroying* the hosted cluster.

    When a discovered cluster is detached, the following annotation is added to the `DiscoveredCluster` resource to prevent the policy to import the discovered cluster again. If you want the detached discovered cluster to be reimported, remove this annotation:

    ``` bash
      annotations:
        discovery.open-cluster-management.io/previously-auto-imported: "true"
    ```

</div>

<a id="import-discover-rosa"></a>

## Automated import for discovered Red Hat OpenShift Service on AWS (classic) clusters

Automated import of Red Hat OpenShift Service on AWS (classic) clusters uses Red Hat Advanced Cluster Management policy enforcement for faster cluster management, without manually importing individual clusters.

**Required access:** Cluster administrator

<div>

<div class="title">

Additional resources

</div>

- [Create the automatic import policy](mce_acm_integration.md#creating-rosa-policy)

- [Create the Red Hat OpenShift Service on AWS (classic) placement definition](mce_acm_integration.md#create-rosa-placement)

- [Bind the import policy to a Red Hat OpenShift Service on AWS (classic) placement definition](mce_acm_integration.md#bind-rosa-placement)

</div>

<a id="creating-rosa-policy"></a>

### Create the automatic import policy

Create an automatic import policy as an example of how to import all your discovered Red Hat OpenShift Service on AWS (classic) clusters automatically. Log in to your hub cluster from the CLI to complete the following procedure:

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You need Red Hat Advanced Cluster Management installed. See the Red Hat Advanced Cluster Management [Get started with Red Hat Advanced Cluster Management](get_started.md#get-started-acm) documentation.

- You need to learn about *Policies*. See the introduction to [Governance](governance.md#governance) in the Red Hat Advanced Cluster Management documentation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file with the following example and apply the changes that are referenced in the next steps:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: policy-rosa-autoimport
      annotations:
        policy.open-cluster-management.io/standards: NIST SP 800-53
        policy.open-cluster-management.io/categories: CM Configuration Management
        policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
        policy.open-cluster-management.io/description: OpenShift Service on AWS discovered clusters can be automatically imported into
    Red Hat Advanced Cluster Management as managed clusters with this policy. You can select and configure those managed clusters so you can import. Configure filters or add an annotation if you do not want all of your OpenShift Service on AWS clusters to be automatically imported.
    spec:
      remediationAction: inform
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: rosa-autoimport-config
            spec:
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: v1
                    kind: ConfigMap
                    metadata:
                      name: discovery-config
                      namespace: open-cluster-management-global-set
                    data:
                      rosa-filter: ""
              remediationAction: enforce
              severity: low
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: policy-rosa-autoimport
            spec:
              remediationAction: enforce
              severity: low
              object-templates-raw: |
                {{- /* find the ROSA DiscoveredClusters */ -}}
                {{- range $dc := (lookup "discovery.open-cluster-management.io/v1" "DiscoveredCluster" "" "").items }}
                  {{- /* Check for the flag that indicates the import should be skipped */ -}}
                  {{- $skip := "false" -}}
                  {{- range $key, $value := $dc.metadata.annotations }}
                    {{- if and (eq $key "discovery.open-cluster-management.io/previously-auto-imported")
                               (eq $value "true") }}
                      {{- $skip = "true" }}
                    {{- end }}
                  {{- end }}
                  {{- /* if the type is ROSA and the status is Active */ -}}
                  {{- if and (eq $dc.spec.status "Active")
                             (contains (fromConfigMap "open-cluster-management-global-set" "discovery-config" "rosa-filter") $dc.spec.displayName)
                             (eq $dc.spec.type "ROSA")
                             (eq $skip "false") }}
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: discovery.open-cluster-management.io/v1
                    kind: DiscoveredCluster
                    metadata:
                      name: {{ $dc.metadata.name }}
                      namespace: {{ $dc.metadata.namespace }}
                    spec:
                      importAsManagedCluster: true
                  {{- end }}
                {{- end }}
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: policy-rosa-managedcluster-status
            spec:
              remediationAction: enforce
              severity: low
              object-templates-raw: |
                {{- /* Use the same DiscoveredCluster list to check ManagedCluster status */ -}}
                {{- range $dc := (lookup "discovery.open-cluster-management.io/v1" "DiscoveredCluster" "" "").items }}
                  {{- /* Check for the flag that indicates the import should be skipped */ -}}
                  {{- $skip := "false" -}}
                  {{- range $key, $value := $dc.metadata.annotations }}
                    {{- if and (eq $key "discovery.open-cluster-management.io/previously-auto-imported")
                               (eq $value "true") }}
                      {{- $skip = "true" }}
                    {{- end }}
                  {{- end }}
                  {{- /* if the type is ROSA and the status is Active */ -}}
                  {{- if and (eq $dc.spec.status "Active")
                             (contains (fromConfigMap "open-cluster-management-global-set" "discovery-config" "rosa-filter") $dc.spec.displayName)
                             (eq $dc.spec.type "ROSA")
                             (eq $skip "false") }}
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: cluster.open-cluster-management.io/v1
                    kind: ManagedCluster
                    metadata:
                      name: {{ $dc.spec.displayName }}
                      namespace: {{ $dc.spec.displayName }}
                    status:
                      conditions:
                        - type: ManagedClusterConditionAvailable
                          status: "True"
                  {{- end }}
                {{- end }}
    ```

2.  To enable automatic import, change the `spec.remediationAction` to `enforce`.

3.  Optional: Specify a value here to select a subset of the matching Red Hat OpenShift Service on AWS (classic) clusters, which are based on *discovered* cluster names. The `rosa-filter` has no value by default, so the filter does not restrict cluster names without a subset value.

4.  Run `oc apply -f <filename>.yaml -n <namespace>` to apply the file.

</div>

<a id="create-rosa-placement"></a>

### Create the Red Hat OpenShift Service on AWS (classic) placement definition

Create a placement definition that specifies the managed cluster for the policy deployment.

<div>

<div class="title">

Procedure

</div>

1.  Create the placement definition that selects only the `local-cluster`, which is a hub cluster that is managed. Use the following YAML sample:

    ``` yaml
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: placement-openshift-plus-hub
    spec:
      predicates:
      - requiredClusterSelector:
          labelSelector:
            matchExpressions:
            - key: name
                operator: In
                values:
                - local-cluster
    ```

2.  Run `oc apply -f placement.yaml -n <namespace>`, where `namespace` matches the namespace that you used for the policy that you previously created.

</div>

<a id="bind-rosa-placement"></a>

### Bind the import policy to a Red Hat OpenShift Service on AWS (classic) placement definition

Bind the policy to the placement after you create both resources.

<div>

<div class="title">

Procedure

</div>

1.  Connect the resources by using a `PlacementBinding`. See the following example where `placementRef` references the `Placement` that you created, and `subjects` references the `Policy` that you created:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: PlacementBinding
    metadata:
      name: binding-policy-rosa-autoimport
    placementRef:
      apiGroup: cluster.open-cluster-management.io
      kind: Placement
      name: placement-policy-rosa-autoimport
    subjects:
    - apiGroup: policy.open-cluster-management.io
      kind: Policy
      name: policy-rosa-autoimport
    ```

2.  To check the binding, run the following command:

    ``` bash
    oc get policies.policy.open-cluster-management.io policy-rosa-autoimport -n <namespace>
    ```

</div>

<a id="propagate-hosted-labels"></a>

## Label propagation for hosted clusters between Red Hat Advanced Cluster Management and multicluster engine operator hub clusters

Propagate user-defined labels to `ManagedCluster` resources across Red Hat Advanced Cluster Management and multicluster engine operator hub clusters for discovered hosted clusters. Labels can originate from a `HostedCluster` custom resource on an multicluster engine operator cluster or from a `ManagedCluster` on the Red Hat Advanced Cluster Management hub cluster.

You can propagate user-defined labels to `ManagedCluster` resources in two ways:

- From a `HostedCluster` custom resource: Labels added to a `HostedCluster` on the multicluster engine operator cluster are automatically applied to the corresponding `ManagedCluster` resource on the multicluster engine operator cluster and on the Red Hat Advanced Cluster Management hub cluster.

- From the Red Hat Advanced Cluster Management hub cluster: Labels added to a `ManagedCluster` on the Red Hat Advanced Cluster Management hub cluster are synced to the corresponding `ManagedCluster` on the multicluster engine operator cluster.

  **Notes:**

  - The `HostedCluster` custom resource is the source of truth. If a label conflict exists, the `HostedCluster` value takes precedence. System-managed labels are not propagated.

  - Labels with the `cluster.open-cluster-management.io/` prefix are propagated. This allows `ClusterSet` membership label, `cluster.open-cluster-management.io/clusterset`, to be synced across hub clusters.

- System labels excluded from propagation

  The following exact key labels are never propagated: `name`, `vendor`, `cloud`, `region`, `openshiftVersion`, `openshiftVersion-major`, `openshiftVersion-major-minor`, `clusterID`, `local-cluster`, `velero.io/exclude-from-backup`

  See the following prefix-based exclusions: `open-cluster-management.io/`, `kubernetes.io/`, `openshift.io/`, `k8s.io/`

- Label conflict behavior

  The controller only propagates new labels and does not overwrite existing labels that it is not already tracking. The following rules apply:

- If the label key does not exist on the target `ManagedCluster`, the label is added and tracked.

- If the label key already exists on the target with the same value, the label is tracked but not modified.

- If the label key already exists on the target with a different value and the controller is already tracking it, the value is overwritten with the source value.

- If the label key already exists on the target with a different value and the controller is not tracking it, the label is not overwritten. The existing local value is preserved.

The controller tracks which labels it has propagated using the following annotations on the `ManagedCluster` resource:

`hypershift.open-cluster-management.io/propagated-labels`  
Labels propagated from the Red Hat Advanced Cluster Management hub cluster.

`hypershift.open-cluster-management.io/hc-propagated-labels`  
Labels propagated from the `HostedCluster` custom resource.

<div>

<div class="title">

Additional resources

</div>

- [Propagating HostedCluster labels to ManagedCluster resources](mce_acm_integration.md#propagate-labels-hc)

- [Propagating labels from Red Hat Advanced Cluster Management hub cluster to multicluster engine operator ManagedCluster resources](mce_acm_integration.md#propagate-labels-hub)

- [multicluster engine operator hosted cluster discovery in Red Hat Advanced Cluster Management](mce_acm_integration.md#discover-hosted-acm)

- [Automated import for discovered hosted clusters](mce_acm_integration.md#auto-import-hcp)

- [Discovering hosted clusters in the hypershift-addon-operator repository](https://github.com/stolostron/hypershift-addon-operator/blob/main/docs/management/discovering_hostedclusters.md)

</div>

<a id="propagate-labels-hc"></a>

### Propagating HostedCluster labels to ManagedCluster resources

Propagate labels from a `HostedCluster` custom resource on the multicluster engine operator cluster to the corresponding `ManagedCluster` resources on the multicluster engine operator and the Red Hat Advanced Cluster Management hub cluster. The `HostedCluster` is the source of truth. If the same label key exists with a different value, the `HostedCluster` value takes precedence.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Access to the multicluster engine operator cluster where the `HostedCluster` custom resources reside.

- `HostedCluster` custom resources exist on the multicluster engine operator cluster with hosted clusters that have been discovered by the Red Hat Advanced Cluster Management hub.

- You completed the shared prerequisites in *Label propagation for hosted clusters between Red Hat Advanced Cluster Management and multicluster engine operator hub clusters*.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the multicluster engine operator cluster.

2.  Add a label to the `HostedCluster` custom resource:

    ``` bash
    oc label hostedcluster <hosted-cluster-name> -n <namespace> env=production
    ```

3.  Verify the label was propagated to the corresponding `ManagedCluster` on the multicluster engine operator cluster:

    ``` bash
    oc get managedcluster <managed-cluster-name> --show-labels
    ```

4.  Verify the label was also propagated to the Red Hat Advanced Cluster Management hub `ManagedCluster` if the multicluster engine operator hub was imported.

5.  Verify that the controller is tracking propagated labels. Run the following command on the target cluster:

    ``` bash
    oc get managedcluster <managed-cluster-name> -o jsonpath='{.metadata.annotations}' | jq .
    ```

6.  Confirm that the `hypershift.open-cluster-management.io/hc-propagated-labels` annotation lists the label keys that you added to the `HostedCluster` custom resource.

7.  Untrack a label to stop the controller from managing a specific label. Remove that label key from the tracking annotation. Run the following command, if the `hc-propagated-labels` annotation contains `env,team` and you want to untrack `env`:

    ``` bash
    oc annotate managedcluster <managed-cluster-name> hypershift.open-cluster-management.io/hc-propagated-labels=team --overwrite
    ```

    **Note:** Once untracked, the controller no longer overwrites that label, and the administrator can set it to any local value. The label is not re-tracked unless it is removed from the target and re-propagated from the source.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Label propagation for hosted clusters between Red Hat Advanced Cluster Management and multicluster engine operator hub clusters](mce_acm_integration.md#propagate-hosted-labels)

- [Propagating labels from Red Hat Advanced Cluster Management hub cluster to multicluster engine operator ManagedCluster resources](mce_acm_integration.md#propagate-labels-hub)

</div>

<a id="propagate-labels-hub"></a>

### Propagating labels from Red Hat Advanced Cluster Management hub cluster to multicluster engine operator ManagedCluster resources

Propagate labels added to a `ManagedCluster` resource on the Red Hat Advanced Cluster Management hub cluster to sync corresponding `ManagedCluster` resources on the multicluster engine operator cluster. This allows centralized label management from the Red Hat Advanced Cluster Management hub cluster without accessing individual multicluster engine operator clusters.

**Important:** If a label key is owned by the `HostedCluster` (tracked in the `hc-propagated-labels` annotation), hub-to-spoke sync skips that key. The `HostedCluster` always takes precedence.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Access to the Red Hat Advanced Cluster Management hub cluster to add labels on `ManagedCluster` resources.

- The `ManagedCluster` on the Red Hat Advanced Cluster Management hub represents a discovered hosted cluster (with annotation `open-cluster-management/created-via: hypershift`).

- The corresponding multicluster engine operator cluster is reachable from the Red Hat Advanced Cluster Management hub.

- You completed the shared prerequisites in *Label propagation for hosted clusters between Red Hat Advanced Cluster Management and multicluster engine operator hub clusters*.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the Red Hat Advanced Cluster Management hub cluster.

2.  Identify `ManagedCluster` resources representing discovered hosted clusters. These are identified by the `open-cluster-management/created-via: hypershift` annotation:

    ``` bash
    oc get managedclusters -o json | jq -r '.items[] | select(.metadata.annotations["open-cluster-management/created-via"] == "hypershift") | .metadata.name'
    ```

3.  Add a label to the `ManagedCluster` on the Red Hat Advanced Cluster Management hub cluster:

    ``` bash
    oc label managedcluster <managed-cluster-name> env=production
    ```

4.  Verify the label was synced to the corresponding `ManagedCluster` on the multicluster engine operator cluster:

    ``` bash
    oc get managedcluster <managed-cluster-name> --show-labels
    ```

5.  Verify that the controller is tracking propagated labels. Run the following command on the multicluster engine operator cluster:

    ``` bash
    oc get managedcluster <managed-cluster-name> -o jsonpath='{.metadata.annotations}' | jq .
    ```

6.  Confirm that the `hypershift.open-cluster-management.io/propagated-labels` annotation lists the label keys that you added on the Red Hat Advanced Cluster Management hub cluster.

7.  Untrack a label to stop the controller from managing a specific label. Remove that label key from the tracking annotation. Run the following command, if the `propagated-labels` annotation contains `env,team` and you want to untrack `env` label:

    ``` bash
    oc annotate managedcluster <managed-cluster-name> hypershift.open-cluster-management.io/propagated-labels=team --overwrite
    ```

    **Note:** Once untracked, the controller no longer overwrites that label, and the administrator can set it to any local value. The label is not re-tracked unless it is removed from the target and re-propagated from the source.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Label propagation for hosted clusters between Red Hat Advanced Cluster Management and multicluster engine operator hub clusters](mce_acm_integration.md#propagate-hosted-labels)

- [Propagating HostedCluster labels to ManagedCluster resources](mce_acm_integration.md#propagate-labels-hc)

</div>

<a id="mce-acm-observability"></a>

## Observability integration

With the Red Hat Advanced Cluster Management observability feature, you can view health and utilization of clusters across your fleet. You can install Red Hat Advanced Cluster Management and enable observability.

After you enable the `multicluster-observability` pod, you can use Red Hat Advanced Cluster Management observability Grafana dashboards to view the following information about your hosted control planes:

- **ACM** \> **Hosted Control Planes Overview** dashboard to see cluster capacity estimates for hosting hosted control planes, the related cluster resources, and the list and status of existing hosted control planes. See *Introduction to hosted control planes*.

- **ACM** \> **Resources** \> **Hosted Control Plane** dashboard that you can access from the *Overview* page to see the resource utilization of the selected hosted control plane. See *Installing the hosted control planes command-line interface*.

To enable, see *Observability service*.

<div>

<div class="title">

Additional resources

</div>

- [Introduction to hosted control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/hosted-control-planes-overview#hosted-control-planes-overview_hcp-overview)

- [Installing the hosted control planes command-line interface](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/hosted_control_planes/preparing-to-deploy-hosted-control-planes#installing-the-hosted-control-plane-command-line-interface)

- [Observability service](observability.md#observing-environments-intro)

</div>

<a id="siteconfig"></a>

# SiteConfig

The SiteConfig operator offers a template-driven cluster provisioning solution with a unified `ClusterInstance` API, which comes from the `SiteConfig` API of the `SiteConfig` generator kustomize plugin.

- [About the SiteConfig operator](mce_acm_integration.md#siteconfig-about)

- [Installation templates](mce_acm_integration.md#siteconfig-templates)

  - [Default set of templates](mce_acm_integration.md#siteconfig-default-templates)

  - [Special template variables](mce_acm_integration.md#siteconfig-template-variables)

  - [Customization of the manifests order](mce_acm_integration.md#siteconfig-manifest-order)

  - [Configuration of additional annotations and labels](mce_acm_integration.md#siteconfig-annotations-labels)

  - [Permissible changes after provisioning](mce_acm_integration.md#siteconfig-permissible-changes)

- [Enable the SiteConfig operator](mce_acm_integration.md#enable-sco)

- [single-node OpenShift cluster installation with the SiteConfig operator](mce_acm_integration.md#install-sno-clusters)

  - [Create the target namespace](mce_acm_integration.md#create-target-namespace)

  - [Create the pull secret](mce_acm_integration.md#create-pull-secret)

  - [Create the BMC secret](mce_acm_integration.md#create-bmc-secret)

  - [Create the extra manifests](mce_acm_integration.md#create-extra-manifests)

  - [Render the installation manifests](mce_acm_integration.md#render-install-manifests)

- [Deprovision single-node OpenShift clusters with the SiteConfig operator](mce_acm_integration.md#deprovision-sno-clusters)

- [Image Based Install Operator](mce_acm_integration.md#ibio)

- [SiteConfig advanced topics](mce_acm_integration.md#siteconfig-advanced)

<a id="siteconfig-about"></a>

## About the SiteConfig operator

The SiteConfig operator offers a template-driven cluster provisioning solution, which allows you to provision clusters with various installation methods.

The SiteConfig operator introduces the unified `ClusterInstance` API, which comes from the `SiteConfig` API of the `SiteConfig` generator kustomize plugin.

The `ClusterInstance` API decouples parameters that define a cluster from the manner in which the cluster is deployed.

This separation removes certain limitations that are presented by the `SiteConfig` kustomize plugin in the current [GitOps Zero Touch Provisioning (ZTP) flow](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/edge_computing/ztp-deploying-far-edge-sites), such as agent cluster installations and scalability constraints that are related to Argo CD.

Using the unified `ClusterInstance` API, the SiteConfig operator offers the following improvements:

Isolation  
Separates the cluster definition from the installation method. The `ClusterInstance` custom resource captures the cluster definition, while installation templates capture the cluster architecture and installation methods.

Unification  
The SiteConfig operator unifies both Git and non-Git workflows. You can apply the `ClusterInstance` custom resource directly on the hub cluster, or synchronize resources through a GitOps solution, such as ArgoCD.

Consistency  
Maintains a consistent API across installation methods, whether you are using the Assisted Installer, the Image Based Install Operator, or any other custom template-based approach.

Scalability  
Achieves greater scalability for each cluster than the `SiteConfig` kustomize plugin.

Flexibility  
Provides you with more power to deploy and install clusters by using custom templates.

Troubleshooting  
Offers insightful information regarding cluster deployment status and rendered manifests, significantly enhancing the troubleshooting experience.

The SiteConfig operator dynamically generates installation manifests based on user-defined templates that are instantiated from the data in the `ClusterInstance` custom resource.

You can source the `ClusterInstance` custom resource from your Git repository through Argo CD, or you can create it directly on the hub cluster manually or through external tools and workflows.

The following is a high-level overview of the process:

1.  You create one or more sets of installation templates on the hub cluster.

2.  You create a `ClusterInstance` custom resource that references those installation templates and supporting manifests.

3.  After the resources are created, the SiteConfig operator reconciles the `ClusterInstance` custom resource by populating the templated fields that are referenced in the custom resource.

4.  The SiteConfig operator validates and renders the installation manifests, then the Operator performs a dry run.

5.  If the dry run is successful, the manifests are created, then the underlying Operators consume and process the manifests.

6.  The installation begins.

7.  The SiteConfig operator continuously monitors for changes in the associated `ClusterDeployment` resource and updates the `status` field of the `ClusterInstance` custom resource accordingly.

<div>

<div class="title">

Additional resources

</div>

- [Image Based Install Operator](mce_acm_integration.md#ibio)

- [Installing an on-premise cluster using the Assisted Installer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_an_on-premise_cluster_with_the_agent-based_installer/index)

</div>

<a id="siteconfig-templates"></a>

## Installation templates

Installation templates are data-driven templates that are used to generate the set of installation artifacts. These templates follow the Golang `text/template` format, and are instantiated by using data from the `ClusterInstance` custom resource. This enables dynamic creation of installation manifests for each target cluster that has similar configurations, but with different values.

You can also create multiple sets based on the different installation methods or cluster topologies. The SiteConfig operator supports the following types of installation templates:

Cluster-level  
Templates that must reference only cluster-specific fields.

Node-level  
Templates that can reference both cluster-specific and node-specific fields.

You can customize the templated fields. The SiteConfig operator supports all [Sprig library functions](https://masterminds.github.io/sprig/).

Additionally, the `ClusterInstance` API provides the following function that you can use while creating your custom manifests:

`toYaml`  
The `toYaml` function encodes an item into a YAML string. If the item cannot be converted to YAML, the function returns an empty string.

See the following example of the `.toYaml` specification in the `ClusterInstance.Spec.Proxy` field:

``` yaml
{{ if .Spec.Proxy }}
  proxy:
{{ .Spec.Proxy | toYaml | indent 4 }}
{{ end }}
```

<div>

<div class="title">

Additional resources

</div>

- [Default set of templates](mce_acm_integration.md#siteconfig-default-templates)

- [Special template variables](mce_acm_integration.md#siteconfig-template-variables)

- [Customization of the manifests order](mce_acm_integration.md#siteconfig-manifest-order)

- [Configuration of additional annotations and labels](mce_acm_integration.md#siteconfig-annotations-labels)

- [Permissible changes after provisioning](mce_acm_integration.md#siteconfig-permissible-changes)

</div>

<a id="siteconfig-default-templates"></a>

### Default set of templates

The SiteConfig operator provides the following default, validated, and immutable set of templates in the same namespace in which the operator is installed:

<table>
<caption>Default installation templates</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Installation method</th>
<th style="text-align: left;">Template type</th>
<th style="text-align: left;">File name</th>
<th style="text-align: left;">Template content</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Assisted Installer</p></td>
<td style="text-align: left;"><p>Cluster-level templates</p></td>
<td style="text-align: left;"><p><code>ai-cluster-templates-v1.yaml</code></p></td>
<td style="text-align: left;"><p><code>AgentClusterInstall</code><br />
<code>ClusterDeployment</code><br />
<code>InfraEnv</code><br />
<code>KlusterletAddonConfig</code><br />
<code>ManagedCluster</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Node-level templates</p></td>
<td style="text-align: left;"><p><code>ai-node-templates-v1.yaml</code></p></td>
<td style="text-align: left;"><p><code>BareMetalHost</code><br />
<code>NMStateConfig</code></p></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p>Image-based Install Operator</p></td>
<td style="text-align: left;"><p>Cluster-level templates</p></td>
<td style="text-align: left;"><p><code>ibi-cluster-templates-v1.yaml</code></p></td>
<td style="text-align: left;"><p><code>ClusterDeployment</code><br />
<code>KlusterletAddonConfig</code><br />
<code>ManagedCluster</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Node-level templates</p></td>
<td style="text-align: left;"><p><code>ibi-node-templates-v1.yaml</code></p></td>
<td style="text-align: left;"><p><code>BareMetalHost</code><br />
<code>ImageClusterInstall</code><br />
<code>NetworkSecret</code></p></td>
<td></td>
</tr>
</tbody>
</table>

For more information about the `ClusterInstance` API, use the *API Explorer* in the console, or an `oc` command.

<div>

<div class="title">

Additional resources

</div>

- [Installation templates](mce_acm_integration.md#siteconfig-templates)

</div>

<a id="siteconfig-template-variables"></a>

### Special template variables

The SiteConfig operator provides a set of special template variables that you can use in your templates. See the following list:

`CurrentNode`  
The SiteConfig operator explicitly controls the iteration of the node objects and exposes this variable to access all the content for the current node being handled in templating.

`InstallConfigOverrides`  
Contains the merged `networkType`, `cpuPartitioningMode` and `installConfigOverrides` content.

`ControlPlaneAgents`  
Consists of the number of control plane agents and it is automatically derived from the `ClusterInstance` node objects.

`WorkerAgents`  
Consists of the number of worker agents and it is automatically derived from the `ClusterInstance` node objects.

Capitalize the field name in the text template to create a custom templated field. For example, the `ClusterInstance` `spec` field is referenced with the `.Spec` prefix. However, you must reference special variable fields with the `.SpecialVars` prefix.

**Important:** Instead of using the `.Spec.Nodes` prefix for the `spec.nodes` field, you must reference it with the `.SpecialVars.CurrentNode` special template variable.

For example, if you want to specify the `name` and `namespace` for your current node by using the `CurrentNode` special template variable, use the field names in the following form:

``` yaml
name: "{{ .SpecialVars.CurrentNode.HostName }}"
namespace: "{{ .Spec.ClusterName }}"
```

<div>

<div class="title">

Additional resources

</div>

- [Installation templates](mce_acm_integration.md#siteconfig-templates)

</div>

<a id="siteconfig-manifest-order"></a>

### Customization of the manifests order

The `siteconfig.open-cluster-management.io/sync-wave` annotation controls the order in which manifests are created, updated, and deleted. The annotation takes an integer as a *wave*; you can add one or several manifests to a single wave, and the default value is `0` if you do not specify a value. The SiteConfig operator reconciles the manifests in ascending order when creating or updating resources and deletes resources in descending order.

In the following example, if the SiteConfig operator creates or updates the manifests, the `AgentClusterInstall` and `ClusterDeployment` custom resources are reconciled in the first wave, while `KlusterletAddonConfig` and `ManagedCluster` custom resources are reconciled in the third wave:

``` yaml
apiVersion: v1
data:
  AgentClusterInstall: |-
    ...
        siteconfig.open-cluster-management.io/sync-wave: "1"
    ...
  ClusterDeployment: |-
    ...
        siteconfig.open-cluster-management.io/sync-wave: "1"
    ...
  InfraEnv: |-
    ...
        siteconfig.open-cluster-management.io/sync-wave: "2"
    ...
  KlusterletAddonConfig: |-
    ...
        siteconfig.open-cluster-management.io/sync-wave: "3"
    ...
  ManagedCluster: |-
    ...
        siteconfig.open-cluster-management.io/sync-wave: "3"
    ...
kind: ConfigMap
metadata:
  name: assisted-installer-templates
  namespace: example-namespace
```

If the SiteConfig operator deletes the resources, `KlusterletAddonConfig` and `ManagedCluster` custom resources are the first to be deleted, while the `AgentClusterInstall` and `ClusterDeployment` custom resources are the last.

<div>

<div class="title">

Additional resources

</div>

- [Installation templates](mce_acm_integration.md#siteconfig-templates)

</div>

<a id="siteconfig-annotations-labels"></a>

### Configuration of additional annotations and labels

The SiteConfig operator applies additional annotations and labels to the manifests that you specify in the `ClusterInstance` resource. You can configure them for cluster-level and node-level installation manifests by using the `extraAnnotations` and `extraLabels` fields in the `ClusterInstance` API. A manifest type is required so that the SiteConfig operator applies them to all matching manifests. The annotations and labels are arbitrary, and you can set any key and value pairs that are meaningful to your applications.

**Note:** The additional annotations and labels are only applied to the resources that were rendered through the referenced templates.

View the following example application of `extraAnnotations` and `extraLabels`:

``` yaml
apiVersion: siteconfig.open-cluster-management.io/v1alpha1
kind: ClusterInstance
metadata:
  name: "example-sno"
  namespace: "example-sno"
spec:
  [...]
  clusterName: "example-sno"
  extraAnnotations:
    ClusterDeployment:
      myClusterAnnotation: success
  extraLabels:
    ManagedCluster:
      common: "true"
      group-du: ""
  nodes:
    - hostName: "example-sno.example.redhat.com"
      role: "master"
      extraAnnotations:
        BareMetalHost:
          myNodeAnnotation: success
      extraLabels:
        BareMetalHost:
          "testExtraLabel": "success"
```

- This field supports cluster-level annotations and labels that the SiteConfig operator applies to the `ManagedCluster` and `ClusterDeployment` manifests.

- This field supports node-level annotations and labels that the SiteConfig operator applies to the `BareMetalHost` manifest.

- The `extraAnnotations` in this `BareMetalHost` example is `myNodeAnnotation`.

- The `extraLabels` in this `BareMetalHost` example is `testExtraLabel`.

You can verify that your additional labels with the following command:

``` terminal
oc get managedclusters example-sno -ojsonpath='{.metadata.labels}' | jq
```

View the following example of applied labels:

``` json
{
  "common": "true",
  "group-du": "",
  ...
}
```

The following command verifies that your additional annotations:

``` terminal
oc get bmh example-sno.example.redhat.com -n example-sno -ojsonpath='{.metadata.annotations}' | jq
```

View the following example of applied annotations:

``` json
{
  "myNodeAnnotation": "success",
  ...
}
```

<div>

<div class="title">

Additional resources

</div>

- [Installation templates](mce_acm_integration.md#siteconfig-templates)

</div>

<a id="siteconfig-permissible-changes"></a>

### Permissible changes after provisioning

Changes to the cluster configuration are not allowed during provisioning. After a cluster is provisioned, you can modify the following fields.

- `spec.extraAnnotations`

- `spec.extraLabels`

- `spec.suppressedManifests`

- `spec.pruneManifests`

- `spec.clusterImageSetNameRef`

- `spec.nodes.<node-id>.extraAnnotations`

- `spec.nodes.<node-id>.extraLabels`

- `spec.nodes.<node-id>.suppressedManifests`

- `spec.nodes.<node-id>.pruneManifests`

<div>

<div class="title">

Additional resources

</div>

- [Installation templates](mce_acm_integration.md#siteconfig-templates)

</div>

<a id="enable-sco"></a>

## Enable the SiteConfig operator

Enable the SiteConfig operator to use the default installation templates and install single-node OpenShift clusters at scale. Patch the `MultiClusterHub` resource, then verify that SiteConfig operator is enabled. Complete the following procedure.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You need a Red Hat Advanced Cluster Management hub cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set an environment variable that matches the namespace of the `MultiClusterHub` operator by running the following command:

    ``` terminal
    export MCH_NAMESPACE=<namespace>
    ```

2.  Set the `enabled` field to `true` in the `siteconfig` entry of `spec.overrides.components` in the `Multiclusterhub` resource by running the following command:

    ``` terminal
    oc patch multiclusterhubs.operator.open-cluster-management.io multiclusterhub -n ${MCH_NAMESPACE} --type json --patch '[{"op": "add", "path":"/spec/overrides/components/-", "value": {"name":"siteconfig","enabled": true}}]'
    ```

3.  Verify that the SiteConfig operator is enabled by running the following command on the hub cluster:

    ``` terminal
    oc -n ${MCH_NAMESPACE} get po | grep siteconfig
    ```

    See the following example output:

    ``` terminal
    siteconfig-controller-manager-6fdd86cc64-sdg87                    2/2     Running   0             43s
    ```

4.  **Optional:** Verify that you have the default installation templates by running the following command on the hub cluster:

    ``` terminal
    oc -n ${MCH_NAMESPACE} get cm
    ```

    See the following list of templates in the output example:

    ``` terminal
    NAME                                DATA   AGE
    ai-cluster-templates-v1             5      97s
    ai-node-templates-v1                2      97s
    ...
    ibi-cluster-templates-v1            3      97s
    ibi-node-templates-v1               3      97s
    ...
    ```

</div>

<a id="install-sno-clusters"></a>

## single-node OpenShift cluster installation with the SiteConfig operator

Installation of single-node OpenShift clusters with the SiteConfig operator uses the default installation templates.

Install your clusters with the SiteConfig operator by using the default installation templates. **Required access:** Cluster administrator

<div>

<div class="title">

Additional resources

</div>

- [Create the target namespace](mce_acm_integration.md#create-target-namespace)

- [Create the pull secret](mce_acm_integration.md#create-pull-secret)

- [Create the BMC secret](mce_acm_integration.md#create-bmc-secret)

- [Create the extra manifests](mce_acm_integration.md#create-extra-manifests)

- [Render the installation manifests](mce_acm_integration.md#render-install-manifests)

</div>

<a id="create-target-namespace"></a>

### Create the target namespace

Create a target namespace for the pull secret, the BMC secret, extra manifest `ConfigMap` objects, and the `ClusterInstance` custom resource. You need a target namespace when you create the pull secret, the BMC secret, extra manifest `ConfigMap` objects, and the `ClusterInstance` custom resource. Complete the following steps to create the target namespace.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- If you are using GitOps ZTP, configure your GitOps ZTP environment. To configure your environment, see [Preparing the hub cluster for GitOps ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/edge_computing/ztp-preparing-the-hub-cluster).

- You have the default installation templates. To get familiar with the default templates, see [Default set of templates](mce_acm_integration.md#siteconfig-default-templates)

- Install and configure the underlying operator of your choice.

  - To learn about and install the Image Based Install Operator for single-node OpenShift, see [Image Based Install Operator](mce_acm_integration.md#ibio).

  - To install the Assisted Installer, see [Installing an on-premise cluster with the Assisted Installer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/installing_an_on-premise_cluster_with_the_agent-based_installer/index).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file for the target namespace. See the following example file that is named `clusterinstance-namespace.yaml`:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: example-sno
    ```

2.  Apply your file to create the resource. Run the following command on the hub cluster:

    ``` terminal
    oc apply -f clusterinstance-namespace.yaml
    ```

</div>

<a id="create-pull-secret"></a>

### Create the pull secret

Create a pull secret to enable your clusters to pull images from container registries. You need a pull secret to enable your clusters to pull images from container registries. Complete the following steps to create a pull secret.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file to pull images. See the following example of a file that is named `pull-secret.yaml`:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: pull-secret
      namespace: example-sno
    data:
      .dockerconfigjson: <encoded_docker_configuration>
    type: kubernetes.io/dockerconfigjson
    ```

    - Ensure that the `namespace` value matches the target namespace.

    - Specify the base64-encoded configuration file as the value.

2.  Apply the file to create the resource. Run the following command on the hub cluster:

    ``` terminal
    oc apply -f pull-secret.yaml
    ```

</div>

<a id="create-bmc-secret"></a>

### Create the BMC secret

Create a secret to connect to your baseboard management controller (BMC). You need a secret to connect to your baseboard management controller (BMC). Complete the following steps to create a secret.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file for the BMC secret. See the following sample file that is named `example-bmc-secret.yaml`:

    ``` yaml
    apiVersion: v1
    data:
      password: <password>
      username: <username>
    kind: Secret
    metadata:
      name: example-bmh-secret
      namespace: "example-sno"
    type: Opaque
    ```

    - Ensure that the `namespace` value matches the target namespace.

2.  Apply the file to create the resource. Run the following command on the hub cluster:

    ``` terminal
    oc apply -f example-bmc-secret.yaml
    ```

</div>

<a id="create-extra-manifests"></a>

### Create the extra manifests

Create extra manifests that you need to reference in the `ClusterInstance` custom resource. You can create extra manifests that you need to reference in the `ClusterInstance` custom resource. Complete the following steps to create an extra manifest.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file for an extra manifest `ConfigMap` object, for example named `enable-crun.yaml`:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: enable-crun
      namespace: example-sno
    data:
      enable-crun-master.yaml: |
        apiVersion: machineconfiguration.openshift.io/v1
        kind: ContainerRuntimeConfig
        metadata:
          name: enable-crun-master
        spec:
          machineConfigPoolSelector:
            matchLabels:
              pools.operator.machineconfiguration.openshift.io/master: ""
          containerRuntimeConfig:
            defaultRuntime: crun
      enable-crun-worker.yaml: |
        apiVersion: machineconfiguration.openshift.io/v1
        kind: ContainerRuntimeConfig
        metadata:
          name: enable-crun-worker
        spec:
          machineConfigPoolSelector:
            matchLabels:
              pools.operator.machineconfiguration.openshift.io/worker: ""
          containerRuntimeConfig:
            defaultRuntime: crun
    ```

    - Ensure that the `namespace` value matches the target namespace.

2.  Create the resource by running the following command on the hub cluster:

    ``` terminal
    oc apply -f enable-crun.yaml
    ```

</div>

<a id="render-install-manifests"></a>

### Render the installation manifests

Render the installation manifests by referencing the templates and supporting manifests in the `ClusterInstance` custom resource. Reference the templates and supporting manifests in the `ClusterInstance` custom resource. Complete the following steps to render the installation manifests by using the default cluster and node templates.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  In the `example-sno` namespace, create the `ClusterInstance` custom resource that is named `clusterinstance-ibi.yaml` in the following example:

    ``` yaml
    apiVersion: siteconfig.open-cluster-management.io/v1alpha1
    kind: ClusterInstance
    metadata:
      name: "example-clusterinstance"
      namespace: "example-sno"
    spec:
      #clusterType: "SNO"
      holdInstallation: false
      extraManifestsRefs:
        - name: extra-machine-configs
        - name: enable-crun
      pullSecretRef:
        name: "pull-secret"
      [...]
      clusterName: "example-sno"
      [...]
      clusterImageSetNameRef: "img4.17-x86-64"
      [...]
      reference:
      [...]
        namespace:
        [...]
      templateRefs:
        - name: ibi-cluster-templates-v1
          namespace: rhacm
          hostRef:
            - name: example-bmh
              namespace: example-sno
      [...]
      nodes:
          [...]
          bmcCredentialsName:
            name: "example-bmh-secret"
          [...]
          templateRefs:
            - name: ibi-node-templates-v1
              namespace: rhacm
          [...]
    ```

2.  Ensure that the `namespace` in the `ClusterInstance` custom resource matches the target namespace that you defined.

3.  **Optional:** If you want to scale out or scale in your single-node OpenShift clusters, you must set the `spec.clusterType` field to `"SNO"`.

4.  Reference the `name` of one or more extra manifests `ConfigMap` objects.

5.  Reference the `name` of your pull secret.

6.  Ensure that the value of the `clusterName` field in the `ClusterInstance` custom resource matches the value of the `namespace` field.

7.  Specify dependencies or related objects in different namespaces.

8.  Specify the namespace of the reference object.

9.  Reference the `name` of the cluster-level templates in the `spec.templateRefs` field. If you are using a default installation template, the `namespace` must match the namespace where the Operator is installed.

10. Specify a reference to a `BareMetalHost` resource that is in a different namespace.

11. Reference the `name` of the BMC secret.

12. Reference the `name` of the node-level templates in the `spec.nodes.templateRefs` field. If you are using a default installation template, the `namespace` must match the namespace where the Operator is installed.

13. Apply the file and create the resource by running the following command:

    ``` terminal
    oc apply -f clusterinstance-ibi.yaml
    ```

    After you create the custom resource, the SiteConfig operator starts reconciling the `ClusterInstance` custom resource, then validates and renders the installation manifests.

    The SiteConfig operator continues to monitor for changes in the `ClusterDeployment` custom resources to update the cluster installation progress of the corresponding `ClusterInstance` custom resource.

14. Monitor the process by running the following command:

    ``` terminal
    oc get clusterinstance <cluster_name> -n <target_namespace> -o yaml
    ```

    See the following example output from the `status.conditions` section for successful manifest generation:

    ``` terminal
    message: Applied site config manifests
    reason: Completed
    status: "True"
    type: RenderedTemplatesApplied
    ```

15. Check the manifests that SiteConfig operator rendered by running the following command:

    ``` terminal
    oc get clusterinstance <cluster_name> -n <target_namespace> -o jsonpath='{.status.manifestsRendered}'
    ```

    For more information about status conditions, use the *API Explorer* in the console, or an `oc` command.

</div>

<a id="deprovision-sno-clusters"></a>

## Deprovision single-node OpenShift clusters with the SiteConfig operator

Deprovision your clusters with the SiteConfig operator to delete all resources and accesses associated with that cluster. Complete the following steps to delete your clusters.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- Deploy your clusters with the SiteConfig operator by using the default installation templates.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Delete the `ClusterInstance` custom resource by running the following command:

    ``` bash
    oc delete clusterinstance <cluster_name> -n <target_namespace>
    ```

2.  Verify that the deletion was successful by running the following command:

    ``` bash
    oc get clusterinstance <cluster_name> -n <target_namespace>
    ```

    See the following example output where the `(NotFound)` error indicates that your cluster is deprovisioned.

    ``` terminal
    Error from server (NotFound): clusterinstances.siteconfig.open-cluster-management.io "<cluster_name>" not found
    ```

</div>

<a id="ibio"></a>

## Image Based Install Operator

The Image Based Install Operator completes and manages image-based cluster installations by using the same APIs as existing installation methods.

Install the Image Based Install Operator so that you can complete and manage image-based cluster installations by using the same APIs as existing installation methods.

For more information about, and to learn how to enable the Image Based Install Operator, see [Image-based installations for single-node OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/edge_computing/image-based-installation-for-single-node-openshift).

<a id="siteconfig-advanced"></a>

## SiteConfig advanced topics

The SiteConfig operator provides additional functionalities, such as creating custom templates or scaling worker nodes, expanding the standard operations that apply to most use cases.

<div>

<div class="title">

Additional resources

</div>

- [Create custom templates with the SiteConfig operator](mce_acm_integration.md#create-custom-templates)

- [Add an annotation to your worker node](mce_acm_integration.md#annotate-worker-node)

- [Delete the `BareMetalHost` resource of the worker node](mce_acm_integration.md#delete-worker-bmh)

- [Scale out a single-node OpenShift cluster with the SiteConfig operator](mce_acm_integration.md#scale-out-sno)

- [Mirror images for disconnected environments](mce_acm_integration.md#mirror-disconnected-images)

- [Cluster reinstallation with the SiteConfig operator (Technology Preview)](mce_acm_integration.md#cluster-reinstallation)

  - [Resource labeling for preservation](mce_acm_integration.md#resource-preservation-labels)

  - [Cluster reinstallation monitoring](mce_acm_integration.md#reinstallation-monitoring)

- [Reinstallation of a cluster with the SiteConfig operator (Technology Preview)](mce_acm_integration.md#reinstall-cluster)

  - [Enable cluster reinstallation](mce_acm_integration.md#enable-cluster-reinstallation)

  - [Label resources for preservation](mce_acm_integration.md#label-preservation-resources)

  - [Initiate a cluster reinstallation](mce_acm_integration.md#initiate-cluster-reinstallation)

  - [Monitor the cluster reinstallation](mce_acm_integration.md#monitor-cluster-reinstallation)

- [Hardware replacement with Image-Based Break/Fix for single-node OpenShift (Technology Preview)](mce_acm_integration.md#ibbf-hardware-replacement)

  - [Initiate the Image-Based Break/Fix cluster reinstallation](mce_acm_integration.md#initiate-ibbf-reinstallation)

</div>

<a id="create-custom-templates"></a>

### Create custom templates with the SiteConfig operator

Create user-defined templates that are not provided in the default set of templates. Complete the following steps to create a custom template.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file named `my-custom-secret.yaml` that contains the cluster-level template in a `ConfigMap` object:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: my-custom-secret
      namespace: rhacm
    data:
      MySecret: |-
        apiVersion: v1
        kind: Secret
        metadata:
          name: "{{ .Spec.ClusterName }}-my-custom-secret-key"
          namespace: "clusters"
          annotations:
            siteconfig.open-cluster-management.io/sync-wave: "1"
        type: Opaque
        data:
          key: <key>
    ```

    - The `siteconfig.open-cluster-management.io/sync-wave` annotation controls in which order manifests are created, updated, or deleted.

2.  Apply the custom template on the hub cluster by running the following command:

    ``` terminal
    oc apply -f my-custom-secret.yaml
    ```

3.  Reference your template in the `ClusterInstance` custom resource named `clusterinstance-my-custom-secret.yaml`:

    ``` yaml
    spec:
        ...
      templateRefs:
        - name: ai-cluster-templates-v1.yaml
          namespace: rhacm
        - name: my-custom-secret.yaml
          namespace: rhacm
        ...
    ```

4.  Apply the `ClusterInstance` custom resource by running the following command:

    ``` terminal
    oc apply -f clusterinstance-my-custom-secret.yaml
    ```

</div>

<a id="annotate-worker-node"></a>

### Add an annotation to your worker node

Scale-in of a single-node OpenShift cluster removes a worker node from a cluster that was installed by the SiteConfig operator. Add an annotation to your worker node for removal. Complete the following steps to annotate a worker node from the managed cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- If you are using GitOps ZTP, you have configured your GitOps ZTP environment. To configure your environment, see [Preparing the hub cluster for GitOps ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/edge_computing/ztp-preparing-the-hub-cluster).

- You have the default templates. To get familiar with the default templates, see [Default set of templates](mce_acm_integration.md#siteconfig-default-templates)

- You have installed your cluster with the SiteConfig operator. To install a cluster with the SiteConfig operator, see [single-node OpenShift cluster installation with the SiteConfig operator](mce_acm_integration.md#install-sno-clusters)

- You have set the `spec.clusterType` to `"SNO"`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add an annotation in the `extraAnnotations` field of the worker node entry in the `ClusterInstance` custom resource that is used to provision your cluster:

    ``` yaml
    spec:
       ...
       nodes:
       - hostName: "worker-node2.example.com"
          role: "worker"
          ironicInspect: ""
          extraAnnotations:
            BareMetalHost:
              bmac.agent-install.openshift.io/remove-agent-and-node-on-delete: "true"
    ...
    ```

2.  Apply the changes. See the following options:

    - If you are using Red Hat Advanced Cluster Management without Red Hat OpenShift GitOps, run the following command on the hub cluster:

      ``` terminal
      oc apply -f <clusterinstance>.yaml
      ```

    - If you are using GitOps ZTP, push to your Git repository and wait for Argo CD to synchronize the changes.

3.  Verify that the annotation is applied to the `BaremetalHost` worker resource by running the following command on the hub cluster:

    ``` terminal
    oc get bmh -n <clusterinstance_namespace> worker-node2.example.com -ojsonpath='{.metadata.annotations}' | jq
    ```

    See the following example output for successful application of the annotation:

    ``` terminal
    {
      "baremetalhost.metal3.io/detached": "assisted-service-controller",
      "bmac.agent-install.openshift.io/hostname": "worker-node2.example.com",
      "bmac.agent-install.openshift.io/remove-agent-and-node-on-delete": "true"
      "bmac.agent-install.openshift.io/role": "master",
      "inspect.metal3.io": "disabled",
      "siteconfig.open-cluster-management.io/sync-wave": "1",
    }
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Delete the `BareMetalHost` resource of the worker node](mce_acm_integration.md#delete-worker-bmh)

</div>

<a id="delete-worker-bmh"></a>

### Delete the `BareMetalHost` resource of the worker node

Delete the `BareMetalHost` resource of the worker node that you want to be removed. Complete the following steps to remove a worker node from the managed cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Update the node object that you want to delete in your existing `ClusterInstance` custom resource with the following configuration:

    ``` yaml
    ...
    spec:
       ...
       nodes:
         - hostName: "worker-node2.example.com"
           ...
           pruneManifests:
             - apiVersion: metal3.io/v1alpha1
                kind: BareMetalHost
             - apiVersion: agent-install.openshift.io/v1beta1
                kind: InfraEnv
             - apiVersion: agent-install.openshift.io/v1beta1
                kind: NMStateConfig
    ...
    ```

2.  Apply the changes. See the following options:

    - If you are using Red Hat Advanced Cluster Management without Red Hat OpenShift GitOps, run the following command on the hub cluster:

      ``` terminal
      oc apply -f <clusterinstance>.yaml
      ```

    - If you are using GitOps ZTP, push to your Git repository and wait for Argo CD to synchronize the changes.

3.  Verify that the `BareMetalHost` resources are removed by running the following command on the hub cluster:

    ``` terminal
    oc get bmh -n <clusterinstance_namespace> --watch --kubeconfig <hub_cluster_kubeconfig_filename>
    ```

    See the following example output:

    ``` terminal
    NAME                        STATE                        CONSUMER         ONLINE   ERROR   AGE
    master-node1.example.com    provisioned                  true             81m
    worker-node2.example.com    deprovisioning               true             44m
    worker-node2.example.com    powering off before delete   true             20h
    worker-node2.example.com    deleting                     true             50m
    ```

4.  Verify that the `Agent` resources are removed by running the following command on the hub cluster:

    ``` terminal
    oc get agents -n <clusterinstance_namespace> --kubeconfig <hub_cluster_kubeconfig_filename>
    ```

    See the following example output:

    ``` terminal
    NAME                       CLUSTER                  APPROVED   ROLE     STAGE
    master-node1.example.com   <managed_cluster_name>   true       master   Done
    master-node2.example.com   <managed_cluster_name>   true       master   Done
    master-node3.example.com   <managed_cluster_name>   true       master   Done
    worker-node1.example.com   <managed_cluster_name>   true       worker   Done
    ```

5.  Verify that the `Node` resources are removed by running the following command on the managed cluster:

    ``` terminal
    oc get nodes --kubeconfig <managed_cluster_kubeconfig_filename>
    ```

    See the following example output:

    ``` terminal
    NAME                       STATUS                        ROLES                  AGE   VERSION
    worker-node2.example.com   NotReady,SchedulingDisabled   worker                 19h   v1.30.5
    worker-node1.example.com   Ready                         worker                 19h   v1.30.5
    master-node1.example.com   Ready                         control-plane,master   19h   v1.30.5
    master-node2.example.com   Ready                         control-plane,master   19h   v1.30.5
    master-node3.example.com   Ready                         control-plane,master   19h   v1.30.5
    ```

6.  After the `BareMetalHost` object of the worker node is successfully deleted, remove the associated worker node definition from the `spec.nodes` section in the `ClusterInstance` resource.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Add an annotation to your worker node](mce_acm_integration.md#annotate-worker-node)

</div>

<a id="scale-out-sno"></a>

### Scale out a single-node OpenShift cluster with the SiteConfig operator

Scale out your managed cluster that was installed by the SiteConfig operator. You can scale out your cluster by adding a worker node. Add a worker node by updating your `ClusterInstance` custom resource that is used to provision your cluster. Complete the following steps to add a worker node to the managed cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- If using GitOps ZTP, you have configured your GitOps ZTP environment. To configure your environment, see [Preparing the hub cluster for GitOps ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/edge_computing/ztp-preparing-the-hub-cluster).

- You have the default installation templates. To get familiar with the default templates, see [Default set of templates](mce_acm_integration.md#siteconfig-default-templates).

- You have installed your cluster with the SiteConfig operator. To install a cluster with the SiteConfig operator, see [single-node OpenShift cluster installation with the SiteConfig operator](mce_acm_integration.md#install-sno-clusters).

- You have set the `spec.clusterType` to `"SNO"`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Define a new node object in the existing `ClusterInstance` custom resource:

    ``` yaml
    spec:
      ...
      nodes:
        - hostName: "<host_name>"
          role: "worker"
          templateRefs:
            - name: ai-node-templates-v1
              namespace: rhacm
          bmcAddress: "<bmc_address>"
          bmcCredentialsName:
            name: "<bmc_credentials_name>"
          bootMACAddress: "<boot_mac_address>"
    ...
    ```

2.  Apply the changes. See the following options:

    - If you are using Red Hat Advanced Cluster Management without Red Hat OpenShift GitOps, run the following command on the hub cluster:

      ``` terminal
      oc apply -f <clusterinstance>.yaml
      ```

    - If you are using GitOps ZTP, push to your Git repository and wait for Argo CD to synchronize the changes.

3.  Verify that a new `BareMetalHost` resource is added by running the following command on the hub cluster:

    ``` terminal
    oc get bmh -n <clusterinstance_namespace> --watch --kubeconfig <hub_cluster_kubeconfig_filename>
    ```

    See the following example output:

    ``` terminal
    NAME                        STATE          CONSUMER   ONLINE   ERROR   AGE
    master-node1.example.com    provisioned               true             81m
    worker-node2.example.com    provisioning              true             44m
    ```

4.  Verify that a new `Agent` resource is added by running the following command on the hub cluster:

    ``` terminal
    oc get agents -n <clusterinstance_namespace> --kubeconfig <hub_cluster_kubeconfig_filename>
    ```

    See the following example output:

    ``` terminal
    NAME                       CLUSTER                   APPROVED    ROLE     STAGE
    master-node1.example.com   <managed_cluster_name>    true        master   Done
    master-node2.example.com   <managed_cluster_name>    true        master   Done
    master-node3.example.com   <managed_cluster_name>    true        master   Done
    worker-node1.example.com   <managed_cluster_name>    false       worker
    worker-node2.example.com   <managed_cluster_name>    true        worker   Starting installation
    worker-node2.example.com   <managed_cluster_name>    true        worker   Installing
    worker-node2.example.com   <managed_cluster_name>    true        worker   Writing image to disk
    worker-node2.example.com   <managed_cluster_name>    true        worker   Waiting for control plane
    worker-node2.example.com   <managed_cluster_name>    true        worker   Rebooting
    worker-node2.example.com   <managed_cluster_name>    true        worker   Joined
    worker-node2.example.com   <managed_cluster_name>    true        worker   Done
    ```

5.  Verify that a new `Node` resource is added by running the following command on the managed cluster:

    ``` terminal
    oc get nodes --kubeconfig <managed_cluster_kubeconfig_filename>
    ```

    See the following example output:

    ``` terminal
    NAME                       STATUS    ROLES                  AGE   VERSION
    worker-node2.example.com   Ready     worker                 1h    v1.30.5
    worker-node1.example.com   Ready     worker                 19h   v1.30.5
    master-node1.example.com   Ready     control-plane,master   19h   v1.30.5
    master-node2.example.com   Ready     control-plane,master   19h   v1.30.5
    master-node3.example.com   Ready     control-plane,master   19h   v1.30.5
    ```

</div>

<a id="mirror-disconnected-images"></a>

### Mirror images for disconnected environments

Mirror images as extra manifests in the `ClusterInstance` custom resource when you deploy clusters with the Image Based Install Operator in a disconnected environment. You can deploy a cluster with the SiteConfig operator operator by using the Image Based Install Operator as your underlying operator. If you deploy your clusters with the Image Based Install Operator in a disconnected environment, you must supply your mirror images as extra manifests in the `ClusterInstance` custom resource. Complete the following steps to mirror images for disconnected environments.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file named `idms-configmap.yaml` for your `ImageDigestMirrorSet` object that contains your mirror registry locations:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: "idms-configmap"
      namespace: "example-sno"
    data:
      99-example-idms.yaml: |
        apiVersion: config.openshift.io/v1
        kind: ImageDigestMirrorSet
        metadata:
          name: example-idms
        spec:
          imageDigestMirrors:
          - mirrors:
            - mirror.registry.example.com/image-repo/image
            source: registry.example.com/image-repo/image
    ```

    **Important:** Define the `ConfigMap` resource that contains the extra manifest in the same namespace as the `ClusterInstance` resource.

2.  Create the resource by running the following command on the hub cluster:

    ``` terminal
    oc apply -f idms-configmap.yaml
    ```

3.  Reference your `ImageDigestMirrorSet` object in the `ClusterInstance` custom resource:

    ``` yaml
    apiVersion: siteconfig.open-cluster-management.io/v1alpha1
    kind: ClusterInstance
    metadata:
      name: "example-sno"
      namespace: "example-sno"
    spec:
      ...
      extraManifestsRefs:
        - name: idms-configmap
    ...
    ```

</div>

<a id="cluster-reinstallation"></a>

### Cluster reinstallation with the SiteConfig operator (Technology Preview)

The SiteConfig operator simplifies OpenShift cluster reinstallation through the `ClusterInstance` API while preserving critical configuration data.

With a GitOps-compatible, declarative approach, users can begin reinstallations by updating the `ClusterInstance` resource. The operator also includes a backup and restore mechanism for hub-side `Secret` and `ConfigMap` resources, ensuring essential cluster data, such as authentication credentials and configuration resources, remains intact.

- Cluster identity preservation: Cluster reinstallation supports both single-node OpenShift and multi-node OpenShift clusters. However, cluster identity preservation is only supported for single-node OpenShift clusters installed using the Image Based Install provisioning method. For more information about the Image Based Install, see [Image-based installation for single-node OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/edge_computing/image-based-installation-for-single-node-openshift#deploying-single-node-openshift-clusters).

See the following steps of the cluster reinstallation workflow:

- Label resources for preservation. This is optional if you do not want to preserve resources. You can label your resources well before initiating the cluster reinstallation.

- Initiate a cluster reinstallation.

- Monitor the reinstallation progress and verify that the reinstalled cluster is available. This is optional.

<div>

<div class="title">

Additional resources

</div>

- [Resource labeling for preservation](mce_acm_integration.md#resource-preservation-labels)

- [Cluster reinstallation monitoring](mce_acm_integration.md#reinstallation-monitoring)

</div>

<a id="resource-preservation-labels"></a>

#### Resource labeling for preservation

If you want to retain essential cluster configuration data after reinstallation, the SiteConfig operator provides a backup and restore mechanism for hub-side `Secret` and `ConfigMap` resources within the `ClusterInstance` namespace.

You can control data preservation by setting the `preservationMode` in the `ClusterInstance` resource and adding the appropriate preservation label to your resources. The following preservation modes are available:

| Preservation mode | Behavior | Usage | Label requirement |
|----|----|----|----|
| `None` | `ConfigMap` or `Secret` resources are not preserved. | Select the `None` mode if data preservation is unnecessary for the cluster during reinstallation. | None |
| `All` | All labeled `ConfigMap` and `Secret` resources in the same namespace as the `ClusterInstance` resource are backed up. If the SiteConfig operator does not find any labeled resources, the operator proceeds with the reinstallation without data preservation. The original resources are stored as immutable Kubernetes secrets. | Select the `All` mode if you want to preserve labeled resources, if any. | Add the `siteconfig.open-cluster-management.io/preserve: "<arbitrary-value>"` label with any value, for example, `siteconfig.open-cluster-management.io/preserve: ""`. The label indicates to the operator to back up resources with the specified label only when the preservation mode is set to `All`. |
| `ClusterIdentity` | Only `ConfigMap` and `Secret` resources that are labeled with the `siteconfig.open-cluster-management.io/preserve: "cluster-identity"` label in the same namespace as the `ClusterInstance` CR are backed up. If the SiteConfig operator does not find any labeled resources, the operator stops the reinstallation process and displays an error message. The original CRs of these resources are stored as immutable Kubernetes secrets. | Select the `ClusterIdentity` mode if you want the operator to verify that you labeled at least one resource. | Add the `siteconfig.open-cluster-management.io/preserve: "cluster-identity"` label to indicate to the operator to back up resources with the label when the preservation mode is set to `All` or `ClusterIdentity`. If the preservation mode is set to `ClusterIdentity` and the operator does not find at least one resource with the `siteconfig.open-cluster-management.io/preserve: "cluster-identity"` label, the reinstallation stops. |

Preservation modes

You can label your resources well before initiating the reinstallation.

<a id="reinstallation-monitoring"></a>

#### Cluster reinstallation monitoring

The reinstallation has two phases:

Phase 1 - Reinstallation request handling  
- Request validation: The SiteConfig operator validates the request.

- Data preservation: The SiteConfig operator backs up labeled resources.

- Cleanup: The SiteConfig operator removes existing installation manifests. If this step times out, the reinstallation stops and the `ClusterInstance` resource is paused.

- Data restoration: The SiteConfig operator restores preserved data.

Phase 2 - Cluster provisioning  
- Manifest regeneration: The SiteConfig operator generates new manifests from templates.

- Cluster installation: The cluster is provisioned using the new manifests.

You can track progress in the `status.reinstall.conditions` and `status.conditions` fields for phase 1 and 2, respectively. To track the cluster reinstallation progress, the SiteConfig operator provides the following status conditions:

<table>
<caption>Reinstallation status conditions</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><p>Condition</p></td>
<td style="text-align: left;"><p>Description</p></td>
<td style="text-align: left;"><p>Reasons</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ReinstallRequestProcessed</code></p></td>
<td style="text-align: left;"><p>Indicates the overall status of the reinstallation request.</p></td>
<td style="text-align: left;"><p><code>InProgress</code>: The reinstallation process is ongoing.<br />
<code>Completed</code>: The reinstallation process successfully completed, and the cluster is ready for reprovisioning.<br />
<code>Failed</code>: The reinstallation process encountered an error and failed.<br />
<code>TimedOut</code>: The reinstallation process exceeded the expected time limit and did not complete successfully.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ReinstallRequestValidated</code></p></td>
<td style="text-align: left;"><p>Confirms the validity of the reinstallation request.</p></td>
<td style="text-align: left;"><p><code>Completed</code>: The reinstallation request is valid.<br />
<code>Failed</code>: The reinstallation request is invalid.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ReinstallPreservationDataBackedUp</code></p></td>
<td style="text-align: left;"><p>Tracks the backup status of preserved data.</p></td>
<td style="text-align: left;"><p><code>PreservationNotRequired</code>: No backup required as <code>spec.reinstall.preservationMode: None</code> is set.<br />
<code>DataUnavailable</code>: No <code>Secret</code> or <code>ConfigMap</code> objects with the preservation label are found in the <code>ClusterInstance</code> namespace.<br />
<code>Completed</code>: <code>Secret</code> and <code>ConfigMap</code> objects are successfully backed up.<br />
<code>Failed</code>: One or more <code>Secret</code> and <code>ConfigMap</code> objects are not backed up.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ReinstallClusterIdentityDataDetected</code></p></td>
<td style="text-align: left;"><p>Determines whether cluster identity data is available for preservation.</p></td>
<td style="text-align: left;"><p><code>PreservationNotRequired</code>: Data preservation is not required. The <code>preservationMode</code> field is set to <code>None</code>.<br />
<code>DataAvailable</code>: Cluster identity <code>Secret</code> and <code>ConfigMap</code> objects are successfully located.<br />
<code>DataUnavailable</code>: No cluster identity <code>Secret</code> or <code>ConfigMap</code> objects are detected.<br />
<code>Failed</code>: The preservation mode is set to <code>ClusterIdentity</code> but no cluster identity data is found.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ReinstallRenderedManifestsDeleted</code></p></td>
<td style="text-align: left;"><p>Monitors the deletion of rendered manifests associated with the <code>ClusterInstance</code> resource.</p></td>
<td style="text-align: left;"><p><code>InProgress</code>: Deleting rendered manifests is in progress.<br />
<code>Completed</code>: Successfully deleted all rendered manifests.<br />
<code>Failed</code>: Failed to delete one or more rendered manifests.<br />
<code>TimedOut</code>: Timed out while waiting for rendered manifests to be deleted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ReinstallPreservationDataRestored</code></p></td>
<td style="text-align: left;"><p>Tracks the restoration status of preserved data.</p></td>
<td style="text-align: left;"><p><code>PreservationNotRequired</code>: Preservation is not required because the <code>preservationMode</code> field is set to <code>None</code>.<br />
<code>DataUnavailable</code>: No preserved <code>Secret</code> or <code>ConfigMap</code> objects detected for restoration.<br />
<code>Completed</code>: <code>Secret</code> and <code>ConfigMap</code> objects are successfully restored.<br />
<code>Failed</code>: Failed to restore one or more <code>Secret</code> and <code>ConfigMap</code> objects.</p></td>
</tr>
</tbody>
</table>

The `status.reinstall` field provides further information about the reinstallation process with the following fields:

- `InProgressGeneration`: Identifies the active generation being processed for reinstallation.

- `ObservedGeneration`: Indicates the last successfully processed reinstallation request.

- `RequestStartTime`: Indicates the time when the reinstallation request was initiated.

- `RequestEndTime`: Indicates the time when the reinstallation process was completed.

- `History`: Displays past reinstallation attempts, including generation details, timestamps, and specification changes to the `ClusterInstance` resource.

<a id="reinstall-cluster"></a>

### Reinstallation of a cluster with the SiteConfig operator (Technology Preview)

Reinstallation of a cluster with the SiteConfig operator requires that you enable the process and define a preservation mode.

Reinstall your clusters by using the SiteConfig operator. After enabling the reinstallation, you can define your desired preservation mode and if applicable, label your resources.

**Required access:** Cluster administrator

<div>

<div class="title">

Additional resources

</div>

- [Enable cluster reinstallation](mce_acm_integration.md#enable-cluster-reinstallation)

- [Label resources for preservation](mce_acm_integration.md#label-preservation-resources)

- [Initiate a cluster reinstallation](mce_acm_integration.md#initiate-cluster-reinstallation)

- [Monitor the cluster reinstallation](mce_acm_integration.md#monitor-cluster-reinstallation)

</div>

<a id="enable-cluster-reinstallation"></a>

#### Enable cluster reinstallation

Enable cluster reinstallation in the `siteconfig-operator-configuration` `ConfigMap` resource. You must explicitly enable cluster reinstallation in the `siteconfig-operator-configuration` `ConfigMap` resource, which you can complete well before initiating the process. By default, reinstallation is disabled.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Set the `NAMESPACE` environment variable to match the namespace where the SiteConfig operator is installed. Run the following command:

    ``` bash
    NAMESPACE=<namespace>
    ```

2.  Verify the current configuration by running the following command:

    ``` bash
    oc get configmap siteconfig-operator-configuration -n $NAMESPACE -o yaml
    ```

    **Example output:**

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
        name: siteconfig-operator-configuration
        namespace: <namespace>
    data:
        allowReinstalls: false
        ...
    ```

    - The namespace where the SiteConfig operator is installed.

    - Set `allowReinstalls` to `true` to enable reinstallation.

    **Note:** The operator continuously monitors the `siteconfig-operator-configuration` `ConfigMap` resource for changes.

3.  To enable cluster reinstallation, update the `ConfigMap` resource by setting the `data.allowReinstalls` field to `true`. Run the following command:

    ``` bash
    oc patch configmap siteconfig-operator-configuration \
        -n $NAMESPACE \
        --type=json \
        -p '[{"op": "replace", "path": "/data/allowReinstalls", "value": "true"}]'
    ```

4.  Verify the update by running the following command:

    ``` bash
    oc get configmap siteconfig-operator-configuration -n $NAMESPACE -o yaml
    ```

</div>

<a id="label-preservation-resources"></a>

#### Label resources for preservation

Label resources and set the preservation mode in your `ClusterInstance` custom resource. You can set the desired preservation mode in your `ClusterInstance` custom resource and if applicable, label your resources accordingly. By default, the `preservationMode` field is set to `None`. See *Resource labeling for preservation*.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Label a resource for the `All` preservation mode by running the following command:

  ``` bash
  oc label configmap <your_configmap> "siteconfig.open-cluster-management.io/preserve=all"
  ```

</div>

The `ClusterInstance` custom resource is updated with the correct `preservationMode` corresponding to the applied labels.

<div>

<div class="title">

Additional resources

</div>

- [Resource labeling for preservation](mce_acm_integration.md#resource-preservation-labels)

</div>

<a id="initiate-cluster-reinstallation"></a>

#### Initiate a cluster reinstallation

Initiate a cluster reinstallation by updating the `ClusterInstance` resource with a new `spec.reinstall.generation` value. To start the reinstallation, update the `ClusterInstance` resource with a new `spec.reinstall.generation` value.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Modify the `spec.reinstall.generation` value in the `ClusterInstance` resource:

    ``` yaml
    apiVersion: siteconfig.open-cluster-management.io/v1alpha1
    kind: ClusterInstance
    metadata:
      name: clusterinstance-example
      namespace: some-namespace
    spec:
      reinstall:
        generation: "unique-generation-string"
        preservationMode: "<your-preservation-mode>"
    ```

    **Note:** Ensure you set the appropriate preservation mode when you modify the `ClusterInstance` resource. `"None"`, `"All"`, or `"ClusterIdentity"` are valid values.

2.  **Optional:** When defining the `spec.reinstall` object, you can modify the following additional fields in the `ClusterInstance` resource:

    - `spec.extraAnnotations`

    - `spec.extraLabels`

    - `spec.suppressedManifests`

    - `spec.pruneManifests`

    - `spec.nodes.<node-id>.extraAnnotations`

    - `spec.nodes.<node-id>.extraLabels`

    - `spec.nodes.<node-id>.suppressedManifests`

    - `spec.nodes.<node-id>.pruneManifests`

    - `spec.nodes.<node-id>.bmcAddress`

    - `spec.nodes.<node-id>.bootMACAddress`

    - `spec.nodes.<node-id>.nodeNetwork.interfaces.macAddress`

    - `spec.nodes.<node-id>.rootDeviceHints`

    **Note:** `<node-id>` represents the updated `NodeSpec` object.

3.  Apply the changes. If you are using OpenShift GitOps ZTP, push to your Git repository and wait for Argo CD to synchronize the changes. To manually apply your changes, run the following command on the hub cluster:

    ``` bash
    oc apply -f clusterinstance-example.yaml
    ```

</div>

<a id="monitor-cluster-reinstallation"></a>

#### Monitor the cluster reinstallation

Monitor the cluster reinstallation progress. You can monitor the cluster reinstallation progress. Complete the following steps.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Verify that the reinstallation request is being processed. Run the following command:

    ``` bash
    oc get clusterinstance clusterinstance-example -n some-namespace -o json | jq -r '.status.reinstall.conditions[] | select(.type=="ReinstallRequestProcessed")'
    ```

    See the following example output:

    ``` json
    {
    "type": "ReinstallRequestProcessed"
    "reason": "InProgress",
    "status": "False",
    ...
    }
    ```

2.  Verify that the cluster reinstallation request is validated successfully. Run the following command:

    ``` bash
    oc get clusterinstance clusterinstance-example -n some-namespace -o json | jq -r '.status.reinstall.conditions[] | select(.type=="ReinstallRequestValidated")'
    ```

    See the following example output:

    ``` json
    {
    "type": "ReinstallRequestValidated"
    "reason": "Completed",
    "status": "True",
    ...
    }
    ```

3.  Optional. If you set the `spec.reinstall.preservationMode` field to `All` or `ClusterIdentity`, verify that the cluster identity data is preserved. Run the following command:

    ``` bash
    oc get clusterinstance clusterinstance-example -n some-namespace -o json | jq -r '.status.reinstall.conditions[] | select(.type=="ReinstallPreservationDataBackedup")'
    ```

    See the following example output:

    ``` json
    {
    "type": "ReinstallPreservationDataBackedup"
    "reason": "Completed",
    "status": "True",
    ...
    }
    ```

4.  **Optional:** If you set the `spec.reinstall.preservationMode` field to `All` or `ClusterIdentity`, you can verify that the cluster identity data is detected. Run the following command:

    ``` bash
    oc get clusterinstance clusterinstance-example -n some-namespace -o json | jq -r '.status.reinstall.conditions[] | select(.type=="ReinstallClusterIdentityDataDetected")'
    ```

    See the following example output:

    ``` json
    {
    "type": "ReinstallClusterIdentityDataDetected"
    "reason": "DataAvailable",
    "status": "True",
    ...
    }
    ```

5.  Verify that the installation manifests are deleted. The deletion can take several minutes to complete. Run the following command:

    ``` bash
    oc get clusterinstance clusterinstance-example -n some-namespace -o json | jq -r '.status.reinstall.conditions[] | select(.type=="ReinstallRenderedManifestsDeleted")'
    ```

    See the following example output:

    ``` json
    {
    "type": "ReinstallRenderedManifestsDeleted"
    "reason": "Completed",
    "status": "True",
    ...
    }
    ```

6.  **Optional:** If you set the `preseservationMode` field to `All` or `ClusterIdentity`, you can verify that the data preserved earlier are restored. Run the following command:

    ``` bash
    oc get clusterinstance clusterinstance-example -n some-namespace -o json | jq -r '.status.reinstall.conditions[] | select(.type=="ReinstallPreservationDataRestored")'
    ```

    See the following example output:

    ``` json
    {
    "type": "ReinstallPreservationDataRestored"
    "reason": "Completed",
    "status": "True",
    ...
    }
    ```

7.  Ensure that the reinstallation request completed successfully. Run the following command:

    ``` bash
    oc get clusterinstance clusterinstance-example -n some-namespace -o json | jq -r '.status.reinstall.conditions[] | select(.type=="ReinstallRequestProcessed")'
    ```

    See the following example output:

    ``` json
    {
    "type": "ReinstallRequestProcessed"
    "reason": "Completed",
    "status": "True",
    ...
    }
    ```

8.  Confirm that the cluster is successfully reinstalled and is operational by running an `oc` command with the `kubeconfig` file that is associated with the reinstalled cluster.

</div>

<a id="ibbf-hardware-replacement"></a>

### Hardware replacement with Image-Based Break/Fix for single-node OpenShift (Technology Preview)

The Image-Based Break/Fix feature utilizes the cluster reinstallation mechanism of the SiteConfig operator to simplify single-node OpenShift hardware replacement. The feature minimizes downtime by preserving the original identity of the cluster. The Image-Based Break/Fix feature retains critical cluster details, including identifiers, cryptographic keys, such as `kubeconfig`, and authentication credentials, which enables the replacement node to seamlessly assume the identity of the failed hardware.

Designed for identical hardware replacements in single-node OpenShift clusters installed using the Image Based Install method, Image-Based Break/Fix introduces a GitOps-compatible, declarative API. Users can initiate hardware replacement with a single Git commit. Powered by the SiteConfig operator and Image Based Install Operator, Image-Based Break/Fix enables cluster redeployment using the existing `ClusterInstance` custom resource.

With Image-Based Break/Fix, OpenShift Container Platform users gain a resilient, automated, and GitOps-native solution for quickly restoring single-node OpenShift clusters after hardware failures.

The Image-Based Break/Fix workflow is similar to the cluster reinstallation workflow with certain differences. To familiarize yourself with the differences in the workflows, see the high-level overview of the Image-Based Break/Fix cluster reinstallation workflow:

- The SiteConfig operator reinstallation service is enabled.

- A cluster reinstallation is initiated.

- The `spec.reinstall.preservationMode` is set to `"ClusterIdentity"`.

- The `spec.nodes` object is updated with the changed hardware information.

- **Note**: The Image Based Install Operator automatically labels cluster identity resources.

- The reinstallation progress is monitored.

- During cluster provisioning, the operators consuming the installation manifests provision the cluster using the newly generated manifests.

- **Note**: The Image Based Install Operator detects the preserved cluster identity data and incorporates it into the configuration ISO image.

- The cluster is verified as provisioned and available.

- The `kubeconfig` that is associated with the failed hardware is used to access the reinstalled spoke cluster. See *Cluster reinstallation with the SiteConfig operator (Technology Preview)*.

<div>

<div class="title">

Additional resources

</div>

- [Cluster reinstallation with the SiteConfig operator (Technology Preview)](mce_acm_integration.md#cluster-reinstallation)

- [Initiate the Image-Based Break/Fix cluster reinstallation](mce_acm_integration.md#initiate-ibbf-reinstallation)

</div>

<a id="initiate-ibbf-reinstallation"></a>

#### Initiate the Image-Based Break/Fix cluster reinstallation

Initiate the Image-Based Break/Fix cluster reinstallation by updating the `ClusterInstance` resource. To initiate the Image-Based Break/Fix cluster reinstallation, update the `ClusterInstance` resource by setting the `spec.reinstall.generation` field and updating the `spec.nodes` object with the changed hardware information.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- The cluster is a single-node OpenShift cluster installed using the Image Based Install provisioning method.

- The faulty hardware is replaced with a new node with identical specifications.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Modify the `spec.reinstall.generation` field and update the `spec.nodes` object in the `ClusterInstance` resource with the new node details:

    ``` yaml
    apiVersion: siteconfig.open-cluster-management.io/v1alpha1
    kind: `ClusterInstance`
    metadata:
      name: clusterinstance-example
      namespace: some-namespace
    spec:
      ...
      reinstall:
        generation: "unique-generation-string"
        preservationMode: "ClusterIdentity"
      nodes:
        - bmcAddress: <new-node-bmcAddress>
          bootMACAddress: <new-node-bootMACAddress>
          rootDeviceHints: <new-node-rootDeviceHints>
          nodeNetwork:
            interfaces:
              macAddress: <new-node-macAddress>
              ...
          ...
    ```

2.  Apply the changes. If you are using OpenShift GitOps ZTP, push to your Git repository and wait for Argo CD to synchronize the changes. To manually apply your changes, run the following command on the hub cluster:

    ``` bash
    oc apply -f clusterinstance-example.yaml
    ```

</div>
