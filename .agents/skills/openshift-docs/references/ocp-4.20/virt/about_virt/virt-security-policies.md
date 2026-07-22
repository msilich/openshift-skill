<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Virtualization provides built-in security features and authorization policies to protect virtual machine workloads and ensure secure cluster operations across your environment.

**Key points**

- OpenShift Virtualization adheres to the `restricted` Kubernetes pod security standards profile, which aims to enforce the current best practices for pod security.

- Virtual machine (VM) workloads run as unprivileged pods.

- Security context constraints (SCCs) are defined for the `kubevirt-controller` service account. For more information about SSCs, see "Additional resources".

- TLS certificates for OpenShift Virtualization components are renewed and rotated automatically.

# About workload security

By default, virtual machine (VM) workloads do not run with root privileges in OpenShift Virtualization, and there are no supported OpenShift Virtualization features that require root privileges.

For each VM, a `virt-launcher` pod runs an instance of `libvirt` in *session mode* to manage the VM process. In session mode, the `libvirt` daemon runs as a non-root user account and only permits connections from clients that are running under the same user identifier (UID). Therefore, VMs run as unprivileged pods, adhering to the security principle of least privilege.

# TLS certificates

TLS certificates for OpenShift Virtualization components are renewed and rotated automatically. You are not required to refresh them manually.

## Automatic renewal schedules

TLS certificates are automatically deleted and replaced according to the following schedule:

- KubeVirt certificates are renewed daily.

- Containerized Data Importer controller (CDI) certificates are renewed every 15 days.

- MAC pool certificates are renewed every year.

Automatic TLS certificate rotation does not disrupt any operations. For example, the following operations continue to function without any disruption:

- Migrations

- Image uploads

- VNC and console connections

# Authorization

OpenShift Virtualization uses role-based access control (RBAC) to define permissions for human users and service accounts. The permissions defined for service accounts control the actions that OpenShift Virtualization components can perform.

You can also use RBAC roles to manage user access to virtualization features. For example, an administrator can create an RBAC role that provides the permissions required to launch a virtual machine. The administrator can then restrict access by binding the role to specific users.

## Default cluster roles for OpenShift Virtualization

By using cluster role aggregation, OpenShift Virtualization extends the default OpenShift Container Platform cluster roles to include permissions for accessing virtualization objects. Roles unique to OpenShift Virtualization are not aggregated with OpenShift Container Platform roles.

| Default cluster role | OpenShift Virtualization cluster role | OpenShift Virtualization cluster role description |
|----|----|----|
| `view` | `kubevirt.io:view` | A user that can view all OpenShift Virtualization resources in the cluster but cannot create, delete, modify, or access them. For example, the user can see that a virtual machine (VM) is running but cannot shut it down or gain access to its console. |
| `edit` | `kubevirt.io:edit` | A user that can modify all OpenShift Virtualization resources in the cluster. For example, the user can create VMs, access VM consoles, and delete VMs. |
| `admin` | `kubevirt.io:admin` | A user that has full permissions to all OpenShift Virtualization resources, including the ability to delete collections of resources. The user can also view and modify the OpenShift Virtualization runtime configuration, which is located in the `HyperConverged` custom resource in the `openshift-cnv` namespace. |
| `N/A` | `kubevirt.io:migrate` | A user that can create, delete, and update VM live migration requests, which are represented by namespaced `VirtualMachineInstanceMigration` (VMIM) objects. This role is specific to OpenShift Virtualization. |

OpenShift Virtualization cluster roles

## RBAC roles for storage features in OpenShift Virtualization

Cluster-wide and namespaced RBAC roles enable the Containerized Data Importer (CDI) to manage storage resources, data volumes, and virtual machine disk operations.

### Cluster-wide RBAC roles

| CDI cluster role | Resources | Verbs |
|----|----|----|
| `cdi.kubevirt.io:admin` | `datavolumes`, `uploadtokenrequests` | `*` (all) |
| `datavolumes/source` | `create` |  |
| `cdi.kubevirt.io:edit` | `datavolumes`, `uploadtokenrequests` | `*` |
| `datavolumes/source` | `create` |  |
| `cdi.kubevirt.io:view` | `cdiconfigs`, `dataimportcrons`, `datasources`, `datavolumes`, `objecttransfers`, `storageprofiles`, `volumeimportsources`, `volumeuploadsources`, `volumeclonesources` | `get`, `list`, `watch` |
| `datavolumes/source` | `create` |  |
| `cdi.kubevirt.io:config-reader` | `cdiconfigs`, `storageprofiles` | `get`, `list`, `watch` |

