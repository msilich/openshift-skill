<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

This guide outlines the use of Operator groups with Operator Lifecycle Manager (OLM) in OpenShift Container Platform.

# About Operator groups

An *Operator group*, defined by the `OperatorGroup` resource, provides multitenant configuration to OLM-installed Operators. An Operator group selects target namespaces in which to generate required RBAC access for its member Operators.

The set of target namespaces is provided by a comma-delimited string stored in the `olm.targetNamespaces` annotation of a cluster service version (CSV). This annotation is applied to the CSV instances of member Operators and is projected into their deployments.

# Operator group membership

An Operator is considered a *member* of an Operator group if the following conditions are true:

- The CSV of the Operator exists in the same namespace as the Operator group.

- The install modes in the CSV of the Operator support the set of namespaces targeted by the Operator group.

An install mode in a CSV consists of an `InstallModeType` field and a boolean `Supported` field. The spec of a CSV can contain a set of install modes of four distinct `InstallModeTypes`:

| InstallModeType | Description |
|----|----|
| `OwnNamespace` | The Operator can be a member of an Operator group that selects its own namespace. |
| `SingleNamespace` | The Operator can be a member of an Operator group that selects one namespace. |
| `MultiNamespace` | The Operator can be a member of an Operator group that selects more than one namespace. |
| `AllNamespaces` | The Operator can be a member of an Operator group that selects all namespaces (target namespace set is the empty string `""`). |

Install modes and supported Operator groups

> [!NOTE]
> If the spec of a CSV omits an entry of `InstallModeType`, then that type is considered unsupported unless support can be inferred by an existing entry that implicitly supports it.

# Target namespace selection

You can explicitly name the target namespace for an Operator group using the `spec.targetNamespaces` parameter:

``` yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: my-group
  namespace: my-namespace
spec:
  targetNamespaces:
  - my-namespace
```

You can alternatively specify a namespace using a label selector with the `spec.selector` parameter:

``` yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: my-group
  namespace: my-namespace
spec:
  selector:
    cool.io/prod: "true"
```

> [!IMPORTANT]
> Listing multiple namespaces via `spec.targetNamespaces` or use of a label selector via `spec.selector` is not recommended, as the support for more than one target namespace in an Operator group will likely be removed in a future release.

If both `spec.targetNamespaces` and `spec.selector` are defined, `spec.selector` is ignored. Alternatively, you can omit both `spec.selector` and `spec.targetNamespaces` to specify a *global* Operator group, which selects all namespaces:

``` yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: my-group
  namespace: my-namespace
```

The resolved set of selected namespaces is shown in the `status.namespaces` parameter of an Opeator group. The `status.namespace` of a global Operator group contains the empty string (`""`), which signals to a consuming Operator that it should watch all namespaces.

# Operator group CSV annotations

Member CSVs of an Operator group have the following annotations:

| Annotation | Description |
|----|----|
| `olm.operatorGroup=<group_name>` | Contains the name of the Operator group. |
| `olm.operatorNamespace=<group_namespace>` | Contains the namespace of the Operator group. |
| `olm.targetNamespaces=<target_namespaces>` | Contains a comma-delimited string that lists the target namespace selection of the Operator group. |

> [!NOTE]
> All annotations except `olm.targetNamespaces` are included with copied CSVs. Omitting the `olm.targetNamespaces` annotation on copied CSVs prevents the duplication of target namespaces between tenants.

# Provided APIs annotation

A *group/version/kind (GVK)* is a unique identifier for a Kubernetes API. Information about what GVKs are provided by an Operator group are shown in an `olm.providedAPIs` annotation. The value of the annotation is a string consisting of `<kind>.<version>.<group>` delimited with commas. The GVKs of CRDs and API services provided by all active member CSVs of an Operator group are included.

Review the following example of an `OperatorGroup` object with a single active member CSV that provides the `PackageManifest` resource:

``` yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  annotations:
    olm.providedAPIs: PackageManifest.v1alpha1.packages.apps.redhat.com
  name: olm-operators
  namespace: local
  ...
spec:
  selector: {}
  serviceAccountName:
    metadata:
      creationTimestamp: null
  targetNamespaces:
  - local
status:
  lastUpdated: 2019-02-19T16:18:28Z
  namespaces:
  - local
```

# Role-based access control

When an Operator group is created, three cluster roles are generated. When the cluster roles are generated, they are automatically suffixed with a hash value to ensure that each cluster role is unique. Each Operator group contains a single aggregation rule with a cluster role selector set to match a label, as shown in the following table:

