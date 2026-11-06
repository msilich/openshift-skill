<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure gang scheduling in Red Hat build of Kueue for *all-or-nothing* admission of workloads that require a group of pods to run together.

Gang scheduling can improve resource use, help resolve deadlocks, and reduce costs.

A deadlock can occur when workloads compete for limited resources and not all required pods reach a ready state. For example, running workers in a distributed training job can hold GPUs while waiting for the remaining workers to start.

You can specify how Red Hat build of Kueue admits workloads and responds when pods do not reach a ready state.

To reduce competition for resources while pods start, configure sequential admission. To admit workloads without waiting for pods in admitted workloads to reach a ready state, configure parallel admission.

To limit how long workloads hold quota when pods do not reach a ready state during startup or recovery, set cluster-wide readiness timeouts. Use requeue settings to specify whether and how Red Hat build of Kueue returns the workload to the queue.

# Workload readiness timeouts and retries

Readiness timeouts control how long Red Hat build of Kueue waits for pods to reach a ready state during startup or recovery. You can adjust these timeouts to accommodate tasks such as image pulls and worker initialization.

The `admission` field determines whether Red Hat build of Kueue admits workloads in parallel or sequentially. Readiness timeouts apply after admission.

One set of readiness timeouts applies across the whole cluster. You cannot set different timeouts for individual namespaces or workloads.

Choose timeouts that cover the expected startup and recovery times. A short timeout can trigger eviction before pods reach a ready state. A long timeout can delay other workloads that need the reserved quota.

The following terms describe how readiness timeouts and retries work:

Start timeout
Limits the time from admission until a workload reaches the `PodsReady=True` condition. Pods are ready when they are in the `Running` phase and pass any configured readiness checks.

Recovery timeout
Limits the time for a workload to return to the `PodsReady=True` condition after one or more pods lose readiness.

Workload retry
Allows another admission attempt after a readiness timeout. If retries remain or you omit the limit, Red Hat build of Kueue evicts and requeues the workload. If no retries remain, Red Hat build of Kueue deactivates the workload.

# Gang scheduling configuration

The `spec.config.gangScheduling.policy` field in the `Kueue` custom resource (CR) controls the gang scheduling policy for workloads.

The following example uses parallel admission and a 10-minute start timeout:

<div class="formalpara">

<div class="title">

Example `Kueue` CR with gang scheduling configured

</div>

``` yaml
apiVersion: kueue.openshift.io/v1
kind: Kueue
metadata:
  name: cluster
  labels:
    app.kubernetes.io/managed-by: kustomize
    app.kubernetes.io/name: kueue-operator
spec:
  config:
    integrations:
      frameworks:
      - BatchJob
    gangScheduling:
      policy: ByWorkload
      byWorkload:
        admission: Parallel
        timeoutSeconds: 600
```

</div>

The `policy` field accepts the following values:

| Value | Behavior |
|----|----|
| `ByWorkload` | Processes each workload as a single unit for admission. The readiness timeout applies to the entire workload. If retries remain or you omit the limit, Red Hat build of Kueue evicts and requeues the workload for another admission attempt. If no retries remain, Red Hat build of Kueue deactivates the workload. Include the `byWorkload` field. |
| `ByWorkloadDefaults` | Processes each workload as a single unit for admission and uses the default admission, timeout, and requeue settings. The `ByWorkloadDefaults` policy does not allow the `byWorkload` field. |
| `None` | Uses parallel admission and a fixed one-year readiness timeout. For workloads that reach a ready state within one year, this policy provides the same behavior as disabling gang scheduling. Workloads that do not reach a ready state remain subject to the timeout. The `None` policy does not allow the `byWorkload` field. |
| Empty string (`""`) | Uses `ByWorkloadDefaults`, the default policy. An empty `policy` value does not allow the `byWorkload` field. |

`spec.config.gangScheduling.policy` values

# Manage workload resources with gang scheduling

To manage workload admission and readiness in Red Hat build of Kueue, configure gang scheduling. Set admission modes, cluster-wide readiness timeouts, and retry limits.

The following example uses the `ByWorkload` policy with parallel admission. It sets a 10-minute start timeout, a 30-minute recovery timeout, and a retry limit of five.

