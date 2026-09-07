<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To improve secret security and integrate with enterprise secret management systems, you can use the Secrets Store CSI Driver Operator to mount secrets from external stores without persisting them on the cluster after pod termination.

# Overview of Secrets Store CSI Driver Operator

To store and manage your secrets securely, configure the Secrets Store CSI Driver Operator to mount secrets from an external secret management system, such as Azure Key Vault, by using a provider plugin. Applications can then use the secret, but the secret does not persist on the system after pod termination.

Secret objects are stored with Base64 encoding. etcd provides encryption at rest for these secrets, but when secrets are retrieved, they are decrypted and presented to the user. If role-based access control is not configured properly on your cluster, anyone with API or etcd access can retrieve or modify a secret. Additionally, anyone who is authorized to create a pod in a namespace can use that access to read any secret in that namespace.

The Secrets Store CSI Driver Operator, `secrets-store.csi.k8s.io`, enables OpenShift Container Platform to mount multiple secrets, keys, and certificates stored in enterprise-grade external secrets stores into pods as a volume. The Secrets Store CSI Driver Operator communicates with the provider using gRPC to fetch the mount contents from the specified external secrets store. After the volume is attached, the data in it is mounted into the container’s file system. Secrets store volumes are mounted in-line.

For more information about CSI inline volumes, see "CSI inline ephemeral volumes".

Familiarity with persistent storage and configuring CSI volumes is recommended when working with a CSI driver. For more information, see "Understanding persistent storage" and "Configuring CSI volumes".

<div>

<div class="title">

Additional resources

</div>

- [CSI inline ephemeral volumes](ephemeral-storage-csi-inline.md#ephemeral-storage-csi-inline)

- [Understanding persistent storage](../understanding-persistent-storage.md#understanding-persistent-storage)

- [Configuring CSI volumes](persistent-storage-csi.md#persistent-storage-csi)

</div>

## Secrets store providers

You can store sensitive information needed by your applications in an external secret management system and use the Secrets Store CSI Driver Operator to mount the secret content as a pod volume. Using an external secret store protects information that you do not want developers to have and can be more secure than `secret` objects.

The Secrets Store CSI Driver Operator has been tested with the following secrets store providers:

- AWS Secrets Manager

- AWS Systems Manager Parameter Store

- Azure Key Vault

- Google Secret Manager

- HashiCorp Vault

> [!NOTE]
> Red Hat does not test all factors associated with third-party secrets store provider functionality. For more information about third-party support, see the "Red Hat third-party support policy".

# About CSI

The Container Storage Interface (CSI) enables storage vendors to deliver plugins through a standard interface without modifying Kubernetes core code, replacing traditional embedded storage drivers.

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.

# Support for disconnected environments

You can use certain secrets store providers in disconnected OpenShift Container Platform clusters by configuring VPC endpoints or equivalent connectivity to enable communication between the driver and external secret management systems.

The following secrets store providers support using the Secrets Store CSI driver in disconnected clusters:

- AWS Secrets Manager

- Azure Key Vault

- Google Secret Manager

- HashiCorp Vault

To enable communication between Secrets Store CSI driver and the secrets store provider, configure Virtual Private Cloud (VPC) endpoints or equivalent connectivity to the corresponding secrets store provider, the OpenID Connect (OIDC) issuer, and the Secure Token Service (STS). The exact configuration depends on the secrets store provider, the authentication method, and the type of disconnected cluster.

> [!NOTE]
> For more information about disconnected environments, see "About disconnected environments".

<div>

<div class="title">

Additional resources

</div>

- [About disconnected environments](../../disconnected/about.md#about)

</div>

# Support for network policies

The Secrets Store CSI Driver Operator uses pre-defined `NetworkPolicies` to control ingress and egress traffic for enhanced security of the Operator and driver components.

The following table summarizes the default ingress and egress rules:

| Component | Ingress ports | Egress ports | Description |
|----|----|----|----|
| Secrets Store CSI Driver Operator | `8443` | `6443` | Accesses metrics and communicates with the API server |
| Secrets Store CSI driver | `8095` | `6443` | Accesses metrics and communicates with the API server |

# Installing the Secrets Store CSI driver

To enable OpenShift Container Platform to mount secrets from external secret management systems, install the Secrets Store CSI Driver Operator and create a `ClusterCSIDriver` instance.

<div>

<div class="title">

Prerequisites

</div>

- Access to the OpenShift Container Platform web console.

- Administrator access to the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Install the Secrets Store CSI Driver Operator:

    1.  Log in to the web console.

    2.  Click **Ecosystem** → **Software Catalog**.

    3.  Locate the Secrets Store CSI Driver Operator by typing "Secrets Store CSI" in the filter box.

    4.  Click the **Secrets Store CSI Driver Operator** button.

    5.  On the **Secrets Store CSI Driver Operator** page, click **Install**.

    6.  On the **Install Operator** page, ensure that:

        - **All namespaces on the cluster (default)** is selected.

        - **Installed Namespace** is set to **openshift-cluster-csi-drivers**.

    7.  Click **Install**.

        After the installation finishes, the Secrets Store CSI Driver Operator is listed in the **Installed Operators** section of the web console.

2.  Create the `ClusterCSIDriver` instance for the driver (`secrets-store.csi.k8s.io`):

    1.  Click **Administration** → **CustomResourceDefinitions** → **ClusterCSIDriver**.

    2.  On the **Instances** tab, click **Create ClusterCSIDriver**.

        Use the following YAML file:

        ``` yaml
        apiVersion: operator.openshift.io/v1
        kind: ClusterCSIDriver
        metadata:
            name: secrets-store.csi.k8s.io
        spec:
          managementState: Managed
        ```

    3.  Click **Create**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Providing sensitive data to pods by using an external secrets store](../../nodes/pods/nodes-pods-secrets-store.md#nodes-pods-secrets-store)

</div>

# Uninstalling the Secrets Store CSI Driver Operator

To remove the Secrets Store CSI Driver Operator and free cluster resources, uninstall the Operator after stopping applications and removing the CSI driver.

<div>

<div class="title">

Prerequisites

</div>

- Access to the OpenShift Container Platform web console.

- Administrator access to the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Stop all application pods that use the `secrets-store.csi.k8s.io` provider.

2.  Remove any third-party provider plug-in for your chosen secret store.

3.  Remove the Container Storage Interface (CSI) driver and associated manifests:

    1.  Click **Administration** → **CustomResourceDefinitions** → **ClusterCSIDriver**.

    2.  On the **Instances** tab, for **secrets-store.csi.k8s.io**, on the far left side, click the drop-down menu, and then click **Delete ClusterCSIDriver**.

    3.  When prompted, click **Delete**.

4.  Verify that the CSI driver pods are no longer running.

5.  Uninstall the Secrets Store CSI Driver Operator:

    > [!NOTE]
    > Before you can uninstall the Operator, you must remove the CSI driver first.

    1.  Click **Ecosystem** → **Installed Operators**.

    2.  On the **Installed Operators** page, scroll or type "Secrets Store CSI" into the **Search by name** box to find the Operator, and then click it.

    3.  On the upper, right of the **Installed Operators** \> **Operator details** page, click **Actions** → **Uninstall Operator**.

    4.  When prompted on the **Uninstall Operator** window, click the **Uninstall** button to remove the Operator from the namespace. Any applications deployed by the Operator on the cluster need to be cleaned up manually.

        After uninstalling, the Secrets Store CSI Driver Operator is no longer listed in the **Installed Operators** section of the web console.

</div>

# Additional resources

- [Configuring CSI volumes](persistent-storage-csi.md#persistent-storage-csi)
