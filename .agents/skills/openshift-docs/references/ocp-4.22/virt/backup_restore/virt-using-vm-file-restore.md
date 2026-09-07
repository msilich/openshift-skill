<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Discover VM backups, restore files, and access restored files through a web browser or SSH-based tools.

# Enable OADP VMFR

Enable OADP virtual machine file restore (VMFR) by configuring the `DataProtectionApplication` (DPA) custom resource (CR) with the `vmFileRestore` section. You can allow file-level restore operations for VM backups.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster with the `cluster-admin` role.

- The OADP Operator is installed.

- The `DataProtectionApplication` (DPA) CR is configured.

- OpenShift Virtualization is installed and running on the cluster.

- You have a default storage class configured on the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `DataProtectionApplication` CR to enable the VMFR feature:

    ``` yaml
    apiVersion: oadp.openshift.io/v1alpha1
    kind: DataProtectionApplication
    metadata:
      name: oadp-backup
      namespace: openshift-adp
    spec:
      configuration:
        nodeAgent:
          enable: true
          uploaderType: kopia
        velero:
          defaultPlugins:
            - kubevirt
            - csi
            - openshift
            - aws
          disableFsBackup: false
      vmFileRestore:
        enable: true
      backupLocations:
        - velero:
            config:
              profile: "default"
              region: <region>
            provider: aws
            default: true
            credential:
              key: cloud
              name: <cloud_credentials>
            objectStorage:
              bucket: <bucket_name>
              prefix: velero
    ```

    where:

    `kubevirt`
    Specifies the `kubevirt` Velero plugin in the `defaultPlugins` list. This plugin is required for VM backup and file-level restore operations.

    `vmFileRestore`
    Specifies the section in the DPA `spec` to enable the VMFR feature.

    `enable`
    Specifies whether to enable the VMFR feature. Set to `true` to enable the feature.

2.  Apply the DPA configuration by running the following command:

    ``` terminal
    $ oc apply -f <dpa_cr_filename>
    ```

    Replace `<dpa_cr_filename>` with the file name containing the DPA CR configuration.

</div>

<div>

<div class="title">

Verification

</div>

1.  To verify that the DPA is reconciled with the VMFR feature enabled, run the following command:

    ``` terminal
    $ oc get dpa -n openshift-adp -o yaml
    ```

    In the output, verify that the `status.conditions` section includes a condition with `type: VMFileRestoreReady` and `status: "True"`.

2.  To verify that the `oadp-vm-file-restore-controller-manager` pod is running, run the following command:

    ``` terminal
    $ oc get pod -n openshift-adp
    ```

    The output should include a running `oadp-vm-file-restore-controller-manager` pod.

</div>

# Create a VirtualMachineBackupsDiscovery CR

Create a `VirtualMachineBackupsDiscovery` (VMBD) custom resource (CR) to identify which Velero backups contain a specified virtual machine (VM). You can locate available backups before performing a file-level restore.

After you create a VMBD CR, the CR undergoes the following phases:

- The initial phase for the CR is `New`.

- The controller compiles candidate backups and verifies VM presence in each backup.

- Upon successful discovery, the `status.phase` field of the VMBD CR is updated to `Completed`.

> [!IMPORTANT]
> Create all VMFR custom resources in the protected namespace, which is `openshift-adp` by default.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster with the `cluster-admin` role.

- You have installed the OADP Operator.

- You have configured the `DataProtectionApplication` (DPA) CR with the VMFR feature enabled.

- You have existing Velero backups that contain virtual machine data.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `VirtualMachineBackupsDiscovery` CR YAML manifest file with the following configuration:

    ``` yaml
    apiVersion: oadp.openshift.io/v1alpha1
    kind: VirtualMachineBackupsDiscovery
    metadata:
      name: find-my-vm-backups
      namespace: openshift-adp
    spec:
      virtualMachineName: "production-web-server"
      virtualMachineNamespace: "production"
    ```

    where:

    `name`
    Specifies a name for the VMBD CR. For example, `find-my-vm-backups`.

    `namespace`
    Specifies the namespace where the VMBD CR is created. This must be the OADP protected namespace, typically `openshift-adp`.

    `virtualMachineName`
    Specifies the name of the virtual machine to search for in backups. For example, `production-web-server`.

    `virtualMachineNamespace`
    Specifies the namespace of the target virtual machine. For example, `production`.

