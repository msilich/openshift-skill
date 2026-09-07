> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_for_a_container_image). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter for a container image

The `image` URL parameter specifies a custom container image for the workspace, allowing you to use a different base image than the one defined in the devfile or the default Universal Developer Image.

The `image` parameter applies in the following scenarios:

- The Git repository contains no devfile, and you want to start a new workspace with the custom image.
- The Git repository contains a devfile, and you want to override the first container image listed in the `components` section of the devfile.

The URL parameter for the path to the container image is `image=`:

``` plaintext
https://<openshift_dev_spaces_fqdn>#<git_repository_url>?image=<container_image_url>
```

For example:

`https://`*`<openshift_dev_spaces_fqdn>`*`#https://github.com/eclipse-che/che-docs?image=quay.io/devfile/universal-developer-image:ubi9-latest`
