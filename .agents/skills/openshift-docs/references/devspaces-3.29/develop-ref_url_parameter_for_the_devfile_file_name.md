> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_for_the_devfile_file_name). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter for the devfile file name

Use the `df` URL parameter to specify a custom devfile file name when the repository uses a name other than the default `.devfile.yaml` or `devfile.yaml`.

The URL parameter for specifying an unconventional file name of the devfile is `df=`*`<filename>`*`.yaml`:

``` plaintext
https://<openshift_dev_spaces_fqdn>#<git_repository_url>?df=<filename>.yaml
```

`df=`*`<filename>`*`.yaml`  
*`<filename>`*`.yaml` is an unconventional file name of the devfile in the linked Git repository.

Tip

The `df=`*`<filename>`*`.yaml` parameter also has a long version: `devfilePath=`*`<filename>`*`.yaml`.