2.  Optional: To filter backups by a time range, add `startTime` and `endTime` fields to the `spec` section:

    ``` yaml
    apiVersion: oadp.openshift.io/v1alpha1
    kind: VirtualMachineBackupsDiscovery
    metadata:
      name: find-my-vm-backups
      namespace: openshift-adp
    spec:
      virtualMachineName: "production-web-server"
      virtualMachineNamespace: "production"
      startTime: "2025-08-01"
      endTime: "2025-09-01"
    ```

    where:

    `startTime`
    Specifies the start of the time range to filter backups. Backups created before this date are excluded.

    `endTime`
    Specifies the end of the time range to filter backups. Backups created after this date are excluded.

3.  Optional: To discover specific backups by name, add the `requestedBackups` field to the `spec` section:

    ``` yaml
    apiVersion: oadp.openshift.io/v1alpha1
    kind: VirtualMachineBackupsDiscovery
    metadata:
      name: find-my-vm-backups
      namespace: openshift-adp
    spec:
      virtualMachineName: "production-web-server"
      virtualMachineNamespace: "production"
      requestedBackups:
        - "initial-backup-from-2024-01-01"
        - "last-working-from-2025-07-28"
    ```

    where:

    `requestedBackups`
    Specifies a list of backup names to include in the discovery. These backups are included regardless of any time range filter.

4.  To apply the VMBD CR configuration, run the following command:

    ``` terminal
    $ oc apply -f <vmbd_cr_filename>
    ```

    Replace `<vmbd_cr_filename>` with the file name containing the VMBD CR configuration.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the VMBD CR is successfully created and discovery is complete, run the following command:

  ``` terminal
  $ oc get vmbd find-my-vm-backups -n openshift-adp -o yaml
  ```

  ``` yaml
  apiVersion: oadp.openshift.io/v1alpha1
  kind: VirtualMachineBackupsDiscovery
  metadata:
    name: find-my-vm-backups
    namespace: openshift-adp
  spec:
    virtualMachineName: "production-web-server"
    virtualMachineNamespace: "production"
  status:
    phase: Completed
    validBackups:
      - name: "backup-2025-09-20"
        namespace: openshift-adp
        createdAt: "2025-09-20T02:00:00Z"
      - name: "backup-2025-09-15"
        namespace: openshift-adp
        createdAt: "2025-09-15T02:00:00Z"
    backupDiscoveryProgress:
      - name: "backup-2025-09-20"
        namespace: openshift-adp
        status: Completed
        message: "VM found in backup"
        createdAt: "2025-09-20T02:00:00Z"
      - name: "backup-2025-09-15"
        namespace: openshift-adp
        status: Completed
        message: "VM found in backup"
        createdAt: "2025-09-15T02:00:00Z"
    conditions:
      - type: Ready
        status: "True"
        message: "Successfully discovered 2 valid backups"
        reason: DiscoverySuccessful
    discoveryStats:
      totalCandidates: 2
      completed: 2
      failed: 0
      inProgress: 0
      pending: 0
      skipped: 0
    observedGeneration: 1
  ```

  where:

  `phase: Completed`
  Specifies that the discovery process is complete.

  `validBackups`
  Specifies the list of backups that contain the specified virtual machine. Each entry includes the `name`, `namespace`, and `createdAt` timestamp.

  `backupDiscoveryProgress`
  Specifies the discovery progress for each candidate backup, including the `status` and `message`.

  `discoveryStats`
  Specifies the total number of candidate backups processed and the count of completed, failed, in-progress, pending, and skipped results.

  `observedGeneration`
  Specifies the last generation value processed by the controller.

</div>

# Create a VirtualMachineFileRestore CR

Create a `VirtualMachineFileRestore` (VMFR) custom resource (CR) to make files from discovered virtual machine (VM) backups accessible for browsing and downloading. You can recover individual files without restoring the entire VM.

After you create a VMFR CR, the CR undergoes the following phases:

- The initial phase for the CR is `New`.

- The controller validates the referenced discovery, restores PVCs, and creates file-serving resources.

- Upon successful setup, the `status.phase` field of the VMFR CR is updated to `Completed`.

