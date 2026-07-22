<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Multiarch Tuning Operator optimizes workload management within multi-architecture clusters and in single-architecture clusters transitioning to multi-architecture environments.

Architecture-aware workload scheduling allows the scheduler to place pods onto nodes that match the architecture of the pod images.

By default, the scheduler does not consider the architecture of a pod’s container images when determining the placement of new pods onto nodes.

To enable architecture-aware workload scheduling, you must create the `ClusterPodPlacementConfig` object. When you create the `ClusterPodPlacementConfig` object, the Multiarch Tuning Operator deploys the necessary operands to support architecture-aware workload scheduling. You can also use the `nodeAffinityScoring` plugin in the `ClusterPodPlacementConfig` object to set cluster-wide scores for node architectures. If you enable the `nodeAffinityScoring` plugin, the scheduler first filters nodes with compatible architectures and then places the pod on the node with the highest score.

When a pod is created, the operands perform the following actions:

1.  Add the `multiarch.openshift.io/scheduling-gate` scheduling gate that prevents the scheduling of the pod.

2.  Compute a scheduling predicate that includes the supported architecture values for the `kubernetes.io/arch` label.

3.  Integrate the scheduling predicate as a `nodeAffinity` requirement in the pod specification.

4.  Remove the scheduling gate from the pod.

> [!IMPORTANT]
> Note the following operand behaviors:
>
> - If the `nodeSelector` field is already configured with the `kubernetes.io/arch` label for a workload, the operand does not update the `nodeAffinity` field for that workload.
>
> - If the `nodeSelector` field is not configured with the `kubernetes.io/arch` label for a workload, the operand updates the `nodeAffinity` field for that workload. However, in that `nodeAffinity` field, the operand updates only the node selector terms that are not configured with the `kubernetes.io/arch` label.
>
> - If the `nodeName` field is already set, the Multiarch Tuning Operator does not process the pod.
>
> - If the pod is owned by a DaemonSet, the operand does not update the `nodeAffinity` field.
>
> - If both `nodeSelector` or `nodeAffinity` and `preferredAffinity` fields are set for the `kubernetes.io/arch` label, the operand does not update the `nodeAffinity` field.
>
> - If only `nodeSelector` or `nodeAffinity` field is set for the `kubernetes.io/arch` label and the `nodeAffinityScoring` plugin is disabled, the operand does not update the `nodeAffinity` field.
>
> - If the `nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution` field already contains terms that score nodes based on the `kubernetes.io/arch` label, the operand ignores the configuration in the `nodeAffinityScoring` plugin.

# Installing the Multiarch Tuning Operator by using the CLI

You can install the Multiarch Tuning Operator by using the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to `oc` as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new project named `openshift-multiarch-tuning-operator` by running the following command:

    ``` terminal
    $ oc create ns openshift-multiarch-tuning-operator
    ```

2.  Create an `OperatorGroup` object:

    1.  Create a YAML file with the configuration for creating an `OperatorGroup` object.

        <div class="formalpara">

        <div class="title">

        Example YAML configuration for creating an `OperatorGroup` object

        </div>

        ``` yaml
        apiVersion: operators.coreos.com/v1
        kind: OperatorGroup
        metadata:
          name: openshift-multiarch-tuning-operator
          namespace: openshift-multiarch-tuning-operator
        spec: {}
        ```

        </div>

    2.  Create the `OperatorGroup` object by running the following command:

        ``` terminal
        $ oc create -f <file_name>
        ```

        Replace `<file_name>` with the name of the YAML file that contains the `OperatorGroup` object configuration.

3.  Create a `Subscription` object:

    1.  Create a YAML file with the configuration for creating a `Subscription` object.

        <div class="formalpara">

        <div class="title">

        Example YAML configuration for creating a `Subscription` object

        </div>

        ``` yaml
        apiVersion: operators.coreos.com/v1alpha1
        kind: Subscription
        metadata:
          name: openshift-multiarch-tuning-operator
          namespace: openshift-multiarch-tuning-operator
        spec:
          channel: stable
          name: multiarch-tuning-operator
          source: redhat-operators
          sourceNamespace: openshift-marketplace
          installPlanApproval: Automatic
          startingCSV: multiarch-tuning-operator.<version>
        ```

        </div>

    2.  Create the `Subscription` object by running the following command:

        ``` terminal
        $ oc create -f <file_name>
        ```

        Replace `<file_name>` with the name of the YAML file that contains the `Subscription` object configuration.

        > [!NOTE]
        > For more details about configuring the `Subscription` object and `OperatorGroup` object, see "Installing from the software catalog by using the CLI".

