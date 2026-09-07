<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You might need to replace a healthy etcd member for planned hardware maintenance, hardware upgrades, or migration to new infrastructure.

# About replacing a healthy etcd member

To replace a control plane node without disrupting etcd, remove a healthy member and add a replacement while the cluster remains operational. The procedure you follow depends on how your cluster was installed and whether it uses the Machine API and a control plane machine set.

> [!NOTE]
> If the etcd member is unhealthy because the machine is not running, the node is not ready, or the etcd pod is crashlooping, see "Replacing an unhealthy etcd member".
>
> If you have lost the majority of your control plane hosts, see "Restoring to an earlier cluster state".

# Replacing a healthy etcd member

To replace a healthy etcd member without disrupting cluster operations, choose the procedure that matches your control plane configuration. You can use a control plane machine set, the Machine API, or scale up and scale down control plane nodes.

> [!IMPORTANT]
> Take an etcd backup before you replace a healthy etcd member so that you can restore your cluster if any issues occur. For more information, see "Backing up etcd data".

Depending on your cluster configuration, use one of the following procedures:

- Replacing a healthy etcd member with a control plane machine set

- Replacing a healthy etcd member with the Machine API

- Replacing a healthy etcd member by scaling up and scaling down

For clusters that were installed by using the Assisted Installer, see "Replacing a control plane node in a healthy cluster" in the Assisted Installer documentation.

# Determining how to replace a healthy etcd member

To choose the correct procedure for replacing a healthy etcd member, check whether your cluster uses the Assisted Installer, a control plane machine set, or the Machine API. Use the OpenShift CLI (`oc`) to identify your cluster configuration and follow the matching replacement procedure.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- You logged in to `oc` as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check whether the cluster was installed by using the Assisted Installer by running the following command:

    ``` terminal
    $ oc get agentclusterinstall -A
    ```

    - If the command returns one or more `AgentClusterInstall` resources, follow the procedure in "Replacing a control plane node in a healthy cluster" in the Assisted Installer documentation.

    - If the command returns no resources, continue with the following steps.

2.  Check whether the cluster has a control plane machine set by running the following command:

    ``` terminal
    $ oc -n openshift-machine-api get controlplanemachineset
    ```

    - If the command returns a `ControlPlaneMachineSet` resource, follow the procedure in "Replacing a healthy etcd member with a control plane machine set".

    - If the command returns no resources, continue to the next step.

3.  Check whether the cluster has control plane `Machine` objects by running the following command:

    ``` terminal
    $ oc get machines -l machine.openshift.io/cluster-api-machine-role=master -n openshift-machine-api
    ```

    - If `Machine` objects exist, follow the procedure in "Replacing a healthy etcd member with the Machine API".

    - If there are no `Machine` objects, follow the procedure in "Replacing a healthy etcd member by scaling up and scaling down".

</div>

# Replacing a healthy etcd member with a control plane machine set

On clusters that use a control plane machine set, you can replace a healthy control plane machine by deleting the corresponding `Machine` object.

The control plane machine set creates a replacement machine, and the etcd Operator uses machine lifecycle hooks to protect etcd quorum during the replacement.

For more information about how quorum protection works during control plane machine deletion, see "Quorum protection with machine lifecycle hooks".

<div>

<div class="title">

Prerequisites

</div>

- The cluster has a `ControlPlaneMachineSet` resource.

- You have access to the cluster as a user with the `cluster-admin` role.

- You have taken an etcd backup. For more information, see "Backing up etcd data".

  > [!IMPORTANT]
  > Take an etcd backup before you replace a healthy etcd member so that you can restore your cluster if any issues occur.

</div>

<div>

<div class="title">

Procedure

</div>

1.  List the control plane machines in your cluster by running the following command:

    ``` terminal
    $ oc get machines \
      -l machine.openshift.io/cluster-api-machine-role=master \
      -n openshift-machine-api
    ```

2.  Identify the control plane machine that corresponds to the node that you want to replace.

3.  Optional. If you are performing planned maintenance, cordon the node by running the following command:

    ``` terminal
    $ oc adm cordon <node_name>
    ```

    Replace `<node_name>` with the name of the node that you are replacing.

    > [!IMPORTANT]
    > Delete only one control plane machine at a time. Deleting multiple control plane machines at the same time can cause etcd quorum loss.

