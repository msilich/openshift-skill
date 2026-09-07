# Third-party notices

This repository contains or derives artifacts from the following projects.
Exact revisions and integrity information are recorded in `sources.lock.json`
and the referenced `SOURCE.json` file.

## OpenShift Container Platform documentation

- Project: `openshift/openshift-docs`
- Source revision: `3d4fc17cc6638735acdf8ccfcfe7b183b9fdab98`
- License: Apache License 2.0
- Bundled license:
  `.agents/skills/openshift-docs/references/ocp-4.20/LICENSE.openshift-docs`
- Modifications: converted from AsciiDoc to GitHub-Flavored Markdown, added
  pinned provenance and format notices, removed the generated network-dependent
  viewer, and rewrote cross-references for offline use.

## OpenShift agentic-skills documentation converter

- Project: `openshift/agentic-skills`
- Source revision: `b09c2e645940b945c5a224a8f14927e10216ba07`
- License: Apache License 2.0
- Bundled converter: `tools/docs/convert.py`
- Bundled license: `tools/docs/LICENSE.agentic-skills`
- Local modification: derive the product version from an explicit
  `enterprise-X.Y` or `gitops-docs-X.Y` branch when the distro map is stale; reject missing or
  conflicting versions instead of falling back to 4.17. The original and
  modified converter checksums are recorded in `tools/docs/build.lock.json`.

## Additional GitOps documentation and adapted workflows

- GitOps 1.21 documentation: `openshift/openshift-docs`, branch `gitops-docs-1.21`,
  commit `ca5db8539a097b38e2975980963e0959782d105f`, Apache-2.0. The full topic map is
  converted to Markdown in the documentation skill's `references/gitops-1.21/`.
  Local changes include format notices, product-specific navigation titles and
  offline cross-references. License and exact build metadata accompany the snapshot.
- Workflow adaptations: `openshift/agentic-skills`, commit
  `7aca4bee317cd70a4204795db6b1d7b9eb78f48c`, Apache-2.0; source paths
  `cluster-troubleshoot/investigate-alert/SKILL.md` and
  `cluster-update/cluster-update-advisor/SKILL.md`. The local troubleshooting and
  upgrade skills adapt causal investigation and readiness assessment. They replace
  the upstream execution environment with MCP-first, offline, user-approved access.
  No upstream diagnostic/token scripts are redistributed. The Apache-2.0 license
  text is retained in `tools/docs/LICENSE.agentic-skills`.
- Each domain skill's source map identifies the documentation used. These skills
  and their MCP mappings are project-authored adaptations, not vendor certification.

## Red Hat OpenShift Dev Spaces 3.29 documentation

- Source: https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29
- License: Creative Commons Attribution-ShareAlike 3.0 Unported (CC-BY-SA-3.0),
  with Red Hat's Section 4d waiver retained in the legal notice.
- This snapshot is sourced from official HTML, not a claimed public Git revision.
  All 302 TOC topics and 46 illustrations are bundled. Exact response/fragment
  hashes, retrieval dates, exclusions and link adjustments are in the snapshot's
  `SOURCE.json`; the archive is pinned by `tools/docs/devspaces.lock.json`.
- HTML source fragments and illustrations: `tools/docs/snapshots/devspaces-3.29.zip`.
  Adapted Markdown: `.agents/skills/openshift-docs/references/devspaces-3.29/`.
  `LEGAL-NOTICE.md` preserves attribution and trademarks; `LICENSE.md` contains
  the CC BY-SA 3.0 legal code. Each topic links to its original URL.
- Modifications: extracted article content, removed site chrome/scripts, converted
  to Markdown, retained original anchors, localized document/image links, added
  navigation and integrity metadata. Missing upstream fragments link to the local
  topic and are recorded explicitly. External references are not redistributed.
- `openshift-devspaces` skill text and references are project-authored adaptations
  under CC-BY-SA-3.0; MCP mappings are identified as project modifications. This
  does not relicense other separately licensed code or documentation in the bundle.

## Referenced but not redistributed

The following projects are referenced by configuration and documentation, but
their binaries and source trees are not redistributed here:

- `openshift/openshift-mcp-server`, Apache License 2.0
- `argoproj-labs/mcp-for-argocd`, Apache License 2.0
- OpenCode (`anomalyco/opencode` at the tested baseline), MIT License

OpenShift and Red Hat are trademarks of Red Hat, Inc. This project is an
independent community project and is not an official Red Hat product or support
channel.
