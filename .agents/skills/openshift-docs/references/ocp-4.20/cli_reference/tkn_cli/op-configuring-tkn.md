<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure the Red Hat OpenShift Pipelines `tkn` CLI to enable tab completion.

# Enabling tab completion

After you install the `tkn` CLI, you can enable tab completion to automatically complete `tkn` commands or suggest options when you press Tab.

<div>

<div class="title">

Prerequisites

</div>

- You must have the `tkn` CLI tool installed.

- You must have `bash-completion` installed on your local system.

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

The following procedure enables tab completion for Bash.

</div>

1.  Save the Bash completion code to a file:

    ``` terminal
    $ tkn completion bash > tkn_bash_completion
    ```

2.  Copy the file to `/etc/bash_completion.d/`:

    ``` terminal
    $ sudo cp tkn_bash_completion /etc/bash_completion.d/
    ```

    Alternatively, you can save the file to a local directory and source it from your `.bashrc` file instead.

Tab completion is enabled when you open a new terminal.
