<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Create a project on each Red Hat OpenShift cluster that you want to secure. You then use this project to install RHACS Cloud Service resources by using the Operator or Helm charts.

<a id="cloud-ocp-create-stackrox-project_cloud-ocp-create-project"></a>

# Creating a project on your cluster

You must create a project named `stackrox` on your OpenShift Container Platform cluster to install RHACS Cloud Service resources.

<div>

<div class="title">

Procedure

</div>

- In your OpenShift Container Platform cluster, go to **Home** → **Projects** and create a project for RHACS Cloud Service. Use `stackrox` as the project **Name**.

</div>

<a id="next-steps_cloud-ocp-create-project"></a>

# Next steps

After creating the project on your secured cluster, generate the secrets required for secure communication between the secured cluster and Central.

In the ACS Console, generate a cluster registration secret or an init bundle. These files contain the secrets that set up the initial secured communication between RHACS Cloud Service secured clusters and Central.

<div>

<div class="title">

Additional resources

</div>

- [Generating a cluster registration secret or an init bundle](init-bundle-cloud-ocp-generate.md)

</div>
