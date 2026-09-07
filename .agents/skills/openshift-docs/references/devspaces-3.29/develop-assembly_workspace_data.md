> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-assembly_workspace_data). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Persist and restore workspace data

Persist workspace data across restarts by requesting PersistentVolumes in devfiles or PVCs, and restore Cloud Development Environments from backup snapshots to recover uncommitted changes.

- **[Persistent storage for workspaces](develop-con_requesting_persistent_storage_for_workspaces.md)**  
  OpenShift Dev Spaces workspaces and workspace data are ephemeral and are lost when the workspace stops.
- **[Request persistent storage in a devfile](develop-proc_requesting_persistent_storage_in_a_devfile.md)**  
  When a workspace requires its own persistent storage, request a PersistentVolume (PV) in the devfile, and OpenShift Dev Spaces automatically manages the necessary PersistentVolumeClaims.
- **[Request persistent storage in a PVC](develop-proc_requesting_persistent_storage_with_pvc.md)**  
  Request persistent storage by applying a PersistentVolumeClaim (PVC) to provision a PersistentVolume (PV) for your workspaces, so that data persists beyond workspace restarts and can be shared across workspaces.
- **[View backups in the dashboard](develop-proc_viewing_backups_in_the_dashboard.md)**  
  View the status of your workspace backups in the OpenShift Dev Spaces dashboard. The dashboard displays backups available in the default registry set by the administrator.
- **[Restore a workspace from a backup](develop-proc_restoring_a_workspace_from_backup.md)**  
  Restore a workspace from a backup snapshot through the OpenShift Dev Spaces dashboard to recover uncommitted changes or recreate a workspace environment. When the restoration is complete, the dashboard opens the new workspace in a browser tab.

**Related information**  

- [Back up OpenShift Dev Spaces workspaces](configure-assembly_devworkspace_backup.md)
