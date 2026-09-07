> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_enabling_multiple_workspaces_simultaneously). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Enable users to run multiple workspaces simultaneously

Enable users to run multiple workspaces simultaneously so that they can work on several projects without stopping active sessions. By default, a user can run only one workspace at a time.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

Note

If using the default storage method, users might experience problems when concurrently running workspaces if pods are distributed across nodes in a multi-node cluster. Switching from the per-user `common` storage strategy to the `per-workspace` storage strategy or using the `ephemeral` storage type can avoid or solve those problems.

## Procedure

1.  Get the name of the OpenShift Dev Spaces namespace. The default is `openshift-devspaces`.

    ``` shell-session
    $ oc get checluster --all-namespaces \
      -o=jsonpath="{.items[*].metadata.namespace}"
    ```

2.  Configure the `maxNumberOfRunningWorkspacesPerUser` in the `CheCluster` Custom Resource:

    ``` yaml
    spec:
      devEnvironments:
        maxNumberOfRunningWorkspacesPerUser: <running_workspaces_limit>
    ```

    where:

    ` `*`<running_workspaces_limit>`*` `  
    The maximum number of simultaneously running workspaces per user. The `-1` value enables users to run an unlimited number of workspaces. The default value is `1`.

3.  Apply the change:

    ``` bash
    $ oc patch checluster/devspaces -n openshift-devspaces \
    --type='merge' -p \
    '{"spec":{"devEnvironments":{"maxNumberOfRunningWorkspacesPerUser": <running_workspaces_limit>}}}'
    ```

    where:

    `-n`  
    The OpenShift Dev Spaces namespace that you got in step 1.

## Results

- Verify the `maxNumberOfRunningWorkspacesPerUser` value in the `CheCluster` Custom Resource:

  ``` bash
  oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.spec.devEnvironments.maxNumberOfRunningWorkspacesPerUser}'
  ```

**Related information**  

- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
- [Choose how workspace data is persisted](configure-proc_configuring_storage_strategy.md)
