<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The External Secrets Operator for Red Hat OpenShift operates as a cluster-wide service to deploy and manage the `external-secrets` application. The `external-secrets` application integrates with external secrets management systems and performs secret fetching, refreshing, and provisioning within the cluster.

# About the External Secrets Operator for Red Hat OpenShift

Use the External Secrets Operator for Red Hat OpenShift to integrate [external-secrets](https://external-secrets.io/latest/) application with the OpenShift Container Platform cluster. The `external-secrets` application fetches secrets stored in the external providers such as [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), [HashiCorp Vault](https://developer.hashicorp.com/vault), [Google Secret Manager](https://cloud.google.com/security/products/secret-manager), [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/), [IBM Cloud Secrets Manager](https://www.ibm.com/products/secrets-manager), [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) and integrates them with Kubernetes in a secure manner.

Using the External Secrets Operator ensures the following:

- Decouples applications from the secret-lifecycle management.

- Centralizes secret storage to support compliance requirements.

- Enables secure and automated secret rotation.

- Supports multi-cloud secret sourcing with fine-grained access control.

- Centralizes and audits access control.

> [!IMPORTANT]
> Do not attempt to use more than one External Secrets Operator in your cluster. If you have a community External Secrets Operator installed in your cluster, you must uninstall it before installing the External Secrets Operator for Red Hat OpenShift.

For more information about `external-secrets` application, see [external-secrets](https://external-secrets.io/latest/).

Use the External Secrets Operator to authenticate with the external secrets store, retrieve secrets, and inject the retrieved secrets into a native Kubernetes secret. This method removes the need for applications to directly access or manage external secrets.

# External secrets providers for the External Secrets Operator for Red Hat OpenShift

The External Secrets Operator for Red Hat OpenShift is tested with the following external secrets provider types:

- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)

- [HashiCorp Vault](https://developer.hashicorp.com/vault)

- [Google Secret Manager](https://cloud.google.com/security/products/secret-manager)

- [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/)

- [IBM Cloud Secrets Manager](https://www.ibm.com/products/secrets-manager)

> [!NOTE]
> Red Hat does not test all factors associated with third-party secrets store provider functionality. For more information about third-party support, see the [Red Hat third-party support policy](https://access.redhat.com/third-party-software-support).

# About FIPS compliance for External Secrets Operator for Red Hat OpenShift

The External Secrets Operator for Red Hat OpenShift supports FIPS compliance. When running on OpenShift Container Platform in FIPS mode, External Secrets Operator uses the RHEL cryptographic libraries submitted to NIST for FIPS validation on the x86_64, ppc64le, and s390X architectures. For more information about the NIST validation program, see [Cryptographic module validation program](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/validated-modules). For more information about the latest NIST status for the individual versions of the RHEL cryptographic libraries submitted for validation, see [Compliance activities and government standards](https://access.redhat.com/articles/2918071#fips-140-2-and-fips-140-3-2).

To enable FIPS mode, install the External Secrets Operator on an OpenShift Container Platform cluster that runs in FIPS mode. For more information, see "Do you need extra security for your cluster?".

# Security considerations

When using the External Secrets Operator for Red Hat OpenShift, there are some security concerns you should consider:

- The `external-secrets` operand fetches the secrets from the configured external providers and stores it in a Kubernetes native `Secrets` resource. This results in a secret zero problem. It is recommended to secure the secret objects using additional encryption. For more information, see [Data encryption options](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/4.9/html/planning_your_deployment/security-considerations_rhodf#data-encryption-options_rhodf).

- When configuring `SecretStore` and `ClusterSecretStore` resources, consider using short-term credential-based authorization. This approach enhances security by limiting the window of opportunity for unauthorized access, even if credentials are compromised.

- To enhance the security of the External Secrets Operator for Red Hat OpenShift, it is crucial to implement role-based access controls (RBACs). These RBACs should define and limit access to the custom resources provided by the External Secrets Operator.

# Additional resources

- [external-secrets application](https://external-secrets.io/latest/)

- [Understanding compliance](../container_security/security-compliance.md#security-compliance)

- [Installing a cluster in FIPS mode](../../installing/overview/installing-fips.md#installing-fips-mode_installing-fips)

- [Do you need extra security for your cluster?](../../installing/overview/installing-preparing.md#installing-preparing-security)

- [Security considerations](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/4.19/html/planning_your_deployment/security-considerations_rhodf)

- [Security Best Practices](https://external-secrets.io/latest/guides/security-best-practices/)
