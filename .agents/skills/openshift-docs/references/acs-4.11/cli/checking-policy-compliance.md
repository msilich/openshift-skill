<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use the `roxctl` CLI to check deployment YAML files and images for policy compliance.

<a id="setting-up-environment-variables_checking-policy-compliance"></a>

# Prerequisites

Configure the `ROX_ENDPOINT` environment variable to specify the host and port information for Central.

<div>

<div class="title">

Procedure

</div>

- To configure the `ROX_ENDPOINT` environment variable, run the following command:

  ``` terminal
  $ export ROX_ENDPOINT=<host:port>
  ```

  where:

  `<host:port>`  
  Specifies the host and port information that you want to store in the `ROX_ENDPOINT` environment variable.

</div>

<a id="configuring-output-format_checking-policy-compliance"></a>

# Configuring output format

When you check policy compliance by using the `roxctl deployment check` or `roxctl image check` commands, you can specify the output format by using the `-o` option to the command and specifying the format as `json`, `table`, `csv`, or `junit`. This option determines how the output of a command is displayed in the terminal.

For example, the following command checks a deployment and then displays the result in `csv` format:

``` terminal
$ roxctl deployment check --file =<yaml_filename> -o csv
```

> [!NOTE]
> When you do not specify the `-o` option for the output format, the CLI uses the following default behavior:
>
> - The format for the `deployment check` and the `image check` commands is `table`.
>
> - The default output format for the `image scan` command is `json`. This is the old JSON format output for compatibility with older versions of the CLI. To get the output in the new JSON format, specify the option with format, as `-o json`. Use the old JSON format output when gathering data for troubleshooting purposes.

<a id="configuring-output-format-options_checking-policy-compliance"></a>

## Output format options

The following table lists the configuration options for the output format, including their descriptions and the output format in which they are available.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 50%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Option</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Formats</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>--compact-output</code></p></td>
<td style="text-align: left;"><p>Use this option to display the JSON output in a compact format.</p></td>
<td style="text-align: left;"><p><code>json</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--headers</code></p></td>
<td style="text-align: left;"><p>Use this option to specify custom headers.</p></td>
<td style="text-align: left;"><p><code>table</code> and <code>csv</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--no-header</code></p></td>
<td style="text-align: left;"><p>Use this option to omit the header row from the output.</p></td>
<td style="text-align: left;"><p><code>table</code> and <code>csv</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--row-jsonpath-expressions</code></p></td>
<td style="text-align: left;"><p>Use this option to specify GJSON paths to select specific items from the output. For example, to get the <strong>Policy name</strong> and <strong>Severity</strong> for a deployment check, use the following command:</p>
<pre class="terminal"><code>$ roxctl deployment check --file=&lt;yaml_filename&gt; \
  -o table --headers POLICY-NAME,SEVERITY \
  --row-jsonpath-expressions=&quot;{results..violatedPolicies..name,results..violatedPolicies..severity}&quot;</code></pre></td>
<td style="text-align: left;"><p><code>table</code> and <code>csv</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--merge-output</code></p></td>
<td style="text-align: left;"><p>Use this options to merge table cells that have the same value.</p></td>
<td style="text-align: left;"><p><code>table</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>headers-as-comment</code></p></td>
<td style="text-align: left;"><p>Use this option to include the header row as a comment in the output.</p></td>
<td style="text-align: left;"><p><code>csv</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--junit-suite-name</code></p></td>
<td style="text-align: left;"><p>Use this option to specify the name of the JUnit test suite.</p></td>
<td style="text-align: left;"><p><code>junit</code></p></td>
</tr>
</tbody>
</table>

<div>

<div class="title">

Additional resources

</div>

- [GJSON paths](https://github.com/tidwall/gjson)

</div>

<a id="checking-deployment-yaml-files_checking-policy-compliance"></a>

# Checking deployment YAML files

You can check the build-time and deploy-time violations of your security policies in YAML deployment files.

<div>

<div class="title">

Procedure

</div>

- To check the build-time and deploy-time violations of your security policies in YAML deployment files, run the following command:

  ``` terminal
  $ roxctl deployment check --file=<yaml_filename> \
  --namespace=<cluster_namespace> \
  --cluster=<cluster_name_or_id> \
  --verbose
  ```

  where:

  `<yaml_filename>`  
  Specifies the YAML file with one or more deployments to send to Central for policy evaluation.

  `<cluster_namespace>`  
  Specifies a namespace to enhance deployments with context information such as network policies, role-based access controls (RBACs), and services for deployments that do not have a namespace in their specification. The namespace defined in the specification is not changed. The default value is `default`.

  `<cluster_name_or_id>`  
  Specifies the cluster name or ID that you want to use as the context for the evaluation to enable extended deployments with cluster-specific information.

  `--verbose`  
  Specifies that you receive additional information for each deployment during the policy check, including the RBAC permission level and a comprehensive list of applied network policies.

  The API reference defines the format. To cause Red Hat Advanced Cluster Security for Kubernetes (RHACS) to re-pull image metadata and image scan results from the associated registry and scanner, add the `--force` option.

  > [!NOTE]
  > To check specific image scan results, you must have a token with both `read` and `write` permissions for the `Image` resource. The default **Continuous Integration** system role already has the required permissions.

  This command validates the following items:

  - Configuration options in a YAML file, such as resource limits or privilege options

  - Aspects of the images used in a YAML file, such as components or vulnerabilities

</div>

<a id="checking-images_checking-policy-compliance"></a>

# Checking images

You can check the build-time violations of your security policies in images.

<div>

<div class="title">

Procedure

</div>

- To check the build-time violations of your security policies in images, run the following command:

  ``` terminal
  $ roxctl image check --image=<image_name>
  ```

  The API reference defines the format. To cause Red Hat Advanced Cluster Security for Kubernetes (RHACS) to re-pull image metadata and image scan results from the associated registry and scanner, add the `--force` option.

  > [!NOTE]
  > To check specific image scan results, you must have a token with both `read` and `write` permissions for the `Image` resource. The default **Continuous Integration** system role already has the required permissions.

</div>

<div>

<div class="title">

Additional resources

</div>

- [roxctl image](command-reference/roxctl-image.md)

</div>

<a id="checking-image-scan-results_checking-policy-compliance"></a>

# Checking image scan results

You can check the scan results for specific images.

<div>

<div class="title">

Procedure

</div>

- To return the components and vulnerabilities found in the image in JSON format, run the following command:

  ``` terminal
  $ roxctl image scan --image <image_name>
  ```

  The API reference defines the format. To cause Red Hat Advanced Cluster Security for Kubernetes (RHACS) to re-pull image metadata and image scan results from the associated registry and scanner, add the `--force` option.

  > [!NOTE]
  > To check specific image scan results, you must have a token with both `read` and `write` permissions for the `Image` resource. The default **Continuous Integration** system role already has the required permissions.

</div>

<div>

<div class="title">

Additional resources

</div>

- [roxctl image](command-reference/roxctl-image.md)

</div>
