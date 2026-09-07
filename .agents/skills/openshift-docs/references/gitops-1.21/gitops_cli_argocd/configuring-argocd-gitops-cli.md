<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure the GitOps `argocd` CLI to enable tab completion.

# Enabling tab completion

After you install the GitOps `argocd` CLI, you can enable tab completion to automatically complete `argocd` commands or suggest options when you press Tab.

> [!NOTE]
> Tab completions only exist for the Bash shell.

<div>

<div class="title">

Prerequisites

</div>

- You must have the GitOps `argocd` CLI tool installed.

- You must have `bash-completion` installed on your local system.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Save the Bash completion code to a file:

    ``` terminal
    $ argocd completion bash > argocd_bash_completion
    ```

2.  Copy the file to `/etc/bash_completion.d/`:

    ``` terminal
    $ sudo cp argocd_bash_completion /etc/bash_completion.d/
    ```

    Alternatively, you can save the file to a local directory and source it from your `.bash_profile` file instead.

    Tab completion is enabled when you open a new terminal.

</div>

# Additional resources

- [Installing the GitOps CLI](../installing_gitops/installing-argocd-gitops-cli.md#installing-argocd-gitops-cli)

- [Logging in to the Argo CD server in the default mode](logging-in-to-argocd-server-in-default-mode.md#logging-in-to-argocd-server-in-default-mode)

- [Basic GitOps argocd commands](argocd-gitops-cli-reference.md#argocd-gitops-cli-reference)
