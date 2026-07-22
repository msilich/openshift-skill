<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform, you can use security context constraints (SCCs) to control permissions for the pods in your cluster.

Default SCCs are created during installation and when you install some Operators or other components. As a cluster administrator, you can also create your own SCCs by using the OpenShift CLI (`oc`).

> [!IMPORTANT]
> Do not modify the default SCCs. Customizing the default SCCs can lead to issues when some of the platform pods deploy or OpenShift Container Platform is upgraded. Additionally, the default SCC values are reset to the defaults during some cluster upgrades, which discards all customizations to those SCCs.
>
> Instead of modifying the default SCCs, create and modify your own SCCs as needed. For detailed steps, see [Creating security context constraints](managing-security-context-constraints.md#security-context-constraints-creating_configuring-internal-oauth).

# About security context constraints

Similar to the way that RBAC resources control user access, administrators can use security context constraints (SCCs) to control permissions for pods. These permissions determine the actions that a pod can perform and what resources it can access. You can use SCCs to define a set of conditions that a pod must run with to be accepted into the system.

Security context constraints allow an administrator to control:

- Whether a pod can run privileged containers with the `allowPrivilegedContainer` flag

- Whether a pod is constrained with the `allowPrivilegeEscalation` flag

- The capabilities that a container can request

- The use of host directories as volumes

- The SELinux context of the container

- The container user ID

- The use of host namespaces and networking

- The allocation of an `FSGroup` that owns the pod volumes

- The configuration of allowable supplemental groups

- Whether a container requires write access to its root file system

- The usage of volume types

- The configuration of allowable `seccomp` profiles

> [!IMPORTANT]
> Do not set the `openshift.io/run-level` label on any namespaces in OpenShift Container Platform. This label is for use by internal OpenShift Container Platform components to manage the startup of major API groups, such as the Kubernetes API server and OpenShift API server. If the `openshift.io/run-level` label is set, no SCCs are applied to pods in that namespace, causing any workloads running in that namespace to be highly privileged.

## Default security context constraints

The cluster contains several default security context constraints (SCCs) as described in the table below. Additional SCCs might be installed when you install Operators or other components to OpenShift Container Platform.

> [!IMPORTANT]
> Do not modify the default SCCs. Customizing the default SCCs can lead to issues when some of the platform pods deploy or OpenShift Container Platform is upgraded. Additionally, the default SCC values are reset to the defaults during some cluster upgrades, which discards all customizations to those SCCs.
>
> Instead of modifying the default SCCs, create and modify your own SCCs as needed. For detailed steps, see *Creating security context constraints*.

<table>
<caption>Default security context constraints</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Security context constraint</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>anyuid</code></p></td>
<td style="text-align: left;"><p>Provides all features of the <code>restricted</code> SCC, but allows users to run with any UID and any GID.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostaccess</code></p></td>
<td style="text-align: left;"><p>Allows access to all host namespaces but still requires pods to be run with a UID and SELinux context that are allocated to the namespace.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>This SCC allows host access to namespaces, file systems, and PIDs. It should only be used by trusted pods. Grant with caution.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostmount-anyuid</code></p></td>
<td style="text-align: left;"><p>Provides all the features of the <code>restricted</code> SCC, but allows host mounts and running as any UID and any GID on the system.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>This SCC allows host file system access as any UID, including UID 0. Grant with caution.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostnetwork</code></p></td>
<td style="text-align: left;"><p>Allows using host networking and host ports but still requires pods to be run with a UID and SELinux context that are allocated to the namespace.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>If additional workloads are run on control plane hosts, use caution when providing access to <code>hostnetwork</code>. A workload that runs <code>hostnetwork</code> on a control plane host is effectively root on the cluster and must be trusted accordingly.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostnetwork-v2</code></p></td>
<td style="text-align: left;"><p>Like the <code>hostnetwork</code> SCC, but with the following differences:</p>
<ul>
<li><p><code>ALL</code> capabilities are dropped from containers.</p></li>
<li><p>The <code>NET_BIND_SERVICE</code> capability can be added explicitly.</p></li>
<li><p><code>seccompProfile</code> is set to <code>runtime/default</code> by default.</p></li>
<li><p><code>allowPrivilegeEscalation</code> must be unset or set to <code>false</code> in security contexts.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nested-container</code></p></td>
<td style="text-align: left;"><p>Like the <code>restricted-v2</code> SCC, but with the following differences:</p>
<ul>
<li><p><code>seLinuxContext</code> is set to <code>MustRunAs</code> and <code>seLinuxOptions.type</code> is <code>container_engine_t</code>.</p></li>
<li><p><code>runAsUser</code> is set to <code>MustRunAsRange</code>.</p></li>
<li><p><code>requiredDropCapabilities</code> is set to <code>null</code>.</p></li>
<li><p><code>userNamespaceLevel</code> is set to <code>RequirePodLevel</code>, which forces pods to be in a Linux user namespace (<code>hostUsers: false</code>).</p></li>
</ul>
<p>This SCC allows a user to run a container engine inside of an OpenShift Container Platform pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>node-exporter</code></p></td>
<td style="text-align: left;"><p>Used for the Prometheus node exporter.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>This SCC allows host file system access as any UID, including UID 0. Grant with caution.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nonroot</code></p></td>
<td style="text-align: left;"><p>Provides all features of the <code>restricted</code> SCC, but allows users to run with any non-root UID. The user must specify the UID or it must be specified in the manifest of the container runtime.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nonroot-v2</code></p></td>
<td style="text-align: left;"><p>Like the <code>nonroot</code> SCC, but with the following differences:</p>
<ul>
<li><p><code>ALL</code> capabilities are dropped from containers.</p></li>
<li><p>The <code>NET_BIND_SERVICE</code> capability can be added explicitly.</p></li>
<li><p><code>seccompProfile</code> is set to <code>runtime/default</code> by default.</p></li>
<li><p><code>allowPrivilegeEscalation</code> must be unset or set to <code>false</code> in security contexts.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>privileged</code></p></td>
<td style="text-align: left;"><p>Allows access to all privileged and host features and the ability to run as any user, any group, any FSGroup, and with any SELinux context.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>This is the most relaxed SCC and should be used only for cluster administration. Grant with caution.</p>
</div>
<p>The <code>privileged</code> SCC allows:</p>
<ul>
<li><p>Users to run privileged pods</p></li>
<li><p>Pods to mount host directories as volumes</p></li>
<li><p>Pods to run as any user</p></li>
<li><p>Pods to run with any MCS label</p></li>
<li><p>Pods to use the host’s IPC namespace</p></li>
<li><p>Pods to use the host’s PID namespace</p></li>
<li><p>Pods to use any FSGroup</p></li>
<li><p>Pods to use any supplemental group</p></li>
<li><p>Pods to use any seccomp profiles</p></li>
<li><p>Pods to request any capabilities</p></li>
</ul>
<div class="note">
<div class="title">
&#10;</div>
<p>Setting <code>privileged: true</code> in the pod specification does not necessarily select the <code>privileged</code> SCC. The SCC that has <code>allowPrivilegedContainer: true</code> and has the highest prioritization will be chosen if the user has the permissions to use it.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>restricted</code></p></td>
<td style="text-align: left;"><p>Denies access to all host features and requires pods to be run with a UID, and SELinux context that are allocated to the namespace.</p>
<p>The <code>restricted</code> SCC:</p>
<ul>
<li><p>Ensures that pods cannot run as privileged</p></li>
<li><p>Ensures that pods cannot mount host directory volumes</p></li>
<li><p>Requires that a pod is run as a user in a pre-allocated range of UIDs</p></li>
<li><p>Requires that a pod is run with a pre-allocated MCS label</p></li>
<li><p>Requires that a pod is run with a preallocated FSGroup</p></li>
<li><p>Allows pods to use any supplemental group</p></li>
</ul>
<p>In clusters that were upgraded from OpenShift Container Platform 4.10 or earlier, this SCC is available for use by any authenticated user. The <code>restricted</code> SCC is no longer available to users of new OpenShift Container Platform 4.11 or later installations, unless the access is explicitly granted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>restricted-v2</code></p></td>
<td style="text-align: left;"><p>Like the <code>restricted</code> SCC, but with the following differences:</p>
<ul>
<li><p><code>ALL</code> capabilities are dropped from containers.</p></li>
<li><p>The <code>NET_BIND_SERVICE</code> capability can be added explicitly.</p></li>
<li><p><code>seccompProfile</code> is set to <code>runtime/default</code> by default.</p></li>
<li><p><code>allowPrivilegeEscalation</code> must be unset or set to <code>false</code> in security contexts.</p></li>
</ul>
<p>This SCC is used by default for authenticated users.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>restricted-v3</code></p></td>
<td style="text-align: left;"><p>Like the <code>restricted-v2</code> SCC, but with the following differences:</p>
<ul>
<li><p><code>UserNamespaceLevel</code> is set to <code>RequirePodLevel</code>, which forces pods to be in a Linux user namespace (<code>hostUsers: false</code>).</p></li>
</ul>
<p>This is the most restrictive SCC provided by a new installation and will be used by default for authenticated users.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>The <code>restricted-v3</code> SCC is the most restrictive of the SCCs that is included by default with the system. However, you can create a custom SCC that is even more restrictive. For example, you can create an SCC that restricts <code>readOnlyRootFilesystem</code> to <code>true</code>.</p>
</div></td>
</tr>
</tbody>
</table>

## Security context constraints settings

Security context constraints (SCCs) are composed of settings and strategies that control the security features a pod has access to. These settings fall into three categories:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Category</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Controlled by a boolean</p></td>
<td style="text-align: left;"><p>Fields of this type default to the most restrictive value. For example, <code>AllowPrivilegedContainer</code> is always set to <code>false</code> if unspecified.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Controlled by an allowable set</p></td>
<td style="text-align: left;"><p>Fields of this type are checked against the set to ensure their value is allowed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Controlled by a strategy</p></td>
<td style="text-align: left;"><p>Items that have a strategy to generate a value provide:</p>
<ul>
<li><p>A mechanism to generate the value, and</p></li>
<li><p>A mechanism to ensure that a specified value falls into the set of allowable values.</p></li>
</ul></td>
</tr>
</tbody>
</table>

CRI-O has the following default list of capabilities that are allowed for each container of a pod:

- `CHOWN`

- `DAC_OVERRIDE`

- `FSETID`

- `FOWNER`

- `SETGID`

- `SETUID`

- `SETPCAP`

- `NET_BIND_SERVICE`

- `KILL`

The containers use the capabilities from this default list, but pod manifest authors can alter the list by requesting additional capabilities or removing some of the default behaviors. Use the `allowedCapabilities`, `defaultAddCapabilities`, and `requiredDropCapabilities` parameters to control such requests from the pods. With these parameters you can specify which capabilities can be requested, which ones must be added to each container, and which ones must be forbidden, or dropped, from each container.

> [!NOTE]
> You can drop all capabilites from containers by setting the `requiredDropCapabilities` parameter to `ALL`. This is what the `restricted-v2` SCC does.

## Security context constraints strategies

<div>

<div class="title">

RunAsUser

</div>

- `MustRunAs` - Requires a `runAsUser` to be configured. Uses the configured `runAsUser` as the default. Validates against the configured `runAsUser`.

  <div class="formalpara">

  <div class="title">

  Example `MustRunAs` snippet

  </div>

  ``` yaml
  ...
  runAsUser:
    type: MustRunAs
    uid: <id>
  ...
  ```

  </div>

- `MustRunAsRange` - Requires minimum and maximum values to be defined if not using pre-allocated values. Uses the minimum as the default. Validates against the entire allowable range.

  <div class="formalpara">

  <div class="title">

  Example `MustRunAsRange` snippet

  </div>

  ``` yaml
  ...
  runAsUser:
    type: MustRunAsRange
    uidRangeMax: <maxvalue>
    uidRangeMin: <minvalue>
  ...
  ```

  </div>

- `MustRunAsNonRoot` - Requires that the pod be submitted with a non-zero `runAsUser` or have the `USER` directive defined in the image. No default provided.

  <div class="formalpara">

  <div class="title">

  Example `MustRunAsNonRoot` snippet

  </div>

  ``` yaml
  ...
  runAsUser:
    type: MustRunAsNonRoot
  ...
  ```

  </div>

- `RunAsAny` - No default provided. Allows any `runAsUser` to be specified.

  <div class="formalpara">

  <div class="title">

  Example `RunAsAny` snippet

  </div>

  ``` yaml
  ...
  runAsUser:
    type: RunAsAny
  ...
  ```

  </div>

</div>

<div>

<div class="title">

SELinuxContext

</div>

- `MustRunAs` - Requires `seLinuxOptions` to be configured if not using pre-allocated values. Uses `seLinuxOptions` as the default. Validates against `seLinuxOptions`.

- `RunAsAny` - No default provided. Allows any `seLinuxOptions` to be specified.

</div>

<div>

<div class="title">

SupplementalGroups

</div>

- `MustRunAs` - Requires at least one range to be specified if not using pre-allocated values. Uses the minimum value of the first range as the default. Validates against all ranges.

- `RunAsAny` - No default provided. Allows any `supplementalGroups` to be specified.

</div>

<div>

<div class="title">

FSGroup

</div>

- `MustRunAs` - Requires at least one range to be specified if not using pre-allocated values. Uses the minimum value of the first range as the default. Validates against the first ID in the first range.

- `RunAsAny` - No default provided. Allows any `fsGroup` ID to be specified.

</div>

## Controlling volumes

The usage of specific volume types can be controlled by setting the `volumes` field of the SCC.

The allowable values of this field correspond to the volume sources that are defined when creating a volume:

- [`awsElasticBlockStore`](https://kubernetes.io/docs/concepts/storage/volumes/#awselasticblockstore)

- [`azureDisk`](https://kubernetes.io/docs/concepts/storage/volumes/#azuredisk)

- [`azureFile`](https://kubernetes.io/docs/concepts/storage/volumes/#azurefile)

- [`cephFS`](https://kubernetes.io/docs/concepts/storage/volumes/#cephfs)

- [`cinder`](https://kubernetes.io/docs/concepts/storage/volumes/#cinder)

- [`configMap`](https://kubernetes.io/docs/concepts/storage/volumes/#configmap)

- [`csi`](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#csi-ephemeral-volumes)

- [`downwardAPI`](https://kubernetes.io/docs/concepts/storage/volumes/#downwardapi)

- [`emptyDir`](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir)

- [`fc`](https://kubernetes.io/docs/concepts/storage/volumes/#fc)

- [`flexVolume`](https://kubernetes.io/docs/concepts/storage/volumes/#flexvolume)

- [`flocker`](https://kubernetes.io/docs/concepts/storage/volumes/#flocker)

- [`gcePersistentDisk`](https://kubernetes.io/docs/concepts/storage/volumes/#gcepersistentdisk)

- [`ephemeral`](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes)

- [`gitRepo`](https://kubernetes.io/docs/concepts/storage/volumes/#gitrepo)

- [`glusterfs`](https://kubernetes.io/docs/concepts/storage/volumes/#glusterfs)

- [`hostPath`](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath)

- [`iscsi`](https://kubernetes.io/docs/concepts/storage/volumes/#iscsi)

- [`nfs`](https://kubernetes.io/docs/concepts/storage/volumes/#nfs)

- [`persistentVolumeClaim`](https://kubernetes.io/docs/concepts/storage/volumes/#persistentvolumeclaim)

- `photonPersistentDisk`

- [`portworxVolume`](https://kubernetes.io/docs/concepts/storage/volumes/#portworxvolume)

- [`projected`](https://kubernetes.io/docs/concepts/storage/volumes/#projected)

- [`quobyte`](https://kubernetes.io/docs/concepts/storage/volumes/#quobyte)

- [`rbd`](https://kubernetes.io/docs/concepts/storage/volumes/#rbd)

- [`scaleIO`](https://kubernetes.io/docs/concepts/storage/volumes/#scaleio)

- [`secret`](https://kubernetes.io/docs/concepts/storage/volumes/#secret)

- [`storageos`](https://kubernetes.io/docs/concepts/storage/volumes/#storageos)

- [`vsphereVolume`](https://kubernetes.io/docs/concepts/storage/volumes/#vspherevolume)

- **\*** (A special value to allow the use of all volume types.)

- `none` (A special value to disallow the use of all volumes types. Exists only for backwards compatibility.)

The recommended minimum set of allowed volumes for new SCCs are `configMap`, `downwardAPI`, `emptyDir`, `persistentVolumeClaim`, `secret`, and `projected`.

> [!NOTE]
> This list of allowable volume types is not exhaustive because new types are added with each release of OpenShift Container Platform.

> [!NOTE]
> For backwards compatibility, the usage of `allowHostDirVolumePlugin` overrides settings in the `volumes` field. For example, if `allowHostDirVolumePlugin` is set to false but allowed in the `volumes` field, then the `hostPath` value will be removed from `volumes`.

## Admission control

*Admission control* with SCCs allows for control over the creation of resources based on the capabilities granted to a user.

In terms of the SCCs, this means that an admission controller can inspect the user information made available in the context to retrieve an appropriate set of SCCs. Doing so ensures the pod is authorized to make requests about its operating environment or to generate a set of constraints to apply to the pod.

The set of SCCs that admission uses to authorize a pod are determined by the user identity and groups that the user belongs to. Additionally, if the pod specifies a service account, the set of allowable SCCs includes any constraints accessible to the service account.

> [!NOTE]
> When you create a workload resource, such as deployment, only the service account is used to find the SCCs and admit the pods when they are created.

Admission uses the following approach to create the final security context for the pod:

1.  Retrieve all SCCs available for use.

2.  Generate field values for security context settings that were not specified on the request.

3.  Validate the final settings against the available constraints.

If a matching set of constraints is found, then the pod is accepted. If the request cannot be matched to an SCC, the pod is rejected.

A pod must validate every field against the SCC. The following are examples for just two of the fields that must be validated:

> [!NOTE]
> These examples are in the context of a strategy using the pre-allocated values.

**An FSGroup SCC strategy of `MustRunAs`**

If the pod defines a `fsGroup` ID, then that ID must equal the default `fsGroup` ID. Otherwise, the pod is not validated by that SCC and the next SCC is evaluated.

If the `SecurityContextConstraints.fsGroup` field has value `RunAsAny` and the pod specification omits the `Pod.spec.securityContext.fsGroup`, then this field is considered valid. Note that it is possible that during validation, other SCC settings will reject other pod fields and thus cause the pod to fail.

**A `SupplementalGroups` SCC strategy of `MustRunAs`**

If the pod specification defines one or more `supplementalGroups` IDs, then the pod’s IDs must equal one of the IDs in the namespace’s `openshift.io/sa.scc.supplemental-groups` annotation. Otherwise, the pod is not validated by that SCC and the next SCC is evaluated.

If the `SecurityContextConstraints.supplementalGroups` field has value `RunAsAny` and the pod specification omits the `Pod.spec.securityContext.supplementalGroups`, then this field is considered valid. Note that it is possible that during validation, other SCC settings will reject other pod fields and thus cause the pod to fail.

## Security context constraints prioritization

Security context constraints (SCCs) have a priority field that affects the ordering when attempting to validate a request by the admission controller.

> [!WARNING]
> Setting an SCC priority greater than 0 for the default OpenShift Container Platform SCCs can cause critical cluster instability.

A priority value of `0` is the lowest possible priority. A nil priority is considered a `0`, or lowest, priority. Higher priority SCCs are moved to the front of the set when sorting.

When the complete set of available SCCs is determined, the SCCs are ordered in the following manner:

1.  The highest priority SCCs are ordered first.

2.  If the priorities are equal, the SCCs are sorted from most restrictive to least restrictive.

3.  If both the priorities and restrictions are equal, the SCCs are sorted by name.

By default, the `anyuid` SCC granted to cluster administrators is given priority in their SCC set. This allows cluster administrators to run pods as any user by specifying `RunAsUser` in the pod’s `SecurityContext`.

# About pre-allocated security context constraints values

The admission controller is aware of certain conditions in the security context constraints (SCCs) that trigger it to look up pre-allocated values from a namespace and populate the SCC before processing the pod. Each SCC strategy is evaluated independently of other strategies, with the pre-allocated values, where allowed, for each policy aggregated with pod specification values to make the final values for the various IDs defined in the running pod.

The following SCCs cause the admission controller to look for pre-allocated values when no ranges are defined in the pod specification:

1.  A `RunAsUser` strategy of `MustRunAsRange` with no minimum or maximum set. Admission looks for the `openshift.io/sa.scc.uid-range` annotation to populate range fields.

2.  An `SELinuxContext` strategy of `MustRunAs` with no level set. Admission looks for the `openshift.io/sa.scc.mcs` annotation to populate the level.

3.  A `FSGroup` strategy of `MustRunAs`. Admission looks for the `openshift.io/sa.scc.supplemental-groups` annotation.

4.  A `SupplementalGroups` strategy of `MustRunAs`. Admission looks for the `openshift.io/sa.scc.supplemental-groups` annotation.

During the generation phase, the security context provider uses default values for any parameter values that are not specifically set in the pod. Default values are based on the selected strategy:

1.  `RunAsAny` and `MustRunAsNonRoot` strategies do not provide default values. If the pod needs a parameter value, such as a group ID, you must define the value in the pod specification.

2.  `MustRunAs` (single value) strategies provide a default value that is always used. For example, for group IDs, even if the pod specification defines its own ID value, the namespace’s default parameter value also appears in the pod’s groups.

3.  `MustRunAsRange` and `MustRunAs` (range-based) strategies provide the minimum value of the range. As with a single value `MustRunAs` strategy, the namespace’s default parameter value appears in the running pod. If a range-based strategy is configurable with multiple ranges, it provides the minimum value of the first configured range.

> [!NOTE]
> `FSGroup` and `SupplementalGroups` strategies fall back to the `openshift.io/sa.scc.uid-range` annotation if the `openshift.io/sa.scc.supplemental-groups` annotation does not exist on the namespace. If neither exists, the SCC is not created.

> [!NOTE]
> By default, the annotation-based `FSGroup` strategy configures itself with a single range based on the minimum value for the annotation. For example, if your annotation reads `1/3`, the `FSGroup` strategy configures itself with a minimum and maximum value of `1`. If you want to allow more groups to be accepted for the `FSGroup` field, you can configure a custom SCC that does not use the annotation.

> [!NOTE]
> The `openshift.io/sa.scc.supplemental-groups` annotation accepts a comma-delimited list of blocks in the format of `<start>/<length` or `<start>-<end>`. The `openshift.io/sa.scc.uid-range` annotation accepts only a single block.

# Example security context constraints

The following examples show the security context constraints (SCC) format and annotations:

<div class="formalpara">

<div class="title">

Annotated `privileged` SCC

</div>

``` yaml
allowHostDirVolumePlugin: true
allowHostIPC: true
allowHostNetwork: true
allowHostPID: true
allowHostPorts: true
allowPrivilegedContainer: true
allowedCapabilities:
- '*'
apiVersion: security.openshift.io/v1
defaultAddCapabilities: []
fsGroup:
  type: RunAsAny
groups:
- system:cluster-admins
- system:nodes
kind: SecurityContextConstraints
metadata:
  annotations:
    kubernetes.io/description: 'privileged allows access to all privileged and host
      features and the ability to run as any user, any group, any fsGroup, and with
      any SELinux context.  WARNING: this is the most relaxed SCC and should be used
      only for cluster administration. Grant with caution.'
  creationTimestamp: null
  name: privileged
priority: null
readOnlyRootFilesystem: false
requiredDropCapabilities: null
runAsUser:
  type: RunAsAny
seLinuxContext:
  type: RunAsAny
seccompProfiles:
- '*'
supplementalGroups:
  type: RunAsAny
users:
- system:serviceaccount:default:registry
- system:serviceaccount:default:router
- system:serviceaccount:openshift-infra:build-controller
volumes:
- '*'
```

</div>

- A list of capabilities that a pod can request. An empty list means that none of capabilities can be requested while the special symbol `*` allows any capabilities.

- A list of additional capabilities that are added to any pod.

- The `FSGroup` strategy, which dictates the allowable values for the security context.

- The groups that can access this SCC.

- A list of capabilities to drop from a pod. Or, specify `ALL` to drop all capabilities.

- The `runAsUser` strategy type, which dictates the allowable values for the security context.

- The `seLinuxContext` strategy type, which dictates the allowable values for the security context.

- The `supplementalGroups` strategy, which dictates the allowable supplemental groups for the security context.

- The users who can access this SCC.

- The allowable volume types for the security context. In the example, `*` allows the use of all volume types.

The `users` and `groups` fields on the SCC control which users can access the SCC. By default, cluster administrators, nodes, and the build controller are granted access to the privileged SCC. All authenticated users are granted access to the `restricted-v2` SCC.

> [!NOTE]
> When verifying access to an SCC, be aware of the following command behaviors:
>
> - The `oc adm policy who-can use scc <scc_name>` and `oc auth can-i use scc/<scc_name>` commands evaluate only RBAC policies (`RoleBinding` or `ClusterRoleBinding` resources). Their output does not include users or groups configured directly in the SCC `users` and `groups` fields.
>
> - The `oc describe scc <scc_name>` command displays only the users and groups configured directly within the SCC object. Its output does not include access granted through RBAC policies.

<div class="formalpara">

<div class="title">

Without explicit `runAsUser` setting

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo
spec:
  securityContext:
  containers:
  - name: sec-ctx-demo
    image: gcr.io/google-samples/node-hello:1.0
```

</div>

- When a container or pod does not request a user ID under which it should be run, the effective UID depends on the SCC that emits this pod. Because the `restricted-v2` SCC is granted to all authenticated users by default, it will be available to all users and service accounts and used in most cases. The `restricted-v2` SCC uses `MustRunAsRange` strategy for constraining and defaulting the possible values of the `securityContext.runAsUser` field. The admission plugin will look for the `openshift.io/sa.scc.uid-range` annotation on the current project to populate range fields, as it does not provide this range. In the end, a container will have `runAsUser` equal to the first value of the range that is hard to predict because every project has different ranges.

<div class="formalpara">

<div class="title">

With explicit `runAsUser` setting

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo
spec:
  securityContext:
    runAsUser: 1000
  containers:
    - name: sec-ctx-demo
      image: gcr.io/google-samples/node-hello:1.0
```

</div>

- A container or pod that requests a specific user ID will be accepted by OpenShift Container Platform only when a service account or a user is granted access to a SCC that allows such a user ID. The SCC can allow arbitrary IDs, an ID that falls into a range, or the exact user ID specific to the request.

This configuration is valid for SELinux, fsGroup, and Supplemental Groups.

# Creating security context constraints

If the default security context constraints (SCCs) do not satisfy your application workload requirements, you can create a custom SCC by using the OpenShift CLI (`oc`).

> [!IMPORTANT]
> Creating and modifying your own SCCs are advanced operations that might cause instability to your cluster. If you have questions about using your own SCCs, contact Red Hat Support. For information about contacting Red Hat support, see *Getting support*.

> [!WARNING]
> Setting an SCC priority greater than 0 for the default OpenShift Container Platform SCCs can cause critical cluster instability.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Define the SCC in a YAML file named `scc-admin.yaml`:

    ``` yaml
    kind: SecurityContextConstraints
    apiVersion: security.openshift.io/v1
    metadata:
      name: scc-admin
    allowPrivilegedContainer: true
    runAsUser:
      type: RunAsAny
    seLinuxContext:
      type: RunAsAny
    fsGroup:
      type: RunAsAny
    supplementalGroups:
      type: RunAsAny
    users:
    - my-admin-user
    groups:
    - my-admin-group
    ```

    Optionally, you can drop specific capabilities for an SCC by setting the `requiredDropCapabilities` field with the desired values. Any specified capabilities are dropped from the container. To drop all capabilities, specify `ALL`. For example, to create an SCC that drops the `KILL`, `MKNOD`, and `SYS_CHROOT` capabilities, add the following to the SCC object:

    ``` yaml
    requiredDropCapabilities:
    - KILL
    - MKNOD
    - SYS_CHROOT
    ```

    > [!NOTE]
    > You cannot list a capability in both `allowedCapabilities` and `requiredDropCapabilities`.

    CRI-O supports the same list of capability values that are found in the [Docker documentation](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities).

2.  Create the SCC by passing in the file:

    ``` terminal
    $ oc create -f scc-admin.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    securitycontextconstraints "scc-admin" created
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the SCC was created:

  ``` terminal
  $ oc get scc scc-admin
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME        PRIV      CAPS      SELINUX    RUNASUSER   FSGROUP    SUPGROUP   PRIORITY   READONLYROOTFS   VOLUMES
  scc-admin   true      []        RunAsAny   RunAsAny    RunAsAny   RunAsAny   <none>     false            [awsElasticBlockStore azureDisk azureFile cephFS cinder configMap downwardAPI emptyDir fc flexVolume flocker gcePersistentDisk gitRepo glusterfs iscsi nfs persistentVolumeClaim photonPersistentDisk quobyte rbd secret vsphere]
  ```

  </div>

</div>

# Configuring a workload to require a specific SCC

You can configure a workload to require a certain security context constraint (SCC). This is useful in scenarios where you want to pin a specific SCC to the workload or if you want to prevent your required SCC from being preempted by another SCC in the cluster.

To require a specific SCC, set the `openshift.io/required-scc` annotation on your workload. You can set this annotation on any resource that can set a pod manifest template, such as a deployment or daemon set.

The SCC must exist in the cluster and must be applicable to the workload, otherwise pod admission fails. An SCC is considered applicable to the workload if the user creating the pod or the pod’s service account has `use` permissions for the SCC in the pod’s namespace.

> [!WARNING]
> Do not change the `openshift.io/required-scc` annotation in the live pod’s manifest, because doing so causes the pod admission to fail. To change the required SCC, update the annotation in the underlying pod template, which causes the pod to be deleted and re-created.

<div>

<div class="title">

Prerequisites

</div>

- The SCC must exist in the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file for the deployment and specify a required SCC by setting the `openshift.io/required-scc` annotation:

    <div class="formalpara">

    <div class="title">

    Example `deployment.yaml`

    </div>

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Deployment
    apiVersion: apps/v1
    spec:
    # ...
      template:
        metadata:
          annotations:
            openshift.io/required-scc: "my-scc"
    # ...
    ```

    </div>

    - Specify the name of the SCC to require.

2.  Create the resource by running the following command:

    ``` terminal
    $ oc create -f deployment.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the deployment used the specified SCC:

  1.  View the value of the pod’s `openshift.io/scc` annotation by running the following command:

      ``` terminal
      $ oc get pod <pod_name> -o jsonpath='{.metadata.annotations.openshift\.io\/scc}{"\n"}'
      ```

      - Replace `<pod_name>` with the name of your deployment pod.

  2.  Examine the output and confirm that the displayed SCC matches the SCC that you defined in the deployment:

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      my-scc
      ```

      </div>

</div>

# Role-based access to security context constraints

You can specify SCCs as resources that are handled by RBAC. This allows you to scope access to your SCCs to a certain project or to the entire cluster. Assigning users, groups, or service accounts directly to an SCC retains cluster-wide scope.

> [!IMPORTANT]
> Do not run workloads in or share access to default projects. Default projects are reserved for running core cluster components.
>
> The following default projects are considered highly privileged: `default`, `kube-public`, `kube-system`, `openshift`, `openshift-infra`, `openshift-node`, and other system-created projects that have the `openshift.io/run-level` label set to `0` or `1`. Functionality that relies on admission plugins, such as pod security admission, security context constraints, cluster resource quotas, and image reference resolution, does not work in highly privileged projects.

To include access to SCCs for your role, specify the `scc` resource when creating a role.

``` terminal
$ oc create role <role-name> --verb=use --resource=scc --resource-name=<scc-name> -n <namespace>
```

This results in the following role definition:

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
...
  name: role-name
  namespace: namespace
...
rules:
- apiGroups:
  - security.openshift.io
  resourceNames:
  - scc-name
  resources:
  - securitycontextconstraints
  verbs:
  - use
```

- The role’s name.

- Namespace of the defined role. Defaults to `default` if not specified.

- The API group that includes the `SecurityContextConstraints` resource. Automatically defined when `scc` is specified as a resource.

- An example name for an SCC you want to have access.

- Name of the resource group that allows users to specify SCC names in the `resourceNames` field.

- A list of verbs to apply to the role.

A local or cluster role with such a rule allows the subjects that are bound to it with a role binding or a cluster role binding to use the user-defined SCC called `scc-name`.

> [!NOTE]
> Because RBAC is designed to prevent escalation, even project administrators are unable to grant access to an SCC. By default, they are not allowed to use the verb `use` on SCC resources, including the `restricted-v2` SCC.

# Reference of security context constraints commands

You can manage security context constraints (SCCs) in your instance as normal API objects by using the OpenShift CLI (`oc`).

> [!NOTE]
> You must have `cluster-admin` privileges to manage SCCs.

## Listing security context constraints

To get a current list of SCCs:

``` terminal
$ oc get scc
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
NAME                              PRIV    CAPS                   SELINUX     RUNASUSER          FSGROUP     SUPGROUP    PRIORITY     READONLYROOTFS   VOLUMES
anyuid                            false   <no value>             MustRunAs   RunAsAny           RunAsAny    RunAsAny    10           false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
hostaccess                        false   <no value>             MustRunAs   MustRunAsRange     MustRunAs   RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","hostPath","persistentVolumeClaim","projected","secret"]
hostmount-anyuid                  false   <no value>             MustRunAs   RunAsAny           RunAsAny    RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","hostPath","nfs","persistentVolumeClaim","projected","secret"]
hostnetwork                       false   <no value>             MustRunAs   MustRunAsRange     MustRunAs   MustRunAs   <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
hostnetwork-v2                    false   ["NET_BIND_SERVICE"]   MustRunAs   MustRunAsRange     MustRunAs   MustRunAs   <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
node-exporter                     true    <no value>             RunAsAny    RunAsAny           RunAsAny    RunAsAny    <no value>   false            ["*"]
nonroot                           false   <no value>             MustRunAs   MustRunAsNonRoot   RunAsAny    RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
nonroot-v2                        false   ["NET_BIND_SERVICE"]   MustRunAs   MustRunAsNonRoot   RunAsAny    RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
privileged                        true    ["*"]                  RunAsAny    RunAsAny           RunAsAny    RunAsAny    <no value>   false            ["*"]
restricted                        false   <no value>             MustRunAs   MustRunAsRange     MustRunAs   RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
restricted-v2                     false   ["NET_BIND_SERVICE"]   MustRunAs   MustRunAsRange     MustRunAs   RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
```

</div>

## Examining security context constraints

You can view information about a particular SCC, including which users, service accounts, and groups the SCC is applied to.

For example, to examine the `restricted` SCC:

``` terminal
$ oc describe scc restricted
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
Name:                                  restricted
Priority:                              <none>
Access:
  Users:                               <none>
  Groups:                              <none>
Settings:
  Allow Privileged:                    false
  Allow Privilege Escalation:          true
  Default Add Capabilities:            <none>
  Required Drop Capabilities:          KILL,MKNOD,SETUID,SETGID
  Allowed Capabilities:                <none>
  Allowed Seccomp Profiles:            <none>
  Allowed Volume Types:                configMap,downwardAPI,emptyDir,persistentVolumeClaim,projected,secret
  Allowed Flexvolumes:                 <all>
  Allowed Unsafe Sysctls:              <none>
  Forbidden Sysctls:                   <none>
  Allow Host Network:                  false
  Allow Host Ports:                    false
  Allow Host PID:                      false
  Allow Host IPC:                      false
  Read Only Root Filesystem:           false
  Run As User Strategy: MustRunAsRange
    UID:                               <none>
    UID Range Min:                     <none>
    UID Range Max:                     <none>
  SELinux Context Strategy: MustRunAs
    User:                              <none>
    Role:                              <none>
    Type:                              <none>
    Level:                             <none>
  FSGroup Strategy: MustRunAs
    Ranges:                            <none>
  Supplemental Groups Strategy: RunAsAny
    Ranges:                            <none>
```

</div>

- Lists which users and service accounts the SCC is applied to.

- Lists which groups the SCC is applied to.

> [!NOTE]
> To preserve customized SCCs during upgrades, do not edit settings on the default SCCs.

## Updating security context constraints

If your custom SCC no longer satisfies your application workloads requirements, you can update your SCC by using the OpenShift CLI (`oc`).

To update an existing SCC:

``` terminal
$ oc edit scc <scc_name>
```

> [!IMPORTANT]
> To preserve customized SCCs during upgrades, do not edit settings on the default SCCs.

## Deleting security context constraints

If you no longer require your custom SCC, you can delete the SCC by using the OpenShift CLI (`oc`).

To delete an SCC:

``` terminal
$ oc delete scc <scc_name>
```

> [!IMPORTANT]
> Do not delete default SCCs. If you delete a default SCC, it is regenerated by the Cluster Version Operator.

# Additional resources

- [Getting support](../support/getting-support.md#getting-support)
