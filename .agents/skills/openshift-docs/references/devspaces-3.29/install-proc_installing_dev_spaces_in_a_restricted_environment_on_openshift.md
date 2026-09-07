> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-proc_installing_dev_spaces_in_a_restricted_environment_on_openshift). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy in an air-gapped environment

Deploy OpenShift Dev Spaces on an OpenShift cluster with no internet access by mirroring the required container images and Operator catalogs to a private registry.

## Before you begin

- You have an OpenShift cluster with at least 64 GB of disk space.
- You have an OpenShift cluster ready to operate on a restricted network. See [About disconnected installation mirroring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/installing-mirroring-disconnected-about) and [Using Operator Lifecycle Manager on restricted networks](https://docs.openshift.com/container-platform/4.22/operators/admin/olm-restricted-networks.html).
- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have an active `oc registry` session to the `registry.redhat.io` Red Hat Ecosystem Catalog. See [Red Hat Container Registry authentication](https://access.redhat.com/RegistryAuthentication).
- You have `opm` installed. See [Installing the `opm` CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/opm/cli-opm-install.html).
- You have `jq` installed. See [Downloading `jq`](https://stedolan.github.io/jq/download/).
- You have `podman` installed. See [Podman Installation Instructions](https://podman.io/docs/installation).
- You have `skopeo` version 1.6 or higher installed. See [Installing Skopeo](https://github.com/containers/skopeo/blob/main/install.md).
- You have an active `skopeo` session with administrative access to the private Docker registry. See [Authenticating to a registry](https://github.com/containers/skopeo#authenticating-to-a-registry) and [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/installing-mirroring-disconnected-about).
- You have `dsc` for OpenShift Dev Spaces version 3.29 installed. See [Installing the dsc management tool](plan-proc_installing_the_dsc_management_tool.md).

## About this task

On a restricted network, deploying OpenShift Dev Spaces and running workspaces requires the following public resources:

- Operator catalog
- Container images
- Sample projects

To make these resources available, you can replace them with their copy in a registry accessible by the OpenShift cluster.

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
    The private Docker registry where the images will be mirrored

2.  Install OpenShift Dev Spaces with the configuration set in the `che-operator-cr-patch.yaml` created in step 1:

    ``` bash
    $ dsc server:deploy \
      --platform=openshift \
      --olm-channel stable \
      --catalog-source-name=devspaces-disconnected-install \
      --catalog-source-namespace=openshift-marketplace \
      --skip-devworkspace-operator \
      --che-operator-cr-patch-yaml=che-operator-cr-patch.yaml
    ```

3.  Allow incoming traffic from the OpenShift Dev Spaces namespace to all Pods in the user projects. See [Restrict network traffic between workspaces](configure-proc_configuring_network_policies.md).

## Results

- Verify that the OpenShift Dev Spaces instance is running:

  ``` bash
  $ dsc server:status
  ```

<!-- -->

- If `dsc server:deploy` fails with image pull errors, verify that all required images are mirrored to your private registry and that the `ImageContentSourcePolicy` or `ImageDigestMirrorSet` is configured correctly.
- If workspaces fail to start, verify that the network policies allow traffic from the `openshift-devspaces` namespace to user projects. See [Restrict network traffic between workspaces](configure-proc_configuring_network_policies.md).

**Related information**  

- [Red Hat-provided Operator catalogs](https://docs.openshift.com/container-platform/4.22/operators/understanding/olm-rh-catalogs.html)
- [Managing custom catalogs](https://docs.openshift.com/container-platform/4.22/operators/admin/olm-managing-custom-catalogs.html)
