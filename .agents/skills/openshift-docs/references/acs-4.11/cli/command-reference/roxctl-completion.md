<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl completion` command to generate shell completion scripts for Bash, Zsh, Fish, and PowerShell.

<a id="roxctl-completion-overview_roxctl-completion"></a>

# roxctl completion

Generate shell completion scripts.

<a id="roxctl-completion-usage_roxctl-completion"></a>

## roxctl completion usage

Usage syntax for the `roxctl completion` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl completion [bash|zsh|fish|powershell]
```

</div>

<a id="roxctl-completion-supported-shell-types_roxctl-completion"></a>

## Supported shell types

Shell types supported by the `roxctl completion` command.

| Shell type   | Description                                            |
|--------------|--------------------------------------------------------|
| `bash`       | Generate a completion script for the Bash shell.       |
| `zsh`        | Generate a completion script for the Zsh shell.        |
| `fish`       | Generate a completion script for the Fish shell.       |
| `powershell` | Generate a completion script for the PowerShell shell. |

<a id="options-inherited-from-the-parent-command_roxctl-completion"></a>

# roxctl completion command options inherited from the parent command

The `roxctl completion` command supports the following options inherited from the parent `roxctl` command:

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
