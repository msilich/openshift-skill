> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_deleting_extension_from_postgresql_database). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Remove an extension directly from the database

Remove extension records and related data directly from the PostgreSQL database when the administrator API is not available or when you need to clean up specific data. If the extension uses local storage, you must also remove its files from the Open VSX server pod.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- The Open VSX registry is deployed in the `openvsx` project.
- You know the publisher name and extension name that you want to delete.

## Procedure

1.  Open a command prompt in the PostgreSQL pod and connect to the database:

    ``` bash
    export POSTGRESQL_POD_NAME=$(oc get pods -n openvsx \
       -o jsonpath="{.items[*].metadata.name}" | tr ' ' '\n' | grep '^postgresql' | head -n 1)
    oc exec -it $POSTGRESQL_POD_NAME -n openvsx -- /bin/bash
    ```

    Inside the pod, run `psql`:

    ``` shell-session
    psql
    ```

    At the `postgres=#` prompt, connect to the database:

    ``` shell-session
    \c openvsx
    ```

    You are now connected to the `openvsx` database as the `postgres` user.

2.  Find the publisher ID and extension ID:

    Identify the extension publisher. Replace *`<publisher_name>`* with the actual publisher name:

    ``` plaintext
    SELECT id, name FROM namespace WHERE name = '<publisher_name>';
    ```

    Identify the extension ID. Replace *`<publisher_id>`* and *`<extension_name>`* with the values from the previous query:

    ``` plaintext
    SELECT id, name, namespace_id FROM extension WHERE namespace_id = <publisher_id> AND name = '<extension_name>';
    ```

    Note the ID of the extension to use as *`<extension_id>`* in the next steps.

3.  Optional: Preview extension versions and file resources:

    Preview the versions:

    ``` plaintext
    SELECT id, version, pre_release, semver_pre_release, semver_is_pre_release FROM extension_version WHERE extension_id = <extension_id> ORDER BY timestamp DESC;
    ```

    Preview the file resources:

    ``` plaintext
    SELECT id, name, type, storage_type FROM file_resource WHERE extension_id = <extension_id> ORDER BY id;
    ```

    If the `storage_type` value is `local`, you must also remove the extension files from the file system on the Open VSX server pod.

4.  Delete the extension from the database:

    Run the following commands in a single transaction. Replace *`<extension_id>`* with the extension ID from step 2.

    ``` plaintext
    BEGIN;
    -- 1. Delete all file resources for the extension
    DELETE FROM file_resource WHERE extension_id = <extension_id>;
    -- 2. Delete all extension reviews
    DELETE FROM extension_review WHERE extension_id = <extension_id>;
    -- 3. Delete all versions of the extension
    DELETE FROM extension_version WHERE extension_id = <extension_id>;
    -- 4. Delete the extension entry itself
    DELETE FROM extension WHERE id = <extension_id>;
    COMMIT;
    ```

    Important

    Run these commands in order within one transaction. Do not skip the `COMMIT` command, or the system does not apply the changes.

5.  If the extension used local storage, remove the extension files from the Open VSX server pod:

    Get the Open VSX server pod name:

    ``` bash
    export OPENVSX_POD_NAME=$(oc get pods -n openvsx -o jsonpath="{.items[*].metadata.name}" | tr ' ' '\n' | grep '^openvsx-server' | head -n 1)
    ```

    Delete the extension folder:

    ``` bash
    oc exec -it $OPENVSX_POD_NAME -n openvsx -- /bin/bash -c "rm -rf /tmp/extensions/<publisher>/<extension>"
    ```

## Results

- Refresh your Open VSX registry and verify that the extension no longer appears in the gallery.

**Related tasks**  

- [Remove an extension through the registry API](extend-proc_deleting_extension_using_openvsx_admin_api.md "Remove an extension from your private Open VSX registry by calling the administrator API with an administrator user and a Personal Access Token (PAT).")
- [Deploy from a prebuilt image](extend-proc_deploy_open_vsx_with_prebuilt_image.md "Deploy a standalone Open VSX extension registry by using an existing container image. Use a private, on-premises registry to control which extensions are available in your OpenShift Dev Spaces workspaces without building from source.")