<div>

<div class="title">

Prerequisites

</div>

- You have cluster administrator permissions.

- You installed the Red Hat build of Kueue Operator on your cluster.

- You created a `Kueue` custom resource (CR) named `cluster`.

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Update the `Kueue` CR configuration by setting the `spec.config.gangScheduling` field to the following values. Keep the other CR settings.

    ``` yaml
    apiVersion: kueue.openshift.io/v1
    kind: Kueue
    metadata:
      name: cluster
    spec:
      config:
        integrations:
          frameworks:
          - BatchJob
        gangScheduling:
          policy: ByWorkload
          byWorkload:
            admission: Parallel
            timeoutSeconds: 600
            recoveryTimeoutSeconds: 1800
            requeuingStrategy:
              timeReference: Eviction
              retryLimit: 5
              backoffBaseSeconds: 120
              backoffMaxSeconds: 7200
    # ...
    ```

    For more information about the policy field, see "Gang scheduling configuration". For more information about admission, timeout, and requeue fields, see "Gang scheduling admission, timeout, and requeue fields".

2.  Apply the updated `Kueue` CR to the cluster by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

</div>

# Gang scheduling admission, timeout, and requeue fields

The `spec.config.gangScheduling.byWorkload` fields in Red Hat build of Kueue configure admission, readiness timeouts, and requeue behavior.

Set the `admission` field when you use the `ByWorkload` policy. The `admission` field accepts the following values:

| Value | Behavior |
|----|----|
| `Parallel` | Admits workloads without waiting for pods in admitted workloads to reach a ready state. Quota and other admission requirements still apply. Workloads can compete for cluster capacity and cause a deadlock. |
| `Sequential` | Waits for pods in admitted workloads to reach a ready state before admitting more workloads across any cluster queue. Sequential admission reduces competition for resources while pods start. It can delay workloads even when the cluster has capacity to run them. |
| Empty string (`""`) | Uses `Parallel`, the default value. |

`spec.config.gangScheduling.byWorkload.admission` values

The `byWorkload` field supports the following timeout fields:

| Field | Description | Valid values | If omitted |
|----|----|----|----|
| `timeoutSeconds` | Sets the start timeout for an admitted workload to reach the `PodsReady=True` condition. Allow enough time for image pulls, initialization, and resource provisioning. | `30`–`86400` seconds | Uses `1800` seconds (30 minutes). |
| `recoveryTimeoutSeconds` | Sets the recovery timeout for a workload to return to the `PodsReady=True` condition after one or more pods lose readiness. A value of `0` disables recovery timeout checks. The start timeout still applies. | `0`–`86400` seconds | Uses the value of `timeoutSeconds`. |

`spec.config.gangScheduling.byWorkload` fields

The `requeuingStrategy` field supports the following fields. If you include `requeuingStrategy`, specify at least one field. An empty `requeuingStrategy: {}` value is invalid.

| Field | Description | Valid values | If omitted |
|----|----|----|----|
| `timeReference` | Selects which timestamp Red Hat build of Kueue uses to order a workload in the queue after a readiness timeout. | `Eviction` uses the eviction time. `Creation` uses the workload creation time. | Uses `Eviction`. |
| `retryLimit` | Limits repeated admission attempts after readiness timeouts. After a workload uses all retries, the next timeout deactivates the workload. The `spec.active` field of the `Workload` object changes to `false`. | `1`–`200` | Sets no retry limit. |
| `backoffBaseSeconds` | Sets the base delay before a workload can be admitted again. The delay increases exponentially with the retry count. | `30`–`3600` seconds | Uses `60` seconds. |
| `backoffMaxSeconds` | Sets the maximum delay before a workload can be admitted again. If you set both delay fields, `backoffBaseSeconds` must not exceed `backoffMaxSeconds`. | `30`–`7200` seconds | Uses `3600` seconds. |

`spec.config.gangScheduling.byWorkload.requeuingStrategy` fields

After the configured delay, the workload must still meet quota and other admission requirements before Red Hat build of Kueue can admit it again.

# Additional resources

- [Creating a Kueue custom resource](install-kueue.md#create-kueue-cr_install-kueue)
