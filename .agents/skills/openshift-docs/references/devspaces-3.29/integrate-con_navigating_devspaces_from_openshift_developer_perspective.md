> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-con_navigating_devspaces_from_openshift_developer_perspective). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How OpenShift Dev Spaces appears in the OpenShift console

OpenShift Dev Spaces appears in the OpenShift console through a ConsoleLink Custom Resource that adds an interactive link to the **Red Hat Applications** menu. When the OpenShift Dev Spaces Operator is deployed into OpenShift Container Platform 4.2 and later, it creates a `ConsoleLink` Custom Resource (CR). This adds an interactive link to the **Red Hat Applications** menu for accessing the OpenShift Dev Spaces installation. To access the menu, click the three-by-three matrix icon on the main screen of the OpenShift web console. The OpenShift Dev Spaces **Console Link** creates a new workspace or redirects you to an existing one. For step-by-step instructions, see Additional resources.

The console link requires HTTPS. When installing OpenShift Dev Spaces with the **From Git** option, the console link is only created if OpenShift Dev Spaces is deployed with HTTPS.

Starting with OpenShift Container Platform 4.19, the web console perspectives have unified. There is no longer a separate **Developer** perspective in the default view. All OpenShift Container Platform web console features remain discoverable to all users, but you might need to request permission for certain features from the cluster owner. The **Getting Started** pane includes a quick start for enabling the **Developer** perspective if you prefer the previous layout.

**Related tasks**  

- [Edit application code from the OpenShift Developer Perspective](integrate-proc_editing_code_from_openshift_developer_perspective.md "Edit the source code of applications running on OpenShift directly from the Developer Perspective to fix and iterate on deployed components without switching tools. .Prerequisites")
- [Access OpenShift Dev Spaces from Red Hat Applications menu](integrate-proc_accessing_devspaces_from_openshift_menu.md "Access OpenShift Dev Spaces directly from the Red Hat Applications menu on OpenShift Container Platform to reach the Dashboard without navigating away from your current OpenShift context. .Prerequisites")

**Related information**  

- [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/)
