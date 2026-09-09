<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Each component of Red Hat Advanced Cluster Security for Kubernetes uses an X.509 certificate to authenticate itself to other components. These certificates have expiration dates, and you must reissue, or rotate, certificates before they expire. You can view the certificate expiration dates by selecting **Platform Configuration** → **Clusters** in the RHACS portal and viewing the **Credential Expiration** column.

<a id="reissuing-internal-certificates-for-central-services_reissue-internal-certificates"></a>

# Reissuing internal certificates for Central services

The Central services contain the Central, Central DB, Scanner, and Scanner V4 components. The Central services use a built-in server certificate for authentication when communicating with other Red Hat Advanced Cluster Security for Kubernetes (RHACS) services. This certificate is unique to your Central service installation. The RHACS portal shows an informational banner when a Central service certificate is about to expire.

> [!NOTE]
> The informational banner is only displayed 15 days before the certificate expiration date.

Beginning with RHACS 4.3.4, the Operator automatically rotates the service transport layer security (TLS) certificates for all of the Central components 6 months before they expire.

<div class="important">

<div class="title">

</div>

- The automated rotation of the TLS certificates applies only to Operator-based installations. For all other installation methods, you must manually rotate the TLS certificates.

- The rotation of the TLS certificates within the secrets does not automatically trigger the components to reload them. If the corresponding pods are not restarted at least every 6 months, you must manually restart the pods to load the new certificates before the old ones expire.

- Certificate authority (CA) certificates are not updated. They are valid for 5 years.

</div>

<a id="reissue-internal-certificates-central_reissue-internal-certificates"></a>

## Reissuing internal certificates for Central

You can maintain a secure communication between Central and other Red Hat Advanced Cluster Security for Kubernetes (RHACS) components by reissuing the internal certificates.

<div>

<div class="title">

Prerequisites

</div>

- You have `write` permission for the `Administration` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click the link in the banner that announces the certificate expiration to download a YAML configuration file, which contains a new secret. The secret includes the certificate and key values.

2.  To apply the new YAML configuration file to the cluster where you have installed Central, run the following command:

    ``` terminal
    $ oc apply -f <secret_file.yaml>
    ```

3.  To apply the changes, restart Central.

</div>

<a id="restart-central_reissue-internal-certificates"></a>

### Restarting the Central container

You can restart the Central container by deleting the Central pod.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

- To delete the Central pod, run the following command:

  ``` terminal
  $ oc -n stackrox delete pod -lapp=central
  ```

</div>

<a id="reissuing-internal-certificates-for-central-db_reissue-internal-certificates"></a>

## Reissuing internal certificates for Central DB

You can maintain a secure communication between Central DB and other Red Hat Advanced Cluster Security for Kubernetes (RHACS) components by reissuing the internal certificates.

<div>

<div class="title">

Prerequisites

</div>

- You have `write` permission for the `Administration` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click the link in the banner that announces the certificate expiration to download a YAML configuration file, which contains a new secret. The secret includes the certificate and key values.

2.  To apply the new YAML configuration file to the cluster where you have installed Central DB, run the following command:

    ``` terminal
    $ oc apply -f <secret_file.yaml>
    ```

3.  To apply the changes, restart Central DB.

</div>

<a id="restarting-the-central-db-container_reissue-internal-certificates"></a>

### Restarting the Central DB container

You can restart the Central DB container by deleting the Central DB pod.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

- To delete the Central DB pod, run the following command:

  ``` terminal
  $ oc -n stackrox delete pod -lapp=central-db
  ```

</div>

<a id="reissue-internal-certificates-scanner_reissue-internal-certificates"></a>

## Reissuing internal certificates for Scanner

You can maintain a secure communication between Scanner and other Red Hat Advanced Cluster Security for Kubernetes (RHACS) components by reissuing the internal certificates.

<div>

<div class="title">

Prerequisites

</div>

- You have `write` permission for the `Administration` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Click the link in the banner to download a YAML configuration file, which contains a new OpenShift Container Platform secret, including the certificate and key values.

2.  To apply the new YAML configuration file to the cluster where you have installed Scanner, run the following command:

    ``` terminal
    $ oc apply -f <secret_file.yaml>
    ```

3.  To apply the changes, restart Scanner.

</div>

<a id="restart-scanner_reissue-internal-certificates"></a>

### Restarting the Scanner and Scanner DB containers

You can restart the Scanner and Scanner DB containers by deleting the pods.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

- To delete the Scanner pods, run the following command:

  ``` terminal
  $ oc delete pod -n stackrox -l app=scanner
  ```

- To delete the Scanner DB pods, run the following command:

  ``` terminal
  $ oc -n stackrox delete pod -l app=scanner-db
  ```

</div>

<a id="reissuing-internal-certificates-for-scanner-v4_reissue-internal-certificates"></a>

## Reissuing internal certificates for Scanner V4

You can maintain a secure communication between Scanner V4 and other Red Hat Advanced Cluster Security for Kubernetes (RHACS) components by reissuing the internal certificates.

<div>

<div class="title">

Prerequisites

</div>

- You have `write` permission for the `Administration` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Click the link in the banner to download a YAML configuration file, which contains a new OpenShift Container Platform secret, including the certificate and key values.

2.  To apply the new YAML configuration file to the cluster where you have installed Scanner V4, run the following command:

    ``` terminal
    $ oc apply -f <secret_file.yaml>
    ```

3.  To apply the changes, restart Scanner V4.

</div>

<a id="restarting-the-scanner-v4-containers_reissue-internal-certificates"></a>

### Restarting the Scanner V4 containers

