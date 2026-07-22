<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Learn how to upgrade your existing OADP 1.4 installation to OADP 1.5.

> [!NOTE]
> Always upgrade to the next minor version. Do not skip versions. To update to a later version, upgrade only one channel at a time. For example, to upgrade from OADP 1.1 to 1.3, upgrade first to 1.2, and then to 1.3.

# Changes from OADP 1.4 to 1.5

The Velero server has been updated from version 1.14 to 1.16.

This changes the following:

Version Support changes
OpenShift API for Data Protection implements a streamlined version support policy. Red Hat supports only one version of OpenShift API for Data Protection (OADP) on one OpenShift version to ensure better stability and maintainability. OADP 1.5.0 is only supported on OpenShift 4.19 version.

OADP Self-Service
OADP 1.5.0 introduces a new feature named OADP Self-Service, enabling namespace admin users to back up and restore applications on the OpenShift Container Platform. In the earlier versions of OADP, you needed the cluster-admin role to perform OADP operations such as backing up and restoring an application, creating a backup storage location, and so on.

From OADP 1.5.0 onward, you do not need the cluster-admin role to perform the backup and restore operations. You can use OADP with the namespace admin role. The namespace admin role has administrator access only to the namespace the user is assigned to. You can use the Self-Service feature only after the cluster administrator installs the OADP Operator and provides the necessary permissions.

`backupPVC` and `restorePVC` configurations
A `backupPVC` resource is an intermediate persistent volume claim (PVC) to access data during the data movement backup operation. You create a `readonly` backup PVC by using the `nodeAgent.backupPVC` section of the `DataProtectionApplication` (DPA) custom resource.

A `restorePVC` resource is an intermediate PVC that is used to write data during the Data Mover restore operation.

You can configure `restorePVC` in the DPA by using the `ignoreDelayBinding` field.

# Backing up the DPA configuration

You must back up your current `DataProtectionApplication` (DPA) configuration.

<div>

<div class="title">

Procedure

</div>

- Save your current DPA configuration by running the following command:

  <div class="formalpara">

  <div class="title">

  Example command

  </div>

  ``` terminal
  $ oc get dpa -n openshift-adp -o yaml > dpa.orig.backup
  ```

  </div>

</div>

# Upgrading the OADP Operator

You can upgrade the OpenShift API for Data Protection (OADP) Operator using the following procedure.

> [!NOTE]
> Do not install OADP 1.5.0 on a OpenShift 4.18 cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the latest OADP 1.4.6.

- You have backed up your data.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Upgrade OpenShift 4.18 to OpenShift 4.19.

    > [!NOTE]
    > OpenShift API for Data Protection (OADP) 1.4 is not supported on OpenShift 4.19.

2.  Change your subscription channel for the OADP Operator from `stable-1.4` to `stable`.

3.  Wait for the Operator and containers to update and restart.

</div>

# Converting DPA to the new version for OADP 1.5.0

The OpenShift API for Data Protection (OADP) 1.4 is not supported on OpenShift 4.19. You can convert Data Protection Application (DPA) to the new OADP 1.5 version by using the new `spec.configuration.nodeAgent` field and its sub-fields.

<div>

<div class="title">

Procedure

</div>

1.  To configure `nodeAgent` daemon set, use the `spec.configuration.nodeAgent` parameter in DPA. See the following example:

    <div class="formalpara">

    <div class="title">

    Example `DataProtectionApplication` configuration

    </div>

    ``` yaml
    ...
     spec:
       configuration:
         nodeAgent:
           enable: true
           uploaderType: kopia
    ...
    ```

    </div>

2.  To configure `nodeAgent` daemon set by using the `ConfigMap` resource named `node-agent-config`, see the following example configuration:

    <div class="formalpara">

    <div class="title">

    Example config map

    </div>

    ``` yaml
    ...
     spec:
       configuration:
         nodeAgent:
           backupPVC:
             ...
           loadConcurrency:
             ...
           podResources:
             ...
           restorePVC:
            ...
    ...
    ```

    </div>

</div>

# Verifying the upgrade

You can verify the OpenShift API for Data Protection (OADP) upgrade by using the following procedure.

<div>

<div class="title">

Procedure

</div>

1.  Verify that the `DataProtectionApplication` (DPA) has been reconciled successfully:

    ``` terminal
    $ oc get dpa dpa-sample -n openshift-adp
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME            RECONCILED   AGE
    dpa-sample      True         2m51s
    ```

    </div>

    > [!NOTE]
    > The `RECONCILED` column must be `True`.

2.  Verify that the installation finished by viewing the OADP resources by running the following command:

    ``` terminal
    $ oc get all -n openshift-adp
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                                    READY   STATUS    RESTARTS   AGE
    pod/node-agent-9pjz9                                    1/1     Running   0          3d17h
    pod/node-agent-fmn84                                    1/1     Running   0          3d17h
    pod/node-agent-xw2dg                                    1/1     Running   0          3d17h
    pod/openshift-adp-controller-manager-76b8bc8d7b-kgkcw   1/1     Running   0          3d17h
    pod/velero-64475b8c5b-nh2qc                             1/1     Running   0          3d17h

    NAME                                                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
    service/openshift-adp-controller-manager-metrics-service   ClusterIP   172.30.194.192   <none>        8443/TCP   3d17h
    service/openshift-adp-velero-metrics-svc                   ClusterIP   172.30.190.174   <none>        8085/TCP   3d17h

    NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
    daemonset.apps/node-agent   3         3         3       3            3           <none>          3d17h

    NAME                                               READY   UP-TO-DATE   AVAILABLE   AGE
    deployment.apps/openshift-adp-controller-manager   1/1     1            1           3d17h
    deployment.apps/velero                             1/1     1            1           3d17h

    NAME                                                          DESIRED   CURRENT   READY   AGE
    replicaset.apps/openshift-adp-controller-manager-76b8bc8d7b   1         1         1       3d17h
    replicaset.apps/openshift-adp-controller-manager-85fff975b8   0         0         0       3d17h
    replicaset.apps/velero-64475b8c5b                             1         1         1       3d17h
    replicaset.apps/velero-8b5bc54fd                              0         0         0       3d17h
    replicaset.apps/velero-f5c9ffb66                              0         0         0       3d17h
    ```

    </div>

    > [!NOTE]
    > The `node-agent` pods are created only while using `restic` or `kopia` in `DataProtectionApplication` (DPA). In OADP 1.4.0 and OADP 1.3.0 version, the `node-agent` pods are labeled as `restic`.

3.  Verify the backup storage location and confirm that the `PHASE` is `Available` by running the following command:

    ``` terminal
    $ oc get backupstoragelocations.velero.io -n openshift-adp
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME           PHASE       LAST VALIDATED   AGE     DEFAULT
    dpa-sample-1   Available   1s               3d16h   true
    ```

    </div>

</div>
