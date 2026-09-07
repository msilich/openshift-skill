<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Optimize etcd reliability and scalability by understanding hardware, network, and cluster factors that affect control plane performance, from storage latency to API transaction rates.

# Leader election and log replication of etcd

etcd uses Raft leader election and log replication so the cluster stays consistent during writes. Understanding how the leader handles quorum requests helps you diagnose control plane latency and write failures.

etcd is a consistent, distributed key-value store that operates as a cluster of replicated nodes. Following the Raft algorithm, etcd operates by electing one node as the leader and the others as followers. The leader maintains the system’s current state and ensures that the followers are up-to-date.

The leader node is responsible for log replication. It handles incoming write transactions from the client and writes a Raft log entry that it then broadcasts to the followers.

When an etcd client such as `kube-apiserver` connects to an etcd member that is requesting an action that requires a quorum, such as writing a value, if the etcd member is a follower, it returns a message indicating the transaction should be sent to the leader.

When the etcd client requests an action that requires a quorum from the leader, the leader keeps the client connection open while it writes the local Raft log, broadcasts the log to the followers, and waits for the majority of the followers to acknowledge to have committed the log without failures. Only then does the leader send the acknowledgment to the etcd client and close the session. If failure notifications are received from the followers and the majority fails to reach a consensus, the leader returns the error message to the client and closes the session.

<div>

<div class="title">

Additional resources

</div>

