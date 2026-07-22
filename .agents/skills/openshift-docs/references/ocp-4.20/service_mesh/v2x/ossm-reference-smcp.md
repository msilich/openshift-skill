<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can customize your Red Hat OpenShift Service Mesh by modifying the default `ServiceMeshControlPlane` (SMCP) resource or by creating a completely custom SMCP resource. This reference section documents the configuration options available for the SMCP resource.

# Service Mesh Control plane parameters

The following table lists the top-level parameters for the `ServiceMeshControlPlane` resource.

| Name | Description | Type |
|----|----|----|
| `apiVersion` | APIVersion defines the versioned schema of this representation of an object. Servers convert recognized schemas to the latest internal value, and may reject unrecognized values. The value for the `ServiceMeshControlPlane` version 2.0 is `maistra.io/v2`. | The value for `ServiceMeshControlPlane` version 2.0 is `maistra.io/v2`. |
| `kind` | Kind is a string value that represents the REST resource this object represents. | `ServiceMeshControlPlane` is the only valid value for a ServiceMeshControlPlane. |
| `metadata` | Metadata about this `ServiceMeshControlPlane` instance. You can provide a name for your Service Mesh control plane installation to keep track of your work, for example, `basic`. | string |
| `spec` | The specification of the desired state of this `ServiceMeshControlPlane`. This includes the configuration options for all components that comprise the Service Mesh control plane. | For more information, see Table 2. |
| `status` | The current status of this `ServiceMeshControlPlane` and the components that comprise the Service Mesh control plane. | For more information, see Table 3. |

`ServiceMeshControlPlane` resource parameters

The following table lists the specifications for the `ServiceMeshControlPlane` resource. Changing these parameters configures Red Hat OpenShift Service Mesh components.

| Name | Description | Configurable parameters |
|----|----|----|
| `addons` | The `addons` parameter configures additional features beyond core Service Mesh control plane components, such as visualization, or metric storage. | `3scale`, `grafana`, `jaeger`, `kiali`, and `prometheus`. |
| `cluster` | The `cluster` parameter sets the general configuration of the cluster (cluster name, network name, multi-cluster, mesh expansion, etc.) | `meshExpansion`, `multiCluster`, `name`, and `network` |
| `gateways` | You use the `gateways` parameter to configure ingress and egress gateways for the mesh. | `enabled`, `additionalEgress`, `additionalIngress`, `egress`, `ingress`, and `openshiftRoute` |
| `general` | The `general` parameter represents general Service Mesh control plane configuration that does not fit anywhere else. | `logging` and `validationMessages` |
| `policy` | You use the `policy` parameter to configure policy checking for the Service Mesh control plane. Policy checking can be enabled by setting `spec.policy.enabled` to `true`. | `mixer` `remote`, or `type`. `type` can be set to `Istiod`, `Mixer` or `None`. |
| `profiles` | You select the `ServiceMeshControlPlane` profile to use for default values using the `profiles` parameter. | `default` |
| `proxy` | You use the `proxy` parameter to configure the default behavior for sidecars. | `accessLogging`, `adminPort`, `concurrency`, and `envoyMetricsService` |
| `runtime` | You use the `runtime` parameter to configure the Service Mesh control plane components. | `components`, and `defaults` |
| `security` | The `security` parameter allows you to configure aspects of security for the Service Mesh control plane. | `certificateAuthority`, `controlPlane`, `identity`, `dataPlane` and `trust` |
| `techPreview` | The `techPreview` parameter enables early access to features that are in technology preview. | N/A |
| `telemetry` | If `spec.mixer.telemetry.enabled` is set to `true`, telemetry is enabled. | `mixer`, `remote`, and `type`. `type` can be set to `Istiod`, `Mixer` or `None`. |
| `tracing` | You use the `tracing` parameter to enables distributed tracing for the mesh. | `sampling`, `type`. `type` can be set to `Jaeger` or `None`. |
| `version` | You use the `version` parameter to specify what Maistra version of the Service Mesh control plane to install. When creating a `ServiceMeshControlPlane` with an empty version, the admission webhook sets the version to the current version. New `ServiceMeshControlPlanes` with an empty version are set to `v2.0`. Existing `ServiceMeshControlPlanes` with an empty version keep their setting. | string |

`ServiceMeshControlPlane` resource spec

`ControlPlaneStatus` represents the current state of your service mesh.

