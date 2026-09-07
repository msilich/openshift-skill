> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-proc_configuring_machine_autoscaling). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Prevent workspace failures during node scaling

Prevent workspace failures during node scaling by configuring OpenShift Dev Spaces startup timeouts and pod annotations to work with the cluster autoscaler.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have the cluster autoscaler enabled on the OpenShift cluster.

## About this task

When the autoscaler adds a new node, workspace startup can take longer than usual until node provisioning is complete. When the autoscaler removes a node, workspace pods should not be evicted because eviction can cause interruptions and loss of unsaved data.

## Procedure

1.  Set the startup timeout and event handling in the `CheCluster` Custom Resource to handle autoscaler node additions:

    ``` yaml
    spec:
      devEnvironments:
        startTimeoutSeconds: 600
        ignoredUnrecoverableEvents:
          - FailedScheduling
    ```

    where:

    `startTimeoutSeconds`  
    Set to at least 600 seconds to allow time for a new node to be provisioned during workspace startup.

    `ignoredUnrecoverableEvents`  
    Ignore the `FailedScheduling` event to allow workspace startup to continue when a new node is provisioned. This setting is enabled by default.

2.  Add the safe-to-evict annotation to the `CheCluster` Custom Resource to prevent workspace pod eviction when the autoscaler removes a node:

    ``` yaml
    spec:
      devEnvironments:
        workspacesPodAnnotations:
          cluster-autoscaler.kubernetes.io/safe-to-evict: "false"
    ```

## Results

- Start a workspace and verify that the workspace pod contains the `cluster-autoscaler.kubernetes.io/safe-to-evict: "false"` annotation:

  ``` bash
  $ oc get pod <workspace_pod_name> -o jsonpath='{.metadata.annotations.cluster-autoscaler\.kubernetes\.io/safe-to-evict}'
  false
  ```

**Related tasks**  

- [Scale OpenShift Dev Spaces for high availability](optimize-proc_configuring_number_of_replicas.md "Scale OpenShift Dev Spaces for high availability by defining a Kubernetes HorizontalPodAutoscaler (HPA) resource for OpenShift Dev Spaces operands. The HPA dynamically adjusts the number of replicas based on specified metrics.")
