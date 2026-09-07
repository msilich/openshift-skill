> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_provisioning_projects_in_advance). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Provision projects in advance

Provision workspace projects in advance, rather than relying on automatic provisioning, to control namespace naming and apply custom resource quotas. Repeat the procedure for each user.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Disable automatic namespace provisioning on the `CheCluster` level:

    ``` yaml
    devEnvironments:
      defaultNamespace:
        autoProvision: false
    ```

2.  Create the *\<project_name\>* project for *\<username\>* user with the following labels and annotations:

    ``` yaml
    kind: Namespace
    apiVersion: v1
    metadata:
      name: <project_name>
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: workspaces-namespace
      annotations:
        che.eclipse.org/username: <username>
    ```

    where:

    ` `*`<project_name>`*` `  
    A project name of your choosing.

    ` `*`<username>`*` `  
    The username of the OpenShift Dev Spaces user.

## Results

- Verify that the project was created with the correct labels:

  ``` bash
  $ oc get namespace <project_name> --show-labels
  ```

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
