> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-proc_installing_image_puller_on_openshift_by_using_web_console). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy Image Puller from the web console

Deploy the Kubernetes Image Puller Operator on OpenShift by using the OpenShift web console to cache images and reduce workspace startup time.

## Before you begin

- You have an OpenShift web console session as a cluster administrator. See [Accessing the web console](https://docs.openshift.com/container-platform/4.22/web_console/web-console.html).

## Procedure

1.  Install the Kubernetes Image Puller Operator. See [Installing from OperatorHub using the web console](https://docs.openshift.com/container-platform/4.22/operators/admin/olm-adding-operators-to-cluster.html#olm-installing-from-operatorhub-using-web-console_olm-adding-operators-to-a-cluster).
2.  Create a `KubernetesImagePuller` operand from the Kubernetes Image Puller Operator. See [Creating applications from installed Operators](https://docs.openshift.com/container-platform/4.22/operators/user/olm-creating-apps-from-installed-operators.html).

## Results

- In the OpenShift web console, go to **Operators** **Installed Operators** and verify that the Kubernetes Image Puller Operator status is **Succeeded**.

**Related concepts**  

- [How image caching speeds up workspace starts](optimize-con_caching_images_for_faster_workspace_start.md "To improve workspace start time, use the Image Puller, a community-supported OpenShift Dev Spaces-agnostic component that pre-pulls images for OpenShift clusters.")

**Related tasks**  

- [Deploy Image Puller from the command line](optimize-proc_installing_image_puller_on_openshift_using_cli.md "Deploy the Kubernetes Image Puller on OpenShift by using the oc CLI to cache images and reduce workspace startup time.")
- [Cache default OpenShift Dev Spaces images on all nodes](optimize-proc_configuring_image_puller_to_pre_pull_default_devspaces_images.md "Cache default OpenShift Dev Spaces images on all nodes by enabling Kubernetes Image Puller to reduce workspace startup time. The Red Hat OpenShift Dev Spaces Operator controls the image list and updates it automatically on OpenShift Dev Spaces upgrade.")
