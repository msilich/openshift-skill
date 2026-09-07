> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_configuring_default_editor). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set the default IDE for new workspaces

Set the default editor that OpenShift Dev Spaces uses when creating new workspaces to ensure a consistent development experience. The default editor is specified by its plugin ID in the `publisher/name/version` format.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have `jq` installed. See [Downloading `jq`](https://stedolan.github.io/jq/download/).

## Procedure

1.  Determine the IDs of the available editors. An editor ID has the following format: `publisher/name/version`.

    ``` bash
    oc exec deploy/devspaces-dashboard -n openshift-devspaces  \
        -- curl -s http://localhost:8080/dashboard/api/editors | jq -r '[.[] | "\(.metadata.attributes.publisher)/\(.metadata.name)/\(.metadata.attributes.version)"]'
    ```

2.  Configure the `defaultEditor`:

    ``` bash
    oc patch checluster/devspaces \
        --namespace openshift-devspaces \
        --type='merge' \
        -p '{"spec":{"devEnvironments":{"defaultEditor": "<default_editor>"}}}'
    ```

    where:

    ` `*`<default_editor>`*` `  
    The default editor specified as a plugin ID in `publisher/name/version` format or as a URI.

## Results

- Create a new workspace from the OpenShift Dev Spaces Dashboard and verify that the configured default editor opens.

**Related tasks**  

- [Add custom editors to the dashboard](extend-proc_configuring_editors_definitions.md "Add custom editor definitions to OpenShift Dev Spaces by creating a devfile with the editor configuration and storing it in a ConfigMap to offer additional IDE options to your users.")
- [Hide editors from the dashboard](extend-proc_concealing_editors.md "Hide selected OpenShift Dev Spaces editors from the Dashboard UI, for example IntelliJ IDEA Ultimate, and have only Visual Studio Code - Open Source visible.")

**Related information**  

- [Editor definition samples](https://github.com/devfile/devworkspace-operator/tree/main/samples/editors)
