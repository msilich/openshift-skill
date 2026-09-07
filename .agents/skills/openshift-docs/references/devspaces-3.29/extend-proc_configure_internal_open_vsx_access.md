> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_configure_internal_open_vsx_access). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Restrict the extension registry to internal traffic

Restrict your Open VSX registry to internal cluster traffic by removing the public route and configuring OpenShift Dev Spaces to use the internal service URL. Internal routing keeps extension registry traffic within the cluster and avoids public exposure.

## Before you begin

- You have Open VSX deployed in the `openvsx` project.
- You have the `oc` tool installed.
- You are logged in to the OpenShift cluster as a cluster administrator.
- You have `jq` installed.

## Procedure

1.  Delete the public route for the Open VSX registry:

    ``` bash
    oc delete route internal -n openvsx
    ```

2.  Update the CheCluster custom resource to use the internal service DNS URL:

    ``` bash
    export CHECLUSTER_NAME="$({orch-cli} get checluster --all-namespaces -o json | jq -r '.items[0].metadata.name')" &&
    export CHECLUSTER_NAMESPACE="$({orch-cli} get checluster --all-namespaces -o json | jq -r '.items[0].metadata.namespace')" &&
    export PATCH='{"spec":{"components":{"pluginRegistry":{"openVSXURL":"http://openvsx-server.openvsx.svc:8080"}}}}' &&
    {orch-cli} patch checluster "${CHECLUSTER_NAME}" --type=merge --patch "${PATCH}" -n "${CHECLUSTER_NAMESPACE}"
    ```

3.  Restart any running workspaces to apply the new registry URL.

## Results

- Start a workspace and verify that extensions are available in the Extensions view using the internal registry.

**Related tasks**  

- [Deploy from a prebuilt image](extend-proc_deploy_open_vsx_with_prebuilt_image.md "Deploy a standalone Open VSX extension registry by using an existing container image. Use a private, on-premises registry to control which extensions are available in your OpenShift Dev Spaces workspaces without building from source.")
- [Build a custom extension registry from source](extend-proc_deploy_open_vsx_from_source.md "Build custom Open VSX server and CLI images from source and deploy them to your cluster. A source build gives you full control over the Open VSX version and allows custom modifications to the registry.")
- [Use an alternative extension registry](extend-proc_configuring_open_vsx_registry_url.md "Use an alternative Open VSX registry instance instead of the default embedded registry. Switch to the public open-vsx.org registry for internet-connected environments, or to a standalone on-premises instance for full control over available extensions.")
