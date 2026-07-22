<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the Lifecycle Agent to generate the seed image with the `SeedGenerator` custom resource (CR).

# Seed image configuration

The seed image targets a set of single-node OpenShift clusters with the same hardware and similar configuration. This means that the seed image must have all of the components and configuration that the seed cluster shares with the target clusters. Therefore, the seed image generated from the seed cluster cannot contain any cluster-specific configuration.

The following table lists the components, resources, and configurations that you must and must not include in your seed image:

<table>
<caption>Seed image configuration</caption>
<colgroup>
<col style="width: 66%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Cluster configuration</th>
<th style="text-align: left;">Include in seed image</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Performance profile</p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>MachineConfig</code> resources for the target cluster</p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>IP version configuration, either IPv4, IPv6, or dual-stack networking</p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Set of Day 2 Operators, including the Lifecycle Agent and the OADP Operator</p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Disconnected registry configuration <sup>[2]</sup></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Valid proxy configuration <sup>[3]</sup></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>FIPS configuration</p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Dedicated partition on the primary disk for container storage that matches the size of the target clusters</p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Local volumes</p>
<ul>
<li><p><code>StorageClass</code> used in <code>LocalVolume</code> for LSO</p></li>
<li><p><code>LocalVolume</code> for LSO</p></li>
<li><p><code>LVMCluster</code> CR for LVMS</p></li>
</ul></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>OADP <code>DataProtectionApplication</code> CR</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
</tbody>
</table>

1.  If the seed cluster is installed in a disconnected environment, the target clusters must also be installed in a disconnected environment.

2.  The proxy configuration must be either enabled or disabled in both the seed and target clusters. However, the proxy servers configured on the clusters does not have to match.

## Seed image configuration using the RAN DU profile

The following table lists the components, resources, and configurations that you must and must not include in the seed image when using the RAN DU profile:

| Resource | Include in seed image |
|----|----|
| All extra manifests that are applied as part of Day 0 installation | Yes |
| All Day 2 Operator subscriptions | Yes |
| `DisableOLMPprof.yaml` | Yes |
| `TunedPerformancePatch.yaml` | Yes |
| `PerformanceProfile.yaml` | Yes |
| `SriovOperatorConfig.yaml` | Yes |
| `DisableSnoNetworkDiag.yaml` | Yes |
| `StorageClass.yaml` | No, if it is used in `StorageLV.yaml` |
| `StorageLV.yaml` | No |
| `StorageLVMCluster.yaml` | No |
| `SriovFecClusterConfig.yaml` | No |
| `SriovVrbClusterConfig.yaml` | No |

Seed image configuration with RAN DU profile

<table style="width:80%;">
<caption>Seed image configuration with RAN DU profile for extra manifests</caption>
<colgroup>
<col style="width: 40%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Resource</th>
<th style="text-align: left;">Apply as extra manifest</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>ClusterLogForwarder.yaml</code></p></td>
<td style="text-align: left;"><p>Yes</p>
<div class="note">
<div class="title">
&#10;</div>
<p>The DU profile includes the Cluster Logging Operator, but the profile does not configure or apply any Cluster Logging Operator CRs. To enable log forwarding, include the <code>ClusterLogForwarder.yaml</code> CR as an extra manifest. The extra manifest is applied to the target single-node OpenShift cluster during the image-based upgrade process.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ReduceMonitoringFootprint.yaml</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>PtpOperatorConfigForEvent.yaml</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>DefaultCatsrc.yaml</code></p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>PtpConfig.yaml</code></p></td>
<td style="text-align: left;"><p>If the interfaces of the target cluster are common with the seed cluster, you can include them in the seed image. Otherwise, apply it as extra manifests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>SriovNetwork.yaml</code> <code>SriovNetworkNodePolicy.yaml</code></p></td>
<td style="text-align: left;"><p>If the configuration, including namespaces, is exactly the same on both the seed and target cluster, you can include them in the seed image. Otherwise, apply them as extra manifests.</p></td>
</tr>
</tbody>
</table>

# Generating a seed image with the Lifecycle Agent

Use the Lifecycle Agent to generate a seed image from a managed cluster. The Operator checks for required system configurations, performs any necessary system cleanup before generating the seed image, and launches the image generation. The seed image generation includes the following tasks:

- Stopping cluster Operators

- Preparing the seed image configuration

- Generating and pushing the seed image to the image repository specified in the `SeedGenerator` CR

- Restoring cluster Operators

- Expiring seed cluster certificates

- Generating new certificates for the seed cluster

- Restoring and updating the `SeedGenerator` CR on the seed cluster

<div>

<div class="title">

Prerequisites

</div>

- RHACM and multicluster engine for Kubernetes Operator are not installed on the seed cluster.

- You have configured a shared container directory on the seed cluster.

- You have installed the minimum version of the OADP Operator and the Lifecycle Agent on the seed cluster.

- Ensure that persistent volumes are not configured on the seed cluster.

- Ensure that the `LocalVolume` CR does not exist on the seed cluster if the Local Storage Operator is used.

- Ensure that the `LVMCluster` CR does not exist on the seed cluster if LVM Storage is used.

