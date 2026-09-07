<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use `ClusterInstance` custom resources (CRs) to deploy custom functionality and configurations in your managed clusters at installation time.

# Customizing extra installation manifests in the GitOps ZTP pipeline

You can define a set of extra manifests for inclusion in the installation phase of the GitOps Zero Touch Provisioning (ZTP) pipeline. These manifests are linked to the `ClusterInstance` custom resources (CRs) and are applied to the cluster during installation. Including `MachineConfig` CRs at install time makes the installation process more efficient.

Extra manifests must be packaged in `ConfigMap` resources and referenced in the `extraManifestsRefs` field of the `ClusterInstance` CR.

<div>

<div class="title">

Prerequisites

</div>

- Create a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a set of extra manifest CRs that the GitOps ZTP pipeline uses to customize the cluster installs.

2.  In your `/clusterinstance` directory, create a subdirectory with your extra manifests. The following example illustrates a sample folder structure:

    ``` text
    clusterinstance/
    ├── site1-sno-du.yaml
    ├── extra-manifest/
    │   ├── 01-example-machine-config.yaml
    │   ├── enable-crun-master.yaml
    │   └── enable-crun-worker.yaml
    └── kustomization.yaml
    ```

3.  Create or update the `kustomization.yaml` file to use `configMapGenerator` to package your extra manifests into a `ConfigMap`:

    ``` yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization
    resources:
      - site1-sno-du.yaml
    configMapGenerator:
      - name: extra-manifests-cm
        namespace: site1-sno-du
        files:
          - extra-manifest/01-example-machine-config.yaml
          - extra-manifest/enable-crun-master.yaml
          - extra-manifest/enable-crun-worker.yaml
    generatorOptions:
      disableNameSuffixHash: true
    ```

    - The `configMapGenerator.namespace` value must match the `ClusterInstance` namespace.

    - Setting `generatorOptions.disableNameSuffixHash` to `true` disables the hash suffix so the `ConfigMap` name is predictable.

4.  In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field:

    ``` yaml
    apiVersion: siteconfig.open-cluster-management.io/v1alpha1
    kind: ClusterInstance
    metadata:
      name: "site1-sno-du"
      namespace: "site1-sno-du"
    spec:
      clusterName: "site1-sno-du"
      networkType: "OVNKubernetes"
      extraManifestsRefs:
        - name: extra-manifests-cm
      # ...
    ```

    - The `extraManifestsRefs` field references the `ConfigMap` containing the extra manifests.

5.  Commit the `ClusterInstance` CR, extra manifest files, and `kustomization.yaml` to your Git repository and push the changes.

    During cluster provisioning, the SiteConfig Operator applies the CRs contained in the referenced `ConfigMap` resources as extra manifests.

    > [!NOTE]
    > You can reference multiple `ConfigMap` resources in `extraManifestsRefs` to organize your manifests logically. For example, you might have separate `ConfigMap` resources for crun configuration, custom `MachineConfig` CRs, and other Day 0 configurations.

</div>

# Configuring cluster network MTU at installation time

You can explicitly set the cluster network maximum transmission unit (MTU) during installation by including a `Network` custom resource (CR) as an extra manifest in the GitOps Zero Touch Provisioning (ZTP) pipeline.

Setting the cluster network MTU with additional headroom during deployment prevents the need for a Day 2 MTU update that requires at least two rolling reboots of all cluster nodes.

During installation, the Cluster Network Operator (CNO) automatically calculates the cluster network MTU based on the primary network interface MTU. When you enable IPsec at installation time, the calculation includes both the OVN-Kubernetes overhead of 100 bytes and the IPsec overhead. If you plan to enable IPsec or another encapsulation technology as a Day 2 operation, the calculated MTU includes only the OVN-Kubernetes overhead and might be insufficient.

By explicitly setting the cluster network MTU at installation time, you can include additional headroom for those future needs and avoid a disruptive MTU migration.