> [!NOTE]
> All VMFR custom resources must be created in the protected namespace, which is `openshift-adp` by default.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster with the `cluster-admin` role.

- You have installed the OADP Operator.

- You have configured the `DataProtectionApplication` (DPA) CR with the VMFR feature enabled.

- You have created a `VirtualMachineBackupsDiscovery` (VMBD) CR and its `status.phase` is `Completed`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  \[Optional\] Create a secret containing the credentials for accessing the file browser:

    If you do not create a secret, the VMFR controller creates a secret for you and references it in the VMFR CR.

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: vmfr-credentials
      namespace: openshift-adp
    type: Opaque
    data:
      password: <base64_encoded_password>
      username: <base64_encoded_username>
    ```

    where:

    `password`
    Specifies the base64-encoded password for the file browser. The password must be at least 12 characters long before encoding.

    `username`
    Specifies the base64-encoded username for the file browser.

2.  Create a `VirtualMachineFileRestore` CR YAML manifest file with the following configuration.

    To configure file browser access:

    ``` yaml
    apiVersion: oadp.openshift.io/v1alpha1
    kind: VirtualMachineFileRestore
    metadata:
      name: restore-config-files
      namespace: openshift-adp
    spec:
      backupsDiscoveryRef: find-my-vm-backups
      selectedBackups:
        - backup-2025-09-20
        - backup-2025-09-15
      fileAccess:
        fileBrowser:
          credentialsSecretRef:
            name: vmfr-credentials
          exposeExternally: true
    ```

    To configure SSH access:

    ``` yaml
    apiVersion: oadp.openshift.io/v1alpha1
    kind: VirtualMachineFileRestore
    metadata:
      name: restore-config-files
      namespace: openshift-adp
    spec:
      backupsDiscoveryRef: find-my-vm-backups
      selectedBackups:
        - backup-2025-09-20
        - backup-2025-09-15
      fileAccess:
        ssh: {}
    ```

    where:

    `name`
    Specifies a name for the VMFR CR. For example, `restore-config-files`.

    `namespace`
    Specifies the namespace where the VMFR CR is created. This must be the OADP protected namespace, typically `openshift-adp`.

    `backupsDiscoveryRef`
    Specifies the name of the VMBD CR that contains the discovery results. This VMBD CR must be in the `Completed` phase.

    `selectedBackups`
    Specifies a list of backup names from the VMBD valid results to restore. A Velero restore operation is created for each backup in this list.

    `fileAccess`
    Specifies the configuration for accessing the restored files.

    `fileBrowser`
    Specifies the file browser configuration for web-based access.

    `credentialsSecretRef`
    Specifies the name of the Kubernetes secret that contains the credentials for file browser access.

    `exposeExternally`
    Specifies whether to create an external route for accessing the file browser. Set to `true` to create a publicly accessible route.

    `ssh`
    Specifies the SSH access configuration. Set to `{}` to enable SSH access with autogenerated credentials. The controller generates an SSH key pair and stores it in a Kubernetes secret.

    Optionally, you can also specify a `username`, and `publickey` for enabling the SSH access as shown in the following example:

    ``` yaml
    ...
       ssh:
         username: fedora
         publicKey: ""
    ```

3.  To apply the VMFR CR configuration, run the following command:

    ``` terminal
    $ oc apply -f <vmfr_cr_filename>
    ```

    Replace `<vmfr_cr_filename>` with the file name containing the VMFR CR configuration.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the VMFR CR is successfully created and file access is available, run the following command:

  ``` terminal
  $ oc get vmfr restore-config-files -n openshift-adp -o yaml
  ```

  ``` yaml
  apiVersion: oadp.openshift.io/v1alpha1
  kind: VirtualMachineFileRestore
  metadata:
    name: restore-config-files
    namespace: openshift-adp
  spec:
    backupsDiscoveryRef: find-my-vm-backups
    selectedBackups:
      - backup-2025-09-20
      - backup-2025-09-15
    fileAccess:
      fileBrowser:
        credentialsSecretRef:
          name: vmfr-credentials
        exposeExternally: true
  status:
    phase: Completed
    fileServingInfo:
      fileBrowser:
        clusterAccess: https://restore-config-files-fileserver-svc.production-production-web-server-a1b2c3.svc.cluster.local:8443
        publicAccess: https://restore-config-files.vmfr.apps.example.com
        credentialsSecretRef:
          name: restore-config-files-filebrowser-xk4wm
          namespace: production-production-web-server-a1b2c3
    conditions:
      - type: Ready
        status: "True"
        message: "File restore completed, files accessible via file server and external route"
        reason: Completed
      - type: Available
        status: "True"
        message: "File server is accessible and serving files"
        reason: FileServerAvailable
    pvcRestores:
      - pvcName: production-web-server-dv
        pvcNamespace: production
        pvcUID: 05ac1521-2a16-4a71-b81f-ccad592b89cd
        restores:
          - veleroBackupName: backup-2025-09-20
            veleroBackupNamespace: openshift-adp
            veleroRestoreName: vmfr-restore-config-files-backup-2025-09-20-89lfl
            veleroRestoreNamespace: openshift-adp
            phase: Completed
            state: available
            timestamp: "2025-09-20T02:00:00Z"
          - veleroBackupName: backup-2025-09-15
            veleroBackupNamespace: openshift-adp
            veleroRestoreName: vmfr-restore-config-files-backup-2025-09-15-bfqx4
            veleroRestoreNamespace: openshift-adp
            phase: Completed
            state: available
            timestamp: "2025-09-15T02:00:00Z"
        size: 150Mi
    createdNamespace: production-production-web-server-a1b2c3
    observedGeneration: 1
  ```

  where:

  `phase: Completed`
  Specifies that the file restore process is complete and file-serving endpoints are available.

  `fileServingInfo.fileBrowser`
  Specifies the endpoint details and credentials for accessing the restored files through the file browser.

  `clusterAccess`
  Specifies the cluster-internal URL for accessing the file browser.

  `publicAccess`
  Specifies the externally accessible URL for the file browser. This field is present only when `exposeExternally` is set to `true`.

  `credentialsSecretRef`
  Specifies the Kubernetes secret that contains the generated credentials for accessing the file browser interface, including the `name` and `namespace` of the secret.

  `pvcRestores`
  Specifies the restore status grouped by PVC. Each PVC entry includes the `pvcName`, `pvcNamespace`, `pvcUID`, and a `restores` list with details for each backup restore.

  `state`
  Specifies the state of the restored PVC. Possible values include `available`, `processing`, `failed`, `backup-deleted`, `backup-missing`, `unsupported-plugin`, and `extraction-failed`.

  `createdNamespace`
  Specifies the temporary namespace created for hosting the file-serving resources. This namespace is cleaned up when you delete the VMFR CR.

</div>

# Access restored files through a web browser

Access restored virtual machine (VM) files through a web browser by using the file browser interface provided by the `VirtualMachineFileRestore` (VMFR) custom resource (CR). You can browse, preview, and download files from VM backups.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster with the `cluster-admin` role.

- A `VirtualMachineFileRestore` (VMFR) CR with the `fileAccess.fileBrowser` section configured exists.

- The VMFR CR `status.phase` is `Completed`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To retrieve the file browser access URLs, run the following command:

    ``` terminal
    $ oc get vmfr <vmfr_cr_name> -n openshift-adp -o jsonpath='{.status.fileServingInfo.fileBrowser}'
    ```

    Replace `<vmfr_cr_name>` with the name of the VMFR CR. The output includes the `clusterAccess` URL for cluster-internal access and the `publicAccess` URL if `exposeExternally` is set to `true`.

2.  If the VMFR CR has `exposeExternally` set to `true`, open a web browser and navigate to the `publicAccess` URL from the status output.

    If `exposeExternally` is not enabled, set up port forwarding to the file-serving service by running the following command:

    ``` terminal
    $ oc port-forward svc/vmfr-<vmfr_cr_name>-fileserver-svc -n <restore_namespace> 8443:8443
    ```

    Replace `<vmfr_cr_name>` with the name of the VMFR CR and `<restore_namespace>` with the namespace from the `status.createdNamespace` field. Then navigate to `https://localhost:8443` in your web browser.

