<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Secret management tools can be used to automate the lifecycle of sensitive data, such as passwords, private files, and certificates, by providing a centralized system to control and monitor access. This approach enhances security by limiting the uncontrolled spread of secrets and enables automation for the entire secret lifecycle, including updates, expiration, and removal.

OpenShift Container Platform uses a flexible Operator and plugin design to decouple your workloads from external secret managers, ensuring you are not locked into a single vendor. In this model, the Operator acts as an intermediary, while a vendor-specific plugin manages communication between the cluster and the external storage. This allows applications to access secrets without needing to know the details of where or how they are stored.

# Secrets management Operators in OpenShift Container Platform

OpenShift Container Platform offers a suite of supported Operators designed to secure and automate the management of sensitive data, such as external credentials and digital certificates. Each secrets management Operator provides quick starts and sample YAML manifests to streamline the onboarding process. These tools simplify installation and deployment, and help you build complex custom resources by using pre-defined YAML snippets. The following list details the key Operators available for these tasks:

- **Secrets Store CSI driver**: Enables Kubernetes to connect to external systems, and mount credentials from the external system into an application workload.

- **External Secrets Operator for Red Hat OpenShift**: Retrieves credentials stored in external management systems and makes them available within OpenShift Container Platform as standard Kubernetes Secrets.

- **cert-manager Operator for Red Hat OpenShift**: Manages the lifecycle of digital certificates that are used by applications running on OpenShift Container Platform by automating the process of issuance and renewal.

# Secrets management use cases

Using secrets management tools with other Red Hat products can protect sensitive data across your OpenShift Container Platform cluster. You can integrate secrets management Operators with other OpenShift Container Platform components to securely manage, automate, and consume credentials across various infrastructure and application workflows.

## External Secrets Operator for Red Hat OpenShift use cases

You can integrate the External Secrets Operator with other OpenShift Container Platform components to securely manage and inject credentials. Learn how to apply External Secrets Operator in real-world deployment strategies, by reviewing the following example.

Securing Red Hat OpenShift GitOps by using External Secrets Operator short-lived tokens
To reduce the security risk of compromised credentials, you can configure the External Secrets Operator to generate short-lived tokens. Red Hat OpenShift GitOps can then use these temporary tokens to securely authenticate when accessing GitHub repositories. You can refer to an example of the integration in the External Secrets Operator and GitOps demonstration.

<div>

<div class="title">

Additional resources

</div>

- [External Secrets Operator and GitOps demonstration](https://interact.redhat.com/share/tcwyXElfYLWTvHl5dJ5n)

- [Zero trust GitOps: Build a secure, secretless GitOps pipeline](https://developers.redhat.com/articles/2026/03/13/zero-trust-gitops-build-secure-secretless-gitops-pipeline)

</div>

<div>

<div class="title">

Additional resources

</div>

- [Secrets Store Container Storage Interface Driver Operator](../storage/container_storage_interface/persistent-storage-csi-secrets-store.md#persistent-storage-csi-secrets-store)

- [External Secrets Operator for Red Hat OpenShift](external_secrets_operator/index.md#external-secrets-operator-about)

- [cert-manager Operator for Red Hat OpenShift](cert_manager_operator/index.md#cert-manager-operator-about)

</div>
