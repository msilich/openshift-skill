> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_for_the_ide). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter for the IDE

The `che-editor=` URL parameter specifies a supported IDE when starting a workspace, allowing you to override the default editor or the `che-editor.yaml` file without modifying the Git repository.

Tip

Use the `che-editor=` parameter when you cannot add or edit a [`/.che/che-editor.yaml`](develop-proc_defining_a_common_ide.md "Define a common IDE for all workspaces in a Git repository by using a che-editor.yaml file so that all team members and new contributors use the most suitable IDE for the project. You can also use this file to override the OpenShift Dev Spaces instance default IDE for a particular Git repository.") file in the source-code Git repository to be cloned for workspaces.

Note

The `che-editor=` parameter overrides the [`/.che/che-editor.yaml`](develop-proc_defining_a_common_ide.md "Define a common IDE for all workspaces in a Git repository by using a che-editor.yaml file so that all team members and new contributors use the most suitable IDE for the project. You can also use this file to override the OpenShift Dev Spaces instance default IDE for a particular Git repository.") file.

This parameter accepts two types of values:

- `che-editor=`*`<editor_key>`*

  ``` shell-session
  https://<openshift_dev_spaces_fqdn>#<git_repository_url>?che-editor=<editor_key>
  ```

<span id="ref_url-parameter-for-the-ide_devspaces__entry__1"></span><span id="ref_url-parameter-for-the-ide_devspaces__entry__2"></span><span id="ref_url-parameter-for-the-ide_devspaces__entry__3"></span><span id="ref_url-parameter-for-the-ide_devspaces__entry__4"></span>

<table>
<caption>Table 1. The URL parameter <code>&lt;editor_key&gt;</code> values for supported IDEs</caption>
<thead>
<tr>
<th>IDE</th>
<th>Status</th>
<th><code>editor_key</code> value</th>
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

<span id="ref_url-parameter-for-the-ide_devspaces___using_a_url_to_a_file"></span>

## [Using a URL to a file](develop-ref_url_parameter_for_the_ide.md#ref_url-parameter-for-the-ide_devspaces___using_a_url_to_a_file)

To start a workspace with an IDE defined by a URL to a file with devfile content, use the `che-editor=`*`<url_to_a_file>`* parameter:

``` shell-session
pass:c,a,q[https://__<openshift_dev_spaces_fqdn>__#<git_repository_url>?che-editor=<url_to_a_file>]
```

Tip

- The URL must point to the raw file content.
- To use this parameter with a [`che-editor.yaml`](develop-proc_defining_a_common_ide.md "Define a common IDE for all workspaces in a Git repository by using a che-editor.yaml file so that all team members and new contributors use the most suitable IDE for the project. You can also use this file to override the OpenShift Dev Spaces instance default IDE for a particular Git repository.") file, copy the file with another name or path, and remove the line with `inline` from the file.

**Related information**  

- [The che-editors.yaml file with devfiles of all supported IDEs](https://github.com/eclipse-che/che-plugin-registry/blob/main/che-editors.yaml)