4.  Delete the control plane machine by running the following command:

    ``` terminal
    $ oc delete machine <control_plane_machine_name> -n openshift-machine-api
    ```

    Replace `<control_plane_machine_name>` with the name of the control plane machine to delete.

    > [!NOTE]
    > If you delete multiple control plane machines, the control plane machine set replaces them according to the configured update strategy:
    >
    > - For clusters that use the default `RollingUpdate` update strategy, the Operator replaces one machine at a time until each machine is replaced.
    >
    > - For clusters that are configured to use the `OnDelete` update strategy, the Operator creates all of the required replacement machines simultaneously.
    >
    > Both strategies maintain etcd health during control plane machine replacement.

5.  Monitor the replacement by running the following commands:

    1.  Verify that a new control plane machine is created:

        ``` terminal
        $ oc get machines \
          -l machine.openshift.io/cluster-api-machine-role=master \
          -n openshift-machine-api -o wide
        ```

    2.  Verify that the etcd cluster Operator reports `Available=True` and `Degraded=False`:

        ``` terminal
        $ oc get clusteroperator etcd
        ```

        > [!NOTE]
        > During the replacement `Progressing=True` is expected and transitions to `False` once the new member is fully reconciled.

    3.  Verify that all control plane nodes are in the `Ready` state:

        ``` terminal
        $ oc get nodes -l node-role.kubernetes.io/control-plane
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify etcd health by running the following commands:

    1.  Open a remote shell session to a control plane etcd pod:

        ``` terminal
        $ oc rsh -n openshift-etcd <etcd_pod_name>
        ```

        Replace `<etcd_pod_name>` with the name of a running etcd pod.

    2.  Check endpoint health:

        ``` terminal
        sh-4.2# etcdctl endpoint health
        ```

        Expected output shows `is healthy` for each endpoint.

    3.  List etcd members and verify that the cluster has three members:

        ``` terminal
        sh-4.2# etcdctl member list -w table
        ```

2.  Verify that all cluster Operators are available by running the following command:

    ``` terminal
    $ oc get clusteroperators
    ```

</div>

# Replacing a healthy etcd member with the Machine API

On clusters that access the Machine API but do not use a control plane machine set, you can replace a healthy control plane machine by deleting the corresponding `Machine` object. The Machine API provisions a replacement machine, and the etcd cluster Operator adds the new node as an etcd member.

<div>

<div class="title">

Prerequisites

</div>

- The cluster has access to the Machine API.

- The cluster does not have a `ControlPlaneMachineSet` resource.

- You have access to the cluster as a user with the `cluster-admin` role.

- You have taken an etcd backup. For more information, see "Backing up etcd data".

  > [!IMPORTANT]
  > Take an etcd backup before you replace a healthy etcd member so that you can restore your cluster if any issues occur.

</div>

<div>

<div class="title">

Procedure

</div>

1.  List the control plane machines in your cluster by running the following command:

    ``` terminal
    $ oc get machines \
      -l machine.openshift.io/cluster-api-machine-role=master \
      -n openshift-machine-api -o wide
    ```

2.  Identify the control plane machine that corresponds to the node that you want to replace.

3.  Optional. If you are performing planned maintenance, cordon the node by running the following command:

    ``` terminal
    $ oc adm cordon <node_name>
    ```

    Replace `<node_name>` with the name of the node that you are replacing.

4.  Delete the control plane machine by running the following command:

    ``` terminal
    $ oc delete machine <control_plane_machine_name> -n openshift-machine-api
    ```

    Replace `<control_plane_machine_name>` with the name of the control plane machine to delete.

    > [!IMPORTANT]
    > Delete only one control plane machine at a time. Deleting multiple control plane machines at the same time can cause etcd quorum loss.

    A new machine is automatically provisioned after you delete the control plane machine.

5.  Monitor the replacement by running the following commands until the new machine reaches the `Running` phase:

    ``` terminal
    $ oc get machines \
      -l machine.openshift.io/cluster-api-machine-role=master \
      -n openshift-machine-api -o wide
    ```

    ``` terminal
    $ oc get clusteroperator etcd
    ```

    ``` terminal
    $ oc get nodes -l node-role.kubernetes.io/control-plane
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify etcd health by running the following commands:

    1.  Open a remote shell session to a control plane etcd pod:

        ``` terminal
        $ oc rsh -n openshift-etcd <etcd_pod_name>
        ```

        Replace `<etcd_pod_name>` with the name of a running etcd pod.

    2.  Check endpoint health:

        ``` terminal
        sh-4.2# etcdctl endpoint health
        ```

        Expected output shows `is healthy` for each endpoint.

    3.  List etcd members and verify that the cluster has three members:

        ``` terminal
        sh-4.2# etcdctl member list -w table
        ```

2.  Verify that all cluster Operators are available by running the following command:

    ``` terminal
    $ oc get clusteroperators
    ```

</div>

