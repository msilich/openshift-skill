> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-proc_retrieving_default_list_of_images_for_kubernetes_image_puller). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Review the default images cached by Image Puller

Review the default list of images used by Kubernetes Image Puller to decide which images to pre-cache. This list helps administrators configure Image Puller to use only a subset of these images in advance.

## Before you begin

- You have an instance of OpenShift Dev Spaces installed and running on a Kubernetes cluster. :\_mod-docs-content-type: SNIPPET
- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Determine the namespace where the OpenShift Dev Spaces Operator is deployed:

    ``` bash
    OPERATOR_NAMESPACE=$(oc get pods -l app.kubernetes.io/component=devspaces-operator -o jsonpath={".items[0].metadata.namespace"} --all-namespaces)
    ```

2.  Determine the images that can be pre-pulled by the Image Puller:

    ``` bash
    oc exec -n $OPERATOR_NAMESPACE deploy/devspaces-operator -- cat /tmp/external_images.txt
    ```

**Related concepts**  

- [How image caching speeds up workspace starts](optimize-con_caching_images_for_faster_workspace_start.md "To improve workspace start time, use the Image Puller, a community-supported OpenShift Dev Spaces-agnostic component that pre-pulls images for OpenShift clusters.")

**Related tasks**  

- [Deploy Image Puller from the command line](optimize-proc_installing_image_puller_on_openshift_using_cli.md "Deploy the Kubernetes Image Puller on OpenShift by using the oc CLI to cache images and reduce workspace startup time.")
- [Deploy Image Puller from the web console](optimize-proc_installing_image_puller_on_openshift_by_using_web_console.md "Deploy the Kubernetes Image Puller Operator on OpenShift by using the OpenShift web console to cache images and reduce workspace startup time.")