| Name | Description | Type |
|----|----|----|
| `annotations` | The `annotations` parameter stores additional, usually redundant status information, such as the number of components deployed by the `ServiceMeshControlPlane`. These statuses are used by the command-line tool, `oc`, which does not yet allow counting objects in JSONPath expressions. | Not configurable |
| `conditions` | Represents the latest available observations of the object’s current state. `Reconciled` indicates whether the operator has finished reconciling the actual state of deployed components with the configuration in the `ServiceMeshControlPlane` resource. `Installed` indicates whether the Service Mesh control plane has been installed. `Ready` indicates whether all Service Mesh control plane components are ready. | string |
| `components` | Shows the status of each deployed Service Mesh control plane component. | string |
| `appliedSpec` | The resulting specification of the configuration options after all profiles have been applied. | `ControlPlaneSpec` |
| `appliedValues` | The resulting values.yaml used to generate the charts. | `ControlPlaneSpec` |
| `chartVersion` | The version of the charts that were last processed for this resource. | string |
| `observedGeneration` | The generation observed by the controller during the most recent reconciliation. The information in the status pertains to this particular generation of the object. The `status.conditions` are not up-to-date if the `status.observedGeneration` field does not match `metadata.generation`. | integer |
| `operatorVersion` | The version of the operator that last processed this resource. | string |
| `readiness` | The readiness status of components & owned resources. | string |

`ServiceMeshControlPlane` resource `ControlPlaneStatus`

This example `ServiceMeshControlPlane` definition contains all of the supported parameters.

<div class="formalpara">

<div class="title">

Example `ServiceMeshControlPlane` resource

</div>

``` yaml
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  version: v2.6
  proxy:
    runtime:
      container:
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 128Mi
  tracing:
    type: Jaeger
  gateways:
    ingress: # istio-ingressgateway
      service:
        type: ClusterIP
        ports:
        - name: status-port
          port: 15020
        - name: http2
          port: 80
          targetPort: 8080
        - name: https
          port: 443
          targetPort: 8443
      meshExpansionPorts: []
    egress: # istio-egressgateway
      service:
        type: ClusterIP
        ports:
        - name: status-port
          port: 15020
        - name: http2
          port: 80
          targetPort: 8080
        - name: https
          port: 443
          targetPort: 8443
    additionalIngress:
      some-other-ingress-gateway: {}
    additionalEgress:
      some-other-egress-gateway: {}

  policy:
    type: Mixer
    mixer: # only applies if policy.type: Mixer
      enableChecks: true
      failOpen: false

  telemetry:
    type: Istiod # or Mixer
    mixer: # only applies if telemetry.type: Mixer, for v1 telemetry
      sessionAffinity: false
      batching:
        maxEntries: 100
        maxTime: 1s
      adapters:
        kubernetesenv: true
        stdio:
          enabled: true
          outputAsJSON: true
  addons:
    grafana:
      enabled: true
      install:
        config:
          env: {}
          envSecrets: {}
        persistence:
          enabled: true
          storageClassName: ""
          accessMode: ReadWriteOnce
          capacity:
            requests:
              storage: 5Gi
        service:
          ingress:
            contextPath: /grafana
            tls:
              termination: reencrypt
    kiali:
      name: kiali
      enabled: true
      install: # install kiali CR if not present
        dashboard:
          viewOnly: false
          enableGrafana: true
          enableTracing: true
          enablePrometheus: true
      service:
        ingress:
          contextPath: /kiali
    jaeger:
      name: jaeger
      install:
        storage:
          type: Elasticsearch # or Memory
          memory:
            maxTraces: 100000
          elasticsearch:
            nodeCount: 3
            storage: {}
            redundancyPolicy: SingleRedundancy
            indexCleaner: {}
        ingress: {} # jaeger ingress configuration
  runtime:
    components:
      pilot:
        deployment:
          replicas: 2
        pod:
          affinity: {}
        container:
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 128Mi
      grafana:
        deployment: {}
        pod: {}
      kiali:
        deployment: {}
        pod: {}
```

</div>

# spec parameters

## general parameters

Here is an example that illustrates the `spec.general` parameters for the `ServiceMeshControlPlane` object and a description of the available parameters with appropriate values.

<div class="formalpara">

<div class="title">

Example general parameters

</div>

``` yaml
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  general:
    logging:
      componentLevels: {}
          # misc: error
      logAsJSON: false
    validationMessages: true
```

</div>

<table>
<caption>Istio general parameters</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Values</th>
<th style="text-align: left;">Default value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>logging:</code></pre></td>
<td style="text-align: left;"><p>Use to configure logging for the Service Mesh control plane components.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>logging:
 componentLevels:</code></pre></td>
<td style="text-align: left;"><p>Use to specify the component logging level.</p></td>
<td style="text-align: left;"><p>Possible values: <code>debug</code>, <code>info</code>, <code>warn</code>, <code>error</code>, <code>fatal</code>.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>logging:
 logAsJSON:</code></pre></td>
