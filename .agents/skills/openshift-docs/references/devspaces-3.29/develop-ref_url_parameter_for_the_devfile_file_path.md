> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_for_the_devfile_file_path). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter for the devfile file path

Use the `devfilePath` URL parameter to specify a custom path to the devfile when it is not in the root directory of the linked Git repository.

The URL parameter for specifying an unconventional file path of the devfile is `devfilePath=`*`<relative_file_path>`*:

``` plaintext
https://<openshift_dev_spaces_fqdn>#<git_repository_url>?devfilePath=<relative_file_path>
```

`devfilePath=`*`<relative_file_path>`*  
*`<relative_file_path>`* is an unconventional file path of the devfile in the linked Git repository.
