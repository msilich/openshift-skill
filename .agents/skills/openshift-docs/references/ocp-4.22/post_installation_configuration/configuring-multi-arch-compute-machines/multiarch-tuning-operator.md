<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Multiarch Tuning Operator optimizes workload management within multi-architecture clusters and in single-architecture clusters transitioning to multi-architecture environments.

Architecture-aware workload scheduling allows the scheduler to place pods onto nodes that match the architecture of the pod images.

By default, the scheduler does not consider the architecture of a pod’s container images when determining the placement of new pods onto nodes.

To enable architecture-aware workload scheduling, you must create the `ClusterPodPlacementConfig` object. When you create the `ClusterPodPlacementConfig` object, the Multiarch Tuning Operator deploys the necessary operands to support architecture-aware workload scheduling. You can also use the `nodeAffinityScoring` plugin in the `ClusterPodPlacementConfig` object to set cluster-wide scores for node architectures. If you enable the `nodeAffinityScoring` plugin, the scheduler first filters nodes with compatible architectures and then places the pod on the node with the highest score.

At the namespace level, you can use the `celArchitecturePlacement` plugin in a `PodPlacementConfig` object to place workloads on specific architectures based on Common Expression Language (CEL) expressions that evaluate pod metadata.

When a pod is created, the operands perform the following actions:

1.  Add the `multiarch.openshift.io/scheduling-gate` scheduling gate that prevents the scheduling of the pod.

2.  Compute a scheduling predicate that includes the supported architecture values for the `kubernetes.io/arch` label.

3.  Integrate the scheduling predicate as a `nodeAffinity` requirement in the pod specification.

4.  Remove the scheduling gate from the pod.

> [!IMPORTANT]
> The following exclusions apply before CEL placement or image-based architecture detection:
>
> - The Operator ignores pods with `spec.nodeName` already set and pods owned by a DaemonSet.
>
> - The Operator ignores pods in its own namespace, pods in namespaces with the `kube-` prefix, and pods with a control-plane node selector.
>
> - If a pod has a `kubernetes.io/arch` node selector, or architecture constraints in every required node affinity term, together with architecture-based preferred node affinity, the Operator ignores the pod. This combination prevents CEL from overriding the existing architecture constraints.
>
> For otherwise eligible pods, CEL can replace architecture selectors and required node affinity while preserving preferred node affinity. If a pod already has architecture-based preferred node affinity, the Operator skips `nodeAffinityScoring`, not CEL placement.
>
> For image-based architecture detection, the Operator preserves existing architecture selectors and required affinity constraints. When neither a matching namespace-scoped placement plugin nor cluster-wide `nodeAffinityScoring` requires processing, pods with existing architecture constraints are not processed.

Before installing the Operator, ensure that existing network policies allow its pods to reach the Kubernetes API server. If egress isolation blocks that access, configure the required allow policy before installation so that the Operator can create its managed network policies. An ingress-only default-deny policy does not block this egress.

<div>

<div class="title">

Additional resources

</div>

