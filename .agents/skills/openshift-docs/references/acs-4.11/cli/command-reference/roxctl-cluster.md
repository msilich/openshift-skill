<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl cluster` command to manage cluster operations and remove Sensors from Central. This reference covers the command syntax, available subcommands, and configuration options.

<a id="roxctl-cluster-overview_roxctl-cluster"></a>

# roxctl cluster

Commands related to a cluster.

<a id="roxctl-cluster-usage_roxctl-cluster"></a>

## roxctl cluster usage

Usage syntax for the `roxctl cluster` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl cluster [command] [flags]
```

</div>

<a id="roxctl-cluster-available-commands_roxctl-cluster"></a>

## Available commands

Available commands for the `roxctl cluster` command.

| Command  | Description                 |
|----------|-----------------------------|
| `delete` | Remove Sensor from Central. |

<a id="roxctl-cluster-options_roxctl-cluster"></a>

## Options

Options for the `roxctl cluster` command.

| Option | Description |
|----|----|
| `--retry-timeout duration` | Set the retry timeout for API requests. A value of zero allows the full request duration without retry. The default value is `20s`. |
| `-t`, `--timeout duration` | Set the timeout for API requests representing the maximum duration of a request. The default value is `1m0s`. |

<a id="options-inherited-from-the-parent-command_roxctl-cluster"></a>

# roxctl cluster command options inherited from the parent command

The `roxctl cluster` command supports the following options inherited from the parent `roxctl` command:

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
> These options are applicable to all the sub-commands of the `roxctl cluster` command.

<a id="roxctl-cluster-delete_roxctl-cluster"></a>

# roxctl cluster delete

Remove Sensor from Central.

<a id="roxctl-cluster-delete-usage_roxctl-cluster"></a>

## roxctl cluster delete usage

Usage syntax for the `roxctl cluster delete` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl cluster delete [flags]
```

</div>

<a id="roxctl-cluster-delete-options_roxctl-cluster"></a>

## Options

Options for the `roxctl cluster delete` command.

| Option          | Description                         |
|-----------------|-------------------------------------|
| `--name string` | Specify the cluster name to delete. |
