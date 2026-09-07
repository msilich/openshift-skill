> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-proc_verify_optimization_impact). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Check replica counts, image cache, and workspace startup

Check replica counts, image-cache DaemonSets, and workspace startup time so that you can confirm optimization changes are working.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Verify that OpenShift Dev Spaces server components are running with the expected replica count:

    ``` bash
    $ oc get deployment -n openshift-devspaces \
      -o custom-columns='NAME:.metadata.name,REPLICAS:.spec.replicas,AVAILABLE:.status.availableReplicas'
    ```

    All components should show the configured number of replicas in the `AVAILABLE` column.

2.  If you enabled the Kubernetes Image Puller, verify that the DaemonSet is running on all schedulable nodes:

    ``` bash
    $ oc get daemonset -n openshift-devspaces -l app=kubernetes-image-puller
    ```

    The `DESIRED` and `READY` columns should show the same number, matching your schedulable node count.

3.  Verify that the pre-cached images are present on a node by checking the DaemonSet pod logs:

    ``` bash
    $ oc logs -n openshift-devspaces -l app=kubernetes-image-puller --tail=5
    ```

4.  Start a workspace and observe the startup time. With image pre-caching enabled, workspaces on nodes that have the DaemonSet pod should start within 30 seconds.

5.  Verify overall platform health:

    ``` bash
    $ oc get pods -n openshift-devspaces -o custom-columns='NAME:.metadata.name,READY:.status.containerStatuses[*].ready,STATUS:.status.phase'
    ```

    All pods should show `Running` status with all containers ready.

**Related concepts**  

- [Speed up workspace starts with image caching](optimize-assembly_caching_images_for_faster_workspace_start.md "Speed up workspace starts by deploying the Kubernetes Image Puller to pre-cache container images on cluster nodes so that workspaces start in seconds instead of minutes.")

**Related information**  

- [Monitor OpenShift Dev Spaces platform health](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/observe_monitor/index#monitor-platform-health_observe_monitor)
