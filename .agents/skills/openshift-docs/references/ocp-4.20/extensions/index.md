<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure the operating system of your nodes and extend capabilities to your cluster by using pre-packaged software extensions. These extensions include ready-to-use tools that customize your environment for your requirements.

Operator Lifecycle Manager (OLM) has been included with OpenShift Container Platform 4 since its initial release. OpenShift Container Platform 4.20 includes components for a next-generation iteration of OLM as a Generally Available (GA) feature, known during this phase as *OLM v1*. This updated framework evolves many of the concepts that have been part of previous versions of OLM and adds new capabilities.

> [!NOTE]
> For OpenShift Container Platform 4.20, documented procedures for OLM v1 are CLI-based only. Alternatively, administrators can create and view related objects in the web console by using normal methods, such as the **Import YAML** and **Search** pages. However, the existing **Software Catalog** and **Installed Operators** pages do not yet display OLM v1 components.

# OLM v1 highlights

As an administrator, use OLM v1 to securely manage your cluster configurations and streamline updates through GitOps-based declarative management, granular extension controls, and flexible packaging formats.

Administrators can explore the following highlights:

Fully declarative model that supports GitOps workflows
OLM v1 simplifies extension management through two key APIs:

- A new `ClusterExtension` API streamlines management of installed extensions, which includes Operators via the `registry+v1` bundle format, by consolidating user-facing APIs into a single object. This API is provided as `clusterextension.olm.operatorframework.io` by the new Operator Controller component. Administrators and SREs can use the API to automate processes and define desired states by using GitOps principles.

  > [!NOTE]
  > Earlier Technology Preview phases of OLM v1 introduced a new `Operator` API; this API is renamed `ClusterExtension` in OpenShift Container Platform 4.16 to address the following improvements:
  >
  > - More accurately reflects the simplified functionality of extending a cluster’s capabilities
  >
  > - Better represents a more flexible packaging format
  >
  > - `Cluster` prefix clearly indicates that `ClusterExtension` objects are cluster-scoped, a change from OLM (Classic) where Operators could be either namespace-scoped or cluster-scoped

- The `Catalog` API, provided by the new catalogd component, serves as the foundation for OLM v1, unpacking catalogs for on-cluster clients so that users can discover installable content, such as Kubernetes extensions and Operators. This provides increased visibility into all available Operator bundle versions, including their details, channels, and update edges.

For more information, see "Operator Controller and Catalogd".

Improved control over extension updates
With improved insight into catalog content, administrators can specify target versions for installation and updates. This grants administrators more control over the target version of extension updates. For more information, see "Updating a cluster extension".

Flexible extension packaging format
Administrators can use file-based catalogs to install and manage extensions, such as OLM-based Operators, similar to the OLM (Classic) experience.

In addition, bundle size is no longer constrained by the etcd value size limit. For more information, see "Installing extensions".

Secure catalog communication
OLM v1 uses HTTPS encryption for catalogd server responses.

Basic support for proxied environments and trusted CA certificates
Operator Controller and catalogd can run in proxied environments and include basic support for trusted CA certificates.

# Purpose of Operator Lifecycle Manager

The Operator Lifecycle Manager (OLM) simplifies management of extensions on Kubernetes clusters. It provides administrators with a safe, reliable, and centralized way to install, run, and update cluster extensions.

The initial version of OLM, which launched with OpenShift Container Platform 4 and is included by default, focused on providing unique support for these specific needs for a particular type of cluster extension, known as Operators. Operators are classified as one or more Kubernetes controllers, shipping with one or more API extensions, as `CustomResourceDefinition` (CRD) objects, to provide additional functionality to the cluster.

After running in production clusters for many releases, the next-generation of OLM aims to encompass lifecycles for cluster extensions that are not just Operators.

<div>

<div class="title">

Additional resources

</div>

- [Operator Controller](arch/operator-controller.md#operator-controller)

- [Catalogd](arch/catalogd.md#catalogd)

- [Updating a cluster extension](ce/managing-ce.md#olmv1-updating-an-operator_managing-ce)

- [Installing extensions](ce/managing-ce.md#managing-ce)

</div>
