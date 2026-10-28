<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If your cluster was installed without an external registry, you can configure the cluster to use an external registry as a postinstallation task in order to use a mirroring workflow for your image management.

> [!IMPORTANT]
> This configuration is applicable only to clusters installed using the method described in [Installing a cluster without an external registry](../installing/installing_with_agent_based_installer/installing-ove.md#installing-ove).

When you install a cluster using the method described in "Installing a cluster without an external registry", the cluster relies on images contained in the downloaded ISO for its lifecycle management. However, you might want to configure your cluster to use an external image registry and mirror images to the registry instead. To do this, you must set up an external registry, successfully complete an update using images from the external registry, and finally delete `InternalReleaseImage` custom resource, which maintains an internal image registry in the cluster.

> [!IMPORTANT]
> Configuring your cluster to use an external registry is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Pre-configuration tasks

Before you can configure your cluster to use an external registry, you must prepare your environment with an image registry and perform an update using images on the registry.

To prevent the accidental deletion of the cluster’s internal image registry, you cannot delete the `InternalReleaseImage` custom resource without first having completed the following tasks:

- You have created a mirror registry in your environment. For more information, see "Creating a mirror registry with mirror registry for Red Hat OpenShift".

- You have mirrored images to the mirror registry. For more information, see "Mirroring images for a disconnected installation by using the oc-mirror plugin v2".

- You have updated your cluster using the images you mirrored to your registry. For more information, see "Updating a cluster in a disconnected environment using the OpenShift Update Service".

<div>

<div class="title">

Additional resources

</div>

- [Creating a mirror registry with mirror registry for Red Hat OpenShift](installing-mirroring-creating-registry.md#installing-mirroring-creating-registry)

- [Mirroring images for a disconnected installation by using the oc-mirror plugin v2](about-installing-oc-mirror-v2.md#about-installing-oc-mirror-v2)

- [Updating a cluster in a disconnected environment using the OpenShift Update Service](updating/disconnected-update-osus.md#updating-disconnected-cluster-osus)

</div>

# Deleting the internal image registry

You can complete configuring your cluster to use an external image registry by deleting the resource responsible for maintaining the internal image registry that was installed on your cluster.

<div>

<div class="title">

Prerequisites

</div>

- You installed your cluster using the method described in "Installing a cluster without an external registry".

- You have successfully performed a cluster update using images mirrored to your external image registry. You can ensure that your cluster has been updated to this new version by running the `oc get clusterversion` command.

  > [!IMPORTANT]
  > The version you updated your cluster to must not be listed in the `status.releases` field of the `InternalReleaseImage` custom resource (CR). You can check the contents of the CR by running the `oc get InternalReleaseImage -o yaml` command.

</div>

<div>

<div class="title">

Procedure

</div>

- Delete the singleton `InternalReleaseImage` CR by running the following command:

  ``` terminal
  $ oc delete internalreleaseimages cluster
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster without an external registry](../installing/installing_with_agent_based_installer/installing-ove.md#installing-ove)

</div>
