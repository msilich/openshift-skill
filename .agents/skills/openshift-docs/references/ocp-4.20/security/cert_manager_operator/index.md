<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The cert-manager Operator for Red Hat OpenShift is a cluster-wide service that provides application certificate lifecycle management. The cert-manager Operator for Red Hat OpenShift allows you to integrate with external certificate authorities and provides certificate provisioning, renewal, and retirement.

# About the cert-manager Operator for Red Hat OpenShift

The cert-manager project introduces certificate authorities and certificates as resource types in the Kubernetes API, which makes it possible to provide certificates on-demand to developers working within your cluster. The cert-manager Operator for Red Hat OpenShift provides a supported way to integrate cert-manager into your OpenShift Container Platform cluster.

The cert-manager Operator for Red Hat OpenShift provides the following features:

- Support for integrating with external certificate authorities

- Tools to manage certificates

- Ability for developers to self-serve certificates

- Automatic certificate renewal

> [!IMPORTANT]
> Do not attempt to use both cert-manager Operator for Red Hat OpenShift for OpenShift Container Platform and the community cert-manager Operator at the same time in your cluster.
>
> Also, you should not install cert-manager Operator for Red Hat OpenShift for OpenShift Container Platform in multiple namespaces within a single OpenShift cluster.

# cert-manager Operator for Red Hat OpenShift issuer providers

To configure certificate authorities for your cluster, review the issuer providers offered with the cert-manager Operator for Red Hat OpenShift. You can use the following issuer types to automate certificate validation and issuance:

- Automated Certificate Management Environment (ACME)

- Certificate Authority (CA)

- Self-signed

- [Vault](https://cert-manager.io/docs/configuration/vault/)

- [Venafi](https://cert-manager.io/docs/configuration/venafi/)

- [Nokia NetGuard Certificate Manager](https://www.nokia.com/networks/security-portfolio/netguard/certificate-manager/) (NCM)

- [Google cloud Certificate Authority Service](https://cloud.google.com/security/products/certificate-authority-service) (Google CAS)

> [!NOTE]
> OpenShift Container Platform does not test all factors associated with third-party cert-manager Operator for Red Hat OpenShift provider functionality. For more information about third-party support, see the [OpenShift Container Platform third-party support policy](https://access.redhat.com/third-party-software-support).

# Certificate request methods

To obtain certificates for your workloads, choose a request method supported by the cert-manager Operator for Red Hat OpenShift. You can select the approach that fits your operational requirements and automation workflow.

There are two ways to request a certificate using the cert-manager Operator for Red Hat OpenShift:

Using the `cert-manager.io/CertificateRequest` object
With this method a service developer creates a `CertificateRequest` object with a valid `issuerRef` pointing to a configured issuer (configured by a service infrastructure administrator). A service infrastructure administrator then accepts or denies the certificate request. Only accepted certificate requests create a corresponding certificate.

Using the `cert-manager.io/Certificate` object
With this method, a service developer creates a `Certificate` object with a valid `issuerRef` and obtains a certificate from a secret that they pointed to the `Certificate` object.

# Supported cert-manager Operator for Red Hat OpenShift versions

To maintain a supported configuration, review the compatibility of the cert-manager Operator for Red Hat OpenShift with different OpenShift Container Platform releases. To find the list of supported versions of the cert-manager Operator for Red Hat OpenShift across different OpenShift Container Platform releases, see the "Platform Agnostic Operators" section in "OpenShift Container Platform update and support policy".

# About FIPS compliance for cert-manager Operator for Red Hat OpenShift

Starting with version 1.14.0, cert-manager Operator for Red Hat OpenShift is designed for FIPS compliance. When running on OpenShift Container Platform in FIPS mode, it uses the RHEL cryptographic libraries submitted to NIST for FIPS validation on the x86_64, ppc64le, and s390X architectures. For more information about the NIST validation program, see "Cryptographic module validation program". For the latest NIST status for the individual versions of the RHEL cryptographic libraries submitted for validation, see "Compliance activities and government standards".

To enable FIPS mode, you must install cert-manager Operator for Red Hat OpenShift on an OpenShift Container Platform cluster configured to operate in FIPS mode. For more information, see "Do you need extra security for your cluster?"

# Additional resources

- [Cryptographic module validation program](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/validated-modules)

- [cert-manager project documentation](https://cert-manager.io/docs/)

- [OpenShift Container Platform update and support policy](https://access.redhat.com/support/policy/updates/openshift_operators)

- [Understanding compliance](../container_security/security-compliance.md#security-compliance)

- [Installing a cluster in FIPS mode](../../installing/overview/installing-fips.md#installing-fips-mode_installing-fips)

- [Do you need extra security for your cluster?](../../installing/overview/installing-preparing.md#installing-preparing-security)
