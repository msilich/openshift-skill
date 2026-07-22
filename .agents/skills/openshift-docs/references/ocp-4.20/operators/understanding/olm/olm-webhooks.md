<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Webhooks allow Operator authors to intercept, modify, and accept or reject resources before they are saved to the object store and handled by the Operator controller. Operator Lifecycle Manager (OLM) can manage the lifecycle of these webhooks when they are shipped alongside your Operator.

# Additional resources

- [Types of webhook admission plugins](../../../architecture/admission-plug-ins.md#admission-webhook-types_admission-plug-ins)

- Kubernetes documentation:

  - [Validating admission webhooks](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook)

  - [Mutating admission webhooks](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook)

  - [Conversion webhooks](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#webhook-conversion)
