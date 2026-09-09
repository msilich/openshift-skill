# ACS sources and modifications

The skill and workflow references are project-authored adaptations under the
repository's Apache-2.0 license. Documentation source:
[openshift/openshift-docs](https://github.com/openshift/openshift-docs/tree/e516555e0cb6bcc6ba88c423e88c8dd054532425),
branch `rhacs-docs-4.11`, commit `e516555e0cb6bcc6ba88c423e88c8dd054532425`,
distribution `openshift-acs`, RHACS **4.11**. Retain the bundled
[source license](../../openshift-docs/references/acs-4.11/LICENSE.openshift-docs),
[SOURCE.json](../../openshift-docs/references/acs-4.11/SOURCE.json) and
[conversion inventory](../../openshift-docs/references/acs-4.11/CONVERSION.json).

The full topic map includes cloud-service material, REST services and the common
object reference. Operational instructions here target self-managed RHACS in an
airgap. Cloud chapters do not authorize external service connections. External
links and unresolved upstream references are recorded, not silently downloaded.

| Procedure reference | Local source/section mapping |
| --- | --- |
| [Platform](platform.md) | System health dashboard component sections; Collector log retrieval; Central/SecuredCluster configuration options; trusted CAs and internal CA rotation procedures. Exact chapter links are in the reference. |
| [Vulnerabilities](vulnerabilities.md) | Vulnerability management and common tasks, image examination, offline Scanner-definition updates. |
| [Policies](policies.md) | Responding to violations, custom policies, admission enforcement, policies as code, declarative configuration; Policy Service method sections and linked request models; Vulnerability Exception Service. |
| [Compliance/network](compliance-network.md) | Compliance feature overview; OpenShift scan schedules, coverage and results; network graph, simulation and policy generation. Legacy compliance dashboard procedures are excluded from the 4.11 topic map. |
| [Lifecycle](lifecycle.md) | Offline images/Scanner updates, installation-method-specific upgrade prerequisites, backup/restore database/certificate/deployment procedures. |
| [Execution](execution.md) | REST method and common-object sections; roxctl command reference/options; unchanged sibling MCP safety/Day-2 contract. |
| [StackRox MCP](stackrox-mcp.md) | `stackrox/stackrox-mcp@57264356341b0f5a6aa3cb3b31da33dcb3307104`: config, tool implementations, Go/build definitions; Apache-2.0, Developer Preview. |

Modifications: condensed documented workflows, added cross-plane identity checks,
explicit evidence/freshness gaps, MCP/oc/REST routing, fresh once approvals and
outcome verification. MCP mappings and permission profiles are project adaptations.
They neither certify product compatibility nor grant RHACS/OpenShift permissions.
Do not substitute Kubernetes schemas for Central API models. For any version
other than 4.11 request matching local evidence before version-specific procedures.
