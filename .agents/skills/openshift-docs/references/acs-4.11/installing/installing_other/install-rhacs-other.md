<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) provides security services for self-managed RHACS on platforms such as Amazon Elastic Kubernetes Service (Amazon EKS), Google Kubernetes Engine (Google GKE), and Microsoft Azure Kubernetes Service (Microsoft AKS).

<a id="install-rhacs-other-overview_install-rhacs-other"></a>

# Installation overview

Before installing RHACS on other platforms, review the prerequisites and understand the high-level installation workflow.

Before you install:

- Understand the installation methods for different platforms.

- Understand the RHACS architecture.

- Check the default resource requirements.

The following list provides a high-level overview of installation steps:

1.  Install Central services on a cluster by using Helm charts or the `roxctl` CLI.

2.  Generate and apply a cluster registration secret or an init bundle.

3.  Install secured cluster resources on each of your secured clusters.

<a id="additional-resources-install-rhacs-other_install-rhacs-other"></a>

# Additional resources

- [Installation methods for different platforms](../acs-high-level-overview.md#install-platforms-methods_acs-high-level-overview)

- [Red Hat Advanced Cluster Security for Kubernetes architecture](../../architecture/acs-architecture.md#acs-architecture_acs-architecture)

- [Default resource requirements](../acs-default-requirements.md)

- [Installing Central services](install-central-other.md)

- [Generating cluster registration secrets and init bundles](init-bundle-other.md)

- [Installing secured cluster resources](install-secured-cluster-other.md)
