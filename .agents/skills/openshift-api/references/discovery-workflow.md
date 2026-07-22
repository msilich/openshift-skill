# Discovery Workflow

## 1. Resolve the resource

Use the same explicit, single-context kubeconfig for every command shown below; never rely on or change the ambient context. Run `oc api-resources -o wide` first. Record the exact `NAME`, `APIVERSION`, `NAMESPACED`, `KIND`, and supported verbs. When a short name or plural is ambiguous, use the fully qualified resource name returned by discovery, such as `<plural>.<group>`.

Do not assume that an API installed on one OpenShift cluster exists on another.

## 2. Confirm the served version

Run `oc api-versions` and require an exact match for the selected API version. Core resources use versions such as `v1`; grouped resources use `<group>/<version>`.

If the version is absent, stop. Do not silently fall back to another version because fields and validation may differ.

## 3. Inspect `oc explain`

Use the explicit version on every call:

```text
oc explain <resource> --api-version=<group/version>
oc explain <resource>.<field-path> --api-version=<group/version> --recursive
```

Use `<resource>` itself as the recursive target when the question concerns the complete resource. A failed or incomplete `explain` result is a reason to continue, not a reason to infer fields.

## 4. Inspect OpenAPI v3

Run:

```text
oc get --raw /openapi/v3
```

Find the entry for the exact group/version and copy its `serverRelativeURL` verbatim, including any query string or hash. Then fetch it:

```text
oc get --raw '<serverRelativeURL from the index>'
```

Locate the schema by its fully qualified definition and preserve required fields, enums, formats, defaults, list semantics, and validation extensions in the evidence. Do not guess a URL or reuse a URL from another cluster.

## 5. Inspect a CRD schema

Only use this step for a resource backed by a CRD. Verify the CRD name, then run:

```text
oc get crd <plural>.<group> -o json
```

Within `.spec.versions[]`, select the entry whose `.name` matches the version already verified by `oc api-versions`. Read `.schema.openAPIV3Schema`; also record `.served`, `.storage`, `.deprecated`, and conversion settings when relevant.

If the matching version has no structural schema, state that limitation. Never fabricate the missing schema.

## Failure handling

- Failure of `api-resources` or `api-versions`: target discovery is unavailable; stop.
- Failure of `oc explain`: continue to OpenAPI v3.
- Missing OpenAPI schema for a CRD: inspect the CRD object.
- No field-bearing source: report the requested field or manifest as unverified and request the missing command output or cluster access.
