<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
DeploymentConfigRollback provides the input to rollback generation.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `name`

- `spec`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the deployment config that will be rolled back. |
| `spec` | `object` | DeploymentConfigRollbackSpec represents the options for rollback generation. |
| `updatedAnnotations` | `object (string)` | UpdatedAnnotations is a set of new annotations that will be added in the deployment config. |

## .spec

Description
DeploymentConfigRollbackSpec represents the options for rollback generation.

Type
`object`

Required
- `from`

- `includeTriggers`

- `includeTemplate`

- `includeReplicationMeta`

- `includeStrategy`

| Property | Type | Description |
|----|----|----|
| `from` | [`ObjectReference`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | From points to a ReplicationController which is a deployment. |
| `includeReplicationMeta` | `boolean` | IncludeReplicationMeta specifies whether to include the replica count and selector. |
| `includeStrategy` | `boolean` | IncludeStrategy specifies whether to include the deployment Strategy. |
| `includeTemplate` | `boolean` | IncludeTemplate specifies whether to include the PodTemplateSpec. |
| `includeTriggers` | `boolean` | IncludeTriggers specifies whether to include config Triggers. |
| `revision` | `integer` | Revision to rollback to. If set to 0, rollback to the last revision. |

# API endpoints

The following API endpoints are available:

- `/apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/rollback`

  - `POST`: create rollback of a DeploymentConfig

## /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/rollback

| Parameter | Type     | Description                          |
|-----------|----------|--------------------------------------|
| `name`    | `string` | name of the DeploymentConfigRollback |

Global path parameters

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Global query parameters

HTTP method
`POST`

Description
create rollback of a DeploymentConfig

| Parameter | Type | Description |
|----|----|----|
| `body` | [`DeploymentConfigRollback`](deploymentconfigrollback-apps-openshift-io-v1.md#deploymentconfigrollback-apps-openshift-io-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`DeploymentConfigRollback`](deploymentconfigrollback-apps-openshift-io-v1.md#deploymentconfigrollback-apps-openshift-io-v1) schema |
| 201 - Created | [`DeploymentConfigRollback`](deploymentconfigrollback-apps-openshift-io-v1.md#deploymentconfigrollback-apps-openshift-io-v1) schema |
| 202 - Accepted | [`DeploymentConfigRollback`](deploymentconfigrollback-apps-openshift-io-v1.md#deploymentconfigrollback-apps-openshift-io-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
