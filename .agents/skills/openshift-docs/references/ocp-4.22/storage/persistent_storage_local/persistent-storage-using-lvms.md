<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Logical Volume Manager (LVM) Storage uses LVM2 through the `TopoLVM CSI` driver to dynamically provision local storage on a cluster with limited resources. With LVM Storage, you can create volume groups, persistent volume claims (PVCs), snapshots, and clones.

# Logical Volume Manager Storage installation

You can install LVM Storage on an OpenShift Container Platform cluster and configure it to dynamically provision storage for your workloads.

You can install LVM Storage by using the OpenShift Container Platform CLI (`oc`), OpenShift Container Platform web console, or Red Hat Advanced Cluster Management (RHACM).

> [!WARNING]
> When using LVM Storage on multi-node clusters, LVM Storage only supports provisioning local storage. LVM Storage does not support storage data replication mechanisms across nodes. You must ensure storage data replication through active or passive replication mechanisms to avoid a single point of failure.

## Prerequisites to install LVM Storage

The prerequisites to install LVM Storage are as follows:

- Ensure that you have a minimum of 10 milliCPU and 100 MiB of RAM.

- Ensure that every managed cluster has dedicated disks that are used to provision storage. LVM Storage uses only those disks that are empty and do not contain file system signatures. To ensure that the disks are empty and do not contain file system signatures, wipe the disks before using them.

- Before installing LVM Storage in a private CI environment where you can reuse the storage devices that you configured in the previous LVM Storage installation, ensure that you have wiped the disks that are not in use. If you do not wipe the disks before installing LVM Storage, you cannot reuse the disks without manual intervention.

  > [!NOTE]
  > You cannot wipe the disks that are in use.

- If you want to install LVM Storage by using Red Hat Advanced Cluster Management (RHACM), ensure that you have installed RHACM on an OpenShift Container Platform cluster. For more information, see "Installing LVM Storage by using RHACM".

## Installing LVM Storage by using the CLI

You can install LVM Storage by using the OpenShift CLI (`oc`) to dynamically provision local storage on clusters with limited resources.

> [!NOTE]
> The default namespace for the LVM Storage Operator is `openshift-lvm-storage`.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to OpenShift Container Platform as a user with `cluster-admin` and Operator installation permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file with the configuration for creating a namespace:

    <div class="formalpara">

    <div class="title">

    Example YAML configuration for creating a namespace

    </div>

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      labels:
        openshift.io/cluster-monitoring: "true"
        pod-security.kubernetes.io/enforce: privileged
        pod-security.kubernetes.io/audit: privileged
        pod-security.kubernetes.io/warn: privileged
      name: openshift-lvm-storage
    ```

    </div>

2.  Create the namespace by running the following command:

    ``` terminal
    $ oc create -f <file_name>
    ```

3.  Create an `OperatorGroup` CR YAML file:

    <div class="formalpara">

    <div class="title">

    Example `OperatorGroup` CR

    </div>

    ``` yaml
    apiVersion: operators.coreos.com/v1
    kind: OperatorGroup
    metadata:
      name: openshift-storage-operatorgroup
      namespace: openshift-lvm-storage
    spec:
      targetNamespaces:
      - openshift-storage
    ```

    </div>

4.  Create the `OperatorGroup` CR by running the following command:

    ``` terminal
    $ oc create -f <file_name>
    ```

5.  Create a `Subscription` CR YAML file:

    <div class="formalpara">

    <div class="title">

    Example `Subscription` CR

    </div>

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: lvms
      namespace: openshift-lvm-storage
    spec:
      installPlanApproval: Automatic
      name: lvms-operator
      source: redhat-operators
      sourceNamespace: openshift-marketplace
    ```

    </div>

6.  Create the `Subscription` CR by running the following command:

    ``` terminal
    $ oc create -f <file_name>
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  To verify that LVM Storage is installed, run the following command:

    ``` terminal
    $ oc get csv -n openshift-lvm-storage -o custom-columns=Name:.metadata.name,Phase:.status.phase
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name                         Phase
    4.13.0-202301261535          Succeeded
    ```

    </div>

</div>

## Installing LVM Storage by using the web console

Install LVM Storage from the OpenShift Container Platform web console to dynamically provision local storage on clusters with limited resources.

> [!NOTE]
> The default namespace for the LVM Storage Operator is `openshift-lvm-storage`.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster.

- You have access to OpenShift Container Platform with `cluster-admin` and Operator installation permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Click **Ecosystem** → **Software Catalog**.

3.  Click **LVM Storage** on the software catalog page.

4.  Set the following options on the **Operator Installation** page:

    1.  **Update Channel** as **stable-4.22**.

    2.  **Installation Mode** as **A specific namespace on the cluster**.

    3.  **Installed Namespace** as **Operator recommended namespace openshift-storage**. If the `openshift-lvm-storage` namespace does not exist, it is created during the operator installation.

    4.  **Update approval** as **Automatic** or **Manual**.

        > [!NOTE]
        > If you select **Automatic** updates, the Operator Lifecycle Manager (OLM) automatically updates the running instance of LVM Storage without any intervention.
        >
        > If you select **Manual** updates, the OLM creates an update request. As a cluster administrator, you must manually approve the update request to update LVM Storage to a newer version.

5.  Optional: Select the **Enable Operator recommended cluster monitoring on this Namespace** checkbox.

6.  Click **Install**.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that LVM Storage shows a green tick, indicating successful installation.

</div>

## Installing LVM Storage in a disconnected environment

Install LVM Storage in a disconnected environment where your cluster has no internet access, such as air-gapped networks, high-security facilities, or regulated industries requiring network isolation for security and compliance.

<div>

<div class="title">

Prerequisites

</div>

- You read "About disconnected installation mirroring".

- You have access to the OpenShift Container Platform image repository.

- You created a mirror registry (see "Creating a mirror registry with mirror registry for Red Hat OpenShift").

</div>

<div>

<div class="title">

Procedure

</div>

1.  Follow the steps in the "Creating the image set configuration" procedure. To create an `ImageSetConfiguration` custom resource (CR) for LVM Storage, you can use the following example `ImageSetConfiguration` CR configuration:

    <div class="formalpara">

    <div class="title">

    Example `ImageSetConfiguration` CR for LVM Storage

    </div>

    ``` yaml
    kind: ImageSetConfiguration
    apiVersion: mirror.openshift.io/v1alpha2
    archiveSize: 4
    storageConfig:
      registry:
        imageURL: example.com/mirror/oc-mirror-metadata
        skipTLS: false
    mirror:
      platform:
        channels:
        - name: stable-4.22
          type: ocp
        graph: true
      operators:
      - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.22
        packages:
        - name: lvms-operator
          channels:
          - name: stable
      additionalImages:
      - name: registry.redhat.io/ubi9/ubi:latest
      helm: {}
    ```

    </div>

    - `archiveSize`: Specifies the maximum size (in GiB) of each file within the image set.

    - `storageConfig`: Specifies the location in which you want to save the image set. This location can be a registry or a local directory. You must configure the `storageConfig` field unless you are using the Technology Preview OCI feature.

    - `storageConfig.registry.imageURL`: Specifies the storage URL for the image stream when using a registry. For more information, see "Why use imagestreams".

    - `mirror.platform.name`: Specifies the channel from which you want to retrieve the OpenShift Container Platform images.

    - `mirror.platform.channels[].name`: Set this field to `true` to generate the OpenShift Update Service (OSUS) graph image. For more information, see "About the OpenShift Update Service".

    - `mirror.operators.catalog`: Specifies the Operator catalog from which you want to retrieve the OpenShift Container Platform images.

    - `mirror.operators.packages.name`: Specifies the Operator packages to include in the image set. If this field is empty, all packages in the catalog are retrieved.

    - `mirror.operators[].packages[].channels.name`: Specifies the channels of the Operator packages to include in the image set. You must include the default channel for the Operator package even if you do not use the bundles in that channel. You can find the default channel by running the following command: `$ oc mirror list operators --catalog=<catalog_name> --package=<package_name>`.

    - `mirror.additionalImages.name`: Specifies any additional images to include in the image set.

2.  Follow the procedure in "Mirroring an image set to a mirror registry".

3.  Follow the procedure in "Configuring image registry repository mirroring".

</div>

<div>

<div class="title">

Additional resources

</div>

- [About disconnected installation mirroring](../../disconnected/index.md#installing-mirroring-disconnected-about)

- [Mirroring the OpenShift Container Platform image repository](../../disconnected/installing-mirroring-installation-images.md#installation-mirror-repository_installing-mirroring-installation-images)

- [Creating the image set configuration](../../disconnected/about-installing-oc-mirror-v2.md#oc-mirror-building-image-set-config-v2_about-installing-oc-mirror-v2)

- [Mirroring an image set to a mirror registry](../../disconnected/about-installing-oc-mirror-v2.md#using-oc-mirror_about-installing-oc-mirror-v2)

- [Configuring image registry repository mirroring](../../openshift_images/image-configuration.md#images-configuration-registry-mirror_image-configuration)

- [Why use imagestreams](../../openshift_images/image-streams-manage.md#images-imagestream-use_image-configuration)

- [About the OpenShift Update Service](../../updating/understanding_updates/intro-to-updates.md#update-service-overview_understanding-openshift-updates)

</div>

## Installing LVM Storage by using RHACM

To install LVM Storage on clusters by using Red Hat Advanced Cluster Management (RHACM), you must create a `Policy` custom resource (CR) and configure the criteria to select the target clusters.

> [!NOTE]
> The `Policy` CR that is created to install LVM Storage is also applied to the clusters that are imported or created after creating the `Policy` CR.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the RHACM cluster using an account with `cluster-admin` and Operator installation permissions.

- You have dedicated disks that LVM Storage can use on each cluster.

- The cluster must be managed by RHACM.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the RHACM CLI using your OpenShift Container Platform credentials.

2.  Create a namespace.

    ``` terminal
    $ oc create ns <namespace>
    ```

3.  Create a `Policy` CR YAML file:

    <div class="formalpara">

    <div class="title">

    Example `Policy` CR to install and configure LVM Storage

    </div>

    ``` yaml
    apiVersion: apps.open-cluster-management.io/v1
    kind: PlacementRule
    metadata:
      name: placement-install-lvms
    spec:
      clusterConditions:
      - status: "True"
        type: ManagedClusterConditionAvailable
      clusterSelector:
        matchExpressions:
        - key: mykey
          operator: In
          values:
          - myvalue
    ---
    apiVersion: policy.open-cluster-management.io/v1
    kind: PlacementBinding
    metadata:
      name: binding-install-lvms
    placementRef:
      apiGroup: apps.open-cluster-management.io
      kind: PlacementRule
      name: placement-install-lvms
    subjects:
    - apiGroup: policy.open-cluster-management.io
      kind: Policy
      name: install-lvms
    ---
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      annotations:
        policy.open-cluster-management.io/categories: CM Configuration Management
        policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
        policy.open-cluster-management.io/standards: NIST SP 800-53
      name: install-lvms
    spec:
      disabled: false
      remediationAction: enforce
      policy-templates:
      - objectDefinition:
          apiVersion: policy.open-cluster-management.io/v1
          kind: ConfigurationPolicy
          metadata:
            name: install-lvms
          spec:
            object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: v1
                kind: Namespace
                metadata:
                  labels:
                    openshift.io/cluster-monitoring: "true"
                    pod-security.kubernetes.io/enforce: privileged
                    pod-security.kubernetes.io/audit: privileged
                    pod-security.kubernetes.io/warn: privileged
                  name: openshift-lvm-storage
            - complianceType: musthave
              objectDefinition:
                apiVersion: operators.coreos.com/v1
                kind: OperatorGroup
                metadata:
                  name: openshift-storage-operatorgroup
                  namespace: openshift-lvm-storage
                spec:
                  targetNamespaces:
                  - openshift-lvm-storage
            - complianceType: musthave
              objectDefinition:
                apiVersion: operators.coreos.com/v1alpha1
                kind: Subscription
                metadata:
                  name: lvms
                  namespace: openshift-lvm-storage
                spec:
                  installPlanApproval: Automatic
                  name: lvms-operator
                  source: redhat-operators
                  sourceNamespace: openshift-marketplace
            remediationAction: enforce
            severity: low
    ```

    </div>

    - `spec.clusterSelector`: Set the `key` field and `values` field in `PlacementRule.spec.clusterSelector` to match the labels that are configured in the clusters on which you want to install LVM Storage.

    - `spec.policy-templates[0].objectDefinition[0].spec.object-templates[0].objectDefinition`: Specifies the namespace configuration.

    - `spec.policy-templates[0].objectDefinition[1].spec.object-templates[1].objectDefinition`: Specifies the `OperatorGroup` CR configuration.

    - `spec.policy-templates[0].objectDefinition.spec.object-templates[2].objectDefinition`:Specifies the `Subscription` CR configuration.

4.  Create the `Policy` CR by running the following command:

    ``` terminal
    $ oc create -f <file_name> -n <namespace>
    ```

    Upon creating the `Policy` CR, the following custom resources are created on the clusters that match the selection criteria configured in the `PlacementRule` CR:

    - `Namespace`

    - `OperatorGroup`

    - `Subscription`

      > [!NOTE]
      > The default namespace for the LVM Storage Operator is `openshift-lvm-storage`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the `LVMCluster` custom resource](persistent-storage-using-lvms.md#about-lvmcluster_logical-volume-manager-storage)

</div>

# Static and dynamic device discovery in LVM Storage

You can use static or dynamic discovery policies to manage how block devices join your volume groups. Selecting the appropriate policy helps you automate storage expansion safely or preserve a locked, predictable storage footprint over time.

Static
The Operator creates the volume group by using devices it finds at installation time. The Operator ignores devices discovered after the volume group exists.

Static discovery is the default policy for new volume groups. It eliminates operational risk by locking the device set after the Operator creates the volume group.

Combined with explicit device paths, it provides a fully deterministic storage configuration.

Without explicit paths, the Operator discovers devices only at creation time and then stops the set.

Dynamic
The Operator continuously discovers and adds devices to the volume group on each reconciliation cycle.

Dynamic discovery remains the default for existing volume groups where the policy field is nil to maintain backward compatibility.

However, this policy can lead to unexpected behavior in production environments. Devices that appear after the initial setup because of hardware changes, driver reloads, or kernel device renaming are automatically added to the volume group.

This creates operational risk because the volume group composition becomes non-deterministic and depends on the runtime state of the node rather than explicit administrator intent.

> [!NOTE]
> The Operator adds the `DeviceDiscoveryPolicy` field to the `DeviceClass` specification. If you explicitly set device paths in `deviceSelector.paths` or `deviceSelector.optionalPaths`, the cluster always uses those exact paths, and ignores your discovery policy setting.

The cluster status reports the effective policy by using `DeviceDiscoveryPolicyStatus`, which distinguishes three runtime states:

| Status value | Description |
|----|----|
| `Preconfigured` | Explicit device paths configuration by using `deviceSelector`. Discovery policy is not applicable. |
| `RuntimeDynamic` | No explicit paths. Discovery policy is Dynamic. The Operator continuously discovers devices. |
| `RuntimeStatic` | No explicit paths. Discovery policy is Static. The Operator discovers devices once at creation time. |

Effective policy status values

The following table shows the behavior matrix:

| Explicit paths | Discovery policy | Effective behavior |
|----|----|----|
| Yes | Any / nil | `Preconfigured`: The Operator honors the specified paths and ignores the discovery policy. |
| No | `Static` | `RuntimeStatic`: The Operator locks the device set immediately after creating the volume group |
| No | `Dynamic` | `RuntimeDynamic`: continuous discovery every 30 seconds |
| No | nil (new volume group) | `RuntimeStatic`: defaults to Static |
| No | nil (existing volume group) | `RuntimeDynamic`: defaults to Dynamic for backward compatibility |

Device discovery behavior by configuration

## Static mode enforcement

In static mode, the system locks the device set after initial discovery. If a volume group lacks explicit paths, newly attached devices are automatically excluded to prevent unintended volume expansions.

This strict filtering behavior does not apply during the very first reconciliation cycle. During this initial pass, the Operator discovers all available devices to successfully create the volume group. Once created, the Operator locks the device set during all subsequent reconciliations.

The discovery policy also controls whether the controller re-queues for periodic device scanning:

| Configuration | Periodic requeue |
|----|----|
| Explicit paths | No: paths define the exact device set; changes trigger reconciliation by using the `LVMVolumeGroup` watch |
| Dynamic without explicit paths | Yes: every 30 seconds |
| Static without explicit paths | No: device set is locked after creation |

Requeue behavior by configuration

## Validation rules for device discovery policy

To ensure your storage cluster deploys successfully and avoids misconfiguration errors, the validating webhook enforces strict rules when you create or update an `LVMCluster` custom resource.

Creation
- If you define one device class without paths, a webhook warning appears. Avoid the default `Static` policy in production. Set `deviceDiscoveryPolicy` explicitly.

- If multiple device classes are defined, every device class must specify device paths. Auto-discovery without paths is not allowed with many device classes. The cluster cannot determine which devices belong to which class.

- If the `deviceDiscoveryPolicy` is empty and paths are missing, a webhook warning appears. Administrators must define the policy explicitly.

Updates
No specific update restrictions apply to the `deviceDiscoveryPolicy` field. You can change it at any time.

The following table shows how the device discovery policy feature interacts with other features:

| Feature | Interaction |
|----|----|
| `forceWipeDevicesAndDestroyAllData` | Works independently of the discovery policy. Devices are wiped before being added to the volume group, regardless of how they were discovered. |
| Node selector | Works independently. The discovery policy applies only to the set of devices found on nodes matching the selector. |

Device discovery policy feature interactions

## LVMCluster custom resource examples

You can configure the `deviceDiscoveryPolicy` field in your `LVMCluster` custom resource (CR) by using these examples to meet your specific storage requirements.

Explicit device paths (recommended for production)
``` yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
spec:
  storage:
    deviceClasses:
    - name: vg1
      deviceSelector:
        paths:
        - /dev/disk/by-id/scsi-SATA_VBOX_HARDDISK_VB12345678-90abcdef
        - /dev/disk/by-id/scsi-SATA_VBOX_HARDDISK_VBabcdef01-23456789
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
```

The discovery policy is not relevant here. Explicit paths always define the device set.

Static discovery without explicit paths
``` yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
spec:
  storage:
    deviceClasses:
    - name: vg1
      deviceDiscoveryPolicy: Static
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
```

The Operator discovers and adds all available devices to the volume group during the initial reconciliation. After the Operator creates the volume group, it adds no new devices.

Dynamic discovery without explicit paths (not recommended for production)
``` yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
spec:
  storage:
    deviceClasses:
    - name: vg1
      deviceDiscoveryPolicy: Dynamic
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
```

The Operator continuously discovers and adds devices to the volume group every 30 seconds. This setting is useful for development and testing. However, it might introduce operational risks in production environments.

## LVM cluster custom resource status reporting

To view a list of excluded devices and the reason for their exclusion, use the `LVMVolumeGroupNodeStatus` custom resource (CR).

If static device discovery excludes a device, the status report displays the error in the following format:

``` text
<device> was not part of <vg_name> at creation (static device discovery enabled)
```

The `VGStatus.DeviceDiscoveryPolicy` parameter reports the effective discovery policy as one of the following values:

- `Preconfigured`

- `RuntimeDynamic`

- `RuntimeStatic`.

# About the LVMCluster custom resource

The `LVMCluster` custom resource (CR) is the primary configuration for LVM Storage deployment, defining how storage is provisioned across your cluster by specifying volume groups, devices, node selection, and thin pool settings to meet your workload requirements.

You can configure the `LVMCluster` CR to perform the following actions:

- Create LVM volume groups that you can use to provision persistent volume claims (PVCs).

- Configure a list of devices that you want to add to the LVM volume groups.

- Configure the requirements to select the nodes on which you want to create an LVM volume group, and the thin pool configuration for the volume group.

- Force wipe the selected devices.

After you have installed LVM Storage, you must create an `LVMCluster` custom resource (CR).

<div class="formalpara">

<div class="title">

Example `LVMCluster` CR YAML file

</div>

``` yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
spec:
  tolerations:
  - effect: NoSchedule
    key: xyz
    operator: Equal
    value: "true"
  storage:
    deviceClasses:
    - name: vg1
      fstype: ext4
      default: true
      nodeSelector:
        nodeSelectorTerms:
        - matchExpressions:
          - key: mykey
            operator: In
            values:
            - ssd
      deviceSelector:
        paths:
        - /dev/disk/by-path/pci-0000:87:00.0-nvme-1
        - /dev/disk/by-path/pci-0000:88:00.0-nvme-1
        optionalPaths:
        - /dev/disk/by-path/pci-0000:89:00.0-nvme-1
        - /dev/disk/by-path/pci-0000:90:00.0-nvme-1
        forceWipeDevicesAndDestroyAllData: true
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
        chunkSize: 128Ki
        chunkSizeCalculationPolicy: Static
        metadataSize: 1Gi
        metadataSizeCalculationPolicy: Host
