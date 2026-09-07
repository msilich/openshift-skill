> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-assembly_deploying_private_registry). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy a private extension registry

Deploy an on-premises Open VSX registry for air-gapped OpenShift Dev Spaces environments where workspaces cannot reach the public internet. Build the registry from a prebuilt image or from source, restrict it to internal traffic, and manage its extension catalog.

- **[Deploy from a prebuilt image](extend-proc_deploy_open_vsx_with_prebuilt_image.md)**  
  Deploy a standalone Open VSX extension registry by using an existing container image. Use a private, on-premises registry to control which extensions are available in your OpenShift Dev Spaces workspaces without building from source.
- **[Build a custom extension registry from source](extend-proc_deploy_open_vsx_from_source.md)**  
  Build custom Open VSX server and CLI images from source and deploy them to your cluster. A source build gives you full control over the Open VSX version and allows custom modifications to the registry.
- **[Build the extension registry inside a workspace](extend-proc_running_open_vsx_using_workspace.md)**  
  Build an on-premises Open VSX extension registry by using predefined devfile tasks in a OpenShift Dev Spaces workspace. The workspace environment includes all necessary tools and commands defined in the `.devfile.yaml` file of the Open VSX repository.
- **[Restrict the extension registry to internal traffic](extend-proc_configure_internal_open_vsx_access.md)**  
  Restrict your Open VSX registry to internal cluster traffic by removing the public route and configuring OpenShift Dev Spaces to use the internal service URL. Internal routing keeps extension registry traffic within the cluster and avoids public exposure.
- **[Remove an extension through the registry API](extend-proc_deleting_extension_using_openvsx_admin_api.md)**  
  Remove an extension from your private Open VSX registry by calling the administrator API with an administrator user and a Personal Access Token (PAT).
- **[Remove an extension directly from the database](extend-proc_deleting_extension_from_postgresql_database.md)**  
  Remove extension records and related data directly from the PostgreSQL database when the administrator API is not available or when you need to clean up specific data. If the extension uses local storage, you must also remove its files from the Open VSX server pod.

**Related information**  

- [Register AI coding assistants](extend-assembly_configuring_ai_providers.md)
