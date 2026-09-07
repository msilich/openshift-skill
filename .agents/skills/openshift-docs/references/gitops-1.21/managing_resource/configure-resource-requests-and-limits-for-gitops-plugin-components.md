<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure CPU and memory resource requests and limits for the GitOps console plugin and its backend cluster components. Resource allocation is controlled through the `GitOpsService` custom resource (CR) and can be modified during creation or update. The `GitOpsService` controller reconciles both the backend and plugin resources. You can define separate or identical resource configurations for each component depending on your requirements.

# Enabling the GitOpsService custom resource

To enable resource configuration for the GitOps plugin components, specify the `.spec.consolePlugin.backend.resources` field for the backend component and the `.spec.consolePlugin.gitopsPlugin.resources` field for the GitOps console plugin. The `resources` section defines the `requests` (minimum resources) and `limits` (maximum resources) for each component.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the `GitOpsService` CR by running the following command.

    ``` terminal
    $ oc get gitopsservice -A
    ```

    Example output:

    ``` terminal
    NAMESPACE          NAME      AGE
    openshift-gitops   cluster   5d
    ```

2.  Edit the `GitOpsService` CR by running the following command.

    ``` terminal
    $ oc edit gitopsservice cluster -n openshift-gitops
    ```

3.  In the `.spec.consolePlugin` section, add the `.backend.resources` and `.gitopsPlugin.resources` fields. These sections define requests and limits for CPU and memory.

    **Example configuration:**

    ``` yaml
    apiVersion: pipelines.openshift.io/v1alpha1
    kind: GitOpsService
    metadata:
      name: cluster
    spec:
      consolePlugin:
        backend:
          resources:
            limits:
              cpu: 100m
              memory: 1Gi
            requests:
              cpu: 100m
              memory: 1Gi
        gitopsPlugin:
          resources:
            limits:
              cpu: 200m
              memory: 2Gi
            requests:
              cpu: 100m
              memory: 1Gi
    ```

4.  Save and exit the editor.

    After you update the `GitOpsService` CR, the `GitOpsService` controller applies the specified resource requests and limits to the backend and the GitOps plugin components.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

To verify that the resource requests and limits have been applied:

</div>

1.  Verify the resource configuration:

    ``` terminal
    $ oc describe pod <pod-name> -n openshift-gitops
    ```

    Look for the `Limits` and `Requests` sections in the output and ensure they match your configuration.

# Behavior of resource configuration

The following information describes how the `GitOpsService` controller applies resource values defined in the `GitOpsService` custom resource (CR).

- Specified values: When you define resource values in the `GitOpsService` CR, the `GitOpsService` controller applies those values only to the components you specify. For example, if you configure resource limits only for the backend, those values apply to the backend deployment and not to the plugin.

- Default values: If you do not define any resource values in the `GitOpsService` custom resource, the `GitOpsService` controller applies default values to all components.

| Component     | Request CPU | Request Memory | Limit CPU | Limit Memory |
|---------------|-------------|----------------|-----------|--------------|
| Backend       | 250m        | 128Mi          | 500m      | 256Mi        |
| GitOps plugin | 250m        | 128Mi          | 500m      | 256Mi        |

Default resource values