```

</div>

The following are optional fields: `fstype`, `nodeSelector`, `deviceSelector`, `sizePercent`, `chunkSize`, `chunkSizeCalculationPolicy`, `metadataSize`,`metadataSizeCalculationPolicy`.

## Explanation of fields in the LVMCluster CR

The `LVMCluster` CR fields are described in the following table:

<table>
<caption><code>LVMCluster</code> CR fields</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>spec.storage.deviceClasses</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Contains the configuration to assign the local storage devices to the LVM volume groups.</p>
<p>LVM Storage creates a storage class and volume snapshot class for each device class that you create.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deviceClasses.name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specify a name for the LVM volume group (VG).</p>
<p>You can also configure this field to reuse a volume group that you created in the previous installation. For more information, see "Reusing a volume group from the previous LVM Storage installation".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deviceClasses.fstype</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Set this field to <code>ext4</code> or <code>xfs</code>. By default, this field is set to <code>xfs</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deviceClasses.default</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Set this field to <code>true</code> to indicate that a device class is the default. Otherwise, you can set it to <code>false</code>. You can only configure a single default device class.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deviceClasses.nodeSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Contains the configuration to choose the nodes on which you want to create the LVM volume group. If this field is empty, all nodes without no-schedule taints are considered.</p>
<p>On the control-plane node, LVM Storage detects and uses the additional worker nodes when the new nodes become active in the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeSelector.nodeSelectorTerms</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Configure the requirements that are used to select the node.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deviceClasses.deviceSelector</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Contains the configuration to perform the following actions:</p>
<ul>
<li><p>Specify the paths to the devices that you want to add to the LVM volume group.</p></li>
<li><p>Force wipe the devices that are added to the LVM volume group.</p></li>
</ul>
<p>For more information, see "About adding devices to a volume group".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deviceSelector.paths</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Specify the device paths.</p>
<p>If the device path specified in this field does not exist, or the device is not supported by LVM Storage, the <code>LVMCluster</code> CR moves to the <code>Failed</code> state.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deviceSelector.optionalPaths</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Specify the optional device paths.</p>
<p>If the device path specified in this field does not exist, or the device is not supported by LVM Storage, LVM Storage ignores the device without causing an error.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deviceSelector. forceWipeDevicesAndDestroyAllData</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>LVM Storage uses only those disks that are empty and do not contain file system signatures. To ensure that the disks are empty and do not contain file system signatures, wipe the disks before using them.</p>
<p>To force wipe the selected devices, set this field to <code>true</code>. By default, this field is set to <code>false</code>.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>If this field is set to <code>true</code>, LVM Storage wipes all previous data on the devices. Use this feature with caution.</p>
</div>
<p>Wiping the device can lead to inconsistencies in data integrity if any of the following conditions are met:</p>
<ul>
<li><p>The device is being used as swap space.</p></li>
<li><p>The device is part of a RAID array.</p></li>
<li><p>The device is mounted.</p></li>
</ul>
<p>If any of these conditions are true, do not force wipe the disk. Instead, you must manually wipe the disk.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>deviceClasses.storageClassOptions</p></td>
<td style="text-align: left;"><p>object</p></td>
<td style="text-align: left;"><p>Optional. Allows customization of the StorageClass created for this device class, including reclaim policy, volume binding mode, additional parameters, and labels. For more information, see "StorageClass customization for LVMS device classes".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deviceClasses.thinPoolConfig</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>Contains the configuration to create a thin pool in the LVM volume group.</p>
<p>If you exclude this field, logical volumes are thick provisioned.</p>
<p>Using thick-provisioned storage includes the following limitations:</p>
<ul>
<li><p>No copy-on-write support for volume cloning.</p></li>
<li><p>No support for snapshot class.</p></li>
<li><p>No support for over-provisioning. As a result, the provisioned capacity of <code>PersistentVolumeClaims</code> (PVCs) is immediately reduced from the volume group.</p></li>
<li><p>No support for thin metrics. Thick-provisioned devices only support volume group metrics.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>thinPoolConfig.name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specify a name for the thin pool.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>thinPoolConfig.sizePercent</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specify the percentage of space in the LVM volume group for creating the thin pool.</p>
<p>By default, this field is set to 90. The minimum value that you can set is 10, and the maximum value is 90.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>thinPoolConfig.overprovisionRatio</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specify a factor by which you can provision additional storage based on the available storage in the thin pool.</p>
<p>For example, if this field is set to 10, you can provision up to 10 times the amount of available storage in the thin pool. You can modify this field after the LVM cluster has been created.</p>
<p>To update the parameter, do any of the following tasks:</p>
<ul>
<li><p>To edit the LVM Cluster, run the following command:</p></li>
</ul>
<pre><code>$ oc edit lvmcluster &lt;lvmcluster_name&gt;</code></pre>
<ul>
<li><p>To apply a patch, run the following command:</p></li>
</ul>
<pre><code>$ oc patch lvmcluster &lt;lvmcluster_name&gt; -p &lt;patch_file.yaml&gt;</code></pre>
<p>To disable over-provisioning, set this field to 1.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>thinPoolConfig.chunkSize</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the statically calculated chunk size for the thin pool. This field is only used when the <code>ChunkSizeCalculationPolicy</code> field is set to <code>Static</code>. The value for this field must be configured in the range of 64 KiB to 1 GiB because of the underlying limitations of <code>lvm2</code>.</p>
<p>If you do not configure this field and the <code>ChunkSizeCalculationPolicy</code> field is set to <code>Static</code>, the default chunk size is set to 128 KiB.</p>
<p>For more information, see "Overview of chunk size".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>thinPoolConfig.chunkSizeCalculationPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the policy to calculate the chunk size for the underlying volume group. You can set this field to either <code>Static</code> or <code>Host</code>. By default, this field is set to <code>Static</code>.</p>
<p>If this field is set to <code>Static</code>, the chunk size is set to the value of the <code>chunkSize</code> field. If the <code>chunkSize</code> field is not configured, chunk size is set to 128 KiB.</p>
<p>If this field is set to <code>Host</code>, the chunk size is calculated based on the configuration in the <code>lvm.conf</code> file.</p>
<p>For more information, see "Limitations to configure the size of the devices used in LVM Storage".</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>thinPoolConfig.metadataSize</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the metadata size for the thin pool. You can configure this field only when the <code>MetadataSizeCalculationPolicy</code> field is set to <code>Static</code>.</p>
<p>If this field is not configured, and the <code>MetadataSizeCalculationPolicy</code> field is set to <code>Static</code>, the default metadata size is set to 1 GiB.</p>
<p>The value for this field must be configured in the range of 2 MiB to 16 GiB due to the underlying limitations of <code>lvm2</code>. You can only increase the value of this field during updates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>thinPoolConfig.metadataSizeCalculationPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the policy to calculate the metadata size for the underlying volume group. You can set this field to either <code>Static</code> or <code>Host</code>. By default, this field is set to <code>Host</code>.</p>
<p>If this field is set to <code>Static</code>, the metadata size is calculated based on the value of the <code>thinPoolConfig.metadataSize</code> field.</p>
<p>If this field is set to <code>Host</code>, the metadata size is calculated based on the <code>lvm2</code> settings.</p></td>
</tr>
</tbody>
</table>

<div>

<div class="title">

Additional resources

</div>

- [Overview of chunk size](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_and_managing_logical_volumes/index#overview-of-chunk-size_creating-and-managing-thin-provisioned-volumes)

- [Limitations to configure the size of the devices used in LVM Storage](persistent-storage-using-lvms.md#limitations-to-configure-size-of-devices_logical-volume-manager-storage)

- [Reusing a volume group from the previous LVM Storage installation](persistent-storage-using-lvms.md#lvms-reusing-vg-from-prev-installation_logical-volume-manager-storage)

- [About adding devices to a volume group](persistent-storage-using-lvms.md#about-adding-devices-to-a-vg_logical-volume-manager-storage)

- [Adding worker nodes to single-node OpenShift clusters](../../nodes/nodes/nodes-sno-worker-nodes.md#nodes-sno-worker-nodes)

</div>

## Limitations to configure the size of the devices used in LVM Storage

To ensure your devices are compatible with storage operations, review the size configuration limitations in LVM Storage. Adhering to these constraints prevents provisioning failures by ensuring selected devices meet the required capacity specifications.

When provisioning storage by using LVM Storage, the following factors limit device size:

- The total storage size that you can provision is limited by the size of the underlying Logical Volume Manager (LVM) thin pool and the over-provisioning factor.

- The size of the logical volume depends on the size of the Physical Extent (PE) and the Logical Extent (LE).

  - You can define the size of PE and LE during the physical and logical device creation.

  - The default PE and LE size is 4 MiB.

  - If the size of the PE is increased, the maximum size of the LVM is determined by the kernel limits and your disk space.

The following tables describe the chunk size and volume size limits for static and host configurations:

| Parameter           | Value   |
|---------------------|---------|
| Chunk size          | 128 KiB |
| Maximum volume size | 32 TiB  |

Tested configuration

| Parameter | Minimum value | Maximum value |
|----|----|----|
| Chunk size | 64 KiB | 1 GiB |
| Volume size | Minimum size of the underlying Red Hat Enterprise Linux CoreOS (RHCOS) system. | Maximum size of the underlying RHCOS system. |

Theoretical size limits for static configuration

| Parameter | Value |
|----|----|
| Chunk size | This value is based on the configuration in the `lvm.conf` file. By default, the configuration sets the value to `128` KiB. |
| Maximum volume size | Equal to the maximum volume size of the underlying RHCOS system. |
| Minimum volume size | Equal to the minimum volume size of the underlying RHCOS system. |

Theoretical size limits for a host configuration

## About adding devices to a volume group

To add devices to the Logical Volume Manager (LVM) volume group, use the `deviceSelector` field in the `LVMCluster` Custom Resource (CR) to specify the paths to the devices.

You can specify the device paths in the `deviceSelector.paths` field, the `deviceSelector.optionalPaths` field, or both. If you do not specify the device paths in both the `deviceSelector.paths` field and the `deviceSelector.optionalPaths` field, LVM Storage adds the supported unused devices to the volume group (VG).

> [!IMPORTANT]
> It is recommended to avoid referencing disks using symbolic naming, such as `/dev/sdX`, as these names may change across reboots within RHCOS. Instead, you must use stable naming schemes, such as `/dev/disk/by-path/` or `/dev/disk/by-id/`, to ensure consistent disk identification.
>
> With this change, you might need to adjust existing automation workflows in the cases where monitoring collects information about the install device for each node.
>
> For more information, see the "RHEL documentation".

You can add the path to the Redundant Array of Independent Disks (RAID) arrays in the `deviceSelector` field to integrate the RAID arrays with LVM Storage. You can create the RAID array by using the `mdadm` utility. LVM Storage does not support creating a software RAID.

> [!NOTE]
> You can create a RAID array only during an OpenShift Container Platform installation. For information on creating a RAID array, see:
>
> - "Configuring a RAID-enabled data volume"
>
> - "Creating a software RAID on an installed system"
>
> - "Replacing a failed disk in RAID"
>
> - "Repairing RAID disks"

You can also add encrypted devices to the volume group. You can enable disk encryption on the cluster nodes during an OpenShift Container Platform installation. After encrypting a device, you can specify the path to the LUKS encrypted device in the `deviceSelector` field. For information on disk encryption, see "About disk encryption" and "Configuring disk encryption and mirroring".

The devices that you want to add to the VG must be supported by LVM Storage. For information about unsupported devices, see "Devices not supported by LVM Storage".

LVM Storage adds the devices to the VG only if the following conditions are met:

- The device path exists.

- The device is supported by LVM Storage.

> [!IMPORTANT]
> After a device is added to the VG, you cannot remove the device.

LVM Storage supports dynamic device discovery. If you do not add the `deviceSelector` field in the `LVMCluster` CR, LVM Storage automatically adds the new devices to the VG when the devices are available.

> [!WARNING]
> It is not recommended to add the devices to the VG through dynamic device discovery due to the following reasons:
>
> - When you add a new device that you do not intend to add to the VG, LVM Storage automatically adds this device to the VG through dynamic device discovery.
>
> - If LVM Storage adds a device to the VG through dynamic device discovery, LVM Storage does not restrict you from removing the device from the node. Removing or updating the devices that are already added to the VG can disrupt the VG. This can also lead to data loss and necessitate manual node remediation.

<div>

<div class="title">

Additional resources

</div>

- [RHEL documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_file_systems/assembly_overview-of-persistent-naming-attributes_managing-file-systems)

- [Creating a software RAID on an installed system](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_storage_devices/managing-raid_managing-storage-devices#creating-a-software-raid-on-an-installed-system_managing-raid)

- [Replacing a failed disk in RAID](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_storage_devices/managing-raid_managing-storage-devices#replacing-a-failed-disk-in-raid_managing-raid)

- [Repairing RAID disks](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_storage_devices/managing-raid_managing-storage-devices#repairing-raid-disks_managing-raid)

- [Configuring a RAID-enabled data volume](../../installing/install_config/installing-customizing.md#installation-special-config-raid_installing-customizing)

- [About disk encryption](../../installing/install_config/installing-customizing.md#installation-special-config-storage_installing-customizing)

- [Configuring disk encryption and mirroring](../../installing/install_config/installing-customizing.md#installation-special-config-storage-procedure_installing-customizing)

- [Devices not supported by LVM Storage](persistent-storage-using-lvms.md#lvms-unsupported-devices_logical-volume-manager-storage)

</div>

## About removing devices and device classes from a volume group

You can remove devices and device classes from a Logical Volume Manager (LVM) volume group to decommission storage hardware or reorganize your storage configuration by updating the `deviceSelector` field in the `LVMCluster` CR.

### Removing the device paths in the deviceSelector.paths field

You can remove the device paths in the `deviceSelector.paths` field.

> [!IMPORTANT]
> Ensure that the following criteria are met before removing device paths:
>
> - The device that you want to remove is empty. You can use the `pvdisplay` command to see attributes of physical volumes (PVs) used in LVM.
>
> - At least one additional device is specified in the `deviceSelector.paths` field.

### Removing the deviceClass from the LVMCluster

You can also remove the `deviceClass` object from the `LVMCluster` resource. For device class deletion, there is no need to delete `deviceSelector.paths` object.

> [!IMPORTANT]
> Ensure that the following criteria are met before removing a device class:
>
> - The `deviceClasses.default` field is set to `false`.
>
> - The disks specified in the `deviceSelector.paths` field are empty.
>
> - At least one additional device class is specified in the `storage` field.

## Devices not supported by LVM Storage

When adding device paths to the `LVMCluster` custom resource (CR), ensure devices are supported by LVM Storage. LVM Storage excludes unsupported devices to avoid complexity in managing logical volumes.

If you do not specify any device path in the `deviceSelector` field, LVM Storage adds only the unused devices that it supports.

> [!NOTE]
> To get information about the devices, run the following command:
>
> ``` terminal
> $ lsblk --paths --json -o \
> NAME,ROTA,TYPE,SIZE,MODEL,VENDOR,RO,STATE,KNAME,SERIAL,PARTLABEL,FSTYPE
> ```

LVM Storage does not support the following devices:

Read-only devices
Devices with the `ro` parameter set to `true`.

Suspended devices
Devices with the `state` parameter set to `suspended`.

ROM devices
Devices with the `type` parameter set to `rom`.

LVM partition devices
Devices with the `type` parameter set to `lvm`.

Devices with invalid partition labels
Devices with the `partlabel` parameter set to `bios`, `boot`, or `reserved`.

Devices with an invalid filesystem
Devices with the `fstype` parameter set to any value other than `null` or `LVM2_member`.

> [!IMPORTANT]
> LVM Storage supports devices with `fstype` parameter set to `LVM2_member` only if the devices do not contain children devices.

Devices that are part of another volume group
To get the information about the volume groups of the device, run the following command:

``` terminal
$ pvs <device-name>
```

Where `<device-name>` is the device name.

Devices with bind mounts
To get the mount points of a device, run the following command:

``` terminal
$ cat /proc/1/mountinfo | grep <device-name>
```

Where `<device-name>` is the device name.

Devices that contain children devices

> [!NOTE]
> It is recommended to wipe the device before using it in LVM Storage to prevent unexpected behavior.

# Ways to create an LVMCluster custom resource

You can create an `LVMCluster` custom resource (CR) to configure LVM Storage deployment and provision storage for your workloads by using the OpenShift CLI (`oc`), OpenShift Container Platform web console, or Red Hat Advanced Cluster Management (RHACM).

You must install LVM Storage by using RHACM if you want to create an `LVMCluster` CR by using RHACM.

> [!IMPORTANT]
> You must create the `LVMCluster` CR in the same namespace where you installed the LVM Storage Operator, which is `openshift-storage` by default.

After creating the `LVMCluster` CR, LVM Storage creates the following system-managed CRs:

- A `storageClass` and `volumeSnapshotClass` for each device class.

  > [!NOTE]
  > LVM Storage configures the name of the storage class and volume snapshot class in the format `lvms-<device_class_name>`, where, `<device_class_name>` is the value of the `deviceClasses.name` field in the `LVMCluster` CR. For example, if the `deviceClasses.name` field is set to vg1, the name of the storage class and volume snapshot class is `lvms-vg1`.

- `LVMVolumeGroup`: This CR is a specific type of persistent volume (PV) that is backed by an LVM volume group. It tracks the individual volume groups across multiple nodes.

- `LVMVolumeGroupNodeStatus`: This CR tracks the status of the volume groups on a node.

## Reusing a volume group from the previous LVM Storage installation

You can reuse an existing volume group (VG) from a previous LVM Storage installation to preserve your existing storage configuration and avoid recreating VGs when reinstalling or upgrading LVM Storage.

You can only reuse a VG, but not the logical volume associated with the VG.

> [!IMPORTANT]
> You can perform this procedure only while creating an `LVMCluster` custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- The VG that you want to reuse must not be corrupted.

- The VG that you want to reuse must have the `lvms` tag. For more information on adding tags to LVM objects, see "Grouping LVM objects with tags".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Open the `LVMCluster` CR YAML file.

2.  Configure the `LVMCluster` CR parameters as described in the following example:

    <div class="formalpara">

    <div class="title">

    Example `LVMCluster` CR YAML file

    </div>

    ``` yaml
    apiVersion: lvm.topolvm.io/v1alpha1
    kind: LVMCluster
    metadata:
      name: my-lvmcluster
    spec:
    # ...
      storage:
        deviceClasses:
        - name: vg1
          fstype: ext4
          default: true
          deviceSelector:
    # ...
            forceWipeDevicesAndDestroyAllData: false
          thinPoolConfig:
    # ...
          nodeSelector:
    # ...
    ```

    </div>

    - `spec.storage.deviceClasses.name`: Specifies the name of a VG from the previous LVM Storage installation.

    - `spec.storage.deviceClasses.fstype`: Set this field to `ext4` or `xfs`. By default, this field is set to `xfs`.

    - `spec.storage.deviceClasses.name.deviceSelector`: You can add new devices to the VG that you want to reuse by specifying the new device paths in the `deviceSelector` field. If you do not want to add new devices to the VG, ensure that the `deviceSelector` configuration in the current LVM Storage installation is same as that of the previous LVM Storage installation.

    - `spec…​forceWipeDevicesAndDestroyAllData`: If this field is set to `true`, LVM Storage wipes all the data on the devices that are added to the VG.

    - `spec…​.thinPoolConfig`: To retain the `thinPoolConfig` configuration of the VG that you want to reuse, ensure that the `thinPoolConfig` configuration in the current LVM Storage installation is same as that of the previous LVM Storage installation. Otherwise, you can configure the `thinPoolConfig` field as required.

    - `spec…​nodeSelector`: Configure the requirements to choose the nodes on which you want to create the LVM volume group. If this field is empty, all nodes without no-schedule taints are considered.

3.  Save the `LVMCluster` CR YAML file.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

To view the devices that are part a volume group, run the following command:

</div>

``` terminal
$ pvs -S vgname=<vg_name>
```

Replace `<vg_name>` with the name of the volume group.

<div>

<div class="title">

Additional resources

</div>

- [Grouping LVM objects with tags](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/grouping-lvm-objects-with-tags_configuring-and-managing-logical-volumes#doc-wrapper)

</div>

## Creating an LVMCluster CR by using the CLI

You can create an `LVMCluster` custom resource (CR) on a worker node by using the OpenShift CLI (`oc`) to configure storage deployment and provision local storage for your workloads.

> [!IMPORTANT]
> You can only create a single instance of the `LVMCluster` custom resource (CR) on an OpenShift Container Platform cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to OpenShift Container Platform as a user with `cluster-admin` privileges.

- You have installed LVM Storage.

- You have installed a worker node in the cluster.

- You read "About the LVMCluster custom resource".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an `LVMCluster` custom resource (CR) YAML file:

    <div class="formalpara">

    <div class="title">

    Example `LVMCluster` CR YAML file

    </div>

    ``` yaml
    apiVersion: lvm.topolvm.io/v1alpha1
    kind: LVMCluster
    metadata:
      name: my-lvmcluster
      namespace: openshift-lvm-storage
    spec:
    # ...
      storage:
        deviceClasses:
    # ...
          nodeSelector:
    # ...
          deviceSelector:
    # ...
          thinPoolConfig:
    # ...
    ```

    </div>

    - `spec.storage.deviceClasses`: Specifies the configuration to assign the local storage devices to the LVM volume groups.

    - `spec…​nodeSelector`: Specifies the configuration to choose the nodes on which you want to create the LVM volume group. If this field is empty, all nodes without no-schedule taints are considered.

    - `spec…​deviceSelector`: Specifies the configuration to specify the paths to the devices that you want to add to the LVM volume group, and force wipe the devices that are added to the LVM volume group.

    - `spec…​thinPoolConfig`: Specifies the configuration to create a thin pool in the LVM volume group. If you exclude this field, logical volumes are thick provisioned.

2.  Create the `LVMCluster` CR by running the following command:

    ``` terminal
    $ oc create -f <file_name>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    lvmcluster/lvmcluster created
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Check that the `LVMCluster` CR is in the `Ready` state by running the following command:

    ``` terminal
    $ oc get lvmclusters.lvm.topolvm.io -o jsonpath='{.items[*].status}' -n <namespace>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` json
    {"deviceClassStatuses":
    [
      {
        "name": "vg1",
        "nodeStatus": [
            {
                "devices": [
                    "/dev/nvme0n1",
                    "/dev/nvme1n1",
                    "/dev/nvme2n1"
                ],
                "node": "kube-node",
                "status": "Ready"
            }
        ]
      }
    ]
    "state":"Ready"}
    ```

    </div>

    - `deviceClassStatuses`: Specifies the status of the device class.

    - `nodeStatus`: Specifies the status of the LVM volume group on each node.

    - `devices`: Specifies the list of devices used to create the LVM volume group.

    - `node`: Specifies the node on which the device class is created.

    - `status`: Specifies the status of the LVM volume group on the node.

    - `state`: Specifies the status of the `LVMCluster` CR.

      > [!NOTE]
      > If the `LVMCluster` CR is in the `Failed` state, you can view the reason for failure in the `status` field.
      >
      > \+ Example of `status` field with the reason for failure:
      >
      > ``` yaml
      > status:
      >   deviceClassStatuses:
      >     - name: vg1
      >       nodeStatus:
      >         - node: my-node-1.example.com
      >           reason: no available devices found for volume group
      >           status: Failed
      >   state: Failed
      > ```

2.  To view the storage classes created by LVM Storage for each device class, run the following command:

    ``` terminal
    $ oc get storageclass
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME          PROVISIONER          RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
    lvms-vg1      topolvm.io           Delete          WaitForFirstConsumer   true                   31m
    ```

    </div>

3.  To view the volume snapshot classes created by LVM Storage for each device class, run the following command:

    ``` terminal
    $ oc get volumesnapshotclass
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME          DRIVER               DELETIONPOLICY   AGE
    lvms-vg1      topolvm.io           Delete           24h
    ```

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the `LVMCluster` custom resource](persistent-storage-using-lvms.md#about-lvmcluster_logical-volume-manager-storage)

</div>

## Creating an LVMCluster CR by using the web console

You can create an `LVMCluster` custom resource (CR) on a worker node by using the OpenShift Container Platform web console to configure storage deployment and provision local storage for your workloads.

> [!IMPORTANT]
> You can only create a single instance of the `LVMCluster` custom resource (CR) on an OpenShift Container Platform cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform cluster with `cluster-admin` privileges.

- You have installed LVM Storage.

- You have installed a worker node in the cluster.

- You read the "About the LVMCluster custom resource" section.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Click **Ecosystem** → **Installed Operators**.

3.  In the `openshift-lvm-storage` namespace, click **LVM Storage**.

4.  Click **Create LVMCluster** and select either **Form view** or **YAML view**.

5.  Configure the required `LVMCluster` CR parameters.

6.  Click **Create**.

7.  Optional: If you want to edit the `LVMCLuster` CR, perform the following actions:

    1.  Click the **LVMCluster** tab.

    2.  From the **Actions** menu, select **Edit LVMCluster**.

    3.  Click **YAML** and edit the required `LVMCLuster` CR parameters.

    4.  Click **Save**.

</div>

<div>

<div class="title">

Verification

</div>

1.  On the **LVMCLuster** page, check that the `LVMCluster` CR is in the `Ready` state.

2.  Optional: To view the available storage classes created by LVM Storage for each device class, click **Storage** → **StorageClasses**.

3.  Optional: To view the available volume snapshot classes created by LVM Storage for each device class, click **Storage** → **VolumeSnapshotClasses**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the `LVMCluster` custom resource](persistent-storage-using-lvms.md#about-lvmcluster_logical-volume-manager-storage)

</div>

## Creating an LVMCluster CR by using RHACM

After installing Logical Volume Manager (LVM) Storage by using RHACM, create an `LVMCluster` custom resource (CR) to configure storage deployment, specify devices and volume groups, and provision storage for your workloads.

<div>

<div class="title">

Prerequisites

</div>

- You have installed LVM Storage by using RHACM.

- You have access to the RHACM cluster using an account with `cluster-admin` permissions.

- You read the "About the LVMCluster custom resource" section.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the RHACM CLI using your OpenShift Container Platform credentials.

2.  Create a `ConfigurationPolicy` CR YAML file with the configuration to create an `LVMCluster` CR:

    <div class="formalpara">

    <div class="title">

    Example `ConfigurationPolicy` CR YAML file to create an `LVMCluster` CR

    </div>

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: ConfigurationPolicy
    metadata:
      name: lvms
      namespace: openshift-lvm-storage
    spec:
      object-templates:
      - complianceType: musthave
        objectDefinition:
          apiVersion: lvm.topolvm.io/v1alpha1
          kind: LVMCluster
          metadata:
            name: my-lvmcluster
            namespace: openshift-lvm-storage
          spec:
            storage:
              deviceClasses:
    # ...
                deviceSelector:
    # ...
                thinPoolConfig:
    # ...
                nodeSelector:
    # ...
      remediationAction: enforce
      severity: low
    ```

    </div>

    - `spec.object-templates.objectDefinition.spec.storage.deviceClasses`: Specifies the configuration to assign the local storage devices to the LVM volume groups.

    - `spec…​deviceSelector`: Contains the configuration to specify the paths to the devices that you want to add to the LVM volume group, and force wipe the devices that are added to the LVM volume group.

    - `spec…​thinPoolConfig`: Contains the configuration to create a thin pool in the LVM volume group. If you exclude this field, logical volumes are thick provisioned.

    - `spec…​nodeSelector`: Contains the configuration to choose the nodes on which you want to create the LVM volume groups. If this field is empty, then all nodes without no-schedule taints are considered.

