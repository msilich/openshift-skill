> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-proc_configuring_image_puller_to_pre_pull_additional_images). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Cache additional images for faster starts

Cache additional images with Kubernetes Image Puller to reduce workspace startup time by ensuring that required images are already cached on each node.

## Before you begin

- You have an instance of OpenShift Dev Spaces installed and running on a Kubernetes cluster.
- You have Image Puller installed on the Kubernetes cluster.

<!-- -->

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Create `k8s-image-puller` namespace:

    ``` bash
    oc create namespace k8s-image-puller
    ```

2.  Create `KubernetesImagePuller` Custom Resource:

    ``` bash
    oc apply -f - <<EOF
    apiVersion: che.eclipse.org/v1alpha1
    kind: KubernetesImagePuller
    metadata:
      name: k8s-image-puller-images
      namespace: k8s-image-puller
    spec:
      images: "NAME-1=IMAGE-1;NAME-2=IMAGE-2"
    EOF
    ```

    where:

    `images`  
    The semicolon-separated list of images in `name=image` format.

## Results

- Verify that the image puller `DaemonSet` is running in the `k8s-image-puller` namespace:

  ``` bash
  oc get daemonset -n k8s-image-puller
  ```

**Related information**  

- [Kubernetes Image Puller source code repository](https://github.com/che-incubator/kubernetes-image-puller)
- [community supported Kubernetes Image Puller Operator source code repository](https://github.com/che-incubator/kubernetes-image-puller-operator)
