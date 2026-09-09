<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="CreateComplianceScanConfiguration_ComplianceScanConfigurationService"></a>

# CreateComplianceScanConfiguration

`POST /v2/compliance/scan/configurations`

CreateComplianceScanConfiguration creates a compliance scan configuration

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V2ComplianceScanConfiguration](../CommonObjectReference/CommonObjectReference.md#V2ComplianceScanConfiguration_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[V2ComplianceScanConfiguration](../CommonObjectReference/CommonObjectReference.md#V2ComplianceScanConfiguration_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ComplianceScanConfiguration](../CommonObjectReference/CommonObjectReference.md#V2ComplianceScanConfiguration_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="DeleteComplianceScanConfiguration_ComplianceScanConfigurationService"></a>

# DeleteComplianceScanConfiguration

`DELETE /v2/compliance/scan/configurations/{id}`

DeleteComplianceScanConfiguration removes the compliance scan configuration with given Name

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_path_parameters"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_2"></a>

## Return Type

`Object`

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="DeleteReport_ComplianceScanConfigurationService"></a>

# DeleteReport

`DELETE /v2/compliance/scan/configurations/reports/{id}`

DeleteReport deletes a given snapshot (scan execution).

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_path_parameters_2"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_3"></a>

## Return Type

`Object`

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples

<a id="GetComplianceScanConfiguration_ComplianceScanConfigurationService"></a>

# GetComplianceScanConfiguration

`GET /v2/compliance/scan/configurations/{id}`

GetComplianceScanConfiguration retrieves the specified compliance scan configurations

<a id="_description_4"></a>

## Description

<a id="_parameters_4"></a>

## Parameters

<a id="_path_parameters_3"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_4"></a>

## Return Type

[V2ComplianceScanConfigurationStatus](../CommonObjectReference/CommonObjectReference.md#V2ComplianceScanConfigurationStatus_CommonObjectReference)

<a id="_content_type_4"></a>

## Content Type

- application/json

<a id="_responses_4"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ComplianceScanConfigurationStatus](../CommonObjectReference/CommonObjectReference.md#V2ComplianceScanConfigurationStatus_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_4"></a>

## Samples

<a id="GetMyReportHistory_ComplianceScanConfigurationService"></a>

# GetMyReportHistory

`GET /v2/compliance/scan/configurations/{id}/reports/my-history`

GetMyReportHistory returns a list of snapshots (scan executions) executed by the current user from a given scan configuration.

<a id="_description_5"></a>

## Description

<a id="_parameters_5"></a>

## Parameters

<a id="_path_parameters_4"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_query_parameters"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| reportParamQuery.query |  | \- | null |  |
| reportParamQuery.pagination.limit |  | \- | null |  |
| reportParamQuery.pagination.offset |  | \- | null |  |
| reportParamQuery.pagination.sortOption.field |  | \- | null |  |
| reportParamQuery.pagination.sortOption.reversed |  | \- | null |  |
| reportParamQuery.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| reportParamQuery.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_5"></a>

## Return Type

[V2ComplianceReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ComplianceReportHistoryResponse_CommonObjectReference)

<a id="_content_type_5"></a>

## Content Type

- application/json

<a id="_responses_5"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ComplianceReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ComplianceReportHistoryResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_5"></a>

## Samples

<a id="GetReportHistory_ComplianceScanConfigurationService"></a>

# GetReportHistory

`GET /v2/compliance/scan/configurations/{id}/reports/history`

GetReportHistory returns a list of snapshots (scan executions) from a given scan configuration.

<a id="_description_6"></a>

## Description

<a id="_parameters_6"></a>

## Parameters

<a id="_path_parameters_5"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_query_parameters_2"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| reportParamQuery.query |  | \- | null |  |
| reportParamQuery.pagination.limit |  | \- | null |  |
| reportParamQuery.pagination.offset |  | \- | null |  |
| reportParamQuery.pagination.sortOption.field |  | \- | null |  |
| reportParamQuery.pagination.sortOption.reversed |  | \- | null |  |
| reportParamQuery.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| reportParamQuery.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_6"></a>

## Return Type

[V2ComplianceReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ComplianceReportHistoryResponse_CommonObjectReference)

<a id="_content_type_6"></a>

## Content Type

- application/json

<a id="_responses_6"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ComplianceReportHistoryResponse](../CommonObjectReference/CommonObjectReference.md#V2ComplianceReportHistoryResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_6"></a>

## Samples

<a id="ListComplianceScanConfigClusterProfiles_ComplianceScanConfigurationService"></a>

# ListComplianceScanConfigClusterProfiles

`GET /v2/compliance/scan/configurations/clusters/{clusterId}/profiles/collection`

GetComplianceScanConfiguration retrieves the specified compliance scan configurations

<a id="_description_7"></a>

## Description

<a id="_parameters_7"></a>

## Parameters

<a id="_path_parameters_6"></a>

### Path Parameters

| Name      | Description | Required | Default | Pattern |
|-----------|-------------|----------|---------|---------|
| clusterId |             | X        | null    |         |

<a id="_query_parameters_3"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query.query |  | \- | null |  |
| query.pagination.limit |  | \- | null |  |
| query.pagination.offset |  | \- | null |  |
| query.pagination.sortOption.field |  | \- | null |  |
| query.pagination.sortOption.reversed |  | \- | null |  |
| query.pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| query.pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_7"></a>

## Return Type

[V2ListComplianceScanConfigsClusterProfileResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceScanConfigsClusterProfileResponse_CommonObjectReference)

<a id="_content_type_7"></a>

## Content Type

- application/json

<a id="_responses_7"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceScanConfigsClusterProfileResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceScanConfigsClusterProfileResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_7"></a>

## Samples

<a id="ListComplianceScanConfigProfiles_ComplianceScanConfigurationService"></a>

# ListComplianceScanConfigProfiles

`GET /v2/compliance/scan/configurations/profiles/collection`

ListComplianceScanConfigurations lists all the compliance operator scan configurations for the secured clusters

<a id="_description_8"></a>

## Description

<a id="_parameters_8"></a>

## Parameters

<a id="_query_parameters_4"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query |  | \- | null |  |
| pagination.limit |  | \- | null |  |
| pagination.offset |  | \- | null |  |
| pagination.sortOption.field |  | \- | null |  |
| pagination.sortOption.reversed |  | \- | null |  |
| pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_8"></a>

## Return Type

[V2ListComplianceScanConfigsProfileResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceScanConfigsProfileResponse_CommonObjectReference)

<a id="_content_type_8"></a>

## Content Type

- application/json

<a id="_responses_8"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceScanConfigsProfileResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceScanConfigsProfileResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_8"></a>

## Samples

<a id="ListComplianceScanConfigurations_ComplianceScanConfigurationService"></a>

# ListComplianceScanConfigurations

`GET /v2/compliance/scan/configurations`

ListComplianceScanConfigurations lists all the compliance operator scan configurations for the secured clusters

<a id="_description_9"></a>

## Description

<a id="_parameters_9"></a>

## Parameters

<a id="_query_parameters_5"></a>

### Query Parameters

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| query |  | \- | null |  |
| pagination.limit |  | \- | null |  |
| pagination.offset |  | \- | null |  |
| pagination.sortOption.field |  | \- | null |  |
| pagination.sortOption.reversed |  | \- | null |  |
| pagination.sortOption.aggregateBy.aggrFunc |  | \- | UNSET |  |
| pagination.sortOption.aggregateBy.distinct |  | \- | null |  |

<a id="_return_type_9"></a>

## Return Type

[V2ListComplianceScanConfigurationsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceScanConfigurationsResponse_CommonObjectReference)

<a id="_content_type_9"></a>

## Content Type

- application/json

<a id="_responses_9"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ListComplianceScanConfigurationsResponse](../CommonObjectReference/CommonObjectReference.md#V2ListComplianceScanConfigurationsResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_9"></a>

## Samples

<a id="RunComplianceScanConfiguration_ComplianceScanConfigurationService"></a>

# RunComplianceScanConfiguration

`POST /v2/compliance/scan/configurations/{id}/run`

RunComplianceScanConfiguration launches scan for the specified scan configuration, which will invoke scans to run for the applicable profiles across the configured clusters.

<a id="_description_10"></a>

## Description

<a id="_parameters_10"></a>

## Parameters

<a id="_path_parameters_7"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_return_type_10"></a>

## Return Type

`Object`

<a id="_content_type_10"></a>

## Content Type

- application/json

<a id="_responses_10"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_10"></a>

## Samples

<a id="RunReport_ComplianceScanConfigurationService"></a>

# RunReport

`POST /v2/compliance/scan/configurations/reports/run`

RunReport runs an on demand compliance report for the scan configuration

<a id="_description_11"></a>

## Description

<a id="_parameters_11"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V2ComplianceRunReportRequest](../CommonObjectReference/CommonObjectReference.md#V2ComplianceRunReportRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_11"></a>

## Return Type

[V2ComplianceRunReportResponse](../CommonObjectReference/CommonObjectReference.md#V2ComplianceRunReportResponse_CommonObjectReference)

<a id="_content_type_11"></a>

## Content Type

- application/json

<a id="_responses_11"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V2ComplianceRunReportResponse](../CommonObjectReference/CommonObjectReference.md#V2ComplianceRunReportResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_11"></a>

## Samples

<a id="UpdateComplianceScanConfiguration_ComplianceScanConfigurationService"></a>

# UpdateComplianceScanConfiguration

`PUT /v2/compliance/scan/configurations/{id}`

UpdateComplianceScanConfiguration updates a compliance scan configuration

<a id="_description_12"></a>

## Description

<a id="_parameters_12"></a>

## Parameters

<a id="_path_parameters_8"></a>

### Path Parameters

| Name | Description | Required | Default | Pattern |
|------|-------------|----------|---------|---------|
| id   |             | X        | null    |         |

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [ComplianceScanConfigurationServiceUpdateComplianceScanConfigurationBody](../CommonObjectReference/CommonObjectReference.md#ComplianceScanConfigurationServiceUpdateComplianceScanConfigurationBody_CommonObjectReference) | X |  |  |

<a id="_return_type_12"></a>

## Return Type

`Object`

<a id="_content_type_12"></a>

## Content Type

- application/json

<a id="_responses_12"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | `Object` |
| 0 | An unexpected error response. | [RpcStatus](../CommonObjectReference/CommonObjectReference.md#RpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_12"></a>

## Samples
