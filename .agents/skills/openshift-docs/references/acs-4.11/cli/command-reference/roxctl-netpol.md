<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl netpol` command to manage network policies, analyze connectivity, and generate network policy recommendations based on deployment information.

<a id="roxctl-netpol-overview_roxctl-netpol"></a>

# roxctl netpol

Commands related to the network policies.

<a id="roxctl-netpol-usage_roxctl-netpol"></a>

## roxctl netpol usage

Usage syntax for the `roxctl netpol` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl netpol [command] [flags]
```

</div>

<a id="roxctl-netpol-available-commands_roxctl-netpol"></a>

## Available commands

Available commands for the `roxctl netpol` command.

| Command | Description |
|----|----|
| `connectivity` | Connectivity analysis of the network policy resources. |
| `generate` | Recommend network policies based on the deployment information. |

<a id="options-inherited-from-the-parent-command_roxctl-netpol"></a>

# roxctl netpol command options inherited from the parent command

The `roxctl netpol` command supports the following options inherited from the parent `roxctl` command:

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
> These options are applicable to all the sub-commands of the `roxctl netpol` command.

<a id="roxctl-netpol-generate_roxctl-netpol"></a>

# roxctl netpol generate

Recommend network policies based on the deployment information.

If you do not specify a port, the `roxctl netpol generate` command uses port `53` for DNS connections.

If you are using OpenShift Container Platform, you might need to change the port when generating network policies by using the `roxctl` CLI. If you do not change the port, OpenShift Container Platform uses port `5353` and assigns the name `dns` for this port automatically. You can use the `--dnsport` option to override the default DNS port. For example:

- `roxctl netpol generate --dnsport 5353 <other_options>`

- `roxctl netpol generate --dnsport dns <other-options>`.

<a id="roxctl-netpol-generate-usage_roxctl-netpol"></a>

## roxctl netpol generate usage

Usage syntax for the `roxctl netpol generate` command.

Enter the following command:

``` terminal
$ roxctl netpol generate <folder_path> [flags]
```

where:

`<folder_path>`  
Specifies the path to the directory containing your Kubernetes deployment and service configuration files.

<a id="roxctl-netpol-generate-options_roxctl-netpol"></a>

## Options

Options for the `roxctl netpol generate` command.

The following options are available:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Option</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>--dnsport &lt;int_or_string&gt;</code></p></td>
<td style="text-align: left;"><p>Specify the DNS port or a named port that you want to use in the egress rules of synthesized network policies. For example:</p>
<ul>
<li><p><code>roxctl netpol generate --dnsport 5353 &lt;other_options&gt;</code></p></li>
<li><p><code>roxctl netpol generate --dnsport foo-dns &lt;other_options&gt;</code>.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--fail</code></p></td>
<td style="text-align: left;"><p>Fail on the first encountered error. The default value is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-d</code>, <code>--output-dir string</code></p></td>
<td style="text-align: left;"><p>Save generated policies into the target folder.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-f</code>, <code>--output-file string</code></p></td>
<td style="text-align: left;"><p>Save and merge generated policies into a single YAML file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--remove</code></p></td>
<td style="text-align: left;"><p>Remove the output path if it already exists. The default value is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--strict</code></p></td>
<td style="text-align: left;"><p>Treat warnings as errors. The default value is <code>false</code>.</p></td>
</tr>
</tbody>
</table>

<a id="roxctl-netpol-connectivity_roxctl-netpol"></a>

# roxctl netpol connectivity

Commands related to the connectivity analysis of the network policy resources.

<a id="roxctl-netpol-connectivity-usage_roxctl-netpol"></a>

## roxctl netpol connectivity usage

Usage syntax for the `roxctl netpol connectivity` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl netpol connectivity [flags]
```

</div>

<a id="roxctl-netpol-connectivity-map_roxctl-netpol"></a>

## roxctl netpol connectivity map

You can create a connectivity map by using the `netpol` command to analyze connectivity based on the network policies and other resources.

<a id="roxctl-netpol-connectivity-map-usage_roxctl-netpol"></a>

### roxctl netpol connectivity map usage

Usage syntax for the `roxctl netpol connectivity map` command.

Enter the following command:

``` terminal
$ roxctl netpol connectivity map <folder_path> [flags]
```

where:

`<folder_path>`  
Specifies the path to the directory containing your Kubernetes deployment and service configuration files.

<a id="roxctl-netpol-connectivity-map-options_roxctl-netpol"></a>

### Options

Options for the `roxctl netpol connectivity map` command.

The following options are available:

| Option | Description |
|----|----|
| `--explain` | Enhance the analysis of permitted connectivity with explanations per denied/allowed connection; supported only for txt output format. |
| `--exposure` | Enhance the analysis of permitted connectivity by using exposure analysis. The default value is `false`. |
| `--fail` | Fail on the first encountered error. The default value is `false`. |
| `--focus-workload string` | Focus on connections of the specified workload name in the output. |
| `-f`, `--output-file string` | Save the connections list output into a specific file. |
| `-h`, `--help` | View the help text for the `roxctl netpol connectivity map` command. |
| `-o`, `--output-format string` | Configure the connections list in a specific format. Supported formats include `txt`, `json`, `md`, `dot`, and `csv`. The default value is `txt`. |
| `--remove` | Remove the output path if it already exists. The default value is `false`. |
| `--save-to-file` | Define whether you want to save the output of the connection list in the default file. The default value is `false`. |
| `--strict` | Treat warnings as errors. The default value is `false`. |

<a id="roxctl-netpol-connectivity-diff_roxctl-netpol"></a>

## roxctl netpol connectivity diff

You can report connectivity differences based on two network policy directories and YAML manifests with workload resources.

<a id="roxctl-netpol-connectivity-diff-usage_roxctl-netpol"></a>

### roxctl netpol connectivity diff usage

Usage syntax for the `roxctl netpol connectivity diff` command.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ roxctl netpol connectivity diff [flags]
```

</div>

<a id="roxctl-netpol-connectivity-diff-options_roxctl-netpol"></a>

### Options

Options for the `roxctl netpol connectivity diff` command.

| Option | Description |
|----|----|
| `--dir1 string` | Specify the first directory path of the input resources. This value is mandatory. |
| `--dir2 string` | Specify the second directory path of the input resources that you want to compare with the first directory path. This value is mandatory. |
| `--fail` | Fail on the first encounter. The default value is `false`. |
| `-f`, `--output-file string` | Save the output of the connectivity difference command into a specific file. |
| `-o`, `--output-format string` | Configure the output of the connectivity difference command in a specific format. Supported formats include `txt`, `md`, `csv`. The default value is `txt`.. |
| `--remove` | Remove the output path if it already exists. The default value is `false`. |
| `--save-to-file` | Define whether you want to store the output of the connectivity differences in the default file. The default value is `false`. |
| `--strict` | Treat warnings as errors. The default value is `false`. |
