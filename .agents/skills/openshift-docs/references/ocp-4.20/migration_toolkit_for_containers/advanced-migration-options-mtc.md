<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can automate your migrations and modify the `MigPlan` and `MigrationController` custom resources in order to perform large-scale migrations and to improve performance.

# Terminology

<table>
<caption>MTC terminology</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Term</th>
<th style="text-align: left;">Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Source cluster</p></td>
<td style="text-align: left;"><p>Cluster from which the applications are migrated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Destination cluster<sup>[1]</sup></p></td>
<td style="text-align: left;"><p>Cluster to which the applications are migrated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Replication repository</p></td>
<td style="text-align: left;"><p>Object storage used for copying images, volumes, and Kubernetes objects during indirect migration or for Kubernetes objects during direct volume migration or direct image migration.</p>
<p>The replication repository must be accessible to all clusters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Host cluster</p></td>
<td style="text-align: left;"><p>Cluster on which the <code>migration-controller</code> pod and the web console are running. The host cluster is usually the destination cluster but this is not required.</p>
<p>The host cluster does not require an exposed registry route for direct image migration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Remote cluster</p></td>
<td style="text-align: left;"><p>A remote cluster is usually the source cluster but this is not required.</p>
<p>A remote cluster requires a <code>Secret</code> custom resource that contains the <code>migration-controller</code> service account token.</p>
<p>A remote cluster requires an exposed secure registry route for direct image migration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Indirect migration</p></td>
<td style="text-align: left;"><p>Images, volumes, and Kubernetes objects are copied from the source cluster to the replication repository and then from the replication repository to the destination cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Direct volume migration</p></td>
<td style="text-align: left;"><p>Persistent volumes are copied directly from the source cluster to the destination cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Direct image migration</p></td>
<td style="text-align: left;"><p>Images are copied directly from the source cluster to the destination cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Stage migration</p></td>
<td style="text-align: left;"><p>Data is copied to the destination cluster without stopping the application.</p>
<p>Running a stage migration multiple times reduces the duration of the cutover migration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Cutover migration</p></td>
<td style="text-align: left;"><p>The application is stopped on the source cluster and its resources are migrated to the destination cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>State migration</p></td>
<td style="text-align: left;"><p>Application state is migrated by copying specific persistent volume claims to the destination cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Rollback migration</p></td>
<td style="text-align: left;"><p>Rollback migration rolls back a completed migration.</p></td>
</tr>
</tbody>
</table>

<sup>1</sup> Called the *target* cluster in the MTC web console.

# Migrating applications by using the command line

You can migrate applications with the MTC API by using the command-line interface (CLI) in order to automate the migration.

## Migration prerequisites

- You must be logged in as a user with `cluster-admin` privileges on all clusters.

<div>

<div class="title">

Direct image migration

</div>

- You must ensure that the secure OpenShift image registry of the source cluster is exposed.

- You must create a route to the exposed registry.

</div>

<div>

<div class="title">

Direct volume migration

</div>

- If your clusters use proxies, you must configure an Stunnel TCP proxy.

</div>

<div>

<div class="title">

Clusters

</div>

- The source cluster must be upgraded to the latest MTC z-stream release.

- The MTC version must be the same on all clusters.

</div>

<div>

<div class="title">

Network

</div>

- The clusters have unrestricted network access to each other and to the replication repository.

- If you copy the persistent volumes with `move`, the clusters must have unrestricted network access to the remote volumes.

- You must enable the following ports on an OpenShift Container Platform 4 cluster:

  - `6443` (API server)

  - `443` (routes)

  - `53` (DNS)

- You must enable port `443` on the replication repository if you are using TLS.

</div>

<div>

<div class="title">

Persistent volumes (PVs)

</div>

- The PVs must be valid.

- The PVs must be bound to persistent volume claims.

- If you use snapshots to copy the PVs, the following additional prerequisites apply:

  - The cloud provider must support snapshots.

  - The PVs must have the same cloud provider.

  - The PVs must be located in the same geographic region.

  - The PVs must have the same storage class.

</div>

## Creating a registry route for direct image migration

For direct image migration, you must create a route to the exposed OpenShift image registry on all remote clusters.

<div>

<div class="title">

Prerequisites

</div>

- The OpenShift image registry must be exposed to external traffic on all remote clusters.

  The OpenShift Container Platform 4 registry is exposed by default.

</div>

<div>

<div class="title">

Procedure

</div>

- To create a route to an OpenShift Container Platform 4 registry, run the following command:

  ``` terminal
  $ oc create route passthrough --service=image-registry -n openshift-image-registry
  ```

</div>

## Proxy configuration

For OpenShift Container Platform 4.1 and earlier versions, you must configure proxies in the `MigrationController` custom resource (CR) manifest after you install the Migration Toolkit for Containers Operator because these versions do not support a cluster-wide `proxy` object.

For OpenShift Container Platform 4.2 to 4.17, the MTC inherits the cluster-wide proxy settings. You can change the proxy parameters if you want to override the cluster-wide proxy settings.

### Direct volume migration

Direct Volume Migration (DVM) was introduced in MTC 1.4.2. DVM supports only one proxy. The source cluster cannot access the route of the target cluster if the target cluster is also behind a proxy.

If you want to perform a DVM from a source cluster behind a proxy, you must configure a TCP proxy that works at the transport layer and forwards the SSL connections transparently without decrypting and re-encrypting them with their own SSL certificates. A Stunnel proxy is an example of such a proxy.

#### TCP proxy setup for DVM

You can set up a direct connection between the source and the target cluster through a TCP proxy and configure the `stunnel_tcp_proxy` variable in the `MigrationController` CR to use the proxy:

``` yaml
apiVersion: migration.openshift.io/v1alpha1
kind: MigrationController
metadata:
  name: migration-controller
  namespace: openshift-migration
spec:
  [...]
  stunnel_tcp_proxy: http://username:password@ip:port
```

Direct volume migration (DVM) supports only basic authentication for the proxy. Moreover, DVM works only from behind proxies that can tunnel a TCP connection transparently. HTTP/HTTPS proxies in man-in-the-middle mode do not work. The existing cluster-wide proxies might not support this behavior. As a result, the proxy settings for DVM are intentionally kept different from the usual proxy configuration in MTC.

