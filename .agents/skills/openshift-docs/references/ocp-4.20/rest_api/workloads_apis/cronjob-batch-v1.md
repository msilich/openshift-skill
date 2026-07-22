<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Description
CronJob represents the configuration of a single cron job.

Type
`object`

# Specification

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | CronJobSpec describes how the job execution will look like and when it will actually run. |
| `status` | `object` | CronJobStatus represents the current state of a cron job. |

## .spec

Description
CronJobSpec describes how the job execution will look like and when it will actually run.

Type
`object`

Required
- `schedule`

- `jobTemplate`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>concurrencyPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies how to treat concurrent executions of a Job. Valid values are:</p>
<p>- "Allow" (default): allows CronJobs to run concurrently; - "Forbid": forbids concurrent runs, skipping next run if previous run hasn’t finished yet; - "Replace": cancels currently running job and replaces it with a new one</p>
<p>Possible enum values: - <code>"Allow"</code> allows CronJobs to run concurrently. - <code>"Forbid"</code> forbids concurrent runs, skipping next run if previous hasn’t finished yet. - <code>"Replace"</code> cancels currently running job and replaces it with a new one.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>failedJobsHistoryLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The number of failed finished jobs to retain. Value must be non-negative integer. Defaults to 1.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>jobTemplate</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>JobTemplateSpec describes the data a Job should have when created from a template</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>schedule</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The schedule in Cron format, see <a href="https://en.wikipedia.org/wiki/Cron">https://en.wikipedia.org/wiki/Cron</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>startingDeadlineSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional deadline in seconds for starting the job if it misses scheduled time for any reason. Missed jobs executions will be counted as failed ones.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>successfulJobsHistoryLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>The number of successful finished jobs to retain. Value must be non-negative integer. Defaults to 3.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>suspend</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>This flag tells the controller to suspend subsequent executions, it does not apply to already started executions. Defaults to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>timeZone</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The time zone name for the given schedule, see <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">https://en.wikipedia.org/wiki/List_of_tz_database_time_zones</a>. If not specified, this will default to the time zone of the kube-controller-manager process. The set of valid time zone names and the time zone offset is loaded from the system-wide time zone database by the API server during CronJob validation and the controller manager during execution. If no system-wide time zone database can be found a bundled version of the database is used instead. If the time zone name becomes invalid during the lifetime of a CronJob or due to a change in host configuration, the controller will stop creating new new Jobs and will create a system event with the reason UnknownTimeZone. More information can be found in <a href="https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones">https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones</a></p></td>
</tr>
</tbody>
</table>

## .spec.jobTemplate

Description
JobTemplateSpec describes the data a Job should have when created from a template

Type
`object`

