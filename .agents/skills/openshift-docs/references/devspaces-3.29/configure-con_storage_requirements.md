> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-con_storage_requirements). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# What storage your workspaces need

OpenShift Dev Spaces workspaces store project files in a hierarchical directory structure and require specific storage capabilities depending on the selected strategy.

All workspace storage must use `volumeMode: FileSystem`.

The `per-user` storage strategy shares a single Persistent Volume Claim (PVC) across all of a user’s workspaces. This requires `ReadWriteMany` (RWX) access mode so that multiple workspace pods can mount the same volume simultaneously.

<span id="con_storage-requirements_devspaces___choosing_a_storage_backend_for_the_per_user_strategy"></span>

## [Choosing a storage backend for the Per-User strategy](configure-con_storage_requirements.md#con_storage-requirements_devspaces___choosing_a_storage_backend_for_the_per_user_strategy)

Generic NFS provisioning supports RWX access but has two operational limitations:

- **Quota enforcement:** Kubernetes PVCs cannot reliably enforce storage quotas on generic NFS volumes. A single workspace can exceed its allocation and consume the entire shared volume, causing instability for all users on that node.
- **Data integrity:** Generic NFS implementations often lack the locking and cache coherency required when multiple cluster nodes access the same volume concurrently.

To avoid these issues, use a certified clustered or managed storage solution with a CSI driver that enforces quota limits and provides high-performance RWX file access. Most cloud providers offer suitable CSI drivers, and community-supported distributed storage projects are also available. For instructions on configuring the storage strategy and storage classes, see Additional resources.

**Related tasks**  

- [Choose how workspace data is persisted](configure-proc_configuring_storage_strategy.md "Choose a storage strategy for OpenShift Dev Spaces to provide persistent or non-persistent storage to workspaces. The selected strategy applies to all newly created workspaces by default.")
- [Use a custom storage provisioner](configure-proc_configuring_storage_classes.md "Use storage classes to bind persistent volumes from a non-default provisioner in OpenShift Dev Spaces.")
