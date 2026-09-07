<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

On disconnected OpenShift Container Platform clusters, Operator Lifecycle Manager (OLM) cannot access the Red Hat-provided catalog sources hosted on remote registries by default. As a cluster administrator, you can use a workstation with full internet access to prepare local mirrors of the remote sources, and push the content to a mirror registry.

The mirror registry can be located on a bastion host, which requires connectivity to both your workstation and the disconnected cluster, or a completely disconnected, or *airgapped*, host, which requires removable media to physically move the mirrored content to the disconnected environment.

This guide describes the following process that is required to enable OLM in disconnected environments:

- Disable the default remote OperatorHub sources for OLM.

- Use a workstation with full internet access to create and push local mirrors of the OperatorHub content to a mirror registry.

- Configure OLM to install and manage Operators from local sources on the mirror registry instead of the default remote sources.

After enabling OLM in a disconnected environment, you can continue to use your unrestricted workstation to keep your local OperatorHub sources updated as newer versions of Operators are released.

# Additional resources

- [Using Operator Lifecycle Manager in disconnected environments](../../disconnected/using-olm.md#olm-restricted-networks)
