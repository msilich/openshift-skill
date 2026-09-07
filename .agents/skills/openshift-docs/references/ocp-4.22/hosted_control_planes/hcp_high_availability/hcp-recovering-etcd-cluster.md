<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In a highly available control plane, three etcd pods run as a part of a stateful set in an etcd cluster. To recover an etcd cluster, identify unhealthy etcd pods by checking the etcd cluster health.

# Checking the status of an etcd cluster

You can check the status of the etcd cluster health by logging into any etcd pod.

<div>

<div class="title">

Procedure

</div>

1.  Log in to an etcd pod by entering the following command:

    ``` terminal
    $ oc rsh -n clusters-<hosted_cluster_name> -c etcd <etcd_pod_name>
    ```

2.  Print the health status of an etcd cluster by entering the following command:

    ``` terminal
    sh-4.4# etcdctl endpoint status -w table
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    +------------------------------+-----------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
    |          ENDPOINT            |       ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
    +------------------------------+-----------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
    | https://192.168.1xxx.20:2379 | 8fxxxxxxxxxx    |  3.5.12 |  123 MB |     false |      false |        10 |     180156 |             180156 |        |
    | https://192.168.1xxx.21:2379 | a5xxxxxxxxxx    |  3.5.12 |  122 MB |     false |      false |        10 |     180156 |             180156 |        |
    | https://192.168.1xxx.22:2379 | 7cxxxxxxxxxx    |  3.5.12 |  124 MB |      true |      false |        10 |     180156 |             180156 |        |
    +-----------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
    ```

    </div>

</div>

# Recovering a failing etcd pod

Each etcd pod of a 3-node cluster has its own persistent volume claim (PVC) to store its data. An etcd pod might fail because of corrupted or missing data. You can recover a failing etcd pod and its PVC.

<div>

<div class="title">

Procedure

</div>

1.  To confirm that the etcd pod is failing, enter the following command:

    ``` terminal
    $ oc get pods -l app=etcd -n clusters-<hosted_cluster_name>
    ```

    Replace `<hosted_cluster_name>` with the name of the hosted cluster of the etcd instance.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME     READY   STATUS             RESTARTS     AGE
    etcd-0   2/2     Running            0            64m
    etcd-1   2/2     Running            0            45m
    etcd-2   1/2     CrashLoopBackOff   1 (5s ago)   64m
    ```

    </div>

    The failing etcd pod might have the `CrashLoopBackOff` or `Error` status.

2.  Delete the failing pod and its PVC by entering the following command:

    ``` terminal
    $ oc delete pods <etcd_pod_name> -n clusters-<hosted_cluster_name>
    ```

    Replace `<etcd_pod_name>` with the name of the failing pod.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that a new etcd pod is up and running by entering the following command:

  ``` terminal
  $ oc get pods -l app=etcd -n clusters-<hosted_cluster_name>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME     READY   STATUS    RESTARTS   AGE
  etcd-0   2/2     Running   0          67m
  etcd-1   2/2     Running   0          48m
  etcd-2   2/2     Running   0          2m2s
  ```

  </div>

</div>