#### Why use a TCP proxy instead of an HTTP/HTTPS proxy?

You can enable DVM by running Rsync between the source and the target cluster over an OpenShift route. Traffic is encrypted using Stunnel, a TCP proxy. The Stunnel running on the source cluster initiates a TLS connection with the target Stunnel and transfers data over an encrypted channel.

Cluster-wide HTTP/HTTPS proxies in OpenShift are usually configured in man-in-the-middle mode where they negotiate their own TLS session with the outside servers. However, this does not work with Stunnel. Stunnel requires that its TLS session be untouched by the proxy, essentially making the proxy a transparent tunnel which simply forwards the TCP connection as-is. Therefore, you must use a TCP proxy.

#### Known issue

<div class="formalpara">

<div class="title">

Migration fails with error `Upgrade request required`

</div>

The migration Controller uses the SPDY protocol to execute commands within remote pods. If the remote cluster is behind a proxy or a firewall that does not support the SPDY protocol, the migration controller fails to execute remote commands. The migration fails with the error message `Upgrade request required`. Workaround: Use a proxy that supports the SPDY protocol.

</div>

In addition to supporting the SPDY protocol, the proxy or firewall also must pass the `Upgrade` HTTP header to the API server. The client uses this header to open a websocket connection with the API server. If the `Upgrade` header is blocked by the proxy or firewall, the migration fails with the error message `Upgrade request required`. Workaround: Ensure that the proxy forwards the `Upgrade` header.

### Tuning network policies for migrations

OpenShift supports restricting traffic to or from pods using *NetworkPolicy* or *EgressFirewalls* based on the network plugin used by the cluster. If any of the source namespaces involved in a migration use such mechanisms to restrict network traffic to pods, the restrictions might inadvertently stop traffic to Rsync pods during migration.

Rsync pods running on both the source and the target clusters must connect to each other over an OpenShift Route. Existing *NetworkPolicy* or *EgressNetworkPolicy* objects can be configured to automatically exempt Rsync pods from these traffic restrictions.

#### NetworkPolicy configuration

##### Egress traffic from Rsync pods

You can use the unique labels of Rsync pods to allow egress traffic to pass from them if the `NetworkPolicy` configuration in the source or destination namespaces blocks this type of traffic. The following policy allows **all** egress traffic from Rsync pods in the namespace:

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-all-egress-from-rsync-pods
spec:
  podSelector:
    matchLabels:
      owner: directvolumemigration
      app: directvolumemigration-rsync-transfer
  egress:
  - {}
  policyTypes:
  - Egress
```

##### Ingress traffic to Rsync pods

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-all-egress-from-rsync-pods
spec:
  podSelector:
    matchLabels:
      owner: directvolumemigration
      app: directvolumemigration-rsync-transfer
  ingress:
  - {}
  policyTypes:
  - Ingress
```

#### EgressNetworkPolicy configuration

The `EgressNetworkPolicy` object or *Egress Firewalls* are OpenShift constructs designed to block egress traffic leaving the cluster.

Unlike the `NetworkPolicy` object, the Egress Firewall works at a project level because it applies to all pods in the namespace. Therefore, the unique labels of Rsync pods do not exempt only Rsync pods from the restrictions. However, you can add the CIDR ranges of the source or target cluster to the *Allow* rule of the policy so that a direct connection can be setup between two clusters.

Based on which cluster the Egress Firewall is present in, you can add the CIDR range of the other cluster to allow egress traffic between the two:

``` yaml
apiVersion: network.openshift.io/v1
kind: EgressNetworkPolicy
metadata:
  name: test-egress-policy
  namespace: <namespace>
spec:
  egress:
  - to:
      cidrSelector: <cidr_of_source_or_target_cluster>
    type: Deny
```

#### Choosing alternate endpoints for data transfer

By default, DVM uses an OpenShift Container Platform route as an endpoint to transfer PV data to destination clusters. You can choose another type of supported endpoint, if cluster topologies allow.

For each cluster, you can configure an endpoint by setting the `rsync_endpoint_type` variable on the appropriate **destination** cluster in your `MigrationController` CR:

``` yaml
apiVersion: migration.openshift.io/v1alpha1
kind: MigrationController
metadata:
  name: migration-controller
  namespace: openshift-migration
spec:
  [...]
  rsync_endpoint_type: [NodePort|ClusterIP|Route]
```

#### Configuring supplemental groups for Rsync pods

When your PVCs use a shared storage, you can configure the access to that storage by adding supplemental groups to Rsync pod definitions in order for the pods to allow access:

| Variable | Type | Default | Description |
|----|----|----|----|
| `src_supplemental_groups` | string | Not set | Comma-separated list of supplemental groups for source Rsync pods |
| `target_supplemental_groups` | string | Not set | Comma-separated list of supplemental groups for target Rsync pods |

Supplementary groups for Rsync pods

<div class="formalpara">

<div class="title">

Example usage

</div>

The `MigrationController` CR can be updated to set values for these supplemental groups:

</div>

``` yaml
spec:
  src_supplemental_groups: "1000,2000"
  target_supplemental_groups: "2000,3000"
```

### Configuring proxies

<div>

<div class="title">

Prerequisites

</div>

- You must be logged in as a user with `cluster-admin` privileges on all clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the `MigrationController` CR manifest:

    ``` terminal
    $ oc get migrationcontroller <migration_controller> -n openshift-migration
    ```

2.  Update the proxy parameters:

    ``` yaml
    apiVersion: migration.openshift.io/v1alpha1
    kind: MigrationController
    metadata:
      name: <migration_controller>
      namespace: openshift-migration
    ...
    spec:
      stunnel_tcp_proxy: http://<username>:<password>@<ip>:<port>
      noProxy: example.com
    ```

    - Stunnel proxy URL for direct volume migration.

    - Comma-separated list of destination domain names, domains, IP addresses, or other network CIDRs to exclude proxying.

      Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass proxy for all destinations. If you scale up workers that are not included in the network defined by the `networking.machineNetwork[].cidr` field from the installation configuration, you must add them to this list to prevent connection issues.

      This field is ignored if neither the `httpProxy` nor the `httpsProxy` field is set.

