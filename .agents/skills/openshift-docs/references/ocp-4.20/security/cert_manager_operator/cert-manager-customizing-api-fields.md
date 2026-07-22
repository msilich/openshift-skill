<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can customize the cert-manager Operator for Red Hat OpenShift after installation to suit your cluster requirements.

- Configure the `CertManager` custom resource (CR) to modify the behavior of cert-manager components, such as the cert-manager controller, CA injector, and webhook.

- Set environment variables for the controller pod.

- Define resource requests and limits to manage CPU and memory usage.

- Configure scheduling rules to control where pods run in your cluster.

- Configure the cluster `APIServer` custom resource (CR) to apply the cluster-wide TLS security profile to cert-manager components.

<div class="formalpara">

<div class="title">

Example CertManager CR YAML file

</div>

``` yaml
apiVersion: operator.openshift.io/v1alpha1
kind: CertManager
metadata:
  name: cluster
spec:
  controllerConfig:
    overrideArgs:
      - "--dns01-recursive-nameservers=8.8.8.8:53,1.1.1.1:53"
    overrideEnv:
      - name: HTTP_PROXY
        value: http://proxy.example.com:8080
    overrideResources:
      limits:
        cpu: "200m"
        memory: "512Mi"
      requests:
        cpu: "100m"
        memory: "256Mi"
    overrideScheduling:
      nodeSelector:
        custom: "label"
      tolerations:
        - key: "key1"
          operator: "Equal"
          value: "value1"
          effect: "NoSchedule"
    overrideReplicas: 2
#...

  webhookConfig:
    overrideArgs:
#...
    overrideResources:
#...
    overrideScheduling:
#...
    overrideReplicas:
#...

  cainjectorConfig:
    overrideArgs:
#...
    overrideResources:
#...
    overrideScheduling:
#...
    overrideReplicas:
#...
```

</div>

> [!WARNING]
> To override unsupported arguments, you can add `spec.unsupportedConfigOverrides` section in the `CertManager` resource, but using `spec.unsupportedConfigOverrides` is unsupported.

# Explanation of fields in the CertManager custom resource

To configure core components of the cert-manager Operator for Red Hat OpenShift, use the CertManager custom resource (CR). You can define settings for the cert-manager controller, such as the spec.controllerConfig field, to customize your deployment.

The core components of the cert-manager Operator for Red Hat OpenShift are as follows:

- Cert-manager controller: You can use the `spec.controllerConfig` field to configure the cert‑manager controller pod.

- Webhook: You can use the `spec.webhookConfig` field to configure the webhook pod, which handles validation and mutation requests.

- CA injector: You can use the `spec.cainjectorConfig` field to configure the CA injector pod.

## Common configurable fields in the CertManager CR for the cert-manager components

The following table lists the common fields that you can configure in the `spec.controllerConfig`, `spec.webhookConfig`, and `spec.cainjectorConfig` sections in the `CertManager` CR.

<table>
<caption>Common configurable fields in the CertManager CR for the cert-manager components</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>overrideArgs</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>You can override the supported arguments for the cert-manager components.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>overrideEnv</code></p></td>
<td style="text-align: left;"><p><code>dict</code></p></td>
<td style="text-align: left;"><p>You can override the supported environment variables for the cert-manager controller. This field is only supported for the cert-manager controller component.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>overrideReplicas</code></p></td>
<td style="text-align: left;"><p><code>int</code></p></td>
<td style="text-align: left;"><p>You can configure the replicas for the cert-manager components. The default value is <code>1</code>. For production environments, the following replica counts are recommended:</p>
<ul>
<li><p>controller: 2</p></li>
<li><p>cainjector: 2</p></li>
<li><p>webhook: At least 3.</p></li>
</ul>
<p>For more information, see <a href="https://cert-manager.io/docs/installation/best-practice/#high-availability">High Availability</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>overrideResources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>You can configure the CPU and memory limits for the cert-manager components.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>overrideScheduling</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>You can configure the pod scheduling constraints for the cert-manager components.</p></td>
</tr>
</tbody>
</table>

## Overridable arguments for the cert-manager components

You can configure the overridable arguments for the cert-manager components in the `spec.controllerConfig`, `spec.webhookConfig`, and `spec.cainjectorConfig` sections in the `CertManager` CR.

