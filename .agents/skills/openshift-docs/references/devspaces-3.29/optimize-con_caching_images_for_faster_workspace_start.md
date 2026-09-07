> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-con_caching_images_for_faster_workspace_start). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How image caching speeds up workspace starts

To improve workspace start time, use the Image Puller, a community-supported OpenShift Dev Spaces-agnostic component that pre-pulls images for OpenShift clusters.

The Image Puller is an additional OpenShift deployment that creates a *DaemonSet* to pre-pull relevant OpenShift Dev Spaces workspace images on each node. These images are already available when a workspace starts, improving the workspace start time.

For instructions on deploying, configuring, and reviewing cached images, see Additional resources.

**Related tasks**  

- [Deploy Image Puller from the web console](optimize-proc_installing_image_puller_on_openshift_by_using_web_console.md "Deploy the Kubernetes Image Puller Operator on OpenShift by using the OpenShift web console to cache images and reduce workspace startup time.")
- [Deploy Image Puller from the command line](optimize-proc_installing_image_puller_on_openshift_using_cli.md "Deploy the Kubernetes Image Puller on OpenShift by using the oc CLI to cache images and reduce workspace startup time.")
- [Cache default OpenShift Dev Spaces images on all nodes](optimize-proc_configuring_image_puller_to_pre_pull_default_devspaces_images.md "Cache default OpenShift Dev Spaces images on all nodes by enabling Kubernetes Image Puller to reduce workspace startup time. The Red Hat OpenShift Dev Spaces Operator controls the image list and updates it automatically on OpenShift Dev Spaces upgrade.")
- [Cache your organization’s custom images](optimize-proc_configuring_image_puller_to_pre_pull_custom_images.md "Cache your organization’s custom images with Kubernetes Image Puller so that workspaces using organization-specific container images start without waiting for large image downloads.")
- [Cache additional images for faster starts](optimize-proc_configuring_image_puller_to_pre_pull_additional_images.md "Cache additional images with Kubernetes Image Puller to reduce workspace startup time by ensuring that required images are already cached on each node.")
- [Review the default images cached by Image Puller](optimize-proc_retrieving_default_list_of_images_for_kubernetes_image_puller.md "Review the default list of images used by Kubernetes Image Puller to decide which images to pre-cache. This list helps administrators configure Image Puller to use only a subset of these images in advance.")

**Related information**  

- [Kubernetes Image Puller source code repository](https://github.com/che-incubator/kubernetes-image-puller)
