<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Learn how to monitor Red Hat Advanced Cluster Security for Kubernetes (RHACS) by using Red Hat OpenShift monitoring or custom Prometheus.

<a id="monitoring-overview_monitor-acs"></a>

# Monitoring options for RHACS

You can monitor Red Hat Advanced Cluster Security for Kubernetes (RHACS) by using the built-in monitoring for Red Hat OpenShift or by using custom Prometheus monitoring.

If you use RHACS with Red Hat OpenShift, OpenShift Container Platform includes a preconfigured, preinstalled, and self-updating monitoring stack that provides monitoring for core platform components. RHACS exposes metrics to Red Hat OpenShift monitoring through an encrypted and authenticated endpoint.

<div>

<div class="title">

Additional resources

</div>

- [OpenShift Container Platform monitoring overview](https://docs.openshift.com/container-platform/4.13/monitoring/monitoring-overview.html)

</div>

<a id="monitoring-osp_monitor-acs"></a>

# Monitoring with Red Hat OpenShift

Monitoring with Red Hat OpenShift is enabled by default. No configuration is required for this default behavior.

> [!IMPORTANT]
> If you have previously configured monitoring with the Prometheus Operator, consider removing your custom `ServiceMonitor` resources. RHACS ships with a pre-configured `ServiceMonitor` for Red Hat OpenShift monitoring. Multiple `ServiceMonitors` might result in duplicated scraping.

Monitoring with Red Hat OpenShift is not supported by Scanner. If you want to monitor Scanner, you must first disable the default Red Hat OpenShift monitoring. Then, configure custom Prometheus monitoring.

<a id="monitoring-custom-prometheus_monitor-acs"></a>

# Monitoring with custom Prometheus

Prometheus is an open-source monitoring and alerting platform. You can use it to monitor health and availability of Central and Sensor components of RHACS. When you enable monitoring, RHACS creates a new monitoring service on port number 9090 and a network policy allowing inbound connections to that port.

> [!NOTE]
> This monitoring service exposes an endpoint that TLS does not encrypt and has no authorization. Use this only when you do not want to use Red Hat OpenShift monitoring.

Before you can use custom Prometheus monitoring, if you have Red Hat OpenShift, you must disable the default monitoring. If you are using Kubernetes, you do not need to perform this step.

<div>

<div class="title">

Additional resources

</div>

- [Prometheus documentation](https://prometheus.io/)

</div>

<a id="monitor-osp-disable-operator_monitor-acs"></a>

## Disabling Red Hat OpenShift monitoring for Central services by using the RHACS Operator

To disable the default monitoring by using the Operator, change the configuration of the `Central` custom resource as shown in the following example.

<div>

<div class="title">

Procedure

</div>

1.  On the OpenShift Container Platform web console, go to the **Ecosystem** → **Installed Operators** page.

2.  Select the RHACS Operator from the list of installed Operators.

3.  Click on the **Central** tab.

4.  From the list of Central instances, click on a Central instance for which you want to enable monitoring.

5.  Click on the **YAML** tab and update the YAML configuration as shown in the following example:

    ``` yaml
    monitoring:
        openshift:
            enabled: false
    ```

</div>

<a id="monitor-osp-disable-helm_monitor-acs"></a>

## Disabling Red Hat OpenShift monitoring for Central services by using Helm

To disable the default monitoring by using Helm, change the configuration options in the `central-services` Helm chart.

<div>

<div class="title">

Procedure

</div>

1.  Update the configuration file with the following value:

    ``` yaml
    monitoring.openshift.enabled: false
    ```

2.  Run the `helm upgrade` command and specify the configuration files.

</div>

<a id="enable-monitoring-central-operator_monitor-acs"></a>

## Monitoring Central services by using the RHACS Operator

You can monitor Central services, Central and Scanner, by changing the configuration of the `Central` custom resource.

<div>

<div class="title">

Procedure

</div>

1.  On the OpenShift Container Platform web console, go to the **Ecosystem** → **Installed Operators** page.

2.  Select the Red Hat Advanced Cluster Security for Kubernetes Operator from the list of installed Operators.

3.  Click on the **Central** tab.

4.  From the list of Central instances, click on a Central instance for which you want to enable monitoring for.

5.  Click on the **YAML** tab and update the YAML configuration:

    - For monitoring Central, enable the `central.monitoring.exposeEndpoint` configuration option for the `Central` custom resource.

    - For monitoring Scanner, enable the `scanner.monitoring.exposeEndpoint` configuration option for the `Central` custom resource.

6.  Click **Save**.

</div>

<a id="enable-monitoring-central-helm_monitor-acs"></a>

## Monitoring Central services by using Helm

You can monitor Central services, Central and Scanner, by changing the configuration options in the `central-services` Helm chart.

<div>

<div class="title">

Procedure

</div>

1.  Update the `values-public.yaml` configuration file with the following values:

    ``` yaml
    central.exposeMonitoring: true
    scanner.exposeMonitoring: true
    ```

2.  Run the `helm upgrade` command and specify the configuration files.

</div>

<a id="prometheus-service-monitor-example_monitor-acs"></a>

## Monitoring Central by using Prometheus service monitor

If you are using the Prometheus Operator, you can use a service monitor to scrape the metrics from Red Hat Advanced Cluster Security for Kubernetes (RHACS).

<div class="important">

<div class="title">

</div>

- If you are not using the Prometheus operator, you must edit the Prometheus configuration files to receive the data from RHACS.

- If you use Kubernetes, enter `kubectl` instead of `oc`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new `servicemonitor.yaml` file with the following content:

    ``` yaml
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      name: prometheus-stackrox
      namespace: stackrox
    spec:
      endpoints:
        - interval: 30s
          port: monitoring
          scheme: http
      selector:
        matchLabels:
          app.kubernetes.io/name: <stackrox-service>
    ```

    where:

    `app.kubernetes.io/name:<stackrox-service>`  
    Specifies the name of the service to monitor. The label must match with the `Service` resource that you want to monitor. For example, `central` or `scanner`.

2.  Apply the YAML to the cluster:

    ``` terminal
    $ oc apply -f servicemonitor.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Run the following command to check the status of service monitor:

  ``` terminal
  $ oc get servicemonitor --namespace stackrox
  ```

</div>

<a id="custom-prometheus-metrics_monitor-acs"></a>

# Custom Prometheus metrics

You can enable some Red Hat Advanced Cluster Security for Kubernetes (RHACS) product metrics and scrape them with a dedicated Prometheus server in order to display them in a visualization application such as Perses or Grafana.

You can use a tool such as Perses to display charts based on these metrics. For example, you can create a Perses dashboard to use in the OpenShift Container Platform console that displays RHACS data.

<div>

<div class="title">

Additional resources

</div>

- [Perses documentation](https://perses.dev/perses/docs/overview/)

</div>

<a id="custom-metric-categories_monitor-acs"></a>

## Custom metric categories

You can enable specific Prometheus metrics that you want to expose on the `/metrics` path of the central API endpoint.

The following table lists the available metric categories, their configurability, and default status:

| Metric category       | Configurable | Default status      |
|-----------------------|--------------|---------------------|
| Image vulnerabilities | Yes          | Disabled by default |
| Node vulnerabilities  | Yes          | Disabled by default |
| Policy violations     | Yes          | Disabled by default |
| Total policy numbers  | No           | Enabled by default  |
| Cluster health        | No           | Enabled by default  |
| Certificate expiry    | No           | Enabled by default  |

Metric category and configuration status

Each category is configured with a data gathering period and a list of metrics. A metric is associated with a set of labels and their include and exclude filters. The label filters are regular expressions, applied to the values before calculating totals.

You can use the filters to reduce the /metrics output to relevant records. Use include filters to count only values that match and exclude filters to ignore values that do not match. For example, include filter `ACTIVE` for label "State" to total only active policy violation alerts, or exclude filter `false` for label "IsPlatformWorkload" to exclude platform workload vulnerabilities.

Include filters are applied before exclude filters.

> [!NOTE]
> The `/metrics` path is accessible for API tokens with Administration resource view permissions. The value of the labels are subject to scoped access control.

<a id="configure-custom-prometheus-metrics_monitor-acs"></a>

## Configure custom Prometheus metrics

You can configure custom Prometheus metrics for Red Hat Advanced Cluster Security for Kubernetes (RHACS) by using the API or RHACS portal. You can view the Prometheus metrics that are exposed on the API endpoint at the `/metrics` path. Use the `/v1/config` API to configure metrics with custom names and labels. You can enable or disable one or more of the predefined metrics in the **System Configuration** page.

Collecting and exposing metrics is resource intensive in large environments. The output size depends on the selected labels. For example, selecting only the `Cluster` and `Severity` labels for an image vulnerability metric produces up to five times the number of clusters in records. Adding labels such as `Namespace` increases the output proportionally. Choose labels carefully to avoid unnecessary load.

> [!NOTE]
> Scrape requests require permissions to view the Administration resources and are subject for the scoped access control.

<a id="configuring-custom-prometheus-metrics-by-using-the-api_monitor-acs"></a>

### Configuring custom Prometheus metrics by using the API

You can configure custom Prometheus metrics for Red Hat Advanced Cluster Security for Kubernetes (RHACS) by using the API. The metrics configuration is a part of the private config section of the `/v1/config` service request or response payload.

<div>

<div class="title">

Procedure

</div>

1.  To get the current configuration, run the following command:

    ``` terminal
    $ curl "$ROX_API_ENDPOINT/v1/config" -H "Authorization: Bearer $ROX_API_TOKEN" | jq
    ```

    The `jq` command formats and displays the JSON response from the API in a readable way.

    The following is an example output:

    ``` terminal
    {
      "publicConfig": { ... }
      "privateConfig": { ... }
    }
    ```

2.  To add a policy violation metric named `component_severity`, which includes only component and severity labels, to the configuration, run the following command:

    ``` text
    $ curl "$ROX_API_ENDPOINT/v1/config" -H "Authorization: Bearer $ROX_API_TOKEN" | \
      jq '.privateConfig.metrics.policyViolations.descriptors += {
            component_severity: { labels: [ "Component", "Severity" ] }
          } |
          { config: . }' | \
      curl -X PUT "$ROX_API_ENDPOINT/v1/config" -H "Authorization: Bearer $ROX_API_TOKEN" --data-binary @-
    ```

    The `jq` command adds a new `component_severity` metric descriptor with the labels `Component` and `Severity` to the `policyViolations` configuration, then wraps the result in a `config` object for the update request.

</div>

<a id="configuring-custom-prometheus-metrics-by-using-the-rhacs-portal_monitor-acs"></a>

### Configuring custom Prometheus metrics by using the RHACS portal

You can configure custom Prometheus metrics for Red Hat Advanced Cluster Security for Kubernetes (RHACS) by using the RHACS portal.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Platform Configuration** → **System Configuration**.

2.  Click **Edit**.

3.  Scroll down to the **Prometheus metrics configuration** section, and do any of the following tasks:

    - To enable metrics gathering:

      1.  Enter a positive integer for the gathering period in minutes. You can adjust the number by using the up and down arrows in the spin button.

          > [!IMPORTANT]
          > Use a larger value to reduce how often Central gathers metrics, as the process is resource intensive.

      2.  Select one or more predefined metrics from the list of metrics.

    - To disable metrics gathering, enter `0`.

4.  Click **Save**.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the predefined metric that you enabled is being exposed by Central, run the following command:

  ``` terminal
  $ curl "$ROX_API_ENDPOINT/metrics" \
    -H "Authorization: Bearer $ROX_API_TOKEN" \
    -s | grep <metric_name> | head
  ```

  where:

  `<metric_name>`  
  Specifies the predefined metric that you enabled. For example, `rox_central_image_vuln_deployment_severity`.

  The `grep` command filters the output for the predefined metric.

  The `head` command limits the output to the first few matching lines for readability.

  The output shows the predefined metric aggregated by cluster, namespace, and severity, indicating the number of vulnerabilities for each combination.

</div>

<a id="setting-up-a-prometheus-server-scraping-from-central-service_monitor-acs"></a>

## Setting up a Prometheus server scraping from Central service

Before connecting Perses or other monitoring tools, configure Prometheus to scrape metrics from the Central service. For example, configure the machine access integration for the Kubernetes service account by creating a service account, performing role mapping, and assigning the necessary permissions. This ensures that Prometheus can securely access Central API data for monitoring and visualization purposes.

<div>

<div class="title">

Procedure

</div>

1.  Perform role mapping to ensure that the Prometheus server can access the Central API with a service account token:

    1.  Create and assign a role with the appropriate permission set and scope.

    2.  Add a role mapping to the machine access configuration by using the following service account information:

        |         |                                                    |
        |---------|----------------------------------------------------|
        | `type`  | `KUBE_SERVICE_ACCOUNT`                             |
        | `key`   | `sub`                                              |
        | `value` | `system:serviceaccount:stackrox:prometheus-server` |

2.  Verify that the Prometheus custom resource (CR) contains the following information:

    ``` yaml
    # ...
      serviceAccountName: prometheus-server
      volumes:
      - name: prometheus-token
        projected:
          sources:
          - serviceAccountToken:
              path: token
              expirationSeconds: 3600
      volumeMounts:
      - name: prometheus-token
        mountPath: /var/run/secrets/tokens
        readOnly: true
      additionalScrapeConfigs:
        name: prometheus-additional-scrape-configs
        key: prometheus-additional.yaml
    # ...
    ```

3.  Create the additional scrape configuration secret by using the following content, for example:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: prometheus-additional-scrape-configs
      namespace: stackrox
    stringData:
      prometheus-additional.yaml: |
        - job_name: 'central-metrics'
          scheme: https
          metrics_path: /metrics
          bearer_token_file: /var/run/secrets/tokens/token
          tls_config:
            insecure_skip_verify: true
          static_configs:
          - targets: ['central.stackrox.svc.cluster.local:443']
    ```

</div>

<a id="prometheus-server-example_monitor-acs"></a>

## Setting up a Perses dashboard in OpenShift Container Platform to monitor RHACS

You can configure an in-cluster Prometheus server to work with Red Hat Advanced Cluster Security for Kubernetes (RHACS). You can then use a tool such as Perses running in OpenShift Container Platform or externally to monitor RHACS.

To view a sample Perses configuration, go to the `monitoring-examples` repository in the `stackrox` organization on GitHub, select the `main` branch, and then open the `perses` directory.

<div>

<div class="title">

Prerequisites

</div>

- You have configured Prometheus to scrape metrics from the Central service.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the Perses data source by using the following content, for example:

    ``` yaml
    apiVersion: perses.dev/v1alpha1
    kind: PersesDatasource
    metadata:
      name: rhacs-datasource
      namespace: stackrox
    spec:
      client:
        tls:
          caCert:
            certPath: /ca/service-ca.crt
            type: file
          enable: true
      config:
        default: true
        display:
          name: RHACS Prometheus Datasource
        plugin:
          kind: PrometheusDatasource
          spec:
            proxy:
              kind: HTTPProxy
              spec:
                url: 'http://<PROMETHEUS_SERVICE_HOSTNAME>:<PROMETHEUS_SERVICE_PORT>'
    ```

    where:

    `<PROMETHEUS_SERVICE_HOSTNAME>`  
    Specifies the hostname of the Prometheus service in your cluster.

    - If Prometheus is installed by using the monitoring stack, the hostname might be, for example, `prometheus-operated.stackrox.svc.cluster.local`.

    - If Prometheus in installed by using the Prometheus Operator or another installation, the hostname might be something different.

    `<PROMETHEUS_SERVICE_PORT>`  
    Specifies the port of the Prometheus service in your cluster. For example, `9090`.

2.  Create a Perses dashboard by using the following content, for example:

    ``` yaml
    apiVersion: perses.dev/v1alpha1
    kind: PersesDashboard
    metadata:
      name: sample-stackrox-dashboard-mini
      namespace: stackrox
    spec:
      display:
        name: Advanced Cluster Security / Sample
      panels:
        "total_policy_violations":
          kind: "Panel"
          spec:
            display:
              name: "Total policy violations"
            plugin:
              kind: "StatChart"
              spec:
                calculation: "last"
            queries:
              - kind: "TimeSeriesQuery"
                spec:
                  plugin:
                    kind: "PrometheusTimeSeriesQuery"
                    spec:
                      query: sum(rox_central_policy_violation_namespace_severity{Cluster=~'$Cluster',Namespace=~'$Namespace'})

      layouts:
        - kind: Grid
          spec:
            display:
              title: Policies
              collapse:
                open: true
            items:
              - content:
                  $ref: "#/spec/panels/total_policy_violations"
                "x": 0
                "y": 0
                "width": 6
                "height": 3

      variables:
        - kind: ListVariable
          spec:
            name: Cluster
            allowMultiple: true
            allowAllValue: true
            plugin:
              kind: PrometheusLabelValuesVariable
              spec:
                labelName: Cluster

        - kind: ListVariable
          spec:
            name: Namespace
            allowMultiple: true
            allowAllValue: true
            plugin:
              kind: PrometheusLabelValuesVariable
              spec:
                labelName: Namespace
      duration: 30d
      refreshInterval: 1m
    ```

    This YAML creates a Perses dashboard in the `stackrox` namespace that shows a status panel for the total policy violations over the last 30 days, with variables for `Cluster` and `Namespace`, that refreshes every minute.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Setting up a Prometheus server scraping from Central service](monitor-acs.md#setting-up-a-prometheus-server-scraping-from-central-service_monitor-acs)

</div>

<a id="metric-categories-for-custom-metrics_monitor-acs"></a>

## Metric categories for custom metrics

You can configure the Prometheus custom metrics by specifying a set of labels for each metric category. When using the API, you need to define the metric category for your custom metric.

The following are the supported metric categories:

- `imageVulnerabilities`

- `nodeVulnerabilities`

- `policyViolations`

The following example shows the API request body for configuring a custom metric:

``` yaml
{
# ...

  "metrics": {
    "imageVulnerabilities": {
      "gatheringPeriodMinutes": 60,
      "descriptors": {
        "<metric_name>": {
          "labels": [ "<Labels>" ]
        }
      }
    }
  }

# ...
}
```

where:

`metrics.imageVulnerabilities.descriptors.<metric_name>`  
Specifies the name of a custom metric descriptor.

`metrics.imageVulnerabilities.descriptors.<metric name>.labels`  
Specifies the one or more labels separated by a comma used to total and filter the metric data.

Each metric descriptor defines the labels to collect for that metric within the chosen category.

The following table lists the labels for image vulnerabilities, node vulnerabilities, and policy violations:

| Metric category | Labels |
|----|----|
| Image vulnerabilities | `Cluster`, `Namespace`, `Deployment`, `Type`, `IsActive`, `IsPlatformWorkload`, `ImageID`, `ImageRegistry`, `ImageRemote`, `ImageTag`, `Component`, `ComponentVersion`, `OperatingSystem`, `CVE`, `CVSS`, `Severity`, `EPSSPercentile`, `EPSSProbability`, `IsFixable` |
| Node vulnerabilities | `Cluster`, `Node`, `Kernel`, `OperatingSystem`, `OSImage`, `Component`, `ComponentVersion`, `CVE`, `CVSS`, `Severity`, `EPSSPercentile`, `EPSSProbability`, `IsFixable`, `IsSnoozed` |
| Policy violations | `Cluster`, `Namespace`, `Resource`, `Deployment`, `IsDeploymentActive`, `IsPlatformComponent`, `Policy`, `Categories`, `Severity`, `Action`, `Message`, `Stage`, `State`, `Entity`, `EntityName` |

Metric categories and labels

<a id="system-metrics-and-labels_monitor-acs"></a>

## System metrics and labels

You can view additional system metrics that are exposed by default. These metrics are gathered once every hour.

The following table lists the metric names and their corresponding labels:

| Metric category | Metric name | Labels |
|----|----|----|
| Total policy numbers | `rox_central_cfg_total_policies` | `Enabled` |
| Cluster health | `rox_central_health_cluster_info` | `Cluster`, `Type`, `Status`, `Upgradability` |
| Certificate expiry | `rox_central_cert_exp_hours` | `Component` |

Metric names and labels

> [!NOTE]
> The Certificate expiry metric requires permission to view the integrations.

<a id="additional-resources_monitoring-acs"></a>

# Additional resources

- [Central configuration options using the Operator](../installing/installing_ocp/install-central-config-options-ocp.md)

- [Changing configuration options after deploying the central-services Helm chart](../installing/installing_other/install-central-other.md#change-config-options-after-deployment-central-services_install-central-other)

- [Helm documentation](https://helm.sh/docs/helm/helm_install/#synopsis)
