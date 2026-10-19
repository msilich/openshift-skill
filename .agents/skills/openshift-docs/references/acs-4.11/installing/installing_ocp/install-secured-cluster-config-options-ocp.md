<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When installing Secured Cluster services by using the Operator, you can configure optional settings.

<a id="secured-cluster-configuration-options-operator_install-secured-cluster-config-options-ocp"></a>

# Secured Cluster services configuration options

When you create a `SecuredCluster` instance, the Operator exposes the parameters that control how Secured Cluster services connect to Central and how each secured cluster component is deployed and scheduled.

Two parameters are required, and the Operator applies defaults to the rest. You set the remaining parameters only when you want to override a default, for example, to reserve nodes for a component, adjust resource limits, or turn off a component that your environment does not need.

The parameters are grouped into the following categories:

Required configuration settings  
Identify the Central instance to connect to and the name that the secured cluster is registered under.

Admission controller settings  
Control admission control enforcement, scheduling, and webhook behavior.

Scanner configuration settings for the Operator  
Configure the Scanner and Scanner V4 components, including scaling, database storage, and monitoring.

Image configuration  
Specify the image pull secrets that are used to pull component images.

Per node settings  
Configure the components that run on every node, such as Collector and Compliance.

Sensor configuration settings  
Configure scheduling and resources for Sensor.

General and miscellaneous settings  
Configure cluster-wide behavior such as annotations, environment variables, egress mode, network policies, and TLS.

The following sections describe each parameter in these categories.

<a id="admission-controller-settings_install-secured-cluster-config-options-ocp"></a>

## Admission controller settings

Configure the admission controller component of the `SecuredCluster` custom resource to enforce security policies on workload create and update operations.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>admissionControl.enforcement</code></p></td>
<td style="text-align: left;"><p>This parameter determines if you configured the admission controller to enforce policies that have enforcement enabled. For a new secured cluster deployed with RHACS 4.9, the default value is <code>Enabled</code>. For secured clusters updating from RHACS versions before 4.9, previous values for the admission controller configuration parameters determine the value of this parameter. Before the update, if either of the <code>admissionControl.listenOnCreates</code> or <code>admissionControl.listenOnUpdates</code> parameters was set to <code>true</code>, the value of this parameter defaults to <code>Enabled</code> after upgrade. If both of these parameters were set to <code>false</code>, the default value becomes <code>Disabled</code> on update.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.listenOnCreates</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated. RHACS checks the value during updates to version 4.9 and is used to set a default value for the new <code>admissionControl.enforcement</code> parameter. On new installations, changing this parameter has no effect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.listenOnEvents</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated. RHACS checks the value during updates to version 4.9 and is used to set a default value for the new <code>admissionControl.enforcement</code> parameter. On new installations, changing this parameter has no effect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.listenOnUpdates</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated and RHACS ignores its value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.nodeSelector</code></p></td>
<td style="text-align: left;"><p>If you want this component to only run on specific nodes, you can configure a node selector using this parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Admission Control. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.hostAliases</code></p></td>
<td style="text-align: left;"><p>Use this parameter to inject hosts and IP addresses into the pod’s hosts file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.resources.limits</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource limits for the admission controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.resources.requests</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default resource requests for the admission controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.bypass</code></p></td>
<td style="text-align: left;"><p>Use one of the following values to configure whether RHACS allows bypassing the admission controller enforcement:</p>
<ul>
<li><p><code>BreakGlassAnnotation</code> to enable bypassing the admission controller by using the <code>admission.stackrox.io/break-glass</code> annotation.</p></li>
<li><p><code>Disabled</code> to disable the ability to bypass admission controller enforcement for the secured cluster.</p></li>
</ul>
<p>The default value is <code>BreakGlassAnnotation</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.contactImageScanners</code></p></td>
<td style="text-align: left;"><p>This field is deprecated. Setting it has no effect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.failurePolicy</code></p></td>
<td style="text-align: left;"><p>Determines whether the API server request is allowed (fail open) or blocked (fail closed) if an error or timeout happens in the RHACS validating webhook’s evaluation. Valid values are <code>Ignore</code> and <code>Fail</code>. The default value is <code>Ignore</code> to fail open.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.timeoutSeconds</code></p></td>
<td style="text-align: left;"><p>The ability to configure this parameter is deprecated. RHACS uses a preset value for the timeout period and you cannot change it. This parameter is ignored.</p></td>
</tr>
</tbody>
</table>

<a id="customize-installation-operator-overlays_install-secured-cluster-config-options-ocp"></a>

# Customizing the installation using the Operator with overlays

Learn how to tailor the installation of RHACS using the Operator method with overlays.

<a id="overlays_install-secured-cluster-config-options-ocp"></a>

## Overlays

When `Central` or `SecuredCluster` custom resources do not expose certain low-level configuration options as parameters, you can use the `.spec.overlays` field for adjustments. Use this field to change the Kubernetes resources generated by these custom resources.

The `.spec.overlays` field comprises a sequence of patches, applied in their listed order. The Operator processes these patches on the Kubernetes resources before deployment to the cluster.

