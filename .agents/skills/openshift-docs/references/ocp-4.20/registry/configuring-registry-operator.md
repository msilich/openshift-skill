<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Image Registry on cloud platforms and OpenStack

The Image Registry Operator installs a single instance of the OpenShift image registry and manages all registry configuration, including setting up registry storage.

> [!NOTE]
> Storage is only automatically configured when you install an installer-provisioned infrastructure cluster on AWS, Azure, Google Cloud, IBM®, or RHOSP.
>
> When you install or upgrade an installer-provisioned infrastructure cluster on AWS, Azure, Google Cloud, IBM®, or RHOSP, the Image Registry Operator sets the `spec.storage.managementState` parameter to `Managed`. If the `spec.storage.managementState` parameter is set to `Unmanaged`, the Image Registry Operator takes no action related to storage.

After the control plane deploys in the management cluster, the Operator creates a default `configs.imageregistry.operator.openshift.io` custom resource (CR) instance based on configuration detected in the cluster.

If insufficient information is available to define a complete `configs.imageregistry.operator.openshift.io` CR, the incomplete resource is defined and the Operator updates the resource status with information about what is missing.

> [!IMPORTANT]
> The Image Registry Operator’s behavior for managing the pruner is orthogonal to the `managementState` specified on the `ClusterOperator` object for the Image Registry Operator. If the Image Registry Operator is not in the `Managed` state, the image pruner can still be configured and managed by the `Pruning` custom resource.
>
> However, the `managementState` of the Image Registry Operator alters the behavior of the deployed image pruner job:
>
> - `Managed`: the `--prune-registry` flag for the image pruner is set to `true`.
>
> - `Removed`: the `--prune-registry` flag for the image pruner is set to `false`, meaning the image pruner job only prunes image metadata in etcd.

# Image Registry on bare metal, Nutanix, and vSphere

## Image registry removed during installation

On platforms that do not provide shareable object storage, the OpenShift Image Registry Operator bootstraps itself as `Removed`. This allows `openshift-installer` to complete installations on these platform types.

After installation, you must edit the Image Registry Operator configuration to switch the `managementState` from `Removed` to `Managed`. When this has completed, you must configure storage.

# Image Registry Operator distribution across availability zones

The default configuration of the Image Registry Operator spreads image registry pods across topology zones to prevent delayed recovery times in case of a complete zone failure where all pods are impacted. Reference the example YAML to understand the default parameter values that the Image Registry Operator uses when the Operator deploys with a zone-related topology constraint:

``` yaml
  topologySpreadConstraints:
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: DoNotSchedule
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: node-role.kubernetes.io/worker
    whenUnsatisfiable: DoNotSchedule
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: topology.kubernetes.io/zone
    whenUnsatisfiable: DoNotSchedule
```

Reference the following YAML to understand the default parameter value that the Image Registry Operator uses when the Operator deploys with a zone-related topology constraint, which applies to bare metal and vSphere instances:

``` yaml
 topologySpreadConstraints:
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: kubernetes.io/hostname
    whenUnsatisfiable: DoNotSchedule
  - labelSelector:
      matchLabels:
        docker-registry: default
    maxSkew: 1
    topologyKey: node-role.kubernetes.io/worker
    whenUnsatisfiable: DoNotSchedule
```

As a cluster administrator. you can override the default `topologySpreadConstraints` section values by configuring the `configs.imageregistry.operator.openshift.io/cluster` spec file.

# Additional resources

