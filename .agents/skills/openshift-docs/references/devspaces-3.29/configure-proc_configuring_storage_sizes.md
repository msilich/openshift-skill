> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_storage_sizes). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Adjust workspace storage capacity

Adjust the persistent volume claim (PVC) size for the `per-user` or `per-workspace` storage strategy by setting the `claimSize` field in the `CheCluster` Custom Resource. Specify PVC sizes as a Kubernetes resource quantity.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

Default persistent volume claim sizes:

- ``` yaml
  per-user: 10Gi
  ```

- ``` yaml
  per-workspace: 5Gi
  ```

## Procedure

1.  Edit the `CheCluster` Custom Resource on the cluster:

    ``` bash
    $ oc edit checluster/devspaces -n openshift-devspaces
    ```

2.  Set the appropriate `claimSize` field for the desired storage strategy:

    ``` yaml
    spec:
      devEnvironments:
        storage:
          pvc:
            pvcStrategy: '<strategy_name>'
            perUserStrategyPvcConfig:
              claimSize: <resource_quantity>
            perWorkspaceStrategyPvcConfig:
              claimSize: <resource_quantity>
    ```

    where:

    ` `*`<strategy_name>`*` `  
    Select the storage strategy: `per-user` or `per-workspace` or `ephemeral`. Note: the `ephemeral` storage strategy does not use persistent storage, therefore you cannot configure its storage size or other PVC-related attributes.

    `perUserStrategyPvcConfig`, `perWorkspaceStrategyPvcConfig`  
    Specify a claim size on the next line or omit the next line to set the default claim size value. The specified claim size is only used when you select this storage strategy.

    ` `*`<resource_quantity>`*` `  
    The claim size must be specified as a [Kubernetes resource quantity](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/). The available quantity units include: `Ei`, `Pi`, `Ti`, `Gi`, `Mi` and `Ki`.

    Important

    Manually modifying a PVC on the cluster that was provisioned by OpenShift Dev Spaces is not officially supported and may result in unexpected consequences.

    If you want to resize a PVC that is in use by a workspace, you must restart the workspace for the PVC change to occur.

## Results

- Start a workspace and verify that the PersistentVolumeClaim has the configured size:

  ``` bash
  oc get pvc -n <user_namespace> -o jsonpath='{.items[*].spec.resources.requests.storage}'
  ```

**Related concepts**  

- [How workspace files persist across restarts](configure-con_persistent_user_home.md "Red Hat OpenShift Dev Spaces preserves the /home/user directory across workspace restarts for each non-ephemeral workspace, so that user-specific configurations, shell history, and tooling settings persist between sessions.")

**Related tasks**  

- [Use a custom storage provisioner](configure-proc_configuring_storage_classes.md "Use storage classes to bind persistent volumes from a non-default provisioner in OpenShift Dev Spaces.")
- [Choose how workspace data is persisted](configure-proc_configuring_storage_strategy.md "Choose a storage strategy for OpenShift Dev Spaces to provide persistent or non-persistent storage to workspaces. The selected strategy applies to all newly created workspaces by default.")

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
