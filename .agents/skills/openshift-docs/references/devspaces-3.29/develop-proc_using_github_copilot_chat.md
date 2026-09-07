> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_using_github_copilot_chat). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set up GitHub Copilot Chat

Configure GitHub Copilot Chat in your OpenShift Dev Spaces workspace to receive AI-powered code suggestions, completions, and inline explanations directly in the editor.

## Before you begin

- You have a GitHub account with an active [GitHub Copilot](https://github.com/features/copilot) subscription.
- You have a running OpenShift Dev Spaces workspace with the Code - OSS editor.
- You have access to the following URLs from the workspace (ensure they are added to the allowlist if you are in a restricted or air-gapped environment):
  - [`https://github.com`](https://github.com)
  - [`https://api.github.com`](https://api.github.com)
  - [`https://api.githubcopilot.com`](https://api.githubcopilot.com)

## Procedure

1.  Install version 0.36.2 of the [Dev Spaces Copilot Chat Integration](https://open-vsx.org/extension/redhat/devspaces-copilot-chat-integration/0.36.2) extension.

    Choose one of the following options depending on your Open VSX registry configuration:

    - If your OpenShift Dev Spaces instance is configured to use the [public Open VSX registry](https://open-vsx.org) or a standalone Open VSX registry that contains the extension:

      Open the Extensions view by pressing Ctrl+Shift+X, search for `Dev Spaces Copilot Chat Integration`, select version **0.36.2**, and click **Install**.

    - If your OpenShift Dev Spaces instance uses the default embedded Open VSX registry or a registry that does not contain the extension, install it manually from a `.vsix` file:

      Download the `.vsix` file from the [Open VSX registry](https://open-vsx.org/extension/redhat/devspaces-copilot-chat-integration/0.36.2), then press F1 to open the Command Palette and run `Extensions: Install from VSIX…​`.

    Important

    Use version 0.36.2 of the extension. Other versions may not be compatible with the current OpenShift Dev Spaces editor.

2.  Authenticate using Device Authentication.

    Press F1 to open the Command Palette, type `GitHub: Device Authentication`, and select the command.

    Important

    You must complete Device Authentication **before** attempting to use AI features. Initiating "Sign in to use AI Features" without a valid device authentication token causes authentication errors that require signing out and re-authenticating.

3.  Complete the device authentication flow.

    A notification appears with a device code. Click the link to open the GitHub device activation page in your browser, paste the code, and authorize access.

4.  Refresh the browser page.

    After successful authentication, a notification prompts you to refresh the browser page. Refresh the page to apply the authentication token. Copilot Chat is authenticated automatically and ready to use.

## Results

- Open the Copilot Chat panel, type a prompt such as "Explain this file", and verify that a response appears.

Note

Device Authentication is a one-time step. The credentials are saved as a OpenShift object and persist across workspaces on the same cluster.

If you attempted to use Copilot Chat before completing Device Authentication, the extension may enter an error state. Typical symptoms include:

- Copilot Chat appears to be connected but does not respond to prompts.

- The Copilot Chat output log contains errors such as:

  ``` plaintext
  Failed to get copilot token. reason: NotAuthorized
  GitHub Copilot could not connect to server. Extension activation failed: "Failed to get copilot token. reason: NotAuthorized"
  ```

This happens when **Sign in to use AI Features** is triggered before a valid Device Authentication token exists.

To recover:

1.  Click the **Accounts** icon on the left activity bar, select your account, and click **Sign Out**. A confirmation dialog appears indicating the account has been used by the Dev Spaces Copilot Chat Integration. Click **Sign Out** to confirm.
2.  Press F1 to open the Command Palette and run `GitHub: Device Authentication`. Complete the device authentication flow in the browser.
3.  Refresh the browser page when prompted. Copilot Chat is now ready to use.