3.  Log in by using the credentials from the secret you created for file browser access.

    <figure>
    <img src="data:image/png;base64,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" alt="OADP VM File Restore Browser login page" />
    <figcaption aria-hidden="true">OADP VM File Restore Browser login page</figcaption>
    </figure>

4.  Browse the files organized by date, backup name, and PVC name.

    <figure>
    <img src="data:image/png;base64,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" alt="File browser listing showing backup contents" />
    <figcaption aria-hidden="true">File browser listing showing backup contents</figcaption>
    </figure>

5.  View the file content by selecting the file. To download a file, select the file and click **Download**. To download a directory as an archive, select the directory and click **Download**.

    <figure>
    <img src="data:image/png;base64,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AAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACBH+AQAAAAAAAAAAQIjwDwAAAAAAAAAAAEKEfwAAAAAAAAAAABAi/AMAAAAAAAAAAIAQ4R8AAAAAAAAAAACECP8AAAAAAAAAAAAgRPgHAAAAAAAAAAAAIcI/AAAAAAAAAAAACPkDFBtMQ2g5k8IAAAAASUVORK5CYII=" alt="File preview in the file browser" />
    <figcaption aria-hidden="true">File preview in the file browser</figcaption>
    </figure>

</div>

# Access restored files through SSH

