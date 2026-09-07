# Requested update and completion

Begin with [readiness.md](readiness.md). Confirm the target and original success
criteria, including workload checks and maintenance constraints.

A proposed version path is not an authorization to update. Follow the existing
Day-2 gates. Discover the exact live API and current installed CLI behavior,
show the intended target/digest and impact, and obtain fresh approval before the
actual request. When no real update dry-run is supported, label the readiness
assessment as a preflight, not a dry-run.

Do not force an update, suppress failed prerequisites, invent a skipped-version
path, or promise a downgrade as rollback. Follow only the vendor-documented
recovery options for the exact state. If an update is already running, investigate
its phase before proposing any second request.

Monitor ClusterVersion history/conditions, operator versions, pools and affected
nodes with bounded observations. Relate a stalled pool to the node, workload,
PDB or operand evidence. Do not unpause a pool, drain a node or delete an operand
without a separately scoped approved change.

Completion requires the intended release to be reported complete, expected
operator/pool convergence, no unexplained new degradation, and the agreed
application checks. An accepted desiredUpdate is only submission. Report any
unverified service checks and remaining degraded component.
