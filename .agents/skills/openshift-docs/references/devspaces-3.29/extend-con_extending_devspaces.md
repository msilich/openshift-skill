> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-con_extending_devspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# What you can customize in workspace tooling

OpenShift Dev Spaces creates a Cloud Development Environment (CDE) for every project. The dashboard and CLI refer to each CDE as a **workspace**. You can customize every layer of the developer tooling to match your organization’s requirements.

By default, OpenShift Dev Spaces provides:

- Visual Studio Code - Open Source as the workspace editor.
- An embedded Open VSX registry running in the `plugin-registry` pod. This registry contains a curated subset of extensions from the public open-vsx.org registry and supports air-gapped environments.

As a Platform administrator, you can customize the following areas:

<span id="con_extending-devspaces_devspaces__entry__1"></span><span id="con_extending-devspaces_devspaces__entry__2"></span>

| Goal | Description |
|----|----|
| Choose which editors are available | Add custom editor definitions, set the default IDE, hide or restore editors, and host editor binaries internally for air-gapped clusters. |
| Customize the default IDE | Configure multi-root project layout, trusted and default extensions, editor settings, and extension installation policies for Visual Studio Code - Open Source. |
| Add or remove IDE extensions | Change which extensions are available by pointing to a different Open VSX registry, editing workspace devfiles, or using the command line. |
| Deploy a private extension registry | Run an on-premises Open VSX instance for air-gapped environments where workspaces cannot reach the public internet. |

Table 1. What do you need to customize?

**Related information**  

- [Add AI and analytics capabilities](extend-con_ai_and_analytics_capabilities.md)
- [Install OpenShift Dev Spaces](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/installation_guide/index#proc_installing-devspaces-on-openshift-using-cli_installation_guide)