- [The etcd learner design](https://etcd.io/docs/v3.5/learning/design-learner/)

- [Failure modes](https://etcd.io/docs/v3.5/op-guide/failures/)

</div>

# Node scaling for etcd

In general, clusters must have 3 control plane nodes. However, if your cluster is installed on a bare metal platform, it can have up to 5 control plane nodes. If your bare-metal cluster has fewer than 5 control plane nodes, you can scale up the cluster as a postinstallation task.

For example, to scale from 3 to 4 control plane nodes after installation, you can add a host and install it as a control plane node. Then, the etcd Operator scales accordingly to account for the additional control plane node.

Scaling a cluster to 4 or 5 control plane nodes is available only on bare metal platforms.

For more information about how to scale control plane nodes by using the Assisted Installer, see "Adding hosts" and "Replacing a control plane node in a healthy cluster".

> [!NOTE]
> While adding control plane nodes can increase reliability and availability, it can decrease throughput and increase latency, affecting performance.

The following table shows failure tolerance for clusters of different sizes:

| Cluster size | Majority | Failure tolerance |
|--------------|----------|-------------------|
| 1 node       | 1        | 0                 |
| 3 nodes      | 2        | 1                 |
| 4 nodes      | 3        | 1                 |
| 5 nodes      | 3        | 2                 |

Failure tolerances by cluster size

For more information about recovering from quorum loss, see "Restoring to an earlier cluster state".

<div>

<div class="title">

Additional resources

</div>

- [Adding hosts](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2026/html/installing_openshift_container_platform_with_the_assisted_installer/installing-with-api#adding-hosts_installing-with-api)

- [Replacing a control plane node in a healthy cluster](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2026/html/installing_openshift_container_platform_with_the_assisted_installer/expanding-the-cluster#installing-control-plane-node-healthy-cluster_expanding-the-cluster)

- [Expanding the cluster](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2026/html/installing_openshift_container_platform_with_the_assisted_installer/expanding-the-cluster)

- [Restoring to an earlier cluster state](../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md#dr-restoring-cluster-state)

</div>

# Managing etcd size by limiting the duration of Kubernetes events

To manage etcd size, you can set the maximum time that Kubernetes events are stored in the etcd database of the Kubernetes API server. By specifying the `eventTTLMinutes` property, you can control how long events are stored in the etcd database before they are purged.

The `eventTTLMinutes` property is managed through the `KubeAPIServer` custom resource, which is maintained by the Kube API Server Operator.

<div>

<div class="title">

Procedure

</div>

1.  Edit the `KubeAPIServer` custom resource by entering the following command:

    ``` terminal
    $ oc patch kubeapiserver/cluster -p='{"spec": {"eventTTLMinutes": 5 }}' --type=merge
    ```

    The value for the `eventTTLMinutes` property specifies how many minutes events are stored in the etcd database. Valid values are `5` - `180`.

2.  Save the changes to the `KubeAPIServer` custom resource.

    The Kube API Server Operator automatically reconciles the change, which involves rolling out new configurations to the Kube API Server pods.

3.  Wait for the rollout to finish by entering the following command:

    ``` terminal
    $ oc adm wait-for-stable-cluster
    ```

    The following example shows the output that is displayed during that process:

    ``` terminal
    ...
    clusteroperators/kube-apiserver is still progressing after 10s
    ...
    clusteroperators/kube-apiserver stabilized at 2025-11-12T12:02:40+01:00 after 9m0s
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the configuration was applied, enter the following command:

  ``` terminal
  $ oc get cm config -n openshift-kube-apiserver -ojsonpath='{.data.config\.yaml}' | jq -r ".apiServerArguments[\"event-ttl\"][0]"
  ```

  The output shows the configured duration, which is 5m in the following example:

  ``` terminal
  5m
  ```

  > [!NOTE]
  > Only newly created events are written to etcd by using the new value for the `eventTTLMinutes` property. Older, existing events are not updated and will expire according to any previously specified TTL values.

- To manually verify that a given event was written with a shorter lease, examine the lease directly on etcd by entering the following command:

  ``` terminal
  $ oc exec -it pods/<etcd_pod_name> -n openshift-etcd -c etcdctl -- sh
  ```

  The output of the command looks similar to the following example:

  ``` terminal
  sh-5.1h# $ etcdctl lease list | xargs -I {} etcdctl lease timetolive {}
  lease 1e6e9a77a71d8235 granted with TTL(15s), remaining(1s)
  lease 1e6e9a77a71d8247 granted with TTL(15s), remaining(3s)
  lease 1e6e9a77a71d8252 granted with TTL(15s), remaining(3s)
  lease 1e6e9a77a71d8310 granted with TTL(15s), remaining(11s)
  lease 1e6e9a77a71d8332 granted with TTL(15s), remaining(12s)
  lease 1e6e9a77a71d833e granted with TTL(15s), remaining(13s)
  lease 086e9a77a31f0776 granted with TTL(315s), remaining(177s)
  lease 086e9a779dcd8245 granted with TTL(10860s), remaining(8369s)
  lease 086e9a779dcd8fdf granted with TTL(10860s), remaining(8369s)
  ```

  > [!NOTE]
  > Other API objects can also have leases.

- To inspect the attached keys, filter for the key prefix of the event by entering the following command:

  ``` terminal
  $ etcdctl lease list | xargs -I {} etcdctl lease timetolive --keys {} | grep "/kubernetes.io/events"
  ```

  The output looks similar to the following example:

  ``` terminal
  lease 0f009a77a48509ac granted with TTL(315s), remaining(74s), attached keys([/kubernetes.io/events/openshift-marketplace/redhat-operators-rrq79.18773e905b3e29a8 /kubernetes.io/events/openshift-marketplace/community-operators-csds7.18773e91b1e551a3])
  ...
  ...
  lease 1e6e9a77a71d3df1 granted with TTL(10860s), remaining(9478s), attached keys([/kubernetes.io/events/openshift-kube-apiserver/kube-apiserver-guard-ci-ln-pbkb71t-72292-dwp9h-master-2.18773c38ef4dcc03])
  ```

  In the example, the TTL value is 5 minutes (`300s`), but the output shows `315s` because a lease buffer reuse of 5% is added.

  > [!NOTE]
  > If a lease can be reused, etcd reuses it. Instead of creating a unique etcd lease for every resource that requires a `TTL` property, which would force the API server to track thousands of separate objects, the system reuses a smaller pool of existing leases. When a new object needs a lease for a specific duration, the manager checks for an existing lease that still has enough remaining life to cover that duration, plus a small safety buffer of 5%. If a match is found, the new object uses that existing lease. If not, a new lease is created and added to the pool for others to share.

</div>

# Effects of disk latency on etcd

etcd performance depends heavily on disk latency for fsync operations. Validate storage with `fio` before deployment so you avoid instability, failed writes, and service-affecting control plane events.

An etcd cluster is sensitive to disk latencies. To understand the disk latency that is experienced by etcd in your control plane environment, run the `fio` tests or suite.

Ensure that the final report classifies the disk as appropriate for etcd, as shown in the following example:

``` terminal
...
99th percentile of fsync is 5865472 ns
99th percentile of the fsync is within the recommended threshold: - 20 ms, the disk can be used to host etcd
```

When a high latency disk is used, a message states that the disk is not recommended for etcd, as shown in the following example:

``` terminal
...
99th percentile of fsync is 15865472 ns
99th percentile of the fsync is greater than the recommended value which is 20 ms, faster disks are recommended to host etcd for better performance
```

When you use cluster deployments that span multiple data centers that are using disks for etcd that do not meet the recommended latency, it increases the chances of service-affecting failures and dramatically reduces the network latency that the control plane can sustain.

# Monitoring consensus latency for etcd

Use the `etcdctl` command-line interface (CLI) to check endpoint health and consensus latency on a running cluster. Regular monitoring helps you spot delays before they cause leader elections and Kubernetes API instability.

By using the `etcdctl` CLI, you can monitor the latency for reaching consensus as experienced by etcd. You must identify one of the etcd pods and then retrieve the endpoint health.

This procedure, which validates and monitors cluster health, can be run only on an active cluster.

<div>

<div class="title">

Prerequisites

</div>

- During planning for cluster deployment, you completed the disk and network tests.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enter the following command:

    ``` terminal
    # oc get pods -n openshift-etcd -l app=etcd
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME      READY   STATUS    RESTARTS   AGE
    etcd-m0   4/4     Running   4          8h
    etcd-m1   4/4     Running   4          8h
    etcd-m2   4/4     Running   4          8h
    ```

    </div>

2.  Enter the following command. To better understand the etcd latency for consensus, run this command on a precise watch cycle for a few minutes. Observe that the numbers remain below the ~66 ms threshold. The closer the consensus time is to 100 ms, the more likely the cluster experiences service-affecting events and instability.

    ``` terminal
    # oc exec -ti etcd-m0 -- etcdctl endpoint health -w table
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    +----------------------------+--------+-------------+-------+
    |          ENDPOINT          | HEALTH |    TOOK     | ERROR |
    +----------------------------+--------+-------------+-------+
    | https://198.18.111.12:2379 |   true |  3.798349ms |       |
    | https://198.18.111.14:2379 |   true |  7.389608ms |       |
    | https://198.18.111.13:2379 |   true |  6.263117ms |       |
    +----------------------------+--------+-------------+-------+
    ```

    </div>

3.  Enter the following command:

    ``` terminal
    # oc exec -ti etcd-m0 -- watch -dp -c etcdctl endpoint health -w table
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    +----------------------------+--------+-------------+-------+
    |          ENDPOINT          | HEALTH |    TOOK     | ERROR |
    +----------------------------+--------+-------------+-------+
    | https://198.18.111.12:2379 |   true |  9.533405ms |       |
    | https://198.18.111.13:2379 |   true |  4.628054ms |       |
    | https://198.18.111.14:2379 |   true |  5.803378ms |       |
    +----------------------------+--------+-------------+-------+
    ```

    </div>

</div>

# Moving etcd to a different disk

Move etcd data from a shared disk to a dedicated disk to resolve or prevent performance problems. Isolating etcd storage reduces latency from competing I/O on the control plane.

You can move etcd from a shared disk to a separate disk to prevent or resolve performance issues.

The Machine Config Operator (MCO) is responsible for mounting a secondary disk for OpenShift Container Platform 4.22 container storage.

> [!NOTE]
> This encoded script only supports device names for the following device types:
>
> - SCSI or SATA: `/dev/sd*`
>
> - Virtual device: `/dev/vd*`
>
> - NVMe: `/dev/nvme*[0-9]*n*`

When the new disk is attached to the cluster, the etcd database is part of the root mount. It is not part of the secondary disk or the intended disk when the primary node is recreated. As a result, the primary node does not create a separate `/var/lib/etcd` mount.

<div>

<div class="title">

Prerequisites

</div>

- You have a backup of your cluster’s etcd data.

- You have installed the OpenShift CLI (`oc`).

- You have access to the cluster with `cluster-admin` privileges.

- You have attached additional disks before uploading the machine configuration.

- The `MachineConfigPool` matches `metadata.labels[machineconfiguration.openshift.io/role]`. This applies to a controller, worker, or a custom pool.

</div>

> [!NOTE]
> This procedure does not move parts of the root file system, such as `/var/`, to another disk or partition on an installed node.

> [!IMPORTANT]
> This procedure is not supported when using control plane machine sets.

<div>

<div class="title">

Procedure

</div>

1.  Attach the new disk to the cluster and verify that the disk is detected in the node by running the `lsblk` command in a debug shell:

    ``` terminal
    $ oc debug node/<node_name>
    ```

    ``` terminal
    # lsblk
    ```

    Note the device name of the new disk reported by the `lsblk` command.

2.  Create the following script and name it `etcd-find-secondary-device.sh`:

    ``` bash
    #!/bin/bash
    set -uo pipefail

    for device in <device_type_glob>; do
    /usr/sbin/blkid "${device}" &> /dev/null
     if [ $? == 2  ]; then
        echo "secondary device found ${device}"
        echo "creating filesystem for etcd mount"
        mkfs.xfs -L var-lib-etcd -f "${device}" &> /dev/null
        udevadm settle
        touch /etc/var-lib-etcd-mount
        exit
     fi
    done
    echo "Couldn't find secondary block device!" >&2
    exit 77
    ```

    Replace `<device_type_glob>` with a shell glob for your block device type. For SCSI or SATA drives, use `/dev/sd*`; for virtual drives, use `/dev/vd*`; for NVMe drives, use `/dev/nvme*[0-9]*n*`.

3.  Create a base64-encoded string from the `etcd-find-secondary-device.sh` script and note its contents:

    ``` terminal
    $ base64 -w0 etcd-find-secondary-device.sh
    ```

4.  Create a `MachineConfig` YAML file named `etcd-mc.yml` with contents such as the following example:

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfig
    metadata:
      labels:
        machineconfiguration.openshift.io/role: master
      name: 98-var-lib-etcd
    spec:
      config:
        ignition:
          version: 3.5.0
        storage:
          files:
            - path: /etc/find-secondary-device
              mode: 0755
              contents:
                source: data:text/plain;charset=utf-8;base64,<encoded_etcd_find_secondary_device_script>
        systemd:
          units:
            - name: find-secondary-device.service
              enabled: true
              contents: |
                [Unit]
                Description=Find secondary device
                DefaultDependencies=false
                After=systemd-udev-settle.service
                Before=local-fs-pre.target
                ConditionPathExists=!/etc/var-lib-etcd-mount

                [Service]
                RemainAfterExit=yes
                ExecStart=/etc/find-secondary-device

                RestartForceExitStatus=77

                [Install]
                WantedBy=multi-user.target
            - name: var-lib-etcd.mount
              enabled: true
              contents: |
                [Unit]
                Before=local-fs.target

                [Mount]
                What=/dev/disk/by-label/var-lib-etcd
                Where=/var/lib/etcd
                Type=xfs
                TimeoutSec=120s

                [Install]
                RequiredBy=local-fs.target
            - name: sync-var-lib-etcd-to-etcd.service
              enabled: true
              contents: |
                [Unit]
                Description=Sync etcd data if new mount is empty
                DefaultDependencies=no
                After=var-lib-etcd.mount var.mount
                Before=crio.service

                [Service]
                Type=oneshot
                RemainAfterExit=yes
                ExecCondition=/usr/bin/test ! -d /var/lib/etcd/member
                ExecStart=/usr/sbin/setsebool -P rsync_full_access 1
                ExecStart=/bin/rsync -ar /sysroot/ostree/deploy/rhcos/var/lib/etcd/ /var/lib/etcd/
                ExecStart=/usr/sbin/semanage fcontext -a -t container_var_lib_t '/var/lib/etcd(/.*)?'
                ExecStart=/usr/sbin/setsebool -P rsync_full_access 0
                TimeoutSec=0

                [Install]
                WantedBy=multi-user.target graphical.target
            - name: restorecon-var-lib-etcd.service
              enabled: true
              contents: |
                [Unit]
                Description=Restore recursive SELinux security contexts
                DefaultDependencies=no
                After=var-lib-etcd.mount
                Before=crio.service

                [Service]
                Type=oneshot
                RemainAfterExit=yes
                ExecStart=/sbin/restorecon -R /var/lib/etcd/
                TimeoutSec=0

                [Install]
                WantedBy=multi-user.target graphical.target
    ```

    Replace `<encoded_etcd_find_secondary_device_script>` with the encoded script contents that you noted.

5.  Apply the created `MachineConfig` YAML file:

    ``` terminal
    $ oc create -f etcd-mc.yml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Run the `grep /var/lib/etcd /proc/mounts` command in a debug shell for the node to ensure that the disk is mounted:

  ``` terminal
  $ oc debug node/<node_name>
  ```

  ``` terminal
  # grep -w "/var/lib/etcd" /proc/mounts
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  /dev/sdb /var/lib/etcd xfs rw,seclabel,relatime,attr2,inode64,logbufs=8,logbsize=32k,noquota 0 0
  ```

  </div>

</div>

# Data defragmentation for etcd

To prevent etcd performance degradation and cluster-wide maintenance alarms on large clusters, monitor etcd database metrics and defragment the data store when the keyspace grows too large.

For large and dense clusters, etcd can suffer from poor performance if the keyspace grows too large and exceeds the space quota. Periodically maintain and defragment etcd to free up space in the data store. Monitor Prometheus for etcd metrics and defragment it when required. Otherwise, etcd can raise a cluster-wide alarm that puts the cluster into a maintenance mode, which accepts only key reads and deletes.

Monitor these key metrics:

- `etcd_server_quota_backend_bytes`, which is the current quota limit

- `etcd_mvcc_db_total_size_in_use_in_bytes`, which indicates the actual database usage after a history compaction

- `etcd_mvcc_db_total_size_in_bytes`, which shows the database size, including free space waiting for defragmentation

Defragment etcd data to reclaim disk space after events that cause disk fragmentation, such as etcd history compaction.

History compaction is performed automatically every five minutes and leaves gaps in the back-end database. This fragmented space is available for use by etcd, but is not available to the host file system. You must defragment etcd to make this space available to the host file system.

Defragmentation occurs automatically, but you can also trigger it manually.

## Automatic defragmentation

When etcd database growth affects performance, the etcd Operator can automatically defragment member disks based on cluster metrics.

> [!NOTE]
> Automatic defragmentation works well in most cases because the etcd Operator uses cluster metrics to choose the most efficient defragmentation approach.

The etcd Operator automatically defragments disks. No manual intervention is needed.

Verify that defragmentation succeeded by checking one of these logs:

- etcd logs

- cluster-etcd-operator pod

- operator status error log

> [!WARNING]
> Automatic defragmentation can cause leader election failure in various OpenShift Container Platform core components, such as the Kubernetes controller manager, which triggers a restart of the failing component. The restart is harmless and either triggers failover to the next running instance or the component resumes work again after the restart.

The following is example log output for successful defragmentation:

``` terminal
etcd member has been defragmented: <member_name>, memberID: <member_id>
```

The following is example log output for unsuccessful defragmentation:

``` terminal
failed defrag on member: <member_name>, memberID: <member_id>: <error_message>
```

## Manually defragmenting etcd data

When automatic etcd defragmentation cannot reclaim enough space, manually defragment etcd on each member to restore disk availability and normal cluster operation.

A Prometheus alert indicates when you need to use manual defragmentation. The alert is displayed in two cases:

- When etcd uses more than 50% of its available space for more than 10 minutes

- When etcd is actively using less than 50% of its total database size for more than 10 minutes

You can also determine whether defragmentation is needed by checking the etcd database size in MB that will be freed by defragmentation with the PromQL expression: `(etcd_mvcc_db_total_size_in_bytes - etcd_mvcc_db_total_size_in_use_in_bytes)/1024/1024`

> [!WARNING]
> Defragmenting etcd is a blocking action. The etcd member does not respond until defragmentation is complete. For this reason, wait at least one minute between defragmentation actions on each of the pods to allow the cluster to recover.

Follow this procedure to defragment etcd data on each etcd member.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Determine which etcd member is the leader, because the leader should be defragmented last.

    1.  Get the list of etcd pods:

        ``` terminal
        $ oc -n openshift-etcd get pods -l k8s-app=etcd -o wide
        ```

        The following is example output:

        ``` terminal
        etcd-ip-10-0-159-225.example.redhat.com                3/3     Running     0          175m   10.0.159.225   ip-10-0-159-225.example.redhat.com   <none>           <none>
        etcd-ip-10-0-191-37.example.redhat.com                 3/3     Running     0          173m   10.0.191.37    ip-10-0-191-37.example.redhat.com    <none>           <none>
        etcd-ip-10-0-199-170.example.redhat.com                3/3     Running     0          176m   10.0.199.170   ip-10-0-199-170.example.redhat.com   <none>           <none>
        ```

    2.  Choose a pod and run the following command to determine which etcd member is the leader:

        ``` terminal
        $ oc rsh -n openshift-etcd etcd-ip-10-0-159-225.example.redhat.com etcdctl endpoint status --cluster -w table
        ```

        The following is example output:

        ``` terminal
        Defaulting container name to etcdctl.
        Use 'oc describe pod/etcd-ip-10-0-159-225.example.redhat.com -n openshift-etcd' to see all of the containers in this pod.
        +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        |         ENDPOINT          |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
        +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        |  https://10.0.191.37:2379 | 251cd44483d811c3 |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
        | https://10.0.159.225:2379 | 264c7c58ecbdabee |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
        | https://10.0.199.170:2379 | 9ac311f93915cc79 |   3.5.9 |  104 MB |      true |      false |         7 |      91624 |              91624 |        |
        +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        ```

        Based on the `IS LEADER` column of this output, the `https://10.0.199.170:2379` endpoint is the leader. Matching this endpoint with the output of the previous step, the pod name of the leader is `etcd-ip-10-0-199-170.example.redhat.com`.

2.  Defragment an etcd member.

    1.  Connect to the running etcd container, passing in the name of a pod that is *not* the leader:

        ``` terminal
        $ oc rsh -n openshift-etcd etcd-ip-10-0-159-225.example.redhat.com
        ```

    2.  Unset the `ETCDCTL_ENDPOINTS` environment variable:

        ``` terminal
        sh-4.4# unset ETCDCTL_ENDPOINTS
        ```

    3.  Defragment the etcd member:

        ``` terminal
        sh-4.4# etcdctl --command-timeout=30s --endpoints=https://localhost:2379 defrag
        ```

        The following is example output:

        ``` terminal
        Finished defragmenting etcd member[https://localhost:2379]
        ```

        If a timeout error occurs, increase the value for `--command-timeout` until the command succeeds.

    4.  Verify that the database size was reduced:

        ``` terminal
        sh-4.4# etcdctl endpoint status -w table --cluster
        ```

        The following is example output:

        ``` terminal
        +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        |         ENDPOINT          |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
        +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        |  https://10.0.191.37:2379 | 251cd44483d811c3 |   3.5.9 |  104 MB |     false |      false |         7 |      91624 |              91624 |        |
        | https://10.0.159.225:2379 | 264c7c58ecbdabee |   3.5.9 |   41 MB |     false |      false |         7 |      91624 |              91624 |        |
        | https://10.0.199.170:2379 | 9ac311f93915cc79 |   3.5.9 |  104 MB |      true |      false |         7 |      91624 |              91624 |        |
        +---------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
        ```

        This example shows that the database size for this etcd member is now 41 MB as opposed to the starting size of 104 MB.

    5.  Repeat these steps to connect to each of the other etcd members and defragment them. Always defragment the leader last.

        Wait at least one minute between defragmentation actions to allow the etcd pod to recover. Until the etcd pod recovers, the etcd member does not respond.

3.  If any `NOSPACE` alarms were triggered due to the space quota being exceeded, clear them.

    1.  Check if there are any `NOSPACE` alarms:

        ``` terminal
        sh-4.4# etcdctl alarm list
        ```

        The following is example output:

        ``` terminal
        memberID:12345678912345678912 alarm:NOSPACE
        ```

    2.  Clear the alarms:

        ``` terminal
        sh-4.4# etcdctl alarm disarm
        ```

</div>

# Setting tuning parameters for etcd

Configure the control plane hardware speed setting for etcd to match your environment’s latency.

You can set the control plane hardware speed to `"Standard"` or `"Slower"`, or use the default, which is `""`.

The default setting allows the system to decide the speed to use. This value enables upgrades from versions where this feature does not exist, as the system can select values from previous versions.

By selecting one of the other values, you are overriding the default. If you see many leader elections due to timeouts or missed heartbeats, and your system is set to `""` or `"Standard"`, set the hardware speed to `"Slower"`. This change makes the system more tolerant to the increased latency.

<div>

<div class="title">

Procedure

</div>

1.  Check to see what the current value is by entering the following command:

    ``` terminal
    $ oc describe etcd/cluster | grep "Control Plane Hardware Speed"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Control Plane Hardware Speed:  <VALUE>
    ```

    </div>

    > [!NOTE]
    > If the output is empty, the field has not been set and should be considered as the default ("").

2.  Change the value by entering the following command. Replace `<value>` with one of the valid values: `""`, `"Standard"`, or `"Slower"`:

    ``` terminal
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"controlPlaneHardwareSpeed": "<value>"}}'
    ```

    The following table indicates the heartbeat interval and leader election timeout for each profile. These values are subject to change.

    |            |                              |                              |
    |------------|------------------------------|------------------------------|
    | Profile    | ETCD_HEARTBEAT_INTERVAL      | ETCD_LEADER_ELECTION_TIMEOUT |
    | `""`       | Varies depending on platform | Varies depending on platform |
    | `Standard` | 100                          | 1000                         |
    | `Slower`   | 500                          | 2500                         |

    Heartbeat interval and leader election timeout by hardware speed profile

3.  Review the output:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    etcd.operator.openshift.io/cluster patched
    ```

    </div>

    If you enter any value besides the valid values, error output is displayed. For example, if you entered `"Faster"` as the value, the output is as follows:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    The Etcd "cluster" is invalid: spec.controlPlaneHardwareSpeed: Unsupported value: "Faster": supported values: "", "Standard", "Slower"
    ```

    </div>

4.  Verify that the value was changed by entering the following command:

    ``` terminal
    $ oc describe etcd/cluster | grep "Control Plane Hardware Speed"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Control Plane Hardware Speed:  ""
    ```

    </div>

5.  Wait for etcd pods to roll out:

    ``` terminal
    $ oc get pods -n openshift-etcd -w
    ```

    The following output shows the expected entries for the `main-0` control plane node. Before you continue, wait until all control plane nodes show a status of `4/4 Running`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Pending             0          0s
    installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Pending             0          0s
    installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     ContainerCreating   0          0s
    installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     ContainerCreating   0          1s
    installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           1/1     Running             0          2s
    installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Completed           0          34s
    installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Completed           0          36s
    installer-9-ci-ln-qkgs94t-72292-9clnd-main-0           0/1     Completed           0          36s
    etcd-guard-ci-ln-qkgs94t-72292-9clnd-main-0            0/1     Running             0          26m
    etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  4/4     Terminating         0          11m
    etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  4/4     Terminating         0          11m
    etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     Pending             0          0s
    etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     Init:1/3            0          1s
    etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     Init:2/3            0          2s
    etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  0/4     PodInitializing     0          3s
    etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  3/4     Running             0          4s
    etcd-guard-ci-ln-qkgs94t-72292-9clnd-main-0            1/1     Running             0          26m
    etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  3/4     Running             0          20s
    etcd-ci-ln-qkgs94t-72292-9clnd-main-0                  4/4     Running             0          20s
    ```

    </div>

6.  Enter the following command to review to the values:

    ``` terminal
    $ oc describe -n openshift-etcd pod/<ETCD_PODNAME> | grep -e HEARTBEAT_INTERVAL -e ELECTION_TIMEOUT
    ```

    > [!NOTE]
    > These values might not have changed from the default.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Understanding feature gates](../nodes/clusters/nodes-cluster-enabling-features.md#nodes-cluster-enabling-features-about_nodes-cluster-enabling-features)

</div>

# OpenShift Container Platform timer tunables for etcd

OpenShift Container Platform sets platform-specific etcd election timeout and heartbeat interval values. Knowing these tunables helps you align network and disk requirements with expected cluster behavior.

OpenShift Container Platform maintains etcd timers that are optimized for each platform. OpenShift Container Platform has prescribed validated values that are optimized for each platform provider. The default etcd timers with `platform=none` or `platform=metal` are as follows:

``` terminal
- name: ETCD_ELECTION_TIMEOUT
  value: "1000"
  ...
- name: ETCD_HEARTBEAT_INTERVAL
  value: "100"
```

From an etcd perspective, the two key values are election timeout and heartbeat interval:

Heartbeat interval
The frequency with which the leader notifies followers that it is still the leader.

Election timeout
This timeout is how long a follower node will go without hearing a heartbeat before it attempts to become leader itself.

These values do not provide the whole story for the control plane or even etcd. An etcd cluster is sensitive to disk latencies. Because etcd must persist proposals to its log, disk activity from other processes might cause long fsync latencies. The consequence is that etcd might miss heartbeats, causing request timeouts and temporary leader loss. During a leader loss and reelection, the Kubernetes API cannot process any request that causes a service-affecting event and instability of the cluster.

# Determining the size of the etcd database and understanding its effects

etcd database size affects defragmentation duration, resync time after network partitions, and transaction rates. Plan capacity so maintenance and recovery do not degrade cluster stability.

The size of the etcd database has a direct impact on the time to complete the etcd defragmentation process. OpenShift Container Platform automatically runs the etcd defragmentation on one etcd member at a time when it detects at least 45% fragmentation. During the defragmentation process, the etcd member cannot process any requests. On small etcd databases, the defragmentation process happens in less than a second. With larger etcd databases, the disk latency directly impacts the fragmentation time, causing additional latency, as operations are blocked while defragmentation happens.

The size of the etcd database is a factor to consider when network partitions isolate a control plane node for a period and the control plane needs to resync after communication is re-established.

Minimal options exist for controlling the size of the etcd database, as it depends on the operators and applications in the system. When you consider the latency range under which the system will operate, account for the effects of synchronization or defragmentation per size of the etcd database.

The magnitude of the effects is specific to the deployment. The time to complete a defragmentation will cause degradation in the transaction rate, as the etcd member cannot accept updates during the defragmentation process. Similarly, the time for the etcd re-synchronization for large databases with high change rate affects the transaction rate and transaction latency on the system.

Consider the following two examples for the type of impacts to plan for.

Example of the effect of etcd defragmentation based on database size
Writing an etcd database of 1 GB to a slow 7200 RPMs disk at 80 Mbits/sec takes about 1 minute and 40 seconds. In such a scenario, the defragmentation process takes at least this long, if not longer, to complete the defragmentation.

Example of the effect of database size on etcd synchronization
If there is a change of 10% of the etcd database during the disconnection of one of the control plane nodes, the resync needs to transfer at least 100 MB. Transferring 100 MB over a 1 Gbps link takes 800 ms. On clusters with regular transactions with the Kubernetes API, the larger the etcd database size, the more network instabilities will cause control plane instabilities.

You can determine the size of an etcd database by using the OpenShift Container Platform console or by running commands in the `etcdctl` tool.

<div>

<div class="title">

Procedure

</div>

- To find the database size in the OpenShift Container Platform console, go to the **etcd** dashboard to view a plot that reports the size of the etcd database.

- To find the database size by using the `etcdctl` tool, enter the following commands:

  1.  Enter the following command to list the pods:

      ``` terminal
      # oc get pods -n openshift-etcd -l app=etcd
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      NAME      READY   STATUS    RESTARTS   AGE
      etcd-m0   4/4     Running   4          22h
      etcd-m1   4/4     Running   4          22h
      etcd-m2   4/4     Running   4          22h
      ```

      </div>

  2.  Enter the following command and view the database size in the output:

      ``` terminal
      # oc exec -t etcd-m0 -- etcdctl endpoint status -w simple | cut -d, -f 1,3,4
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      https://198.18.111.12:2379, 3.5.6, 1.1 GB
      https://198.18.111.13:2379, 3.5.6, 1.1 GB
      https://198.18.111.14:2379, 3.5.6, 1.1 GB
      ```

      </div>

</div>

# Increasing the database size for etcd

Increase the etcd disk quota when low space or excessive growth alerts appear. Expanding the quota before etcd runs out of space prevents write failures and cluster instability.

You can set the disk quota in gibibytes (GiB) for each etcd instance. If you set a disk quota for your etcd instance, you can specify integer values from 8 to 32. The default value is 8. You can specify only increasing values.

You might want to increase the disk quota if you encounter a `low space` alert. This alert indicates that the cluster is too large to fit in etcd despite automatic compaction and defragmentation. If you see this alert, you need to increase the disk quota immediately because after etcd runs out of space, writes fail.

Another scenario where you might want to increase the disk quota is if you encounter an `excessive database growth` alert. This alert is a warning that the database might grow too large in the next four hours. In this scenario, consider increasing the disk quota so that you do not eventually encounter a `low space` alert and possible write fails.

If you increase the disk quota, the disk space that you specify is not immediately reserved. Instead, etcd can grow to that size if needed. Ensure that etcd is running on a dedicated disk that is larger than the value that you specify for the disk quota.

For large etcd databases, the control plane nodes must have additional memory and storage. Because you must account for the API server cache, the minimum memory required is at least three times the configured size of the etcd database.

> [!IMPORTANT]
> Increasing the database size for etcd is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Procedure

</div>

1.  Check the current value of the disk quota for each etcd instance by entering the following command:

    ``` terminal
    $ oc describe etcd/cluster | grep "Backend Quota"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Backend Quota Gi B: <value>
    ```

    </div>

2.  Change the value of the disk quota by entering the following command:

    ``` terminal
    $ oc patch etcd/cluster --type=merge -p '{"spec": {"backendQuotaGiB": <value>}}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    etcd.operator.openshift.io/cluster patched
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the new value for the disk quota is set by entering the following command:

    ``` terminal
    $ oc describe etcd/cluster | grep "Backend Quota"
    ```

    The etcd Operator automatically rolls out the etcd instances with the new values.

2.  Verify that the etcd pods are up and running by entering the following command:

    ``` terminal
    $ oc get pods -n openshift-etcd
    ```

    The following output shows the expected entries.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                                   READY   STATUS      RESTARTS   AGE
    etcd-ci-ln-b6kfsw2-72292-mzwbq-master-0                4/4     Running     0          39m
    etcd-ci-ln-b6kfsw2-72292-mzwbq-master-1                4/4     Running     0          37m
    etcd-ci-ln-b6kfsw2-72292-mzwbq-master-2                4/4     Running     0          41m
    etcd-guard-ci-ln-b6kfsw2-72292-mzwbq-master-0          1/1     Running     0          51m
    etcd-guard-ci-ln-b6kfsw2-72292-mzwbq-master-1          1/1     Running     0          49m
    etcd-guard-ci-ln-b6kfsw2-72292-mzwbq-master-2          1/1     Running     0          54m
    installer-5-ci-ln-b6kfsw2-72292-mzwbq-master-1         0/1     Completed   0          51m
    installer-7-ci-ln-b6kfsw2-72292-mzwbq-master-0         0/1     Completed   0          46m
    installer-7-ci-ln-b6kfsw2-72292-mzwbq-master-1         0/1     Completed   0          44m
    installer-7-ci-ln-b6kfsw2-72292-mzwbq-master-2         0/1     Completed   0          49m
    installer-8-ci-ln-b6kfsw2-72292-mzwbq-master-0         0/1     Completed   0          40m
    installer-8-ci-ln-b6kfsw2-72292-mzwbq-master-1         0/1     Completed   0          38m
    installer-8-ci-ln-b6kfsw2-72292-mzwbq-master-2         0/1     Completed   0          42m
    revision-pruner-7-ci-ln-b6kfsw2-72292-mzwbq-master-0   0/1     Completed   0          43m
    revision-pruner-7-ci-ln-b6kfsw2-72292-mzwbq-master-1   0/1     Completed   0          43m
    revision-pruner-7-ci-ln-b6kfsw2-72292-mzwbq-master-2   0/1     Completed   0          43m
    revision-pruner-8-ci-ln-b6kfsw2-72292-mzwbq-master-0   0/1     Completed   0          42m
    revision-pruner-8-ci-ln-b6kfsw2-72292-mzwbq-master-1   0/1     Completed   0          42m
    revision-pruner-8-ci-ln-b6kfsw2-72292-mzwbq-master-2   0/1     Completed   0          42m
    ```

    </div>

3.  Verify that the disk quota value is updated for the etcd pod by entering the following command:

    ``` terminal
    $ oc describe -n openshift-etcd pod/<etcd_podname> | grep "ETCD_QUOTA_BACKEND_BYTES"
    ```

    The value might not have changed from the default value of `8`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ETCD_QUOTA_BACKEND_BYTES:                               8589934592
    ```

    </div>

    > [!NOTE]
    > While the value that you set is an integer in GiB, the value shown in the output is converted to bytes.

</div>

# Troubleshooting etcd database size increases

Resolve common errors when increasing the etcd disk quota, including values that are too small, too large, or lower than the current setting.

If you encounter issues when you try to increase the database size for etcd, the following examples might help.

## Value is too small

If the value that you specify is less than `8`, you see an error message. For example, if you enter the following command:

``` terminal
$ oc patch etcd/cluster --type=merge -p '{"spec": {"backendQuotaGiB": 5}}'
```

The following error message is displayed:

<div class="formalpara">

<div class="title">

Example error message

</div>

``` terminal
The Etcd "cluster" is invalid:
* spec.backendQuotaGiB: Invalid value: 5: spec.backendQuotaGiB in body should be greater than or equal to 8
* spec.backendQuotaGiB: Invalid value: "integer": etcd backendQuotaGiB may not be decreased
```

</div>

To resolve this issue, specify an integer between `8` and `32`.

## Value is too large

If the value that you specify is greater than `32`, you see an error message. For example, if you enter the following command:

``` terminal
$ oc patch etcd/cluster --type=merge -p '{"spec": {"backendQuotaGiB": 64}}'
```

The following error message is displayed:

<div class="formalpara">

<div class="title">

Example error message

</div>

``` terminal
The Etcd "cluster" is invalid: spec.backendQuotaGiB: Invalid value: 64: spec.backendQuotaGiB in body should be less than or equal to 32
```

</div>

To resolve this issue, specify an integer between `8` and `32`.

## Value is decreasing

If the value is set to a valid value between `8` and `32`, you cannot decrease the value. Otherwise, you see an error message.

For example, check the current value by entering the following command:

``` terminal
$ oc describe etcd/cluster | grep "Backend Quota"
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
Backend Quota Gi B: 10
```

</div>

If you decrease the disk quota value by entering the following command, an error message is displayed.

``` terminal
$ oc patch etcd/cluster --type=merge -p '{"spec": {"backendQuotaGiB": 8}}'
```

<div class="formalpara">

<div class="title">

Example error message

</div>

``` terminal
The Etcd "cluster" is invalid: spec.backendQuotaGiB: Invalid value: "integer": etcd backendQuotaGiB may not be decreased
```

</div>

To resolve this issue, specify an integer greater than `10`.

# Measuring network jitter between control plane nodes

Measure network jitter between control plane nodes to validate latency for etcd heartbeats. High jitter causes missed heartbeats, leader loss, and Kubernetes API request failures.

The value of the heartbeat interval should be around the maximum of the average round-trip time (RTT) between members, normally around 1.5 times the RTT. With the OpenShift Container Platform default heartbeat interval of 100 ms, the recommended RTT between control plane nodes is less than approximately 33 ms. The maximum RTT should be less than 66 ms (66 ms multiplied by 1.5 equals 99 ms). For more information, see "Setting tuning parameters for etcd". Any network latency that is higher might cause service-affecting events and cluster instability.

The network latency is influenced by many factors, including but not limited to the following factors:

- The technology of the transport networks, such as copper, fiber, wireless, or satellite

- The number and quality of the network devices in the transport network

A good evaluation reference is the comparison of the network latency in the organization with the commercial latencies that are published by telecommunications providers, such as monthly IP latency statistics.

Consider network latency with network jitter for more accurate calculations. *Network jitter* is the variance in network latency or, more specifically, the variation in the delay of received packets. On ideal network conditions, the jitter is as close to zero as possible. Network jitter affects the network latency calculations for etcd because the actual network latency over time will be the RTT plus or minus jitter. For example, a network with a maximum latency of 80 ms and jitter of 30 ms will experience latencies of 110 ms, which means etcd is missing heartbeats, causing request timeouts and temporary leader loss. During a leader loss and reelection, the Kubernetes API cannot process any request that causes a service-affecting event and instability of the cluster.

It is important to measure the network jitter among all control plane nodes. To do so, you can use the `iPerf3` tool in UDP mode.

<div>

<div class="title">

Prerequisite

</div>

- You built your own `iPerf` image. For more information, see the following Red Hat Knowledgebase articles:

  - [Testing Network Bandwidth in OpenShift using iPerf Container](https://access.redhat.com/articles/5233541)

  - [How to run iPerf network performance test in OpenShift 4](https://access.redhat.com/solutions/6129701)

</div>

<div>

<div class="title">

Procedure

</div>

1.  Connect to one of the control plane nodes and run the `iPerf` container as `iPerf` server in host network mode. When you are running in server mode, the tool accepts TCP and UDP tests. Enter the following command, being careful to replace `<iperf_image>` with your `iPerf` image:

    ``` terminal
    # podman run -ti --rm --net host <iperf_image> iperf3 -s
    ```

2.  Connect to another control plane node and run the `iPerf3` tool in UDP client mode by entering the following command:

    ``` terminal
    # podman run -ti --rm --net host <iperf_image> iperf3 -u -c <node_iperf_server> -t 300
    ```

    The default test runs for 10 seconds, and at the end, the client output shows the average jitter from the client perspective.

3.  Run the debug node mode by entering the following command:

    ``` terminal
    # oc debug node/m1
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Starting pod/m1-debug ...
    To use host binaries, run `chroot /host`
    Pod IP: 198.18.111.13
    If you do not see a command prompt, try pressing Enter.
    ```

    </div>

4.  Enter the following commands:

    ``` terminal
    sh-4.4# chroot /host
    ```

    ``` terminal
    sh-4.4# podman run -ti --rm --net host <iperf_image> iperf3 -u -c m0
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Connecting to host m0, port 5201
    [  5] local 198.18.111.13 port 60878 connected to 198.18.111.12 port 5201
    [ ID] Interval           Transfer     Bitrate         Total Datagrams
    [  5]   0.00-1.00   sec   129 KBytes  1.05 Mbits/sec  91
    [  5]   1.00-2.00   sec   127 KBytes  1.04 Mbits/sec  90
    [  5]   2.00-3.00   sec   129 KBytes  1.05 Mbits/sec  91
    [  5]   3.00-4.00   sec   129 KBytes  1.05 Mbits/sec  91
    [  5]   4.00-5.00   sec   127 KBytes  1.04 Mbits/sec  90
    [  5]   5.00-6.00   sec   129 KBytes  1.05 Mbits/sec  91
    [  5]   6.00-7.00   sec   127 KBytes  1.04 Mbits/sec  90
    [  5]   7.00-8.00   sec   129 KBytes  1.05 Mbits/sec  91
    [  5]   8.00-9.00   sec   127 KBytes  1.04 Mbits/sec  90
    [  5]   9.00-10.00  sec   129 KBytes  1.05 Mbits/sec  91
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
    [  5]   0.00-10.00  sec  1.25 MBytes  1.05 Mbits/sec  0.000 ms  0/906 (0%)  sender
    [  5]   0.00-10.04  sec  1.25 MBytes  1.05 Mbits/sec  1.074 ms  0/906 (0%)  receiver

    iperf Done.
    ```

    </div>

5.  On the `iPerf` server, the output shows the jitter on every second interval. The average is shown at the end. For the purpose of this test, you want to identify the maximum jitter that is experienced during the test, ignoring the output of the first second as it might contain an invalid measurement. Enter the following command:

    ``` terminal
    # oc debug node/m0
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Starting pod/m0-debug ...
    To use host binaries, run `chroot /host`
    Pod IP: 198.18.111.12
    If you do not see a command prompt, try pressing Enter.
    ```

    </div>

6.  Enter the following commands:

    ``` terminal
    sh-4.4# chroot /host
    ```

    ``` terminal
    sh-4.4# podman run -ti --rm --net host <iperf_image> iperf3 -s
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    -----------------------------------------------------------
    Server listening on 5201
    -----------------------------------------------------------
    Accepted connection from 198.18.111.13, port 44136
    [  5] local 198.18.111.12 port 5201 connected to 198.18.111.13 port 60878
    [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
    [  5]   0.00-1.00   sec   124 KBytes  1.02 Mbits/sec  4.763 ms  0/88 (0%)
    [  5]   1.00-2.00   sec   127 KBytes  1.04 Mbits/sec  4.735 ms  0/90 (0%)
    [  5]   2.00-3.00   sec   129 KBytes  1.05 Mbits/sec  0.568 ms  0/91 (0%)
    [  5]   3.00-4.00   sec   127 KBytes  1.04 Mbits/sec  2.443 ms  0/90 (0%)
    [  5]   4.00-5.00   sec   129 KBytes  1.05 Mbits/sec  1.372 ms  0/91 (0%)
    [  5]   5.00-6.00   sec   127 KBytes  1.04 Mbits/sec  2.769 ms  0/90 (0%)
    [  5]   6.00-7.00   sec   129 KBytes  1.05 Mbits/sec  2.393 ms  0/91 (0%)
    [  5]   7.00-8.00   sec   127 KBytes  1.04 Mbits/sec  0.883 ms  0/90 (0%)
    [  5]   8.00-9.00   sec   129 KBytes  1.05 Mbits/sec  0.594 ms  0/91 (0%)
    [  5]   9.00-10.00  sec   127 KBytes  1.04 Mbits/sec  0.953 ms  0/90 (0%)
    [  5]  10.00-10.04  sec  5.66 KBytes  1.30 Mbits/sec  1.074 ms  0/4 (0%)
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
    [  5]   0.00-10.04  sec  1.25 MBytes  1.05 Mbits/sec  1.074 ms  0/906 (0%)  receiver
    -----------------------------------------------------------
    Server listening on 5201
    -----------------------------------------------------------
    ```

    </div>

7.  Add the calculated jitter as a penalty to the network latency. For example, if the network latency is 80 ms and the jitter is 30 ms, consider an effective network latency of 110 ms for the purposes of the control plane. In this example, that value goes above the 100 ms threshold, and the system will miss heartbeats.

8.  When you calculate the network latency for etcd, use the effective network latency, which is the sum of the following equation:

    RTT + jitter

    You might be able to use the average jitter value to calculate the penalty, but the cluster can sporadically miss heartbeats if the etcd heartbeat timer is lower than the sum of the following equation:

    RTT + max(jitter)

    Instead, consider using the 99th percentile or max jitter value for a more resilient deployment:

    Effective Network Latency = RTT + max(jitter)

</div>

<div>

<div class="title">

Additional resources

</div>

- [Setting tuning parameters for etcd](etcd-performance.md#etcd-tuning-parameters_etcd-performance)

</div>

# How etcd peer round-trip time affects performance

The etcd peer round-trip time (RTT) metric shows replication latency across members, beyond raw network RTT. Monitor it to detect control plane slowdowns before they affect cluster operations.

The etcd peer RTT is an end-to-end test metric on how quickly something can be replicated among members. It shows the latency of etcd to finish replicating a client request among all the etcd members. The etcd peer RTT is not the same thing as the network RTT.

You can monitor various etcd metrics on dashboards in the OpenShift Container Platform console. In the console, click **Observe** → **Dashboards** and from the dropdown list, select **etcd**.

Near the end of the **etcd** dashboard, you can find a plot that summarizes the etcd peer RTT.

> [!NOTE]
> These etcd metrics are collected by the OpenShift Container Platform metrics system in Prometheus. You can access them from the CLI by using a Prometheus query. For more information, see the Red Hat Knowledgebase solution, "How to query from the command line Prometheus statistics".

``` terminal
# Get token to connect to Prometheus
SECRET=$(oc get secret -n openshift-user-workload-monitoring | grep  prometheus-user-workload-token | head -n 1 | awk '{print $1 }')
export TOKEN=$(oc get secret $SECRET -n openshift-user-workload-monitoring -o json | jq -r '.data.token' | base64 -d)
export THANOS_QUERIER_HOST=$(oc get route thanos-querier -n openshift-monitoring -o json | jq -r '.spec.host')
```

Queries must be URL-encoded. The following example shows how to retrieve the metrics that are reporting the RTT (in seconds) for etcd to finish replicating the client requests among the members:

``` terminal
# prometheus query
query="histogram_quantile(0.99, rate(etcd_network_peer_round_trip_time_seconds_bucket[5m]))"

# urlencoded query
encoded_query=$(printf "%s" $query |jq -sRr @uri)

# querying the metrics service
curl -s -X GET -k -H "Authorization: Bearer $TOKEN" "https://$THANOS_QUERIER_HOST/api/v1/query?query=$encoded_query" | jq '.data.result[] | .metric.pod,.value[1]'

"etcd-m2"
"0.09318400000000004"   # example ~93ms
"etcd-m0"
"0.050688"              # example ~51ms
"etcd-m1"
"0.050688"              # example ~51ms
```

The following metrics are also relevant to understanding etcd performance:

`etcd_disk_wal_fsync_duration_seconds_bucket`
Reports the etcd write-ahead log (WAL) fsync duration.

`etcd_disk_backend_commit_duration_seconds_bucket`
Reports the etcd backend commit latency duration.

`etcd_server_leader_changes_seen_total`
Reports the leader changes.

<div>

<div class="title">

Additional resources

</div>

- [How to query from the command line Prometheus statistics (Red Hat Knowledgebase)](https://access.redhat.com/solutions/5151831)

</div>

# Determining Kubernetes API transaction rate for your environment

Test sustained Kubernetes API transaction rates for stretched control plane deployments by using `kube-burner-ocp` density profiles. Validate limits before production workloads exceed etcd capacity.

When you are using stretched control planes, the Kubernetes API transaction rate depends on the characteristics of the particular deployment. Specifically, it depends on the following combined factors:

- The etcd disk latency

- The etcd round trip time

- The size of objects that are being written to the API

As a result, when you use stretched control planes, cluster administrators must test the environment to determine the sustained transaction rate that is possible for the environment. The `kube-burner` tool is useful for that purpose. The binary includes a wrapper for testing OpenShift clusters: `kube-burner-ocp`. You can use `kube-burner-ocp` to test cluster or node density.

To test the control plane, `kube-burner-ocp` has three workload profiles: `cluster-density`, `cluster-density-v2`, and `cluster-density-ms`. Each workload profile creates a series of resources that are designed to load the control plane. For more information about each profile, see the `kube-burner-ocp` workload documentation.

<div>

<div class="title">

Procedure

</div>

1.  Enter a command to create and delete resources. The following example shows a command that creates and deletes resources within 20 minutes:

    ``` terminal
    # kube-burner ocp cluster-density-ms --churn-duration 20m --churn-delay 0s --iterations 10 --timeout 30m
    ```

2.  The OpenShift Container Platform console provides a dashboard with all the relevant API performance information. To access API performance information, click **Observe** → **Dashboards**. From the **Dashboards** menu, click **API Performance**.

3.  During the run, observe the API performance dashboard in the OpenShift Container Platform console by clicking **Observe** → **Dashboards**. From the **Dashboards** menu, click **API Performance**.

    On the dashboard, notice how the control plane responds during load and the 99th percentile transaction rate it can achieve for the execution of various verbs and request rates by read and write. Use this information and the knowledge of your organization’s workload to determine the load that the organization can put in the clusters for the specific stretched control plane deployment.

</div>

<div>

<div class="title">

Additional resources

</div>

- [kube-burner-ocp documentation](https://kube-burner.github.io/kube-burner-ocp/latest/)

</div>
