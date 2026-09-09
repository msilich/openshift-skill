<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can perform data backups for Red Hat Advanced Cluster Security for Kubernetes and use these for data restoration in case of an infrastructure disaster or corrupt data.

You can configure automatic backups for the Central database by integrating with Amazon S3, S3 API compatible services, or Google Cloud Storage. You can perform on-demand backups of the Central database by using the `roxctl` CLI. You can also back up your Central deployment by using RHACS Operator or Helm Chart installation methods.

Depending on your requirements, you can create two types of backups:

1.  A backup of the Central database: It includes RHACS configurations, resources, events, and certificates. In an unforeseen incident, such as database failure or data corruption, you can use the backup to recover and restore the Central database to its earlier functional state. Doing this ensures the availability and integrity of essential data, allowing you to continue normal operations without significant disruptions or loss of critical information.

2.  A backup of all custom deployment configurations: If you installed RHACS by using Helm charts or the RHACS Operator, you can back up settings, parameters, and customizations specific to your installation. When the RHACS installation gets accidentally deleted, or you need to migrate it to another cluster or namespace, having a backup of the deployment configurations enables a seamless recovery process. In addition, by restoring the custom settings from the backup, you can efficiently reinstate your Central installation’s unique requirements and configurations, ensuring consistent and exact deployment of the system.

> [!IMPORTANT]
> Because backup files include secrets and certificates, you must securely store the backup files.

<div>

<div class="title">

Additional resources

</div>

- [Perform on-demand backups with Amazon S3](../integration/integrate-with-amazon-s3.md#perform-on-demand-backups-amazon-s3_integrate-with-amazon-s3)

- [Perform on-demand backups with S3 API compatible services](../integration/integrate-with-s3-api-compatible-services.md#perform-on-demand-backups-s3-api-compatible-services_integrate-with-s3-api-compatible-services)

- [Perform on-demand backups with Google Cloud Storage](../integration/integrate-with-google-cloud-storage.md#perform-on-demand-backups-google-cloud-storage_integrate-with-google-cloud-storage)

</div>

<a id="backup-considerations-for-external-databases-and-cloud-users_backing-up-acs"></a>

# Backup considerations for external databases and cloud users

You must manage your backups differently if you use an external database or if you are a cloud user.

<a id="backup-external-database_backing-up-acs"></a>

## Back up with an external database

If you use an external database, you cannot use the automatic backup option or start a backup process from within Red Hat Advanced Cluster Security for Kubernetes (RHACS).

<div class="important">

<div class="title">

</div>

- When you upgrade your external database, you must scale down Central before you start the backup. Central attempts to connect to the database until it is successful, which can cause issues during the upgrade process.

- For a database that you manage, you must use the backup procedures that your database vendor recommends.

</div>

<a id="backup-cloud-users_backing-up-acs"></a>

## Back up for cloud users

If you are a cloud user, you cannot use the automatic backup option or start the backup process from an integration. Red Hat is responsible for backing up your data.

<a id="backing-up-your-postgresql-database-and-certificates_backing-up-acs"></a>

## Backing up your PostgreSQL database and certificates

By backing up your Red Hat Advanced Cluster Security for Kubernetes (RHACS) instance with an external PostgreSQL database, you can ensure the security and integrity of your data by following a vendor-recommended procedure. In this process, you back up the PostgreSQL database first, and then back up the RHACS certificates.

<div>

<div class="title">

Procedure

</div>

1.  To back up the PostgreSQL database, run the following command:

    ``` terminal
    $ pg_dump -U <username> -d <database_name> -f <output_file_path>
    ```

    where:

    `<username>`  
    Specifies the name of the user who has the necessary permissions to perform the dump.

    `<database_name>`  
    Specifies the actual name of the database.

    `<output_file_path>`  
    Specifies the desired location and name for your backup file.

2.  To back up the RHACS certificates, run the following command:

    ``` terminal
    $ roxctl central backup --certs-only=true
    ```

</div>

<a id="backing-up-central-db-roxctl_backing-up-acs"></a>

# Backing up Central database by using the roxctl CLI

Backing up the Central database is critical to ensure data integrity and system reliability. Regular backups of the database, containing necessary configurations, resources, events, and certificates, protect against database failures, corruption, and accidental data loss.

You can use the `roxctl` CLI to take the backups by using the `backup` command. You require an API token or your administrator password to run this command.

> [!NOTE]
> Red Hat supports backups for the Central database through integration with Amazon S3 or Google Cloud Storage.
>
> Backing up to S3 API compatible storage is not guaranteed to work. Red Hat does not test and support every S3 API compatible provider for backing up RHACS.

<div>

<div class="title">

Additional resources

</div>

- [Perform on-demand backups with Amazon S3](../integration/integrate-with-amazon-s3.md#perform-on-demand-backups-amazon-s3_integrate-with-amazon-s3)

- [Perform on-demand backups with Google Cloud Storage](../integration/integrate-with-google-cloud-storage.md#perform-on-demand-backups-google-cloud-storage_integrate-with-google-cloud-storage)

- [Integrate with S3 API compatible services](../integration/integrate-with-s3-api-compatible-services.md)

</div>

<a id="on-demand-backups-roxctl-api_backing-up-acs"></a>

## On-demand backups by using an API token

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

<a id="on-demand-backups-roxctl-admin-pass_backing-up-acs"></a>

## On-demand backups by using the administrator password

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

<a id="backing-up-central-deployment_backing-up-acs"></a>

# Backing up Central deployment

You can back up the deployment of a Central instance. This backup can be useful if you want to migrate Central to another namespace or cluster by using the same configuration values.

> [!NOTE]
> Red Hat does not support backing up deployment configurations by using the `roxctl` CLI. You can use the `oc` or `kubectl` CLI to back up manifests related to your Central instance and restore the configuration.

<a id="backup-deployment-config-operator_backing-up-acs"></a>

## Backing up deployment using the RHACS Operator

When you use the RHACS Operator to instal RHACS, OpenShift Container Platform stores all the custom configuration for your Central deployment within the Central custom resource. You can backup the Central custom resource, the `central-tls` secret, and the administrator password. The `central-tls` secret includes the certificates for authenticating with Secured clusters and signing API tokens.

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to save the Central custom resource in a YAML file:

    ``` terminal
    $ oc get central -n _<central-namespace>_ _<central-name>_ -o yaml > central-cr.yaml
    ```

2.  Run the following command to save `central-tls` in a JSON file:

    ``` terminal
    $ oc get secret -n _<central-namespace>_ central-tls -o json | jq 'del(.metadata.ownerReferences)' > central-tls.json
    ```

3.  Run the following command to the administrator password in a JSON file:

    ``` terminal
    $ oc get secret -n _<central-namespace>_ central-htpasswd -o json | jq 'del(.metadata.ownerReferences)' > central-htpasswd.json
    ```

</div>

<a id="backup-deployment-config-helm_backing-up-acs"></a>

## Backing up deployment using Helm

When you use the Helm chart to install RHACS, you store all the custom configuration for your Central deployment within the custom values that you apply to the Helm chart.

You can back up the custom values and save it in a YAML file.

<div>

<div class="title">

Procedure

</div>

- Run the following command to back up custom Helm chart values in a YAML file:

  ``` terminal
  $ helm get values --all -n _<central-namespace>_ _<central-helm-release>_ -o yaml > central-values-backup.yaml
  ```

</div>