3.  Save the manifest as `migration-controller.yaml`.

4.  Apply the updated manifest:

    ``` terminal
    $ oc replace -f migration-controller.yaml -n openshift-migration
    ```

</div>

## Migrating an application by using the MTC API

You can migrate an application from the command line by using the Migration Toolkit for Containers (MTC) API.

<div>

<div class="title">

Procedure

</div>

1.  Create a `MigCluster` CR manifest for the host cluster:

    ``` yaml
    $ cat << EOF | oc apply -f -
    apiVersion: migration.openshift.io/v1alpha1
    kind: MigCluster
    metadata:
      name: <host_cluster>
      namespace: openshift-migration
    spec:
      isHostCluster: true
    EOF
    ```

2.  Create a `Secret` object manifest for each remote cluster:

    ``` yaml
    $ cat << EOF | oc apply -f -
    apiVersion: v1
    kind: Secret
    metadata:
      name: <cluster_secret>
      namespace: openshift-config
    type: Opaque
    data:
      saToken: <sa_token>
    EOF
    ```

    - Specify the base64-encoded `migration-controller` service account (SA) token of the remote cluster. You can obtain the token by running the following command:

      ``` terminal
      $ oc sa get-token migration-controller -n openshift-migration | base64 -w 0
      ```

3.  Create a `MigCluster` CR manifest for each remote cluster:

    ``` yaml
    $ cat << EOF | oc apply -f -
    apiVersion: migration.openshift.io/v1alpha1
    kind: MigCluster
    metadata:
      name: <remote_cluster>
      namespace: openshift-migration
    spec:
      exposedRegistryPath: <exposed_registry_route>
      insecure: false
      isHostCluster: false
      serviceAccountSecretRef:
        name: <remote_cluster_secret>
        namespace: openshift-config
      url: <remote_cluster_url>
    EOF
    ```

    - Specify the `Cluster` CR of the remote cluster.

    - Optional: For direct image migration, specify the exposed registry route.

    - SSL verification is enabled if `false`. CA certificates are not required or checked if `true`.

    - Specify the `Secret` object of the remote cluster.

    - Specify the URL of the remote cluster.

4.  Verify that all clusters are in a `Ready` state:

    ``` terminal
    $ oc describe MigCluster <cluster>
    ```

5.  Create a `Secret` object manifest for the replication repository:

    ``` yaml
    $ cat << EOF | oc apply -f -
    apiVersion: v1
    kind: Secret
    metadata:
      namespace: openshift-config
      name: <migstorage_creds>
    type: Opaque
    data:
      aws-access-key-id: <key_id_base64>
      aws-secret-access-key: <secret_key_base64>
    EOF
    ```

    - Specify the key ID in base64 format.

    - Specify the secret key in base64 format.

      AWS credentials are base64-encoded by default. For other storage providers, you must encode your credentials by running the following command with each key:

      ``` terminal
      $ echo -n "<key>" | base64 -w 0
      ```

    - Specify the key ID or the secret key. Both keys must be base64-encoded.

6.  Create a `MigStorage` CR manifest for the replication repository:

    ``` yaml
    $ cat << EOF | oc apply -f -
    apiVersion: migration.openshift.io/v1alpha1
    kind: MigStorage
    metadata:
      name: <migstorage>
      namespace: openshift-migration
    spec:
      backupStorageConfig:
        awsBucketName: <bucket>
        credsSecretRef:
          name: <storage_secret>
          namespace: openshift-config
      backupStorageProvider: <storage_provider>
      volumeSnapshotConfig:
        credsSecretRef:
          name: <storage_secret>
          namespace: openshift-config
      volumeSnapshotProvider: <storage_provider>
    EOF
    ```

    - Specify the bucket name.

    - Specify the `Secrets` CR of the object storage. You must ensure that the credentials stored in the `Secrets` CR of the object storage are correct.

    - Specify the storage provider.

    - Optional: If you are copying data by using snapshots, specify the `Secrets` CR of the object storage. You must ensure that the credentials stored in the `Secrets` CR of the object storage are correct.

    - Optional: If you are copying data by using snapshots, specify the storage provider.

7.  Verify that the `MigStorage` CR is in a `Ready` state:

    ``` terminal
    $ oc describe migstorage <migstorage>
    ```

8.  Create a `MigPlan` CR manifest:

    ``` yaml
    $ cat << EOF | oc apply -f -
    apiVersion: migration.openshift.io/v1alpha1
    kind: MigPlan
    metadata:
      name: <migplan>
      namespace: openshift-migration
    spec:
      destMigClusterRef:
        name: <host_cluster>
        namespace: openshift-migration
      indirectImageMigration: true
      indirectVolumeMigration: true
      migStorageRef:
        name: <migstorage>
        namespace: openshift-migration
      namespaces:
        - <source_namespace_1>
        - <source_namespace_2>
        - <source_namespace_3>:<destination_namespace>
      srcMigClusterRef:
        name: <remote_cluster>
        namespace: openshift-migration
    EOF
    ```

    - Direct image migration is enabled if `false`.

    - Direct volume migration is enabled if `false`.

    - Specify the name of the `MigStorage` CR instance.

    - Specify one or more source namespaces. By default, the destination namespace has the same name.

    - Specify a destination namespace if it is different from the source namespace.

    - Specify the name of the source cluster `MigCluster` instance.

9.  Verify that the `MigPlan` instance is in a `Ready` state:

    ``` terminal
    $ oc describe migplan <migplan> -n openshift-migration
    ```

10. Create a `MigMigration` CR manifest to start the migration defined in the `MigPlan` instance:

    ``` yaml
    $ cat << EOF | oc apply -f -
    apiVersion: migration.openshift.io/v1alpha1
    kind: MigMigration
    metadata:
      name: <migmigration>
      namespace: openshift-migration
    spec:
      migPlanRef:
        name: <migplan>
        namespace: openshift-migration
      quiescePods: true
      stage: false
      rollback: false
    EOF
    ```

    - Specify the `MigPlan` CR name.

    - The pods on the source cluster are stopped before migration if `true`.

    - A stage migration, which copies most of the data without stopping the application, is performed if `true`.

    - A completed migration is rolled back if `true`.

