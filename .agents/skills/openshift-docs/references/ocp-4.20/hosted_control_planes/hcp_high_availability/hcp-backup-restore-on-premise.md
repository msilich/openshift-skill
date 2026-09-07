<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

By backing up and restoring etcd on a hosted cluster, you can fix failures, such as corrupted or missing data in an etcd member of a three-node cluster. If members of the etcd cluster lose data or have a `CrashLoopBackOff` status, this approach helps prevent an etcd quorum loss.

# Backing up etcd on a hosted cluster

Fix failures by taking a snapshot of etcd on a hosted cluster.

<div>

<div class="title">

Prerequisites

</div>

- The `oc` and `jq` binaries have been installed.

- For hosted control planes on AWS, the OIDC provider configuration must be accessible so that any necessary fixes can be completed after the restore process. See the following procedure for more information about applying any necessary fixes.

- For hosted control planes on bare metal, the `InfraEnv` resource must reside in a different namespace from the hosted control plane namespace. Do not delete the `InfraEnv` resource during the backup or restore process.

- Management cluster prerequisites:

  - A valid `StorageClass` resource is configured in the management cluster.

  - You have `cluster-admin` access to the management cluster.

  - You have access to online storage that is compatible with OpenShift API for Data Protection (OADP) cloud storage providers, such as Amazon Web Services (AWS) S3, Microsoft Azure, Google Cloud, or MinIO. If you use S3 for backup storage, ensure that IAM roles and policies are configured. For more information, see "Configuring Amazon Web Services".

  - Hosted control plane pods are accessible and functioning properly.

  - You have access to the `openshift-adp` subscription through a `CatalogSource` object.

- Service publishing strategy prerequisites for hosted clusters:

  - The `APIServer` service must have a fixed hostname. Otherwise, the restore process fails and nodes cannot rejoin the cluster. For hosted control planes on AWS, the `APIServer` service can also use a `Route` service publishing strategy with a fixed hostname.

  - For production environments, it is strongly recommended to configure all services with fixed hostnames. By having fixed hostnames, you can ensure full service continuity and DNS consistency during the restore process on a different management cluster.

  - When you restore a hosted cluster to a different management cluster, all services in the hosted cluster must be configured with a fixed hostname in its `servicePublishingStrategy` property. This requirement applies to all platforms. Restoring a hosted cluster to a different management cluster is a Technology Preview feature. Restoring a hosted cluster to its original management cluster is supported.

</div>

> [!IMPORTANT]
> After you back up the hosted cluster, you must back up workloads in the data cluster and then delete the original hosted cluster so that the restore process can begin.

<div>

<div class="title">

Procedure

</div>

1.  Set up environment variables for your hosted cluster by entering the following commands, replacing values as necessary:

    ``` terminal
    $ CLUSTER_NAME=my-cluster
    ```

    ``` terminal
    $ HOSTED_CLUSTER_NAMESPACE=clusters
    ```

    ``` terminal
    $ CONTROL_PLANE_NAMESPACE="${HOSTED_CLUSTER_NAMESPACE}-${CLUSTER_NAME}"
    ```

2.  Pause reconciliation of the hosted cluster by entering the following command, replacing values as necessary:

    ``` terminal
    $ oc patch -n ${HOSTED_CLUSTER_NAMESPACE} hostedclusters/${CLUSTER_NAME} \
      -p '{"spec":{"pausedUntil":"true"}}' --type=merge
    ```

