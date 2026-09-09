<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl sensor` command to deploy Red Hat Advanced Cluster Security for Kubernetes (RHACS) services in secured clusters. This reference covers the command syntax, available subcommands, and configuration options.

<a id="roxctl-sensor-overview_roxctl-sensor"></a>

# roxctl sensor

Deploy Red Hat Advanced Cluster Security for Kubernetes (RHACS) services in secured clusters.

<a id="roxctl-sensor-usage_roxctl-sensor"></a>

## roxctl sensor usage

Usage syntax for the `roxctl sensor` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl sensor [command] [flags]
```

</div>

<a id="roxctl-sensor-available-commands_roxctl-sensor"></a>

## Available commands

Available commands for the `roxctl sensor` command.

| Command | Description |
|----|----|
| `generate` | Generate files to deploy RHACS services in secured clusters. |
| `generate-certs` | Download a YAML file with renewed certificates for Sensor, Collector, and Admission controller. |
| `get-bundle` | Download a bundle with the files to deploy RHACS services in a cluster. |

<a id="roxctl-sensor-options_roxctl-sensor"></a>

## Options

Options for the `roxctl sensor` command.

| Option | Description |
|----|----|
| `--retry-timeout duration` | Set the timeout before retrying API requests. A value of zero disables retries and waits for the entire request duration. The default value is `20s`. |
| `-t`, `--timeout duration` | Set the timeout for API requests representing the maximum duration of a request. The default value is `1m0s`. |

<a id="options-inherited-from-the-parent-command_roxctl-sensor"></a>

# roxctl sensor command options inherited from the parent command

The `roxctl sensor` command supports the following options inherited from the parent `roxctl` command:

| Option | Description |
|----|----|
| `--ca string` | Specify a custom CA certificate file path for secure connections. Alternatively, you can specify the file path by using the `ROX_CA_CERT_FILE` environment variable. |
| `--direct-grpc` | Set `--direct-grpc` for improved connection performance. Alternatively, by setting the `ROX_DIRECT_GRPC_CLIENT` environment variable to `true`, you can enable direct gRPC . The default value is `false`. |
| `-e`, `--endpoint string` | Set the endpoint for the service to contact. Alternatively, you can set the endpoint by using the `ROX_ENDPOINT` environment variable. The default value is `localhost:8443`. |
| `--force-http1` | Force the use of HTTP/1 for all connections. Alternatively, by setting the `ROX_CLIENT_FORCE_HTTP1` environment variable to `true`, you can force the use of HTTP/1. The default value is `false`. |
| `--insecure` | Enable insecure connection options. Alternatively, by setting the `ROX_INSECURE_CLIENT` environment variable to `true`, you can enable insecure connection options. The default value is `false`. |
| `--insecure-skip-tls-verify` | Skip the TLS certificate validation. Alternatively, by setting the `ROX_INSECURE_CLIENT_SKIP_TLS_VERIFY` environment variable to `true`, you can skip the TLS certificate validation. The default value is `false`. |
| `--no-color` | Disable the color output. Alternatively, by setting the `ROX_NO_COLOR environment variable` to `true`, you can disable the color output. The default value is `false`. |
| `-p`, `--password string` | Specify the password for basic authentication. Alternatively, you can set the password by using the `ROX_ADMIN_PASSWORD` environment variable. |
| `--plaintext` | Use an unencrypted connection. Alternatively, by setting the `ROX_PLAINTEXT` environment variable to `true`, you can enable an unencrypted connection. The default value is `false`. |
| `-s`, `--server-name string` | Set the TLS server name to use for SNI. Alternatively, you can set the server name by using the `ROX_SERVER_NAME` environment variable. |
| `--token-file string` | Use the API token provided in the specified file for authentication. Alternatively, you can set the token by using the `ROX_API_TOKEN` environment variable. |

> [!NOTE]
> These options are applicable to all the sub-commands of the `roxctl sensor` command.

