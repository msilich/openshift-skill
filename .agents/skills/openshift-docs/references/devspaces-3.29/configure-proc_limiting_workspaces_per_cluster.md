> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_limiting_workspaces_per_cluster). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Limit the number of workspaces that all users can run simultaneously

Limit the number of concurrently running workspaces across the cluster to manage resource consumption. By default, all users can run an unlimited number of workspaces.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Configure the `maxNumberOfRunningWorkspacesPerCluster` in the `CheCluster` Custom Resource:

    ``` yaml
    spec:
      devEnvironments:
        maxNumberOfRunningWorkspacesPerCluster: <running_workspaces_limit>
    ```

    where:

    ` `*`<running_workspaces_limit>`*` `  
    The maximum number of concurrently running workspaces across the entire Kubernetes cluster. This applies to all users in the system. The `-1` value means there is no limit on the number of running workspaces.

2.  Apply the change:

    ``` bash
    $ oc patch checluster/devspaces -n openshift-devspaces \
    --type='merge' -p \
    '{"spec":{"devEnvironments":{"maxNumberOfRunningWorkspacesPerCluster": <running_workspaces_limit>}}}'
    ```

## Results

- Verify the `maxNumberOfRunningWorkspacesPerCluster` value in the `CheCluster` Custom Resource:

  ``` bash
  $ oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.spec.devEnvironments.maxNumberOfRunningWorkspacesPerCluster}'
  ```

**Related information**  

- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
