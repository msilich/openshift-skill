<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After installing RHACS Cloud Service, you can verify that the installation was successful by accessing the ACS Console and reviewing cluster monitoring data.

<a id="verify-installation-cloud-other-procedure_verify-installation-cloud-other"></a>

# Verifying installation by accessing the ACS Console

You can verify that RHACS Cloud Service is successfully installed by accessing the ACS Console and checking the Dashboard for cluster monitoring data.

<div>

<div class="title">

Procedure

</div>

1.  Access your ACS Console from the Red Hat Hybrid Cloud Console.

2.  Review the Dashboard, which displays the number of clusters that RHACS Cloud Service is monitoring, along with information about nodes, deployments, images, and violations.

    If no data is displayed in the ACS Console, perform the following troubleshooting steps:

    - Ensure that at least one secured cluster connects to your RHACS Cloud Service instance. For more information, see the instructions for installing by using Helm charts or by using the `roxctl` CLI.

    - Examine your Sensor pod logs to ensure that the connection to your RHACS Cloud Service instance is successful.

    - Examine the values in the `SecuredCluster` API in the Operator on your local cluster to ensure that you entered the **Central API Endpoint** correctly. This value should be the same value as shown in the **ACS instance** details in the Red Hat Hybrid Cloud Console.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing RHACS Cloud Service on secured clusters by using Helm charts](../installing_cloud_ocp/install-secured-cluster-cloud-ocp.md#installing-sc-helm-cloud-ocp_install-secured-cluster-cloud-ocp)

- [Installing RHACS Cloud Service on secured clusters by using the roxctl CLI](../installing_cloud_ocp/install-secured-cluster-cloud-ocp.md#installing-sc-roxctl-cloud-ocp_install-secured-cluster-cloud-ocp)

</div>
