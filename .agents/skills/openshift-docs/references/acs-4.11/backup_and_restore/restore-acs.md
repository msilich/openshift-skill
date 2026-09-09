<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can restore Red Hat Advanced Cluster Security for Kubernetes (RHACS) from an existing backup by using the `roxctl` command-line interface (CLI).

Depending upon your requirements and the data you have backed up, you can restore from the following types of backups:

1.  **Restore an external PostgreSQL database**: Use this to restore your RHACS instance when you use an external PostgreSQL database. You can recover your system data while maintaining your existing database setup.

2.  **Restore the Central certificates and redeploy Central**: Use this to restore the Central certificates and redeploy Central after a database restoration. This ensures that authentication certificates for secured clusters and API tokens remain valid.

3.  **Restore Central database from the Central database backup**: Use this to recover from a database failure or data corruption event. You can restore and recover the Central database to its earlier functional state.

4.  **Restore Central from the Central deployment backup**: Use this if you are migrating Central to another cluster or namespace. This option restores the configurations of your Central installation.

<a id="restoring-an-external-postgresql-database_restore-acs"></a>

# Restoring an external PostgreSQL database

By restoring an external PostgreSQL database, you can recover your Red Hat Advanced Cluster Security for Kubernetes (RHACS) instance from a backup while maintaining your existing database setup.

This procedure focuses on restoring the database that has your RHACS system data. You can perform a PostgreSQL database restore by using the vendor-recommended `pg_restore` command.

<div>

<div class="title">

Prerequisites

</div>

- You have scaled down Central to `0`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To perform a PostgreSQL restore, run the following command:

    ``` terminal
    $ pg_restore -U <username> -d <database_name> <path_to_backup_file>
    ```

    where:

    `<username>`  
    Specifies the actual user name.

    `<database_name>`  
    Specifies the name of the target database.

    `<path_to_backup_file>`  
    Specifies the location and name of the file you want to restore. You can use `.tar`, `.gz`, or another custom file format.

    After you restore the external PostgreSQL database, you must restore the RHACS Central certificates.

</div>

<a id="restoring-central-certificates-and-redeploying-central_restore-acs"></a>

# Restoring the central certificates and redeploying Central

You must restore the Central certificates and redeploy Central to ensure that authentication certificates for secured clusters and API tokens remain valid for the redeployed Central instance.

<div>

<div class="title">

Procedure

</div>

- Run the `roxctl central generate interactive` command and give the path to your backup file, which creates a central-bundle folder with the necessary manifests and scripts.

  You can then use these files to install Central, ensuring that all your authentication certificates and API tokens remain valid.

  For more

</div>

<div>

<div class="title">

Additional resources

</div>

