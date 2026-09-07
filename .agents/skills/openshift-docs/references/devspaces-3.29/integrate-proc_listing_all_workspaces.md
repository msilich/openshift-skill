> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_listing_all_workspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# List workspaces from the command line

List workspaces from the command line to check their status, identify stopped or failed workspaces, and monitor resource usage across your OpenShift Dev Spaces environment. .Prerequisites

## About this task

- You have an active `oc` session with permissions to `get` the `DevWorkspace` resources in your project on the cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You know the relevant OpenShift Dev Spaces user namespace on the cluster. Visit `https://`*`<openshift_dev_spaces_fqdn>`*`/api/kubernetes/namespace` to get your OpenShift Dev Spaces user namespace as `name`.
- You are in the OpenShift Dev Spaces user namespace on the cluster. On OpenShift, use `oc` to [display your current namespace or switch to a namespace](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/developer-cli-commands.html#oc-project).

## Procedure

1.  List your workspaces:

    ``` bash
    $ oc get devworkspaces
    ```

    Example output:

    ``` plaintext
    NAMESPACE   NAME                 DEVWORKSPACE ID             PHASE     INFO
    user1-dev   spring-petclinic     workspace6d99e9ffb9784491   Running   https://url-to-workspace.com
    user1-dev   golang-example       workspacedf64e4a492cd4701   Stopped   Stopped
    user1-dev   python-hello-world   workspace69c26884bbc141f2   Failed    Container tooling has state CrashLoopBackOff
    ```

2.  Optional: Add the `--watch` flag to show **PHASE** changes live:

    ``` bash
    $ oc get devworkspaces --watch
    ```

3.  Optional: Add the `--all-namespaces` flag to list workspaces from all OpenShift Dev Spaces users. This requires administrative permissions on the cluster.

    ``` bash
    $ oc get devworkspaces --all-namespaces
    ```

    **Additional resources**

    - [How workspaces connect to OpenShift](integrate-con_integrating_with_openshift.md "OpenShift Dev Spaces workspaces connect to OpenShift through automatic token injection, the OpenShift CLI, and console navigation.")
    - [How OpenShift Dev Spaces appears in the OpenShift console](integrate-con_navigating_devspaces_from_openshift_developer_perspective.md "OpenShift Dev Spaces appears in the OpenShift console through a ConsoleLink Custom Resource that adds an interactive link to the Red Hat Applications menu. When the OpenShift Dev Spaces Operator is deployed into OpenShift Container Platform 4.2 and later, it creates a ConsoleLink Custom Resource (CR). This adds an interactive link to the Red Hat Applications menu for accessing the OpenShift Dev Spaces installation. To access the menu, click the three-by-three matrix icon on the main screen of the OpenShift web console. The OpenShift Dev Spaces Console Link creates a new workspace or redirects you to an existing one. For step-by-step instructions, see Additional resources.")
    - [Create a workspace from the command line](integrate-proc_creating_workspaces.md "Create a workspace from the command line by applying a DevWorkspace custom resource to the cluster. Use this method when your workflow does not permit the OpenShift Dev Spaces dashboard.")
