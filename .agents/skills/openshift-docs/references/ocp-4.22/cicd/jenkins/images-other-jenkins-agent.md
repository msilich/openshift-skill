<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Container Platform provides a base image for use as a Jenkins agent.

The Base image for Jenkins agents does the following:

- Pulls in both the required tools, headless Java, the Jenkins JNLP client, and the useful ones, including `git`, `tar`, `zip`, and `nss`, among others.

- Establishes the JNLP agent as the entry point.

- Includes the `oc` client tool for invoking command-line operations from within Jenkins jobs.

- Provides Dockerfiles for both Red Hat Enterprise Linux (RHEL) and `localdev` images.

> [!IMPORTANT]
> Use a version of the agent image that is appropriate for your OpenShift Container Platform release version. Embedding an `oc` client version that is not compatible with the OpenShift Container Platform version can cause unexpected behavior.

The OpenShift Container Platform Jenkins image also defines the following sample `java-builder` pod template to illustrate how you can use the agent image with the Jenkins Kubernetes plugin.

The `java-builder` pod template employs two containers:

- A `jnlp` container that uses the OpenShift Container Platform Base agent image and handles the JNLP contract for starting and stopping Jenkins agents.

- A `java` container that uses the `java` OpenShift Container Platform Sample ImageStream, which contains the various Java binaries, including the Maven binary `mvn`, for building code.

# Jenkins agent images

