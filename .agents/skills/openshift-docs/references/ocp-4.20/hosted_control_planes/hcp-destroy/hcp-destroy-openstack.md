<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You might want to remove a hosted cluster if you are no longer using it, you are trying to reduce resources, or the hosted cluster is experiencing issues that are difficult to resolve.

# Destroying a hosted cluster by using the CLI

You can destroy a hosted cluster and its associated resources on Red Hat OpenStack Platform (RHOSP) by using the `hcp` CLI tool.

<div>

<div class="title">

Prerequisites

</div>

- You installed the hosted control planes CLI, `hcp`.

</div>

<div>

<div class="title">

Procedure

</div>

- To destroy the cluster and its associated resources, run the following command:

  ``` terminal
  $ hcp destroy cluster openstack --name=<cluster_name>
  ```

  Replace `<cluster_name>` with the name of the hosted cluster.

  After the process completes, your cluster and all resources that are associated with it are destroyed.

</div>