| Property | Type | Description |
|----|----|----|
| `metadata` | [`ObjectMeta`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata of the jobs created from this template. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | JobSpec describes how the job execution will look like. |

## .spec.jobTemplate.spec

Description
JobSpec describes how the job execution will look like.

Type
`object`

Required
- `template`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>activeDeadlineSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the duration in seconds relative to the startTime that the job may be continuously active before the system tries to terminate it; value must be positive integer. If a Job is suspended (at creation or through an update), this timer will effectively be stopped and reset when the Job is resumed again.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>backoffLimit</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the number of retries before marking this job failed. Defaults to 6</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>backoffLimitPerIndex</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the limit for the number of retries within an index before marking this index as failed. When enabled the number of failures per index is kept in the pod’s batch.kubernetes.io/job-index-failure-count annotation. It can only be set when Job’s completionMode=Indexed, and the Pod’s restart policy is Never. The field is immutable.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>completionMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>completionMode specifies how Pod completions are tracked. It can be <code>NonIndexed</code> (default) or <code>Indexed</code>.</p>
<p><code>NonIndexed</code> means that the Job is considered complete when there have been .spec.completions successfully completed Pods. Each Pod completion is homologous to each other.</p>
<p><code>Indexed</code> means that the Pods of a Job get an associated completion index from 0 to (.spec.completions - 1), available in the annotation batch.kubernetes.io/job-completion-index. The Job is considered complete when there is one successfully completed Pod for each index. When value is <code>Indexed</code>, .spec.completions must be specified and <code>.spec.parallelism</code> must be less than or equal to 10^5. In addition, The Pod name takes the form <code>$(job-name)-$(index)-$(random-string)</code>, the Pod hostname takes the form <code>$(job-name)-$(index)</code>.</p>
<p>More completion modes can be added in the future. If the Job controller observes a mode that it doesn’t recognize, which is possible during upgrades due to version skew, the controller skips updates for the Job.</p>
<p>Possible enum values: - <code>"Indexed"</code> is a Job completion mode. In this mode, the Pods of a Job get an associated completion index from 0 to (.spec.completions - 1). The Job is considered complete when a Pod completes for each completion index. - <code>"NonIndexed"</code> is a Job completion mode. In this mode, the Job is considered complete when there have been .spec.completions successfully completed Pods. Pod completions are homologous to each other.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>completions</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the desired number of successfully finished pods the job should be run with. Setting to null means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value. Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: <a href="https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/">https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managedBy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>ManagedBy field indicates the controller that manages a Job. The k8s Job controller reconciles jobs which don’t have this field at all or the field value is the reserved string <code>kubernetes.io/job-controller</code>, but skips reconciling Jobs with a custom value for this field. The value must be a valid domain-prefixed path (e.g. acme.io/foo) - all characters before the first "/" must be a valid subdomain as defined by RFC 1123. All characters trailing the first "/" must be valid HTTP Path characters as defined by RFC 3986. The value cannot exceed 63 characters. This field is immutable.</p>
<p>This field is beta-level. The job controller accepts setting the field when the feature gate JobManagedBy is enabled (enabled by default).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>manualSelector</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>manualSelector controls generation of pod labels and pod selectors. Leave <code>manualSelector</code> unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template. When true, the user is responsible for picking unique labels and specifying the selector. Failure to pick a unique label may cause this and other jobs to not function correctly. However, You may see <code>manualSelector=true</code> in jobs that were created with the old <code>extensions/v1beta1</code> API. More info: <a href="https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector">https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxFailedIndexes</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the maximal number of failed indexes before marking the Job as failed, when backoffLimitPerIndex is set. Once the number of failed indexes exceeds this number the entire Job is marked as Failed and its execution is terminated. When left as null the job continues execution of all of its indexes and is marked with the <code>Complete</code> Job condition. It can only be specified when backoffLimitPerIndex is set. It can be null or up to completions. It is required and must be less than or equal to 10^4 when is completions greater than 10^5.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>parallelism</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) &lt; .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: <a href="https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/">https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>podFailurePolicy</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodFailurePolicy describes how failed pods influence the backoffLimit.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>podReplacementPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>podReplacementPolicy specifies when to create replacement Pods. Possible values are: - TerminatingOrFailed means that we recreate pods when they are terminating (has a metadata.deletionTimestamp) or failed. - Failed means to wait until a previously created Pod is fully terminated (has phase Failed or Succeeded) before creating a replacement Pod.</p>
<p>When using podFailurePolicy, Failed is the the only allowed value. TerminatingOrFailed and Failed are allowed values when podFailurePolicy is not in use. This is an beta field. To use this, enable the JobPodReplacementPolicy feature toggle. This is on by default.</p>
<p>Possible enum values: - <code>"Failed"</code> means to wait until a previously created Pod is fully terminated (has phase Failed or Succeeded) before creating a replacement Pod. - <code>"TerminatingOrFailed"</code> means that we recreate pods when they are terminating (has a metadata.deletionTimestamp) or failed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector"><code>LabelSelector</code></a></p></td>
<td style="text-align: left;"><p>A label query over pods that should match the pod count. Normally, the system sets this field for you. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors">https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>successPolicy</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>SuccessPolicy describes when a Job can be declared as succeeded based on the success of some indexes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>suspend</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>suspend specifies whether the Job controller should create Pods or not. If a Job is created with suspend set to true, no Pods are created by the Job controller. If a Job is suspended after creation (i.e. the flag goes from false to true), the Job controller will delete all active Pods associated with this Job. Users must design their workload to gracefully handle this. Suspending a Job will reset the StartTime field of the Job, effectively resetting the ActiveDeadlineSeconds timer too. Defaults to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>template</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-api-core-v1-PodTemplateSpec"><code>PodTemplateSpec</code></a></p></td>
<td style="text-align: left;"><p>Describes the pod that will be created when executing a job. The only allowed template.spec.restartPolicy values are "Never" or "OnFailure". More info: <a href="https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/">https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ttlSecondsAfterFinished</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won’t be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes.</p></td>
</tr>
</tbody>
</table>