# Replacing a healthy etcd member by scaling up and scaling down

On bare-metal clusters that do not use a control plane machine set, replace a healthy control plane node by temporarily scaling the control plane to four nodes, and then removing the node that you want to replace.

> [!IMPORTANT]
> Red Hat supports a cluster that has 4 or 5 control plane nodes only on bare-metal infrastructure.

<div>

<div class="title">

Prerequisites

</div>

- The cluster does not have a `ControlPlaneMachineSet` resource.

- The cluster is installed on bare-metal infrastructure.

- You have access to the cluster as a user with the `cluster-admin` role.

- You have taken an etcd backup. For more information, see "Backing up etcd data".

- You have created a single control plane node that you intend to add to your cluster as a postinstallation task.

  > [!IMPORTANT]
  > Take an etcd backup before you replace a healthy etcd member so that you can restore your cluster if any issues occur.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add the new control plane node to your cluster by following the steps in "Adding a control plane node to your cluster".

2.  Verify that the new control plane node is in the `Ready` state and that etcd has four members by running the following commands:

    ``` terminal
    $ oc get nodes -l node-role.kubernetes.io/control-plane
    ```

    ``` terminal
    $ oc rsh -n openshift-etcd <etcd_pod_name>
    ```

    Replace `<etcd_pod_name>` with the name of a running etcd pod.

    ``` terminal
    sh-4.2# etcdctl member list -w table
    ```

    ``` terminal
    sh-4.2# etcdctl endpoint health
    ```

    Expected output shows four etcd members and `is healthy` for each endpoint.

3.  Remove the control plane node that you want to replace.

    1.  Optional. If you are performing planned maintenance, cordon the node by running the following command:

        ``` terminal
        $ oc adm cordon <node_name>
        ```

        Replace `<node_name>` with the name of the node that you are replacing.

    2.  Delete the `BareMetalHost` object for the control plane node that you want to replace by running the following command:

        ``` terminal
        $ oc delete bmh <node_name> -n openshift-machine-api
        ```

        Replace `<node_name>` with the name of the node that you are replacing.

    3.  Delete the `Machine` object for the control plane node that you want to replace by running the following command:

        ``` terminal
        $ oc delete machine <machine_name> -n openshift-machine-api
        ```

        Replace `<machine_name>` with the name of the machine that is associated with the node that you are replacing.

        > [!NOTE]
        > After you remove the `BareMetalHost` and `Machine` objects, the machine controller automatically deletes the `Node` object.

4.  Monitor the cluster until the control plane returns to three nodes and etcd is healthy by running the following commands:

    ``` terminal
    $ oc get nodes -l node-role.kubernetes.io/control-plane
    ```

    ``` terminal
    $ oc get clusteroperator etcd
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify etcd health by running the following commands:

    1.  Open a remote shell session to a control plane etcd pod:

        ``` terminal
        $ oc rsh -n openshift-etcd <etcd_pod_name>
        ```

    2.  Check endpoint health:

        ``` terminal
        sh-4.2# etcdctl endpoint health
        ```

        Expected output shows `is healthy` for each endpoint.

    3.  List etcd members and verify that the cluster has three members:

        ``` terminal
        sh-4.2# etcdctl member list -w table
        ```

2.  Verify that all cluster Operators are available by running the following command:

    ``` terminal
    $ oc get clusteroperators
    ```

</div>

# Additional resources

- [Backing up etcd data](../../backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.md#backing-up-etcd-data_backup-etcd)

- [Replacing an unhealthy etcd member](../../backup_and_restore/control_plane_backup_and_restore/replacing-unhealthy-etcd-member.md#replacing-unhealthy-etcd-member)

- [Restoring to an earlier cluster state](../../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md#dr-restoring-cluster-state)

- [Replacing a control plane node in a healthy cluster](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2026/html/installing_openshift_container_platform_with_the_assisted_installer/expanding-the-cluster#installing-control-plane-node-healthy-cluster_expanding-the-cluster)

- [Quorum protection with machine lifecycle hooks](../../machine_management/deleting-machine.md#machine-lifecycle-hook-deletion-etcd_deleting-machine)

- [Replacing a control plane machine](../../machine_management/control_plane_machine_management/cpmso-managing-machines.md#cpmso-feat-replace_cpmso-managing-machines)

- [Adding a control plane node to your cluster](../../machine_management/control_plane_machine_management/cpmso-manually-scaling-control-planes.md#creating-control-plane-node_cpmso-manually-scaling-control-planes)

- [How to replace all master nodes in OpenShift Container Platform 4 (Red Hat Knowledgebase article)](https://access.redhat.com/articles/6270901)
