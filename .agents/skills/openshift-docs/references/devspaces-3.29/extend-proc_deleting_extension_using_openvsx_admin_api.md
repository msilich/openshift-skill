> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_deleting_extension_using_openvsx_admin_api). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Remove an extension through the registry API

Remove an extension from your private Open VSX registry by calling the administrator API with an administrator user and a Personal Access Token (PAT).

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- The Open VSX registry is deployed in the `openvsx` project.

## Procedure

1.  Add the Open VSX administrator user and PAT to the database:

    ``` bash
    export POSTGRESQL_POD_NAME=$(oc get pods -n openvsx \
       -o jsonpath="{.items[*].metadata.name}" | tr ' ' '\n' | grep '^postgresql' | head -n 1)
    ```

    ``` bash
    oc exec -n openvsx "$POSTGRESQL_POD_NAME" -- bash -c \
       "psql -d openvsx -c \"INSERT INTO user_data (id, login_name, role) VALUES (1002, 'openvsx-admin', 'admin');\""
    ```

    ``` bash
    oc exec -n openvsx "$POSTGRESQL_POD_NAME" -- bash -c \
       "psql -d openvsx -c \"INSERT INTO personal_access_token (id, user_data, value, active, created_timestamp, accessed_timestamp, description, notified) VALUES (1002, 1002, '<your_admin_token>', true, current_timestamp, current_timestamp, 'Admin API Token', false);\""
    ```

    Note

    Use a strong, unique value for *`<your_admin_token>`* in production environments.

2.  Delete an extension and all its versions:

    ``` bash
    curl -X POST \
      "https://<your_openvsx_server_url>/admin/api/extension/<publisher>/<extension>/delete?token=<your_admin_token>"
    ```

    where:

    ` `*`<your_openvsx_server_url>`*` `  
    The URL of the Open VSX server.

    ` `*`<publisher>`*` `  
    The extension publisher name.

    ` `*`<extension>`*` `  
    The extension name.

    ` `*`<your_admin_token>`*` `  
    The PAT value created in step 1.

3.  Optional: Delete a specific version of an extension:

    ``` bash
    curl -X POST \
      -H "Content-Type: application/json" \
      -d '[{"version": "<version>", "targetPlatform": "<platform>"}]' \
      "https://<your_openvsx_server_url>/admin/api/extension/<publisher>/<extension>/delete?token=<your_admin_token>"
    ```

    You can list multiple version and platform pairs in the JSON array.

## Results

- Refresh the Open VSX registry and verify that the extension no longer appears.

**Related tasks**  

- [Remove an extension directly from the database](extend-proc_deleting_extension_from_postgresql_database.md "Remove extension records and related data directly from the PostgreSQL database when the administrator API is not available or when you need to clean up specific data. If the extension uses local storage, you must also remove its files from the Open VSX server pod.")
- [Deploy from a prebuilt image](extend-proc_deploy_open_vsx_with_prebuilt_image.md "Deploy a standalone Open VSX extension registry by using an existing container image. Use a private, on-premises registry to control which extensions are available in your OpenShift Dev Spaces workspaces without building from source.")
