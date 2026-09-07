# Disconnected Dev Spaces

Open the installation, restricted-dependency and private-extension-registry chapters
from [sources.md](sources.md). Use `openshift-disconnected` for the broader OCP mirror
workflow, while keeping Dev Spaces-specific requirements tied to the 3.29 source.

Separate connected preparation, approved transfer, and disconnected target operation.
Inventory the selected Operator/catalog, operand and workspace/IDE images, registries,
devfile sources, extensions and language-package dependencies required by this task.
A mirrored Dev Spaces Operator alone is not proof that workspace startup is offline-ready.

On the connected preparation host prepare the documented image and metadata set
for the selected versions, verify hashes/digests and transfer it through the approved
process. On the disconnected side use internal registries and repositories only.
No runtime downloads of tools, external documentation, sample devfiles, extensions
or dependencies; an external URL in the guide is a preparation reference.

For image-pull failures collect the exact failing image/digest, pull event and registry
host. Distinguish missing content, incorrect mirror mapping, DNS/reachability, TLS
trust and authorization using permitted observations. Check the effective generated
workspace image and owning configuration; do not blindly edit an Operator-managed pod.
Resolve Secret choices before examining pull credentials. Never disable TLS checking
or print registry credentials as a diagnostic shortcut.

For Maven/npm/Python or IDE-extension failures inspect which endpoint the workspace
actually uses and whether the requested artifact exists internally. Treat package
manager and extension-registry configuration separately from container-image mirrors.
Proposed trust, mirror or CheCluster changes require the existing Day-2 approval gates.
Verify a fresh agreed workspace can pull its image and resolve the specific required
artifact without external egress; state any check that was not performed.