3.  Take a snapshot of etcd by using one of the following methods:

    - Use a previously backed-up snapshot of etcd.

    - If you have an available etcd pod, take a snapshot from the active etcd pod by completing the following steps:

      1.  List etcd pods by entering the following command:

          ``` terminal
          $ oc get -n ${CONTROL_PLANE_NAMESPACE} pods -l app=etcd
          ```

      2.  Take a snapshot of the pod database and save it locally to your machine by entering the following commands:

          ``` terminal
          $ ETCD_POD=etcd-0
          ```

          ``` terminal
          $ oc exec -n ${CONTROL_PLANE_NAMESPACE} -c etcd -t ${ETCD_POD} -- \
            env ETCDCTL_API=3 /usr/bin/etcdctl \
            --cacert /etc/etcd/tls/etcd-ca/ca.crt \
            --cert /etc/etcd/tls/client/etcd-client.crt \
            --key /etc/etcd/tls/client/etcd-client.key \
            --endpoints=https://localhost:2379 \
            snapshot save /var/lib/snapshot.db
          ```

      3.  Verify that the snapshot is successful by entering the following command:

          ``` terminal
          $ oc exec -n ${CONTROL_PLANE_NAMESPACE} -c etcd -t ${ETCD_POD} -- \
            env ETCDCTL_API=3 /usr/bin/etcdctl -w table snapshot status \
            /var/lib/snapshot.db
          ```

    - Make a local copy of the snapshot:

      1.  Copy the snapshot by entering the following command:

          ``` terminal
          $ oc cp -c etcd ${CONTROL_PLANE_NAMESPACE}/${ETCD_POD}:/var/lib/snapshot.db \
            /tmp/etcd.snapshot.db
          ```

      2.  Copy the snapshot database from etcd persistent storage:

          1.  List etcd pods by entering the following command:

              ``` terminal
              $ oc get -n ${CONTROL_PLANE_NAMESPACE} pods -l app=etcd
              ```

          2.  Find a pod that is running and set its name as the value of `ETCD_POD: ETCD_POD=etcd-0`, and then copy its snapshot database by entering the following command:

              ``` terminal
              $ oc cp -c etcd \
                ${CONTROL_PLANE_NAMESPACE}/${ETCD_POD}:/var/lib/data/member/snap/db \
                /tmp/etcd.snapshot.db
              ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring Amazon Web Services](../../backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.md#migration-configuring-aws-s3_installing-oadp-aws)

</div>

# Restoring etcd on a hosted cluster

Fix failures by restoring a snapshot of etcd on a hosted cluster.

<div>

<div class="title">

Prerequisites

</div>

- You completed the steps in "Backing up etcd on a hosted cluster". Ensure that you meet the prerequisites listed in that procedure.

</div>

> [!IMPORTANT]
> After you back up the hosted cluster, you must back up workloads in the data cluster and then delete the original hosted cluster so that the restore process can begin.

<div>

<div class="title">

Procedure

</div>

1.  If you are working in a new terminal session from the session you used to complete the steps in "Backing up etcd on a hosted cluster", set the environment variables again as described in the backup procedure.

2.  Scale down the etcd statefulset by entering the following command:

    ``` terminal
    $ oc scale -n ${CONTROL_PLANE_NAMESPACE} statefulset/etcd --replicas=0
    ```

3.  Delete volumes for second and third members by entering the following command:

    ``` terminal
    $ oc delete -n ${CONTROL_PLANE_NAMESPACE} pvc/data-etcd-1 pvc/data-etcd-2
    ```

4.  Create a pod to access the first etcd member’s data:

    1.  Get the etcd image by entering the following command:

        ``` terminal
        $ ETCD_IMAGE=$(oc get -n ${CONTROL_PLANE_NAMESPACE} statefulset/etcd \
          -o jsonpath='{ .spec.template.spec.containers[0].image }')
        ```

    2.  Create a pod that allows access to etcd data:

        ``` yaml
        $ cat << EOF | oc apply -n ${CONTROL_PLANE_NAMESPACE} -f -
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: etcd-data
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: etcd-data
          template:
            metadata:
              labels:
                app: etcd-data
            spec:
              containers:
              - name: access
                image: $ETCD_IMAGE
                volumeMounts:
                - name: data
                  mountPath: /var/lib
                command:
                - /usr/bin/bash
                args:
                - -c
                - |-
                  while true; do
                    sleep 1000
                  done
              volumes:
              - name: data
                persistentVolumeClaim:
                  claimName: data-etcd-0
            EOF
        ```

    3.  Check the status of the `etcd-data` pod and wait for it to be running by entering the following command:

        ``` terminal
        $ oc get -n ${CONTROL_PLANE_NAMESPACE} pods -l app=etcd-data
        ```

    4.  Get the name of the `etcd-data` pod by entering the following command:

        ``` terminal
        $ DATA_POD=$(oc get -n ${CONTROL_PLANE_NAMESPACE} pods --no-headers \
          -l app=etcd-data -o name | cut -d/ -f2)
        ```

5.  Copy an etcd snapshot into the pod by entering the following command:

    ``` terminal
    $ oc cp /tmp/etcd.snapshot.db \
      ${CONTROL_PLANE_NAMESPACE}/${DATA_POD}:/var/lib/restored.snap.db
    ```

6.  Remove old data from the `etcd-data` pod by entering the following commands:

    ``` terminal
    $ oc exec -n ${CONTROL_PLANE_NAMESPACE} ${DATA_POD} -- rm -rf /var/lib/data
    ```

    ``` terminal
    $ oc exec -n ${CONTROL_PLANE_NAMESPACE} ${DATA_POD} -- mkdir -p /var/lib/data
    ```

7.  Restore the etcd snapshot by entering the following command:

    ``` terminal
    $ oc exec -n ${CONTROL_PLANE_NAMESPACE} ${DATA_POD} -- \
         etcdutl snapshot restore /var/lib/restored.snap.db \
         --data-dir=/var/lib/data --skip-hash-check \
         --name etcd-0 \
         --initial-cluster-token=etcd-cluster \
         --initial-cluster etcd-0=https://etcd-0.etcd-discovery.${CONTROL_PLANE_NAMESPACE}.svc:2380,etcd-1=https://etcd-1.etcd-discovery.${CONTROL_PLANE_NAMESPACE}.svc:2380,etcd-2=https://etcd-2.etcd-discovery.${CONTROL_PLANE_NAMESPACE}.svc:2380 \
         --initial-advertise-peer-urls https://etcd-0.etcd-discovery.${CONTROL_PLANE_NAMESPACE}.svc:2380
    ```

8.  Remove the temporary etcd snapshot from the pod by entering the following command:

    ``` terminal
    $ oc exec -n ${CONTROL_PLANE_NAMESPACE} ${DATA_POD} -- \
      rm /var/lib/restored.snap.db
    ```

9.  Delete data access deployment by entering the following command:

    ``` terminal
    $ oc delete -n ${CONTROL_PLANE_NAMESPACE} deployment/etcd-data
    ```

10. Scale up the etcd cluster by entering the following command:

    ``` terminal
    $ oc scale -n ${CONTROL_PLANE_NAMESPACE} statefulset/etcd --replicas=3
    ```

11. Wait for the etcd member pods to return and report as available by entering the following command:

    ``` terminal
    $ oc get -n ${CONTROL_PLANE_NAMESPACE} pods -l app=etcd -w
    ```

12. Restore reconciliation of the hosted cluster by entering the following command:

    ``` terminal
    $ oc patch -n ${HOSTED_CLUSTER_NAMESPACE} hostedclusters/${CLUSTER_NAME} \
      -p '{"spec":{"pausedUntil":"null"}}' --type=merge
    ```

    This command uses the `"null"` string. When you use that string, the controller treats unrecognized strings as not paused, but it logs an error. Instead of `"null"`, you can also use `"false"`, which is valid per Common Expression Language (CEL) validation, or JSON `null`, which removes the field.

13. Manually roll out the hosted cluster by entering the following command:

    ``` terminal
    $ oc annotate hostedcluster -n \
      <hosted_cluster_namespace> <hosted_cluster_name> \
      hypershift.openshift.io/restart-date=$(date --iso-8601=seconds)
    ```

    The Multus admission controller and network node identity pods do not start yet.

14. Delete the pods for the second and third members of etcd and their PVCs by entering the following commands:

    ``` terminal
    $ oc delete -n ${CONTROL_PLANE_NAMESPACE} pvc/data-etcd-1 pod/etcd-1 --wait=false
    ```

    ``` terminal
    $ oc delete -n ${CONTROL_PLANE_NAMESPACE} pvc/data-etcd-2 pod/etcd-2 --wait=false
    ```

15. Manually roll out the hosted cluster again by entering the following command:

    ``` terminal
    $ oc annotate hostedcluster -n \
      <hosted_cluster_namespace> <hosted_cluster_name> \
      hypershift.openshift.io/restart-date=$(date --iso-8601=seconds) \
      --overwrite
    ```

    After a few minutes, the control plane pods start running.

16. If your hosted cluster is on AWS and you need to apply OIDC fixes after the restore process, enter the following command:

    ``` terminal
    $ hcp fix dr-oidc-iam --hc-name <hosted_cluster_name> --hc-namespace <hosted_cluster_namespace> --aws-creds ~/.aws/credentials
    ```

    This command regenerates the OIDC in S3 in case OIDC is deleted.

</div>
