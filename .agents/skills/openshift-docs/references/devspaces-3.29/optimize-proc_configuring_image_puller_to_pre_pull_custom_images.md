> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-proc_configuring_image_puller_to_pre_pull_custom_images). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Cache your organization’s custom images

Cache your organization’s custom images with Kubernetes Image Puller so that workspaces using organization-specific container images start without waiting for large image downloads.

## Before you begin

- You have an instance of OpenShift Dev Spaces installed and running on a Kubernetes cluster.
- You have Image Puller installed on the Kubernetes cluster.

<!-- -->

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

Configure the Image Puller to pre-pull custom images.

``` bash
oc patch checluster/devspaces \
    --namespace openshift-devspaces \
    --type='merge' \
    --patch '{
              "spec": {
                "components": {
                  "imagePuller": {
                    "enable": true,
                    "spec": {
                      "images": "NAME-1=IMAGE-1;NAME-2=IMAGE-2"
                    }
                  }
                }
              }
            }'
```

where:

`images`  
The semicolon-separated list of images in `name=image` format.

## Results

- Verify that the image puller is configured with the custom images:

  ``` bash
  oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.spec.components.imagePuller.spec.images}'
  ```

**Related concepts**  

- [How image caching speeds up workspace starts](optimize-con_caching_images_for_faster_workspace_start.md "To improve workspace start time, use the Image Puller, a community-supported OpenShift Dev Spaces-agnostic component that pre-pulls images for OpenShift clusters.")

**Related tasks**  

- [Deploy Image Puller from the command line](optimize-proc_installing_image_puller_on_openshift_using_cli.md "Deploy the Kubernetes Image Puller on OpenShift by using the oc CLI to cache images and reduce workspace startup time.")
- [Deploy Image Puller from the web console](optimize-proc_installing_image_puller_on_openshift_by_using_web_console.md "Deploy the Kubernetes Image Puller Operator on OpenShift by using the OpenShift web console to cache images and reduce workspace startup time.")
