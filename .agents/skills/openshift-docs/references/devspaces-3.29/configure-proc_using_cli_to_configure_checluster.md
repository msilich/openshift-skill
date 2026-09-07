> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_using_cli_to_configure_checluster). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Edit the central configuration from the command line

Edit the `CheCluster` Custom Resource YAML file to customize the behavior of a running OpenShift Dev Spaces instance for your environment.

## Before you begin

- You have an instance of OpenShift Dev Spaces on OpenShift. :\_mod-docs-content-type: SNIPPET
- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Edit the CheCluster Custom Resource on the cluster:

    ``` bash
    $ oc edit checluster/devspaces -n openshift-devspaces
    ```

2.  Save and close the file to apply the changes.

## Results

1.  Verify the value of the configured property:

    ``` bash
    $ oc get configmap che -o jsonpath='{.data.<configured_property>}' \
    -n openshift-devspaces
    ```

**Related concepts**  

- [Fine-tune the server](configure-con_advanced_configuration_devspaces_server.md "Fine-tune the OpenShift Dev Spaces server by setting environment variables or overriding properties that are not exposed through the standard CheCluster Custom Resource fields.")

**Related reference**  

- [CheCluster Custom Resource fields reference](configure-ref_checluster_custom_resource_fields.md "Customize the CheCluster Custom Resource by configuring its specification fields to control OpenShift Dev Spaces server, dashboard, gateway, and workspace components.")
