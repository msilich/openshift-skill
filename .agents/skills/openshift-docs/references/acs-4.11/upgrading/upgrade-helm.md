<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You must follow a specific upgrade path for RHACS depending on the release of RHACS that you are running. You must also back up your Central database before updating the Helm chart and performing the upgrade.

> [!IMPORTANT]
> In RHACS 4.11, all container image names changed from the `-rhel8` suffix to `-rhel9` as part of the migration to UBI 9 Minimal base images. For example, `rhacs-main-rhel8` is now `rhacs-main-rhel9`.
>
> If you use image mirrors, allowlists, or firewall rules that reference specific RHACS image names, you must update them to use the new `-rhel9` names before upgrading.

<a id="helm-upgrade-overview_upgrade-helm"></a>

# Helm upgrade overview

If you have installed RHACS by using Helm charts, you must follow specific steps to upgrade to the latest version.

1.  Back up the Central database.

2.  Optional: Optimize Central’s database and Persistent Volume Claim (PVC).

3.  Optional: Generate a `values-private.yaml` configuration file containing root certificates for the central-services Helm chart.

4.  Run the `helm upgrade` command.

<div class="important">

<div class="title">

</div>

- To ensure optimal functionality, use the same version for your secured-cluster-services Helm chart and central-services Helm chart.

- To upgrade to RHACS 4.8, which includes an upgrade to PostgreSQL 15, you must free up disk space. Before beginning the upgrade, ensure that you have free disk space that is at least double the size of your existing database.

</div>

<a id="back-up-central-database_upgrade-helm"></a>

# Backing up the Central database

You can back up the Central database and use that backup for rolling back from a failed upgrade or data restoration in the case of an infrastructure disaster.

<div>

<div class="title">

Prerequisites

</div>

- You must have an API token with `read` permission for all resources of Red Hat Advanced Cluster Security for Kubernetes. The **Analyst** system role has `read` permissions for all resources.

- You have installed the `roxctl` CLI.

- You have configured the `ROX_API_TOKEN` and the `ROX_CENTRAL_ADDRESS` environment variables.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the backup command:

  ``` terminal
  $ roxctl -e "$ROX_CENTRAL_ADDRESS" central backup
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [On-demand backups by using the roxctl CLI](../backup_and_restore/backing-up-acs.md)

- [Installing the roxctl CLI](../cli/installing-the-roxctl-cli.md)

</div>

<a id="helm-optimize-central-db-and-pvc_upgrade-helm"></a>

# Optimizing the Central database and persistent volume claims

When you upgrade to Red Hat Advanced Cluster Security for Kubernetes (RHACS) 4.0, RHACS creates a PostgreSQL instance called `central-db`. This instance uses a default Persistent Volume Claim (PVC). You can customize the `central-db` or PVC configuration.

Red Hat recommends the following minimum memory and CPU requests:

``` yaml
central:
  db:
    resources:
      requests:
        memory: 16Gi
        cpu: 8
      limits:
        memory: 16Gi
        cpu: 8
```

<a id="helm-generate-root-certificates_upgrade-helm"></a>

# Generating root certificates file

If you do not have access to your `values-private.yaml` configuration file that you have used to install Red Hat Advanced Cluster Security for Kubernetes (RHACS), use the following instruction to generate the `values-private.yaml` configuration file containing root certificates.

Skip the instruction here, if you have access to your `values-private.yaml` configuration file.

> [!IMPORTANT]
> The generated `values-private.yaml` file has sensitive configuration options. Ensure that you store this file securely.

<div>

<div class="title">

Procedure

</div>

1.  Download the [`create_certificate_values_file.sh`](https://raw.githubusercontent.com/openshift/openshift-docs/rhacs-docs-main/files/create_certificate_values_file.sh) script.

2.  Make the `create_certificate_values_file.sh` script executable:

    ``` terminal
    $ chmod +x create_certificate_values_file.sh
    ```

3.  Run the `create_certificate_values_file.sh` script file:

    ``` terminal
    $ create_certificate_values_file.sh values-private.yaml
    ```

</div>

<a id="updating-helm-repository_upgrade-helm"></a>

# Updating the Helm chart repository

You must always update Helm charts before upgrading to a new version of Red Hat Advanced Cluster Security for Kubernetes.

<div>

<div class="title">

Prerequisites

</div>

- You must have already added the Red Hat Advanced Cluster Security for Kubernetes Helm chart repository.

- You must be using Helm version 3.8.3 or newer.

</div>

<div>

<div class="title">

Procedure

</div>

- Update Red Hat Advanced Cluster Security for Kubernetes charts repository.

  ``` terminal
  $ helm repo update
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Run the following command to verify the added chart repository:

  ``` terminal
  $ helm search repo -l rhacs/
  ```

