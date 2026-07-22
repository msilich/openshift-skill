# Third-party notices

This repository contains or derives artifacts from the following projects.
Exact revisions and integrity information are recorded in `sources.lock.json`
and the referenced `SOURCE.json` file.

## OpenShift Container Platform documentation

- Project: `openshift/openshift-docs`
- Source revision: `5aee2719f9ad01a82bb80b391e5af25f566c73c0`
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

## Referenced but not redistributed

The following projects are referenced by configuration and documentation, but
their binaries and source trees are not redistributed here:

- `openshift/openshift-mcp-server`, Apache License 2.0
- `argoproj-labs/mcp-for-argocd`, Apache License 2.0
- OpenCode (`anomalyco/opencode` at the tested baseline), MIT License

OpenShift and Red Hat are trademarks of Red Hat, Inc. This project is an
independent community project and is not an official Red Hat product or support
channel.
