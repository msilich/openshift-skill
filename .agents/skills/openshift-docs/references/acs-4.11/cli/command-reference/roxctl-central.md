<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Commands related to the Central service.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central [command] [flags]
```

</div>

| Command | Description |
|----|----|
| `backup` | Create a backup of the Red Hat Advanced Cluster Security for Kubernetes (RHACS) database and the certificates. |
| `cert` | Download the certificate chain for the Central service. |
| `crs` | Generate a cluster registration secret (CRS) that allows communication between Central and secured clusters for the initial setup, to retrieve a list of CRSes, or to revoke a CRS. |
| `db` | Control the database operations. |
| `debug` | Debug the Central service. |
| `generate` | Generate the required YAML configuration files containing the orchestrator objects for the deployment of Central. |
| `init-bundles` | Initialize bundles for Central. |
| `login` | Log in to the Central instance to obtain a token. |
| `userpki` | Manage the user certificate authorization providers. |
| `whoami` | Display information about the current user and their authentication method. |

Available commands

<a id="options-inherited-from-the-parent-command_roxctl-central"></a>

# roxctl central command options inherited from the parent command

The `roxctl central` command supports the following options inherited from the parent `roxctl` command:

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
> These options are applicable to all the sub-commands of the `roxctl central` command.

<a id="roxctl-central-backup_roxctl-central"></a>

# roxctl central backup

Create a backup of the RHACS database and certificates.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central backup [flags]
```

</div>

<table>
<caption>Options</caption>
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
<td style="text-align: left;"><p><code>--certs-only</code></p></td>
<td style="text-align: left;"><p>Specify to only back up the certificates. When using an external database, this option is used to generate a backup bundle with certificates. The default value is <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--output string</code></p></td>
<td style="text-align: left;"><p>Specify where you want to save the backup. The behavior depends on the specified path:</p>
<ul>
<li><p>If the path is a file path, the backup is written to the file and overwrites it if it already exists. The directory must exist.</p></li>
<li><p>If the path is a directory, the backup is saved in this directory under the file name that the server specifies.</p></li>
<li><p>If this argument is omitted, the backup is saved in the current working directory under the file name that the server specifies.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-t</code>, <code>--timeout duration</code></p></td>
<td style="text-align: left;"><p>Specify the timeout for API requests. It represents the maximum duration of a request. The default value is <code>1h0m0s</code>.</p></td>
</tr>
</tbody>
</table>

<a id="roxctl-central-cert_roxctl-central"></a>

# roxctl central cert

Download the certificate chain for the Central service.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central cert [flags]
```

</div>

| Option | Description |
|----|----|
| `--output string` | Specify the file name to which you want to save the PEM certificate. Use `-` to produce output to the standard output stream (`stdout`). The default value is `-`. |
| `--retry-timeout duration` | Specify the timeout after which API requests are retried. A value of zero means that the entire request duration is waited for without retrying. The default value is `20s`. |
| `-t`, `--timeout duration` | Specify the timeout for API requests representing the maximum duration of a request. The default value is `1m0s`. |

Options

<a id="roxctl-central-crs_roxctl-central"></a>

# roxctl central crs

Manage cluster registration secrets that allow communication between Central and secured clusters for the initial setup.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central crs [command] [flags]
```

</div>

For available flags, see "roxctl central command options inherited from the parent command".

<a id="roxctl-central-crs-generate_roxctl-central"></a>

## roxctl central crs generate

Generate a cluster registration secret (CRS) that allows communication between Central and secured clusters for the initial setup.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central crs generate <crs name> [flags]
```

</div>

| Flag | Description |
|----|----|
| -o, --output | File to be used for storing the newly generated CRS. Use `-` for `stdout`. |
| --valid-for | Specify the validity duration for the new CRS, for example, `10m`, `1d`. |
| --valid-until | Specify the validity as an RFC 3339 timestamp for the new CRS. |

Flags

If you do not specify the validity for the new CRS, `24h` is selected as a default value.

For information about additional flags, see "roxctl central command options inherited from the parent command".

<a id="roxctl-central-crs-list_roxctl-central"></a>

## roxctl central crs list

Generate a list of previously generated cluster registration secrets that allow communication between Central and secured clusters for the initial setup.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central crs list [flags]
```

</div>

For available flags, see "roxctl central command options inherited from the parent command".

<a id="roxctl-central-crs-revoke_roxctl-central"></a>

## roxctl central crs revoke

