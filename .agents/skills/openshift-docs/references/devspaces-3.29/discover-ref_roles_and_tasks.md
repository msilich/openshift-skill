> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/discover-ref_roles_and_tasks). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Common user roles and tasks

OpenShift Dev Spaces documentation is written for specific user roles. Each guide and procedure identifies its intended audience so that you can find the content relevant to your responsibilities.

<span id="ref_roles-and-tasks_devspaces___platform_administrator_tasks_and_guides"></span>

## [Platform administrator tasks and guides](discover-ref_roles_and_tasks.md#ref_roles-and-tasks_devspaces___platform_administrator_tasks_and_guides)

Platform administrators deploy, configure, secure, upgrade, and monitor OpenShift Dev Spaces on OpenShift clusters. They manage the Operator, the `CheCluster` custom resource, and the platform infrastructure that developers use.

Common tasks include:

- Deploy OpenShift Dev Spaces on a cluster. See [Install Red Hat OpenShift Dev Spaces](install-assembly_installing_dev_spaces.md).
- Configure the `CheCluster` custom resource. See [Customize the central configuration](configure-assembly_configuring_the_checluster_custom_resource.md).
- Set up OAuth for Git providers. See [Connect Git providers with OAuth](integrate-assembly_connecting_git_providers_with_oauth.md).
- Control workspace start times with image caching. See [Speed up workspace starts with image caching](optimize-assembly_caching_images_for_faster_workspace_start.md).
- Upgrade to the latest version. See [Upgrade from the web console](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/upgrade/index#assembly_upgrading-dev-spaces-using-web-console_upgrade).
- Monitor metrics and logs. See [Monitor platform health](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/observe_monitor/index#monitor-platform-health_observe_monitor).

<span id="ref_roles-and-tasks_devspaces___developer_tasks_and_guides"></span>

## [Developer tasks and guides](discover-ref_roles_and_tasks.md#ref_roles-and-tasks_devspaces___developer_tasks_and_guides)

Developers create workspaces, write code, use IDE extensions, and integrate with Git repositories. They consume the cloud development environments that platform administrators provide.

Common tasks include:

- Create a workspace from a Git repository. See [Start a workspace from a Git repository URL](get_started-proc_starting_a_workspace_from_a_git_repository_url.md).
- Authenticate to Git servers. See [Authenticate to Git servers](get_started-assembly_authenticate_to_git_servers.md).
- Install and manage IDE extensions. See [Automate installation of Visual Studio Code extensions](develop-proc_automating_installation_of_vscode_extensions.md).
- Use devfiles to define workspace configuration. See [Introduction to devfiles](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop/index#devfile-introduction_develop).
