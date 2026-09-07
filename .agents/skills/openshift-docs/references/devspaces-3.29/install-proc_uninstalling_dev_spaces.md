> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-proc_uninstalling_dev_spaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Remove OpenShift Dev Spaces from your cluster

Remove OpenShift Dev Spaces and all related user data from your OpenShift cluster when you no longer need the platform or want to perform a clean reinstallation.

## Before you begin

- An active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/openshift-cli-oc#getting-started-with-the-openshift-cli).
- You have the `dsc` management tool installed. See [Set up the dsc command-line tool](plan-proc_installing_the_dsc_management_tool.md).

## About this task

Warning

Uninstalling OpenShift Dev Spaces removes all OpenShift Dev Spaces-related user data.

## Procedure

Remove the OpenShift Dev Spaces instance:

``` bash
$ dsc server:delete
```

Tip

The `--delete-namespace` option removes the OpenShift Dev Spaces namespace.

The `--delete-all` option removes the Dev Workspace Operator and the related resources.

Important

Standard operating procedure (SOP) for removing Dev Workspace Operator manually without `dsc` is available in the OpenShift Container Platform [official documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/web-terminal#removing-devworkspace-operator_uninstalling-web-terminal).

## Results

- Verify that the OpenShift Dev Spaces namespace has been removed:

  ``` bash
  oc get namespace openshift-devspaces
  ```

  The expected output is `NotFound`.

**Related information**  

- [Set up the dsc command-line tool](plan-proc_installing_the_dsc_management_tool.md)
