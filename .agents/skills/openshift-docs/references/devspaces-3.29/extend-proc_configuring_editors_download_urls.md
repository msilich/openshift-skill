> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_configuring_editors_download_urls). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Host editor binaries internally for air-gapped clusters

Host editor binaries internally by configuring custom download URLs for editors in air-gapped OpenShift Dev Spaces environments where editors cannot be retrieved from the public internet. This option applies only to JetBrains editors.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have `jq` installed. See [Downloading `jq`](https://stedolan.github.io/jq/download/).

## Procedure

1.  Determine the IDs of the available editors. An editor ID has the following format: `publisher/name/version`.

    ``` bash
    oc exec deploy/devspaces-dashboard -n openshift-devspaces  \
        -- curl -s http://localhost:8080/dashboard/api/editors | jq -r '[.[] | "\(.metadata.attributes.publisher)/\(.metadata.name)/\(.metadata.attributes.version)"]'
    ```

2.  Configure the download URLs for editors:

    ``` bash
    oc patch checluster/devspaces \
      --namespace openshift-devspaces \
      --type='merge' \
      -p '{
        "spec": {
          "devEnvironments": {
            "editorsDownloadUrls": [
              { "editor": "publisher1/editor-name1/version1", "url": "https://example.com/editor1.tar.gz" },
              { "editor": "publisher2/editor-name2/version2", "url": "https://example.com/editor2.tar.gz" }
            ]
          }
        }
      }'
    ```

    where:

    `editor`  
    The editor ID in the format `publisher/name/version`. Determine the IDs by running the command in step 1.

    `url`  
    The URL of the editor archive to download.

## Results

- Verify that the editor download URLs appear in the `CheCluster` Custom Resource specification.

**Related tasks**  

- [Add custom editors to the dashboard](extend-proc_configuring_editors_definitions.md "Add custom editor definitions to OpenShift Dev Spaces by creating a devfile with the editor configuration and storing it in a ConfigMap to offer additional IDE options to your users.")
- [Restore access to deprecated editors](extend-proc_show_deprecated_editors.md "Restore access to deprecated OpenShift Dev Spaces editors on the Dashboard to support users who need them during migration to a supported editor. By default, the Dashboard UI hides them.")

**Related information**  

- [Customize the dashboard samples for your team](configure-proc_configuring_getting_started_samples.md)
