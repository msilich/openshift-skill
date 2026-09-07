> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/get_started-ref_what_to_configure_next). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# What to configure next

After verifying the platform and configuring Git access, continue with these configuration tasks based on your organization’s priorities.

<span id="ref_what-to-configure-next_devspaces__entry__1"></span><span id="ref_what-to-configure-next_devspaces__entry__2"></span><span id="ref_what-to-configure-next_devspaces__entry__3"></span>

| Priority | Task | Guide |
|----|----|----|
| Recommended | Speed up workspace starts by pre-caching container images on cluster nodes. | [Speed up workspace starts with image caching](optimize-assembly_caching_images_for_faster_workspace_start.md) |
| Recommended | Configure workspace resource limits, idle timeouts, and the number of workspaces per user. | [Set workspace policies for all users](configure-assembly_configuring_workspaces_globally.md) |
| Recommended | Configure OAuth for additional Git providers (GitLab, Bitbucket, Azure DevOps). | [Connect Git providers with OAuth](integrate-assembly_connecting_git_providers_with_oauth.md) |
| As needed | Control access to OpenShift Dev Spaces with role-based access control and Security Context Constraints. | [Control access to OpenShift Dev Spaces](secure-assembly_managing_identities_and_authorizations.md) |
| As needed | Customize the `CheCluster` custom resource to change OpenShift Dev Spaces behavior. | [Customize the central configuration](configure-assembly_configuring_the_checluster_custom_resource.md) |
| As needed | Connect OpenShift Dev Spaces to artifact registries and package managers. | [Connect workspaces to your organization’s package registries](integrate-assembly_connecting_package_registries.md) |

Table 1. Post-installation configuration tasks

Share the OpenShift Dev Spaces dashboard URL with your developers. They can find their first-day instructions in the [Get started as a developer](get_started-assembly_start_your_first_workspace.md) guide.
