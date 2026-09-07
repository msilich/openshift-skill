# Mirror preparation, transfer and import

Start with [sources.md](sources.md), especially the v2 workflow, prerequisites
and restrictions on generated resources. Establish the installed oc-mirror
version; its ImageSetConfiguration is plugin input, not a CRD to apply to the
cluster. Do not invent fields from a Kubernetes API schema.

## Preparation host

Record the requested release versions/architectures, Operator packages/channels,
additional images, source registries, destination registry, storage paths and
available disk space. Separate the connected preparation host from the air-gapped
import host. Online mirroring belongs only on the explicitly designated connected
host. Do not download binaries, documentation or packages inside the air gap.

Resolve credential handling before inspecting auth files. Prefer existing
protected credential-file paths; never print their contents. Use the local
oc-mirror documentation and the installed CLI help to prepare the exact
configuration and v2 command. Do not mix v1 metadata/incremental assumptions
with v2 cache workflows. Preserve the documented workspace/cache between runs.

## Transfer and target registry

For a fully disconnected environment use the documented mirror-to-disk,
approved media transfer and disk-to-mirror phases. Specify exact input/output
directories, archive checksums and destination. Registry imports and archive
creation are writes, even without a Kubernetes mutation. Show scope and use
fresh approval before each requested persistent phase. A preview that lists
selected images is not proof that the import will succeed.

The Day-2 profile permits reviewed `oc-mirror --v2 ...` commands; use the
user-installed executable and only its verified syntax. If it is absent, supply
preparation instructions instead of installing it. Use internal endpoints at runtime.

After import inspect the command result and generated cluster resources.
Discover the live IDMS/ITMS and catalog APIs before applying applicable outputs.
Follow the local restrictions on editing generated resources. A CatalogSource
and a newer catalog API are not interchangeable; use the installed OLM generation.
Verify referenced images and catalog readiness with the target cluster before
claiming the mirror is ready for an update. Delegate that update to openshift-upgrade.

Never add registry garbage collection or image deletion to an import request.