| Cluster role | Label to match |
|----|----|
| `olm.og.<operatorgroup_name>-admin-<hash_value>` | `olm.opgroup.permissions/aggregate-to-admin: <operatorgroup_name>` |
| `olm.og.<operatorgroup_name>-edit-<hash_value>` | `olm.opgroup.permissions/aggregate-to-edit: <operatorgroup_name>` |
| `olm.og.<operatorgroup_name>-view-<hash_value>` | `olm.opgroup.permissions/aggregate-to-view: <operatorgroup_name>` |

> [!NOTE]
> To use the cluster role of an Operator group to assign role-based access control (RBAC) to a resource, get the full name of cluster role and hash value by running the following command:
>
> ``` terminal
> $ oc get clusterroles | grep <operatorgroup_name>
> ```
>
> Because the hash value is generated when the Operator group is created, you must create the Operator group before you can look up the complete name of the cluster role.

The following RBAC resources are generated when a CSV becomes an active member of an Operator group, as long as the CSV is watching all namespaces with the `AllNamespaces` install mode and is not in a failed state with reason `InterOperatorGroupOwnerConflict`:

- Cluster roles for each API resource from a CRD

- Cluster roles for each API resource from an API service

- Additional roles and role bindings

<table id="olm-resources-per-api-resource-crd_olm-understanding-operatorgroups">
<caption>Cluster roles generated for each API resource from a CRD</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Cluster role</th>
<th style="text-align: left;">Settings</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>&lt;kind&gt;.&lt;group&gt;-&lt;version&gt;-admin</code></p></td>
<td style="text-align: left;"><p>Verbs on <code>&lt;kind&gt;</code>:</p>
<ul>
<li><p><code>*</code></p></li>
</ul>
<p>Aggregation labels:</p>
<ul>
<li><p><code>rbac.authorization.k8s.io/aggregate-to-admin: true</code></p></li>
<li><p><code>olm.opgroup.permissions/aggregate-to-admin: &lt;operatorgroup_name&gt;</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>&lt;kind&gt;.&lt;group&gt;-&lt;version&gt;-edit</code></p></td>
<td style="text-align: left;"><p>Verbs on <code>&lt;kind&gt;</code>:</p>
<ul>
<li><p><code>create</code></p></li>
<li><p><code>update</code></p></li>
<li><p><code>patch</code></p></li>
<li><p><code>delete</code></p></li>
</ul>
<p>Aggregation labels:</p>
<ul>
<li><p><code>rbac.authorization.k8s.io/aggregate-to-edit: true</code></p></li>
<li><p><code>olm.opgroup.permissions/aggregate-to-edit: &lt;operatorgroup_name&gt;</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>&lt;kind&gt;.&lt;group&gt;-&lt;version&gt;-view</code></p></td>
<td style="text-align: left;"><p>Verbs on <code>&lt;kind&gt;</code>:</p>
<ul>
<li><p><code>get</code></p></li>
<li><p><code>list</code></p></li>
<li><p><code>watch</code></p></li>
</ul>
<p>Aggregation labels:</p>
<ul>
<li><p><code>rbac.authorization.k8s.io/aggregate-to-view: true</code></p></li>
<li><p><code>olm.opgroup.permissions/aggregate-to-view: &lt;operatorgroup_name&gt;</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>&lt;kind&gt;.&lt;group&gt;-&lt;version&gt;-view-crdview</code></p></td>
<td style="text-align: left;"><p>Verbs on <code>apiextensions.k8s.io</code> <code>customresourcedefinitions</code> <code>&lt;crd-name&gt;</code>:</p>
<ul>
<li><p><code>get</code></p></li>
</ul>
<p>Aggregation labels:</p>
<ul>
<li><p><code>rbac.authorization.k8s.io/aggregate-to-view: true</code></p></li>
<li><p><code>olm.opgroup.permissions/aggregate-to-view: &lt;operatorgroup_name&gt;</code></p></li>
</ul></td>
</tr>
</tbody>
</table>

