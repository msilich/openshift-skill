<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Managing DeploymentConfig objects

> [!IMPORTANT]
> As of OpenShift Container Platform 4.14, `DeploymentConfig` objects are deprecated. `DeploymentConfig` objects are still supported, but are not recommended for new installations. Only security-related and critical issues will be fixed.
>
> Instead, use `Deployment` objects or another alternative to provide declarative updates for pods.

`DeploymentConfig` objects can be managed from the OpenShift Container Platform web console’s **Workloads** page or using the `oc` CLI. The following procedures show CLI usage unless otherwise stated.

## Starting a deployment

You can start a rollout to begin the deployment process of your application.

<div>

<div class="title">

Procedure

</div>

1.  To start a new deployment process from an existing `DeploymentConfig` object, run the following command:

    ``` terminal
    $ oc rollout latest dc/<name>
    ```

    > [!NOTE]
    > If a deployment process is already in progress, the command displays a message and a new replication controller will not be deployed.

</div>

## Viewing a deployment

You can view a deployment to get basic information about all the available revisions of your application.

<div>

<div class="title">

Procedure

</div>

1.  To show details about all recently created replication controllers for the provided `DeploymentConfig` object, including any currently running deployment process, run the following command:

    ``` terminal
    $ oc rollout history dc/<name>
    ```

2.  To view details specific to a revision, add the `--revision` flag:

    ``` terminal
    $ oc rollout history dc/<name> --revision=1
    ```

3.  For more detailed information about a `DeploymentConfig` object and its latest revision, use the `oc describe` command:

    ``` terminal
    $ oc describe dc <name>
    ```

</div>

## Retrying a deployment

If the current revision of your `DeploymentConfig` object failed to deploy, you can restart the deployment process.

<div>

<div class="title">

Procedure

</div>

1.  To restart a failed deployment process:

    ``` terminal
    $ oc rollout retry dc/<name>
    ```

    If the latest revision of it was deployed successfully, the command displays a message and the deployment process is not retried.

    > [!NOTE]
    > Retrying a deployment restarts the deployment process and does not create a new deployment revision. The restarted replication controller has the same configuration it had when it failed.

</div>

## Rolling back a deployment

Rollbacks revert an application back to a previous revision and can be performed using the REST API, the CLI, or the web console.

<div>

<div class="title">

Procedure

</div>

1.  To rollback to the last successful deployed revision of your configuration:

    ``` terminal
    $ oc rollout undo dc/<name>
    ```

    The `DeploymentConfig` object’s template is reverted to match the deployment revision specified in the undo command, and a new replication controller is started. If no revision is specified with `--to-revision`, then the last successfully deployed revision is used.

2.  Image change triggers on the `DeploymentConfig` object are disabled as part of the rollback to prevent accidentally starting a new deployment process soon after the rollback is complete.

    To re-enable the image change triggers:

    ``` terminal
    $ oc set triggers dc/<name> --auto
    ```

</div>

> [!NOTE]
> Deployment configs also support automatically rolling back to the last successful revision of the configuration in case the latest deployment process fails. In that case, the latest template that failed to deploy stays intact by the system and it is up to users to fix their configurations.

## Executing commands inside a container

You can add a command to a container, which modifies the container’s startup behavior by overruling the image’s `ENTRYPOINT`. This is different from a lifecycle hook, which instead can be run once per deployment at a specified time.

<div>

<div class="title">

Procedure

</div>

1.  Add the `command` parameters to the `spec` field of the `DeploymentConfig` object. You can also add an `args` field, which modifies the `command` (or the `ENTRYPOINT` if `command` does not exist).

    ``` yaml
    kind: DeploymentConfig
    apiVersion: apps.openshift.io/v1
    metadata:
      name: example-dc
    # ...
    spec:
      template:
    # ...
        spec:
         containers:
         - name: <container_name>
           image: 'image'
           command:
             - '<command>'
           args:
             - '<argument_1>'
             - '<argument_2>'
             - '<argument_3>'
    ```

    For example, to execute the `java` command with the `-jar` and `/opt/app-root/springboots2idemo.jar` arguments:

    ``` yaml
    kind: DeploymentConfig
    apiVersion: apps.openshift.io/v1
    metadata:
      name: example-dc
    # ...
    spec:
      template:
    # ...
        spec:
          containers:
            - name: example-spring-boot
              image: 'image'
              command:
                - java
              args:
                - '-jar'
                - /opt/app-root/springboots2idemo.jar
    # ...
    ```

