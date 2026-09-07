> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_preventing_workspace_idling_for_long_running_commands). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Prevent workspace idling for long-running commands

Prevent a workspace from stopping while long-running CLI tools such as `helm`, `odo`, or `sleep` are active, so that unattended tasks can complete without interruption.

## Before you begin

- You have a running OpenShift Dev Spaces workspace.

## About this task

The CLI Watcher periodically checks for running processes that match the commands you specify. When it detects an active watched command, it resets the workspace idle timer. This configuration works entirely in user space and does not require administrator privileges.

## Procedure

1.  Create a `.noidle` file in your workspace:

    ``` yaml
    enabled: true
    watchedCommands:
      - helm
      - odo
      - sleep
    checkPeriodSeconds: 60
    ```

    where:

    `enabled`  
    Enables or disables the CLI Watcher. Set to `true` to activate it.

    `watchedCommands`  
    A list of command names to monitor. When any of these commands are detected as a running process, the workspace idle timer is reset.

    `checkPeriodSeconds`  
    The polling interval in seconds. The default value is `60`.

2.  Place the `.noidle` file in one of the following locations, listed from highest to lowest priority:
    - Set the `CLI_WATCHER_CONFIG` environment variable to the absolute path of your `.noidle` file.

    - Place the file in your project directory or any parent directory up to `$PROJECTS_ROOT`. The watcher searches upward from the current project directory.

    - Place the file in your home directory as `~/.noidle`.

      If the CLI Watcher finds no configuration file, it waits and checks again on the next poll cycle.

## Results

1.  Start a watched command in the terminal. For example: `sleep 600`.
2.  Verify that the workspace remains active beyond the configured idle timeout.

Note

The `.noidle` file supports live updates. You can add, edit, or remove the file while the workspace is running. Changes are picked up automatically on the next poll cycle.

The following processes are always excluded from watching and do not prevent workspace idling: PID 1 (the main container process) and `tail`.