Revoke a cluster registration secret (CRS) that allows communication between Central and secured clusters for the initial setup.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central crs revoke <CRS unique identifier or name> [flags]
```

</div>

For available flags, see "roxctl central command options inherited from the parent command".

<a id="roxctl-central-login_roxctl-central"></a>

# roxctl central login

Login to the Central instance to obtain a token.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central login [flags]
```

</div>

| Option | Description |
|----|----|
| `-t`, `--timeout duration` | Specify the timeout for API requests representing the maximum duration of a request. The default value is `5m0s`. |

Options

<a id="roxctl-central-whoami_roxctl-central"></a>

# roxctl central whoami

Display information about the current user and their authentication method.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central whoami [flags]
```

</div>

| Option | Description |
|----|----|
| `--retry-timeout duration` | Specify the timeout after which API requests are retried. A value of zero means that the entire request duration is waited for without retrying. The default value is `20s`. |
| `-t`, `--timeout duration` | Specify the timeout for API requests representing the maximum duration of a request. The default value is `1m0s`. |

Options

<a id="roxctl-central-db_roxctl-central"></a>

# roxctl central db

Control the database operations.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central db [flags]
```

</div>

| Option | Description |
|----|----|
| `-t`, `--timeout duration` | Specify the timeout for API requests representing the maximum duration of a request. The default value is `1h0m0s`. |

Options

<a id="roxctl-central-db-restore_roxctl-central"></a>

## roxctl central db restore

Restore the RHACS database from a previous backup.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central db restore <file> [flags]
```

</div>

where:

`<file>`  
Specifies the database backup file that you want to restore.

| Option | Description |
|----|----|
| `-f`, `--force` | If set to `true`, the restoration is performed without confirmation. The default value is `false`. |
| `--interrupt` | If set to `true`, it interrupts the running restore process to allow it to continue. The default value is `false`. |

Options

<a id="roxctl-central-db-generate_roxctl-central"></a>

## roxctl central db generate

Generate a Central database bundle.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central db generate [flags]
```

</div>

| Option | Description |
|----|----|
| `--debug` | If set to `true`, templates are read from the local file system. The default value is `false`. |
| `--debug-path string` | Specify the path to the Helm templates in your local file system. For more details, run the `roxctl central db generate` command. |
| `--enable-pod-security-policies` | If set to `true`, `PodSecurityPolicy` resources are created. The default value is `true`. |

Options

<a id="roxctl-central-db-generate-k8s_roxctl-central"></a>

## roxctl central db generate k8s

Generate Kubernetes YAML files for deploying Central’s database components.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central db generate k8s [flags]
```

</div>

| Option | Description |
|----|----|
| `--central-db-image string` | Specify the Central database image that you want to use. If not specified, a default value corresponding to the `--image-defaults` is used. |
| `--image-defaults string` | Specify the default settings for container images. It controls the repositories from which the images are downloaded, the image names and the format of the tags. The default value is `development_build`. |
| `--output-dir output directory` | Specify the directory to which you want to save the deployment bundle. The default value is `central-db-bundle`. |

Options

<a id="roxctl-central-db-restore-cancel_roxctl-central"></a>

## roxctl central db restore cancel

Cancel the ongoing Central database restore process.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central db restore cancel [flags]
```

</div>

| Option | Description |
|----|----|
| `f`, `--force` | If set to `true`, proceed with the cancellation without confirmation. The default value is `false`. |

Options

<a id="roxctl-central-db-restore-status_roxctl-central"></a>

## roxctl central db restore status

Display information about the ongoing database restore process.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central db restore status [flags]
```

</div>

<a id="roxctl-central-db-generate-k8s-pvc_roxctl-central"></a>

## roxctl central db generate k8s pvc

Generate Kubernetes YAML files for persistent volume claims (PVCs) in Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central db generate k8s pvc [flags]
```

</div>

| Option | Description |
|----|----|
| `--name string` | Specify the external volume name for the Central database. The default value is `central-db`. |
| `--size uint32` | Specify the external volume size in gigabytes for the Central database. The default value is `100`. |
| `--storage-class string` | Specify the storage class name for the Central database. This is optional if you have a default storage class configured. |

Options

<a id="roxctl-central-db-generate-openshift_roxctl-central"></a>

## roxctl central db generate openshift

