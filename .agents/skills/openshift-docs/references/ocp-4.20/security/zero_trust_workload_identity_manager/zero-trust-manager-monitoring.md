<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Track the performance of the Zero Trust Workload Identity Manager by collecting metrics. Configure monitoring to collect metrics from the Security Production Identity Framework for Everyone (SPIRE) Server and SPIRE Agent components.

# Enabling user workload monitoring

Enable user workload monitoring to track metrics for your user-defined projects. Configuring this feature allows you to observe application performance and helps you maintain the health of your services.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` cluster role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `cluster-monitoring-config.yaml` file to define and configure the `ConfigMap`:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: cluster-monitoring-config
      namespace: openshift-monitoring
    data:
      config.yaml: |
        enableUserWorkload: true
    ```

2.  Apply the `ConfigMap` by running the following command:

    ``` terminal
    $ oc apply -f cluster-monitoring-config.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the monitoring components for user workloads are running in the `openshift-user-workload-monitoring` namespace:

  ``` terminal
  $ oc -n openshift-user-workload-monitoring get pod
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` text
  NAME                                   READY   STATUS    RESTARTS   AGE
  prometheus-operator-6cb6bd9588-dtzxq   2/2     Running   0          50s
  prometheus-user-workload-0             6/6     Running   0          48s
  prometheus-user-workload-1             6/6     Running   0          48s
  thanos-ruler-user-workload-0           4/4     Running   0          42s
  thanos-ruler-user-workload-1           4/4     Running   0          42s
  ```

  </div>

</div>

The status of the pods such as `prometheus-operator`, `prometheus-user-workload`, and `thanos-ruler-user-workload` must be `Running`.

<div>

<div class="title">

Additional resources

</div>