3.  Create the `ConfigurationPolicy` CR by running the following command:

    ``` terminal
    $ oc create -f <file_name> -n <cluster_namespace>
    ```

    `<cluster_namespace>` is the namespace of the OpenShift Container Platform cluster on which LVM Storage is installed.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the `LVMCluster` custom resource](persistent-storage-using-lvms.md#about-lvmcluster_logical-volume-manager-storage)

</div>

# Ways to delete an LVMCluster custom resource

Delete an `LVMCluster` custom resource (CR) when decommissioning LVM Storage or reconfiguring storage by using the OpenShift CLI (`oc`), OpenShift Container Platform web console, or Red Hat Advanced Cluster Management (RHACM).

You must have installed LVM Storage by using RHACM to delete an `LVMCluster` CR by using RHACM.

After deleting the `LVMCluster` CR, LVM Storage deletes the following CRs:

- `storageClass`

- `volumeSnapshotClass`

- `LVMVolumeGroup`

- `LVMVolumeGroupNodeStatus`

## Deleting an LVMCluster CR by using the CLI

You can delete an `LVMCluster` custom resource (CR) when decommissioning LVM Storage or reconfiguring storage by using the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.

- You have deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by LVM Storage. You have also deleted the applications that are using these resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Delete the `LVMCluster` CR by running the following command:

    ``` terminal
    $ oc delete lvmcluster <lvm_cluster_name> -n <namespace>
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the `LVMCluster` CR has been deleted, run the following command:

  ``` terminal
  $ oc get lvmcluster -n <namespace>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  No resources found in openshift-lvm-storage namespace.
  ```

  </div>

</div>

## Deleting an LVMCluster CR by using the web console

You can delete an `LVMCluster` custom resource (CR) when decommissioning LVM Storage or reconfiguring storage by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.

- You have deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by LVM Storage. You have also deleted the applications that are using these resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Click **Ecosystem** → **Installed Operators** to view all the installed Operators.

3.  Click **LVM Storage** in the `openshift-lvm-storage` namespace.

4.  Click the **LVMCluster** tab.

5.  From the **Actions**, select **Delete LVMCluster**.

6.  Click **Delete**.

</div>

<div>

<div class="title">

Verification

</div>

- On the `LVMCLuster` page, check that the `LVMCluster` CR has been deleted.

</div>

## Deleting an LVMCluster CR by using RHACM

You can delete an `LVMCluster` custom resource (CR) when decommissioning LVM Storage or reconfiguring storage by using Red Hat Advanced Cluster Management (RHACM).

You can only delete an `LVMCluster` CR by using RHACM If you installed LVM Storage by using Red Hat Advanced Cluster Management (RHACM).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the RHACM cluster as a user with `cluster-admin` permissions.

- You have deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by LVM Storage. You have also deleted the applications that are using these resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the RHACM CLI using your OpenShift Container Platform credentials.

2.  Delete the `ConfigurationPolicy` CR YAML file that was created for the `LVMCluster` CR:

    ``` terminal
    $ oc delete -f <file_name> -n <cluster_namespace>
    ```

    `<cluster_namespace>` is the namespace of the OpenShift Container Platform cluster on which LVM Storage is installed.

3.  Create a `Policy` CR YAML file to delete the `LVMCluster` CR:

    <div class="formalpara">

    <div class="title">

    Example `Policy` CR to delete the `LVMCluster` CR

    </div>

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: policy-lvmcluster-delete
      annotations:
        policy.open-cluster-management.io/standards: NIST SP 800-53
        policy.open-cluster-management.io/categories: CM Configuration Management
        policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
    spec:
      remediationAction: enforce
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: policy-lvmcluster-removal
            spec:
              remediationAction: enforce
              severity: low
              object-templates:
                - complianceType: mustnothave
                  objectDefinition:
                    kind: LVMCluster
                    apiVersion: lvm.topolvm.io/v1alpha1
                    metadata:
                      name: my-lvmcluster
                      namespace: openshift-lvm-storage
    ---
    apiVersion: policy.open-cluster-management.io/v1
    kind: PlacementBinding
    metadata:
      name: binding-policy-lvmcluster-delete
    placementRef:
      apiGroup: apps.open-cluster-management.io
      kind: PlacementRule
      name: placement-policy-lvmcluster-delete
    subjects:
      - apiGroup: policy.open-cluster-management.io
        kind: Policy
        name: policy-lvmcluster-delete
    ---
    apiVersion: apps.open-cluster-management.io/v1
    kind: PlacementRule
    metadata:
      name: placement-policy-lvmcluster-delete
    spec:
      clusterConditions:
        - status: "True"
          type: ManagedClusterConditionAvailable
      clusterSelector:
        matchExpressions:
          - key: mykey
            operator: In
            values:
              - myvalue
    ```

    </div>

    - `spec.policy-templates.spec.remediationAction`: This field is overridden by the preceding parameter value for `spec.remediationAction`.

    - `spec.policy-templates.objectDefinition.spec.objectDefinition.metadata.namespace`: This `namespace` field must have the `openshift-lvm-storage` value.

    - `spec.clusterSelector`: Configures the requirements to select the clusters. LVM Storage is uninstalled on the clusters that match the selection criteria.

4.  Create the `Policy` CR by running the following command:

    ``` terminal
    $ oc create -f <file_name> -n <namespace>
    ```

5.  Create a `Policy` CR YAML file to check if the `LVMCluster` CR has been deleted:

    <div class="formalpara">

    <div class="title">

    Example `Policy` CR to check if the `LVMCluster` CR has been deleted

    </div>

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: policy-lvmcluster-inform
      annotations:
        policy.open-cluster-management.io/standards: NIST SP 800-53
        policy.open-cluster-management.io/categories: CM Configuration Management
        policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
    spec:
      remediationAction: inform
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: policy-lvmcluster-removal-inform
            spec:
              remediationAction: inform
              severity: low
              object-templates:
                - complianceType: mustnothave
                  objectDefinition:
                    kind: LVMCluster
                    apiVersion: lvm.topolvm.io/v1alpha1
                    metadata:
                      name: my-lvmcluster
                      namespace: openshift-lvm-storage
    ---
    apiVersion: policy.open-cluster-management.io/v1
    kind: PlacementBinding
    metadata:
      name: binding-policy-lvmcluster-check
    placementRef:
      apiGroup: apps.open-cluster-management.io
      kind: PlacementRule
      name: placement-policy-lvmcluster-check
    subjects:
      - apiGroup: policy.open-cluster-management.io
        kind: Policy
        name: policy-lvmcluster-inform
    ---
    apiVersion: apps.open-cluster-management.io/v1
    kind: PlacementRule
    metadata:
      name: placement-policy-lvmcluster-check
    spec:
      clusterConditions:
        - status: "True"
          type: ManagedClusterConditionAvailable
      clusterSelector:
        matchExpressions:
          - key: mykey
            operator: In
            values:
              - myvalue
    ```

    </div>

    - `spec.policy-templates.objectDefinition.spec.remediationAction`: This field is overridden by the preceding parameter value for `spec.remediationAction`.

    - `spec.policy-templates.objectDefinition.spec.object-templates.objectDefinition.metadata.namespace`: This `namespace` field must have the `openshift-lvm-storage` value.

6.  Create the `Policy` CR by running the following command:

    ``` terminal
    $ oc create -f <file_name> -n <namespace>
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Check the status of the `Policy` CRs by running the following command:

  ``` terminal
  $ oc get policy -n <namespace>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                       REMEDIATION ACTION   COMPLIANCE STATE   AGE
  policy-lvmcluster-delete   enforce              Compliant          15m
  policy-lvmcluster-inform   inform               Compliant          15m
  ```

  </div>

  > [!IMPORTANT]
  > The `Policy` CRs must be in `Compliant` state.

</div>

## Deleting an LVMCluster

When you delete an `LVMCluster` custom resource (CR), the Operator enforces deletion gates to prevent data loss. The gates that apply depend on the reclaim policy that is configured for the storage class.

<div>

<div class="title">

Prerequisites

</div>

- You have administrative access to the cluster.

- You have identified the reclaim policy in use: `Delete` or `Retain`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Delete all Persistent Volume Claims (PVCs) that reference LVM `StorageClass` resources.

    If PVCs that reference LVM StorageClasses still exist, the Operator blocks `LVMCluster` deletion and generates a `DeletionPending` event:

    ``` terminal
    found PVCs provisioned by LVMS, waiting 10s for their deletion
    ```

2.  Back up any data before deleting PVCs.

    1.  List the PVCs that use the LVM StorageClass by running the following command:

        ``` terminal
        $ oc get pvc -A -o custom-columns='NAMESPACE:.metadata.namespace,NAME:.metadata.name,SC:.spec.storageClassName' | grep lvms-vg1
        ```

    2.  Delete the PVCs by running the following command:

        ``` terminal
        $ oc delete pvc <pvc_name> -n <namespace>
        ```

        With the `Delete` reclaim policy, deleting the PVCs automatically removes the persistent volumes (PVs) and on-disk logical volumes. After all PVCs are removed, `LVMCluster` deletion completes automatically. No further action is required.

3.  If you use the `Retain` reclaim policy, delete the retained PVs.

    After you delete PVCs, if the reclaim policy is `Retain`, the Operator blocks `LVMCluster` deletion and generates a `DeletionPending` event:

    ``` terminal
    found PVs with Retain policy from LVMS, waiting 10s for manual cleanup
    ```

    1.  List the retained PVs by running the following command:

        ``` terminal
        $ oc get pv -o custom-columns='NAME:.metadata.name,SC:.spec.storageClassName' | grep lvms-vg1
        ```

    2.  Delete the PVs by running the following command:

        ``` terminal
        $ oc delete pv <pv_name>
        ```

4.  If you are using the `Retain` reclaim policy, delete the TopoLVM `LogicalVolume` custom resources.

    After you delete PV objects from Kubernetes, the underlying logical volumes remain on disk because the `Retain` policy preserved them. The VG Manager detects this and generates a `ManualCleanupRequired` event:

    ``` terminal
    Warning  ManualCleanupRequired  volume group vg1 has retained logical volumes [pvc-abc123]; manual cleanup required before deletion can proceed
    ```

5.  Deleting the `LogicalVolume` custom resources triggers on-disk logical volume cleanup.

    1.  List the `LogicalVolume` custom resources by running the following command:

        ``` terminal
        $ oc get logicalvolumes
        ```

    2.  Delete the `LogicalVolume` custom resources for your device class by running the following command:

        ``` terminal
        $ oc delete logicalvolume <lv_name>
        ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `LVMCluster` deletion completed by confirming the resource no longer exists by running the following command:

  ``` terminal
  $ oc get lvmcluster -A
  ```

</div>

# Provisioning storage by using LVM Storage

After you have created the LVM volume groups by using the `LVMCluster` custom resource (CR), you can provision storage for your workloads by creating persistent volume claims (PVCs) that dynamically allocate local storage from the volume groups.

The following are the minimum storage sizes that you can request for each file system type:

- `block`: 8 MiB

- `xfs`: 300 MiB

- `ext4`: 32 MiB

To create a PVC, you must create a `PersistentVolumeClaim` object.

<div>

<div class="title">

Prerequisites

</div>

- You have created an `LVMCluster` CR.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Create a `PersistentVolumeClaim` object:

    <div class="formalpara">

    <div class="title">

    Example `PersistentVolumeClaim` object

    </div>

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: lvm-block-1
      namespace: default
    spec:
      accessModes:
        - ReadWriteOnce
      volumeMode: Filesystem
      resources:
        requests:
          storage: 10Gi
        limits:
          storage: 20Gi
      storageClassName: lvms-vg1
    ```

    </div>

    - `metadata.name`: Specifies a name for the PVC.

    - `spec.volumeMode`: To create a file PVC, set this field to `Filesystem`. To create a block PVC, set this field to `Block`.

    - `spec.resources.requests.storage`: Specifies the storage size. If the value is less than the minimum storage size, the requested storage size is rounded to the minimum storage size. The total storage size you can provision is limited by the size of the Logical Volume Manager (LVM) thin pool and the over-provisioning factor.

    - `spec.resources.limits.storage`: (optional) Specifies the storage limit. Set this field to a value that is greater than or equal to the minimum storage size. Otherwise, PVC creation fails with an error.

    - `spec.storageClassName`: The value of the `storageClassName` field must be in the format `lvms-<device_class_name>` where `<device_class_name>` is the value of the `deviceClasses.name` field in the `LVMCluster` CR.

      For example, if the `deviceClasses.name` field is set to `vg1`, you must set the `storageClassName` field to `lvms-vg1`.

      > [!NOTE]
      > The `volumeBindingMode` field of the storage class is set to `WaitForFirstConsumer`.

3.  Create the PVC by running the following command:

    ``` terminal
    # oc create -f <file_name> -n <application_namespace>
    ```

    > [!NOTE]
    > The created PVCs remain in `Pending` state until you deploy the pods that use them.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the PVC is created, run the following command:

  ``` terminal
  $ oc get pvc -n <namespace>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
  lvm-block-1   Bound    pvc-e90169a8-fd71-4eea-93b8-817155f60e47   1Gi        RWO            lvms-vg1       5s
  ```

  </div>

</div>

# StorageClass customization for LVMS device classes

You can customize the StorageClass for each device class by specifying reclaim policy, volume binding mode, parameters, and labels in the LVMCluster custom resource (CR).

Before, Logical Volume Manager Storage (LVMS) automatically created a StorageClass for each device class without allowing modification. If you attempted to manually edit a generated StorageClass, the Operator overwrote your changes during the next reconciliation loop.

The `storageClassOptions` field lets you control four properties of the generated StorageClass:

- `reclaimPolicy`

- `volumeBindingMode`

- `additionalParameters`

- `additionalLabels`

If you omit `storageClassOptions`, LVMS creates the StorageClass with the same defaults as in previous versions. Existing `LVMCluster` configurations are fully compatible with earlier versions.

> [!NOTE]
> No user action is required after upgrading. The `storageClassOptions` field is optional, and default values match the behavior before this feature was introduced.

## StorageClass options for LVMS device classes

You can configure custom StorageClass behaviors for each device class, including reclaim policy, volume binding mode, and custom parameters and labels, by defining the storageClassOptions field in the LVMCluster custom resource.

If you set an empty configuration (storageClassOptions: {}) or omit the field entirely, the Operator uses the following default settings:

<table>
<caption>StorageClass Options Reference</caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 37%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Immutable</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>reclaimPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>Controls what happens to the PersistentVolume (PV) and its underlying logical volume when the PersistentVolumeClaim (PVC) is deleted.</p>
<p>Allowed values: <code>Delete</code> (default), <code>Retain</code></p>
<p>When set to <code>Retain</code>, deleting a PVC does not delete the PV or the underlying logical volume on disk. Data is preserved, useful for data protection scenarios where accidental PVC deletion must not cause data loss. Manual cleanup is required before you can delete the <code>LVMCluster</code>.</p>
<p>When set to <code>Delete</code>, both the PV and the on-disk logical volume are removed when the PVC is deleted.</p></td>
<td style="text-align: left;"><div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">storageClassOptions</span><span class="kw">:</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">reclaimPolicy</span><span class="kw">:</span><span class="at"> Retain</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeBindingMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>Controls when volume binding and dynamic provisioning occur.</p>
<p>Allowed values: <code>WaitForFirstConsumer</code> (default), <code>Immediate</code></p>
<p><code>WaitForFirstConsumer</code> delays PV provisioning until a pod that uses the PVC is scheduled, enabling topology-aware scheduling where LVMS creates the PV on the node where the pod will run.</p>
<p><code>Immediate</code> provisions and binds the PV as soon as the PVC is created, without waiting for a consumer pod. On multi-node clusters, PVs might be provisioned on nodes where the consuming pod cannot run. Use <code>Immediate</code> only on single-node clusters or when node affinity is managed externally.</p></td>
<td style="text-align: left;"><div class="sourceCode" id="cb2"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">storageClassOptions</span><span class="kw">:</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">volumeBindingMode</span><span class="kw">:</span><span class="at"> Immediate</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>additionalParameters</code></p></td>
<td style="text-align: left;"><p><code>map[string]string</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
<td style="text-align: left;"><p>Adds custom key-value pairs to the <code>StorageClass .parameters</code> map.</p>
<p>Default: <code>{}</code> (empty). Maximum entries: 16.</p>
<p>StorageClass parameters are passed to the CSI driver (TopoLVM) during volume provisioning. TopoLVM recognizes only <code>topolvm.io/device-class</code> and <code>csi.storage.k8s.io/fstype</code>. Use <code>additionalParameters</code> for forward-compatibility or for parameters consumed by other Kubernetes components.</p>
<p>The following keys are managed by LVMS and are rejected at admission:</p>
<ul>
<li><p><code>topolvm.io/device-class</code> — automatically set to the device class name</p></li>
<li><p><code>csi.storage.k8s.io/fstype</code> — automatically set from the <code>fstype</code> field on the device class</p></li>
</ul>
<div class="important">
<div class="title">
&#10;</div>
<p>To change the filesystem type, use the <code>fstype</code> field on the device class directly. Do not use <code>additionalParameters</code>.</p>
</div></td>
<td style="text-align: left;"><div class="sourceCode" id="cb3"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="fu">storageClassOptions</span><span class="kw">:</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">additionalParameters</span><span class="kw">:</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">custom-param-key</span><span class="kw">:</span><span class="at"> custom-param-value</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>additionalLabels</code></p></td>
<td style="text-align: left;"><p><code>map[string]string</code></p></td>
<td style="text-align: left;"><p>No</p></td>
<td style="text-align: left;"><p>Adds custom labels to the StorageClass metadata.</p>
<p>Default: none. Maximum entries: 16.</p>
<p>Use for organizational tagging, cluster policy integration, or monitoring. When you remove a label from <code>additionalLabels</code>, the operator removes it from the StorageClass during the next reconciliation. Labels added directly by other tools are not affected.</p>
<p>The following label keys are reserved and cannot be set through <code>additionalLabels</code>:</p>
<ul>
<li><p><code>app.kubernetes.io/managed-by</code></p></li>
<li><p><code>app.kubernetes.io/part-of</code></p></li>
<li><p><code>app.kubernetes.io/name</code></p></li>
<li><p><code>app.kubernetes.io/component</code></p></li>
<li><p>Any key with the prefix <code>owned-by.topolvm.io/</code></p></li>
</ul></td>
<td style="text-align: left;"><div class="sourceCode" id="cb4"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="fu">storageClassOptions</span><span class="kw">:</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">additionalLabels</span><span class="kw">:</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">environment</span><span class="kw">:</span><span class="at"> production</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">team</span><span class="kw">:</span><span class="at"> storage</span></span></code></pre></div></td>
</tr>
</tbody>
</table>

## Updating LVM cluster labels

To organize and categorize your storage resources, you can update, remove, or clear custom StorageClass labels by patching the additionalLabels field in the LVMCluster custom resource.

<div>

<div class="title">

Procedure

</div>

1.  Patch the `LVMCluster` resource to update `additionalLabels` by running the following command:

    ``` terminal
    $ oc -n openshift-lvm-storage patch lvmcluster <name> --type=json \
      -p '[{"op":"replace","path":"/spec/storage/deviceClasses/0/storageClassOptions/additionalLabels","value":{"environment":"staging"}}]'
    ```

2.  To remove a specific label, update `additionalLabels` without the label you want to remove. The Operator removes the label from the `StorageClass` during the next reconciliation.

3.  To remove all custom labels, set `additionalLabels` to an empty map `{}`.

    > [!NOTE]
    > The Operator preserves labels that you add directly to the `StorageClass`, for example with `oc label storageclass lvms-vg1 my-label=value`. The Operator prunes only the labels that you manage through the `additionalLabels` field in the `LVMCluster` custom resource (CR) when you remove them from the CR.

</div>

## Sample LVM cluster configuration with storage class option

Use these examples to configure `storageClassOptions` in your `LVMCluster` custom resource (CR) to meet your specific storage requirements.

<div class="formalpara">

<div class="title">

Default StorageClass behavior (no options)

</div>

``` yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-lvm-storage
spec:
  storage:
    deviceClasses:
    - name: vg1
      default: true
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
```

</div>

This produces a `StorageClass` with `reclaimPolicy: Delete` and `volumeBindingMode: WaitForFirstConsumer`, which is the same as the behavior before this feature.

<div class="formalpara">

<div class="title">

Retain policy for data protection

</div>

``` yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-lvm-storage
spec:
  storage:
    deviceClasses:
    - name: vg1
      default: true
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
      storageClassOptions:
        reclaimPolicy: Retain
```

</div>

<div class="formalpara">

<div class="title">

Immediate binding for pre-provisioning

</div>

``` yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-lvm-storage
spec:
  storage:
    deviceClasses:
    - name: vg1
      default: true
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
      storageClassOptions:
        volumeBindingMode: Immediate
```

</div>

<div class="formalpara">

<div class="title">

All options configured together

</div>

``` yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-lvm-storage
spec:
  storage:
    deviceClasses:
    - name: vg1
      default: true
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
      storageClassOptions:
        reclaimPolicy: Retain
        volumeBindingMode: WaitForFirstConsumer
        additionalParameters:
          custom-key: custom-value
        additionalLabels:
          environment: production
          team: storage
```

</div>

<div class="formalpara">

<div class="title">

Multiple device classes with different options

</div>

``` yaml
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: my-lvmcluster
  namespace: openshift-lvm-storage
spec:
  storage:
    deviceClasses:
    - name: vg-fast
      default: true
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
      deviceSelector:
        paths:
        - /dev/nvme0n1
      storageClassOptions:
        reclaimPolicy: Delete
        volumeBindingMode: WaitForFirstConsumer
        additionalLabels:
          tier: fast
    - name: vg-archive
      thinPoolConfig:
        name: thin-pool-1
        sizePercent: 90
        overprovisionRatio: 10
      deviceSelector:
        paths:
        - /dev/sda
      storageClassOptions:
        reclaimPolicy: Retain
        volumeBindingMode: WaitForFirstConsumer
        additionalLabels:
          tier: archive
```

</div>

For a device class named `vg1` with the full configuration, LVMS generates a `StorageClass` named `lvms-vg1` with the following structure:

``` yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: lvms-vg1
  annotations:
    description: "Provides RWO and RWOP Filesystem & Block volumes"
    storageclass.kubernetes.io/is-default-class: "true"
  labels:
    environment: production
    team: storage
provisioner: topolvm.io
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
parameters:
  custom-key: custom-value
  topolvm.io/device-class: vg1
  csi.storage.k8s.io/fstype: xfs
```

The `StorageClass` name always follows the convention `lvms-<device_class_name>`.

## Immutable fields of the storage class options

After you create the LVMCluster custom resource, you cannot change certain `storageClassOptions` fields, such as `reclaimPolicy`, `volumeBindingMode`, and `additionalParameters`. To change an immutable field, you must delete and recreate the LVMCluster with the new values.

This mirrors the behavior of Kubernetes `StorageClasses`, which do not allow changes to these fields after creation.

If you attempt to modify an immutable field, the API server rejects the request:

``` terminal
Invalid value: "object": reclaimPolicy is immutable once set
```

There is no way to patch or update immutable fields in place. To change an immutable field, you must delete the `LVMCluster` and recreate it with the new values.

For example, you cannot change the filesystem type through `additionalParameters`. The `csi.storage.k8s.io/fstype` parameter is managed by LVMS and is rejected at admission if set through `additionalParameters`. To use `ext4` instead of the default `xfs`, use the `fstype` field on the device class:

``` yaml
deviceClasses:
- name: vg1
  fstype: ext4
```

However, the `fstype` field is also immutable after creation.

> [!NOTE]
> The deletion gates require all PVCs and, for the `Retain` policy, all PVs to be removed before the `LVMCluster` can be deleted. After you recreate the `LVMCluster` with the new values, new PVCs use the updated StorageClass configuration.

## Behaviors not controlled by StorageClass options

Review these behaviors before you delete an LVMCluster. Although these behaviors relate to `storageClassOptions`, the `storageClassOptions` field does not control them.

Volume expansion behavior
Logical Volume Manager Storage (LVMS) always enables volume expansion by setting `allowVolumeExpansion: true` on generated StorageClasses. You cannot control this setting by using the `storageClassOptions` field. All LVMS volumes support online expansion.

VolumeSnapshotClass management
The `storageClassOptions` field only affects StorageClasses. When you configure thin provisioning, LVMS generates a `VolumeSnapshotClass` for each device class. This generated class always uses a fixed value `deletionPolicy: Delete`, regardless of the reclaimPolicy that you set in `storageClassOptions`.

Additionally, LVMS does not apply the `additionalParameters` and `additionalLabels` fields to `VolumeSnapshotClasses`. If you need to retain snapshot data, you must manage it separately from the StorageClass reclaim policy.

Default StorageClass annotation behavior
The default field on a device class controls the `storageclass.kubernetes.io/is-default-class` annotation on the generated StorageClass.

Setting `default: true` does not guarantee that the LVMS StorageClass becomes the cluster default. If another default StorageClass already exists on the cluster, for example, gp3-csi on AWS-based OpenShift Container Platform clusters, LVMS sets the annotation to `false` to prevent many cluster-wide defaults. Because the Operator actively manages this annotation, it reverts any manual, out-of-band changes during the next reconciliation loop.

# Ways to scale up the storage of clusters

Scale up worker node storage capacity when running out of space, adding new applications, or expanding cluster capacity by using the OpenShift CLI (`oc`) to add new devices or worker nodes.

OpenShift Container Platform supports additional worker nodes for clusters on bare metal user-provisioned infrastructure.

Logical Volume Manager (LVM) Storage detects and uses additional worker nodes when the nodes become active.

To add a new device to the existing worker nodes on a cluster, you must add the path to the new device in the `deviceSelector` field of the `LVMCluster` custom resource (CR).

> [!IMPORTANT]
> You can add the `deviceSelector` field in the `LVMCluster` CR only while creating the `LVMCluster` CR. If you have not added the `deviceSelector` field while creating the `LVMCluster` CR, you must delete the `LVMCluster` CR and create a new `LVMCluster` CR containing the `deviceSelector` field.

If you do not add the `deviceSelector` field in the `LVMCluster` CR, LVM Storage automatically adds the new devices when the devices are available.

> [!NOTE]
> LVM Storage adds only the supported devices. For information about unsupported devices, see "Devices not supported by LVM Storage".

<div>

<div class="title">

Additional resources

</div>

- [Adding worker nodes to single-node OpenShift clusters](../../nodes/nodes/nodes-sno-worker-nodes.md#nodes-sno-worker-nodes)

- [Devices not supported by LVM Storage](persistent-storage-using-lvms.md#lvms-unsupported-devices_logical-volume-manager-storage)

</div>

## Scaling up the storage of clusters by using the CLI

Scale up worker node storage capacity when running out of space, adding new applications, or expanding cluster capacity by using the OpenShift CLI (`oc`) to add new devices or worker nodes.

<div>

<div class="title">

Prerequisites

</div>

- You have additional unused devices on each cluster to be used by Logical Volume Manager (LVM) Storage.

- You have installed the OpenShift CLI (`oc`).

- You have created an `LVMCluster` custom resource (CR).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `LVMCluster` CR by running the following command:

    ``` terminal
    $ oc edit <lvmcluster_file_name> -n <namespace>
    ```

2.  Add the path to the new device in the `deviceSelector` field.

    <div class="formalpara">

    <div class="title">

    Example `LVMCluster` CR

    </div>

    ``` yaml
    apiVersion: lvm.topolvm.io/v1alpha1
    kind: LVMCluster
    metadata:
      name: my-lvmcluster
    spec:
      storage:
        deviceClasses:
    # ...
          deviceSelector:
            paths:
            - /dev/disk/by-path/pci-0000:87:00.0-nvme-1
            - /dev/disk/by-path/pci-0000:88:00.0-nvme-1
            optionalPaths:
            - /dev/disk/by-path/pci-0000:89:00.0-nvme-1
            - /dev/disk/by-path/pci-0000:90:00.0-nvme-1
    # ...
    ```

    </div>

    - `spec…​deviceSelector`: Contains the configuration to specify the paths to the devices that you want to add to the LVM volume group. You can specify the device paths in the `paths` field, the `optionalPaths` field, or both. If you do not specify the device paths in both `paths` and `optionalPaths`, Logical Volume Manager (LVM) Storage adds the supported unused devices to the LVM volume group. LVM Storage adds the devices to the LVM volume group only if the following conditions are met:

      - The device path exists.

      - The device is supported by LVM Storage. For information about unsupported devices, see "Devices not supported by LVM Storage".

    - `spec…​deviceSelector.paths`: Specifies the device paths. If the device path specified in this field does not exist, or the device is not supported by LVM Storage, the `LVMCluster` CR moves to the `Failed` state.

    - `spec…​deviceSelector.optionalPaths`: Specifies the optional device paths. If the device path specified in this field does not exist, or the device is not supported by LVM Storage, LVM Storage ignores the device without causing an error.

      > [!IMPORTANT]
      > After a device is added to the LVM volume group, it cannot be removed.

3.  Save the `LVMCluster` CR.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the `LVMCluster` custom resource](persistent-storage-using-lvms.md#about-lvmcluster_logical-volume-manager-storage)

- [Devices not supported by LVM Storage](persistent-storage-using-lvms.md#lvms-unsupported-devices_logical-volume-manager-storage)

- [About adding devices to a volume group](persistent-storage-using-lvms.md#about-adding-devices-to-a-vg_logical-volume-manager-storage)

</div>

## Scaling up the storage of clusters by using the web console

Scale up worker node storage capacity when running out of space, adding new applications, or expanding cluster capacity by using the OpenShift Container Platform web console to add new devices or worker nodes.

<div>

<div class="title">

Prerequisites

</div>

- You have additional unused devices on each cluster to be used by Logical Volume Manager (LVM) Storage.

- You have created an `LVMCluster` custom resource (CR).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Click **Ecosystem** → **Installed Operators**.

3.  Click **LVM Storage** in the `openshift-lvm-storage` namespace.

4.  Click the **LVMCluster** tab to view the `LVMCluster` CR created on the cluster.

5.  From the **Actions** menu, select **Edit LVMCluster**.

6.  Click the **YAML** tab.

7.  Edit the `LVMCluster` CR to add the new device path in the `deviceSelector` field:

    <div class="formalpara">

    <div class="title">

    Example `LVMCluster` CR

    </div>

    ``` yaml
    apiVersion: lvm.topolvm.io/v1alpha1
    kind: LVMCluster
    metadata:
      name: my-lvmcluster
    spec:
      storage:
        deviceClasses:
    # ...
          deviceSelector:
            paths:
            - /dev/disk/by-path/pci-0000:87:00.0-nvme-1
            - /dev/disk/by-path/pci-0000:88:00.0-nvme-1
            optionalPaths:
            - /dev/disk/by-path/pci-0000:89:00.0-nvme-1
            - /dev/disk/by-path/pci-0000:90:00.0-nvme-1
    # ...
    ```

    </div>

    - `spec…​deviceSelector`: Contains the configuration to specify the paths to the devices that you want to add to the LVM volume group. You can specify the device paths in the `paths` field, the `optionalPaths` field, or both. If you do not specify the device paths in both `paths` and `optionalPaths`, Logical Volume Manager (LVM) Storage adds the supported unused devices to the LVM volume group. LVM Storage adds the devices to the LVM volume group only if the following conditions are met:

      - The device path exists.

      - The device is supported by LVM Storage. For information about unsupported devices, see "Devices not supported by LVM Storage".

    - `spec…​deviceSelector.paths`: Specifies the device paths. If the device path specified in this field does not exist, or the device is not supported by LVM Storage, the `LVMCluster` CR moves to the `Failed` state.

    - `spec…​deviceSelector.optionalPaths`: Specifies the optional device paths. If the device path specified in this field does not exist, or the device is not supported by LVM Storage, LVM Storage ignores the device without causing an error.

      > [!IMPORTANT]
      > After a device is added to the LVM volume group, it cannot be removed.

8.  Click **Save**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the `LVMCluster` custom resource](persistent-storage-using-lvms.md#about-lvmcluster_logical-volume-manager-storage)

- [Devices not supported by LVM Storage](persistent-storage-using-lvms.md#lvms-unsupported-devices_logical-volume-manager-storage)

- [About adding devices to a volume group](persistent-storage-using-lvms.md#about-adding-devices-to-a-vg_logical-volume-manager-storage)

</div>

## Scaling up the storage of clusters by using RHACM

Scale up worker node storage capacity when running out of space, adding new applications, or expanding cluster capacity by using RHACM to add new devices or worker nodes.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the RHACM cluster using an account with `cluster-admin` privileges.

- You have created an `LVMCluster` custom resource (CR) by using RHACM.

- You have additional unused devices on each cluster to be used by Logical Volume Manager (LVM) Storage.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the RHACM CLI using your OpenShift Container Platform credentials.

2.  Edit the `LVMCluster` CR that you created using RHACM by running the following command:

    ``` terminal
    $ oc edit -f <file_name> -n <namespace>
    ```

    Replace `<file_name>` with the name of the `LVMCluster` CR.

3.  In the `LVMCluster` CR, add the path to the new device in the `deviceSelector` field.

    <div class="formalpara">

    <div class="title">

    Example `LVMCluster` CR

    </div>

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: ConfigurationPolicy
    metadata:
      name: lvms
    spec:
      object-templates:
         - complianceType: musthave
           objectDefinition:
             apiVersion: lvm.topolvm.io/v1alpha1
             kind: LVMCluster
             metadata:
               name: my-lvmcluster
               namespace: openshift-lvm-storage
             spec:
               storage:
                 deviceClasses:
    # ...
                   deviceSelector:
                     paths:
                     - /dev/disk/by-path/pci-0000:87:00.0-nvme-1
                     optionalPaths:
                     - /dev/disk/by-path/pci-0000:89:00.0-nvme-1
    # ...
    ```

    </div>

    - `deviceSelector`: Contains the configuration to specify the paths to the devices that you want to add to the LVM volume group. You can specify the device paths in the `paths` field, the `optionalPaths` field, or both. If you do not specify the device paths in both `paths` and `optionalPaths`, Logical Volume Manager (LVM) Storage adds the supported unused devices to the LVM volume group. LVM Storage adds the devices to the LVM volume group only if the following conditions are met:

      - The device path exists.

      - The device is supported by LVM Storage. For information about unsupported devices, see "Devices not supported by LVM Storage".

    - `paths`: Specifies the device paths. If the device path specified in this field does not exist, or the device is not supported by LVM Storage, the `LVMCluster` CR moves to the `Failed` state.

    - `optionalPaths`: Specifies the optional device paths. If the device path specified in this field does not exist, or the device is not supported by LVM Storage, LVM Storage ignores the device without causing an error.

      > [!IMPORTANT]
      > After a device is added to the LVM volume group, it cannot be removed.

4.  Save the `LVMCluster` CR.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the `LVMCluster` custom resource](persistent-storage-using-lvms.md#about-lvmcluster_logical-volume-manager-storage)

- [Devices not supported by LVM Storage](persistent-storage-using-lvms.md#lvms-unsupported-devices_logical-volume-manager-storage)

- [About adding devices to a volume group](persistent-storage-using-lvms.md#about-adding-devices-to-a-vg_logical-volume-manager-storage)

</div>

# Expanding a persistent volume claim

After scaling up cluster storage, you can expand existing persistent volume claims (PVCs) to increase their storage capacity by updating the `storage` field in the PVC.

<div>

<div class="title">

Prerequisites

</div>

- Dynamic provisioning is used.

- The `StorageClass` object associated with the PVC has the `allowVolumeExpansion` field set to `true`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Update the value of the `spec.resources.requests.storage` field to a value that is greater than the current value by running the following command:

    ``` terminal
    $ oc patch pvc <pvc_name> -n <application_namespace> \
      --type=merge -p \ '{ "spec": { "resources": { "requests": { "storage": "<desired_size>" }}}}'
    ```

    - Replace `<pvc_name>` with the name of the PVC that you want to expand.

    - Replace `<desired_size>` with the new size to expand the PVC.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that resizing is completed, run the following command:

  ``` terminal
  $ oc get pvc <pvc_name> -n <application_namespace> -o=jsonpath={.status.capacity.storage}
  ```

  LVM Storage adds the `Resizing` condition to the PVC during expansion. It deletes the `Resizing` condition after the PVC expansion.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Ways to scale up the storage of clusters](persistent-storage-using-lvms.md#lvms-about-scaling-storage-of-cluster_logical-volume-manager-storage)

- [Enabling volume expansion support](../expanding-persistent-volumes.md#add-volume-expansion_expanding-persistent-volumes)

</div>

# Deleting a persistent volume claim

You can delete a persistent volume claim (PVC) when it is no longer needed to free up storage resources or when decommissioning an application by using the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Delete the PVC by running the following command:

    ``` terminal
    $ oc delete pvc <pvc_name> -n <namespace>
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the PVC is deleted, run the following command:

  ``` terminal
  $ oc get pvc -n <namespace>
  ```

  The deleted PVC must not be present in the output of this command.

</div>

# About volume snapshots

You can create volume snapshots of persistent volume claims (PVCs) provisioned by LVM Storage to back up application data or revert to a previous state, providing data protection and recovery capabilities.

You can perform the following actions using the volume snapshots:

- Back up your application data.

  > [!IMPORTANT]
  > Volume snapshots are located on the same devices as the original data. To use the volume snapshots as backups, you must move the snapshots to a secure location. You can use OpenShift API for Data Protection (OADP) backup and restore solutions. For information about OADP, see "OADP features".

- Revert to a state at which the volume snapshot was taken.

> [!NOTE]
> You can also create volume snapshots of the volume clones.

## Limitations for creating volume snapshots in multi-node topology

LVM Storage has the following limitations for creating volume snapshots in multi-node topology:

- Creating volume snapshots is based on the LVM thin pool capabilities.

- After creating a volume snapshot, the node must have additional storage space for further updating the original data source.

- You can create volume snapshots only on the node where you have deployed the original data source.

- Pods relying on the PVC that uses the snapshot data can be scheduled only on the node where you have deployed the original data source.

<div>

<div class="title">

Additional resources

</div>

- [OADP features](../../backup_and_restore/application_backup_and_restore/oadp-features-plugins.md#oadp-features_oadp-features-plugins)

</div>

## Creating volume snapshots

Create volume snapshots to capture point-in-time copies of persistent volume claims (PVCs) for data backup or recovery purposes by creating a `VolumeSnapshot` object, based on the available thin pool capacity and over-provisioning limits.

To create a volume snapshot, you must create a `VolumeSnapshotClass` object.

<div>

<div class="title">

Prerequisites

</div>

- You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.

- You ensured that the persistent volume claim (PVC) is in `Bound` state. This is required for a consistent snapshot.

- You stopped all the I/O to the PVC.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Create a `VolumeSnapshot` object:

    <div class="formalpara">

    <div class="title">

    Example `VolumeSnapshot` object

    </div>

    ``` yaml
    apiVersion: snapshot.storage.k8s.io/v1
    kind: VolumeSnapshot
    metadata:
      name: lvm-block-1-snap
    spec:
      source:
        persistentVolumeClaimName: lvm-block-1
      volumeSnapshotClassName: lvms-vg1
    ```

    </div>

    - `metadata.name`: Specifies a name for the volume snapshot.

    - `spec.source.persistentVolumeClaimName`: Specifies the name of the source PVC. LVM Storage creates a snapshot of this PVC.

    - `spec.volumeSnapshotClassName`: Specifies the name of a volume snapshot class.

      > [!NOTE]
      > To get the list of available volume snapshot classes, run the following command:
      >
      > ``` terminal
      > $ oc get volumesnapshotclass
      > ```

3.  Create the volume snapshot in the namespace where you created the source PVC by running the following command:

    ``` terminal
    $ oc create -f <file_name> -n <namespace>
    ```

    LVM Storage creates a read-only copy of the PVC as a volume snapshot.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the volume snapshot is created, run the following command:

  ``` terminal
  $ oc get volumesnapshot -n <namespace>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME               READYTOUSE   SOURCEPVC     SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS   SNAPSHOTCONTENT                                    CREATIONTIME   AGE
  lvm-block-1-snap   true         lvms-test-1                           1Gi           lvms-vg1        snapcontent-af409f97-55fc-40cf-975f-71e44fa2ca91   19s            19s
  ```

  </div>

  The value of the `READYTOUSE` field for the volume snapshot that you created must be `true`.

</div>

## Restoring volume snapshots

Restore volume snapshots to recover data from a previous point in time by creating a persistent volume claim (PVC) that references the snapshot, producing an independent copy separate from the original snapshot and source PVC.

To restore a volume snapshot, you must create a persistent volume claim (PVC) with the `dataSource.name` field set to the name of the volume snapshot.

The restored PVC is independent of the volume snapshot and the source PVC.

<div>

<div class="title">

Prerequisites

</div>

- You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.

- You have created a volume snapshot.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Create a `PersistentVolumeClaim` object with the configuration to restore the volume snapshot:

    <div class="formalpara">

    <div class="title">

    Example `PersistentVolumeClaim` object to restore a volume snapshot

    </div>

    ``` yaml
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: lvm-block-1-restore
    spec:
      accessModes:
      - ReadWriteOnce
      volumeMode: Block
      Resources:
        Requests:
          storage: 2Gi
      storageClassName: lvms-vg1
      dataSource:
        name: lvm-block-1-snap
        kind: VolumeSnapshot
        apiGroup: snapshot.storage.k8s.io
    ```

    </div>

    - `spec.Resources.Requests.storage`: Specifies the storage size of the restored PVC. The storage size of the requested PVC must be greater than or equal to the storage size of the volume snapshot that you want to restore. If a larger PVC is required, you can also resize the PVC after restoring the volume snapshot.

    - `spec.storageClassName`: Set this field to the value of the `storageClassName` field in the source PVC of the volume snapshot that you want to restore.

    - `spec.dataSource.name`: Set this field to the name of the volume snapshot that you want to restore.

3.  Create the PVC in the namespace where you created the volume snapshot by running the following command:

    ``` terminal
    $ oc create -f <file_name> -n <namespace>
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the volume snapshot is restored, run the following command:

  ``` terminal
  $ oc get pvc -n <namespace>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                  STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
  lvm-block-1-restore   Bound    pvc-e90169a8-fd71-4eea-93b8-817155f60e47   1Gi        RWO            lvms-vg1       5s
  ```

  </div>

</div>

## Deleting volume snapshots

Delete volume snapshots when they are no longer needed to free up storage resources and prevent orphaned snapshots, since LVM Storage does not automatically delete snapshots when you delete the source persistent volume claim (PVC).

> [!IMPORTANT]
> When you delete a persistent volume claim (PVC), LVM Storage deletes only the PVC, but not the snapshots of the PVC.

<div>

<div class="title">

Prerequisites

</div>

- You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.

- You have ensured that the volume snapshot that you want to delete is not in use.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Delete the volume snapshot by running the following command:

    ``` terminal
    $ oc delete volumesnapshot <volume_snapshot_name> -n <namespace>
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the volume snapshot is deleted, run the following command:

  ``` terminal
  $ oc get volumesnapshot -n <namespace>
  ```

  The deleted volume snapshot must not be present in the output of this command.

</div>

# About volume clones

A volume clone is a duplicate of an existing persistent volume claim (PVC) that creates a point-in-time copy of data more efficiently than snapshots, useful for testing, development, or creating independent copies of application data.

## Limitations for creating volume clones in multi-node topology

LVM Storage has the following limitations for creating volume clones in multi-node topology:

- Creating volume clones is based on the LVM thin pool capabilities.

- The node must have additional storage after creating a volume clone for further updating the original data source.

- You can create volume clones only on the node where you have deployed the original data source.

- Pods relying on the PVC that uses the clone data can be scheduled only on the node where you have deployed the original data source.

## Creating volume clones

Create volume clones to duplicate persistent volume claim (PVC) data for testing, development, or creating independent writable copies by creating a `PersistentVolumeClaim` object that references the source PVC.

You must create a `PersistentVolumeClaim` object in the namespace where you created the source PVC.

> [!IMPORTANT]
> The cloned PVC has write access.

<div>

<div class="title">

Prerequisites

</div>

- You ensured that the source PVC is in `Bound` state. This is required for a consistent clone.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Create a `PersistentVolumeClaim` object:

    <div class="formalpara">

    <div class="title">

    Example `PersistentVolumeClaim` object to create a volume clone

    </div>

    ``` yaml
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: lvm-pvc-clone
    spec:
      accessModes:
      - ReadWriteOnce
      storageClassName: lvms-vg1
      volumeMode: Filesystem
      dataSource:
        kind: PersistentVolumeClaim
        name: lvm-pvc
      resources:
        requests:
          storage: 1Gi
    ```

    </div>

    - `spec.storageClassName`: Set this field to the value of the `storageClassName` field in the source PVC.

    - `spec.volumeMode`: Set this field to the `volumeMode` field in the source PVC.

    - `spec.dataSource.name`: Specifies the name of the source PVC.

    - `spec.resources.requests.storage`: Specifies the storage size for the cloned PVC. The storage size of the cloned PVC must be greater than or equal to the storage size of the source PVC.

3.  Create the PVC in the namespace where you created the source PVC by running the following command:

    ``` terminal
    $ oc create -f <file_name> -n <namespace>
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the volume clone is created, run the following command:

  ``` terminal
  $ oc get pvc -n <namespace>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
  lvm-block-1-clone   Bound    pvc-e90169a8-fd71-4eea-93b8-817155f60e47   1Gi        RWO            lvms-vg1       5s
  ```

  </div>

</div>

## Deleting volume clones

Delete volume clones when they are no longer needed to free up storage resources, since LVM Storage does not automatically delete clones when you delete the source persistent volume claim (PVC).

> [!IMPORTANT]
> When you delete a persistent volume claim (PVC), LVM Storage deletes only the source persistent volume claim (PVC) but not the clones of the PVC.

<div>

<div class="title">

Prerequisites

</div>

- You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Delete the cloned PVC by running the following command:

    ``` terminal
    $ oc delete pvc <clone_pvc_name> -n <namespace>
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the volume clone is deleted, run the following command:

  ``` terminal
  $ oc get pvc -n <namespace>
  ```

  The deleted volume clone must not be present in the output of this command.

</div>

# Updating LVM Storage

You can update LVM Storage to ensure compatibility with the OpenShift Container Platform version after upgrading your cluster.

> [!NOTE]
> The default namespace for the LVM Storage Operator is `openshift-lvm-storage`.

<div>

<div class="title">

Prerequisites

</div>

- You have updated your OpenShift Container Platform cluster.

- You have installed a previous version of LVM Storage.

- You have installed the OpenShift CLI (`oc`).

- You have access to the cluster using an account with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Update the `Subscription` custom resource (CR) that you created while installing LVM Storage by running the following command:

    ``` terminal
    $ oc patch subscription lvms-operator -n openshift-lvm-storage --type merge --patch '{"spec":{"channel":"<update_channel>"}}'
    ```

    Replace `<update_channel>` with the version of LVM Storage that you want to install. For example, `stable-4.22`.

3.  View the update events to check that the installation is complete by running the following command:

    ``` terminal
    $ oc get events -n openshift-lvm-storage
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ...
    8m13s       Normal    RequirementsUnknown   clusterserviceversion/lvms-operator.v4.22   requirements not yet checked
    8m11s       Normal    RequirementsNotMet    clusterserviceversion/lvms-operator.v4.22   one or more requirements couldn't be found
    7m50s       Normal    AllRequirementsMet    clusterserviceversion/lvms-operator.v4.22   all requirements found, attempting install
    7m50s       Normal    InstallSucceeded      clusterserviceversion/lvms-operator.v4.22   waiting for install components to report healthy
    7m49s       Normal    InstallWaiting        clusterserviceversion/lvms-operator.v4.22   installing: waiting for deployment lvms-operator to become ready: deployment "lvms-operator" waiting for 1 outdated replica(s) to be terminated
    7m39s       Normal    InstallSucceeded      clusterserviceversion/lvms-operator.v4.22   install strategy completed with no errors
    ...
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

- Verify the LVM Storage version by running the following command:

  ``` terminal
  $ oc get subscription lvms-operator -n openshift-lvm-storage -o jsonpath='{.status.installedCSV}'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  lvms-operator.v4.22
  ```

  </div>

</div>

# Monitoring LVM Storage

You can monitor LVM Storage by enabling cluster monitoring with a namespace label, then viewing metrics to track storage usage and receiving alerts when thin pool and volume group capacity reaches critical thresholds to prevent data loss.

To enable cluster monitoring, you must add a label in the namespace where you have installed LVM Storage.

> [!IMPORTANT]
> For information about enabling cluster monitoring in RHACM, see "Observability" and "Adding custom metrics".

<div>

<div class="title">

Procedure

</div>

- To enable cluster monitoring, add the following label in the namespace where you have installed LVM Storage:

</div>

    openshift.io/cluster-monitoring=true

<div>

<div class="title">

Additional resources

</div>

- [Observability](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/observability/index)

- [Adding custom metrics](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.17/html-single/observability/index#adding-custom-metrics)

</div>

# Metrics and alerts overview

You can monitor thin pool and volume group usage through LVM Storage metrics, and receive alerts at 75% (near full) and 85% (critical) capacity thresholds to take corrective action before storage operations fail.

## Metrics

You can monitor LVM Storage by viewing the metrics.

The following table describes the `topolvm` metrics:

| Alert | Description |
|----|----|
| `topolvm_thinpool_data_percent` | Indicates the percentage of data space used in the LVM thinpool. |
| `topolvm_thinpool_metadata_percent` | Indicates the percentage of metadata space used in the LVM thinpool. |
| `topolvm_thinpool_size_bytes` | Indicates the size of the LVM thin pool in bytes. |
| `topolvm_volumegroup_available_bytes` | Indicates the available space in the LVM volume group in bytes. |
| `topolvm_volumegroup_size_bytes` | Indicates the size of the LVM volume group in bytes. |
| `topolvm_thinpool_overprovisioned_available` | Indicates the available over-provisioned size of the LVM thin pool in bytes. |

`topolvm` metrics

> [!NOTE]
> Metrics are updated every 10 minutes or when there is a change, such as a new logical volume creation, in the thin pool.

## Alerts

When the thin pool and volume group reach maximum storage capacity, further operations fail. This can lead to data loss.

LVM Storage sends the following alerts when the usage of the thin pool and volume group exceeds a certain value:

| Alert | Description |
|----|----|
| `VolumeGroupUsageAtThresholdNearFull` | This alert is triggered when both the volume group and thin pool usage exceeds 75% on nodes. Data deletion or volume group expansion is required. |
| `VolumeGroupUsageAtThresholdCritical` | This alert is triggered when both the volume group and thin pool usage exceeds 85% on nodes. In this case, the volume group is critically full. Data deletion or volume group expansion is required. |
| `ThinPoolDataUsageAtThresholdNearFull` | This alert is triggered when the thin pool data uusage in the volume group exceeds 75% on nodes. Data deletion or thin pool expansion is required. |
| `ThinPoolDataUsageAtThresholdCritical` | This alert is triggered when the thin pool data usage in the volume group exceeds 85% on nodes. Data deletion or thin pool expansion is required. |
| `ThinPoolMetaDataUsageAtThresholdNearFull` | This alert is triggered when the thin pool metadata usage in the volume group exceeds 75% on nodes. Data deletion or thin pool expansion is required. |
| `ThinPoolMetaDataUsageAtThresholdCritical` | This alert is triggered when the thin pool metadata usage in the volume group exceeds 85% on nodes. Data deletion or thin pool expansion is required. |

LVM Storage alerts

# Uninstalling LVM Storage by using the CLI

Uninstall LVM Storage when it is no longer needed or before upgrading to a different storage solution by using the OpenShift CLI (`oc`) after removing all provisioned storage resources.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to `oc` as a user with `cluster-admin` permissions.

- You deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by LVM Storage. You have also deleted the applications that are using these resources.

- You deleted the `LVMCluster` custom resource (CR).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the `currentCSV` value for the LVM Storage Operator by running the following command:

    ``` terminal
    $ oc get subscription.operators.coreos.com lvms-operator -n <namespace> -o yaml | grep currentCSV
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    currentCSV: lvms-operator.v4.15.3
    ```

    </div>

2.  Delete the subscription by running the following command:

    ``` terminal
    $ oc delete subscription.operators.coreos.com lvms-operator -n <namespace>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    subscription.operators.coreos.com "lvms-operator" deleted
    ```

    </div>

3.  Delete the CSV for the LVM Storage Operator in the target namespace by running the following command:

    ``` terminal
    $ oc delete clusterserviceversion <currentCSV> -n <namespace>
    ```

    Replace `<currentCSV>` with the `currentCSV` value for the LVM Storage Operator.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    clusterserviceversion.operators.coreos.com "lvms-operator.v4.15.3" deleted
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the LVM Storage Operator is uninstalled, run the following command:

  ``` terminal
  $ oc get csv -n <namespace>
  ```

  If the LVM Storage Operator was successfully uninstalled, it does not appear in the output of this command.

</div>

# Uninstalling LVM Storage by using the web console

Uninstall LVM Storage when it is no longer needed or before upgrading to a different storage solution by using the OpenShift Container Platform web console after removing all provisioned storage resources.

<div>

<div class="title">

Prerequisites

</div>

- You have access to OpenShift Container Platform as a user with `cluster-admin` permissions.

- You have deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by LVM Storage. You have also deleted the applications that are using these resources.

- You have deleted the `LVMCluster` custom resource (CR).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Click **Ecosystem** → **Installed Operators**.

3.  Click **LVM Storage** in the `openshift-lvm-storage` namespace.

4.  Click the **Details** tab.

5.  From the **Actions** menu, select **Uninstall Operator**.

6.  Optional: When prompted, select the **Delete all operand instances for this operator** checkbox to delete the operand instances for LVM Storage.

7.  Click **Uninstall**.

</div>

# Uninstalling LVM Storage installed using RHACM

To uninstall LVM Storage that you installed by using RHACM when it is no longer needed or before switching to a different storage solution, delete the RHACM `Policy` custom resource (CR) that you created for installation after removing all provisioned storage resources.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the RHACM cluster as a user with `cluster-admin` permissions.

- You have deleted the persistent volume claims (PVCs), volume snapshots, and volume clones provisioned by LVM Storage. You have also deleted the applications that are using these resources.

- You have deleted the `LVMCluster` CR that you created using RHACM.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift CLI (`oc`).

2.  Delete the RHACM `Policy` CR that you created for installing and configuring LVM Storage by using the following command:

    ``` terminal
    $ oc delete -f <policy> -n <namespace>
    ```

    Replace `<policy>` with the name of the `Policy` CR YAML file.

3.  Create a `Policy` CR YAML file with the configuration to uninstall LVM Storage:

    <div class="formalpara">

    <div class="title">

    Example `Policy` CR to uninstall LVM Storage

    </div>

    ``` yaml
    apiVersion: apps.open-cluster-management.io/v1
    kind: PlacementRule
    metadata:
      name: placement-uninstall-lvms
    spec:
      clusterConditions:
      - status: "True"
        type: ManagedClusterConditionAvailable
      clusterSelector:
        matchExpressions:
        - key: mykey
          operator: In
          values:
          - myvalue
    ---
    apiVersion: policy.open-cluster-management.io/v1
    kind: PlacementBinding
    metadata:
      name: binding-uninstall-lvms
    placementRef:
      apiGroup: apps.open-cluster-management.io
      kind: PlacementRule
      name: placement-uninstall-lvms
    subjects:
    - apiGroup: policy.open-cluster-management.io
      kind: Policy
      name: uninstall-lvms
    ---
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      annotations:
        policy.open-cluster-management.io/categories: CM Configuration Management
        policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
        policy.open-cluster-management.io/standards: NIST SP 800-53
      name: uninstall-lvms
    spec:
      disabled: false
      policy-templates:
      - objectDefinition:
          apiVersion: policy.open-cluster-management.io/v1
          kind: ConfigurationPolicy
          metadata:
            name: uninstall-lvms
          spec:
            object-templates:
            - complianceType: mustnothave
              objectDefinition:
                apiVersion: v1
                kind: Namespace
                metadata:
                  name: openshift-lvm-storage
            - complianceType: mustnothave
              objectDefinition:
                apiVersion: operators.coreos.com/v1
                kind: OperatorGroup
                metadata:
                  name: openshift-storage-operatorgroup
                  namespace: openshift-lvm-storage
                spec:
                  targetNamespaces:
                  - openshift-lvm-storage
            - complianceType: mustnothave
              objectDefinition:
                apiVersion: operators.coreos.com/v1alpha1
                kind: Subscription
                metadata:
                  name: lvms-operator
                  namespace: openshift-lvm-storage
            remediationAction: enforce
            severity: low
      - objectDefinition:
          apiVersion: policy.open-cluster-management.io/v1
          kind: ConfigurationPolicy
          metadata:
            name: policy-remove-lvms-crds
          spec:
            object-templates:
            - complianceType: mustnothave
              objectDefinition:
                apiVersion: apiextensions.k8s.io/v1
                kind: CustomResourceDefinition
                metadata:
                  name: logicalvolumes.topolvm.io
            - complianceType: mustnothave
              objectDefinition:
                apiVersion: apiextensions.k8s.io/v1
                kind: CustomResourceDefinition
                metadata:
                  name: lvmclusters.lvm.topolvm.io
            - complianceType: mustnothave
              objectDefinition:
                apiVersion: apiextensions.k8s.io/v1
                kind: CustomResourceDefinition
                metadata:
                  name: lvmvolumegroupnodestatuses.lvm.topolvm.io
            - complianceType: mustnothave
              objectDefinition:
                apiVersion: apiextensions.k8s.io/v1
                kind: CustomResourceDefinition
                metadata:
                  name: lvmvolumegroups.lvm.topolvm.io
            remediationAction: enforce
            severity: high
    ```

    </div>

4.  Create the `Policy` CR by running the following command:

    ``` terminal
    $ oc create -f <policy> -ns <namespace>
    ```

</div>

# Downloading log files and diagnostic information using must-gather

Use the must-gather tool to collect log files and diagnostic information when LVM Storage cannot automatically resolve a problem. You or Red Hat Support can then review the collected data to troubleshoot the issue.

<div>

<div class="title">

Procedure

</div>

- Run the `must-gather` command from the client connected to the LVM Storage cluster:

  ``` terminal
  $ oc adm must-gather --image=registry.redhat.io/lvms4/lvms-must-gather-rhel9:v4.22 --dest-dir=<directory_name>
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the must-gather tool](../../support/gathering-cluster-data.md#about-must-gather_gathering-cluster-data)

</div>

# Troubleshooting persistent storage

If persistent storage issues occur with Logical Volume Manager (LVM) Storage, such as persistent volume claims (PVCs) stuck in a pending state, missing components, or node and disk failures, you can diagnose and resolve the problem by reviewing logs and recovering affected resources.

## Investigating a PVC stuck in the Pending state

Investigate persistent volume claims (PVCs) stuck in a `Pending` state to determine whether the cause is insufficient resources, network problems, mismatched storage classes, or unavailable persistent volumes (PVs).

A persistent volume claim (PVC) can get stuck in the `Pending` state for the following reasons:

- Insufficient computing resources.

- Network problems.

- Mismatched storage class or node selector.

- No available persistent volumes (PVs).

- The node with the PV is in the `Not Ready` state.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to the OpenShift CLI (`oc`) as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Retrieve the list of PVCs by running the following command:

    ``` terminal
    $ oc get pvc
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        STATUS    VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
    lvms-test   Pending                                      lvms-vg1       11s
    ```

    </div>

2.  Inspect the events associated with a PVC stuck in the `Pending` state by running the following command:

    ``` terminal
    $ oc describe pvc <pvc_name>
    ```

    Replace `<pvc_name>` with the name of the PVC. For example, `lvms-vg1`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Type     Reason              Age               From                         Message
    ----     ------              ----              ----                         -------
    Warning  ProvisioningFailed  4s (x2 over 17s)  persistentvolume-controller  storageclass.storage.k8s.io "lvms-vg1" not found
    ```

    </div>

</div>

## Recovering from a missing storage class

Resolve the "storage class not found" error by verifying that the LVMCluster custom resource (CR) exists and all Logical Volume Manager (LVM) Storage pods are running, then reviewing logs to identify configuration issues.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to the OpenShift CLI (`oc`) as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the `LVMCluster` CR is present by running the following command:

    ``` terminal
    $ oc get lvmcluster -n <namespace>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME            AGE
    my-lvmcluster   65m
    ```

    </div>

2.  If the `LVMCluster` CR is not present, create an `LVMCluster` CR. For more information, see "Ways to create an LVMCluster custom resource".

3.  In the namespace where the operator is installed, check that all the LVM Storage pods are in the `Running` state by running the following command:

    ``` terminal
    $ oc get pods -n <namespace>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                  READY   STATUS    RESTARTS      AGE
    lvms-operator-7b9fb858cb-6nsml        3/3     Running   0             70m
    topolvm-controller-5dd9cf78b5-7wwr2   5/5     Running   0             66m
    topolvm-node-dr26h                    4/4     Running   0             66m
    vg-manager-r6zdv                      1/1     Running   0             66m
    ```

    </div>

    The output of this command must contain a running instance of the following pods:

    - `lvms-operator`

    - `vg-manager`

      If the `vg-manager` pod is stuck while loading a configuration file, it is due to a failure to locate an available disk for LVM Storage to use. To retrieve the necessary information to troubleshoot this issue, review the logs of the `vg-manager` pod by running the following command:

      ``` terminal
      $ oc logs -l app.kubernetes.io/component=vg-manager -n <namespace>
      ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the `LVMCluster` custom resource](persistent-storage-using-lvms.md#about-lvmcluster_logical-volume-manager-storage)

- [Ways to create an `LVMCluster` custom resource](persistent-storage-using-lvms.md#about-creating-lvmcluster-cr_logical-volume-manager-storage)

</div>

## Recovering from node failure

Identify failed nodes causing persistent volume claims (PVCs) to remain in pending state by examining the restart count of the `topolvm-node` pod, which indicates potential underlying node problems requiring investigation.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to the OpenShift CLI (`oc`) as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

- Examine the restart count of the `topolvm-node` pod instances by running the following command:

  ``` terminal
  $ oc get pods -n <namespace>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                                  READY   STATUS    RESTARTS      AGE
  lvms-operator-7b9fb858cb-6nsml        3/3     Running   0             70m
  topolvm-controller-5dd9cf78b5-7wwr2   5/5     Running   0             66m
  topolvm-node-dr26h                    4/4     Running   0             66m
  topolvm-node-54as8                    4/4     Running   0             66m
  topolvm-node-78fft                    4/4     Running   17 (8s ago)   66m
  vg-manager-r6zdv                      1/1     Running   0             66m
  vg-manager-990ut                      1/1     Running   0             66m
  vg-manager-an118                      1/1     Running   0             66m
  ```

  </div>

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

If the PVC is stuck in the `Pending` state even after you have resolved any issues with the node, you must perform a forced clean-up. For more information, see "Performing a forced clean-up".

</div>

<div>

<div class="title">

Additional resources

</div>

- [Performing a forced clean-up](persistent-storage-using-lvms.md#performing-a-forced-cleanup_logical-volume-manager-storage)

</div>

## Recovering from disk failure

Diagnose and resolve disk and volume provisioning failures by inspecting persistent volume claim (PVC) events to identify specific error messages, then connecting to the affected host to fix the underlying disk issue.

Disk and volume provisioning issues result with a generic error message such as `Failed to provision volume with storage class <storage_class_name>`. The generic error message is followed by a specific volume failure error message.

The following table describes the volume failure error messages:

| Error message | Description |
|----|----|
| `Failed to check volume existence` | Indicates a problem in verifying whether the volume already exists. Volume verification failure can be caused by network connectivity problems or other failures. |
| `Failed to bind volume` | Failure to bind a volume can happen if the persistent volume (PV) that is available does not match the requirements of the PVC. |
| `FailedMount` or `FailedAttachVolume` | This error indicates problems when trying to mount the volume to a node. If the disk has failed, this error can appear when a pod tries to use the PVC. |
| `FailedUnMount` | This error indicates problems when trying to unmount a volume from a node. If the disk has failed, this error can appear when a pod tries to use the PVC. |
| `Volume is already exclusively attached to one node and cannot be attached to another` | This error can appear with storage solutions that do not support `ReadWriteMany` access modes. |

Volume failure error messages

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to the OpenShift CLI (`oc`) as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Inspect the events associated with a PVC by running the following command:

    ``` terminal
    $ oc describe pvc <pvc_name>
    ```

    Replace `<pvc_name>` with the name of the PVC.

2.  Establish a direct connection to the host where the problem is occurring.

3.  Resolve the disk issue.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

If the volume failure messages persist or recur even after you have resolved the issue with the disk, you must perform a forced clean-up. For more information, see "Performing a forced clean-up".

</div>

<div>

<div class="title">

Additional resources

</div>

- [Performing a forced clean-up](persistent-storage-using-lvms.md#performing-a-forced-cleanup_logical-volume-manager-storage)

</div>

## Performing a forced clean-up

Perform a forced clean-up by removing all Logical Volume Manager (LVM) Storage custom resources (CRs) when disk or node-related problems continue after standard troubleshooting, to restore proper storage functioning.

If the disk or node-related problems persist even after you have completed the troubleshooting procedures, you must perform a forced clean-up. A forced clean-up is used to address persistent issues and ensure the proper functioning of LVM Storage.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to the OpenShift CLI (`oc`) as a user with `cluster-admin` permissions.

- You have deleted all the persistent volume claims (PVCs) that were created by using LVM Storage.

- You have stopped the pods that are using the PVCs that were created by using LVM Storage.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Switch to the namespace where you have installed the LVM Storage Operator by running the following command:

    ``` terminal
    $ oc project <namespace>
    ```

2.  Check if the `LogicalVolume` custom resources are present by running the following command:

    ``` terminal
    $ oc get logicalvolume
    ```

    1.  If the `LogicalVolume` CRs are present, delete them by running the following command:

        ``` terminal
        $ oc delete logicalvolume <name>
        ```

        Replace `<name>` with the name of the `LogicalVolume` CR.

    2.  After deleting the `LogicalVolume` CRs, remove their finalizers by running the following command:

        ``` terminal
        $ oc patch logicalvolume <name> -p '{"metadata":{"finalizers":[]}}' --type=merge
        ```

        Replace `<name>` with the name of the `LogicalVolume` CR.

3.  Check if the `LVMVolumeGroup` CRs are present by running the following command:

    ``` terminal
    $ oc get lvmvolumegroup
    ```

    1.  If the `LVMVolumeGroup` CRs are present, delete them by running the following command:

        ``` terminal
        $ oc delete lvmvolumegroup <name>
        ```

        Replace `<name>` with the name of the `LVMVolumeGroup` CR.

    2.  After deleting the `LVMVolumeGroup` CRs, remove their finalizers by running the following command:

        ``` terminal
        $ oc patch lvmvolumegroup <name> -p '{"metadata":{"finalizers":[]}}' --type=merge
        ```

        Replace `<name>` with the name of the `LVMVolumeGroup` CR.

4.  Delete any `LVMVolumeGroupNodeStatus` CRs by running the following command:

    ``` terminal
    $ oc delete lvmvolumegroupnodestatus --all
    ```

5.  Delete the `LVMCluster` CR by running the following command:

    ``` terminal
    $ oc delete lvmcluster --all
    ```

    1.  After deleting the `LVMCluster` CR, remove its finalizer by running the following command:

        ``` terminal
        $ oc patch lvmcluster <name> -p '{"metadata":{"finalizers":[]}}' --type=merge
        ```

        Replace `<name>` with the name of the `LVMCluster` CR.

</div>

# Additional resources

- [Red Hat Advanced Cluster Management for Kubernetes: Installing while connected online](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/install/installing#installing-while-connected-online)
