> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-ref_troubleshooting_oauth_configuration). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Fix OAuth configuration errors

Verify your OAuth configuration against common misconfigurations when connecting OpenShift Dev Spaces to Git providers.

<span id="ref_troubleshooting-oauth-configuration_devspaces___callback_url_mismatch"></span>

## [Callback URL mismatch](troubleshoot-ref_troubleshooting_oauth_configuration.md#ref_troubleshooting-oauth-configuration_devspaces___callback_url_mismatch)

Every Git provider OAuth application requires a callback URL that matches your OpenShift Dev Spaces instance. If the callback URL is wrong, authentication fails after the user authorizes the application.

The correct callback URL for all providers is:

``` plaintext
https://<openshift_dev_spaces_fqdn>/api/oauth/callback
```

Verify this value in your Git provider OAuth application settings:

- **GitHub**: **Authorization callback URL** field
- **GitLab**: **Redirect URI** field
- **Bitbucket Cloud**: **Callback URL** field
- **Bitbucket Server** (OAuth 2.0): **Redirect URL** field
- **Microsoft Azure DevOps**: Redirect URI registered in Microsoft Entra ID

<span id="ref_troubleshooting-oauth-configuration_devspaces___secret_labels_and_namespace"></span>

## [Secret labels and namespace](troubleshoot-ref_troubleshooting_oauth_configuration.md#ref_troubleshooting-oauth-configuration_devspaces___secret_labels_and_namespace)

The OpenShift Secret that stores the OAuth credentials must have the correct labels and be in the correct namespace. If the labels or namespace are wrong, OpenShift Dev Spaces does not detect the OAuth configuration.

**Required Secret labels**

``` yaml
metadata:
  namespace: openshift-devspaces
  labels:
    app.kubernetes.io/part-of: che.eclipse.org
    app.kubernetes.io/component: oauth-scm-configuration
```

<span id="ref_troubleshooting-oauth-configuration_devspaces___gitlab_scope_requirements"></span>

## [GitLab scope requirements](troubleshoot-ref_troubleshooting_oauth_configuration.md#ref_troubleshooting-oauth-configuration_devspaces___gitlab_scope_requirements)

The GitLab authorized application must have the following scopes enabled. Missing scopes cause permission errors when developers push code or access repositories:

- `api`
- `write_repository`
- `openid`

<span id="ref_troubleshooting-oauth-configuration_devspaces___bitbucket_server_oauth_1_0_public_key"></span>

## [Bitbucket Server OAuth 1.0 public key](troubleshoot-ref_troubleshooting_oauth_configuration.md#ref_troubleshooting-oauth-configuration_devspaces___bitbucket_server_oauth_1_0_public_key)

Bitbucket Server application links using OAuth 1.0 require an RSA public key. If the public key is missing or incorrectly formatted, authentication fails silently.

Verify that the content of the `public-stripped.pub` file (generated during setup) is pasted into the **Public Key** field of the incoming link configuration on Bitbucket Server.
