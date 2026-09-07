<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Operators are the foundational control plane extensions of OpenShift Container Platform. Operators are the preferred method to package, deploy, and manage services on the control plane, and to support your applications.

Operators integrate with Kubernetes APIs and CLI tools such as `kubectl` and the OpenShift CLI (`oc`). They provide the means of monitoring applications, performing health checks, managing over-the-air (OTA) updates, and ensuring that applications remain in your specified state.

Operators are designed specifically for Kubernetes-native applications to implement and automate common Day 1 operations, such as installation and configuration. Operators can also automate Day 2 operations, such as autoscaling up or down and creating backups. All of these activities are directed by a piece of software running on your cluster.

While both follow similar Operator concepts and goals, Operators in OpenShift Container Platform are managed by two different systems, depending on their purpose:

Cluster Operators
Managed by the Cluster Version Operator (CVO) and installed by default to perform cluster functions.

Optional add-on Operators
Managed by Operator Lifecycle Manager (OLM) and can be made accessible for users to run in their applications. Also known as *OLM-based Operators*.

# OLM-based Operator tasks

To maintain cluster security and operational boundaries, your assigned user role, such as cluster administrator or application developer, determines whether you can install, manage, or use Operator Lifecycle Manager (OLM)-based Operators.

For developers
As an Operator author, you can perform the following development tasks for OLM-based Operators:

- Install and subscribe an Operator to your namespace.

- Create an application from an installed Operator through the web console.

<!-- -->

For administrators
As a cluster administrator, you can perform the following administrative tasks for OLM-based Operators:

- Manage custom catalogs.

- Allow non-cluster administrators to install Operators

- Install an Operator from the software catalog

- View Operator status

- Manage Operator conditions

- Upgrade installed Operators

- Delete installed Operators

- Configure proxy support

- Using Operator Lifecycle Manager in disconnected environments

For information about the cluster Operators that Red Hat provides, see "Cluster Operators reference".

<div>

<div class="title">

Additional resources

</div>

- [Manage custom catalogs](admin/olm-managing-custom-catalogs.md#olm-managing-custom-catalogs)

- [Machine deletion lifecycle hook examples for Operator developers](../machine_management/deleting-machine.md#machine-lifecycle-hook-deletion-uses_deleting-machine)

- [Install and subscribe an Operator to your namespace](user/olm-installing-operators-in-namespace.md#olm-installing-operators-in-namespace)

- [Allow non-cluster administrators to install Operators](admin/olm-creating-policy.md#olm-creating-policy)

- [Install an Operator from the software catalog](user/olm-installing-operators-in-namespace.md#olm-installing-operators-in-namespace)

- [Using Operator Lifecycle Manager in disconnected environments](../disconnected/using-olm.md#olm-restricted-networks)

- [Cluster Operators reference](operator-reference.md#operator-reference)

- [Create an application from an installed Operator through the web console](user/olm-creating-apps-from-installed-operators.md#olm-creating-apps-from-installed-operators)

- [View Operator status](admin/olm-status.md#olm-status)

- [Manage Operator conditions](admin/olm-managing-operatorconditions.md#olm-managing-operatorconditions)

- [Upgrade installed Operators](admin/olm-upgrading-operators.md#olm-upgrading-operators)

- [Delete installed Operators](admin/olm-deleting-operators-from-cluster.md#olm-deleting-operators-from-a-cluster)

- [Configure proxy support](admin/olm-configuring-proxy-support.md#olm-configuring-proxy-support)

- [What are Operators?](understanding/olm-what-operators-are.md#olm-what-operators-are)

</div>
