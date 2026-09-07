> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_parameters_for_che_editor_yaml). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Parameters for che-editor.yaml

Configure the `che-editor.yaml` file to select and customize the IDE for your workspace, including the editor type, version, and container image.

<span id="ref_parameters-for-che-editor-yaml_devspaces__entry__1"></span><span id="ref_parameters-for-che-editor-yaml_devspaces__entry__2"></span><span id="ref_parameters-for-che-editor-yaml_devspaces__entry__3"></span><span id="ref_parameters-for-che-editor-yaml_devspaces__entry__4"></span>

<table>
<caption>Table 1. Supported IDEs</caption>
<thead>
<tr>
<th>IDE</th>
<th>Status</th>
<th><code>id</code></th>
<th>Note</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><a href="https://github.com/che-incubator/che-code">Microsoft Visual Studio Code - Open Source</a></p></td>
<td><p>Available</p></td>
<td><ul>
<li><code>che-incubator/che-code/latest</code></li>
<li><code>che-incubator/che-code/insiders</code></li>
</ul></td>
<td><ul>
<li><code>latest</code> is the default IDE that loads in a new workspace when the URL parameter or <code>che-editor.yaml</code> is not used.</li>
<li><code>insiders</code> is the development version.</li>
</ul></td>
</tr>
<tr>
<td><p><a href="https://github.com/redhat-developer/devspaces-gateway-plugin/">JetBrains IntelliJ IDEA Ultimate Edition (over JetBrains Gateway)</a></p></td>
<td><p>Available</p></td>
<td><ul>
<li><code>che-incubator/che-idea-server/latest</code></li>
<li><code>che-incubator/che-idea-server/next</code></li>
</ul></td>
<td><ul>
<li><code>latest</code> is the stable version.</li>
<li><code>next</code> is the development version.</li>
</ul></td>
</tr>
</tbody>
</table>

## `id` selects an IDE from the plugin registry

``` yaml
id: che-incubator/che-idea/latest
```

As alternatives to the `id` parameter, the `che-editor.yaml` file supports two other options. You can use a `reference` to the URL of another `che-editor.yaml` file or an `inline` definition for an IDE outside of a plugin registry:

## `reference` points to a remote `che-editor.yaml` file

``` yaml
reference: https://<hostname_and_path_to_a_remote_file>/che-editor.yaml
```

## `inline` specifies a complete definition for a customized IDE without a plugin registry

``` yaml
inline:
  schemaVersion: 2.1.0
  metadata:
    name: JetBrains IntelliJ IDEA Community IDE
  components:
    - name: intellij
      container:
        image: 'quay.io/che-incubator/che-idea:next'
        volumeMounts:
          - name: projector-user
            path: /home/projector-user
        mountSources: true
        memoryLimit: 2048M
        memoryRequest: 32Mi
        cpuLimit: 1500m
        cpuRequest: 100m
        endpoints:
          - name: intellij
            attributes:
              type: main
              cookiesAuthEnabled: true
              urlRewriteSupported: true
              discoverable: false
              path: /?backgroundColor=434343&wss
            targetPort: 8887
            exposure: public
            secure: false
            protocol: https
      attributes: {}
    - name: projector-user
      volume: {}
```

For more complex scenarios, the `che-editor.yaml` file supports the `registryUrl` and `override` parameters:

## `registryUrl` points to a custom plugin registry rather than to the default OpenShift Dev Spaces plugin registry

``` yaml
id: <editor_id>
registryUrl: <url_of_custom_plugin_registry>
```

id  
The `id` of the IDE in the custom plugin registry.

## `override` of the default value of one or more defined properties of the IDE

``` yaml
...
override:
  containers:
    - name: che-idea
      memoryLimit: 1280Mi
      cpuLimit: 1510m
      cpuRequest: 102m
    ...
```

The preceding field can be `id:`, `registryUrl:`, or `reference:`.

**Related concepts**  

- [Share preconfigured workspace links with your team](develop-assembly_optional_parameters_for_urls.md "Share preconfigured workspace links with your team by appending optional parameters to the URL that starts a new workspace so you can control the IDE, storage, resource limits, and devfile configuration without editing files.")

**Related tasks**  

- [Define a common IDE](develop-proc_defining_a_common_ide.md "Define a common IDE for all workspaces in a Git repository by using a che-editor.yaml file so that all team members and new contributors use the most suitable IDE for the project. You can also use this file to override the OpenShift Dev Spaces instance default IDE for a particular Git repository.")
