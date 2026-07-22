<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Insights Operator periodically gathers configuration and component failure status and, by default, reports that data every two hours to Red Hat. This information enables Red Hat to assess configuration and deeper failure data than is reported through Telemetry. Users of OpenShift Container Platform can display the report in the [Advisor](https://console.redhat.com/openshift/insights/advisor/) service on Red Hat Hybrid Cloud Console.

<div>

<div class="title">

Additional resources

</div>

- The Insights Operator is installed and enabled by default. If you need to opt out of remote health reporting, see [Remote health reporting](remote-health-reporting.md#remote-health-reporting).

- For more information on using the Red Hat Lightspeed advisor service to identify issues with your cluster, see [Using Red Hat Lightspeed to identify issues with your cluster](using-insights-to-identify-issues-with-your-cluster.md#using-insights-to-identify-issues-with-your-cluster).

</div>

# The Insights Operator configuration

The Insights Operator configuration combines default settings with configurations stored in either the `insights-config` `ConfigMap` in the `openshift-insights` namespace or the support secret in the `openshift-config` namespace.

When a `ConfigMap` object or support secret exists, the contained attribute values override the default Operator configuration values. If both a `ConfigMap` object *and* a support secret exist, the Operator reads the `ConfigMap` object.

The `ConfigMap` object does not exist by default, so an OpenShift Container Platform cluster administrator must create it.

## ConfigMap object configuration structure

View the example of an `insights-config` `ConfigMap` object (`config.yaml` configuration) to better understand the configuration options for the `ConfigMap` object.

<div class="formalpara">

<div class="title">

Example insights-config ConfigMap object

</div>

``` yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: insights-config
  namespace: openshift-insights
data:
  config.yaml: |
    dataReporting:
      uploadEndpoint: https://console.redhat.com/api/ingress/v1/upload
      storagePath: /var/lib/insights-operator
      downloadEndpoint: https://console.redhat.com/api/insights-results-aggregator/v2/cluster/%s/reports
      conditionalGathererEndpoint: https://console.redhat.com/api/gathering/gathering_rules
      disableRuntimeExtractor: true
    sca:
        disabled: false
        endpoint: https://api.openshift.com/api/accounts_mgmt/v1/entitlement_certificates
        interval: 8h0m0s
    alerting:
        disabled: false
    proxy:
        httpProxy: http://example.com
        httpsProxy: https://example.com
        noProxy: test.org
```

</div>

The following table describes the available configuration attributes:

> [!NOTE]
> The `insights-config` `ConfigMap` object follows standard YAML formatting, wherein child values are below the parent attribute and indented two spaces. For the `Obfuscation` attribute, enter values as bulleted children of the parent attribute.

<table>
<caption>Insights Operator configurable attributes</caption>
<colgroup>
<col style="width: 28%" />
<col style="width: 42%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Attribute name</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Value type</th>
<th style="text-align: left;">Default value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>alerting:
    disabled: false</code></pre></td>
<td style="text-align: left;"><p>Disables Insights Operator alerts to the cluster Prometheus instance.</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>clusterTransfer:
    endpoint: &lt;url&gt;</code></pre></td>
<td style="text-align: left;"><p>The endpoint for checking and downloading cluster transfer data.</p></td>
<td style="text-align: left;"><p>URL</p></td>
<td style="text-align: left;"><p><a href="https://api.openshift.com/api/accounts_mgmt/v1/cluster_transfers/">https://api.openshift.com/api/accounts_mgmt/v1/cluster_transfers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>clusterTransfer:
    interval: 1h0m0s</code></pre></td>
<td style="text-align: left;"><p>Sets the frequency for checking available cluster transfers.</p></td>
<td style="text-align: left;"><p>Time interval</p></td>
<td style="text-align: left;"><p><code>24h</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>dataReporting:
    interval: 30m0s</code></pre></td>
<td style="text-align: left;"><p>Sets the data gathering and upload frequency.</p></td>
<td style="text-align: left;"><p>Time interval</p></td>
<td style="text-align: left;"><p><code>2h</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>dataReporting:
    uploadEndpoint: &lt;url&gt;</code></pre></td>
<td style="text-align: left;"><p>Sets the upload endpoint.</p></td>
<td style="text-align: left;"><p>URL</p></td>
<td style="text-align: left;"><p><a href="https://console.redhat.com/api/ingress/v1/upload">https://console.redhat.com/api/ingress/v1/upload</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>dataReporting:
    storagePath: &lt;path&gt;</code></pre></td>
<td style="text-align: left;"><p>Configures the path where archived data gets stored.</p></td>
<td style="text-align: left;"><p>File path</p></td>
<td style="text-align: left;"><p>/var/lib/insights-operator</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>dataReporting:
    downloadEndpoint: &lt;url&gt;</code></pre></td>
<td style="text-align: left;"><p>Specifies the endpoint for downloading the latest Red Hat Lightspeed analysis.</p></td>
<td style="text-align: left;"><p>URL</p></td>
<td style="text-align: left;"><p><a href="https://console.redhat.com/api/ingress/v1/download">https://console.redhat.com/api/ingress/v1/download</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>dataReporting:
    conditionalGathererEndpoint: &lt;url&gt;</code></pre></td>
<td style="text-align: left;"><p>Sets the endpoint for providing conditional gathering rule definitions.</p></td>
<td style="text-align: left;"><p>URL</p></td>
<td style="text-align: left;"><p><a href="https://console.redhat.com/api/gathering/gathering_rules">https://console.redhat.com/api/gathering/gathering_rules</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>dataReporting:
    disableRuntimeExtractor: true</code></pre></td>
<td style="text-align: left;"><p>When set to true, it disables the deployment and management of all insights-runtime-extractor resources.</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>dataReporting:
    obfuscation:
    - networking</code></pre></td>
<td style="text-align: left;"><p>Enables the global obfuscation of IP addresses and the cluster domain name.</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"><p>Not applicable</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>dataReporting:
    obfuscation:
    - workload_names</code></pre></td>
<td style="text-align: left;"><p>Enables the obfuscation of Data Validation Operator data. The cluster resource ID is only visible in the archive file and not the resource name.</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"><p>Not applicable</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>proxy:
    httpProxy: http://example.com
    httpsProxy: http://example.com
    noProxy: test.org</code></pre></td>
<td style="text-align: left;"><p>Set custom proxy for Insights Operator.</p></td>
<td style="text-align: left;"><p>URL</p></td>
<td style="text-align: left;"><p>No default</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>sca:
    interval: 8h0m0s</code></pre></td>
<td style="text-align: left;"><p>Specifies the frequency of the simple content access (SCA) entitlements download.</p></td>
<td style="text-align: left;"><p>Time interval</p></td>
<td style="text-align: left;"><p><code>2h</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>sca:
    endpoint: &lt;url&gt;</code></pre></td>
<td style="text-align: left;"><p>Specifies the endpoint for downloading the simple content access (SCA) entitlements.</p></td>
<td style="text-align: left;"><p>URL</p></td>
<td style="text-align: left;"><p><a href="https://api.openshift.com/api/accounts_mgmt/v1/entitlement_certificates">https://api.openshift.com/api/accounts_mgmt/v1/entitlement_certificates</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>sca:
    disabled: false</code></pre></td>
<td style="text-align: left;"><p>Disables the simple content access entitlements download.</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: left;"><p><code>false</code></p></td>
</tr>
</tbody>
</table>

# Insights Operator alerts

The Insights Operator declares alerts through the Prometheus monitoring system to the Alertmanager. You can view these alerts in the Alerting UI in the OpenShift Container Platform web console.

To view these alerts in the Alerting UI in the OpenShift Container Platform web console, choose one of the following methods:

- In the **Administrator** perspective, click **Observe** → **Alerting**.

- In the **Developer** perspective, click **Observe** → \<project_name\> → **Alerts** tab.

Currently, Insights Operator sends the following alerts when the conditions are met:

| Alert | Description |
|----|----|
| `InsightsDisabled` | Insights Operator is disabled. |
| `SimpleContentAccessNotAvailable` | Simple content access is not enabled in Red Hat Subscription Management. |
| `InsightsRecommendationActive` | Red Hat Lightspeed has an active recommendation for the cluster. |

Insights Operator alerts

## Disabling Insights Operator alerts

To prevent the Insights Operator from sending alerts to the cluster Prometheus instance, you create or edit the `insights-config` `ConfigMap` object.

> [!NOTE]
> Previously, a cluster administrator would create or edit the Insights Operator configuration using a support secret in the `openshift-config` namespace. Red Hat Lightspeed now supports the creation of a `ConfigMap` object to configure the Operator. The Operator gives preference to the config map configuration over the support secret if both exist.

If the `insights-config` `ConfigMap` object does not exist, you must create it when you first add custom configurations. Note that configurations within the `ConfigMap` object take precedence over the default settings defined in the `config/pod.yaml` file.

<div>

<div class="title">

Prerequisites

</div>

- Remote health reporting is enabled, which is the default.

- You are logged in to the OpenShift Container Platform web console as `cluster-admin`.

- The `insights-config` `ConfigMap` object exists in the `openshift-insights` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to **Workloads** → **ConfigMaps** and select **Project: openshift-insights**.

2.  Click the **insights-config** `ConfigMap` object to open it.

3.  Click **Actions** and select **Edit ConfigMap**.

4.  Click the **YAML view** radio button.

5.  In the file, set the `alerting` attribute to `disabled: true`.

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    # ...
    data:
      config.yaml: |
        alerting:
          disabled: true
    # ...
    ```

6.  Click **Save**. The `insights-config` ConfigMap details page opens.

7.  Verify that the value of the `config.yaml` `alerting` attribute is set to `disabled: true`.

</div>

After you save the changes, Insights Operator no longer sends alerts to the cluster Prometheus instance.

## Enabling Insights Operator alerts

When alerts are disabled, the Insights Operator no longer sends alerts to the cluster Prometheus instance. You can re-enable them.

> [!NOTE]
> Previously, a cluster administrator would create or edit the Insights Operator configuration using a support secret in the `openshift-config` namespace. Red Hat Lightspeed now supports the creation of a `ConfigMap` object to configure the Insights Operator. The Insights Operator gives preference to the config map configuration over the support secret if both exist.

<div>

<div class="title">

Prerequisites

</div>

- Remote health reporting is enabled, which is the default.

- You are logged in to the OpenShift Container Platform web console as `cluster-admin`.

- The `insights-config` `ConfigMap` object exists in the `openshift-insights` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to **Workloads** → **ConfigMaps** and select **Project: openshift-insights**.

2.  Click on the `insights-config` `ConfigMap` object to open it.

3.  Click **Actions** and select **Edit ConfigMap**.

4.  Click the **YAML view** radio button.

5.  In the file, set the `alerting` attribute to `disabled: false`.

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    # ...
    data:
      config.yaml: |
        alerting:
          disabled: false
    # ...
    ```

6.  Click **Save**. The `insights-config` `ConfigMap` details page opens.

7.  Verify that the value of the `config.yaml` `alerting` attribute is set to `disabled: false`.

</div>

After you save the changes, Insights Operator again sends alerts to the cluster Prometheus instance.

# Downloading your Insights Operator archive

Insights Operator stores gathered data in an archive located in the `openshift-insights` namespace of your cluster. You can download and review the data that is gathered by the Insights Operator.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Find the name of the running pod for the Insights Operator:

    ``` terminal
    $ oc get pods --namespace=openshift-insights -o custom-columns=:metadata.name --no-headers  --field-selector=status.phase=Running
    ```

2.  Copy the recent data archives collected by the Insights Operator:

    ``` terminal
    $ oc cp openshift-insights/<insights_operator_pod_name>:/var/lib/insights-operator ./insights-data
    ```

    - Replace `<insights_operator_pod_name>` with the pod name output from the preceding command.

</div>

The recent Insights Operator archives are now available in the `insights-data` directory.

# On-demand Insights Operator gather operations

Instead of waiting for the next periodic data gather operation, you can run a custom on-demand Insights Operator data gather operation by using the OpenShift Container Platform web console or command-line interface (CLI).

A periodic data gather operation uses the `InsightsDataGather` custom resource definition (CRD) for configuration instructions, whereas an on-demand equivalent requires a `DataGather` CRD to be configured.

An on-demand `DataGather` operation is:

- Useful for one-off data collections that require different CRD configurations to the periodic data gathering (`InsightsDataGather`) specification.

- Independent from the periodic data gathering. When you create an on-demand `DataGather` CRD, the configuration is independent from the `InsightsDataGather` CRD specification of your periodic data gathering job.

**Custom specification options**

You can optionally customize the following items for the on-demand data gather operation:

- **Enable and define data obfuscation:** By defining the `DataGather` `dataPolicy` specification, you can enable additional obfuscation of the Red Hat Lightspeed archive data, for example, the IP address or workload names.

- **Enable persistent storage:** By default, the Insights Operator uses ephemeral storage, which means that a new pod will be created for each gather operation and the history of gather operations and data collected is not retained. You can switch to persistent storage to retain the data and history for up to the last 10 gather operations by defining the `DataGather` `storage` specification in the CRD.

- **Exclude specific data gather operations:** You can choose to disable specific gather operations from running by defining the `DataGather` `gatherers` specification. For example, you can choose to disable the cluster authentication operation or the workload data operation.

> [!IMPORTANT]
> Excluding gather operations from the default list might reduce or limit the recommendations offered by the Red Hat Lightspeed advisor service for your cluster.

If you do not configure any custom specification options in the `DataGather` CRD, the default Insights Operator data collection job will run. This means that all gather operations will run, the collected data will be unobfuscated and the archive file will not be retained.

When you run a gather operation on-demand, any configuration that was previously applied to disable Insights Operator gather operations for your cluster will be overridden.

> [!IMPORTANT]
> The `DataGather` custom resource is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

> [!NOTE]
> If you enable Technology Preview in your cluster, the Insights Operator runs gather operations in individual pods. This is part of the Technology Preview feature set for the Insights Operator and supports the new data gathering features.

## Viewing Insights Operator gather durations

You can view the time it takes for the Insights Operator to gather the information contained in the archive. This helps you to understand Insights Operator resource usage and issues with Red Hat Lightspeed Advisor.

<div>

<div class="title">

Prerequisites

</div>

- A recent copy of your Insights Operator archive.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From your archive, open `/insights-operator/gathers.json`.

    The file contains a list of Insights Operator gather operations:

    ``` json
        {
          "name": "clusterconfig/authentication",
          "duration_in_ms": 730,
          "records_count": 1,
          "errors": null,
          "panic": null
        }
    ```

    - `duration_in_ms` is the amount of time in milliseconds for each gather operation.

2.  Inspect each gather operation for abnormalities.

</div>

## Gathering data on demand with the Insights Operator from the web console

You can run a custom Insights Operator gather operation on-demand from the OpenShift Container Platform web console. An on-demand `DataGather` operation is useful for one-off data collections that require different configurations to the periodic data gathering (`InsightsDataGather`) specification.

Use the following procedure to create a `DataGather` custom resource definition (CRD), and then run the data gather operation on demand from the web console.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On the console, select **Administration** \> **CustomResourceDefinitions**.

2.  On the **CustomResourceDefinitions** page, in the **Search by name** field, find and then click the **DataGather** resource definition.

3.  On the **CustomResourceDefinition details** page, click the **Instances** tab.

4.  Click **Create DataGather**.

5.  To create a new `DataGather` operation where all gather operations will run, complete the following YAML specification, and then save your changes.

    ``` yaml
    apiVersion: insights.openshift.io/v1alpha2
    kind: DataGather
    metadata:
      name: <your_data_gather>
    spec:
    # Gatherers configuration
      gatherers:
        mode: All # Options: All, Custom
    # ...
    ```

    <div class="important">

    <div class="title">

    </div>

    - The name you specify for your gather operation, `<your_data_gather>`, must be unique and must not include a prefix of `periodic-gathering-` because this string is reserved for other administrative operations and might impact the intended gather operation.

    - If the `spec` of `DataGather` CRD is undefined, the default Insights Operator data collection job will run. This means that all gather operations will run, the collected data will be unobfuscated and the archive file will not be retained.

    </div>

6.  Optional: To customize the data gather operation, you can configure any of the following options in your `DataGather` YAML file:

    - To disable specific gatherers, change the value of `mode` to **Custom**, and then specify the individual gatherer that you intend to disable. For example, to disable the workload gatherer, add the following example:

      ``` yaml
      apiVersion: insights.openshift.io/v1alpha2
      kind: DataGather
      metadata:
        name: <your_data_gather>
      spec:
          # Gatherers configuration
        gatherers:
          mode: Custom  # Options: All, Custom
          custom:
            configs:
              # Essential cluster configuration gatherers
              - name: clusterconfig/authentication
                state: Enabled
              - name: clusterconfig/clusteroperators
                state: Enabled
              - name: workloads
                state: Disabled
      ```

    - To enable persistent storage to retain the data archive file and history for up to the last 10 data gathering jobs, define the `storage` specification. Set **type** to `PersistentVolume`, and define the `mountPath` and `name` of the volume, as outlined in the following example:

      ``` yaml
      apiVersion: insights.openshift.io/v1alpha2
      kind: DataGather
      metadata:
        name: <your_data_gather>
      spec:
        storage:
          type: PersistentVolume
          mountPath: /data
          persistentVolume:
            claim:
              name: on-demand-gather-pvc
      ```

      > [!IMPORTANT]
      > Ensure that the volume name specified matches the existing `PersistentVolumeClaim` value in the `openshift-insights` namespace. For more information, see [Persistent volume claims](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/storage/understanding-persistent-storage#persistent-volume-claims_understanding-persistent-storage).

    - To enable data obfuscation, define the `dataPolicy` key and required values. For example, to obfuscate IP addresses and workload names, add the following configuration:

      ``` yaml
      apiVersion: insights.openshift.io/v1alpha2
      kind: DataGather
      metadata:
        name: <your_data_gather>
      spec:
        dataPolicy:
          - ObfuscateNetworking
          - WorkloadNames
      ```

</div>

<div>

<div class="title">

Verification

</div>

1.  On the console, select **Workloads** \> **Pods**.

2.  On the Pods page, go to the **Project** pull-down menu, and then select **Show default projects**.

3.  Select the `openshift-insights` project from the **Project** pull-down menu.

4.  Check that your new gather operation is prefixed with your chosen name under the list of pods in the `openshift-insights` project. Upon completion, the Insights Operator automatically uploads the data to Red Hat for processing.

</div>

## Gathering data on demand with the Insights Operator from the OpenShift CLI

You can run a custom Insights Operator gather operation on-demand from the OpenShift Container Platform command-line interface (CLI). An on-demand `DataGather` operation is useful for one-off data collections that require different configurations to the periodic data gathering (`InsightsDataGather`) specification.

Use the following procedure to create a `DataGather` custom resource definition (CRD), and then run the data gather operation on demand from the CLI.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file with the following `DataGather` specification:

    ``` yaml
    apiVersion: insights.openshift.io/v1alpha2
    kind: DataGather
    metadata:
      name: <your_data_gather>
    spec:
    # Gatherers configuration
      gatherers:
        mode: All # Options: All, Custom
    # ...
    ```

    <div class="important">

    <div class="title">

    </div>

    - The name you specify for your gather operation, `<your_data_gather>`, must be unique and must not include a prefix of `periodic-gathering-` because this string is reserved for other administrative operations and might impact the intended gather operation.

    - If the `spec` of `DataGather` CRD is undefined, the default Insights Operator data collection job will run. This means that all gather operations will run, the collected data will be unobfuscated and the archive file will not be retained.

    </div>

2.  Optional: To customize the data gather operation, you can configure any of the following options in your `DataGather` YAML file:

    - To disable specific gatherers, change the value of `mode` to **Custom**, and then specify the individual gatherer that you intend to disable. For example, to disable the workload gatherer, add the following example:

      ``` yaml
      apiVersion: insights.openshift.io/v1alpha2
      kind: DataGather
      metadata:
        name: <your_data_gather>
      spec:
          # Gatherers configuration
        gatherers:
          mode: Custom  # Options: All, Custom
          custom:
            configs:
              # Essential cluster configuration gatherers
              - name: clusterconfig/authentication
                state: Enabled
              - name: clusterconfig/clusteroperators
                state: Enabled
              - name: workloads
                state: Disabled
      ```

    - To enable persistent storage to retain the data archive file and history for up to the last 10 data gathering jobs, define the `storage` specification. Set `type` to `PersistentVolume`, and define the `mountPath` and `name` of the volume:

      ``` yaml
      apiVersion: insights.openshift.io/v1alpha2
      kind: DataGather
      metadata:
        name: <your_data_gather>
      spec:
        storage:
          type: PersistentVolume
          mountPath: /data
          persistentVolume:
            claim:
              name: on-demand-gather-pvc
      ```

      > [!IMPORTANT]
      > Ensure that the volume name specified matches the existing `PersistentVolumeClaim` value in the `openshift-insights` namespace. For more information, see [Persistent volume claims](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/storage/understanding-persistent-storage#persistent-volume-claims_understanding-persistent-storage).

    - To enable data obfuscation, define the `dataPolicy` key and required values. For example, to obfuscate IP addresses and workload names, add the following configuration:

      ``` yaml
      apiVersion: insights.openshift.io/v1alpha2
      kind: DataGather
      metadata:
        name: <your_data_gather>
      spec:
        dataPolicy:
          - ObfuscateNetworking
          - WorkloadNames
      ```

3.  On the OpenShift Container Platform CLI, enter the following command to run the gather operation:

    ``` terminal
    $ oc apply -f <your_data_gather_definition>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Check that your new gather operation is prefixed with your chosen name under the list of pods in the `openshift-insights` project. Upon completion, the Insights Operator automatically uploads the data to Red Hat for processing.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Insights Operator Gathered Data GitHub repository](https://github.com/openshift/insights-operator/blob/master/docs/gathered-data.md)

</div>

## Disabling the Insights Operator periodic gather operations

You can optionally disable the periodic `InsightsDataGather` operations that the Insights Operator runs every 2 hours by default. Disabling the periodic data gather operations increases privacy for your organization as Insights Operator will no longer gather and send Red Hat Lightspeed cluster reports to Red Hat.

Disabling gather operations will also disable Red Hat Lightspeed analysis and recommendations for your cluster without affecting other core functions that require communication with Red Hat such as cluster transfers.

You can view a list of attempted gather operations for your cluster from the `/insights-operator/gathers.json` file in your Insights Operator archive. Be aware that some gather operations occur only when certain conditions are met and might not show in your most recent archive.

> [!IMPORTANT]
> The `InsightsDataGather` custom resource is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

> [!NOTE]
> If you enable Technology Preview in your cluster, the Insights Operator runs gather operations in individual pods. This is part of the Technology Preview feature set for the Insights Operator and supports the new data gathering features.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Administration** \> **CustomResourceDefinitions**.

2.  On the **CustomResourceDefinitions** page, use the **Search by name** field to find the **InsightsDataGather** custom resource definition (CRD), and click to open.

3.  On the **CustomResourceDefinition details** page, click the **Instances** tab.

4.  Click **cluster**, and then click the **YAML** tab.

5.  Edit the `InsightsDataGather` CRD, and complete one of the following steps:

    - To disable all the gather operations and data collection, define the `gatherers` specification and set the `mode` to `None`:

      ``` yaml
      apiVersion: insights.openshift.io/v1alpha2
      kind: InsightsDataGather
      metadata:
        name: cluster
      spec:
      # Gatherers configuration
        gatherers:
          mode: None # Options: All, None, Custom
      ```

    - To disable individual gather operations, under `gatherers`, set the `mode` to `Custom` and then specify the individual gatherer that you intend to disable. For example, to disable the workload gatherer, define the following specification:

      ``` yaml
      apiVersion: insights.openshift.io/v1alpha2
      kind: InsightsDataGather
      metadata:
        name: cluster
      spec:
          # Gatherers configuration
        gatherers:
          mode: Custom  # Options: All, None, Custom
          custom:
            configs:
              # Essential cluster configuration gatherers
              - name: clusterconfig/authentication
                state: Enabled
              - name: clusterconfig/clusteroperators
                state: Enabled
              - name: workloads
                state: Disabled
      ```

6.  Click **Save**.

</div>

<div class="formalpara">

<div class="title">

Results

</div>

The Insights Operator updates the gather configurations and no longer runs the operations that you disabled.

</div>

> [!NOTE]
> Disabling gather operations restricts the ability of the Red Hat Lightspeed advisor service to offer effective recommendations for your cluster.

## Re-enabling the Insights Operator periodic gather operations

If you disabled the default `InsightsDataGather` data gather operations, you can enable them again so that the Insights Operator resumes the periodic data collection, and sends the resulting Red Hat Lightspeed cluster reports to Red Hat.

> [!IMPORTANT]
> The `InsightsDataGather` custom resource is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Administration** \> **CustomResourceDefinitions**.

2.  On the **CustomResourceDefinitions** page, use the **Search by name** field to find the **InsightsDataGather** custom resource definition (CRD), and click to open.

3.  On the **CustomResourceDefinition details** page, click the **Instances** tab.

4.  Click **cluster**, and then click the **YAML** tab.

5.  Edit the `InsightsDataGather` CRD, and complete one of the following steps:

    - To enable all disabled gather operations, under the `gatherers` specification, set the `mode` back to `All`:

      ``` yaml
      apiVersion: insights.openshift.io/v1alpha2
      kind: InsightsDataGather
      metadata:
        name: cluster
      spec:
      # Gatherers configuration
        gatherers:
          mode: All # Options: All, None, Custom
      ```

    - To enable individual gather operations that were previously disabled, find the name of the gatherer operation under the `gatherers:custom:configs` key section and change the `state` to `Enabled`. Alternatively, under the `config` specification, remove the `name` and `state` configuration lines for the operation you want to enable.

      ``` yaml
      apiVersion: insights.openshift.io/v1alpha2
      kind: InsightsDataGather
      metadata:
        name: cluster
      spec:
          # Gatherers configuration
        gatherers:
          mode: Custom  # Options: All, None, Custom
          custom:
            configs:
              # Essential cluster configuration gatherers
              - name: clusterconfig/authentication
                state: Enabled
              - name: clusterconfig/clusteroperators
                state: Enabled
              - name: workloads
                state: Enabled
      ```

6.  Click **Save**.

    After you save the changes, the Insights Operator gather configurations are updated and the affected gather operations start.

</div>

> [!NOTE]
> Disabling gather operations restricts the ability of the Red Hat Lightspeed advisor service to offer effective recommendations for your cluster.

# Obfuscating Deployment Validation Operator data

By default, when you install the Deployment Validation Operator (DVO), the name and unique identifier (UID) of a resource are included in the data that is captured and processed by the Insights Operator for OpenShift Container Platform. If you are a cluster administrator, you can configure the Insights Operator to obfuscate data from the Deployment Validation Operator (DVO). For example, you can obfuscate workload names in the archive file that is then sent to Red Hat.

To obfuscate the name of resources, you must manually set the `obfuscation` attribute in the `insights-config` `ConfigMap` object to include the `workload_names` value, as outlined in the following procedure.

<div>

<div class="title">

Prerequisites

</div>

- Remote health reporting is enabled, which is the default.

- You are logged in to the OpenShift Container Platform web console with the "cluster-admin" role.

- The `insights-config` `ConfigMap` object exists in the `openshift-insights` namespace.

- The cluster is self managed and the Deployment Validation Operator is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to **Workloads** → **ConfigMaps** and select **Project: openshift-insights**.

2.  Click the `insights-config` `ConfigMap` object to open it.

3.  Click **Actions** and select **Edit ConfigMap**.

4.  Click the **YAML view** radio button.

5.  In the file, set the `obfuscation` attribute with the `workload_names` value.

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    # ...
    data:
      config.yaml: |
        dataReporting:
          obfuscation:
            - workload_names
    # ...
    ```

6.  Click **Save**. The `insights-config` ConfigMap details page opens.

7.  Verify that the value of the `config.yaml` `obfuscation` attribute is set to `- workload_names`.

</div>
