> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_storage_classes). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Use a custom storage provisioner

Use storage classes to bind persistent volumes from a non-default provisioner in OpenShift Dev Spaces.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- A `StorageClass` resource is already provisioned in the cluster. You need the exact name of the storage class to configure.

## About this task

OpenShift Dev Spaces has one component that requires persistent volumes to store data:

- A OpenShift Dev Spaces workspace. OpenShift Dev Spaces workspaces store source code using volumes, for example `/projects` volume.

Note

OpenShift Dev Spaces workspaces source code is stored in the persistent volume only if a workspace is not ephemeral.

Persistent volume claims facts:

- OpenShift Dev Spaces does not create persistent volumes in the infrastructure.
- OpenShift Dev Spaces uses persistent volume claims (PVC) to mount persistent volumes.
- The Dev Workspace operator creates persistent volume claims.

Define a storage class name in the OpenShift Dev Spaces configuration to use the storage classes feature in the OpenShift Dev Spaces PVC.

Use CheCluster Custom Resource definition to define storage classes:

## Procedure

Define storage class names in the `CheCluster` Custom Resource.

``` yaml
spec:
  devEnvironments:
    storage:
      perUserStrategyPvcConfig:
        claimSize: <claim_size>
        storageClass: <storage_class_name>
      perWorkspaceStrategyPvcConfig:
        claimSize: <claim_size>
        storageClass: <storage_class_name>
      pvcStrategy: <pvc_strategy>
```

where:

claimSize  
Persistent Volume Claim size.

storageClass  
Storage class for the Persistent Volume Claim. When omitted or left blank, a default storage class is used.

pvcStrategy  
Persistent volume claim strategy. The supported strategies are:

- `per-user`: All workspaces Persistent Volume Claims share one volume.
- `per-workspace`: Each workspace gets its own individual Persistent Volume Claim.
- `ephemeral`: Non-persistent storage. Local changes are lost when the workspace stops.

## Results

- Start a workspace and verify that the PersistentVolumeClaim uses the configured storage class:

  ``` bash
  oc get pvc -n <user_namespace> -o jsonpath='{.items[*].spec.storageClassName}'
  ```

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