Generate an OpenShift YAML manifest for deploying a Central database instance on a Red Hat OpenShift cluster.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central db generate openshift [flags]
```

</div>

| Option | Description |
|----|----|
| `--central-db-image string` | Specify the Central database image that you want to use. If not specified, a default value corresponding to the `--image-defaults` is used. |
| `--image-defaults string` | Specify the default settings for container images. It controls the repositories from which the images are downloaded, the image names and the format of the tags. The default value is `development_build`. |
| `--openshift-version int` | Specify the Red Hat OpenShift major version 3 or 4 for the deployment. The default value is `3`. |
| `--output-dir output-directory` | Specify the directory to which you want to save the deployment bundle. The default value is `central-db-bundle`. |

Options

<a id="roxctl-central-db-generate-k8s-hostpath_roxctl-central"></a>

## roxctl central db generate k8s hostpath

Generate a Kubernetes YAML manifest for a database deployment with a hostpath volume type in Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central db generate k8s hostpath [flags]
```

</div>

| Option | Description |
|----|----|
| `--hostpath string` | Specify the path on the host. The default value is `/var/lib/stackrox-central-db`. |
| `--node-selector-key string` | Specify the node selector key. Valid values include `kubernetes.io` and `hostname`. |
| `--node-selector-value string` | Specify the node selector value. |

Options

<a id="roxctl-central-db-generate-openshift-pvc_roxctl-central"></a>

## roxctl central db generate openshift pvc

Generate an OpenShift YAML manifest for a database deployment with a persistent volume claim (PVC) in Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central db generate openshift pvc [flags]
```

</div>

| Option | Description |
|----|----|
| --name string | Specify the external volume name for the Central database. The default value is `central-db`. |
| --size uint32 | Specify the external volume size in gigabytes for the Central database. The default value is `100`. |
| --storage-class string | Specify the storage class name for the Central database. This is optional if you have a default storage class configured. |

Options

<a id="roxctl-central-db-generate-openshift-hostpath_roxctl-central"></a>

## roxctl central db generate openshift hostpath

Add a hostpath external volume to the Central database.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central db generate openshift hostpath [flags]
```

</div>

| Option | Description |
|----|----|
| `--hostpath string` | Specify the path on the host. The default value is `/var/lib/stackrox-central-db`. |
| `--node-selector-key string` | Specify the node selector key. Valid values include `kubernetes.io` and `hostname`. |
| `--node-selector-value string` | Specify the node selector value. |

Options

<a id="roxctl-central-debug_roxctl-central"></a>

# roxctl central debug

Debug the Central service.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central debug [flags]
```

</div>

<a id="roxctl-central-debug-db_roxctl-central"></a>

## roxctl central debug db

Control the debugging of the database.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central debug db [flags]
```

</div>

| Option | Description |
|----|----|
| `-t`, `--timeout duration` | Specify the timeout for API requests representing the maximum duration of a request. The default value is `1m0s`. |

Options

<a id="roxctl-central-debug-log_roxctl-central"></a>

## roxctl central debug log

Retrieve the current log level.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central debug log [flags]
```

</div>

| Option | Description |
|----|----|
| `-l`, `--level string` | Specify the log level to which you want to set the modules. Valid values include `Debug`, `Info`, `Warn`, `Error`, `Panic`, and `Fatal`. |
| `-m`, `--modules strings` | Specify the modules to which you want to apply the command. |
| `--retry-timeout duration` | Specify the timeout after which API requests are retried. A value of zero means that the entire request duration is waited for without retrying. The default value is `20s`. |
| `-t`, `--timeout duration` | Specify the timeout for API requests, which is the maximum duration of a request. The default value is `1m0s`. |

Options

<a id="roxctl-central-debug-dump_roxctl-central"></a>

## roxctl central debug dump

Download a bundle containing the debug information for Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central debug dump [flags]
```

</div>

| Option | Description |
|----|----|
| `--logs` | If set to `true`, logs are included in the Central dump. The default value is `false`. |
| `--output-dir string` | Specify the output directory for the bundle content. The default value is an automatically generated directory name within the current directory. |
| `-t`, `--timeout duration` | Specify the timeout for API requests, which is the maximum duration of a request. The default value is `5m0s`. |

Options

<a id="roxctl-central-debug-db-stats_roxctl-central"></a>

## roxctl central debug db stats

Control the statistics of the Central database.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central debug db stats [flags]
```

</div>

<a id="roxctl-central-debug-authz-trace_roxctl-central"></a>

## roxctl central debug authz-trace

Enable or disable authorization tracing in Central for debugging purposes.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central debug authz-trace [flags]
```

</div>

