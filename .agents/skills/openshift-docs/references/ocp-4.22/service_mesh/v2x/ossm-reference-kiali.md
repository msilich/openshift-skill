<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When the Service Mesh Operator creates the `ServiceMeshControlPlane` it also processes the Kiali resource. The Kiali Operator then uses this object when creating Kiali instances.

# Specifying Kiali configuration in the SMCP

You can configure Kiali under the `addons` section of the `ServiceMeshControlPlane` resource. Kiali is enabled by default. To disable Kiali, set `spec.addons.kiali.enabled` to `false`.

You can specify your Kiali configuration in either of two ways:

- Specify the Kiali configuration in the `ServiceMeshControlPlane` resource under `spec.addons.kiali.install`. This approach has some limitations, because the complete list of Kiali configurations is not available in the SMCP.

- Configure and deploy a Kiali instance and specify the name of the Kiali resource as the value for `spec.addons.kiali.name` in the `ServiceMeshControlPlane` resource. You must create the CR in the same namespace as the Service Mesh control plane, for example, `istio-system`. If a Kiali resource matching the value of `name` exists, the control plane will configure that Kiali resource for use with the control plane. This approach lets you fully customize your Kiali configuration in the Kiali resource. Note that with this approach, various fields in the Kiali resource are overwritten by the Service Mesh Operator, specifically, the `accessible_namespaces` list, as well as the endpoints for Grafana, Prometheus, and tracing.

<div class="formalpara">

<div class="title">

Example SMCP parameters for Kiali

</div>

``` yaml
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  addons:
    kiali:
      name: kiali
      enabled: true
      install:
        dashboard:
          viewOnly: false
          enableGrafana: true
          enableTracing: true
          enablePrometheus: true
        service:
          ingress:
            contextPath: /kiali
```

</div>

<table>
<caption><code>ServiceMeshControlPlane</code> Kiali parameters</caption>
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
<td style="text-align: left;"><pre><code>spec:
  addons:
    kiali:
      name:</code></pre></td>
<td style="text-align: left;"><p>Name of Kiali custom resource. If a Kiali CR matching the value of <code>name</code> exists, the Service Mesh Operator will use that CR for the installation. If no Kiali CR exists, the Operator will create one using this <code>name</code> and the configuration options specified in the SMCP.</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p><code>kiali</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  enabled:</code></pre></td>
<td style="text-align: left;"><p>This parameter enables or disables Kiali. Kiali is enabled by default.</p></td>
<td style="text-align: left;"><p><code>true</code>/<code>false</code></p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:</code></pre></td>
<td style="text-align: left;"><p>Install a Kiali resource if the named Kiali resource is not present. The <code>install</code> section is ignored if <code>addons.kiali.enabled</code> is set to <code>false</code>.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    dashboard:</code></pre></td>
<td style="text-align: left;"><p>Configuration parameters for the dashboards shipped with Kiali.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    dashboard:
      viewOnly:</code></pre></td>
<td style="text-align: left;"><p>This parameter enables or disables view-only mode for the Kiali console. When view-only mode is enabled, users cannot use the Kiali console to make changes to the Service Mesh.</p></td>
<td style="text-align: left;"><p><code>true</code>/<code>false</code></p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    dashboard:
      enableGrafana:</code></pre></td>
<td style="text-align: left;"><p>Grafana endpoint configured based on <code>spec.addons.grafana</code> configuration.</p></td>
<td style="text-align: left;"><p><code>true</code>/<code>false</code></p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    dashboard:
      enablePrometheus:</code></pre></td>
<td style="text-align: left;"><p>Prometheus endpoint configured based on <code>spec.addons.prometheus</code> configuration.</p></td>
<td style="text-align: left;"><p><code>true</code>/<code>false</code></p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    dashboard:
      enableTracing:</code></pre></td>
<td style="text-align: left;"><p>Tracing endpoint configured based on Jaeger custom resource configuration.</p></td>
<td style="text-align: left;"><p><code>true</code>/<code>false</code></p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    service:</code></pre></td>
<td style="text-align: left;"><p>Configuration parameters for the Kubernetes service associated with the Kiali installation.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    service:
      metadata:</code></pre></td>
<td style="text-align: left;"><p>Use to specify additional metadata to apply to resources.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    service:
      metadata:
        annotations:</code></pre></td>
<td style="text-align: left;"><p>Use to specify additional annotations to apply to the component’s service.</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    service:
      metadata:
        labels:</code></pre></td>
<td style="text-align: left;"><p>Use to specify additional labels to apply to the component’s service.</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    service:
      ingress:</code></pre></td>
<td style="text-align: left;"><p>Use to specify details for accessing the component’s service through an OpenShift Route.</p></td>
<td style="text-align: left;"><p>N/A</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    service:
      ingress:
        metadata:
          annotations:</code></pre></td>
<td style="text-align: left;"><p>Use to specify additional annotations to apply to the component’s service ingress.</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    service:
      ingress:
        metadata:
          labels:</code></pre></td>
<td style="text-align: left;"><p>Use to specify additional labels to apply to the component’s service ingress.</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    service:
      ingress:
        enabled:</code></pre></td>
<td style="text-align: left;"><p>Use to customize an OpenShift Route for the service associated with a component.</p></td>
<td style="text-align: left;"><p><code>true</code>/<code>false</code></p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    service:
      ingress:
        contextPath:</code></pre></td>
<td style="text-align: left;"><p>Use to specify the context path to the service.</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>install:
  service:
    ingress:
      hosts:</code></pre></td>
<td style="text-align: left;"><p>Use to specify a single hostname per OpenShift route. An empty hostname implies a default hostname for the Route.</p></td>
<td style="text-align: left;"><p>string</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>install:
  service:
    ingress:
      tls:</code></pre></td>
<td style="text-align: left;"><p>Use to configure the TLS for the OpenShift route.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>kiali:
  install:
    service:
      nodePort:</code></pre></td>
<td style="text-align: left;"><p>Use to specify the <code>nodePort</code> for the component’s service <code>Values.&lt;component&gt;.service.nodePort.port</code></p></td>
<td style="text-align: left;"><p>integer</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
</tbody>
</table>

# Specifying Kiali configuration in a Kiali custom resource

You can fully customize your Kiali deployment by configuring Kiali in the Kiali custom resource (CR) rather than in the `ServiceMeshControlPlane` (SMCP) resource. This configuration is sometimes called an "external Kiali" since the configuration is specified outside of the SMCP.

> [!NOTE]
> You must deploy the `ServiceMeshControlPlane` and Kiali custom resources in the same namespace. For example, `istio-system`.

You can configure and deploy a Kiali instance and then specify the `name` of the Kiali resource as the value for `spec.addons.kiali.name` in the SMCP resource. If a Kiali CR matching the value of `name` exists, the Service Mesh control plane will use the existing installation. This approach lets you fully customize your Kiali configuration.