11. Verify the migration by watching the `MigMigration` CR progress:

    ``` terminal
    $ oc watch migmigration <migmigration> -n openshift-migration
    ```

    The output resembles the following:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    Name:         c8b034c0-6567-11eb-9a4f-0bc004db0fbc
    Namespace:    openshift-migration
    Labels:       migration.openshift.io/migplan-name=django
    Annotations:  openshift.io/touch: e99f9083-6567-11eb-8420-0a580a81020c
    API Version:  migration.openshift.io/v1alpha1
    Kind:         MigMigration
    ...
    Spec:
      Mig Plan Ref:
        Name:       migplan
        Namespace:  openshift-migration
      Stage:        false
    Status:
      Conditions:
        Category:              Advisory
        Last Transition Time:  2021-02-02T15:04:09Z
        Message:               Step: 19/47
        Reason:                InitialBackupCreated
        Status:                True
        Type:                  Running
        Category:              Required
        Last Transition Time:  2021-02-02T15:03:19Z
        Message:               The migration is ready.
        Status:                True
        Type:                  Ready
        Category:              Required
        Durable:               true
        Last Transition Time:  2021-02-02T15:04:05Z
        Message:               The migration registries are healthy.
        Status:                True
        Type:                  RegistriesHealthy
      Itinerary:               Final
      Observed Digest:         7fae9d21f15979c71ddc7dd075cb97061895caac5b936d92fae967019ab616d5
      Phase:                   InitialBackupCreated
      Pipeline:
        Completed:  2021-02-02T15:04:07Z
        Message:    Completed
        Name:       Prepare
        Started:    2021-02-02T15:03:18Z
        Message:    Waiting for initial Velero backup to complete.
        Name:       Backup
        Phase:      InitialBackupCreated
        Progress:
          Backup openshift-migration/c8b034c0-6567-11eb-9a4f-0bc004db0fbc-wpc44: 0 out of estimated total of 0 objects backed up (5s)
        Started:        2021-02-02T15:04:07Z
        Message:        Not started
        Name:           StageBackup
        Message:        Not started
        Name:           StageRestore
        Message:        Not started
        Name:           DirectImage
        Message:        Not started
        Name:           DirectVolume
        Message:        Not started
        Name:           Restore
        Message:        Not started
        Name:           Cleanup
      Start Timestamp:  2021-02-02T15:03:18Z
    Events:
      Type    Reason   Age                 From                     Message
      ----    ------   ----                ----                     -------
      Normal  Running  57s                 migmigration_controller  Step: 2/47
      Normal  Running  57s                 migmigration_controller  Step: 3/47
      Normal  Running  57s (x3 over 57s)   migmigration_controller  Step: 4/47
      Normal  Running  54s                 migmigration_controller  Step: 5/47
      Normal  Running  54s                 migmigration_controller  Step: 6/47
      Normal  Running  52s (x2 over 53s)   migmigration_controller  Step: 7/47
      Normal  Running  51s (x2 over 51s)   migmigration_controller  Step: 8/47
      Normal  Ready    50s (x12 over 57s)  migmigration_controller  The migration is ready.
      Normal  Running  50s                 migmigration_controller  Step: 9/47
      Normal  Running  50s                 migmigration_controller  Step: 10/47
    ```

    </div>

</div>

## State migration

You can perform repeatable, state-only migrations by using Migration Toolkit for Containers (MTC) to migrate persistent volume claims (PVCs) that constitute an application’s state. You migrate specified PVCs by excluding other PVCs from the migration plan. You can map the PVCs to ensure that the source and the target PVCs are synchronized. Persistent volume (PV) data is copied to the target cluster. The PV references are not moved, and the application pods continue to run on the source cluster.

State migration is specifically designed to be used in conjunction with external CD mechanisms, such as OpenShift Gitops. You can migrate application manifests using GitOps while migrating the state using MTC.

If you have a CI/CD pipeline, you can migrate stateless components by deploying them on the target cluster. Then you can migrate stateful components by using MTC.

You can perform a state migration between clusters or within the same cluster.

> [!IMPORTANT]
> State migration migrates only the components that constitute an application’s state. If you want to migrate an entire namespace, use stage or cutover migration.

<div>

<div class="title">

Prerequisites

</div>

- The state of the application on the source cluster is persisted in `PersistentVolumes` provisioned through `PersistentVolumeClaims`.

- The manifests of the application are available in a central repository that is accessible from both the source and the target clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Migrate persistent volume data from the source to the target cluster.

    You can perform this step as many times as needed. The source application continues running.

2.  Quiesce the source application.

    You can do this by setting the replicas of workload resources to `0`, either directly on the source cluster or by updating the manifests in GitHub and re-syncing the Argo CD application.

3.  Clone application manifests to the target cluster.

    You can use Argo CD to clone the application manifests to the target cluster.

4.  Migrate the remaining volume data from the source to the target cluster.

    Migrate any new data created by the application during the state migration process by performing a final data migration.

5.  If the cloned application is in a quiesced state, unquiesce it.

6.  Switch the DNS record to the target cluster to re-direct user traffic to the migrated application.

</div>

> [!NOTE]
> MTC 1.6 cannot quiesce applications automatically when performing state migration. It can only migrate PV data. Therefore, you must use your CD mechanisms for quiescing or unquiescing applications.
>
> MTC 1.7 introduces explicit Stage and Cutover flows. You can use staging to perform initial data transfers as many times as needed. Then you can perform a cutover, in which the source applications are quiesced automatically.

## Additional resources

- See [Excluding PVCs from migration](advanced-migration-options-mtc.md#migration-excluding-pvcs_advanced-migration-options-mtc) to select PVCs for state migration.

- See [Mapping PVCs](advanced-migration-options-mtc.md#migration-mapping-pvcs_advanced-migration-options-mtc) to migrate source PV data to provisioned PVCs on the destination cluster.

- See [Migrating Kubernetes objects](advanced-migration-options-mtc.md#migration-kubernetes-objects_advanced-migration-options-mtc) to migrate the Kubernetes objects that constitute an application’s state.

# Migration hooks

You can add up to four migration hooks to a single migration plan, with each hook running at a different phase of the migration. Migration hooks perform tasks such as customizing application quiescence, manually migrating unsupported data types, and updating applications after migration.

A migration hook runs on a source or a target cluster at one of the following migration steps:

- `PreBackup`: Before resources are backed up on the source cluster.

- `PostBackup`: After resources are backed up on the source cluster.

- `PreRestore`: Before resources are restored on the target cluster.

- `PostRestore`: After resources are restored on the target cluster.

You can create a hook by creating an Ansible playbook that runs with the default Ansible image or with a custom hook container.

<div class="formalpara">

<div class="title">

Ansible playbook

</div>

The Ansible playbook is mounted on a hook container as a config map. The hook container runs as a job, using the cluster, service account, and namespace specified in the `MigPlan` custom resource. The job continues to run until it reaches the default limit of 6 retries or a successful completion. This continues even if the initial pod is evicted or killed.

</div>

The default Ansible runtime image is `registry.redhat.io/rhmtc/openshift-migration-hook-runner-rhel7:1.8`. This image is based on the Ansible Runner image and includes `python-openshift` for Ansible Kubernetes resources and an updated `oc` binary.

<div class="formalpara">

<div class="title">

Custom hook container

</div>

You can use a custom hook container instead of the default Ansible image.

</div>

## Writing an Ansible playbook for a migration hook

You can write an Ansible playbook to use as a migration hook. The hook is added to a migration plan by using the MTC web console or by specifying values for the `spec.hooks` parameters in the `MigPlan` custom resource (CR) manifest.

The Ansible playbook is mounted onto a hook container as a config map. The hook container runs as a job, using the cluster, service account, and namespace specified in the `MigPlan` CR. The hook container uses a specified service account token so that the tasks do not require authentication before they run in the cluster.

### Ansible modules

You can use the Ansible `shell` module to run `oc` commands.

<div class="formalpara">

<div class="title">

Example `shell` module

</div>

``` yaml
- hosts: localhost
  gather_facts: false
  tasks:
  - name: get pod name
    shell: oc get po --all-namespaces
