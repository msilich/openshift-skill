<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can monitor application health on your OpenShift Container Platform cluster by configuring readiness, liveness, and startup probes for your application containers. You can also observe probe failure events so you can address issues before they affect users.

In software systems, components can become unhealthy due to transient issues such as temporary connectivity loss, configuration errors, or problems with external dependencies. OpenShift Container Platform applications have a number of options to detect and handle unhealthy containers.

# Health checks

You can configure health checks by understanding the differences between readiness, liveness, and startup probes.

A health check periodically performs diagnostics on a running container using any combination of the readiness, liveness, and startup health checks.

You can include one or more probes in the specification for the pod that contains the container which you want to perform the health checks.

> [!NOTE]
> If you want to add or edit health checks in an existing pod, you must edit the pod `DeploymentConfig` object or use the web console. You cannot use the CLI to add or edit health checks for an existing pod.

Readiness probe
A *readiness probe* determines if a container is ready to accept service requests. If the readiness probe fails for a container, the kubelet removes the pod from the list of available service endpoints.

After a failure, the probe continues to examine the pod. If the pod becomes available, the kubelet adds the pod to the list of available service endpoints.

Liveness health check
A *liveness probe* determines if a container is still running. If the liveness probe fails due to a condition such as a deadlock, the kubelet kills the container. The pod then responds based on the pod restart policy.

For example, a liveness probe on a pod with a `restartPolicy` of `Always` or `OnFailure` kills and restarts the container.

Startup probe
A *startup probe* indicates whether the application within a container is started. All other probes are disabled until the startup succeeds. If the startup probe does not succeed within a specified time period, the kubelet kills the container, and the container is subject to the pod `restartPolicy`.

Some applications can require additional startup time on their first initialization. You can use a startup probe with a liveness or readiness probe to delay that probe long enough to handle lengthy start-up time using the `failureThreshold` and `periodSeconds` parameters.

For example, you can add a startup probe to a liveness probe. Use a `failureThreshold` of 30 failures and a `periodSeconds` of 10 seconds. This combination (30 × 10s = 300s) gives a maximum startup window of 5 minutes. After the startup probe succeeds the first time, the liveness probe takes over.

You can configure liveness, readiness, and startup probes with any of the following types of tests:

- HTTP `GET`: When using an HTTP `GET` test, the test determines the healthiness of the container by using a webhook. The test is successful if the HTTP response code is between `200` and `399`.

  You can use an HTTP `GET` test with applications that return HTTP status codes when completely initialized.

- Container Command: When using a container command test, the probe executes a command inside the container. The probe is successful if the test exits with a `0` status.

- Transmission Control Protocol (TCP) socket: When using a TCP socket test, the probe attempts to open a socket to the container. The container is considered healthy only if the probe can establish a connection. You can use a TCP socket test with applications that do not start listening until initialization is complete.

You can configure several fields to control the behavior of a probe:

- `initialDelaySeconds`: The time, in seconds, after the container starts before the probe can be scheduled. The default is 0.

- `periodSeconds`: The delay, in seconds, between performing probes. The default is `10`. This value must be greater than `timeoutSeconds`.

- `timeoutSeconds`: The number of seconds of inactivity after which the probe times out and the container is assumed to have failed. The default is `1`. This value must be lower than `periodSeconds`.

- `successThreshold`: The number of times that the probe must report success after a failure to reset the container status to successful. The value must be `1` for a liveness probe. The default is `1`.

- `failureThreshold`: The number of times that the probe is allowed to fail. The default is 3. When the threshold is reached:

  - for a liveness probe, the container is restarted

  - for a readiness probe, the pod is marked `Unready`

  - for a startup probe, the container is killed and is subject to the `restartPolicy` of the pod

## Example probes

The following are samples of different probes as they appear in an object specification.

<div class="formalpara">

<div class="title">

Sample readiness probe with a container command readiness probe in a pod spec

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: health-check
  name: my-application
# ...
spec:
  containers:
  - name: goproxy-app
    args:
    image: registry.k8s.io/goproxy:0.1
    readinessProbe:
      exec:
        command:
        - cat
        - /tmp/healthy