- Ensure that the `DataProtectionApplication` CR does not exist on the seed cluster if OADP is used.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Detach the managed cluster from the hub to delete any RHACM-specific resources from the seed cluster that must not be in the seed image:

    1.  Manually detach the seed cluster by running the following command:

        ``` terminal
        $ oc delete managedcluster sno-worker-example
        ```

        1.  Wait until the managed cluster is removed. After the cluster is removed, create the proper `SeedGenerator` CR. The Lifecycle Agent cleans up the RHACM artifacts.

    2.  If you are using GitOps ZTP, detach your cluster by removing the seed cluster’s `SiteConfig` CR from the `kustomization.yaml`.

        1.  If you have a `kustomization.yaml` file that references multiple `SiteConfig` CRs, remove your seed cluster’s `SiteConfig` CR from the `kustomization.yaml`:

            ``` yaml
            apiVersion: kustomize.config.k8s.io/v1beta1
            kind: Kustomization

            generators:
            #- example-seed-sno1.yaml
            - example-target-sno2.yaml
            - example-target-sno3.yaml
            ```

        2.  If you have a `kustomization.yaml` that references one `SiteConfig` CR, remove your seed cluster’s `SiteConfig` CR from the `kustomization.yaml` and add the `generators: {}` line:

            ``` yaml
            apiVersion: kustomize.config.k8s.io/v1beta1
            kind: Kustomization

            generators: {}
            ```

        3.  Commit the `kustomization.yaml` changes in your Git repository and push the changes to your repository.

            The ArgoCD pipeline detects the changes and removes the managed cluster.

2.  Create the `Secret` object so that you can push the seed image to your registry.

    1.  Create the authentication file by running the following commands:

        ``` terminal
        $ MY_USER=myuserid
        ```

        ``` terminal
        $ AUTHFILE=/tmp/my-auth.json
        ```

        ``` terminal
        $ podman login --authfile ${AUTHFILE} -u ${MY_USER} quay.io/${MY_USER}
        ```

        ``` terminal
        $ base64 -w 0 ${AUTHFILE} ; echo
        ```

    2.  Copy the output into the `seedAuth` field in the `Secret` YAML file named `seedgen` in the `openshift-lifecycle-agent` namespace:

        ``` yaml
        apiVersion: v1
        kind: Secret
        metadata:
          name: <secret_name>
          namespace: openshift-lifecycle-agent
        type: Opaque
        data:
          seedAuth: <encoded_authfile>
        ```

        where:

        `<secret_name>`
        Specifies the name of the `Secret` resource. The value must be `seedgen`.

        `<encoded_authfile>`
        Specifies a base64-encoded authfile for write-access to the registry for pushing the generated seed images.

    3.  Apply the `Secret` by running the following command:

        ``` terminal
        $ oc apply -f secretseedgenerator.yaml
        ```

3.  Create the `SeedGenerator` CR:

    ``` yaml
    apiVersion: lca.openshift.io/v1
    kind: SeedGenerator
    metadata:
      name: <seedgenerator_name>
    spec:
      seedImage: <seed_container_image>
    ```

    where:

    `<seedgenerator_name>`
    Specifies the name of the `SeedGenerator` CR. The value must be `seedimage`.

    `<seed_container_image>`
    Specifies the container image URL, for example, `quay.io/example/seed-container-image:<tag>`. It is recommended to use the `<seed_cluster_name>:<ocp_version>` format.

4.  Generate the seed image by running the following command:

    ``` terminal
    $ oc apply -f seedgenerator.yaml
    ```

    > [!IMPORTANT]
    > The cluster reboots and loses API capabilities while the Lifecycle Agent generates the seed image. Applying the `SeedGenerator` CR stops the `kubelet` and the CRI-O operations, then it starts the image generation.

</div>

<div>

<div class="title">

Verification

</div>

- After the cluster recovers and it is available, you can check the status of the `SeedGenerator` CR by running the following command:

  ``` terminal
  $ oc get seedgenerator -o yaml
  ```

  The following example shows the output when the seed image generation is complete:

  ``` yaml
  status:
    conditions:
    - lastTransitionTime: "2024-02-13T21:24:26Z"
      message: Seed Generation completed
      observedGeneration: 1
      reason: Completed
      status: "False"
      type: SeedGenInProgress
    - lastTransitionTime: "2024-02-13T21:24:26Z"
      message: Seed Generation completed
      observedGeneration: 1
      reason: Completed
      status: "True"
      type: SeedGenCompleted
    observedGeneration: 1
  ```

  The `SeedGenCompleted` type indicates that the seed image generation is complete.

  If you want to generate more seed images, you must provision a new seed cluster with the version that you want to generate a seed image from.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring a shared container partition between ostree stateroots](cnf-image-based-upgrade-shared-container-partition.md#cnf-image-based-upgrade-shared-container-partition_shared-container-partition)

- [Configuring a shared container partition between ostree stateroots when using GitOps ZTP](cnf-image-based-upgrade-shared-container-partition.md#ztp-image-based-upgrade-shared-container-partition_shared-container-partition)

</div>
