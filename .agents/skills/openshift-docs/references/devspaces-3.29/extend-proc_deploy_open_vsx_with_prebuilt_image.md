> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_deploy_open_vsx_with_prebuilt_image). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy from a prebuilt image

Deploy a standalone Open VSX extension registry by using an existing container image. Use a private, on-premises registry to control which extensions are available in your OpenShift Dev Spaces workspaces without building from source.

## Before you begin

- You have the `oc` tool installed.

- You are logged in to the OpenShift cluster where OpenShift Dev Spaces is deployed as a cluster administrator. Tip

  `$ oc login https://`*`<openshift_dev_spaces_fqdn>`*` --username=`*`<my_user>`*

- You have `jq` installed.

## Procedure

1.  Create a new OpenShift project for Open VSX:

    ``` bash
    oc new-project openvsx
    ```

2.  Save the [openvsx-deployment-no-es.yml](https://github.com/eclipse-openvsx/openvsx/blob/master/deploy/openshift/openvsx-deployment-no-es.yml) deployment template file on your file system.

3.  Deploy Open VSX from the directory where you saved the file:

    ``` bash
    oc process -f openvsx-deployment-no-es.yml \
       -p OPENVSX_SERVER_IMAGE=registry.redhat.io/devspaces/openvsx-rhel9:3.29 \
       | oc apply -f -
    ```

4.  Verify that all pods in the `openvsx` project are running and ready:

    ``` bash
    {orch-cli} get pods -n openvsx \
      -o jsonpath='\{range .items[]}\{@.metadata.name}\{"\t"}\{@.status.phase}\{"\t"}\{.status.containerStatuses[].ready}\{"\n"}{end}'
    ```

5.  Add an Open VSX user with a Personal Access Token (PAT) to the database.
    1.  Find the PostgreSQL pod:

        ``` bash
        export POSTGRESQL_POD_NAME=$({orch-cli} get pods -n openvsx \
           -o jsonpath="\{.items[*].metadata.name}" | tr ' ' '\n' | grep '^postgresql' | head -n 1)
        ```

    2.  Insert the username into the Open VSX database:

        ``` bash
        oc exec -n openvsx "${POSTGRESQL_POD_NAME}" -- bash -c \
           "psql -d openvsx -c \"INSERT INTO user_data (id, login_name, role) VALUES (1001, 'eclipse-che', 'privileged');\""
        ```

    3.  Insert the user PAT into the Open VSX database:

        ``` bash
        oc exec -n openvsx "${POSTGRESQL_POD_NAME}" -- bash -c \
           "psql -d openvsx -c \"INSERT INTO personal_access_token (id, user_data, value, active, created_timestamp, accessed_timestamp, description, notified) VALUES (1001, 1001, 'eclipse_che_token', true, current_timestamp, current_timestamp, 'extensions publisher', false);\""
        ```

        Important

        The user PAT must match the decoded value of `OVSX_PAT_BASE64` specified in the deployment file. If you update `OVSX_PAT_BASE64`, use the new decoded value as the user PAT.

6.  Configure OpenShift Dev Spaces to use the internal Open VSX registry:

    ``` bash
    export CHECLUSTER_NAME="$({orch-cli} get checluster --all-namespaces -o json | jq -r '.items[0].metadata.name')" &&
    export CHECLUSTER_NAMESPACE="$({orch-cli} get checluster --all-namespaces -o json | jq -r '.items[0].metadata.namespace')" &&
    export OPENVSX_ROUTE_URL="$({orch-cli} get route internal -n openvsx -o jsonpath='\{.spec.host}')" &&
    export PATCH='\{"spec":\{"components":\{"pluginRegistry":\{"openVSXURL":"https://'"$OPENVSX_ROUTE_URL"'"\}\}\}\}' &&
    {orch-cli} patch checluster "${CHECLUSTER_NAME}" --type=merge --patch "${PATCH}" -n "${CHECLUSTER_NAMESPACE}"
    ```

    Tip

    For detailed instructions on configuring the Open VSX registry URL, see [Use an alternative extension registry](extend-proc_configuring_open_vsx_registry_url.md "Use an alternative Open VSX registry instance instead of the default embedded registry. Switch to the public open-vsx.org registry for internet-connected environments, or to a standalone on-premises instance for full control over available extensions.").

7.  Publish a Visual Studio Code extension from a `.vsix` file. The Open VSX registry does not provide any extension by default. You need the extension publisher name and the download URL of the `.vsix` package.
    1.  Retrieve the name of the pod running the Open VSX server:

        ``` bash
        export OVSX_POD_NAME=$({orch-cli} get pods -n openvsx -o jsonpath="\{.items[*].metadata.name}" | tr ' ' '\n' | grep ^openvsx-server)
        ```

    2.  Download the `.vsix` extension:

        ``` bash
        oc exec -n openvsx "${OVSX_POD_NAME}" -- bash -c "wget -O /tmp/extension.vsix <EXTENSION_DOWNLOAD_URL>"
        ```

    3.  Create an extension publisher:

        ``` bash
        oc exec -n openvsx "${OVSX_POD_NAME}" -- bash -c "ovsx create-namespace <EXTENSION_PUBLISHER_NAME>" || true
        ```

    4.  Publish the extension:

        ``` bash
        oc exec -n openvsx "${OVSX_POD_NAME}" -- bash -c "ovsx publish /tmp/extension.vsix"
        ```

    5.  Delete the downloaded extension file:

        ``` bash
        oc exec -n openvsx "${OVSX_POD_NAME}" -- bash -c "rm /tmp/extension.vsix"
        ```

8.  Optional: Publish multiple extensions from a list. Update the `deploy/openshift/extensions.txt` file with the download URLs of each `.vsix` file, then publish all listed extensions:

    ``` bash
    while IFS= read -r url; do
      oc exec -n openvsx "${OVSX_POD_NAME}" -- bash -c "wget -O /tmp/extension.vsix '$url' && ovsx publish /tmp/extension.vsix && rm /tmp/extension.vsix"
    done < deploy/openshift/extensions.txt
    ```

## Results

- Start any workspace and verify the published extensions are available in the Extensions view of the workspace IDE.
- Navigate to the Open VSX route URL to verify the registry UI displays the published extensions.

**Related tasks**  

- [Restrict the extension registry to internal traffic](extend-proc_configure_internal_open_vsx_access.md "Restrict your Open VSX registry to internal cluster traffic by removing the public route and configuring OpenShift Dev Spaces to use the internal service URL. Internal routing keeps extension registry traffic within the cluster and avoids public exposure.")
- [Remove an extension through the registry API](extend-proc_deleting_extension_using_openvsx_admin_api.md "Remove an extension from your private Open VSX registry by calling the administrator API with an administrator user and a Personal Access Token (PAT).")
- [Build a custom extension registry from source](extend-proc_deploy_open_vsx_from_source.md "Build custom Open VSX server and CLI images from source and deploy them to your cluster. A source build gives you full control over the Open VSX version and allows custom modifications to the registry.")
- [Use an alternative extension registry](extend-proc_configuring_open_vsx_registry_url.md "Use an alternative Open VSX registry instance instead of the default embedded registry. Switch to the public open-vsx.org registry for internet-connected environments, or to a standalone on-premises instance for full control over available extensions.")

**Related information**  

- [Eclipse Open VSX sources](https://github.com/eclipse-openvsx/openvsx/)
- [Eclipse Open VSX documentation](https://github.com/eclipse-openvsx/openvsx/wiki/)
