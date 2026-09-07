<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use WebAssembly extensions to add new features directly into the Red Hat OpenShift Service Mesh proxies. This lets you move even more common functionality out of your applications, and implement them in a single language that compiles to WebAssembly bytecode.

> [!NOTE]
> WebAssembly extensions are not supported on IBM Z® and IBM Power®.

# WebAssembly modules overview

WebAssembly modules can be run on many platforms, including proxies, and have broad language support, fast execution, and a sandboxed-by-default security model.

Red Hat OpenShift Service Mesh extensions are [Envoy HTTP Filters](https://www.envoyproxy.io/docs/envoy/v1.20.0/intro/arch_overview/http/http_filters#arch-overview-http-filters), giving them a wide range of capabilities:

- Manipulating the body and headers of requests and responses.

- Out-of-band HTTP requests to services not in the request path, such as authentication or policy checking.

- Side-channel data storage and queues for filters to communicate with each other.

> [!NOTE]
> When creating new WebAssembly extensions, use the `WasmPlugin` API. The `ServiceMeshExtension` API was deprecated in Red Hat OpenShift Service Mesh version 2.2 and was removed in Red Hat OpenShift Service Mesh version 2.3.

There are two parts to writing a Red Hat OpenShift Service Mesh extension:

1.  You must write your extension using an SDK that exposes the [proxy-wasm API](https://github.com/proxy-wasm/spec) and compile it to a WebAssembly module.

2.  You must then package the module into a container.

<div class="formalpara">

<div class="title">

Supported languages

</div>

You can use any language that compiles to WebAssembly bytecode to write a Red Hat OpenShift Service Mesh extension, but the following languages have existing SDKs that expose the proxy-wasm API so that it can be consumed directly.

</div>

| Language | Maintainer | Repository |
|----|----|----|
| AssemblyScript | solo.io | [solo-io/proxy-runtime](https://github.com/solo-io/proxy-runtime) |
| C++ | proxy-wasm team (Istio Community) | [proxy-wasm/proxy-wasm-cpp-sdk](https://github.com/proxy-wasm/proxy-wasm-cpp-sdk) |
| Go | tetrate.io | [tetratelabs/proxy-wasm-go-sdk](https://github.com/tetratelabs/proxy-wasm-go-sdk) |
| Rust | proxy-wasm team (Istio Community) | [proxy-wasm/proxy-wasm-rust-sdk](https://github.com/proxy-wasm/proxy-wasm-rust-sdk) |

Supported languages

# `WasmPlugin` container format

Istio supports Open Container Initiative (OCI) images in its Wasm Plugin mechanism. You can distribute your Wasm Plugins as a container image, and you can use the `spec.url` field to refer to a container registry location. For example, `quay.io/my-username/my-plugin:latest`.

Because each execution environment (runtime) for a WASM module can have runtime-specific configuration parameters, a WASM image can be composed of two layers:

- **plugin.wasm** (Required) - Content layer. This layer consists of a `.wasm` binary containing the bytecode of your WebAssembly module, to be loaded by the runtime. You must name this file `plugin.wasm`.

- **runtime-config.json** (Optional) - Configuration layer. This layer consists of a JSON-formatted string that describes metadata about the module for the target runtime. The config layer might also contain additional data, depending on the target runtime. For example, the config for a WASM Envoy Filter contains root_ids available on the filter.

# WasmPlugin API reference

The WasmPlugins API provides a mechanism to extend the functionality provided by the Istio proxy through WebAssembly filters.

You can deploy multiple WasmPlugins. The `phase` and `priority` settings determine the order of execution (as part of Envoy’s filter chain), allowing the configuration of complex interactions between user-supplied WasmPlugins and Istio’s internal filters.

In the following example, an authentication filter implements an OpenID flow and populates the Authorization header with a JSON Web Token (JWT). Istio authentication consumes this token and deploys it to the ingress gateway. The WasmPlugin file lives in the proxy sidecar filesystem. Note the field `url`.

``` yaml
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: openid-connect
  namespace: istio-ingress
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  url: file:///opt/filters/openid.wasm
  sha256: 1ef0c9a92b0420cf25f7fe5d481b231464bc88f486ca3b9c83ed5cc21d2f6210
  phase: AUTHN
  pluginConfig:
    openid_server: authn
    openid_realm: ingress
```

Below is the same example, but this time an Open Container Initiative (OCI) image is used instead of a file in the filesystem. Note the fields `url`, `imagePullPolicy`, and `imagePullSecret`.

``` yaml
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: openid-connect
  namespace: istio-system
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  url: oci://private-registry:5000/openid-connect/openid:latest
  imagePullPolicy: IfNotPresent
  imagePullSecret: private-registry-pull-secret
  phase: AUTHN
  pluginConfig:
    openid_server: authn
    openid_realm: ingress
```

| Field | Type | Description | Required |
|----|----|----|----|
| spec.selector | WorkloadSelector | Criteria used to select the specific set of pods/VMs on which this plugin configuration should be applied. If omitted, this configuration will be applied to all workload instances in the same namespace. If the `WasmPlugin` field is present in the config root namespace, it will be applied to all applicable workloads in any namespace. | No |
| spec.url | string | URL of a Wasm module or OCI container. If no scheme is present, defaults to `oci://`, referencing an OCI image. Other valid schemes are `file://` for referencing .wasm module files present locally within the proxy container, and `http[s]://` for .wasm module files hosted remotely. | No |
| spec.sha256 | string | SHA256 checksum that will be used to verify the Wasm module or OCI container. If the `url` field already references a SHA256 (using the `@sha256:` notation), it must match the value of this field. If an OCI image is referenced by tag and this field is set, its checksum will be verified against the contents of this field after pulling. | No |
| spec.imagePullPolicy | PullPolicy | The pull behavior to be applied when fetching an OCI image. Only relevant when images are referenced by tag instead of SHA. Defaults to the value `IfNotPresent`, except when an OCI image is referenced in the `url` field and the `latest` tag is used, in which case the value `Always` is the default, mirroring K8s behavior. Setting is ignored if the `url` field is referencing a Wasm module directly using `file://` or `http[s]://`. | No |
| spec.imagePullSecret | string | Credentials to use for OCI image pulling. The name of a secret in the same namespace as the `WasmPlugin` object that contains a pull secret for authenticating against the registry when pulling the image. | No |
| spec.phase | PluginPhase | Determines where in the filter chain this `WasmPlugin` object is injected. | No |
| spec.priority | `int64` | Determines the ordering of `WasmPlugins` objects that have the same `phase` value. When multiple `WasmPlugins` objects are applied to the same workload in the same phase, they will be applied by priority and in descending order. If the `priority` field is not set, or two `WasmPlugins` objects with the same value, the ordering will be determined from the name and namespace of the `WasmPlugins` objects. Defaults to the value `0`. | No |
| spec.pluginName | string | The plugin name used in the Envoy configuration. Some Wasm modules might require this value to select the Wasm plugin to execute. | No |
| spec.pluginConfig | Struct | The configuration that will be passed on to the plugin. | No |
| spec.pluginConfig.verificationKey | string | The public key used to verify signatures of signed OCI images or Wasm modules. Must be supplied in PEM format. | No |

WasmPlugin Field Reference

The `WorkloadSelector` object specifies the criteria used to determine if a filter can be applied to a proxy. The matching criteria includes the metadata associated with a proxy, workload instance information such as labels attached to the pod/VM, or any other information that the proxy provides to Istio during the initial handshake. If multiple conditions are specified, all conditions need to match in order for the workload instance to be selected. Currently, only label based selection mechanism is supported.

| Field | Type | Description | Required |
|----|----|----|----|
| matchLabels | map\<string, string\> | One or more labels that indicate a specific set of pods/VMs on which a policy should be applied. The scope of label search is restricted to the configuration namespace in which the resource is present. | Yes |

WorkloadSelector

The `PullPolicy` object specifies the pull behavior to be applied when fetching an OCI image.

| Value | Description |
|----|----|
| \<empty\> | Defaults to the value `IfNotPresent`, except for OCI images with tag latest, for which the default will be the value `Always`. |
| IfNotPresent | If an existing version of the image has been pulled before, that will be used. If no version of the image is present locally, we will pull the latest version. |
| Always | Always pull the latest version of an image when applying this plugin. |

PullPolicy

`Struct` represents a structured data value, consisting of fields which map to dynamically typed values. In some languages, Struct might be supported by a native representation. For example, in scripting languages like JavaScript a struct is represented as an object.

| Field  | Type                 | Description                      |
|--------|----------------------|----------------------------------|
| fields | map\<string, Value\> | Map of dynamically typed values. |

Struct

`PluginPhase` specifies the phase in the filter chain where the plugin will be injected.

| Field | Description |
|----|----|
| \<empty\> | Control plane decides where to insert the plugin. This will generally be at the end of the filter chain, right before the Router. Do not specify PluginPhase if the plugin is independent of others. |
| AUTHN | Insert plugin before Istio authentication filters. |
| AUTHZ | Insert plugin before Istio authorization filters and after Istio authentication filters. |
| STATS | Insert plugin before Istio stats filters and after Istio authorization filters. |

PluginPhase

## Deploying `WasmPlugin` resources

You can enable Red Hat OpenShift Service Mesh extensions using the `WasmPlugin` resource. In this example, `istio-system` is the name of the Service Mesh control plane project. The following example creates an `openid-connect` filter that performs an OpenID Connect flow to authenticate the user.

<div>

<div class="title">

Procedure

</div>

1.  Create the following example resource:

    <div class="formalpara">

    <div class="title">

    Example plugin.yaml

    </div>

    ``` yaml
    apiVersion: extensions.istio.io/v1alpha1
    kind: WasmPlugin
    metadata:
      name: openid-connect
      namespace: istio-system
    spec:
      selector:
        matchLabels:
          istio: ingressgateway
      url: oci://private-registry:5000/openid-connect/openid:latest
      imagePullPolicy: IfNotPresent
      imagePullSecret: private-registry-pull-secret
      phase: AUTHN
      pluginConfig:
        openid_server: authn
        openid_realm: ingress
    ```

    </div>

2.  Apply your `plugin.yaml` file with the following command:

    ``` terminal
    $ oc apply -f plugin.yaml
    ```

</div>

# `ServiceMeshExtension` container format

You must have a `.wasm` file containing the bytecode of your WebAssembly module, and a `manifest.yaml` file in the root of the container filesystem to make your container image a valid extension image.

> [!NOTE]
> When creating new WebAssembly extensions, use the `WasmPlugin` API. The `ServiceMeshExtension` API was deprecated in Red Hat OpenShift Service Mesh version 2.2 and was removed in Red Hat OpenShift Service Mesh version 2.3.

<div class="formalpara">

<div class="title">

manifest.yaml

</div>

``` yaml
schemaVersion: 1

name: <your-extension>
description: <description>
version: 1.0.0
phase: PreAuthZ
priority: 100
module: extension.wasm
```

</div>

| Field | Description | Required |
|----|----|----|
| schemaVersion | Used for versioning of the manifest schema. Currently the only possible value is `1`. | This is a required field. |
| name | The name of your extension. | This field is just metadata and currently unused. |
| description | The description of your extension. | This field is just metadata and currently unused. |
| version | The version of your extension. | This field is just metadata and currently unused. |
| phase | The default execution phase of your extension. | This is a required field. |
| priority | The default priority of your extension. | This is a required field. |
| module | The relative path from the container filesystem’s root to your WebAssembly module. | This is a required field. |

Field Reference for manifest.yml

# ServiceMeshExtension reference

The ServiceMeshExtension API provides a mechanism to extend the functionality provided by the Istio proxy through WebAssembly filters. There are two parts to writing a WebAssembly extension:

1.  Write your extension using an SDK that exposes the proxy-wasm API and compile it to a WebAssembly module.

2.  Package it into a container.

> [!NOTE]
> When creating new WebAssembly extensions, use the `WasmPlugin` API. The `ServiceMeshExtension` API, which was deprecated in Red Hat OpenShift Service Mesh version 2.2, was removed in Red Hat OpenShift Service Mesh version 2.3.

| Field | Description |
|----|----|
| metadata.namespace | The `metadata.namespace` field of a `ServiceMeshExtension` source has a special semantic: if it equals the Control Plane Namespace, the extension will be applied to all workloads in the Service Mesh that match its `workloadSelector` value. When deployed to any other Mesh Namespace, it will only be applied to workloads in that same Namespace. |
| spec.workloadSelector | The `spec.workloadSelector` field has the same semantic as the `spec.selector` field of the [Istio Gateway resource](https://istio.io/v1.6/docs/reference/config/networking/gateway/#Gateway). It will match a workload based on its Pod labels. If no `workloadSelector` value is specified, the extension will be applied to all workloads in the namespace. |
| spec.config | This is a structured field that will be handed over to the extension, with the semantics dependent on the extension you are deploying. |
| spec.image | A container image URI pointing to the image that holds the extension. |
| spec.phase | The phase determines where in the filter chain the extension is injected, in relation to existing Istio functionality like Authentication, Authorization and metrics generation. Valid values are: PreAuthN, PostAuthN, PreAuthZ, PostAuthZ, PreStats, PostStats. This field defaults to the value set in the `manifest.yaml` file of the extension, but can be overwritten by the user. |
| spec.priority | If multiple extensions with the same `spec.phase` value are applied to the same workload instance, the `spec.priority` value determines the ordering of execution. Extensions with higher priority will be executed first. This allows for inter-dependent extensions. This field defaults to the value set in the `manifest.yaml` file of the extension, but can be overwritten by the user. |

ServiceMeshExtension Field Reference

## Deploying `ServiceMeshExtension` resources

You can enable Red Hat OpenShift Service Mesh extensions using the `ServiceMeshExtension` resource. In this example, `istio-system` is the name of the Service Mesh control plane project.

> [!NOTE]
> When creating new WebAssembly extensions, use the `WasmPlugin` API. The `ServiceMeshExtension` API was deprecated in Red Hat OpenShift Service Mesh version 2.2 and removed in Red Hat OpenShift Service Mesh version 2.3.

For a complete example that was built using the Rust SDK, take a look at the [header-append-filter](https://github.com/maistra/header-append-filter). It is a simple filter that appends one or more headers to the HTTP responses, with their names and values taken out from the `config` field of the extension. See a sample configuration in the snippet below.

<div>

<div class="title">

Procedure

</div>

1.  Create the following example resource:

    <div class="formalpara">

    <div class="title">

    Example ServiceMeshExtension resource extension.yaml

    </div>

    ``` yaml
    apiVersion: maistra.io/v1
    kind: ServiceMeshExtension
    metadata:
      name: header-append
      namespace: istio-system
    spec:
      workloadSelector:
        labels:
          app: httpbin
      config:
        first-header: some-value
        another-header: another-value
      image: quay.io/maistra-dev/header-append-filter:2.1
      phase: PostAuthZ
      priority: 100
    ```

    </div>

2.  Apply your `extension.yaml` file with the following command:

    ``` terminal
    $ oc apply -f <extension>.yaml
    ```

</div>

# Migrating from `ServiceMeshExtension` to `WasmPlugin` resources

The `ServiceMeshExtension` API, which was deprecated in Red Hat OpenShift Service Mesh version 2.2, was removed in Red Hat OpenShift Service Mesh version 2.3. If you are using the `ServiceMeshExtension` API, you must migrate to the `WasmPlugin` API to continue using your WebAssembly extensions.

The APIs are very similar. The migration consists of two steps:

1.  Renaming your plugin file and updating the module packaging.

2.  Creating a `WasmPlugin` resource that references the updated container image.

## API changes

The new `WasmPlugin` API is similar to the `ServiceMeshExtension`, but with a few differences, especially in the field names:

| ServiceMeshExtension | WasmPlugin |
|----|----|
| `spec.config` | `spec.pluginConfig` |
| `spec.workloadSelector` | `spec.selector` |
| `spec.image` | `spec.url` |
| `spec.phase` valid values: PreAuthN, PostAuthN, PreAuthZ, PostAuthZ, PreStats, PostStats | `spec.phase` valid values: \<empty\>, AUTHN, AUTHZ, STATS |

Field changes between `ServiceMeshExtensions` and `WasmPlugin`

The following is an example of how a `ServiceMeshExtension` resource could be converted into a `WasmPlugin` resource.

<div class="formalpara">

<div class="title">

ServiceMeshExtension resource

</div>

``` yaml
apiVersion: maistra.io/v1
kind: ServiceMeshExtension
metadata:
  name: header-append
  namespace: istio-system
spec:
  workloadSelector:
    labels:
      app: httpbin
  config:
    first-header: some-value
    another-header: another-value
  image: quay.io/maistra-dev/header-append-filter:2.2
  phase: PostAuthZ
  priority: 100
```

</div>

<div class="formalpara">

<div class="title">

New WasmPlugin resource equivalent to the ServiceMeshExtension above

</div>

``` yaml
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: header-append
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: httpbin
  url: oci://quay.io/maistra-dev/header-append-filter:2.2
  phase: STATS
  pluginConfig:
    first-header: some-value
    another-header: another-value
```

</div>

## Container image format changes

The new `WasmPlugin` container image format is similar to the `ServiceMeshExtensions`, with the following differences:

- The `ServiceMeshExtension` container format required a metadata file named `manifest.yaml` in the root directory of the container filesystem. The `WasmPlugin` container format does not require a `manifest.yaml` file.

- The `.wasm` file (the actual plugin) that previously could have any filename now must be named `plugin.wasm` and must be located in the root directory of the container filesystem.

## Migrating to `WasmPlugin` resources

To upgrade your WebAssembly extensions from the `ServiceMeshExtension` API to the `WasmPlugin` API, you rename your plugin file.

<div>

<div class="title">

Prerequisites

</div>

- `ServiceMeshControlPlane` is upgraded to version 2.2 or later.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Update your container image. If the plugin is already in `/plugin.wasm` inside the container, skip to the next step. If not:

    1.  Ensure the plugin file is named `plugin.wasm`. You must name the extension file `plugin.wasm`.

    2.  Ensure the plugin file is located in the root (/) directory. You must store extension files in the root of the container filesystem..

    3.  Rebuild your container image and push it to a container registry.

2.  Remove the `ServiceMeshExtension` resource and create a `WasmPlugin` resource that refers to the new container image you built.

</div>
