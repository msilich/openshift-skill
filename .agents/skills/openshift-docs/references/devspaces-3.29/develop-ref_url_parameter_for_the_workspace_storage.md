> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_for_the_workspace_storage). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter for the workspace storage

Use the `storageType` URL parameter to override the default storage strategy for a new workspace, choosing between persistent and ephemeral storage based on your data retention needs.

The URL parameter for specifying a storage type for a workspace is `storageType=`*`<storage_type>`*:

``` plaintext
https://<openshift_dev_spaces_fqdn>#<git_repository_url>?storageType=<storage_type>
```

`storageType=`*`<storage_type>`*  
Possible *`<storage_type>`* values:

- `ephemeral`
- `per-user` (persistent)
- `per-workspace` (persistent)

Tip

With the `ephemeral` or `per-workspace` storage type, you can run multiple workspaces concurrently, which is not possible with the default `per-user` storage type.

**Related concepts**  

- [Persistent storage for workspaces](develop-con_requesting_persistent_storage_for_workspaces.md "OpenShift Dev Spaces workspaces and workspace data are ephemeral and are lost when the workspace stops.")
