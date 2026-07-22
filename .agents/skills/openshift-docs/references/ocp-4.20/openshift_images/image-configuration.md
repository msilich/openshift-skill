<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure an image registry to store and serve container images.

# Image controller configuration parameters

You can configure certain parameters that handle images cluster-wide in the `spec` of the `image.config.openshift.io/cluster` resource.

> [!NOTE]
> The following non-configurable parameters are not listed in the table:
>
> - `DisableScheduledImport`
>
> - `MaxImagesBulkImportedPerRepository`
>
> - `MaxScheduledImportsPerMinute`
>
> - `ScheduledImageImportMinimumIntervalSeconds`
>
> - `InternalRegistryHostname`

<table>
<caption>Image controller configuration parameters</caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field name</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>kind.Image</code></p></td>
<td style="text-align: left;"><p>Holds cluster-wide information about how to handle images. The canonical, and only valid name for this CR is <code>cluster</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allowedRegistriesForImport</code></p></td>
<td style="text-align: left;"><p>Limits the container image registries from which normal users can import images. Set this list to the registries that you trust to contain valid images, and that you want applications to be able to import from. Users with permission to create images or <code>ImageStreamMappings</code> from the API are not affected by this policy. Typically only cluster administrators have the appropriate permissions.</p>
<p>Every element of this list contains a location of the registry specified by the registry domain name.</p>
<p><code>domainName</code>: Specifies a domain name for the registry. If the registry uses a non-standard <code>80</code> or <code>443</code> port, the port should be included in the domain name as well.</p>
<p><code>insecure</code>: Insecure indicates whether the registry is secure or insecure. By default, if not otherwise specified, the registry is assumed to be secure.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>additionalTrustedCA</code></p></td>
<td style="text-align: left;"><p>A reference to a config map containing additional CAs that should be trusted during <code>image stream import</code>, <code>pod image pull</code>, <code>openshift-image-registry pullthrough</code>, and builds.</p>
<p>The namespace for this config map is <code>openshift-config</code>. The format of the config map is to use the registry hostname as the key, and the PEM-encoded certificate as the value, for each additional registry CA to trust.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>externalRegistryHostnames</code></p></td>
<td style="text-align: left;"><p>Provides the hostnames for the default external image registry. The external hostname should be set only when the image registry is exposed externally. The first value is used in <code>publicDockerImageRepository</code> field in image streams. The value must be in <code>hostname[:port]</code> format.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registrySources</code></p></td>
<td style="text-align: left;"><p>Contains configuration that determines how the container runtime should treat individual registries when accessing images for builds and pods. For example, whether or not to allow insecure access. It does not contain configuration for the internal cluster registry.</p>
<p><code>insecureRegistries</code>: Registries that do not have a valid TLS certificate or only support HTTP connections. To specify all subdomains, add the asterisk (<code>*</code>) wildcard character as a prefix to the domain name. For example, <code>*.example.com</code>. You can specify an individual repository within a registry. For example: <code>reg1.io/myrepo/myapp:latest</code>.</p>
<p><code>blockedRegistries</code>: Registries for which image pull and push actions are denied. To specify all subdomains, add the asterisk (<code>*</code>) wildcard character as a prefix to the domain name. For example, <code>*.example.com</code>. You can specify an individual repository within a registry. For example: <code>reg1.io/myrepo/myapp:latest</code>. All other registries are allowed.</p>
<p><code>allowedRegistries</code>: Registries for which image pull and push actions are allowed. To specify all subdomains, add the asterisk (<code>*</code>) wildcard character as a prefix to the domain name. For example, <code>*.example.com</code>. You can specify an individual repository within a registry. For example: <code>reg1.io/myrepo/myapp:latest</code>. All other registries are blocked.</p>
<p><code>containerRuntimeSearchRegistries</code>: Registries for which image pull and push actions are allowed using image short names. All other registries are blocked.</p>
<p>You can set either <code>blockedRegistries</code> or <code>allowedRegistries</code>, but not both.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>imageStreamImportMode</code></p></td>
<td style="text-align: left;"><p>Controls the import mode behavior of image streams.</p>
<p>You must enable the <code>TechPreviewNoUpgrade</code> feature set in the <code>FeatureGate</code> custom resource (CR) to enable the <code>imageStreamImportMode</code> feature. For more information about feature gates, see "Understanding feature gates".</p>
<p>You can set the <code>imageStreamImportMode</code> field to either of the following values:</p>
<ul>
<li><p><code>Legacy</code>: Indicates that the legacy behavior must be used. The legacy behavior discards the manifest list and imports a single sub-manifest. In this case, the platform is chosen in the following order of priority:</p>
<ol type="1">
<li><p>Tag annotations: Determining the platform by using the platform-specific annotations in the image tags.</p></li>
<li><p>Control plane architecture or the operating system: Selecting the platform based on the architecture or the operating system of the control plane.</p></li>
<li><p><code>linux/amd64</code>: If no platform is selected by the preceeding methods, the <code>linux/amd64</code> platform is selected.</p></li>
<li><p>The first manifest in the list is selected.</p></li>
</ol></li>
<li><p><code>PreserveOriginal</code>: Indicates that the original manifest is preserved. The manifest list and its sub-manifests are imported.</p></li>
</ul>
<p>If you specify a value for this field, the value is applied to the newly created image stream tags that do not already have this value manually set.</p>
<p>If you do not configure this field, the behavior is decided based on the payload type advertised by the <code>ClusterVersion</code> status. In this case, the platform is chosen as follows:</p>
<ul>
<li><p>The single architecture payload implies that the <code>Legacy</code> mode is applicable.</p></li>
<li><p>The multi payload implies that the <code>PreserveOriginal</code> mode is applicable.</p></li>
</ul>
<p>For information about importing manifest lists, see "Working with manifest lists".</p>
<div class="important">
<div class="title">
&#10;</div>
<p><code>imageStreamImportMode</code> is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
</tbody>
</table>