```

</div>

You can use `kubernetes.core` modules, such as `k8s_info`, to interact with Kubernetes resources.

<div class="formalpara">

<div class="title">

Example `k8s_facts` module

</div>

``` yaml
- hosts: localhost
  gather_facts: false
  tasks:
  - name: Get pod
    k8s_info:
      kind: pods
      api: v1
      namespace: openshift-migration
      name: "{{ lookup( 'env', 'HOSTNAME') }}"
    register: pods

  - name: Print pod name
    debug:
      msg: "{{ pods.resources[0].metadata.name }}"
```

</div>

You can use the `fail` module to produce a non-zero exit status in cases where a non-zero exit status would not normally be produced, ensuring that the success or failure of a hook is detected. Hooks run as jobs and the success or failure status of a hook is based on the exit status of the job container.

<div class="formalpara">

<div class="title">

Example `fail` module

</div>

``` yaml
- hosts: localhost
  gather_facts: false
  tasks:
  - name: Set a boolean
    set_fact:
      do_fail: true

  - name: "fail"
    fail:
      msg: "Cause a failure"
    when: do_fail
```

</div>

### Environment variables

The `MigPlan` CR name and migration namespaces are passed as environment variables to the hook container. These variables are accessed by using the `lookup` plugin.

<div class="formalpara">

<div class="title">

Example environment variables

</div>

``` yaml
- hosts: localhost
  gather_facts: false
  tasks:
  - set_fact:
      namespaces: "{{ (lookup( 'env', 'MIGRATION_NAMESPACES')).split(',') }}"

  - debug:
      msg: "{{ item }}"
    with_items: "{{ namespaces }}"

  - debug:
      msg: "{{ lookup( 'env', 'MIGRATION_PLAN_NAME') }}"
```

</div>

# Migration plan options

You can exclude, edit, and map components in the `MigPlan` custom resource (CR).

## Excluding resources

You can exclude resources, for example, image streams, persistent volumes (PVs), or subscriptions, from a Migration Toolkit for Containers (MTC) migration plan to reduce the resource load for migration or to migrate images or PVs with a different tool.

By default, the MTC excludes service catalog resources and Operator Lifecycle Manager (OLM) resources from migration. These resources are parts of the service catalog API group and the OLM API group, neither of which is supported for migration at this time.

<div>

<div class="title">

Procedure

</div>

1.  Edit the `MigrationController` custom resource manifest:

    ``` terminal
    $ oc edit migrationcontroller <migration_controller> -n openshift-migration
    ```

2.  Update the `spec` section by adding parameters to exclude specific resources. For those resources that do not have their own exclusion parameters, add the `additional_excluded_resources` parameter:

    ``` yaml
    apiVersion: migration.openshift.io/v1alpha1
    kind: MigrationController
    metadata:
      name: migration-controller
      namespace: openshift-migration
    spec:
      disable_image_migration: true
      disable_pv_migration: true
      additional_excluded_resources:
      - resource1
      - resource2
      ...
    ```

    - Add `disable_image_migration: true` to exclude image streams from the migration. `imagestreams` is added to the `excluded_resources` list in `main.yml` when the `MigrationController` pod restarts.

    - Add `disable_pv_migration: true` to exclude PVs from the migration plan. `persistentvolumes` and `persistentvolumeclaims` are added to the `excluded_resources` list in `main.yml` when the `MigrationController` pod restarts. Disabling PV migration also disables PV discovery when you create the migration plan.

    - You can add OpenShift Container Platform resources that you want to exclude to the `additional_excluded_resources` list.

3.  Wait two minutes for the `MigrationController` pod to restart so that the changes are applied.

4.  Verify that the resource is excluded:

    ``` terminal
    $ oc get deployment -n openshift-migration migration-controller -o yaml | grep EXCLUDED_RESOURCES -A1
    ```

    The output contains the excluded resources:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    name: EXCLUDED_RESOURCES
    value:
    resource1,resource2,imagetags,templateinstances,clusterserviceversions,packagemanifests,subscriptions,servicebrokers,servicebindings,serviceclasses,serviceinstances,serviceplans,imagestreams,persistentvolumes,persistentvolumeclaims
    ```

    </div>

