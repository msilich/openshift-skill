> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_automatic_token_injection). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Use automatic OpenShift token injection

Use the OpenShift user token that is automatically injected into workspace containers to run `oc` and `kubectl` commands against the OpenShift cluster without explicit login.

## Before you begin

- You have a running instance of Red Hat OpenShift Dev Spaces.

## About this task

Warning

Automatic token injection works only on the OpenShift infrastructure.

## Procedure

1.  Open the OpenShift Dev Spaces dashboard and start a workspace.

2.  After the workspace starts, open a terminal in the workspace container.

3.  Run `oc` or `kubectl` commands to deploy applications, inspect and manage cluster resources, or view logs. The injected OpenShift user token authenticates these commands automatically.

    ``` bash
    $ oc get pods
    ```

      
    ![Token Injection in IDE](assets/d881d51a1d48c11b6795.png)  

**Related concepts**  

- [How workspaces connect to OpenShift](integrate-con_integrating_with_openshift.md "OpenShift Dev Spaces workspaces connect to OpenShift through automatic token injection, the OpenShift CLI, and console navigation.")
- [How OpenShift Dev Spaces appears in the OpenShift console](integrate-con_navigating_devspaces_from_openshift_developer_perspective.md "OpenShift Dev Spaces appears in the OpenShift console through a ConsoleLink Custom Resource that adds an interactive link to the Red Hat Applications menu. When the OpenShift Dev Spaces Operator is deployed into OpenShift Container Platform 4.2 and later, it creates a ConsoleLink Custom Resource (CR). This adds an interactive link to the Red Hat Applications menu for accessing the OpenShift Dev Spaces installation. To access the menu, click the three-by-three matrix icon on the main screen of the OpenShift web console. The OpenShift Dev Spaces Console Link creates a new workspace or redirects you to an existing one. For step-by-step instructions, see Additional resources.")

**Related tasks**  

- [List workspaces from the command line](integrate-proc_listing_all_workspaces.md "List workspaces from the command line to check their status, identify stopped or failed workspaces, and monitor resource usage across your OpenShift Dev Spaces environment. .Prerequisites")
