<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service) provides security services for your Red Hat OpenShift and Kubernetes clusters.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

</div>

<a id="getting-started-prerequisites_getting-started-rhacs-cloud-ocp"></a>

# Prerequisites

Prerequisites for getting started with Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service).

- Ensure that you can access the **Advanced Cluster Security** menu option from the Red Hat Hybrid Cloud Console.

  > [!NOTE]
  > To access the RHACS Cloud Service console, you need your Red Hat Single Sign-On (SSO) credentials, or credentials for another identity provider if that has been configured.

<div>

<div class="title">

Additional resources

</div>

- [Default access to the ACS Console](getting-started-rhacs-cloud-ocp.md#default-access-acs-console_getting-started-rhacs-cloud-ocp)

</div>

<a id="installation-overview-acs-cloud_getting-started-rhacs-cloud-ocp"></a>

# High-level overview of installation steps

Overview of the high-level installation steps for securing Red Hat OpenShift and Kubernetes clusters.

The following sections provide an overview of installation steps and links to the relevant documentation.

<a id="securing-rh-cloud-clusters_getting-started-rhacs-cloud-ocp"></a>

# Securing Red Hat OpenShift clusters

You can secure Red Hat OpenShift clusters by using the RHACS Operator, Helm charts, or the `roxctl` CLI.

<a id="overview-installing-cloud-secured-clusters-osp-operator_getting-started-rhacs-cloud-ocp"></a>

## Securing Red Hat OpenShift clusters by using the Operator

You can secure Red Hat OpenShift clusters by installing the RHACS Operator and using it to deploy secured cluster resources.

<div>

<div class="title">

Procedure

</div>

1.  Verify that the clusters you want to secure meet the default requirements.

2.  In the Red Hat Hybrid Cloud Console, create an ACS Instance.

3.  On each Red Hat OpenShift cluster you want to secure, create a project named `stackrox`. This project will contain the resources for RHACS Cloud Service secured clusters.

4.  Generate a cluster registration secret (CRS) or an init bundle, which contains secrets that are used to establish initial trust between Central and the secured clusters. Using a CRS is the preferred method. Complete only one of the following actions to generate the CRS:

    - In the ACS Console, generate a CRS.

    - Log in to Central and use the `roxctl` CLI to generate a CRS.

5.  On each Red Hat OpenShift cluster, apply the CRS.

6.  On each Red Hat OpenShift cluster, install the RHACS Operator.

7.  On each Red Hat OpenShift cluster, install secured cluster resources in the `stackrox` project by using the Operator.

8.  Verify the installation by ensuring that your secured clusters can communicate with the ACS instance.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Default requirements](acscs-default-requirements.md)

- [Creating an ACS Instance](installing_cloud_ocp/cloud-create-instance-ocp.md)

- [Creating a project named `stackrox`](installing_cloud_ocp/cloud-ocp-create-project.md)