## .spec.jobTemplate.spec.podFailurePolicy

Description
PodFailurePolicy describes how failed pods influence the backoffLimit.

Type
`object`

Required
- `rules`

| Property | Type | Description |
|----|----|----|
| `rules` | `array` | A list of pod failure policy rules. The rules are evaluated in order. Once a rule matches a Pod failure, the remaining of the rules are ignored. When no rule matches the Pod failure, the default handling applies - the counter of pod failures is incremented and it is checked against the backoffLimit. At most 20 elements are allowed. |
| `rules[]` | `object` | PodFailurePolicyRule describes how a pod failure is handled when the requirements are met. One of onExitCodes and onPodConditions, but not both, can be used in each rule. |

## .spec.jobTemplate.spec.podFailurePolicy.rules

Description
A list of pod failure policy rules. The rules are evaluated in order. Once a rule matches a Pod failure, the remaining of the rules are ignored. When no rule matches the Pod failure, the default handling applies - the counter of pod failures is incremented and it is checked against the backoffLimit. At most 20 elements are allowed.

Type
`array`

## .spec.jobTemplate.spec.podFailurePolicy.rules\[\]

Description
PodFailurePolicyRule describes how a pod failure is handled when the requirements are met. One of onExitCodes and onPodConditions, but not both, can be used in each rule.

Type
`object`

Required
- `action`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>action</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are:</p>
<p>- FailJob: indicates that the pod’s job is marked as Failed and all running pods are terminated. - FailIndex: indicates that the pod’s index is marked as Failed and will not be restarted. - Ignore: indicates that the counter towards the .backoffLimit is not incremented and a replacement pod is created. - Count: indicates that the pod is handled in the default way - the counter towards the .backoffLimit is incremented. Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule.</p>
<p>Possible enum values: - <code>"Count"</code> This is an action which might be taken on a pod failure - the pod failure is handled in the default way - the counter towards .backoffLimit, represented by the job’s .status.failed field, is incremented. - <code>"FailIndex"</code> This is an action which might be taken on a pod failure - mark the Job’s index as failed to avoid restarts within this index. This action can only be used when backoffLimitPerIndex is set. - <code>"FailJob"</code> This is an action which might be taken on a pod failure - mark the pod’s job as Failed and terminate all running pods. - <code>"Ignore"</code> This is an action which might be taken on a pod failure - the counter towards .backoffLimit, represented by the job’s .status.failed field, is not incremented and a replacement pod is created.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>onExitCodes</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodFailurePolicyOnExitCodesRequirement describes the requirement for handling a failed pod based on its container exit codes. In particular, it lookups the .state.terminated.exitCode for each app container and init container status, represented by the .status.containerStatuses and .status.initContainerStatuses fields in the Pod status, respectively. Containers completed with success (exit code 0) are excluded from the requirement check.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>onPodConditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>onPodConditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PodFailurePolicyOnPodConditionsPattern describes a pattern for matching an actual pod condition type.</p></td>
</tr>
</tbody>
</table>

## .spec.jobTemplate.spec.podFailurePolicy.rules\[\].onExitCodes

Description
PodFailurePolicyOnExitCodesRequirement describes the requirement for handling a failed pod based on its container exit codes. In particular, it lookups the .state.terminated.exitCode for each app container and init container status, represented by the .status.containerStatuses and .status.initContainerStatuses fields in the Pod status, respectively. Containers completed with success (exit code 0) are excluded from the requirement check.

Type
`object`

Required
- `operator`