<table id="olm-resources-per-api-resource-api_olm-understanding-operatorgroups">
<caption>Cluster roles generated for each API resource from an API service</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Cluster role</th>
<th style="text-align: left;">Settings</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>&lt;kind&gt;.&lt;group&gt;-&lt;version&gt;-admin</code></p></td>
<td style="text-align: left;"><p>Verbs on <code>&lt;kind&gt;</code>:</p>
<ul>
<li><p><code>*</code></p></li>
</ul>
<p>Aggregation labels:</p>
<ul>
<li><p><code>rbac.authorization.k8s.io/aggregate-to-admin: true</code></p></li>
<li><p><code>olm.opgroup.permissions/aggregate-to-admin: &lt;operatorgroup_name&gt;</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>&lt;kind&gt;.&lt;group&gt;-&lt;version&gt;-edit</code></p></td>
<td style="text-align: left;"><p>Verbs on <code>&lt;kind&gt;</code>:</p>
<ul>
<li><p><code>create</code></p></li>
<li><p><code>update</code></p></li>
<li><p><code>patch</code></p></li>
<li><p><code>delete</code></p></li>
</ul>
<p>Aggregation labels:</p>
<ul>
<li><p><code>rbac.authorization.k8s.io/aggregate-to-edit: true</code></p></li>
<li><p><code>olm.opgroup.permissions/aggregate-to-edit: &lt;operatorgroup_name&gt;</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>&lt;kind&gt;.&lt;group&gt;-&lt;version&gt;-view</code></p></td>
<td style="text-align: left;"><p>Verbs on <code>&lt;kind&gt;</code>:</p>
<ul>
<li><p><code>get</code></p></li>
<li><p><code>list</code></p></li>
<li><p><code>watch</code></p></li>
</ul>
<p>Aggregation labels:</p>
<ul>
<li><p><code>rbac.authorization.k8s.io/aggregate-to-view: true</code></p></li>
<li><p><code>olm.opgroup.permissions/aggregate-to-view: &lt;operatorgroup_name&gt;</code></p></li>
</ul></td>
</tr>
</tbody>
</table>

<div id="olm-resources-additional-roles-rolebindings_olm-understanding-operatorgroups">

<div class="title">

Additional roles and role bindings

</div>

- If the CSV defines exactly one target namespace that contains `*`, then a cluster role and corresponding cluster role binding are generated for each permission defined in the `permissions` field of the CSV. All resources generated are given the `olm.owner: <csv_name>` and `olm.owner.namespace: <csv_namespace>` labels.

- If the CSV does *not* define exactly one target namespace that contains `*`, then all roles and role bindings in the Operator namespace with the `olm.owner: <csv_name>` and `olm.owner.namespace: <csv_namespace>` labels are copied into the target namespace.

</div>

# Copied CSVs

OLM creates copies of all active member CSVs of an Operator group in each of the target namespaces of that Operator group. The purpose of a copied CSV is to tell users of a target namespace that a specific Operator is configured to watch resources created there.

Copied CSVs have a status reason `Copied` and are updated to match the status of their source CSV. The `olm.targetNamespaces` annotation is stripped from copied CSVs before they are created on the cluster. Omitting the target namespace selection avoids the duplication of target namespaces between tenants.

Copied CSVs are deleted when their source CSV no longer exists or the Operator group that their source CSV belongs to no longer targets the namespace of the copied CSV.

> [!NOTE]
> By default, the `disableCopiedCSVs` field is disabled. After enabling a `disableCopiedCSVs` field, the OLM deletes existing copied CSVs on a cluster. When a `disableCopiedCSVs` field is disabled, the OLM adds copied CSVs again.
>
> - Disable the `disableCopiedCSVs` field:
>
>   ``` yaml
>   $ cat << EOF | oc apply -f -
>   apiVersion: operators.coreos.com/v1
>   kind: OLMConfig
>   metadata:
>     name: cluster
>   spec:
>     features:
>       disableCopiedCSVs: false
>   EOF
>   ```
>
> - Enable the `disableCopiedCSVs` field:
>
>   ``` yaml
>   $ cat << EOF | oc apply -f -
>   apiVersion: operators.coreos.com/v1
>   kind: OLMConfig
>   metadata:
>     name: cluster
>   spec:
>     features:
>       disableCopiedCSVs: true
>   EOF
>   ```

# Static Operator groups

An Operator group is *static* if its `spec.staticProvidedAPIs` field is set to `true`. As a result, OLM does not modify the `olm.providedAPIs` annotation of an Operator group, which means that it can be set in advance. This is useful when a user wants to use an Operator group to prevent resource contention in a set of namespaces but does not have active member CSVs that provide the APIs for those resources.

Below is an example of an Operator group that protects `Prometheus` resources in all namespaces with the `something.cool.io/cluster-monitoring: "true"` annotation:

``` yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: cluster-monitoring
  namespace: cluster-monitoring
  annotations:
    olm.providedAPIs: Alertmanager.v1.monitoring.coreos.com,Prometheus.v1.monitoring.coreos.com,PrometheusRule.v1.monitoring.coreos.com,ServiceMonitor.v1.monitoring.coreos.com
spec:
  staticProvidedAPIs: true
  selector:
    matchLabels:
      something.cool.io/cluster-monitoring: "true"
```

# Operator group intersection

Two Operator groups are said to have *intersecting provided APIs* if the intersection of their target namespace sets is not an empty set and the intersection of their provided API sets, defined by `olm.providedAPIs` annotations, is not an empty set.

A potential issue is that Operator groups with intersecting provided APIs can compete for the same resources in the set of intersecting namespaces.

