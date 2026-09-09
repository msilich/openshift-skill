<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can upgrade your secured clusters in RHACS Cloud Service by using Helm charts.

If you installed RHACS secured clusters by using Helm charts, you can upgrade to the latest version of RHACS by updating the Helm chart and running the `helm upgrade` command.

<a id="updating-helm-repository_upgrade-cloudsvc-helm"></a>

# Updating the Helm chart repository

You must always update Helm charts before upgrading to a new version of Red Hat Advanced Cluster Security for Kubernetes.

<div>

<div class="title">

Prerequisites

</div>

- You must have already added the Red Hat Advanced Cluster Security for Kubernetes Helm chart repository.

- You must be using Helm version 3.8.3 or newer.

</div>

<div>

<div class="title">

Procedure

</div>

- Update Red Hat Advanced Cluster Security for Kubernetes charts repository.

  ``` terminal
  $ helm repo update
  ```

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

<a id="upgrade-helm-chart_upgrade-cloudsvc-helm"></a>

# Running the Helm upgrade command

You can use the `helm upgrade` command to update Red Hat Advanced Cluster Security for Kubernetes (RHACS).

<div>

<div class="title">

Prerequisites

</div>

- You must have access to the `values-private.yaml` configuration file that you have used to install Red Hat Advanced Cluster Security for Kubernetes (RHACS). Otherwise, you must generate the `values-private.yaml` configuration file containing root certificates before proceeding with these commands.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the helm upgrade command and specify the configuration files by using the `-f` option:

  ``` terminal
  $ helm upgrade -n stackrox stackrox-secured-cluster-services \
    rhacs/secured-cluster-services --version <current_rhacs_version> \
    -f values-private.yaml
  ```

</div>

<a id="_additional_resources"></a>

# Additional resources

- [Installing RHACS Cloud Service on secured clusters by using Helm charts](../installing_cloud_ocp/install-secured-cluster-cloud-ocp.md#installing-sc-helm-cloud-ocp_install-secured-cluster-cloud-ocp)
