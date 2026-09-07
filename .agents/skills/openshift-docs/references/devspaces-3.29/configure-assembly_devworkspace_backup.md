> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-assembly_devworkspace_backup). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Back up workspaces

Back up OpenShift Dev Spaces workspace data to an OCI-compatible registry on a recurring schedule.

The Dev Workspace backup controller creates periodic snapshots of stopped workspace PVCs and stores them as tar.gz archives in a target registry. Supported registries include the OpenShift Container Platform integrated registry and Quay.io. Configure the backup schedule, target registry, and authentication by editing the `DevWorkspaceOperatorConfig` resource.

The `backoffLimit` field sets the number of retries before marking the backup job as failed. The default value is `1`.

Note

By default, the Dev Workspace backup job is disabled.

After you configure backups, you can restore workspace data from a backup. For restore instructions, see Additional resources.

- **[Configure backup with the integrated OpenShift registry](configure-proc_configuring_backup_with_integrated_openshift_registry.md)**  
  Configure the Dev Workspace backup job to use the integrated OpenShift Container Platform container registry. This option requires no additional authentication configuration.
- **[Configure backup with a regular OCI-compatible registry](configure-proc_configuring_backup_with_regular_oci_registry.md)**  
  Configure the Dev Workspace backup job to use a regular OCI-compatible registry for backups. Provide registry credentials through a Kubernetes Secret in the Operator project or in each Dev Workspace project.

**Related information**  

- [Restore workspaces from backups](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop/index#assembly_restoring-workspaces-from-backups_develop)