- [Setting up metrics collection for user-defined projects](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/configuring_user_workload_monitoring/configuring-metrics-uwm#setting-up-metrics-collection-for-user-defined-projects_configuring-metrics-uwm)

</div>

# Configuring metrics collection for SPIRE Server by using a ServiceMonitor

To collect custom metrics from the SPIRE Server, create a ServiceMonitor custom resource (CR). This configuration enables the Prometheus Operator to scrape metrics from the default endpoint, which helps you monitor your SPIRE deployment.

The SPIRE Server operand exposes metrics by default on port `9402` at the `/metrics` endpoint. You can configure metrics collection for the SPIRE Server by creating a `ServiceMonitor` custom resource (CR) that enables the Prometheus Operator to collect custom metrics.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` cluster role.

- You have installed the Zero Trust Workload Identity Manager.

- You have deployed the SPIRE Server operand in the cluster.

- You have enabled the user workload monitoring.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `ServiceMonitor` CR:

    1.  Create the YAML file that defines the `ServiceMonitor` CR:

        <div class="formalpara">

        <div class="title">

        Example `servicemonitor-spire-server` file

        </div>

        ``` yaml
        apiVersion: monitoring.coreos.com/v1
        kind: ServiceMonitor
        metadata:
        labels:
          app.kubernetes.io/name: server
          app.kubernetes.io/instance: spire
        name: spire-server-metrics
        namespace: zero-trust-workload-identity-manager
        spec:
        endpoints:
        - port: metrics
          interval: 30s
          path: /metrics
        selector:
          matchLabels:
            app.kubernetes.io/name: server
            app.kubernetes.io/instance: spire
        namespaceSelector:
          matchNames:
          - zero-trust-workload-identity-manager
        ```

        </div>

    2.  Create the `ServiceMonitor` CR by running the following command:

        ``` terminal
        $ oc create -f servicemonitor-spire-server.yaml
        ```

        After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the SPIRE Server. The collected metrics are labeled with `job="spire-server"`.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the OpenShift Container Platform web console, navigate to **Observe** → **Targets**.

2.  In the **Label** filter field, enter the following label to filter the metrics targets:

    ``` terminal
    $ service=zero-trust-workload-identity-manager-metrics-service
    ```

3.  Confirm that the **Status** column shows `Up` for the `spire-server-metrics` entry.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring user workload monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm)

</div>

# Configuring metrics collection for SPIRE Agent by using a Service Monitor

Configure metrics collection for the SPIRE Agent by creating a `ServiceMonitor` custom resource (CR). This enables the Prometheus Operator to collect custom metrics that the SPIRE Agent exposes on the default port.

The SPIRE Agent operand exposes metrics by default on port `9402` at the `/metrics` endpoint. You can configure metrics collection for the SPIRE Agent by creating a `ServiceMonitor` custom resource (CR), which enables the Prometheus Operator to collect custom metrics.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` cluster role.

- You have installed the Zero Trust Workload Identity Manager.

- You have deployed the SPIRE Agent operand in the cluster.

- You have enabled the user workload monitoring.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `ServiceMonitor` CR:

    1.  Create the YAML file that defines the `ServiceMonitor` CR:

        <div class="formalpara">

        <div class="title">

        Example `servicemonitor-spire-agent.yaml` file

        </div>

        ``` yaml
        apiVersion: monitoring.coreos.com/v1
        kind: ServiceMonitor
        metadata:
          labels:
            app.kubernetes.io/name: agent
            app.kubernetes.io/instance: spire
          name: spire-agent-metrics
          namespace: zero-trust-workload-identity-manager
        spec:
          endpoints:
          - port: metrics
            interval: 30s
            path: /metrics
          selector:
            matchLabels:
              app.kubernetes.io/name: agent
              app.kubernetes.io/instance: spire
          namespaceSelector:
            matchNames:
            - zero-trust-workload-identity-manager
        ```

        </div>

    2.  Create the `ServiceMonitor` CR by running the following command:

        ``` terminal
        $ oc create -f servicemonitor-spire-agent.yaml
        ```

        After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the SPIRE Agent. The collected metrics are labeled with `job="spire-agent"`.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the OpenShift Container Platform web console, navigate to **Observe** → **Targets**.

2.  In the **Label** filter field, enter the following label to filter the metrics targets:

    ``` terminal
    $ service=spire-agent
    ```

3.  Confirm that the **Status** column shows `Up` for the `spire-agent-metrics` entry.

</div>

# Configuring metrics collection for the Operator by using a ServiceMonitor

The Zero Trust Workload Identity Manager exposes metrics by default on port 8443 at the `/metrics` service endpoint. You can configure metrics collection for the Operator by creating a `ServiceMonitor` custom resource (CR) that enables the Prometheus Operator to collect custom metrics. For more information, see "Configuring user workload monitoring".

The SPIRE Server operand exposes metrics by default on port `9402` at the `/metrics` endpoint. You can configure metrics collection for the SPIRE Server by creating a `ServiceMonitor` custom resource (CR) that enables the Prometheus Operator to collect custom metrics.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` cluster role.

- You have installed the Zero Trust Workload Identity Manager.

- You have enabled the user workload monitoring.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the Operator to use HTTP or HTTPS protocols for the metrics server.

    1.  Update the subscription object for Zero Trust Workload Identity Manager to configure the HTTP protocol by running the following command:

        ``` terminal
        $ oc -n zero-trust-workload-identity-manager patch subscription zero-trust-workload-identity-manager-subscription --type='merge' -p '{"spec":{"config":{"env":[{"name":"METRICS_BIND_ADDRESS","value":":8080"}, {"name": "METRICS_SECURE", "value": "false"}]}}}'
        ```

    2.  Verify the Zero Trust Workload Identity Manager pod is redeployed and that the configured values for `METRICS_BIND_ADDRESS` and `METRICS_SECURE` is updated by running the following command:

        ``` terminal
        $ oc set env --list deployment/zero-trust-workload-identity-manager-controller-manager -n zero-trust-workload-identity-manager | grep -e METRICS_BIND_ADDRESS -e METRICS_SECURE -e container
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` text
        deployments/zero-trust-workload-identity-manager-controller-manager, container manager
        METRICS_BIND_ADDRESS=:8080
        METRICS_SECURE=false
        ```

        </div>

2.  Create the `Secret` resource with `kubernetes.io/service-account.name` annotation to inject the token required for authenticating with the metrics server.

    1.  Create the `secret-zero-trust-workload-identity-manager.yaml` YAML file:

        ``` yaml
        apiVersion: v1
        kind: Secret
        metadata:
         labels:
           name: zero-trust-workload-identity-manager
         name: zero-trust-workload-identity-manager-metrics-auth
         namespace: zero-trust-workload-identity-manager
         annotations:
           kubernetes.io/service-account.name: zero-trust-workload-identity-manager-controller-manager
        type: kubernetes.io/service-account-token
        ```

    2.  Create the `Secret` resource by running the following command:

        ``` terminal
        $ oc apply -f secret-zero-trust-workload-identity-manager.yaml
        ```

3.  Create the `ClusterRoleBinding` resource required for granting permissions to access the metrics.

    1.  Create the `clusterrolebinding-zero-trust-workload-identity-manager.yaml` YAML file:

        ``` yaml
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRoleBinding
        metadata:
         labels:
           name: zero-trust-workload-identity-manager
         name: zero-trust-workload-identity-manager-allow-metrics-access
        roleRef:
         apiGroup: rbac.authorization.k8s.io
         kind: ClusterRole
         name: zero-trust-workload-identity-manager-metrics-reader
        subjects:
        - kind: ServiceAccount
          name: zero-trust-workload-identity-manager-controller-manager
          namespace: zero-trust-workload-identity-manager
        ```

    2.  Create the `ClusterRoleBinding` resource by running the following command:

        ``` terminal
        $ oc apply -f clusterrolebinding-zero-trust-workload-identity-manager.yaml
        ```

4.  Create the following `ServiceMonitor` CR if the metrics server is configured to use `http`.

    1.  Create the `servicemonitor-zero-trust-workload-identity-manager-http.yaml` YAML file:

        ``` yaml
        apiVersion: monitoring.coreos.com/v1
        kind: ServiceMonitor
        metadata:
          labels:
            name: zero-trust-workload-identity-manager
          name: zero-trust-workload-identity-manager-metrics-monitor
          namespace: zero-trust-workload-identity-manager
        spec:
          endpoints:
            - authorization:
                credentials:
                  name: zero-trust-workload-identity-manager-metrics-auth
                  key: token
                type: Bearer
              interval: 60s
              path: /metrics
              port: metrics-http
              scheme: http
              scrapeTimeout: 30s
          namespaceSelector:
            matchNames:
              - zero-trust-workload-identity-manager
          selector:
            matchLabels:
              name: zero-trust-workload-identity-manager
        ```

    2.  Create the `ServiceMonitor` CR by running the following command:

        ``` terminal
        $ oc apply -f servicemonitor-zero-trust-workload-identity-manager-http.yaml
        ```

5.  Create the following `ServiceMonitor` CR if the metrics server is configured to use `https`.

    1.  Create the `servicemonitor-zero-trust-workload-identity-manager-https.yaml` YAML file:

        ``` yaml
        apiVersion: monitoring.coreos.com/v1
        kind: ServiceMonitor
        metadata:
          labels:
            name: zero-trust-workload-identity-manager
          name: zero-trust-workload-identity-manager-metrics-monitor
          namespace: zero-trust-workload-identity-manager
        spec:
          endpoints:
            - authorization:
                credentials:
                  name: zero-trust-workload-identity-manager-metrics-auth
                  key: token
                type: Bearer
              interval: 60s
              path: /metrics
              port: metrics-https
              scheme: https
              scrapeTimeout: 30s
              tlsConfig:
                ca:
                  configMap:
                    name: openshift-service-ca.crt
                    key: service-ca.crt
                serverName: zero-trust-workload-identity-manager-metrics-service.zero-trust-workload-identity-manager.svc.cluster.local
          namespaceSelector:
            matchNames:
              - zero-trust-workload-identity-manager
          selector:
            matchLabels:
              name: zero-trust-workload-identity-manager
        ```

    2.  Create the `ServiceMonitor` CR by running the following command:

        ``` terminal
        $ oc apply -f servicemonitor-zero-trust-workload-identity-manager-https.yaml
        ```

        After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the SPIRE Server. The collected metrics are labeled with `job="zero-trust-workload-identity-manager-metrics-service"`.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the OpenShift Container Platform web console, navigate to **Observe** → **Targets**.

2.  In the **Label** filter field, enter the following label to filter the metrics targets:

    ``` terminal
    $ service=zero-trust-workload-identity-manager-metrics-service
    ```

3.  Confirm that the **Status** column shows `Up` for the `zero-trust-workload-identity-manager` entry.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring user workload monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm)

