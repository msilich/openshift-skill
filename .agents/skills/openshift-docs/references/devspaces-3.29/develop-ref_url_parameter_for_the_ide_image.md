> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_for_the_ide_image). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter for the IDE image

The `editor-image` URL parameter sets a custom IDE image for the workspace, allowing you to test prerelease IDE builds or use a customized IDE container.

Important

- If the Git repository contains [`/.che/che-editor.yaml`](develop-proc_defining_a_common_ide.md "Define a common IDE for all workspaces in a Git repository by using a che-editor.yaml file so that all team members and new contributors use the most suitable IDE for the project. You can also use this file to override the OpenShift Dev Spaces instance default IDE for a particular Git repository.") file, the custom editor is overridden with the new IDE image.
- If there is no [`/.che/che-editor.yaml`](develop-proc_defining_a_common_ide.md "Define a common IDE for all workspaces in a Git repository by using a che-editor.yaml file so that all team members and new contributors use the most suitable IDE for the project. You can also use this file to override the OpenShift Dev Spaces instance default IDE for a particular Git repository.") file in the Git repository, the default editor is overridden with the new IDE image.
- If you want to override the supported IDE and change the target editor image, you can use both parameters together: `che-editor` and `editor-image` URL parameters.

The URL parameter to override the IDE image is `editor-image=`:

``` plaintext
https://<openshift_dev_spaces_fqdn>#<git_repository_url>?editor-image=<container_registry/image_name:image_tag>
```

For example:

- To start a workspace with a custom IDE image:

  ``` plaintext
  pass:c,a,q[https://__<openshift_dev_spaces_fqdn>__]#https://github.com/eclipse-che/che-docs?editor-image=quay.io/che-incubator/che-code:next
  ```

- To combine the `che-editor` and `editor-image` parameters:

  ``` plaintext
  pass:c,a,q[https://__<openshift_dev_spaces_fqdn>__]#https://github.com/eclipse-che/che-docs?che-editor=che-incubator/che-code/latest&editor-image=quay.io/che-incubator/che-code:next
  ```
