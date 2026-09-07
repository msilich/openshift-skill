<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Monitoring GitOps instances helps you track application deployments, troubleshoot synchronization issues, and optimize resource usage. The Red Hat OpenShift GitOps monitoring dashboards provide a graphical view of instance health, application status, component performance, and rollout metrics across your cluster.

There are four GitOps dashboards available:

- **GitOps Overview**: See an overview of all GitOps instances installed on the cluster, including the number of applications, health and sync status, application and sync activity.

- **GitOps Components**: View detailed resource metrics, such as CPU and memory usage, for the application-controller, repo-server, server, and other GitOps components.

- **GitOps gRPC Services**: View metrics related to gRPC service activity between the various components in Red Hat OpenShift GitOps.

- **GitOps Rollouts**: View metrics related to the total active Rollouts resources, the number of available, desired, and unavailable replicas, and statistics on the performance of the Rollouts controller.

# Accessing GitOps monitoring dashboards

The Red Hat OpenShift GitOps Operator automatically deploys monitoring dashboards when you install it. Access these dashboards from the **Administrator** perspective of the OpenShift Container Platform web console to monitor instance health, application synchronization status, and component performance.

> [!NOTE]
> Disabling or changing the content of the dashboards is not supported.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console.

- The Red Hat OpenShift GitOps Operator is installed in the default namespace, `openshift-gitops-operator`.

- Cluster monitoring is enabled on the `openshift-gitops-operator` namespace.

- A GitOps instance is installed and running in a namespace, such as `openshift-gitops`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the web console, go to **Observe** → **Dashboards**.

2.  From the **Dashboard** drop-down list, select the desired GitOps dashboard: **GitOps (Overview)**, **GitOps / Components**, **GitOps / gRPC Services** or **GitOps / Rollouts**.

3.  Optional: Choose a specific namespace, cluster, and interval from the **Namespace**, **Cluster**, and **Interval** drop-down lists.

4.  Review the metrics displayed in the dashboard to monitor your GitOps instance health and performance.

</div>
