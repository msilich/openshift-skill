<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can deploy a managed single-node OpenShift cluster by using Red Hat Advanced Cluster Management (RHACM) and the assisted service.

> [!NOTE]
> If you are creating multiple managed clusters, use the `SiteConfig` method described in [Deploying far edge sites with ZTP](ztp-deploying-far-edge-sites.md#ztp-deploying-far-edge-sites).

> [!IMPORTANT]
> The target bare-metal host must meet the networking, firmware, and hardware requirements listed in [Recommended cluster configuration for vDU application workloads](ztp-reference-cluster-configuration-for-vdu.md#sno-configure-for-vdu).

# Generating GitOps ZTP installation and configuration CRs manually

Use the `generator` entrypoint for the `ztp-site-generate` container to generate the site installation and configuration custom resource (CRs) for a cluster based on `SiteConfig` and `PolicyGenerator` CRs.

> [!IMPORTANT]
> SiteConfig v1 is deprecated starting with OpenShift Container Platform version 4.18. Equivalent and improved functionality is now available through the SiteConfig Operator using the `ClusterInstance` custom resource. For more information, see [Procedure to transition from SiteConfig CRs to the ClusterInstance API](https://access.redhat.com/articles/7105238).
>
> For more information about the SiteConfig Operator, see [SiteConfig](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.12/html-single/multicluster_engine_operator_with_red_hat_advanced_cluster_management/index#siteconfig-intro).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to the hub cluster as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an output folder by running the following command:

    ``` terminal
    $ mkdir -p ./out
    ```

2.  Export the `argocd` directory from the `ztp-site-generate` container image:

    ``` terminal
    $ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.17 extract /home/ztp --tar | tar x -C ./out
    ```

    The `./out` directory has the reference `PolicyGenerator` and `SiteConfig` CRs in the `out/argocd/example/` folder.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    out
     └── argocd
          └── example
               ├── acmpolicygenerator
               │     ├── {policy-prefix}common-ranGen.yaml
               │     ├── {policy-prefix}example-sno-site.yaml
               │     ├── {policy-prefix}group-du-sno-ranGen.yaml
               │     ├── {policy-prefix}group-du-sno-validator-ranGen.yaml
               │     ├── ...
               │     ├── kustomization.yaml
               │     └── ns.yaml
               └── siteconfig
                      ├── example-sno.yaml
                      ├── KlusterletAddonConfigOverride.yaml
                      └── kustomization.yaml
    ```

    </div>

3.  Create an output folder for the site installation CRs:

    ``` terminal
    $ mkdir -p ./site-install
    ```

4.  Modify the example `SiteConfig` CR for the cluster type that you want to install. Copy `example-sno.yaml` to `site-1-sno.yaml` and modify the CR to match the details of the site and bare-metal host that you want to install, for example:

    ``` yaml
    # example-node1-bmh-secret & assisted-deployment-pull-secret need to be created under same namespace example-sno
    ---
    apiVersion: ran.openshift.io/v1
    kind: SiteConfig
    metadata:
      name: "example-sno"
      namespace: "example-sno"
    spec:
      baseDomain: "example.com"
      pullSecretRef:
        name: "assisted-deployment-pull-secret"
      clusterImageSetNameRef: "openshift-4.18"
      sshPublicKey: "ssh-rsa AAAA..."
      clusters:
        - clusterName: "example-sno"
          networkType: "OVNKubernetes"
          # installConfigOverrides is a generic way of passing install-config
          # parameters through the siteConfig.  The 'capabilities' field configures
          # the composable openshift feature.  In this 'capabilities' setting, we
          # remove all the optional set of components.
          # Notes:
          # - OperatorLifecycleManager is needed for 4.15 and later
          # - NodeTuning is needed for 4.13 and later, not for 4.12 and earlier
          # - Ingress is needed for 4.16 and later
          installConfigOverrides: |
            {
              "capabilities": {
                "baselineCapabilitySet": "None",
                "additionalEnabledCapabilities": [
                  "NodeTuning",
                  "OperatorLifecycleManager",
                  "Ingress"
                ]
              }
            }
          # It is strongly recommended to include crun manifests as part of the additional install-time manifests for 4.13+.
          # The crun manifests can be obtained from source-crs/optional-extra-manifest/ and added to the git repo ie.sno-extra-manifest.
          # extraManifestPath: sno-extra-manifest
          clusterLabels:
            # These example cluster labels correspond to the bindingRules in the PolicyGenTemplate examples
            du-profile: "latest"
            # These example cluster labels correspond to the bindingRules in the PolicyGenTemplate examples in ../policygentemplates:
            # ../acmpolicygenerator/common-ranGen.yaml will apply to all clusters with 'common: true'
            common: true
            # ../policygentemplates/group-du-sno-ranGen.yaml will apply to all clusters with 'group-du-sno: ""'
            group-du-sno: ""
            # ../policygentemplates/example-sno-site.yaml will apply to all clusters with 'sites: "example-sno"'
            # Normally this should match or contain the cluster name so it only applies to a single cluster
            sites: "example-sno"
          clusterNetwork:
            - cidr: 1001:1::/48
              hostPrefix: 64
          machineNetwork:
            - cidr: 1111:2222:3333:4444::/64
          serviceNetwork:
            - 1001:2::/112
          additionalNTPSources:
            - 1111:2222:3333:4444::2
          # Initiates the cluster for workload partitioning. Setting specific reserved/isolated CPUSets is done via PolicyTemplate
          # please see Workload Partitioning Feature for a complete guide.
          cpuPartitioningMode: AllNodes
          # Optionally; This can be used to override the KlusterletAddonConfig that is created for this cluster:
          #crTemplates:
          #  KlusterletAddonConfig: "KlusterletAddonConfigOverride.yaml"
          nodes:
            - hostName: "example-node1.example.com"
              role: "master"
              # Optionally; This can be used to configure desired BIOS setting on a host:
              #biosConfigRef:
              #  filePath: "example-hw.profile"
              bmcAddress: "idrac-virtualmedia+https://[1111:2222:3333:4444::bbbb:1]/redfish/v1/Systems/System.Embedded.1"
              bmcCredentialsName:
                name: "example-node1-bmh-secret"
              bootMACAddress: "AA:BB:CC:DD:EE:11"
              # Use UEFISecureBoot to enable secure boot.
              bootMode: "UEFISecureBoot"
              rootDeviceHints:
                deviceName: "/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:0:0"
              #crTemplates:
              #  BareMetalHost: "bmhOverride.yaml"
              # disk partition at `/var/lib/containers` with ignitionConfigOverride. Some values must be updated. See DiskPartitionContainer.md for more details
              ignitionConfigOverride: |
                {
                  "ignition": {
                    "version": "3.2.0"
                  },
                  "storage": {
                    "disks": [
                      {
                        "device": "/dev/disk/by-id/wwn-0x6b07b250ebb9d0002a33509f24af1f62",
                        "partitions": [
                          {
                            "label": "var-lib-containers",
                            "sizeMiB": 0,
                            "startMiB": 250000
                          }
                        ],
                        "wipeTable": false
                      }
                    ],
                    "filesystems": [
                      {
                        "device": "/dev/disk/by-partlabel/var-lib-containers",
                        "format": "xfs",
                        "mountOptions": [
                          "defaults",
                          "prjquota"
                        ],
                        "path": "/var/lib/containers",
                        "wipeFilesystem": true
                      }
                    ]
                  },
                  "systemd": {
                    "units": [
                      {
                        "contents": "# Generated by Butane\n[Unit]\nRequires=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\nAfter=systemd-fsck@dev-disk-by\\x2dpartlabel-var\\x2dlib\\x2dcontainers.service\n\n[Mount]\nWhere=/var/lib/containers\nWhat=/dev/disk/by-partlabel/var-lib-containers\nType=xfs\nOptions=defaults,prjquota\n\n[Install]\nRequiredBy=local-fs.target",
                        "enabled": true,
                        "name": "var-lib-containers.mount"
                      }
                    ]
                  }
                }
              nodeNetwork:
                interfaces:
                  - name: eno1
                    macAddress: "AA:BB:CC:DD:EE:11"
                config:
                  interfaces:
                    - name: eno1
                      type: ethernet
                      state: up
                      ipv4:
                        enabled: false
                      ipv6:
                        enabled: true
                        address:
                          # For SNO sites with static IP addresses, the node-specific,
                          # API and Ingress IPs should all be the same and configured on
                          # the interface
                          - ip: 1111:2222:3333:4444::aaaa:1
                            prefix-length: 64
                  dns-resolver:
                    config:
                      search:
                        - example.com
                      server:
                        - 1111:2222:3333:4444::2
                  routes:
                    config:
                      - destination: ::/0
                        next-hop-interface: eno1
                        next-hop-address: 1111:2222:3333:4444::1
                        table-id: 254
    ```

    > [!NOTE]
    > Once you have extracted reference CR configuration files from the `out/extra-manifest` directory of the `ztp-site-generate` container, you can use `extraManifests.searchPaths` to include the path to the git directory containing those files. This allows the GitOps ZTP pipeline to apply those CR files during cluster installation. If you configure a `searchPaths` directory, the GitOps ZTP pipeline does not fetch manifests from the `ztp-site-generate` container during site installation.

5.  Generate the Day 0 installation CRs by processing the modified `SiteConfig` CR `site-1-sno.yaml` by running the following command:

    ``` terminal
    $ podman run -it --rm -v `pwd`/out/argocd/example/siteconfig:/resources:Z -v `pwd`/site-install:/output:Z,U registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.17 generator install site-1-sno.yaml /output
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    site-install
    └── site-1-sno
        ├── site-1_agentclusterinstall_example-sno.yaml
        ├── site-1-sno_baremetalhost_example-node1.example.com.yaml
        ├── site-1-sno_clusterdeployment_example-sno.yaml
        ├── site-1-sno_configmap_example-sno.yaml
        ├── site-1-sno_infraenv_example-sno.yaml
        ├── site-1-sno_klusterletaddonconfig_example-sno.yaml
        ├── site-1-sno_machineconfig_02-master-workload-partitioning.yaml
        ├── site-1-sno_machineconfig_predefined-extra-manifests-master.yaml
        ├── site-1-sno_machineconfig_predefined-extra-manifests-worker.yaml
        ├── site-1-sno_managedcluster_example-sno.yaml
        ├── site-1-sno_namespace_example-sno.yaml
        └── site-1-sno_nmstateconfig_example-node1.example.com.yaml
    ```

    </div>

6.  Optional: Generate just the Day 0 `MachineConfig` installation CRs for a particular cluster type by processing the reference `SiteConfig` CR with the `-E` option. For example, run the following commands:

    1.  Create an output folder for the `MachineConfig` CRs:

        ``` terminal
        $ mkdir -p ./site-machineconfig
        ```

    2.  Generate the `MachineConfig` installation CRs:

        ``` terminal
        $ podman run -it --rm -v `pwd`/out/argocd/example/siteconfig:/resources:Z -v `pwd`/site-machineconfig:/output:Z,U registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.17 generator install -E site-1-sno.yaml /output
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        site-machineconfig
        └── site-1-sno
            ├── site-1-sno_machineconfig_02-master-workload-partitioning.yaml
            ├── site-1-sno_machineconfig_predefined-extra-manifests-master.yaml
            └── site-1-sno_machineconfig_predefined-extra-manifests-worker.yaml
        ```

        </div>

7.  Generate and export the Day 2 configuration CRs using the reference `PolicyGenerator` CRs from the previous step. Run the following commands:

    1.  Create an output folder for the Day 2 CRs:

        ``` terminal
        $ mkdir -p ./ref
        ```

    2.  Generate and export the Day 2 configuration CRs:

        ``` terminal
        $ podman run -it --rm -v `pwd`/out/argocd/example/acmpolicygenerator:/resources:Z -v `pwd`/ref:/output:Z,U registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.17 generator config -N . /output
        ```

        The command generates example group and site-specific `PolicyGenerator` CRs for single-node OpenShift, three-node clusters, and standard clusters in the `./ref` folder.

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        ref
         └── customResource
              ├── common
              ├── example-multinode-site
              ├── example-sno
              ├── group-du-3node
              ├── group-du-3node-validator
              │    └── Multiple-validatorCRs
              ├── group-du-sno
              ├── group-du-sno-validator
              ├── group-du-standard
              └── group-du-standard-validator
                   └── Multiple-validatorCRs
        ```

        </div>

8.  Use the generated CRs as the basis for the CRs that you use to install the cluster. You apply the installation CRs to the hub cluster as described in "Installing a single managed cluster". The configuration CRs can be applied to the cluster after cluster installation is complete.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the custom roles and labels are applied after the node is deployed:

  ``` terminal
  $ oc describe node example-node.example.com
  ```

</div>

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
Name:   example-node.example.com
Roles:  control-plane,example-label,master,worker
Labels: beta.kubernetes.io/arch=amd64
        beta.kubernetes.io/os=linux
        custom-label/parameter1=true
        kubernetes.io/arch=amd64
        kubernetes.io/hostname=cnfdf03.telco5gran.eng.rdu2.redhat.com
        kubernetes.io/os=linux
        node-role.kubernetes.io/control-plane=
        node-role.kubernetes.io/example-label=
        node-role.kubernetes.io/master=
        node-role.kubernetes.io/worker=
        node.openshift.io/os_id=rhcos
```

</div>

- The custom label is applied to the node.

<div>

<div class="title">

Additional resources

</div>

- [Workload partitioning](ztp-reference-cluster-configuration-for-vdu.md#ztp-sno-du-enabling-workload-partitioning_sno-configure-for-vdu)

- [BMC addressing](../installing/installing_bare_metal/ipi/ipi-install-installation-workflow.md#bmc-addressing_ipi-install-installation-workflow)

- [About root device hints](../installing/installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.md#root-device-hints_preparing-to-install-with-agent-based-installer)

- [Single-node OpenShift SiteConfig CR installation reference](ztp-deploying-far-edge-sites.md#ztp-sno-siteconfig-config-reference_ztp-deploying-far-edge-sites)

</div>

# Creating the managed bare-metal host secrets

Add the required `Secret` custom resources (CRs) for the managed bare-metal host to the hub cluster. You need a secret for the GitOps Zero Touch Provisioning (ZTP) pipeline to access the Baseboard Management Controller (BMC) and a secret for the assisted installer service to pull cluster installation images from the registry.

> [!NOTE]
> The secrets are referenced from the `SiteConfig` CR by name. The namespace must match the `SiteConfig` namespace.

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML secret file containing credentials for the host Baseboard Management Controller (BMC) and a pull secret required for installing OpenShift and all add-on cluster Operators:

    1.  Save the following YAML as the file `example-sno-secret.yaml`:

        ``` yaml
        apiVersion: v1
        kind: Secret
        metadata:
          name: example-sno-bmc-secret
          namespace: example-sno
        data:
          password: <base64_password>
          username: <base64_username>
        type: Opaque
        ---
        apiVersion: v1
        kind: Secret
        metadata:
          name: pull-secret
          namespace: example-sno
        data:
          .dockerconfigjson: <pull_secret>
        type: kubernetes.io/dockerconfigjson
        ```

        where:

        `namespace`
        Must match the namespace configured in the related `SiteConfig` CR.

        `password`, `username`
        Base64-encoded values for `password` and `username`.

        `.dockerconfigjson`
        Base64-encoded pull secret.

2.  Add the relative path to `example-sno-secret.yaml` to the `kustomization.yaml` file that you use to install the cluster.

</div>

# Configuring Discovery ISO kernel arguments for manual installations using GitOps ZTP

The GitOps Zero Touch Provisioning (ZTP) workflow uses the Discovery ISO as part of the OpenShift Container Platform installation process on managed bare-metal hosts. You can edit the `InfraEnv` resource to specify kernel arguments for the Discovery ISO. This is useful for cluster installations with specific environmental requirements. For example, configure the `rd.net.timeout.carrier` kernel argument for the Discovery ISO to facilitate static networking for the cluster or to receive a DHCP address before downloading the root file system during installation. In OpenShift Container Platform 4.17, you can only add kernel arguments. You can not replace or delete kernel arguments.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (oc).

- You have logged in to the hub cluster as a user with cluster-admin privileges.

- You have manually generated the installation and configuration custom resources (CRs).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `spec.kernelArguments` specification in the `InfraEnv` CR to configure kernel arguments:

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: InfraEnv
    metadata:
      name: <cluster_name>
      namespace: <cluster_name>
    spec:
      kernelArguments:
        - operation: append
          value: audit=0
        - operation: append
          value: trace=1
      clusterRef:
        name: <cluster_name>
        namespace: <cluster_name>
      pullSecretRef:
        name: pull-secret
    ```

    where:

    `operation`
    Specify the `append` operation to add a kernel argument.

    `value`
    Specify the kernel argument you want to configure. This example configures the `audit` kernel argument and the `trace` kernel argument.

    > [!NOTE]
    > The `SiteConfig` CR generates the `InfraEnv` resource as part of the day-0 installation CRs.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

To verify that the kernel arguments are applied, after the Discovery image verifies that OpenShift Container Platform is ready for installation, you can SSH to the target host before the installation process begins. At that point, you can view the kernel arguments for the Discovery ISO in the `/proc/cmdline` file.

</div>

1.  Begin an SSH session with the target host:

    ``` terminal
    $ ssh -i /path/to/privatekey core@<host_name>
    ```

2.  View the system’s kernel arguments by using the following command:

    ``` terminal
    $ cat /proc/cmdline
    ```

# Installing a single managed cluster

You can manually deploy a single managed cluster using the assisted service and Red Hat Advanced Cluster Management (RHACM).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to the hub cluster as a user with `cluster-admin` privileges.

- You have created the baseboard management controller (BMC) `Secret` and the image pull-secret `Secret` custom resources (CRs). See "Creating the managed bare-metal host secrets" for details.

- Your target bare-metal host meets the networking and hardware requirements for managed clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ClusterImageSet` for each specific cluster version to be deployed, for example `clusterImageSet-4.17.yaml`. A `ClusterImageSet` has the following format:

    ``` yaml
    apiVersion: hive.openshift.io/v1
    kind: ClusterImageSet
    metadata:
      name: openshift-4.17.0
    spec:
       releaseImage: quay.io/openshift-release-dev/ocp-release:4.17.0-x86_64
    ```

    where:

    `name`
    The descriptive version that you want to deploy.

    `releaseImage`
    Specifies the `releaseImage` to deploy and determines the operating system image version. The discovery ISO is based on the image version as set by `releaseImage`, or the latest version if the exact version is unavailable.

2.  Apply the `clusterImageSet` CR:

    ``` terminal
    $ oc apply -f clusterImageSet-4.17.yaml
    ```

3.  Create the `Namespace` CR in the `cluster-namespace.yaml` file:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
         name: <cluster_name>
         labels:
            name: <cluster_name>
    ```

    where:

    `name`
    The name of the managed cluster to provision.

4.  Apply the `Namespace` CR by running the following command:

    ``` terminal
    $ oc apply -f cluster-namespace.yaml
    ```

5.  Apply the generated day-0 CRs that you extracted from the `ztp-site-generate` container and customized to meet your requirements:

    ``` terminal
    $ oc apply -R ./site-install/site-sno-1
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Connectivity prerequisites for managed cluster networks](ztp-reference-cluster-configuration-for-vdu.md#ztp-managed-cluster-network-prereqs_sno-configure-for-vdu)

- [Deploying LVM Storage on single-node OpenShift clusters](../storage/persistent_storage_local/persistent-storage-using-lvms.md#lvms-preface-sno-ran_logical-volume-manager-storage)

- [Configuring LVM Storage using PolicyGenerator CRs](policygenerator_for_ztp/ztp-advanced-policygenerator-config.md#ztp-provisioning-lvm-storage_ztp-advanced-policy-config)

</div>

# Monitoring the managed cluster installation status

Ensure that cluster provisioning was successful by checking the cluster status.

<div>

<div class="title">

Prerequisites

</div>

- All of the custom resources have been configured and provisioned, and the `Agent` custom resource is created on the hub for the managed cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check the status of the managed cluster:

    ``` terminal
    $ oc get managedcluster
    ```

    `True` indicates the managed cluster is ready.

2.  Check the agent status:

    ``` terminal
    $ oc get agent -n <cluster_name>
    ```

3.  Use the `describe` command to provide an in-depth description of the agent’s condition. Statuses to be aware of include `BackendError`, `InputError`, `ValidationsFailing`, `InstallationFailed`, and `AgentIsConnected`. These statuses are relevant to the `Agent` and `AgentClusterInstall` custom resources.

    ``` terminal
    $ oc describe agent -n <cluster_name>
    ```

4.  Check the cluster provisioning status:

    ``` terminal
    $ oc get agentclusterinstall -n <cluster_name>
    ```

5.  Use the `describe` command to provide an in-depth description of the cluster provisioning status:

    ``` terminal
    $ oc describe agentclusterinstall -n <cluster_name>
    ```

6.  Check the status of the managed cluster’s add-on services:

    ``` terminal
    $ oc get managedclusteraddon -n <cluster_name>
    ```

7.  Retrieve the authentication information of the `kubeconfig` file for the managed cluster:

    ``` terminal
    $ oc get secret -n <cluster_name> <cluster_name>-admin-kubeconfig -o jsonpath={.data.kubeconfig} | base64 -d > <directory>/<cluster_name>-kubeconfig
    ```

</div>

# Troubleshooting the managed cluster

Use this procedure to diagnose any installation issues that might occur with the managed cluster.

<div>

<div class="title">

Procedure

</div>

1.  Check the status of the managed cluster:

    ``` terminal
    $ oc get managedcluster
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME            HUB ACCEPTED   MANAGED CLUSTER URLS   JOINED   AVAILABLE   AGE
    SNO-cluster     true                                   True     True      2d19h
    ```

    </div>

    If the status in the `AVAILABLE` column is `True`, the managed cluster is being managed by the hub.

    If the status in the `AVAILABLE` column is `Unknown`, the managed cluster is not being managed by the hub. Use the following steps to continue checking to get more information.

2.  Check the `AgentClusterInstall` install status:

    ``` terminal
    $ oc get clusterdeployment -n <cluster_name>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        PLATFORM            REGION   CLUSTERTYPE   INSTALLED    INFRAID    VERSION  POWERSTATE AGE
    Sno0026    agent-baremetal                               false                          Initialized
    2d14h
    ```

    </div>

    If the status in the `INSTALLED` column is `false`, the installation was unsuccessful.

3.  If the installation failed, enter the following command to review the status of the `AgentClusterInstall` resource:

    ``` terminal
    $ oc describe agentclusterinstall -n <cluster_name> <cluster_name>
    ```

4.  Resolve the errors and reset the cluster:

    1.  Remove the cluster’s managed cluster resource:

        ``` terminal
        $ oc delete managedcluster <cluster_name>
        ```

    2.  Remove the cluster’s namespace:

        ``` terminal
        $ oc delete namespace <cluster_name>
        ```

        This deletes all of the namespace-scoped custom resources created for this cluster. You must wait for the `ManagedCluster` CR deletion to complete before proceeding.

    3.  Recreate the custom resources for the managed cluster.

</div>

# RHACM generated cluster installation CRs reference

Red Hat Advanced Cluster Management (RHACM) supports deploying OpenShift Container Platform on single-node clusters, three-node clusters, and standard clusters with a specific set of installation custom resources (CRs) that you generate using `SiteConfig` CRs for each site.

> [!NOTE]
> Every managed cluster has its own namespace, and all of the installation CRs except for `ManagedCluster` and `ClusterImageSet` are under that namespace. `ManagedCluster` and `ClusterImageSet` are cluster-scoped, not namespace-scoped. The namespace and the CR names match the cluster name.

The following table lists the installation CRs that are automatically applied by the RHACM assisted service when it installs clusters using the `SiteConfig` CRs that you configure.

<table>
<caption>Cluster installation CRs generated by RHACM</caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 42%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">CR</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Usage</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>BareMetalHost</code></p></td>
<td style="text-align: left;"><p>Contains the connection information for the Baseboard Management Controller (BMC) of the target bare-metal host.</p></td>
<td style="text-align: left;"><p>Provides access to the BMC to load and start the discovery image on the target server by using the Redfish protocol.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>InfraEnv</code></p></td>
<td style="text-align: left;"><p>Contains information for installing OpenShift Container Platform on the target bare-metal host.</p></td>
<td style="text-align: left;"><p>Used with <code>ClusterDeployment</code> to generate the discovery ISO for the managed cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>AgentClusterInstall</code></p></td>
<td style="text-align: left;"><p>Specifies details of the managed cluster configuration such as networking and the number of control plane nodes. Displays the cluster <code>kubeconfig</code> and credentials when the installation is complete.</p></td>
<td style="text-align: left;"><p>Specifies the managed cluster configuration information and provides status during the installation of the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ClusterDeployment</code></p></td>
<td style="text-align: left;"><p>References the <code>AgentClusterInstall</code> CR to use.</p></td>
<td style="text-align: left;"><p>Used with <code>InfraEnv</code> to generate the discovery ISO for the managed cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>NMStateConfig</code></p></td>
<td style="text-align: left;"><p>Provides network configuration information such as <code>MAC</code> address to <code>IP</code> mapping, DNS server, default route, and other network settings.</p></td>
<td style="text-align: left;"><p>Sets up a static IP address for the managed cluster’s Kube API server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Agent</code></p></td>
<td style="text-align: left;"><p>Contains hardware information about the target bare-metal host.</p></td>
<td style="text-align: left;"><p>Created automatically on the hub when the target machine’s discovery image boots.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ManagedCluster</code></p></td>
<td style="text-align: left;"><p>When a cluster is managed by the hub, it must be imported and known. This Kubernetes object provides that interface.</p></td>
<td style="text-align: left;"><p>The hub uses this resource to manage and show the status of managed clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>KlusterletAddonConfig</code></p></td>
<td style="text-align: left;"><p>Contains the list of services provided by the hub to be deployed to the <code>ManagedCluster</code> resource.</p></td>
<td style="text-align: left;"><p>Tells the hub which addon services to deploy to the <code>ManagedCluster</code> resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Namespace</code></p></td>
<td style="text-align: left;"><p>Logical space for <code>ManagedCluster</code> resources existing on the hub. Unique per site.</p></td>
<td style="text-align: left;"><p>Propagates resources to the <code>ManagedCluster</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>Secret</code></p></td>
<td style="text-align: left;"><p>Two CRs are created: <code>BMC Secret</code> and <code>Image Pull Secret</code>.</p></td>
<td style="text-align: left;"><ul>
<li><p><code>BMC Secret</code> authenticates into the target bare-metal host using its username and password.</p></li>
<li><p><code>Image Pull Secret</code> contains authentication information for the OpenShift Container Platform image installed on the target bare-metal host.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ClusterImageSet</code></p></td>
<td style="text-align: left;"><p>Contains OpenShift Container Platform image information such as the repository and image name.</p></td>
<td style="text-align: left;"><p>Passed into resources to provide OpenShift Container Platform images.</p></td>
</tr>
</tbody>
</table>