The following table describes the overridable arguments for the cert-manager components:

<table>
<caption>Overridable arguments for the cert-manager components</caption>
<colgroup>
<col style="width: 45%" />
<col style="width: 18%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Argument</th>
<th style="text-align: left;">Component</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>--dns01-recursive-nameservers=&lt;server_address&gt;</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>Provide a comma-separated list of nameservers to query for the DNS-01 self check. The nameservers can be specified either as <code>&lt;host&gt;:&lt;port&gt;</code>, for example, <code>1.1.1.1:53</code>, or use DNS over HTTPS (DoH), for example, <code>https://1.1.1.1/dns-query</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>DNS over HTTPS (DoH) is supported starting only from cert-manager Operator for Red Hat OpenShift version 1.13.0 and later.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--dns01-recursive-nameservers-only</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>Specify to only use recursive nameservers instead of checking the authoritative nameservers associated with that domain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--acme-http01-solver-nameservers=&lt;host&gt;:&lt;port&gt;</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>Provide a comma-separated list of <code>&lt;host&gt;:&lt;port&gt;</code> nameservers to query for the Automated Certificate Management Environment (ACME) HTTP01 self check. For example, <code>--acme-http01-solver-nameservers=1.1.1.1:53</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--metrics-listen-address=&lt;host&gt;:&lt;port&gt;</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>Specify the host and port for the metrics endpoint. The default value is <code>--metrics-listen-address=0.0.0.0:9402</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--issuer-ambient-credentials</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>You can use this argument to configure an ACME Issuer to solve DNS-01 challenges by using ambient credentials.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--enable-certificate-owner-ref</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>This argument sets the certificate resource as an owner of the secret where the TLS certificate is stored. For more information, see "Deleting a TLS secret automatically upon Certificate removal".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--acme-http01-solver-resource-limits-cpu</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>Defines the maximum CPU limit for ACME HTTP‑01 solver pods. The default value is <code>100m</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--acme-http01-solver-resource-limits-memory</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>Defines the maximum memory limit for ACME HTTP‑01 solver pods. The default value is <code>64Mi</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--acme-http01-solver-resource-request-cpu</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>Defines the minimum CPU request for ACME HTTP‑01 solver pods. The default value is <code>10m</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--acme-http01-solver-resource-request-memory</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>Defines the minimum memory request for ACME HTTP‑01 solver pods. The default value is <code>64Mi</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--certificate-request-minimum-backoff-duration</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>Specify the minimum backoff duration for certificate requests. The default value is <code>1h0m0s</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--concurrent-workers</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>The number of concurrent workers for each controller. The default value is <code>5</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--kube-api-qps</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>The maximum number of queries per second sent to the Kubernetes API server. The default value is <code>20</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--kube-api-burst</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>The maximum burst of queries per second sent to the Kubernetes API server. Must be greater than or equal to <code>--kube-api-qps</code>. The default value is <code>50</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--max-concurrent-challenges</code></p></td>
<td style="text-align: left;"><p>Controller</p></td>
<td style="text-align: left;"><p>The maximum number of ACME challenges that can run concurrently. The default value is <code>60</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--v=&lt;verbosity_level&gt;</code></p></td>
<td style="text-align: left;"><p>Controller, Webhook, CA injector</p></td>
<td style="text-align: left;"><p>Specify the log level verbosity to determine the verbosity of log messages.</p></td>
</tr>
</tbody>
</table>

## Overridable environment variables for the cert-manager controller

You can configure the overridable environment variables for the cert-manager controller in the `spec.controllerConfig.overrideEnv` field in the `CertManager` CR.

The following table describes the overridable environment variables for the cert-manager controller:

| Environment variable | Description                                          |
|----------------------|------------------------------------------------------|
| `HTTP_PROXY`         | Proxy server for outgoing HTTP requests.             |
| `HTTPS_PROXY`        | Proxy server for outgoing HTTPS requests.            |
| `NO_PROXY`           | Comma‑separated list of hosts that bypass the proxy. |

Overridable environment variables for the cert-manager controller

## Overridable resource parameters for the cert-manager components

You can configure the CPU and memory limits for the cert-manager components in the `spec.controllerConfig`, `spec.webhookConfig`, and `spec.cainjectorConfig` sections in the `CertManager` CR.

The following table describes the overridable resource parameters for the cert-manager components:

| Field | Description |
|----|----|
| `overrideResources.limits.cpu` | Defines the maximum amount of CPU that a component pod can use. |
| `overrideResources.limits.memory` | Defines the maximum amount of memory that a component pod can use. |
| `overrideResources.requests.cpu` | Defines the minimum amount of CPU requested by the scheduler for a component pod. |
| `overrideResources.requests.memory` | Defines the minimum amount of memory requested by the scheduler for a component pod. |

Overridable resource parameters for the cert-manager components

## Overridable scheduling parameters for the cert-manager components

You can configure the pod scheduling constraints for the cert-manager components in the `spec.controllerConfig`, `spec.webhookConfig` field, and `spec.cainjectorConfig` sections in the `CertManager` CR.

The following table describes the pod scheduling parameters for the cert-manager components:

| Field | Description |
|----|----|
| `overrideScheduling.nodeSelector` | Key‑value pairs to constrain pods to specific nodes. |
| `overrideScheduling.tolerations` | List of tolerations to schedule pods on tainted nodes. |

Overridable scheduling parameters for the cert-manager components

<div>

<div class="title">

Additional resources

</div>

- [Deleting a TLS secret automatically upon Certificate removal](cert-manager-customizing-api-fields.md#cert-manager-override-flag-controller_cert-manager-customizing-api-fields)

</div>

# Customizing cert-manager by overriding environment variables from the cert-manager Operator API

To refine your deployment for specific operational requirements, override supported environment variables for the cert-manager Operator for Red Hat OpenShift. You can customize these variables through the Operator API to apply configurations, such as proxy settings or system-level adjustments, that differ from the default values.

You can override the supported environment variables for the cert-manager Operator for Red Hat OpenShift by adding a `spec.controllerConfig` section in the `CertManager` resource.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `CertManager` resource by running the following command:

    ``` terminal
    $ oc edit certmanager cluster
    ```

2.  Add a `spec.controllerConfig` section with the following override arguments:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: CertManager
    metadata:
      name: cluster
      ...
    spec:
      ...
      controllerConfig:
        overrideEnv:
          - name: HTTP_PROXY
            value: http://<proxy_url>
          - name: HTTPS_PROXY
            value: https://<proxy_url>
          - name: NO_PROXY
            value: <ignore_proxy_domains>
    ```

    where:

    `HTTP_PROXY`
    Specifies the proxy server URL.

    `NO_PROXY`
    Specifies a comma separated list of domains. These domains are ignored by the proxy server.

    > [!NOTE]
    > For more information about the overridable environment variables, see "Overridable environment variables for the cert-manager components" in "Explanation of fields in the CertManager custom resource".

3.  Save your changes and quit the text editor to apply your changes.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the cert-manager controller pod is redeployed by running the following command:

    ``` terminal
    $ oc get pods -l app.kubernetes.io/name=cert-manager -n cert-manager
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                          READY   STATUS    RESTARTS   AGE
    cert-manager-bd7fbb9fc-wvbbt  1/1     Running   0          39s
    ```

    </div>

2.  Verify that environment variables are updated for the cert-manager pod by running the following command:

    ``` terminal
    $ oc get pod <redeployed_cert-manager_controller_pod> -n cert-manager -o yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
        env:
        ...
        - name: HTTP_PROXY
          value: http://<PROXY_URL>
        - name: HTTPS_PROXY
          value: https://<PROXY_URL>
        - name: NO_PROXY
          value: <IGNORE_PROXY_DOMAINS>
    ```

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Explanation of fields in the CertManager custom resource](cert-manager-customizing-api-fields.md#cert-manager-explanation-of-certmanager-cr-fields_cert-manager-customizing-api-fields)

</div>

# Customizing cert-manager by overriding arguments from the cert-manager Operator API

You can override the supported arguments for the cert-manager Operator for Red Hat OpenShift by adding a `spec.controllerConfig` section in the `CertManager` resource.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `CertManager` resource by running the following command:

    ``` terminal
    $ oc edit certmanager cluster
    ```

2.  Add a `spec.controllerConfig` section with the following override arguments:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: CertManager
    metadata:
      name: cluster
      ...
    spec:
      ...
      controllerConfig:
        overrideArgs:
          - '--dns01-recursive-nameservers=<server_address>'
          - '--dns01-recursive-nameservers-only'
          - '--acme-http01-solver-nameservers=<host>:<port>'
          - '--v=<verbosity_level>'
          - '--metrics-listen-address=<host>:<port>'
          - '--issuer-ambient-credentials'
          - '--acme-http01-solver-resource-limits-cpu=<quantity>'
          - '--acme-http01-solver-resource-limits-memory=<quantity>'
          - '--acme-http01-solver-resource-request-cpu=<quantity>'
          - '--acme-http01-solver-resource-request-memory=<quantity>'
          - '--certificate-request-minimum-backoff-duration=<duration>'
          - '--concurrent-workers=<quantity>'
          - '--kube-api-qps=<quantity>'
          - '--kube-api-burst=<quantity>'
          - '--max-concurrent-challenges=<quantity>'
      webhookConfig:
        overrideArgs:
          - '--v=<verbosity_level>'
      cainjectorConfig:
        overrideArgs:
          - '--v=<verbosity_level>'
    ```

    For information about the overridable aruguments, see "Overridable arguments for the cert-manager components" in "Explanation of fields in the CertManager custom resource".

3.  Save your changes and quit the text editor to apply your changes.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that arguments are updated for cert-manager pods by running the following command:

  ``` terminal
  $ oc get pods -n cert-manager -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` yaml
  ...
    metadata:
      name: cert-manager-6d4b5d4c97-kldwl
      namespace: cert-manager
  ...
    spec:
      containers:
      - args:
        # ...
          - --acme-http01-solver-nameservers=1.1.1.1:53
          - --concurrent-workers=5
          - --dns01-recursive-nameservers=1.1.1.1:53
          - --dns01-recursive-nameservers-only
          - --kube-api-burst=50
          - --kube-api-qps=20
          - --max-concurrent-challenges=60
          - --metrics-listen-address=0.0.0.0:9042
          - --v=6
  ...
    metadata:
      name: cert-manager-cainjector-866c4fd758-ltxxj
      namespace: cert-manager
  ...
    spec:
      containers:
      - args:
        # ...
          - --v=2
  ...
    metadata:
      name: cert-manager-webhook-6d48f88495-c88gd
      namespace: cert-manager
  ...
    spec:
      containers:
      - args:
        # ...
          - --v=2
  ```

  </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Explanation of fields in the CertManager custom resource](cert-manager-customizing-api-fields.md#cert-manager-explanation-of-certmanager-cr-fields_cert-manager-customizing-api-fields)

</div>

# Deleting a TLS secret automatically upon Certificate removal

You can enable the `--enable-certificate-owner-ref` flag for the cert-manager Operator for Red Hat OpenShift by adding a `spec.controllerConfig` section in the `CertManager` resource. The `--enable-certificate-owner-ref` flag sets the certificate resource as an owner of the secret where the TLS certificate is stored.

> [!WARNING]
> If you uninstall the cert-manager Operator for Red Hat OpenShift or delete certificate resources from the cluster, the secret is deleted automatically. This might cause network connectivity issues depending upon where the certificate TLS secret is being used.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.

- You have installed version 1.12.0 or later of the cert-manager Operator for Red Hat OpenShift.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check that the `Certificate` object and its secret are available by running the following command:

    ``` terminal
    $ oc get certificate
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                             READY   SECRET                                           AGE
    certificate-from-clusterissuer-route53-ambient   True    certificate-from-clusterissuer-route53-ambient   8h
    ```

    </div>

2.  Edit the `CertManager` resource by running the following command:

    ``` terminal
    $ oc edit certmanager cluster
    ```

3.  Add a `spec.controllerConfig` section with the following override arguments:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: CertManager
    metadata:
      name: cluster
    # ...
    spec:
    # ...
      controllerConfig:
        overrideArgs:
          - '--enable-certificate-owner-ref'
    ```

4.  Save your changes and quit the text editor to apply your changes.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `--enable-certificate-owner-ref` flag is updated for cert-manager controller pod by running the following command:

  ``` terminal
  $ oc get pods -l app.kubernetes.io/name=cert-manager -n cert-manager -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` yaml
  # ...
    metadata:
      name: cert-manager-6e4b4d7d97-zmdnb
      namespace: cert-manager
  # ...
    spec:
      containers:
      - args:
        - --enable-certificate-owner-ref
  ```

  </div>

</div>

# Overriding CPU and memory limits for the cert-manager components

To ensure stable resource allocation and operation, configure CPU and memory limits for cert-manager Operator for Red Hat OpenShift components. You can set specific constraints for the cert-manager controller, CA injector, and Webhook to align with your specific cluster requirements.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.

- You have installed version 1.12.0 or later of the cert-manager Operator for Red Hat OpenShift.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check that the deployments of the cert-manager controller, CA injector, and Webhook are available by entering the following command:

    ``` terminal
    $ oc get deployment -n cert-manager
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
    cert-manager              1/1     1            1           53m
    cert-manager-cainjector   1/1     1            1           53m
    cert-manager-webhook      1/1     1            1           53m
    ```

    </div>

2.  Before setting the CPU and memory limit, check the existing configuration for the cert-manager controller, CA injector, and Webhook by entering the following command:

    ``` terminal
    $ oc get deployment -n cert-manager -o yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    # ...
      metadata:
        name: cert-manager
        namespace: cert-manager
    # ...
      spec:
        template:
          spec:
            containers:
            - name: cert-manager-controller
              resources: {}
    # ...
      metadata:
        name: cert-manager-cainjector
        namespace: cert-manager
    # ...
      spec:
        template:
          spec:
            containers:
            - name: cert-manager-cainjector
              resources: {}
    # ...
      metadata:
        name: cert-manager-webhook
        namespace: cert-manager
    # ...
      spec:
        template:
          spec:
            containers:
            - name: cert-manager-webhook
              resources: {}
    # ...
    ```

    </div>

    The `spec.resources` field is empty by default. The cert-manager components do not have CPU and memory limits.

3.  To configure the CPU and memory limits for the cert-manager controller, CA injector, and Webhook, enter the following command:

    ``` terminal
    $ oc patch certmanager.operator cluster --type=merge -p="
    spec:
      controllerConfig:
        overrideResources:
          limits:
            cpu: 200m
            memory: 64Mi
          requests:
            cpu: 10m
            memory: 16Mi
      webhookConfig:
        overrideResources:
          limits:
            cpu: 200m
            memory: 64Mi
          requests:
            cpu: 10m
            memory: 16Mi
      cainjectorConfig:
        overrideResources:
          limits:
            cpu: 200m
            memory: 64Mi
          requests:
            cpu: 10m
            memory: 16Mi
    "
    ```

    For information about the overridable resource parameters, see "Overridable resource parameters for the cert-manager components" in "Explanation of fields in the CertManager custom resource".

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    certmanager.operator.openshift.io/cluster patched
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the CPU and memory limits are updated for the cert-manager components:

    ``` terminal
    $ oc get deployment -n cert-manager -o yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    # ...
      metadata:
        name: cert-manager
        namespace: cert-manager
    # ...
      spec:
        template:
          spec:
            containers:
            - name: cert-manager-controller
              resources:
                limits:
                  cpu: 200m
                  memory: 64Mi
                requests:
                  cpu: 10m
                  memory: 16Mi
    # ...
      metadata:
        name: cert-manager-cainjector
        namespace: cert-manager
    # ...
      spec:
        template:
          spec:
            containers:
            - name: cert-manager-cainjector
              resources:
                limits:
                  cpu: 200m
                  memory: 64Mi
                requests:
                  cpu: 10m
                  memory: 16Mi
    # ...
      metadata:
        name: cert-manager-webhook
        namespace: cert-manager
    # ...
      spec:
        template:
          spec:
            containers:
            - name: cert-manager-webhook
              resources:
                limits:
                  cpu: 200m
                  memory: 64Mi
                requests:
                  cpu: 10m
                  memory: 16Mi
    # ...
    ```

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Explanation of fields in the CertManager custom resource](cert-manager-customizing-api-fields.md#cert-manager-explanation-of-certmanager-cr-fields_cert-manager-customizing-api-fields)

</div>

# Configuring scheduling overrides for cert-manager components

You can configure the pod scheduling from the cert-manager Operator for Red Hat OpenShift API for the cert-manager Operator for Red Hat OpenShift components, such as the cert-manager controller, CA injector, and Webhook.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.

- You have installed version 1.15.0 or later of the cert-manager Operator for Red Hat OpenShift.

</div>

<div>

<div class="title">

Procedure

</div>

- Update the `certmanager.operator` custom resource to configure pod scheduling overrides for the desired components by running the following command. Use the `overrideScheduling` field under the `controllerConfig`, `webhookConfig`, or `cainjectorConfig` sections to define `nodeSelector` and `tolerations` settings.

  ``` terminal
  $ oc patch certmanager.operator cluster --type=merge -p="
  spec:
    controllerConfig:
      overrideScheduling:
        nodeSelector:
          node-role.kubernetes.io/control-plane: ''
        tolerations:
          - key: node-role.kubernetes.io/master
            operator: Exists
            effect: NoSchedule
    webhookConfig:
      overrideScheduling:
        nodeSelector:
          node-role.kubernetes.io/control-plane: ''
        tolerations:
          - key: node-role.kubernetes.io/master
            operator: Exists
            effect: NoSchedule
    cainjectorConfig:
      overrideScheduling:
        nodeSelector:
          node-role.kubernetes.io/control-plane: ''
        tolerations:
          - key: node-role.kubernetes.io/master
            operator: Exists
            effect: NoSchedule"
  "
  ```

  For information about the overridable scheduling parameters, see "Overridable scheduling parameters for the cert-manager components" in "Explanation of fields in the CertManager custom resource".

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify pod scheduling settings for `cert-manager` pods:

    1.  Check the deployments in the `cert-manager` namespace to confirm they have the correct `nodeSelector` and `tolerations` by running the following command:

        ``` terminal
        $ oc get pods -n cert-manager -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                                       READY   STATUS    RESTARTS   AGE   IP            NODE                         NOMINATED NODE   READINESS GATES
        cert-manager-58d9c69db4-78mzp              1/1     Running   0          10m   10.129.0.36   ip-10-0-1-106.ec2.internal   <none>           <none>
        cert-manager-cainjector-85b6987c66-rhzf7   1/1     Running   0          11m   10.128.0.39   ip-10-0-1-136.ec2.internal   <none>           <none>
        cert-manager-webhook-7f54b4b858-29bsp      1/1     Running   0          11m   10.129.0.35   ip-10-0-1-106.ec2.internal   <none>           <none>
        ```

        </div>

    2.  Check the `nodeSelector` and `tolerations` settings applied to deployments by running the following command:

        ``` terminal
        $ oc get deployments -n cert-manager -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{.spec.template.spec.nodeSelector}{"\n"}{.spec.template.spec.tolerations}{"\n\n"}{end}'
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        cert-manager
        {"kubernetes.io/os":"linux","node-role.kubernetes.io/control-plane":""}
        [{"effect":"NoSchedule","key":"node-role.kubernetes.io/master","operator":"Exists"}]

        cert-manager-cainjector
        {"kubernetes.io/os":"linux","node-role.kubernetes.io/control-plane":""}
        [{"effect":"NoSchedule","key":"node-role.kubernetes.io/master","operator":"Exists"}]

        cert-manager-webhook
        {"kubernetes.io/os":"linux","node-role.kubernetes.io/control-plane":""}
        [{"effect":"NoSchedule","key":"node-role.kubernetes.io/master","operator":"Exists"}]
        ```

        </div>

2.  Verify pod scheduling events in the `cert-manager` namespace by running the following command:

    ``` terminal
    $ oc get events -n cert-manager --field-selector reason=Scheduled
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Explanation of fields in the CertManager custom resource](cert-manager-customizing-api-fields.md#cert-manager-explanation-of-certmanager-cr-fields_cert-manager-customizing-api-fields)

</div>

# Configuring cluster TLS security profile adherence for cert-manager components

You can configure the cert-manager Operator for Red Hat OpenShift to apply the cluster-wide TLS security profile by setting the TLS adherence policy on the cluster `APIServer` resource. When the adherence policy is set to `StrictAllComponents`, cert-manager components automatically apply the cluster TLS security profile settings.

> [!IMPORTANT]
> TLS adherence for cert-manager operands is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You installed the cert-manager Operator for Red Hat OpenShift.

- You enabled the `TechPreviewNoUpgrade` feature set. For more information, see "Enabling features using feature gates".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the cluster `APIServer` custom resource (CR) by running the following command:

    ``` terminal
    $ oc edit apiserver cluster
    ```

2.  Add or modify the `tlsAdherence` field in the `spec` section and set it to `StrictAllComponents` by using the following example:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: APIServer
    metadata:
      name: cluster
    spec:
      tlsSecurityProfile:
        type: Intermediate
        intermediate: {}
      tlsAdherence: StrictAllComponents
    ```

    where:

    `tlsSecurityProfile.type`
    Optional: Specifies the TLS security profile type. Valid values are `Old`, `Intermediate`, `Modern`, or `Custom`. If not specified, the default is `Intermediate`. When specifying a profile type, you must also include the corresponding profile-specific field, for example, `intermediate: {}` for the `Intermediate` profile.

    `tlsAdherence: StrictAllComponents`
    Specifies that cluster-wide TLS settings are enforced on all components, including cert-manager.

3.  Save the changes and exit the editor.

</div>

<div>

<div class="title">

Verification

</div>

1.  The cert-manager Operator for Red Hat OpenShift automatically applies the cluster TLS security profile to the cert-manager controller, webhook, and CA injector deployments. Check that the TLS configuration is applied to the cert-manager components. For more information, see "Verifying TLS security profile adherence for cert-manager components".

</div>

# Verifying TLS security profile adherence for cert-manager components

After configuring the cluster TLS security profile adherence, you can verify that the TLS configuration is applied to the cert-manager controller, webhook, and CA injector deployments.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You installed the cert-manager Operator for Red Hat OpenShift.

- You enabled the `TechPreviewNoUpgrade` feature set. For more information, see "Enabling features using feature gates".

- You configured the cluster TLS security profile adherence for cert-manager components. For more information, see "Configuring cluster TLS security profile adherence for cert-manager components".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the cert-manager controller deployment has the TLS configuration applied by running the following command:

    ``` terminal
    $ oc get deployment -n cert-manager cert-manager -o yaml | grep -A 15 "args:"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    args:
    - --v=2
    - --cluster-resource-namespace=$(POD_NAMESPACE)
    - --leader-election-namespace=kube-system
    - --acme-http01-solver-image=registry.redhat.io/cert-manager/cert-manager-acmesolver-rhel9@sha256:...
    - --max-concurrent-challenges=60
    - --metrics-tls-min-version=VersionTLS12
    - --metrics-tls-cipher-suites=TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
    ```

    </div>

    The `--metrics-tls-min-version` flag shows the minimum TLS version configured based on the cluster TLS security profile. The `--metrics-tls-cipher-suites` flag shows TLS cipher suites configured based on the cluster TLS security profile.

2.  Verify that the webhook deployment has the TLS configuration applied by running the following command:

    ``` terminal
    $ oc get deployment -n cert-manager cert-manager-webhook -o yaml | grep -A 20 "args:"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    args:
    - --v=2
    - --dynamic-serving-ca-secret-namespace=$(POD_NAMESPACE)
    - --dynamic-serving-ca-secret-name=cert-manager-webhook-ca
    - --dynamic-serving-dns-names=cert-manager-webhook
    - --tls-min-version=VersionTLS12
    - --tls-cipher-suites=TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
    - --metrics-tls-min-version=VersionTLS12
    - --metrics-tls-cipher-suites=TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
    ```

    </div>

    The webhook deployment includes serving TLS flags (`--tls-min-version` and `--tls-cipher-suites`) for the webhook HTTPS endpoint, and TLS flags for the metrics endpoint.

3.  Verify that the CA injector deployment has the TLS configuration applied by running the following command:

    ``` terminal
    $ oc get deployment -n cert-manager cert-manager-cainjector -o yaml | grep -A 10 "args:"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    args:
    - --v=2
    - --leader-election-namespace=kube-system
    - --metrics-tls-min-version=VersionTLS12
    - --metrics-tls-cipher-suites=TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
    ```

    </div>

    The CA injector deployment includes metrics endpoint TLS flags.

    > [!NOTE]
    > TLS profile enforcement is not available for the IstioCSR and TrustManager operands.
    >
    > When the cluster TLS security profile is set to `Modern` (TLS 1.3), the cipher suite flags are automatically omitted.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Understanding feature gates](../../nodes/clusters/nodes-cluster-enabling-features.md#nodes-cluster-enabling-features-about_nodes-cluster-enabling)

- [Understanding TLS security profiles](../tls-security-profiles.md#tls-profiles-understanding_tls-security-profiles)

</div>