> [!IMPORTANT]
> The cluster network MTU value must be lower than the machine network MTU by at least 100 bytes to account for OVN-Kubernetes overlay overhead. If you plan to enable IPsec as a Day 2 operation, allow an additional 46 bytes for IPsec headroom. For example, with a machine network MTU of `9100` bytes, set the cluster network MTU to `8900` bytes, which accounts for the following offset:
>
> - OVN-Kubernetes overhead: 100 bytes
>
> - IPsec headroom: 46 bytes
>
> - Extra headroom: 54 bytes
>
> - Total offset: 200 bytes
>
> To avoid selecting an MTU value that a node cannot support, verify the maximum MTU (`maxmtu`) that the network interface accepts by running the `ip -d link` command.

<div>

<div class="title">

Prerequisites

</div>

- You have configured the hub cluster to provision managed clusters by using the GitOps ZTP pipeline.

- You have a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for the Argo CD application.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In your `ClusterInstance` CR, set the machine network MTU on the network interface for all nodes.

    The following example configures a VLAN interface with MTU `9100`:

    ``` yaml
    apiVersion: siteconfig.open-cluster-management.io/v1alpha1
    kind: ClusterInstance
    metadata:
      name: "site1-sno-du"
      namespace: "site1-sno-du"
    spec:
      nodes:
        - hostName: "node1.example.com"
          nodeNetwork:
            interfaces:
              - name: "bond0.120"
                macAddress: "00:00:00:00:00:00"
            config:
              interfaces:
                - name: bond0.120
                  type: vlan
                  state: up
                  mtu: 9100
                  ipv4:
                    enabled: true
                    dhcp: false
                    address:
                      - ip: "192.168.120.15"
                        prefix-length: 25
                  vlan:
                    base-iface: bond0
                    id: 120
      # ...
    ```

