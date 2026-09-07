> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-proc_installing_image_puller_on_openshift_using_cli). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy Image Puller from the command line

Deploy the Kubernetes Image Puller on OpenShift by using the `oc` CLI to cache images and reduce workspace startup time.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

Important

If the Image Puller is installed with the `oc` CLI, it cannot be configured through the `CheCluster` Custom Resource.

## Procedure

1.  Gather a list of relevant container images to pull. See [Review the default images cached by Image Puller](optimize-proc_retrieving_default_list_of_images_for_kubernetes_image_puller.md "Review the default list of images used by Kubernetes Image Puller to decide which images to pre-cache. This list helps administrators configure Image Puller to use only a subset of these images in advance.").

2.  Define the memory requests and limits parameters to ensure pulled containers and the platform have enough memory to run.

    When defining the minimal value for `CACHING_MEMORY_REQUEST` or `CACHING_MEMORY_LIMIT`, consider the necessary amount of memory required to run each of the container images to pull.

    When defining the maximal value for `CACHING_MEMORY_REQUEST` or `CACHING_MEMORY_LIMIT`, consider the total memory allocated to the DaemonSet Pods in the cluster:

    ``` shell-session
    (memory limit) * (number of images) * (number of nodes in the cluster)
    ```

    Pulling 5 images on 20 nodes, with a container memory limit of `20Mi` requires `2000Mi` of memory.

3.  Clone the Image Puller repository and get in the directory containing the OpenShift templates:

    ``` bash
    git clone https://github.com/che-incubator/kubernetes-image-puller
    cd kubernetes-image-puller/deploy/openshift
    ```

4.  Configure the `app.yaml`, `configmap.yaml`, and `serviceaccount.yaml` OpenShift templates using the following parameters: <span id="proc_installing-image-puller-on-openshift-using-cli_devspaces__entry__1"></span><span id="proc_installing-image-puller-on-openshift-using-cli_devspaces__entry__2"></span><span id="proc_installing-image-puller-on-openshift-using-cli_devspaces__entry__3"></span>

    | Value | Usage | Default |
    |----|----|----|
    | `DEPLOYMENT_NAME` | The value of `DEPLOYMENT_NAME` in the ConfigMap | `kubernetes-image-puller` |
    | `IMAGE` | Image used for the `kubernetes-image-puller` deployment | `registry.redhat.io/devspaces/imagepuller-rhel8` |
    | `IMAGE_TAG` | The image tag to pull | `latest` |
    | `SERVICEACCOUNT_NAME` | The name of the ServiceAccount created and used by the deployment | `kubernetes-image-puller` |

    Table 1. Image Puller OpenShift templates parameters in `app.yaml`

    <span id="proc_installing-image-puller-on-openshift-using-cli_devspaces__entry__16"></span><span id="proc_installing-image-puller-on-openshift-using-cli_devspaces__entry__17"></span><span id="proc_installing-image-puller-on-openshift-using-cli_devspaces__entry__18"></span>

    | Value | Usage | Default |
    |----|----|----|
    | `CACHING_CPU_LIMIT` | The value of `CACHING_CPU_LIMIT` in the ConfigMap | `.2` |
    | `CACHING_CPU_REQUEST` | The value of `CACHING_CPU_REQUEST` in the ConfigMap | `.05` |
    | `CACHING_INTERVAL_HOURS` | The value of `CACHING_INTERVAL_HOURS` in the ConfigMap | `"1"` |
    | `CACHING_MEMORY_LIMIT` | The value of `CACHING_MEMORY_LIMIT` in the ConfigMap | `"20Mi"` |
    | `CACHING_MEMORY_REQUEST` | The value of `CACHING_MEMORY_REQUEST` in the ConfigMap | `"10Mi"` |
    | `DAEMONSET_NAME` | The value of `DAEMONSET_NAME` in the ConfigMap | `kubernetes-image-puller` |
    | `DEPLOYMENT_NAME` | The value of `DEPLOYMENT_NAME` in the ConfigMap | `kubernetes-image-puller` |
    | `IMAGES` | The value of `IMAGES` in the ConfigMap | `{}` |
    | `NAMESPACE` | The value of `NAMESPACE` in the ConfigMap | `k8s-image-puller` |
    | `NODE_SELECTOR` | The value of `NODE_SELECTOR` in the ConfigMap | `"{}"` |

    Table 2. Image Puller OpenShift templates parameters in `configmap.yaml`

    <span id="proc_installing-image-puller-on-openshift-using-cli_devspaces__entry__49"></span><span id="proc_installing-image-puller-on-openshift-using-cli_devspaces__entry__50"></span><span id="proc_installing-image-puller-on-openshift-using-cli_devspaces__entry__51"></span>

    | Value | Usage | Default |
    |----|----|----|
    | `SERVICEACCOUNT_NAME` | The name of the ServiceAccount created and used by the deployment | `kubernetes-image-puller` |
    | `KIP_IMAGE` | The image puller image to copy the sleep binary from | `registry.redhat.io/devspaces/imagepuller-rhel8:latest` |

    Table 3. Image Puller OpenShift templates parameters in `serviceaccount.yaml`

5.  Create an OpenShift project to host the Image Puller:

    ``` bash
    oc new-project <k8s-image-puller>
    ```

6.  Process and apply the templates to install the puller:

    ``` bash
    oc process -f serviceaccount.yaml | oc apply -f -
    oc process -f configmap.yaml | oc apply -f -
    oc process -f app.yaml | oc apply -f -
    ```

## Results

1.  Verify the existence of a *\<kubernetes-image-puller\>* deployment and a *\<kubernetes-image-puller\>* DaemonSet. The DaemonSet needs to have a Pod for each node in the cluster:

    ``` plaintext
    oc get deployment,daemonset,pod --namespace <k8s-image-puller>
    ```

2.  Verify the values of the *\<kubernetes-image-puller\>*`ConfigMap`.

    ``` plaintext
    oc get configmap <kubernetes-image-puller> --output yaml
    ```

**Related tasks**  

- [Review the default images cached by Image Puller](optimize-proc_retrieving_default_list_of_images_for_kubernetes_image_puller.md "Review the default list of images used by Kubernetes Image Puller to decide which images to pre-cache. This list helps administrators configure Image Puller to use only a subset of these images in advance.")