> [!NOTE]
> When checking intersection rules, an Operator group namespace is always included as part of its selected target namespaces.

## Rules for intersection

Each time an active member CSV synchronizes, OLM queries the cluster for the set of intersecting provided APIs between the Operator group of the CSV and all others. OLM then checks if that set is an empty set:

- If `true` and the CSV’s provided APIs are a subset of the Operator group’s:

  - Continue transitioning.

- If `true` and the CSV’s provided APIs are *not* a subset of the Operator group’s:

  - If the Operator group is static:

    - Clean up any deployments that belong to the CSV.

    - Transition the CSV to a failed state with status reason `CannotModifyStaticOperatorGroupProvidedAPIs`.

  - If the Operator group is *not* static:

    - Replace the Operator group’s `olm.providedAPIs` annotation with the union of itself and the CSV’s provided APIs.

- If `false` and the CSV’s provided APIs are *not* a subset of the Operator group’s:

  - Clean up any deployments that belong to the CSV.

  - Transition the CSV to a failed state with status reason `InterOperatorGroupOwnerConflict`.

- If `false` and the CSV’s provided APIs are a subset of the Operator group’s:

  - If the Operator group is static:

    - Clean up any deployments that belong to the CSV.

    - Transition the CSV to a failed state with status reason `CannotModifyStaticOperatorGroupProvidedAPIs`.

  - If the Operator group is *not* static:

    - Replace the Operator group’s `olm.providedAPIs` annotation with the difference between itself and the CSV’s provided APIs.

> [!NOTE]
> Failure states caused by Operator groups are non-terminal.

The following actions are performed each time an Operator group synchronizes:

- The set of provided APIs from active member CSVs is calculated from the cluster. Note that copied CSVs are ignored.

- The cluster set is compared to `olm.providedAPIs`, and if `olm.providedAPIs` contains any extra APIs, then those APIs are pruned.

- All CSVs that provide the same APIs across all namespaces are requeued. This notifies conflicting CSVs in intersecting groups that their conflict has possibly been resolved, either through resizing or through deletion of the conflicting CSV.

# Limitations for multitenant Operator management

OpenShift Container Platform provides limited support for simultaneously installing different versions of an Operator on the same cluster. Operator Lifecycle Manager (OLM) installs Operators multiple times in different namespaces. One constraint of this is that the Operator’s API versions must be the same.

Operators are control plane extensions due to their usage of `CustomResourceDefinition` objects (CRDs), which are global resources in Kubernetes. Different major versions of an Operator often have incompatible CRDs. This makes them incompatible to install simultaneously in different namespaces on a cluster.

All tenants, or namespaces, share the same control plane of a cluster. Therefore, tenants in a multitenant cluster also share global CRDs, which limits the scenarios in which different instances of the same Operator can be used in parallel on the same cluster.

The supported scenarios include the following:

- Operators of different versions that ship the exact same CRD definition (in case of versioned CRDs, the exact same set of versions)

- Operators of different versions that do not ship a CRD, and instead have their CRD available in a separate bundle in the software catalog

All other scenarios are not supported, because the integrity of the cluster data cannot be guaranteed if there are multiple competing or overlapping CRDs from different Operator versions to be reconciled on the same cluster.

<div>

<div class="title">

Additional resources

</div>

- [Operator Lifecycle Manager (OLM) → Multitenancy and Operator colocation](olm-colocation.md#olm-colocation)

- [Operators in multitenant clusters](../olm-multitenancy.md#olm-multitenancy)

- [Allowing non-cluster administrators to install Operators](../../admin/olm-creating-policy.md#olm-creating-policy)

</div>

# Troubleshooting Operator groups

## Membership

- An install plan’s namespace must contain only one Operator group. When attempting to generate a cluster service version (CSV) in a namespace, an install plan considers an Operator group invalid in the following scenarios:

  - No Operator groups exist in the install plan’s namespace.

  - Multiple Operator groups exist in the install plan’s namespace.

  - An incorrect or non-existent service account name is specified in the Operator group.

  If an install plan encounters an invalid Operator group, the CSV is not generated and the `InstallPlan` resource continues to install with a relevant message. For example, the following message is provided if more than one Operator group exists in the same namespace:

  ``` terminal
  attenuated service account query failed - more than one operator group(s) are managing this namespace count=2
  ```

  where `count=` specifies the number of Operator groups in the namespace.

- If the install modes of a CSV do not support the target namespace selection of the Operator group in its namespace, the CSV transitions to a failure state with the reason `UnsupportedOperatorGroup`. CSVs in a failed state for this reason transition to pending after either the target namespace selection of the Operator group changes to a supported configuration, or the install modes of the CSV are modified to support the target namespace selection.
