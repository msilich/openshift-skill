> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/health_metrics/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="health-metrics-intro"></a>

# Health metrics

Learn how you can use metrics to monitor the health of your components. Many custom metrics are documented in the [Metrics chronicle overview](https://github.com/stolostron/metrics-chronicle#application-metrics).

- [Access the hub cluster metrics service](health_metrics.md#accessing-hub-metrics)

- [Scrape the hub cluster](health_metrics.md#scraping-hub)

- [Scrape the managed cluster](health_metrics.md#scraping-managed)

- [Scrape the standalone cluster](health_metrics.md#scraping-standalone)

<a id="accessing-hub-metrics"></a>

## Access the hub cluster metrics service

Access hub cluster metrics from the OpenShift Container Platform console. To view the collected metrics, you must expose the metrics service on the hub cluster. If your metrics are already exposed in the Grafana dashboard, this procedure is optional.

<div>

<div class="title">

Procedure

</div>

- From the OpenShift Container Platform console, find the metrics service. Click **Observe** \> **Metrics**.

  If you do not see the metrics in the Grafana dashboard, Grafana Explorer, or in the OpenShift Container Platform console, Prometheus might not be configured to scrape metrics. Continue with [Scrape the hub cluster](health_metrics.md#scraping-hub) to expose your metrics.

</div>

<a id="scraping-hub"></a>

## Scrape the hub cluster

Scrape metrics for the hub cluster. You can use Prometheus to expose metrics that are not exposed from the product console. These files are within the `openshift-monitoring` namespace:

<div>

<div class="title">

Procedure

</div>

1.  Create a `ServiceMonitor` for collecting services and exposing metrics. See the following YAML example:

    ``` yaml
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      name: hub-subscription-metrics
      namespace: openshift-monitoring
    spec:
      endpoints:
      - port: metrics
      namespaceSelector:
        matchNames:
        - open-cluster-management
      selector:
        matchLabels:
          app: hub-subscription-metrics
    ```

2.  Run the following command to apply the file:

    ``` bash
    oc apply -f
    ```

3.  Create a `Role` for setting the permissions for monitoring. See the following YAML file:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      name: prometheus-k8s-monitoring
      namespace: open-cluster-management
    rules:
    - apiGroups:
      - ""
      resources:
      - services
      - endpoints
      - pods
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - extensions
      resources:
      - ingresses
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - networking.k8s.io
      resources:
      - ingresses
      verbs:
      - get
      - list
      - watch
    ```

4.  Run the following command to apply the file:

    ``` bash
    oc apply -f
    ```

5.  Create a `RoleBinding` for binding the role to the Prometheus monitoring `ServiceAccount`, as it is in the following example:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: prometheus-k8s-monitoring-binding
      namespace: open-cluster-management
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: Role
      name: prometheus-k8s-monitoring
    subjects:
    - kind: ServiceAccount
      name: prometheus-k8s
      namespace: monitoring
    ```

6.  Run the following command to apply the file:

    ``` bash
    oc apply -f
    ```

7.  To verify, run the following query in the dashboard to find metrics that are reported by the Subscription Operator Metrics Service:

    ``` bash
    {service="hub-subscription-metrics"}
    ```

</div>

<a id="scraping-managed"></a>

## Scrape the managed cluster

Scrape metrics for managed clusters. These files are within the `openshift-monitoring` namespace:

<div>

<div class="title">

Procedure

</div>

1.  Create a `ServiceMonitor` for collecting services exposing metrics. See the following YAML file example:

    ``` yaml
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      name: mc-subscription-metrics
      namespace: openshift-monitoring
    spec:
      endpoints:
      - port: metrics
      namespaceSelector:
        matchNames:
        - open-cluster-management-agent-addon
      selector:
        matchLabels:
          app: mc-subscription-metrics
    ```

2.  Run the following command to apply your file:

    ``` bash
    oc apply -f
    ```

3.  Create a `Role` for setting the permissions for monitoring. See the following YAML file example:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      name: prometheus-k8s-monitoring
      namespace: open-cluster-management-agent-addon
    rules:
    - apiGroups:
      - ""
      resources:
      - services
      - endpoints
      - pods
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - extensions
      resources:
      - ingresses
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - networking.k8s.io
      resources:
      - ingresses
      verbs:
      - get
      - list
      - watch
    ```

4.  Run the following command to apply the file:

    ``` bash
    oc apply -f
    ```

5.  Create a `RoleBinding` for binding the `Role` to the Prometheus monitoring `ServiceAccount`:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: prometheus-k8s-monitoring-binding
      namespace: open-cluster-management-agent-addon
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: Role
      name: prometheus-k8s-monitoring
    subjects:
    - kind: ServiceAccount
      name: prometheus-k8s
      namespace: monitoring
    ```

6.  Run the following command to apply the file:

    ``` bash
    oc apply -f
    ```

7.  Verify in the `Prometheus` dashboard by running the following query to find metrics that are reported by the Subscription Operator Metrics Service:

    ``` bash
    {service="mc-subscription-metrics"}
    ```

</div>

<a id="scraping-standalone"></a>

## Scrape the standalone cluster

Scrape metrics for a standalone cluster.

<div>

<div class="title">

Procedure

</div>

1.  Create a `ServiceMonitor` for collecting services exposing metrics:

    ``` yaml
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      name: standalone-subscription-metrics
      namespace: openshift-monitoring
    spec:
      endpoints:
      - port: metrics
      namespaceSelector:
        matchNames:
        - open-cluster-management
      selector:
        matchLabels:
          app: standalone-subscription-metrics
    ```

2.  Create a `Role` for setting the permissions for monitoring:

    ``` bash
    oc apply -f
    ```

    <!-- Separate adjacent source examples. -->

        See the following `Role` YAML file example:

    <!-- Separate adjacent source examples. -->

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      name: prometheus-k8s-monitoring
      namespace: open-cluster-management
    rules:
    - apiGroups:
      - ""
      resources:
      - services
      - endpoints
      - pods
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - extensions
      resources:
      - ingresses
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - networking.k8s.io
      resources:
      - ingresses
      verbs:
      - get
      - list
      - watch
    ```

3.  Create a `RoleBinding` for binding the `Role` to the Prometheus monitoring `ServiceAccount`. See the following YAML file example:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: prometheus-k8s-monitoring-binding
      namespace: open-cluster-management
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: Role
      name: prometheus-k8s-monitoring
    subjects:
    - kind: ServiceAccount
      name: prometheus-k8s
      namespace: monitoring
    ```

4.  Run the following command to apply the file:

    ``` bash
    oc apply -f
    ```

5.  Verify in the `Prometheus` dashboard by running the following query to find metrics that are reported by the Subscription Operator Metrics Service:

    ``` bash
    {service="standalone-subscription-metrics"}
    ```

</div>
