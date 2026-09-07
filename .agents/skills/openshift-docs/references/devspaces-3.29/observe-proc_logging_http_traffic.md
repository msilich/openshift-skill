> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-proc_logging_http_traffic). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Log HTTP traffic

Log the HTTP traffic between the OpenShift Dev Spaces server and the API server of the Kubernetes or OpenShift cluster to troubleshoot communication issues and debug API errors.

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
        CHE_LOGGER_CONFIG: "che.infra.request-logging=TRACE"
```

## Results

- Verify that HTTP traffic is logged in the OpenShift Dev Spaces server logs:

  ``` bash
  $ oc logs deploy/devspaces -n openshift-devspaces | grep "request-logging"
  ```

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
- [Configure the CheCluster Custom Resource using the CLI](configure-proc_using_cli_to_configure_checluster.md)
