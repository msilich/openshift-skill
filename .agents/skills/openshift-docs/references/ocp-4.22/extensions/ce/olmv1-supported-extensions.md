<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To install an Operator as a cluster extension, it must meet bundle format, install mode, and dependency requirements. Operator Lifecycle Manager (OLM) v1 supports extensions that use webhooks for validation, mutation, or conversion.

Operator Lifecycle Manager (OLM) v1 supports extensions that use the `AllNamespaces` install mode. With this mode, the Operator watches and manages resources across all namespaces in the cluster.

As a Technology Preview feature, you can configure an extension to watch a specific namespace. This limits watching to one namespace instead of the entire cluster.

# Supported bundle formats and dependencies

To install an Operator as a cluster extension, the Operator must be packaged using the `registry+v1` bundle format. OLM v1 does not support Operators that declare dependencies by using file-based catalog properties.

To install an Operator as a cluster extension, it must meet the following criteria:

- The Operator is packaged using the `registry+v1` bundle format.

- The Operator does not declare dependencies by using the following file-based catalog properties:

  - `olm.gvk.required`

  - `olm.package.required`

  - `olm.constraint`

OLM v1 verifies that an Operator meets these requirements during installation. If an Operator does not meet these criteria, OLM v1 reports the issue in the cluster extension status conditions.

Operator Lifecycle Manager (OLM) v1 does not support the `OperatorConditions` API introduced in OLM (Classic).

If an extension relies on only the `OperatorConditions` API to manage updates, the extension might not install correctly. Most extensions that rely on this API fail at start time, but some might fail during reconciliation.

As a workaround, you can pin your extension to a specific version. When you want to update your extension, consult the extension’s documentation to find out when it is safe to pin the extension to a new version.

<div>

<div class="title">

Additional resources

</div>

- [Bundle format](../../operators/understanding/olm-packaging-format.md#olm-bundle-format_olm-packaging-format)

- [Operator conditions](../../operators/understanding/olm/olm-operatorconditions.md#olm-operatorconditions)

</div>

# Webhook support

Operator Lifecycle Manager (OLM) v1 supports Operators that use webhooks for validation, mutation, or conversion. Operators use webhooks to enforce security policies or inject configurations into resources.

The OpenShift Service CA Operator automatically manages webhook certificates. When you install an Operator that includes webhooks, the OpenShift Service CA Operator completes the following actions:

- Applies Service CA annotations to webhook configurations and services.

- Generates TLS certificates in the namespace where you install the cluster extension.

- Mounts certificate secrets to the Operator deployment.

- Configures webhook services with proper TLS settings.

<div>

<div class="title">

Additional resources

</div>

- [Types of webhook admission plugins](../../architecture/admission-plug-ins.md#admission-webhook-types_admission-plug-ins)

- [Service CA certificates](../../security/certificate_types_descriptions/service-ca-certificates.md#add-service-certificate_service-ca-certificates)

- [OpenShift Service CA Operator](../../operators/operator-reference.md#openshift-service-ca-operator_operator-reference)

- [Validating admission webhooks (Kubernetes documentation)](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook)

- [Mutating admission webhooks (Kubernetes documentation)](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook)

- [Conversion webhooks (Kubernetes documentation)](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#webhook-conversion)

</div>
