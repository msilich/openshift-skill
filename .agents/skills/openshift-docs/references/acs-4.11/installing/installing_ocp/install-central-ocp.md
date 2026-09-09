<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Central is the resource that contains the Red Hat Advanced Cluster Security for Kubernetes (RHACS) application management interface and services. It handles data persistence, API interactions, and RHACS portal access. You can use the same Central instance to secure many OpenShift Container Platform or Kubernetes clusters.

You can install Central on your OpenShift Container Platform or Kubernetes cluster by using one of the following methods:

- Install using the Operator

- Install using Helm charts

- Install using the `roxctl` CLI (do not use this method unless you have a specific installation need that requires using it)

<a id="install-central-using-operator_install-central-ocp"></a>

# Install Central by using the Operator

To install Central, first install the Operator. Then, use the Operator to install RHACS on the cluster where you want Central.

<a id="install-acs-operator-annotations_install-central-ocp"></a>

## Operator annotations used during installation

RHACS uses annotations attached to the custom resource (CR) so that for installations performed by using the Operator, the Operator determines the default values for certain configuration items at runtime based on the current environment, allowing the previously configured value of an item to persist.

For some configuration items, using a static default value for the installation is not ideal. Beginning with RHACS version 4.8, the Operator can add annotations, attaching them to the CR that you apply to clusters. These annotations allow a default decision that the Operator made before to persist and reapply in the future, even if the default behavior for a fresh installation has changed. In summary, RHACS uses annotations to persist runtime defaults. This means that the Operator determines the default value for a certain configuration setting at runtime.

For example, in release 4.8 and later, if a value is not specified for enabling Scanner V4, the default behavior is to enable Scanner V4. However, if you configure a value in the CR, such as `disable`, then RHACS uses that value. In the Scanner V4 example, Scanner V4 disabled by default in version 4.7; when updating to version 4.8 by using the Operator, that disabled setting persists and Scanner V4 remains disabled.

Annotations are in the form `feature-defaults.platform.stackrox.io/<identifier>`. For example, `feature-defaults.platform.stackrox.io/scannerV4` is the annotation that allows the Operator to keep the default Scanner V4 enablement toggle stable during updating to RHACS version 4.8.

> [!IMPORTANT]
> Do not change or delete these annotations.

<a id="install-acs-operator_install-central-ocp"></a>

## Installing the Red Hat Advanced Cluster Security for Kubernetes Operator

Using the Software Catalog provided with OpenShift Container Platform is the easiest way to install Red Hat Advanced Cluster Security for Kubernetes.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster using an account with Operator installation permissions.

- You must be using OpenShift Container Platform 4.12 or later. For information about supported platforms and architecture, see the "Red Hat Advanced Cluster Security for Kubernetes Support Matrix". For life cycle support information for RHACS, see the "Red Hat Advanced Cluster Security for Kubernetes Support Policy".

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the web console, go to the **Ecosystem** → **Software Catalog** page.

2.  If Red Hat Advanced Cluster Security for Kubernetes is not displayed, enter **Advanced Cluster Security** into the **Filter by keyword** box to find the Red Hat Advanced Cluster Security for Kubernetes Operator. You might have to select a project first.

3.  Select the **Red Hat Advanced Cluster Security for Kubernetes Operator** to view the details page.

4.  Read the information about the Operator, and then click **Install**.

5.  On the **Install Operator** page:

    - Keep the default value for **Installation mode** as **All namespaces on the cluster**.

    - Choose a specific namespace in which to install the Operator for the **Installed namespace** field. Install the Red Hat Advanced Cluster Security for Kubernetes Operator in the **rhacs-operator** namespace.

    - Select automatic or manual updates for **Update approval**.

      If you choose automatic updates, when a new version of the Operator is available, Operator Lifecycle Manager (OLM) automatically upgrades the running instance of your Operator.

      If you choose manual updates, when a newer version of the Operator is available, OLM creates an update request. As a cluster administrator, you must manually approve the update request to update the Operator to the latest version.

      > [!IMPORTANT]
      > If you choose manual updates, you must update the RHACS Operator in all secured clusters when you update the RHACS Operator in the cluster where Central is installed. The secured clusters and the cluster where Central is installed must have the same version to ensure optimal functionality.

6.  Click **Install**.

</div>

<div>

<div class="title">

Verification

</div>

- After the installation completes, go to **Ecosystem** → **Installed Operators** to verify that the Red Hat Advanced Cluster Security for Kubernetes Operator is listed with the status of **Succeeded**.

</div>

After you install the Operator into the **rhacs-operator** project, you can install, configure, and deploy the `Central` custom resource (CR) into the `stackrox` project by using the installed Operator.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

