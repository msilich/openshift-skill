<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) provides the ability to audit the processes that are listening on ports in your secured clusters and filter this data by deployment, namespace, or cluster.

<a id="audit-listening-endpoints-overview_audit-listening-endpoints"></a>

# Listening endpoints overview

You can view information about processes and the ports that they are listening on by using the RHACS web portal or the API.

Use one of the following methods:

- In the RHACS web portal, go to **Network** → **Listening Endpoints**.

- Connect to the `ListeningEndpointsService` object in the API. For more information on the API, go to **Help** → **API reference** in the RHACS web portal.

The page provides a list of processes by deployment, with the following information displayed for each process on the list:

- Deployment name

- Cluster

- Namespace

- Count, or the number of processes listening on the ports in the deployment

You can further filter the information displayed on the page by using the filter field and entering individual deployments, namespaces, and clusters.

Click the expand icon at the top of the list to expand all sections for all deployments listed, or click the expand icon on a single deployment line to view additional information about that deployment. The expanded view displays the following information:

- Exec file path: Location of the process

- PID: System ID of the process

- Port: Port on which the process is listening

- Protocol: Protocol in use by the process

- Pod ID: Name of the pod that contains the process

- Container name: Name of the container that runs the listening process

Clicking on a deployment name brings you to the **Risk** page in the RHACS web portal, where you can view information about the deployment, including risk indicators such as policy violations and additional deployment details.
