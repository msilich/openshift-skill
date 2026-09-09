<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can install RHACS Cloud Service on your secured clusters by using one of the following methods:

- By using Helm charts

- By using the `roxctl` CLI (do not use this method unless you have a specific installation need that requires using it)

<a id="installing-sc-helm-cloud-other_install-secured-cluster-cloud-other"></a>

# Installing RHACS Cloud Service on secured clusters by using Helm charts

You can install RHACS on secured clusters by adding the Helm chart repository and then selecting your installation method.

The installation methods include using Helm charts with no customization, using Helm charts with the default values, or using Helm charts with customizations of configuration parameters.

<a id="adding-helm-repository_install-secured-cluster-cloud-other"></a>

## Adding the Helm chart repository

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

<a id="installing-sc-helm-default-cloud-other_install-secured-cluster-cloud-other"></a>

## Installing RHACS Cloud Service on secured clusters by using Helm charts without customizations

Use the secured-cluster-services Helm chart without customizations for a quick deployment with default settings.

<a id="installing-secured-cluster-services-quickly_install-secured-cluster-cloud-other"></a>

### Installing the secured-cluster-services Helm chart without customization

Use the following instructions to install the `secured-cluster-services` Helm chart to deploy the per-cluster and per-node components (Sensor, Admission controller, Collector, and Scanner-slim).

<div>

<div class="title">

Prerequisites

</div>

- You must have generated a RHACS cluster registration secret (CRS) or an init bundle for your cluster.

- You must have access to the Red Hat Container Registry and a pull secret for authentication. For information about downloading images from `registry.redhat.io`, see "Red Hat Container Registry Authentication".

- You must have the **Central API Endpoint** address. You can view this information by selecting **Advanced Cluster Security** → **ACS Instances** from the Red Hat Hybrid Cloud Console navigation menu, then clicking the ACS instance you created.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command on your Kubernetes-based clusters:

  - If you are using a CRS, run the following command:

    ``` terminal
    $ helm install -n stackrox --create-namespace \
        stackrox-secured-cluster-services rhacs/secured-cluster-services \
        --set-file crs.file=<crs_file_name.yaml> \
        -f <path_to_pull_secret.yaml> \
        --set clusterName=<name_of_the_secured_cluster> \
        --set centralEndpoint=<endpoint_of_central_service>
    ```

    where:

    `<crs_file_name.yaml>`  
    Specifies the name of the file where you stored the generated CRS.

    `<path_to_pull_secret.yaml>`  
    Specifies the path for the pull secret for Red Hat Container Registry authentication. Or, you can specify `--set imagePullSecrets.username=<your redhat.com username>` and `--set imagePullSecrets.password=<your redhat.com password>` in the command.

    `<endpoint_of_central_service>`  
    Specifies the address and port number for Central. For example, `acs.domain.com:443`.

    `<your redhat.com username>`  
    Specifies the user name for your pull secret for Red Hat Container Registry authentication.

    `<your redhat.com password>`  
    Specifies the password for your pull secret for Red Hat Container Registry authentication.

  - If you are using an init bundle, run the following command:

    ``` terminal
    $ helm install -n stackrox --create-namespace \
        stackrox-secured-cluster-services rhacs/secured-cluster-services \
        -f <path_to_cluster_init_bundle.yaml> \
        -f <path_to_pull_secret.yaml> \
        --set clusterName=<name_of_the_secured_cluster> \
        --set centralEndpoint=<endpoint_of_central_service>
    ```

    where:

    `<path_to_cluster_init_bundle.yaml>`  
    Specifies the path for the init bundle.

    `<path_to_pull_secret.yaml>`  
    Specifies the path for the pull secret for Red Hat Container Registry authentication. Or, you can specify `--set imagePullSecrets.username=<your redhat.com username>` and `--set imagePullSecrets.password=<your redhat.com password>` in the command.

    `<endpoint_of_central_service>`  
    Specifies the **Central API Endpoint** address. You can view this information by choosing **Advanced Cluster Security** → **ACS Instances** from the Red Hat Hybrid Cloud Console navigation menu, and then clicking the RHACS instance you created.

    `<your redhat.com username>`  
    Specifies the user name for your pull secret for Red Hat Container Registry authentication.

    `<your redhat.com password>`  
    Specifies the password for your pull secret for Red Hat Container Registry authentication.

