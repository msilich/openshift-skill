<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl collector` command to manage support packages for the Collector service.

<a id="roxctl-collector-overview_roxctl-collector"></a>

# roxctl collector

Commands related to the Collector service.

<a id="roxctl-collector-usage_roxctl-collector"></a>

## roxctl collector usage

Usage syntax for the `roxctl collector` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl collector [command] [flags]
```

</div>

<a id="roxctl-collector-available-commands_roxctl-collector"></a>

## Available commands

Available commands for the `roxctl collector` command.

| Command            | Description                            |
|--------------------|----------------------------------------|
| `support-packages` | Upload support packages for Collector. |

<a id="options-inherited-from-the-parent-command_roxctl-collector"></a>

# roxctl collector command options inherited from the parent command

The `roxctl collector` command supports the following options inherited from the parent `roxctl` command:

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
> These options are applicable to all the sub-commands of the `roxctl collector` command.

<a id="roxctl-collector-support-packages_roxctl-collector"></a>

# roxctl collector support-packages

You can view and manage support packages for the Collector component, including uploading support packages to Central.

> [!NOTE]
> Support packages are deprecated and have no effect on secured clusters running version 4.5 or later. Support package uploads only affect secured clusters on version 4.4 or earlier.

<a id="roxctl-collector-support-packages-usage_roxctl-collector"></a>

## roxctl collector support-packages usage

Usage syntax for the `roxctl collector support-packages` command.

``` terminal
$ roxctl collector support-packages [flags]
```

<a id="roxctl-collector-support-packages-upload_roxctl-collector"></a>

## roxctl collector support-packages upload

You can upload a file containing kernel support packages such as eBPF probes to Central in offline or disconnected environments where Central cannot connect to the internet to download these required driver files automatically.

<a id="roxctl-collector-support-packages-upload-usage_roxctl-collector"></a>

### roxctl collector support-packages upload usage

Usage syntax for the `roxctl collector support-packages upload` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl collector support-packages upload [flags]
```

</div>

<a id="roxctl-collector-support-packages-upload-options_roxctl-collector"></a>

### Options

Options for the `roxctl collector support-packages upload` command.

| Option | Description |
|----|----|
| `--overwrite` | Specify whether you want to overwrite existing but different files. The default value is `false`. |
| `--retry-timeout duration` | Set the timeout for retrying API requests. A value of zero waits for the entire request duration without retrying. The default value is `20s`. |
| `-t`, `--timeout duration` | Set the timeout for API requests. This option represents the maximum duration of a request. The default value is `1m0s`. |

Options