- `values`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>containerName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Restricts the check for exit codes to the container with the specified name. When null, the rule applies to all containers. When specified, it should match one the container or initContainer names in the pod template.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Represents the relationship between the container exit code(s) and the specified values. Containers completed with success (exit code 0) are excluded from the requirement check. Possible values are:</p>
<p>- In: the requirement is satisfied if at least one container exit code (might be multiple if there are multiple containers not restricted by the 'containerName' field) is in the set of specified values. - NotIn: the requirement is satisfied if at least one container exit code (might be multiple if there are multiple containers not restricted by the 'containerName' field) is not in the set of specified values. Additional values are considered to be added in the future. Clients should react to an unknown operator by assuming the requirement is not satisfied.</p>
<p>Possible enum values: - <code>"In"</code> - <code>"NotIn"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>values</code></p></td>
<td style="text-align: left;"><p><code>array (integer)</code></p></td>
<td style="text-align: left;"><p>Specifies the set of values. Each returned container exit code (might be multiple in case of multiple containers) is checked against this set of values with respect to the operator. The list of values must be ordered and must not contain duplicates. Value '0' cannot be used for the In operator. At least one element is required. At most 255 elements are allowed.</p></td>
</tr>
</tbody>
</table>

## .spec.jobTemplate.spec.podFailurePolicy.rules\[\].onPodConditions

Description
Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.

Type
`array`

## .spec.jobTemplate.spec.podFailurePolicy.rules\[\].onPodConditions\[\]

Description
PodFailurePolicyOnPodConditionsPattern describes a pattern for matching an actual pod condition type.

Type
`object`

Required
- `type`

- `status`

| Property | Type | Description |
|----|----|----|
| `status` | `string` | Specifies the required Pod condition status. To match a pod condition it is required that the specified status equals the pod condition status. Defaults to True. |
| `type` | `string` | Specifies the required Pod condition type. To match a pod condition it is required that specified type equals the pod condition type. |

## .spec.jobTemplate.spec.successPolicy

Description
SuccessPolicy describes when a Job can be declared as succeeded based on the success of some indexes.

Type
`object`

Required
- `rules`

| Property | Type | Description |
|----|----|----|
| `rules` | `array` | rules represents the list of alternative rules for the declaring the Jobs as successful before `.status.succeeded >= .spec.completions`. Once any of the rules are met, the "SucceededCriteriaMet" condition is added, and the lingering pods are removed. The terminal state for such a Job has the "Complete" condition. Additionally, these rules are evaluated in order; Once the Job meets one of the rules, other rules are ignored. At most 20 elements are allowed. |
| `rules[]` | `object` | SuccessPolicyRule describes rule for declaring a Job as succeeded. Each rule must have at least one of the "succeededIndexes" or "succeededCount" specified. |

## .spec.jobTemplate.spec.successPolicy.rules

Description
rules represents the list of alternative rules for the declaring the Jobs as successful before `.status.succeeded >= .spec.completions`. Once any of the rules are met, the "SucceededCriteriaMet" condition is added, and the lingering pods are removed. The terminal state for such a Job has the "Complete" condition. Additionally, these rules are evaluated in order; Once the Job meets one of the rules, other rules are ignored. At most 20 elements are allowed.

Type
`array`

## .spec.jobTemplate.spec.successPolicy.rules\[\]

Description
SuccessPolicyRule describes rule for declaring a Job as succeeded. Each rule must have at least one of the "succeededIndexes" or "succeededCount" specified.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `succeededCount` | `integer` | succeededCount specifies the minimal required size of the actual set of the succeeded indexes for the Job. When succeededCount is used along with succeededIndexes, the check is constrained only to the set of indexes specified by succeededIndexes. For example, given that succeededIndexes is "1-4", succeededCount is "3", and completed indexes are "1", "3", and "5", the Job isn’t declared as succeeded because only "1" and "3" indexes are considered in that rules. When this field is null, this doesn’t default to any value and is never evaluated at any time. When specified it needs to be a positive integer. |
| `succeededIndexes` | `string` | succeededIndexes specifies the set of indexes which need to be contained in the actual set of the succeeded indexes for the Job. The list of indexes must be within 0 to ".spec.completions-1" and must not contain duplicates. At least one element is required. The indexes are represented as intervals separated by commas. The intervals can be a decimal integer or a pair of decimal integers separated by a hyphen. The number are listed in represented by the first and last element of the series, separated by a hyphen. For example, if the completed indexes are 1, 3, 4, 5 and 7, they are represented as "1,3-5,7". When this field is null, this field doesn’t default to any value and is never evaluated at any time. |

## .status

