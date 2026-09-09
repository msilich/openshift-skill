<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After installing RHACS Cloud Service, you can perform some steps to verify that the installation was successful.

<a id="verifying-installation-secured-clusters-cloud_verify-installation-cloud-ocp"></a>

# Verifying installation of secured clusters

After installing RHACS Cloud Service, you can verify that the installation was successful by accessing your ACS Console and checking the Dashboard.

To verify installation, access your ACS Console from the Red Hat Hybrid Cloud Console. The Dashboard displays the number of clusters that RHACS Cloud Service is monitoring, along with information about nodes, deployments, images, and violations.

<div>

<div class="title">

Additional resources

</div>

- [Installing secured cluster resources from RHACS Cloud Service](install-secured-cluster-cloud-ocp.md#installing-sc-operator-cloud-ocp_install-secured-cluster-cloud-ocp)

</div>

<a id="troubleshooting-verification-secured-clusters-cloud_verify-installation-cloud-ocp"></a>

## Troubleshooting verification

If no data is displayed in the ACS Console after installation, you can perform the following troubleshooting steps.

- Ensure that at least one secured cluster connects to your RHACS Cloud Service instance.

- Examine your Sensor pod logs to ensure that the connection to your RHACS Cloud Service instance is successful.

- In the Red Hat OpenShift cluster, go to **Platform Configuration** → **Clusters** to verify that the components are healthy and to view additional operational information.

- Examine the values in the `SecuredCluster` API in the Operator on your local cluster to ensure that you entered the **Central API Endpoint** correctly. This value should be the same value as shown in the **ACS instance** details in the Red Hat Hybrid Cloud Console.