- [Restore certificates using the roxctl CLI](restore-acs.md#restore-cert-roxctl_restore-acs)

</div>

<a id="restore-central-db-roxctl_restore-acs"></a>

# Restoring Central database by using the roxctl CLI

You can use the `roxctl` CLI to restore Red Hat Advanced Cluster Security for Kubernetes by using the `restore` command. You require an API token or your administrator password to run this command.

<a id="restore-acs-roxctl-api_restore-acs"></a>

## Restoring by using an API token

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

<a id="restore-acs-roxctl-admin-pass_restore-acs"></a>

## Restoring by using the administrator password

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

<a id="resume-acs-restore_restore-acs"></a>

## Resuming the restore operation

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

<a id="restore-central-deployment-roxctl_restore-acs"></a>

# Restoring Central deployment by using the roxctl CLI

You can restore your Central deployment to its original configuration by using the backups you made.

You must first restore certificates by using the `roxctl` CLI, and then restore the Central deployment by running the Central installation scripts.

<a id="restore-cert-roxctl_restore-acs"></a>

## Restore certificates by using the roxctl CLI

Use the `roxctl` CLI to generate Kubernetes manifests to install the RHACS Central component to your cluster. By doing this, you can ensure that authentication certificates for Secured clusters and the API tokens remain valid for the restored version. If you backed up another instance of RHACS Central, you can use the certificate files from that backup.

> [!NOTE]
> With the `roxctl` CLI, you cannot restore the entire Central deployment. Instead, first you use the `roxctl` CLI to generate new manifests using the certificates in your central data backup. Afterwards, you use those manifests to install Central.

<div>

<div class="title">

Prerequisites

</div>

- You must have the Red Hat Advanced Cluster Security for Kubernetes backup file.

- You must have installed the `roxctl` CLI.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the interactive install command:

    ``` terminal
    $ roxctl central generate interactive
    ```

2.  For the following prompt, enter the path of the Red Hat Advanced Cluster Security for Kubernetes backup file:

    ``` terminal
    Enter path to the backup bundle from which to restore keys and certificates (optional): _<backup_file_path>_
    ```

3.  For other following prompts, press Enter to accept the default value or enter custom values as required.

    On completion, the interactive install command creates a folder named `central-bundle`, which has the necessary YAML manifests and scripts to deploy Central.

</div>

<a id="install-central-roxctl_restore-acs"></a>

## Running the Central installation scripts

After you run the interactive installer, you can run the `setup.sh` script to install Central.

<div>

<div class="title">

Procedure

</div>

1.  Run the `setup.sh` script to configure image registry access:

    ``` terminal
    $ ./central-bundle/central/scripts/setup.sh
    ```

2.  Create the necessary resources:

    ``` terminal
    $ oc create -R -f central-bundle/central
    ```

3.  Check the deployment progress:

    ``` terminal
    $ oc get pod -n stackrox -w
    ```

4.  After Central is running, find the RHACS portal IP address and open it in your browser. Depending on the exposure method you selected when answering the prompts, use one of the following methods to get the IP address.

    | Exposure method | Command | Address | Example |
    |----|----|----|----|
    | **Route** | `oc -n stackrox get route central` | The address under the `HOST/PORT` column in the output | `https://central-stackrox.example.route` |
    | **Node Port** | `oc get node -owide && oc -n stackrox get svc central-loadbalancer` | IP or hostname of any node, on the port shown for the service | `https://198.51.100.0:31489` |
    | **Load Balancer** | `oc -n stackrox get svc central-loadbalancer` | EXTERNAL-IP or hostname shown for the service, on port 443 | `https://192.0.2.0` |
    | **None** | `central-bundle/central/scripts/port-forward.sh 8443` | `https://localhost:8443` | `https://localhost:8443` |

    > [!NOTE]
    > If you have selected autogenerate password during the interactive install, you can run the following command to see it for logging into Central:
    >
    > ``` terminal
    > $ cat central-bundle/password
    > ```

</div>

<a id="restore-deployment-config-operator_restore-acs"></a>

# Restore Central deployment by using the RHACS Operator

You can restore your Central deployment to its original configuration by using the RHACS Operator. To successfully restore, you need the backup of your Central custom resource, `central-tls`, and the administrator password.

<div>

<div class="title">

Prerequisites

</div>

- You must have the `central-tls` backup file.

- You must have the Central custom resource backup file.

- You must have the administrator password backup file.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Use the `central-tls` backup file to create resources:

    ``` terminal
    $ oc apply -f central-tls.json
    ```

2.  Use the `central-htpasswd` backup file to create secrets:

    ``` terminal
    $ oc apply -f central-htpasswd.json
    ```

3.  Use the `central-cr.yaml` file to create the Central deployment:

    ``` terminal
    $ oc apply -f central-cr.yaml
    ```

</div>

<a id="restore-deployment-config-helm_restore-acs"></a>

# Restore Central deployment using Helm

You can restore your Central deployment to its original configuration by using Helm. To successfully restore, you need the backup of your Central custom resource, the `central-tls` secret, and the administrator password.

<div>

<div class="title">

Prerequisites

</div>

- You must have the Helm values backup file.

- You must have a Red Hat Advanced Cluster Security for Kubernetes backup file.

- You must have installed the `roxctl` CLI.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Generate `values-private.yaml` from the RHACS database backup file:

    ``` terminal
    $ roxctl central generate k8s pvc --backup-bundle _<path_to_backup_file>_ --output-format "helm-values"
    ```

2.  Run the `helm install` command and specify your backup files:

    ``` terminal
    $ helm install -n stackrox --create-namespace stackrox-central-services rhacs/central-services -f central-values-backup.yaml -f central-bundle/values-private.yaml
    ```

</div>

<a id="restore-central-another-cluster_restore-acs"></a>

# Restoring Central to another cluster or namespace

You can use the backups of the RHACS Central database and the deployment to restore Central to another cluster or namespace.

The following list provides a high-level overview of installation steps:

1.  Depending upon your installation method, you must first restore Central deployment.

    <div class="important">

    <div class="title">

    </div>

    - Make sure to use the backed-up Central certificates so that secured clusters and API tokens issued by the old Central instance remain valid.

    - If you are deploying to another namespace, you must change the namespace in backed-up resources or commands.

    </div>

    - Restore Central deployment by using the `roxctl` CLI.

    - Restore Central deployment by using the RHACS Operator.

    - Restore Central deployment by using Helm.

2.  Restore Central database by using the `roxctl` CLI.

3.  If you have an external DNS entry pointing to your old RHACS Central instance, you must reconfigure it to point to the new RHACS Central instance that you create.

<div>

<div class="title">

Additional resources

</div>

- [Restoring Central deployment by using the roxctl CLI](restore-acs.md#restore-central-deployment-roxctl_restore-acs)

- [Restore Central deployment by using the RHACS Operator](restore-acs.md#restore-deployment-config-operator_restore-acs)

- [Restore Central deployment by using Helm](restore-acs.md#restore-deployment-config-helm_restore-acs)

- [Restoring Central database by using the roxctl CLI](restore-acs.md#restore-central-db-roxctl_restore-acs)

</div>