Description
CronJobStatus represents the current state of a cron job.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `active` | [`array (ObjectReference)`](../objects/index.md#io-k8s-api-core-v1-ObjectReference) | A list of pointers to currently running jobs. |
| `lastScheduleTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | Information when was the last time the job was successfully scheduled. |
| `lastSuccessfulTime` | [`Time`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | Information when was the last time the job successfully completed. |

# API endpoints

The following API endpoints are available:

- `/apis/batch/v1/cronjobs`

  - `GET`: list or watch objects of kind CronJob

- `/apis/batch/v1/watch/cronjobs`

  - `GET`: watch individual changes to a list of CronJob. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/batch/v1/namespaces/{namespace}/cronjobs`

  - `DELETE`: delete collection of CronJob

  - `GET`: list or watch objects of kind CronJob

  - `POST`: create a CronJob

- `/apis/batch/v1/watch/namespaces/{namespace}/cronjobs`

  - `GET`: watch individual changes to a list of CronJob. deprecated: use the 'watch' parameter with a list operation instead.

- `/apis/batch/v1/namespaces/{namespace}/cronjobs/{name}`

  - `DELETE`: delete a CronJob

  - `GET`: read the specified CronJob

  - `PATCH`: partially update the specified CronJob

  - `PUT`: replace the specified CronJob

- `/apis/batch/v1/watch/namespaces/{namespace}/cronjobs/{name}`

  - `GET`: watch changes to an object of kind CronJob. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

- `/apis/batch/v1/namespaces/{namespace}/cronjobs/{name}/status`

  - `GET`: read status of the specified CronJob

  - `PATCH`: partially update status of the specified CronJob

  - `PUT`: replace status of the specified CronJob

## /apis/batch/v1/cronjobs

HTTP method
`GET`

Description
list or watch objects of kind CronJob

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CronJobList`](../objects/index.md#io-k8s-api-batch-v1-CronJobList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/batch/v1/watch/cronjobs

HTTP method
`GET`

Description
watch individual changes to a list of CronJob. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/batch/v1/namespaces/{namespace}/cronjobs

HTTP method
`DELETE`

Description
delete collection of CronJob

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
list or watch objects of kind CronJob

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CronJobList`](../objects/index.md#io-k8s-api-batch-v1-CronJobList) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`POST`

Description
create a CronJob

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 201 - Created | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 202 - Accepted | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/batch/v1/watch/namespaces/{namespace}/cronjobs

HTTP method
`GET`

Description
watch individual changes to a list of CronJob. deprecated: use the 'watch' parameter with a list operation instead.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/batch/v1/namespaces/{namespace}/cronjobs/{name}

| Parameter | Type     | Description         |
|-----------|----------|---------------------|
| `name`    | `string` | name of the CronJob |

Global path parameters

HTTP method
`DELETE`

Description
delete a CronJob

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 202 - Accepted | [`Status`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`GET`

Description
read the specified CronJob

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update the specified CronJob

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 201 - Created | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace the specified CronJob

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 201 - Created | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/batch/v1/watch/namespaces/{namespace}/cronjobs/{name}

| Parameter | Type     | Description         |
|-----------|----------|---------------------|
| `name`    | `string` | name of the CronJob |

Global path parameters

HTTP method
`GET`

Description
watch changes to an object of kind CronJob. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`WatchEvent`](../objects/index.md#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema |
| 401 - Unauthorized | Empty |

HTTP responses

## /apis/batch/v1/namespaces/{namespace}/cronjobs/{name}/status

| Parameter | Type     | Description         |
|-----------|----------|---------------------|
| `name`    | `string` | name of the CronJob |

Global path parameters

HTTP method
`GET`

Description
read status of the specified CronJob

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PATCH`

Description
partially update status of the specified CronJob

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 201 - Created | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses

HTTP method
`PUT`

Description
replace status of the specified CronJob

| Parameter | Type | Description |
|----|----|----|
| `dryRun` | `string` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `fieldValidation` | `string` | fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered. |

Query parameters

| Parameter | Type | Description |
|----|----|----|
| `body` | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |  |

Body parameters

| HTTP code | Reponse body |
|----|----|
| 200 - OK | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 201 - Created | [`CronJob`](cronjob-batch-v1.md#cronjob-batch-v1) schema |
| 401 - Unauthorized | Empty |

HTTP responses