</div>

## Mapping namespaces

If you map namespaces in the `MigPlan` custom resource (CR), you must ensure that the namespaces are not duplicated on the source or the destination clusters because the UID and GID ranges of the namespaces are copied during migration.

<div class="formalpara">

<div class="title">

Two source namespaces mapped to the same destination namespace

</div>

``` yaml
spec:
  namespaces:
    - namespace_2
    - namespace_1:namespace_2
```

</div>

If you want the source namespace to be mapped to a namespace of the same name, you do not need to create a mapping. By default, a source namespace and a target namespace have the same name.

<div class="formalpara">

<div class="title">

Incorrect namespace mapping

</div>

``` yaml
spec:
  namespaces:
    - namespace_1:namespace_1
```

</div>

<div class="formalpara">

<div class="title">

Correct namespace reference

</div>

``` yaml
spec:
  namespaces:
    - namespace_1
```

</div>

## Excluding persistent volume claims

You select persistent volume claims (PVCs) for state migration by excluding the PVCs that you do not want to migrate. You exclude PVCs by setting the `spec.persistentVolumes.pvc.selection.action` parameter of the `MigPlan` custom resource (CR) after the persistent volumes (PVs) have been discovered.

<div>

<div class="title">

Prerequisites

</div>

- `MigPlan` CR is in a `Ready` state.

</div>

<div>

<div class="title">

Procedure

</div>

- Add the `spec.persistentVolumes.pvc.selection.action` parameter to the `MigPlan` CR and set it to `skip`:

  ``` yaml
  apiVersion: migration.openshift.io/v1alpha1
  kind: MigPlan
  metadata:
    name: <migplan>
    namespace: openshift-migration
  spec:
  ...
    persistentVolumes:
    - capacity: 10Gi
      name: <pv_name>
      pvc:
  ...
      selection:
        action: skip
  ```

</div>

## Mapping persistent volume claims

You can migrate persistent volume (PV) data from the source cluster to persistent volume claims (PVCs) that are already provisioned in the destination cluster in the `MigPlan` CR by mapping the PVCs. This mapping ensures that the destination PVCs of migrated applications are synchronized with the source PVCs.

You map PVCs by updating the `spec.persistentVolumes.pvc.name` parameter in the `MigPlan` custom resource (CR) after the PVs have been discovered.

<div>

<div class="title">

Prerequisites

</div>

- `MigPlan` CR is in a `Ready` state.

</div>

<div>

<div class="title">

Procedure

</div>

- Update the `spec.persistentVolumes.pvc.name` parameter in the `MigPlan` CR:

  ``` yaml
  apiVersion: migration.openshift.io/v1alpha1
  kind: MigPlan
  metadata:
    name: <migplan>
    namespace: openshift-migration
  spec:
  ...
    persistentVolumes:
    - capacity: 10Gi
      name: <pv_name>
      pvc:
        name: <source_pvc>:<destination_pvc>
  ```

  - Specify the PVC on the source cluster and the PVC on the destination cluster. If the destination PVC does not exist, it will be created. You can use this mapping to change the PVC name during migration.

</div>

## Editing persistent volume attributes

After you create a `MigPlan` custom resource (CR), the `MigrationController` CR discovers the persistent volumes (PVs). The `spec.persistentVolumes` block and the `status.destStorageClasses` block are added to the `MigPlan` CR.

You can edit the values in the `spec.persistentVolumes.selection` block. If you change values outside the `spec.persistentVolumes.selection` block, the values are overwritten when the `MigPlan` CR is reconciled by the `MigrationController` CR.

> [!NOTE]
> The default value for the `spec.persistentVolumes.selection.storageClass` parameter is determined by the following logic:
>
> 1.  If the source cluster PV is Gluster or NFS, the default is either `cephfs`, for `accessMode: ReadWriteMany`, or `cephrbd`, for `accessMode: ReadWriteOnce`.
>
> 2.  If the PV is neither Gluster nor NFS *or* if `cephfs` or `cephrbd` are not available, the default is a storage class for the same provisioner.
>
> 3.  If a storage class for the same provisioner is not available, the default is the default storage class of the destination cluster.
>
> You can change the `storageClass` value to the value of any `name` parameter in the `status.destStorageClasses` block of the `MigPlan` CR.
>
> If the `storageClass` value is empty, the PV will have no storage class after migration. This option is appropriate if, for example, you want to move the PV to an NFS volume on the destination cluster.

<div>

<div class="title">

Prerequisites

</div>

- `MigPlan` CR is in a `Ready` state.

</div>

<div>

<div class="title">

Procedure

</div>

- Edit the `spec.persistentVolumes.selection` values in the `MigPlan` CR:

  ``` yaml
  apiVersion: migration.openshift.io/v1alpha1
  kind: MigPlan
  metadata:
    name: <migplan>
    namespace: openshift-migration
  spec:
    persistentVolumes:
    - capacity: 10Gi
      name: pvc-095a6559-b27f-11eb-b27f-021bddcaf6e4
      proposedCapacity: 10Gi
      pvc:
        accessModes:
        - ReadWriteMany
        hasReference: true
        name: mysql
        namespace: mysql-persistent
      selection:
        action: <copy>
        copyMethod: <filesystem>
        verify: true
        storageClass: <gp2>
        accessMode: <ReadWriteMany>
      storageClass: cephfs
  ```

  - Allowed values are `move`, `copy`, and `skip`. If only one action is supported, the default value is the supported action. If multiple actions are supported, the default value is `copy`.

  - Allowed values are `snapshot` and `filesystem`. Default value is `filesystem`.

  - The `verify` parameter is displayed if you select the verification option for file system copy in the MTC web console. You can set it to `false`.

  - You can change the default value to the value of any `name` parameter in the `status.destStorageClasses` block of the `MigPlan` CR. If no value is specified, the PV will have no storage class after migration.

  - Allowed values are `ReadWriteOnce` and `ReadWriteMany`. If this value is not specified, the default is the access mode of the source cluster PVC. You can only edit the access mode in the `MigPlan` CR. You cannot edit it by using the MTC web console.