- [Generating a CRS in the ACS Console](installing_cloud_ocp/init-bundle-cloud-ocp-generate.md#portal-generate-init-bundle_init-bundle-cloud-ocp-generate)

- [Generating a CRS by using the roxctl CLI](installing_cloud_ocp/init-bundle-cloud-ocp-generate.md#crs-generate-roxctl_init-bundle-cloud-ocp-generate)

- [Applying the CRS](installing_cloud_ocp/init-bundle-cloud-ocp-apply.md)

- [Installing the RHACS Operator](installing_cloud_ocp/cloud-install-operator.md)

- [Installing secured cluster resources by using the Operator](installing_cloud_ocp/install-secured-cluster-cloud-ocp.md#installing-sc-operator-cloud-ocp_install-secured-cluster-cloud-ocp)

- [Verifying installation](installing_cloud_ocp/verify-installation-cloud-ocp.md)

</div>

<a id="overview-installing-cloud-secured-clusters-osp-helm_getting-started-rhacs-cloud-ocp"></a>

## Securing Red Hat OpenShift clusters by using Helm charts

You can secure Red Hat OpenShift clusters by using Helm charts to install secured cluster resources.

<div>

<div class="title">

Procedure

</div>

1.  Verify that the clusters you want to secure meet the default requirements.

2.  In the Red Hat Hybrid Cloud Console, create an ACS Instance.

3.  On each Red Hat OpenShift cluster you want to secure, create a project named `stackrox`. This project will contain the resources for RHACS Cloud Service secured clusters.

4.  Generate a cluster registration secret (CRS) or an init bundle, which contains secrets that are used to establish initial trust between Central and the secured clusters. Using a CRS is the preferred method. Complete only one of the following actions to generate the CRS:

    - In the ACS Console, generate a CRS. This file contains the secrets that are used to set up the initial secured communication between RHACS Cloud Service secured clusters and Central.

    - Log in to Central and use the `roxctl` CLI to generate a CRS.

5.  On each Red Hat OpenShift cluster, run the `helm install` command to install RHACS by using Helm charts, specifying the path of the CRS.

6.  Verify the installation by ensuring that your secured clusters can communicate with the ACS instance.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Default requirements](acscs-default-requirements.md)

- [Creating an ACS Instance](installing_cloud_ocp/cloud-create-instance-ocp.md)

- [Creating a project named `stackrox`](installing_cloud_ocp/cloud-ocp-create-project.md)

- [Generating a CRS in the ACS Console](installing_cloud_ocp/init-bundle-cloud-ocp-generate.md#portal-generate-init-bundle_init-bundle-cloud-ocp-generate)

- [Generating a CRS by using the roxctl CLI](installing_cloud_ocp/init-bundle-cloud-ocp-generate.md#crs-generate-roxctl_init-bundle-cloud-ocp-generate)

- [Installing RHACS by using Helm charts](installing_cloud_ocp/install-secured-cluster-cloud-ocp.md#installing-sc-helm-cloud-ocp_install-secured-cluster-cloud-ocp)

- [Verifying installation](installing_cloud_ocp/verify-installation-cloud-ocp.md)

</div>

<a id="overview-installing-cloud-secured-clusters-osp-roxctl_getting-started-rhacs-cloud-ocp"></a>

## Securing Red Hat OpenShift clusters by using the roxctl CLI, also called the manifest method

You can secure Red Hat OpenShift clusters by using the `roxctl` CLI to generate and apply manifests for secured cluster resources.

<div>

<div class="title">

Procedure

</div>

1.  Verify that the clusters you want to secure meet the default requirements.

2.  In the Red Hat Hybrid Cloud Console, create an ACS Instance.

3.  On each Red Hat OpenShift cluster you want to secure, create a project named `stackrox`. This project will contain the resources for RHACS Cloud Service secured clusters.

4.  Complete only one of the following steps:

    - In the ACS Console, use the legacy installation method to generate a cluster bundle.

    - From a system that has access to the monitored cluster, generate the configuration and extract and run the sensor script from the cluster bundle.

5.  Verify the installation by ensuring that your secured clusters can communicate with the ACS instance.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Default requirements](acscs-default-requirements.md)

- [Creating an ACS Instance](installing_cloud_ocp/cloud-create-instance-ocp.md)

- [Creating a project named `stackrox`](installing_cloud_ocp/cloud-ocp-create-project.md)

- [Installing secured clusters by using the roxctl CLI](installing_cloud_ocp/install-secured-cluster-cloud-ocp.md)

- [Verifying installation](installing_cloud_ocp/verify-installation-cloud-ocp.md)

</div>

<a id="securing-kubernetes-clusters_getting-started-rhacs-cloud-ocp"></a>

# Securing Kubernetes clusters

You can secure Kubernetes clusters by using Helm charts or the `roxctl` CLI.

<a id="overview-installing-cloud-secured-clusters-kube-helm_getting-started-rhacs-cloud-ocp"></a>

## Securing Kubernetes clusters by using Helm charts

You can secure Kubernetes clusters by using Helm charts to install secured cluster resources.

<div>

<div class="title">

Procedure

</div>

1.  Verify that the clusters you want to secure meet the default requirements.

2.  In the Red Hat Hybrid Cloud Console, create an ACS Instance.

3.  Generate a cluster registration secret (CRS) or an init bundle, which has secrets. RHACS uses these secrets to establish initial trust between Central and the secured clusters. Using a CRS is the preferred method. Complete only one of the following actions to generate the CRS:

    - In the ACS Console, generate a CRS. This file contains the secrets that are used to set up the initial secured communication between RHACS Cloud Service secured clusters and Central.

    - Log in to Central and use the `roxctl` CLI to generate a CRS.

4.  On each Kubernetes cluster, run the `helm install` command to install RHACS by using Helm charts, specifying the path of the CRS.

5.  Verify the installation by ensuring that your secured clusters can communicate with the ACS instance.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Default requirements](acscs-default-requirements.md)

- [Creating an ACS Instance](installing_cloud_other/cloud-create-instance-other.md)

- [Generating a CRS in the ACS Console](installing_cloud_other/init-bundle-cloud-other-generate.md#portal-generate-init-bundle_init-bundle-cloud-other-generate)

- [Generating a CRS by using the roxctl CLI](installing_cloud_other/init-bundle-cloud-other-generate.md#crs-generate-roxctl_init-bundle-cloud-other-generate)

- [Installing by using Helm charts](installing_cloud_other/install-secured-cluster-cloud-other.md)

- [Verifying installation](installing_cloud_other/verify-installation-cloud-other.md)

</div>

<a id="overview-installing-cloud-secured-clusters-kube-roxctl_getting-started-rhacs-cloud-ocp"></a>

## Securing Kubernetes clusters by using the roxctl CLI, also called the manifest method

You can secure Kubernetes clusters by using the `roxctl` CLI to generate and apply manifests for secured cluster resources.

<div>

<div class="title">

Procedure

</div>

1.  Verify that the clusters you want to secure meet the default requirements.

2.  In the Red Hat Hybrid Cloud Console, create an ACS Instance.

3.  On each cluster you want to secure, create a namespace named `stackrox`. This namespace will contain the resources for RHACS Cloud Service secured clusters.

4.  Complete only one of the following steps:

    - In the ACS Console, use the legacy installation method to generate a cluster bundle.

    - From a system that has access to the monitored cluster, generate the configuration and extract and run the sensor script from the cluster bundle.

5.  Verify the installation by ensuring that your secured clusters can communicate with the ACS instance.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Default requirements](acscs-default-requirements.md)

- [Creating an ACS Instance](installing_cloud_other/cloud-create-instance-other.md)

- [Installing secured clusters by using the roxctl CLI](installing_cloud_other/install-secured-cluster-cloud-other.md)

- [Generating configuration and running the sensor script](installing_cloud_ocp/install-secured-cluster-cloud-ocp.md)

- [Verifying installation](installing_cloud_ocp/verify-installation-cloud-ocp.md)

</div>

<a id="default-access-acs-console_getting-started-rhacs-cloud-ocp"></a>

# Default access to the ACS Console

By default, the authentication mechanism available to users is authentication by using Red Hat Single Sign-On (SSO). You cannot delete or change the Red Hat SSO authentication provider, but you can change the minimum access role and add additional rules, or add another identity provider.

> [!NOTE]
> To learn how authentication providers work in ACS, see "Understanding authentication providers".

RHACS Cloud Service creates a dedicated OIDC client of `sso.redhat.com` for each ACS Console. All OIDC clients share the same `sso.redhat.com` realm. RHACS Cloud Service maps claims from the token issued by `sso.redhat.com` to an ACS-issued token as follows:

- `realm_access.roles` to `groups`

- `org_id` to `rh_org_id`

- `is_org_admin` to `rh_is_org_admin`

- `sub` to `userid`

The built-in Red Hat SSO authentication provider has the required attribute `rh_org_id` set to the organization ID assigned to account of the user who created the RHACS Cloud Service instance. This is the organizational account ID. Only users from the same organizational account can access the ACS Console by using the Red Hat SSO authentication provider.

> [!NOTE]
> To gain more control over access to your ACS Console, configure another identity provider instead of relying on the Red Hat SSO authentication provider. For more information, see "Understanding authentication providers". To configure another authentication provider to be the first authentication option on the login page, its name should be lexicographically smaller than `Red Hat SSO`.

By default, the minimum access role is `None`. Assigning a different value to this field gives access to the RHACS Cloud Service instance to all users with the same organizational account.

The built-in Red Hat SSO authentication provider sets up other rules that include the following:

- Rule mapping your `userid` to `Admin`

- Rules mapping administrators of the organization to `Admin`

You can add more rules to grant access to the ACS Console to someone else with the same organizational account. For example, you can use `email` as a key.

<div>

<div class="title">

Additional resources

</div>

- [Understanding authentication providers](../operating/manage-user-access/understanding-authentication-providers.md)

- [Authentication provider structure](../operating/manage-user-access/understanding-authentication-providers.md)

</div>
