> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/whats_new-ref_known_issues). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Known issues

The following release notes detail the known issues for the Red Hat OpenShift Dev Spaces 3.29 general availability release.

## Workspace startup fails on IBM Z with OpenShift Container Platform 4.22

On IBM Z (s390x) clusters running OpenShift Container Platform 4.22, workspace startup fails with a `FailedPostStartHook` error. This issue affects OpenShift Dev Spaces with DevWorkspace Operator 0.42 on OpenShift Container Platform 4.22. Workspaces start successfully on IBM Z with OpenShift Container Platform 4.16 and 4.21, and on x86_64, arm64, and IBM Power architectures with OpenShift Container Platform 4.22.

**Workaround:** Patch the `DevWorkspaceTemplate` to remove the `postStart` event and add a direct entrypoint command, then restart the workspace.

**Additional resources**

- [CRW-11537](https://redhat.atlassian.net/browse/CRW-11537)

## Workspace terminals do not inherit the logged-in user identity

Workspace terminals use the workspace Pod Service Account identity instead of the logged-in user's OAuth token. Running `oc whoami` in a workspace terminal returns the service account name instead of the expected user identity. CLI commands that require the user's permissions, such as `oc get nodes`, fail with a Forbidden error.

**Workaround:** There is currently no workaround available.

**Additional resources**

- [CRW-11193](https://redhat.atlassian.net/browse/CRW-11193)

## Restarting a workspace fails after disconnecting from a remote JetBrains desktop editor

After closing the connection to a remote JetBrains Ultimate desktop editor, restarting the workspace fails with the error: "The workspace has not received an IDE URL in the last 20 seconds. Try to re-open the workspace."

**Workaround:** There is currently no workaround available.

**Additional resources**

- [CRW-10994](https://redhat.atlassian.net/browse/CRW-10994)

## The C# extension is not available for .NET workspaces on IBM Power and IBM Z

The recommended C# extension (`muhammad-sammy.csharp`) is not available in .NET sample workspaces on IBM Power (ppc64le) and IBM Z (s390x).

**Workaround:** Install version 2.110.4 of the extension manually from open-vsx.org, or patch the CheCluster custom resource to use the embedded plugin registry image from the previous release: `registry.redhat.io/devspaces/pluginregistry-rhel9:3.27.1`.

**Additional resources**

- [CRW-10989](https://redhat.atlassian.net/browse/CRW-10989)

## Workspace backup list is empty for non-administrator users after workspace removal

When logged in as a non-administrator user, the workspace backup list appears empty after removing a workspace.

**Workaround:** Log in with an administrator account to view and manage workspace backups. Alternatively, view the ImageStream resources in the user namespace to identify previous backups.

**Additional resources**

- [CRW-10984](https://redhat.atlassian.net/browse/CRW-10984)

## Podman build fails with a permission denied error on IBM Z with NFS storage

Container builds using Podman fail with a permission denied error in workspaces on IBM Z (s390x) that use NFS or network-attached storage classes.

**Workaround:** Redirect the Podman storage directories to a local path by creating or editing the `~/.config/containers/storage.conf` file in the workspace.

**Additional resources**

- [CRW-10982](https://redhat.atlassian.net/browse/CRW-10982)

## Workspaces using JetBrains Toolbox App (desktop) editor ignore idling timeouts

Workspaces using the desktop version of the JetBrains Toolbox App editor ignore idling timeouts specified by CheCluster properties such as `secondsOfRunBeforeIdling` and `secondsOfInactivityBeforeIdling`. There is currently no workaround available.

**Additional resources**

- [CRW-10624](https://redhat.atlassian.net/browse/CRW-10624)

## SSH connection to workspaces fails when nested containers are enabled

SSH connections to developer workspaces fail when the `disableContainerRunCapabilities` option is set to `false` in the CheCluster custom resource. This affects the VS Code (desktop) and JetBrains remote workflows that connect over SSH.

**Workaround:** Set `disableContainerRunCapabilities` to `true` in the CheCluster custom resource.

**Additional resources**

- [CRW-10545](https://redhat.atlassian.net/browse/CRW-10545)

## Workspaces using Visual Studio Code (desktop) editor ignore idling timeouts

Workspaces using the desktop version of Visual Studio Code editor ignore idling timeouts specified by CheCluster properties such as `secondsOfRunBeforeIdling` and `secondsOfInactivityBeforeIdling`. There is currently no workaround available.

**Additional resources**

- [CRW-9548](https://redhat.atlassian.net/browse/CRW-9548)

## 504 Gateway Time-out error on arm64 with IntelliJ IDEA Ultimate

When starting a workspace using IntelliJ IDEA Ultimate IDE on the arm64 architecture, a "504 Gateway Time-out" error appears. There is no workaround available.

**Additional resources**

- [CRW-9217](https://redhat.atlassian.net/browse/CRW-9217)

## PostStartHook failed error with Ansible sample on arm64

The Ansible sample fails to start on the arm64 architecture with the error: "Error creating DevWorkspace deployment: Detected unrecoverable event FailedPostStartHook: PostStartHook failed." There is no workaround available.

**Additional resources**

- [CRW-9216](https://redhat.atlassian.net/browse/CRW-9216)

## .NET sample fails to start on arm64 architecture

The .NET sample fails to start on the arm64 architecture because there is no `quay.io/devspaces/dotnet-90` image available for arm64. There is no workaround available.

**Additional resources**

- [CRW-9215](https://redhat.atlassian.net/browse/CRW-9215)

## Error when starting a workspace on OpenShift Platform 4.18

When starting a workspace in Dev Spaces deployed to OpenShift Platform 4.18, the following error appears: "Error creating DevWorkspace deployment: Container tools has state ImagePullBackOff".

**Workaround:** Restart the workspace.

**Additional resources**

- [CRW-8361](https://redhat.atlassian.net/browse/CRW-8361)

## JetBrains editors cause workspace startup failure on IBM Power and IBM Z

The downloaded JetBrains IDE binaries are not multi-arch, causing workspace startup to fail on IBM Power and IBM Z architectures. There is currently no workaround available.

**Additional resources**

- [CRW-8296](https://redhat.atlassian.net/browse/CRW-8296)

## Refresh token mode causes cyclic reload of the workspace start page

When experimental refresh token mode is applied using the `CHE_FORCE_REFRESH_PERSONAL_ACCESS_TOKEN` property for the GitHub and Microsoft Azure DevOps OAuth providers, workspace starts reload the dashboard cyclically, creating a new personal access token on each page restart. The refresh token mode works correctly for GitLab and BitBucket OAuth providers.

**Additional resources**

- [CRW-6859](https://redhat.atlassian.net/browse/CRW-6859)
