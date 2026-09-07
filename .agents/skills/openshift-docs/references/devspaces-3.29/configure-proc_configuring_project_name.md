> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_project_name). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set the workspace namespace naming convention

Set the project name template that OpenShift Dev Spaces uses when creating workspace projects to enforce naming conventions and organizational compliance.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

A valid project name template follows these conventions:

- The `<username>` or `<userid>` placeholder is mandatory.
- Usernames and IDs cannot contain invalid characters. If a username or ID is incompatible with OpenShift naming conventions, OpenShift Dev Spaces replaces incompatible characters with the `-` symbol.
- OpenShift Dev Spaces evaluates the `<userid>` placeholder into a 14 character long string, and adds a random six character long suffix to prevent IDs from colliding. The result is stored in the user preferences for reuse.
- Kubernetes limits the length of a project name to 63 characters.
- OpenShift limits the length further to 49 characters.

## Procedure

Edit the `CheCluster` Custom Resource on the cluster:

``` bash
$ oc edit checluster/devspaces -n openshift-devspaces
```

``` yaml
spec:
  components:
    devEnvironments:
      defaultNamespace:
        template: <workspace_namespace_template>
```

where:

` `*`<workspace_namespace_template>`*` `  
The project name template. Must include the `<username>` or `<userid>` placeholder.

<span id="proc_configuring-project-name_devspaces__entry__1"></span><span id="proc_configuring-project-name_devspaces__entry__2"></span>

| User workspaces project name template | Resulting project example |
|----|----|
| `<username>-devspaces` (default) | user1-devspaces |
| `<userid>-namespace` | `cge1egvsb2nhba-namespace-ul1411` |
| `<userid>-aka-<username>-namespace` | `cgezegvsb2nhba-aka-user1-namespace-6m2w2b` |

Table 1. User workspaces project name template examples

## Results

- Start a workspace and verify that the workspace project name matches the configured template:

  ``` bash
  oc get devworkspaces -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"\n"}{end}'
  ```

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
