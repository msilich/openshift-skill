<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Updates for hosted control planes involve updating the hosted cluster and the node pools.

For a cluster to remain fully operational during an update process, you must meet the requirements of the Kubernetes version skew policy while completing the control plane and node updates. For more information, see "Kubernetes version skew policy".

# Requirements to upgrade hosted control planes

The multicluster engine for Kubernetes Operator can manage one or more OpenShift Container Platform clusters. After you create a hosted cluster on OpenShift Container Platform, you must import your hosted cluster in the multicluster engine Operator as a managed cluster.

You can then use the OpenShift Container Platform cluster as a management cluster.

Consider the following requirements before you start updating hosted control planes:

- You must use the bare metal platform for an OpenShift Container Platform cluster when using OpenShift Virtualization as a provider.

- You must use bare metal or OpenShift Virtualization as the cloud platform for the hosted cluster. You can find the platform type of your hosted cluster in the `spec.Platform.type` specification of the `HostedCluster` custom resource (CR).

> [!IMPORTANT]
> You must update hosted control planes in the following order:
>
> 1.  Upgrade an OpenShift Container Platform cluster to the latest version. For more information, see "Updating a cluster using the web console" or "Updating a cluster using the CLI".
>
> 2.  Upgrade the multicluster engine Operator to the latest version. For more information, see "Updating installed Operators".
>
> 3.  Upgrade the hosted cluster and node pools from the previous OpenShift Container Platform version to the latest version. For more information, see "Updating a control plane in a hosted cluster" and "Updating node pools in a hosted cluster".

<div>

<div class="title">

Additional resources

</div>

