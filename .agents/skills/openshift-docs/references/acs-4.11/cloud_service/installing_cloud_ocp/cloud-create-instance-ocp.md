<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Access Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service) by selecting an instance in the Red Hat Hybrid Cloud Console. An *ACS instance* contains the RHACS Cloud Service management interface and services that Red Hat configures and manages for you. The management interface connects to your secured clusters, which contain the services that scan and collect information about vulnerabilities. One instance can connect to and monitor many clusters.

<a id="cloud-create-instance-steps_cloud-create-instance-ocp"></a>

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

<a id="cloud-create-instance-ocp-next-steps_cloud-create-instance-ocp"></a>

# Next steps

After creating an ACS instance, you need to prepare your Red Hat OpenShift clusters for securing.

On each Red Hat OpenShift cluster you want to secure, create a project named `stackrox`. This project will contain the resources for RHACS Cloud Service secured clusters.

<div>

<div class="title">

Additional resources

</div>

- [Create a project named stackrox](cloud-ocp-create-project.md)

</div>