Aggregated cluster roles for the `cdi.kubevirt.io` API group

<table>
<caption>Cluster-wide roles for the <code>cdi-operator</code> service account</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">API group</th>
<th style="text-align: left;">Resources</th>
<th style="text-align: left;">Verbs</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>rbac.authorization.k8s.io</code></p></td>
<td style="text-align: left;"><p><code>clusterrolebindings</code>, <code>clusterroles</code></p></td>
<td style="text-align: left;"><p><code>get</code>, <code>list</code>, <code>watch</code>, <code>create</code>, <code>update</code>, <code>delete</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>security.openshift.io</code></p></td>
<td style="text-align: left;"><p><code>securitycontextconstraints</code></p></td>
<td style="text-align: left;"><p><code>get</code>, <code>list</code>, <code>watch</code>, <code>update</code>, <code>create</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>apiextensions.k8s.io</code></p></td>
<td style="text-align: left;"><p><code>customresourcedefinitions</code>, <code>customresourcedefinitions/status</code></p></td>
<td style="text-align: left;"><p><code>get</code>, <code>list</code>, <code>watch</code>, <code>create</code>, <code>update</code>, <code>delete</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cdi.kubevirt.io</code></p></td>
<td style="text-align: left;"><p><code>*</code></p></td>
<td style="text-align: left;"><p><code>*</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>upload.cdi.kubevirt.io</code></p></td>
<td style="text-align: left;"><p><code>*</code></p></td>
<td style="text-align: left;"><p><code>*</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionregistration.k8s.io</code></p></td>
<td style="text-align: left;"><p><code>validatingwebhookconfigurations</code>, <code>mutatingwebhookconfigurations</code></p></td>
<td style="text-align: left;"><p><code>create</code>, <code>list</code>, <code>watch</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionregistration.k8s.io</code></p></td>
<td style="text-align: left;"><p><code>validatingwebhookconfigurations</code></p>
<p>Allow list: <code>cdi-api-dataimportcron-validate, cdi-api-populator-validate, cdi-api-datavolume-validate, cdi-api-validate, objecttransfer-api-validate</code></p></td>
<td style="text-align: left;"><p><code>get</code>, <code>update</code>, <code>delete</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>admissionregistration.k8s.io</code></p></td>
<td style="text-align: left;"><p><code>mutatingwebhookconfigurations</code></p>
<p>Allow list: <code>cdi-api-datavolume-mutate</code></p></td>
<td style="text-align: left;"><p><code>get</code>, <code>update</code>, <code>delete</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>apiregistration.k8s.io</code></p></td>
<td style="text-align: left;"><p><code>apiservices</code></p></td>
<td style="text-align: left;"><p><code>get</code>, <code>list</code>, <code>watch</code>, <code>create</code>, <code>update</code>, <code>delete</code></p></td>
</tr>
</tbody>
</table>

| API group | Resources | Verbs |
|----|----|----|
| `""` (core) | `events` | `create`, `patch` |
| `""` (core) | `persistentvolumeclaims` | `get`, `list`, `watch`, `create`, `update`, `delete`, `deletecollection`, `patch` |
| `""` (core) | `persistentvolumes` | `get`, `list`, `watch`, `update` |
| `""` (core) | `persistentvolumeclaims/finalizers`, `pods/finalizers` | `update` |
| `""` (core) | `pods`, `services` | `get`, `list`, `watch`, `create`, `delete` |
| `""` (core) | `configmaps` | `get`, `create` |
| `storage.k8s.io` | `storageclasses`, `csidrivers` | `get`, `list`, `watch` |
| `config.openshift.io` | `proxies` | `get`, `list`, `watch` |
| `cdi.kubevirt.io` | `*` | `*` |
| `snapshot.storage.k8s.io` | `volumesnapshots`, `volumesnapshotclasses`, `volumesnapshotcontents` | `get`, `list`, `watch`, `create`, `delete` |
| `snapshot.storage.k8s.io` | `volumesnapshots` | `update`, `deletecollection` |
| `apiextensions.k8s.io` | `customresourcedefinitions` | `get`, `list`, `watch` |
| `scheduling.k8s.io` | `priorityclasses` | `get`, `list`, `watch` |
| `image.openshift.io` | `imagestreams` | `get`, `list`, `watch` |
| `""` (core) | `secrets` | `create` |
| `kubevirt.io` | `virtualmachines/finalizers` | `update` |

