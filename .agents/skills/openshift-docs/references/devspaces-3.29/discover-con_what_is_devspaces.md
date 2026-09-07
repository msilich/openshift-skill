> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/discover-con_what_is_devspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# What is OpenShift Dev Spaces?

Evaluate OpenShift Dev Spaces as a cloud development platform that delivers container-based, reproducible workspaces on OpenShift to accelerate developer onboarding and reduce environment inconsistencies.

Red Hat OpenShift Dev Spaces is an OpenShift-native platform that provides Cloud Development Environments (CDEs) to development teams. OpenShift Dev Spaces creates a CDE for your project. The dashboard and CLI refer to each CDE as a **workspace**. Instead of configuring local machines, developers get on-demand workspaces: container-based environments with all the tools, dependencies, and IDE access needed to code, build, test, and debug applications.

<span id="con_what-is-devspaces_devspaces___core_goals"></span>

## [Core goals](discover-con_what_is_devspaces.md#con_what-is-devspaces_devspaces___core_goals)

OpenShift Dev Spaces addresses three fundamental challenges in enterprise software development:

Accelerate project and developer onboarding  
As a zero-install development environment accessible through a browser or desktop IDE, OpenShift Dev Spaces enables anyone to join a team and contribute to a project within minutes rather than hours or days of local setup.

Remove inconsistency between developer environments  
Every developer works in the same container-based environment defined by a devfile. Code behaves identically across all team members' workspaces, removing "works on my machine" issues.

Provide built-in security and enterprise readiness  
OpenShift Dev Spaces keeps source code on the cluster rather than on individual workstations, supports role-based access control through OpenShift RBAC, and integrates with enterprise identity providers through OIDC authentication.

<span id="con_what-is-devspaces_devspaces___what_openshift_dev_spaces_provides"></span>

## [What OpenShift Dev Spaces provides](discover-con_what_is_devspaces.md#con_what-is-devspaces_devspaces___what_openshift_dev_spaces_provides)

Workspaces  
Container-based developer workspaces running as OpenShift Pods that provide all the tools and dependencies needed for development. Each workspace is isolated, reproducible, and defined by a devfile.

Browser-based and desktop IDEs  
Microsoft Visual Studio Code - Open Source runs in the browser by default. JetBrains IntelliJ IDEA connects through JetBrains Gateway for a native desktop experience.

Extensible platform  
Customize workspaces through devfiles and Visual Studio Code extensions from Open VSX registries. Platform engineers define standardized environments that developers consume without manual configuration.

AI coding assistants  
Platform administrators configure AI providers centrally through the `CheCluster` custom resource. Developers access AI-powered code completion and chat in their workspace IDE without managing API keys individually. Air-gapped deployments can connect to self-hosted models.

Enterprise integration  
OpenShift-native deployment through an Operator, OIDC authentication, OpenShift RBAC for access control, and integration with Prometheus for monitoring.

<span id="con_what-is-devspaces_devspaces___workspace_model"></span>

## [Workspace model](discover-con_what_is_devspaces.md#con_what-is-devspaces_devspaces___workspace_model)

OpenShift Dev Spaces defines a workspace as the project source code together with all dependencies necessary to edit, build, run, and debug it. The IDE and development runtime are treated as workspace dependencies, embedded and always included. This differentiates OpenShift Dev Spaces from traditional development environments where the IDE is bound to a workstation and runtimes are configured locally.

OpenShift Dev Spaces workspaces are OpenShift Pods that replicate application runtimes used in production and provide a development layer on top: intelligent code completion, debugging, and IDE tools. Workspaces are isolated from one another and manage the lifecycle of their own components. Additional resources describes the architecture that delivers these workspaces, the server deployments that manage multi-tenancy, and the internal structure of each workspace pod.

**Related concepts**  

- [OpenShift Dev Spaces architecture](discover-con_architecture_overview.md "OpenShift Dev Spaces connects three groups of components through Dev Workspace custom resources on OpenShift: server components, the Dev Workspace Operator, and user workspaces. OpenShift RBAC controls access to all resources.")
- [What runs on your cluster](discover-con_server_components.md "Your cluster runs four OpenShift Dev Spaces server deployments that manage multi-tenancy and workspace lifecycle.")
- [What developers get in a workspace](discover-con_user_workspaces.md "Developers get browser-based IDEs running in OpenShift containers, with on-demand access to editors, language servers, debugging tools, and application runtimes without local setup.")
