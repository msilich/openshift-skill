<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

By default, the External Secrets Operator for Red Hat OpenShift exposes metrics for the Operator and the operands. You can configure OpenShift Monitoring to collect these metrics by using the Prometheus Operator format.

# Enabling user workload monitoring

By default, the OpenShift Container Platform monitoring stack does not scrape metrics from user-installed applications like the External Secrets Operator. Enabling user workload monitoring is necessary to collect critical operational data, such as synchronization status, API error rates, and controller performance. This helps you to configure custom alerts for secret sync failures and create dashboards to monitor the overall health of your secret management system. You can enable monitoring for user-defined projects by configuring user workload monitoring in the cluster. For more information, see "Setting up metrics collection for user-defined projects".

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `cluster-monitoring-config.yaml` YAML file:

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

- Verify that the monitoring components for user workloads are running in the `openshift-user-workload-monitoring` namespace by running the following command:

  ``` terminal
  $ oc -n openshift-user-workload-monitoring get pod
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                                   READY   STATUS    RESTARTS   AGE
  prometheus-operator-5f79cff9c9-67pjb   2/2     Running   0          25h
  prometheus-user-workload-0             6/6     Running   0          25h
  thanos-ruler-user-workload-0           4/4     Running   0          25h
  ```

  </div>

  The status of the pods such as `prometheus-operator`, `prometheus-user-workload`, and `thanos-ruler-user-workload` must be `Running`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Setting up metrics collection for user-defined projects](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/configuring_user_workload_monitoring/configuring-metrics-uwm#setting-up-metrics-collection-for-user-defined-projects_configuring-metrics-uwm)

</div>

# Configuring metrics collection for External Secrets Operator for Red Hat OpenShift by using a ServiceMonitor

The External Secrets Operator for Red Hat OpenShift exposes metrics by default on port `8443` at the `/metrics` service endpoint. You can configure metrics collection for the Operator by creating a `ServiceMonitor` custom resource (CR) that enables the Prometheus Operator to collect custom metrics. For more information, see "Configuring user workload monitoring".

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the External Secrets Operator for Red Hat OpenShift.

- You have enabled the user workload monitoring.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the Operator to use `HTTP` for the metrics server. `HTTPS` is enabled by default.

    1.  Update the subscription object for External Secrets Operator for Red Hat OpenShift to configure the `HTTP` protocol by running the following command:

        ``` terminal
        $ oc -n external-secrets-operator patch subscription openshift-external-secrets-operator --type='merge' -p '{"spec":{"config":{"env":[{"name":"METRICS_BIND_ADDRESS","value":":8080"}, {"name": "METRICS_SECURE", "value": "false"}]}}}'
        ```

    2.  To verify that the External Secrets Operator pod is redeployed and that the configured values for `METRICS_BIND_ADDRESS` and `METRICS_SECURE` are updated, run the following command:

        ``` terminal
        $ oc set env --list deployment/external-secrets-operator-controller-manager -n external-secrets-operator | grep -e METRICS_BIND_ADDRESS -e METRICS_SECURE -e container
        ```

        The following example shows that the `METRICS_BIND_ADDRESS` and `METRICS_SECURE` have been updated:

        ``` terminal
        # deployments/external-secrets-operator-controller-manager, container manager
        METRICS_BIND_ADDRESS=:8080
        METRICS_SECURE=false
        ```

2.  Create the `Secret` resource with the `kubernetes.io/service-account.name` annotation to inject the token required for authenticating with the metrics server.

    1.  Create the `secret-external-secrets-operator.yaml` YAML file:

        ``` yaml
        apiVersion: v1
        kind: Secret
        metadata:
          labels:
            app: external-secrets-operator
          name: external-secrets-operator-metrics-auth
          namespace: external-secrets-operator
          annotations:
            kubernetes.io/service-account.name: external-secrets-operator-controller-manager
        type: kubernetes.io/service-account-token
        ```

    2.  Create the `Secret` resource by running the following command:

        ``` terminal
        $ oc apply -f secret-external-secrets-operator.yaml
        ```

3.  Create the `ClusterRoleBinding` resource required for granting permissions to access metrics:

    1.  Create the `clusterrolebinding-external-secrets.yaml` YAML file:

        The following example shows a `clusterrolebinding-external-secrets.yaml` file.

        ``` yaml
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRoleBinding
        metadata:
          labels:
            app: external-secrets-operator
          name: external-secrets-allow-metrics-access
        roleRef:
          apiGroup: rbac.authorization.k8s.io
          kind: ClusterRole
          name: external-secrets-operator-metrics-reader
        subjects:
          - kind: ServiceAccount
            name: external-secrets-operator-controller-manager
            namespace: external-secrets-operator
        ```

    2.  Create the `ClusterRoldeBinding` custom resource by running the following command:

        ``` terminal
        $ oc apply -f clusterrolebinding-external-secrets.yaml
        ```

4.  Create the `ServiceMonitor` CR if using the default `HTTPS`:

    1.  Create the `servicemonitor-external-secrets-operator-https.yaml` YAML file:

        ``` yaml
        apiVersion: monitoring.coreos.com/v1
        kind: ServiceMonitor
        metadata:
          labels:
            app: external-secrets-operator
          name: external-secrets-operator-metrics-monitor
          namespace: external-secrets-operator
        spec:
          endpoints:
            - authorization:
                credentials:
                  name: external-secrets-operator-metrics-auth
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
                serverName: external-secrets-operator-controller-manager-metrics-service.external-secrets-operator.svc.cluster.local
          namespaceSelector:
            matchNames:
              - external-secrets-operator
          selector:
            matchLabels:
              app: external-secrets-operator
              svc: external-secrets-operator-controller-manager-metrics-service
        ```

    2.  Create the `ServiceMonitor` CR by running the following command:

        ``` terminal
        $ oc apply -f servicemonitor-external-secrets-operator-https.yaml
        ```

5.  Create the `ServiceMonitor` CR if configured to use `HTTP`:

    1.  Create the `servicemonitor-external-secrets-operator-http.yaml` YAML file:

        ``` yaml
        apiVersion: monitoring.coreos.com/v1
        kind: ServiceMonitor
        metadata:
          labels:
            app: external-secrets-operator
          name: external-secrets-operator-metrics-monitor
          namespace: external-secrets-operator
        spec:
          endpoints:
            - authorization:
                credentials:
                  name: external-secrets-operator-metrics-auth
                  key: token
                type: Bearer
              interval: 60s
              path: /metrics
              port: metrics-http
              scheme: http
              scrapeTimeout: 30s
          namespaceSelector:
            matchNames:
              - external-secrets-operator
          selector:
            matchLabels:
              app: external-secrets-operator
              svc: external-secrets-operator-controller-manager-metrics-service
        ```

    2.  Create the `ServiceMonitor` CR by running the following command:

        ``` terminal
        $ oc apply -f servicemonitor-external-secrets-operator-http.yaml
        ```

        After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the Operator. The collected metrics are labeled with `job="external-secrets-operator-controller-manager-metrics-service"`.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the OpenShift Container Platform web console, navigate to **Observe** → **Targets**.

2.  In the Label filter field, enter the following labels to filter the metrics targets for each operand:

    ``` terminal
    $ service=external-secrets-operator-controller-manager-metrics-service
    ```

3.  Confirm that the **Status** column shows `Up` for the `external-secrets-operator`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configurable monitoring components](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm#configurable-monitoring-components_preparing-to-configure-the-monitoring-stack-uwm)

</div>

# Querying metrics for the External Secrets Operator for Red Hat OpenShift

As a cluster administrator, or as a user with view access to all namespaces, you can query the Operator metrics by using the OpenShift Container Platform web console or the command-line interface (CLI). For more information, see "Accessing metrics".

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the External Secrets Operator for Red Hat OpenShift.

- You have enabled monitoring and metrics collection by creating a `ServiceMonitor` object.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, navigate to **Observe** → **Metrics**.

2.  In the query field, enter the following PromQL expressions to query the External Secrets Operator for Red Hat OpenShift metric:

    ``` promql
    {job="external-secrets-operator-controller-manager-metrics-service"}
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Accessing metrics](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/accessing_metrics/index)

</div>

# Configuring metrics collection for External Secrets Operator for Red Hat OpenShift operands by using a ServiceMonitor

The External Secrets Operator for Red Hat OpenShift operands exposes metrics by default on port `8080` at the `/metrics` service endpoint for all three components (`external-secrets`, `external-secrets-cert-controll`, and `external-secrets-webhook`). You can configure metrics collection for the external-secrets operands by creating a `ServiceMonitor` custom resource (CR) that enables the Prometheus Operator to collect custom metrics. For more information, see "Configuring user workload monitoring".

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the External Secrets Operator for Red Hat OpenShift.

- You have enabled the user workload monitoring.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `ClusterRoleBinding` resource required for granting permissions to access metrics:

    1.  Create the `clusterrolebinding-external-secrets.yaml` YAML file:

        The following example shows a `clusterrolebinding-external-secrets.yaml` file.

        ``` yaml
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRoleBinding
        metadata:
          labels:
            app: external-secrets
          name: external-secrets-allow-metrics-access
        roleRef:
          apiGroup: rbac.authorization.k8s.io
          kind: ClusterRole
          name: external-secrets-operator-metrics-reader
        subjects:
          - kind: ServiceAccount
            name: external-secrets
            namespace: external-secrets
          - kind: ServiceAccount
            name: external-secrets-cert-controller
            namespace: external-secrets
          - kind: ServiceAccount
            name: external-secrets-webhook
            namespace: external-secrets
        ```

    2.  Create the `ClusterRoldeBinding` custom resource by running the following command:

        ``` terminal
        $ oc apply -f clusterrolebinding-external-secrets.yaml
        ```

2.  Create the `ServiceMonitor` CR:

    1.  Create the `servicemonitor-external-secrets.yaml` YAML file:

        ``` yaml
        apiVersion: monitoring.coreos.com/v1
        kind: ServiceMonitor
        metadata:
          labels:
            app: external-secrets
          name: external-secrets-metrics-monitor
          namespace: external-secrets
        spec:
          endpoints:
            - interval: 60s
              path: /metrics
              port: metrics
              scheme: http
              scrapeTimeout: 30s
          namespaceSelector:
            matchNames:
              - external-secrets
          selector:
            matchExpressions:
              - key: app.kubernetes.io/name
                operator: In
                values:
                  - external-secrets
                  - external-secrets-cert-controller
                  - external-secrets-webhook
              - key: app.kubernetes.io/instance
                operator: In
                values:
                  - external-secrets
              - key: app.kubernetes.io/managed-by
                operator: In
                values:
                  - external-secrets-operator
        ```

    2.  Create the `ServiceMonitor` CR by running the following command:

        ``` terminal
        $ oc apply -f servicemonitor-external-secrets.yaml
        ```

        After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the External Secrets Operator for Red Hat OpenShift operands. The collected metrics are labeled with `job="external-secrets"`,`job="external-secrets-cainjector"`, and `job="external-secrets-webhook"`.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the OpenShift Container Platform web console, navigate to **Observe** → **Targets**.

2.  In the Label filter field, enter the following labels to filter the metrics targets for each operand:

    ``` terminal
    $ service=external-secrets
    ```

    ``` terminal
    $ service=external-secrets-cert-controller-metrics
    ```

    ``` terminal
    $ service=external-secrets-webhook
    ```

3.  Confirm that the **Status** column shows `Up` for the `external-secrets`, `external-secrets-cert-controller` and `external-secrets-webhook`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring user workload monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm)

</div>

# Querying metrics for the external-secrets operand

As a cluster administrator, or as a user with view access to all namespaces, you can query `external-secrets` operand metrics by using the OpenShift Container Platform web console or the command-line interface (CLI). For more information, see "Accessing metrics".

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the External Secrets Operator for Red Hat OpenShift.

- You have enabled monitoring and metrics collection by creating a `ServiceMonitor` object.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, navigate to **Observe** → **Metrics**.

2.  In the query field, enter the following PromQL expressions to query the External Secrets Operator for Red Hat OpenShift operands metric for each operand:

    ``` promql
    {job="external-secrets"}
    ```

    ``` promql
    {job="external-secrets-webhook"}
    ```

    ``` promql
    {job="external-secrets-cert-controller-metrics"}
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Accessing metrics](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/accessing_metrics/index)

</div>
