<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can organize workloads into isolated projects and streamline your application lifecycle by using the web console or command-line interface (CLI) to create, manage, and deploy applications in OpenShift Container Platform.

# Working on a project

Manage the complete lifecycle of isolated projects, from initial provisioning to user access control, to securely organize applications across your cluster.

After you create the project, you can grant or revoke access to a project and manage cluster roles for the users. You can also edit the project configuration resource while creating a project template that is used for automatic provisioning of new projects.

Using the CLI, you can create a project as a different user by impersonating a request to the OpenShift Container Platform API. When you make a request to create a new project, the OpenShift Container Platform uses an endpoint to provision the project according to a customizable template. As a cluster administrator, you can choose to prevent an authenticated user group from self-provisioning new projects.

# Working on an application

Manage your complete application lifecycle by creating, maintaining, and deploying software by using the web console, CLI, or Operators to optimize cluster resources and minimize downtime.

Creating an application
To create applications, you must have created a project or have access to a project with the appropriate roles and permissions. You can create an application by using either installed Operators, or the OpenShift CLI (`oc`). You can source the applications to be added to the project from Git, JAR files, devfiles, or the developer catalog.

You can also use components that include source or binary code, images, and templates to create an application by using the OpenShift CLI (`oc`). With the OpenShift Container Platform web console, you can create an application from an Operator installed by a cluster administrator.

Maintaining an application
After you create the application, you can use the web console to monitor your project or application metrics. You can also edit or delete the application using the web console.

When the application is running, not all application resources are used. As a cluster administrator, you can choose to idle these scalable resources to reduce resource consumption.

Deploying an application
You can deploy your application using `Deployment` or `DeploymentConfig` objects and manage them from the web console. You can create deployment strategies that help reduce downtime during a change or an upgrade to the application.

You can also use Helm, a software package manager that simplifies deployment of applications and services to OpenShift Container Platform clusters.

# Additional resources

- [Working with projects](projects/working-with-projects.md#working-with-projects)

- [Customizing the available cluster roles using the web console](projects/working-with-projects.md#odc-customizing-available-cluster-roles-using-the-web-console_projects)

- [Configuring project creation](projects/configuring-project-creation.md#configuring-project-creation)

- [Creating a project as a another user](projects/creating-project-other-user.md#creating-project-other-user)

- [Disabling project self-provisioning](projects/configuring-project-creation.md#disabling-project-self-provisioning_configuring-project-creation)

- [Creating applications from installed Operators](creating_applications/creating-apps-from-installed-operators.md#creating-apps-from-installed-operators)

- [Creating applications by using the CLI](creating_applications/creating-applications-using-cli.md#creating-applications-using-cli)

- [Understanding deployments](deployments/what-deployments-are.md#what-deployments-are)

- [Managing deployment processes](deployments/managing-deployment-processes.md#deployment-operations)

- [Using deployment strategies](deployments/deployment-strategies.md#deployment-strategies)

- [Idling applications](idling-applications.md#idling-applications)

- [Understanding Helm](working_with_helm_charts/understanding-helm.md#understanding-helm)
