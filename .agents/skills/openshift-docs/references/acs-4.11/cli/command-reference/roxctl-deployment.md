<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl deployment` command to check deployments for violations of deployment time policies. This reference covers the command syntax, available subcommands, and configuration options.

<a id="roxctl-deployment-overview_roxctl-deployment"></a>

# roxctl deployment

Commands related to deployments.

<a id="roxctl-deployment-usage_roxctl-deployment"></a>

## roxctl deployment usage

Usage syntax for the `roxctl deployment` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl deployment [command] [flags]
```

</div>

<a id="roxctl-deployment-available-commands_roxctl-deployment"></a>

## Available commands

Available commands for the `roxctl deployment` command.

| Command | Description |
|----|----|
| `check` | Check the deployments for violations of the deployment time policy. |

<a id="roxctl-deployment-options_roxctl-deployment"></a>

## Options

Options for the `roxctl deployment` command.

| Option | Description |
|----|----|
| `-t`, `--timeout duration` | Set the timeout for API requests. This option represents the maximum duration of a request. The default value is `10m0s`. |

<a id="options-inherited-from-the-parent-command_roxctl-deployment"></a>

# roxctl deployment command options inherited from the parent command

The `roxctl deployment` command supports the following options inherited from the parent `roxctl` command:

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
> These options are applicable to all the sub-commands of the `roxctl deployment` command.

<a id="roxctl-deployment-check_roxctl-deployment"></a>

# roxctl deployment check

Check deployments for violations of the deployment time policy.

<a id="roxctl-deployment-check-usage_roxctl-deployment"></a>

## roxctl deployment check usage

Usage syntax for the `roxctl deployment check` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl deployment check [flags]
```

</div>

<a id="roxctl-deployment-check-options_roxctl-deployment"></a>

## Options

Options for the `roxctl deployment check` command.

| Option | Description |
|----|----|
| `-c`, `--categories strings` | Define the policy categories to run. By default, the command runs all policy categories. |
| `--cluster string` | Set the cluster name or ID that you want to use as the context for the evaluation to enable extended deployments with cluster-specific information. |
| `--compact-output` | Print the JSON output in compact form. The default value is `false`. |
| `-f`, `--file stringArray` | Specify the YAML files to send to Central for policy evaluation. |
| `--force` | Bypass the Central cache for images and force a new pull from Scanner. The default value is `false`. |
| `--headers strings` | Define headers that you want to print in the tabular output. The default values include `POLICY`, `SEVERITY`, `BREAKS DEPLOY`, `DEPLOYMENT`, `DESCRIPTION`, `VIOLATION`, and `REMEDIATION`. |
| `--headers-as-comments` | Print headers as comments in the CSV tabular output. The default value is `false`. |
| `--junit-suite-name string` | Set the name of the JUnit test suite. The default value is `deployment-check`. |
| `--merge-output` | Merge duplicate cells in the tabular output. The default value is `false`. |
| `-n`, `--namespace string` | Specify a namespace to enhance deployments with context information such as network policies, role-based access controls (RBACs), and services for deployments that do not have a namespace in their specification. The namespace defined in the specification is not changed. The default value is `default`. |
| `--no-header` | Do not print headers for a tabular output. The default value is `false`. |
| `-o`, `--output string` | Choose the output format. Output formats include `json`, `junit`, `sarif`, `table`, and `csv`. The default value is `table`. |
| `-r`, `--retries int` | Set the number of retries before exiting as an error. The default value is `3`. |
| `-d`, `--retry-delay int` | Set the time to wait between retries in seconds. The default value is `3`. |
| `--row-jsonpath-expressions string` | Define the JSON path expressions to create a row from the JSON object. For more details, run the `roxctl deployment check --help` command. |