</div>

- Run one of the following commands on an OpenShift Container Platform cluster:

  - If you are using a CRS, run the following command:

    ``` terminal
    $ helm install -n stackrox --create-namespace \
        stackrox-secured-cluster-services rhacs/secured-cluster-services \
        --set-file crs.file=<crs_file_name.yaml> \
        -f <path_to_pull_secret.yaml> \
        --set clusterName=<name_of_the_secured_cluster> \
        --set centralEndpoint=<endpoint_of_central_service> \
        --set scanner.disable=false
    ```

    where:

    `<crs_file_name.yaml>`  
    Specifies the name of the file where you stored the generated CRS.

    `<path_to_pull_secret.yaml>`  
    Specifies the path for the pull secret for Red Hat Container Registry authentication.

    `<endpoint_of_central_service>`  
    Specifies the **Central API Endpoint** address. You can view this information by choosing **Advanced Cluster Security** → **ACS Instances** from the Red Hat Hybrid Cloud Console navigation menu, then clicking the RHACS instance you created.

    `--set scanner.disable=false`  
    Sets the value of the `scanner.disable` parameter to `false`, which enables Scanner-slim during the installation. In Kubernetes, the secured cluster services now include Scanner-slim.

  - If you are using an init bundle, run the following command:

    ``` terminal
    $ helm install -n stackrox --create-namespace \
        stackrox-secured-cluster-services rhacs/secured-cluster-services \
        -f <path_to_cluster_init_bundle.yaml> \
        -f <path_to_pull_secret.yaml> \
        --set clusterName=<name_of_the_secured_cluster> \
        --set centralEndpoint=<endpoint_of_central_service> \
        --set scanner.disable=false
    ```

    where:

    `<path_to_cluster_init_bundle.yaml>`  
    Specifies the path for the init bundle.

    `<path_to_pull_secret.yaml>`  
    Specifies the path for the pull secret for Red Hat Container Registry authentication.

    `<endpoint_of_central_service>`  
    Specifies the **Central API Endpoint** address. You can view this information by choosing **Advanced Cluster Security** → **ACS Instances** from the Red Hat Hybrid Cloud Console navigation menu, then clicking the RHACS instance you created.

    `--set scanner.disable=false`  
    Sets the value of the `scanner.disable` parameter to `false`, which enables Scanner-slim during the installation. In Kubernetes, the secured cluster services now include Scanner-slim.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication)

</div>

<a id="configure-secured-cluster-services-helm-chart-customizations-cloud-other_install-secured-cluster-cloud-other"></a>

## Configuring the secured-cluster-services Helm chart with customizations

Customize the secured-cluster-services Helm chart installation by using configuration parameters.

You can use Helm chart configuration parameters with the `helm install` and `helm upgrade` commands by using the `--set` option or by creating YAML configuration files.

Create the following files for configuring the Helm chart for installing Red Hat Advanced Cluster Security for Kubernetes:

- Public configuration file `values-public.yaml`: Use this file to save all non-sensitive configuration options.

- Private configuration file `values-private.yaml`: Use this file to save all sensitive configuration options. Ensure that you store this file securely.

> [!IMPORTANT]
> While using the `secured-cluster-services` Helm chart, do not change the `values.yaml` file that is part of the chart.

<a id="secured-cluster-services-config_install-secured-cluster-cloud-other"></a>

### Configuration parameters

