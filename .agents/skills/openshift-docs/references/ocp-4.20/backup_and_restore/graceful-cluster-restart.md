<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can restart your OpenShift Container Platform cluster after a graceful shutdown by powering on nodes and verifying cluster health. The cluster returns to normal operations when nodes and Operators are healthy.

Even though the cluster is expected to be functional after the restart, the cluster might not recover due to unexpected conditions:

- etcd data corruption during shutdown

- Node failure due to hardware

- Network connectivity issues

If your cluster fails to recover, follow the steps in "Restoring to an earlier cluster state".

# Restarting the cluster

You can restart the cluster after a graceful shutdown by powering on nodes, uncordoning schedulable nodes, and approving pending certificate signing requests (CSRs) if nodes are not ready. The cluster returns to normal operations after all nodes and Operators are healthy.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have gracefully shut down your cluster.

</div>

If your cluster fails to recover, follow the steps in "Restoring to an earlier cluster state".

<div>

<div class="title">

Procedure

</div>

1.  Turn on the control plane nodes.

    - If you are using the `admin.kubeconfig` from the cluster installation and the API virtual IP address (VIP) is up, complete the following steps:

      1.  Set the `KUBECONFIG` environment variable to the `admin.kubeconfig` path.

      2.  Uncordon each control plane node in the cluster by running the following command:

          ``` terminal
          $ oc adm uncordon <node>
          ```

    - If you do not have access to your `admin.kubeconfig` credentials, complete the following steps:

      1.  Use SSH to connect to a control plane node.

      2.  Copy the `localhost-recovery.kubeconfig` file to the `/root` directory.

      3.  Use that file to uncordon each control plane node in the cluster by running the following command:

          ``` terminal
          $ oc adm uncordon <node>
          ```

2.  Power on any cluster dependencies, such as external storage or a Lightweight Directory Access Protocol (LDAP) server.

3.  Start all cluster machines.

    Use the appropriate method for your cloud environment to start the machines, for example, from the web console for your cloud provider.

    Wait approximately 10 minutes before continuing to check the status of control plane nodes.

4.  Verify that all control plane nodes are ready by running the following command:

    ``` terminal
    $ oc get nodes -l node-role.kubernetes.io/master
    ```

    The control plane nodes are ready if the status is `Ready`, as shown in the following output:

    ``` terminal
    NAME                           STATUS   ROLES                  AGE   VERSION
    ip-10-0-168-251.ec2.internal   Ready    control-plane,master   75m   v1.33.4
    ip-10-0-170-223.ec2.internal   Ready    control-plane,master   75m   v1.33.4
    ip-10-0-211-16.ec2.internal    Ready    control-plane,master   75m   v1.33.4
    ```

5.  If the control plane nodes are not ready, then check whether there are any pending CSRs that must be approved.

    1.  Get the list of current CSRs by running the following command:

        ``` terminal
        $ oc get csr
        ```

    2.  Review the details of each CSR to verify that it is valid by running the following command:

        ``` terminal
        $ oc describe csr <csr_name>
        ```

    3.  Approve each valid CSR by running the following command:

        ``` terminal
        $ oc adm certificate approve <csr_name>
        ```

6.  After the control plane nodes are ready, verify that all compute nodes are ready by running the following command:

    ``` terminal
    $ oc get nodes -l node-role.kubernetes.io/worker
    ```

    The worker nodes are ready if the status is `Ready`, as shown in the following output:

    ``` terminal
    NAME                           STATUS   ROLES    AGE   VERSION
    ip-10-0-179-95.ec2.internal    Ready    worker   64m   v1.33.4
    ip-10-0-182-134.ec2.internal   Ready    worker   64m   v1.33.4
    ip-10-0-250-100.ec2.internal   Ready    worker   64m   v1.33.4
    ```

7.  If the compute nodes are not ready, then check whether there are any pending CSRs that must be approved.

    1.  Get the list of current CSRs by running the following command:

        ``` terminal
        $ oc get csr
        ```

    2.  Review the details of each CSR to verify the validity of the CSR by running the following command:

        ``` terminal
        $ oc describe csr <csr_name>
        ```

    3.  Approve each valid CSR by running the following command:

        ``` terminal
        $ oc adm certificate approve <csr_name>
        ```

8.  After the control plane and compute nodes are ready, mark all the nodes in the cluster as schedulable by running the following command:

    ``` terminal
    $ for node in $(oc get nodes -o jsonpath='{.items[*].metadata.name}'); do echo ${node} ; oc adm uncordon ${node} ; done
    ```

9.  Verify that the cluster started properly.

    1.  Check that there are no degraded cluster Operators by running the following command:

        ``` terminal
        $ oc get clusteroperators
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
        authentication                             4.20.0    True        False         False      59m
        cloud-credential                           4.20.0    True        False         False      85m
        cluster-autoscaler                         4.20.0    True        False         False      73m
        config-operator                            4.20.0    True        False         False      73m
        console                                    4.20.0    True        False         False      62m
        csi-snapshot-controller                    4.20.0    True        False         False      66m
        dns                                        4.20.0    True        False         False      76m
        etcd                                       4.20.0    True        False         False      76m
        ...
        ```

        </div>

    2.  Check that all nodes are in the `Ready` state by running the following command:

        ``` terminal
        $ oc get nodes
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                           STATUS   ROLES                  AGE   VERSION
        ip-10-0-168-251.ec2.internal   Ready    control-plane,master   82m   v1.33.4
        ip-10-0-170-223.ec2.internal   Ready    control-plane,master   82m   v1.33.4
        ip-10-0-179-95.ec2.internal    Ready    worker                 70m   v1.33.4
        ip-10-0-182-134.ec2.internal   Ready    worker                 70m   v1.33.4
        ip-10-0-211-16.ec2.internal    Ready    control-plane,master   82m   v1.33.4
        ip-10-0-250-100.ec2.internal   Ready    worker                 69m   v1.33.4
        ```

        </div>

        If the cluster did not start properly, follow the steps in "Restoring to an earlier cluster state".

</div>

<div>

<div class="title">

Additional resources

</div>

- [Shutting down the cluster gracefully](graceful-cluster-shutdown.md#graceful-shutdown-cluster)

- [Restoring to an earlier cluster state](control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md#dr-restoring-cluster-state)

</div>
