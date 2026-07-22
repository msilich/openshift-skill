<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can run Kubernetes jobs with Red Hat build of Kueue enabled to manage resource allocation within defined quota limits. This can help to ensure predictable resource availability, cluster stability, and optimized performance.

# Identifying available local queues

Before you can submit a job to a queue, you must find the name of the local queue.

<div>

<div class="title">

Prerequisites

</div>

- A cluster administrator has installed and configured Red Hat build of Kueue on your OpenShift Container Platform cluster.

- A cluster administrator has assigned you the `kueue-batch-user-role` cluster role.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command to list available local queues in your namespace:

  ``` terminal
  $ oc -n <namespace> get localqueues
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME         CLUSTERQUEUE    PENDING WORKLOADS
  user-queue   cluster-queue   3
  ```

  </div>

</div>

# Defining a job to run with Red Hat build of Kueue

When you are defining a job to run with Red Hat build of Kueue, ensure that it meets the following criteria:

- Specify the local queue to submit the job to, by using the `kueue.x-k8s.io/queue-name` label.

- Include the resource requests for each job pod.

Red Hat build of Kueue suspends the job, and then starts it when resources are available. Red Hat build of Kueue creates a corresponding workload, represented as a `Workload` object with a name that matches the job.

<div>

<div class="title">

Prerequisites

</div>

- A cluster administrator has installed and configured Red Hat build of Kueue on your OpenShift Container Platform cluster.

- A cluster administrator has assigned you the `kueue-batch-user-role` cluster role.

- You have installed the OpenShift CLI (`oc`).

- You have identified the name of the local queue that you want to submit jobs to.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Job` object.

    <div class="formalpara">

    <div class="title">

    Example job

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
      parallelism: 3
      completions: 3
      template:
        spec:
          containers:
          - name: dummy-job
            image: registry.k8s.io/e2e-test-images/agnhost:2.53
            args: ["entrypoint-tester", "hello", "world"]
            resources:
              requests:
                cpu: 1
                memory: "200Mi"
          restartPolicy: Never
    ```

    </div>

    - Defines the resource type as a `Job` object, which represents a batch computation task.

    - Provides a prefix for generating a unique name for the job.

    - Identifies the queue to send the job to.

    - Defines the resource requests for each pod.

2.  Run the job by running the following command:

    ``` terminal
    $ oc create -f <filename>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that pods are running for the job you have created, by running the following command and observing the output:

  ``` terminal
  $ oc get job <job-name>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME               STATUS      COMPLETIONS   DURATION   AGE
  sample-job-sk42x   Suspended   0/1                      2m12s
  ```

  </div>

- Verify that a workload has been created in your namespace for the job, by running the following command and observing the output:

  ``` terminal
  $ oc -n <namespace> get workloads
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                         QUEUE          RESERVED IN   ADMITTED   FINISHED   AGE
  job-sample-job-sk42x-77c03   user-queue                                         3m8s
  ```

  </div>

</div>
