> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_getting_started_samples). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Customize the dashboard samples for your team

Customize the OpenShift Dev Spaces Dashboard to display custom samples that reflect your organization’s preferred languages, frameworks, and project templates for faster onboarding.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Create a JSON file with the samples configuration. The file must contain an array of objects, where each object represents a sample.

    ``` bash
    cat > my-samples.json <<EOF
    [
      {
        "displayName": "<display_name>",
        "description": "<description>",
        "tags": <tags>,
        "url": "<url>",
        "icon": {
          "base64data": "<base64data>",
          "mediatype": "<mediatype>"
        }
      }
    ]
    EOF
    ```

    where:

    `displayName`  
    The display name of the sample.

    `description`  
    The description of the sample.

    `tags`  
    The JSON array of tags, for example, `["java", "spring"]`.

    `url`  
    The URL to the repository containing the devfile.

    `base64data`  
    The base64-encoded data of the icon.

    `mediatype`  
    The media type of the icon. For example, `image/png`.

2.  Create a ConfigMap with the samples configuration:

    ``` bash
    oc create configmap getting-started-samples --from-file=my-samples.json -n openshift-devspaces
    ```

3.  Add the required labels to the ConfigMap:

    ``` bash
    oc label configmap getting-started-samples app.kubernetes.io/part-of=che.eclipse.org app.kubernetes.io/component=getting-started-samples -n openshift-devspaces
    ```

## Results

- Refresh the OpenShift Dev Spaces Dashboard page and verify that the new samples are displayed on the **Create Workspace** page.

**Related information**  

- [Add custom editors to the dashboard](extend-proc_configuring_editors_definitions.md)
- [Restore access to deprecated editors](extend-proc_show_deprecated_editors.md)
- [Set the default IDE for new workspaces](extend-proc_configuring_default_editor.md)