</div>

<a id="additional-resources_upgrade-helm"></a>

# Additional resources

- [Installing Central using Helm charts](../installing/installing_ocp/install-central-ocp.md)

- [Installing RHACS on secured clusters by using Helm charts](../installing/installing_ocp/install-secured-cluster-ocp.md)

<a id="upgrade-crd-helm_upgrade-helm"></a>

# Preparing the custom resource definition for upgrade

If upgrading from version 4.6 or 4.7, you must prepare the `SecurityPolicy` custom resource definition (CRD) to avoid upgrade errors.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

- Apply Helm-specific labels and annotations to the CRD by running the following commands:

  ``` terminal
  $ oc annotate crd/securitypolicies.config.stackrox.io meta.helm.sh/release-name=stackrox-central-services
  ```

  Adjust the value of the `release-name` as needed. The default value is `stackrox-central-services`.

  ``` terminal
  $ oc annotate crd/securitypolicies.config.stackrox.io meta.helm.sh/release-namespace=stackrox
  ```

  Adjust the value of the `release-namespace` as needed. The default value is `stackrox`.

  ``` terminal
  $ oc label crd/securitypolicies.config.stackrox.io app.kubernetes.io/managed-by=Helm
  ```

</div>

<a id="upgrade-helm-chart_upgrade-helm"></a>

# Running the Helm upgrade command

You can use the `helm upgrade` command to update Red Hat Advanced Cluster Security for Kubernetes (RHACS).

<div>

<div class="title">

Prerequisites

</div>

- You must have access to the `values-private.yaml` configuration file that you have used to install Red Hat Advanced Cluster Security for Kubernetes (RHACS). Otherwise, you must generate the `values-private.yaml` configuration file containing root certificates before proceeding with these commands.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the helm upgrade command and specify the configuration files by using the `-f` option:

  ``` terminal
  $ helm upgrade -n stackrox stackrox-central-services \
    rhacs/central-services --version <current_rhacs_version> \
    -f values-private.yaml \
    --set central.db.password.generate=true \
    --set central.db.serviceTLS.generate=true \
    --set central.db.persistence.persistentVolumeClaim.createClaim=true
  ```

  ``` terminal
  $ helm upgrade -n stackrox stackrox-secured-cluster-services \
    rhacs/secured-cluster-services --version <current_rhacs_version> \
    -f values-private.yaml
  ```

  > [!NOTE]
  > You might use the `--reuse-values` option to preserve the Helm values that you configured before the upgrade. If you do that, you must turn off `central-db` creation before you upgrade to the next version.
  >
  > See the following command example:
  >
  > ``` terminal
  > $ helm upgrade -n stackrox stackrox-central-services \
  >   rhacs/central-services --version <current_rhacs_version> --reuse-values \
  >   -f values-private.yaml \
  >   --set central.db.password.generate=false \
  >   --set central.db.serviceTLS.generate=false \
  >   --set central.db.persistence.persistentVolumeClaim.createClaim=false
  > ```

</div>

<a id="rollback-helm-upgrade_upgrade-helm"></a>

# Rolling back a Helm upgrade

You can roll back to an earlier version of Central if the upgrade to a new version is unsuccessful.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Run the following `helm upgrade` command:

    ``` terminal
    $ helm upgrade -n stackrox \
      stackrox-central-services rhacs/central-services \
      --version <previous_rhacs_74_version> \
      --set central.db.enabled=false
    ```

    where:

    `<previous_rhacs_74_version>`  
    Specifies the RHACS version installed before the upgrade.

2.  Delete the `central-db` persistent volume claim (PVC):

    ``` terminal
    $ oc -n stackrox delete pvc central-db
    ```

</div>