> [!WARNING]
> When you define the `allowedRegistries` parameter, all registries, including `registry.redhat.io`, `quay.io`, and the default OpenShift image registry, are blocked unless explicitly listed. You must add all of the registries that your payload images require to the `allowedRegistries` list. For example, list `registry.redhat.io`, `quay.io`, and the `internalRegistryHostname` registries. For disconnected clusters, you must also add your mirror registries. Otherwise, you risk pod failure.

The `status` field of the `image.config.openshift.io/cluster` resource holds observed values from the cluster.

| Parameter | Description |
|----|----|
| `internalRegistryHostname` | Set by the Image Registry Operator, which controls the `internalRegistryHostname`. It sets the hostname for the default OpenShift image registry. The value must be in `hostname[:port]` format. For backward compatibility, you can still use the `OPENSHIFT_DEFAULT_REGISTRY` environment variable, but this setting overrides the environment variable. |
| `externalRegistryHostnames` | Set by the Image Registry Operator, provides the external hostnames for the image registry when it is exposed externally. The first value is used in `publicDockerImageRepository` field in image streams. The values must be in `hostname[:port]` format. |

Image controller status field parameters

# Machine Config Operator behavior and registry changes

The Machine Config Operator (MCO) watches the `image.config.openshift.io/cluster` custom resource (CR) for any changes to registries and takes specific steps when the registry changes.

When changes to the registry are applied to the `image.config.openshift.io/cluster` CR, the MCO performs the following sequential actions:

1.  Cordons the node; certain parameters result in drained nodes, and others do not

2.  Applies changes by restarting CRI-O

3.  Uncordons the node

    > [!NOTE]
    > The MCO does not restart nodes when it detects changes. During this period, you might experience service unavailability.

## When allowing and blocking registry sources

The MCO watches the `image.config.openshift.io/cluster` resource for any changes to the registries. When the MCO detects a change, it triggers a rollout on nodes in machine config pool (MCP). The allowed registries list is used to update the image signature policy in the `/etc/containers/policy.json` file on each node. Changes to the `/etc/containers/policy.json` file do not require the node to drain.

## When using the containerRuntimeSearchRegistries parameter

After the nodes return to the `Ready` state, if the `containerRuntimeSearchRegistries` parameter is added, the MCO creates a file in the `/etc/containers/registries.conf.d` directory on each node with the listed registries. The file overrides the default list of unqualified search registries in the `/etc/containers/registries.conf` file. There is no way to fall back to the default list of unqualified search registries.

> [!IMPORTANT]
> The `containerRuntimeSearchRegistries` parameter works only with the Podman and CRI-O container engines. The registries in the list can be used only in pod specs, not in builds and image streams.

# Configuring image registry settings

You can configure image registry settings by editing the `image.config.openshift.io/cluster` custom resource (CR).

<div>

<div class="title">

Procedure

</div>

1.  Edit the `image.config.openshift.io/cluster` CR by running the following command:

    ``` terminal
    $ oc edit image.config.openshift.io/cluster
    ```

    The following is an example `image.config.openshift.io/cluster` CR:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Image
    metadata:
      annotations:
        release.openshift.io/create-only: "true"
      creationTimestamp: "2019-05-17T13:44:26Z"
      generation: 1
      name: cluster
      resourceVersion: "8302"
      selfLink: /apis/config.openshift.io/v1/images/cluster
      uid: e34555da-78a9-11e9-b92b-06d6c7da38dc
    spec:
      allowedRegistriesForImport:
        - domainName: quay.io
          insecure: false
      additionalTrustedCA:
        name: myconfigmap
      registrySources:
        allowedRegistries:
        - example.com
        - quay.io
        - registry.redhat.io
        - image-registry.openshift-image-registry.svc:5000
        - reg1.io/myrepo/myapp:latest
        insecureRegistries:
        - insecure.com
    status:
      internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
    ```

    > [!NOTE]
    > When you use the `allowedRegistries`, `blockedRegistries`, or `insecureRegistries` parameter, you can specify an individual repository within a registry. For example: `reg1.io/myrepo/myapp:latest`.
    >
    > Avoid insecure external registries to reduce possible security risks.

</div>

<div>

<div class="title">

Verification

</div>

1.  To verify your changes, list your nodes by running the following command:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                         STATUS                     ROLES                  AGE   VERSION
    ip-10-0-137-182.us-east-2.compute.internal   Ready,SchedulingDisabled   worker                 65m   v1.33.4
    ip-10-0-139-120.us-east-2.compute.internal   Ready,SchedulingDisabled   control-plane          74m   v1.33.4
    ip-10-0-176-102.us-east-2.compute.internal   Ready                      control-plane          75m   v1.33.4
    ip-10-0-188-96.us-east-2.compute.internal    Ready                      worker                 65m   v1.33.4
    ip-10-0-200-59.us-east-2.compute.internal    Ready                      worker                 63m   v1.33.4
    ip-10-0-223-123.us-east-2.compute.internal   Ready                      control-plane          73m   v1.33.4
    ```

    </div>

</div>

## Adding specific registries to an allowlist

You can add an allowlist of registries, or an individual repository, within a registry for image pull and push actions by editing the `image.config.openshift.io/cluster` custom resource (CR).

OpenShift Container Platform applies the changes to this CR to all nodes in the cluster.

When pulling or pushing images, the container runtime searches the registries listed under the `registrySources` parameter in the `image.config.openshift.io/cluster` CR. If you created a list of registries under the `allowedRegistries` parameter, the container runtime searches only those registries. Registries not in your allowlist are blocked.

