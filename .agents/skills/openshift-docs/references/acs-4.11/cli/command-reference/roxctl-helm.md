<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl helm` command to manage Red Hat Advanced Cluster Security for Kubernetes (RHACS) Helm Charts. This reference covers the command syntax, available subcommands, and configuration options.

<a id="roxctl-helm-overview_roxctl-helm"></a>

# roxctl helm

Commands related to Red Hat Advanced Cluster Security for Kubernetes (RHACS) Helm Charts.

<a id="roxctl-helm-usage_roxctl-helm"></a>

## roxctl helm usage

Usage syntax for the `roxctl helm` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl helm [command] [flags]
```

</div>

<a id="roxctl-helm-available-commands_roxctl-helm"></a>

## Available commands

Available commands for the `roxctl helm` command.

| Command | Description |
|----|----|
| `derive-local-values` | Derive local Helm values from the cluster configuration. |
| `output` | Output a Helm chart. |

<a id="options-inherited-from-the-parent-command_roxctl-helm"></a>

# roxctl helm command options inherited from the parent command

The `roxctl helm` command supports the following options inherited from the parent `roxctl` command:

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
> These options are applicable to all the sub-commands of the `roxctl helm` command.

<a id="roxctl-helm-output_roxctl-helm"></a>

# roxctl helm output

Output a Helm chart.

<a id="roxctl-helm-output-usage_roxctl-helm"></a>

## roxctl helm output usage

Usage syntax for the `roxctl helm output` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl helm output <central_services or secured_cluster_services> [flags]
```

</div>

where:

`<central_services or secured_cluster_services>`  
Specifies the path to either the central services or the secured cluster services to generate a Helm chart output.

<a id="roxctl-helm-output-options_roxctl-helm"></a>

## Options

Options for the `roxctl helm output` command.

| Option | Description |
|----|----|
| `--debug` | Read templates from the local filesystem. The default value is `false`. |
| `--debug-path string` | Specify the path to the Helm templates on your local filesystem. For more details, run the `roxctl helm output --help` command. |
| `--image-defaults string` | Set the default container image settings. Image settings include `development_build`, `stackrox.io`, `rhacs`, and `opensource`. It influences repositories for image downloads, image names, and tag formats. The default value is `development_build`. |
| `--output-dir string` | Define the path to the output directory for the Helm chart. The default path is `./stackrox-<chart name>-chart`. |
| `--remove` | Remove the output directory if it already exists. The default value is `false`. |

<a id="roxctl-helm-derive-local-values_roxctl-helm"></a>

# roxctl helm derive-local-values

Derive local Helm values from the cluster configuration.

<a id="roxctl-helm-derive-local-values-usage_roxctl-helm"></a>

## roxctl helm derive-local-values usage

Usage syntax for the `roxctl helm derive-local-values` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl helm derive-local-values --output <path> \
<central_services> [flags]
```

</div>

where:

`<path>`  
Specifies the path where you want to save the generated local values file.

`<central_services>`  
Specifies the path to the central services configuration file.

<a id="roxctl-helm-derive-local-values-options_roxctl-helm"></a>

## Options

Options for the `roxctl helm derive-local-values` command.

| Option | Description |
|----|----|
| `--input string` | Specify the path to the file or directory containing the YAML input. |
| `--output string` | Define the path to the output file. |
| `--output-dir string` | Define the path to the output directory. |
| `--retry-timeout duration` | Set the timeout before retrying API requests. The timeout waits for the entire request duration before initiating a retry. The default value is `20s`. |
| `-t`, `--timeout duration` | Set the timeout for API requests representing the maximum duration of a request. The default value is `1m0s`. |
