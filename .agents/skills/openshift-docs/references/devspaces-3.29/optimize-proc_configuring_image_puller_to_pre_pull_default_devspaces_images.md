> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-proc_configuring_image_puller_to_pre_pull_default_devspaces_images). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Cache default OpenShift Dev Spaces images on all nodes

Cache default OpenShift Dev Spaces images on all nodes by enabling Kubernetes Image Puller to reduce workspace startup time. The Red Hat OpenShift Dev Spaces Operator controls the image list and updates it automatically on OpenShift Dev Spaces upgrade.

## Before you begin

- You have an instance of OpenShift Dev Spaces installed and running on a Kubernetes cluster.
- You have Image Puller installed on the Kubernetes cluster. :\_mod-docs-content-type: SNIPPET
- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

Configure the Image Puller to pre-pull OpenShift Dev Spaces images.

``` bash
oc patch checluster/devspaces \
    --namespace openshift-devspaces \
    --type='merge' \
    --patch '{
              "spec": {
                "components": {
                  "imagePuller": {
                    "enable": true
                  }
                }
              }
            }'
```

## Results

- Verify that the image puller is enabled:

  ``` bash
  oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.spec.components.imagePuller.enable}'
  ```

**Related tasks**  

- [Review the default images cached by Image Puller](optimize-proc_retrieving_default_list_of_images_for_kubernetes_image_puller.md "Review the default list of images used by Kubernetes Image Puller to decide which images to pre-cache. This list helps administrators configure Image Puller to use only a subset of these images in advance.")
