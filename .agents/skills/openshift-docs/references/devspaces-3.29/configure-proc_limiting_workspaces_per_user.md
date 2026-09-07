> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_limiting_workspaces_per_user). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Limit the number of workspaces that a user can keep

Limit the number of workspaces a user can keep in the dashboard to reduce demand on the cluster. By default, users can keep an unlimited number of workspaces.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Get the name of the OpenShift Dev Spaces namespace. The default is `openshift-devspaces`.

    ``` shell-session
    $ oc get checluster --all-namespaces \
      -o=jsonpath="{.items[*].metadata.namespace}"
    ```

2.  Configure the `maxNumberOfWorkspacesPerUser` in the `CheCluster` Custom Resource:

    ``` yaml
    spec:
      devEnvironments:
        maxNumberOfWorkspacesPerUser: <kept_workspaces_limit>
    ```

    where:

    ` `*`<kept_workspaces_limit>`*` `  
    The maximum number of workspaces per user. The default value, `-1`, allows users to keep an unlimited number of workspaces. Use a positive integer to set the maximum number of workspaces per user.

3.  Apply the change:

    ``` bash
    $ oc patch checluster/devspaces -n openshift-devspaces \
    --type='merge' -p \
    '{"spec":{"devEnvironments":{"maxNumberOfWorkspacesPerUser": <kept_workspaces_limit>}}}'
    ```

    where:

    `-n`  
    The OpenShift Dev Spaces namespace that you got in step 1.

## Results

- Verify the `maxNumberOfWorkspacesPerUser` value in the `CheCluster` Custom Resource:

  ``` bash
  $ oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.spec.devEnvironments.maxNumberOfWorkspacesPerUser}'
  ```

**Related information**  

- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
