<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

A *resource quota*, defined by a `ResourceQuota` object, provides constraints that limit aggregate resource consumption per project. It can limit the quantity of objects that can be created in a project by type, as well as the total amount of compute resources and storage that might be consumed by resources in that project.

This guide describes how resource quotas work, how cluster administrators can set and manage resource quotas on a per project basis, and how developers and cluster administrators can view them.

# Resources managed by quotas

The following describes the set of compute resources and object types that can be managed by a quota.

> [!NOTE]
> A pod is in a terminal state if `status.phase in (Failed, Succeeded)` is true.

| Resource Name | Description |
|----|----|
| `cpu` | The sum of CPU requests across all pods in a non-terminal state cannot exceed this value. `cpu` and `requests.cpu` are the same value and can be used interchangeably. |
| `memory` | The sum of memory requests across all pods in a non-terminal state cannot exceed this value. `memory` and `requests.memory` are the same value and can be used interchangeably. |
| `requests.cpu` | The sum of CPU requests across all pods in a non-terminal state cannot exceed this value. `cpu` and `requests.cpu` are the same value and can be used interchangeably. |
| `requests.memory` | The sum of memory requests across all pods in a non-terminal state cannot exceed this value. `memory` and `requests.memory` are the same value and can be used interchangeably. |
| `limits.cpu` | The sum of CPU limits across all pods in a non-terminal state cannot exceed this value. |
| `limits.memory` | The sum of memory limits across all pods in a non-terminal state cannot exceed this value. |

Compute resources managed by quota

| Resource Name | Description |
|----|----|
| `requests.storage` | The sum of storage requests across all persistent volume claims in any state cannot exceed this value. |
| `persistentvolumeclaims` | The total number of persistent volume claims that can exist in the project. |
| `<storage-class-name>.storageclass.storage.k8s.io/requests.storage` | The sum of storage requests across all persistent volume claims in any state that have a matching storage class, cannot exceed this value. |
| `<storage-class-name>.storageclass.storage.k8s.io/persistentvolumeclaims` | The total number of persistent volume claims with a matching storage class that can exist in the project. |
| `ephemeral-storage` | The sum of local ephemeral storage requests across all pods in a non-terminal state cannot exceed this value. `ephemeral-storage` and `requests.ephemeral-storage` are the same value and can be used interchangeably. |
| `requests.ephemeral-storage` | The sum of ephemeral storage requests across all pods in a non-terminal state cannot exceed this value. `ephemeral-storage` and `requests.ephemeral-storage` are the same value and can be used interchangeably. |
| `limits.ephemeral-storage` | The sum of ephemeral storage limits across all pods in a non-terminal state cannot exceed this value. |

Storage resources managed by quota

| Resource Name | Description |
|----|----|
| `pods` | The total number of pods in a non-terminal state that can exist in the project. |
| `replicationcontrollers` | The total number of ReplicationControllers that can exist in the project. |
| `resourcequotas` | The total number of resource quotas that can exist in the project. |
| `services` | The total number of services that can exist in the project. |
| `services.loadbalancers` | The total number of services of type `LoadBalancer` that can exist in the project. |
| `services.nodeports` | The total number of services of type `NodePort` that can exist in the project. |
| `secrets` | The total number of secrets that can exist in the project. |
| `configmaps` | The total number of `ConfigMap` objects that can exist in the project. |
| `persistentvolumeclaims` | The total number of persistent volume claims that can exist in the project. |
| `openshift.io/imagestreams` | The total number of imagestreams that can exist in the project. |

