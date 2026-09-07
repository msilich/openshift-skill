<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

By default, OpenShift API for Data Protection processes only one backup in the `InProgress` phase at a time. Configure the `DataProtectionApplication` (DPA) custom resource (CR) to run several backups simultaneously to prevent smaller backups from being queued behind larger operations.

<div>

<div class="title">

Prerequisites

</div>

- You must be logged in as a user with `cluster-admin` privileges.

- You must have a DPA CR configured and deployed in your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit your DPA CR:

    ``` terminal
    $ oc edit dpa <dpa_name> -n openshift-adp
    ```

2.  Add the `concurrentBackups` field in the `spec.configuration.velero` section of your DPA CR:

    ``` yaml
      configuration:
        velero:
          concurrentBackups: <integer_limit>
          defaultPlugins:
            - openshift
            - aws
            - csi
    ```

    Replace `<integer_limit>` with the maximum number of backups you want OADP to process simultaneously. The default value is `1`. Backups that target overlapping namespaces are automatically serialized.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that all backups are in the `InProgress` phase simultaneously:

  ``` terminal
  $ oc get backups.velero.io -n openshift-adp
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                STATUS       CREATED                        EXPIRES
  backup-namespace1   InProgress   2026-04-28 10:00:00 +0000 UTC  29d
  backup-namespace2   InProgress   2026-04-28 10:00:05 +0000 UTC  29d
  ```

  </div>

</div>
