<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When you create jobs in your cluster, Red Hat build of Kueue represents each job as a `Workload` object to track resource requirements, decisions, and statuses.

Red Hat build of Kueue does not directly manipulate your jobs. Instead, Red Hat build of Kueue manages `Workload` objects that represent the resource requirements of a job, and syncs any decisions and statuses between the two objects.

# Labeling namespaces to allow Red Hat build of Kueue to manage jobs

You must add the `kueue.openshift.io/managed=true` label to each namespace where you want Red Hat build of Kueue to manage jobs, because the Operator only enforces policies on labeled namespaces.

<div>

<div class="title">

Prerequisites

</div>

- You have cluster administrator permissions.

- The Red Hat build of Kueue Operator is installed on your cluster, and you have created a `Kueue` custom resource (CR).

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Add the `kueue.openshift.io/managed=true` label to a namespace by running the following command:

  ``` terminal
  $ oc label namespace <namespace> kueue.openshift.io/managed=true
  ```

  When you add this label, you instruct the Red Hat build of Kueue Operator that the namespace is managed by its webhook admission controllers. As a result, any Red Hat build of Kueue resources within that namespace are properly validated and mutated.

</div>

# Configuring label policies for jobs

You can configure the `spec.config.workloadManagement.labelPolicy` field in the `Kueue` CR to control whether Red Hat build of Kueue manages or ignores specific jobs.

The allowed values are `QueueName`, `None`, and empty (`""`).

If the `labelPolicy` setting is omitted or empty (`""`), the default policy is that Red Hat build of Kueue manages jobs that have a `kueue.x-k8s.io/queue-name` label, and ignores jobs that do not have the `kueue.x-k8s.io/queue-name` label. This is the same workflow as if the `labelPolicy` is set to `QueueName`.

If the `labelPolicy` setting is set to `None`, jobs are managed by Red Hat build of Kueue even if they do not have the `kueue.x-k8s.io/queue-name` label.

<div class="formalpara">

<div class="title">

Example `workloadManagement` spec configuration

</div>

``` yaml
apiVersion: kueue.openshift.io/v1
kind: Kueue
metadata:
  labels:
    app.kubernetes.io/name: kueue-operator
    app.kubernetes.io/managed-by: kustomize
  name: cluster
  namespace: openshift-kueue-operator
spec:
  config:
    workloadManagement:
      labelPolicy: QueueName
# ...
```

</div>

<div class="formalpara">

<div class="title">

Example user-created `Job` object containing the `kueue.x-k8s.io/queue-name` label

</div>

``` yaml
apiVersion: batch/v1
kind: Job
metadata:
  generateName: sample-job-
  namespace: my-namespace
  labels:
    kueue.x-k8s.io/queue-name: user-queue
spec:
# ...
```

</div>