</div>

# Querying metrics for the Zero Trust Workload Identity Manager

Query SPIRE Agent and SPIRE Server metrics using the OpenShift Container Platform web console or the command line. This helps you monitor the performance of SPIRE components that match specific job labels.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the Zero Trust Workload Identity Manager.

- You have deployed the SPIRE Server and SPIRE Agent operands in the cluster.

- You have enabled monitoring and metrics collection by creating `ServiceMonitor` objects.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, navigate to **Observe** → **Metrics**.

2.  In the query field, enter the following PromQL expression to query SPIRE Server metrics:

    ``` promql
    {job="spire-server"}
    ```

3.  In the query field, enter the following PromQL expression to query SPIRE Agent metrics.

    ``` promql
    {job="spire-agent"}
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Accessing metrics](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/accessing_metrics/index)

</div>

# Zero Trust Workload Identity Manager monitoring available metrics

Monitor the health and performance of Zero Trust Workload Identity Manager components by reviewing exposed metrics. This reference describes controller, certificate, and runtime metrics that help you maintain system health and troubleshoot errors.

The Zero Trust Workload Identity Manager exposes the following metrics:

Controller runtime metrics
- `controller_runtime_active_workers`: Number of currently used workers per controller

- `controller_runtime_max_concurrent_reconciles`: Maximum number of concurrent reconciles per controller

- `controller_runtime_reconcile_errors_total`: Total number of reconciliation errors per controller

- `controller_runtime_reconcile_time_seconds`: Length of time per reconciliation per controller

- `controller_runtime_reconcile_total`: Total number of reconciliations per controller

Certificate watcher metrics
- `certwatcher_read_certificate_errors_total`: Total number of certificate read errors

- `certwatcher_read_certificate_total`: Total number of certificates read

Go runtime metrics
Standard Go runtime metrics including:

- `go_gc_duration_seconds`: Garbage collection duration

- `go_goroutines`: Number of goroutines

- `go_memstats_*`: Memory statistics

- `process_*`: Process statistics

Custom Operator metrics
The operator also exposes custom metrics related to:

- SPIRE Server status and health

- SPIRE Agent deployment status

- SPIFFE CSI Driver status

- OIDC Discovery Provider status

- Workload identity management operations
