<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure Kubernetes Key Management Service (KMS) v2 on OpenShift Container Platform to centralize encryption key management and meet regulatory compliance requirements.

> [!IMPORTANT]
> Kubernetes KMS v2 is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# About Kubernetes KMS v2 encryption

Kubernetes KMS v2 uses external Key Management Services to encrypt etcd data and centralize key management.

Kubernetes KMS v2 provides:

- Customer-managed encryption keys that never leave the external KMS

- Centralized key management and auditing

- Regulatory compliance support

## Encrypted resources

When you enable KMS encryption, OpenShift Container Platform encrypts the following sensitive resources in etcd:

- Secrets

- ConfigMaps

- Routes

- OAuth access tokens

- OAuth authorize tokens

> [!NOTE]
> Resource types, namespaces, and object names are not encrypted.

<div>

<div class="title">

Additional resources

</div>

- [Using a KMS provider for data encryption](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)

</div>

# KMS Technology Preview limitations

Review the current limitations of Kubernetes KMS v2 to plan deployments and avoid unsupported configurations in OpenShift Container Platform 4.21 or later.

## Current limitations

- Plugins require manual installation on each control plane node

- Plugins must listen at `unix:///var/run/kmsplugin/kms.sock`

- Only one KMS plugin can run at a time

- KMS-to-KMS migration requires intermediate migration to `identity` or `aescbc`

# Additional resources

- [Enabling features using feature gates](../../nodes/clusters/nodes-cluster-enabling-features.md#nodes-cluster-enabling-features)

- [Using a KMS provider for data encryption](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)

- [HashiCorp Vault Transit Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/transit)

- [Use Vault as a Kubernetes KMS provider](https://developer.hashicorp.com/vault/docs/deploy/kubernetes/kms)