Reference of configuration parameters for customizing the secured-cluster-services Helm chart installation.

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
<td style="text-align: left;"><p><code>clusterName</code></p></td>
<td style="text-align: left;"><p>Name of your cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>centralEndpoint</code></p></td>
<td style="text-align: left;"><p>Address of the Central endpoint. If you are using a non-gRPC capable load balancer, use the WebSocket protocol by prefixing the endpoint address with <code>wss://</code>. When configuring multiple clusters, use the hostname for the address. For example, <code>central.example.com</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>env.grpcEnforceALPN</code></p></td>
<td style="text-align: left;"><p>Use <code>true</code> to force application-level protocol negotiation (ALPN) during the TLS handshake.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sensor.endpoint</code></p></td>
<td style="text-align: left;"><p>Address of the Sensor endpoint including port number.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sensor.imagePullPolicy</code></p></td>
<td style="text-align: left;"><p>Image pull policy for the Sensor container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sensor.serviceTLS.cert</code></p></td>
<td style="text-align: left;"><p>The internal service-to-service TLS certificate that Sensor uses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sensor.serviceTLS.key</code></p></td>
<td style="text-align: left;"><p>The internal service-to-service TLS certificate key that Sensor uses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sensor.resources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for the Sensor container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sensor.resources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for the Sensor container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sensor.resources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for the Sensor container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sensor.resources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for the Sensor container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sensor.nodeSelector</code></p></td>
<td style="text-align: left;"><p>Specify a node selector label as <code>label-key: label-value</code> to force Sensor to only schedule on nodes with the specified label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sensor.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Sensor. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.main.name</code></p></td>
<td style="text-align: left;"><p>The name of the <code>main</code> image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.collector.name</code></p></td>
<td style="text-align: left;"><p>The name of the Collector image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.main.registry</code></p></td>
<td style="text-align: left;"><p>The address of the registry you are using for the main image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.collector.registry</code></p></td>
<td style="text-align: left;"><p>The address of the registry you are using for the Collector image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.scanner.registry</code></p></td>
<td style="text-align: left;"><p>The address of the registry you are using for the Scanner image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.scannerDb.registry</code></p></td>
<td style="text-align: left;"><p>The address of the registry you are using for the Scanner DB image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.scannerV4.registry</code></p></td>
<td style="text-align: left;"><p>The address of the registry you are using for the Scanner V4 image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.scannerV4DB.registry</code></p></td>
<td style="text-align: left;"><p>The address of the registry you are using for the Scanner V4 DB image.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.main.pullPolicy</code></p></td>
<td style="text-align: left;"><p>Image pull policy for <code>main</code> images.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.collector.pullPolicy</code></p></td>
<td style="text-align: left;"><p>Image pull policy for the Collector images.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.main.tag</code></p></td>
<td style="text-align: left;"><p>Tag of <code>main</code> image to use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>image.collector.tag</code></p></td>
<td style="text-align: left;"><p>Tag of <code>collector</code> image to use.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.collectionMethod</code></p></td>
<td style="text-align: left;"><p>Either <code>CORE_BPF</code> or <code>NO_COLLECTION</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.imagePullPolicy</code></p></td>
<td style="text-align: left;"><p>Image pull policy for the Collector container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.complianceImagePullPolicy</code></p></td>
<td style="text-align: left;"><p>Image pull policy for the Compliance container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.disableTaintTolerations</code></p></td>
<td style="text-align: left;"><p>If you specify <code>false</code>, tolerations are applied to Collector, and the collector pods can schedule onto all nodes with taints. If you specify it as <code>true</code>, no tolerations are applied, and no collector pods are scheduled onto nodes with taints.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.resources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for the Collector container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.resources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for the Collector container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.resources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for the Collector container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.resources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for the Collector container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.complianceResources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for the Compliance container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.complianceResources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for the Compliance container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.complianceResources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for the Compliance container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.complianceResources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for the Compliance container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.serviceTLS.cert</code></p></td>
<td style="text-align: left;"><p>The internal service-to-service TLS certificate that Collector uses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.serviceTLS.key</code></p></td>
<td style="text-align: left;"><p>The internal service-to-service TLS certificate key that Collector uses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.enforce</code></p></td>
<td style="text-align: left;"><p>This parameter determines if the admission controller was configured to enforce policies that have enforcement enabled. For a new secured cluster deployed with RHACS 4.9, the default value is <code>true</code>. For secured clusters updating from RHACS versions before 4.9, previous values for the admission controller configuration parameters determine the value of this parameter. Before the update, if either of the <code>admissionControl.enforceOnCreates</code> or <code>admissionControl.enforceOnUpdates</code> parameters was set to <code>true</code>, the value of this parameter defaults to <code>true</code> after upgrade. If both of these parameters were set to <code>false</code>, the default value becomes <code>false</code> on update.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.failurePolicy</code></p></td>
<td style="text-align: left;"><p>Determines whether API server request is allowed (fail open) or blocked (fail closed) if an error or timeout happens in the RHACS validating webhook’s evaluation. Valid values are <code>Ignore</code> and <code>Fail</code>. The default value is <code>Ignore</code> to fail open.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.listenOnCreates</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated and RHACS ignores its value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.listenOnUpdates</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated and RHACS ignores its value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.listenOnEvents</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated and RHACS ignores its value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.dynamic.enforceOnCreates</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated. RHACS checks its value during updates to version 4.9 and uses it to set a default value for the new <code>admissionControl.enforce</code> parameter. On new installations, changing this parameter has no effect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.dynamic.enforceOnUpdates</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated. RHACS checks its value during updates to version 4.9 and uses it to set a default value for the new <code>admissionControl.enforce</code> parameter. On new installations, changing this parameter has no effect.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.dynamic.scanInline</code></p></td>
<td style="text-align: left;"><p>This parameter is deprecated and RHACS ignores its value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.dynamic.disableBypass</code></p></td>
<td style="text-align: left;"><p>Set this parameter to <code>true</code> to disable bypassing the admission controller. The default value is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.dynamic.timeout</code></p></td>
<td style="text-align: left;"><p>The ability to configure this parameter is deprecated. RHACS uses a preset value for the timeout period and you cannot change it. This parameter is ignored.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.resources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for the Admission Control container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.resources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for the Admission Control container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.resources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for the Admission Control container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.resources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for the Admission Control container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.nodeSelector</code></p></td>
<td style="text-align: left;"><p>Specify a node selector label as <code>label-key: label-value</code> to force Admission Control to only schedule on nodes with the specified label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Admission Control. This parameter is mainly used for infrastructure nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.namespaceSelector</code></p></td>
<td style="text-align: left;"><p>If the admission controller webhook needs a specific <code>namespaceSelector</code>, you can specify the corresponding selector here. Use this parameter to override the default, which avoids a few system namespaces.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.serviceTLS.cert</code></p></td>
<td style="text-align: left;"><p>The internal service-to-service TLS certificate that Admission Control uses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.serviceTLS.key</code></p></td>
<td style="text-align: left;"><p>The internal service-to-service TLS certificate key that Admission Control uses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registryOverride</code></p></td>
<td style="text-align: left;"><p>Use this parameter to override the default <code>docker.io</code> registry. Specify the name of your registry if you are using some other registry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.disableTaintTolerations</code></p></td>
<td style="text-align: left;"><p>If you specify <code>false</code>, tolerations are applied to Collector, and the Collector pods can schedule onto all nodes with taints. If you specify it as <code>true</code>, no tolerations are applied, and no Collector pods are scheduled onto nodes with taints.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>createUpgraderServiceAccount</code></p></td>
<td style="text-align: left;"><p>Specify <code>true</code> to create the <code>sensor-upgrader</code> account. By default, Red Hat Advanced Cluster Security for Kubernetes creates a service account called <code>sensor-upgrader</code> in each secured cluster. This account is highly privileged but is only used during upgrades. If you do not create this account, you must complete future upgrades manually if the Sensor does not have enough permissions.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>createSecrets</code></p></td>
<td style="text-align: left;"><p>Specify <code>false</code> to skip the orchestrator secret creation for the Sensor, Collector, and Admission controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.slimMode</code></p></td>
<td style="text-align: left;"><p>Deprecated. Specify <code>true</code> if you want to use a slim Collector image for deploying Collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sensor.resources</code></p></td>
<td style="text-align: left;"><p>Resource specification for Sensor.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionControl.resources</code></p></td>
<td style="text-align: left;"><p>Resource specification for Admission controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.resources</code></p></td>
<td style="text-align: left;"><p>Resource specification for Collector.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>collector.complianceResources</code></p></td>
<td style="text-align: left;"><p>Resource specification for Collector’s Compliance container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>perNode.sfa.agent</code></p></td>
<td style="text-align: left;"><p>If you set this option to <code>Enabled</code>, you can enable file activity monitoring in your secured cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exposeMonitoring</code></p></td>
<td style="text-align: left;"><p>If you set this option to <code>true</code>, Red Hat Advanced Cluster Security for Kubernetes exposes Prometheus metrics endpoints on port number 9090 for the Sensor, Collector, and the Admission controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>auditLogs.disableCollection</code></p></td>
<td style="text-align: left;"><p>If you set this option to <code>true</code>, Red Hat Advanced Cluster Security for Kubernetes disables the audit log detection features used to detect access and modifications to configuration maps and secrets.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>autoLockProcessBaselines.enabled</code></p></td>
<td style="text-align: left;"><p>If you set this option to <code>true</code>, Red Hat Advanced Cluster Security for Kubernetes enables automatically locking process baselines. The default is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.disable</code></p></td>
<td style="text-align: left;"><p>If you set this option to <code>false</code>, Red Hat Advanced Cluster Security for Kubernetes deploys a Scanner-slim and Scanner DB in the secured cluster to allow scanning images on the integrated OpenShift image registry. Enabling Scanner-slim is supported on OpenShift Container Platform and Kubernetes secured clusters. Defaults to <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.dbTolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Scanner DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.replicas</code></p></td>
<td style="text-align: left;"><p>Resource specification for Collector’s Compliance container.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.logLevel</code></p></td>
<td style="text-align: left;"><p>Setting this parameter allows you to change the scanner log level. Use this option only for troubleshooting purposes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.autoscaling.disable</code></p></td>
<td style="text-align: left;"><p>If you set this option to <code>true</code>, Red Hat Advanced Cluster Security for Kubernetes disables autoscaling on the Scanner deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.autoscaling.minReplicas</code></p></td>
<td style="text-align: left;"><p>The minimum number of replicas for autoscaling. Defaults to 2.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.autoscaling.maxReplicas</code></p></td>
<td style="text-align: left;"><p>The maximum number of replicas for autoscaling. Defaults to 5.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.nodeSelector</code></p></td>
<td style="text-align: left;"><p>Specify a node selector label as <code>label-key: label-value</code> to force Scanner to only schedule on nodes with the specified label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.tolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Scanner.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.dbNodeSelector</code></p></td>
<td style="text-align: left;"><p>Specify a node selector label as <code>label-key: label-value</code> to force Scanner DB to only schedule on nodes with the specified label.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.dbTolerations</code></p></td>
<td style="text-align: left;"><p>If the node selector selects tainted nodes, use this parameter to specify a taint toleration key, value, and effect for Scanner DB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.resources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for the Scanner container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.resources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for the Scanner container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.resources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for the Scanner container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.resources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for the Scanner container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.dbResources.requests.memory</code></p></td>
<td style="text-align: left;"><p>The memory request for the Scanner DB container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.dbResources.requests.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU request for the Scanner DB container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.dbResources.limits.memory</code></p></td>
<td style="text-align: left;"><p>The memory limit for the Scanner DB container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scanner.dbResources.limits.cpu</code></p></td>
<td style="text-align: left;"><p>The CPU limit for the Scanner DB container. Use this parameter to override the default value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>monitoring.openshift.enabled</code></p></td>
<td style="text-align: left;"><p>If you set this option to <code>false</code>, Red Hat Advanced Cluster Security for Kubernetes will not set up Red Hat OpenShift monitoring. Defaults to <code>true</code> on Red Hat OpenShift 4.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>network.enableNetworkPolicies</code></p></td>
<td style="text-align: left;"><p>To provide security at the network level, RHACS creates default <code>NetworkPolicy</code> resources in the namespace where secured cluster resources are installed. These network policies allow ingress to specific components on specific ports. If you do not want RHACS to create these policies, set this parameter to <code>False</code>. This is a Boolean value. The default value is <code>True</code>, which means the default policies are automatically created.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>Disabling creation of default network policies can break communication between RHACS components. If you disable creation of default policies, you must create your own network policies to allow this communication.</p>
</div></td>
</tr>
</tbody>
</table>

