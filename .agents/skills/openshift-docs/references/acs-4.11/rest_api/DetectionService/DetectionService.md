<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="DetectBuildTime_DetectionService"></a>

# DetectBuildTime

`POST /v1/detect/build`

DetectBuildTime checks if any images violate build time policies.

<a id="_description"></a>

## Description

<a id="_parameters"></a>

## Parameters

<a id="_body_parameter"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1BuildDetectionRequest](../CommonObjectReference/CommonObjectReference.md#V1BuildDetectionRequest_CommonObjectReference) | X |  |  |

<a id="_return_type"></a>

## Return Type

[V1BuildDetectionResponse](../CommonObjectReference/CommonObjectReference.md#V1BuildDetectionResponse_CommonObjectReference)

<a id="_content_type"></a>

## Content Type

- application/json

<a id="_responses"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1BuildDetectionResponse](../CommonObjectReference/CommonObjectReference.md#V1BuildDetectionResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples"></a>

## Samples

<a id="DetectDeployTime_DetectionService"></a>

# DetectDeployTime

`POST /v1/detect/deploy`

DetectDeployTime checks if any deployments violate deploy time policies.

<a id="_description_2"></a>

## Description

<a id="_parameters_2"></a>

## Parameters

<a id="_body_parameter_2"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1DeployDetectionRequest](../CommonObjectReference/CommonObjectReference.md#V1DeployDetectionRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_2"></a>

## Return Type

[V1DeployDetectionResponse](../CommonObjectReference/CommonObjectReference.md#V1DeployDetectionResponse_CommonObjectReference)

<a id="_content_type_2"></a>

## Content Type

- application/json

<a id="_responses_2"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DeployDetectionResponse](../CommonObjectReference/CommonObjectReference.md#V1DeployDetectionResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_2"></a>

## Samples

<a id="DetectDeployTimeFromYAML_DetectionService"></a>

# DetectDeployTimeFromYAML

`POST /v1/detect/deploy/yaml`

DetectDeployTimeFromYAML checks if the given deployment yaml violates any deploy time policies.

<a id="_description_3"></a>

## Description

<a id="_parameters_3"></a>

## Parameters

<a id="_body_parameter_3"></a>

### Body Parameter

| Name | Description | Required | Default | Pattern |
|----|----|----|----|----|
| body | [V1DeployYAMLDetectionRequest](../CommonObjectReference/CommonObjectReference.md#V1DeployYAMLDetectionRequest_CommonObjectReference) | X |  |  |

<a id="_return_type_3"></a>

## Return Type

[V1DeployDetectionResponse](../CommonObjectReference/CommonObjectReference.md#V1DeployDetectionResponse_CommonObjectReference)

<a id="_content_type_3"></a>

## Content Type

- application/json

<a id="_responses_3"></a>

## Responses

| Code | Message | Datatype |
|----|----|----|
| 200 | A successful response. | [V1DeployDetectionResponse](../CommonObjectReference/CommonObjectReference.md#V1DeployDetectionResponse_CommonObjectReference) |
| 0 | An unexpected error response. | [GoogleRpcStatus](../CommonObjectReference/CommonObjectReference.md#GoogleRpcStatus_CommonObjectReference) |

HTTP Response Codes

<a id="_samples_3"></a>

## Samples