Object counts managed by quota {#quotas-object-counts-managed_quotas-setting-per-project}

# Quota scopes

Each quota can have an associated set of *scopes*. A quota only measures usage for a resource if it matches the intersection of enumerated scopes.

Adding a scope to a quota restricts the set of resources to which that quota can apply. Specifying a resource outside of the allowed set results in a validation error.

|  |  |
|----|----|
| Scope | Description |
| `BestEffort` | Match pods that have best effort quality of service for either `cpu` or `memory`. |
| `NotBestEffort` | Match pods that do not have best effort quality of service for `cpu` and `memory`. |

A `BestEffort` scope restricts a quota to limiting the following resources:

- `pods`

A `NotBestEffort` scope restricts a quota to tracking the following resources:

- `pods`

- `memory`

- `requests.memory`

- `limits.memory`

- `cpu`

- `requests.cpu`

- `limits.cpu`

# Quota enforcement

After a resource quota for a project is first created, the project restricts the ability to create any new resources that may violate a quota constraint until it has calculated updated usage statistics.

After a quota is created and usage statistics are updated, the project accepts the creation of new content. When you create or modify resources, your quota usage is incremented immediately upon the request to create or modify the resource.

When you delete a resource, your quota use is decremented during the next full recalculation of quota statistics for the project. A configurable amount of time determines how long it takes to reduce quota usage statistics to their current observed system value.

If project modifications exceed a quota usage limit, the server denies the action, and an appropriate error message is returned to the user explaining the quota constraint violated, and what their currently observed usage statistics are in the system.

# Requests versus limits

When allocating compute resources, each container might specify a request and a limit value each for CPU, memory, and ephemeral storage. Quotas can restrict any of these values.

If the quota has a value specified for `requests.cpu` or `requests.memory`, then it requires that every incoming container make an explicit request for those resources. If the quota has a value specified for `limits.cpu` or `limits.memory`, then it requires that every incoming container specify an explicit limit for those resources.

# Sample resource quota definitions

<div class="formalpara">

<div class="title">

`core-object-counts.yaml`

</div>

``` yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: core-object-counts
spec:
  hard:
    configmaps: "10"
    persistentvolumeclaims: "4"
    replicationcontrollers: "20"
    secrets: "10"
    services: "10"
    services.loadbalancers: "2"
```

</div>

- The total number of `ConfigMap` objects that can exist in the project.

- The total number of persistent volume claims (PVCs) that can exist in the project.

- The total number of replication controllers that can exist in the project.

- The total number of secrets that can exist in the project.

- The total number of services that can exist in the project.

- The total number of services of type `LoadBalancer` that can exist in the project.

<div class="formalpara">

<div class="title">

`openshift-object-counts.yaml`

</div>

``` yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: openshift-object-counts
spec:
  hard:
    openshift.io/imagestreams: "10"
```

</div>

- The total number of image streams that can exist in the project.

<div class="formalpara">

<div class="title">

`compute-resources.yaml`

</div>

``` yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources
spec:
  hard:
    pods: "4"
    requests.cpu: "1"
    requests.memory: 1Gi
    limits.cpu: "2"
    limits.memory: 2Gi
```

</div>

- The total number of pods in a non-terminal state that can exist in the project.

- Across all pods in a non-terminal state, the sum of CPU requests cannot exceed 1 core.

- Across all pods in a non-terminal state, the sum of memory requests cannot exceed 1Gi.

- Across all pods in a non-terminal state, the sum of CPU limits cannot exceed 2 cores.

- Across all pods in a non-terminal state, the sum of memory limits cannot exceed 2Gi.

<div class="formalpara">

<div class="title">

`besteffort.yaml`

</div>

``` yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: besteffort
spec:
  hard:
    pods: "1"
  scopes:
  - BestEffort
```

</div>

- The total number of pods in a non-terminal state with `BestEffort` quality of service that can exist in the project.

- Restricts the quota to only matching pods that have `BestEffort` quality of service for either memory or CPU.

<div class="formalpara">

<div class="title">

`compute-resources-long-running.yaml`

</div>

``` yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources-long-running
spec:
  hard:
    pods: "4"
    limits.cpu: "4"
    limits.memory: "2Gi"
  scopes:
  - NotTerminating
```

</div>

- The total number of pods in a non-terminal state.

- Across all pods in a non-terminal state, the sum of CPU limits cannot exceed this value.

- Across all pods in a non-terminal state, the sum of memory limits cannot exceed this value.

- Restricts the quota to only matching pods where `spec.activeDeadlineSeconds` is set to `nil`. Build pods fall under `NotTerminating` unless the `RestartNever` policy is applied.

<div class="formalpara">

<div class="title">

`compute-resources-time-bound.yaml`

</div>

``` yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources-time-bound
spec:
  hard:
    pods: "2"
    limits.cpu: "1"
    limits.memory: "1Gi"
  scopes:
  - Terminating
```

</div>

- The total number of pods in a terminating state.

- Across all pods in a terminating state, the sum of CPU limits cannot exceed this value.

- Across all pods in a terminating state, the sum of memory limits cannot exceed this value.

- Restricts the quota to only matching pods where `spec.activeDeadlineSeconds >=0`. For example, this quota charges for build or deployer pods, but not long running pods like a web server or database.

<div class="formalpara">

<div class="title">

`storage-consumption.yaml`

</div>

``` yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: storage-consumption
spec:
  hard:
    persistentvolumeclaims: "10"
    requests.storage: "50Gi"
    gold.storageclass.storage.k8s.io/requests.storage: "10Gi"
    silver.storageclass.storage.k8s.io/requests.storage: "20Gi"
    silver.storageclass.storage.k8s.io/persistentvolumeclaims: "5"
    bronze.storageclass.storage.k8s.io/requests.storage: "0"
    bronze.storageclass.storage.k8s.io/persistentvolumeclaims: "0"
    requests.ephemeral-storage: 2Gi
    limits.ephemeral-storage: 4Gi
```

</div>

- The total number of persistent volume claims in a project

- Across all persistent volume claims in a project, the sum of storage requested cannot exceed this value.

- Across all persistent volume claims in a project, the sum of storage requested in the gold storage class cannot exceed this value.

- Across all persistent volume claims in a project, the sum of storage requested in the silver storage class cannot exceed this value.

- Across all persistent volume claims in a project, the total number of claims in the silver storage class cannot exceed this value.

- Across all persistent volume claims in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this is set to `0`, it means bronze storage class cannot request storage.

- Across all persistent volume claims in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this is set to `0`, it means bronze storage class cannot create claims.

- Across all pods in a non-terminal state, the sum of ephemeral storage requests cannot exceed 2Gi.

- Across all pods in a non-terminal state, the sum of ephemeral storage limits cannot exceed 4Gi.

# Creating a quota

You can create a quota to constrain resource usage in a given project.

<div>

<div class="title">

Procedure

</div>

1.  Define the quota in a file.

2.  Use the file to create the quota and apply it to a project:

    ``` terminal
    $ oc create -f <file> [-n <project_name>]
    ```

    For example:

    ``` terminal
    $ oc create -f core-object-counts.yaml -n demoproject
    ```

</div>

## Creating object count quotas

You can create an object count quota for all standard namespaced resource types on OpenShift Container Platform, such as `BuildConfig` and `DeploymentConfig` objects. An object quota count places a defined quota on all standard namespaced resource types.

When using a resource quota, an object is charged against the quota upon creation. These types of quotas are useful to protect against exhaustion of resources. The quota can only be created if there are enough spare resources within the project.

<div class="formalpara">

<div class="title">

Procedure

</div>

To configure an object count quota for a resource:

</div>

1.  Run the following command:

    ``` terminal
    $ oc create quota <name> \
        --hard=count/<resource>.<group>=<quota>,count/<resource>.<group>=<quota>
    ```

    - The `<resource>` variable is the name of the resource, and `<group>` is the API group, if applicable. Use the `oc api-resources` command for a list of resources and their associated API groups.

      For example:

      ``` terminal
      $ oc create quota test \
          --hard=count/deployments.apps=2,count/replicasets.apps=4,count/pods=3,count/secrets=4
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      resourcequota "test" created
      ```

      </div>

      This example limits the listed resources to the hard limit in each project in the cluster.

2.  Verify that the quota was created:

    ``` terminal
    $ oc describe quota test
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name:                         test
    Namespace:                    quota
    Resource                      Used  Hard
    --------                      ----  ----
    count/deployments.apps        0     2
    count/pods                    0     3
    count/replicasets.apps        0     4
    count/secrets                 0     4
    ```

    </div>

## Setting resource quota for extended resources

Overcommitment of resources is not allowed for extended resources, so you must specify `requests` and `limits` for the same extended resource in a quota. Currently, only quota items with the prefix `requests.` is allowed for extended resources. The following is an example scenario of how to set resource quota for the GPU resource `nvidia.com/gpu`.

<div>

<div class="title">

Procedure

</div>

1.  Determine how many GPUs are available on a node in your cluster. For example:

    ``` terminal
    # oc describe node ip-172-31-27-209.us-west-2.compute.internal | egrep 'Capacity|Allocatable|gpu'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
                        openshift.com/gpu-accelerator=true
    Capacity:
     nvidia.com/gpu:  2
    Allocatable:
     nvidia.com/gpu:  2
      nvidia.com/gpu  0           0
    ```

    </div>

    In this example, 2 GPUs are available.

2.  Create a `ResourceQuota` object to set a quota in the namespace `nvidia`. In this example, the quota is `1`:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    apiVersion: v1
    kind: ResourceQuota
    metadata:
      name: gpu-quota
      namespace: nvidia
    spec:
      hard:
        requests.nvidia.com/gpu: 1
    ```

    </div>

3.  Create the quota:

    ``` terminal
    # oc create -f gpu-quota.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    resourcequota/gpu-quota created
    ```

    </div>

4.  Verify that the namespace has the correct quota set:

    ``` terminal
    # oc describe quota gpu-quota -n nvidia
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name:                    gpu-quota
    Namespace:               nvidia
    Resource                 Used  Hard
    --------                 ----  ----
    requests.nvidia.com/gpu  0     1
    ```

    </div>

5.  Define a pod that asks for a single GPU. The following example definition file is called `gpu-pod.yaml`:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      generateName: gpu-pod-
      namespace: nvidia
    spec:
      restartPolicy: OnFailure
      containers:
      - name: rhel7-gpu-pod
        image: rhel7
        env:
          - name: NVIDIA_VISIBLE_DEVICES
            value: all
          - name: NVIDIA_DRIVER_CAPABILITIES
            value: "compute,utility"
          - name: NVIDIA_REQUIRE_CUDA
            value: "cuda>=5.0"
        command: ["sleep"]
        args: ["infinity"]
        resources:
          limits:
            nvidia.com/gpu: 1
    ```

6.  Create the pod:

    ``` terminal
    # oc create -f gpu-pod.yaml
    ```

7.  Verify that the pod is running:

    ``` terminal
    # oc get pods
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME              READY     STATUS      RESTARTS   AGE
    gpu-pod-s46h7     1/1       Running     0          1m
    ```

    </div>

8.  Verify that the quota `Used` counter is correct:

    ``` terminal
    # oc describe quota gpu-quota -n nvidia
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name:                    gpu-quota
    Namespace:               nvidia
    Resource                 Used  Hard
    --------                 ----  ----
    requests.nvidia.com/gpu  1     1
    ```

    </div>

9.  Attempt to create a second GPU pod in the `nvidia` namespace. This is technically available on the node because it has 2 GPUs:

    ``` terminal
    # oc create -f gpu-pod.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Error from server (Forbidden): error when creating "gpu-pod.yaml": pods "gpu-pod-f7z2w" is forbidden: exceeded quota: gpu-quota, requested: requests.nvidia.com/gpu=1, used: requests.nvidia.com/gpu=1, limited: requests.nvidia.com/gpu=1
    ```

    </div>

    This **Forbidden** error message is expected because you have a quota of 1 GPU and this pod tried to allocate a second GPU, which exceeds its quota.

</div>

# Viewing a quota

You can view usage statistics related to any hard limits defined in a quota for a project by navigating in the web console to the project’s **Quota** page.

You can also use the CLI to view quota details.

<div>

<div class="title">

Procedure

</div>

1.  Get the list of quotas defined in the project. For example, for a project called `demoproject`:

    ``` terminal
    $ oc get quota -n demoproject
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                           AGE    REQUEST                                                                                                      LIMIT
    besteffort                     4s     pods: 1/2
    compute-resources-time-bound   10m    pods: 0/2                                                                                                    limits.cpu: 0/1, limits.memory: 0/1Gi
    core-object-counts             109s   configmaps: 2/10, persistentvolumeclaims: 1/4, replicationcontrollers: 1/20, secrets: 9/10, services: 2/10
    ```

    </div>

2.  Describe the quota you are interested in, for example the `core-object-counts` quota:

    ``` terminal
    $ oc describe quota core-object-counts -n demoproject
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name:            core-object-counts
    Namespace:      demoproject
    Resource        Used    Hard
    --------        ----    ----
    configmaps      3   10
    persistentvolumeclaims  0   4
    replicationcontrollers  3   20
    secrets         9   10
    services        2   10
    ```

    </div>

</div>

# Configuring explicit resource quotas

Configure explicit resource quotas in a project request template to apply specific resource quotas in new projects.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the cluster-admin role.

- Install the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add a resource quota definition to a project request template:

    - If a project request template does not exist in a cluster:

      1.  Create a bootstrap project template and output it to a file called `template.yaml`:

          ``` terminal
          $ oc adm create-bootstrap-project-template -o yaml > template.yaml
          ```

      2.  Add a resource quota definition to `template.yaml`. The following example defines a resource quota named 'storage-consumption'. The definition must be added before the `parameters:` section in the template:

          ``` yaml
          - apiVersion: v1
            kind: ResourceQuota
            metadata:
              name: storage-consumption
              namespace: ${PROJECT_NAME}
            spec:
              hard:
                persistentvolumeclaims: "10"
                requests.storage: "50Gi"
                gold.storageclass.storage.k8s.io/requests.storage: "10Gi"
                silver.storageclass.storage.k8s.io/requests.storage: "20Gi"
                silver.storageclass.storage.k8s.io/persistentvolumeclaims: "5"
                bronze.storageclass.storage.k8s.io/requests.storage: "0"
                bronze.storageclass.storage.k8s.io/persistentvolumeclaims: "0"
          ```

          - The total number of persistent volume claims in a project.

          - Across all persistent volume claims in a project, the sum of storage requested cannot exceed this value.

          - Across all persistent volume claims in a project, the sum of storage requested in the gold storage class cannot exceed this value.

          - Across all persistent volume claims in a project, the sum of storage requested in the silver storage class cannot exceed this value.

          - Across all persistent volume claims in a project, the total number of claims in the silver storage class cannot exceed this value.

          - Across all persistent volume claims in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this value is set to `0`, the bronze storage class cannot request storage.

          - Across all persistent volume claims in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this value is set to `0`, the bronze storage class cannot create claims.

      3.  Create a project request template from the modified `template.yaml` file in the `openshift-config` namespace:

          ``` terminal
          $ oc create -f template.yaml -n openshift-config
          ```

          > [!NOTE]
          > To include the configuration as a `kubectl.kubernetes.io/last-applied-configuration` annotation, add the `--save-config` option to the `oc create` command.

          By default, the template is called `project-request`.

    - If a project request template already exists within a cluster:

      > [!NOTE]
      > If you declaratively or imperatively manage objects within your cluster by using configuration files, edit the existing project request template through those files instead.

      1.  List templates in the `openshift-config` namespace:

          ``` terminal
          $ oc get templates -n openshift-config
          ```

      2.  Edit an existing project request template:

          ``` terminal
          $ oc edit template <project_request_template> -n openshift-config
          ```

      3.  Add a resource quota definition, such as the preceding `storage-consumption` example, into the existing template. The definition must be added before the `parameters:` section in the template.

2.  If you created a project request template, reference it in the cluster’s project configuration resource:

    1.  Access the project configuration resource for editing:

        - By using the web console:

          1.  Navigate to the **Administration** → **Cluster Settings** page.

          2.  Click **Configuration** to view all configuration resources.

          3.  Find the entry for **Project** and click **Edit YAML**.

        - By using the CLI:

          1.  Edit the `project.config.openshift.io/cluster` resource:

              ``` terminal
              $ oc edit project.config.openshift.io/cluster
              ```

    2.  Update the `spec` section of the project configuration resource to include the `projectRequestTemplate` and `name` parameters. The following example references the default project request template name `project-request`:

        ``` yaml
        apiVersion: config.openshift.io/v1
        kind: Project
        metadata:
        #  ...
        spec:
          projectRequestTemplate:
            name: project-request
        ```

3.  Verify that the resource quota is applied when projects are created:

    1.  Create a project:

        ``` terminal
        $ oc new-project <project_name>
        ```

    2.  List the project’s resource quotas:

        ``` terminal
        $ oc get resourcequotas
        ```

    3.  Describe the resource quota in detail:

        ``` terminal
        $ oc describe resourcequotas <resource_quota_name>
        ```

</div>