Access restored virtual machine (VM) files through SSH by using `rsync`, `scp`, or `sftp` with the `VirtualMachineFileRestore` (VMFR) custom resource (CR). You can transfer files from VM backups efficiently.

When you configure SSH access, the VMFR controller autogenerates an SSH key pair and stores it in a Kubernetes secret. The default SSH username is `oadp`. The SSH file server listens on port `2222`.

The remote path for restored files follows the format `/restores/<date>/<backup_name>/<vm_name>/<path_to_file>`.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster with the `cluster-admin` role.

- You have created a `VirtualMachineFileRestore` (VMFR) CR with the `fileAccess.ssh` section configured.

- The VMFR CR `status.phase` is `Completed`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To retrieve the SSH access information, run the following command:

    ``` terminal
    $ oc get vmfr <vmfr_cr_name> -o jsonpath='{.status.fileServingInfo.ssh}' | jq
    ```

    Replace `<vmfr_cr_name>` with the name of the VMFR CR. The output includes the `clusterAccess` URL and `credentialsSecretRef` containing the name and namespace of the generated SSH key secret.

2.  Retrieve the private key from the generated secret and save it to a file:

    ``` terminal
    $ oc get secret <secret_name> -n <secret_namespace> -o jsonpath='{.data.privateKey}' | base64 -d > id-rsa
    ```

    Replace `<secret_name>` and `<secret_namespace>` with the values from the `status.fileServingInfo.ssh.credentialsSecretRef` field.

3.  Set the correct permissions on the private key file:

    ``` terminal
    $ chmod 600 id-rsa
    ```

4.  Get the name of the file server service created in the VMFR namespace:

    ``` terminal
    $ oc get svc -n <created_namespace> | grep fileserver
    ```

    Replace `<created_namespace>` with the value from the `status.createdNamespace` field of the VMFR CR.

5.  To copy a file from the backup by using `scp`, run the following command:

    ``` terminal
    $ scp -P 2222 -i id-rsa \
      -o StrictHostKeyChecking=no \
      -o UserKnownHostsFile=/dev/null \
      oadp@<fileserver_svc>.<created_namespace>.svc.cluster.local:<remote_path> \
      <local_destination>
    ```

    where:

    `<fileserver_svc>`
    Specifies the name of the file server service.

    `<created_namespace>`
    Specifies the namespace from the `status.createdNamespace` field.

    `<remote_path>`
    Specifies the path to the file in the format `/restores/<date>/<backup_name>/<vm_name>/<path_to_file>`.

    `<local_destination>`
    Specifies the local file path to save the restored file.

6.  To start an interactive SFTP session, run the following command:

    ``` terminal
    $ sftp -P 2222 -i id-rsa \
      -o StrictHostKeyChecking=no \
      oadp@<fileserver_svc>.<created_namespace>.svc.cluster.local
    ```

</div>

# Delete a VirtualMachineFileRestore CR

Delete a `VirtualMachineFileRestore` (VMFR) custom resource (CR) to clean up file-serving resources after you have recovered the files you need. This helps you free cluster resources used by the file-serving pod and temporary namespace.

