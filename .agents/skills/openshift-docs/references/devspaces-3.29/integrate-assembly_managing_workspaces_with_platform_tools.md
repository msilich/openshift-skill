> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-assembly_managing_workspaces_with_platform_tools). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Manage workspaces with OpenShift tools

Manage OpenShift Dev Spaces workspaces with the OpenShift CLI, automatic token injection, and the OpenShift web console.

- **[How workspaces connect to OpenShift](integrate-con_integrating_with_openshift.md)**  
  OpenShift Dev Spaces workspaces connect to OpenShift through automatic token injection, the OpenShift CLI, and console navigation.
- **[Use automatic OpenShift token injection](integrate-proc_automatic_token_injection.md)**  
  Use the OpenShift user token that is automatically injected into workspace containers to run `oc` and `kubectl` commands against the OpenShift cluster without explicit login.
- **[List workspaces from the command line](integrate-proc_listing_all_workspaces.md)**  
  List workspaces from the command line to check their status, identify stopped or failed workspaces, and monitor resource usage across your OpenShift Dev Spaces environment. .Prerequisites
- **[Create a workspace from the command line](integrate-proc_creating_workspaces.md)**  
  Create a workspace from the command line by applying a `DevWorkspace` custom resource to the cluster. Use this method when your workflow does not permit the OpenShift Dev Spaces dashboard.
- **[Stop a workspace from the command line](integrate-proc_stopping_workspaces.md)**  
  Stop a workspace from the command line by setting the `spec.started` field in the `DevWorkspace` custom resource to `false`. .Prerequisites
- **[Start a stopped workspace from the command line](integrate-proc_starting_stopped_workspaces.md)**  
  Start a stopped workspace from the command line by setting the `spec.started` field in the `DevWorkspace` custom resource to `true`. .Prerequisites
- **[Remove a workspace from the command line](integrate-proc_removing_workspaces.md)**  
  Remove a workspace from the command line by deleting its `DevWorkspace` custom resource.
- **[How OpenShift Dev Spaces appears in the OpenShift console](integrate-con_navigating_devspaces_from_openshift_developer_perspective.md)**  
  OpenShift Dev Spaces appears in the OpenShift console through a ConsoleLink Custom Resource that adds an interactive link to the **Red Hat Applications** menu. When the OpenShift Dev Spaces Operator is deployed into OpenShift Container Platform 4.2 and later, it creates a `ConsoleLink` Custom Resource (CR). This adds an interactive link to the **Red Hat Applications** menu for accessing the OpenShift Dev Spaces installation. To access the menu, click the three-by-three matrix icon on the main screen of the OpenShift web console. The OpenShift Dev Spaces **Console Link** creates a new workspace or redirects you to an existing one. For step-by-step instructions, see Additional resources.
- **[Edit application code from the OpenShift Developer Perspective](integrate-proc_editing_code_from_openshift_developer_perspective.md)**  
  Edit the source code of applications running on OpenShift directly from the Developer Perspective to fix and iterate on deployed components without switching tools. .Prerequisites
- **[Access OpenShift Dev Spaces from Red Hat Applications menu](integrate-proc_accessing_devspaces_from_openshift_menu.md)**  
  Access OpenShift Dev Spaces directly from the **Red Hat Applications** menu on OpenShift Container Platform to reach the Dashboard without navigating away from your current OpenShift context. .Prerequisites
- **[Open the OpenShift web console from OpenShift Dev Spaces](integrate-proc_navigating_to_openshift_console.md)**  
  Open the OpenShift web console from the OpenShift Dev Spaces dashboard to manage cluster resources, inspect pods, and troubleshoot workspace issues. .Prerequisites

**Related information**  

- [How the components fit together](discover-con_architecture_overview.md)
- [Daily development workflow](develop-con_developing_with_devspaces.md)