# ...
```

</div>

where:

`spec.containers.name`
Specifies the container name.

`spec.containers.image`
Specifies the container image to deploy.

`spec.containers.readinessProbe`
Specifies a readiness probe.

`spec.containers.readinessProbe.exec`
Specifies a container command test.

`spec.containers.readinessProbe.exec.command`
Specifies the commands to execute on the container.

<div class="formalpara">

<div class="title">

Sample container command startup probe and liveness probe with container command tests in a pod spec

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: health-check
  name: my-application
# ...
spec:
  containers:
  - name: goproxy-app
    args:
    image: registry.k8s.io/goproxy:0.1
    livenessProbe:
      httpGet:
        scheme: HTTPS
        path: /healthz
        port: 8080
        httpHeaders:
        - name: X-Custom-Header
          value: Awesome
    startupProbe:
      httpGet:
        path: /healthz
        port: 8080
      failureThreshold: 30
      periodSeconds: 10
# ...
```

</div>

where:

`spec.containers.name`
Specifies the container name.

`spec.containers.image`
Specifies the container image to deploy.

`spec.containers.livenessProbe`
Specifies a liveness probe.

`spec.containers.livenessProbe.httpGet`
Specifies an HTTP `GET` test.

`spec.containers.livenessProbe.httpGet.scheme`
Specifies the internet scheme: `HTTP` or `HTTPS`. The default value is `HTTP`.

`spec.containers.livenessProbe.httpGet.port`
Specifies the port on which the container is listening.

`spec.containers.startupProbe`
Specifies a startup probe.

`spec.containers.startupProbe.httpGet`
Specifies an HTTP `GET` test.

`spec.containers.startupProbe.httpGet.port`
Specifies the port on which the container is listening.

`spec.containers.startupProbe.failureThreshold`
Specifies the number of times to try the probe after a failure.

`spec.containers.startupProbe.periodSeconds`
Specifies the number of seconds to perform the probe.

<div class="formalpara">

<div class="title">

Sample liveness probe with a container command test that uses a timeout in a pod spec

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: health-check
  name: my-application
# ...
spec:
  containers:
  - name: goproxy-app
    args:
    image: registry.k8s.io/goproxy:0.1
    livenessProbe:
      exec:
        command:
        - /bin/bash
        - '-c'
        - timeout 60 /opt/eap/bin/livenessProbe.sh
      periodSeconds: 10
      successThreshold: 1
      failureThreshold: 3
# ...
```

</div>

where:

`spec.containers.name`
Specifies the container name.

`spec.containers.image`
Specifies the container image to deploy.

`spec.containers.livenessProbe`
Specifies the liveness probe.

`spec.containers.livenessProbe.exec`
Specifies the type of probe, here a container command probe.

`spec.containers.livenessProbe.exec.command`
Specifies the command line to execute inside the container.

`spec.containers.livenessProbe.periodSeconds`
Specifies how often in seconds to perform the probe.

`spec.containers.livenessProbe.successThreshold`
Specifies the number of consecutive successes needed to show success after a failure.

`spec.containers.livenessProbe.failureThreshold`
Specifies the number of times to try the probe after a failure.

<div class="formalpara">

<div class="title">

Sample readiness probe and liveness probe with a TCP socket test in a deployment

</div>

``` yaml
kind: Deployment
apiVersion: apps/v1
metadata:
  labels:
    test: health-check
  name: my-application
spec:
# ...
  template:
    spec:
      containers:
        - resources: {}
          readinessProbe:
            tcpSocket:
              port: 8080
            timeoutSeconds: 1
            periodSeconds: 10
            successThreshold: 1
            failureThreshold: 3
          terminationMessagePath: /dev/termination-log
          name: ruby-ex
          livenessProbe:
            tcpSocket:
              port: 8080
            initialDelaySeconds: 15
            timeoutSeconds: 1
            periodSeconds: 10
            successThreshold: 1
            failureThreshold: 3
