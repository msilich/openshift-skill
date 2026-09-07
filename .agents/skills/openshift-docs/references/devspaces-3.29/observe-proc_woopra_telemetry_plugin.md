> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-proc_woopra_telemetry_plugin). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Configure the Woopra telemetry plugin

Configure the [Woopra Telemetry Plugin](https://github.com/che-incubator/devworkspace-telemetry-woopra-plugin) to send telemetry from a Red Hat OpenShift Dev Spaces installation to Segment and Woopra. Any Red Hat OpenShift Dev Spaces deployment can use this plugin with a valid Woopra domain and Segment Write key.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have a valid Woopra domain and Segment Write key.

## About this task

The devfile v2 for the plugin, [plugin.yaml](https://raw.githubusercontent.com/che-incubator/devworkspace-telemetry-woopra-plugin/main/plugin.yaml), has four environment variables that can be passed to the plugin:

- `WOOPRA_DOMAIN` - The Woopra domain to send events to.
- `SEGMENT_WRITE_KEY` - The write key to send events to Segment and Woopra.
- `WOOPRA_DOMAIN_ENDPOINT` - If you prefer not to pass in the Woopra domain directly, the plugin gets it from a supplied HTTP endpoint that returns the Woopra Domain.
- `SEGMENT_WRITE_KEY_ENDPOINT` - If you prefer not to pass in the Segment write key directly, the plugin gets it from a supplied HTTP endpoint that returns the Segment write key.

## Procedure

1.  Deploy the `plugin.yaml` devfile v2 file to an HTTP server with the environment variables set correctly.

2.  Edit the `CheCluster` Custom Resource on the cluster:

    ``` bash
    $ oc edit checluster/devspaces -n openshift-devspaces
    ```

    ``` yaml
    spec:
      devEnvironments:
        defaultPlugins:
        - editor: che-incubator/che-code/latest
          plugins:
          - '<your_plugin_url>'
    ```

    where:

    `editor`  
    The `editorId` to set the telemetry plugin for.

    `plugins`  
    The URL to the telemetry plugin's devfile v2 definition, for example, `https://your-web-server/plugin.yaml`.

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
- [Configure the CheCluster Custom Resource using the CLI](configure-proc_using_cli_to_configure_checluster.md)
