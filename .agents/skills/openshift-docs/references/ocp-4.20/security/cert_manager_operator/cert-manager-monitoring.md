<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

By default, the cert-manager Operator for Red Hat OpenShift exposes metrics for the three core components: controller, cainjector, and webhook. You can configure OpenShift Monitoring to collect these metrics by using the Prometheus Operator format.

# Enabling user workload monitoring

To collect metrics from your specific applications, enable monitoring for user-defined projects. You can enable monitoring for user-defined projects by configuring user workload monitoring in the cluster. For more information, see "Setting up metrics collection for user-defined projects".

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

1.  Verify that the monitoring components for user workloads are running in the `openshift-user-workload-monitoring` namespace by running the following command:

    ``` terminal
    $ oc -n openshift-user-workload-monitoring get pod
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                   READY   STATUS    RESTARTS   AGE
    prometheus-operator-6cb6bd9588-dtzxq   2/2     Running   0          50s
    prometheus-user-workload-0             6/6     Running   0          48s
    prometheus-user-workload-1             6/6     Running   0          48s
    thanos-ruler-user-workload-0           4/4     Running   0          42s
    thanos-ruler-user-workload-1           4/4     Running   0          42s
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

# Configuring metrics collection for cert-manager Operator for Red Hat OpenShift operands by using a ServiceMonitor

The cert-manager Operator for Red Hat OpenShift operands expose metrics by default on port `9402` at the `/metrics` service endpoint. You can configure metrics collection for the cert-manager operands by creating a `ServiceMonitor` custom resource (CR) that enables Prometheus Operator to collect custom metrics. For more information, see "Configuring user workload monitoring".

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the cert-manager Operator for Red Hat OpenShift.

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

        Example `servicemonitor-cert-manager.yaml` file

        </div>

        ``` yaml
        apiVersion: monitoring.coreos.com/v1
        kind: ServiceMonitor
        metadata:
          labels:
            app: cert-manager
            app.kubernetes.io/instance: cert-manager
            app.kubernetes.io/name: cert-manager
          name: cert-manager
          namespace: cert-manager
        spec:
          endpoints:
            - honorLabels: false
              interval: 60s
              path: /metrics
              scrapeTimeout: 30s
              targetPort: 9402
          selector:
            matchExpressions:
              - key: app.kubernetes.io/name
                operator: In
                values:
                  - cainjector
                  - cert-manager
                  - webhook
              - key: app.kubernetes.io/instance
                operator: In
                values:
                  - cert-manager
              - key: app.kubernetes.io/component
                operator: In
                values:
                  - cainjector
                  - controller
                  - webhook
        ```

        </div>

    2.  Create the `ServiceMonitor` CR by running the following command:

        ``` terminal
        $ oc apply -f servicemonitor-cert-manager.yaml
        ```

        After the `ServiceMonitor` CR is created, the user workload Prometheus instance begins metrics collection from the cert-manager Operator for Red Hat OpenShift operands. The collected metrics are labeled with `job="cert-manager"`,`job="cert-manager-cainjector"`, and `job="cert-manager-webhook"`.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the OpenShift Container Platform web console, navigate to **Observe** → **Targets**.

2.  In the **Label** filter field, enter the following labels to filter the metrics targets for each operand:

    ``` terminal
    $ service=cert-manager
    ```

    ``` terminal
    $ service=cert-manager-webhook
    ```

    ``` terminal
    $ service=cert-manager-cainjector
    ```

3.  Confirm that the **Status** column shows `Up` for the `cert-manager`, `cert-manager-webhook`, and `cert-manager-cainjector` entries.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring user workload monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm)

</div>

# Querying metrics for the cert-manager Operator for Red Hat OpenShift operands

As a cluster administrator, or as a user with view access to all namespaces, you can query cert-manager Operator for Red Hat OpenShift operands metrics by using the OpenShift Container Platform web console or the command-line interface (CLI). For more information, see "Accessing metrics".

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the cert-manager Operator for Red Hat OpenShift.

- You have enabled monitoring and metrics collection by creating `ServiceMonitor` object.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, navigate to **Observe** → **Metrics**.

2.  In the query field, enter the following PromQL expressions to query the cert-manager Operator for Red Hat OpenShift operands metric for each operand:

    ``` promql
    {job="cert-manager"}
    ```

    ``` promql
    {job="cert-manager-webhook"}
    ```

    ``` promql
    {job="cert-manager-cainjector"}
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Accessing metrics as an administrator](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/accessing_metrics/accessing-metrics-as-an-administrator)

</div>

# Configuring metrics collection for the istio-csr operand

The `istio-csr` operand exposes metrics by default on port `9402` at the `/metrics` service endpoint. You can configure metrics collection for the operand by creating a `ServiceMonitor` custom resource (CR), which enables the Prometheus Operator to collect custom metrics. For more information, see "Configuring user workload monitoring".

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have installed the cert-manager Operator for Red Hat OpenShift.

- You have enabled user workload monitoring.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `ServiceMonitor` CR definition file:

    <div class="formalpara">

    <div class="title">

    Example `servicemonitor-istio-csr.yaml` file

    </div>

    ``` yaml
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      labels:
        app: cert-manager-istio-csr
        app.kubernetes.io/instance: cert-manager-istio-csr
        app.kubernetes.io/name: cert-manager-istio-csr
      name: cert-manager-istio-csr
      namespace: <istio_csr_project_name>
    spec:
      endpoints:
        - honorLabels: false
          interval: 60s
          path: /metrics
          scrapeTimeout: 30s
          targetPort: 9402
      namespaceSelector:
        matchNames:
          - <istio_csr_project_name>
      selector:
        matchLabels:
          app: cert-manager-istio-csr
          app.kubernetes.io/instance: cert-manager-istio-csr
          app.kubernetes.io/name: cert-manager-istio-csr
    ```

    </div>

    Replace `<istio_csr_project_name>` with the namespace where you created the `IstioCSR` CR.

2.  Create the `ServiceMonitor` CR by running the following command:

    ``` terminal
    $ oc apply -f servicemonitor-istio-csr.yaml
    ```

    After the `ServiceMonitor` CR is created, the user workload Prometheus instance starts collecting metrics from the istio-csr operand. The collected metrics are labeled with `job="cert-manager-istio-csr"`.

</div>

<div>

<div class="title">

Verification

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Click **Observe** → **Targets**.

3.  In the **Label filter** field, enter the `service=cert-manager-istio-csr` label to filter the metrics targets.

4.  Confirm that the **Status** column shows **Up** for the `cert-manager-istio-csr` target.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring user workload monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm)

</div>

# Querying metrics for the istio-csr operand

Cluster administrators, or users with view access to all namespaces, can query metrics for the istio-csr operand by using the OpenShift Container Platform web console. For more information, see "Accessing metrics".

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have installed the cert-manager Operator for Red Hat OpenShift.

- You have enabled monitoring and metrics collection by creating the `ServiceMonitor` object for the istio-csr operand.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Click **Observe** → **Metrics**.

3.  In the query field, enter the `{job="cert-manager-istio-csr"}` PromQL expression to query the `istio-csr` operand metrics. The results display metrics collected for the istio-csr operand, which can help you monitor its performance and behavior.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Accessing metrics as an administrator](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/accessing_metrics/accessing-metrics-as-an-administrator)

</div>