# ...
```

</div>

where:

`spec.template.spec.containers.readinessProbe`
Specifies the readiness probe.

`spec.template.spec.containers.livenessProbe`
Specifies the liveness probe.

# Configuring health checks using the CLI

To configure readiness, liveness, and startup probes, add one or more probes to the specification for the pod that contains the container on which you want to perform the health checks. Probes let the cluster detect unhealthy containers and respond before failures affect application availability.

> [!NOTE]
> If you want to add or edit health checks in an existing pod, you must edit the pod `DeploymentConfig` object or use the web console. You cannot use the CLI to add or edit health checks for an existing pod.

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file that defines a `Pod` object with one or more probes:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        test: health-check
      name: my-application
    spec:
      containers:
      - name: my-container
        args:
        image: registry.k8s.io/goproxy:0.1
        livenessProbe:
          tcpSocket:
            port: 8080
          initialDelaySeconds: 15
          periodSeconds: 20
          timeoutSeconds: 10
        readinessProbe:
          httpGet:
            host: my-host
            scheme: HTTPS
            path: /healthz
            port: 8080
        startupProbe:
          exec:
            command:
            - cat
            - /tmp/healthy
          failureThreshold: 30
          periodSeconds: 20
          timeoutSeconds: 10
    ```

    > [!NOTE]
    > Include only the probe types your application needs. The example shows liveness, readiness, and startup probes together for reference.

    where:

    `spec.containers.name`
    Specifies the container name.

    `spec.containers.image`
    Specifies the container image to deploy.

    `spec.containers.livenessProbe`
    Specifies a liveness probe. This value is optional.

    `spec.containers.livenessProbe.tcpSocket`
    Specifies a test to perform, here a Transmission Control Protocol (TCP) socket test.

    `spec.containers.livenessProbe.tcpSocket.port`
    Specifies the port on which the container is listening.

    `spec.containers.livenessProbe.initialDelaySeconds`
    Specifies the time, in seconds, after the container starts before the probe can be scheduled.

    `spec.containers.livenessProbe.periodSeconds`
    Specifies the number of seconds to perform the probe. The default is `10`. This value must be greater than `timeoutSeconds`.

    `spec.containers.livenessProbe.timeoutSeconds`
    Specifies the number of seconds of inactivity after which the probe is assumed to have failed. The default is `1`. This value must be lower than `periodSeconds`.

    `spec.containers.readinessProbe`
    Specifies a readiness probe. This value is optional.

    `spec.containers.readinessProbe.httpGet`
    Specifies the type of test to perform, here an HTTP test.

    `spec.containers.readinessProbe.httpGet.host`
    Specifies a host IP address. When `host` is not defined, the `PodIP` is used.

    `spec.containers.readinessProbe.httpGet.scheme`
    Specifies `HTTP` or `HTTPS`. When `scheme` is not defined, the `HTTP` scheme is used.

    `spec.containers.readinessProbe.httpGet.port`
    Specifies the port on which the container is listening.

    `spec.containers.startupProbe`
    Specifies a startup probe. This value is optional.

    `spec.containers.startupProbe.exec`
    Specifies the type of test to perform, here a container execution probe.

    `spec.containers.startupProbe.exec.command`
    Specifies the commands to execute on the container.

    `spec.containers.startupProbe.failureThreshold`
    Specifies the number of times to try the probe after a failure.

    `spec.containers.startupProbe.periodSeconds`
    Specifies the number of seconds to perform the probe. The default is `10`. This value must be greater than `timeoutSeconds`.

    `spec.containers.startupProbe.timeoutSeconds`
    Specifies the number of seconds of inactivity after which the probe is assumed to have failed. The default is `1`. This value must be lower than `periodSeconds`.

    > [!NOTE]
    > If the `initialDelaySeconds` value is lower than the `periodSeconds` value, the first readiness probe occurs at some point between the two periods due to an issue with timers.
    >
    > The `timeoutSeconds` value must be lower than the `periodSeconds` value.

2.  Apply the YAML file by running the following command:

    ``` terminal
    $ oc create -f <file-name>.yaml
    ```

