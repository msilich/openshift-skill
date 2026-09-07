> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-assembly_configuring_storage). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Control where workspace data is stored

Control storage classes, strategies, and volume sizes so that workspace data persists reliably and meets your organization’s capacity and performance requirements.

- **[What storage your workspaces need](configure-con_storage_requirements.md)**  
  OpenShift Dev Spaces workspaces store project files in a hierarchical directory structure and require specific storage capabilities depending on the selected strategy.
- **[Use a custom storage provisioner](configure-proc_configuring_storage_classes.md)**  
  Use storage classes to bind persistent volumes from a non-default provisioner in OpenShift Dev Spaces.
- **[Choose how workspace data is persisted](configure-proc_configuring_storage_strategy.md)**  
  Choose a storage strategy for OpenShift Dev Spaces to provide persistent or non-persistent storage to workspaces. The selected strategy applies to all newly created workspaces by default.
- **[Adjust workspace storage capacity](configure-proc_configuring_storage_sizes.md)**  
  Adjust the persistent volume claim (PVC) size for the `per-user` or `per-workspace` storage strategy by setting the `claimSize` field in the `CheCluster` Custom Resource. Specify PVC sizes as a Kubernetes resource quantity.
- **[How workspace files persist across restarts](configure-con_persistent_user_home.md)**  
  Red Hat OpenShift Dev Spaces preserves the `/home/user` directory across workspace restarts for each non-ephemeral workspace, so that user-specific configurations, shell history, and tooling settings persist between sessions.

**Related concepts**  

- [Configure fuse-overlayfs](configure-assembly_configuring_fuse_overlayfs.md "Configure fuse-overlayfs for building container images within OpenShift Dev Spaces workspaces. For related container build procedures, see Additional resources.")
- [Back up workspaces](configure-assembly_devworkspace_backup.md "Back up OpenShift Dev Spaces workspace data to an OCI-compatible registry on a recurring schedule.")