</div>

<div>

<div class="title">

Verification

</div>

1.  To verify that the Multiarch Tuning Operator is installed, run the following command:

    ``` terminal
    $ oc get csv -n openshift-multiarch-tuning-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                   DISPLAY                     VERSION       REPLACES                            PHASE
    multiarch-tuning-operator.<version>   Multiarch Tuning Operator   <version>     multiarch-tuning-operator.1.0.0      Succeeded
    ```

    </div>

    The installation is successful if the Operator is in `Succeeded` phase.

2.  Optional: To verify that the `OperatorGroup` object is created, run the following command:

    ``` terminal
    $ oc get operatorgroup -n openshift-multiarch-tuning-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                        AGE
    openshift-multiarch-tuning-operator-q8zbb   133m
    ```

    </div>

3.  Optional: To verify that the `Subscription` object is created, run the following command:

    ``` terminal
    $ oc get subscription -n openshift-multiarch-tuning-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                        PACKAGE                     SOURCE                  CHANNEL
    multiarch-tuning-operator   multiarch-tuning-operator   redhat-operators        stable
    ```

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing from the software catalog using the CLI](../../operators/user/olm-installing-operators-in-namespace.md#olm-installing-operator-from-software-catalog-using-cli_olm-installing-operators-in-namespace)

</div>

# Installing the Multiarch Tuning Operator by using the web console

You can install the Multiarch Tuning Operator by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Navigate to **Ecosystem** → **Software Catalog**.

3.  Enter **Multiarch Tuning Operator** in the search field.

4.  Click **Multiarch Tuning Operator**.

5.  Select the **Multiarch Tuning Operator** version from the **Version** list.

6.  Click **Install**

7.  Set the following options on the **Operator Installation** page:

    1.  Set **Update Channel** to **stable**.

    2.  Set **Installation Mode** to **All namespaces on the cluster**.

    3.  Set **Installed Namespace** to **Operator recommended Namespace** or **Select a Namespace**.

        The recommended Operator namespace is `openshift-multiarch-tuning-operator`. If the `openshift-multiarch-tuning-operator` namespace does not exist, the namespace is created during the operator installation.

        If you select **Select a namespace**, you must select a namespace for the Operator from the **Select Project** list.

    4.  **Update approval** as **Automatic** or **Manual**.

        If you select **Automatic** updates, Operator Lifecycle Manager (OLM) automatically updates the running instance of the Multiarch Tuning Operator without any intervention.

        If you select **Manual** updates, OLM creates an update request. As a cluster administrator, you must manually approve the update request to update the Multiarch Tuning Operator to a newer version.

8.  Optional: Select the **Enable Operator recommended cluster monitoring on this Namespace** checkbox.

9.  Click **Install**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Navigate to **Ecosystem** → **Installed Operators**.

2.  Verify that the **Multiarch Tuning Operator** is listed with the **Status** field as **Succeeded** in the `openshift-multiarch-tuning-operator` namespace.

</div>

# Multiarch Tuning Operator pod labels and architecture support overview

After installing the Multiarch Tuning Operator, you can verify the multi-architecture support for workloads in your cluster. You can identify and manage pods based on their architecture compatibility by using the pod labels. These labels are automatically set on the newly created pods to provide insights into their architecture support.

The following table describes the labels that the Multiarch Tuning Operator adds when you create a pod:

| Label | Description |
|----|----|
| `multiarch.openshift.io/multi-arch: ""` | The pod supports multiple architectures. |
| `multiarch.openshift.io/single-arch: ""` | The pod supports only a single architecture. |
| `multiarch.openshift.io/arm64: ""` | The pod supports the `arm64` architecture. |
| `multiarch.openshift.io/amd64: ""` | The pod supports the `amd64` architecture. |
| `multiarch.openshift.io/ppc64le: ""` | The pod supports the `ppc64le` architecture. |
| `multiarch.openshift.io/s390x: ""` | The pod supports the `s390x` architecture. |
| `multirach.openshift.io/node-affinity: set` | The Operator has set the node affinity requirement for the architecture. |
| `multirach.openshift.io/node-affinity: not-set` | The Operator did not set the node affinity requirement. For example, when the pod already has a node affinity for the architecture, the Multiarch Tuning Operator adds this label to the pod. |
| `multiarch.openshift.io/scheduling-gate: gated` | The pod is gated. |
| `multiarch.openshift.io/scheduling-gate: removed` | The pod gate has been removed. |
| `multiarch.openshift.io/inspection-error: ""` | An error has occurred while building the node affinity requirements. |
| `multiarch.openshift.io/preferred-node-affinity: set` | The Operator has set the architecture preferences in the pod. |
| `multiarch.openshift.io/preferred-node-affinity: not-set` | The Operator did not set the architecture preferences in the pod because the user had already set them in the `preferredDuringSchedulingIgnoredDuringExecution` node affinity. |

Pod labels that the Multiarch Tuning Operator adds when you create a pod

# The ClusterPodPlacementConfig object

After installing the Multiarch Tuning Operator, you must create a `ClusterPodPlacementConfig` object. The object instructs the Operator to deploy its operand, which enables architecture-aware workload scheduling across your cluster.

The `ClusterPodPlacementConfig` object supports two optional plugins:

- The `node affinity scoring` plugin patches pods to set soft preferences, using weighted affinities, for the architectures specified by the user. Pods are more likely to be scheduled on nodes running architectures with higher weights.

- The `exec format error monitor` plugin detects `ENOEXEC` errors, which occur when a pod attempts to execute a binary incompatible with the architecture of the node. When enabled, this plugin generates events in the affected event stream of the pod. The plugin triggers an `ExecFormatErrorsDetected` Prometheus alert if one or more `ENOEXEC` errors are detected within the last six hours. These errors can result from incorrect architecture node selectors, invalid image metadata that affects architecture-aware workload scheduling, an incorrect binary in an image, or an incompatible binary injected at runtime.

> [!NOTE]
> You can create only one instance of the `ClusterPodPlacementConfig` object.

<div class="formalpara">

<div class="title">

Example `ClusterPodPlacementConfig` object configuration

</div>

``` yaml
apiVersion: multiarch.openshift.io/v1beta1
kind: ClusterPodPlacementConfig
metadata:
  name: cluster
spec:
  logVerbosityLevel: Normal
  namespaceSelector:
    matchExpressions:
      - key: multiarch.openshift.io/exclude-pod-placement
        operator: DoesNotExist
  plugins:
    nodeAffinityScoring:
      enabled: true
      platforms:
        - architecture: amd64
          weight: 100
        - architecture: arm64
          weight: 50
    execFormatErrorMonitor:
      enabled: true
```

</div>

where:

`metadata.name`
Specifies the name of the object. You must set this parameter to `cluster`.

`spec.logVerbosity`
Optional parameter. Specifies the log verbosity level. You can set the field value to `Normal`, `Debug`, `Trace`, or `TraceAll`. The value is set to `Normal` by default.

`spec.namespaceSelector`
Optional parameter. You can configure the `namespaceSelector` to select the namespaces in which the Multiarch Tuning Operator’s pod placement operand must process the `nodeAffinity` of the pods. All namespaces are considered by default.

`spec.plugins.nodeAffinityScoring.enabled`
Optional parameter. You can enable the node affinity scoring plugin to set architecture preferences for pod placement. When enabled, the scheduler first filters out nodes that do not meet the pod’s requirements. Then, it prioritizes the remaining nodes based on the architecture scores defined in the `nodeAffinityScoring.platforms` field. The default value is false.

`spec.plugins.nodeAffinityScoring.platforms`
Optional parameter. Defines a list of architectures and their corresponding scores. The scheduler prioritizes nodes for pod placement based on the architecture scores that you set and the scheduling requirements defined in the pod specification.

`spec.plugins.nodeAffinityScoring.platforms.architecture`
Specifies the architecture for the node affinity scoring plugin. Accepted values are `arm64`, `amd64`, `ppc64le`, or `s390x`.

`spec.plugins.nodeAffinityScoring.platforms.weight`
Specifies the weight for the architecture you specified in the `spec.plugins.nodeAffinityScoring.platforms.architecture` parameter. The value must be configured in the range of `1` (lowest priority) to `100` (highest priority). The scheduler uses this score to prioritize nodes for pod placement, favoring nodes with architectures that have higher scores.

`spec.plugins.execFormatErrorMonitor.enabled`
Optional parameter. Set this field to `true` to enable the `execFormatErrorMonitor` plugin. When enabled, the plugin detects `ENOEXEC` errors, caused when a pod executes a binary incompatible with the node’s architecture. The plugin generates events in the affected pods, and triggers the `ExecFormatErrorsDetected` Prometheus alert if one or more errors are found in the last six hours.

In this example, the `operator` field value is set to `DoesNotExist`. Therefore, if the `key` field value (`multiarch.openshift.io/exclude-pod-placement`) is set as a label in a namespace, the operand does not process the `nodeAffinity` of the pods in that namespace. Instead, the operand processes the `nodeAffinity` of the pods in namespaces that do not contain the label.

If you want the operand to process the `nodeAffinity` of the pods only in specific namespaces, you can configure the `namespaceSelector` as follows:

``` yaml
namespaceSelector:
  matchExpressions:
    - key: multiarch.openshift.io/include-pod-placement
      operator: Exists
```

In this example, the `operator` field value is set to `Exists`. Therefore, the operand processes the `nodeAffinity` of the pods only in namespaces that contain the `multiarch.openshift.io/include-pod-placement` label.

> [!IMPORTANT]
> This Operator excludes pods in namespaces starting with `kube-`. The Operator also excludes pods that are expected to be scheduled on control plane nodes.

## Creating the ClusterPodPlacementConfig object by using the CLI

To deploy the pod placement operand that enables architecture-aware workload scheduling, you can create the `ClusterPodPlacementConfig` object by using the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to `oc` as a user with `cluster-admin` privileges.

- You have installed the Multiarch Tuning Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ClusterPodPlacementConfig` object YAML file:

    <div class="formalpara">

    <div class="title">

    Example `ClusterPodPlacementConfig` object configuration

    </div>

    ``` yaml
    apiVersion: multiarch.openshift.io/v1beta1
    kind: ClusterPodPlacementConfig
    metadata:
      name: cluster
    spec:
      logVerbosityLevel: Normal
      namespaceSelector:
        matchExpressions:
          - key: multiarch.openshift.io/exclude-pod-placement
            operator: DoesNotExist
      plugins:
        nodeAffinityScoring:
          enabled: true
          platforms:
            - architecture: amd64
              weight: 100
            - architecture: arm64
              weight: 50
    ```

    </div>

2.  Create the `ClusterPodPlacementConfig` object by running the following command:

    ``` terminal
    $ oc create -f <file_name>
    ```

    Replace `<file_name>` with the name of the `ClusterPodPlacementConfig` object YAML file.

</div>

<div>

<div class="title">

Verification

</div>

- To check that the `ClusterPodPlacementConfig` object is created, run the following command:

  ``` terminal
  $ oc get clusterpodplacementconfig
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME      AGE
  cluster   29s
  ```

  </div>

</div>

## Creating the ClusterPodPlacementConfig object by using the web console

To deploy the pod placement operand that enables architecture-aware workload scheduling, you can create the `ClusterPodPlacementConfig` object by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

- You have installed the Multiarch Tuning Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Go to **Ecosystem** → **Installed Operators**.

3.  On the **Installed Operators** page, click **Multiarch Tuning Operator**.

4.  Click the **Cluster Pod Placement Config** tab.

5.  Select either **Form view** or **YAML view**.

6.  Configure the `ClusterPodPlacementConfig` object parameters.

7.  Click **Create**.

8.  Optional: If you want to edit the `ClusterPodPlacementConfig` object, perform the following actions:

    1.  Click the **Cluster Pod Placement Config** tab.

    2.  Select **Edit ClusterPodPlacementConfig** from the options menu.

    3.  Click **YAML** and edit the `ClusterPodPlacementConfig` object parameters.

    4.  Click **Save**.

</div>

<div>

<div class="title">

Verification

</div>

- On the **Cluster Pod Placement Config** page, check that the `ClusterPodPlacementConfig` object is in the `Ready` state.

</div>

# Deleting the ClusterPodPlacementConfig object by using the CLI

You can create only one instance of the `ClusterPodPlacementConfig` object. If you want to re-create this object, you must first delete the existing instance.

You can delete this object by using the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to `oc` as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Delete the `ClusterPodPlacementConfig` object by running the following command:

    ``` terminal
    $ oc delete clusterpodplacementconfig cluster
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To check that the `ClusterPodPlacementConfig` object is deleted, run the following command:

  ``` terminal
  $ oc get clusterpodplacementconfig
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  No resources found
  ```

  </div>

</div>

# Deleting the ClusterPodPlacementConfig object by using the web console

You can create only one instance of the `ClusterPodPlacementConfig` object. If you want to recreate this object, you must first delete the existing instance.

You can delete this object by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

- You have created the `ClusterPodPlacementConfig` object.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Navigate to **Ecosystem** → **Installed Operators**.

3.  On the **Installed Operators** page, click **Multiarch Tuning Operator**.

4.  Click the **Cluster Pod Placement Config** tab.

5.  Select **Delete ClusterPodPlacementConfig** from the options menu.

6.  Click **Delete**.

</div>

<div>

<div class="title">

Verification

</div>

- On the **Cluster Pod Placement Config** page, check that the `ClusterPodPlacementConfig` object has been deleted.

</div>

# Uninstalling the Multiarch Tuning Operator by using the CLI

You can uninstall the Multiarch Tuning Operator by using the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to `oc` as a user with `cluster-admin` privileges.

- You deleted the `ClusterPodPlacementConfig` object.

  > [!IMPORTANT]
  > You must delete the `ClusterPodPlacementConfig` object before uninstalling the Multiarch Tuning Operator. Uninstalling the Operator without deleting the `ClusterPodPlacementConfig` object leads to unexpected behavior.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the `Subscription` object name for the Multiarch Tuning Operator by running the following command:

    ``` terminal
    $ oc get subscription.operators.coreos.com -n <namespace>
    ```

    Replace `<namespace>` with the name of the namespace where you want to uninstall the Multiarch Tuning Operator.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                  PACKAGE                     SOURCE             CHANNEL
    openshift-multiarch-tuning-operator   multiarch-tuning-operator   redhat-operators   stable
    ```

    </div>

2.  Get the `currentCSV` value for the Multiarch Tuning Operator by running the following command:

    ``` terminal
    $ oc get subscription.operators.coreos.com <subscription_name> -n <namespace> -o yaml | grep currentCSV
    ```

    - Replace `<subscription_name>` with the `Subscription` object name. For example, `openshift-multiarch-tuning-operator`.

    - Replace `<namespace>` with the name of the namespace where you want to uninstall the Multiarch Tuning Operator.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      currentCSV: multiarch-tuning-operator.<version>
      ```

      </div>

3.  Delete the `Subscription` object by running the following command:

    ``` terminal
    $ oc delete subscription.operators.coreos.com <subscription_name> -n <namespace>
    ```

    - Replace `<subscription_name>` with the `Subscription` object name.

    - Replace `<namespace>` with the name of the namespace where you want to uninstall the Multiarch Tuning Operator.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      subscription.operators.coreos.com "openshift-multiarch-tuning-operator" deleted
      ```

      </div>

4.  Delete the CSV for the Multiarch Tuning Operator in the target namespace by using the `currentCSV` value by running the following command:

    ``` terminal
    $ oc delete clusterserviceversion <currentCSV_value> -n <namespace>
    ```

    - Replace `<currentCSV_value>` with the `currentCSV` value for the Multiarch Tuning Operator. For example: `multiarch-tuning-operator.<version>`.

    - Replace `<namespace>` with the name of the namespace where you want to uninstall the Multiarch Tuning Operator.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      clusterserviceversion.operators.coreos.com "multiarch-tuning-operator.<version>" deleted
      ```

      </div>

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the Multiarch Tuning Operator is uninstalled, run the following command:

  ``` terminal
  $ oc get csv -n <namespace>
  ```

  Replace `<namespace>` with the name of the namespace where you have uninstalled the Multiarch Tuning Operator.

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  No resources found in openshift-multiarch-tuning-operator namespace.
  ```

  </div>

</div>

# Uninstalling the Multiarch Tuning Operator by using the web console

You can uninstall the Multiarch Tuning Operator by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` permissions.

- You deleted the `ClusterPodPlacementConfig` object.

  > [!IMPORTANT]
  > You must delete the `ClusterPodPlacementConfig` object before uninstalling the Multiarch Tuning Operator. Uninstalling the Operator without deleting the `ClusterPodPlacementConfig` object leads to unexpected behavior.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Navigate to **Ecosystem** → **Software Catalog**.

3.  Enter **Multiarch Tuning Operator** in the search field.

4.  Click **Multiarch Tuning Operator**.

5.  Click the **Details** tab.

6.  From the **Actions** menu, select **Uninstall Operator**.

7.  When prompted, click **Uninstall**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Navigate to **Ecosystem** → **Installed Operators**.

2.  On the **Installed Operators** page, verify that the **Multiarch Tuning Operator** is not listed.

</div>
