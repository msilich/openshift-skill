<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To restore etcd quorum when a single member is unhealthy, identify the member and determine whether its machine is stopped, its node is not ready, or its pod is crashlooping. You can then follow the replacement procedure that matches that state.

> [!NOTE]
> If you have lost the majority of your control plane hosts, follow the steps in "Restoring to an earlier cluster state" instead of this procedure.
>
> If the control plane certificates are not valid on the member being replaced, then you must follow the steps in "Recovering from expired control plane certificates" instead of this procedure.
>
> If a control plane node is lost and a new one is created, the etcd cluster Operator handles generating the new TLS certificates and adding the node as an etcd member.

Take an etcd backup before replacing an unhealthy etcd member. For more information see, "Backing up etcd data".

# Identifying an unhealthy etcd member

You can identify an unhealthy etcd member by checking the `EtcdMembersAvailable` status condition to see how many members are available and which member is unhealthy.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You created an etcd backup.

</div>

<div>

<div class="title">

Procedure

</div>

- Check the status of the `EtcdMembersAvailable` status condition by running the following command:

  ``` terminal
  $ oc get etcd -o=jsonpath='{range .items[0].status.conditions[?(@.type=="EtcdMembersAvailable")]}{"\n"}{end}'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  2 of 3 members are available, ip-10-0-131-183.ec2.internal is unhealthy
  ```

  </div>

</div>

# Determining the state of the unhealthy etcd member

Determine whether the unhealthy etcd member has a stopped machine, an unready node, or a crashlooping etcd pod. Knowing the failure state enables you to follow the correct replacement procedure.

Depending on the state of your unhealthy etcd member, use one of the following procedures:

- Machine not running or node not ready. For more information, see "Replacing an unhealthy etcd member whose machine is not running or whose node is not ready".

- Bare-metal machine not running or node not ready on installer-provisioned bare metal. For more information, see "Replacing an unhealthy bare metal etcd member whose machine is not running or whose node is not ready".

- Crashlooping etcd pod. For more information, see "Replacing an unhealthy etcd member whose etcd pod is crashlooping".

> [!NOTE]
> If the machine is not running or the node is not ready, you might expect either to recover soon. In that case, you do not need to replace the etcd member. The etcd cluster Operator automatically syncs when the machine or node returns to a healthy state.

<div>

<div class="title">

Prerequisites

</div>

- You confirmed access to the cluster as a user with the `cluster-admin` role.

- You identified an unhealthy etcd member.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Determine if the machine is not running by running the following command:

    ``` terminal
    $ oc get machines -A -ojsonpath='{range .items[*]}{@.status.nodeRef.name}{"\t"}{@.status.providerStatus.instanceState}{"\n"}' | grep -v running
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ip-10-0-131-183.ec2.internal  stopped
    ```

    </div>

    This output lists the node and the status of the machine of the node. If the status is anything other than `running`, then the machine is not running.

2.  Determine if the status of the node is `NotReady`.

    If either of the following scenarios are true, then the node is not ready.

    1.  If the machine is running, then check whether the node has an `unreachable` taint by running the following command:

        ``` terminal
        $ oc get nodes -o jsonpath='{range .items[*]}{"\n"}{.metadata.name}{"\t"}{range .spec.taints[*]}{" "}' | grep unreachable
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        ip-10-0-131-183.ec2.internal node-role.kubernetes.io/master node.kubernetes.io/unreachable node.kubernetes.io/unreachable
        ```

        </div>

        If the node is listed with an `unreachable` taint, then the node is not ready.

    2.  If the node is still reachable, then check whether the node is listed as `NotReady` by running the following command:

        ``` terminal
        $ oc get nodes -l node-role.kubernetes.io/master | grep "NotReady"
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        ip-10-0-131-183.ec2.internal   NotReady   master   122m   v1.35.4
        ```

        </div>

        If the node is listed as `NotReady`, then the node is not ready.

        If the **node is not ready**, then follow the "Replacing an unhealthy etcd member whose machine is not running or whose node is not ready" procedure.

3.  Determine if the etcd pod is crashlooping.

    If the machine is running and the node status is `Ready`, check the status of the etcd pod.

    1.  Verify that all control plane nodes are listed as `Ready` by running the following command:

        ``` terminal
        $ oc get nodes -l node-role.kubernetes.io/master
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                           STATUS   ROLES    AGE     VERSION
        ip-10-0-131-183.ec2.internal   Ready    master   6h13m   v1.35.4
        ip-10-0-164-97.ec2.internal    Ready    master   6h13m   v1.35.4
        ip-10-0-154-204.ec2.internal   Ready    master   6h13m   v1.35.4
        ```

        </div>

    2.  Check whether the status of an etcd pod is either `Error` or `CrashloopBackoff` by running the following command:

        ``` terminal
        $ oc -n openshift-etcd get pods -l k8s-app=etcd
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        etcd-ip-10-0-131-183.ec2.internal                2/3     Error       7          6h9m
        etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          6h6m
        etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          6h6m
        ```

        </div>

        The etcd pod crashloops because the `etcd-ip-10-0-131-183.ec2.internal` is `Error`.

        If the **etcd pod is crashlooping**, then follow the steps in "Replacing an unhealthy etcd member whose etcd pod is crashlooping".

</div>

# Replacing the unhealthy etcd member

You can replace an unhealthy etcd member by following one of several procedures, depending on whether the machine is not running, the node is not ready, the etcd pod is crashlooping, or the member is a stopped bare-metal instance.

Use one of the following procedures, based on the state of your unhealthy etcd member:

- [Replacing an unhealthy etcd member whose machine is not running or whose node is not ready](replacing-unhealthy-etcd-member.md#restore-replace-stopped-etcd-member_replacing-unhealthy-etcd-member)

- [Replacing a control plane node in an unhealthy cluster](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2026/html/installing_openshift_container_platform_with_the_assisted_installer/expanding-the-cluster#installing-control-plane-node-unhealthy-cluster_expanding-the-cluster)

- [Replacing an unhealthy etcd member whose etcd pod is crashlooping](replacing-unhealthy-etcd-member.md#restore-replace-crashlooping-etcd-member_replacing-unhealthy-etcd-member)

- [Replacing an unhealthy stopped baremetal etcd member](replacing-unhealthy-etcd-member.md#restore-replace-stopped-baremetal-etcd-member_replacing-unhealthy-etcd-member)

## Replacing an unhealthy etcd member whose machine is not running or whose node is not ready

Replace an unhealthy etcd member when the member machine is stopped or the node is not ready. Restoring the member returns the control plane to a healthy state.

> [!NOTE]
> If your cluster uses a control plane machine set, see "Recovering a degraded etcd Operator" in "Troubleshooting the control plane machine set" for an etcd recovery procedure.

<div>

<div class="title">

Prerequisites

</div>

- You identified the unhealthy etcd member.

- You verified that either the machine is not running or the node is not ready.

- Do not power on other control plane nodes until the unhealthy etcd member replacement is complete.

- You confirmed access to the cluster as a user with the `cluster-admin` role.

- You created an etcd backup before replacing the unhealthy etcd member.

  > [!IMPORTANT]
  > Without a recent etcd backup, you might not be able to restore the cluster if replacement fails.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Remove the unhealthy member.

    1.  List etcd pods and choose one that is not on the affected node by running the following command:

        ``` terminal
        $ oc -n openshift-etcd get pods -l k8s-app=etcd
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        etcd-ip-10-0-131-183.ec2.internal                3/3     Running     0          123m
        etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          123m
        etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          124m
        ```

        </div>

        From the output, note a pod that is not on the affected node. In this example, the unhealthy member is `ip-10-0-131-183.ec2.internal`, so you could use `etcd-ip-10-0-154-204.ec2.internal`.

    2.  Connect to the running etcd container on the pod you chose by running the following command:

        ``` terminal
        $ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
        ```

    3.  View the member list by running the following command:

        ``` terminal
        sh-4.2# etcdctl member list -w table
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        |        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        | 6fc1e7c9db35841d | started | ip-10-0-131-183.ec2.internal | https://10.0.131.183:2380 | https://10.0.131.183:2379 |
        | 757b6793e2408b6c | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
        | ca8c2990a0aa29d1 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        ```

        </div>

        Take note of the ID and the name of the unhealthy etcd member because you need these values later in the procedure. The `etcdctl endpoint health` command continues to list the removed member until replacement is complete and a new member is added.

    4.  Remove the unhealthy etcd member by providing the ID to the `etcdctl member remove` command by running the following command:

        ``` terminal
        sh-4.2# etcdctl member remove <etcd_member_id>
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Member 6fc1e7c9db35841d removed from cluster ead669ce1fbfb346
        ```

        </div>

    5.  View the member list again and verify that the member was removed by running the following command:

        ``` terminal
        sh-4.2# etcdctl member list -w table
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        |        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        | 757b6793e2408b6c | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
        | ca8c2990a0aa29d1 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        ```

        </div>

        You can now exit the node shell.

2.  Turn off the quorum guard by running the following command:

    ``` terminal
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
    ```

    This command ensures that you can successfully re-create secrets and roll out the static pods.

    > [!IMPORTANT]
    > After you turn off the quorum guard, the cluster might be unreachable for a short period of time while the remaining etcd instances reboot to reflect the configuration change.

    > [!NOTE]
    > etcd cannot tolerate any additional member failure when running with two members. Restarting either remaining member breaks the quorum and causes downtime in your cluster. The quorum guard protects etcd from restarts due to configuration changes that could cause downtime, so it must be disabled to complete this procedure.

3.  Delete the affected node by running the following command:

    ``` terminal
    $ oc delete node <node_name>
    ```

    <div class="formalpara">

    <div class="title">

    Example command

    </div>

    ``` terminal
    $ oc delete node ip-10-0-131-183.ec2.internal
    ```

    </div>

4.  Remove the old secrets for the unhealthy etcd member that was removed.

    1.  List the secrets for the unhealthy etcd member that was removed by running the following command:

        ``` terminal
        $ oc get secrets -n openshift-etcd | grep ip-10-0-131-183.ec2.internal
        ```

        Replace `ip-10-0-131-183.ec2.internal` in the command with the name of the unhealthy etcd member that you noted earlier in this procedure.

        There is a peer, serving, and metrics secret as shown in the following output:

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        etcd-peer-ip-10-0-131-183.ec2.internal              kubernetes.io/tls                     2      47m
        etcd-serving-ip-10-0-131-183.ec2.internal           kubernetes.io/tls                     2      47m
        etcd-serving-metrics-ip-10-0-131-183.ec2.internal   kubernetes.io/tls                     2      47m
        ```

        </div>

    2.  Delete the peer secret by running the following command:

        ``` terminal
        $ oc delete secret -n openshift-etcd etcd-peer-ip-10-0-131-183.ec2.internal
        ```

    3.  Delete the serving secret by running the following command:

        ``` terminal
        $ oc delete secret -n openshift-etcd etcd-serving-ip-10-0-131-183.ec2.internal
        ```

    4.  Delete the metrics secret by running the following command:

        ``` terminal
        $ oc delete secret -n openshift-etcd etcd-serving-metrics-ip-10-0-131-183.ec2.internal
        ```

5.  Check whether a control plane machine set exists by running the following command:

    ``` terminal
    $ oc -n openshift-machine-api get controlplanemachineset
    ```

    If the control plane machine set exists, delete and re-create the control plane machine. After this machine is re-created, a new revision is forced and etcd scales up automatically. For more information, see "Replacing an unhealthy etcd member whose machine is not running or whose node is not ready".

    If you are running installer-provisioned infrastructure, or you used the Machine API to create your machines, follow these steps. Otherwise, you must create the new control plane by using the same method that was used to originally create it.

    1.  Obtain the machine for the unhealthy member by running the following command.

        ``` terminal
        $ oc get machines -n openshift-machine-api -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                                        PHASE     TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
        clustername-8qw5l-master-0                  Running   m4.xlarge   us-east-1   us-east-1a   3h37m   ip-10-0-131-183.ec2.internal   aws:///us-east-1a/i-0ec2782f8287dfb7e   stopped
        clustername-8qw5l-master-1                  Running   m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
        clustername-8qw5l-master-2                  Running   m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
        clustername-8qw5l-worker-us-east-1a-wbtgd   Running   m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
        clustername-8qw5l-worker-us-east-1b-lrdxb   Running   m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
        clustername-8qw5l-worker-us-east-1c-pkg26   Running   m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
        ```

        </div>

        In the example output, `clustername-8qw5l-master-0` is the control plane machine for the unhealthy node `ip-10-0-131-183.ec2.internal`. Its `STATE` is `stopped`.

    2.  Delete the machine of the unhealthy member by running the following command:

        ``` terminal
        $ oc delete machine -n openshift-machine-api clustername-8qw5l-master-0
        ```

        Replace `clustername-8qw5l-master-0` with the name of the control plane machine for the unhealthy node.

        A new machine is automatically provisioned after deleting the machine of the unhealthy member.

    3.  Verify that a new machine was created by running the following command:

        ``` terminal
        $ oc get machines -n openshift-machine-api -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                                        PHASE          TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
        clustername-8qw5l-master-1                  Running        m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
        clustername-8qw5l-master-2                  Running        m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
        clustername-8qw5l-master-3                  Provisioning   m4.xlarge   us-east-1   us-east-1a   85s     ip-10-0-133-53.ec2.internal    aws:///us-east-1a/i-015b0888fe17bc2c8   running
        clustername-8qw5l-worker-us-east-1a-wbtgd   Running        m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
        clustername-8qw5l-worker-us-east-1b-lrdxb   Running        m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
        clustername-8qw5l-worker-us-east-1c-pkg26   Running        m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
        ```

        </div>

        In the example output, `clustername-8qw5l-master-3` is the new control plane machine. The machine is ready when the `PHASE` changes from `Provisioning` to `Running`.

        It might take a few minutes for the new machine to be created. The etcd cluster Operator automatically syncs when the machine or node returns to a healthy state.

        > [!NOTE]
        > Verify the subnet IDs that you are using for your machine sets to ensure that they end up in the correct availability zone.

        If the control plane machine set does not exist, delete and re-create the control plane machine. After this machine is re-created, a new revision is forced and etcd scales up automatically.

        If you are running installer-provisioned infrastructure, or you used the Machine API to create your machines, follow these steps. Otherwise, you must create the new control plane by using the same method that was used to originally create it.

    4.  Obtain the machine for the unhealthy member by running the following command:

        ``` terminal
        $ oc get machines -n openshift-machine-api -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                                        PHASE     TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
        clustername-8qw5l-master-0                  Running   m4.xlarge   us-east-1   us-east-1a   3h37m   ip-10-0-131-183.ec2.internal   aws:///us-east-1a/i-0ec2782f8287dfb7e   stopped
        clustername-8qw5l-master-1                  Running   m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
        clustername-8qw5l-master-2                  Running   m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
        clustername-8qw5l-worker-us-east-1a-wbtgd   Running   m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
        clustername-8qw5l-worker-us-east-1b-lrdxb   Running   m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
        clustername-8qw5l-worker-us-east-1c-pkg26   Running   m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
        ```

        </div>

        In the example output, `clustername-8qw5l-master-0` is the control plane machine for the unhealthy node `ip-10-0-131-183.ec2.internal`. Its `STATE` is `stopped`.

    5.  Save the machine configuration to a file on your file system by running the following command:

        ``` terminal
        $ oc get machine clustername-8qw5l-master-0 \
            -n openshift-machine-api \
            -o yaml \
            > new-master-machine.yaml
        ```

        Replace `clustername-8qw5l-master-0` with the name of the control plane machine for the unhealthy node.

6.  Edit the `new-master-machine.yaml` file that was created in the previous step to assign a new name and remove unnecessary fields:

    1.  Remove the entire `status` section:

        ``` yaml
        status:
          addresses:
          - address: 10.0.131.183
            type: InternalIP
          - address: ip-10-0-131-183.ec2.internal
            type: InternalDNS
          - address: ip-10-0-131-183.ec2.internal
            type: Hostname
          lastUpdated: "2020-04-20T17:44:29Z"
          nodeRef:
            kind: Node
            name: ip-10-0-131-183.ec2.internal
            uid: acca4411-af0d-4387-b73e-52b2484295ad
          phase: Running
          providerStatus:
            apiVersion: awsproviderconfig.openshift.io/v1beta1
            conditions:
            - lastProbeTime: "2020-04-20T16:53:50Z"
              lastTransitionTime: "2020-04-20T16:53:50Z"
              message: machine successfully created
              reason: MachineCreationSucceeded
              status: "True"
              type: MachineCreation
            instanceId: i-0fdb85790d76d0c3f
            instanceState: stopped
            kind: AWSMachineProviderStatus
        ```

    2.  Change the `metadata.name` field to a new name.

        For example:

        ``` yaml
        apiVersion: machine.openshift.io/v1beta1
        kind: Machine
        metadata:
          ...
          name: clustername-8qw5l-master-3
          ...
        ```

        Keep the same base name as the old machine and change the ending number to the next available number. In this example, `clustername-8qw5l-master-0` is changed to `clustername-8qw5l-master-3`

    3.  Remove the `spec.providerID` field:

        ``` yaml
          providerID: aws:///us-east-1a/i-0fdb85790d76d0c3f
        ```

7.  Delete the machine of the unhealthy member by running the following command:

    ``` terminal
    $ oc delete machine -n openshift-machine-api clustername-8qw5l-master-0
    ```

    In the command, replace `clustername-8qw5l-master-0` with the control plane machine name for the unhealthy node that you identified in the example output above.

8.  Verify that the machine was deleted by running the following command:

    ``` terminal
    $ oc get machines -n openshift-machine-api -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                        PHASE     TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
    clustername-8qw5l-master-1                  Running   m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
    clustername-8qw5l-master-2                  Running   m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
    clustername-8qw5l-worker-us-east-1a-wbtgd   Running   m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
    clustername-8qw5l-worker-us-east-1b-lrdxb   Running   m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
    clustername-8qw5l-worker-us-east-1c-pkg26   Running   m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
    ```

    </div>

9.  Create the new machine by using the `new-master-machine.yaml` file by running the following command:

    ``` terminal
    $ oc apply -f new-master-machine.yaml
    ```

10. Verify that the new machine was created by running the following command:

    ``` terminal
    $ oc get machines -n openshift-machine-api -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                        PHASE          TYPE        REGION      ZONE         AGE     NODE                           PROVIDERID                              STATE
    clustername-8qw5l-master-1                  Running        m4.xlarge   us-east-1   us-east-1b   3h37m   ip-10-0-154-204.ec2.internal   aws:///us-east-1b/i-096c349b700a19631   running
    clustername-8qw5l-master-2                  Running        m4.xlarge   us-east-1   us-east-1c   3h37m   ip-10-0-164-97.ec2.internal    aws:///us-east-1c/i-02626f1dba9ed5bba   running
    clustername-8qw5l-master-3                  Provisioning   m4.xlarge   us-east-1   us-east-1a   85s     ip-10-0-133-53.ec2.internal    aws:///us-east-1a/i-015b0888fe17bc2c8   running
    clustername-8qw5l-worker-us-east-1a-wbtgd   Running        m4.large    us-east-1   us-east-1a   3h28m   ip-10-0-129-226.ec2.internal   aws:///us-east-1a/i-010ef6279b4662ced   running
    clustername-8qw5l-worker-us-east-1b-lrdxb   Running        m4.large    us-east-1   us-east-1b   3h28m   ip-10-0-144-248.ec2.internal   aws:///us-east-1b/i-0cb45ac45a166173b   running
    clustername-8qw5l-worker-us-east-1c-pkg26   Running        m4.large    us-east-1   us-east-1c   3h28m   ip-10-0-170-181.ec2.internal   aws:///us-east-1c/i-06861c00007751b0a   running
    ```

    </div>

    In the example output, `clustername-8qw5l-master-3` is the new control plane machine. The machine is ready when the `PHASE` changes from `Provisioning` to `Running`.

    It might take a few minutes for the new machine to be created. The etcd cluster Operator automatically syncs when the machine or node returns to a healthy state.

11. Turn the quorum guard back on by running the following command:

    ``` terminal
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
    ```

12. You can verify that the `unsupportedConfigOverrides` section is removed from the object by running the following command:

    ``` terminal
    $ oc get etcd/cluster -oyaml
    ```

13. If you are using single-node OpenShift, restart the node. Otherwise, you might experience the following error in the etcd cluster Operator:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    EtcdCertSignerControllerDegraded: [Operation cannot be fulfilled on secrets "etcd-peer-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-metrics-sno-0": the object has been modified; please apply your changes to the latest version and try again]
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that all etcd pods are running properly by running the following command:

    ``` terminal
    $ oc -n openshift-etcd get pods -l k8s-app=etcd
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    etcd-ip-10-0-133-53.ec2.internal                 3/3     Running     0          7m49s
    etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          123m
    etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          124m
    ```

    </div>

2.  If the output from the previous command lists only two pods, force an etcd redeployment by running the following command:

    ``` terminal
    $ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$( date --rfc-3339=ns )"'"}}' --type=merge
    ```

    The `forceRedeploymentReason` value must be unique, which is why a timestamp is appended in the example.

3.  Verify that there are exactly three etcd members.

    1.  Connect to the running etcd container, passing in the name of a pod that was not on the affected node by running the following command:

        ``` terminal
        $ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
        ```

    2.  View the member list by running the following command:

        ``` terminal
        sh-4.2# etcdctl member list -w table
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        |        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        | 5eb0d6b8ca24730c | started |  ip-10-0-133-53.ec2.internal |  https://10.0.133.53:2380 |  https://10.0.133.53:2379 |
        | 757b6793e2408b6c | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
        | ca8c2990a0aa29d1 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        ```

        </div>

        If the output from the previous command lists more than three etcd members, you must carefully remove the unwanted member.

        > [!WARNING]
        > Be sure to remove the correct etcd member; removing a good etcd member might lead to quorum loss.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Recovering a degraded etcd Operator](../../machine_management/control_plane_machine_management/cpmso-troubleshooting.md#cpmso-ts-etcd-degraded_cpmso-troubleshooting)

</div>

## Replacing an unhealthy etcd member whose etcd pod is crashlooping

Replace an unhealthy etcd member when the etcd pod is crashlooping. Restoring the member returns the control plane to a healthy state.

<div>

<div class="title">

Prerequisites

</div>

- You identified the unhealthy etcd member.

- You verified that the etcd pod is crashlooping.

- You confirmed access to the cluster as a user with the `cluster-admin` role.

- You created an etcd backup before replacing the unhealthy etcd member.

  > [!IMPORTANT]
  > It is important to take an etcd backup before performing this procedure so that your cluster can be restored if you encounter any issues.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Stop the crashlooping etcd pod.

    1.  Debug the node that is crashlooping by running the following command:

        ``` terminal
        $ oc debug node/<unhealthy_node>
        ```

        Replace `<unhealthy_node>` with the name of the unhealthy etcd member.

    2.  Change your root directory to `/host` by running the following command:

        ``` terminal
        sh-4.2# chroot /host
        ```

    3.  Create a backup directory by running the following command:

        ``` terminal
        sh-4.2# mkdir /var/lib/etcd-backup
        ```

2.  Move the existing etcd pod file out of the kubelet manifest directory by running the following commands:

    ``` terminal
    sh-4.2# mv /etc/kubernetes/manifests/etcd-pod.yaml /var/lib/etcd-backup/
    ```

    1.  Move the etcd data directory to a different location by running the following command:

        ``` terminal
        sh-4.2# mv /var/lib/etcd/ /tmp
        ```

        You can now exit the node shell.

3.  Remove the unhealthy member.

    1.  Choose a pod that is *not* on the affected node by running the following command:

        ``` terminal
        $ oc -n openshift-etcd get pods -l k8s-app=etcd
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        etcd-ip-10-0-131-183.ec2.internal                2/3     Error       7          6h9m
        etcd-ip-10-0-164-97.ec2.internal                 3/3     Running     0          6h6m
        etcd-ip-10-0-154-204.ec2.internal                3/3     Running     0          6h6m
        ```

        </div>

    2.  Connect to the running etcd container, passing in the name of a pod that is not on the affected node by running the following command:

        ``` terminal
        $ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
        ```

    3.  View the member list by running the following command:

        ``` terminal
        sh-4.2# etcdctl member list -w table
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        |        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        | 62bcf33650a7170a | started | ip-10-0-131-183.ec2.internal | https://10.0.131.183:2380 | https://10.0.131.183:2379 |
        | b78e2856655bc2eb | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
        | d022e10b498760d5 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        ```

        </div>

        Take note of the ID and the name of the unhealthy etcd member, because these values are needed later in the procedure.

    4.  Remove the unhealthy etcd member by providing the ID to the `etcdctl member remove` command:

        ``` terminal
        sh-4.2# etcdctl member remove 62bcf33650a7170a
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Member 62bcf33650a7170a removed from cluster ead669ce1fbfb346
        ```

        </div>

    5.  View the member list again and verify that the member was removed by running the following command:

        ``` terminal
        sh-4.2# etcdctl member list -w table
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        |        ID        | STATUS  |             NAME             |        PEER ADDRS         |       CLIENT ADDRS        |
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        | b78e2856655bc2eb | started |  ip-10-0-164-97.ec2.internal |  https://10.0.164.97:2380 |  https://10.0.164.97:2379 |
        | d022e10b498760d5 | started | ip-10-0-154-204.ec2.internal | https://10.0.154.204:2380 | https://10.0.154.204:2379 |
        +------------------+---------+------------------------------+---------------------------+---------------------------+
        ```

        </div>

        You can now exit the node shell.

4.  Turn off the quorum guard by running the following command:

    ``` terminal
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
    ```

    This command ensures that you can successfully re-create secrets and roll out the static pods.

5.  Remove the old secrets for the unhealthy etcd member that was removed.

    1.  List the secrets for the unhealthy etcd member that was removed by running the following command:

        ``` terminal
        $ oc get secrets -n openshift-etcd | grep <unhealthy_node>
        ```

        Replace `<unhealthy_node>` in the command with the name of the unhealthy etcd member that you noted earlier in this procedure.

        There is a peer, serving, and metrics secret as shown in the following output:

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        etcd-peer-ip-10-0-131-183.ec2.internal              kubernetes.io/tls                     2      47m
        etcd-serving-ip-10-0-131-183.ec2.internal           kubernetes.io/tls                     2      47m
        etcd-serving-metrics-ip-10-0-131-183.ec2.internal   kubernetes.io/tls                     2      47m
        ```

        </div>

    2.  Delete the peer secret for the unhealthy etcd member that was removed by running the following command:

        ``` terminal
        $ oc delete secret -n openshift-etcd etcd-peer-ip-10-0-131-183.ec2.internal
        ```

    3.  Delete the serving secret by running the following command:

        ``` terminal
        $ oc delete secret -n openshift-etcd etcd-serving-ip-10-0-131-183.ec2.internal
        ```

    4.  Delete the metrics secret by running the following command:

        ``` terminal
        $ oc delete secret -n openshift-etcd etcd-serving-metrics-ip-10-0-131-183.ec2.internal
        ```

6.  Force etcd redeployment by running the following command:

    ``` terminal
    $ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "single-master-recovery-'"$( date --rfc-3339=ns )"'"}}' --type=merge
    ```

    The `forceRedeploymentReason` value must be unique, which is why a timestamp is appended.

    When the etcd cluster Operator performs a redeployment, it ensures that all control plane nodes have a functioning etcd pod.

7.  Turn the quorum guard back on by running the following command:

    ``` terminal
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
    ```

8.  Verify that the `unsupportedConfigOverrides` section is removed from the object by running the following command:

    ``` terminal
    $ oc get etcd/cluster -oyaml
    ```

9.  If you are using single-node OpenShift, restart the node. Otherwise, you might encounter the following error in the etcd cluster Operator:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    EtcdCertSignerControllerDegraded: [Operation cannot be fulfilled on secrets "etcd-peer-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-metrics-sno-0": the object has been modified; please apply your changes to the latest version and try again]
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the new member is available and healthy.

  - Connect to the running etcd container by running the following command:

    ``` terminal
    $ oc rsh -n openshift-etcd etcd-ip-10-0-154-204.ec2.internal
    ```

  - Verify that all members are healthy by running the following command:

    ``` terminal
    sh-4.2# etcdctl endpoint health
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    https://10.0.131.183:2379 is healthy: successfully committed proposal: took = 16.671434ms
    https://10.0.154.204:2379 is healthy: successfully committed proposal: took = 16.698331ms
    https://10.0.164.97:2379 is healthy: successfully committed proposal: took = 16.621645ms
    ```

    </div>

</div>

## Replacing an unhealthy bare metal etcd member whose machine is not running or whose node is not ready

Replace an unhealthy bare metal etcd member when the machine is not running or the node is not ready. Restoring the member returns the control plane to a healthy state.

If you are running installer-provisioned infrastructure or you used the Machine API to create your machines, follow these steps. Otherwise you must create the new control plane node using the same method that was used to originally create it.

<div>

<div class="title">

Prerequisites

</div>

- You identified the unhealthy bare metal etcd member.

- You verified that either the machine is not running or the node is not ready.

- You confirmed access to the cluster as a user with the `cluster-admin` role.

- You created an etcd backup.

  > [!IMPORTANT]
  > You must take an etcd backup before performing this procedure so that your cluster can be restored if you encounter any issues.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify and remove the unhealthy member.

    1.  Choose a pod that is not on the affected node by running the following command:

        ``` terminal
        $ oc -n openshift-etcd get pods -l k8s-app=etcd -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        etcd-openshift-control-plane-0   5/5   Running   11   3h56m   192.168.10.9   openshift-control-plane-0  <none>           <none>
        etcd-openshift-control-plane-1   5/5   Running   0    3h54m   192.168.10.10   openshift-control-plane-1   <none>           <none>
        etcd-openshift-control-plane-2   5/5   Running   0    3h58m   192.168.10.11   openshift-control-plane-2   <none>           <none>
        ```

        </div>

    2.  Connect to the running etcd container, passing in the name of a pod that is not on the affected node by running the following command:

        ``` terminal
        $ oc rsh -n openshift-etcd etcd-openshift-control-plane-0
        ```

    3.  View the member list by running the following command:

        ``` terminal
        sh-4.2# etcdctl member list -w table
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        +------------------+---------+--------------------+---------------------------+---------------------------+---------------------+
        | ID               | STATUS  | NAME                      | PEER ADDRS                  | CLIENT ADDRS                | IS LEARNER |
        +------------------+---------+--------------------+---------------------------+---------------------------+---------------------+
        | 7a8197040a5126c8 | started | openshift-control-plane-2 | https://192.168.10.11:2380/ | https://192.168.10.11:2379/ | false |
        | 8d5abe9669a39192 | started | openshift-control-plane-1 | https://192.168.10.10:2380/ | https://192.168.10.10:2379/ | false |
        | cc3830a72fc357f9 | started | openshift-control-plane-0 | https://192.168.10.9:2380/ | https://192.168.10.9:2379/   | false |
        +------------------+---------+--------------------+---------------------------+---------------------------+---------------------+
        ```

        </div>

        Take note of the ID and the name of the unhealthy etcd member, because these values are required later in the procedure. The `etcdctl endpoint health` command lists the removed member until the replacement procedure is completed and the new member is added.

        > [!WARNING]
        > Be sure to remove the correct etcd member. Removing a good etcd member might lead to quorum loss.

    4.  Remove the unhealthy etcd member by providing the ID to the `etcdctl member remove` command:

        ``` terminal
        sh-4.2# etcdctl member remove 7a8197040a5126c8
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Member 7a8197040a5126c8 removed from cluster b23536c33f2cdd1b
        ```

        </div>

    5.  View the member list again and verify that the member was removed by running the following command:

        ``` terminal
        sh-4.2# etcdctl member list -w table
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        +------------------+---------+--------------------+---------------------------+---------------------------+-------------------------+
        | ID               | STATUS  | NAME                      | PEER ADDRS                  | CLIENT ADDRS                | IS LEARNER |
        +------------------+---------+--------------------+---------------------------+---------------------------+-------------------------+
        | cc3830a72fc357f9 | started | openshift-control-plane-2 | https://192.168.10.11:2380/ | https://192.168.10.11:2379/ | false |
        | 8d5abe9669a39192 | started | openshift-control-plane-1 | https://192.168.10.10:2380/ | https://192.168.10.10:2379/ | false |
        +------------------+---------+--------------------+---------------------------+---------------------------+-------------------------+
        ```

        </div>

        You can now exit the node shell.

        > [!IMPORTANT]
        > After you remove the member, the cluster might be unreachable for a short time while the remaining etcd instances reboot.

2.  Turn off the quorum guard by running the following command:

    ``` terminal
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": {"useUnsupportedUnsafeNonHANonProductionUnstableEtcd": true}}}'
    ```

    This command ensures that you can successfully re-create secrets and roll out the static pods.

3.  Remove the old secrets for the unhealthy etcd member that was removed.

    1.  List the secrets for the unhealthy etcd member that was removed by running the following command:

        ``` terminal
        $ oc get secrets -n openshift-etcd | grep openshift-control-plane-2
        ```

        Pass in the name of the unhealthy etcd member that you took note of earlier in this procedure.

        There is a peer, serving, and metrics secret as shown in the following output:

        ``` terminal
        etcd-peer-openshift-control-plane-2             kubernetes.io/tls   2   134m
        etcd-serving-metrics-openshift-control-plane-2  kubernetes.io/tls   2   134m
        etcd-serving-openshift-control-plane-2          kubernetes.io/tls   2   134m
        ```

    2.  Delete the secrets for the unhealthy etcd member by running the following command:

        ``` terminal
        $ oc delete secret etcd-peer-openshift-control-plane-2 -n openshift-etcd
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        secret "etcd-peer-openshift-control-plane-2" deleted
        ```

        </div>

    3.  Delete the serving secret by running the following command:

        ``` terminal
        $ oc delete secret etcd-serving-metrics-openshift-control-plane-2 -n openshift-etcd
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        secret "etcd-serving-metrics-openshift-control-plane-2" deleted
        ```

        </div>

    4.  Delete the metrics secret by running the following command:

        ``` terminal
        $ oc delete secret etcd-serving-openshift-control-plane-2 -n openshift-etcd
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        secret "etcd-serving-openshift-control-plane-2" deleted
        ```

        </div>

4.  Obtain the machine for the unhealthy member by running the following command:

    ``` terminal
    $ oc get machines -n openshift-machine-api -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                              PHASE     TYPE   REGION   ZONE   AGE     NODE                               PROVIDERID                                                                                              STATE
    examplecluster-control-plane-0    Running                          3h11m   openshift-control-plane-0   baremetalhost:///openshift-machine-api/openshift-control-plane-0/da1ebe11-3ff2-41c5-b099-0aa41222964e   externally provisioned
    examplecluster-control-plane-1    Running                          3h11m   openshift-control-plane-1   baremetalhost:///openshift-machine-api/openshift-control-plane-1/d9f9acbc-329c-475e-8d81-03b20280a3e1   externally provisioned
    examplecluster-control-plane-2    Running                          3h11m   openshift-control-plane-2   baremetalhost:///openshift-machine-api/openshift-control-plane-2/3354bdac-61d8-410f-be5b-6a395b056135   externally provisioned
    examplecluster-compute-0          Running                          165m    openshift-compute-0         baremetalhost:///openshift-machine-api/openshift-compute-0/3d685b81-7410-4bb3-80ec-13a31858241f         provisioned
    examplecluster-compute-1          Running                          165m    openshift-compute-1         baremetalhost:///openshift-machine-api/openshift-compute-1/0fdae6eb-2066-4241-91dc-e7ea72ab13b9         provisioned
    ```

    </div>

    `examplecluster-control-plane-2` is the control plane machine for the unhealthy node `openshift-control-plane-2`.

5.  Ensure that the Bare Metal Operator is available by running the following command:

    ``` terminal
    $ oc get clusteroperator baremetal
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
    baremetal   4.22.0    True        False         False      3d15h
    ```

    </div>

6.  Remove the old `BareMetalHost` object by running the following command:

    ``` terminal
    $ oc delete bmh openshift-control-plane-2 -n openshift-machine-api
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    baremetalhost.metal3.io "openshift-control-plane-2" deleted
    ```

    </div>

7.  Delete the machine of the unhealthy member by running the following command:

    ``` terminal
    $ oc delete machine -n openshift-machine-api examplecluster-control-plane-2
    ```

    After you remove the `BareMetalHost` and `Machine` objects, then the `Machine` controller automatically deletes the `Node` object.

    If deletion of the machine is delayed for any reason or the command is obstructed and delayed, you can force deletion by removing the machine object finalizer field.

    > [!IMPORTANT]
    > Do not interrupt machine deletion by pressing `Ctrl+c`. You must allow the command to proceed to completion. Open a new terminal window to edit and delete the finalizer fields.

    A new machine is automatically provisioned after deleting the machine of the unhealthy member.

    1.  Edit the machine configuration by running the following command:

        ``` terminal
        $ oc edit machine -n openshift-machine-api examplecluster-control-plane-2
        ```

    2.  Delete the following fields in the `Machine` custom resource, and then save the updated file:

        ``` yaml
        finalizers:
        - machine.machine.openshift.io
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        machine.machine.openshift.io/examplecluster-control-plane-2 edited
        ```

        </div>

8.  Verify that the machine was deleted by running the following command:

    ``` terminal
    $ oc get machines -n openshift-machine-api -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                              PHASE     TYPE   REGION   ZONE   AGE     NODE                                 PROVIDERID                                                                                       STATE
    examplecluster-control-plane-0    Running                          3h11m   openshift-control-plane-0   baremetalhost:///openshift-machine-api/openshift-control-plane-0/da1ebe11-3ff2-41c5-b099-0aa41222964e   externally provisioned
    examplecluster-control-plane-1    Running                          3h11m   openshift-control-plane-1   baremetalhost:///openshift-machine-api/openshift-control-plane-1/d9f9acbc-329c-475e-8d81-03b20280a3e1   externally provisioned
    examplecluster-compute-0          Running                          165m    openshift-compute-0         baremetalhost:///openshift-machine-api/openshift-compute-0/3d685b81-7410-4bb3-80ec-13a31858241f         provisioned
    examplecluster-compute-1          Running                          165m    openshift-compute-1         baremetalhost:///openshift-machine-api/openshift-compute-1/0fdae6eb-2066-4241-91dc-e7ea72ab13b9         provisioned
    ```

    </div>

9.  Verify that the node has been deleted by running the following command:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                     STATUS ROLES   AGE   VERSION
    openshift-control-plane-0 Ready master 3h24m v1.35.4
    openshift-control-plane-1 Ready master 3h24m v1.35.4
    openshift-compute-0       Ready worker 176m v1.35.4
    openshift-compute-1       Ready worker 176m v1.35.4
    ```

    </div>

10. Create the new `BareMetalHost` object and the secret to store the Baseboard Management Controller (BMC) credentials by running the following command:

    ``` terminal
    $ cat <<EOF | oc apply -f -
    apiVersion: v1
    kind: Secret
    metadata:
      name: openshift-control-plane-2-bmc-secret
      namespace: openshift-machine-api
    data:
      password: <password>
      username: <username>
    type: Opaque
    ---
    apiVersion: metal3.io/v1alpha1
    kind: BareMetalHost
    metadata:
      name: openshift-control-plane-2
      namespace: openshift-machine-api
    spec:
      automatedCleaningMode: disabled
      bmc:
        address: redfish://10.46.61.18:443/redfish/v1/Systems/1
        credentialsName: openshift-control-plane-2-bmc-secret
        disableCertificateVerification: true
      bootMACAddress: 48:df:37:b0:8a:a0
      bootMode: UEFI
      externallyProvisioned: false
      online: true
      rootDeviceHints:
        deviceName: /dev/disk/by-id/scsi-<serial_number>
      userData:
        name: master-user-data-managed
        namespace: openshift-machine-api
    EOF
    ```

    > [!NOTE]
    > The username and password can be found from the secrets of the other bare-metal host. The protocol to use in `bmc:address` can be taken from other bmh objects.

    > [!IMPORTANT]
    > If you reuse the `BareMetalHost` object definition from an existing control plane host, do not leave the `externallyProvisioned` field set to `true`.
    >
    > Existing control plane `BareMetalHost` objects may have the `externallyProvisioned` flag set to `true` if they were provisioned by the OpenShift Container Platform installation program.

    After the inspection is complete, the `BareMetalHost` object is created and available to be provisioned.

11. Verify the creation process using available `BareMetalHost` objects by running the following command:

    ``` terminal
    $ oc get bmh -n openshift-machine-api
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                      STATE                  CONSUMER                      ONLINE ERROR   AGE
    openshift-control-plane-0 externally provisioned examplecluster-control-plane-0 true         4h48m
    openshift-control-plane-1 externally provisioned examplecluster-control-plane-1 true         4h48m
    openshift-control-plane-2 available              examplecluster-control-plane-3 true         47m
    openshift-compute-0       provisioned            examplecluster-compute-0       true         4h48m
    openshift-compute-1       provisioned            examplecluster-compute-1       true         4h48m
    ```

    </div>

    1.  Verify that a new machine has been created by running the following command:

        ``` terminal
        $ oc get machines -n openshift-machine-api -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                                   PHASE     TYPE   REGION   ZONE   AGE     NODE                              PROVIDERID                                                                                            STATE
        examplecluster-control-plane-0         Running                          3h11m   openshift-control-plane-0   baremetalhost:///openshift-machine-api/openshift-control-plane-0/da1ebe11-3ff2-41c5-b099-0aa41222964e   externally provisioned
        examplecluster-control-plane-1         Running                          3h11m   openshift-control-plane-1   baremetalhost:///openshift-machine-api/openshift-control-plane-1/d9f9acbc-329c-475e-8d81-03b20280a3e1   externally provisioned
        examplecluster-control-plane-2         Running                          3h11m   openshift-control-plane-2   baremetalhost:///openshift-machine-api/openshift-control-plane-2/3354bdac-61d8-410f-be5b-6a395b056135   externally provisioned
        examplecluster-compute-0               Running                          165m    openshift-compute-0         baremetalhost:///openshift-machine-api/openshift-compute-0/3d685b81-7410-4bb3-80ec-13a31858241f         provisioned
        examplecluster-compute-1               Running                          165m    openshift-compute-1         baremetalhost:///openshift-machine-api/openshift-compute-1/0fdae6eb-2066-4241-91dc-e7ea72ab13b9         provisioned
        ```

        </div>

        The new machine is ready when the phase changes from `Provisioning` to `Running`.

        It should take a few minutes for the new machine to be created. The etcd cluster Operator automatically syncs when the machine or node returns to a healthy state.

    2.  Verify that the bare metal host becomes provisioned and no error reported by running the following command:

        ``` terminal
        $ oc get bmh -n openshift-machine-api
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                      STATE                  CONSUMER                       ONLINE ERROR AGE
        openshift-control-plane-0 externally provisioned examplecluster-control-plane-0 true         4h48m
        openshift-control-plane-1 externally provisioned examplecluster-control-plane-1 true         4h48m
        openshift-control-plane-2 provisioned            examplecluster-control-plane-3 true          47m
        openshift-compute-0       provisioned            examplecluster-compute-0       true         4h48m
        openshift-compute-1       provisioned            examplecluster-compute-1       true         4h48m
        ```

        </div>

    3.  Verify that the new node is added and in a ready state by running the following command:

        ``` terminal
        $ oc get nodes
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                     STATUS ROLES   AGE   VERSION
        openshift-control-plane-0 Ready master 4h26m v1.35.4
        openshift-control-plane-1 Ready master 4h26m v1.35.4
        openshift-control-plane-2 Ready master 12m   v1.35.4
        openshift-compute-0       Ready worker 3h58m v1.35.4
        openshift-compute-1       Ready worker 3h58m v1.35.4
        ```

        </div>

12. Turn the quorum guard back on by running the following command:

    ``` terminal
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"unsupportedConfigOverrides": null}}'
    ```

13. You can verify that the `unsupportedConfigOverrides` section is removed from the object by running the following command:

    ``` terminal
    $ oc get etcd/cluster -oyaml
    ```

14. If you are using single-node OpenShift, restart the node. Otherwise, you might encounter the following error in the etcd cluster Operator:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    EtcdCertSignerControllerDegraded: [Operation cannot be fulfilled on secrets "etcd-peer-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-sno-0": the object has been modified; please apply your changes to the latest version and try again, Operation cannot be fulfilled on secrets "etcd-serving-metrics-sno-0": the object has been modified; please apply your changes to the latest version and try again]
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that all etcd pods are running properly by running the following command:

    ``` terminal
    $ oc -n openshift-etcd get pods -l k8s-app=etcd
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    etcd-openshift-control-plane-0      5/5     Running     0     105m
    etcd-openshift-control-plane-1      5/5     Running     0     107m
    etcd-openshift-control-plane-2      5/5     Running     0     103m
    ```

    </div>

    If the output from the previous command only lists two pods, you can manually force an etcd redeployment. In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:

    ``` terminal
    $ oc patch etcd cluster -p='{"spec": {"forceRedeploymentReason": "recovery-'"$( date --rfc-3339=ns )"'"}}' --type=merge
    ```

    The `forceRedeploymentReason` value must be unique, which is why a timestamp is appended.

    To verify there are exactly three etcd members, connect to the running etcd container, passing in the name of a pod that was not on the affected node. In a terminal that has access to the cluster as a `cluster-admin` user, run the following command:

    ``` terminal
    $ oc rsh -n openshift-etcd etcd-openshift-control-plane-0
    ```

2.  View the member list by running the following command:

    ``` terminal
    sh-4.2# etcdctl member list -w table
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    +------------------+---------+--------------------+---------------------------+---------------------------+-----------------+
    |        ID        | STATUS  |        NAME        |        PEER ADDRS         |       CLIENT ADDRS        |    IS LEARNER    |
    +------------------+---------+--------------------+---------------------------+---------------------------+-----------------+
    | 7a8197040a5126c8 | started | openshift-control-plane-2 | https://192.168.10.11:2380 | https://192.168.10.11:2379 |   false |
    | 8d5abe9669a39192 | started | openshift-control-plane-1 | https://192.168.10.10:2380 | https://192.168.10.10:2379 |   false |
    | cc3830a72fc357f9 | started | openshift-control-plane-0 | https://192.168.10.9:2380 | https://192.168.10.9:2379 |     false |
    +------------------+---------+--------------------+---------------------------+---------------------------+-----------------+
    ```

    </div>

    > [!NOTE]
    > If the output from the previous command lists more than three etcd members, you must carefully remove the unwanted member.

3.  Verify that all etcd members are healthy by running the following command:

    ``` terminal
    # etcdctl endpoint health --cluster
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    https://192.168.10.10:2379 is healthy: successfully committed proposal: took = 8.973065ms
    https://192.168.10.9:2379 is healthy: successfully committed proposal: took = 11.559829ms
    https://192.168.10.11:2379 is healthy: successfully committed proposal: took = 11.665203ms
    ```

    </div>

4.  Validate that all nodes are at the latest revision by running the following command:

    ``` terminal
    $ oc get etcd -o=jsonpath='{range.items[0].status.conditions[?(@.type=="NodeInstallerProgressing")]}{"\n"}{"\n"}'
    ```

        AllNodesAtLatestRevision

</div>

# Additional resources

- [Restoring to an earlier cluster state](disaster_recovery/scenario-2-restoring-cluster-state.md#dr-restoring-cluster-state)

- [Recovering from expired control plane certificates](disaster_recovery/scenario-3-expired-certs.md#dr-recovering-expired-certs)

- [etcd backup](backing-up-etcd.md#backing-up-etcd-data_backup-etcd)

- [Quorum protection with machine lifecycle hooks](../../machine_management/deleting-machine.md#machine-lifecycle-hook-deletion-etcd_deleting-machine)
