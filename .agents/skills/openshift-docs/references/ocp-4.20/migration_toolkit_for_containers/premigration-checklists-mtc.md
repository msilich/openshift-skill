<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you migrate your application workloads with the Migration Toolkit for Containers (MTC), review the following checklists.

# Cluster health checklist

- [ ] The clusters meet the minimum hardware requirements for the specific platform and installation method, for example, on [bare metal](../installing/installing_bare_metal/upi/installing-bare-metal.md#minimum-resource-requirements_installing-bare-metal).

- [ ] All [MTC prerequisites](migrating-applications-with-mtc.md#migration-prerequisites_migrating-applications-with-mtc) are met.

- [ ] All nodes have an active OpenShift Container Platform subscription.

- [ ] You have [verified node health](../support/troubleshooting/verifying-node-health.md#verifying-node-health).

- [ ] The [identity provider](../authentication/understanding-identity-provider.md#supported-identity-providers) is working.

- [ ] The migration network has a minimum throughput of 10 Gbps.

- [ ] The clusters have sufficient resources for migration.

  > [!NOTE]
  > Clusters require additional memory, CPUs, and storage in order to run a migration on top of normal workloads. Actual resource requirements depend on the number of Kubernetes resources being migrated in a single migration plan. You must test migrations in a non-production environment in order to estimate the resource requirements.

- [ ] The [etcd disk performance](https://access.redhat.com/solutions/4885641) of the clusters has been checked with `fio`.

# Source cluster checklist

- [ ] You have checked for persistent volumes (PVs) with abnormal configurations stuck in a **Terminating** state by running the following command:

  ``` terminal
  $ oc get pv
  ```

- [ ] You have checked for pods whose status is other than **Running** or **Completed** by running the following command:

  ``` terminal
  $ oc get pods --all-namespaces | egrep -v 'Running | Completed'
  ```

- [ ] You have checked for pods with a high restart count by running the following command:

  ``` terminal
  $ oc get pods --all-namespaces --field-selector=status.phase=Running \
    -o json | jq '.items[]|select(any( .status.containerStatuses[]; \
    .restartCount > 3))|.metadata.name'
  ```

  Even if the pods are in a **Running** state, a high restart count might indicate underlying problems.

- [ ] The cluster certificates are valid for the duration of the migration process.

- [ ] You have checked for pending certificate-signing requests by running the following command:

  ``` terminal
  $ oc get csr -A | grep pending -i
  ```

- [ ] The registry uses a [recommended storage type](../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage).

- [ ] You can read and write images to the registry.

- [ ] The [etcd cluster](https://access.redhat.com/articles/3093761) is healthy.

- [ ] The [average API server response time](../post_installation_configuration/node-tasks.md#create-a-kubeletconfig-crd-to-edit-kubelet-parameters_post-install-node-tasks) on the source cluster is less than 50 ms.

# Target cluster checklist

- [ ] The cluster has the correct network configuration and permissions to access external services, for example, databases, source code repositories, container image registries, and CI/CD tools.

- [ ] External applications and services that use services provided by the cluster have the correct network configuration and permissions to access the cluster.

- [ ] Internal container image dependencies are met.

- [ ] The target cluster and the replication repository have sufficient storage space.