| Option | Description |
|----|----|
| `-t`, `--timeout duration` | Specify the timeout for API requests representing the maximum duration of a request. The default value is `20m0s`. |

Options

<a id="roxctl-central-debug-db-stats-reset_roxctl-central"></a>

## roxctl central debug db stats reset

Reset the statistics of the Central database.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central debug db stats reset [flags]
```

</div>

<a id="roxctl-central-debug-download-diagnostics_roxctl-central"></a>

## roxctl central debug download-diagnostics

Download a bundle containing a snapshot of diagnostic information about the platform.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central debug download-diagnostics [flags]
```

</div>

| Option | Description |
|----|----|
| `--clusters strings` | Specify a comma-separated list of the Sensor clusters from which you want to collect the logs. |
| `--output-dir string` | Specify the output directory in which you want to save the diagnostic bundle. |
| `--since string` | Specify the timestamp from which you want to collect the logs from the Sensor clusters. |
| `-t`, `--timeout duration` | Specify the timeout for API requests, which specifies the maximum duration of a request. The default value is `5m0s`. |

Options

<a id="roxctl-central-generate_roxctl-central"></a>

# roxctl central generate

Generate the required YAML configuration files that contain the orchestrator objects to deploy Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central generate [flags]
```

</div>

| Option | Description |
|----|----|
| `--backup-bundle string` | Specify the path to the backup bundle from which you want to restore the keys and certificates. |
| `--debug` | If set to `true`, templates are read from the local file system. The default value is `false`. |
| `--debug-path string` | Specify the path to Helm templates on your local file system. For more details, run the `roxctl central generate --help` command. |
| `--default-tls-certfile` | Specify the PEM certificate bundle file that you want to use as the default. |
| `--default-tls-keyfile` | Specify the PEM private key file that you want to use as the default. |
| `--enable-pod-security-policies` | If set to `true`, `PodSecurityPolicy` resources are created. The default value is `true`. |
| `-p`, `--password string` | Specify the administrator password. The default value is automatically generated. |
| `--plaintext-endpoints string` | Specify the ports or endpoints you want to use for unencrypted exposure as a comma-separated list. |

Options

<a id="roxctl-central-generate-k8s_roxctl-central"></a>

## roxctl central generate k8s

Generate the required YAML configuration files to deploy Central into a Kubernetes cluster.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central generate k8s [flags]
```

</div>

| Option | Description |
|----|----|
| `--central-db-image string` | Specify the Central database image you want to use. If not specified, a default value corresponding to the `--image-defaults` is used. |
| `--declarative-config-config-maps strings` | Specify a list of configuration maps that you want to add as declarative configuration mounts in Central. |
| `--declarative-config-secrets strings` | Specify a list of secrets that you want to add as declarative configuration mounts in Central. |
| `--enable-telemetry` | Specify whether you want to enable telemetry. The default value is `false`. |
| `--image-defaults string` | Specify the default settings for container images. The specified settings control the repositories from which the images are downloaded, the image names and the format of the tags. The default value is `development_build`. |
| `--istio-support version` | Generate deployment files that support the specified Istio version. Valid values include `1.0`, `1.1`, `1.2`, `1.3`, `1.4`, `1.5`, `1.6`, and `1.7`. |
| `--lb-type load balancer type` | Specify the method in which you want to suspend Central. Valid values include `lb`, `np` and `none`. The default value is `none`. |
| `-i`, `--main-image string` | Specify the main image that you want to use. If not specified, a default value corresponding to the `--image-defaults` is used. |
| `--offline` | Specify whether you want to run RHACS in offline mode, avoiding a connection to the Internet. The default value is `false`. |
| `--output-dir output directory` | Specify the directory to which you want to save the deployment bundle. The default value is `central-bundle`. |
| `--output-format output format` | Specify the deployment tool that you want to use. Valid values include `kubectl`, `helm`, and `helm-values`. The default value is `kubectl`. |
| `--scanner-db-image string` | Specify the Scanner database image that you want to use. If not specified, a default value corresponding to the `--image-defaults` is used. |
| `--scanner-image string` | Specify the Scanner image that you want to use. If not specified, a default value corresponding to the \`--image-defaults" is used. |

Options

<a id="roxctl-central-generate-k8s-pvc_roxctl-central"></a>

## roxctl central generate k8s pvc

Generate Kubernetes YAML files for persistent volume claims (PVCs) in Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central generate k8s pvc [flags]
```

</div>

