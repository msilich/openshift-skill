> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_configuring_open_vsx_registry_url). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Use an alternative extension registry

Use an alternative Open VSX registry instance instead of the default embedded registry. Switch to the public open-vsx.org registry for internet-connected environments, or to a standalone on-premises instance for full control over available extensions.

## Before you begin

- You have administrator access to the OpenShift cluster where OpenShift Dev Spaces is deployed.
- You have an active `oc` session with administrative permissions. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

The default is the embedded instance of the Open VSX registry.

If the default Open VSX registry instance does not meet your requirements, you can select one of the following instances:

- The Open VSX registry instance at `https://open-vsx.org` that requires access to the internet.
- A standalone Open VSX registry instance that is deployed on a network accessible from OpenShift Dev Spaces workspace pods.

## Procedure

Edit the `CheCluster` custom resource to update the `openVSXURL` value:

``` yaml
spec:
  components:
    pluginRegistry:
      openVSXURL: "<url_of_an_open_vsx_registry_instance>"
```

where:

` `*`<url_of_an_open_vsx_registry_instance>`*` `  
The URL of the Open VSX registry instance. For example: `openVSXURL: "https://open-vsx.org"`.

- To select the embedded Open VSX registry instance in the `plugin-registry` pod, use `openVSXURL: ''`. You can customize the list of included extensions. See [Add or remove extensions in a workspace](extend-proc_adding_or_removing_extensions_in_a_workspace.md "Add or remove extensions in the embedded Open VSX registry instance directly within a workspace to create a custom extension catalog for your organization.") or [Add or remove extensions from the Linux command line](extend-proc_adding_or_removing_extensions_on_linux.md "Add or remove extensions in a custom plugin registry from the Linux command line to create a tailored Open VSX registry with the specific extensions your organization needs.").
- You can also point `openVSXURL` at the URL of a standalone Open VSX registry instance. The URL must be accessible from within your organization’s cluster and not blocked by a proxy.

Note

To ensure the stability and performance of the community-supported Open VSX Registry, API usage is organized into defined tiers. The Eclipse Foundation implements these limits to protect infrastructure from high-frequency automated traffic and to provide consistent service quality for all users. For more information, see [Rate Limits and Usage Tiers](https://github.com/EclipseFdn/open-vsx.org/wiki/rate-limiting) and the [open-vsx.org wiki](https://github.com/EclipseFdn/open-vsx.org/wiki).

Important

Using <https://open-vsx.org> is not recommended in an air-gapped environment, isolated from the internet. To reduce the risk of malware infections and unauthorized access to your code, use the embedded or self-hosted Open VSX registry with a curated set of extensions.

Warning

Due to the dedicated Microsoft [Terms of Use](https://cdn.vsassets.io/v/M190_20210811.1/_content/Microsoft-Visual-Studio-Marketplace-Terms-of-Use.pdf), [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/vscode) is not supported by Red Hat OpenShift Dev Spaces.

## Results

- Confirm that the `plugin-registry` pod has restarted and is running.
- Open a workspace and verify that extensions are available from the selected registry instance in the **Extensions** view.

**Related information**  

- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
- [Open VSX registry](https://open-vsx.org/)
