<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you migrate your application workloads with the Migration Toolkit for Containers (MTC), review the following checklists.

# Resources

- [ ] If your application uses an internal service network or an external route for communicating with services, the relevant route exists.

- [ ] If your application uses cluster-level resources, you have re-created them on the target cluster.

- [ ] You have [excluded](advanced-migration-options-3-4.md#migration-excluding-resources_advanced-migration-options-3-4) persistent volumes (PVs), image streams, and other resources that you do not want to migrate.

- [ ] PV data has been backed up in case an application displays unexpected behavior after migration and corrupts the data.

# Source cluster

- [ ] The cluster meets the [minimum hardware requirements](https://docs.openshift.com/container-platform/3.11/install/prerequisites.html#hardware).

- [ ] You have installed the correct legacy Migration Toolkit for Containers Operator version:

  - `operator-3.7.yml` on OpenShift Container Platform version 3.7.

  - `operator.yml` on OpenShift Container Platform versions 3.9 to 4.5.

- [ ] All nodes have an active OpenShift Container Platform subscription.

- [ ] You have performed all the [run-once tasks](https://docs.openshift.com/container-platform/3.11/day_two_guide/run_once_tasks.html#day-two-guide-default-storage-class).

- [ ] You have performed all the [environment health checks](https://docs.openshift.com/container-platform/3.11/day_two_guide/environment_health_checks.html).

- [ ] You have checked for PVs with abnormal configurations stuck in a **Terminating** state by running the following command:

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

- [ ] You have removed old builds, deployments, and images from each namespace to be migrated by [pruning](../applications/pruning-objects.md#pruning-objects).

- [ ] The OpenShift image registry uses a [supported storage type](https://docs.openshift.com/container-platform/3.11/scaling_performance/optimizing_storage.html#registry).

- [ ] Direct image migration only: The OpenShift image registry is [exposed](https://docs.openshift.com/container-platform/3.11/install_config/registry/securing_and_exposing_registry.html#exposing-the-registry) to external traffic.

- [ ] You can read and write images to the registry.

- [ ] The [etcd cluster](https://access.redhat.com/articles/3093761) is healthy.

- [ ] The [average API server response time](https://docs.openshift.com/container-platform/3.11/install_config/master_node_configuration.html#master-node-configuration-node-qps-burst) on the source cluster is less than 50 ms.

- [ ] The cluster certificates are [valid](https://docs.openshift.com/container-platform/3.11/install_config/redeploying_certificates.html#install-config-cert-expiry) for the duration of the migration process.

- [ ] You have checked for pending certificate-signing requests by running the following command:

  ``` terminal
  $ oc get csr -A | grep pending -i
  ```

- [ ] The [identity provider](https://docs.openshift.com/container-platform/3.11/install_config/configuring_authentication.html#overview) is working.

- [ ] You have set the value of the `openshift.io/host.generated` annotation parameter to `true` for each OpenShift Container Platform route, which updates the host name of the route for the target cluster. Otherwise, the migrated routes retain the source cluster host name.

# Target cluster

- [ ] You have installed Migration Toolkit for Containers Operator version 1.5.1.

- [ ] All [MTC prerequisites](migrating-applications-3-4.md#migration-prerequisites_migrating-applications-3-4) are met.

- [ ] The cluster meets the minimum hardware requirements for the specific platform and installation method, for example, on [bare metal](../installing/installing_bare_metal/upi/installing-bare-metal.md#minimum-resource-requirements_installing-bare-metal).

- [ ] The cluster has [storage classes](../storage/dynamic-provisioning.md#defining-storage-classes_dynamic-provisioning) defined for the storage types used by the source cluster, for example, block volume, file system, or object storage.

  > [!NOTE]
  > NFS does not require a defined storage class.

- [ ] The cluster has the correct network configuration and permissions to access external services, for example, databases, source code repositories, container image registries, and CI/CD tools.

- [ ] External applications and services that use services provided by the cluster have the correct network configuration and permissions to access the cluster.

- [ ] Internal container image dependencies are met.

  If an application uses an internal image in the `openshift` namespace that is not supported by OpenShift Container Platform 4.17, you can manually update the [OpenShift Container Platform 3 image stream tag](troubleshooting-3-4.md#migration-updating-deprecated-internal-images_troubleshooting-3-4) with `podman`.

- [ ] The target cluster and the replication repository have sufficient storage space.

- [ ] The [identity provider](../authentication/understanding-identity-provider.md#supported-identity-providers) is working.

- [ ] DNS records for your application exist on the target cluster.

- [ ] Certificates that your application uses exist on the target cluster.

- [ ] You have configured appropriate firewall rules on the target cluster.

- [ ] You have correctly configured load balancing on the target cluster.

- [ ] If you migrate objects to an existing namespace on the target cluster that has the same name as the namespace being migrated from the source, the target namespace contains no objects of the same name and type as the objects being migrated.

  > [!NOTE]
  > Do not create namespaces for your application on the target cluster before migration because this might cause quotas to change.

# Performance

- [ ] The migration network has a minimum throughput of 10 Gbps.

- [ ] The clusters have sufficient resources for migration.

  > [!NOTE]
  > Clusters require additional memory, CPUs, and storage in order to run a migration on top of normal workloads. Actual resource requirements depend on the number of Kubernetes resources being migrated in a single migration plan. You must test migrations in a non-production environment in order to estimate the resource requirements.

- [ ] The [memory and CPU usage](../support/troubleshooting/verifying-node-health.md#reviewing-node-status-use-and-configuration_verifying-node-health) of the nodes are healthy.

- [ ] The [etcd disk performance](https://access.redhat.com/solutions/4885641) of the clusters has been checked with `fio`.