<a id="secured-cluster-services-environment-variables_install-secured-cluster-cloud-other"></a>

### Environment variables

Specify custom environment variables for Sensor and Admission controller components in the secured-cluster-services Helm chart.

You can specify environment variables for Sensor and Admission controller in the following format:

``` yaml
customize:
  envVars:
    ENV_VAR1: "value1"
    ENV_VAR2: "value2"
```

Use the `customize` setting to specify custom Kubernetes metadata (labels and annotations) for all objects created by this Helm chart and additional pod labels, pod annotations, and container environment variables for workloads.

The configuration is hierarchical, in the sense that metadata defined at a more generic scope (for example, for all objects) can be overridden by metadata defined at a narrower scope (for example, only for the Sensor deployment).

<a id="install-secured-cluster-services-helm-chart_install-secured-cluster-cloud-other"></a>

### Installing the secured-cluster-services Helm chart with customizations

Install the secured-cluster-services Helm chart with custom configuration to deploy Sensor, Admission Controller, Collector, and Scanner components.

After you configure the `values-public.yaml` and `values-private.yaml` files, install the `secured-cluster-services` Helm chart to deploy the following per-cluster and per-node components:

- Sensor

- Admission controller

- Collector

- Scanner: optional for secured clusters when the StackRox Scanner is installed