</div>

## Converting storage classes in the MTC web console

You can convert the storage class of a persistent volume (PV) by migrating it within the same cluster. To do so, you must create and run a migration plan in the Migration Toolkit for Containers (MTC) web console.

<div>

<div class="title">

Prerequisites

</div>

- You must be logged in as a user with `cluster-admin` privileges on the cluster on which MTC is running.

- You must add the cluster to the MTC web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the left-side navigation pane of the OpenShift Container Platform web console, click **Projects**.

2.  In the list of projects, click your project.

    The **Project details** page opens.

3.  Click the **DeploymentConfig** name. Note the name of its running pod.

4.  Open the YAML tab of the project. Find the PVs and note the names of their corresponding persistent volume claims (PVCs).

5.  In the MTC web console, click **Migration plans**.

6.  Click **Add migration plan**.

7.  Enter the **Plan name**.

    The migration plan name must contain 3 to 63 lower-case alphanumeric characters (`a-z, 0-9`) and must not contain spaces or underscores (`_`).

8.  From the **Migration type** menu, select **Storage class conversion**.

9.  From the **Source cluster** list, select the desired cluster for storage class conversion.

10. Click **Next**.

    The **Namespaces** page opens.

11. Select the required project.

12. Click **Next**.

    The **Persistent volumes** page opens. The page displays the PVs in the project, all selected by default.

13. For each PV, select the desired target storage class.

14. Click **Next**.

    The wizard validates the new migration plan and shows that it is ready.

15. Click **Close**.

    The new plan appears on the **Migration plans** page.

16. To start the conversion, click the options menu of the new plan.

    Under **Migrations**, two options are displayed, **Stage** and **Cutover**.

    > [!NOTE]
    > Cutover migration updates PVC references in the applications.
    >
    > Stage migration does not update PVC references in the applications.

17. Select the desired option.

    Depending on which option you selected, the **Stage migration** or **Cutover migration** notification appears.

18. Click **Migrate**.

    Depending on which option you selected, the **Stage started** or **Cutover started** message appears.

19. To see the status of the current migration, click the number in the **Migrations** column.

    The **Migrations** page opens.

20. To see more details on the current migration and monitor its progress, select the migration from the **Type** column.

    The **Migration details** page opens. When the migration progresses to the DirectVolume step and the status of the step becomes `Running Rsync Pods to migrate Persistent Volume data`, you can click **View details** and see the detailed status of the copies.

21. In the breadcrumb bar, click **Stage** or **Cutover** and wait for all steps to complete.

22. Open the **PersistentVolumeClaims** tab of the OpenShift Container Platform web console.

    You can see new PVCs with the names of the initial PVCs but ending in `new`, which are using the target storage class.

23. In the left-side navigation pane, click **Pods**. See that the pod of your project is running again.

</div>

### Additional resources

