<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl` CLI to interact with RHACS services and manage deployments, policies, and configurations.

<a id="roxctl-overview_roxctl"></a>

# roxctl

Display the available commands and optional parameters for the `roxctl` CLI. You must have an account with administrator privileges to use these commands.

<a id="roxctl-usage_roxctl"></a>

## roxctl usage

Usage syntax for the `roxctl` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl [command] [flags]
```

</div>

<a id="roxctl-available-commands_roxctl"></a>

## Available commands

Available commands for the `roxctl` CLI.

| Command | Description |
|----|----|
| `central` | Commands related to the Central service. |
| `cluster` | Commands related to a cluster. |
| `collector` | Commands related to the Collector service. |
| `completion` | Generate shell completion scripts. |
| `declarative-config` | Manage declarative configuration. |
| `deployment` | Commands related to deployments. |
| `helm` | Commands related to Red Hat Advanced Cluster Security for Kubernetes (RHACS) Helm Charts. |
| `image` | Commands that you can run on a specific image. |
| `netpol` | Commands related to network policies. |
| `scanner` | Commands related to the Scanner service. |
| `sensor` | Deploy RHACS services in secured clusters. |
| `version` | Display the current roxctl version. |

<a id="roxctl-command-options_roxctl"></a>

## Options

Options for the `roxctl` command.

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
