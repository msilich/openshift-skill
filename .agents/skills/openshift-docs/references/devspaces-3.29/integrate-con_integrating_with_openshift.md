> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-con_integrating_with_openshift). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How workspaces connect to OpenShift

OpenShift Dev Spaces workspaces connect to OpenShift through automatic token injection, the OpenShift CLI, and console navigation.

Key integration features include:

- Managing workspaces using Kubernetes APIs
- Automatic token injection for cluster access
- Navigating to OpenShift Dev Spaces from the OpenShift Developer Perspective
- Navigating to the OpenShift Web Console from OpenShift Dev Spaces

On your organization’s OpenShift cluster, each OpenShift Dev Spaces workspace is represented as a `DevWorkspace` custom resource of the same name. For example, a workspace named `my-workspace` in the OpenShift Dev Spaces dashboard has a corresponding `DevWorkspace` custom resource in the user’s project. You can manage OpenShift Dev Spaces workspaces by using OpenShift APIs with clients such as the command-line `oc`.

Each `DevWorkspace` custom resource contains details derived from the devfile of the Git repository cloned for the workspace, such as devfile commands and workspace container configurations.
