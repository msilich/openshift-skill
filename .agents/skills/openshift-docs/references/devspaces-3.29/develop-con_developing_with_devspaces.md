> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-con_developing_with_devspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# What you can do in a Cloud Development Environment

OpenShift Dev Spaces Cloud Development Environments provide a complete, pre-configured development setup defined by a devfile in your Git repository. You can mount credentials, run containers, persist data, and collaborate with your team.

**How devfiles define your environment**

A `devfile.yaml` in your Git repository specifies container images, commands, endpoints, and volume mounts for your Cloud Development Environment. Devfile components map to containers in the workspace pod. When no devfile is present, OpenShift Dev Spaces uses the Universal Developer Image (UDI) with common language runtimes and tools pre-installed.

**How credentials are injected**

OpenShift Secrets and ConfigMaps with specific labels are automatically mounted into all workspace containers by the Dev Workspace Controller. Git credentials, SSH keys, Maven settings, and API keys are injected without manual setup per Cloud Development Environment.

**How storage works**

Cloud Development Environment data is ephemeral by default and lost when the workspace stops. To persist data across restarts, request a PersistentVolume through a `volume` component in the devfile or apply a PersistentVolumeClaim (PVC) directly. Backup snapshots can restore uncommitted changes after a workspace is deleted.

**Your development workflow**

A typical development session follows this cycle: start a Cloud Development Environment from a Git URL, write and test code, commit changes, and stop the workspace. Data in `/projects` persists across restarts when using per-user storage. When you delete a workspace, backup snapshots preserve uncommitted work.

Tip

Before starting your daily workflow, set up your IDE and AI tools. For IDE and AI tool setup, see Additional resources.

<span id="con_developing-with-devspaces_devspaces__entry__1"></span><span id="con_developing-with-devspaces_devspaces__entry__2"></span>

| Goal | Description |
|----|----|
| Manage credentials and configurations | Mount Secrets, ConfigMaps, SSH keys, and Git configuration so that tools authenticate automatically. |
| Run containers in your Cloud Development Environment | Use fuse-overlayfs for Podman and Buildah, or kubedock for lightweight container execution. |
| Collaborate with your team | Add factory badges for contributors, review pull requests in cloud workspaces, and integrate with GitHub Actions. |
| Persist and restore workspace data | Request persistent storage in devfiles or PVCs, and restore Cloud Development Environments from backup snapshots. |
| Prevent workspace idling | Keep long-running commands active so that unattended tasks complete without interruption. |
| URL parameter reference | Customize Cloud Development Environment creation by appending parameters to the workspace start URL. |

Table 1. What do you need to do?

**Related information**  

- [Your first-day experience](get_started-con_your_first_workspace.md)
- [Choose and configure your IDE](develop-assembly_choosing_your_ide.md)
- [Connect workspaces to your organization’s package registries](integrate-assembly_connecting_package_registries.md)
