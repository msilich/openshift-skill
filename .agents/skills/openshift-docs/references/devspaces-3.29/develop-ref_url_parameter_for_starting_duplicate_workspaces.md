> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_for_starting_duplicate_workspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter for starting duplicate workspaces

Use the `new` URL parameter to create multiple workspaces from the same devfile and Git repository, which is useful when you need parallel environments for testing or comparing changes.

The URL parameter for starting a duplicate workspace is `new`:

``` plaintext
https://<openshift_dev_spaces_fqdn>#<git_repository_url>?new
```

Note

If you currently have a workspace that you started by using a URL, then visiting the URL again without the `new` URL parameter opens the existing workspace.