> [!WARNING]
> When you define the `allowedRegistries` parameter, all registries, including `registry.redhat.io`, `quay.io`, and the default OpenShift image registry, are blocked unless explicitly listed. You must add all of the registries that your payload images require to the `allowedRegistries` list. For example, list `registry.redhat.io`, `quay.io`, and the `internalRegistryHostname` registries. For disconnected clusters, you must also add your mirror registries. Otherwise, you risk pod failure.

<div>

<div class="title">

Procedure

</div>

- Edit the `image.config.openshift.io/cluster` custom resource by running the following command:

  ``` terminal
  $ oc edit image.config.openshift.io/cluster
  ```

  The following is an example `image.config.openshift.io/cluster` CR with an allowed list:

  ``` yaml
  apiVersion: config.openshift.io/v1
  kind: Image
  metadata:
    annotations:
      release.openshift.io/create-only: "true"
    creationTimestamp: "2019-05-17T13:44:26Z"
    generation: 1
    name: cluster
    resourceVersion: "8302"
    selfLink: /apis/config.openshift.io/v1/images/cluster
    uid: e34555da-78a9-11e9-b92b-06d6c7da38dc
  spec:
    registrySources:
      allowedRegistries:
      - example.com
      - quay.io
      - registry.redhat.io
      - reg1.io/myrepo/myapp:latest
      - image-registry.openshift-image-registry.svc:5000
  status:
    internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
  ```

  1.  After you make your configuration updates, list your nodes by running the following command:

      ``` terminal
      $ oc get nodes
      ```

      Example output

      ``` terminal
      NAME               STATUS   ROLES                  AGE   VERSION
      <node_name>        Ready    control-plane,master   37m   v1.27.8+4fab27b
      ```

  2.  Enter debug mode on the node by running the following command:

      ``` terminal
      $ oc debug node/<node_name>
      ```

      Replace \<node_name\> with the name of your node.

  3.  When prompted, enter `chroot /host` into the terminal:

      ``` terminal
      sh-4.4# chroot /host
      ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check that the registries are in the policy file by running the following command:

    ``` terminal
    sh-5.1# cat /etc/containers/policy.json | jq '.'
    ```

    The following policy indicates that only images from the `example.com`, `quay.io`, and `registry.redhat.io` registries are accessible for image pulls and pushes:

    <div class="formalpara">

    <div class="title">

    Example image signature policy file

    </div>

    ``` text
    {
       "default":[
          {
             "type":"reject"
          }
       ],
       "transports":{
          "atomic":{
             "example.com":[
                {
                   "type":"insecureAcceptAnything"
                }
             ],
             "image-registry.openshift-image-registry.svc:5000":[
                {
                   "type":"insecureAcceptAnything"
                }
             ],
             "insecure.com":[
                {
                   "type":"insecureAcceptAnything"
                }
             ],
             "quay.io":[
                {
                   "type":"insecureAcceptAnything"
                }
             ],
             "reg4.io/myrepo/myapp:latest":[
                {
                   "type":"insecureAcceptAnything"
                }
             ],
             "registry.redhat.io":[
                {
                   "type":"insecureAcceptAnything"
                }
             ]
          },
          "docker":{
             "example.com":[
                {
                   "type":"insecureAcceptAnything"
                }
             ],
             "image-registry.openshift-image-registry.svc:5000":[
                {
                   "type":"insecureAcceptAnything"
                }
             ],
             "insecure.com":[
                {
                   "type":"insecureAcceptAnything"
                }
             ],
             "quay.io":[
                {
                   "type":"insecureAcceptAnything"
                }
             ],
             "reg4.io/myrepo/myapp:latest":[
                {
                   "type":"insecureAcceptAnything"
                }
             ],
             "registry.redhat.io":[
                {
                   "type":"insecureAcceptAnything"
                }
             ]
          },
          "docker-daemon":{
             "":[
                {
                   "type":"insecureAcceptAnything"
                }
             ]
          }
       }
    }
    ```

    </div>

    > [!NOTE]
    > If your cluster uses the `registrySources.insecureRegistries` parameter, ensure that any insecure registries are included in the allowed list.
    >
    > For example:
    >
    > ``` yaml
    > spec:
    >   registrySources:
    >     insecureRegistries:
    >     - insecure.com
    >     allowedRegistries:
    >     - example.com
    >     - quay.io
    >     - registry.redhat.io
    >     - insecure.com
    >     - image-registry.openshift-image-registry.svc:5000
    > ```

</div>

## Blocking specific registries

You can block any registry, or an individual repository, within a registry by editing the `image.config.openshift.io/cluster` custom resource (CR).

OpenShift Container Platform applies the changes to this CR to all nodes in the cluster.

When pulling or pushing images, the container runtime searches the registries listed under the `registrySources` parameter in the `image.config.openshift.io/cluster` CR. If you created a list of registries under the `blockedRegistries` parameter, the container runtime does not search those registries. All other registries are allowed.

> [!WARNING]
> To prevent pod failure, do not add the `registry.redhat.io` and `quay.io` registries to the `blockedRegistries` list. Payload images within your environment require access to these registries.

<div>

<div class="title">

Procedure

</div>

- Edit the `image.config.openshift.io/cluster` custom resource by running the following command:

  ``` terminal
  $ oc edit image.config.openshift.io/cluster
  ```

  The following is an example `image.config.openshift.io/cluster` CR with a blocked list:

  ``` yaml
  apiVersion: config.openshift.io/v1
  kind: Image
  metadata:
    annotations:
      release.openshift.io/create-only: "true"
    creationTimestamp: "2019-05-17T13:44:26Z"
    generation: 1
    name: cluster
    resourceVersion: "8302"
    selfLink: /apis/config.openshift.io/v1/images/cluster
    uid: e34555da-78a9-11e9-b92b-06d6c7da38dc
  spec:
    registrySources:
      blockedRegistries:
      - untrusted.com
      - reg1.io/myrepo/myapp:latest
  status:
    internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
  ```

  You cannot set both the `blockedRegistries` and `allowedRegistries` parameters. You must select one or the other.

  1.  Get a list of your nodes by running the following command:

      ``` terminal
      $ oc get nodes
      ```

      Example output

      ``` terminal
      NAME                STATUS   ROLES                  AGE   VERSION
      <node_name>         Ready    control-plane,master   37m   v1.27.8+4fab27b
      ```

  2.  Run the following command to enter debug mode on the node:

      ``` terminal
      $ oc debug node/<node_name>
      ```

      Replace \<node_name\> with the name of the node you want details about.

  3.  When prompted, enter `chroot /host` into the terminal:

      ``` terminal
      sh-4.4# chroot /host
      ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the registries are in the policy file by running the following command:

    ``` terminal
    sh-5.1# cat etc/containers/registries.conf
    ```

    The following example indicates that images from the `untrusted.com` registry are blocked for image pulls and pushes:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]

    [[registry]]
      prefix = ""
      location = "untrusted.com"
      blocked = true
    ```

    </div>

</div>

## Blocking a payload registry

In a mirroring configuration, you can block upstream payload registries in a disconnected environment by using a `ImageContentSourcePolicy` (ICSP) object. The following example procedure demonstrates how to block the `quay.io/openshift-payload` payload registry.

<div>

<div class="title">

Procedure

</div>

1.  Create the mirror configuration using an `ImageContentSourcePolicy` (ICSP) object to mirror the payload to a registry in your instance. The following example ICSP file mirrors the payload `internal-mirror.io/openshift-payload`:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ImageContentSourcePolicy
    metadata:
      name: my-icsp
    spec:
      repositoryDigestMirrors:
      - mirrors:
        - internal-mirror.io/openshift-payload
        source: quay.io/openshift-payload
    ```