<td style="text-align: left;"><p>Use to enable or disable JSON logging.</p></td>
<td style="text-align: left;"><p><code>true</code>/<code>false</code></p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>validationMessages:</code></pre></td>
<td style="text-align: left;"><p>Use to enable or disable validation messages to the status fields of istio.io resources. This can be useful for detecting configuration errors in resources.</p></td>
<td style="text-align: left;"><p><code>true</code>/<code>false</code></p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
</tbody>
</table>

## profiles parameters

You can create reusable configurations with `ServiceMeshControlPlane` object profiles. If you do not configure the `profile` setting, Red Hat OpenShift Service Mesh uses the default profile.

Here is an example that illustrates the `spec.profiles` parameter for the `ServiceMeshControlPlane` object:

<div class="formalpara">

<div class="title">

Example profiles parameters

</div>

``` yaml
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  profiles:
  - YourProfileName
```

</div>

For information about creating profiles, see the [Creating control plane profiles](ossm-profiles-users.md#ossm-control-plane-profiles_ossm-profiles-users).

For more detailed examples of security configuration, see [Mutual Transport Layer Security (mTLS)](ossm-security.md#ossm-security-mtls_ossm-security).

## techPreview parameters

The `spec.techPreview` parameter enables early access to features that are in Technology Preview.

> [!IMPORTANT]
> Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

## tracing parameters

The following example illustrates the `spec.tracing` parameters for the `ServiceMeshControlPlane` object, and a description of the available parameters with appropriate values.

<div class="formalpara">

<div class="title">

Example tracing parameters

</div>

``` yaml
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  version: v2.6
  tracing:
    sampling: 100
    type: Jaeger
```

</div>

<table>
<caption>Istio tracing parameters</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Values</th>
<th style="text-align: left;">Default value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>tracing:
 sampling:</code></pre></td>
<td style="text-align: left;"><p>The sampling rate determines how often the Envoy proxy generates a trace. You use the sampling rate to control what percentage of requests get reported to your tracing system.</p></td>
<td style="text-align: left;"><p>Integer values between 0 and 10000 representing increments of 0.01% (0 to 100%). For example, setting the value to <code>10</code> samples 0.1% of requests, setting the value to <code>100</code> will sample 1% of requests setting the value to <code>500</code> samples 5% of requests, and a setting of <code>10000</code> samples 100% of requests.</p></td>
<td style="text-align: left;"><p><code>10000</code> (100% of traces)</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>tracing:
 type:</code></pre></td>
<td style="text-align: left;"><p>Currently the only tracing type that is supported is <code>Jaeger</code>. Jaeger is enabled by default. To disable tracing, set the <code>type</code> parameter to <code>None</code>.</p></td>
<td style="text-align: left;"><p><code>None</code>, <code>Jaeger</code></p></td>
<td style="text-align: left;"><p><code>Jaeger</code></p></td>
</tr>
</tbody>
</table>

## version parameter

The Red Hat OpenShift Service Mesh Operator supports installation of different versions of the `ServiceMeshControlPlane`. You use the version parameter to specify what version of the Service Mesh control plane to install. If you do not specify a version parameter when creating your SMCP, the Operator sets the value to the latest version: (2.6). Existing `ServiceMeshControlPlane` objects keep their version setting during upgrades of the Operator.

## 3scale configuration

The following table explains the parameters for the 3scale Istio Adapter in the `ServiceMeshControlPlane` resource.

<div class="formalpara">

<div class="title">

Example 3scale parameters

</div>

``` yaml
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  addons:
    3Scale:
      enabled: false
      PARAM_THREESCALE_LISTEN_ADDR: 3333
      PARAM_THREESCALE_LOG_LEVEL: info
      PARAM_THREESCALE_LOG_JSON: true
      PARAM_THREESCALE_LOG_GRPC: false
      PARAM_THREESCALE_REPORT_METRICS: true
      PARAM_THREESCALE_METRICS_PORT: 8080
      PARAM_THREESCALE_CACHE_TTL_SECONDS: 300
      PARAM_THREESCALE_CACHE_REFRESH_SECONDS: 180
      PARAM_THREESCALE_CACHE_ENTRIES_MAX: 1000
      PARAM_THREESCALE_CACHE_REFRESH_RETRIES: 1
      PARAM_THREESCALE_ALLOW_INSECURE_CONN: false
      PARAM_THREESCALE_CLIENT_TIMEOUT_SECONDS: 10
      PARAM_THREESCALE_GRPC_CONN_MAX_SECONDS: 60
      PARAM_USE_CACHED_BACKEND: false
      PARAM_BACKEND_CACHE_FLUSH_INTERVAL_SECONDS: 15
      PARAM_BACKEND_CACHE_POLICY_FAIL_CLOSED: true
# ...
```

</div>

| Parameter | Description | Values | Default value |
|----|----|----|----|
| `enabled` | Whether to use the 3scale adapter | `true`/`false` | `false` |
| `PARAM_THREESCALE_LISTEN_ADDR` | Sets the listen address for the gRPC server | Valid port number | `3333` |
| `PARAM_THREESCALE_LOG_LEVEL` | Sets the minimum log output level. | `debug`, `info`, `warn`, `error`, or `none` | `info` |
| `PARAM_THREESCALE_LOG_JSON` | Controls whether the log is formatted as JSON | `true`/`false` | `true` |
| `PARAM_THREESCALE_LOG_GRPC` | Controls whether the log contains gRPC info | `true`/`false` | `true` |
| `PARAM_THREESCALE_REPORT_METRICS` | Controls whether 3scale system and backend metrics are collected and reported to Prometheus | `true`/`false` | `true` |
| `PARAM_THREESCALE_METRICS_PORT` | Sets the port that the 3scale `/metrics` endpoint can be scrapped from | Valid port number | `8080` |
| `PARAM_THREESCALE_CACHE_TTL_SECONDS` | Time period, in seconds, to wait before purging expired items from the cache | Time period in seconds | `300` |
| `PARAM_THREESCALE_CACHE_REFRESH_SECONDS` | Time period before expiry when cache elements are attempted to be refreshed | Time period in seconds | `180` |
| `PARAM_THREESCALE_CACHE_ENTRIES_MAX` | Max number of items that can be stored in the cache at any time. Set to `0` to disable caching | Valid number | `1000` |
| `PARAM_THREESCALE_CACHE_REFRESH_RETRIES` | The number of times unreachable hosts are retried during a cache update loop | Valid number | `1` |
| `PARAM_THREESCALE_ALLOW_INSECURE_CONN` | Allow to skip certificate verification when calling `3scale` APIs. Enabling this is not recommended. | `true`/`false` | `false` |
| `PARAM_THREESCALE_CLIENT_TIMEOUT_SECONDS` | Sets the number of seconds to wait before terminating requests to 3scale System and Backend | Time period in seconds | `10` |
| `PARAM_THREESCALE_GRPC_CONN_MAX_SECONDS` | Sets the maximum amount of seconds (+/-10% jitter) a connection may exist before it is closed | Time period in seconds | 60 |
| `PARAM_USE_CACHE_BACKEND` | If true, attempt to create an in-memory apisonator cache for authorization requests | `true`/`false` | `false` |
| `PARAM_BACKEND_CACHE_FLUSH_INTERVAL_SECONDS` | If the backend cache is enabled, this sets the interval in seconds for flushing the cache against 3scale | Time period in seconds | 15 |
| `PARAM_BACKEND_CACHE_POLICY_FAIL_CLOSED` | Whenever the backend cache cannot retrieve authorization data, whether to deny (closed) or allow (open) requests | `true`/`false` | `true` |

3scale parameters

# status parameter

The `status` parameter describes the current state of your service mesh. This information is generated by the Operator and is read-only.

| Name | Description | Type |
|----|----|----|
| `observedGeneration` | The generation observed by the controller during the most recent reconciliation. The information in the status pertains to this particular generation of the object. The `status.conditions` are not up-to-date if the `status.observedGeneration` field does not match `metadata.generation`. | integer |
| `annotations` | The `annotations` parameter stores additional, usually redundant status information, such as the number of components deployed by the `ServiceMeshControlPlane` object. These statuses are used by the command-line tool, `oc`, which does not yet allow counting objects in JSONPath expressions. | Not configurable |
| `readiness` | The readiness status of components and owned resources. | string |
| `operatorVersion` | The version of the Operator that last processed this resource. | string |
| `components` | Shows the status of each deployed Service Mesh control plane component. | string |
| `appliedSpec` | The resulting specification of the configuration options after all profiles have been applied. | `ControlPlaneSpec` |
| `conditions` | Represents the latest available observations of the object’s current state. `Reconciled` indicates that the Operator has finished reconciling the actual state of deployed components with the configuration in the `ServiceMeshControlPlane` resource. `Installed` indicates that the Service Mesh control plane has been installed. `Ready` indicates that all Service Mesh control plane components are ready. | string |
| `chartVersion` | The version of the charts that were last processed for this resource. | string |
| `appliedValues` | The resulting `values.yaml` file that was used to generate the charts. | `ControlPlaneSpec` |

Istio status parameters

# Additional resources

- For more information about how to configure the features in the `ServiceMeshControlPlane` resource, see the following links:

  - [Security](ossm-security.md#ossm-security-mtls_ossm-security)

  - [Traffic management](ossm-traffic-manage.md#ossm-routing-bookinfo_traffic-management)

  - [Metrics and traces](ossm-observability.md#ossm-observability)
