<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can set build resources and maximum duration, assign builds to nodes, chain builds, prune builds, and configure build run policies.

# Setting build resources

By default, builds are completed by pods using unbound resources, such as memory and CPU. These resources can be limited.

<div class="formalpara">

<div class="title">

Procedure

</div>

You can limit resource use in two ways:

</div>

- Limit resource use by specifying resource limits in the default container limits of a project.

- Limit resource use by specifying resource limits as part of the build configuration.

  - In the following example, each of the `resources`, `cpu`, and `memory` parameters are optional:

    ``` yaml
    apiVersion: "v1"
    kind: "BuildConfig"
    metadata:
      name: "sample-build"
    spec:
      resources:
        limits:
          cpu: "100m"
          memory: "256Mi"
    ```

    - `cpu` is in CPU units: `100m` represents 0.1 CPU units (100 \* 1e-3).

    - `memory` is in bytes: `256Mi` represents 268435456 bytes (256 \* 2 ^ 20).

      However, if a quota has been defined for your project, one of the following two items is required:

      - A `resources` section set with an explicit `requests`:

        ``` yaml
        resources:
          requests:
            cpu: "100m"
            memory: "256Mi"
        ```

    - The `requests` object contains the list of resources that correspond to the list of resources in the quota.

      - A limit range defined in your project, where the defaults from the `LimitRange` object apply to pods created during the build process.

        Otherwise, build pod creation will fail, citing a failure to satisfy quota.

# Setting maximum duration

When defining a `BuildConfig` object, you can define its maximum duration by setting the `completionDeadlineSeconds` field. It is specified in seconds and is not set by default. When not set, there is no maximum duration enforced.

The maximum duration is counted from the time when a build pod gets scheduled in the system, and defines how long it can be active, including the time needed to pull the builder image. After reaching the specified timeout, the build is terminated by OpenShift Container Platform.

<div>

<div class="title">

Procedure

</div>

- To set maximum duration, specify `completionDeadlineSeconds` in your `BuildConfig`. The following example shows the part of a `BuildConfig` specifying `completionDeadlineSeconds` field for 30 minutes:

  ``` yaml
  spec:
    completionDeadlineSeconds: 1800
  ```

</div>

> [!NOTE]
> This setting is not supported with the Pipeline Strategy option.

# Assigning builds to specific nodes

Builds can be targeted to run on specific nodes by specifying labels in the `nodeSelector` field of a build configuration. The `nodeSelector` value is a set of key-value pairs that are matched to `Node` labels when scheduling the build pod.

The `nodeSelector` value can also be controlled by cluster-wide default and override values. Defaults will only be applied if the build configuration does not define any key-value pairs for the `nodeSelector` and also does not define an explicitly empty map value of `nodeSelector:{}`. Override values will replace values in the build configuration on a key by key basis.

> [!NOTE]
> If the specified `NodeSelector` cannot be matched to a node with those labels, the build still stay in the `Pending` state indefinitely.

<div>

<div class="title">

Procedure

</div>

- Assign builds to run on specific nodes by assigning labels in the `nodeSelector` field of the `BuildConfig`, for example:

  ``` yaml
  apiVersion: "v1"
  kind: "BuildConfig"
  metadata:
    name: "sample-build"
  spec:
    nodeSelector:
      key1: value1
      key2: value2
  ```

  - Builds associated with this build configuration will run only on nodes with the `key1=value2` and `key2=value2` labels.

</div>

# Chained builds

For compiled languages such as Go, C, C++, and Java, including the dependencies necessary for compilation in the application image might increase the size of the image or introduce vulnerabilities that can be exploited.

To avoid these problems, two builds can be chained together. One build that produces the compiled artifact, and a second build that places that artifact in a separate image that runs the artifact.

In the following example, a source-to-image (S2I) build is combined with a docker build to compile an artifact that is then placed in a separate runtime image.

> [!NOTE]
> Although this example chains a S2I build and a docker build, the first build can use any strategy that produces an image containing the desired artifacts, and the second build can use any strategy that can consume input content from an image.

The first build takes the application source and produces an image containing a `WAR` file. The image is pushed to the `artifact-image` image stream. The path of the output artifact depends on the `assemble` script of the S2I builder used. In this case, it is output to `/wildfly/standalone/deployments/ROOT.war`.

``` yaml
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: artifact-build
spec:
  output:
    to:
      kind: ImageStreamTag
      name: artifact-image:latest
  source:
    git:
      uri: https://github.com/openshift/openshift-jee-sample.git
      ref: "master"
  strategy:
    sourceStrategy:
      from:
        kind: ImageStreamTag
        name: wildfly:10.1
        namespace: openshift
```

The second build uses image source with a path to the WAR file inside the output image from the first build. An inline `dockerfile` copies that `WAR` file into a runtime image.

``` yaml
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: image-build
spec:
  output:
    to:
      kind: ImageStreamTag
      name: image-build:latest
  source:
    dockerfile: |-
      FROM jee-runtime:latest
      COPY ROOT.war /deployments/ROOT.war
    images:
    - from:
        kind: ImageStreamTag
        name: artifact-image:latest
      paths:
      - sourcePath: /wildfly/standalone/deployments/ROOT.war
        destinationDir: "."
  strategy:
    dockerStrategy:
      from:
        kind: ImageStreamTag
        name: jee-runtime:latest
  triggers:
  - imageChange: {}
    type: ImageChange
```

- `from` specifies that the docker build should include the output of the image from the `artifact-image` image stream, which was the target of the previous build.

- `paths` specifies which paths from the target image to include in the current docker build.

- The runtime image is used as the source image for the docker build.

The result of this setup is that the output image of the second build does not have to contain any of the build tools that are needed to create the `WAR` file. Also, because the second build contains an image change trigger, whenever the first build is run and produces a new image with the binary artifact, the second build is automatically triggered to produce a runtime image that contains that artifact. Therefore, both builds behave as a single build with two stages.

# Pruning builds

By default, builds that have completed their lifecycle are persisted indefinitely. You can limit the number of previous builds that are retained.

<div>

<div class="title">

Procedure

</div>

1.  Limit the number of previous builds that are retained by supplying a positive integer value for `successfulBuildsHistoryLimit` or `failedBuildsHistoryLimit` in your `BuildConfig`, for example:

    ``` yaml
    apiVersion: "v1"
    kind: "BuildConfig"
    metadata:
      name: "sample-build"
    spec:
      successfulBuildsHistoryLimit: 2
      failedBuildsHistoryLimit: 2
    ```

    - `successfulBuildsHistoryLimit` will retain up to two builds with a status of `completed`.

    - `failedBuildsHistoryLimit` will retain up to two builds with a status of `failed`, `canceled`, or `error`.

2.  Trigger build pruning by one of the following actions:

    - Updating a build configuration.

    - Waiting for a build to complete its lifecycle.

</div>

Builds are sorted by their creation timestamp with the oldest builds being pruned first.

> [!NOTE]
> Administrators can manually prune builds using the 'oc adm' object pruning command.

# Build run policy

The build run policy describes the order in which the builds created from the build configuration should run. This can be done by changing the value of the `runPolicy` field in the `spec` section of the `Build` specification.

It is also possible to change the `runPolicy` value for existing build configurations, by:

- Changing `Parallel` to `Serial` or `SerialLatestOnly` and triggering a new build from this configuration causes the new build to wait until all parallel builds complete as the serial build can only run alone.

- Changing `Serial` to `SerialLatestOnly` and triggering a new build causes cancellation of all existing builds in queue, except the currently running build and the most recently created build. The newest build runs next.