- [Configuring pod topology spread constraints](../nodes/scheduling/nodes-scheduler-pod-topology-spread-constraints.md#nodes-scheduler-pod-topology-spread-constraints)

# Image Registry Operator configuration parameters

You can configure the Image Registry Operator using the `configs.imageregistry.operator.openshift.io` resource. The resource provides parameters for managing registry state, storage, logging, routing, and deployment settings.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>managementState</code></p></td>
<td style="text-align: left;"><p><code>Managed</code>: The Operator updates the registry as configuration resources are updated.</p>
<p><code>Unmanaged</code>: The Operator ignores changes to the configuration resources.</p>
<p><code>Removed</code>: The Operator removes the registry instance and tear down any storage that the Operator provisioned.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>logLevel</code></p></td>
<td style="text-align: left;"><p>Sets <code>logLevel</code> of the registry instance. Defaults to <code>Normal</code>.</p>
<p>The following values for <code>logLevel</code> are supported:</p>
<ul>
<li><p><code>Normal</code></p></li>
<li><p><code>Debug</code></p></li>
<li><p><code>Trace</code></p></li>
<li><p><code>TraceAll</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpSecret</code></p></td>
<td style="text-align: left;"><p>Value needed by the registry to secure uploads, generated by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operatorLogLevel</code></p></td>
<td style="text-align: left;"><p>The <code>operatorLogLevel</code> configuration parameter provides intent-based logging for the Operator itself and a simple way to manage coarse-grained logging choices that Operators must interpret for themselves. This configuration parameter defaults to <code>Normal</code>. It does not provide fine-grained control.</p>
<p>The following values for <code>operatorLogLevel</code> are supported:</p>
<ul>
<li><p><code>Normal</code></p></li>
<li><p><code>Debug</code></p></li>
<li><p><code>Trace</code></p></li>
<li><p><code>TraceAll</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>proxy</code></p></td>
<td style="text-align: left;"><p>Defines the Proxy to be used when calling master API and upstream registries.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>affinity</code></p></td>
<td style="text-align: left;"><p>You can use the <code>affinity</code> parameter to configure pod scheduling preferences and constraints for Image Registry Operator pods.</p>
<p>Affinity settings can use the <code>podAffinity</code> or <code>podAntiAffinity</code> spec. Both options can use either <code>preferredDuringSchedulingIgnoredDuringExecution</code> rules or <code>requiredDuringSchedulingIgnoredDuringExecution</code> rules.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>storage</code></p></td>
<td style="text-align: left;"><p><code>Storagetype</code>: Details for configuring registry storage, for example S3 bucket coordinates. Normally configured by default.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>readOnly</code></p></td>
<td style="text-align: left;"><p>Indicates whether the registry instance should reject attempts to push new images or delete existing ones.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p>API Request Limit details. Controls how many parallel requests a given registry instance will handle before queuing additional requests.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>defaultRoute</code></p></td>
<td style="text-align: left;"><p>Determines whether or not an external route is defined using the default hostname. If enabled, the route uses re-encrypt encryption. Defaults to <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>routes</code></p></td>
<td style="text-align: left;"><p>Array of additional routes to create. You provide the hostname and certificate for the route.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rolloutStrategy</code></p></td>
<td style="text-align: left;"><p>Defines rollout strategy for the image registry deployment. Defaults to <code>RollingUpdate</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>replicas</code></p></td>
<td style="text-align: left;"><p>Replica count for the registry.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>disableRedirect</code></p></td>
<td style="text-align: left;"><p>Controls whether to route all data through the registry, rather than redirecting to the back end. Defaults to <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.storage.managementState</code></p></td>
<td style="text-align: left;"><p>The Image Registry Operator sets the <code>spec.storage.managementState</code> parameter to <code>Managed</code> on new installations or upgrades of clusters using installer-provisioned infrastructure on AWS or Azure.</p>
<ul>
<li><p><code>Managed</code>: Determines that the Image Registry Operator manages underlying storage. If the Image Registry Operator’s <code>managementState</code> is set to <code>Removed</code>, then the storage is deleted.</p>
<ul>
<li><p>If the <code>managementState</code> is set to <code>Managed</code>, the Image Registry Operator attempts to apply some default configuration on the underlying storage unit. For example, if set to <code>Managed</code>, the Operator tries to enable encryption on the S3 bucket before making it available to the registry. If you do not want the default settings to be applied on the storage you are providing, make sure the <code>managementState</code> is set to <code>Unmanaged</code>.</p></li>
</ul></li>
<li><p><code>Unmanaged</code>: Determines that the Image Registry Operator ignores the storage settings. If the Image Registry Operator’s <code>managementState</code> is set to <code>Removed</code>, then the storage is not deleted. If you provided an underlying storage unit configuration, such as a bucket or container name, and the <code>spec.storage.managementState</code> is not yet set to any value, then the Image Registry Operator configures it to <code>Unmanaged</code>.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Enabling the Image Registry default route by using a CRD

In OpenShift Container Platform, the `Registry` Operator controls the OpenShift image registry feature and you define this Operator in the `configs.imageregistry.operator.openshift.io` Custom Resource Definition (CRD). If you need to automatically enable the Image Registry default route, patch the Image Registry Operator CRD.

<div>

<div class="title">

Procedure

</div>

- Patch the Image Registry Operator CRD:

  ``` terminal
  $ oc patch configs.imageregistry.operator.openshift.io/cluster --type merge -p '{"spec":{"defaultRoute":true}}'
  ```

</div>

# Configuring additional trust stores for image registry access

You can add references to a config map that has additional certificate authorities (CAs) to be trusted during image registry access to the `image.config.openshift.io/cluster` custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- The certificate authorities (CAs) must be PEM-encoded.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a config map in the `openshift-config` namespace, then and use the config map name in the `AdditionalTrustedCA` parameter of the `image.config.openshift.io` CR. This adds CAs that should be trusted when the cluster contacts external image registries.

    <div class="formalpara">

    <div class="title">

    Image registry CA config map example

    </div>

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: my-registry-ca
    data:
      registry.example.com: |
        -----BEGIN CERTIFICATE-----
        ...
        -----END CERTIFICATE-----
      registry-with-port.example.com..5000: |
        -----BEGIN CERTIFICATE-----
        ...
        -----END CERTIFICATE-----
    ```

    </div>

    where:

    `data:registry.example.com:`
    An example hostname of a registry for which this CA is to be trusted.

    `data:registry-with-port.example.com..5000:`
    An example hostname of a registry with the port for which this CA is to be trusted. If the registry has a port, such as `registry-with-port.example.com:5000`, `:` must be replaced with `..`.

    The PEM certificate content is the value for each additional registry CA to trust.

2.  Optional. Configure an additional CA by running the following command:

    ``` terminal
    $ oc create configmap registry-config --from-file=<external_registry_address>=ca.crt -n openshift-config
    ```

    ``` terminal
    $ oc edit image.config.openshift.io cluster
    ```

    ``` yaml
    spec:
      additionalTrustedCA:
        name: registry-config
    ```

</div>

# Configuring storage credentials for the Image Registry Operator

In addition to the `configs.imageregistry.operator.openshift.io` Custom Resource (CR) and ConfigMap resources, storage credential configuration is provided to the Operator by a separate secret resource. This resource is located within the `openshift-image-registry` namespace.

You can create an `image-registry-private-configuration-user` secret that in turn creates custom credentials needed for storage access and management. If default credentials exist, the custom credentials override the default credentials used by the Operator.

<div>

<div class="title">

Procedure

</div>

- Create an OpenShift Container Platform secret that contains the required keys.

  ``` terminal
  $ oc create secret generic image-registry-private-configuration-user --from-literal=KEY1=value1 --from-literal=KEY2=value2 --namespace openshift-image-registry
  ```

</div>

# Additional resources

- [Configuring the registry for AWS user-provisioned infrastructure](configuring_registry_storage/configuring-registry-storage-aws-user-infrastructure.md#configuring-registry-storage-aws-user-infrastructure)

- [Configuring the registry for Google Cloud user-provisioned infrastructure](configuring_registry_storage/configuring-registry-storage-gcp-user-infrastructure.md#configuring-registry-storage-gcp-user-infrastructure)

- [Configuring the registry for Azure user-provisioned infrastructure](configuring_registry_storage/configuring-registry-storage-azure-user-infrastructure.md#configuring-registry-storage-azure-user-infrastructure)

- [Configuring the registry for bare metal](configuring_registry_storage/configuring-registry-storage-baremetal.md#configuring-registry-storage-baremetal)

- [Configuring the registry for vSphere](configuring_registry_storage/configuring-registry-storage-vsphere.md#configuring-registry-storage-vsphere)

- [Configuring the registry for RHOSP](configuring_registry_storage/configuring-registry-storage-osp.md#configuring-registry-storage-openstack)

- [Configuring the registry for Red Hat OpenShift Data Foundation](configuring_registry_storage/configuring-registry-storage-rhodf.md#configuring-registry-storage-rhodf)

- [Configuring the registry for Nutanix](configuring_registry_storage/configuring-registry-storage-nutanix.md#configuring-registry-storage-nutanix)
