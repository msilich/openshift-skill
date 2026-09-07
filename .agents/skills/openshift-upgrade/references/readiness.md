# Update readiness

Read the target-relevant chapters in [sources.md](sources.md). Record the exact
current and requested release, architecture, channel, update graph evidence and
release image digest. A supplied readiness report may be used when its cluster,
timestamp and coverage are known; verify gaps with permitted live reads.

Read ClusterVersion conditions and available/conditional updates, ClusterOperator
conditions/versions, MachineConfigPools, node readiness, workload capacity and PDBs.
`oc --kubeconfig <verified-path> adm upgrade` without arguments can report update
information when MCP cannot; never add a target or force flag to a read-only check.

## Assess blockers with evidence

- Distinguish a patch update from a minor update when interpreting Upgradeable.
  Apply the documented condition semantics, not a universal rule for every update.
- Evaluate conditional-update risks against the actual cluster. An unavailable
  graph or offline compatibility source is an unknown, not an approved update path.
- Examine APIRequestCount and applicable alerts for APIs removed in the target.
  A served API on the current cluster says nothing about target availability.
- Inspect affected Operators' installed versions and target compatibility from
  matching local release/support material. Do not query Jira or lifecycle services
  at runtime, or invent compatibility from an installed CRD.
- Check paused/degraded pools, spare capacity, topology and PDB status.
  `disruptionsAllowed=0` with all replicas required can prevent a needed drain.
  Do not lower the PDB automatically. Describe the affected workload and maintenance
  options for its owner.
- Check etcd health and evidence of a usable backup under the documented procedure.
  Do not read backup contents. Use openshift-backup-restore for coverage questions.
- In an air gap verify the target release digest and dependencies in the internal
  mirror with openshift-disconnected. A version string alone is insufficient.

Report findings as blockers, warnings or unknowns, each with object/source evidence.
If a prerequisite cannot be verified, state which evidence is missing rather than
labeling the cluster ready. Do not adopt fixed headroom percentages, backup ages,
or per-node duration estimates from upstream examples as universal requirements.