2.  After the object deploys onto your nodes, verify that the mirror configuration is set by checking the `/etc/containers/registries.conf` custom resource (CR):

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    [[registry]]
      prefix = ""
      location = "quay.io/openshift-payload"
      mirror-by-digest-only = true

    [[registry.mirror]]
      location = "internal-mirror.io/openshift-payload"
    ```

    </div>

3.  Use the following command to edit the `image.config.openshift.io` CR:

    ``` terminal
    $ oc edit image.config.openshift.io cluster
    ```

4.  To block the payload registry, add the following configuration to the `image.config.openshift.io` CR:

    ``` yaml
    spec:
      registrySources:
        blockedRegistries:
         - quay.io/openshift-payload
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the upstream payload registry is blocked by checking the `/etc/containers/registries.conf` file on the node.

  <div class="formalpara">

  <div class="title">

  Example `/etc/containers/registries.conf` file

  </div>

  ``` terminal
  [[registry]]
    prefix = ""
    location = "quay.io/openshift-payload"
    blocked = true
    mirror-by-digest-only = true

  [[registry.mirror]]
    location = "internal-mirror.io/openshift-payload"
  ```

  </div>

</div>

## Allowing insecure registries

You can add insecure registries, or an individual repository, within a registry by editing the `image.config.openshift.io/cluster` custom resource (CR).

OpenShift Container Platform applies the changes to this CR to all nodes in the cluster. Registries that do not use valid SSL certificates or do not require HTTPS connections are considered insecure.

> [!IMPORTANT]
> Avoid insecure external registries to reduce possible security risks.

\+ :leveloffset: +1

> [!WARNING]
> When you define the `allowedRegistries` parameter, all registries, including `registry.redhat.io`, `quay.io`, and the default OpenShift image registry, are blocked unless explicitly listed. You must add all of the registries that your payload images require to the `allowedRegistries` list. For example, list `registry.redhat.io`, `quay.io`, and the `internalRegistryHostname` registries. For disconnected clusters, you must also add your mirror registries. Otherwise, you risk pod failure.

<div>

<div class="title">

Procedure

</div>

- Edit the `image.config.openshift.io/cluster` custom resource (CR) by running the following command:

  ``` terminal
  $ oc edit image.config.openshift.io/cluster
  ```

  The following is an example `image.config.openshift.io/cluster` CR with an insecure registries list:

  ``` yaml
  apiVersion: config.openshift.io/v1
  kind: Image
  metadata:
    annotations:
      release.openshift.io/create-only: "true"
    creationTimestamp: "2019-05-17T13:44:26Z"
    generation: 1
    name: cluster
    resourceVersion: "8302"
    selfLink: /apis/config.openshift.io/v1/images/cluster
    uid: e34555da-78a9-11e9-b92b-06d6c7da38dc
  spec:
    registrySources:
      insecureRegistries:
      - insecure.com
      - reg4.io/myrepo/myapp:latest
      allowedRegistries:
      - example.com
      - quay.io
      - registry.redhat.io
      - insecure.com
      - reg4.io/myrepo/myapp:latest
      - image-registry.openshift-image-registry.svc:5000
  status:
    internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Check that the registries are added to the policy file by running the following command on a node:

  ``` terminal
  $ cat /etc/containers/registries.conf
  ```

  The following example indicates that images from the `insecure.com` registry is insecure and are allowed for image pulls and pushes.

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]

  [[registry]]
    prefix = ""
    location = "insecure.com"
    insecure = true
  ```

  </div>

</div>

# About adding registries that allow image short names

With an image short name, you can search for images without including the fully qualified domain name in the pull `spec` parameter.

For example, you could use `rhel7/etcd` instead of `registry.access.redhat.com/rhe7/etcd`. You can add registries to search for an image short name by editing the `image.config.openshift.io/cluster` custom resource (CR).

You might use short names in situations where using the full path is not practical. For example, if your cluster references multiple internal registries whose DNS changes often, you would need to update the fully qualified domain names in your pull specs with each change. In this case, using an image short name might be beneficial.

