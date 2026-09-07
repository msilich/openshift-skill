> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_for_additional_remotes). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter for additional remotes

Configure additional Git remotes when starting a workspace by specifying extra repository URLs as parameters, enabling work with multiple upstream sources in a single workspace.

The URL parameter for cloning and configuring additional remotes for the workspace is `remotes=`:

``` plaintext
https://<openshift_dev_spaces_fqdn>#<git_repository_url>?remotes={{<name_1>,<url_1>},{<name_2>,<url_2>},{<name_3>,<url_3>},...}
```

Important

- If you do not enter the name `origin` for any of the additional remotes, the remote from *\<git_repository_url\>* is cloned and named `origin` by default. Its expected branch is checked out automatically.
- If you enter the name `origin` for one of the additional remotes, its default branch is checked out automatically. However, the remote from *\<git_repository_url\>* is NOT cloned for the workspace.