| Option | Description |
|----|----|
| `--db-name string` | Specify the external volume name for the Central database. The default value is `central-db`. |
| `--db-size uint32` | Specify the external volume size in gigabytes for the Central database. The default value is `100`. |
| `--db-storage-class string` | Specify the storage class name for the Central database. This is optional if you have a default storage class configured. |

Options

<a id="roxctl-central-generate-openshift_roxctl-central"></a>

## roxctl central generate openshift

Generate the required YAML configuration files to deploy Central in a Red Hat OpenShift cluster.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central generate openshift [flags]
```

</div>

| Option | Description |
|----|----|
| `--central-db-image string` | Specify the Central database image that you want to use. If not specified, a default value is created corresponding to the `--image-defaults`. |
| `--declarative-config-config-maps strings` | Specify a list of configuration maps that you want to add as declarative configuration mounts in Central. |
| `--declarative-config-secrets strings` | Specify a list of secrets that you want to add as declarative configuration mounts in Central. |
| `--enable-telemetry` | Specify whether you want to enable telemetry. The default value is `false`. |
| `--image-defaults string` | Specify the default settings for container images. It controls the repositories from which the images are downloaded, the image names and the format of the tags. The default value is `development_build`. |
| `--istio-support version` | Generate deployment files that support the specified Istio version. Valid values include `1.0`, `1.1`, `1.2`, `1.3`, `1.4`, `1.5`, `1.6`, and `1.7`. |
| `--lb-type load balancer type` | Specify the method of exposing Central. Valid values include `route`, `lb`, `np` and `none`. The default value is `none`. |
| `-i`, `--main-image string` | Specify the main image that you want to use. If not specified, a default value corresponding to `--image-defaults` is used. |
| `--offline` | Specify whether you want to run RHACS in offline mode, avoiding a connection to the Internet. The default value is `false`. |
| `--openshift-monitoring false\|true\|auto[=true]` | Specify integration with Red Hat OpenShift 4 monitoring. The default value is `auto`. |
| `--openshift-version int` | Specify the Red Hat OpenShift major version 3 or 4 for the deployment. |
| `--output-dir output directory` | Specify the directory to which you want to save the deployment bundle. The default value is `central-bundle`. |
| `--output-format output format` | Specify the deployment tool that you want to use. Valid values include `kubectl`, `helm` and `helm-values`. The default value is `kubectl`. |
| `--scanner-db-image string` | Specify the Scanner database image that you want to use. If not specified, a default value corresponding to the `--image-defaults` is used. |
| `--scanner-image string` | Specify the Scanner image that you want to use. If not specified, a default value corresponding to `--image-defaults` is used. |

Options

<a id="roxctl-central-generate-interactive_roxctl-central"></a>

## roxctl central generate interactive

Generate interactive resources in Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central generate interactive [flags]
```

</div>

<a id="roxctl-central-generate-k8s-hostpath_roxctl-central"></a>

## roxctl central generate k8s hostpath

Generate a Kubernetes YAML manifest for deploying a Central instance by using the hostpath volume type.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central generate k8s hostpath [flags]
```

</div>

| Option | Description |
|----|----|
| `--db-hostpath string` | Specify the path on the host for the Central database. The default value is `/var/lib/stackrox-central`. |
| `--db-node-selector-key string` | Specify the node selector key for the Central database. Valid values include `kubernetes.io` and `hostname`. |
| `--db-node-selector-value string` | Specify the node selector value for the Central database. |

Options

<a id="roxctl-central-generate-openshift-pvc_roxctl-central"></a>

## roxctl central generate openshift pvc

Generate a OpenShift YAML manifest for deploying a persistent volume claim (PVC) in Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central generate openshift pvc [flags]
```

</div>

| Option | Description |
|----|----|
| `--db-name string` | Specify the external volume name for the Central database. The default value is `central-db`. |
| `--db-size uint32` | Specify the external volume size in gigabytes for the Central database. The default value is `100`. |
| `--db-storage-class string` | Specify the storage class name for the Central database. This is optional if you have a default storage class configured. |

Options

<a id="roxctl-central-generate-openshift-hostpath_roxctl-central"></a>

## roxctl central generate openshift hostpath

