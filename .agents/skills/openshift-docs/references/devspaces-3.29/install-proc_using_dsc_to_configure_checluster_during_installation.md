> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-proc_using_dsc_to_configure_checluster_during_installation). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Customize settings during deployment

Customize the `CheCluster` Custom Resource during installation so that OpenShift Dev Spaces deploys with your organization’s specific settings instead of Operator defaults.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have the `dsc` management tool installed. See [Set up the dsc command-line tool](plan-proc_installing_the_dsc_management_tool.md).

## Procedure

1.  Create a `che-operator-cr-patch.yaml` YAML file that contains the subset of the `CheCluster` Custom Resource to configure:

    ``` yaml
    spec:
      <component>:
          <property_to_configure>: <value>
    ```

2.  Deploy OpenShift Dev Spaces and apply the changes described in `che-operator-cr-patch.yaml` file:

    ``` bash
    $ dsc server:deploy \
    --che-operator-cr-patch-yaml=che-operator-cr-patch.yaml \
    --platform <chosen_platform>
    ```

## Results

- Verify the value of the configured property:

  ``` bash
  $ oc get configmap che -o jsonpath='{.data.<configured_property>}' \
  -n openshift-devspaces
  ```

**Related information**  

- [CheCluster Custom Resource fields](configure-ref_checluster_custom_resource_fields.md)
- [Fine-tune the OpenShift Dev Spaces server](configure-con_advanced_configuration_devspaces_server.md)
