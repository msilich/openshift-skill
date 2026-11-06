> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/search/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="acm-search"></a>

# Search

Search returns and lists each cluster with the resource that you search. For resources in the *hub* cluster, the cluster name is displayed as *local-cluster*.

You can change the `local-cluster` name if the `enabled` field is set to `false`. You must use 34 or fewer characters for the `<your-local-cluster-name>` value. The `local-cluster` cannot be renamed if it is set as `enabled: true`.

**Note:** If you change the default name of your `local-cluster` to another value, the results appear within the changed local cluster name.

Your search results are grouped by `kind`, and each resource `kind` is grouped in a table. Search options depend on your cluster objects. Refine your results with specific labels.

Learn about the Red Hat Advanced Cluster Management Search service. Use Search to query resource data from your clusters. See the following documentation:

- [Search service](search.md#search-service)

- [Creating search configurable collection](search.md#create-search-collection)

- [Customizing the Search service](search.md#customize-search-console)

- [Customizing the console for Search](search.md#customize-search-console)

- [Querying in the console](search.md#query-console)

- [Updating klusterlet-addon-search deployments](search.md#update-klusterlet-search)

- [Search API](search.md#search-api)

<a id="search-service"></a>

## Search service

For Red Hat Advanced Cluster Management for Kubernetes, search provides visibility into your Kubernetes resources across all of your clusters. Search also indexes the Kubernetes resources and the relationships to other resources.

Search is configured by default on the hub cluster. When you provision or manually import a managed cluster, the `klusterlet-addon-search` is enabled.

The search architecture is composed of the following components:

<table>
<caption>Search component table</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Component name</th>
<th style="text-align: left;">Metrics</th>
<th style="text-align: left;">Metric type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>search-collector</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Watches the Kubernetes resources, collects the resource metadata, computes relationships for resources across all of your managed clusters, and sends the collected data to the <code>search-indexer</code>. The <code>search-collector</code> on your managed cluster runs as a pod named, <code>klusterlet-addon-search</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>search-indexer</code></p>
<p>Receives resource metadata from the collectors and writes to PostgreSQL database. The <code>search-indexer</code> also watches resources in the hub cluster to keep track of active managed clusters.</p></td>
<td style="text-align: left;"><p><code>search_indexer_request_duration</code></p></td>
<td style="text-align: left;"><p>Histogram</p></td>
<td style="text-align: left;"><p>Time (seconds) the search indexer takes to process a request (from managed cluster).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>search_indexer_request_size</code></p></td>
<td style="text-align: left;"><p>Histogram</p></td>
<td style="text-align: left;"><p>Total changes (add, update, delete) in the search indexer request (from managed cluster).</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>search_indexer_request_count</code></p></td>
<td style="text-align: left;"><p>Counter</p></td>
<td style="text-align: left;"><p>Total requests received by the search indexer (from managed clusters).</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>search_indexer_requests_in_flight</code></p></td>
<td style="text-align: left;"><p>Gauge</p></td>
<td style="text-align: left;"><p>Total requests the search indexer is processing at a given time.</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>search-api</code></p>
<p>Provides access to all cluster data in the <code>search-indexer</code> through GraphQL and enforces role-based access control (RBAC).</p></td>
<td style="text-align: left;"><p><code>search_api_requests</code></p></td>
<td style="text-align: left;"><p>Histogram</p></td>
<td style="text-align: left;"><p>Histogram of HTTP requests duration in seconds.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>search_dbquery_duration_seconds</code></p></td>
<td style="text-align: left;"><p>Histogram</p></td>
<td style="text-align: left;"><p>Latency of database requests in seconds.</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>search_api_db_connection_failed_total</code></p></td>
<td style="text-align: left;"><p>Counter</p></td>
<td style="text-align: left;"><p>The total number of database connection attempts that failed.</p></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>search-postgres</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Stores collected data from all managed clusters in an instance of the PostgreSQL database. The database contains no historical data. When the database restarts, the data is overridden. If you recreate the database, consider the time it takes to rebuild the cache.</p></td>
</tr>
</tbody>
</table>

Specify your search query by using search operations as conditions. Characters such as `>, >=, <, <=, !=` are supported. See the following search operation table:

| Default operation | Data type | Description |
|----|----|----|
| `=` | string, number | This is the default operation. |
| `!` or `!=` | string, number | This represents the *NOT* operation, which means to exclude from the search results. |
| `<, ⇐, >, >=` | number |  |
| `>` | date | Dates matching the last hour, day, week, month, and year. |
| `*` | string | Partial string match. |

Search operation and data types table

<div>

<div class="title">

Additional resources

</div>

- For more topics about the Red Hat Advanced Cluster Management for Kubernetes console, see [Web console](console.md#web-console).

- If you want to disable the search service on your managed cluster, see [Modify the klusterlet add-ons settings of your cluster](add-ons.md#modify-klusterlet-add-ons) for more information.

</div>

<a id="create-search-collection"></a>

## Creating search configurable collection

Define which Kubernetes resources are collected from the cluster by creating a `search-collector-config` config map for each managed cluster where you want to customize the resources that search collects. **Important:** Be sure to place the config map in the same namespace where the search add-on is deployed. The default namespace is `open-cluster-management-agent-addon`.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to create the `search-collector-config` config map:

    ``` bash
    oc apply -f <your-search-collector-config>.yaml
    ```

2.  List the resources in the `data.AllowedResources` and the `data.DeniedResources` fields within the config map.

3.  Collect services and pods from all `apiGroups`, while also collecting all resources from the `admission.k8s.io` and `authentication.k8s.io` `apiGroups`.

4.  Configure your config map to prevent the central collection of secrets from all `apiGroups`, while preventing the collection of `policies`, `iampolicies`, and `certificatepolicies` from the `admission.k8s.io` `apiGroup`.

    Your config map might resemble the following YAML file:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
     name: search-collector-config
     namespace: <namespace where search-collector add-on is deployed>
    data:
     AllowedResources: |-
       - apiGroups:
           - "*"
         resources:
           - services
           - pods
       - apiGroups:
           - admission.k8s.io
           - authentication.k8s.io
         resources:
           - "*"
     DeniedResources: |-
       - apiGroups:
           - "*"
         resources:
           - secrets
       - apiGroups:
           - admission.k8s.io
         resources:
           - policies
           - iampolicies
           - certificatepolicies
    ```

    **Note:** If you do not provide a config map, all resources are collected by default. When you specify `AllowedResources`, all other resources are automatically excluded. If you list resources in both the `AllowedResources` and `DeniedResources`, resources are excluded from the collection.

5.  Add the `backup` label to include the `search-collector-config` config map to the cluster backups. Run the following command:

    ``` bash
    oc label configmap search-collector-config -n <namespace-for-search-collector> cluster.open-cluster-management.io/backup=""
    ```

</div>

<a id="customize-search-service"></a>

## Customizing the search service

Customize the search service to set up persistent storage, to fine-tune for performance and scalability, or to modify certain behaviors through environment variables. Access the search configuration options from the search operator, which watches the `search-v2-operator` custom resource, reconciles the changes, and updates active pods.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You must have access to the `open-cluster-management` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Modify the default values in the `search-v2-operator` custom resource.

    1.  To view details of the custom resource, run the following command:

        ``` bash
        oc get search search-v2-operator -n <acm-namespace> -o yaml
        ```

    2.  Configure a persistent volume claim for clusters that are in production. If the empty directory size is limited, store the PostgreSQL data on a persistent volume claim to improve search performance.

        **Notes:**

        - During installation, the default configuration for the Red Hat Advanced Cluster Management PostgreSQL database uses an `emptyDir` volume for data storage.

        - If a persistent volume claim is missing, the `SearchPVCNotPresent` alert is visible in the **Status** pane.

        - If a persistent volume claim for search is missing and critical conditions exist, you receive the `SearchPVCNotPresentCritical` Prometheus alert.

    3.  To persist your search data, select a storage class from your Red Hat Advanced Cluster Management hub cluster.

    4.  For example, create a persistent volume claim if you select the `gp2` storageclass and mount the claim to the `search-postgres` pod. Your configuration might resemble the following example:

    ``` yaml
    apiVersion: search.open-cluster-management.io/v1alpha1
    kind: Search
    metadata:
      name: search-v2-operator
      namespace: open-cluster-management
      labels:
        cluster.open-cluster-management.io/backup: ""
    spec:
      dbStorage:
        size: 10Gi
        storageClassName: gp2
    ```

    1.  Modify the storage size if you need to. By default, the storage size is `10Gi`. For example, `20Gi` might be sufficient for about 200 managed clusters.

2.  Optimize cost by tuning the pod memory or CPU requirements, replica count, and update log levels for any of the four search pods: `indexer`, `database`, `queryapi`, or `collector`.

    1.  Update the `deployment` section of the `search-v2-operator` custom resource. There are four deployments managed by the `search-v2-operator`, which you can update individually.

    2.  Apply resources for the `indexer`, `database`, `queryapi`, or `collector` pod.

    3.  Add multiple environment variables in the `envVar` section to specify a value for each variable that you name.

    4.  Specify a value for each variable that you name by adding multiple environment variables in the `envVar` specification.

    5.  Add the `- -v=3` argument for the `queryapi` specification to control the log level verbosity for any of the four pods. Your `search-v2-operator` custom resource might resemble the following file:

    ``` yaml
    apiVersion: search.open-cluster-management.io/v1alpha1
    kind: Search
    metadata:
      name: search-v2-operator
      namespace: open-cluster-management
    spec:
      deployments:
        collector:
          resources:
            limits:
              cpu: 500m
              memory: 128Mi
            requests:
              cpu: 250m
              memory: 64Mi
        indexer:
          replicaCount: 3
        database:
            envVar:
              - name: POSTGRESQL_EFFECTIVE_CACHE_SIZE
                value: 1024MB
              - name: POSTGRESQL_SHARED_BUFFERS
                value: 512MB
              - name: WORK_MEM
                value: 128MB
        queryapi:
          arguments:
          - -v=3
    ```

3.  Apply memory resources for the `indexer` pod. See the following example:

    ``` yaml
        indexer:
          resources:
            limits:
              memory: 5Gi
            requests:
              memory: 1Gi
    ```

4.  Define the node placement for search pods.

    1.  Update the `Placement` resource of search pods by using the `nodeSelector` parameter, or the `tolerations` parameter. View the following example configuration:

    ``` yaml
    spec:
     dbStorage:
      size: 10Gi
     deployments:
      collector: {}
      database: {}
      indexer: {}
      queryapi: {}
     nodeSelector:
      node-role.kubernetes.io/infra: ""
     tolerations:
     - effect: NoSchedule
      key: node-role.kubernetes.io/infra
      operator: Exists
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring persistent storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/monitoring/configuring-core-platform-monitoring#configuring-persistent-storage_storing-and-recording-data) in the OpenShift Container Platform documentation

</div>

<a id="customize-search-console"></a>

## Customizing the console for Search

Customize your console for Search to specify how you want data and search results to be displayed.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You must have access to the `open-cluster-management` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Customize the search result limit from the OpenShift Container Platform console.

    1.  Update the `console-mce-config` in the `multicluster-engine` namespace. These settings apply to all users and might affect performance. View the following performance parameter descriptions:

        - `SAVED_SEARCH_LIMIT` - The maximum amount of saved searches for each user. By default, there is a limit of ten saved searches for each user. The default value is `10`. To update the limit, add the following key value to the `console-config` config map: `SAVED_SEARCH_LIMIT: x`.

        - `SEARCH_RESULT_LIMIT` - The maximum amount of search results displayed in the console. Default value is `1000`. To remove this limit set to `-1`.

        - `SEARCH_AUTOCOMPLETE_LIMIT` - The maximum number of suggestions retrieved for the search bar typeahead. Default value is `10,000`. To remove this limit set to `-1`.

    2.  Change the search result to `100` items by running the following `patch` command from the OpenShift Container Platform console:

    ``` bash
    oc patch configmap console-mce-config -n multicluster-engine --type merge -p '{"data":{"SEARCH_RESULT_LIMIT":"100"}}'
    ```

2.  To add, edit, or remove suggested searches, create a config map named `console-search-config` and configure the `suggestedSearches` section. Suggested searches that are listed are also displayed from the console. It is required to have an `id, name, and searchText` for each search object.

    1.  Add the namespace where search is enabled. View the following config map example:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: console-search-config
      namespace: <acm-namespace>
    data:
      suggestedSearches: |-
        [
          {
            "id": "search.suggested.workloads.name",
            "name": "Workloads",
            "description": "Show workloads running on your fleet",
            "searchText": "kind:DaemonSet,Deployment,Job,StatefulSet,ReplicaSet"
          },
          {
            "id": "search.suggested.unhealthy.name",
            "name": "Unhealthy pods",
            "description": "Show pods with unhealthy status",
            "searchText": "kind:Pod status:Pending,Error,Failed,Terminating,ImagePullBackOff,CrashLoopBackOff,RunContainerError,ContainerCreating"
          },
          {
            "id": "search.suggested.createdLastHour.name",
            "name": "Created last hour",
            "description": "Show resources created within the last hour",
            "searchText": "created:hour"
          },
          {
            "id": "search.suggested.virtualmachines.name",
            "name": "Virtual Machines",
            "description": "Show virtual machine resources",
            "searchText": "kind:VirtualMachine"
          }
        ]
    ```

</div>

<a id="query-console"></a>

## Querying in the console

You can type any text value in the *Search box* and results include anything with that value from any property, such as a name or namespace. Queries that contain an empty space are not supported.

As you search for resources, you receive other resources that are related to your original search result, which help you visualize how the resources interact with other resources in the system.

For more specific search results, include the property selector in your search. You can combine related values for the property for a more precise scope of your search. For example, search for `cluster:dev red` to receive results that match the string "red" in the `dev` cluster.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Click **Search** in the navigation menu.

2.  Type a word in the *Search box*, then Search finds your resources that contain that value.

    **Note:** Search is case-sensitive when you query labels.

3.  See the following examples that you can select for filtering: `name`, `namespace`, `status`, and other resource fields. Auto-complete provides suggestions to refine your search. See the following example:

    - Search for a single field, such as `kind:pod` to find all pod resources.

    - Search for multiple fields, such as `kind:pod namespace:default` to find the pods in the default namespace.

      **Notes:**

    - When you search for more than one property selector with multiple values, the search returns either of the values that were queried. View the following examples:

    - When you search for `kind:Pod name:a`, any pod named `a` is returned.

    - When you search for `kind:Pod name:a,b`, any pod named `a` or `b` are returned.

    - Search for `kind:pod status:!Running` to find all pod resources where the status is not `Running`.

    - Search for `kind:pod restarts:>1` to find all pods that restarted at least twice.

4.  Specify your search query by selecting the **Advanced search** drop-down button to filter the *Column*, *Operator*, and *Value* options or add a search constraint.

5.  If you want to save your search, click the **Save search** icon.

6.  To download your search results, select the **Export as CSV** button.

</div>

<a id="update-klusterlet-search"></a>

## Updating klusterlet-addon-search deployments

To collect the Kubernetes objects from the managed clusters, the `klusterlet-addon-search` pod is run on all the managed clusters where search is enabled. This deployment is run in the `open-cluster-management-agent-addon` namespace. A managed cluster with a high number of resources might require more memory for the `klusterlet-addon-search` deployment to function.

Resource requirements for the `klusterlet-addon-search` pod in a managed cluster can be specified in the `ManagedClusterAddon` custom resource in your Red Hat Advanced Cluster Management hub cluster. There is a namespace for each managed cluster with the managed cluster name.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

1.  Edit the `ManagedClusterAddon` custom resource from the namespace matching the managed cluster name. Run the following command to update the resource requirement in `xyz` managed cluster:

    ``` bash
    oc edit managedclusteraddon search-collector -n xyz
    ```

2.  Append the resource requirements as annotations. When you define both `annotations` and `resourceRequirements`, the `annotations` value overrides the `resourceRequirements` value. View the following example:

    ``` yaml
    apiVersion: addon.open-cluster-management.io/v1alpha1
    kind: ManagedClusterAddOn
    metadata:
      annotations: addon.open-cluster-management.io/search_memory_limit: 2048Mi
      addon.open-cluster-management.io/search_memory_request: 512Mi
    ```

    **Notes:**

    - The annotation overrides the resource requirements on the managed clusters and automatically restarts the pod with new resource requirements.

    - You can discover all resources defined in your managed cluster by using the API Explorer in the console. Alternatively, you can discover all resources by running the following command:

    ``` bash
    oc api-resources
    ```

3.  Create an `AddonDeploymentConfig` resource and update the limit in the `resourceRequirements` field for the `klusterlet-addon-search` deployment . Your `AddonDeploymentConfig` resource might resemble the following example:

    ``` yaml
    apiVersion: addon.open-cluster-management.io/v1alpha1
    kind: AddOnDeploymentConfig
    metadata:
      name: search-addon-resources
      namespace: your-managed-ns
    spec:
      resourceRequirements:
      - containerID: deployments:klusterlet-addon-search:collector
        resources:
          limits:
            memory: 1024Mi
          requests:
            memory: 512Mi
    ```

4.  Add the `backup` label to include the `AddOnDeploymentConfig` resource to the cluster backups. Run the following command:

    ``` bash
    oc label addondeploymentconfig search-addon-resources -n <namespace-for-search-addon-resources> cluster.open-cluster-management.io/backup=""
    ```

5.  Apply the `search-addon-resources` `AddOnDeploymentConfig` file to your klusterlet add-on by running the following command:

    ``` bash
    oc apply -f search-addon-resources.yaml
    ```

6.  Update the `klusterlet-addon-search` deployment to use the new `AddonDeploymentConfig` resource. Run the following command:

    ``` bash
    oc patch managedclusteraddon search-collector -n your-test-managed --type merge -p '{"spec": { "configs": [{"group": "addon.open-cluster-management.io","resource": "addondeploymentconfigs","name": "search-addon-resources","namespace": "your-test-managed"}]}}'
    ```

</div>

<a id="search-api"></a>

## Search API

Use the Search API to query resources that match filters or keywords, and to view resource changes across your managed clusters. Access the GraphQL endpoint and enable the schema documentation.

- Configure API access

  Create a route to access the Search API externally with the following command:

  ``` bash
  oc create route passthrough search-api --service=search-search-api -n open-cluster-management
  ```

  **Important:** You must configure your route to secure your environment.

- Enable API documentation

  Before you can access the Search API documentation, you must update the `search-v2-operator` resource to enable the `API_DOCUMENTATION` environment variable on the `search-api` deployment. To edit the resource, run the following command:

  ``` bash
  oc patch search -n open-cluster-management search-v2-operator --type json -p '[{"op": "add", "path": "/spec/deployments/queryapi/envVar", "value": [{"name": "API_DOCUMENTATION", "value": "true"}]}]'
  ```

- Search for deployments

  - Use the following query:

    ``` graphql
    query mySearch($input: [SearchInput]) {
        search(input: $input) {
                items
            }
    }
    ```

  - Use the following variables:

    ``` graphql
    {"input":[
        {
            "keywords": [],
            "filters": [
              {
                "property": "kind",
                "values": [
                  "Deployment"
                ]
              }
            ],
            "limit": 10,
            "offset": 5,
            "orderBy": "name asc"
        }
    ]}
    ```

- Sample output of search for deployments

  ``` json
  {
    "data": {
      "search": [
        {
          "count": 132,
          "items": [
            {
              "_hubClusterResource": "true",
              "_uid": "local-cluster/01778e22-5ccb-4f30-bff2-3c7725f046f5",
              "apigroup": "apps",
              "apiversion": "v1",
              "available": "1",
              "cluster": "local-cluster",
              "created": "2026-08-07T01:30:33Z",
              "current": "1",
              "desired": "1",
              "kind": "Deployment",
              "kind_plural": "deployments",
              "label": "app=cluster-manager-registration-webhook; open-cluster-management.io/created-by-clustermanager=cluster-manager",
              "name": "cluster-manager-registration-webhook",
              "namespace": "open-cluster-management-hub",
              "ready": "1"
            },
            {
              "_hubClusterResource": "true",
              "_uid": "local-cluster/0197d717-3c67-456e-9dbe-e233f1cb05c3",
              "apigroup": "apps",
              "apiversion": "v1",
              "available": "1",
              "cluster": "local-cluster",
              "created": "2026-08-07T01:29:30Z",
              "current": "1",
              "desired": "1",
              "kind": "Deployment",
              "kind_plural": "deployments",
              "label": "installer.name=multiclusterhub; installer.namespace=open-cluster-management",
              "name": "multicluster-integrations",
              "namespace": "open-cluster-management",
              "ready": "1"
            },
            {
              "_hubClusterResource": "true",
              "_uid": "local-cluster/046ab6d3-7153-4e15-ad6d-56b669b73f34",
              "apigroup": "apps",
              "apiversion": "v1",
              "available": "1",
              "cluster": "local-cluster",
              "created": "2026-08-06T08:19:00Z",
              "current": "1",
              "desired": "1",
              "kind": "Deployment",
              "kind_plural": "deployments",
              "label": "app.kubernetes.io/component=networking-console-plugin; app.kubernetes.io/managed-by=cluster-network-operator; app.kubernetes.io/name=networking-console-plugin; app.kubernetes.io/part-of=cluster-network-operator; networkoperator.openshift.io/generates-operator-status=stand-alone",
              "name": "networking-console-plugin",
              "namespace": "openshift-network-console",
              "ready": "1"
            }
          ]
        }
      ]
    }
  }
  ```

- Search for pods with the label `app=search`

  - Use the following query:

    ``` graphql
    query mySearch($input: [SearchInput]) {
        search(input: $input) {
                items
            }
    }
    ```

  - Use the following variables:

    ``` graphql
    {"input":[
        {
            "keywords":[],
            "filters":[
                {"property":"kind","values":["Pod"]},
                {"property":"label","values":["app=search"]}],

            "limit":10
        }
    ]}
    ```

- Sample output of search for pods with the label `app=search`

  ``` json
  {
    "data": {
      "search": [
        {
          "count": 5,
          "items": [
            {
              "_hubClusterResource": "true",
              "_ownerUID": "local-cluster/832d85e1-2e79-4d22-8772-3bf50b63db07",
              "_uid": "local-cluster/16c69c2d-aaa2-4946-b12b-a553b1799bd8",
              "apiversion": "v1",
              "cluster": "local-cluster",
              "condition": "ContainersReady=True; Initialized=True; PodReadyToStartContainers=True; PodScheduled=True; Ready=True",
              "container": "search-postgres",
              "created": "2026-08-07T01:43:48Z",
              "hostIP": "10.0.14.198",
              "image": "quay.io:443/acm-d/postgresql-16@sha256:4a8176d682b613c3cc6eebf1b225ac51f7b7e26bba75c95bc0181c74dc869057",
              "kind": "Pod",
              "kind_plural": "pods",
              "label": "app=search; component=search-v2-operator; name=search-postgres; pod-template-hash=7dbbc6cc9b; topology.kubernetes.io/region=us-east-1; topology.kubernetes.io/zone=us-east-1a",
              "name": "search-postgres-7dbbc6cc9b-6gvww",
              "namespace": "open-cluster-management",
              "podIP": "10.128.0.206",
              "restarts": "0",
              "startedAt": "2026-08-07T01:43:48Z",
              "status": "Running"
            },
            {
              "_hubClusterResource": "true",
              "_ownerUID": "local-cluster/fc06ede7-12fa-4fef-974e-c8079c5a5302",
              "_uid": "local-cluster/50a91bad-e4a8-4a3e-a96c-8f375ec98d88",
              "apiversion": "v1",
              "cluster": "local-cluster",
              "condition": "ContainersReady=True; Initialized=True; PodReadyToStartContainers=True; PodScheduled=True; Ready=True",
              "container": "search-collector",
              "created": "2026-08-07T01:42:40Z",
              "hostIP": "10.0.14.198",
              "image": "quay.io:443/acm-d/search-collector-rhel9@sha256:f55b25f334348c58d2729e31be825c2363e5cc4edf5803b8e8d2e9b214f60ac1",
              "kind": "Pod",
              "kind_plural": "pods",
              "label": "app=search; component=search-v2-operator; name=search-collector; pod-template-hash=5dbf7c547b; topology.kubernetes.io/region=us-east-1; topology.kubernetes.io/zone=us-east-1a",
              "name": "search-collector-5dbf7c547b-g2vbd",
              "namespace": "open-cluster-management",
              "podIP": "10.128.0.204",
              "restarts": "0",
              "startedAt": "2026-08-07T01:42:40Z",
              "status": "Running"
            },
            {
              "_hubClusterResource": "true",
              "_ownerUID": "local-cluster/298c9c4f-abd6-4ca9-9896-8bd9b5df82a9",
              "_uid": "local-cluster/67166485-e0d1-42fd-9487-52e8efeb6aae",
              "apiversion": "v1",
              "cluster": "local-cluster",
              "condition": "ContainersReady=True; Initialized=True; PodReadyToStartContainers=True; PodScheduled=True; Ready=True",
              "container": "search-api",
              "created": "2026-08-07T01:42:40Z",
              "hostIP": "10.0.14.198",
              "image": "quay.io:443/acm-d/acm-search-v2-api-rhel9@sha256:3e2eddb15877e3f77888ce51b472f1698480f11b12b520818b66e80bd121968d",
              "kind": "Pod",
              "kind_plural": "pods",
              "label": "app=search; component=search-v2-operator; name=search-api; pod-template-hash=f979884b9; topology.kubernetes.io/region=us-east-1; topology.kubernetes.io/zone=us-east-1a",
              "name": "search-api-f979884b9-v5wt5",
              "namespace": "open-cluster-management",
              "podIP": "10.128.0.205",
              "restarts": "0",
              "startedAt": "2026-08-07T01:42:40Z",
              "status": "Running"
            }
          ]
        }
      ]
    }
  }
  ```

<div>

<div class="title">

Additional resources

</div>

- [Configuring Routes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/ingress_and_load_balancing/index#configuring-routes)

</div>
