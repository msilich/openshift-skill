> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/mce_troubleshooting/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="troubleshooting-mce"></a>

# Troubleshooting

Before using the Troubleshooting guide, you can run the `oc adm must-gather` command to gather details, logs, and take steps in debugging issues. For more details, see [Running the must-gather command to troubleshoot](mce_troubleshooting.md#running-the-must-gather-command-to-troubleshoot-mce).

Additionally, check your role-based access. See [multicluster engine operator Role-based access control](clusters.md#mce-rbac) for details.

<div>

<div class="title">

Procedure

</div>

- Documented troubleshooting

  View the list of troubleshooting topics for the multicluster engine operator:

  **Installation:**

  To view the main documentation for the installing tasks, see [Get started with multicluster engine operator](clusters.md#get-started-mce).

- [Troubleshooting installation status stuck in installing or pending](mce_troubleshooting.md#troubleshooting-stuck-pending-mce)

- [Troubleshooting reinstallation failure](mce_troubleshooting.md#troubleshooting-reinstallation-failure-mce)

  **Cluster management:**

  To view the main documentation about managing your clusters, see [Cluster lifecycle introduction](clusters.md#cluster-intro).

- [Troubleshooting adding day-two nodes to an existing cluster fails with pending user action](mce_troubleshooting.md#troubleshooting-network-config-fail)

- [Troubleshooting an offline cluster](mce_troubleshooting.md#troubleshooting-an-offline-cluster-mce)

- [Troubleshooting a managed cluster import failure](mce_troubleshooting.md#troubleshooting-a-managed-cluster-import-failure-mce)

- [Reimporting cluster fails with unknown authority error](mce_troubleshooting.md#troubleshooting-cluster-reimport-kubeconfig-mce)

- [Troubleshooting cluster with pending import status](mce_troubleshooting.md#troubleshooting-cluster-with-pending-import-status-mce)

- [Troubleshooting imported clusters offline after certificate change](mce_troubleshooting.md#troubleshooting-imported-clusters-offline-after-certificate-change-mce)

- [Troubleshooting cluster status changing from offline to available](mce_troubleshooting.md#troubleshooting-cluster-status-offline-available-mce)

- [Troubleshooting cluster creation on VMware vSphere](mce_troubleshooting.md#troubleshooting-cluster-creation-on-vmware-vsphere-mce)

- [Troubleshooting cluster in console with pending or failed status](mce_troubleshooting.md#troubleshooting-cluster-in-console-with-pending-or-failed-status-mce)

- [Troubleshooting Klusterlet with degraded conditions](mce_troubleshooting.md#troubleshooting-klusterlet-with-degraded-conditions-mce)

- [Troubleshooting namespace that remains after deleting a cluster](mce_troubleshooting.md#trouble-cluster-remove-namespace-mce)

- [Auto-import-secret-exists error when importing a cluster](mce_troubleshooting.md#trouble-auto-import-secret-exists-mce)

- [Troubleshooting no PlacementDecision after creating Placement](mce_troubleshooting.md#troubleshooting-no-placementdecision-mce)

- [Troubleshooting a discovery failure of bare metal hosts on Dell hardware](mce_troubleshooting.md#troubleshooting-idrac-discovery-fails-mce)

- [Troubleshooting Minimal ISO boot failures](mce_troubleshooting.md#trouble-min-iso-boot)

- [Troubleshooting managed clusters *Unknown* on Red Hat OpenShift Service on AWS (classic) with hosted control planes cluster](mce_troubleshooting.md#trouble-unknown-status-rosa-hcp)

- [Troubleshooting an attempt to update managed cluster with missing OpenShift Container Platform version](mce_troubleshooting.md#update-managed-missing-ocp)

- [Troubleshooting certificate authority update error on Hive and Assisted Installer clusters](mce_troubleshooting.md#ca-update-error-hive-ai)

- [Troubleshooting: Missing `open-cluster-management-global-set` namespace](mce_troubleshooting.md#trouble-miss-namespace)

</div>

<a id="running-the-must-gather-command-to-troubleshoot-mce"></a>

## Running the must-gather command to troubleshoot

To get started with troubleshooting, learn about the troubleshooting scenarios for users to run the `must-gather` command to debug the issues, then see the procedures to start using the command.

**Required access:** Cluster administrator

<div>

<div class="title">

Procedure

</div>

- Must-gather scenarios

- **Scenario one:** Use the *Documented troubleshooting* section to see if a solution to your problem is documented. The guide is organized by the major functions of the product.

  With this scenario, you check the guide to see if your solution is in the documentation.

- **Scenario two:** If your problem is not documented with steps to resolve, run the `must-gather` command and use the output to debug the issue.

- **Scenario three:** If you cannot debug the issue using your output from the `must-gather` command, then share your output with Red Hat Support.

- Must-gather procedure

  See the following procedure to start using the `must-gather` command:

  1.  Learn about the `must-gather` command and install the prerequisites that you need at [Gathering data about your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/support/support-overview#support-overview-gather-data-cluster) in the OpenShift Container Platform documentation.

  2.  Log in to your cluster. For the usual use-case, you should run the `must-gather` while you are logged into your *engine* cluster.

      **Note:** If you want to check your managed clusters, find the `gather-managed.log` file that is located in the `cluster-scoped-resources` directory:

          <your-directory>/cluster-scoped-resources/gather-managed.log>

      Check for managed clusters that are not set `True` for the JOINED and AVAILABLE column. You can run the `must-gather` command on those clusters that are not connected with `True` status.

  3.  Add the multicluster engine for Kubernetes image that is used for gathering data and the directory. Run the following command:

          oc adm must-gather --image=registry.redhat.io/multicluster-engine/must-gather-rhel9:v2.17 --dest-dir=<directory>

  4.  Go to your specified directory to see your output, which is organized in the following levels:

      - Two peer levels: `cluster-scoped-resources` and `namespace` resources.

      - Sub-level for each: API group for the custom resource definitions for both cluster-scope and namespace-scoped resources.

      - Next level for each: YAML file sorted by `kind`.

- Must-gather in a disconnected environment

  Complete the following steps to run the `must-gather` command in a disconnected environment:

  1.  In a disconnected environment, mirror the Red Hat operator catalog images into their mirror registry. For more information, see [Install on disconnected networks](clusters.md#install-on-disconnected-networks).

  2.  Run the following command to extract logs, which reference the image from their mirror registry. Replace `sha256` with the current image:

          REGISTRY=registry.example.com:5000
          IMAGE=$REGISTRY/multicluster-engine/must-gather-rhel9@sha256:ff9f37eb400dc1f7d07a9b6f2da9064992934b69847d17f59e385783c071b9d8>

          oc adm must-gather --image=$IMAGE --dest-dir=./data

  You can open a Jira bug for the product team [here](https://issues.redhat.com/projects/ACM/summary/).

</div>

<a id="troubleshooting-network-config-fail"></a>

## Troubleshooting: Adding day-two nodes to an existing cluster fails with pending user action

Adding a node, or scaling out, to your existing cluster that is created by the multicluster engine for Kubernetes operator with Zero Touch Provisioning or Host inventory create methods fails during installation. The installation process works correctly during the Discovery phase, but fails on the installation phase.

The configuration of the network is failing. From the hub cluster in the integrated console, you see a `Pending` user action. In the description, you can see it failing on the rebooting step.

The error message about failing is not very accurate, since the agent that is running in the installing host cannot report information.

<div>

<div class="title">

Procedure

</div>

- Symptom: Installation for day two workers fails

  After the Discover phase, the host reboots to continue the installation, but it cannot configure the network. Check for the following symptoms and messages:

- From the hub cluster in the integrated console, check for `Pending` user action on the adding node, with the `Rebooting` indicator:

      This host is pending user action. Host timed out when pulling ignition. Check the host console... Rebooting

- From the Red Hat OpenShift Container Platform configuration managed cluster, check the `MachineConfigs` of the existing cluster. Check if any of the `MachineConfigs` create any file on the following directories:

  - `/sysroot/etc/NetworkManager/system-connections/`

  - `/sysroot/etc/sysconfig/network-scripts/`

- From the terminal of the installing host, check the failing host for the following messages. You can use `journalctl` to see the log messages:

      info: networking config is defined in the real root

      info: will not attempt to propagate initramfs networking

  If you get the last message in the log, the networking configuration is not propagated because it already found an existing network configuration on the folders previously listed in the *Symptom*.

- Resolving the problem: Recreate the node merging network configuration

  Perform the following task to use a proper network configuration during the installation:

  1.  Delete the node from your hub cluster.

  2.  Repeat your previous process to install the node in the same way.

  3.  Create the `BareMetalHost` object of the node with the following annotation:

      ``` bash
      "bmac.agent-install.openshift.io/installer-args": "[\"--append-karg\", \"coreos.force_persist_ip\"]"
      ```

  The node starts the installation. After the Discovery phase, the node merges the network configuration between the changes on the existing cluster and the initial configuration.

</div>

<a id="troubleshooting-destroy-cluster-fail"></a>

## Troubleshooting deletion failure of a hosted control plane cluster on the Agent platform

When you destroy a hosted control plane cluster on the Agent platform, all the back-end resources are normally deleted. If the machine resources are not deleted properly, a cluster deletion fails. In that case, you must manually remove the remaining machine resources.

<div>

<div class="title">

Procedure

</div>

- Symptom: An error occurs when destroying a hosted control plane cluster

  After you attempt to destroy the hosted control plane cluster on the Agent platform, the `hcp destroy` command fails with the following error:

      2024-02-22T09:56:19-05:00    ERROR    HostedCluster deletion failed    {"namespace": "clusters", "name": "hosted-0", "error": "context deadline exceeded"}
      2024-02-22T09:56:19-05:00    ERROR    Failed to destroy cluster    {"error": "context deadline exceeded"}

- Resolving the problem: Remove the remaining machine resources manually

  Complete the following steps to destroy a hosted control plane cluster successfully on the Agent platform:

  1.  Run the following command to see the list of remaining machine resources by replacing `<hosted_cluster_namespace>` with the name of hosted cluster namespace:

          oc get machine -n <hosted_cluster_namespace>

      See the following example output:

          NAMESPACE           NAME             CLUSTER          NODENAME   PROVIDERID   PHASE      AGE   VERSION
          clusters-hosted-0   hosted-0-9gg8b   hosted-0-nhdbp                           Deleting   10h   <4.x.0>-rc.8

  2.  Run the following command to remove the `machine.cluster.x-k8s.io` finalizer attached to machine resources:

          oc edit machines -n <hosted_cluster_namespace>

  3.  Run the following command to verify you receive the `No resources found` message on your terminal:

          oc get agentmachine -n <hosted_cluster_namespace>

  4.  Run the following command to destroy a hosted control plane cluster on the Agent platform:

          hcp destroy cluster agent --name <cluster_name>

  Replace `<cluster_name>` with the name of your cluster.

</div>

<a id="troubleshooting-stuck-pending-mce"></a>

## Troubleshooting installation status stuck in installing or pending

When installing the multicluster engine operator, the `MultiClusterEngine` remains in `Installing` phase, or multiple pods maintain a `Pending` status.

<div>

<div class="title">

Procedure

</div>

- Symptom: Stuck in Pending status

  More than ten minutes passed since you installed `MultiClusterEngine` and one or more components from the `status.components` field of the `MultiClusterEngine` resource report `ProgressDeadlineExceeded`. Resource constraints on the cluster might be the issue.

  Check the pods in the namespace where `MultiClusterEngine` was installed. You might see `Pending` with a status similar to the following:

      reason: Unschedulable
      message: '0/6 nodes are available: 3 Insufficient cpu, 3 node(s) had taint {node-role.kubernetes.io/master:
              }, that the pod didn't tolerate.'

  In this case, the worker nodes resources are not sufficient in the cluster to run the product.

- Resolving the problem: Adjust worker node sizing

  If you have this problem, then your cluster needs to be updated with either larger or more worker nodes. See [Sizing your cluster](get_started.md) for guidelines on sizing your cluster.

</div>

<a id="troubleshooting-reinstallation-failure-mce"></a>

## Troubleshooting reinstallation failure

When reinstalling multicluster engine operator, the pods do not start.

<div>

<div class="title">

Procedure

</div>

- Symptom: Reinstallation failure

  If your pods do not start after you install the multicluster engine operator, it is often because items from a previous installation of multicluster engine operator were not removed correctly when it was uninstalled.

  In this case, the pods do not start after completing the installation process.

- Resolving the problem: Reinstallation failure

  If you have this problem, complete the following steps:

  1.  Run the uninstallation process to remove the current components by following the steps in [Uninstalling](clusters.md#uninstalling-mce).

  2.  Ensure that your Red Hat OpenShift Container Platform CLI is configured to run `oc` commands. See [Getting started with the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started) in the OpenShift Container Platform documentation for more information about how to configure the `oc` commands.

  3.  Copy the following script into a file, replacing the `<namespace>` value in the script with the name of the namespace where you previously installed multicluster engine operator.

      **Important:** Ensure that you specify the correct namespace because the namespace is also cleaned out and deleted when you run the script.

  ``` bash
  MCE_NAMESPACE=<namespace>
  oc delete multiclusterengine --all
  oc delete apiservice v1.admission.cluster.open-cluster-management.io v1.admission.work.open-cluster-management.io
  oc delete crd discoveredclusters.discovery.open-cluster-management.io discoveryconfigs.discovery.open-cluster-management.io
  oc delete mutatingwebhookconfiguration ocm-mutating-webhook managedclustermutators.admission.cluster.open-cluster-management.io
  oc delete validatingwebhookconfiguration ocm-validating-webhook
  oc delete ns $MCE_NAMESPACE
  ```

  1.  Run the script. When you receive a message that no resources were found, then you can proceed with the installation.

  2.  Run the installation. See [Installing while connected online](clusters.md#installing-while-connected-online-mce).

</div>

<a id="troubleshooting-an-offline-cluster-mce"></a>

## Troubleshooting an offline cluster

There are a few common causes for a cluster showing an offline status.

<div>

<div class="title">

Procedure

</div>

- Symptom: Cluster status is offline

  After you complete the procedure for creating a cluster, you cannot access it from the Red Hat Advanced Cluster Management console, and it shows a status of `offline`.

- Resolving the problem: Cluster status is offline

  1.  Determine if the managed cluster is available. You can check this in the *Clusters* area of the Red Hat Advanced Cluster Management console.

      If it is not available, try restarting the managed cluster.

  2.  If the managed cluster status is still offline, complete the following steps:

      1.  Run the `oc get managedcluster <cluster_name> -o yaml` command on the hub cluster. Replace `<cluster_name>` with the name of your cluster.

      2.  Find the `status.conditions` section.

      3.  Check the messages for `type: ManagedClusterConditionAvailable` and resolve any problems.

</div>

<a id="troubleshooting-a-managed-cluster-import-failure-mce"></a>

## Troubleshooting a managed cluster import failure

If your cluster import fails, there are a few steps that you can take to determine why the cluster import failed.

<div>

<div class="title">

Procedure

</div>

- Symptom: Imported cluster not available

  After you complete the procedure for importing a cluster, you cannot access it from the console.

- Resolving the problem: Imported cluster not available

  There can be a few reasons why an imported cluster is not available after an attempt to import it. If the cluster import fails, complete the following steps, until you find the reason for the failed import:

  1.  On the hub cluster, run the following command to ensure that the import controller is running.

          kubectl -n multicluster-engine get pods -l app=managedcluster-import-controller-v2

      You should see two pods that are running. If either of the pods is not running, run the following command to view the log to determine the reason:

          kubectl -n multicluster-engine logs -l app=managedcluster-import-controller-v2 --tail=-1

  2.  On the hub cluster, run the following command to determine if the managed cluster import secret was generated successfully by the import controller:

          kubectl -n <managed_cluster_name> get secrets <managed_cluster_name>-import

      If the import secret does not exist, run the following command to view the log entries for the import controller and determine why it was not created:

          kubectl -n multicluster-engine logs -l app=managedcluster-import-controller-v2 --tail=-1 | grep importconfig-controller

  3.  On the hub cluster, if your managed cluster is the `local-cluster`, provisioned by Hive, or has an auto-import secret, run the following command to check the import status of the managed cluster.

          kubectl get managedcluster <managed_cluster_name> -o=jsonpath='{range .status.conditions[*]}{.type}{"\t"}{.status}{"\t"}{.message}{"\n"}{end}' | grep ManagedClusterImportSucceeded

      If the condition `ManagedClusterImportSucceeded` is not `true`, the result of the command indicates the reason for the failure.

  4.  Check the Klusterlet status of the managed cluster for a degraded condition. See [Troubleshooting Klusterlet with degraded conditions](mce_troubleshooting.md#troubleshooting-klusterlet-with-degraded-conditions-mce) to find the reason that the Klusterlet is degraded.

</div>

<a id="troubleshooting-cluster-reimport-kubeconfig-mce"></a>

## Reimporting cluster fails with unknown authority error

If you experience a problem when reimporting a managed cluster to your multicluster engine operator hub cluster, follow the procedure to troubleshoot the problem.

<div>

<div class="title">

Procedure

</div>

- Symptom: Reimporting cluster fails with unknown authority error

  After you provision an OpenShift Container Platform cluster with multicluster engine operator, reimporting the cluster might fail with a `x509: certificate signed by unknown authority` error when you change or add API server certificates to your OpenShift Container Platform cluster.

- Identifying the problem: Reimporting cluster fails with unknown authority error

  After failing to reimport your managed cluster, run the following command to get the import controller log on your multicluster engine operator hub cluster:

      kubectl -n multicluster-engine logs -l app=managedcluster-import-controller-v2 -f

  If the following error log appears, your managed cluster API server certificates might have changed:

  `ERROR Reconciler error {"controller": "clusterdeployment-controller", "object": {"name":"awscluster1","namespace":"awscluster1"}, "namespace": "awscluster1", "name": "awscluster1", "reconcileID": "a2cccf24-2547-4e26-95fb-f258a6710d80", "error": "Get \"https://api.awscluster1.dev04.red-chesterfield.com:6443/api?timeout=32s\": x509: certificate signed by unknown authority"}`

  To determine if your managed cluster API server certificates have changed, complete the following steps:

  1.  Run the following command to specify your managed cluster name by replacing `your-managed-cluster-name` with the name of your managed cluster:

          cluster_name=<your-managed-cluster-name>

  2.  Get your managed cluster `kubeconfig` secret name by running the following command:

          kubeconfig_secret_name=$(oc -n ${cluster_name} get clusterdeployments ${cluster_name} -ojsonpath='{.spec.clusterMetadata.adminKubeconfigSecretRef.name}')

  3.  Export `kubeconfig` to a new file by running the following commands:

          oc -n ${cluster_name} get secret ${kubeconfig_secret_name} -ojsonpath={.data.kubeconfig} | base64 -d > kubeconfig.old

      <!-- Separate adjacent source examples. -->

          export KUBECONFIG=kubeconfig.old

  4.  Get the namespace from your managed cluster with `kubeconfig` by running the following command:

          oc get ns

      If you receive an error that resembles the following message, your cluster API server ceritificates have been changed and your `kubeconfig` file is invalid.

  `Unable to connect to the server: x509: certificate signed by unknown authority`

- Resolving the problem: Reimporting cluster fails with unknown authority error

  The managed cluster administrator must create a new valid `kubeconfig` file for your managed cluster.

  After creating a new `kubeconfig`, complete the following steps to update the new `kubeconfig` for your managed cluster:

  1.  Run the following commands to set your `kubeconfig` file path and cluster name. Replace `<path_to_kubeconfig>` with the path to your new `kubeconfig` file. Replace `<managed_cluster_name>` with the name of your managed cluster:

          cluster_name=<managed_cluster_name>
          kubeconfig_file=<path_to_kubeconfig>

  2.  Run the following command to encode your new `kubeconfig`:

          kubeconfig=$(cat ${kubeconfig_file} | base64 -w0)

      **Note:** On macOS, run the following command instead:

          kubeconfig=$(cat ${kubeconfig_file} | base64)

  3.  Run the following command to define the `kubeconfig` json patch:

          kubeconfig_patch="[\{\"op\":\"replace\", \"path\":\"/data/kubeconfig\", \"value\":\"${kubeconfig}\"}, \{\"op\":\"replace\", \"path\":\"/data/raw-kubeconfig\", \"value\":\"${kubeconfig}\"}]"

  4.  Retrieve your administrator `kubeconfig` secret name from your managed cluster by running the following command:

          kubeconfig_secret_name=$(oc -n ${cluster_name} get clusterdeployments ${cluster_name} -ojsonpath='{.spec.clusterMetadata.adminKubeconfigSecretRef.name}')

  5.  Patch your administrator `kubeconfig` secret with your new `kubeconfig` by running the following command:

          oc -n ${cluster_name} patch secrets ${kubeconfig_secret_name} --type='json' -p="${kubeconfig_patch}"

</div>

<a id="troubleshooting-cluster-with-pending-import-status-mce"></a>

## Troubleshooting cluster with pending import status

If you receive *Pending import* continually on the console of your cluster, follow the procedure to troubleshoot the problem.

<div>

<div class="title">

Procedure

</div>

- Symptom: Cluster with pending import status

  After importing a cluster by using the Red Hat Advanced Cluster Management console, the cluster appears in the console with a status of *Pending import*.

- Identifying the problem: Cluster with pending import status

  1.  Run the following command on the managed cluster to view the Kubernetes pod names that are having the issue:

          kubectl get pod -n open-cluster-management-agent | grep klusterlet-agent

  2.  Run the following command on the managed cluster to find the log entry for the error:

  <!-- -->

      kubectl logs <klusterlet_agent_pod> -n open-cluster-management-agent

  \+ Replace *registration_agent_pod* with the pod name that you identified in step 1.

  1.  Search the returned results for text that indicates there was a networking connectivity problem.

      Example includes: `no such host`.

- Resolving the problem: Cluster with pending import status

  1.  Retrieve the port number that is having the problem by entering the following command on the hub cluster:

          oc get infrastructure cluster -o yaml | grep apiServerURL

  2.  Ensure that the hostname from the managed cluster can be resolved, and that outbound connectivity to the host and port is occurring.

      If the communication cannot be established by the managed cluster, the cluster import is not complete.

      The cluster status for the managed cluster is *Pending import*.

</div>

<a id="troubleshooting-imported-clusters-offline-after-certificate-change-mce"></a>

## Troubleshooting imported clusters offline after certificate change

Installing a custom `apiserver` certificate is supported, but one or more clusters that were imported before you changed the certificate information can have an `offline` status.

<div>

<div class="title">

Procedure

</div>

- Symptom: Clusters offline after certificate change

  After you complete the procedure for updating a certificate secret, one or more of your clusters that were online are now displaying an `offline` status in the console.

- Identifying the problem: Clusters offline after certificate change

  After updating the information for a custom API server certificate, clusters that were imported and running before the new certificate are now in an `offline` state.

  The errors that indicate that the certificate is the problem are found in the logs for the pods in the `open-cluster-management-agent` namespace of the offline managed cluster. The following examples are similar to the errors that are displayed in the logs:

  See the following `klusterlet-agent` log:

      E0917 02:58:26.315984       1 reflector.go:127] k8s.io/client-go@v0.19.0/tools/cache/reflector.go:156: Failed to watch *v1beta1.CertificateSigningRequest: Get "https://api.aaa-ocp.dev02.location.com:6443/apis/cluster.management.io/v1/managedclusters?allowWatchBookmarks=true&fieldSelector=metadata.name%3Dtest-1&resourceVersion=607408&timeout=9m33s&timeoutSeconds=573&watch=true"": x509: certificate signed by unknown authority
      E0917 02:58:26.598343       1 reflector.go:127] k8s.io/client-go@v0.19.0/tools/cache/reflector.go:156: Failed to watch *v1.ManagedCluster: Get "https://api.aaa-ocp.dev02.location.com:6443/apis/cluster.management.io/v1/managedclusters?allowWatchBookmarks=true&fieldSelector=metadata.name%3Dtest-1&resourceVersion=607408&timeout=9m33s&timeoutSeconds=573&watch=true": x509: certificate signed by unknown authority
      E0917 02:58:27.613963       1 reflector.go:127] k8s.io/client-go@v0.19.0/tools/cache/reflector.go:156: Failed to watch *v1.ManagedCluster: failed to list *v1.ManagedCluster: Get "https://api.aaa-ocp.dev02.location.com:6443/apis/cluster.management.io/v1/managedclusters?allowWatchBookmarks=true&fieldSelector=metadata.name%3Dtest-1&resourceVersion=607408&timeout=9m33s&timeoutSeconds=573&watch=true"": x509: certificate signed by unknown authority
      E0917 03:04:05.874759       1 manifestwork_controller.go:179] Reconcile work test-1-klusterlet-addon-workmgr fails with err: Failed to update work status with err Get "https://api.aaa-ocp.dev02.location.com:6443/apis/cluster.management.io/v1/namespaces/test-1/manifestworks/test-1-klusterlet-addon-workmgr": x509: certificate signed by unknown authority
      E0917 03:04:05.874887       1 base_controller.go:231] "ManifestWorkAgent" controller failed to sync "test-1-klusterlet-addon-workmgr", err: Failed to update work status with err Get "api.aaa-ocp.dev02.location.com:6443/apis/cluster.management.io/v1/namespaces/test-1/manifestworks/test-1-klusterlet-addon-workmgr": x509: certificate signed by unknown authority
      E0917 03:04:37.245859       1 reflector.go:127] k8s.io/client-go@v0.19.0/tools/cache/reflector.go:156: Failed to watch *v1.ManifestWork: failed to list *v1.ManifestWork: Get "api.aaa-ocp.dev02.location.com:6443/apis/cluster.management.io/v1/namespaces/test-1/manifestworks?resourceVersion=607424": x509: certificate signed by unknown authority

- Resolving the problem: Clusters offline after certificate change

  If you want to recover a managed cluster, complete the following steps to import the managed cluster again:

  1.  On the hub cluster, recreate the managed cluster import secret by running the following command:

          oc delete secret -n <cluster_name> <cluster_name>-import

      Replace `<cluster_name>` with the name of the managed cluster that you want to import.

  2.  On the hub cluster, expose the managed cluster import secret to a YAML file by running the following command:

          oc get secret -n <cluster_name> <cluster_name>-import -ojsonpath='{.data.import\.yaml}' | base64 --decode  > import.yaml

      Replace `<cluster_name>` with the name of the managed cluster that you want to import.

  3.  On the managed cluster, apply the `import.yaml` file by running the following command:

          oc apply -f import.yaml

  **Note:** The previous steps do not detach the managed cluster from the hub cluster. The steps update the required manifests with current settings on the managed cluster, including the new certificate information.

</div>

<a id="troubleshooting-cluster-status-offline-available-mce"></a>

## Troubleshooting cluster status changing from offline to available

The status of the managed cluster alternates between `offline` and `available` without any manual change to the environment or cluster.

<div>

<div class="title">

Procedure

</div>

- Symptom: Cluster status changing from offline to available

  When the network that connects the managed cluster to the hub cluster is unstable, the status of the managed cluster that is reported by the hub cluster cycles between `offline` and `available`.

- Resolving the problem: Cluster status changing from offline to available

  To attempt to resolve this issue, complete the following steps:

  1.  Edit your `ManagedCluster` specification on the hub cluster by entering the following command:

          oc edit managedcluster <cluster-name>

      Replace *cluster-name* with the name of your managed cluster.

  2.  Increase the value of `leaseDurationSeconds` in your `ManagedCluster` specification. The default value is 60 seconds, and the offline grace period for the managed cluster is 5 minutes, which is 5 times the `leaseDurationSeconds`. This might not be enough time to maintain the connection with the network issues. Specify a greater amount of time for the lease. For example, setting `leaseDurationSeconds` to 240 seconds provides a 20 minute offline grace period.

</div>

<a id="troubleshooting-cluster-creation-on-vmware-vsphere-mce"></a>

## Troubleshooting cluster creation on VMware vSphere

If you experience a problem when creating a Red Hat OpenShift Container Platform cluster on VMware vSphere, see the following troubleshooting information to see if one of them addresses your problem.

**Note:** Sometimes when the cluster creation process fails on VMware vSphere, the link is not enabled for you to view the logs. If this happens, you can identify the problem by viewing the log of the `hive-controllers` pod. The `hive-controllers` log is in the `hive` namespace.

<div>

<div class="title">

Procedure

</div>

- Managed cluster creation fails with certificate IP SAN error

- Symptom: Managed cluster creation fails with certificate IP SAN error

  After creating a new Red Hat OpenShift Container Platform cluster on VMware vSphere, the cluster fails with an error message that indicates a certificate IP SAN error.

- Identifying the problem: Managed cluster creation fails with certificate IP SAN error

  The deployment of the managed cluster fails and returns the following errors in the deployment log:

      time="2020-08-07T15:27:55Z" level=error msg="Error: error setting up new vSphere SOAP client: Post https://147.1.1.1/sdk: x509: cannot validate certificate for xx.xx.xx.xx because it doesn't contain any IP SANs"
      time="2020-08-07T15:27:55Z" level=error

- Resolving the problem: Managed cluster creation fails with certificate IP SAN error

  Use the VMware vCenter server fully-qualified host name instead of the IP address in the credential. You can also update the VMware vCenter CA certificate to contain the IP SAN.

- Managed cluster creation fails with unknown certificate authority

- Symptom: Managed cluster creation fails with unknown certificate authority

  After creating a new Red Hat OpenShift Container Platform cluster on VMware vSphere, the cluster fails because the certificate is signed by an unknown authority.

- Identifying the problem: Managed cluster creation fails with unknown certificate authority

  The deployment of the managed cluster fails and returns the following errors in the deployment log:

      Error: error setting up new vSphere SOAP client: Post https://vspherehost.com/sdk: x509: certificate signed by unknown authority"

- Resolving the problem: Managed cluster creation fails with unknown certificate authority

  Ensure you entered the correct certificate from the certificate authority when creating the credential.

- Managed cluster creation fails with expired certificate

- Symptom: Managed cluster creation fails with expired certificate

  After creating a new Red Hat OpenShift Container Platform cluster on VMware vSphere, the cluster fails because the certificate is expired or is not yet valid.

- Identifying the problem: Managed cluster creation fails with expired certificate

  The deployment of the managed cluster fails and returns the following errors in the deployment log:

      x509: certificate has expired or is not yet valid

- Resolving the problem: Managed cluster creation fails with expired certificate

  Ensure that the time on your ESXi hosts is synchronized.

- Managed cluster creation fails with insufficient privilege for tagging

- Symptom: Managed cluster creation fails with insufficient privilege for tagging

  After creating a new Red Hat OpenShift Container Platform cluster on VMware vSphere, the cluster fails because there is insufficient privilege to use tagging.

- Identifying the problem: Managed cluster creation fails with insufficient privilege for tagging

  The deployment of the managed cluster fails and returns the following errors in the deployment log:

      time="2020-08-07T19:41:58Z" level=debug msg="vsphere_tag_category.category: Creating..."
      time="2020-08-07T19:41:58Z" level=error
      time="2020-08-07T19:41:58Z" level=error msg="Error: could not create category: POST https://vspherehost.com/rest/com/vmware/cis/tagging/category: 403 Forbidden"
      time="2020-08-07T19:41:58Z" level=error
      time="2020-08-07T19:41:58Z" level=error msg="  on ../tmp/openshift-install-436877649/main.tf line 54, in resource \"vsphere_tag_category\" \"category\":"
      time="2020-08-07T19:41:58Z" level=error msg="  54: resource \"vsphere_tag_category\" \"category\" {"

- Resolving the problem: Managed cluster creation fails with insufficient privilege for tagging

  Ensure that your VMware vCenter required account privileges are correct. See [Image registry removed during installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html-single/installing_on_vmware_vsphere/index#registry-removed_installing-vsphere-installer-provisioned-network-customizations) for more information.

- Managed cluster creation fails with invalid dnsVIP

- Symptom: Managed cluster creation fails with invalid dnsVIP

  After creating a new Red Hat OpenShift Container Platform cluster on VMware vSphere, the cluster fails because there is an invalid dnsVIP.

- Identifying the problem: Managed cluster creation fails with invalid dnsVIP

  If you see the following message when trying to deploy a new managed cluster with VMware vSphere, it is because you have an older OpenShift Container Platform release image that does not support VMware Installer Provisioned Infrastructure (IPI):

      failed to fetch Master Machines: failed to load asset \\\"Install Config\\\": invalid \\\"install-config.yaml\\\" file: platform.vsphere.dnsVIP: Invalid value: \\\"\\\": \\\"\\\" is not a valid IP

- Resolving the problem: Managed cluster creation fails with invalid dnsVIP

  Select a release image from a later version of OpenShift Container Platform that supports VMware Installer Provisioned Infrastructure.

- Managed cluster creation fails with incorrect network type

- Symptom: Managed cluster creation fails with incorrect network type

  After creating a new Red Hat OpenShift Container Platform cluster on VMware vSphere, the cluster fails because there is an incorrect network type specified.

- Identifying the problem: Managed cluster creation fails with incorrect network type

  If you see the following message when trying to deploy a new managed cluster with VMware vSphere, it is because you have an older OpenShift Container Platform image that does not support VMware Installer Provisioned Infrastructure (IPI):

      time="2020-08-11T14:31:38-04:00" level=debug msg="vsphereprivate_import_ova.import: Creating..."
      time="2020-08-11T14:31:39-04:00" level=error
      time="2020-08-11T14:31:39-04:00" level=error msg="Error: rpc error: code = Unavailable desc = transport is closing"
      time="2020-08-11T14:31:39-04:00" level=error
      time="2020-08-11T14:31:39-04:00" level=error
      time="2020-08-11T14:31:39-04:00" level=fatal msg="failed to fetch Cluster: failed to generate asset \"Cluster\": failed to create cluster: failed to apply Terraform: failed to complete the change"

- Resolving the problem: Managed cluster creation fails with incorrect network type

  Select a valid VMware vSphere network type for the specified VMware cluster.

- Managed cluster creation fails with an error processing disk changes

- Symptom: Adding the VMware vSphere managed cluster fails due to an error processing disk changes

  After creating a new Red Hat OpenShift Container Platform cluster on VMware vSphere, the cluster fails because there is an error when processing disk changes.

- Identifying the problem: Adding the VMware vSphere managed cluster fails due to an error processing disk changes

  A message similar to the following is displayed in the logs:

      ERROR
      ERROR Error: error reconfiguring virtual machine: error processing disk changes post-clone: disk.0: ServerFaultCode: NoPermission: RESOURCE (vm-71:2000), ACTION (queryAssociatedProfile): RESOURCE (vm-71), ACTION (PolicyIDByVirtualDisk)

- Resolving the problem: Adding the VMware vSphere managed cluster fails due to an error processing disk changes

  Use the VMware vSphere client to give the user **All privileges** for *Profile-driven Storage Privileges*.

</div>

<a id="troubleshooting-cluster-in-console-with-pending-or-failed-status-mce"></a>

## Troubleshooting cluster in console with pending or failed status

If you observe *Pending* status or *Failed* status in the console for a cluster you created, follow the procedure to troubleshoot the problem.

<div>

<div class="title">

Procedure

</div>

- Symptom: Cluster in console with pending or failed status

  After creating a new cluster by using the console, the cluster does not progress beyond the status of *Pending* or displays *Failed* status.

- Identifying the problem: Cluster in console with pending or failed status

  If the cluster displays *Failed* status, navigate to the details page for the cluster and follow the link to the logs provided. If no logs are found or the cluster displays *Pending* status, continue with the following procedure to check for logs:

- Procedure 1

  1.  Run the following command on the hub cluster to view the names of the Kubernetes pods that were created in the namespace for the new cluster:

          oc get pod -n <new_cluster_name>

      Replace `new_cluster_name` with the name of the cluster that you created.

  2.  If no pod that contains the string `provision` in the name is listed, continue with Procedure 2. If there is a pod with `provision` in the title, run the following command on the hub cluster to view the logs of that pod:

          oc logs <new_cluster_name_provision_pod_name> -n <new_cluster_name> -c hive

      Replace `new_cluster_name_provision_pod_name` with the name of the cluster that you created, followed by the pod name that contains `provision`.

  3.  Search for errors in the logs that might explain the cause of the problem.

- Procedure 2

  If there is not a pod with `provision` in its name, the problem occurred earlier in the process. Complete the following procedure to view the logs:

  1.  Run the following command on the hub cluster:

          oc describe clusterdeployments -n <new_cluster_name>

      Replace `new_cluster_name` with the name of the cluster that you created.

      For more information about cluster installation logs, see [Gathering installation logs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.4/html/installing/installing-gather-logs) in the Red Hat OpenShift documentation.

  2.  See if there is additional information about the problem in the *Status.Conditions.Message* and *Status.Conditions.Reason* entries of the resource.

- Resolving the problem: Cluster in console with pending or failed status

  After you identify the errors in the logs, determine how to resolve the errors before you destroy the cluster and create it again.

  The following example provides a possible log error of selecting an unsupported zone, and the actions that are required to resolve it:

      No subnets provided for zones

  When you created your cluster, you selected one or more zones within a region that are not supported. Complete one of the following actions when you recreate your cluster to resolve the issue:

- Select a different zone within the region.

- Omit the zone that does not provide the support, if you have other zones listed.

- Select a different region for your cluster.

  After determining the issues from the log, destroy the cluster and recreate it.

  See [Creating clusters](clusters.md#create-intro) for more information about creating a cluster.

</div>

<a id="troubleshooting-klusterlet-with-degraded-conditions-mce"></a>

## Troubleshooting Klusterlet with degraded conditions

The Klusterlet degraded conditions can help to diagnose the status of the klusterlet agent on managed cluster. If a Klusterlet is in the degraded condition, the klusterlet agent on managed cluster might have errors that need to be troubleshooted. See the following information for Klusterlet degraded conditions that are set to `True`.

<div>

<div class="title">

Procedure

</div>

- Symptom: Klusterlet is in the degraded condition

  After deploying a Klusterlet on managed cluster, the `RegistrationDesiredDegraded` or `WorkDesiredDegraded` condition displays a status of *True*.

- Identifying the problem: Klusterlet is in the degraded condition

  1.  Run the following command on the managed cluster to view the Klusterlet status:

          kubectl get klusterlets klusterlet -oyaml

  2.  Check `RegistrationDesiredDegraded` or `WorkDesiredDegraded` to see if the condition is set to `True`. Proceed to *Resolving the problem* for any degraded conditions that are listed.

- Resolving the problem: Klusterlet is in the degraded condition

  See the following list of degraded statuses and how you can attempt to resolve those issues:

  - If the `RegistrationDesiredDegraded` condition with a status of *True* and the condition reason is: *BootStrapSecretMissing*, you need create a bootstrap secret on `open-cluster-management-agent` namespace.

  - If the `RegistrationDesiredDegraded` condition displays *True* and the condition reason is a *BootstrapSecretError*, or *BootstrapSecretUnauthorized*, then the current bootstrap secret is invalid. Delete the current bootstrap secret and recreate a valid bootstrap secret on `open-cluster-management-agent` namespace.

  - If the `RegistrationDesiredDegraded` and `WorkDesiredDegraded` displays *True* and the condition reason is *HubKubeConfigSecretMissing*, delete the Klusterlet and recreate it.

  - If the `RegistrationDesiredDegraded` and `WorkDesiredDegraded` displays *True* and the condition reason is: *ClusterNameMissing*, *KubeConfigMissing*, *HubConfigSecretError*, or *HubConfigSecretUnauthorized*, delete the hub cluster kubeconfig secret from `open-cluster-management-agent` namespace. The klusterlet agent creates a new hub cluster kubeconfig secret.

  - If the `RegistrationDesiredDegraded` displays *True* and the condition reason is *GetRegistrationDeploymentFailed* or *UnavailableRegistrationPod*, you can check the condition message to get the problem details and attempt to resolve.

  - If the `WorkDesiredDegraded` displays *True* and the condition reason is *GetWorkDeploymentFailed* or *UnavailableWorkPod*, you can check the condition message to get the problem details and attempt to resolve.

</div>

<a id="trouble-cluster-remove-namespace-mce"></a>

## Troubleshooting namespace that remains after deleting a cluster

When you remove a managed cluster, the namespace is normally removed as part of the cluster removal process. In rare cases, the namespace remains with some artifacts, so you must manually remove the namespace.

<div>

<div class="title">

Procedure

</div>

- Symptom: Namespace remains after deleting a cluster

  After removing a managed cluster, the namespace is not removed.

- Resolving the problem: Namespace remains after deleting a cluster

  Complete the following steps to remove the namespace manually:

  1.  Run the following command to produce a list of the resources that remain in the \<cluster_name\> namespace:

      ``` bash
      oc api-resources --verbs=list --namespaced -o name | grep -E '^secrets|^serviceaccounts|^managedclusteraddons|^roles|^rolebindings|^manifestworks|^leases|^managedclusterinfo|^appliedmanifestworks|^clusteroauths'| xargs -n 1 oc get --show-kind --ignore-not-found -n <cluster_name>
      ```

      Replace `<cluster_name>` with the name of the namespace for the cluster that you attempted to remove.

  2.  Delete each identified resource on the list that does not have a status of `Delete` by entering the following command to edit the list:

      ``` bash
      oc edit <resource_kind> <resource_name> -n <namespace>
      ```

      Replace `<resource_kind>` with the kind of the resource.

      Replace `<resource_name>` with the name of the resource.

      Replace `<namespace>` with the name of the namespace of the resource.

  3.  Locate the `finalizer` attribute in the in the metadata.

  4.  Delete the non-Kubernetes finalizers by using the `vi` editor `dd` command.

  5.  Save the list and exit the `vi` editor by entering the `:wq` command.

  6.  Delete the namespace by entering the following command:

  ``` bash
  oc delete ns <cluster-name>
  ```

  \+ Replace `<cluster-name>` with the name of the namespace that you are trying to delete.

</div>

<a id="trouble-auto-import-secret-exists-mce"></a>

## Auto-import-secret-exists error when importing a cluster

Your cluster import fails with an error message that reads: auto import secret exists.

<div>

<div class="title">

Procedure

</div>

- Symptom: Auto import secret exists error when importing a cluster

  When importing a hive cluster for management, an `auto-import-secret already exists` error is displayed.

- Resolving the problem: Auto-import-secret-exists error when importing a cluster

  This problem occurs when you attempt to import a cluster that was previously managed. When this happens, the secrets conflict when you try to reimport the cluster.

  To work around this problem, complete the following steps:

  1.  To manually delete the existing `auto-import-secret`, run the following command on the hub cluster:

          oc delete secret auto-import-secret -n <cluster-namespace>

      Replace `cluster-namespace` with the namespace of your cluster.

  2.  Import your cluster again by using the procedure in [Cluster import introduction](clusters.md#import-intro).

</div>

<a id="troubleshooting-no-placementdecision-mce"></a>

## Troubleshooting missing PlacementDecision after creating Placement

If the `PlacementDecision` is missing after you create a `Placement`, follow the procedure to troubleshoot the problem.

<div>

<div class="title">

Procedure

</div>

- Symptom: Missing PlacementDecision after creating Placement

  After creating a `Placement`, a `PlacementDecision` is not automatically generated.

- Resolving the problem: Missing PlacementDecision after creating Placement

  To resolve the issue, complete the following steps:

  1.  Check the `Placement` conditions by running the following command:

      ``` bash
      oc describe placement <placement-name>
      ```

      Replace `placement-name` with the name of the `Placement`.

      The output might resemble the following example:

  ``` bash
  Name:         demo-placement
  Namespace:    default
  Labels:       <none>
  Annotations:  <none>
  API Version:  cluster.open-cluster-management.io/v1beta1
  Kind:         Placement
  Status:
    Conditions:
      Last Transition Time:       2022-09-30T07:39:45Z
      Message:                    Placement configurations check pass
      Reason:                     Succeedconfigured
      Status:                     False
      Type:                       PlacementMisconfigured
      Last Transition Time:       2022-09-30T07:39:45Z
      Message:                    No valid ManagedClusterSetBindings found in placement namespace
      Reason:                     NoManagedClusterSetBindings
      Status:                     False
      Type:                       PlacementSatisfied
    Number Of Selected Clusters:  0
  ```

  1.  Check the output for the `Status` of `PlacementMisconfigured` and `PlacementSatisfied`:

- If the `PlacementMisconfigured` `Status` is true, your `Placement` has configuration errors. Check the included message for more details on the configuration errors and how to resolve them.

- If the `PlacementSatisfied` `Status` is false, no managed cluster satisfies your `Placement`. Check the included message for more details and how to resolve the error. In the previous example, no `ManagedClusterSetBindings` were found in the placement namespace.

  1.  You can check the score of each cluster in `Events` to find out why some clusters with lower scores are not selected. The output might resemble the following example:

      ``` bash
      Name:         demo-placement
      Namespace:    default
      Labels:       <none>
      Annotations:  <none>
      API Version:  cluster.open-cluster-management.io/v1beta1
      Kind:         Placement
      Events:
        Type    Reason          Age   From                 Message
        ----    ------          ----  ----                 -------
        Normal  DecisionCreate  2m10s   placementController  Decision demo-placement-decision-1 is created with placement demo-placement in namespace default
        Normal  DecisionUpdate  2m10s   placementController  Decision demo-placement-decision-1 is updated with placement demo-placement in namespace default
        Normal  ScoreUpdate     2m10s   placementController  cluster1:0 cluster2:100 cluster3:200
        Normal  DecisionUpdate  3s      placementController  Decision demo-placement-decision-1 is updated with placement demo-placement in namespace default
        Normal  ScoreUpdate     3s      placementController  cluster1:200 cluster2:145 cluster3:189 cluster4:200
      ```

      **Note:** The placement controller assigns a score and generates an event for each filtered `ManagedCluster`. The placement controller generates a new event when the cluster score changes.

  2.  Check if clusters are being filtered due to taints by running the following command:

      ``` bash
      oc get managedcluster <cluster-name> -o yaml
      ```

      Replace `cluster-name` with the name of a cluster that you expected to be selected.

      Look for the `taints` section in the output. If the cluster has taints, it is selected only by placements with matching tolerations. The output might resemble the following example:

      ``` yaml
      apiVersion: cluster.open-cluster-management.io/v1
      kind: ManagedCluster
      metadata:
        name: cluster1
      spec:
        hubAcceptsClient: true
        taints:
          - effect: NoSelect
            key: cluster.open-cluster-management.io/unreachable
            timeAdded: '2022-02-21T08:11:06Z'
      ```

      In this example, the cluster has an `unreachable` taint. To select this cluster, your placement must include a matching toleration:

      ``` yaml
      apiVersion: cluster.open-cluster-management.io/v1beta1
      kind: Placement
      metadata:
        name: demo-placement
        namespace: default
      spec:
        tolerations:
          - key: cluster.open-cluster-management.io/unreachable
            operator: Exists
      ```

  Built-in taints are automatically added to clusters when they become unavailable or unreachable. See [Taints and tolerations](clusters.md#taints-tolerations) for more information about taints and tolerations.

</div>

<a id="troubleshooting-idrac-discovery-fails-mce"></a>

## Troubleshooting a discovery failure of bare metal hosts on Dell hardware

If the discovery of bare metal hosts fails on Dell hardware, the Integrated Dell Remote Access Controller (iDRAC) is likely configured to not allow certificates from unknown certificate authorities.

<div>

<div class="title">

Procedure

</div>

- Symptom: Discovery failure of bare metal hosts on Dell hardware

  After you complete the procedure for discovering bare metal hosts by using the baseboard management controller, an error message similar to the following is displayed:

      ProvisioningError 51s metal3-baremetal-controller Image provisioning failed: Deploy step deploy.deploy failed with BadRequestError: HTTP POST https://<bmc_address>/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD/Actions/VirtualMedia.InsertMedia returned code 400. Base.1.8.GeneralError: A general error has occurred. See ExtendedInfo for more information Extended information: [
      {"Message": "Unable to mount remote share https://<ironic_address>/redfish/boot-<uuid>.iso.", 'MessageArgs': ["https://<ironic_address>/redfish/boot-<uuid>.iso"], "MessageArgs@odata.count": 1, "MessageId": "IDRAC.2.5.RAC0720", "RelatedProperties": ["#/Image"], "RelatedProperties@odata.count": 1, "Resolution": "Retry the operation.", "Severity": "Informational"}
      ]

- Resolving the problem: Discovery failure of bare metal hosts on Dell hardware

  The iDRAC is configured not to accept certificates from unknown certificate authorities.

  To bypass the problem, disable the certificate verification on the baseboard management controller of the host iDRAC by completing the following steps:

  1.  In the iDRAC console, navigate to **Configuration** \> **Virtual media** \> **Remote file share**.

  2.  Change the value of **Expired or invalid certificate action** to `Yes`.

</div>

<a id="trouble-min-iso-boot"></a>

## Troubleshooting Minimal ISO boot failures

You might encounter issues when trying to boot a minimal ISO.

<div>

<div class="title">

Procedure

</div>

- Symptom: Minimal ISO boot failures

  The boot screen shows that the host has failed to download the root file system image.

- Resolving the problem: Minimal ISO boot failures

  See [Troubleshooting minimal discovery ISO issues](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025/html/installing_openshift_container_platform_with_the_assisted_installer/assembly_troubleshooting#con_minimal-iso-image_troubleshooting) in the Assisted Installer for OpenShift Container Platform} documentation to learn how to troubleshoot the issue.

</div>

<a id="trouble-mirror-rhcos-image"></a>

## Troubleshooting the RHCOS image mirroring

For hosted control planes on Red Hat OpenShift Virtualization in a disconnected environment, `oc-mirror` fails to automatically mirror the Red Hat Enterprise Linux CoreOS (RHCOS) image to the internal registry. When you create your first hosted cluster, the Kubevirt virtual machine does not boot, because the boot image is not availble in the internal registry.

<div>

<div class="title">

Procedure

</div>

- Symptom: *oc-mirror* fails to attempt the RHCOS image mirroring

  The `oc-mirror` plugin does not mirror the {op-system-first} image from the release payload to the internal registry.

- Resolving the problem: *oc-mirror* fails to attempt the RHCOS image mirroring

  To resolve this issue, manually mirror the RHCOS image to the internal registry. Complete the following steps:

  1.  Get the internal registry name by running the following command:

      ``` bash
      oc get imagecontentsourcepolicy -o json | jq -r '.items[].spec.repositoryDigestMirrors[0].mirrors[0]'
      ```

  2.  Get a payload image by running the following command:

      ``` bash
      oc get clusterversion version -ojsonpath='{.status.desired.image}'
      ```

  3.  Extract the `0000_50_installer_coreos-bootimages.yaml` file that contains boot images from your payload image on the hosted cluster. Replace `<payload_image>` with the name of your payload image. Run the following command:

      ``` bash
      oc image extract --file /release-manifests/0000_50_installer_coreos-bootimages.yaml <payload_image> --confirm
      ```

  4.  Get the RHCOS image by running the following command:

      ``` bash
      cat 0000_50_installer_coreos-bootimages.yaml | yq -r .data.stream | jq -r '.architectures.x86_64.images.kubevirt."digest-ref"'
      ```

  5.  Mirror the RHCOS image to your internal registry. Replace `<rhcos_image>` with your RHCOS image for example, `quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:d9643ead36b1c026be664c9c65c11433c6cdf71bfd93ba229141d134a4a6dd94`. Replace `<internal_registry>` with the name of your internal registry, for example, `virthost.ostest.test.metalkube.org:5000/localimages/ocp-v4.0-art-dev`. Run the following command:

      ``` bash
      oc image mirror <rhcos_image> <internal_registry>
      ```

  6.  Create a YAML file named `rhcos-boot-kubevirt.yaml` that defines the `ImageDigestMirrorSet` object. See the following example configuration:

      ``` yaml
      apiVersion: config.openshift.io/v1
      kind: ImageDigestMirrorSet
      metadata:
        name: rhcos-boot-kubevirt
      spec:
        repositoryDigestMirrors:
          - mirrors:
              - <rhcos_image_no_digest>
            source: virthost.ostest.test.metalkube.org:5000/localimages/ocp-v4.0-art-dev
      ```

      - Specify your RHCOS image without its digest, for example, `quay.io/openshift-release-dev/ocp-v4.0-art-dev`.

      - Specify the name of your internal registry, for example, `virthost.ostest.test.metalkube.org:5000/localimages/ocp-v4.0-art-dev`.

  7.  Apply the `rhcos-boot-kubevirt.yaml` file to create the `ImageDigestMirrorSet` object by running the following command:

  ``` bash
  oc apply -f rhcos-boot-kubevirt.yaml
  ```

</div>

<a id="troubleshooting-return-non-bm-cluster"></a>

## Troubleshooting: Returning non bare metal clusters to the late binding pool

If you are using late binding managed clusters without `BareMetalHosts`, you must complete additional manual steps to destroy a late binding cluster and return the nodes back to the Discovery ISO.

<div>

<div class="title">

Procedure

</div>

- Symptom: Returning non bare metal clusters to the late binding pool

  For late binding managed clusters without `BareMetalHosts`, removing cluster information does not automatically return all nodes to the Discovery ISO.

- Resolving the problem: Returning non bare metal clusters to the late binding pool

  To unbind the non bare metal nodes with late binding, complete the following steps:

  1.  Remove the cluster information. See [Cluster removal overview](clusters.md#remove-managed-cluster) to learn more.

  2.  Clean the root disks.

  3.  Reboot manually with the Discovery ISO.

</div>

<a id="trouble-unknown-status-rosa-hcp"></a>

## Troubleshooting managed clusters *Unknown* on Red Hat OpenShift Service on AWS (classic) with hosted control planes cluster

The status of all managed clusters on a Red Hat OpenShift Service on AWS (classic) hosted clusters suddenly becomes `Unknown`.

<div>

<div class="title">

Procedure

</div>

- Symptom: All managed clusters are in *Unknown* status on Red Hat OpenShift Service on AWS (classic) with hosted control planes cluster

  When you check the `klusterlet-agent` pod log in the `open-cluster-management-agent` namespace on your managed cluster, you see an error that resembles the following:

  ``` terminal
  E0809 18:45:29.450874       1 reflector.go:147] k8s.io/client-go@v0.29.4/tools/cache/reflector.go:229: Failed to watch *v1.CertificateSigningRequest: failed to list *v1.CertificateSigningRequest: Get "https://api.xxx.openshiftapps.com:443/apis/certificates.k8s.io/v1/certificatesigningrequests?limit=500&resourceVersion=0": tls: failed to verify certificate: x509: certificate signed by unknown authority
  ```

- Resolving the problem: All managed clusters are in *Unknown* status on Red Hat OpenShift Service on AWS (classic) with hosted control planes cluster

  1.  Create a `KlusterletConfig` resource with name `global` if it does not exist.

  2.  Set the `spec.hubKubeAPIServerConfig.serverVerificationStrategy` to `UseSystemTruststore`. See the following example:

      ``` yaml
      apiVersion: config.open-cluster-management.io/v1alpha1
      kind: KlusterletConfig
      metadata:
        name: global
      spec:
        hubKubeAPIServerConfig:
          serverVerificationStrategy: UseSystemTruststore
      ```

  3.  Apply the resource by running the following command on the hub cluster. Replace `<filename>` with the name of your file:

      ``` bash
      oc apply -f <filename>
      ```

      The state of some managed clusters might recover. Continue with the process for managed clusters that remain in the `Unknown` status.

  4.  Export and decode the `` import.yaml `file from the hub cluster by running the following command on the hub cluster. Replace `<cluster_name> `` with the name of your cluster.

      ``` bash
      oc get secret <cluster_name>-import -n <cluster_name> -o jsonpath={.data.import\.yaml} | base64 --decode > <cluster_name>-import.yaml
      ```

  5.  Apply the file by running the following command on the managed cluster.

  ``` bash
  oc apply -f <cluster_name>-import.yaml
  ```

</div>

<a id="update-managed-missing-ocp"></a>

## Troubleshooting an attempt to update managed cluster with missing OpenShift Container Platform version

You do not see the OpenShift Container Platform version that you want in the console when you attempt to update your managed cluster in the console.

<div>

<div class="title">

Procedure

</div>

- Symptom: Attempt to update managed cluster with missing OpenShift Container Platform version

  When you attempt to update a managed cluster from the console and click **Update available** in the *Cluster details* view to choose the OpenShift Container Platform version from the dropdown list, the version is missing.

- Resolving the problem: Attempt to update managed cluster with missing OpenShift Container Platform version

</div>

<a id="ca-update-error-hive-ai"></a>

## Troubleshooting certificate authority update error on Hive and Assisted Installer clusters

Troubleshoot a connection error message that appears after you update the cluster certificate authority (CA) on a Hive-provisioned or Assisted Installer cluster.

<div>

<div class="title">

Procedure

</div>

- Symptom: Certificate authority update error on Hive and Assisted Installer clusters

  When you update the cluster CA with your enterprise CA on the Hive-provisioned or Assisted Installer cluster, the corresponding cluster deployment on the hub cluster displays the following connection error message:

  ``` terminal
  x509: certificate signed by unknown authority
  ```

  If you back up and restore the cluster in this state, you cannot automatically import the managed cluster to the restored hub cluster.

- Resolving the problem: Certificate authority update error on Hive and Assisted Installer clusters

  Use the following procedure to resolve the error:

  1.  Define your custom CA with the global variable in your system. Run the following command:

      ``` bash
      export CA=<your_customized_CA>
      ```

  2.  Run the following command to generate a new secret with your customized CA:

      ``` bash
      oc create secret generic additional-ca \
        --from-literal=ca.crt="$CA" \
        --namespace hive
      ```

  3.  Update your cluster with the new secret. Run the following command with the additional CA patch:

  ``` bash
  oc patch hiveconfig hive --type=merge -p '
  {
    "spec": {
      "additionalCertificateAuthoritiesSecretRef": [
        {
          "name": "additional-ca"
        }
      ]
    }
  }'
  ```

</div>

<a id="trouble-miss-namespace"></a>

## Troubleshooting: Missing `open-cluster-management-global-set` namespace

The `open-cluster-management-global-set` namespace contains the `global` Placement, which is required to deploy add-ons such as `cluster-proxy`, `managed-serviceaccount`, and `work-manager` to managed clusters.

If the `open-cluster-management-global-set` namespace is missing or deleted, add-ons are not installed on managed clusters. If you previously installed the add-ons, they are removed if the namespace is missing or deleted.

<div>

<div class="title">

Procedure

</div>

- Symptom: Missing `open-cluster-management-global-set` namespace

  After installing Red Hat Advanced Cluster Management, the `open-cluster-management-global-set` namespace is missing on the hub cluster. As a result, no `ManagedClusterAddOn` resources are created for the `cluster-proxy`, `managed-serviceaccount`, and `work-manager` add-ons.

- Identifying the problem: Missing `open-cluster-management-global-set` namespace

  The `open-cluster-management-global-set` namespace is missing and the `ManagedClusterSet` called `global` includes the `open-cluster-management.io/ns-create: "true"` annotation. You can also find the following message in the 'ocm-controller' log in the `multicluster-engine` namespace:

  ``` bash
  I0904 04:50:09.628951       1 globalset_controller.go:202] GlobalSet Namespace open-cluster-management-global-set does not exist, skip applying binding and placement
  ```

- Resolving the problem: Missing `open-cluster-management-global-set` namespace

  To resolve the issue, remove the annotation from the `ManagedClusterSet` called `global`. Run the following command to recreate the namespace and the `global` Placement:

  ``` bash
  oc annotate managedclusterset global open-cluster-management.io/ns-create- --overwrite
  ```

</div>
