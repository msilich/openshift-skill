> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_storage_strategy). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Choose how workspace data is persisted

Choose a storage strategy for OpenShift Dev Spaces to provide persistent or non-persistent storage to workspaces. The selected strategy applies to all newly created workspaces by default.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

Available storage strategies:

- `per-user`: Use a single PVC for all workspaces created by a user.
- `per-workspace`: Each workspace gets its own PVC.
- `ephemeral`: Non-persistent storage; any local changes are lost when the workspace is stopped.

The default storage strategy used in OpenShift Dev Spaces is `per-user`.

## Procedure

Set the `pvcStrategy` field in the `CheCluster` Custom Resource to `per-user`, `per-workspace`, or `ephemeral`:

``` yaml
spec:
  devEnvironments:
    storage:
      pvc:
        pvcStrategy: 'per-user'
```

where:

pvcStrategy  
The available storage strategies are `per-user`, `per-workspace`, and `ephemeral`.

Note

You can set this field at installation or update it on the command line.

## Results

- Verify the `pvcStrategy` value in the `CheCluster` Custom Resource:

  ``` bash
  oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.spec.devEnvironments.storage.pvc.pvcStrategy}'
  ```

**Related concepts**  

- [How workspace files persist across restarts](configure-con_persistent_user_home.md "Red Hat OpenShift Dev Spaces preserves the /home/user directory across workspace restarts for each non-ephemeral workspace, so that user-specific configurations, shell history, and tooling settings persist between sessions.")

**Related tasks**  

- [Use a custom storage provisioner](configure-proc_configuring_storage_classes.md "Use storage classes to bind persistent volumes from a non-default provisioner in OpenShift Dev Spaces.")
- [Adjust workspace storage capacity](configure-proc_configuring_storage_sizes.md "Adjust the persistent volume claim (PVC) size for the per-user or per-workspace storage strategy by setting the claimSize field in the CheCluster Custom Resource. Specify PVC sizes as a Kubernetes resource quantity.")

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
