<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl image` command to run operations on container images, including scanning for vulnerabilities, checking for policy violations, and generating Software Bill of Materials (SBOM) reports. This reference covers the command syntax, available subcommands, and configuration options.

<a id="roxctl-image-overview_roxctl-image"></a>

# roxctl image

Commands that you can run on a specific image.

<a id="roxctl-image-usage_roxctl-image"></a>

## roxctl image usage

Usage syntax for the `roxctl image` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl image [command] [flags]
```

</div>

<a id="roxctl-image-available-commands_roxctl-image"></a>

## Available commands

Available commands for the `roxctl image` command.

| Command | Description |
|----|----|
| `check` | Check images for build time policy violations, and report them. |
| `sbom` | Generate an SPDX 2.3 SBOM from an image scan. You must have write permissions for the `Image` resource. |
| `scan` | Scan the specified image, and return the scan results. |

<a id="roxctl-image-options_roxctl-image"></a>

## Options

Options for the `roxctl image` command.

| Option | Description |
|----|----|
| `-t`, `--timeout duration` | Set the timeout for API requests representing the maximum duration of a request. The default value is `10m0s`. |

<a id="options-inherited-from-the-parent-command_roxctl-image"></a>

# roxctl image command options inherited from the parent command

The `roxctl image` command supports the following options inherited from the parent `roxctl` command:

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
> These options are applicable to all the sub-commands of the `roxctl image` command.

<a id="roxctl-image-sbom_roxctl-image"></a>

# roxctl image sbom

Generate an SPDX 2.3 SBOM from an image scan. You must have write permissions for the `Image` resource.

<a id="roxctl-image-sbom-usage_roxctl-image"></a>

## roxctl image sbom usage

Usage syntax for the `roxctl image sbom` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl image sbom [flags]
```

</div>

<a id="roxctl-image-sbom-options_roxctl-image"></a>

## Options

Options for the `roxctl image sbom` command.

| Option | Description |
|----|----|
| `--cluster` string | Cluster name or ID that you want to delegate the image scan to. |
| `--namespace` string | Namespace on the secured cluster from which to read context information when delegating image scans, specifically pull secrets for accessing the image registry. |
| `-f, --force` | Bypass Central’s cache for the image and force a new pull from the scanner. The default is `false`. |
| `-d, --retry-delay integer` | Sets the time to wait between retries in seconds. The default is 3. |
| `-i, --image string` | Image name and reference, for example, `nginx:latest` or `nginx@sha256:…​`. |
| `-r, --retries integer` | Sets the number of times that Scanner V4 should retry before exiting with an error. The default is 3. |

Options

<a id="roxctl-image-scan_roxctl-image"></a>

# roxctl image scan

Scan the specified image, and return the scan results.

<a id="roxctl-image-scan-usage_roxctl-image"></a>

## roxctl image scan usage

Usage syntax for the `roxctl image scan` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl image scan [flags]
```

</div>

<a id="roxctl-image-scan-options_roxctl-image"></a>

## Options

Options for the `roxctl image scan` command.

| Option | Description |
|----|----|
| `--cluster string` | Specify the cluster name or ID to which you want to delegate the image scan. |
| `--compact-output` | Print JSON output in a compact format. The default value is `false`. |
| `--fail` | Fail if the scan finds vulnerabilities. The default value is `false`. |
| `-f`, `--force` | Ignore Central’s cache and force a fresh re-pull from Scanner. The default value is `false`. |
| `--headers strings` | Specify the headers to print in a tabular output. The default values include `COMPONENT`, `VERSION`,`CVE`,`SEVERITY`, and `LINK`. |
| `--headers-as-comments` | Print headers as comments in a CSV tabular output. The default value is `false`. |
| `-i`, `--image string` | Specify the image name and reference to scan. For example, `nginx:latest` or `nginx@sha256:…​`. |
| `-a`, `--include-snoozed` | Include snoozed and unsnoozed CVEs in the scan results. The default value is `false`. |
| `--merge-output` | Merge duplicate cells in a tabular output. The default value is `true`. |
| `--namespace` | Specify a namespace on the secured cluster from which to read context information, specifically pull secrets to access the image registry, when delegating image scans. |
| `--no-header` | Do not print headers for a tabular output. The default value is `false`. |
| `-o`, `--output string` | Specify the output format. Output formats include `table`, `csv`, `json`, and `sarif`. |
| `-r`, `--retries int` | Specify the number of retries before exiting as an error. The default value is `3`. |
| `-d`, `--retry-delay int` | Set the time to wait between retries in seconds. The default value is `3`. |
| `--row-jsonpath-expressions string` | Specify JSON path expressions to create a row from the JSON object. For more details, run the `roxctl image scan --help` command. |
| `--severity strings` | List of severities to include in the output. Use this to filter for specific severities. The default values include `LOW`, `MODERATE`, `IMPORTANT`, and `CRITICAL`. |

Options

<a id="roxctl-image-check_roxctl-image"></a>

# roxctl image check

Check images for build time policy violations, and report them.

<a id="roxctl-image-check-usage_roxctl-image"></a>

## roxctl image check usage

Usage syntax for the `roxctl image check` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl image check [flags]
```

</div>

<a id="roxctl-image-check-options_roxctl-image"></a>

## Options

Options for the `roxctl image check` command.

| Option | Description |
|----|----|
| `-c`, `--categories strings` | List of the policy categories that you want to run. By default, the command uses all policy categories. |
| `--cluster string` | Define the cluster name or ID that you want to use as the context for evaluation. |
| `--compact-output` | Print JSON output in a compact format. The default value is `false`. |
| `-f`, `--force` | Bypass the Central cache for the image and force a new pull from the Scanner. The default value is `false`. |
| `--headers strings` | Define headers to print in a tabular output. The default values include `POLICY`, `SEVERITY`, `BREAKS BUILD`, `DESCRIPTION`, `VIOLATION`, and `REMEDIATION`. |
| `--headers-as-comments` | Print headers as comments in a CSV tabular output. The default value is `false`. |
| `-i`, `--image string` | Specify the image name and reference. For example, `nginx:latest` or `nginx@sha256:…​)`. |
| `--junit-suite-name string` | Set the name of the JUnit test suite. Default value is `image-check`. |
| `--merge-output` | Merge duplicate cells in a tabular output. The default value is `false`. |
| `--namespace` | Specify a namespace on the secured cluster from which to read context information, specifically pull secrets to access the image registry, when delegating image scans. |
| `--no-header` | Do not print headers for a tabular output. The default value is `false`. |
| `-o`, `--output string` | Choose the output format. Output formats include `junit`, `sarif`, `table`, `csv`, and `json`. The default value is `table`. |
| `-r`, `--retries int` | Set the number of retries before exiting as an error. The default value is `3`. |
| `-d`, `--retry-delay int` | Set the time to wait between retries in seconds. The default value is `3`. |
| `--row-jsonpath-expressions string` | Create a row from the JSON object by using JSON path expression. For more details, run the `roxctl image check --help` command. |
| `--send-notifications` | Define whether you want to send notifications if violations occur. The default value is `false`. |

Options