- Scanner DB: optional for secured clusters when the StackRox Scanner is installed

- Scanner V4 Indexer and Scanner V4 DB: optional for secured clusters when Scanner V4 is installed

<div>

<div class="title">

Prerequisites

</div>

- You must have generated a cluster registration secret (CRS) or an init bundle for your cluster.

- You must have access to the Red Hat Container Registry and a pull secret for authentication. For information about downloading images from `registry.redhat.io`, see "Red Hat Container Registry Authentication".

- You must have the **Central API Endpoint** address. You can view this information by choosing **Advanced Cluster Security** → **ACS Instances** from the Red Hat Hybrid Cloud Console navigation menu, then clicking the RHACS instance you created.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command:

  ``` terminal
  $ helm install -n stackrox \
    --create-namespace stackrox-secured-cluster-services rhacs/secured-cluster-services \
    -f <name_of_cluster_init_bundle.yaml> \
    -f <path_to_values_public.yaml> \
    -f <path_to_values_private.yaml> \
    --set imagePullSecrets.username=<username> \
    --set imagePullSecrets.password=<password>
  ```

  where:

  `<path_to_values_public.yaml>`  
  Specifies the path to your public YAML configuration file.

  `<path_to_values_private.yaml>`  
  Specifies the path to your private YAML configuration file.

  `<username>`  
  Specifies the user name for your pull secret for Red Hat Container Registry authentication.

  `<password>`  
  Specifies the password for your pull secret for Red Hat Container Registry authentication.

  > [!NOTE]
  > To deploy `secured-cluster-services` Helm chart by using a continuous integration (CI) system, pass the CRS or the init bundle YAML file as an environment variable to the `helm install` command:
  >
  > ``` terminal
  > $ helm install ... -f <(echo "$INIT_BUNDLE_YAML_SECRET")
  > ```
  >
  > If you are using base64 encoded variables, use the `helm install …​ -f <(echo "$INIT_BUNDLE_YAML_SECRET" | base64 --decode)` command instead.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication)

