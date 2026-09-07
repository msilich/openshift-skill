> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/discover-con_cloud_vs_local_development). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# When to use OpenShift Dev Spaces

OpenShift Dev Spaces is designed for teams that need consistent, secure, and centrally managed development environments on OpenShift. Not every team requires a cloud development platform, so evaluate your development workflow against the use cases below.

<span id="con_cloud-vs-local-development_devspaces___teams_that_benefit_from_openshift_dev_spaces"></span>

## [Teams that benefit from OpenShift Dev Spaces](discover-con_cloud_vs_local_development.md#con_cloud-vs-local-development_devspaces___teams_that_benefit_from_openshift_dev_spaces)

OpenShift Dev Spaces is a strong fit when your team faces one or more of these situations:

- New developers join regularly and need to be productive on day one.
- Builds fail because of differences between developer machines.
- Your organization requires credentials to stay on cluster infrastructure, not on individual machines.
- Development must happen within a controlled network boundary, including air-gapped environments.
- Projects have complex dependency chains that are difficult to reproduce consistently across developer machines.

<span id="con_cloud-vs-local-development_devspaces___what_openshift_dev_spaces_provides_for_the_enterprise"></span>

## [What OpenShift Dev Spaces provides for the enterprise](discover-con_cloud_vs_local_development.md#con_cloud-vs-local-development_devspaces___what_openshift_dev_spaces_provides_for_the_enterprise)

On-premises control  
OpenShift Dev Spaces runs within your OpenShift cluster. When deployed on-premises, your source code and credentials stay within your own infrastructure.

Air-gapped deployment  
OpenShift Dev Spaces operates in disconnected environments with mirrored container images and internal extension registries.

Native OpenShift integration  
OpenShift Dev Spaces uses OpenShift RBAC, OAuth, networking, and storage directly. No additional identity or access management layer is required.

Open devfile standard  
Workspace definitions use the devfile format, an open standard maintained by the devfile.io community. The community site in Additional resources includes the devfile specification, sample devfiles, and tools for authoring workspace definitions.

<span id="con_cloud-vs-local-development_devspaces___what_developers_need_to_work_with_openshift_dev_spaces"></span>

## [What developers need to work with OpenShift Dev Spaces](discover-con_cloud_vs_local_development.md#con_cloud-vs-local-development_devspaces___what_developers_need_to_work_with_openshift_dev_spaces)

Developers need a supported web browser and network access to the OpenShift Dev Spaces dashboard URL. No local tools, CLI installations, or cluster credentials are required.

**Related information**  

- [Devfile.io community](https://devfile.io)