When you delete a VMFR CR, the controller performs the following cleanup operations:

- Stops the file-serving pod and associated services.

- Deletes the restored PVCs.

- Deletes the temporary namespace if one was automatically created.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster with the `cluster-admin` role.

- You have a `VirtualMachineFileRestore` CR that you want to delete.

</div>

<div>

<div class="title">

Procedure

</div>

- To delete a `VirtualMachineFileRestore` CR, run the following command:

  ``` terminal
  $ oc delete vmfr <vmfr_cr_name> -n openshift-adp
  ```

  Replace `<vmfr_cr_name>` with the name of the VMFR CR.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the VMFR CR is deleted and resources are cleaned up, run the following command:

  ``` terminal
  $ oc get vmfr -n openshift-adp
  ```

  The deleted VMFR CR should not appear in the output.

</div>

# Test the VM file restore workflow

Complete an end-to-end workflow that creates a VM, backs it up, and restores individual files through SSH to test the VM file restore feature or verify your configuration.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster with the `cluster-admin` role.

- You have installed the OADP Operator.

- OpenShift Virtualization is installed and running on the cluster.

- You have installed the `virtctl` CLI tool to access the VM.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a secret for the cloud storage credentials by running the following command:

    ``` terminal
    $ oc create secret generic <secret_name> -n openshift-adp --from-file cloud=<credentials_file_path>
    ```

    where:

    `<secret_name>`
    Specifies the name of the cloud credentials secret.

    `<credentials_file_path>`
    Specifies the path to the file that contains the cloud storage credentials.

2.  Create a `DataProtectionApplication` (DPA) CR with the VMFR feature enabled and the `kubevirt` plugin:

    ``` yaml
    apiVersion: oadp.openshift.io/v1alpha1
    kind: DataProtectionApplication
    metadata:
      name: vmfr-dpa
      namespace: openshift-adp
    spec:
      backupLocations:
        - velero:
            credential:
              key: cloud
              name: <secret_name>
            default: true
            objectStorage:
              bucket: <bucket_name>
              prefix: velero
            provider: <provider>
      configuration:
        velero:
          defaultPlugins:
            - csi
            - openshift
            - kubevirt
            - <provider>
          disableFsBackup: false
        nodeAgent:
          enable: true
          uploaderType: kopia
      vmFileRestore:
        enable: true
    ```

    where:

    `<secret_name>`
    Specifies the name of the cloud credentials secret you created.

    `<bucket_name>`
    Specifies the name of the object storage bucket.

    `<provider>`
    Specifies the cloud provider plugin, such as `aws`, `gcp`, or `azure`.

    `vmFileRestore`
    Enables the VMFR feature by setting the `enable` field to `true`.

3.  Apply the DPA configuration by running the following command:

    ``` terminal
    $ oc apply -f <dpa_cr_filename>
    ```

4.  Verify that the DPA is reconciled and the VMFR feature is enabled by running the following command:

    ``` terminal
    $ oc get dpa -n openshift-adp -o yaml
    ```

    In the output, verify that the `status.conditions` section includes a condition with `type: VMFileRestoreReady` and `status: "True"`.

5.  Verify that the `velero`, `nodeAgent`, and `oadp-vm-file-restore-controller-manager` pods are running by running the following command:

    ``` terminal
    $ oc get pod -n openshift-adp
    ```

6.  Generate an SSH key pair for accessing the VM:

    ``` terminal
    $ ssh-keygen -t ed25519 -f ~/.ssh/<vm_key_name> -C "<vm_key_name>"
    ```

    Replace `<vm_key_name>` with a name for the SSH folder and the key file.

7.  Create a namespace for the VM by running the following command:

    ``` terminal
    $ oc create ns <vm_namespace>
    ```

8.  Create a Kubernetes secret with the SSH public key in the VM namespace:

    ``` terminal
    $ oc create secret generic <ssh_secret_name> \
      --from-file=key=<path_to_public_key> \
      -n <vm_namespace>
    ```

    where:

    `<ssh_secret_name>`
    Specifies the name of the secret that contains the SSH public key.

    `<path_to_public_key>`
    Specifies the path to the SSH public key file you created in an earlier step. For example, `$HOME/.ssh/vm-key.pub`.

    `<vm_namespace>`
    Specifies the namespace for the VM.

