> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/discover-con_who_is_devspaces_for). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Who is OpenShift Dev Spaces for?

OpenShift Dev Spaces serves two personas: platform administrators who deploy and manage the platform, and developers who use it to write code.

<span id="con_who-is-devspaces-for_devspaces___platform_administrators"></span>

## [Platform administrators](discover-con_who_is_devspaces_for.md#con_who-is-devspaces-for_devspaces___platform_administrators)

Platform administrators install OpenShift Dev Spaces on an OpenShift cluster and manage its lifecycle. Their responsibilities include:

- Deploying the OpenShift Dev Spaces Operator and configuring the `CheCluster` Custom Resource
- Setting up OAuth for Git providers so that developers can access repositories without re-entering credentials
- Managing workspace policies such as idle timeouts, resource limits, and maximum workspaces per user
- Monitoring platform health through Dev Workspace Operator metrics and Grafana dashboards
- Upgrading OpenShift Dev Spaces to new versions

Administrators primarily interact with OpenShift Dev Spaces through the OpenShift web console and the `oc` and `dsc` command-line tools.

<span id="con_who-is-devspaces-for_devspaces___developers"></span>

## [Developers](discover-con_who_is_devspaces_for.md#con_who-is-devspaces-for_devspaces___developers)

Developers receive the OpenShift Dev Spaces dashboard URL from their administrator and use it to create cloud workspaces. Their experience includes:

- Opening a Git repository URL in OpenShift Dev Spaces to launch a workspace with their project code, tools, and dependencies
- Coding in a browser-based IDE (Microsoft Visual Studio Code - Open Source by default) with full terminal access
- Pushing commits, reviewing pull requests, and collaborating with their team from the browser
- Switching between projects by creating multiple workspaces, each isolated in its own container

Developers do not need cluster access, `oc` sessions, or any local tooling beyond a web browser.

<span id="con_who-is-devspaces-for_devspaces___team_sizes_and_deployment_models"></span>

## [Team sizes and deployment models](discover-con_who_is_devspaces_for.md#con_who-is-devspaces-for_devspaces___team_sizes_and_deployment_models)

OpenShift Dev Spaces supports different deployment sizes:

Small teams  
A single OpenShift Dev Spaces instance on a standard OpenShift cluster handles workspace creation, storage, and networking with default settings.

Growing teams  
As usage increases, configure resource quotas, deploy the Image Puller for faster workspace starts, and set up monitoring to track usage patterns.

Enterprise deployments  
For security-sensitive environments, consider air-gapped installations and advanced authorization to restrict platform access by team or group. For very large deployments, see the scalability guidance in the planning documentation.
