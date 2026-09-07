> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_for_the_existing_workspace_name). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter for the existing workspace name

Use the `existing` URL parameter to reopen an existing workspace instead of creating a new one, which avoids duplicate workspaces when revisiting a workspace URL.

## Example

`https://`*`<openshift_dev_spaces_fqdn>`*`#<git_repository_url>?existing=workspace_name`

When specifying the `existing` URL parameter, following situations may arise:

- If there is no workspace created from the same URL, a new workspace is created.
- If the specified existing workspace name matches an existing workspace created from the same URL and the existing workspace is opened.
- If the specified existing workspace name does not match any existing workspaces, a warning appears and you need to select one of the following actions:
  - Create a new workspace.
  - Select an existing workspace to open.

Note

To create multiple workspaces from the same URL, you can use the `new` URL parameter:

``` plaintext
https://<openshift_dev_spaces_fqdn>#<git_repository_url>?new
```

**Related reference**  

- [URL parameter for starting duplicate workspaces](develop-ref_url_parameter_for_starting_duplicate_workspaces.md "Use the new URL parameter to create multiple workspaces from the same devfile and Git repository, which is useful when you need parallel environments for testing or comparing changes.")
