> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/upgrade-proc_upgrading_dev_spaces_in_a_restricted_environment). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Upgrade in an air-gapped environment

Upgrade OpenShift Dev Spaces on a cluster with no internet access by mirroring updated container images and Operator catalogs to your private registry before running the upgrade.

## Before you begin

- You have the OpenShift Dev Spaces instance installed on OpenShift using the `dsc --installer operator` method in the `openshift-devspaces` project. See [Install OpenShift Dev Spaces in a restricted environment](install-proc_installing_dev_spaces_in_a_restricted_environment_on_openshift.md).
- You have an OpenShift cluster with at least 64 GB of disk space.
- You have an OpenShift cluster ready to operate on a restricted network. See [About disconnected installation mirroring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/installing-mirroring-disconnected-about) and [Using Operator Lifecycle Manager on restricted networks](https://docs.openshift.com/container-platform/4.22/operators/admin/olm-restricted-networks.html).
- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have an active `oc registry` session to the `registry.redhat.io` Red Hat Ecosystem Catalog. See [Red Hat Container Registry authentication](https://access.redhat.com/RegistryAuthentication).
- You have the following tools installed: `opm` (see [Installing the `opm` CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/opm/cli-opm-install.html)), `jq` (see [Downloading `jq`](https://stedolan.github.io/jq/download/)), `podman` (see [Podman Installation Instructions](https://podman.io/docs/installation)), and `skopeo` version 1.6 or higher (see [Installing Skopeo](https://github.com/containers/skopeo/blob/main/install.md)).
- You have an active `skopeo` session with administrative access to the private Docker registry. [Authenticating to a registry](https://github.com/containers/skopeo#authenticating-to-a-registry), and [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/installing-mirroring-disconnected-about).
- You have `dsc` for OpenShift Dev Spaces version 3.29 installed. See [Installing the dsc management tool](plan-proc_installing_the_dsc_management_tool.md).

## Procedure

1.  Download and execute the mirroring script to install a custom Operator catalog and mirror the related images: [prepare-restricted-environment.sh](https://raw.githubusercontent.com/eclipse-che/che-docs/main/modules/administration-guide/attachments/restricted-environment/prepare-restricted-environment.sh).

    ``` bash
    $ bash prepare-restricted-environment.sh \
      --devworkspace_operator_index registry.redhat.io/redhat/redhat-operator-index:v4.22\
      --devworkspace_operator_version "v0.41.0" \
      --prod_operator_index "registry.redhat.io/redhat/redhat-operator-index:v4.22" \
      --prod_operator_package_name "devspaces" \
      --prod_operator_bundle_name "devspacesoperator" \
      --prod_operator_version "v3.29.0" \
      --my_registry "<my_registry>"
    ```

    where:

    ` `*`<my_registry>`*` `  
    The private Docker registry where the images are mirrored

2.  In all running workspaces in the CodeReady Workspaces 3.27 instance, save and push changes back to the Git repositories.

3.  Stop all workspaces in the CodeReady Workspaces 3.27 instance.

4.  Run the following command:

    ``` bash
    $ dsc server:update --che-operator-image="$TAG" -n openshift-devspaces --k8spodwaittimeout=1800000
    ```

## Results

1.  Navigate to the OpenShift Dev Spaces instance.
2.  The 3.29 version number is visible at the bottom of the page.

**Related information**  

- [Red Hat-provided Operator catalogs](https://docs.openshift.com/container-platform/4.22/operators/understanding/olm-rh-catalogs.html)
- [Managing custom catalogs](https://docs.openshift.com/container-platform/4.22/operators/admin/olm-managing-custom-catalogs.html)