<a id="roxctl-sensor-generate_roxctl-sensor"></a>

# roxctl sensor generate

Generate files to deploy RHACS services in secured clusters.

<a id="roxctl-sensor-generate-usage_roxctl-sensor"></a>

## roxctl sensor generate usage

Usage syntax for the `roxctl sensor generate` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl sensor generate [flags]
```

</div>

<a id="roxctl-sensor-generate-options_roxctl-sensor"></a>

## Options

Options for the `roxctl sensor generate` command.

| Option | Description |
|----|----|
| `--admission-controller-disable-bypass` | Disable the bypass annotations for the admission controller. The default value is `false`. |
| `--admission-controller-enforcement` | Valid values are `true` and `false`. The default value is `true`. When set to `true`, the admission controller enforces policies by rejecting creation or update attempts that are in violation of an enabled policy. When set to `false`, the admission controller does not enforce policies. |
| `--admission-controller-enforce-on-creates` | This field is deprecated and has no effect. Use the `--admission-controller-enforcement` option to configure enforcement. |
| `--admission-controller-enforce-on-updates` | This field is deprecated and has no effect. Use the `--admission-controller-enforcement` option to configure enforcement. |
| `--admission-controller-fail-on-error` | This parameter determines whether the API server request is allowed (fail open) or blocked (fail closed) if an error or timeout happens in the RHACS validating webhook’s evaluation. Valid values are `true` and `false`. The default value is `false`, which allows the request. When set to `true`, the request is blocked. |
| `--admission-controller-listen-on-creates` | This field is deprecated. The `sensor generate` command behaves as if this flag has been specified. |
| `--admission-controller-listen-on-updates` | This field is deprecated. The `sensor generate` command behaves as if this flag has been specified. |
| `--admission-controller-scan-inline` | This field is deprecated. The `sensor generate` command behaves as if this flag has been specified. |
| `--admission-controller-timeout int32` | This field is deprecated and using it has no effect. |
| `--central string` | Set the endpoint to which you want to connect Sensor. The default value is `central.stackrox:443`. |
| `--collection-method collection method` | Specify the collection method that you want to use for runtime support. Collection methods include `none`, `default`, `ebpf` and `core_bpf`. The default value is `default`. |
| `--collector-image-repository string` | Set the image repository that you want to use to deploy Collector. If not specified, a default value corresponding to the effective `--main-image repository` value is derived. |
| `--continue-if-exists` | Continue with downloading the sensor bundle even if the cluster already exists. The default value is `false`. |
| `--create-upgrader-sa` | Decide whether to create the upgrader service account with `cluster-admin` privileges to facilitate automated sensor upgrades. The default value is `true`. |
| `--disable-tolerations` | Disable tolerations for tainted nodes. The default value is `false`. |
| `--enable-pod-security-policies` | Create `PodSecurityPolicy` resources. The default value is `true`. |
| `--istio-support string` | Generate deployment files that support the specified Istio version. Valid versions include `1.0`, `1.1`, `1.2`, `1.3`, `1.4`, `1.5`, `1.6`, `1.7`. |
| `--main-image-repository string` | Specify the image repository that you want to use to deploy Sensor. If not specified, a default value is used. |
| `--name string` | Set the cluster name to identify the cluster. |
| `--output-dir string` | Set the output directory for the bundle contents. The default value is an automatically generated directory name inside the current directory. |
| `--slim-collector string[="true"]` | Use Collector-slim in the deployment bundle. Valid values include `auto`, `true`, and `false`. The default value is `auto`. |
| `-t`, `--timeout duration` | Set the timeout for API requests representing the maximum duration of a request. The default value is `5m0s`. |

Options

<a id="roxctl-sensor-generate-k8s_roxctl-sensor"></a>

## roxctl sensor generate k8s

Generate the required files to deploy RHACS services in a Kubernetes cluster.

<a id="roxctl-sensor-generate-k8s-usage_roxctl-sensor"></a>

### roxctl sensor generate k8s usage

Usage syntax for the `roxctl sensor generate k8s` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl sensor generate k8s [flags]
```

