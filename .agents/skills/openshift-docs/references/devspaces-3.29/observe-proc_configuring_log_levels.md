> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-proc_configuring_log_levels). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Configure log levels

Configure the log levels of individual loggers in the OpenShift Dev Spaces server using the `CHE_LOGGER_CONFIG` environment variable to control log verbosity and simplify troubleshooting.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

Edit the `CheCluster` Custom Resource on the cluster:

``` bash
$ oc edit checluster/devspaces -n openshift-devspaces
```

``` yaml
spec:
  components:
    cheServer:
      extraProperties:
        CHE_LOGGER_CONFIG: "<key1=value1,key2=value2>"
```

where:

` `*`<key1=value1,key2=value2>`*` `  
Comma-separated list of key-value pairs, where keys are the names of the loggers as seen in the OpenShift Dev Spaces server log output and values are the required log levels.

For example, to configure debug mode for the `WorkspaceManager`:

``` yaml
spec:
  components:
    cheServer:
      extraProperties:
        CHE_LOGGER_CONFIG: "org.eclipse.che.api.workspace.server.WorkspaceManager=DEBUG"
```

## Results

- Verify that the log level is applied by checking the OpenShift Dev Spaces server logs:

  ``` bash
  $ oc logs deployment/devspaces -n openshift-devspaces | grep -i "log level"
  ```

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
- [Configure the CheCluster Custom Resource using the CLI](configure-proc_using_cli_to_configure_checluster.md)
