<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Learn more about administrative tasks that cluster admins must perform to successfully initialize an update, as well as optional guidelines for ensuring a successful update.

# Kubernetes API removals

In OpenShift Container Platform 4.17, a previously removed Kubernetes API was inadvertently reintroduced. It has been removed again in OpenShift Container Platform 4.20.

A cluster administrator must provide a manual acknowledgment before the cluster can be updated from OpenShift Container Platform 4.19 to 4.20. This is to help prevent issues after upgrading to OpenShift Container Platform 4.20, where APIs that have been removed are still in use by workloads, tools, or other components running on or interacting with the cluster. Administrators must evaluate their cluster for any APIs in use that will be removed and migrate the affected components to use the appropriate new API version. After this evaluation and migration is complete, the administrator can provide the acknowledgment.

Before you can update your OpenShift Container Platform 4.19 cluster to 4.20, you must provide the administrator acknowledgment.

## Removed APIs

Review the list of Kubernetes APIs that were removed in OpenShift Container Platform 4.20. Use the information to migrate affected manifests and API clients to supported versions before upgrading.

OpenShift Container Platform 4.20 removed the Kubernetes APIs in the table. You must migrate manifests and API clients to use the appropriate API version. For more information about migrating removed APIs, see the [Kubernetes documentation](https://kubernetes.io/docs/reference/using-api/deprecation-guide/).

| Resource | Removed API | Migrate to | Notable changes |
|----|----|----|----|
| `MutatingWebhookConfiguration` | `admissionregistration.k8s.io/v1beta1` | `admissionregistration.k8s.io/v1` | [Yes](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#webhook-resources-v122) |
| `ValidatingAdmissionPolicy` | `admissionregistration.k8s.io/v1beta1` | `admissionregistration.k8s.io/v1` | [Yes](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#webhook-resources-v122) |
| `ValidatingAdmissionPolicyBinding` | `admissionregistration.k8s.io/v1beta1` | `admissionregistration.k8s.io/v1` | [Yes](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#webhook-resources-v122) |
| `ValidatingWebhookConfiguration` | `admissionregistration.k8s.io/v1beta1` | `admissionregistration.k8s.io/v1` | [Yes](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#webhook-resources-v122) |

Kubernetes APIs removed from OpenShift Container Platform 4.20

## Evaluating your cluster for removed APIs

There are several methods to help administrators identify where APIs that will be removed are in use. However, OpenShift Container Platform cannot identify all instances, especially workloads that are idle or external tools that are used. It is the responsibility of the administrator to properly evaluate all workloads and other integrations for instances of removed APIs.

### Reviewing alerts to identify uses of removed APIs

Two alerts fire when an API is in use that will be removed in the next release:

- `APIRemovedInNextReleaseInUse` - for APIs that will be removed in the next OpenShift Container Platform release.

- `APIRemovedInNextEUSReleaseInUse` - for APIs that will be removed in the next OpenShift Container Platform Extended Update Support (EUS) release.

<div>

<div class="title">

Procedure

</div>

- If either of the alerts are firing in your cluster, review the alerts and take action to clear the alerts by migrating manifests and API clients to use the new API version.

</div>

<div>

<div class="title">

Verification

</div>

- Use the `APIRequestCount` API to get more information about which APIs are in use and which workloads are using removed APIs, because the alerts do not provide this information. Additionally, some APIs might not trigger these alerts but are still captured by `APIRequestCount`. The alerts are tuned to be less sensitive to avoid alerting fatigue in production systems.

</div>

### Using APIRequestCount to identify uses of removed APIs

Review the `APIRequestCount` resource to identify which removed APIs are in use by checking the `REMOVEDINRELEASE` column. Use this information to address API deprecations before you apply cluster updates.

<div>

<div class="title">

Prerequisites

</div>

- You must have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command and examine the `REMOVEDINRELEASE` column of the output to identify the removed APIs that are currently in use:

  ``` terminal
  $ oc get apirequestcounts
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                                                                 REMOVEDINRELEASE   REQUESTSINCURRENTHOUR   REQUESTSINLAST24H
  ...
  mutatingwebhookconfigurations.v1beta1.admissionregistration.k8s.io   1.22               0                       3
  ...
  ```

  </div>

  > [!IMPORTANT]
  > You can safely ignore the following entries that appear in the results:
  >
  > - The `system:serviceaccount:kube-system:generic-garbage-collector` and the `system:serviceaccount:kube-system:namespace-controller` users might appear in the results because these services call all registered APIs when searching for resources to remove.
  >
  > - The `system:kube-controller-manager` and `system:cluster-policy-controller` users might appear in the results because they walk through all resources while enforcing various policies.

  You can also use `-o jsonpath` to filter the results:

  ``` terminal
  $ oc get apirequestcounts -o jsonpath='{range .items[?(@.status.removedInRelease!="")]}{.status.removedInRelease}{"\t"}{.metadata.name}{"\n"}{end}'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  1.22 mutatingwebhookconfigurations.v1beta1.admissionregistration.k8s.io
  ```

  </div>

</div>

### Using APIRequestCount to identify which workloads are using the removed APIs

Use the `APIRequestCount` resource to identify which workloads are using a removed API by examining the `username` and `userAgent` fields for that API version.

<div>

<div class="title">

Prerequisites

</div>

- You must have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command and examine the `username` and `userAgent` fields to help identify the workloads that are using the API:

  ``` terminal
  $ oc get apirequestcounts <resource>.<version>.<group> -o yaml
  ```

  For example:

  ``` terminal
  $ oc get apirequestcounts mutatingwebhookconfigurations.v1beta1.admissionregistration.k8s.io -o yaml
  ```

  You can also use `-o jsonpath` to extract the `username` and `userAgent` values from an `APIRequestCount` resource:

  ``` terminal
  $ oc get apirequestcounts mutatingwebhookconfigurations.v1beta1.admissionregistration.k8s.io \
    -o jsonpath='{range .status.currentHour..byUser[*]}{..byVerb[*].verb}{","}{","}{"\n"}{end}' \
    | sort -k 2 -t, -u | column -t -s, -NVERBS,USERNAME,USERAGENT
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  VERBS     USERNAME                            USERAGENT
  create    system:admin                        oc/4.13.0 (linux/amd64)
  list get  system:serviceaccount:myns:default  oc/4.16.0 (linux/amd64)
  watch     system:serviceaccount:myns:webhook  webhook/v1.0.0 (linux/amd64)
  ```

  </div>

</div>

## Migrating instances of removed APIs

Review the Kubernetes Deprecated API Migration Guide for detailed instructions on migrating removed APIs. Use this information to update manifests and API clients before you upgrade your cluster.

For information about how to migrate removed Kubernetes APIs, see the [Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/) in the Kubernetes documentation.

## Providing the administrator acknowledgment

After you have evaluated your cluster for any removed APIs and have migrated any removed APIs, you can acknowledge that your cluster is ready to upgrade from OpenShift Container Platform 4.19 to 4.20.

> [!WARNING]
> Be aware that all responsibility falls on the administrator to ensure that all uses of removed APIs have been resolved and migrated as necessary before providing this administrator acknowledgment. OpenShift Container Platform can assist with the evaluation, but cannot identify all possible uses of removed APIs, especially idle workloads or external tools.

<div>

<div class="title">

Prerequisites

</div>

- You must have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command to acknowledge that you have completed the evaluation and your cluster is ready for the Kubernetes API removals in OpenShift Container Platform 4.17:

  ``` terminal
  $ oc -n openshift-config patch cm admin-acks --patch '{"data":{"ack-4.19-admissionregistration-v1beta1-api-removals-in-4.20":"true"}}' --type=merge
  ```

</div>

# The risk of conditional updates

Conditional updates are update targets flagged by the OpenShift Update Service (OSUS) as available but not recommended due to known risks that apply to your cluster.

The Cluster Version Operator (CVO) periodically queries the OSUS for the most recent data about update recommendations, and some potential update targets might have risks associated with them.

The CVO evaluates the conditional risks, and if the risks are not applicable to the cluster, then the target version is available as a recommended update path for the cluster. If the risk is determined to be applicable, or if for some reason CVO cannot evaluate the risk, then the update target is available to the cluster as a conditional update.

When you encounter a conditional update while you are trying to update to a target version, you must assess the risk of updating your cluster to that version. Generally, if you do not have a specific need to update to that target version, it is best to wait for a recommended update path from Red Hat.

However, if you have a strong reason to update to that version, for example, if you need to fix an important CVE, then the benefit of fixing the CVE might outweigh the risk of the update being problematic for your cluster. You can complete the following tasks to determine whether you agree with the Red Hat assessment of the update risk:

- Complete extensive testing in a non-production environment to the extent that you are comfortable completing the update in your production environment.

- Follow the links provided in the conditional update description, investigate the bug, and determine if it is likely to cause issues for your cluster. If you need help understanding the risk, contact Red Hat Support.

<div>

<div class="title">

Additional resources

</div>

- [Evaluation of update availability](../understanding_updates/how-updates-work.md#update-evaluate-availability_how-updates-work)

</div>

# etcd backups before cluster updates

Create etcd backups before you update clusters to preserve your cluster state and to enable disaster recovery.

etcd backups record the state of your cluster and all of its resource objects. You can use backups to try to restore the state of a cluster when the cluster has become unrecoverable.

In the context of updates, you can attempt an etcd restoration of the cluster if an update introduced catastrophic conditions that cannot be fixed without reverting to the previous cluster version.

etcd restorations might be destructive and destabilizing to a running cluster, use them only as a last resort.

> [!WARNING]
> Due to their high consequences, etcd restorations are not intended to be used as a rollback solution. Rolling your cluster back to a previous version is not supported. If your update is failing to complete, contact Red Hat support.

There are several factors that affect the viability of an etcd restoration. For more information, see "Backing up etcd data" and "Restoring to a previous cluster state".

<div>

<div class="title">

Additional resources

</div>

- [Backing up etcd](../../backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.md#backup-etcd)

- [Restoring to a previous cluster state](../../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md#dr-restoring-cluster-state)

</div>

# Preparing for Gateway API management succession by the Ingress Operator

Prepare your cluster for Gateway API management succession by removing existing unsupported definitions and installing compliant resources. This ensures a seamless update to OpenShift Container Platform 4.19 and prevents conflicts with the Ingress Operator.

Starting in OpenShift Container Platform 4.19, the Ingress Operator manages the lifecycle of any Gateway API custom resource definitions (CRDs). This lifecycle control blocks you from creating, updating, or deleting CRDs within the `gateway.networking.k8s.io` API group.

> [!NOTE]
> Starting in OpenShift Container Platform 4.22, deploying the Gateway API CRD `gateway.networking.x-k8s.io` is no longer restricted. You can deploy that CRD without interference from the Ingress Operator. Experimental Gateway API CRDs in the `gateway.networking.k8s.io` group remain restricted.

> [!WARNING]
> Updating or deleting Gateway API resources can result in downtime and loss of service or data. Be sure you understand how this will affect your cluster before performing the steps in this procedure. If necessary, back up any Gateway API objects in YAML format in order to restore it later.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have access to an OpenShift Container Platform account with cluster administrator access.

- Optional: You have backed up any necessary Gateway API objects.

  > [!WARNING]
  > Backup and restore can fail or result in data loss for any CRD fields that were present in the old definitions but are absent in the new definitions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  List all the Gateway API CRDs that you need to remove by running the following command:

    ``` terminal
    $ oc get crd | grep -F -e gateway.networking.k8s.io -e gateway.networking.x-k8s.io
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    gatewayclasses.gateway.networking.k8s.io
    gateways.gateway.networking.k8s.io
    grpcroutes.gateway.networking.k8s.io
    httproutes.gateway.networking.k8s.io
    referencegrants.gateway.networking.k8s.io
    ```

    </div>

2.  Delete the Gateway API CRDs from the previous step by running the following command:

    ``` terminal
    $ oc delete crd gatewayclasses.networking.k8s.io && \
    oc delete crd gateways.networking.k8s.io && \
    oc delete crd grpcroutes.gateway.networking.k8s.io && \
    oc delete crd httproutes.gateway.networking.k8s.io && \
    oc delete crd referencesgrants.gateway.networking.k8s.io
    ```

    > [!IMPORTANT]
    > Deleting CRDs removes every custom resource that relies on them and can result in data loss. Back up any necessary data before deleting the Gateway API CRDs. Any controller that was previously managing the lifecycle of the Gateway API CRDs will fail to operate properly. Attempting to force its use in conjunction with the Ingress Operator to manage Gateway API CRDs might prevent the cluster update from succeeding.

3.  Get the supported Gateway API CRDs by running the following command:

    ``` terminal
    $ oc apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.2.1/standard-install.yaml
    ```

    > [!WARNING]
    > You can perform this step without deleting your CRDs. If your update to a CRD removes a field that is used by a custom resource, you can lose data. Updating a CRD a second time, to a version that re-adds a field, can cause any previously deleted data to reappear. Any third-party controller that depends on a specific Gateway API CRD version that is not supported in OpenShift Container Platform 4.17 will break upon updating that CRD to one supported by Red Hat.
    >
    > For more information on the OpenShift Container Platform implementation and the dead fields issue, see *Gateway API implementation for OpenShift Container Platform*.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Gateway API implementation for OpenShift Container Platform](../../networking/ingress_load_balancing/configuring_ingress_cluster_traffic/ingress-gateway-api.md#nw-ingress-gateway-api-implementation)

</div>

# Best practices for cluster updates

Follow best practices to ensure successful cluster updates. These best practices include selecting recommended versions, resolving critical alerts, maintaining spare node capacity, and properly configuring pod disruption budgets.

OpenShift Container Platform minimizes workload disruptions during an update. Updates do not begin unless the cluster is in an upgradeable state at the time of the update request.

This design enforces some key conditions before initiating an update, but there are a number of actions you can take to increase your chances of a successful cluster update.

## Choose versions recommended by the OpenShift Update Service

The OpenShift Update Service (OSUS) provides update recommendations based on cluster characteristics such as the cluster’s subscribed channel. The Cluster Version Operator saves these recommendations as either recommended or conditional updates.

While it is possible to attempt an update to a version that is not recommended by OSUS, following a recommended update path protects users from encountering known issues or unintended consequences on the cluster.

Choose only update targets that are recommended by OSUS to ensure a successful update.

## Address all critical alerts on the cluster

Critical alerts must always be addressed as soon as possible, but it is especially important to address these alerts and resolve any problems before initiating a cluster update.

Failing to address critical alerts before beginning an update can cause problematic conditions for the cluster.

In the **Administrator** perspective of the web console, navigate to **Observe** → **Alerting** to find critical alerts.

## Ensure that the cluster is in an Upgradable state

When one or more Operators have not reported their `Upgradeable` condition as `True` for more than an hour, the `ClusterNotUpgradeable` warning alert is triggered in the cluster. In most cases this alert does not block patch updates, but you cannot perform a minor version update until you resolve this alert and all Operators report `Upgradeable` as `True`.

For more information about the `Upgradeable` condition, see "Understanding cluster Operator condition types" in the additional resources section.

### SDN support removal

OpenShift SDN network plugin was deprecated in versions 4.15 and 4.16. With this release, the SDN network plugin is no longer supported and the content has been removed from the documentation.

If your OpenShift Container Platform cluster is still using the OpenShift SDN CNI, see [Migrating from the OpenShift SDN network plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html/networking/ovn-kubernetes-network-plugin#migrate-from-openshift-sdn).

> [!IMPORTANT]
> It is not possible to update a cluster to OpenShift Container Platform 4.17 if it is using the OpenShift SDN network plugin. You must migrate to the OVN-Kubernetes plugin before upgrading to OpenShift Container Platform 4.17.

## Ensure that enough spare nodes are available

A cluster should not be running with little to no spare node capacity, especially when initiating a cluster update. Nodes that are not running and available may limit a cluster’s ability to perform an update with minimal disruption to cluster workloads.

Depending on the configured value of the cluster’s `maxUnavailable` spec, the cluster might not be able to apply machine configuration changes to nodes if there is an unavailable node. Additionally, if compute nodes do not have enough spare capacity, workloads might not be able to temporarily shift to another node while the first node is taken offline for an update.

Make sure that you have enough available nodes in each worker pool, as well as enough spare capacity on your compute nodes, to increase the chance of successful node updates.

> [!WARNING]
> The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.

## Ensure that the cluster’s PodDisruptionBudget is properly configured

You can use the `PodDisruptionBudget` object to define the minimum number or percentage of pod replicas that must be available at any given time. This configuration protects workloads from disruptions during maintenance tasks such as cluster updates.

However, it is possible to configure the `PodDisruptionBudget` for a given topology in a way that prevents nodes from being drained and updated during a cluster update.

When planning a cluster update, check the configuration of the `PodDisruptionBudget` object for the following factors:

- For highly available workloads, make sure there are replicas that can be temporarily taken offline without being prohibited by the `PodDisruptionBudget`.

- For workloads that are not highly available, make sure they are either not protected by a `PodDisruptionBudget` or have some alternative mechanism for draining these workloads eventually, such as periodic restart or guaranteed eventual termination.

<div>

<div class="title">

Additional resources

</div>

- [Understanding cluster Operator condition types](../understanding_updates/intro-to-updates.md#understanding_clusteroperator_conditiontypes_understanding-openshift-updates)

</div>
