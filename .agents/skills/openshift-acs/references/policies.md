# Policies and violations

Read [Responding to violations](../../openshift-docs/references/acs-4.11/operating/respond-to-violations.md),
[custom policies](../../openshift-docs/references/acs-4.11/operating/manage_security_policies/custom-security-policies.md)
and [admission enforcement](../../openshift-docs/references/acs-4.11/operating/manage_security_policies/use-admission-controller-enforcement.md).
Use the sections covering the observed lifecycle stage and enforcement action.
See [sources](sources.md) and [execution](execution.md).

Read the policy ID/version, criteria, lifecycle stage, affected resource and event
time. Explain which evidence matches which criterion and whether enforcement was
configured, attempted or observed. A violation is not proof that admission was
blocked. Preserve evidence before proposing remediation.

Determine ownership from [policies as code](../../openshift-docs/references/acs-4.11/operating/manage_security_policies/managing-policies-as-code.md)
and [declarative configuration](../../openshift-docs/references/acs-4.11/configuration/declarative-configuration-using.md).
Modify the Git/manifest source for managed configuration; direct Central changes
can be rejected or reconciled away. Do not repeatedly overwrite a controller.

Policy disablement, enforcement reduction, vulnerability exceptions, deletion and
notifier/integration changes are high-risk. Explain affected scope, expiration,
compensating checks and rollback. Do not suppress findings merely to make a report
green. Use [Policy Service](../../openshift-docs/references/acs-4.11/rest_api/PolicyService/PolicyService.md)
GetPolicy, PutPolicy, DryRunPolicy and SubmitDryRunPolicyJob sections plus their
linked request models. Asynchronous dry-run jobs are stateful operations.
For exceptions consult [Vulnerability Exception Service](../../openshift-docs/references/acs-4.11/rest_api/VulnerabilityExceptionService/VulnerabilityExceptionService.md)
and the exact method/request model; do not guess endpoints.

Only an explicitly requested change enters the once-approved workflow. Verify the
stored policy, relevant enforcement/violation behavior and absence of unintended
scope expansion. A successful HTTP response alone is insufficient.