Cluster-wide roles for the `cdi-controller` service account

### Namespaced RBAC roles

| API group | Resources | Verbs |
|----|----|----|
| `rbac.authorization.k8s.io` | `rolebindings`, `roles` | `get`, `list`, `watch`, `create`, `update`, `delete` |
| `""` (core) | `serviceaccounts`, `configmaps`, `events`, `secrets`, `services` | `get`, `list`, `watch`, `create`, `update`, `patch`, `delete` |
| `apps` | `deployments`, `deployments/finalizers` | `get`, `list`, `watch`, `create`, `update`, `delete` |
| `route.openshift.io` | `routes`, `routes/custom-host` | `get`, `list`, `watch`, `create`, `update` |
| `config.openshift.io` | `proxies` | `get`, `list`, `watch` |
| `monitoring.coreos.com` | `servicemonitors`, `prometheusrules` | `get`, `list`, `watch`, `create`, `delete`, `update`, `patch` |
| `coordination.k8s.io` | `leases` | `get`, `create`, `update` |

Namespaced roles for the `cdi-operator` service account

| API group | Resources | Verbs |
|----|----|----|
| `""` (core) | `configmaps` | `get`, `list`, `watch`, `create`, `update`, `delete` |
| `""` (core) | `secrets` | `get`, `list`, `watch` |
| `batch` | `cronjobs` | `get`, `list`, `watch`, `create`, `update`, `delete` |
| `batch` | `jobs` | `create`, `delete`, `list`, `watch` |
| `coordination.k8s.io` | `leases` | `get`, `create`, `update` |
| `networking.k8s.io` | `ingresses` | `get`, `list`, `watch` |
| `route.openshift.io` | `routes` | `get`, `list`, `watch` |

Namespaced roles for the `cdi-controller` service account

## Additional SCCs and permissions for the kubevirt-controller service account

Security context constraints (SCCs) control permissions for pods. These permissions include actions that a pod, a collection of containers, can perform and what resources it can access. You can use SCCs to define a set of conditions that a pod must run with to be accepted into the system.

The `virt-controller` is a cluster controller that creates the `virt-launcher` pods for virtual machines in the cluster.

> [!NOTE]
> By default, `virt-launcher` pods run with the `default` service account in the namespace. If your compliance controls require a unique service account, assign one to the VM. The setting applies to the `VirtualMachineInstance` object and the `virt-launcher` pod.

The `kubevirt-controller` service account is granted additional SCCs and Linux capabilities so that it can create `virt-launcher` pods with the appropriate permissions. These extended permissions allow virtual machines to use OpenShift Virtualization features that are beyond the scope of typical pods.

The `kubevirt-controller` service account is granted the following SCCs:

`scc.AllowHostDirVolumePlugin = true`
This allows virtual machines to use the hostpath volume plugin.

`scc.AllowPrivilegedContainer = false`
This ensures the `virt-launcher` pod is not run as a privileged container.

`scc.AllowedCapabilities = []corev1.Capability{"SYS_NICE", "NET_BIND_SERVICE"}`
- `SYS_NICE` allows setting the CPU affinity.

- `NET_BIND_SERVICE` allows DHCP and Slirp operations.

### Viewing the SCC and RBAC definitions for the kubevirt-controller

You can view the `SecurityContextConstraints` definition for the `kubevirt-controller` by using the `oc` tool:

``` terminal
$ oc get scc kubevirt-controller -o yaml
```

You can view the RBAC definition for the `kubevirt-controller` clusterrole by using the `oc` tool:

``` terminal
$ oc get clusterrole kubevirt-controller -o yaml
```

# Additional resources

- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/#restricted)

- [About Security context constraints](../../authentication/managing-security-context-constraints.md#security-context-constraints-about_configuring-internal-oauth)

- [Using RBAC to define and apply permissions](../../authentication/using-rbac.md#using-rbac)

- [Managing security context constraints](../../authentication/managing-security-context-constraints.md#security-context-constraints-about_configuring-internal-oauth)

- [Creating a cluster role](../../authentication/using-rbac.md#creating-cluster-role_using-rbac)

- [Cluster role binding commands](../../authentication/using-rbac.md#cluster-role-binding-commands_using-rbac)

- [Enabling user permissions to clone data volumes across namespaces](../storage/virt-enabling-user-permissions-to-clone-datavolumes.md#virt-enabling-user-permissions-to-clone-datavolumes)
