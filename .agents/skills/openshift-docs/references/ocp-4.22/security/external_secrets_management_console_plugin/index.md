<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The External Secrets Management Console Plug-in is an Operator that manages the secrets and custom resource definitions (CRDs) for the secrets management Operators. Using External Secrets Management Console Plug-in, you can monitor and delete the custom resources (CRs) of all the installed secrets management Operators.

> [!IMPORTANT]
> External Secrets Management Console Plug-in is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The following secrets management Operators can be managed with External Secrets Management Console Plug-in:

- External Secrets Operator for Red Hat OpenShift

- cert-manager Operator for Red Hat OpenShift

- Secrets Store CSI Driver Operator

You can use the plug-in to complete the following tasks:

- View and filter secrets-related CRs from all installed secrets management Operators in a unified dashboard.

- Inspect resource details including metadata, spec, status, and Kubernetes events.

- Delete CRs directly from the console with name-confirmation.

- View real-time resource health and status, including sync state, certificate expiry, and provider type.

- Automatic Operator detection that shows resources only from Operators that are installed on the cluster.