- [Updating a cluster using the web console](../updating/updating_a_cluster/updating-cluster-web-console.md#updating-cluster-web-console)

- [Updating a cluster using the CLI](../updating/updating_a_cluster/updating-cluster-cli.md#updating-cluster-cli)

- [Updating installed Operators](../operators/admin/olm-upgrading-operators.md#olm-upgrading-operators)

- [Updating a control plane in a hosted cluster](hcp-updating.md#hcp-update-ocp-hc_hcp-updating)

- [Updating node pools in a hosted cluster](hcp-updating.md#hcp-update-node-pools_hcp-updating)

</div>

# Setting update channels in a hosted cluster

To see available updates for a hosted cluster, you must set the `spec.channel` field on the `HostedCluster` custom resource (CR).

You can see available updates in the `HostedCluster.Status` field of the `HostedCluster` CR.

The available updates are not fetched from the Cluster Version Operator (CVO) of a hosted cluster. The list of the available updates can be different from the available updates from the following fields of the `HostedCluster` custom resource (CR):

- `status.version.availableUpdates`

- `status.version.conditionalUpdates`

The initial `HostedCluster` CR does not have any information in the `status.version.availableUpdates` and `status.version.conditionalUpdates` fields. After you set the `spec.channel` field to the stable OpenShift Container Platform release version, the HyperShift Operator reconciles the `HostedCluster` CR and updates the `status.version` field with the available and conditional updates.

<div>

<div class="title">

Procedure

</div>

1.  In the `HostedCluster` CR, add the channel configuration as shown in the following example:

    ``` yaml
    spec:
      autoscaling: {}
      channel: stable-<4.y>
      clusterID: d6d42268-7dff-4d37-92cf-691bd2d42f41
      configuration: {}
      controllerAvailabilityPolicy: SingleReplica
      dns:
        baseDomain: dev11.red-chesterfield.com
        privateZoneID: Z0180092I0DQRKL55LN0
        publicZoneID: Z00206462VG6ZP0H2QLWK
    ```

    Replace `<4.y>` with the OpenShift Container Platform release version you specified in `spec.release`. For example, if you set the `spec.release` to `ocp-release:4.16.4-multi`, you must set `spec.channel` to `stable-4.16`.

2.  After you configure the channel in the `HostedCluster` CR, to view the output of the `status.version.availableUpdates` and `status.version.conditionalUpdates` fields, run the following command:

    ``` terminal
    $ oc get -n <hosted_cluster_namespace> hostedcluster <hosted_cluster_name> -o yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    version:
      availableUpdates:
      - channels:
        - candidate-4.16
        - candidate-4.17
        - eus-4.16
        - fast-4.16
        - stable-4.16
        image: quay.io/openshift-release-dev/ocp-release@sha256:b7517d13514c6308ae16c5fd8108133754eb922cd37403ed27c846c129e67a9a
        url: https://access.redhat.com/errata/RHBA-2024:6401
        version: 4.16.11
      - channels:
        - candidate-4.16
        - candidate-4.17
        - eus-4.16
        - fast-4.16
        - stable-4.16
        image: quay.io/openshift-release-dev/ocp-release@sha256:d08e7c8374142c239a07d7b27d1170eae2b0d9f00ccf074c3f13228a1761c162
        url: https://access.redhat.com/errata/RHSA-2024:6004
        version: 4.16.10
      - channels:
        - candidate-4.16
        - candidate-4.17
        - eus-4.16
        - fast-4.16
        - stable-4.16
        image: quay.io/openshift-release-dev/ocp-release@sha256:6a80ac72a60635a313ae511f0959cc267a21a89c7654f1c15ee16657aafa41a0
        url: https://access.redhat.com/errata/RHBA-2024:5757
        version: 4.16.9
      - channels:
        - candidate-4.16
        - candidate-4.17
        - eus-4.16
        - fast-4.16
        - stable-4.16
        image: quay.io/openshift-release-dev/ocp-release@sha256:ea624ae7d91d3f15094e9e15037244679678bdc89e5a29834b2ddb7e1d9b57e6
        url: https://access.redhat.com/errata/RHSA-2024:5422
        version: 4.16.8
      - channels:
        - candidate-4.16
        - candidate-4.17
        - eus-4.16
        - fast-4.16
        - stable-4.16
        image: quay.io/openshift-release-dev/ocp-release@sha256:e4102eb226130117a0775a83769fe8edb029f0a17b6cbca98a682e3f1225d6b7
        url: https://access.redhat.com/errata/RHSA-2024:4965
        version: 4.16.6
      - channels:
        - candidate-4.16
        - candidate-4.17
        - eus-4.16
        - fast-4.16
        - stable-4.16
        image: quay.io/openshift-release-dev/ocp-release@sha256:f828eda3eaac179e9463ec7b1ed6baeba2cd5bd3f1dd56655796c86260db819b
        url: https://access.redhat.com/errata/RHBA-2024:4855
        version: 4.16.5
      conditionalUpdates:
      - conditions:
        - lastTransitionTime: "2024-09-23T22:33:38Z"
          message: |-
            Could not evaluate exposure to update risk SRIOVFailedToConfigureVF (creating PromQL round-tripper: unable to load specified CA cert /etc/tls/service-ca/service-ca.crt: open /etc/tls/service-ca/service-ca.crt: no such file or directory)
              SRIOVFailedToConfigureVF description: OCP Versions 4.14.34, 4.15.25, 4.16.7 and ALL subsequent versions include kernel datastructure changes which are not compatible with older versions of the SR-IOV operator. Please update SR-IOV operator to versions dated 20240826 or newer before updating OCP.
              SRIOVFailedToConfigureVF URL: https://issues.redhat.com/browse/NHE-1171
          reason: EvaluationFailed
          status: Unknown
          type: Recommended
        release:
          channels:
          - candidate-4.16
          - candidate-4.17
          - eus-4.16
          - fast-4.16
          - stable-4.16
          image: quay.io/openshift-release-dev/ocp-release@sha256:fb321a3f50596b43704dbbed2e51fdefd7a7fd488ee99655d03784d0cd02283f
          url: https://access.redhat.com/errata/RHSA-2024:5107
          version: 4.16.7
        risks:
        - matchingRules:
          - promql:
              promql: |
                group(csv_succeeded{_id="d6d42268-7dff-4d37-92cf-691bd2d42f41", name=~"sriov-network-operator[.].*"})
                or
                0 * group(csv_count{_id="d6d42268-7dff-4d37-92cf-691bd2d42f41"})
            type: PromQL
          message: OCP Versions 4.14.34, 4.15.25, 4.16.7 and ALL subsequent versions
            include kernel datastructure changes which are not compatible with older
            versions of the SR-IOV operator. Please update SR-IOV operator to versions
            dated 20240826 or newer before updating OCP.
          name: SRIOVFailedToConfigureVF
          url: https://issues.redhat.com/browse/NHE-1171
    ```

    </div>

</div>

# Updates of the OpenShift Container Platform version in a hosted cluster

Hosted control planes enables the decoupling of updates between the control plane and the data plane.

As a cluster service provider or cluster administrator, you can manage the control plane and the data separately.

You can update a control plane by modifying the `HostedCluster` custom resource (CR) and a node by modifying its `NodePool` CR. Both the `HostedCluster` and `NodePool` CRs specify an OpenShift Container Platform release image in a `.release` field.

To keep your hosted cluster fully operational during an update process, the control plane and the node updates must follow the Kubernetes version skew policy.

## The multicluster engine Operator hub management cluster

The multicluster engine for Kubernetes Operator requires a specific OpenShift Container Platform version for the management cluster to remain in a supported state. You can install the multicluster engine Operator from the software catalog in the OpenShift Container Platform web console.

For more information, see the support matrixes for the multicluster engine Operator versions.

The multicluster engine Operator supports the following OpenShift Container Platform versions:

- The latest unreleased version

- The latest released version

- Two versions before the latest released version

You can also get the multicluster engine Operator version as a part of Red Hat Advanced Cluster Management (RHACM).

## Supported OpenShift Container Platform versions in a hosted cluster

When deploying a hosted cluster, the OpenShift Container Platform version of the management cluster does not affect the OpenShift Container Platform version of a hosted cluster.

The HyperShift Operator creates the `supported-versions` ConfigMap in the `hypershift` namespace. The `supported-versions` ConfigMap describes the range of supported OpenShift Container Platform versions that you can deploy.

See the following example of the `supported-versions` ConfigMap:

``` yaml
apiVersion: v1
data:
    server-version: 2f6cfe21a0861dea3130f3bed0d3ae5553b8c28b
    supported-versions: '{"versions":["4.17","4.16","4.15","4.14"]}'
kind: ConfigMap
metadata:
    creationTimestamp: "2024-06-20T07:12:31Z"
    labels:
        hypershift.openshift.io/supported-versions: "true"
    name: supported-versions
    namespace: hypershift
    resourceVersion: "927029"
    uid: f6336f91-33d3-472d-b747-94abae725f70
```

> [!IMPORTANT]
> To create a hosted cluster, you must use the OpenShift Container Platform version from the support version range. However, the multicluster engine Operator can manage only between `n+1` and `n-2` OpenShift Container Platform versions, where `n` defines the current minor version. You can check the multicluster engine Operator support matrix to ensure the hosted clusters managed by the multicluster engine Operator are within the supported OpenShift Container Platform range.

To deploy a higher version of a hosted cluster on OpenShift Container Platform, you must update the multicluster engine Operator to a new minor version release to deploy a new version of the Hypershift Operator. Upgrading the multicluster engine Operator to a new patch, or z-stream, release does not update the HyperShift Operator to the next version.

See the following example output of the `hcp version` command that shows the supported OpenShift Container Platform versions for OpenShift Container Platform 4.16 in the management cluster:

``` terminal
Client Version: openshift/hypershift: fe67b47fb60e483fe60e4755a02b3be393256343. Latest supported OCP: 4.17.0
Server Version: 05864f61f24a8517731664f8091cedcfc5f9b60d
Server Supports OCP Versions: 4.17, 4.16, 4.15, 4.14
```

<div>

<div class="title">

Additional resources

</div>

- [Kubernetes version skew policy](https://kubernetes.io/releases/version-skew-policy/)

- [multicluster engine Operator 2.10](https://access.redhat.com/articles/7133096)

- [multicluster engine Operator 2.9](https://access.redhat.com/articles/7120837)

- [multicluster engine Operator 2.8](https://access.redhat.com/articles/7099674)

- [multicluster engine Operator 2.7](https://access.redhat.com/articles/7086906)

- [multicluster engine Operator 2.6](https://access.redhat.com/articles/7073030)

- [multicluster engine Operator 2.5](https://access.redhat.com/articles/7056007)

- [multicluster engine Operator 2.4](https://access.redhat.com/articles/7027079)

</div>

# Updates for the hosted cluster

The `spec.release.image` value dictates the version of the control plane. The `HostedCluster` object transmits the intended `spec.release.image` value to the `HostedControlPlane.spec.releaseImage` value and runs the appropriate Control Plane Operator version.

The hosted control plane manages the rollout of the new version of the control plane components along with any OpenShift Container Platform components through the new version of the Cluster Version Operator (CVO).

> [!IMPORTANT]
> In hosted control planes, the `NodeHealthCheck` resource cannot detect the status of the CVO. A cluster administrator must manually pause the remediation triggered by `NodeHealthCheck`, before performing critical operations, such as updating the cluster, to prevent new remediation actions from interfering with cluster updates.
>
> To pause the remediation, enter the array of strings, for example, `pause-test-cluster`, as a value of the `pauseRequests` field in the `NodeHealthCheck` resource. For more information, see "About the Node Health Check Operator".
>
> After the cluster update is complete, you can edit or delete the remediation. Go to the **Compute** → **NodeHealthCheck** page, click your node health check, and then click **Actions**, which shows a drop-down list.

<div>

<div class="title">

Additional resources

</div>

- [About the Node Health Check Operator](https://docs.redhat.com/en/documentation/workload_availability_for_red_hat_openshift/24.4/html/remediation_fencing_and_maintenance/node-health-check-operator#about-node-health-check-operator_node-health-check-operator)

</div>

# Updates for node pools

You can update node pools by exposing the `spec.release` and `spec.config` values.

You can start a rolling node pool update in the following ways:

- Changing the `spec.release` or `spec.config` values.

- Changing any platform-specific field, such as the AWS instance type. The result is a set of new instances with the new type.

- Changing the cluster configuration, if the change propagates to the node.

Node pools support replace updates and in-place updates. The `nodepool.spec.release` value dictates the version of any particular node pool. A `NodePool` object completes a replace or an in-place rolling update according to the `.spec.management.upgradeType` value.

After you create a node pool, you cannot change the update type. If you want to change the update type, you must create a node pool and delete the other one.

## Replace updates for node pools

A *replace* update creates instances in the new version while it removes old instances from the previous version. This update type is effective in cloud environments where this level of immutability is cost effective.

Replace updates do not preserve any manual changes because the node is entirely re-provisioned.

## In place updates for node pools

An *in-place* update directly updates the operating systems of the instances. This type is suitable for environments where the infrastructure constraints are greater, such as bare metal.

In-place updates can preserve manual changes, but reports errors if you manually change any file system or operating system configuration that the cluster directly manages, such as kubelet certificates.

# Updating node pools in a hosted cluster

You can update your version of OpenShift Container Platform by updating the node pools in your hosted cluster. The node pool version must not surpass the hosted control plane version.

The `.spec.release` field in the `NodePool` custom resource (CR) shows the version of a node pool.

<div>

<div class="title">

Procedure

</div>

- Change the `spec.release.image` value in the node pool by entering the following command:

  ``` terminal
  $ oc patch nodepool <node_pool_name> -n <hosted_cluster_namespace> \
    --type=merge \
    -p '{"spec":{"nodeDrainTimeout":"60s","release":{"image":"<openshift_release_image>"}}}'
  ```

- Replace `<node_pool_name>` with your node pool name and `<hosted_cluster_namespace>` with your hosted cluster namespace.

- The `<openshift_release_image>` variable specifies the new OpenShift Container Platform release image that you want to upgrade to, for example, `quay.io/openshift-release-dev/ocp-release:<4.y.z>-x86_64`. Replace `<4.y.z>` with the supported OpenShift Container Platform version.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the new version was rolled out, check the `.status.conditions` value in the node pool by running the following command:

  ``` terminal
  $ oc get -n <hosted_cluster_namespace> nodepool <node_pool_name> -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  status:
   conditions:
   - lastTransitionTime: "2024-05-20T15:00:40Z"
         message: 'Using release image: quay.io/openshift-release-dev/ocp-release:4.20.0-x86_64'
         reason: AsExpected
         status: "True"
         type: ValidReleaseImage
  ```

  </div>

</div>

# Updating a control plane in a hosted cluster

In hosted control planes, you can upgrade your version of OpenShift Container Platform by updating the hosted cluster.

The `.spec.release` in the `HostedCluster` custom resource (CR) shows the version of the control plane. The `HostedCluster` updates the `.spec.release` field to the `HostedControlPlane.spec.release` and runs the appropriate Control Plane Operator version.

The `HostedControlPlane` resource orchestrates the rollout of the new version of the control plane components along with the OpenShift Container Platform component in the data plane through the new version of the Cluster Version Operator (CVO). The `HostedControlPlane` includes the following artifacts:

- CVO

- Cluster Network Operator (CNO)

- Cluster Ingress Operator

- Manifests for the Kube API server, scheduler, and manager

- Machine approver

- Autoscaler

- Infrastructure resources to enable ingress for control plane endpoints such as the Kube API server, ignition, and konnectivity

You can set the `.spec.release` field in the `HostedCluster` CR to update the control plane by using the information from the `status.version.availableUpdates` and `status.version.conditionalUpdates` fields.

<div>

<div class="title">

Procedure

</div>

1.  Add the `hypershift.openshift.io/force-upgrade-to=<openshift_release_image>` annotation to the hosted cluster by entering the following command:

    ``` terminal
    $ oc annotate hostedcluster \
      -n <hosted_cluster_namespace> <hosted_cluster_name> \
      "hypershift.openshift.io/force-upgrade-to=<openshift_release_image>" \
      --overwrite
    ```

    - Replace `<hosted_cluster_name>` with your hosted cluster name and `<hosted_cluster_namespace>` with your hosted cluster namespace.

    - The `<openshift_release_image>` variable specifies the new OpenShift Container Platform release image that you want to upgrade to, for example, `quay.io/openshift-release-dev/ocp-release:<4.y.z>-x86_64`. Replace `<4.y.z>` with the supported OpenShift Container Platform version.

2.  Change the `spec.release.image` value in the hosted cluster by entering the following command:

    ``` terminal
    $ oc patch hostedcluster <hosted_cluster_name> -n <hosted_cluster_namespace> \
      --type=merge \
      -p '{"spec":{"release":{"image":"<openshift_release_image>"}}}'
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the new version was rolled out, check the `.status.conditions` and `.status.version` values in the hosted cluster by running the following command:

  ``` terminal
  $ oc get -n <hosted_cluster_namespace> hostedcluster <hosted_cluster_name> \
    -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  status:
   conditions:
   - lastTransitionTime: "2024-05-20T15:01:01Z"
          message: Payload loaded version="4.20.0" image="quay.io/openshift-release-dev/ocp-release:4.20.0-x86_64"
          status: "True"
          type: ClusterVersionReleaseAccepted
  #...
  version:
        availableUpdates: null
        desired:
        image: quay.io/openshift-release-dev/ocp-release:4.20.0-x86_64
        version: 4.20.0
  ```

  </div>

</div>

# Updating a hosted cluster by using the multicluster engine Operator console

You can update your hosted cluster by using the multicluster engine Operator console.

> [!IMPORTANT]
> Before updating a hosted cluster, you must refer to the available and conditional updates of a hosted cluster. Choosing a wrong release version might break the hosted cluster.

<div>

<div class="title">

Procedure

</div>

1.  Select **All clusters**.

2.  Navigate to **Infrastructure** → **Clusters** to view managed hosted clusters.

3.  Click the **Upgrade available** link to update the control plane and node pools.

</div>

# Additional resources

- [Kubernetes version skew policy](https://kubernetes.io/releases/version-skew-policy/)
