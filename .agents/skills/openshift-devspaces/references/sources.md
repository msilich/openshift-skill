# Dev Spaces procedure sources and modifications

This skill and its references are project-authored adaptations of the official
Red Hat OpenShift Dev Spaces 3.29 documentation. The MCP/oc mapping, evidence
boundaries and OpenCode approval routing are project adaptations, not vendor
certification. The Dev Spaces skill text and adapted product documentation are
distributed under [CC BY-SA 3.0](../../openshift-docs/references/devspaces-3.29/LICENSE.md).
Retain the [Red Hat legal notice](../../openshift-docs/references/devspaces-3.29/LEGAL-NOTICE.md).
The importer code remains under the repository's code license.

Source: [official 3.29 documentation](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29).
No public product Git revision is asserted. The original HTML document fragments
and illustrations were retrieved on September 7, 2026 and pinned in an archive:
`995e09d2a2796f05c9285d54c79be3bc373552efb2536468f3df2dcb3d2621a2` (SHA-256).
Every URL, retrieval time, HTTP-response hash and retained-fragment hash is in
[SOURCE.json](../../openshift-docs/references/devspaces-3.29/SOURCE.json).
This covers all 302 HTML TOC topics, not external websites referenced by those topics.

The links below are relative to this file. Open the listed chapter and its relevant
section before using a procedure; follow its local child-topic links as needed.

| Local workflow | Product chapter and section to read |
| --- | --- |
| Version/platform prerequisites | [Supported platforms and architectures](../../openshift-docs/references/devspaces-3.29/plan-supported_platforms_ref.md), complete topic; [resource requirements](../../openshift-docs/references/devspaces-3.29/plan-proc_calculating_resource_requirements.md), Before you begin and Procedure |
| Installation and ownership | [How the installation works](../../openshift-docs/references/devspaces-3.29/install-con_installation_overview.md), Installation methods and Deployment scenarios; [installation map](../../openshift-docs/references/devspaces-3.29/install-assembly_installing_dev_spaces.md) |
| Operator configuration | [Customize the central configuration](../../openshift-docs/references/devspaces-3.29/configure-assembly_configuring_the_checluster_custom_resource.md); [CheCluster fields](../../openshift-docs/references/devspaces-3.29/configure-ref_checluster_custom_resource_fields.md); [Dev Workspace Operator CRs](../../openshift-docs/references/devspaces-3.29/configure-ref_devworkspace_operator_custom_resources.md). Select the relevant field, then verify it in the live schema. |
| Upgrade readiness and verification | [Pre-upgrade checklist](../../openshift-docs/references/devspaces-3.29/upgrade-ref_pre_upgrade_checklist.md); [Verify the upgrade](../../openshift-docs/references/devspaces-3.29/upgrade-proc_verify_upgrade_completed.md), Procedure and Results |
| Devfiles and workspace lifecycle | [Devfile introduction](../../openshift-docs/references/devspaces-3.29/develop-con_devfile_introduction.md); [workspace CLI map](../../openshift-docs/references/devspaces-3.29/integrate-assembly_managing_workspaces_with_platform_tools.md), List/Create/Stop/Start/Remove workspace child topics. Automatic token injection described there is not authority to change this project's explicit identity contract. |
| Persistent data | [Storage configuration](../../openshift-docs/references/devspaces-3.29/configure-assembly_configuring_storage.md); [persistence across restarts](../../openshift-docs/references/devspaces-3.29/configure-con_persistent_user_home.md); [request PVC storage](../../openshift-docs/references/devspaces-3.29/develop-proc_requesting_persistent_storage_with_pvc.md), Procedure |
| Airgap installation | [Deploy in an air-gapped environment](../../openshift-docs/references/devspaces-3.29/install-proc_installing_dev_spaces_in_a_restricted_environment_on_openshift.md), Before you begin and Procedure; [airgap upgrade](../../openshift-docs/references/devspaces-3.29/upgrade-proc_upgrading_dev_spaces_in_a_restricted_environment.md) |
| Packages and extensions | [Restricted dependencies](../../openshift-docs/references/devspaces-3.29/integrate-assembly_connecting_package_registries.md), relevant language child topic; [private extension registry](../../openshift-docs/references/devspaces-3.29/extend-assembly_deploying_private_registry.md) |
| Pending workspace, PVC, image pull | [Startup failures](../../openshift-docs/references/devspaces-3.29/troubleshoot-ref_troubleshooting_workspace_startup_failures.md), Pod scheduling errors, Image pull errors, DevWorkspace errors and Resource quota errors |
| IDE/network access | [Network problems](../../openshift-docs/references/devspaces-3.29/troubleshoot-proc_troubleshooting_network_problems.md), Procedure; [workspace logs](../../openshift-docs/references/devspaces-3.29/troubleshoot-proc_viewing_workspace_logs_in_cli.md), Procedure |
| Devfile or OAuth failures | [Devfile errors](../../openshift-docs/references/devspaces-3.29/troubleshoot-ref_troubleshooting_devfile_issues.md); [OAuth configuration](../../openshift-docs/references/devspaces-3.29/troubleshoot-ref_troubleshooting_oauth_configuration.md), relevant error section |

Modification notes: condensed the product procedures into task-specific routing
and diagnostic checks; replaced ambient CLI identity with the existing explicit
kubeconfig contract; required schema evidence, Secret choice, approval and outcome
verification. No upstream Eclipse Che documentation, token helper or new MCP server
is substituted for the product source.