When pulling or pushing images, the container runtime searches the registries listed under the `registrySources` parameter in the `image.config.openshift.io/cluster` CR. If you created a list of registries under the `containerRuntimeSearchRegistries` parameter, when pulling an image with a short name, the container runtime searches those registries.

## When not to use image short names

To avoid deployment failures and security risks when using public registries in OpenShift Container Platform, use fully-qualified image names instead of short names. Short names work with Red Hat internal or private registries, but public registries that require authentication might not deploy images with short names.

You cannot list multiple public registries under the `containerRuntimeSearchRegistries` parameter if each public registry requires different credentials and a cluster does not list the public registry in the global pull secret.

For a public registry that requires authentication, you can use an image short name only if the registry has its credentials stored in the global pull secret.

> [!WARNING]
> If you list public registries under the `containerRuntimeSearchRegistries` parameter (including the `registry.redhat.io`, `docker.io`, and `quay.io` registries), you expose your credentials to all the registries on the list, and you risk network and registry attacks. Because you can only have one pull secret for pulling images, as defined by the global pull secret, that secret is used to authenticate against every registry in that list. Therefore, if you include public registries in the list, you introduce a security risk.

## Adding registries that allow image short names

You can add registries to search for an image short name by editing the `image.config.openshift.io/cluster` custom resource (CR). OpenShift Container Platform applies the changes to this CR to all nodes in the cluster.

> [!WARNING]
> When you define the `allowedRegistries` parameter, all registries, including `registry.redhat.io`, `quay.io`, and the default OpenShift image registry, are blocked unless explicitly listed. You must add all of the registries that your payload images require to the `allowedRegistries` list. For example, list `registry.redhat.io`, `quay.io`, and the `internalRegistryHostname` registries. For disconnected clusters, you must also add your mirror registries. Otherwise, you risk pod failure.

<div>

<div class="title">

Procedure

</div>

- Edit the `image.config.openshift.io/cluster` custom resource:

  ``` terminal
  $ oc edit image.config.openshift.io/cluster
  ```

  The following is an example `image.config.openshift.io/cluster` CR:

  ``` yaml
  apiVersion: config.openshift.io/v1
  kind: Image
  metadata:
    annotations:
      release.openshift.io/create-only: "true"
    creationTimestamp: "2019-05-17T13:44:26Z"
    generation: 1
    name: cluster
    resourceVersion: "8302"
    selfLink: /apis/config.openshift.io/v1/images/cluster
    uid: e34555da-78a9-11e9-b92b-06d6c7da38dc
  spec:
    allowedRegistriesForImport:
      - domainName: quay.io
        insecure: false
    additionalTrustedCA:
      name: myconfigmap
    registrySources:
      containerRuntimeSearchRegistries:
      - reg1.io
      - reg2.io
      - reg3.io
      allowedRegistries:
      - example.com
      - quay.io
      - registry.redhat.io
      - reg1.io
      - reg2.io
      - reg3.io
      - image-registry.openshift-image-registry.svc:5000
  ...
  status:
    internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
  ```

  1.  Get a list of your nodes by running the following command:

      ``` terminal
      $ oc get nodes
      ```

      Example output

      ``` terminal
      NAME                STATUS   ROLES                  AGE   VERSION
      <node_name>         Ready    control-plane,master   37m   v1.27.8+4fab27b
      ```

  2.  Run the following command to enter debug mode on the node:

      ``` terminal
      $ oc debug node/<node_name>
      ```

  3.  When prompted, enter `chroot /host` into the terminal:

      ``` terminal
      sh-4.4# chroot /host
      ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that registries are added to the policy file by running the following command:

    ``` terminal
    sh-5.1# cat /etc/containers/registries.conf.d/01-image-searchRegistries.conf
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    unqualified-search-registries = ['reg1.io', 'reg2.io', 'reg3.io']
    ```

    </div>

</div>

## Configuring additional trust stores for image registry access

You can add references to a config map that has additional certificate authorities (CAs) to be trusted during image registry access to the `image.config.openshift.io/cluster` custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- The certificate authorities (CAs) must be PEM-encoded.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a config map in the `openshift-config` namespace, then and use the config map name in the `AdditionalTrustedCA` parameter of the `image.config.openshift.io` CR. This adds CAs that should be trusted when the cluster contacts external image registries.

    <div class="formalpara">

    <div class="title">

    Image registry CA config map example

    </div>

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: my-registry-ca
    data:
      registry.example.com: |
        -----BEGIN CERTIFICATE-----
        ...
        -----END CERTIFICATE-----
      registry-with-port.example.com..5000: |
        -----BEGIN CERTIFICATE-----
        ...
        -----END CERTIFICATE-----
    ```

    </div>

    where:

    `data:registry.example.com:`
    An example hostname of a registry for which this CA is to be trusted.

    `data:registry-with-port.example.com..5000:`
    An example hostname of a registry with the port for which this CA is to be trusted. If the registry has a port, such as `registry-with-port.example.com:5000`, `:` must be replaced with `..`.

    The PEM certificate content is the value for each additional registry CA to trust.

2.  Optional. Configure an additional CA by running the following command:

    ``` terminal
    $ oc create configmap registry-config --from-file=<external_registry_address>=ca.crt -n openshift-config
    ```

    ``` terminal
    $ oc edit image.config.openshift.io cluster
    ```

    ``` yaml
    spec:
      additionalTrustedCA:
        name: registry-config
    ```

</div>

# Understanding image registry repository mirroring

You must mirror images to update clusters in disconnected environments.

By setting up container registry repository mirroring, you can perform the following tasks:

- Configure your OpenShift Container Platform cluster to redirect requests to pull images from a repository on a source image registry and have it resolved by a repository on a mirrored image registry.

- Identify multiple mirrored repositories for each target repository, to make sure that if one mirror is down, another can be used.

Repository mirroring in OpenShift Container Platform includes the following attributes:

- Image pulls are resilient to registry downtimes.

