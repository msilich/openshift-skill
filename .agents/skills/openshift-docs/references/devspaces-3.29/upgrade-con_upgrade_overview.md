> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/upgrade-con_upgrade_overview). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How the upgrade works

Understand what happens during an OpenShift Dev Spaces upgrade so that you can plan the timing, communicate downtime expectations, and verify the result.

When you upgrade OpenShift Dev Spaces, the Operator handles the server component upgrade automatically. You do not need to manually update individual pods or configurations. The Operator:

- Replaces the OpenShift Dev Spaces server, dashboard, gateway, and plugin registry pods with the new version.
- Upgrades the Dev Workspace Operator to the version bundled with the new release.
- Preserves the existing `CheCluster` custom resource configuration.

Running workspaces are not automatically restarted during the upgrade. Developers must stop their workspaces before the upgrade and restart them after the upgrade completes.

<span id="con_upgrade-overview_devspaces___supported_upgrade_path"></span>

## [Supported upgrade path](upgrade-con_upgrade_overview.md#con_upgrade-overview_devspaces___supported_upgrade_path)

OpenShift Dev Spaces supports upgrading from the previous minor version to the current version. For example, upgrading from OpenShift Dev Spaces 3.27 to OpenShift Dev Spaces 3.29.

Direct upgrades that skip minor versions are not supported. If your deployment is more than one minor version behind, upgrade one minor version at a time.

<span id="con_upgrade-overview_devspaces___openshift_version_compatibility"></span>

## [OpenShift version compatibility](upgrade-con_upgrade_overview.md#con_upgrade-overview_devspaces___openshift_version_compatibility)

OpenShift Dev Spaces 3.29 is supported on OpenShift 4.16 through 4.22. Before you upgrade OpenShift Dev Spaces, verify that your OpenShift cluster version is within this range.

<span id="con_upgrade-overview_devspaces___review_the_release_notes"></span>

## [Review the release notes](upgrade-con_upgrade_overview.md#con_upgrade-overview_devspaces___review_the_release_notes)

Review the release notes before upgrading to understand new features, bug fixes, and any changes that might affect your deployment. For the full release notes, see Additional resources.

**Related information**  

- [OpenShift Dev Spaces 3.29 release notes](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/release_notes/)
- [What is OpenShift Dev Spaces](discover-con_what_is_devspaces.md)
