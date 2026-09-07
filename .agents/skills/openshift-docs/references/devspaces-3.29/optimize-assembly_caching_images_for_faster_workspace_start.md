> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-assembly_caching_images_for_faster_workspace_start). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Speed up workspace starts with image caching

Speed up workspace starts by deploying the Kubernetes Image Puller to pre-cache container images on cluster nodes so that workspaces start in seconds instead of minutes.

The largest contributor to workspace startup time is pulling container images. Without caching, OpenShift pulls images from the registry on every workspace start. Images for the Universal Developer Image and IDE editors can exceed 2 GB, resulting in startup times of 2 to 5 minutes on cold nodes.

## How the Image Puller works

The Kubernetes Image Puller runs a DaemonSet that schedules a short-lived pod on each node in the cluster. Each pod pulls the specified images into the node's local container cache, then terminates. When a developer starts a workspace on that node, OpenShift finds the image already cached and skips the registry pull entirely.

The DaemonSet refreshes periodically to keep the cache warm as nodes scale up or images are garbage-collected.

## What the procedures cover

- **Deploy:** Install the Image Puller operator from the OpenShift web console or the command line. The operator creates and manages the DaemonSet automatically.
- **Select images to cache:** Review the default image list shipped with Dev Spaces, add your organization's custom images, or cache additional IDE and sidecar images used by your teams.
- **Verify impact:** Measure workspace startup time before and after caching to confirm the improvement.

<!-- -->

- **[How image caching speeds up workspace starts](optimize-con_caching_images_for_faster_workspace_start.md)**  
  To improve workspace start time, use the Image Puller, a community-supported OpenShift Dev Spaces-agnostic component that pre-pulls images for OpenShift clusters.
- **[Deploy Image Puller from the command line](optimize-proc_installing_image_puller_on_openshift_using_cli.md)**  
  Deploy the Kubernetes Image Puller on OpenShift by using the `oc` CLI to cache images and reduce workspace startup time.
- **[Deploy Image Puller from the web console](optimize-proc_installing_image_puller_on_openshift_by_using_web_console.md)**  
  Deploy the Kubernetes Image Puller Operator on OpenShift by using the OpenShift web console to cache images and reduce workspace startup time.
- **[Cache default OpenShift Dev Spaces images on all nodes](optimize-proc_configuring_image_puller_to_pre_pull_default_devspaces_images.md)**  
  Cache default OpenShift Dev Spaces images on all nodes by enabling Kubernetes Image Puller to reduce workspace startup time. The Red Hat OpenShift Dev Spaces Operator controls the image list and updates it automatically on OpenShift Dev Spaces upgrade.
- **[Cache your organization’s custom images](optimize-proc_configuring_image_puller_to_pre_pull_custom_images.md)**  
  Cache your organization’s custom images with Kubernetes Image Puller so that workspaces using organization-specific container images start without waiting for large image downloads.
- **[Cache additional images for faster starts](optimize-proc_configuring_image_puller_to_pre_pull_additional_images.md)**  
  Cache additional images with Kubernetes Image Puller to reduce workspace startup time by ensuring that required images are already cached on each node.
- **[Review the default images cached by Image Puller](optimize-proc_retrieving_default_list_of_images_for_kubernetes_image_puller.md)**  
  Review the default list of images used by Kubernetes Image Puller to decide which images to pre-cache. This list helps administrators configure Image Puller to use only a subset of these images in advance.

**Related information**  

- [Kubernetes Image Puller source code repository](https://github.com/che-incubator/kubernetes-image-puller)