3.  Verify the state of the health check pod by running the following command:

    ``` terminal
    $ oc describe pod my-application
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Events:
      Type    Reason     Age   From                                  Message
      ----    ------     ----  ----                                  -------
      Normal  Scheduled  9s    default-scheduler                     Successfully assigned openshift-logging/liveness-exec to ip-10-0-143-40.ec2.internal
      Normal  Pulling    2s    kubelet, ip-10-0-143-40.ec2.internal  pulling image "registry.k8s.io/liveness"
      Normal  Pulled     1s    kubelet, ip-10-0-143-40.ec2.internal  Successfully pulled image "registry.k8s.io/liveness"
      Normal  Created    1s    kubelet, ip-10-0-143-40.ec2.internal  Created container
      Normal  Started    1s    kubelet, ip-10-0-143-40.ec2.internal  Started container
    ```

    </div>

    The following example shows output when a liveness probe fails and the container is restarted:

    ``` terminal
    ....

    Events:
      Type     Reason          Age                From                                               Message
      ----     ------          ----               ----                                               -------
      Normal   Scheduled       <unknown>                                                             Successfully assigned aaa/liveness-http to ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj
      Normal   AddedInterface  47s                multus                                             Add eth0 [10.129.2.11/23]
      Normal   Pulled          46s                kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Successfully pulled image "registry.k8s.io/liveness" in 773.406244ms
      Normal   Pulled          28s                kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Successfully pulled image "registry.k8s.io/liveness" in 233.328564ms
      Normal   Created         10s (x3 over 46s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Created container liveness
      Normal   Started         10s (x3 over 46s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Started container liveness
      Warning  Unhealthy       10s (x6 over 34s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Liveness probe failed: HTTP probe failed with statuscode: 500
      Normal   Killing         10s (x2 over 28s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Container liveness failed liveness probe, will be restarted
      Normal   Pulling         10s (x3 over 47s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Pulling image "registry.k8s.io/liveness"
      Normal   Pulled          10s                kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Successfully pulled image "registry.k8s.io/liveness" in 244.116568ms
    ```

</div>

# Application health monitoring by using the Developer perspective

You can monitor application health by adding readiness, liveness, and startup probes from the **Developer** perspective, either when you deploy an application or on a deployed application. Probes detect unhealthy containers and keep applications available before failures affect users.

You can use the **Developer** perspective to add three types of health probes to your container to ensure that your application is healthy:

- Use a readiness probe to check if the container is ready to handle requests.

- Use a liveness probe to check if the container is running.

- Use a startup probe to check if the application within the container has started.

You can add health checks either while creating and deploying an application, or after you have deployed an application.

# Editing health checks using the Developer perspective

You can edit, remove, or add readiness, liveness, and startup probes on a deployed application from the **Topology** view in the **Developer** perspective. Use the **Edit Health Checks** page to update probe parameters, remove probes, or add new probe types.

<div>

<div class="title">

Prerequisites

</div>

- You have switched to the **Developer** perspective in the web console.

- You have created and deployed an application on OpenShift Container Platform using the **Developer** perspective.

- You have added health checks to your application.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Topology** view, right-click your application and select **Edit Health Checks**. Alternatively, in the side panel, click the **Actions** drop-down list and select **Edit Health Checks**.

2.  To remove a previously added health probe, click the **Remove** icon adjoining it.

3.  To edit the parameters of an existing probe:

    1.  Click the **Edit Probe** link next to a previously added probe to see the parameters for the probe.

    2.  Modify the parameters as required, and click the check mark to save your changes.

4.  To add a new health probe, click the add probe links. For example, to add a liveness probe that checks if your container is running:

    1.  Click **Add Liveness Probe** to see a form containing the parameters for the probe.

    2.  Edit the probe parameters as required.

        > [!NOTE]
        > The `Timeout` value must be lower than the `Period` value. The `Timeout` default value is `1`. The `Period` default value is `10`.

    3.  Click the check mark at the bottom of the form. The **Liveness Probe Added** message is displayed.

5.  Click **Save** to save your modifications and add the additional probes to your container. You are redirected to the **Topology** view.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the side panel, verify that the probes have been added by clicking on the deployed pod under the **Pods** section.

2.  In the **Pod Details** page, click the listed container in the **Containers** section.

3.  In the **Container Details** page, verify that the Liveness probe - `HTTP Get 10.129.4.65:8080/` has been added to the container, in addition to the earlier existing probes.

</div>

# Monitoring health check failures using the Developer perspective

You can monitor health check failures for a deployed application from the **Topology** view in the **Developer** perspective. Use the **Observe** tab to view events that report probe failures and show when containers need attention before users are affected.

<div>

<div class="title">

Prerequisites

</div>

- You have switched to the **Developer** perspective in the web console.

- You have created and deployed an application on OpenShift Container Platform using the **Developer** perspective.

- You have added health checks to your application.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Topology** view, click the application node to see the side panel.

2.  Click the **Observe** tab to see health check failure events in the **Events (Warning)** section.

3.  Click the down arrow adjoining **Events (Warning)** to see the details of the health check failure.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Enabling the Developer perspective in the web console](../web_console/web-console-overview.md#enabling-developer-perspective_web-console_web-console-overview)

- [Creating applications using the Developer perspective](creating_applications/odc-creating-applications-using-developer-perspective.md#odc-creating-applications-using-developer-perspective)

</div>