</div>

<a id="change-config-options-after-deployment_install-secured-cluster-cloud-other"></a>

## Changing configuration options after deploying the secured-cluster-services Helm chart

Change configuration options for the secured-cluster-services Helm chart after deployment by using the helm upgrade command.

You can make changes to any configuration options after you have deployed the `secured-cluster-services` Helm chart.

When using the `helm upgrade` command to make changes, the following guidelines and requirements apply:

- You can also specify configuration values using the `--set` or `--set-file` parameters. However, these options are not saved, and you must manually specify all the options again whenever you make changes.

- Some changes, such as enabling a new component, require issuing new certificates for the component. Therefore, you must provide a CA when making these changes.

  - If the Helm chart generated the CA during the initial installation, you must retrieve these automatically generated values from the cluster and provide them to the `helm upgrade` command. The postinstallation notes of the `central-services` Helm chart include a command for retrieving the automatically generated values.

  - If you generated the CA outside of the Helm chart and provided it during the installation of the `central-services` chart, then you must perform that action again when using the `helm upgrade` command, for example, by using the `--reuse-values` flag with the `helm upgrade` command.

<div>

<div class="title">

Procedure

</div>

1.  Update the `values-public.yaml` and `values-private.yaml` configuration files with new values.

2.  Run the `helm upgrade` command and specify the configuration files using the `-f` option:

    ``` terminal
    $ helm upgrade -n stackrox \
      stackrox-secured-cluster-services rhacs/secured-cluster-services \
      --reuse-values \
      -f <path_to_values_public.yaml> \
      -f <path_to_values_private.yaml>
    ```

    where:

    `--reuse-values`  
    Specifies that the modified values are not included in the `values_public.yaml` and `values_private.yaml` files.