- [Network policies created by the Multiarch Tuning Operator](multiarch-tuning-operator.md#multi-arch-tuning-operator-network-policies_multiarch-tuning-operator)

</div>

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

    The installation is successful if the Operator is in the `Succeeded` phase.

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

- [Installing from the software catalog by using the CLI](../../operators/user/olm-installing-operators-in-namespace.md#olm-installing-operator-from-software-catalog-using-cli_olm-installing-operators-in-namespace)

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

6.  Click **Install**.

7.  Set the following options on the **Operator Installation** page:

    1.  Set **Update Channel** to **stable**.

    2.  Set **Installation Mode** to **All namespaces on the cluster**.

    3.  Set **Installed Namespace** to **Operator recommended Namespace** or **Select a Namespace**.

        The recommended Operator namespace is `openshift-multiarch-tuning-operator`. If the `openshift-multiarch-tuning-operator` namespace does not exist, the namespace is created during the Operator installation.

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

After installing the Multiarch Tuning Operator, you can verify the multi-architecture support for workloads in your cluster. You can identify and manage pods based on their architecture compatibility by using the pod labels.

These labels are automatically set on the newly created pods to provide insights into their architecture support.

The following table describes the labels that the Multiarch Tuning Operator adds when you create a pod:

| Label | Description |
|----|----|
| `multiarch.openshift.io/multi-arch: ""` | The pod supports multiple architectures. |
| `multiarch.openshift.io/single-arch: ""` | The pod supports only a single architecture. |
| `multiarch.openshift.io/arm64: ""` | The pod supports the `arm64` architecture. |
| `multiarch.openshift.io/amd64: ""` | The pod supports the `amd64` architecture. |
| `multiarch.openshift.io/ppc64le: ""` | The pod supports the `ppc64le` architecture. |
| `multiarch.openshift.io/s390x: ""` | The pod supports the `s390x` architecture. |
| `multiarch.openshift.io/node-affinity: set` | The Operator has set the node affinity requirement for the architecture. |
| `multiarch.openshift.io/node-affinity: not-set` | The Operator did not set the node affinity requirement. For example, when the pod already has a node affinity for the architecture, the Multiarch Tuning Operator adds this label to the pod. |
| `multiarch.openshift.io/scheduling-gate: gated` | The pod is gated. |
| `multiarch.openshift.io/scheduling-gate: removed` | The pod gate has been removed. |
| `multiarch.openshift.io/inspection-error: ""` | An error has occurred while building the node affinity requirements. |
| `multiarch.openshift.io/preferred-node-affinity: set` | The Operator has set the architecture preferences in the pod. |
| `multiarch.openshift.io/preferred-node-affinity: not-set` | The Operator did not set the architecture preferences in the pod because the user had already set them in the `preferredDuringSchedulingIgnoredDuringExecution` node affinity. |

Pod labels that the Multiarch Tuning Operator adds when you create a pod

# The ClusterPodPlacementConfig object

After installing the Multiarch Tuning Operator, create a `ClusterPodPlacementConfig` object to enable architecture-aware workload scheduling across your cluster.

The object instructs the Operator to deploy its operands and network policies that restrict network traffic to and from the operands.

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
  logVerbosity: Normal
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
  fallbackArchitecture: amd64
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

`spec.fallbackArchitecture`
Optional parameter. Specifies an architecture where pods are scheduled if the image inspector cannot determine the architecture of the image. Valid values are `""`, `arm64`, `amd64`, `ppc64le`, or `s390x`. The value is set to `""` by default.

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

<div>

<div class="title">

Additional resources

</div>

- [Network policies created by the Multiarch Tuning Operator](multiarch-tuning-operator.md#multi-arch-tuning-operator-network-policies_multiarch-tuning-operator)

</div>

# Creating the namespace-scoped PodPlacementConfig object

After creating the `ClusterPodPlacementConfig` object, you can configure pod placement at the namespace level by creating namespace-scoped `PodPlacementConfig` objects.

`PodPlacementConfig` objects modify the pod placement controller’s behavior at the namespace level, and take precedence over the `ClusterPodPlacementConfig` object.

The `PodPlacementConfig` object supports the `nodeAffinityScoring` plugin and the `celArchitecturePlacement` plugin. The `celArchitecturePlacement` plugin uses Common Expression Language (CEL) expressions to place workloads on specific architectures based on pod metadata such as labels and annotations, instead of relying on image inspection.

<div>

<div class="title">

Prerequisites

</div>

- You have created a `ClusterPodPlacementConfig` object.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Using a text editor, create a YAML file based on the following example and modify the example with your namespace values:

    <div class="formalpara">

    <div class="title">

    Example `PodPlacementConfig` object configuration

    </div>

    ``` yaml
    apiVersion: multiarch.openshift.io/v1beta1
    kind: PodPlacementConfig
    metadata:
      name: my-namespace-config
      namespace: my-namespace
    spec:
      labelSelector:
          matchExpressions:
            - key: app
              operator: In
              values:
                - my-label-for-apps-performing-better-on-arm64
      priority: 100
      plugins:
        nodeAffinityScoring:
          enabled: true
          platforms:
            - architecture: amd64
              weight: 25
            - architecture: arm64
              weight: 75
    ```

    </div>

    where:

    `metadata`
    Specifies the object name, and namespace name. This parameter is required.

    `spec.labelSelector`
    Optionally specifies a label so that the `PodPlacementConfig` only applies to a subset of pods in the namespace. If you do not specify this parameter, the `PodPlacementConfig` applies to all pods in the namespace.

    `spec.priority`
    Optionally specifies a priority in case multiple `PodPlacementConfig` objects exist in one namespace. Higher priorities take precedence. Valid values are 0-255, and the default value is 0. If you specify multiple `PodPlacementConfig` objects in one namespace, they must have different priority values.

    `spec.plugins.nodeAffinityScoring`
    Specifies architecture preferences for pod placement. The controller prioritizes nodes based on the architecture scores, with higher weights taking precedence. If you enable this plugin by setting `spec.plugins.nodeAffinityScoring.enabled` to `true`, you must specify at least one platform with an architecture and weight value.

    `spec.plugins.nodeAffinityScoring.platforms[]`
    Specifies one or more platform configurations, each with a required architecture and weight pair. This parameter is required if `spec.plugins.nodeAffinityScoring` is present. Valid architecture values are `arm64`, `amd64`, `ppc64le`, and `s390x`. Valid weight values are 0-100. Each architecture can only be specified once.

2.  Apply the configuration file by running the following command:

    ``` terminal
    $ oc create -f <filename>
    ```

    Replace `<filename>` with the name of the `PodPlacementConfig` configuration file.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring architecture placement rules by using CEL expressions](multiarch-tuning-operator.md#multi-arch-creating-namespace-podplacement-config-cel_multiarch-tuning-operator)

</div>

# Configuring architecture placement rules by using CEL expressions

You can use Common Expression Language (CEL) rules in a namespace-scoped `PodPlacementConfig` object to select pod architectures from pod metadata instead of image inspection.

The `celArchitecturePlacement` plugin can place workloads on specific architectures based on workload characteristics, such as placing database pods on `ppc64le` nodes and web server pods on `amd64` nodes.

For eligible pods, the first rule that evaluates to `true` determines the target architectures. The plugin removes the `kubernetes.io/arch` entry from the pod `nodeSelector` field and replaces architecture constraints in required node affinity. Existing preferred node affinity is preserved. If no rule matches and at least one rule evaluates successfully, the plugin applies `fallbackArchitectures`. An empty or omitted rule list also applies the fallback.

<div class="important">

<div class="title">

</div>

- Ensure that the container images used by the selected pods support every architecture specified by the matching rule or fallback. CEL-based placement overrides image-based architecture detection. Selecting an incompatible architecture can cause `ENOEXEC` errors.

- If a pod combines an architecture node selector, or architecture constraints in every required node affinity term, with architecture-based preferred node affinity, the Operator ignores the pod before evaluating CEL. CEL does not override architecture constraints for this combination. Preferred architecture affinity alone does not disable CEL; for otherwise eligible pods, the Operator preserves those preferred terms and skips `nodeAffinityScoring`.

- Matching `PodPlacementConfig` objects with the `celArchitecturePlacement` plugin enabled are evaluated in descending priority order. The first configuration that produces architectures takes precedence. Rules are not merged across objects, and each object in a namespace must have a different priority value.

- If every rule in a configuration fails at runtime, the Operator skips that configuration without applying its fallback and considers lower-priority configurations. If no CEL configuration applies, processing can continue to image-based detection. This runtime behavior is separate from validation of expressions when you create or update the configuration.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to `oc` as a user with `cluster-admin` privileges.

- You have created the `ClusterPodPlacementConfig` object.

- You have created the namespace where you want to apply the configuration. For the following example and verification steps, use a dedicated test namespace that is selected for processing by `ClusterPodPlacementConfig` and has no other `PodPlacementConfig` objects.

- Your cluster has schedulable nodes for the architectures that you select. The following example requires `amd64` and `ppc64le` nodes.

- Your workload images support all architectures that the rules or fallback can select.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Using a text editor, create a YAML file based on the following example and modify the example with your namespace values:

    <div class="formalpara">

    <div class="title">

    Example `PodPlacementConfig` object with the `celArchitecturePlacement` plugin

    </div>

    ``` yaml
    apiVersion: multiarch.openshift.io/v1beta1
    kind: PodPlacementConfig
    metadata:
      name: my-namespace-cel-config
      namespace: my-namespace
    spec:
      priority: 10
      plugins:
        celArchitecturePlacement:
          enabled: true
          fallbackArchitectures:
            - amd64
          rules:
            - name: database-on-ppc64le
              expression: |
                'app.kubernetes.io/component' in self.metadata.labels &&
                self.metadata.labels['app.kubernetes.io/component'] == 'database'
              architectures:
                - ppc64le
            - name: web-server-on-amd64
              expression: |
                'app.kubernetes.io/component' in self.metadata.labels &&
                self.metadata.labels['app.kubernetes.io/component'] in ['frontend', 'backend']
              architectures:
                - amd64
    ```

    </div>

    where:

    `spec.priority`
    Optional parameter. Specifies a priority in case multiple `PodPlacementConfig` objects exist in one namespace. Higher priorities take precedence. Valid values are `0-255`, and the default value is `0`. If you specify multiple `PodPlacementConfig` objects in one namespace, they must have different priority values.

    `spec.plugins.celArchitecturePlacement.enabled`
    Set this field to `true` to enable the `celArchitecturePlacement` plugin.

    `spec.plugins.celArchitecturePlacement.fallbackArchitectures`
    Required parameter. Specifies the architectures to use when the rule list is empty or when at least one rule evaluates successfully but no rule matches. If every rule fails at runtime, the configuration is skipped without applying its fallback. You must specify at least one architecture, and you can specify up to four architectures. Valid values are `arm64`, `amd64`, `ppc64le`, and `s390x`.

    `spec.plugins.celArchitecturePlacement.rules`
    Optional parameter. Specifies up to 1000 rules that are evaluated in order. For eligible pods, the first matching rule determines the target architectures. If you omit the rules or specify an empty list, the plugin uses the fallback architectures.

    `spec.plugins.celArchitecturePlacement.rules[].name`
    Required parameter. Specifies a descriptive name of 1–253 characters for the rule.

    `spec.plugins.celArchitecturePlacement.rules[].expression`
    Required parameter. Specifies a CEL expression of 1–1024 characters that returns a boolean value. The expression is evaluated against the pod by using the `self` variable, and can access only the `metadata.name`, `metadata.generateName`, `metadata.namespace`, `metadata.labels`, and `metadata.annotations` fields of the pod. References to the `spec` or `status` fields of the pod, such as container images, environment variables, or volumes, are rejected when the `PodPlacementConfig` object is created or updated.

    `spec.plugins.celArchitecturePlacement.rules[].architectures`
    Required parameter. Specifies the target architectures to use when the rule matches. You must specify at least one architecture, and you can specify up to four architectures. Valid values are `arm64`, `amd64`, `ppc64le`, and `s390x`.

    The example omits `spec.labelSelector`, so it applies to all eligible pods in the namespace. Pods labeled `app.kubernetes.io/component=database` select `ppc64le`; pods labeled `frontend` or `backend` select `amd64`. Other eligible pods receive the `amd64` fallback. Add a label selector if you want to limit the configuration to a subset of pods.

    Expressions inspect pod metadata. For controller-managed workloads, such as Deployments, put the labels or annotations on the pod template, not only on the controller object.

2.  Apply the configuration file by running the following command:

    ``` terminal
    $ oc create -f <filename>
    ```

    Replace `<filename>` with the name of the `PodPlacementConfig` configuration file.

</div>

<div>

<div class="title">

Verification

</div>

- Confirm that the example `PodPlacementConfig` object is created:

  ``` terminal
  $ oc get podplacementconfig my-namespace-cel-config -n <namespace>
  ```

  Replace `<namespace>` in the following commands with the test namespace where you created the configuration.

- Create test pods for both rules, the fallback, and the existing-affinity exclusion:

  ``` terminal
  $ oc run cel-database-test -n <namespace> --restart=Never \
      --image=<multi_arch_image> --labels=app.kubernetes.io/component=database \
      --overrides='{"spec":{"affinity":{"nodeAffinity":{"preferredDuringSchedulingIgnoredDuringExecution":[{"weight":100,"preference":{"matchExpressions":[{"key":"kubernetes.io/arch","operator":"In","values":["amd64"]}]}}]}}}}' \
      --command -- sleep 3600
  $ oc run cel-web-test -n <namespace> --restart=Never \
      --image=<multi_arch_image> --labels=app.kubernetes.io/component=frontend \
      --command -- sleep 3600
  $ oc run cel-fallback-test -n <namespace> --restart=Never \
      --image=<multi_arch_image> --command -- sleep 3600
  $ oc run cel-excluded-test -n <namespace> --restart=Never \
      --image=<multi_arch_image> --labels=app.kubernetes.io/component=database \
      --overrides='{"spec":{"nodeSelector":{"kubernetes.io/arch":"amd64"},"affinity":{"nodeAffinity":{"preferredDuringSchedulingIgnoredDuringExecution":[{"weight":100,"preference":{"matchExpressions":[{"key":"kubernetes.io/arch","operator":"In","values":["amd64"]}]}}]}}}}' \
      --command -- sleep 3600
  ```

  Replace `<multi_arch_image>` with a container image that supports both `amd64` and `ppc64le` and includes the `sleep` command. The database test has preferred affinity only; the excluded test combines preferred affinity with an architecture node selector.

- Wait for the test pods to become ready:

  ``` terminal
  $ oc wait --for=condition=Ready pod/cel-database-test pod/cel-web-test pod/cel-fallback-test pod/cel-excluded-test -n <namespace> --timeout=120s
  ```

- Inspect the required architecture constraints and assigned nodes:

  ``` terminal
  $ oc get pods cel-database-test cel-web-test cel-fallback-test cel-excluded-test -n <namespace> -o custom-columns='NAME:.metadata.name,ARCHITECTURES:.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[*].matchExpressions[*].values[*],NODE:.spec.nodeName'
  ```

  For the example configuration, the database test must have required `ppc64le` affinity. The web and fallback tests must have required `amd64` affinity. The excluded test must not receive CEL-required `ppc64le` affinity because its existing selector and preferred affinity exclude it from processing.

- Confirm that the database test retains its preferred `amd64` affinity and that the excluded test retains its `amd64` node selector:

  ``` terminal
  $ oc get pod cel-database-test -n <namespace> -o jsonpath='{.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution}{"\n"}'
  $ oc get pod cel-excluded-test -n <namespace> -o jsonpath='{.spec.nodeSelector}{"\n"}'
  ```

  The database test must retain the preferred `kubernetes.io/arch` expression with value `amd64` and weight `100`, even though its required architecture is `ppc64le`. The excluded test must retain `kubernetes.io/arch: amd64` in its node selector.

- Compare the assigned node names with their architecture labels:

  ``` terminal
  $ oc get nodes -L kubernetes.io/arch
  ```

  The database test must run on a `ppc64le` node. The web, fallback, and excluded tests must run on `amd64` nodes.

- Remove the test pods when you finish verification:

  ``` terminal
  $ oc delete pod cel-database-test cel-web-test cel-fallback-test cel-excluded-test -n <namespace>
  ```

</div>

# Network policies created by the Multiarch Tuning Operator

The Multiarch Tuning Operator restricts network traffic to and from its workloads by creating `NetworkPolicy` objects. The policies are created at runtime by the Operator and are not part of the Operator bundle.

The Operator creates the following network policies:

- A policy that protects the Operator’s own controller manager workload. The Operator recreates this policy if it is deleted.

- Policies that protect the pod placement operands, such as the pod placement controller, the pod placement webhook, and the ENOEXEC event handler workloads. These policies are created when you create the `ClusterPodPlacementConfig` object and are deleted when you delete the `ClusterPodPlacementConfig` object.

Depending on the workload, the network policies allow the following traffic:

- DNS egress on TCP and UDP port `5353` to the `openshift-dns` namespace.

- TCP egress on port `6443` to any destination, to allow access to the Kubernetes API server.

- Metrics ingress on TCP port `8443` from the `openshift-monitoring` namespace.

- Admission webhook ingress on TCP port `9443` from any source, to allow access from the API server.

- TCP egress on all ports to any destination for workloads that inspect container images, to support registries, mirrors, and proxies that use arbitrary hosts and ports.

The API and webhook rules restrict ports, but do not restrict destination and source addresses, respectively. The image-inspection rule permits all TCP egress, not only connections to image registries.

> [!IMPORTANT]
> Before installing the Multiarch Tuning Operator, ensure that existing network policies allow its pods to reach the Kubernetes API server. If egress isolation blocks that access, configure the required allow policy before installation so that the Operator can create its managed network policies. An ingress-only default-deny policy does not block this egress, and an egress-deny policy can coexist with a separate policy that allows the required access.
>
> Because `NetworkPolicy` rules are additive, you can create additional policies to allow more traffic to or from the Operator workloads, but you cannot restrict the traffic further by using additional policies.

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

1.  Delete the `ClusterPodPlacementConfig` object by running the following command:

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

- You have deleted the `ClusterPodPlacementConfig` object.

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

- You have deleted the `ClusterPodPlacementConfig` object.

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