Add a hostpath external volume to the deployment definition in Red Hat OpenShift.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central generate openshift hostpath [flags]
```

</div>

| Option | Description |
|----|----|
| `--db-hostpath string` | Specify the path on the host for the Central database. The default value is `/var/lib/stackrox-central`. |
| `--db-node-selector-key string` | Specify the node selector key. Valid values include `kubernetes.io` and `hostname` for the Central database. |
| `--db-node-selector-value string` | Specify the node selector value for the Central database. |

Options

<a id="roxctl-central-init-bundles_roxctl-central"></a>

# roxctl central init-bundles

Initialize bundles in Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central init-bundles [flag]
```

</div>

| Option | Description |
|----|----|
| `--retry-timeout duration` | Specify the timeout after which API requests are retried. A value of `0s` means that the entire request duration is waited for without retrying. The default value is `20s`. |
| `-t`, `--timeout duration` | Specify the timeout for API requests representing the maximum duration of a request. The default value is `1m0s`. |

Options

<a id="roxctl-central-init-bundles-list_roxctl-central"></a>

## roxctl central init-bundles list

List the available initialization bundles in Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central init-bundles list [flags]
```

</div>

<a id="roxctl-central-init-bundles-revoke_roxctl-central"></a>

## roxctl central init-bundles revoke

Revoke one or more cluster initialization bundles in Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central init-bundles revoke <init_bundle_ID or name> [<init_bundle_ID or name> ...] [flags]
```

</div>

where:

`<init_bundle_ID or name>`  
Specifies the ID or the name of the initialization bundle that you want to revoke. You can provide multiple IDs or names separated by using spaces.

<a id="roxctl-central-init-bundles-fetch-ca_roxctl-central"></a>

## roxctl central init-bundles fetch-ca

Fetch the certificate authority (CA) bundle from Central.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central init-bundles fetch-ca [flags]
```

</div>

| Option | Description |
|----|----|
| `--output string` | Specify the file that you want to use for storing the CA configuration. |

Options

<a id="roxctl-central-init-bundles-generate_roxctl-central"></a>

## roxctl central init-bundles generate

Generate a new cluster initialization bundle.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central init-bundles generate <init_bundle_name> [flags]
```

</div>

where:

`<init_bundle_name>`  
Specifies the name for the initialization bundle you want to generate.

| Option | Description |
|----|----|
| `--output string` | Specify the file you want to use for storing the newly generated initialization bundle in the Helm configuration form. Use `-` to produce output to the standard output stream (`stdout`). |
| `--output-secrets string` | Specify the file that you want to use for storing the newly generated initialization bundle in Kubernetes secret form. Use `-` to produce output to the standard output stream (`stdout`). |

Options

<a id="roxctl-central-userpki_roxctl-central"></a>

# roxctl central userpki

Manage the user certificate authorization providers.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central userpki [flags]
```

</div>

<a id="roxctl-central-userpki-list_roxctl-central"></a>

## roxctl central userpki list

Display all the user certificate authentication providers.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central userpki list [flags]
```

</div>

| Option | Description |
|----|----|
| `-j`, `--json` | Enable the JSON output. The default value is `false`. |
| `--retry-timeout duration` | Specify the timeout after which API requests are retried. A value of zero means that the entire request duration is waited for without retrying. The default value is `20s`. |
| `-t`, `--timeout duration` | Specify the timeout for API requests representing the maximum duration of a request. The default value is `1m0s`. |

Options

<a id="roxctl-central-userpki-create_roxctl-central"></a>

## roxctl central userpki create

Create a new user certificate authentication provider.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central userpki create name [flags]
```

</div>

| Option | Description |
|----|----|
| `-c`, `--cert strings` | Specify the PEM files of the root CA certificates. You can specify several certificate files. |
| `--retry-timeout duration` | Specify the timeout after which API requests are retried. A value of zero means that the entire request duration is waited for without retrying. The default value is `20s`. |
| `-r`, `--role string` | Specify the minimum access role for users of this provider. |
| `-t`, `--timeout duration` | Specify the timeout for API requests representing the maximum duration of a request. The default value is `1m0s`. |

Options

<a id="roxctl-central-userpki-delete_roxctl-central"></a>

## roxctl central userpki delete

Delete a user certificate authentication provider.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl central userpki delete id|name [flags]
```

</div>

| Option | Description |
|----|----|
| `-f`, `--force` | If set to `true`, proceed with the deletion without confirmation. The default value is `false`. |
| `--retry-timeout duration` | Specify the timeout after which API requests are retried. A value of zero means that the entire request duration is waited for without retrying. The default value is `20s`. |
| `-t`, `--timeout duration` | Specify the timeout for API requests representing the maximum duration of a request. The default value is `1m0s`. |

Options