You can restart the Scanner V4 Matcher, Indexer and DB containers by deleting their corresponding pods.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

- To delete the Scanner V4 Matcher pod, run the following command:

  ``` terminal
  $ oc delete pod -n stackrox -l app=scanner-v4-matcher
  ```

- To delete the Scanner V4 Indexer pod, run the following command:

  ``` terminal
  $ oc delete pod -n stackrox -l app=scanner-v4-indexer
  ```

- To delete the Scanner V4 DB pod, run the following command:

  ``` terminal
  $ oc delete pod -n stackrox -l app=scanner-v4-db
  ```

</div>

<a id="reissue-internal-certificates-secured-clusters_reissue-internal-certificates"></a>

# Reissuing internal certificates for secured clusters

Secured clusters contain the Collector, Sensor, Admission Control, and local Scanner components. These components communicate with each other, and with Central by using certificates.

Choose the appropriate method to reissue the internal certificates:

- Use the automatic certificate renewal feature. This is the recommended method for Operator and Helm deployments. It is the only supported method for installations if you used a cluster registration secret (CRS) to set up communication between Central and secured clusters.

- Generate, download, and install an init bundle on the secured cluster. You must have the `Admin` user role to generate an init bundle. This method is only recommended for Operator and Helm deployments if the certificates have already expired and the secured cluster can no longer connect to Central.

- Use the automatic upgrades feature, which is only available for static manifest deployments by using the `roxctl` CLI. This method is only recommended if you have a specific installation requirement that necessitates the use of this method.

<a id="reissuing-internal-certificates-for-secured-clusters-by-using-automatic-certificate-renewal_reissue-internal-certificates"></a>

## Reissuing internal certificates for secured clusters by using automatic certificate renewal

Secured clusters contain the Collector, Sensor, Admission Control, and local Scanner components. You can reissue internal certificates for these components by using automatic certificate renewal.

TLS certificates are automatically renewed several months in advance but are only loaded when RHACS pods restart, for example, during an upgrade.

<a id="verifying-the-status-of-automatic-certificate-renewal_reissue-internal-certificates"></a>

### Verifying the status of automatic certificate renewal

By viewing the **Clusters** page, you can verify that the automatic certificate renewal is active.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Platform Configuration** → **Clusters**.

2.  Verify that **Auto-refresh enabled** is displayed in the **Credential Expiration** column.

    > [!IMPORTANT]
    > If a secured cluster displays a warning about soon-to-expire credentials even though auto-refresh is enabled, you must manually restart the pods of the affected cluster to apply the latest certificates and prevent downtime.
    >
    > For more information, see "Applying the latest internal certificates".

</div>

<a id="applying-the-latest-internal-certificates_reissue-internal-certificates"></a>

### Applying the latest internal certificates

By manually restarting the pods of the affected cluster, you can apply the latest certificates and prevent downtime.

> [!NOTE]
> If you use Kubernetes, use `kubectl` instead of `oc`.

<div>

<div class="title">

Prerequisites

</div>

- You have `write` permission for the `Administration` resource.

</div>

<div>

<div class="title">

Procedure

</div>

- To manually restart the pods of the affected cluster, run the following command:

  ``` terminal
  $ oc -n <namespace> delete pods --all
  ```

  where:

  `<namespace>`  
  Specifies the namespace where you installed the secured cluster. For example, `stackrox`.

</div>

<a id="reissue-internal-certificates-secured-cluster_reissue-internal-certificates"></a>

## Reissuing internal certificates for secured clusters by using init bundles

Secured clusters contain the Collector, Sensor, Admission Control, and local Scanner components. These components use a built-in server certificate for authentication when communicating with other Red Hat Advanced Cluster Security for Kubernetes (RHACS) components.

The RHACS portal shows an information banner when the Central certificate is about to expire.

> [!NOTE]
> The information banner is only displayed 15 days before the certificate expiry date.

<div>

<div class="title">

Prerequisites

</div>

- You have `write` permission for the `Administration` resource.

- You have the `Admin` user role to create init bundles.

</div>

> [!IMPORTANT]
> Store the init bundle securely because it has secrets. You can use the same bundle to set up more than one secured cluster.

<div>

<div class="title">

Procedure

</div>

- Generate an init bundle by using the RHACS portal or by using the `roxctl CLI`, and then apply the bundle to the secured cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Generating and applying a cluster registration secret or an init bundle for RHACS on Red Hat OpenShift](../installing/installing_ocp/init-bundle-ocp.md)

- [Generating and applying a cluster registration secret or an init bundle for RHACS on other platforms](../installing/installing_other/init-bundle-other.md)

</div>

<a id="reissue-internal-certificates-secured-clusters-automatic-upgrade_reissue-internal-certificates"></a>

## Reissuing internal certificates for secured clusters by using automatic upgrades

Secured clusters contain the Collector, Sensor, Admission Control, and local Scanner components. You can reissue internal certificates for these components by using automatic upgrades.

> [!IMPORTANT]
> Automatic upgrades are only applicable to static manifest-based deployments by using the `roxctl` CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have enabled automatic upgrades for all the clusters.

- You have `write` permission for the `Administration` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Platform Configuration** → **Clusters**.

2.  Select a cluster to view its details.

3.  From the cluster details panel, select the link to **Apply credentials by using an automatic upgrade**.

    > [!NOTE]
    > When you apply an automatic upgrade, Red Hat Advanced Cluster Security for Kubernetes (RHACS) creates new credentials in the selected cluster. However, you continue to see a notification. The notification disappears when each RHACS service uses the new credentials after the service restarts.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Install Central using the roxctl CLI](../installing/installing_ocp/install-central-ocp.md)

</div>
