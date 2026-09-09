<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Central stores information about the following:

- Activity observed in your clusters

- Information retrieved from integrated image registries or Scanners

- Red Hat Advanced Cluster Security for Kubernetes (RHACS) configuration

Backing up the Central database is critical to ensure data integrity and system reliability. Regular backups of the database, which contain the necessary configurations, resources, events, and certificates, protect against database failures, corruption, and accidental data loss.

You can use the `roxctl` CLI to back up and restore the Central database by using the `backup` command. This command requires an API token or your administrator password.

<a id="on-demand-backups-roxctl-api_backing-up-central-database-by-using-the-roxctl-cli"></a>

# On-demand backups by using an API token

You can back up the entire database of RHACS by using an API token.

<div>

<div class="title">

Prerequisites

</div>

- You have an API token with the `Admin` role.

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

2.  Initiate a backup for Central by running the following command:

    ``` terminal
    $ roxctl central backup
    ```

    You can use the `--output` option to specify the backup file location.

    By default, the `roxctl` CLI saves the backup file in the directory where you run the command.

</div>

<div>

<div class="title">

Additional resources

</div>

- [System roles](../operating/manage-user-access/manage-role-based-access-control-3630.md#rbac-system-roles-3630_manage-role-based-access-control)

</div>

<a id="on-demand-backups-roxctl-admin-pass_backing-up-central-database-by-using-the-roxctl-cli"></a>

# On-demand backups by using the administrator password

You can back up the entire database of RHACS by using your administrator password.

<div>

<div class="title">

Prerequisites

</div>

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

2.  Initiate a backup for Central by running the following command:

    ``` terminal
    $ roxctl -p <admin_password> central backup
    ```

    where:

    `<admin_password>`  
    Specifies the administrator password.

    By default, the `roxctl` CLI saves the backup file in the directory in which you run the command. You can use the `--output` option to specify the backup file location.

</div>