</div>

<a id="installing-sc-roxctl-cloud-other_install-secured-cluster-cloud-other"></a>

# Installing RHACS on secured clusters by using the roxctl CLI

Install RHACS on secured clusters by using the roxctl CLI to deploy Sensor components.

To install RHACS on secured clusters by using the CLI, perform the following steps:

1.  Install the `roxctl` CLI.

2.  Install Sensor.

<a id="installing-roxctl-cli-sc-cloud-other_install-secured-cluster-cloud-other"></a>

## Installing the roxctl CLI

Install the roxctl CLI binary to manage RHACS from the command line.

You can install `roxctl` on Linux, Windows, or macOS operating systems.

<a id="installing-cli-on-linux_install-secured-cluster-cloud-other"></a>

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

<a id="installing-cli-on-macos_install-secured-cluster-cloud-other"></a>

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

<a id="installing-cli-on-windows_install-secured-cluster-cloud-other"></a>

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

<a id="install-sensor-roxctl_install-secured-cluster-cloud-other"></a>

## Install Sensor

Deploy Sensor to a cluster by using the manifest installation method by using the RHACS portal or the `roxctl` CLI.

To monitor a cluster, you must deploy Sensor. You must deploy Sensor into each cluster that you want to monitor. This installation method is also called the manifest installation method.

To perform an installation by using the manifest installation method, follow *only one* of the following procedures:

- Use the RHACS web portal to download the cluster bundle, and then extract and run the sensor script.

- Use the `roxctl` CLI to generate the required sensor configuration for your OpenShift Container Platform cluster and associate it with your Central instance.

You must have already installed Central services, or you can access Central services by selecting your **ACS instance** on Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service).
