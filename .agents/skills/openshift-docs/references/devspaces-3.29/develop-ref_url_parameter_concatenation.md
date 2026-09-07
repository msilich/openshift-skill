> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_concatenation). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter concatenation

Combine multiple URL parameters when starting an OpenShift Dev Spaces workspace by concatenating them with `&`. This enables you to customize the editor, storage type, devfile, and other workspace settings in a single URL.

Use the following URL syntax:

`https://`*`<openshift_dev_spaces_fqdn>`*`#`*`<git_repository_url>`*`?`*`<url_parameter_1>`*`&`*`<url_parameter_2>`*`&`*`<url_parameter_3>`*

For example, the following URL starts a new workspace with a Git repository, a specific editor, and a custom devfile path:

`https://`*`<openshift_dev_spaces_fqdn>`*`#https://github.com/che-samples/cpp-hello-world?new&che-editor=che-incubator/intellij-community/latest&devfilePath=tests/testdevfile.yaml`

Explanation of the parts of the URL:

``` plaintext
https://<openshift_dev_spaces_fqdn>
#https://github.com/che-samples/cpp-hello-world
?new&che-editor=che-incubator/intellij-community/latest&devfilePath=tests/testdevfile.yaml
```

`https://`*`<openshift_dev_spaces_fqdn>`*  
OpenShift Dev Spaces URL.

`#https://github.com/…​`  
The URL of the Git repository to be cloned into the new workspace.

`?new&che-editor=…​`  
The concatenated optional URL parameters.
