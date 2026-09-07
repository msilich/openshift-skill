<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Monitoring Argo CD instances helps you track application health, troubleshoot synchronization issues, and measure deployment performance. The Red Hat OpenShift GitOps Operator automatically connects Argo CD instances to the cluster monitoring stack to collect metrics and generate alerts for out-of-sync applications.

# Prerequisites

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

- You have installed the Red Hat OpenShift GitOps Operator in your cluster.

- An GitOps instance is installed and running in a namespace, such as `openshift-gitops`.

# Monitoring Argo CD health using Prometheus metrics

Monitor the health status of your Argo CD applications by querying Prometheus metrics. This helps you identify degraded applications, track sync status, and troubleshoot deployment issues.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console.

- At least one application is deployed using GitOps.

- Monitoring is enabled for the namespace where your Argo CD instance is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Developer** perspective of the web console, select the namespace where your application is deployed, and navigate to **Observe** → **Metrics**.

2.  From the **Select query** drop-down list, select **Custom query**.

3.  To check the health status of your application, enter the Prometheus Query Language (PromQL) query similar to the following example in the **Expression** field:

    **Example:**

</div>

    sum(argocd_app_info{dest_namespace=~"<your_defined_namespace>",health_status!=""}) by (health_status)

\+

where:

`<your_defined_namespace>`
Specifies the variable with the actual name of your defined namespace, for example `openshift-gitops`.

\+ Review the query results to check the health status of your applications. The results show the number of applications grouped by health status values such as `Healthy`, `Progressing`, `Degraded`, `Suspended`, or `Missing`.

# Disabling automatic scraping of metrics for Argo CD instances

Disabling automatic metric scraping for Argo CD instances helps prevent excessive storage usage in clusters with multiple instances. By default, the Red Hat OpenShift GitOps Operator scrapes metrics for all Argo CD instances, creating monitoring resources and labels in each namespace.

As a result, the Operator creates the following resources and labels in the namespace where the Argo CD instance is installed:

- `gitops-operator-argocd-alerts` prometheus rule

- `<argocd_namespace>-read` role

- `<argocd_name>`, `<argocd_name>-repo-server`, and `<argocd_name>-server` service monitors

- `<argocd_namespace>-prometheus-k8s-read-binding` role binding

- `openshift.io/cluster-monitoring=true` label

If you have multiple Argo CD instances, scraping metrics for each instance can increase storage usage. To reduce storage consumption and gain more control over monitoring, disable metric scraping for individual instances by using the web console’s YAML view to configure the Argo CD custom resource (CR).

As a cluster administrator, by disabling metric scraping for individual instances, you can give your users better control, flexibility, and stability to manage their defined namespaces.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators**.

3.  From the **Project** list, select the project where the user-defined Argo CD instance is installed.

4.  Select **Red Hat OpenShift GitOps** from the installed Operators list and go to the **Argo CD** tab.

5.  Click your user-defined Argo CD instance.

6.  Configure the `ArgoCD` CR of your user-defined Argo CD instance to disable the automatic scraping of metrics:

    1.  Click the **YAML** tab and edit the YAML file of the `ArgoCD` CR.

    2.  In the `ArgoCD` CR, set the `spec.monitoring.disableMetrics` field value to `true`:

        **Example `ArgoCD` CR:**

        ``` YAML
        apiVersion: argoproj.io/v1beta1
        kind: ArgoCD
        metadata:
         name: example
         namespace: spring-petclinic
        spec:
         monitoring:
           disableMetrics: true
        ```

        where:

        `metadata.name`
        Specifies the name of the user-defined Argo CD instance.

        `metadata.namespace`
        Specifies the namespace where you want to run the user-defined Argo CD instance.

        > [!TIP]
        > Alternatively, use the `oc` CLI to disable automatic metric scraping:
        >
        > ``` terminal
        > $ oc patch argocd example -n spring-petclinic --type='json' -p='[{"op": "replace", "path": "/spec/monitoring/disableMetrics", "value": true}]'
        > ```
        >
        > Example output:
        >
        > ``` terminal
        > argocd.argoproj.io/example patched
        > ```

7.  Verify that the Operator adds the `openshift.io/cluster-monitoring=false` label to your defined namespace:

    1.  Go to **Administration** → **Namespaces**.

        The **Namespaces** page displays the created namespaces.

    2.  Click your defined namespace, go to the **YAML** tab, and verify that under the `metadata.labels` section, the `openshift.io/cluster-monitoring=false` label is added by the Operator.

8.  Verify that the Operator deletes the following resources from your defined namespace:

    1.  Go to **Home** → **Search**.

    2.  From the **Resources** list, select **PrometheusRule**, **Role**, **RoleBinding**, and **ServiceMonitors**.

        The **Search** page displays the selected resources.

    3.  In the **Search** page, verify that under the **PrometheusRule** section, the `gitops-operator-argocd-alerts` prometheus rule is removed.

    4.  Under the **Roles** section, from the **Filter** list, select **Namespace Roles**.

    5.  Verify that the `<argocd_namespace>-read` role is removed.

    6.  Under the **RoleBindings** section, from the **Filter** list, select **Namespace RoleBindings**.

    7.  Verify that the `<argocd_namespace>-prometheus-k8s-read-binding` role binding is removed.

    8.  Verify that under the **ServiceMonitors** section, the `<argocd_name>`, `<argocd_name>-repo-server`, and `<argocd_name>-server` service monitors are removed.

        > [!NOTE]
        > You can enable the metrics for your instance by modifying the `spec.monitoring.disableMetrics` field value to `false`. The Operator then creates the required role, role bindings, and service monitors and adds the `openshift.io/cluster-monitoring=true` label to your defined namespace.

</div>

# Additional resources

- [Monitoring Argo CD custom resource workloads](monitoring-argo-cd-custom-resource-workloads.md#monitoring-argo-cd-custom-resource-workloads)
