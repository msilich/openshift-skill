<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can generate a diagnostic bundle and send that data to enable the support team to give insights into the status and health of Red Hat Advanced Cluster Security for Kubernetes components.

<a id="generate-diagnostic-bundle-overview_generate-diagnostic-bundle"></a>

# Diagnostic bundle overview

Red Hat might request that you send the diagnostic bundle during investigation of your issues with Red Hat Advanced Cluster Security for Kubernetes.

You can generate a diagnostic bundle and inspect its data before sending.

> [!NOTE]
> The diagnostic bundle does not use encryption, and depending upon the number of clusters in your environment, the bundle size is between 100 KB and 1 MB. Always use an encrypted channel to transfer this data back to Red Hat.

<a id="diagnostic-bundle-data_generate-diagnostic-bundle"></a>

# Diagnostic bundle data

When you generate a diagnostic bundle, it includes the following data:

- Central heap profile.

- System logs: Logs of all Red Hat Advanced Cluster Security for Kubernetes components (for the last 20 minutes) and logs of recently crashed components (from up to 20 minutes before the crash). System logs depend on the size of your environment. For large deployments, data includes log files for components with critical errors only, such as a high restart count.

- YAML definitions for Red Hat Advanced Cluster Security for Kubernetes components: This data does not include Kubernetes secrets.

- OpenShift Container Platform or Kubernetes events: Details about the events that relate to the objects in the `stackrox` namespace.

- Online Telemetry data, which includes:

  - Storage information: Details about the database size and the amount of free space available in attached volumes.

  - Red Hat Advanced Cluster Security for Kubernetes components health information: Details about Red Hat Advanced Cluster Security for Kubernetes components versions, their memory usage, and any reported errors.

  - Coarse-grained usage statistics: Details about API endpoint invocation counts and reported error statuses. It does not include the actual data sent in API requests.

  - Nodes information: Details about the nodes in each secured cluster. It includes kernel and operating system versions, resource pressure, and taints.

  - Environment information: Details about each secured cluster, including Kubernetes or OpenShift Container Platform version, Istio version (if applicable), cloud provider type and other similar information.

<a id="generate-diagnostic-bundle-using-acs-portal_generate-diagnostic-bundle"></a>

# Generating a diagnostic bundle by using the RHACS portal

You can generate a diagnostic bundle by using the system health dashboard in the RHACS portal.

<div>

<div class="title">

Prerequisites

</div>

- To generate a diagnostic bundle, you need `read` permission for the `Administration` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, select **Platform Configuration** → **System Health**.

2.  On the **System Health** view header, click **Generate Diagnostic Bundle**.

3.  For the **Filter by clusters** drop-down menu, select the clusters for which you want to generate the diagnostic data.

4.  For **Filter by starting time**, specify the date and time (in UTC format) from which you want to include the diagnostic data.

5.  Click **Download Diagnostic Bundle**.

</div>

<a id="generate-diagnostic-bundle-using-roxctl-cli_generate-diagnostic-bundle"></a>

# Generating a diagnostic bundle by using the roxctl CLI

You can use the `roxctl` CLI to generate a diagnostic bundle. You need the Red Hat Advanced Cluster Security for Kubernetes (RHACS) administrator password or API token and central address.

<div>

<div class="title">

Prerequisites

</div>

- To generate a diagnostic bundle, you need `read` permission for the `Administration` resource.

- You must have configured the RHACS administrator password or API token and central address.

</div>

<div>

<div class="title">

Procedure

</div>

- To generate a diagnostic bundle by using the RHACS administrator password, perform the following steps:

  1.  Run the following command to configure the `ROX_PASSWORD` and `ROX_CENTRAL_ADDRESS` environment variables:

      ``` terminal
      $ export ROX_PASSWORD=<rox_password> && export ROX_CENTRAL_ADDRESS=<address>:<port_number>
      ```

      where:

      \<rox_password\>  
      Specifies the RHACS administrator password.

  2.  Run the following command to generate a diagnostic bundle by using the RHACS administrator password:

      ``` terminal
      $ roxctl -e "$ROX_CENTRAL_ADDRESS" -p "$ROX_PASSWORD" central debug download-diagnostics
      ```

- To generate a diagnostic bundle by using the API token, perform the following steps:

  1.  Run the following command to configure the `ROX_API_TOKEN` environment variable:

      ``` terminal
      $ export ROX_API_TOKEN=<api_token>
      ```

  2.  Run the following command to generate a diagnostic bundle by using the API token:

      ``` terminal
      $ roxctl -e "$ROX_CENTRAL_ADDRESS" central debug download-diagnostics
      ```

</div>

<a id="generate-diagnostic-bundle-roxctl-admin-password_generate-diagnostic-bundle"></a>

## Generating a diagnostic bundle by using the administrator password

You can generate a diagnostic bundle by using the RHACS administrator password with the `roxctl` CLI.

<div>

<div class="title">

Prerequisites

</div>

- To generate a diagnostic bundle, you need `read` permission for the `Administration` resource.

- You must have configured the RHACS administrator password and central address.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to configure the `ROX_PASSWORD` and `ROX_CENTRAL_ADDRESS` environment variables:

    ``` terminal
    $ export ROX_PASSWORD=<rox_password> && export ROX_CENTRAL_ADDRESS=<address>:<port_number>
    ```

    where:

    \<rox_password\>  
    Specifies the RHACS administrator password.

2.  Run the following command to generate a diagnostic bundle by using the RHACS administrator password:

    ``` terminal
    $ roxctl -e "$ROX_CENTRAL_ADDRESS" -p "$ROX_PASSWORD" central debug download-diagnostics
    ```

</div>

<a id="generate-diagnostic-bundle-roxctl-api-token_generate-diagnostic-bundle"></a>

## Generating a diagnostic bundle by using an API token

You can generate a diagnostic bundle by using an API token with the `roxctl` CLI.

<div>

<div class="title">

Prerequisites

</div>

- To generate a diagnostic bundle, you need `read` permission for the `Administration` resource.

- You must have configured the RHACS API token and central address.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to configure the `ROX_API_TOKEN` environment variable:

    ``` terminal
    $ export ROX_API_TOKEN=<api_token>
    ```

2.  Run the following command to generate a diagnostic bundle by using the API token:

    ``` terminal
    $ roxctl -e "$ROX_CENTRAL_ADDRESS" central debug download-diagnostics
    ```

</div>