</div>

## Viewing deployment logs

<div>

<div class="title">

Procedure

</div>

1.  To stream the logs of the latest revision for a given `DeploymentConfig` object:

    ``` terminal
    $ oc logs -f dc/<name>
    ```

    If the latest revision is running or failed, the command returns the logs of the process that is responsible for deploying your pods. If it is successful, it returns the logs from a pod of your application.

2.  You can also view logs from older failed deployment processes, if and only if these processes (old replication controllers and their deployer pods) exist and have not been pruned or deleted manually:

    ``` terminal
    $ oc logs --version=1 dc/<name>
    ```

</div>

## Deployment triggers

A `DeploymentConfig` object can contain triggers, which drive the creation of new deployment processes in response to events inside the cluster.

> [!WARNING]
> If no triggers are defined on a `DeploymentConfig` object, a config change trigger is added by default. If triggers are defined as an empty field, deployments must be started manually.

### Config change deployment triggers

The config change trigger results in a new replication controller whenever configuration changes are detected in the pod template of the `DeploymentConfig` object.

> [!NOTE]
> If a config change trigger is defined on a `DeploymentConfig` object, the first replication controller is automatically created soon after the `DeploymentConfig` object itself is created and it is not paused.

<div class="formalpara">

<div class="title">

Config change deployment trigger

</div>

``` yaml
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: example-dc
# ...
spec:
# ...
  triggers:
    - type: "ConfigChange"
```

</div>

### Image change deployment triggers

The image change trigger results in a new replication controller whenever the content of an image stream tag changes (when a new version of the image is pushed).

<div class="formalpara">

<div class="title">

Image change deployment trigger

</div>

``` yaml
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: example-dc
# ...
spec:
# ...
  triggers:
    - type: "ImageChange"
      imageChangeParams:
        automatic: true
        from:
          kind: "ImageStreamTag"
          name: "origin-ruby-sample:latest"
          namespace: "myproject"
        containerNames:
          - "helloworld"
```

</div>

- If the `imageChangeParams.automatic` field is set to `false`, the trigger is disabled.

With the above example, when the `latest` tag value of the `origin-ruby-sample` image stream changes and the new image value differs from the current image specified in the `DeploymentConfig` object’s `helloworld` container, a new replication controller is created using the new image for the `helloworld` container.

> [!NOTE]
> If an image change trigger is defined on a `DeploymentConfig` object (with a config change trigger and `automatic=false`, or with `automatic=true`) and the image stream tag pointed by the image change trigger does not exist yet, the initial deployment process will automatically start as soon as an image is imported or pushed by a build to the image stream tag.

### Setting deployment triggers

<div>

<div class="title">

Procedure

</div>

1.  You can set deployment triggers for a `DeploymentConfig` object using the `oc set triggers` command. For example, to set a image change trigger, use the following command:

    ``` terminal
    $ oc set triggers dc/<dc_name> \
        --from-image=<project>/<image>:<tag> -c <container_name>
    ```

</div>

## Setting deployment resources

A deployment is completed by a pod that consumes resources (memory, CPU, and ephemeral storage) on a node. By default, pods consume unbounded node resources. However, if a project specifies default container limits, then pods consume resources up to those limits.

> [!NOTE]
> The minimum memory limit for a deployment is 12 MB. If a container fails to start due to a `Cannot allocate memory` pod event, the memory limit is too low. Either increase or remove the memory limit. Removing the limit allows pods to consume unbounded node resources.

You can also limit resource use by specifying resource limits as part of the deployment strategy. Deployment resources can be used with the recreate, rolling, or custom deployment strategies.

<div>

<div class="title">

Procedure

</div>

