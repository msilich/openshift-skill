<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Understand how Operator Lifecycle Manager (OLM) manages certificates for OLM components and creates and rotates certificates when installing Operators that include webhooks or API services. In proxy environments, you must manage Operator certificates yourself because OLM does not update them.

# Management

All certificates for Operator Lifecycle Manager (OLM) components, such as `olm-operator`, `catalog-operator`, `packageserver`, and `marketplace-operator`, are managed by the system.

When installing Operators that include webhooks or API services in their `ClusterServiceVersion` (CSV) object, OLM creates and rotates the certificates for these resources. Certificates for resources in the `openshift-operator-lifecycle-manager` namespace are managed by OLM.

OLM does not update the certificates of Operators that it manages in proxy environments. These certificates must be managed by the user using the subscription config.

# Additional resources

- [Configuring proxy support in Operator Lifecycle Manager](../../operators/admin/olm-configuring-proxy-support.md#olm-configuring-proxy-support)

- [Proxy certificates](proxy-certificates.md#proxy-certificates)

- [Replacing the default ingress certificate](../certificates/replacing-default-ingress-certificate.md#replacing-default-ingress)

- [Updating the CA bundle](../certificates/updating-ca-bundle.md#updating-ca-bundle)
