<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Apply the cluster registration secret (CRS) or the init bundle to the secured cluster.

<a id="create-resource-init-bundle_init-bundle-cloud-other-apply"></a>

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

- Using the `kubectl` CLI, run the following commands to create the resources:

  ``` terminal
  $ kubectl create namespace stackrox
  ```

  This command creates the project where secured cluster resources will be installed. This example uses `stackrox`.

  ``` terminal
  $ kubectl create -f <init_bundle.yaml> \
    -n <stackrox>
  ```

  where:

  `<init_bundle.yaml>`  
  Specifies the file name of the init bundle containing the secrets.

  `<stackrox>`  
  Specifies the project name that you created. This example uses `stackrox`.

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

- [Installing RHACS Cloud Service on secured clusters by using Helm charts](install-secured-cluster-cloud-other.md#installing-sc-helm-cloud-other_install-secured-cluster-cloud-other)

</div>

<a id="next-steps_init-bundle-cloud-other-apply"></a>

# Next steps

After applying the init bundle, complete the installation by installing RHACS secured cluster services.

- Install RHACS secured cluster services in all clusters that you want to monitor.

<a id="additional-resources_init-bundle-cloud-other-apply"></a>

# Additional resources

- [Restarting the Sensor container](../../configuration/add-custom-certificates.md#restart-sensor_add-custom-cert)