- Clusters in disconnected environments can pull images from critical locations, such as `quay.io`, and have registries behind a company firewall provide the requested images.

- A particular order of registries is tried when an image pull request is made, with the permanent registry typically being the last one tried.

- The mirror information you enter is added to the `/etc/containers/registries.conf` file on every node in the OpenShift Container Platform cluster.

- When a node makes a request for an image from the source repository, it tries each mirrored repository in turn until it finds the requested content. If all mirrors fail, the cluster tries the source repository. If successful, the image is pulled to the node.

You can set up repository mirroring in the following ways:

- At OpenShift Container Platform installation:

  By pulling container images needed by OpenShift Container Platform and then bringing those images behind your company’s firewall, you can install OpenShift Container Platform into a data center that is in a disconnected environment.

- After OpenShift Container Platform installation:

  If you did not configure mirroring during OpenShift Container Platform installation, you can do so postinstallation by using any of the following custom resource (CR) objects:

  - `ImageDigestMirrorSet` (IDMS). This object allows you to pull images from a mirrored registry by using digest specifications. The IDMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails.

  - `ImageTagMirrorSet` (ITMS). This object allows you to pull images from a mirrored registry by using image tags. The ITMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails.

  - `ImageContentSourcePolicy` (ICSP). This object allows you to pull images from a mirrored registry by using digest specifications. The ICSP CR always falls back to the source registry if the mirrors do not work.

    > [!IMPORTANT]
    > Using an `ImageContentSourcePolicy` (ICSP) object to configure repository mirroring is a deprecated feature. Deprecated functionality is still included in OpenShift Container Platform and continues to be supported. It will be removed in a future release and is not recommended for new deployments.
    >
    > If you have existing YAML files that you used to create `ImageContentSourcePolicy` objects, you can use the `oc adm migrate icsp` command to convert those files to a `ImageDigestMirrorSet` YAML files. For more information, see "Converting ImageContentSourcePolicy (ICSP) files for image registry repository mirroring".

Each of these custom resource objects identify the following information:

- The source of the container image repository you want to mirror.

- A separate entry for each mirror repository you want to offer the content

Note the following actions and how they affect node drain behavior:

- If you create an IDMS or ICSP CR object, the MCO does not drain or reboot the node.

- If you create an ITMS CR object, the MCO drains and reboots the node.

- If you delete an ITMS, IDMS, or ICSP CR object, the MCO drains and reboots the node.

- If you modify an ITMS, IDMS, or ICSP CR object, the MCO drains and reboots the node.

  <div class="important">

  <div class="title">

  </div>

  - When the MCO detects any of the following changes, it applies the update without draining or rebooting the node:

    - Changes to the SSH key in the `spec.config.passwd.users.sshAuthorizedKeys` parameter of a machine config.

    - Changes to the global pull secret or pull secret in the `openshift-config` namespace.

    - Automatic rotation of the `/etc/kubernetes/kubelet-ca.crt` certificate authority (CA) by the Kubernetes API Server Operator.

  - When the MCO detects changes to the `/etc/containers/registries.conf` file, such as editing an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object, it drains the corresponding nodes, applies the changes, and uncordons the nodes. The node drain does not happen for the following changes:

    - The addition of a registry with the `pull-from-mirror = "digest-only"` parameter set for each mirror.

    - The addition of a mirror with the `pull-from-mirror = "digest-only"` parameter set in a registry.

    - The addition of items to the `unqualified-search-registries` list.

  </div>

For new clusters, you can use IDMS, ITMS, and ICSP CRs objects as needed. However, using IDMS and ITMS is recommended.

If you upgraded a cluster, any existing ICSP objects remain stable, and both IDMS and ICSP objects are supported. Workloads that use ICSP objects continue to function as expected. However, if you want to take advantage of the fallback policies introduced in the IDMS CRs, you can migrate current workloads to IDMS objects by using the `oc adm migrate icsp` command as shown in the **Converting ImageContentSourcePolicy (ICSP) files for image registry repository mirroring** section that follows. Migrating to IDMS objects does not require a cluster reboot.

> [!NOTE]
> If your cluster uses an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object to configure repository mirroring, you can use only global pull secrets for mirrored registries. You cannot add a pull secret to a project.

## Configuring image registry repository mirroring