2.  Create a `Network` CR manifest file named `set-cluster-mtu.yaml` that sets the cluster network MTU:

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: Network
    metadata:
      name: cluster
    spec:
      defaultNetwork:
        ovnKubernetesConfig:
          mtu: 8900
    ```

    where:

    `mtu`
    Specifies the cluster network MTU value. This value must be at least 100 bytes less than the machine network MTU. In this example, the value is 200 bytes less than the machine network MTU of 9100 to allow headroom for IPsec and other future requirements.

3.  In your `clusterinstance` directory, place the manifest file in an extra manifests subdirectory:

    ``` text
    clusterinstance/
    ├── site1-sno-du.yaml
    ├── extra-manifest/
    │   └── set-cluster-mtu.yaml
    └── kustomization.yaml
    ```

4.  Create or update the `kustomization.yaml` file to package the extra manifest into a `ConfigMap`:

    ``` yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization
    resources:
      - site1-sno-du.yaml
    configMapGenerator:
      - name: cluster-mtu-extra-manifests
        namespace: site1-sno-du
        files:
          - extra-manifest/set-cluster-mtu.yaml
    generatorOptions:
      disableNameSuffixHash: true
    ```

5.  In your `ClusterInstance` CR, reference the `ConfigMap` in the `extraManifestsRefs` field:

    ``` yaml
    apiVersion: siteconfig.open-cluster-management.io/v1alpha1
    kind: ClusterInstance
    metadata:
      name: "site1-sno-du"
      namespace: "site1-sno-du"
    spec:
      clusterName: "site1-sno-du"
      networkType: "OVNKubernetes"
      extraManifestsRefs:
        - name: cluster-mtu-extra-manifests
      # ...
    ```

6.  Commit the `ClusterInstance` CR, the `set-cluster-mtu.yaml` manifest, and the `kustomization.yaml` to your Git repository and push the changes.

    During cluster provisioning, the SiteConfig Operator applies the `Network` CR as an extra manifest, and the CNO uses the specified MTU value instead of auto-calculating it.

</div>

<div>

<div class="title">

Verification

</div>

- After the cluster installation is complete, verify the cluster network MTU by running the following command:

  ``` terminal
  $ oc get networks.operator.openshift.io cluster -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` yaml
  apiVersion: operator.openshift.io/v1
  kind: Network
  metadata:
    name: cluster
  # ...
  spec:
    # ...
    defaultNetwork:
      ovnKubernetesConfig:
        # ...
        mtu: 8900
  ```

  </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Customizing extra installation manifests in the GitOps ZTP pipeline](ztp-advanced-install-ztp.md#ztp-customizing-the-install-extra-manifests_ztp-advanced-install-ztp)

</div>

# Deleting a node by using the ClusterInstance CR

By using a `ClusterInstance` custom resource (CR), you can delete and reprovision a node. This method is more efficient than manually deleting the node.

<div>

<div class="title">

Prerequisites

</div>

- You have configured the hub cluster to generate the required installation and policy CRs.

- You have created a Git repository in which you can manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as the source repository for the Argo CD application.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Update the `ClusterInstance` CR to add the `bmac.agent-install.openshift.io/remove-agent-and-node-on-delete=true` annotation to the `BareMetalHost` resource for the node, and push the changes to the Git repository:

    ``` yaml
    apiVersion: siteconfig.open-cluster-management.io/v1alpha1
    kind: ClusterInstance
    metadata:
      name: "example-cluster"
      namespace: "example-cluster"
    spec:
      # ...
      nodes:
        - hostName: "worker-node2.example.com"
          role: "worker"
          extraAnnotations:
            BareMetalHost:
              bmac.agent-install.openshift.io/remove-agent-and-node-on-delete: "true"
    # ...
    ```

2.  Verify that the `BareMetalHost` object is annotated by running the following command:

    ``` terminal
    $ oc get bmh -n <cluster_namespace> <bmh_name> -ojsonpath='' | jq -r '.annotations["bmac.agent-install.openshift.io/remove-agent-and-node-on-delete"]'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    true
    ```

    </div>

3.  Delete the `BareMetalHost` CR by configuring the `pruneManifests` field in the `ClusterInstance` CR to remove the target `BareMetalHost` resource:

    ``` yaml
    apiVersion: siteconfig.open-cluster-management.io/v1alpha1
    kind: ClusterInstance
    metadata:
      name: "example-cluster"
      namespace: "example-cluster"
    spec:
      # ...
      nodes:
        - hostName: "worker-node2.example.com"
          role: "worker"
          pruneManifests:
            - apiVersion: metal3.io/v1alpha1
              kind: BareMetalHost
    # ...
    ```

4.  Push the changes to the Git repository and wait for deprovisioning to start. The status of the `BareMetalHost` CR should change to `deprovisioning`. Wait for the `BareMetalHost` to finish deprovisioning, and be fully deleted.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the `BareMetalHost` and `Agent` CRs for the worker node have been deleted from the hub cluster by running the following commands:

    ``` terminal
    $ oc get bmh -n <cluster_namespace>
    ```

    ``` terminal
    $ oc get agent -n <cluster_namespace>
    ```

2.  Verify that the node record has been deleted from the spoke cluster by running the following command:

    ``` terminal
    $ oc get nodes
    ```

    > [!NOTE]
    > If you are working with secrets, deleting a secret too early can cause an issue because ArgoCD needs the secret to complete resynchronization after deletion. Delete the secret only after the node cleanup, when the current ArgoCD synchronization is complete.

3.  After the `BareMetalHost` object is successfully deleted, remove the worker node definition from the `spec.nodes` section in the `ClusterInstance` CR and push the changes to the Git repository.

</div>

<div class="formalpara">

<div class="title">

Next steps

</div>

To reprovision a node, add the node definition back to the `spec.nodes` section in the `ClusterInstance` CR, push the changes to the Git repository, and wait for the synchronization to complete. This regenerates the `BareMetalHost` CR of the worker node and triggers the re-install of the node.

</div>
