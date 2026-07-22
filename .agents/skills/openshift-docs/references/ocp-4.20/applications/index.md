<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Using OpenShift Container Platform, you can create, edit, delete, and manage applications using the web console or command-line interface (CLI).

# Working on a project

Using projects, you can organize and manage applications in isolation. You can manage the entire project lifecycle, including [creating, viewing, and deleting a project](projects/working-with-projects.md#working-with-projects) in OpenShift Container Platform.

After you create the project, you can [grant or revoke access to a project](projects/working-with-projects.md#odc-providing-project-permissions-using-developer-perspective_projects) and [manage cluster roles](projects/working-with-projects.md#odc-customizing-available-cluster-roles-using-the-web-console_projects) for the users using the Developer perspective. You can also [edit the project configuration resource](projects/configuring-project-creation.md#configuring-project-creation) while creating a project template that is used for automatic provisioning of new projects.

Using the CLI, you can [create a project as a different user](projects/creating-project-other-user.md#creating-project-other-user) by impersonating a request to the OpenShift Container Platform API. When you make a request to create a new project, the OpenShift Container Platform uses an endpoint to provision the project according to a customizable template. As a cluster administrator, you can choose to [prevent an authenticated user group from self-provisioning new projects](projects/configuring-project-creation.md#disabling-project-self-provisioning_configuring-project-creation).

# Working on an application

## Creating an application

To create applications, you must have created a project or have access to a project with the appropriate roles and permissions. You can create an application by using either [the Developer perspective in the web console](creating_applications/odc-creating-applications-using-developer-perspective.md#odc-creating-applications-using-developer-perspective), [installed Operators](creating_applications/creating-apps-from-installed-operators.md#creating-apps-from-installed-operators), or [the OpenShift CLI (`oc`)](creating_applications/creating-applications-using-cli.md#creating-applications-using-cli). You can source the applications to be added to the project from Git, JAR files, devfiles, or the developer catalog.

You can also use components that include source or binary code, images, and templates to create an application by using the OpenShift CLI (`oc`). With the OpenShift Container Platform web console, you can create an application from an Operator installed by a cluster administrator.

## Maintaining an application

After you create the application, you can use the web console to [monitor your project or application metrics](odc-monitoring-project-and-application-metrics-using-developer-perspective.md#odc-monitoring-project-and-application-metrics-using-developer-perspective). You can also [edit](odc-editing-applications.md#odc-editing-applications) or [delete](odc-deleting-applications.md#odc-deleting-applications) the application using the web console.

When the application is running, not all applications resources are used. As a cluster administrator, you can choose to [idle these scalable resources](idling-applications.md#idling-applications) to reduce resource consumption.

## Deploying an application

You can deploy your application using [`Deployment` or `DeploymentConfig`](deployments/what-deployments-are.md#what-deployments-are) objects and [manage](deployments/managing-deployment-processes.md#deployment-operations) them from the web console. You can create [deployment strategies](deployments/deployment-strategies.md#deployment-strategies) that help reduce downtime during a change or an upgrade to the application.

You can also use [Helm](working_with_helm_charts/understanding-helm.md#understanding-helm), a software package manager that simplifies deployment of applications and services to OpenShift Container Platform clusters.