9.  Create a `VirtualMachine` CR by using the built-in VM template `fedora-server-small`:

    ``` terminal
    $ oc process -n openshift fedora-server-small -p NAME=<vm_name> | oc apply -n <vm_namespace> -f -
    ```

    where:

    `<vm_name>`
    Specifies the name of the VM.

    `<vm_namespace>`
    Specifies the namespace for the VM.

10. Wait for the VM to be ready:

    ``` terminal
    $ oc wait --for=condition=Ready vmi/<vm_name> -n <vm_namespace>
    ```

11. Patch the VM configuration `accessCredentials` object with the SSH public key:

    ``` terminal
    $ oc patch vm <vm_name> -n <vm_namespace> --type=merge -p '{"spec":{"template":{"spec":{"accessCredentials":[{"sshPublicKey":{"propagationMethod":{"noCloud":{}},"source":{"secret":{"secretName":"<ssh_secret_name>"}}}}]}}}}'
    ```

    where:

    `<vm_name>`
    Specifies the name of the VM.

    `<vm_namespace>`
    Specifies the namespace for the VM.

    `<ssh_secret_name>`
    Specifies the name of the secret that contains the SSH public key.

12. SSH to the VM and create a test file:

    ``` terminal
    $ virtctl ssh <vm_user>@vmi/<vm_name> \
      -n <vm_namespace> \
      --identity-file=$HOME/.ssh/<vm_key_name> \
      --local-ssh-opts="-o StrictHostKeyChecking=no" \
      -c "echo 'Test file for VMFR validation - $(date)' > /home/fedora/test-vmfr-file.txt"
    ```

    where:

    `<vm_user>`
    Specifies the name of the VM user. For the in-built VM template, the user name is `fedora`.

13. Create a `Backup` CR to back up the VM namespace:

    ``` yaml
    apiVersion: velero.io/v1
    kind: Backup
    metadata:
      name: <backup_name>
      namespace: openshift-adp
    spec:
      includedNamespaces:
        - <vm_namespace>
      snapshotMoveData: true
    ```

14. Apply the `Backup` CR by running the following command:

    ``` terminal
    $ oc apply -f <backup_cr_filename>
    ```

15. Verify that the backup is complete by running the following command:

    ``` terminal
    $ oc get backup.velero <backup_name> -n openshift-adp -o jsonpath='{.status.phase}'
    ```

    The output should display `Completed`.

16. Create a `VirtualMachineBackupsDiscovery` CR to identify which backups contain the target VM:

    ``` yaml
    apiVersion: oadp.openshift.io/v1alpha1
    kind: VirtualMachineBackupsDiscovery
    metadata:
      name: <vmbd_name>
      namespace: openshift-adp
    spec:
      virtualMachineName: <vm_name>
      virtualMachineNamespace: <vm_namespace>
    ```

17. Apply the VMBD CR by running the following command:

    ``` terminal
    $ oc apply -f <vmbd_cr_filename>
    ```

18. Verify that the discovery is complete by running the following command:

    ``` terminal
    $ oc get vmbd <vmbd_name> -n openshift-adp
    ```

    The `PHASE` column should display `Completed`.

19. Create a `VirtualMachineFileRestore` CR with SSH access to restore files from the discovered backups:

    ``` yaml
    apiVersion: oadp.openshift.io/v1alpha1
    kind: VirtualMachineFileRestore
    metadata:
      name: <vmfr_name>
      namespace: openshift-adp
    spec:
      backupsDiscoveryRef: <vmbd_name>
      fileAccess:
        ssh: {}
    ```

    The `ssh: {}` configuration instructs the controller to autogenerate an SSH key pair and store it in a Kubernetes secret. The default SSH username is `oadp`.

20. Apply the VMFR CR by running the following command:

    ``` terminal
    $ oc apply -f <vmfr_cr_filename>
    ```

21. Wait for the VMFR phase to complete:

    ``` terminal
    $ oc get vmfr <vmfr_name> -n openshift-adp
    ```

    The `PHASE` column should display `Completed`.