1.  In the following example, each of `resources`, `cpu`, `memory`, and `ephemeral-storage` is optional:

    ``` yaml
    kind: Deployment
    apiVersion: apps/v1
    metadata:
      name: hello-openshift
    # ...
    spec:
    # ...
      type: "Recreate"
      resources:
        limits:
          cpu: "100m"
          memory: "256Mi"
          ephemeral-storage: "1Gi"
    ```

    - `cpu` is in CPU units: `100m` represents 0.1 CPU units (100 \* 1e-3).

    - `memory` is in bytes: `256Mi` represents 268435456 bytes (256 \* 2 ^ 20).

    - `ephemeral-storage` is in bytes: `1Gi` represents 1073741824 bytes (2 ^ 30).

      However, if a quota has been defined for your project, one of the following two items is required:

      - A `resources` section set with an explicit `requests`:

        ``` yaml
        kind: Deployment
        apiVersion: apps/v1
        metadata:
          name: hello-openshift
        # ...
        spec:
        # ...
          type: "Recreate"
          resources:
            requests:
              cpu: "100m"
              memory: "256Mi"
              ephemeral-storage: "1Gi"
        ```

        - The `requests` object contains the list of resources that correspond to the list of resources in the quota.

      - A limit range defined in your project, where the defaults from the `LimitRange` object apply to pods created during the deployment process.

      To set deployment resources, choose one of the above options. Otherwise, deploy pod creation fails, citing a failure to satisfy quota.

</div>

<div>

<div class="title">

Additional resources

</div>

- For more information about resource limits and requests, see [Understanding managing application memory](../../nodes/clusters/nodes-cluster-resource-configure.md#nodes-cluster-resource-configure-about_nodes-cluster-resource-configure).

</div>

## Scaling manually

In addition to rollbacks, you can exercise fine-grained control over the number of replicas by manually scaling them.

> [!NOTE]
> Pods can also be auto-scaled using the `oc autoscale` command.

<div>

<div class="title">

Procedure

</div>

1.  To manually scale a `DeploymentConfig` object, use the `oc scale` command. For example, the following command sets the replicas in the `frontend` `DeploymentConfig` object to `3`.

    ``` terminal
    $ oc scale dc frontend --replicas=3
    ```

    The number of replicas eventually propagates to the desired and current state of the deployment configured by the `DeploymentConfig` object `frontend`.

</div>

## Accessing private repositories from DeploymentConfig objects

You can add a secret to your `DeploymentConfig` object so that it can access images from a private repository. This procedure shows the OpenShift Container Platform web console method.

<div>

<div class="title">

Procedure

</div>

1.  Create a new project.

2.  Navigate to **Workloads** → **Secrets**.

3.  Create a secret that contains credentials for accessing a private image repository.

4.  Navigate to **Workloads** → **DeploymentConfigs**.

5.  Create a `DeploymentConfig` object.

6.  On the `DeploymentConfig` object editor page, set the **Pull Secret** and save your changes.

</div>

## Assigning pods to specific nodes

You can use node selectors in conjunction with labeled nodes to control pod placement.

Cluster administrators can set the default node selector for a project in order to restrict pod placement to specific nodes. As a developer, you can set a node selector on a `Pod` configuration to restrict nodes even further.

<div>

<div class="title">

Procedure

</div>

1.  To add a node selector when creating a pod, edit the `Pod` configuration, and add the `nodeSelector` value. This can be added to a single `Pod` configuration, or in a `Pod` template:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-pod
    # ...
    spec:
      nodeSelector:
        disktype: ssd
    # ...
    ```

    Pods created when the node selector is in place are assigned to nodes with the specified labels. The labels specified here are used in conjunction with the labels added by a cluster administrator.

    For example, if a project has the `type=user-node` and `region=east` labels added to a project by the cluster administrator, and you add the above `disktype: ssd` label to a pod, the pod is only ever scheduled on nodes that have all three labels.

    > [!NOTE]
    > Labels can only be set to one value, so setting a node selector of `region=west` in a `Pod` configuration that has `region=east` as the administrator-set default, results in a pod that will never be scheduled.

</div>

## Running a pod with a different service account

You can run a pod with a service account other than the default.

<div>

<div class="title">

Procedure

</div>

1.  Edit the `DeploymentConfig` object:

    ``` terminal
    $ oc edit dc/<deployment_config>
    ```

2.  Add the `serviceAccount` and `serviceAccountName` parameters to the `spec` field, and specify the service account you want to use:

    ``` yaml
    apiVersion: apps.openshift.io/v1
    kind: DeploymentConfig
    metadata:
      name: example-dc
    # ...
    spec:
    # ...
      securityContext: {}
      serviceAccount: <service_account>
      serviceAccountName: <service_account>
    ```

</div>
