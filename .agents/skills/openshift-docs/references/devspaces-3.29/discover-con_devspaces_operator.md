> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/discover-con_devspaces_operator). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Operator and lifecycle management

The OpenShift Dev Spaces Operator manages the full lifecycle of OpenShift Dev Spaces server components through the `CheCluster` custom resource. Creating a `CheCluster` CR triggers the Operator to deploy the Dev Workspace Operator, gateway, dashboard, server, and plug-in registry.

`CheCluster` custom resource definition (CRD)  
Defines the `CheCluster` OpenShift object.

OpenShift Dev Spaces controller  
Creates and controls the necessary OpenShift objects to run an OpenShift Dev Spaces instance, such as pods, services, and persistent volumes.

`CheCluster` custom resource (CR)  
On a cluster with the OpenShift Dev Spaces operator, it is possible to create a `CheCluster` custom resource (CR). The OpenShift Dev Spaces operator ensures the full lifecycle management of the OpenShift Dev Spaces server components on this OpenShift Dev Spaces instance. These components include the Dev Workspace Operator, gateway, user dashboard, OpenShift Dev Spaces server, and plug-in registry. The configuration guide in Additional resources documents every field in the `CheCluster` CR, and the install guide walks through initial deployment.

**Related concepts**  

- [Dev Workspace Operator and workspace pods](discover-con_devworkspace_operator.md "The Dev Workspace Operator (DWO) manages workspace pods, services, and persistent volumes by reconciling Dev Workspace custom resources on OpenShift. Every OpenShift Dev Spaces workspace has an underlying Dev Workspace CR that contains the devfile, editor definition, and configuration attributes.")
- [Gateway and request routing](discover-con_gateway.md "The OpenShift Dev Spaces gateway routes requests, authenticates users with OpenID Connect (OIDC), and enforces OpenShift RBAC policies. It controls access to the dashboard, server, plug-in registry, and every user workspace.")
- [Dashboard and workspace management](discover-con_dashboard.md "The user dashboard is the landing page of Red Hat OpenShift Dev Spaces where users create, manage, and access their workspaces. It coordinates with the OpenShift Dev Spaces server, plug-in registry, and OpenShift API to convert devfiles into running workspace pods.")
- [Server and namespace provisioning](discover-con_devspaces_server.md "The OpenShift Dev Spaces server is a Java web service that creates user namespaces, provisions them with secrets and config maps, and integrates with Git service providers for devfile fetching and authentication.")
- [Plug-in registry](discover-con_plugin_registry.md "The OpenShift Dev Spaces plug-in registry provides extensions for the Visual Studio Code editor.")

**Related information**  

- [How the central configuration works](configure-con_understanding_the_checluster_custom_resource.md)
- [Install OpenShift Dev Spaces](install-assembly_installing_dev_spaces.md)
