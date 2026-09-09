<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use the `roxctl` CLI to restore Red Hat Advanced Cluster Security for Kubernetes (RHACS) by using the `restore` command. This command requires an API token or your administrator password.

<a id="restore-acs-roxctl-api_restoring-central-database-by-using-the-roxctl-cli"></a>

# Restoring by using an API token

You can restore the entire database of RHACS by using an API token.

<div>

<div class="title">

Prerequisites

</div>

- You have a RHACS backup file.

- You have an API token with the administrator role.

- You have installed the `roxctl` CLI.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the `ROX_API_TOKEN` and the `ROX_ENDPOINT` environment variables by running the following commands:

    ``` terminal
    $ export ROX_API_TOKEN=<api_token>
    ```

    ``` terminal
    $ export ROX_ENDPOINT=<address>:<port_number>
    ```

2.  Restore the Central database by running the following command:

    ``` terminal
    $ roxctl central db restore <backup_file>
    ```

    where:

    `<backup_file>`  
    Specifies the name of the backup file that you want to restore.

</div>

<a id="restore-acs-roxctl-admin-pass_restoring-central-database-by-using-the-roxctl-cli"></a>

# Restoring by using the administrator password

You can restore the entire database of RHACS by using your administrator password.

<div>

<div class="title">

Prerequisites

</div>

- You have a RHACS backup file.

- You have the administrator password.

- You have installed the `roxctl` CLI.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the `ROX_ENDPOINT` environment variable by running the following command:

    ``` terminal
    $ export ROX_ENDPOINT=<address>:<port_number>
    ```

2.  Restore the Central database by running the following command:

    ``` terminal
    $ roxctl -p <admin_password> \
      central db restore <backup_file>
    ```

    where:

    `<admin_password>`  
    Specifies the administrator password.

    `<backup_file>`  
    Specifies the name of the backup file that you want to restore.

</div>

<a id="resume-acs-restore_restoring-central-database-by-using-the-roxctl-cli"></a>

# Resuming the restore operation

If your connection is interrupted during a restore operation or you need to go offline, you can resume the restore operation.

- If you do not have access to the machine running the resume operation, you can use the `roxctl central db restore status` command to check the status of an ongoing restore operation.

- If the connection is interrupted, the `roxctl` CLI automatically attempts to resume a task as soon as the connection is available again. The automatic connection retries depend on the duration specified by the `timeout` option.

- Use the `--timeout` option to specify the time in seconds, minutes or hours after which the `roxctl` CLI stops trying to resume a restore operation. If the option is not specified, the default timeout is 10 minutes.

- If a restore operation gets stuck or you want to cancel it, use the `roxctl central db restore cancel` command to cancel a running restore operation.

- If a restore operation is stuck, you have canceled it, or the time has expired, you can resume the earlier restore by running the original command again.

<div class="important">

<div class="title">

</div>

- During interruptions, RHACS caches an ongoing restore operation for 24 hours. You can resume this operation by executing the original restore command again.

- The `--timeout` option only controls the client-side connection retries and has no effect on the server-side restore cache of 24 hours.

- You cannot resume restores across Central pod restarts.

- If a restore operation is interrupted, you must restart it within 24 hours and before restarting Central, otherwise RHACS cancels the restore operation.

</div>