- For details about the `move` and `copy` actions, see [MTC workflow](about-mtc.md#migration-mtc-workflow_about-mtc).

- For details about the `skip` action, see [Excluding PVCs from migration](advanced-migration-options-mtc.md#migration-excluding-pvcs_advanced-migration-options-mtc).

- For details about the file system and snapshot copy methods, see [About data copy methods](about-mtc.md#migration-understanding-data-copy-methods_about-mtc).

## Performing a state migration of Kubernetes objects by using the MTC API

After you migrate all the PV data, you can use the Migration Toolkit for Containers (MTC) API to perform a one-time state migration of Kubernetes objects that constitute an application.

You do this by configuring `MigPlan` custom resource (CR) fields to provide a list of Kubernetes resources with an additional label selector to further filter those resources, and then performing a migration by creating a `MigMigration` CR. The `MigPlan` resource is closed after the migration.

> [!NOTE]
> Selecting Kubernetes resources is an API-only feature. You must update the `MigPlan` CR and create a `MigMigration` CR for it by using the CLI. The MTC web console does not support migrating Kubernetes objects.

> [!NOTE]
> After migration, the `closed` parameter of the `MigPlan` CR is set to `true`. You cannot create another `MigMigration` CR for this `MigPlan` CR.

You add Kubernetes objects to the `MigPlan` CR by using one of the following options:

- Adding the Kubernetes objects to the `includedResources` section. When the `includedResources` field is specified in the `MigPlan` CR, the plan takes a list of `group-kind` as input. Only resources present in the list are included in the migration.

- Adding the optional `labelSelector` parameter to filter the `includedResources` in the `MigPlan`. When this field is specified, only resources matching the label selector are included in the migration. For example, you can filter a list of `Secret` and `ConfigMap` resources by using the label `app: frontend` as a filter.

<div>

<div class="title">

Procedure

</div>

1.  Update the `MigPlan` CR to include Kubernetes resources and, optionally, to filter the included resources by adding the `labelSelector` parameter:

    1.  To update the `MigPlan` CR to include Kubernetes resources:

        ``` yaml
        apiVersion: migration.openshift.io/v1alpha1
        kind: MigPlan
        metadata:
          name: <migplan>
          namespace: openshift-migration
        spec:
          includedResources:
          - kind: <kind>
            group: ""
          - kind: <kind>
            group: ""
        ```

        - Specify the Kubernetes object, for example, `Secret` or `ConfigMap`.

    2.  Optional: To filter the included resources by adding the `labelSelector` parameter:

        ``` yaml
        apiVersion: migration.openshift.io/v1alpha1
        kind: MigPlan
        metadata:
          name: <migplan>
          namespace: openshift-migration
        spec:
          includedResources:
          - kind: <kind>
            group: ""
          - kind: <kind>
            group: ""
        ...
          labelSelector:
            matchLabels:
              <label>
        ```

        - Specify the Kubernetes object, for example, `Secret` or `ConfigMap`.

        - Specify the label of the resources to migrate, for example, `app: frontend`.

2.  Create a `MigMigration` CR to migrate the selected Kubernetes resources. Verify that the correct `MigPlan` is referenced in `migPlanRef`:

    ``` yaml
    apiVersion: migration.openshift.io/v1alpha1
    kind: MigMigration
    metadata:
      generateName: <migplan>
      namespace: openshift-migration
    spec:
      migPlanRef:
        name: <migplan>
        namespace: openshift-migration
      stage: false
    ```

</div>

# Migration controller options

You can edit migration plan limits, enable persistent volume resizing, or enable cached Kubernetes clients in the `MigrationController` custom resource (CR) for large migrations and improved performance.

## Increasing limits for large migrations

You can increase the limits on migration objects and container resources for large migrations with the Migration Toolkit for Containers (MTC).

> [!IMPORTANT]
> You must test these changes before you perform a migration in a production environment.

<div>

<div class="title">

Procedure

</div>

1.  Edit the `MigrationController` custom resource (CR) manifest:

    ``` terminal
    $ oc edit migrationcontroller -n openshift-migration
    ```

2.  Update the following parameters:

    ``` yaml
    ...
    mig_controller_limits_cpu: "1"
    mig_controller_limits_memory: "10Gi"
    ...
    mig_controller_requests_cpu: "100m"
    mig_controller_requests_memory: "350Mi"
    ...
    mig_pv_limit: 100
    mig_pod_limit: 100
    mig_namespace_limit: 10
    ...
    ```

    - Specifies the number of CPUs available to the `MigrationController` CR.

    - Specifies the amount of memory available to the `MigrationController` CR.

    - Specifies the number of CPU units available for `MigrationController` CR requests. `100m` represents 0.1 CPU units (100 \* 1e-3).

    - Specifies the amount of memory available for `MigrationController` CR requests.

    - Specifies the number of persistent volumes that can be migrated.

    - Specifies the number of pods that can be migrated.

    - Specifies the number of namespaces that can be migrated.

3.  Create a migration plan that uses the updated parameters to verify the changes.

    If your migration plan exceeds the `MigrationController` CR limits, the MTC console displays a warning message when you save the migration plan.

</div>

## Enabling persistent volume resizing for direct volume migration

You can enable persistent volume (PV) resizing for direct volume migration to avoid running out of disk space on the destination cluster.

When the disk usage of a PV reaches a configured level, the `MigrationController` custom resource (CR) compares the requested storage capacity of a persistent volume claim (PVC) to its actual provisioned capacity. Then, it calculates the space required on the destination cluster.

A `pv_resizing_threshold` parameter determines when PV resizing is used. The default threshold is `3%`. This means that PV resizing occurs when the disk usage of a PV is more than `97%`. You can increase this threshold so that PV resizing occurs at a lower disk usage level.

PVC capacity is calculated according to the following criteria:

- If the requested storage capacity (`spec.resources.requests.storage`) of the PVC is not equal to its actual provisioned capacity (`status.capacity.storage`), the greater value is used.

- If a PV is provisioned through a PVC and then subsequently changed so that its PV and PVC capacities no longer match, the greater value is used.

<div>

<div class="title">

Prerequisites

</div>

- The PVCs must be attached to one or more running pods so that the `MigrationController` CR can execute commands.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the host cluster.

2.  Enable PV resizing by patching the `MigrationController` CR:

    ``` terminal
    $ oc patch migrationcontroller migration-controller -p '{"spec":{"enable_dvm_pv_resizing":true}}' \
      --type='merge' -n openshift-migration
    ```

    - Set the value to `false` to disable PV resizing.

3.  Optional: Update the `pv_resizing_threshold` parameter to increase the threshold:

    ``` terminal
    $ oc patch migrationcontroller migration-controller -p '{"spec":{"pv_resizing_threshold":41}}' \
      --type='merge' -n openshift-migration
    ```

    - The default value is `3`.

      When the threshold is exceeded, the following status message is displayed in the `MigPlan` CR status:

      ``` yaml
      status:
        conditions:
      ...
        - category: Warn
          durable: true
          lastTransitionTime: "2021-06-17T08:57:01Z"
          message: 'Capacity of the following volumes will be automatically adjusted to avoid disk capacity issues in the target cluster:  [pvc-b800eb7b-cf3b-11eb-a3f7-0eae3e0555f3]'
          reason: Done
          status: "False"
          type: PvCapacityAdjustmentRequired
      ```

      > [!NOTE]
      > For AWS gp2 storage, this message does not appear unless the `pv_resizing_threshold` is 42% or greater because of the way gp2 calculates volume usage and size. ([**BZ#1973148**](https://bugzilla.redhat.com/show_bug.cgi?id=1973148))

</div>

## Enabling cached Kubernetes clients

You can enable cached Kubernetes clients in the `MigrationController` custom resource (CR) for improved performance during migration. The greatest performance benefit is displayed when migrating between clusters in different regions or with significant network latency.

> [!NOTE]
> Delegated tasks, for example, Rsync backup for direct volume migration or Velero backup and restore, however, do not show improved performance with cached clients.

Cached clients require extra memory because the `MigrationController` CR caches all API resources that are required for interacting with `MigCluster` CRs. Requests that are normally sent to the API server are directed to the cache instead. The cache watches the API server for updates.

You can increase the memory limits and requests of the `MigrationController` CR if `OOMKilled` errors occur after you enable cached clients.

<div>

<div class="title">

Procedure

</div>

1.  Enable cached clients by running the following command:

    ``` terminal
    $ oc -n openshift-migration patch migrationcontroller migration-controller --type=json --patch \
      '[{ "op": "replace", "path": "/spec/mig_controller_enable_cache", "value": true}]'
    ```

2.  Optional: Increase the `MigrationController` CR memory limits by running the following command:

    ``` terminal
    $ oc -n openshift-migration patch migrationcontroller migration-controller --type=json --patch \
      '[{ "op": "replace", "path": "/spec/mig_controller_limits_memory", "value": <10Gi>}]'
    ```

3.  Optional: Increase the `MigrationController` CR memory requests by running the following command:

    ``` terminal
    $ oc -n openshift-migration patch migrationcontroller migration-controller --type=json --patch \
      '[{ "op": "replace", "path": "/spec/mig_controller_requests_memory", "value": <350Mi>}]'
    ```

</div>
