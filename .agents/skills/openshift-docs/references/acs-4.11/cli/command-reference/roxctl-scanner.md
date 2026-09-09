<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl scanner` command to manage StackRox Scanner and Scanner V4 services, including generating deployment configurations, downloading vulnerability databases, and uploading database files.

<a id="roxctl-scanner-overview_roxctl-scanner"></a>

# roxctl scanner

Commands related to the StackRox Scanner and Scanner V4 services.

<a id="roxctl-scanner-usage_roxctl-scanner"></a>

## roxctl scanner usage

Usage syntax for the `roxctl scanner` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl scanner [command] [flags]
```

</div>

<a id="roxctl-scanner-available-commands_roxctl-scanner"></a>

## Available commands

Available commands for the `roxctl scanner` command.

| Command | Description |
|----|----|
| `download-db` | Download the offline vulnerability database for StackRox Scanner and Scanner V4. |
| `generate` | Generate the required YAML configuration files to deploy the StackRox Scanner and Scanner V4. |
| `upload-db` | Upload a vulnerability database for the StackRox Scanner and Scanner V4. |

<a id="options-inherited-from-the-parent-command_roxctl-scanner"></a>

# roxctl scanner command options inherited from the parent command

The `roxctl scanner` command supports the following options inherited from the parent `roxctl` command:

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
> These options are applicable to all the sub-commands of the `roxctl scanner` command.

<a id="roxctl-scanner-generate_roxctl-scanner"></a>

# roxctl scanner generate

Generate the required YAML configuration files to deploy Scanner.

<a id="roxctl-scanner-generate-usage_roxctl-scanner"></a>

## roxctl scanner generate usage

Usage syntax for the `roxctl scanner generate` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl scanner generate [flags]
```

</div>

<a id="roxctl-scanner-generate-options_roxctl-scanner"></a>

## Options

Options for the `roxctl scanner generate` command.

| Option | Description |
|----|----|
| `--cluster-type cluster type` | Specify the type of cluster on which you want to run Scanner. Cluster types include `k8s` and `openshift`. The default value is `k8s`. |
| `--enable-pod-security-policies` | Create `PodSecurityPolicy` resources. The default value is `true`. |
| `--istio-support string` | Generate deployment files that support the specified Istio version. Valid versions include `1.0`, `1.1`, `1.2`, `1.3`, `1.4`, `1.5`, `1.6`, and `1.7`. |
| `--output-dir string` | Specify the output directory for the Scanner bundle. Leave blank to use the default value. |
| `--retry-timeout duration` | Set the timeout after which the system retries API requests. A value of zero means that the system waits for the entire request duration without retrying. The default value is `20s`. |
| `--scanner-image string` | Specify the Scanner image that you want to use. Leave blank to use the server default. |
| `-t`, `--timeout duration` | Set the timeout for API requests representing the maximum duration of a request. The default value is `1m0s`. |

Options

<a id="roxctl-scanner-upload-db_roxctl-scanner"></a>

# roxctl scanner upload-db

Upload a vulnerability database for Scanner.

<a id="roxctl-scanner-upload-db-usage_roxctl-scanner"></a>

## roxctl scanner upload-db usage

Usage syntax for the `roxctl scanner upload-db` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl scanner upload-db [flags]
```

</div>

<a id="roxctl-scanner-upload-db-options_roxctl-scanner"></a>

## Options

Options for the `roxctl scanner upload-db` command.

| Option | Description |
|----|----|
| `--scanner-db-file string` | Specify the file containing the dumped Scanner definitions DB. |
| `-t`, `--timeout duration` | Set the timeout for API requests representing the maximum duration of a request. The default value is `10m0s`. |

Options

<a id="roxctl-scanner-download-db_roxctl-scanner"></a>

# roxctl scanner download-db

Download the offline vulnerability database for StackRox Scanner or Scanner V4.

This command downloads version-specific offline vulnerability bundles. The system contacts Central to determine the version if one is not specified. If communication fails, the download defaults to the version embedded within `roxctl`.

By default, it will attempt to download the database for the determined version and less-specific variants. For example, if you specify version `4.4.1-extra`, the command attempts downloads for the following version variants:

- 4.4.1-extra

- 4.4.1

- 4.4

<a id="roxctl-scanner-download-db-usage_roxctl-scanner"></a>

## roxctl scanner download-db usage

Usage syntax for the `roxctl scanner download-db` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl scanner download-db [flags]
```

</div>

<a id="roxctl-scanner-download-db-options_roxctl-scanner"></a>

## Options

Options for the `roxctl scanner download-db` command.

| Option | Description |
|----|----|
| `--force` | Force overwriting the output file if it already exists. The default value is `false`. |
| `--scanner-db-file string` | Output file to save the vulnerability database to. The default value is the name and path of the remote file that you download. |
| `--skip-central` | Do not contact Central when detecting the version. The default value is `false`. |
| `--skip-variants` | Do not attempt to process variants of the determined version. The default value is `false`. |
| `-t`, `--timeout duration` | Set the timeout for API requests representing the maximum duration of a request. The default value is `10m0s`. |
| `--version string` | Download a specific version or version variant of the vulnerability database. By default, the version is automatically detected. |

Options