> [!WARNING]
> With the `.spec.overlays` field in both `Central` and `SecuredCluster`, you can change low-level Kubernetes resources in arbitrary ways. Use this feature only when the needed customization is not available through the `SecuredCluster` or `Central` custom resources.
>
> Red Hat limits support for the `.spec.overlays` feature primarily because it grants the ability to make intricate and highly specific modifications to Kubernetes resources, which can vary significantly from one implementation to another. This level of customization introduces a complexity that goes beyond standard usage scenarios, making it challenging to offer broad support. Each modification can be unique, potentially interacting with the Kubernetes system in unpredictable ways across different versions and configurations of the product. This variability means that troubleshooting and guaranteeing the stability of these customizations require a level of expertise and understanding specific to each individual’s setup. You can tailor Kubernetes resources to meet precise needs with this feature, but you must also assume responsibility to ensure the compatibility and stability of your configurations, especially during upgrades or changes to the underlying product.

The following example shows the structure of an overlay:

``` yaml
overlays:
- apiVersion: v1         #
  kind: ExampleKind      #
  name: my-resource      #
  patches:
    - path: .some.field  #
      value: |           #
        key1: data2
        key2: data2
```

where:

`overlays.apiVersion`  
Specifies the targeted Kubernetes resource ApiVersion, for example, `apps/v1`, `v1`, `networking.k8s.io/v1`.

`overlays.kind`  
Specifies the resource type, for example,`Deployment`, `ConfigMap`, `NetworkPolicy`.

`overlays.name`  
Specifies the name of the resource, for example, `my-resource`.

`overlays.patches.path`  
Specifies the JSON path expression to the field, for example, `spec.template.spec.containers[name:central].env[-1]`.

`overlays.patches.value`  
Specifies the YAML string for the new field value. If you do not want to use YAML parsing, you can use the `verbatim` key as shown in the following ConfigMap example.

<a id="adding-an-overlay_install-secured-cluster-config-options-ocp"></a>

### Adding an overlay

For customizations, you can add overlays to `Central` or `SecuredCluster` custom resources. Use the OpenShift CLI (`oc`) or the OpenShift Container Platform web console for modifications.

If overlays do not take effect as expected, check the RHACS Operator logs for any syntax errors or issues logged.

<a id="examples_install-secured-cluster-config-options-ocp"></a>

## Overlay examples

The following examples show common overlay configurations for RHACS components.

<a id="adding-eks-role-arn-annotation_install-secured-cluster-config-options-ocp"></a>

### Specifying an EKS pod role ARN for the Central ServiceAccount

Add an Amazon Elastic Kubernetes Service (EKS) pod role Amazon Resource Name (ARN) annotation to the `central` ServiceAccount as shown in the following example:

``` yaml
apiVersion: platform.stackrox.io
kind: Central
metadata:
  name: central
spec:
  # ...
  overlays:
  - apiVersion: v1
    kind: ServiceAccount
    name: central
    patches:
      - path: metadata.annotations.eks\.amazonaws\.com/role-arn
        value: "\"arn:aws:iam:1234:role\""
```

<a id="adding-an-environment-variable-to-a-deployment_install-secured-cluster-config-options-ocp"></a>

### Injecting an environment variable into the Central deployment

Inject an environment variable into the `central` deployment as shown in the following example:

``` yaml
apiVersion: platform.stackrox.io
kind: Central
metadata:
  name: central
spec:
  # ...
  overlays:
  - apiVersion: apps/v1
    kind: Deployment
    name: central
    patches:
    - path: spec.template.spec.containers[name:central].env[-1]
      value: |
        name: MY_ENV_VAR
        value: value
```

<a id="adding-an-ingress-to-a-network-policy_install-secured-cluster-config-options-ocp"></a>

### Extending network policy with an ingress rule

Add an ingress rule to the `allow-ext-to-central` network policy for port 999 traffic as shown in the following example:

``` yaml
apiVersion: platform.stackrox.io
kind: Central
metadata:
  name: central
spec:
    # ...
    overlays:
    - apiVersion: networking.k8s.io/v1
      kind: NetworkPolicy
      name: allow-ext-to-central
      patches:
        - path: spec.ingress[-1]
          value: |
            ports:
            - port: 999
              protocol: TCP
```

<a id="changing-configmap-data_install-secured-cluster-config-options-ocp"></a>

### Modifying ConfigMap data

Change the `central-endpoints` ConfigMap data as shown in the following example:

``` yaml
apiVersion: platform.stackrox.io
kind: Central
metadata:
  name: central
spec:
    # ...
    overlays:
    - apiVersion: v1
      kind: ConfigMap
      name: central-endpoints
      patches:
      - path: data.endpoints\.yaml
        verbatim: |
          disableDefault: false
          # another line
```

This example shows how to override only a single item (file) under `data`.

Follow this example by taking these steps:

- Use the `verbatim` key, rather than `value`. This helps pass through characters such as newlines or quotes without changing them.

- You must escape the dot in the filename in the `path` key as shown, or you can write the path as `data["endpoints.yaml"]`.

<a id="adding-a-container-to-a-deployment_install-secured-cluster-config-options-ocp"></a>

### Adding a container to the `Central` deployment

Add a new container to the `central` deployment as shown in the following example:

``` yaml
apiVersion: platform.stackrox.io
kind: Central
metadata:
  name: central
spec:
    # ...
    overlays:
    - apiVersion: apps/v1
      kind: Deployment
      name: central
      patches:
        - path: spec.template.spec.containers[-1]
      value: |
        name: nginx
        image: nginx
        ports:
          - containerPort: 8000
            name: http
            protocol: TCP
```