22. Retrieve the SSH access information by running the following command:

    ``` terminal
    $ oc get vmfr <vmfr_name> -o jsonpath='{.status.fileServingInfo.ssh}' | jq
    ```

    The output includes the `clusterAccess` URL and the `credentialsSecretRef` containing the name and namespace of the auto generated SSH key secret.

23. Retrieve the private key from the auto generated secret and save it to a file:

    ``` terminal
    $ oc get secret <secret_name> -n <secret_namespace> -o jsonpath='{.data.privateKey}' | base64 -d > id-rsa
    ```

    Replace `<secret_name>` and `<secret_namespace>` with the values from the `status.fileServingInfo.ssh.credentialsSecretRef` field.

24. Copy the private key to the VM so that you can use it for `scp` from within the VM:

    ``` terminal
    $ virtctl scp id-rsa \
      <vm_user>@vmi/<vm_name>:/home/<vm_user>/id-rsa \
      -n <vm_namespace> \
      --identity-file=$HOME/.ssh/<vm_key_name>
    ```

25. Update the file permissions on the private key inside the VM:

    ``` terminal
    $ virtctl ssh <vm_user>@vmi/<vm_name> \
      -n <vm_namespace> \
      --identity-file=$HOME/.ssh/<vm_key_name> \
      --local-ssh-opts="-o StrictHostKeyChecking=no" \
      -c "chmod 600 /home/<vm_user>/id-rsa"
    ```

26. Get the name of the file server service created in the VMFR namespace:

    ``` terminal
    $ SVC=$(oc get svc -n <created_namespace> | grep fileserver | awk '{print $1}')
    ```

    Replace `<created_namespace>` with the value from the `status.createdNamespace` field of the VMFR CR.

27. Restore the file by using `scp` from within the VM. The remote path format is `/restores/<date>/<backup_name>/<vm_name>/<path_to_file>`:

    ``` terminal
    $ virtctl ssh <vm_user>@vmi/<vm_name> \
      -n <vm_namespace> \
      --identity-file=$HOME/.ssh/<vm_key_name> \
      --local-ssh-opts="-o StrictHostKeyChecking=no" \
      -c "scp -P 2222 \
      -i /home/<vm_user>/id-rsa \
      -o StrictHostKeyChecking=no \
      -o UserKnownHostsFile=/dev/null \
      oadp@<fileserver_svc>.<created_namespace>.svc.cluster.local:<remote_path> \
      /tmp/restored.txt"
    ```

    where:

    `<fileserver_svc>`
    Specifies the name of the file server service you retrieved in an earlier step.

    `<created_namespace>`
    Specifies the namespace from the `status.createdNamespace` field.

    `<remote_path>`
    Specifies the path to the file in the format `/restores/<date>/<backup_name>/<vm_name>/<path_to_file>`. For example, `"/restores/2026-02-10/test-backup/fedora-vm-test/home/fedora/test-vmfr-file.txt"`

28. Verify that the restored file is intact by comparing MD5 checksums:

    ``` terminal
    $ virtctl ssh <vm_user>@vmi/<vm_name> \
      -n <vm_namespace> \
      --identity-file=$HOME/.ssh/<vm_key_name> \
      --local-ssh-opts="-o StrictHostKeyChecking=no" \
      -c "echo '===MD5 Checksums===' && md5sum /home/fedora/test-vmfr-file.txt /tmp/restored.txt"
    ```

    The checksums of the original and restored files should match. You should see an output as shown in the following example:

    ``` terminal
    ===MD5 Checksums===
    92245490c552e83baf5f2a2e898d9fff  /home/fedora/test-vmfr-file.txt
    92245490c552e83baf5f2a2e898d9fff  /tmp/restored.txt
    ```

29. After you have recovered the files, delete the VMFR CR to clean up resources:

    ``` terminal
    $ oc delete vmfr <vmfr_name> -n openshift-adp
    ```

</div>

# Additional resources

- [Recover individual files from virtual machine backups](virt-recovering-individual-files-from-vm-backups.md#virt-recovering-individual-files-from-vm-backups)

- [Backing up and restoring virtual machines](virt-backup-restore-overview.md#virt-backup-restore-overview)

- [Introduction to OpenShift API for Data Protection](../../backup_and_restore/application_backup_and_restore/oadp-intro.md#oadp-introduction)
