> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/discover-assembly_architecture). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How OpenShift Dev Spaces works

OpenShift Dev Spaces delivers cloud development environments through three groups of components: server components that manage multi-tenancy, the Dev Workspace Operator that provisions workspace pods, and user workspaces where developers write code.

<span id="assembly_architecture_devspaces___what_happens_when_a_developer_starts_a_workspace"></span>

## [What happens when a developer starts a workspace](discover-assembly_architecture.md#assembly_architecture_devspaces___what_happens_when_a_developer_starts_a_workspace)

1.  The developer selects a Git repository in the **dashboard** and clicks **Create & Open**.
2.  The **Dev Spaces server** resolves the devfile from the repository, selects the editor, and creates a DevWorkspace custom resource in the developer's namespace.
3.  The **Dev Workspace Operator** reconciles the custom resource into a running pod with the specified containers, persistent storage, and injected credentials.
4.  The **gateway** authenticates the developer's session and routes browser traffic to the IDE running inside the workspace pod.

This sequence completes in under 60 seconds for cached images. The developer gets a full IDE with terminal access, language support, and direct access to the OpenShift cluster API.

<span id="assembly_architecture_devspaces___three_component_groups"></span>

## [Three component groups](discover-assembly_architecture.md#assembly_architecture_devspaces___three_component_groups)

All components run in the `openshift-devspaces` namespace. They divide into three groups with distinct responsibilities:

Server components  
Four long-lived deployments that serve all users: the Traefik-based gateway, the developer dashboard, the Dev Spaces server, and the plug-in registry. These handle authentication, workspace orchestration, and traffic routing.

Dev Workspace Operator  
A Kubernetes operator that translates DevWorkspace custom resources into running pods. It manages container images, persistent volumes, Secrets injection, and network policies. The operator runs independently and can serve multiple Dev Spaces installations on the same cluster.

User workspaces  
One pod per developer session, running in a per-user namespace. Each workspace contains the IDE process, project source code, language servers, and any sidecar containers defined in the devfile. OpenShift RBAC isolates workspaces between users.

<span id="assembly_architecture_devspaces___how_updates_are_delivered"></span>

## [How updates are delivered](discover-assembly_architecture.md#assembly_architecture_devspaces___how_updates_are_delivered)

The Dev Spaces Operator installs through the Operator Lifecycle Manager (OLM). When a new version becomes available on the update channel, OLM replaces the operator pod. The operator then reconciles the CheCluster custom resource and rolls out updated server components without manual intervention or workspace downtime.

- **[OpenShift Dev Spaces architecture](discover-con_architecture_overview.md)**  
  OpenShift Dev Spaces connects three groups of components through Dev Workspace custom resources on OpenShift: server components, the Dev Workspace Operator, and user workspaces. OpenShift RBAC controls access to all resources.
- **[What runs on your cluster](discover-con_server_components.md)**  
  Your cluster runs four OpenShift Dev Spaces server deployments that manage multi-tenancy and workspace lifecycle.
- **[Operator and lifecycle management](discover-con_devspaces_operator.md)**  
  The OpenShift Dev Spaces Operator manages the full lifecycle of OpenShift Dev Spaces server components through the `CheCluster` custom resource. Creating a `CheCluster` CR triggers the Operator to deploy the Dev Workspace Operator, gateway, dashboard, server, and plug-in registry.
- **[Dev Workspace Operator and workspace pods](discover-con_devworkspace_operator.md)**  
  The Dev Workspace Operator (DWO) manages workspace pods, services, and persistent volumes by reconciling Dev Workspace custom resources on OpenShift. Every OpenShift Dev Spaces workspace has an underlying Dev Workspace CR that contains the devfile, editor definition, and configuration attributes.
- **[Gateway and request routing](discover-con_gateway.md)**  
  The OpenShift Dev Spaces gateway routes requests, authenticates users with OpenID Connect (OIDC), and enforces OpenShift RBAC policies. It controls access to the dashboard, server, plug-in registry, and every user workspace.
- **[Dashboard and workspace management](discover-con_dashboard.md)**  
  The user dashboard is the landing page of Red Hat OpenShift Dev Spaces where users create, manage, and access their workspaces. It coordinates with the OpenShift Dev Spaces server, plug-in registry, and OpenShift API to convert devfiles into running workspace pods.
- **[Server and namespace provisioning](discover-con_devspaces_server.md)**  
  The OpenShift Dev Spaces server is a Java web service that creates user namespaces, provisions them with secrets and config maps, and integrates with Git service providers for devfile fetching and authentication.
- **[Plug-in registry](discover-con_plugin_registry.md)**  
  The OpenShift Dev Spaces plug-in registry provides extensions for the Visual Studio Code editor.
- **[What developers get in a workspace](discover-con_user_workspaces.md)**  
  Developers get browser-based IDEs running in OpenShift containers, with on-demand access to editors, language servers, debugging tools, and application runtimes without local setup.
