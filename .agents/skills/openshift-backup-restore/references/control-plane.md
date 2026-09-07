# etcd and control-plane recovery

Read the exact scenario from [sources.md](sources.md) before proposing commands.
OADP is not an etcd or full-cluster disaster-recovery mechanism.

## Backup evidence

Establish the exact z-stream release, topology and backup timestamp/location.
Verify that the snapshot and static Kubernetes resources belong to the same
documented backup operation, using metadata or approved checksums rather than
reading their contents. Treat the artifacts as sensitive.

## Restore prerequisites

Distinguish quorum loss, a failed member and critical-object deletion.
If the API server is unavailable, state that MCP cannot supply live evidence.
Use only explicitly authorized out-of-band evidence/access; do not invent cluster
health or bypass a denied identity.

The documented etcd restore is a last-resort, destabilizing action. Read the
scenario-specific cautions, including API availability, topology, same-z-stream
backup requirements and host access. An etcd snapshot does not restore the
contents of persistent volumes or serve as a general upgrade rollback.

Before any execution, identify the exact hosts, backup artifacts, blast radius,
maintenance approval, recovery procedure and post-checks. Host/SSH commands are
not enabled by the supplied MCP profiles; present the reviewed procedure as
not executed when authorized host tooling is absent. Never wrap host operations
in a pod exec merely to evade that restriction.

After the explicitly requested recovery verify API access, etcd quorum/health,
operator and node convergence, storage relationships, and application/data
behavior. Keep unresolved mismatches visible. Do not repeat restore attempts
or remove members/finalizers based only on a generic failure message.
