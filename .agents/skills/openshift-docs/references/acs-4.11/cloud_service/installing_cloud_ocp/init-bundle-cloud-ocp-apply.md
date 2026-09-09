<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Apply the cluster registration secret (CRS) or the init bundle to the secured cluster.

> [!NOTE]
> You must have the `Admin` user role to apply a CRS or an init bundle.

<a id="crs-apply-secured-cluster_init-bundle-cloud-ocp-apply"></a>

# Applying the cluster registration secret (CRS) on the secured cluster

Before you configure a secured cluster, you must apply the CRS to the secured cluster. After you have applied the CRS, the services on the secured cluster can communicate securely with RHACS Cloud Service.

> [!NOTE]
> If you are installing by using Helm charts, do not perform this step. Complete the installation by using Helm.

<div>

<div class="title">

Prerequisites

</div>

- You must have generated a CRS.

</div>

<div>

<div class="title">

Procedure

</div>

- Create resources using the OpenShift Container Platform web console:

  1.  In the OpenShift Container Platform web console, go to the `stackrox` project or the project where you want to install the secured cluster services.

  2.  In the top menu, click **+** to open the **Import YAML** page.

  3.  You can drag the CRS file or copy and paste its contents into the editor, and then click **Create**. When the command is complete, the display shows that the secret named `cluster-registration-secret` was created.

- Create resources using the Red Hat OpenShift CLI: Using the Red Hat OpenShift CLI, run the following command to create the resources:

  ``` terminal
  $ oc create -f <file_name.yaml> \
    -n <stackrox>
  ```

  where:

  `<file_name.yaml>`  
  Specifies the file name of the CRS.

  `<stackrox>`  
  Specifies the name of the project where secured cluster services are installed.

</div>

<div>

<div class="title">

Verification

</div>

- Restart Sensor to pick up the new certificates.

  For more information about how to restart Sensor, see "Restarting the Sensor container" in the "Additional resources" section.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing RHACS Cloud Service on secured clusters by using Helm charts](install-secured-cluster-cloud-ocp.md#installing-sc-helm-cloud-ocp_install-secured-cluster-cloud-ocp)

</div>

<a id="create-resource-init-bundle_init-bundle-cloud-ocp-apply"></a>

# Applying the init bundle on the secured cluster

Before you configure a secured cluster, you must apply the init bundle to the secured cluster. Applying the init bundle allows the services on the secured cluster to communicate with RHACS Cloud Service.

> [!NOTE]
> If you are installing by using Helm charts, do not perform this step. Complete the installation by using Helm.

<div>

<div class="title">

Prerequisites

</div>

- You must have generated an init bundle containing secrets. The preferred way to set up a secured cluster is by using a CRS.

- You must have created the `stackrox` project, or namespace, on the cluster where you will install secured cluster services. Using `stackrox` for the project is not required, but ensures that vulnerabilities for RHACS processes are not reported when scanning your clusters.

</div>

<div>

<div class="title">

Procedure

</div>

- Create resources using the OpenShift Container Platform web console:

  1.  In the OpenShift Container Platform web console, make sure that you are in the `stackrox` namespace.

  2.  In the top menu, click **+** to open the **Import YAML** page.

  3.  You can drag the init bundle file or copy and paste its contents into the editor, and then click **Create**. When the command is complete, the display shows that the `collector-tls`, `sensor-tls`, and `admission-control-tls` resources were created.

- Create resources using the Red Hat OpenShift CLI: Using the Red Hat OpenShift CLI, run the following command to create the resources:

  ``` terminal
  $ oc create -f <init_bundle.yaml> \
    -n <stackrox>
  ```

  where:

  `<init_bundle.yaml>`  
  Specifies the file name of the init bundle containing the secrets.

  `<stackrox>`  
  Specifies the name of the project where Central services are installed.

</div>

<div>

<div class="title">

Verification

</div>

- Restart Sensor to pick up the new certificates.

  For more information about how to restart Sensor, see "Restarting the Sensor container".

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing RHACS Cloud Service on secured clusters by using Helm charts](install-secured-cluster-cloud-ocp.md#installing-sc-helm-cloud-ocp_install-secured-cluster-cloud-ocp)

</div>

<a id="next-steps_init-bundle-cloud-ocp-apply"></a>

# Next steps

After applying the cluster registration secret or init bundle, complete the installation by installing the RHACS Operator and secured cluster services.

- On each Red Hat OpenShift cluster, install the RHACS Operator.

- Install RHACS secured cluster services in all clusters that you want to monitor.

<a id="additional-resources_init-bundle-cloud-ocp-apply"></a>

# Additional resources

- [Installing the RHACS Operator](cloud-install-operator.md)

- [Restarting the Sensor container](../../configuration/add-custom-certificates.md#restart-sensor_add-custom-cert)