- [Red Hat Advanced Cluster Security for Kubernetes Support Policy](https://access.redhat.com/support/policy/updates/rhacs)

</div>

<a id="configuring-the-rhacs-operator-for-infrastructure-nodes_install-central-ocp"></a>

### Configuring the RHACS Operator for infrastructure nodes

To deploy the Red Hat Advanced Cluster Security for Kubernetes (RHACS) Operator on infrastructure nodes, you can change its subscription YAML to include `nodeSelector` and `tolerations` to ensure that infrastructure nodes schedule Operator pods correctly.

<div>

<div class="title">

Procedure

</div>

1.  Configure the RHACS Operator with the necessary `nodeSelector` and `tolerations` for infrastructure nodes before you apply the Operator Lifecycle Manager (OLM) subscription by using the following content, for example:

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      labels:
        operators.coreos.com/rhacs-operator.rhacs-operator: ""
      name: rhacs-operator
      namespace: rhacs-operator
    spec:
      channel: stable
      config:
        nodeSelector:
          node-role.kubernetes.io/infra: "" #
        tolerations:
          - effect: NoSchedule
            key: node-role.kubernetes.io/infra #
            operator: Exists
      installPlanApproval: Automatic
      name: rhacs-operator
      source: redhat-operators
      sourceNamespace: openshift-marketplace
    ```

    where:

    `spec.config.nodeSelector.node-role.kubernetes.io/infra`  
    Specifies the `nodeSelector` key and value to instruct the Kubernetes scheduler to place the Operator pods on nodes that have the label `node-role.kubernetes.io/infra: ""`.

    `spec.config.tolerations.key`  
    Specifies the `tolerations` entry, which allows nodes with a taint matching the `node-role.kubernetes.io/infra` key to schedule the Operator pods. This is necessary as infrastructure nodes typically have a taint to prevent them from scheduling non-infrastructure workloads.

2.  Save the YAML file and apply it by using the OpenShift CLI (`oc`).

    When you apply the YAML file, you update the subscription for the RHACS Operator. This action configures which nodes can schedule the RHACS Operator pods. The `rhacs-operator` namespace is the designated location for the RHACS Operator.

</div>

<a id="install-central-operator_install-central-ocp"></a>

## Installing Central using the Operator method

The main component of Red Hat Advanced Cluster Security for Kubernetes is called Central. You can install Central on OpenShift Container Platform by using the `Central` custom resource. You deploy Central only once, and you can monitor multiple separate clusters by using the same Central installation.

<div class="important">

<div class="title">

</div>

- When you install Red Hat Advanced Cluster Security for Kubernetes for the first time, you must first install the `Central` custom resource because the `SecuredCluster` custom resource installation is dependent on certificates that Central generates.

- Red Hat recommends installing the Red Hat Advanced Cluster Security for Kubernetes `Central` custom resource in a dedicated project. Do not install it in the project where you have installed the Red Hat Advanced Cluster Security for Kubernetes Operator. Additionally, do not install it in any projects with names that begin with `kube`, `openshift`, or `redhat`, and in the `istio-system` project.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You must be using OpenShift Container Platform 4.12 or later. For information about supported platforms and architecture, see the "Red Hat Advanced Cluster Security for Kubernetes Support Matrix". For life cycle support information for RHACS, see the "Red Hat Advanced Cluster Security for Kubernetes Support Policy".

</div>

<div>

<div class="title">

Procedure

</div>

1.  On the OpenShift Container Platform web console, go to the **Ecosystem** → **Installed Operators** page.

2.  Select the Red Hat Advanced Cluster Security for Kubernetes Operator from the list of installed Operators.

3.  If you have installed the Operator in the recommended namespace, OpenShift Container Platform lists the project as `rhacs-operator`. Select **Project: rhacs-operator** → **Create project**.

4.  Enter the new project name (for example, `stackrox`), and click **Create**. Red Hat recommends that you use `stackrox` as the project name.

5.  Under the **Provided APIs** section, select **Central**. Click **Create Central**.

6.  Optional: If you are using declarative configuration, next to **Configure via:**, click **YAML view** and add the information for the declarative configuration, such as shown in the following example:

    ``` yaml
    ...
    spec:
      central:
        declarativeConfiguration:
          configMaps:
          - name: "<declarative_configs>"
          secrets:
          - name: "<sensitive_declarative_configs>"
    ...
    ```

    where:

    `<declarative_configs>`  
    Specifies the name of the config maps that you are using.

    `<sensitive_declarative_configs>`  
    Specifies the name of the secrets that you are using.

7.  Enter a name for your `Central` custom resource and add any labels you want to apply. Otherwise, accept the default values for the available options.

8.  You can configure available options for Central:

    - Central component settings:

      | Setting | Description |
      |----|----|
      | **Administrator password** | Secret that contains the administrator password. Use this field if you do not want RHACS to generate a password for you. |
      | **Exposure** | Settings for exposing Central by using a route, load balancer, or node port. See the `central.exposure.<parameter>` information in the "Public configuration file" section in "Installing Central services for RHACS on Red Hat OpenShift". |
      | **User-facing TLS certificate secret** | Use this field if you want to terminate TLS in Central and serve a custom server certificate. |
      | **Monitoring** | Configures the monitoring endpoint for Central. See the `central.exposeMonitoring` parameter in the "Public configuration file" section in "Installing Central services for RHACS on Red Hat OpenShift". |
      | **Central DB Settings** | Settings for Central DB, including data persistence. See the `central.db.<parameter>` information in the "Public configuration file" section in "Installing Central services for RHACS on Red Hat OpenShift". |
      | **Resources** | Use these fields after consulting the documentation if you need to override the default settings for memory and CPU resources. For more information, see the "Default resource requirements for RHACS" and "Recommended resource requirements for RHACS" sections in the "Installation" chapter. |
      | **Tolerations** | Use this parameter to configure Central to run only on specific nodes. See the `central.tolerations` parameter in the "Public configuration file" section in "Installing Central services for RHACS on Red Hat OpenShift". |
      | **Host Aliases** | Use this parameter to configure additional hostnames to resolve in the pod’s hosts file. |

    - **Scanner Component Settings**: Settings for the StackRox Scanner. See the "Scanner" table in the "Public configuration file" section in "Installing Central services for RHACS on Red Hat OpenShift". Although the StackRox Scanner is deprecated, it still must be enabled on the cluster where Central is installed due to software dependencies.

    - **Scanner V4 Component Settings**: Settings for Scanner V4 scanner, the default scanner. See the "Scanner V4" table in the "Public configuration file" section in "Installing Central services for RHACS on Red Hat OpenShift".

      You can configure the following options for Scanner V4:

      | Setting | Description |
      |----|----|
      | **Indexer** | The process that indexes images and creates a report of findings. You can configure replicas and autoscaling, resources, and tolerations. Before changing the default resource values, see the "Scanner V4" sections in the "Default resource requirements for RHACS" and "Recommended resource requirements for RHACS" sections in the "Installation" chapter. |
      | **Matcher** | The process that performs vulnerability matching of the report from the indexer against vulnerability data stored in Scanner V4 DB. You can configure replicas and autoscaling, resources, and tolerations. Before changing the default resource values, see the "Scanner V4" sections in the "Default resource requirements for RHACS" and "Recommended resource requirements for RHACS" sections in the "Installation" chapter. |
      | **DB** | The database that stores information for Scanner V4, including vulnerability data and index reports. You can configure persistence, resources, and tolerations. If you are using Scanner V4, a persistent volume claim (PVC) is required on Central clusters. A PVC is strongly recommended on secured clusters for best results. Before changing the default resource values, see the "Scanner V4" sections in the "Default resource requirements for RHACS" and "Recommended resource requirements for RHACS" sections in the "Installation" chapter. |

    - **Egress**: Settings for outgoing network traffic, including whether RHACS should run in online (connected) or offline (disconnected) mode.

    - **TLS**: Use this field to add additional trusted root certificate authorities (CAs).

    - **network**: To provide security at the network level, RHACS creates default `NetworkPolicy` resources in the namespace where Central is installed. To create and manage your own network policies, in the **policies** section, select **Disabled**. By default, this option is **Enabled**.

      > [!WARNING]
      > Disabling creation of default network policies can break communication between RHACS components. If you disable creation of default policies, you must create your own network policies to allow this communication.

    - **Advanced configuration**: You can use these fields to perform the following actions:

      - Specify additional image pull secrets

      - Add custom environment variables to set for managed pods' containers

      - Enable Red Hat OpenShift monitoring

9.  Click **Create**.

    > [!NOTE]
    > If you are using the cluster-wide proxy, Red Hat Advanced Cluster Security for Kubernetes uses that proxy configuration to connect to the external services.

</div>

<div>

<div class="title">

Next steps

</div>

1.  Verify Central installation.

2.  Optional: Configure Central options.

3.  Generate a CRS or an init bundle containing the cluster secrets that allows communication between the `Central` and `SecuredCluster` resources. You need to download this file, use it to generate resources on the clusters you want to secure, and securely store it.

4.  Install secured cluster services on each cluster you want to monitor.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

- [Red Hat Advanced Cluster Security for Kubernetes Support Policy](https://access.redhat.com/support/policy/updates/rhacs)

- [Default resource requirements for Red Hat Advanced Cluster Security for Kubernetes](../acs-default-requirements.md)

- [Recommended resource requirements for Red Hat Advanced Cluster Security for Kubernetes](../acs-recommended-requirements.md)

- [Public configuration file](install-central-ocp.md#central-services-public-configuration-file_install-central-ocp)

</div>

<a id="provision-postgresql-database_install-central-ocp"></a>

## Provisioning a database in your PostgreSQL instance

This step is optional. You can use your existing PostgreSQL infrastructure to provision a database for RHACS. Use the following instructions to configure a PostgreSQL database environment, create a user, database, schema, and role, and grant required permissions.

<div>

<div class="title">

Procedure

</div>

1.  Create a new user:

    ``` terminal
    CREATE USER stackrox WITH PASSWORD <password>;
    ```

2.  Create a database:

    ``` terminal
    CREATE DATABASE stackrox;
    ```

3.  Connect to the database:

    ``` terminal
    \connect stackrox
    ```

4.  Create user schema:

    ``` terminal
    CREATE SCHEMA stackrox;
    ```

5.  (Optional) Revoke rights on public:

    ``` terminal
    REVOKE CREATE ON SCHEMA public FROM PUBLIC;
    REVOKE USAGE ON SCHEMA public FROM PUBLIC;
    REVOKE ALL ON DATABASE stackrox FROM PUBLIC;
    ```

6.  Create a role:

    ``` terminal
    CREATE ROLE readwrite;
    ```

7.  Grant connection permission to the role:

    ``` terminal
    GRANT CONNECT ON DATABASE stackrox TO readwrite;
    ```

8.  Add required permissions to the `readwrite` role:

    ``` terminal
    GRANT USAGE ON SCHEMA stackrox TO readwrite;
    GRANT USAGE, CREATE ON SCHEMA stackrox TO readwrite;
    GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA stackrox TO readwrite;
    ALTER DEFAULT PRIVILEGES IN SCHEMA stackrox GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO readwrite;
    GRANT USAGE ON ALL SEQUENCES IN SCHEMA stackrox TO readwrite;
    ALTER DEFAULT PRIVILEGES IN SCHEMA stackrox GRANT USAGE ON SEQUENCES TO readwrite;
    ```

9.  Assign the `readwrite` role to the `stackrox` user:

    ``` terminal
    GRANT readwrite TO stackrox;
    ```

</div>

<a id="install-central-operator-external-db_install-central-ocp"></a>

## Installing Central with an external database using the Operator method

The main component of Red Hat Advanced Cluster Security for Kubernetes is called Central. You can install Central on OpenShift Container Platform by using the `Central` custom resource. You deploy Central only once, and you can monitor multiple separate clusters by using the same Central installation.

<div class="important">

<div class="title">

</div>

- When you install Red Hat Advanced Cluster Security for Kubernetes for the first time, you must first install the `Central` custom resource because the `SecuredCluster` custom resource installation is dependent on certificates that Central generates.

- If you use Kubernetes, enter `kubectl` instead of `oc`.

</div>

For more information about RHACS databases, see the "Database Scope of Coverage".

<div>

<div class="title">

Prerequisites

</div>

- You must be using OpenShift Container Platform 4.12 or later. For more information about supported OpenShift Container Platform versions, see the "Red Hat Advanced Cluster Security for Kubernetes Support Matrix". Postgres 15 is the recommended and supported version. Red Hat has deprecated the support for Postgres 13 and will remove it in the newer versions of RHACS.

- For detailed requirements, see "Requirements for using an external database".

</div>

<div>

<div class="title">

Procedure

</div>

1.  On the OpenShift Container Platform web console, go to the **Ecosystem** → **Installed Operators** page.

2.  Select the Red Hat Advanced Cluster Security for Kubernetes Operator from the list of installed Operators.

3.  If you have installed the Operator in the recommended namespace, OpenShift Container Platform lists the project as `rhacs-operator`. Select **Project: rhacs-operator** → **Create project**.

    <div class="warning">

    <div class="title">

    </div>

    - If you have installed the Operator in a different namespace, OpenShift Container Platform shows the name of that namespace rather than `rhacs-operator`.

    - Red Hat recommends installing the Red Hat Advanced Cluster Security for Kubernetes `Central` custom resource in a dedicated project. Do not install it in the project where you have installed the Red Hat Advanced Cluster Security for Kubernetes Operator. Additionally, do not install it in any projects with names that begin with `kube`, `openshift`, or `redhat`, and in the `istio-system` project.

    </div>

4.  Enter the new project name (for example, `stackrox`), and click **Create**. Red Hat recommends that you use `stackrox` as the project name.

5.  Create a password secret in the deployed namespace by using the OpenShift Container Platform web console or the terminal.

    - On the OpenShift Container Platform web console, go to the **Workloads** → **Secrets** page. Create a **Key/Value secret** with the key `password` and the value as the path of a plain text file containing the password for the superuser of the provisioned database.

    - Or, run the following command in your terminal:

      ``` terminal
      $ oc create secret generic external-db-password \
        --from-file=password=<password.txt>
      ```

      where:

      `<password.txt>`  
      Specifies the path of the file which has the plain text password.

6.  Return to the Red Hat Advanced Cluster Security for Kubernetes operator page in the OpenShift Container Platform web console. Under the **Provided APIs** section, select **Central**. Click **Create Central**.

7.  Optional: If you are using declarative configuration, next to **Configure via:**, click **YAML view**.

8.  Add the information for the declarative configuration, such as shown in the following example:

    ``` yaml
    ...
    spec:
      central:
        declarativeConfiguration:
          configMaps:
          - name: <declarative_configs>
          secrets:
          - name: <sensitive_declarative_configs>
    ...
    ```

    where:

    `<declarative_configs>`  
    Specifies the name of the config maps that you are using.

    `<sensitive_declarative_configs>`  
    Specifies the name of the secrets that you are using.

9.  Enter a name for your `Central` custom resource and add any labels you want to apply.

10. Go to **Central Component Settings** → **Central DB Settings**.

11. For **Administrator Password** specify the referenced secret as `external-db-password` (or the secret name of the password created previously).

12. For **Connection String** specify the connection string in `keyword=value` format, for example, `host=<host> port=5432 database=stackrox user=stackrox sslmode=verify-ca`

13. For **Persistence** → **PersistentVolumeClaim** → **Claim Name**, remove `central-db`.

14. If necessary, you can specify a Certificate Authority so that there is trust between the database certificate and Central. To add this, go to the YAML view and add a TLS block under the top-level spec, as shown in the following example:

    ``` yaml
    spec:
      tls:
        additionalCAs:
        - name: db-ca
          content: |
            <certificate>
    ```

15. Click **Create**.

    > [!NOTE]
    > If you are using the cluster-wide proxy, Red Hat Advanced Cluster Security for Kubernetes uses that proxy configuration to connect to the external services.

</div>

<div>

<div class="title">

Next steps

</div>

1.  Verify Central installation.

2.  Optional: Configure Central options.

3.  Generate a CRS or an init bundle containing the cluster secrets that allows communication between the `Central` and `SecuredCluster` resources. You need to download this file, use it to generate resources on the clusters you want to secure, and securely store it.

4.  Install secured cluster services on each cluster you want to monitor.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Database Scope of Coverage](https://access.redhat.com/articles/7045053#database-scope-of-coverage-7)

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

- [Requirements for using an external database](../acs-default-requirements.md#default-requirements-central-services_acs-default-requirements)

- [Central configuration options](install-central-config-options-ocp.md)

- [PostgreSQL Connection String Docs](https://www.postgresql.org/docs/15/libpq-connect.html#LIBPQ-CONNSTRING)

</div>

<a id="verify-central-install-operator_install-central-ocp"></a>

## Verifying Central installation using the Operator method

After Central finishes installing, log in to the RHACS portal to verify the successful installation of Central.

<div>

<div class="title">

Procedure

</div>

1.  On the OpenShift Container Platform web console, go to the **Ecosystem** → **Installed Operators** page.

2.  Select the Red Hat Advanced Cluster Security for Kubernetes Operator from the list of installed Operators.

3.  Select the **Central** tab.

4.  From the **Centrals** list, select `stackrox-central-services` to view its details.

5.  To get the password for the `admin` user, you can use one of these methods:

    - Click the link under **Admin Password Secret Reference**.

    - Use the Red Hat OpenShift CLI to enter the command listed under **Admin Credentials Info**:

      ``` terminal
      $ oc -n stackrox get secret central-htpasswd -o go-template='{{index .data "password" | base64decode}}'
      ```

6.  Find the link to the RHACS portal by completing one of these actions:

    - Use the Red Hat OpenShift CLI command:

      ``` terminal
      $ oc -n stackrox get route central -o jsonpath="{.status.ingress[0].host}"
      ```

    - Use the Red Hat Advanced Cluster Security for Kubernetes web console to find the link to the RHACS portal by performing the following commands:

      1.  Go to **Networking** → **Routes**.

      2.  Find the **central** Route and click the RHACS portal link under the **Location** column.

7.  Log in to the RHACS portal using the username **admin** and the password that you retrieved in a previous step. Until RHACS is completely configured (for example, you have the `Central` resource and at least one `SecuredCluster` resource installed and configured), no data is available in the dashboard. The `SecuredCluster` resource can be installed and configured on the same cluster as the `Central` resource. Clusters with the `SecuredCluster` resource are similar to managed clusters in Red Hat Advanced Cluster Management (RHACM).

</div>

<div>

<div class="title">

Next steps

</div>

1.  Optional: Configure central settings.

2.  Generate a CRS or an init bundle containing the cluster secrets that allows communication between the `Central` and `SecuredCluster` resources. You need to download this file, use it to generate resources on the clusters you want to secure, and securely store it.

3.  Install secured cluster services on each cluster you want to monitor.

</div>

<a id="install-using-helm-no-customizations-ocp_install-central-ocp"></a>

# Install Central by using Helm charts

You can install Central by using Helm charts without any customization, by using the default values, or by using Helm charts with additional customizations of configuration parameters.

<a id="install-central-using-helm-charts-without-customization_install-central-ocp"></a>

## Install Central by using Helm charts without customization

You can install RHACS on your cluster without any customizations. You must add the Helm chart repository and install the `central-services` Helm chart to install the centralized components of Central and Scanner.

<a id="adding-helm-repository_install-central-ocp"></a>

### Adding the Helm chart repository

Add the RHACS Helm chart repository to access installation charts for Central services and secured cluster components.

<div>

<div class="title">

Procedure

</div>

- Add the RHACS charts repository.

  ``` terminal
  $ helm repo add rhacs https://mirror.openshift.com/pub/rhacs/charts/
  ```

  The Helm repository for Red Hat Advanced Cluster Security for Kubernetes includes Helm charts for installing different components, including:

- Central services Helm chart (`central-services`) for installing the centralized components (Central and Scanner).

  > [!NOTE]
  > You deploy centralized components only once and you can monitor many separate clusters by using the same installation.

- Secured Cluster Services Helm chart (`secured-cluster-services`) for installing the per-cluster and per-node components (Sensor, Admission Controller, Collector, and Scanner-slim).

  > [!NOTE]
  > Deploy the per-cluster components into each cluster that you want to monitor and deploy the per-node components in all nodes that you want to monitor.

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

<a id="installing-quickly_install-central-ocp"></a>

### Installing the central-services Helm chart without customizations

You can install the `central-services` Helm chart to deploy the centralized components: Central and Scanner.

The output of the installation command includes:

- An automatically generated administrator password

- Instructions on storing all the configuration values

- Any warnings that Helm generates

<div>

<div class="title">

Prerequisites

</div>

- You must have access to the Red Hat Container Registry and a pull secret for authentication. For information about downloading images from `registry.redhat.io`, see "Red Hat Container Registry Authentication".

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command to install Central services and expose Central using a route:

  ``` terminal
  $ helm install -n stackrox \
    --create-namespace stackrox-central-services rhacs/central-services \
    --set imagePullSecrets.username=<username> \
    --set imagePullSecrets.password=<password> \
    --set central.exposure.route.enabled=true
  ```

  where:

  `<username>`  
  Specifies the user name for your pull secret for Red Hat Container Registry authentication.

  `<password>`  
  Specifies the password for your pull secret for Red Hat Container Registry authentication.

- Or, run the following command to install Central services and expose Central using a load balancer:

  ``` terminal
  $ helm install -n stackrox \
    --create-namespace stackrox-central-services rhacs/central-services \
    --set imagePullSecrets.username=<username> \
    --set imagePullSecrets.password=<password> \
    --set central.exposure.loadBalancer.enabled=true
  ```

  where:

  `<username>`  
  Specifies the user name for your pull secret for Red Hat Container Registry authentication.

  `<password>`  
  Specifies the password for your pull secret for Red Hat Container Registry authentication.

- Or, run the following command to install Central services and expose Central using port forward:

  ``` terminal
  $ helm install -n stackrox \
    --create-namespace stackrox-central-services rhacs/central-services \
    --set imagePullSecrets.username=<username> \
    --set imagePullSecrets.password=<password>
  ```

  where:

  `<username>`  
  Specifies the user name for your pull secret for Red Hat Container Registry authentication.

  `<password>`  
  Specifies the password for your pull secret for Red Hat Container Registry authentication.

  <div class="important">

  <div class="title">

  </div>

  - If you are installing Red Hat Advanced Cluster Security for Kubernetes in a cluster that requires a proxy to connect to external services, you must specify your proxy configuration by using the `proxyConfig` parameter. For example:

    ``` yaml
    env:
      proxyConfig: |
        url: http://proxy.name:port
        username: username
        password: password
        excludes:
        - some.domain
    ```

  - If you already created one or more image pull secrets in the namespace in which you are installing, instead of using a username and password, you can use `--set imagePullSecrets.useExisting="<pull-secret-1;pull-secret-2>"`.

  - Do not use image pull secrets if the following conditions apply:

    - If you are pulling your images from `quay.io/stackrox-io` or a registry in a private network that does not require authentication. Use use `--set imagePullSecrets.allowNone=true` instead of specifying a username and password.

    - If you already configured image pull secrets in the default service account in the namespace you are installing. Use `--set imagePullSecrets.useFromDefaultServiceAccount=true` instead of specifying a username and password.

  </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication)

</div>

<a id="automatically-generated-ca_install-central-ocp"></a>

### Retrieving the automatically generated certificate authority

When installing RHACS, a certificate authority (CA) is automatically generated and stored in a Kubernetes secret on the cluster. If you later change your installation by using Helm, you might need to supply this CA. For example, enabling an RHACS component that was initially disabled at installation time requires that you provide this CA.

The automatically generated CA is stored in a secret that is usually named similar to `stackrox-generated-suffix`, where *suffix* is a randomly generated string.

To retrieve the CA and export it to a `generated-values.yaml` file when needed for the `helm upgrade` command, for example, run the following command:

``` terminal
$ kubectl -n <namespace> get secret stackrox-generated-<suffix> \
  -o go-template='{{ index .data "generated-values.yaml" }}' | \
  base64 --decode >generated-values.yaml
```

> [!IMPORTANT]
> This file might contain sensitive data, so store it in a safe place.

If you are using the `helm upgrade` command after changing a configuration, you might need to supply this CA. For example, to update your system and enable Scanner V4, you run the following command:

``` terminal
$ helm upgrade -n stackrox stackrox-central-services rhacs/central-services --reuse-values \
  -f <path_to_generated-values.yaml> \
  --set scannerV4.disable=false
```

<a id="install-using-helm-customizations-ocp_install-central-ocp"></a>

## Install Central using Helm charts with customizations

You can install RHACS on your Red Hat OpenShift cluster with customizations by using Helm chart configuration parameters with the `helm install` and `helm upgrade` commands. You can specify these parameters by using the `--set` option or by creating YAML configuration files.

Create the following files for configuring the Helm chart for installing Red Hat Advanced Cluster Security for Kubernetes:

- Public configuration file `values-public.yaml`: Use this file to save all non-sensitive configuration options.

- Private configuration file `values-private.yaml`: Use this file to save all sensitive configuration options. Ensure that you store this file securely.

- Configuration file `declarative-config-values.yaml`: Create this file if you are using declarative configuration to add the declarative configuration mounts to Central.

<a id="central-services-private-configuration-file_install-central-ocp"></a>

### Private configuration file

The following are the configurable parameters of the `values-private.yaml` file. There are no default values for these parameters.

<a id="central-services-private-configuration-file-image-pull-secrets_install-central-ocp"></a>

#### Image pull secrets

The credentials that you need for pulling images from the registry depend on the following factors:

- If you are using a custom registry, you must specify these parameters:

  - `imagePullSecrets.username`

  - `imagePullSecrets.password`

  - `image.registry`

- If you do not use a username and password to log in to the custom registry, you must specify one of the following parameters:

  - `imagePullSecrets.allowNone`

  - `imagePullSecrets.useExisting`

  - `imagePullSecrets.useFromDefaultServiceAccount`

| Parameter | Description |
|----|----|
| `imagePullSecrets.username` | The username of the account to use to log in to the registry. |
| `imagePullSecrets.password` | The password of the account to use to log in to the registry. |
| `imagePullSecrets.allowNone` | Use `true` if you are using a custom registry and it allows pulling images without credentials. |
| `imagePullSecrets.useExisting` | A comma-separated list of secrets as values. For example, `secret1, secret2, secretN`. Use this option if you have already created pre-existing image pull secrets with the given name in the target namespace. |
| `imagePullSecrets.useFromDefaultServiceAccount` | Use `true` if you have already configured the default service account in the target namespace with sufficiently scoped image pull secrets. |

<a id="central-services-private-configuration-file-proxy-config_install-central-ocp"></a>

#### Proxy configuration

If you are installing Red Hat Advanced Cluster Security for Kubernetes in a cluster that requires a proxy to connect to external services, you must specify your proxy configuration by using the `proxyConfig` parameter. For example:

``` yaml
env:
  proxyConfig: |
    url: http://proxy.name:port
    username: username
    password: password
    excludes:
    - some.domain
```

| Parameter         | Description               |
|-------------------|---------------------------|
| `env.proxyConfig` | Your proxy configuration. |

<a id="central-services-private-configuration-file-central_install-central-ocp"></a>

#### Central

Configurable parameters for Central.

For a new installation, you can skip the following parameters:

- `central.jwtSigner.key`

- `central.serviceTLS.cert`

- `central.serviceTLS.key`

- `central.adminPassword.value`

- `central.adminPassword.htpasswd`

- `central.db.serviceTLS.cert`

- `central.db.serviceTLS.key`

- `central.db.password.value`

- When you do not specify values for these parameters the Helm chart autogenerates values for them.

- If you want to change these values you can use the `helm upgrade` command and specify the values using the `--set` option.

> [!IMPORTANT]
> For setting the administrator password, you can only use either `central.adminPassword.value` or `central.adminPassword.htpasswd`, but not both.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>central.jwtSigner.key</code></p></td>
<td style="text-align: left;"><p>A private key which RHACS should use for signing JSON web tokens (JWTs) for authentication.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.serviceTLS.cert</code></p></td>
<td style="text-align: left;"><p>An internal certificate that the Central service should use for deploying Central.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.serviceTLS.key</code></p></td>
<td style="text-align: left;"><p>The private key of the internal certificate that the Central service should use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.defaultTLS.cert</code></p></td>
<td style="text-align: left;"><p>The user-facing certificate that Central should use. RHACS uses this certificate for RHACS portal.</p>
<ul>
<li><p>For a new installation, you must give a certificate, otherwise, RHACS installs Central by using a self-signed certificate.</p></li>
<li><p>If you are upgrading, RHACS uses the existing certificate and its key.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.defaultTLS.key</code></p></td>
<td style="text-align: left;"><p>The private key of the user-facing certificate that Central should use.</p>
<ul>
<li><p>For a new installation, you must give the private key, otherwise, RHACS installs Central by using a self-signed certificate.</p></li>
<li><p>If you are upgrading, RHACS uses the existing certificate and its key.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.adminPassword.value</code></p></td>
<td style="text-align: left;"><p>Administrator password for logging into RHACS.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.adminPassword.htpasswd</code></p></td>
<td style="text-align: left;"><p>Administrator password for logging into RHACS. RHACS stores this password in hashed format by using bcrypt.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.serviceTLS.cert</code></p></td>
<td style="text-align: left;"><p>An internal certificate that the Central DB service should use for deploying Central DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.serviceTLS.key</code></p></td>
<td style="text-align: left;"><p>The private key of the internal certificate that the Central DB service should use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.password.value</code></p></td>
<td style="text-align: left;"><p>The password used to connect to the Central DB.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> If you are using `central.adminPassword.htpasswd` parameter, you must use a bcrypt encoded password hash. You can run the command `htpasswd -nB admin` to generate a password hash. For example,
>
> ``` yaml
> htpasswd: |
>   admin:<bcrypt_hash>
> ```

<a id="central-services-private-configuration-file-scanner_install-central-ocp"></a>

#### Scanner

Configurable parameters for the StackRox Scanner and Scanner V4.

For a new installation, you can skip the following parameters and the Helm chart autogenerates values for them. Otherwise, if you are upgrading to a new version, specify the values for the following parameters:

- `scanner.dbPassword.value`

- `scanner.serviceTLS.cert`

- `scanner.serviceTLS.key`

- `scanner.dbServiceTLS.cert`

- `scanner.dbServiceTLS.key`

- `scannerV4.db.password.value`

- `scannerV4.indexer.serviceTLS.cert`

- `scannerV4.indexer.serviceTLS.key`

- `scannerV4.matcher.serviceTLS.cert`

- `scannerV4.matcher.serviceTLS.key`

- `scannerV4.db.serviceTLS.cert`

- `scannerV4.db.serviceTLS.key`

| Parameter | Description |
|----|----|
| `scanner.dbPassword.value` | The password to use for authentication with Scanner database. Do not change this parameter because RHACS automatically creates and uses its value internally. |
| `scanner.serviceTLS.cert` | An internal certificate that the StackRox Scanner service should use for deploying the StackRox Scanner. |
| `scanner.serviceTLS.key` | The private key of the internal certificate that the Scanner service should use. |
| `scanner.dbServiceTLS.cert` | An internal certificate that the Scanner-db service should use for deploying Scanner database. |
| `scanner.dbServiceTLS.key` | The private key of the internal certificate that the Scanner-db service should use. |
| `scannerV4.db.password.value` | The password to use for authentication with the Scanner V4 database. Do not change this parameter because RHACS automatically creates and uses its value internally. |
| `scannerV4.db.serviceTLS.cert` | An internal certificate that the Scanner V4 DB service should use for deploying the Scanner V4 database. |
| `scannerV4.db.serviceTLS.key` | The private key of the internal certificate that the Scanner V4 DB service should use. |
| `scannerV4.indexer.serviceTLS.cert` | An internal certificate that the Scanner V4 service should use for deploying the Scanner V4 Indexer. |
| `scannerV4.indexer.serviceTLS.key` | The private key of the internal certificate that the Scanner V4 Indexer should use. |
| `scannerV4.matcher.serviceTLS.cert` | An internal certificate that the Scanner V4 service should use for deploying the Scanner V4 Matcher. |
| `scannerV4.matcher.serviceTLS.key` | The private key of the internal certificate that the Scanner V4 Matcher should use. |

<a id="central-services-public-configuration-file_install-central-ocp"></a>

### Public configuration file

The `values-public.yaml` file has configurable parameters for the installation.

<a id="central-services-public-configuration-file-image-pull-secrets_install-central-ocp"></a>

#### Image pull secrets

Image pull secrets are the credentials required for pulling images from your registry.

| Parameter | Description |
|----|----|
| `imagePullSecrets.allowNone` | Use `true` if you are using a custom registry and it allows pulling images without credentials. |
| `imagePullSecrets.useExisting` | A comma-separated list of secrets as values. For example, `secret1, secret2`. Use this option if you have already created pre-existing image pull secrets with the given name in the target namespace. |
| `imagePullSecrets.useFromDefaultServiceAccount` | Use `true` if you have already configured the default service account in the target namespace with sufficiently scoped image pull secrets. |

<a id="central-services-public-configuration-file-image_install-central-ocp"></a>

#### Image

Image declares the configuration to set up the main registry, which the Helm chart uses to resolve images for the `central.image`, `scanner.image`, `scanner.dbImage`, `scannerV4.image`, and `scannerV4.db.image` parameters.

| Parameter | Description |
|----|----|
| `image.registry` | Address of your image registry. Either use a hostname, such as `registry.redhat.io`, or a remote registry hostname, such as `us.gcr.io/stackrox-mirror`. |

<a id="central-services-public-configuration-file-config-as-code_install-central-ocp"></a>

#### Policy as code

Policy as code offers a way to configure RHACS to work with a continuous delivery tool such as Argo CD to track, manage, and apply policies that you have authored locally or exported from the RHACS portal and modified. You configure Argo CD or your other tool to apply policy as code resources to the same namespace in which you install RHACS.

| Parameter | Description |
|----|----|
| `configAsCode.enabled` | By default, the value is `true` so that RHACS enables policy as code. Set to `false` to disable the policy as code feature. |

<a id="central-services-public-configuration-file-environment-variables_install-central-ocp"></a>

#### Environment variables

Red Hat Advanced Cluster Security for Kubernetes automatically detects your cluster environment and sets values for `env.openshift` and `env.platform`. Only set these values to override the automatic cluster environment detection.

| Parameter | Description |
|----|----|
| `env.openshift` | Use `true` for installing on an OpenShift Container Platform cluster and overriding automatic cluster environment detection. |
| `env.platform` | The platform on which you are installing RHACS. Set its value to `default` or `gke` to specify cluster platform and override automatic cluster environment detection. |
| `env.offlineMode` | Use `true` to use RHACS in offline mode. |
| `env.grpcEnforceALPN` | Use `true` to force application-level protocol negotiation (ALPN) during the TLS handshake. |

<a id="additional-trusted-certificate-authorities_install-central-ocp"></a>

#### Additional trusted certificate authorities

The RHACS automatically references the system root certificates to trust. When Central, the StackRox Scanner, or Scanner V4 must reach out to services that use certificates issued by an authority in your organization or a globally trusted partner organization, you can add trust for these services by specifying the root certificate authority to trust by using the following parameter:

| Parameter | Description |
|----|----|
| `additionalCAs.<certificate_name>` | Specify the PEM encoded certificate of the root certificate authority to trust. |

<a id="default-network-policy-creation_install-central-ocp"></a>

#### Default network policies

To secure components at the network level, RHACS creates default `NetworkPolicy` resources in the namespace where you install Central. These network policies allow ingress to specific components on specific ports. If you do not want RHACS to create these policies, set this parameter to `Disabled`. The default value is `Enabled`.

> [!WARNING]
> Disabling creation of default network policies can break communication between RHACS components. If you disable creation of default policies, you must create your own network policies to allow this communication.

| Parameter | Description |
|----|----|
| `network.enableNetworkPolicies` | Specify if RHACS creates default network policies to allow communication between components. To create your own network policies, set this parameter to `False`. The default value is `True`. |

<a id="central-services-public-configuration-file-central_install-central-ocp"></a>

#### Central

Configurable parameters for Central.

- For exposing Central deployment for external access. You must specify one parameter, either `central.exposure.loadBalancer`, `central.exposure.nodePort`, or `central.exposure.route`. When you do not specify any value for these parameters, you must manually expose Central or access it by using port-forwarding.

The following table includes settings for an external PostgreSQL database.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>central.declarativeConfiguration.mounts.configMaps</code></p></td>
<td style="text-align: left;"><p>Mounts config maps used for declarative configurations.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.declarativeConfiguration.mounts.secrets</code></p></td>
<td style="text-align: left;"><p>Mounts secrets used for declarative configurations.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.endpointsConfig</code></p></td>
<td style="text-align: left;"><p>The endpoint configuration options for Central.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.nodeSelector</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Central. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Central. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposeMonitoring</code></p></td>
<td style="text-align: left;"><p>Specify <code>true</code> to expose Prometheus metrics endpoint for Central on port number <code>9090</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.image.registry</code></p></td>
<td style="text-align: left;"><p>A custom registry that overrides the global <code>image.registry</code> parameter for the Central image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.image.name</code></p></td>
<td style="text-align: left;"><p>The custom image name that overrides the default Central image name (<code>main</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.image.tag</code></p></td>
<td style="text-align: left;"><p>The custom image tag that overrides the default tag for Central image. If you specify your own image tag during a new installation, manually increment this tag when you upgrade to a new version by running the <code>helm upgrade</code> command. If you mirror Central images in your own registry, do not change the original image tags.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.image.fullRef</code></p></td>
<td style="text-align: left;"><p>Full reference including registry address, image name, and image tag for the Central image. Setting a value for this parameter overrides the <code>central.image.registry</code>, <code>central.image.name</code>, and <code>central.image.tag</code> parameters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.resources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for Central.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.resources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for Central.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.resources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for Central.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.resources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for Central.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.loadBalancer.enabled</code></p></td>
<td style="text-align: left;"><p>Use <code>true</code> to expose Central by using a load balancer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.loadBalancer.port</code></p></td>
<td style="text-align: left;"><p>The port number on which to expose Central. The default port number is 443.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.nodePort.enabled</code></p></td>
<td style="text-align: left;"><p>Use <code>true</code> to expose Central by using the node port service.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.nodePort.port</code></p></td>
<td style="text-align: left;"><p>The port number on which to expose Central. When you skip this parameter, OpenShift Container Platform automatically assigns a port number. Red Hat recommends that you do not specify a port number if you are exposing RHACS by using a node port.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.enabled</code></p></td>
<td style="text-align: left;"><p>Use <code>true</code> to expose Central by using a route. Disables all route settings if set to <code>false</code>. This parameter is only available for OpenShift Container Platform clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.host</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify a custom hostname to use for Central’s passthrough route. Leave this unset to accept the default value that OpenShift Container Platform provides. This parameter is only available for OpenShift Container Platform clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.enabled</code></p></td>
<td style="text-align: left;"><p>Set this to <code>true</code> to expose Central through a Red Hat OpenShift reencrypt route. The default value is <code>false</code>. This parameter is only available for OpenShift Container Platform clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.host</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify a custom hostname to use for Central’s reencrypt route. Leave this unset to accept the default value that OpenShift Container Platform provides. This parameter is only available for OpenShift Container Platform clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.tls.caCertificate</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify a PEM-encoded certificate chain that might establish a complete chain of trust. By default, OpenShift Container Platform provides the certificate authority. This parameter is only available for OpenShift Container Platform clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.tls.certificate</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify the PEM-encoded certificate that the route serves. The OpenShift Container Platform certificate authority signs the default certificate. This parameter is only available for OpenShift Container Platform clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.tls.destinationCACertificate</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify the CA certificate of the final destination, that is of Central. The OpenShift Container Platform router uses this certificate to perform health checks on the secure connection. By default, Central provides the certificate authority.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.exposure.route.reencrypt.tls.key</code></p></td>
<td style="text-align: left;"><p>Use this parameter to specify the PEM-encoded private key of the certificate for the route. The OpenShift Container Platform certificate authority signs the default certificate. This parameter is only available for OpenShift Container Platform clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.external</code></p></td>
<td style="text-align: left;"><p>Use <code>true</code> to specify that Central does not deploy Central DB and that you use an external database.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.source.connectionString</code></p></td>
<td style="text-align: left;"><p>The connection string for Central to use to connect to the database. Central uses this only when you set <code>central.db.external</code> to true. The connection string must be in keyword/value format as described in the PostgreSQL documentation in "Additional resources".</p>
<ul>
<li><p>Postgres 15 is the recommended and supported version. Red Hat has deprecated the support for Postgres 13 and will remove it in the newer versions of RHACS.</p></li>
<li><p>Connections through <code>PgBouncer</code> are not supported.</p></li>
<li><p>User must be superuser with ability to create and delete databases.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.source.minConns</code></p></td>
<td style="text-align: left;"><p>The minimum number of connections to the database to establish.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.source.maxConns</code></p></td>
<td style="text-align: left;"><p>The maximum number of connections to the database to establish.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.source.statementTimeoutMs</code></p></td>
<td style="text-align: left;"><p>The number of milliseconds a single query or transaction can be active against the database.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.postgresConfig</code></p></td>
<td style="text-align: left;"><p>The postgresql.conf to use for Central DB as described in the PostgreSQL documentation in "Additional resources".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.hbaConfig</code></p></td>
<td style="text-align: left;"><p>The pg_hba.conf to use for Central DB as described in the PostgreSQL documentation in "Additional resources".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.nodeSelector</code></p></td>
<td style="text-align: left;"><p>Specify a node selector label as <code>label-key: label-value</code> to force Central DB to only schedule on nodes with the specified label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.image.registry</code></p></td>
<td style="text-align: left;"><p>A custom registry that overrides the global <code>image.registry</code> parameter for the Central DB image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.image.name</code></p></td>
<td style="text-align: left;"><p>The custom image name that overrides the default Central DB image name (<code>central-db</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.image.tag</code></p></td>
<td style="text-align: left;"><p>The custom image tag that overrides the default tag for Central DB image. If you specify your own image tag during a new installation, manually increment this tag when you upgrade to a new version by running the <code>helm upgrade</code> command. If you mirror Central DB images in your own registry, do not change the original image tags.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.image.fullRef</code></p></td>
<td style="text-align: left;"><p>Full reference including registry address, image name, and image tag for the Central DB image. Setting a value for this parameter overrides the <code>central.db.image.registry</code>, <code>central.db.image.name</code>, and <code>central.db.image.tag</code> parameters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.resources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for Central DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.resources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for Central DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.resources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for Central DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.resources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for Central DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.persistence.hostPath</code></p></td>
<td style="text-align: left;"><p>The path on the node where RHACS should create a database volume. Red Hat does not recommend using this option.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.persistence.persistentVolumeClaim.claimName</code></p></td>
<td style="text-align: left;"><p>The name of the persistent volume claim (PVC) to use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.persistence.persistentVolumeClaim.createClaim</code></p></td>
<td style="text-align: left;"><p>Use <code>true</code> to create a new persistent volume claim, or <code>false</code> to use an existing claim.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>central.db.persistence.persistentVolumeClaim.size</code></p></td>
<td style="text-align: left;"><p>The size (in GiB) of the persistent volume managed by the specified claim.</p></td>
</tr>
</tbody>
</table>

<a id="central-services-public-configuration-file-scanner_install-central-ocp"></a>

#### StackRox Scanner

The following table lists the configurable parameters for the StackRox Scanner. Although the StackRox Scanner is deprecated, you must still enable it on the cluster where you install Central due to software dependencies.

| Parameter | Description |
|----|----|
| `scanner.disable` | Use `true` to install RHACS without the StackRox Scanner. When you use it with the `helm upgrade` command, Helm removes the existing StackRox Scanner deployment. |
| `scanner.exposeMonitoring` | Specify `true` to expose Prometheus metrics endpoint for the StackRox Scanner on port number `9090`. |
| `scanner.replicas` | The number of replicas to create for the StackRox Scanner deployment. When you use it with the `scanner.autoscaling` parameter, this value sets the initial number of replicas. |
| `scanner.logLevel` | Configure the log level for the StackRox Scanner. Red Hat recommends that you not change the default log level value (`INFO`). |
| `scanner.nodeSelector` | Specify a node selector label as `label-key: label-value` to force the StackRox Scanner to only schedule on nodes with the specified label. |
| `scanner.tolerations` | If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for the StackRox Scanner. This parameter is mainly used for infrastructure nodes. |
| `scanner.autoscaling.disable` | Use `true` to disable autoscaling for the StackRox Scanner deployment. When you disable autoscaling, the `minReplicas` and `maxReplicas` parameters do not have any effect. |
| `scanner.autoscaling.minReplicas` | The minimum number of replicas for autoscaling. |
| `scanner.autoscaling.maxReplicas` | The maximum number of replicas for autoscaling. |
| `scanner.resources.requests.memory` | The memory request for the StackRox Scanner. |
| `scanner.resources.requests.cpu` | The CPU request for the StackRox Scanner. |
| `scanner.resources.limits.memory` | The memory limit for the StackRox Scanner. |
| `scanner.resources.limits.cpu` | The CPU limit for the StackRox Scanner. |
| `scanner.dbResources.requests.memory` | The memory request for the StackRox Scanner database deployment. |
| `scanner.dbResources.requests.cpu` | The CPU request for the StackRox Scanner database deployment. |
| `scanner.dbResources.limits.memory` | The memory limit for the StackRox Scanner database deployment. |
| `scanner.dbResources.limits.cpu` | The CPU limit for the StackRox Scanner database deployment. |
| `scanner.image.registry` | A custom registry for the StackRox Scanner image. |
| `scanner.image.name` | The custom image name that overrides the default StackRox Scanner image name (`scanner`). |
| `scanner.dbImage.registry` | A custom registry for the StackRox Scanner DB image. |
| `scanner.dbImage.name` | The custom image name that overrides the default StackRox Scanner DB image name (`scanner-db`). |
| `scanner.dbNodeSelector` | Specify a node selector label as `label-key: label-value` to force the StackRox Scanner DB to only schedule on nodes with the specified label. |
| `scanner.dbTolerations` | If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for the StackRox Scanner DB. This parameter is mainly used for infrastructure nodes. |

<a id="central-services-public-configuration-file-scannerv4_install-central-ocp"></a>

#### Scanner V4

The following table lists the configurable parameters for Scanner V4.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.persistence.persistentVolumeClaim.claimName</code></p></td>
<td style="text-align: left;"><p>The name of the PVC to manage persistent data for Scanner V4. By default, for Central, RHACS creates a PVC and uses the default value of <code>scanner-v4-db</code> for the name.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.persistence.persistentVolumeClaim.size</code></p></td>
<td style="text-align: left;"><p>The size of the PVC to manage persistent data for Scanner V4.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.persistence.persistentVolumeClaim.storageClassName</code></p></td>
<td style="text-align: left;"><p>The name of the storage class to use for the PVC. If your cluster is not configured with a default storage class, you must give a value for this parameter.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.disable</code></p></td>
<td style="text-align: left;"><p>The following values are valid:</p>
<ul>
<li><p><code>true</code>: RHACS does not deploy Scanner V4.</p></li>
<li><p><code>false</code>: RHACS deploys Scanner V4.</p></li>
</ul>
<p>If you do not specify a value, the following behavior occurs by default:</p>
<ul>
<li><p>New installations: RHACS deploys Scanner V4.</p></li>
<li><p>Upgrades from a release earlier than 4.8: RHACS does not deploy Scanner V4.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.exposeMonitoring</code></p></td>
<td style="text-align: left;"><p>Specify <code>true</code> to expose Prometheus metrics endpoint for Scanner V4 on port number <code>9090</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.replicas</code></p></td>
<td style="text-align: left;"><p>The number of replicas to create for the Scanner V4 Indexer deployment. When you use it with the <code>scannerV4.indexer.autoscaling</code> parameter, this value sets the initial number of replicas.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.logLevel</code></p></td>
<td style="text-align: left;"><p>Configure the log level for the Scanner V4 Indexer. Red Hat recommends that you not change the default log level value (<code>INFO</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.nodeSelector</code></p></td>
<td style="text-align: left;"><p>Specify a node selector label as <code>label-key: label-value</code> to force the Scanner V4 Indexer to only schedule on nodes with the specified label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for the Scanner V4 Indexer. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.autoscaling.disable</code></p></td>
<td style="text-align: left;"><p>Use <code>true</code> to disable autoscaling for the Scanner V4 Indexer deployment. When you disable autoscaling, the <code>minReplicas</code> and <code>maxReplicas</code> parameters do not have any effect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.autoscaling.minReplicas</code></p></td>
<td style="text-align: left;"><p>The minimum number of replicas for autoscaling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.autoscaling.maxReplicas</code></p></td>
<td style="text-align: left;"><p>The maximum number of replicas for autoscaling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.resources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for the Scanner V4 Indexer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.resources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for the Scanner V4 Indexer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.resources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for the Scanner V4 Indexer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.indexer.resources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for the Scanner V4 Indexer.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.matcher.replicas</code></p></td>
<td style="text-align: left;"><p>The number of replicas to create for the Scanner V4 Matcher deployment. When you use it with the <code>scannerV4.matcher.autoscaling</code> parameter, this value sets the initial number of replicas.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.matcher.logLevel</code></p></td>
<td style="text-align: left;"><p>Red Hat recommends that you not change the default log level value (<code>INFO</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.matcher.nodeSelector</code></p></td>
<td style="text-align: left;"><p>Specify a node selector label as <code>label-key: label-value</code> to force the Scanner V4 Matcher to only schedule on nodes with the specified label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.matcher.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for the Scanner V4 Matcher. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.matcher.autoscaling.disable</code></p></td>
<td style="text-align: left;"><p>Use <code>true</code> to disable autoscaling for the Scanner V4 Matcher deployment. When you disable autoscaling, the <code>minReplicas</code> and <code>maxReplicas</code> parameters do not have any effect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.matcher.autoscaling.minReplicas</code></p></td>
<td style="text-align: left;"><p>The minimum number of replicas for autoscaling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.matcher.autoscaling.maxReplicas</code></p></td>
<td style="text-align: left;"><p>The maximum number of replicas for autoscaling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.matcher.resources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for the Scanner V4 Matcher.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.matcher.resources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for the Scanner V4 Matcher.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.resources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for the Scanner V4 database deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.resources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for the Scanner V4 database deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.resources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for the Scanner V4 database deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.resources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for the Scanner V4 database deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.nodeSelector</code></p></td>
<td style="text-align: left;"><p>Specify a node selector label as <code>label-key: label-value</code> to force the Scanner V4 DB to only schedule on nodes with the specified label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for the Scanner V4 DB. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.image.registry</code></p></td>
<td style="text-align: left;"><p>A custom registry for the Scanner V4 DB image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.db.image.name</code></p></td>
<td style="text-align: left;"><p>The custom image name that overrides the default Scanner V4 DB image name (<code>scanner-v4-db</code>).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.image.registry</code></p></td>
<td style="text-align: left;"><p>A custom registry for the Scanner V4 image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scannerV4.image.name</code></p></td>
<td style="text-align: left;"><p>The custom image name that overrides the default Scanner V4 image name (<code>scanner-v4</code>).</p></td>
</tr>
</tbody>
</table>

<a id="central-services-public-configuration-file-customizations_install-central-ocp"></a>

#### Customization

Use these parameters to specify additional attributes for all objects that RHACS creates.

| Parameter | Description |
|----|----|
| `customize.labels` | A custom label to attach to all objects. |
| `customize.annotations` | A custom annotation to attach to all objects. |
| `customize.podLabels` | A custom label to attach to all deployments. |
| `customize.podAnnotations` | A custom annotation to attach to all deployments. |
| `customize.envVars` | A custom environment variable for all containers in all objects. |
| `customize.central.labels` | A custom label to attach to all objects that Central creates. |
| `customize.central.annotations` | A custom annotation to attach to all objects that Central creates. |
| `customize.central.podLabels` | A custom label to attach to all Central deployments. |
| `customize.central.podAnnotations` | A custom annotation to attach to all Central deployments. |
| `customize.central.envVars` | A custom environment variable for all Central containers. |
| `customize.scanner.labels` | A custom label to attach to all objects that Scanner creates. |
| `customize.scanner.annotations` | A custom annotation to attach to all objects that Scanner creates. |
| `customize.scanner.podLabels` | A custom label to attach to all Scanner deployments. |
| `customize.scanner.podAnnotations` | A custom annotation to attach to all Scanner deployments. |
| `customize.scanner.envVars` | A custom environment variable for all Scanner containers. |
| `customize.scanner-db.labels` | A custom label to attach to all objects that Scanner DB creates. |
| `customize.scanner-db.annotations` | A custom annotation to attach to all objects that Scanner DB creates. |
| `customize.scanner-db.podLabels` | A custom label to attach to all Scanner DB deployments. |
| `customize.scanner-db.podAnnotations` | A custom annotation to attach to all Scanner DB deployments. |
| `customize.scanner-db.envVars` | A custom environment variable for all Scanner DB containers. |
| `customize.scanner-v4-indexer.labels` | A custom label to attach to all objects that Scanner V4 Indexer creates and into the pods belonging to them. |
| `customize.scanner-v4-indexer.annotations` | A custom annotation to attach to all objects that Scanner V4 Indexer creates and into the pods belonging to them. |
| `customize.scanner-v4-indexer.podLabels` | A custom label to attach to all objects that Scanner V4 Indexer creates and into the pods belonging to them. |
| `customize.scanner-v4-indexer.podAnnotations` | A custom annotation to attach to all objects that Scanner V4 Indexer creates and into the pods belonging to them. |
| `customize.scanner-v4-indexer.envVars` | A custom environment variable for all Scanner V4 Indexer containers and the pods belonging to them. |
| `customize.scanner-v4-matcher.labels` | A custom label to attach to all objects that Scanner V4 Matcher creates and into the pods belonging to them. |
| `customize.scanner-v4-matcher.annotations` | A custom annotation to attach to all objects that Scanner V4 Matcher creates and into the pods belonging to them. |
| `customize.scanner-v4-matcher.podLabels` | A custom label to attach to all objects that Scanner V4 Matcher creates and into the pods belonging to them. |
| `customize.scanner-v4-matcher.podAnnotations` | A custom annotation to attach to all objects that Scanner V4 Matcher creates and into the pods belonging to them. |
| `customize.scanner-v4-matcher.envVars` | A custom environment variable for all Scanner V4 Matcher containers and the pods belonging to them. |
| `customize.scanner-v4-db.labels` | A custom label to attach to all objects that Scanner V4 DB creates and into the pods belonging to them. |
| `customize.scanner-v4-db.annotations` | A custom annotation to attach to all objects that Scanner V4 DB creates and into the pods belonging to them. |
| `customize.scanner-v4-db.podLabels` | A custom label to attach to all objects that Scanner V4 DB creates and into the pods belonging to them. |
| `customize.scanner-v4-db.podAnnotations` | A custom annotation to attach to all objects that Scanner V4 DB creates and into the pods belonging to them. |
| `customize.scanner-v4-db.envVars` | A custom environment variable for all Scanner V4 DB containers and the pods belonging to them. |

You can also use:

- the `customize.other.service/*.labels` and the `customize.other.service/*.annotations` parameters, to specify labels and annotations for all objects.

- or, give a specific service name, for example, `customize.other.service/central-loadbalancer.labels` and `customize.other.service/central-loadbalancer.annotations` as parameters and set their value.

<a id="central-services-public-configuration-file-advance-customization_install-central-ocp"></a>

#### Advanced customization

Advanced configuration parameters for non-standard namespace and release names.

> [!IMPORTANT]
> The following parameters are for information only. Red Hat supports RHACS instances only when using the default namespace and release names.

| Parameter | Description |
|----|----|
| `allowNonstandardNamespace` | Use `true` to deploy RHACS into a namespace other than the default namespace `stackrox`. |
| `allowNonstandardReleaseName` | Use `true` to deploy RHACS with a release name other than the default `stackrox-central-services`. |

<a id="declarative-configuration-values_install-central-ocp"></a>

### Declarative configuration values

To use declarative configuration, you must create a YAML file (in this example, named "declarative-config-values.yaml") that adds the declarative configuration mounts to Central. This file is used in a Helm installation.

<div>

<div class="title">

Procedure

</div>

1.  Create the YAML file (in this example, named `declarative-config-values.yaml`) using the following example as a guideline:

    ``` yaml
    central:
      declarativeConfiguration:
        mounts:
          configMaps:
            - declarative-configs
          secrets:
            - sensitive-declarative-configs
    ```

2.  Install the Central services Helm chart as documented in the "Installing the central-services Helm chart", referencing the `declarative-config-values.yaml` file.

</div>

<a id="install-central-services-helm-chart_install-central-ocp"></a>

### Installing the central-services Helm chart

After you configure the `values-public.yaml` and `values-private.yaml` files, install the `central-services` Helm chart to deploy the centralized components (Central and Scanner).

<div>

<div class="title">

Procedure

</div>

- Run the following command:

  ``` terminal
  $ helm install -n stackrox --create-namespace \
    stackrox-central-services rhacs/central-services \
    -f <path_to_values_public.yaml> -f <path_to_values_private.yaml>
  ```

  where:

  `<path_to_values_public.yaml>`  
  Specifies the paths for your YAML configuration files.

  > [!NOTE]
  > Optional: If using declarative configuration, add `-f <path_to_declarative-config-values.yaml` to this command to mount the declarative configurations file in Central.

</div>

<a id="change-config-options-after-deployment-central-services_install-central-ocp"></a>

## Changing configuration options after deploying the central-services Helm chart

You can make changes to any configuration options after you have deployed the `central-services` Helm chart.

When using the `helm upgrade` command to make changes, the following guidelines and requirements apply:

- You can also specify configuration values using the `--set` or `--set-file` parameters. However, these options are not saved, and you must manually specify all the options again whenever you make changes.

- Some changes, such as enabling a new component, require new certificates to be issued for the component. Therefore, you must provide a CA when making these changes.

  - If the CA was generated by the Helm chart during the initial installation, you must retrieve these automatically generated values from the cluster and provide them to the `helm upgrade` command. The postinstallation notes of the `central-services` Helm chart include a command for retrieving the automatically generated values.

  - If the CA was generated outside of the Helm chart and provided during the installation of the `central-services` chart, then you must perform that action again when using the `helm upgrade` command, for example, by using the `--reuse-values` flag with the `helm upgrade` command.

<div>

<div class="title">

Procedure

</div>

1.  Update the `values-public.yaml` and `values-private.yaml` configuration files with new values.

2.  Run the `helm upgrade` command and specify the configuration files using the `-f` option:

    ``` terminal
    $ helm upgrade -n stackrox \
      stackrox-central-services rhacs/central-services \
      --reuse-values \
      -f <path_to_init_bundle_file \
      -f <path_to_values_public.yaml> \
      -f <path_to_values_private.yaml>
    ```

    where:

    `--reuse-values`  
    Specifies that the modified values that are not included in the `values_public.yaml` and `values_private.yaml` files.

</div>

<a id="install-using-roxctl-ocp_install-central-ocp"></a>

# Install Central by using the roxctl CLI

For production environments, Red Hat recommends using the Operator or Helm charts to install RHACS.

> [!WARNING]
> Do not use the `roxctl` install method unless you have a specific installation need that requires using this method.

<a id="installing-roxctl-cli-ocp_install-central-ocp"></a>

## Install the roxctl CLI

To install Red Hat Advanced Cluster Security for Kubernetes you must install the `roxctl` CLI by downloading the binary. You can install `roxctl` on Linux, Windows, or macOS.

<a id="installing-cli-on-linux_install-central-ocp"></a>

### Installing the roxctl CLI on Linux

You can install the `roxctl` CLI binary on Linux by using the following procedure.

> [!NOTE]
> `roxctl` CLI for Linux is available for `amd64`, `arm64`, `ppc64le`, and `s390x` architectures.

<div>

<div class="title">

Procedure

</div>

1.  Find the `roxctl` architecture for the target operating system:

    ``` terminal
    $ arch="$(uname -m | sed "s/x86_64//")"; arch="${arch:+-$arch}"
    ```

2.  Download the `roxctl` CLI:

    ``` terminal
    $ curl -L -f -o roxctl "https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Linux/roxctl${arch}"
    ```

3.  Make the `roxctl` binary executable:

    ``` terminal
    $ chmod +x roxctl
    ```

4.  Place the `roxctl` binary in a directory that is on your `PATH`:

    To check your `PATH`, run the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="installing-cli-on-macos_install-central-ocp"></a>

### Installing the roxctl CLI on macOS

You can install the `roxctl` CLI binary on macOS by using the following procedure.

> [!NOTE]
> `roxctl` CLI for macOS is available for `amd64` and `arm64` architectures.

<div>

<div class="title">

Procedure

</div>

1.  Find the `roxctl` architecture for the target operating system:

    ``` terminal
    $ arch="$(uname -m | sed "s/x86_64//")"; arch="${arch:+-$arch}"
    ```

2.  Download the `roxctl` CLI:

    ``` terminal
    $ curl -L -f -o roxctl "https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Darwin/roxctl${arch}"
    ```

3.  Remove all extended attributes from the binary:

    ``` terminal
    $ xattr -c roxctl
    ```

4.  Make the `roxctl` binary executable:

    ``` terminal
    $ chmod +x roxctl
    ```

5.  Place the `roxctl` binary in a directory that is on your `PATH`:

    To check your `PATH`, run the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="installing-cli-on-windows_install-central-ocp"></a>

### Installing the roxctl CLI on Windows

You can install the `roxctl` CLI binary on Windows by using the following procedure.

> [!NOTE]
> `roxctl` CLI for Windows is available for the `amd64` architecture.

<div>

<div class="title">

Procedure

</div>

- Download the `roxctl` CLI:

  ``` terminal
  $ curl -f -O https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Windows/roxctl.exe
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="using-the-interactive-installer_install-central-ocp"></a>

## Using the interactive installer

Use the interactive installer to generate the required secrets, deployment configurations, and deployment scripts for your environment.

<div>

<div class="title">

Procedure

</div>

1.  Run the interactive install command:

    ``` terminal
    $ roxctl central generate interactive
    ```

    > [!IMPORTANT]
    > Installing RHACS using the `roxctl` CLI creates PodSecurityPolicy (PSP) objects by default for backward compatibility. If you install RHACS on Kubernetes versions 1.25 and newer or OpenShift Container Platform version 4.12 and newer, you must disable the PSP object creation. To do this, specify `--enable-pod-security-policies` option as `false` for the `roxctl central generate` and `roxctl sensor generate` commands.

2.  Press **Enter** to accept the default value for a prompt or enter custom values as required. The following example shows the interactive installer prompts:

    ``` terminal
    Path to the backup bundle from which to restore keys and certificates (optional):
    PEM cert bundle file (optional):
    Disable the administrator password (only use this if you have already configured an IdP for your instance) (default: "false"):
    Create PodSecurityPolicy resources (for pre-v1.25 Kubernetes) (default: "false"):
    Administrator password (default: autogenerated):
    Orchestrator (k8s, openshift):
    Default container images settings (rhacs, opensource); it controls repositories from where to download the images, image names and tags format (default: "rhacs"):
    The directory to output the deployment bundle to (default: "central-bundle"):
    Whether to enable telemetry (default: "true"):
    The central-db image to use (if unset, a default will be used according to --image-defaults) (default: "registry.redhat.io/advanced-cluster-security/rhacs-central-db-rhel9:4.11.0"):
    List of secrets to add as declarative configuration mounts in central (default: "[]"):
    The method of exposing Central (lb, np, none) (default: "none"):
    The main image to use (if unset, a default will be used according to --image-defaults) (default: "registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:4.11.0"):
    Whether to run StackRox in offline mode, which avoids reaching out to the Internet (default: "false"):
    List of config maps to add as declarative configuration mounts in central (default: "[]"):
    The deployment tool to use (kubectl, helm, helm-values) (default: "kubectl"):
    Istio version when deploying into an Istio-enabled cluster (leave empty when not running Istio) (optional):
    The scanner-db image to use (if unset, a default will be used according to --image-defaults) (default: "registry.redhat.io/advanced-cluster-security/rhacs-scanner-db-rhel9:4.11.0"):
    The scanner image to use (if unset, a default will be used according to --image-defaults) (default: "registry.redhat.io/advanced-cluster-security/rhacs-scanner-rhel9:4.11.0"):
    The scanner-v4-db image to use (if unset, a default will be used according to --image-defaults) (default: "registry.redhat.io/advanced-cluster-security/rhacs-scanner-v4-db-rhel9:4.11.0"):
    The scanner-v4 image to use (if unset, a default will be used according to --image-defaults) (default: "registry.redhat.io/advanced-cluster-security/rhacs-scanner-v4-rhel9:4.11.0"):
    External volume type (hostpath, pvc): hostpath
    Path on the host (default: "/var/lib/stackrox-central"):
    Node selector key (e.g. kubernetes.io/hostname):
    Node selector value:
    ```

    where:

    `PEM cert bundle file`  
    Specifies whether to add a custom TLS certificate, provide the file path for the PEM-encoded certificate. When you specify a custom certificate the interactive installer also prompts you to provide a PEM private key for the custom certificate you are using.

    `Create PodSecurityPolicy resources`  
    Specifies whether to create `PodSecurityPolicy` resources. If you are running Kubernetes version 1.25 or later, set this value to `false`.

    `List of secrets to add as declarative configuration mounts in central`  
    Specifies the list of secrets to add as declarative configuration mounts in Central. For more information about using declarative configurations for authentication and authorization, see "Declarative configuration for authentication and authorization resources" in "Managing RBAC in Red Hat Advanced Cluster Security for Kubernetes".

    `The method of exposing Central`  
    Specifies the method of exposing Central. You must expose Central by using a route, a load balancer or a node port.

    `List of config maps to add as declarative configuration mounts in central`  
    Specifies the list of config maps to add as declarative configuration mounts in Central. For more information about using declarative configurations for authentication and authorization, see "Declarative configuration for authentication and authorization resources" in "Managing RBAC in Red Hat Advanced Cluster Security for Kubernetes".

    > [!WARNING]
    > On OpenShift Container Platform, for using a hostPath volume, you must modify the SELinux policy to allow access to the directory, which the host and the container share. It is because SELinux blocks directory sharing by default. To modify the SELinux policy, run the following command:
    >
    > ``` terminal
    > $ sudo chcon -Rt svirt_sandbox_file_t <full_volume_path>
    > ```
    >
    > However, you must not modify the SELinux policy, instead use PVC when installing on OpenShift Container Platform.

    On completion, the installer creates a folder named central-bundle, which contains the necessary YAML manifests and scripts to deploy Central. In addition, it shows on-screen instructions for the scripts you need to run to deploy additional trusted certificate authorities, Central and Scanner, and the authentication instructions for logging into the RHACS portal along with the autogenerated password if you did not provide one when answering the prompts.

</div>

<a id="install-central-roxctl_install-central-ocp"></a>

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
