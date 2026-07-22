# Evidence Reporting

For each conclusion, report the selected cluster/context, resource, API version, result, and source command.

Use this compact shape:

```text
Resource: <canonical resource>
API version: <exact served version>
Finding: <verified field, constraint, or unsupported item>
Source: <exact oc command or OpenAPI serverRelativeURL>
Status: verified | unsupported | unverified | conflicting
```

For a CRD finding, add:

```text
CRD: <plural>.<group>
Schema path: .spec.versions[name=<version>].schema.openAPIV3Schema...
```

Apply these rules:

- Say `unsupported` only when live discovery proves the resource or version is absent.
- Say `unverified` when evidence could not be collected.
- Say `conflicting` when live sources disagree, and show each source separately.
- Distinguish schema support from RBAC authorization and from admission success.
- Do not present remembered documentation, examples, generated YAML, or model reasoning as schema evidence.