The OpenShift Container Platform Jenkins agent images are available on [Quay.io](https://quay.io) or [registry.redhat.io](https://registry.redhat.io).

Jenkins images are available through the Red Hat Registry:

``` terminal
$ docker pull registry.redhat.io/ocp-tools-4/jenkins-rhel8:<image_tag>
```

``` terminal
$ docker pull registry.redhat.io/ocp-tools-4/jenkins-agent-base-rhel8:<image_tag>
```

To use these images, you can either access them directly from [Quay.io](https://quay.io) or [registry.redhat.io](https://registry.redhat.io) or push them into your OpenShift Container Platform container image registry.

# Jenkins agent environment variables

Each Jenkins agent container can be configured with the following environment variables.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Variable</th>
<th style="text-align: left;">Definition</th>
<th style="text-align: left;">Example values and settings</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>JAVA_MAX_HEAP_PARAM</code>, <code>CONTAINER_HEAP_PERCENT</code>, <code>JENKINS_MAX_HEAP_UPPER_BOUND_MB</code></p></td>
<td style="text-align: left;"><p>These values control the maximum heap size of the Jenkins JVM. If <code>JAVA_MAX_HEAP_PARAM</code> is set, its value takes precedence. Otherwise, the maximum heap size is dynamically calculated as <code>CONTAINER_HEAP_PERCENT</code> of the container memory limit, optionally capped at <code>JENKINS_MAX_HEAP_UPPER_BOUND_MB</code> MiB.</p>
<p>By default, the maximum heap size of the Jenkins JVM is set to 50% of the container memory limit with no cap.</p></td>
<td style="text-align: left;"><p><code>JAVA_MAX_HEAP_PARAM</code> example setting: <code>-Xmx512m</code></p>
<p><code>CONTAINER_HEAP_PERCENT</code> default: <code>0.5</code>, or 50%</p>
<p><code>JENKINS_MAX_HEAP_UPPER_BOUND_MB</code> example setting: <code>512 MiB</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>JAVA_INITIAL_HEAP_PARAM</code>, <code>CONTAINER_INITIAL_PERCENT</code></p></td>
<td style="text-align: left;"><p>These values control the initial heap size of the Jenkins JVM. If <code>JAVA_INITIAL_HEAP_PARAM</code> is set, its value takes precedence. Otherwise, the initial heap size is dynamically calculated as <code>CONTAINER_INITIAL_PERCENT</code> of the dynamically calculated maximum heap size.</p>
<p>By default, the JVM sets the initial heap size.</p></td>
<td style="text-align: left;"><p><code>JAVA_INITIAL_HEAP_PARAM</code> example setting: <code>-Xms32m</code></p>
<p><code>CONTAINER_INITIAL_PERCENT</code> example setting: <code>0.1</code>, or 10%</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>CONTAINER_CORE_LIMIT</code></p></td>
<td style="text-align: left;"><p>If set, specifies an integer number of cores used for sizing numbers of internal JVM threads.</p></td>
<td style="text-align: left;"><p>Example setting: <code>2</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>JAVA_TOOL_OPTIONS</code></p></td>
<td style="text-align: left;"><p>Specifies options to apply to all JVMs running in this container. It is not recommended to override this value.</p></td>
<td style="text-align: left;"><p>Default: <code>-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -Dsun.zip.disableMemoryMapping=true</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>JAVA_GC_OPTS</code></p></td>
<td style="text-align: left;"><p>Specifies Jenkins JVM garbage collection parameters. It is not recommended to override this value.</p></td>
<td style="text-align: left;"><p>Default: <code>-XX:+UseParallelGC -XX:MinHeapFreeRatio=5 -XX:MaxHeapFreeRatio=10 -XX:GCTimeRatio=4 -XX:AdaptiveSizePolicyWeight=90</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>JENKINS_JAVA_OVERRIDES</code></p></td>
<td style="text-align: left;"><p>Specifies additional options for the Jenkins JVM. These options are appended to all other options, including the Java options above, and can be used to override any of them, if necessary. Separate each additional option with a space and if any option contains space characters, escape them with a backslash.</p></td>
<td style="text-align: left;"><p>Example settings: <code>-Dfoo -Dbar</code>; <code>-Dfoo=first\ value -Dbar=second\ value</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>USE_JAVA_VERSION</code></p></td>
<td style="text-align: left;"><p>Specifies the version of Java version to use to run the agent in its container. The container base image has two versions of java installed: <code>java-11</code> and <code>java-1.8.0</code>. If you extend the container base image, you can specify any alternative version of java using its associated suffix.</p></td>
<td style="text-align: left;"><p>The default value is <code>java-11</code>.</p>
<p>Example setting: <code>java-1.8.0</code></p></td>
</tr>
</tbody>
</table>

# Jenkins agent memory requirements

A JVM is used in all Jenkins agents to host the Jenkins JNLP agent as well as to run any Java applications such as `javac`, Maven, or Gradle.

By default, the Jenkins JNLP agent JVM uses 50% of the container memory limit for its heap. This value can be modified by the `CONTAINER_HEAP_PERCENT` environment variable. It can also be capped at an upper limit or overridden entirely.

By default, any other processes run in the Jenkins agent container, such as shell scripts or `oc` commands run from pipelines, cannot use more than the remaining 50% memory limit without provoking an OOM kill.

By default, each further JVM process that runs in a Jenkins agent container uses up to 25% of the container memory limit for its heap. It might be necessary to tune this limit for many build workloads.

# Jenkins agent Gradle builds

Hosting Gradle builds in the Jenkins agent on OpenShift Container Platform presents additional complications because in addition to the Jenkins JNLP agent and Gradle JVMs, Gradle spawns a third JVM to run tests if they are specified.

The following settings are suggested as a starting point for running Gradle builds in a memory constrained Jenkins agent on OpenShift Container Platform. You can modify these settings as required.

- Ensure the long-lived Gradle daemon is disabled by adding `org.gradle.daemon=false` to the `gradle.properties` file.

- Disable parallel build execution by ensuring `org.gradle.parallel=true` is not set in the `gradle.properties` file and that `--parallel` is not set as a command-line argument.

- To prevent Java compilations running out-of-process, set `java { options.fork = false }` in the `build.gradle` file.

- Disable multiple additional test processes by ensuring `test { maxParallelForks = 1 }` is set in the `build.gradle` file.

- Override the Gradle JVM memory parameters by the `GRADLE_OPTS`, `JAVA_OPTS` or `JAVA_TOOL_OPTIONS` environment variables.

- Set the maximum heap size and JVM arguments for any Gradle test JVM by defining the `maxHeapSize` and `jvmArgs` settings in `build.gradle`, or through the `-Dorg.gradle.jvmargs` command-line argument.

# Jenkins agent pod retention

Jenkins agent pods, are deleted by default after the build completes or is stopped. This behavior can be changed by the Kubernetes plugin pod retention setting. Pod retention can be set for all Jenkins builds, with overrides for each pod template. The following behaviors are supported:

- `Always` keeps the build pod regardless of build result.

- `Default` uses the plugin value, which is the pod template only.

- `Never` always deletes the pod.

- `On Failure` keeps the pod if it fails during the build.

You can override pod retention in the pipeline Jenkinsfile:

``` groovy
podTemplate(label: "mypod",
  cloud: "openshift",
  inheritFrom: "maven",
  podRetention: onFailure(),
  containers: [
    ...
  ]) {
  node("mypod") {
    ...
  }
}
```

- Allowed values for `podRetention` are `never()`, `onFailure()`, `always()`, and `default()`.

> [!WARNING]
> Pods that are kept might continue to run and count against resource quotas.
