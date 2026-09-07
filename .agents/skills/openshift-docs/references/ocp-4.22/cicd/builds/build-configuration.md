<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the following procedure to configure build settings.

# Build controller configuration parameters

The `build.config.openshift.io/cluster` resource offers the following configuration parameters.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>Build</code></p></td>
<td style="text-align: left;"><p>Holds cluster-wide information on how to handle builds. The canonical, and only valid name is <code>cluster</code>.</p>
<p><code>spec</code>: Holds user-settable values for the build controller configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>buildDefaults</code></p></td>
<td style="text-align: left;"><p>Controls the default information for builds.</p>
<p><code>defaultProxy</code>: Contains the default proxy settings for all build operations, including image pull or push and source download.</p>
<p>You can override values by setting the <code>HTTP_PROXY</code>, <code>HTTPS_PROXY</code>, and <code>NO_PROXY</code> environment variables in the <code>BuildConfig</code> strategy.</p>
<p><code>gitProxy</code>: Contains the proxy settings for Git operations only. If set, this overrides any proxy settings for all Git commands, such as <code>git clone</code>.</p>
<p>Values that are not set here are inherited from DefaultProxy.</p>
<p><code>env</code>: A set of default environment variables that are applied to the build if the specified variables do not exist on the build.</p>
<p><code>imageLabels</code>: A list of labels that are applied to the resulting image. You can override a default label by providing a label with the same name in the <code>BuildConfig</code>.</p>
<p><code>resources</code>: Defines resource requirements to execute the build.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ImageLabel</code></p></td>
<td style="text-align: left;"><p><code>name</code>: Defines the name of the label. It must have non-zero length.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>buildOverrides</code></p></td>
<td style="text-align: left;"><p>Controls override settings for builds.</p>
<p><code>imageLabels</code>: A list of labels that are applied to the resulting image. If you provided a label in the <code>BuildConfig</code> with the same name as one in this table, your label will be overwritten.</p>
<p><code>nodeSelector</code>: A selector which must be true for the build pod to fit on a node.</p>
<p><code>tolerations</code>: A list of tolerations that overrides any existing tolerations set on a build pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>BuildList</code></p></td>
<td style="text-align: left;"><p><code>items</code>: Standard object’s metadata.</p></td>
</tr>
</tbody>
</table>

# Configuring build settings

You can configure build settings by editing the `build.config.openshift.io/cluster` resource.

<div>

<div class="title">

Procedure

</div>

- Edit the `build.config.openshift.io/cluster` resource by entering the following command:

  ``` terminal
  $ oc edit build.config.openshift.io/cluster
  ```

  The following is an example `build.config.openshift.io/cluster` resource:

  ``` yaml
  apiVersion: config.openshift.io/v1
  kind: Build
  metadata:
    annotations:
      release.openshift.io/create-only: "true"
    creationTimestamp: "2019-05-17T13:44:26Z"
    generation: 2
    name: cluster
    resourceVersion: "107233"
    selfLink: /apis/config.openshift.io/v1/builds/cluster
    uid: e2e9cc14-78a9-11e9-b92b-06d6c7da38dc
  spec:
    buildDefaults:
      defaultProxy:
        httpProxy: http://proxy.com
        httpsProxy: https://proxy.com
        noProxy: internal.com
      env:
      - name: envkey
        value: envvalue
      gitProxy:
        httpProxy: http://gitproxy.com
        httpsProxy: https://gitproxy.com
        noProxy: internalgit.com
      imageLabels:
      - name: labelkey
        value: labelvalue
      resources:
        limits:
          cpu: 100m
          memory: 50Mi
        requests:
          cpu: 10m
          memory: 10Mi
    buildOverrides:
      imageLabels:
      - name: labelkey
        value: labelvalue
      nodeSelector:
        selectorkey: selectorvalue
      tolerations:
      - effect: NoSchedule
        key: node-role.kubernetes.io/builds
  operator: Exists
  ```

  - `Build`: Holds cluster-wide information on how to handle builds. The canonical, and only valid name is `cluster`.

  - `buildDefaults`: Controls the default information for builds.

  - `defaultProxy`: Contains the default proxy settings for all build operations, including image pull or push and source download.

  - `env`: A set of default environment variables that are applied to the build if the specified variables do not exist on the build.

  - `gitProxy`: Contains the proxy settings for Git operations only. If set, this overrides any Proxy settings for all Git commands, such as `git clone`.

  - `imageLabels`: A list of labels that are applied to the resulting image. You can override a default label by providing a label with the same name in the `BuildConfig`.

  - `resources`: Defines resource requirements to execute the build.

  - `buildOverrides`: Controls override settings for builds.

  - `imageLabels`: A list of labels that are applied to the resulting image. If you provided a label in the `BuildConfig` with the same name as one in this table, your label will be overwritten.

  - `nodeSelector`: A selector which must be true for the build pod to fit on a node.

  - `tolerations`: A list of tolerations that overrides any existing tolerations set on a build pod.

</div>
