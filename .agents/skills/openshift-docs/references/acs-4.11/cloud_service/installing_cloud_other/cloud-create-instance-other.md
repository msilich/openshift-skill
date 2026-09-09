<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Access Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service) by selecting an instance in the Red Hat Hybrid Cloud Console. An **ACS instance** contains the RHACS Cloud Service management interface and services that Red Hat configures and manages for you. The management interface connects to your secured clusters, which contain the services that scan and collect information about vulnerabilities. One instance can connect to and monitor many clusters.

<a id="cloud-create-instance-steps_cloud-create-instance-other"></a>

# Creating an instance in the console

In the Red Hat Hybrid Cloud Console, create an ACS instance to connect to your secured clusters.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the Red Hat Hybrid Cloud Console.

2.  From the navigation menu, select **Advanced Cluster Security** → **ACS Instances**.

3.  Select **Create ACS instance** and enter information into the displayed fields or select the appropriate option from the drop-down list:

    - **Name**: Enter the name of your ACS instance. An *ACS instance* contains the RHACS Central component, also referred to as "Central", which includes the RHACS Cloud Service management interface and services that Red Hat configures and manages for you. You manage your secured clusters that communicate with Central. You can connect many secured clusters to one instance.

    - **Cloud provider**: Select the cloud provider that hosts Central. Use the default value (**AWS**).

    - **Cloud region**: The region for your cloud provider that hosts Central. Select one of the following regions:

      - US-East, N. Virginia

      - Europe, Ireland

    - **Availability zones**: Use the default value (**Multi**).

4.  Click **Create instance**.

</div>

<a id="next-steps_cloud-create-instance-other"></a>

# Next steps

After creating the instance, install secured cluster resources on each Kubernetes cluster that you want to secure.

- On each Kubernetes cluster that you want to secure, install secured cluster resources by using Helm charts or the `roxctl` CLI.

<div>

<div class="title">

Additional resources

</div>

- [Installing secured cluster resources](install-secured-cluster-cloud-other.md)

</div>
