<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Most errors occur during Collector startup when Collector configures itself and loads eBPF probe into the system.

Collector startup process involves the following stages:

- Parse Configuration

- Analyze Host

- Connecting to Sensor

- Loading eBPF probe

Failure at any step is considered fatal. If any part of the startup procedure fails, the logs display a diagnostic summary with details about which steps succeeded or failed.

The following log file example shows a successful startup:

``` terminal
[INFO    2025/07/24 10:05:54] == Collector Startup Diagnostics: ==
[INFO    2025/07/24 10:05:54]  Connected to Sensor?       false
[INFO    2025/07/24 10:05:54]  Kernel driver candidates:
[INFO    2025/07/24 10:05:54]    core_bpf (available)
[INFO    2025/07/24 10:05:54]  Driver loaded into kernel: core_bpf
[INFO    2025/07/24 10:05:54] ====================================
```

The log output confirms that Collector connected to Sensor and loaded the eBPF probe. You can use this log to check for the successful startup of Collector.

<a id="unable-to-connect-to-the-sensor_error-conditions"></a>

# Unable to connect to the Sensor

When starting, first check if you can connect to Sensor. Sensor is responsible for downloading kernel drivers and CIDR blocks for processing network events, making it an essential part of the startup process. The following logs indicate you are unable to connect to the Sensor:

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

This error could mean that Sensor has not started correctly or that Collector configuration is incorrect. To fix this issue, you must verify Collector configuration to ensure that Sensor address is correct and that the Sensor pod is running correctly.

View the Collector logs to specifically check the configured Sensor address. Alternatively, you can run the following command:

``` terminal
$ kubectl -n stackrox get pod <collector_pod_name> -o jsonpath='{.spec.containers[0].env[?(@.name=="GRPC_SERVER")].value}'
```

where:

`<collector_pod_name>`  
Specifies the name of your Collector pod, for example, `collector-vclg5`.

<a id="failing-to-load-the-ebpf-probe_error-conditions"></a>

# Failing to load the eBPF probe

Before Collector starts, it loads the eBPF probe; however, in rare cases, you might encounter issues where Collector cannot load the eBPF probe, which results in various error messages or exceptions. In such cases, you must check the logs to identify the problems with failure in loading the eBPF probe.

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

If you encounter this kind of error, you must report it to Red Hat Advanced Cluster Security for Kubernetes (RHACS) support team or create an issue in the `stackrox/collector` GitHub repository.
