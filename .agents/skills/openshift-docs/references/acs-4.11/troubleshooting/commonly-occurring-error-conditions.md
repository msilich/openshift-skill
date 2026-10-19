<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Most Collector errors occur during startup, when Collector configures itself and loads the eBPF probe into the system. Use the startup diagnostic summary in the Collector logs to identify the startup stage that failed, and then resolve the error condition for that stage.

<a id="collector-startup-diagnostics-overview_error-conditions"></a>

# Collector startup diagnostics

Collector startup involves several stages. A failure at any stage terminates Collector startup, and you must correct the cause of the failure before Collector can start. You can use the diagnostic summary in the logs to identify the stages that succeeded or failed.

Collector startup involves the following stages:

- Parse Configuration

- Analyze Host

- Connecting to Sensor

- Loading eBPF probe

If any part of the startup procedure fails, the logs display a diagnostic summary with details about the stages that succeeded or failed.

The following log file example shows a successful startup:

``` terminal
[INFO    2025/07/24 10:05:54] == Collector Startup Diagnostics: ==
[INFO    2025/07/24 10:05:54]  Connected to Sensor?       true
[INFO    2025/07/24 10:05:54]  Kernel driver candidates:
[INFO    2025/07/24 10:05:54]    core_bpf (available)
[INFO    2025/07/24 10:05:54]  Driver loaded into kernel: core_bpf
[INFO    2025/07/24 10:05:54] ====================================
```

The log output confirms that Collector connected to Sensor and loaded the eBPF probe. You can use this log to check for the successful startup of Collector.

<a id="unable-to-connect-to-the-sensor_error-conditions"></a>

# Resolve Collector connection failures to Sensor

Sensor downloads the kernel drivers and the Classless Inter-Domain Routing (CIDR) blocks that Collector requires to process network events. If Collector cannot connect to Sensor, Collector startup fails. To restore Collector startup, verify the Sensor address in the Collector configuration and confirm that the Sensor pod is running.

The following logs indicate that Collector is unable to connect to Sensor:

``` terminal
Collector Version: 3.15.0
OS: Ubuntu 20.04.4 LTS
Kernel Version: 5.4.0-126-generic
[...]
[INFO    2023/05/13 12:20:43] Sensor configured at address: sensor.stackrox.svc:9998
[INFO    2023/05/13 12:20:43] Attempting to connect to Sensor
[INFO    2023/05/13 12:21:13]
[INFO    2023/05/13 12:21:13] == Collector Startup Diagnostics: ==
[INFO    2023/05/13 12:21:13]  Connected to Sensor?       false
[INFO    2023/05/13 12:21:13]  Kernel driver candidates:
[INFO    2023/05/13 12:21:13] ====================================
[INFO    2023/05/13 12:21:13]
[FATAL   2023/05/13 12:21:13] Unable to connect to Sensor at 'sensor.stackrox.svc:9998'.
```

This error means that either Sensor has not started correctly or the Sensor address in the Collector configuration is wrong. Complete the following steps to identify which of these causes applies and to correct it.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Check the Sensor address in the Collector configuration by viewing the Collector logs, or by running the following command:

    ``` terminal
    $ oc -n stackrox get pod <collector_pod_name> -o jsonpath='{.spec.containers[0].env[?(@.name=="GRPC_SERVER")].value}'
    ```

    where:

    `<collector_pod_name>`  
    Specifies the name of your Collector pod, for example, `collector-vclg5`.

    The command returns the Sensor endpoint that Collector uses, for example, `sensor.stackrox.svc:443`. The hostname, namespace, and port must match the Sensor service in the secured cluster.

2.  Confirm that the Sensor service exists and listens on that port by running the following command:

    ``` terminal
    $ oc -n stackrox get service sensor
    ```

3.  Confirm that the Sensor pod is running by running the following command:

    ``` terminal
    $ oc -n stackrox get pods -l app=sensor
    ```

    The Sensor pod must report the `Running` status and `1/1` in the `READY` column.

4.  Correct the cause of the failure:

    - If the Sensor pod is not running, examine the Sensor pod events and logs to determine why Sensor failed to start, and then resolve that failure.

    - If the Sensor endpoint that Collector uses does not match the Sensor service, redeploy the secured cluster resources with the correct Sensor address.

5.  Restart the Collector pods by running the following command:

    ``` terminal
    $ oc -n stackrox delete pods -l app=collector
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Retrieve the Collector logs and confirm that the startup diagnostic summary reports `Connected to Sensor?` as `true`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Retrieving the Collector logs](retrieving-and-analyzing-the-collector-logs-and-pod-status.md#retrieving-the-collector-logs_logs-and-pod-status)

- [Analyzing the Collector pod status](retrieving-and-analyzing-the-collector-logs-and-pod-status.md#analyzing-the-collector-pod-status_logs-and-pod-status)

- [Verifying installation](../installing/installing_ocp/verify-installation-rhacs-ocp.md#verify-acs-installation_verify-installation-rhacs-ocp)

</div>

<a id="failing-to-load-the-ebpf-probe_error-conditions"></a>

# Failing to load the eBPF probe

Before Collector starts, it loads the eBPF probe. In rare cases, Collector cannot load the eBPF probe, which results in various error messages or exceptions. Check the logs to determine why the eBPF probe failed to load.

Consider the following Collector log:

``` terminal
[...]
[INFO    2025/07/24 10:26:37] Trying to open the right engine!
[INFO    2025/07/24 10:26:41] libbpf: prog 'execve_x': -- BEGIN PROG LOAD LOG --
[...]
-- END PROG LOAD LOG --
[INFO    2025/07/24 10:26:41] libbpf: prog 'execve_x': failed to load: -7
[INFO    2025/07/24 10:26:41] libbpf: failed to load object 'bpf_probe'
[INFO    2025/07/24 10:26:41] libbpf: failed to load BPF skeleton 'bpf_probe': -7
[INFO    2025/07/24 10:26:41] libpman: failed to load BPF object (errno: 7 | message: Argument list too long)
```

If you see this kind of error, report it to the Red Hat Advanced Cluster Security for Kubernetes (RHACS) support team. Alternatively, create an issue in the `stackrox/collector` GitHub repository.

<div>

<div class="title">

Additional resources

</div>

- [stackrox/collector GitHub repository](https://github.com/stackrox/collector/issues/new/choose)

</div>
