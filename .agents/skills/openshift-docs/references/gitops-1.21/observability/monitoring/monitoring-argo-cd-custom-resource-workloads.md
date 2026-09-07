<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With Red Hat OpenShift GitOps, you can monitor the availability of Argo CD custom resource workloads for specific Argo CD instances. When workload pods for components such as the application controller, repository server, or API server fail to start, or when the number of ready replicas does not match the desired replica count, the GitOps Operator triggers alerts. You can enable or disable workload monitoring for individual Argo CD instances.

# Prerequisites

- You are logged in to the cluster as a user with the `cluster-admin` role.

- Red Hat OpenShift GitOps is installed in your cluster.

- The monitoring stack is configured in your cluster in the `openshift-monitoring` project. In addition, the Argo CD instance is in a namespace that you can monitor through Prometheus.

- The `kube-state-metrics` service is running on your cluster.

- Optional: If you are enabling monitoring for an Argo CD instance already present in a user-defined project, ensure that the monitoring is [enabled for user-defined projects](https://docs.openshift.com/container-platform/latest/observability/monitoring/enabling-monitoring-for-user-defined-projects.html#enabling-monitoring-for-user-defined-projects_enabling-monitoring-for-user-defined-projects) in your cluster.

  > [!NOTE]
  > To monitor an Argo CD instance in a namespace not watched by the default openshift-monitoring stack, enable user workload monitoring. This applies to namespaces that do not start with `openshift-*`. Enabling user workload monitoring allows the monitoring stack to detect the created PrometheusRule.

# Enabling monitoring for Argo CD custom resource workloads

By default, the monitoring configuration for Argo CD custom resource workloads is set to `false`.

Enable workload monitoring for specific Argo CD instances to receive alerts when component replica counts drift from the desired state. When enabled, the GitOps Operator creates a `PrometheusRule` object that defines alert rules for all workloads managed by the Argo CD instance. The Operator does not overwrite manual changes to the `PrometheusRule` object.

<div>

<div class="title">

Procedure

</div>

1.  Set the `.spec.monitoring.enabled` field value to `true` on a given Argo CD instance:

    **Example Argo CD custom resource:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example-argocd
      labels:
        example: repo
    spec:
     # ...
      monitoring:
        enabled: true
     # ...
    ```

2.  Verify whether an alert rule is included in the PrometheusRule created by the Operator:

    **Example alert rule:**

    ``` yaml
    apiVersion: monitoring.coreos.com/v1
    kind: PrometheusRule
    metadata:
      name: argocd-component-status-alert
      namespace: openshift-gitops
    spec:
      groups:
        - name: ArgoCDComponentStatus
          rules:
            # ...
            - alert: ApplicationSetControllerNotReady
              annotations:
                message: >-
                  ApplicationSet controller deployment for the Argo CD instance in
                  namespace "default" is not running
              expr: >-
                kube_statefulset_status_replicas{
                  statefulset="openshift-gitops-application-controller",
                  namespace="openshift-gitops"
                } !=
                kube_statefulset_status_replicas_ready{
                  statefulset="openshift-gitops-application-controller",
                  namespace="openshift-gitops"
                }
              for: 1m
              labels:
                severity: critical
    ```

    where:

    `spec.groups.name`
    Specifies the name of the alert rule group.

    `spec.groups.rules.alert`
    Specifies the name of the alert that triggers when workloads created by the Argo CD instance are not running as expected.

    `spec.groups.rules.annotations.message`
    Specifies a description of the alert condition.

    `spec.groups.rules.expr`
    Specifies the Prometheus expression that evaluates the alert condition.

    `spec.groups.rules.for`
    Specifies the duration for which the condition must be true before the alert fires.

    `spec.groups.rules.labels.severity`
    Specifies the severity level of the alert.

</div>

# Disabling monitoring for Argo CD custom resource workloads

Disable workload monitoring for specific Argo CD instances when you no longer need alerts for component workloads. When disabled, the GitOps Operator automatically deletes the associated `PrometheusRule` object.

<div>

<div class="title">

Procedure

</div>

- Set the `.spec.monitoring.enabled` field value to `false` on a given Argo CD instance:

  **Example Argo CD custom resource:**

  ``` yaml
  apiVersion: argoproj.io/v1beta1
  kind: ArgoCD
  metadata:
    name: example-argocd
    labels:
      example: repo
  spec:
   # ...
    monitoring:
      enabled: false
   # ...
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `PrometheusRule` object has been deleted:

  ``` terminal
  $ oc get prometheusrule -n <namespace>
  ```

  The `argocd-component-status-alert` `PrometheusRule` object no longer appears in the list.

</div>

# Additional resources

- [Enabling monitoring for user-defined projects](https://docs.openshift.com/container-platform/latest/observability/monitoring/enabling-monitoring-for-user-defined-projects.html#enabling-monitoring-for-user-defined-projects_enabling-monitoring-for-user-defined-projects)