</div>

<a id="roxctl-sensor-generate-k8s-options_roxctl-sensor"></a>

### Options

Options for the `roxctl sensor generate k8s` command.

| Option | Description |
|----|----|
| `--admission-controller-listen-on-events` | Enable admission controller webhook to listen to Kubernetes events. The default value is `true`. |

Options

<a id="roxctl-sensor-generate-openshift_roxctl-sensor"></a>

## roxctl sensor generate openshift

Generate the required files to deploy RHACS services in a Red Hat OpenShift cluster.

<a id="roxctl-sensor-generate-openshift-usage_roxctl-sensor"></a>

### roxctl sensor generate openshift usage

Usage syntax for the `roxctl sensor generate openshift` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl sensor generate openshift [flags]
```

</div>

<a id="roxctl-sensor-generate-openshift-options_roxctl-sensor"></a>

### Options

Options for the `roxctl sensor generate openshift` command.

| Option | Description |
|----|----|
| \`--admission-controller-listen-on-events false | true |
| auto\[=true\]\` | Enable or disable the admission controller webhook to listen to Kubernetes events. The default value is `auto`. |
| \`--disable-audit-logs false | true |
| auto\[=true\]\` | Enable or disable audit log collection for runtime detection. The default value is `auto`. |
| `--openshift-version int` | Specify the Red Hat OpenShift major version for which you want to generate the deployment files. |

Options

<a id="roxctl-sensor-get-bundle_roxctl-sensor"></a>

# roxctl sensor get-bundle

Download a bundle with the files to deploy RHACS services into a cluster.

<a id="roxctl-sensor-get-bundle-usage_roxctl-sensor"></a>

## roxctl sensor get-bundle usage

Usage syntax for the `roxctl sensor get-bundle` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl sensor get-bundle <cluster_details> [flags]
```

</div>

where:

`<cluster_details>`  
Specifies the cluster name or ID.

<a id="roxctl-sensor-get-bundle-options_roxctl-sensor"></a>

## Options

Options for the `roxctl sensor get-bundle` command.

| Option | Description |
|----|----|
| `--create-upgrader-sa` | Specify whether to create the upgrader service account with `cluster-admin` privileges for automated Sensor upgrades. The default value is `true`. |
| `--istio-support string` | Generate deployment files that support the specified Istio version. Valid versions include `1.0`, `1.1`, `1.2`, `1.3`, `1.4`, `1.5`, `1.6`, and `1.7`. |
| `--output-dir string` | Specify the output directory for the bundle contents. The default value is an automatically generated directory name inside the current directory. |
| `--slim-collector string[="true"]` | Use Collector-slim in the deployment bundle. Valid values include `auto`, `true` and `false`. The default value is `auto`. |
| `-t`, `--timeout duration` | Set the timeout for API requests representing the maximum duration of a request. The default value is `5m0s`. |

Options

<a id="roxctl-sensor-generate-certs_roxctl-sensor"></a>

# roxctl sensor generate-certs

Download a YAML file with renewed certificates for Sensor, Collector, and Admission controller.

<a id="roxctl-sensor-generate-certs-usage_roxctl-sensor"></a>

## roxctl sensor generate-certs usage

Usage syntax for the `roxctl sensor generate-certs` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl sensor generate-certs <cluster_details> [flags]
```

</div>

where:

`<cluster_details>`  
Specifies the cluster name or ID.

<a id="roxctl-sensor-generate-certs-options_roxctl-sensor"></a>

## Options

Options for the `roxctl sensor generate-certs` command.

| Option | Description |
|----|----|
| `--output-dir string` | Specify the output directory for the YAML file. The default value is `.` (the current working directory). |

Options