You can create postinstallation mirror configuration custom resources (CR) to redirect image pull requests from a source image registry to a mirrored image registry.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure mirrored repositories, by either:

    - Setting up a mirrored repository with Red Hat Quay. You can copy images from one repository to another and also automatically sync those repositories repeatedly over time by using Red Hat Quay.

      - [Red Hat Quay Repository Mirroring](https://docs.redhat.com/en/documentation/red_hat_quay/3/html/manage_red_hat_quay/arch-mirroring-intro#enabling-repository-mirroring-quay)

    - Using a tool such as `skopeo` to copy images manually from the source repository to the mirrored repository.

      For example, after installing the skopeo RPM package on a {op-system-base-full system}, use the `skopeo` command as shown in the following example:

      ``` terminal
      $ skopeo copy --all \
      docker://registry.access.redhat.com/ubi9/ubi-minimal:latest@sha256:5cf... \
      docker://example.io/example/ubi-minimal
      ```

      In this example, you have a container image registry named `example.io` and image repository named `example`. You want to copy the `ubi9/ubi-minimal` image from `registry.access.redhat.com` to `example.io`. After you create the mirrored registry, you can configure your OpenShift Container Platform cluster to redirect requests made to the source repository to the mirrored repository.

2.  Create a postinstallation mirror configuration custom resource (CR), by using one of the following examples:

    - Create an `ImageDigestMirrorSet` or `ImageTagMirrorSet` CR, as needed, replacing the source and mirrors with your own registry and repository pairs and images:

      ``` yaml
      apiVersion: config.openshift.io/v1
      kind: ImageDigestMirrorSet
      metadata:
        name: ubi9repo
      spec:
        imageDigestMirrors:
        - mirrors:
          - example.io/example/ubi-minimal
          - example.com/example2/ubi-minimal
          source: registry.access.redhat.com/ubi9/ubi-minimal
          mirrorSourcePolicy: AllowContactingSource
        - mirrors:
          - mirror.example.com/redhat
          source: registry.example.com/redhat
          mirrorSourcePolicy: AllowContactingSource
        - mirrors:
          - mirror.example.com
          source: registry.example.com
          mirrorSourcePolicy: AllowContactingSource
        - mirrors:
          - mirror.example.net/image
          source: registry.example.com/example/myimage
          mirrorSourcePolicy: AllowContactingSource
        - mirrors:
          - mirror.example.net
          source: registry.example.com/example
          mirrorSourcePolicy: AllowContactingSource
        - mirrors:
          - mirror.example.net/registry-example-com
          source: registry.example.com
          mirrorSourcePolicy: AllowContactingSource
      ```

    - Create an `ImageContentSourcePolicy` custom resource, replacing the source and mirrors with your own registry and repository pairs and images:

      ``` yaml
      apiVersion: operator.openshift.io/v1alpha1
      kind: ImageContentSourcePolicy
      metadata:
        name: mirror-ocp
      spec:
        repositoryDigestMirrors:
        - mirrors:
          - mirror.registry.com:443/ocp/release
          source: quay.io/openshift-release-dev/ocp-release
        - mirrors:
          - mirror.registry.com:443/ocp/release
          source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
      ```

      where:

      `- mirror.registry.com:443/ocp/release`
      Specifies the name of the mirror image registry and repository.

      `source: quay.io/openshift-release-dev/ocp-release`
      Specifies the online registry and repository containing the content that is mirrored.

3.  Create the new object by running the following command:

    ``` terminal
    $ oc create -f registryrepomirror.yaml
    ```

    After the object is created, the Machine Config Operator (MCO) drains the nodes for `ImageTagMirrorSet` objects only. The MCO does not drain the nodes for `ImageDigestMirrorSet` and `ImageContentSourcePolicy` objects.

4.  To check that the mirrored configuration settings are applied, do the following on one of the nodes.

    1.  List your nodes:

        ``` terminal
        $ oc get node
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                           STATUS                     ROLES    AGE  VERSION
        worker-1.compute.local         Ready                      worker   7m   v1.35.4
        master-1.compute.local         Ready                      master   11m  v1.35.4
        master-2.compute.local         Ready                      master   11m  v1.35.4
        worker-2.compute.local         Ready                      worker   7m   v1.35.4
        worker-3.compute.local         Ready                      worker   7m   v1.35.4
        master-3.compute.local         Ready                      master   11m  v1.35.4
        ```

        </div>

    2.  Start the debugging process to access the node:

        ``` terminal
        $ oc debug node/worker-1.compute.local
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Starting pod/worker-1.compute.local-debug ...
        To use host binaries, run `chroot /host`
        ```

        </div>

    3.  Change your root directory to `/host`:

        ``` terminal
        sh-4.2# chroot /host
        ```

    4.  Check the `/etc/containers/registries.conf` file to make sure the changes were made:

        ``` terminal
        sh-4.2# cat /etc/containers/registries.conf
        ```

        The following output represents a `registries.conf` file where postinstallation mirror configuration CRs are applied.

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]
        short-name-mode = ""

        [[registry]]
          prefix = ""
          location = "registry.access.redhat.com/ubi9/ubi-minimal"

          [[registry.mirror]]
            location = "example.io/example/ubi-minimal"
            pull-from-mirror = "digest-only"

          [[registry.mirror]]
            location = "example.com/example/ubi-minimal"
            pull-from-mirror = "digest-only"

        [[registry]]
          prefix = ""
          location = "registry.example.com"

          [[registry.mirror]]
            location = "mirror.example.net/registry-example-com"
            pull-from-mirror = "digest-only"

        [[registry]]
          prefix = ""
          location = "registry.example.com/example"

          [[registry.mirror]]
            location = "mirror.example.net"
            pull-from-mirror = "digest-only"

        [[registry]]
          prefix = ""
          location = "registry.example.com/example/myimage"

          [[registry.mirror]]
            location = "mirror.example.net/image"
            pull-from-mirror = "digest-only"

        [[registry]]
          prefix = ""
          location = "registry.example.com"

          [[registry.mirror]]
            location = "mirror.example.com"
            pull-from-mirror = "digest-only"

        [[registry]]
          prefix = ""
          location = "registry.example.com/redhat"

          [[registry.mirror]]
            location = "mirror.example.com/redhat"
            pull-from-mirror = "digest-only"
        [[registry]]
          prefix = ""
          location = "registry.access.redhat.com/ubi9/ubi-minimal"
          blocked = true

          [[registry.mirror]]
            location = "example.io/example/ubi-minimal-tag"
            pull-from-mirror = "tag-only"
        ```

        </div>

        where: `[[registry]].location = "registry.access.redhat.com/ubi9/ubi-minimal"`:: The repository listed in a pull spec. `[[registry.mirror]].location = "example.io/example/ubi-minimal"`:: Indicates the mirror for that repository. `[[registry.mirror]].pull-from-mirror = "digest-only"`:: Means that the image pull from the mirror is a digest reference image. `[[registry]].blocked = true`:: Indicates that the `NeverContactSource` parameter is set for this repository. `[[registry.mirror]].pull-from-mirror = "tag-only"`:: Indicates that the image pull from the mirror is a tag reference image.

    5.  Pull an image to the node from the source and check if it is resolved by the mirror.

        ``` terminal
        sh-4.2# podman pull --log-level=debug registry.access.redhat.com/ubi9/ubi-minimal@sha256:5cf...
        ```

</div>

<div class="formalpara">

<div class="title">

Troubleshooting

</div>

If the repository mirroring procedure does not work as described, use the following information about how repository mirroring works to help troubleshoot the problem:

</div>

- The first working mirror is used to supply the pulled image.

- The main registry is only used if no other mirror works.

- From the system context, the `Insecure` flags are used as fallback.

- The format of the `/etc/containers/registries.conf` file has changed recently. It is now version 2 and in TOML format.

## Image registry repository mirroring configuration parameters

You can use the following table for information about parameters when configuring your image repository for mirroring.

| **Parameter** | **Values and Information** |
|----|----|
| `apiVersion:` | Required. The value must be `config.openshift.io/v1` API. |
| `kind:` | The kind of object according to the pull type. The `ImageDigestMirrorSet` type pulls a digest reference image The `ImageTagMirrorSet` type pulls a tag reference image. |
| `spec: imageDigestMirrors:` | The type of image pull method. Use `imageDigestMirrors` for an `ImageDigestMirrorSet` CR. Use `imageTagMirrors` for an `ImageTagMirrorSet` CR. |
| `- mirrors: - example.io/example/ubi-minimal` | The name of the mirrored image registry and repository. |
| `- mirrors: -example.com/example2/ubi-minimal` | The value of this parameter is the name of a secondary mirror repository for each target repository. If one mirror is down the target repository can use the secondary mirror. |
| `source: registry.access.redhat.com/ubi9/ubi-minimal` | The registry and repository source. The source is the repository that is listed in an image pull specification. |
| `mirrorSourcePolicy: AllowContactingSource` | Optional parameter that indicates the fallback policy if the image pull fails. The `AllowContactingSource` value allows continued attempts to pull the image from the source repository. Default value. `NeverContactSource` prevents continued attempts to pull the image from the source repository. |
| `source: registry.example.com/redhat` | An optional parameter that indicates a namespace inside a registry. Setting a namespace inside a registry allows use of any image in that namespace. If you use a registry domain as a source, the object applies to all of the repositories from the registry. |
| `source: registry.example.com` | Optional parameter that indicates a registry. Allows us of any image in that registry. If you specify a registry name, the object applies to all repositories from a source registry to a mirror registry. |
| `source: registry.example.com/example/myimage` | Pulls the image `registry.example.com/example/myimage@sha256:…​` from the mirror `mirror.example.net/image@sha256:..`. |
| `source: registry.example.com/example` | Pulls the image `registry.example.com/example/image@sha256:…​` in the source registry namespace from the mirror `mirror.example.net/image@sha256:…​`. |
| `source: registry.example.com` | Pulls the image `registry.example.com/myimage@sha256` from the mirror registry `example.net/registry-example-com/myimage@sha256:…​`. |

## Converting ImageContentSourcePolicy (ICSP) files for image registry repository mirroring

You can convert existing `ImageContentSourcePolicy` (ICSP) files to `ImageDigestMirrorSet` files to configure image registry repository mirroring.

Using an `ImageContentSourcePolicy` (ICSP) object to configure repository mirroring is a deprecated feature.

This functionality is still included in OpenShift Container Platform and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments.

ICSP objects are being replaced by `ImageDigestMirrorSet` and `ImageTagMirrorSet` objects to configure repository mirroring. If you have existing YAML files that you used to create `ImageContentSourcePolicy` objects, you can use the `oc adm migrate icsp` command to convert those files to an `ImageDigestMirrorSet` YAML file. The command updates the API to the current version, changes the `kind` value to `ImageDigestMirrorSet`, and changes `spec.repositoryDigestMirrors` to `spec.imageDigestMirrors`. The rest of the file is not changed.

Because the migration does not change the `registries.conf` file, the cluster does not need to reboot.

For more information about `ImageDigestMirrorSet` or `ImageTagMirrorSet` objects, see "Configuring image registry repository mirroring" in the previous section.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

- Ensure that you have `ImageContentSourcePolicy` objects on your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Use the following command to convert one or more `ImageContentSourcePolicy` YAML files to an `ImageDigestMirrorSet` YAML file:

    ``` terminal
    $ oc adm migrate icsp <file_name>.yaml <file_name>.yaml <file_name>.yaml --dest-dir <path_to_the_directory>
    ```

    where:

    `<file_name>`
    Specifies the name of the source `ImageContentSourcePolicy` YAML. You can list multiple file names.

    `--dest-dir`
    Optional: Specifies a directory for the output `ImageDigestMirrorSet` YAML. If unset, the file is written to the current directory.

    For example, the following command converts the `icsp.yaml` and `icsp-2.yaml` file and saves the new YAML files to the `idms-files` directory.

    ``` terminal
    $ oc adm migrate icsp icsp.yaml icsp-2.yaml --dest-dir idms-files
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    wrote ImageDigestMirrorSet to idms-files/imagedigestmirrorset_ubi8repo.5911620242173376087.yaml
    wrote ImageDigestMirrorSet to idms-files/imagedigestmirrorset_ubi9repo.6456931852378115011.yaml
    ```

    </div>

2.  Create the CR object by running the following command:

    ``` terminal
    $ oc create -f <path_to_the_directory>/<file-name>.yaml
    ```

    where:

    `<path_to_the_directory>`
    Specifies the path to the directory, if you used the `--dest-dir` flag.

    `<file_name>`
    Specifies the name of the `ImageDigestMirrorSet` YAML.

3.  Remove the ICSP objects after the IDMS objects are rolled out.

</div>

# Additional resources

- [Working with manifest lists](image-streams-manage.md#images-imagestream-import-import-mode_image-streams-managing)

- [Understanding feature gates](../nodes/clusters/nodes-cluster-enabling-features.md#nodes-cluster-enabling-features-about_nodes-cluster-enabling)

- [Updating the global cluster pull secret](managing_images/using-image-pull-secrets.md#images-update-global-pull-secret_using-image-pull-secrets)
