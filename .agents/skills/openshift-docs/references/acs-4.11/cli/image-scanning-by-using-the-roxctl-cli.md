<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can scan images stored in image registries, including cluster local registries such as the OpenShift Container Platform integrated image registry by using the `roxctl` CLI.

<a id="scanning-images-by-using-a-remote-cluster_image-scanning-by-using-the-roxctl-cli"></a>

# Remote cluster image scanning

By specifying the appropriate cluster in the delegated scanning configuration or through the cluster parameter, you can scan images from cluster local registries by using a remote cluster.

> [!IMPORTANT]
> For more information about how to configure delegated image scanning, see "Accessing delegated image scanning".

<div>

<div class="title">

Additional resources

</div>

- [Accessing delegated image scanning](../operating/examine-images-for-vulnerabilities.md#accessing-delegated-image-scanning_examine-images-for-vulnerabilities)

</div>

<a id="scanning-images-remote-cluster-procedure_image-scanning-by-using-the-roxctl-cli"></a>

## Scanning images by using a remote cluster

You can scan images from cluster local registries by delegating the scan to a remote cluster.

<div>

<div class="title">

Procedure

</div>

- Run the following command to scan the specified image in a remote cluster:

  ``` terminal
  $ roxctl image scan \
    --image=<image_registry>/<image_name> \
    --cluster=<cluster_detail> \
    [flags]
  ```

  where:

  `<image_registry>`  
  Specifies the registry that stores the image, for example, `image-registry.openshift-image-registry.svc:5000/`.

  `image_name`  
  Specifies the name of the image that you want to scan.

  `<cluster_detail>`  
  Specifies the name or ID of the remote cluster. For example, specify the name `remote`.

  `[flags]`  
  Specifies the parameters to modify the behavior of the command. This is optional.

  The following is an example output:

  ``` text
  {
    "Id": "sha256:3f439d7d71adb0a0c8e05257c091236ab00c6343bc44388d091450ff58664bf9",
    "name": {
      "registry": "image-registry.openshift-image-registry.svc:5000",
      "remote": "default/image-stream",
      "tag": "latest",
      "fullName": "image-registry.openshift-image-registry.svc:5000/default/image-stream:latest"
    },
  [...]
  ```

  - `Id` is a unique identifier for the image that serves as a fingerprint for the image. It helps ensure the integrity and authenticity of the image.

  - `registry` is the location of the image registry that stores the image.

  - `remote` is the remote path to the image.

  - `tag` is the version or tag associated with this image.

  - `fullName` is the complete name of the image, combining the registry, remote path, and tag.

</div>

<a id="roxctl-image-scan-command-options_image-scanning-by-using-the-roxctl-cli"></a>

# Options

The `roxctl image scan` command supports the following options:

| Option | Description |
|----|----|
| `--cluster string` | Delegate image scanning to a specific cluster. |
| `--compact-output` | Print the JSON output in a compact format. The default value is `false`. |
| `-f`, `--force` | Ignore Central’s cache for the scan and force a fresh re-pull from Scanner. The default value is `false`. |
| `--headers strings` | Print the headers in a tabular format. Default values include `COMPONENT`,`VERSION`,`CVE`,`SEVERITY`, and `LINK`. |
| `--headers-as-comments` | Print the headers as comments in a CSV tabular output. The default value is `false`. |
| `-h`, `--help` | View the help text for the `roxctl image scan` command. |
| `-i`, `--image string` | Specify the image name and reference you want to scan. |
| `-a`, `--include-snoozed` | Return both snoozed and unsnoozed common vulnerabilities and exposures (CVEs). The default value is `false`. |
| `--merge-output` | Merge duplicate cells in a tabular output. The default value is `true`. |
| `--no-header` | Do not print headers for tabular format. The default value is `false`. |
| `-o`, `--output string` | Specify the output format. You can select a format to customize the display of results. Formats include `table`, `CSV`, `JSON`, and `SARIF`. |
| `-r`, `--retries int` | Set the number of retries before the command aborts the operation with an error. The default value is `3`. |
| `-d`, `--retry-delay int` | Set the time in seconds to wait between retries. The default value is `3`. |
| `--row-jsonpath-expressions string` | Use the JSON path expressions to create rows from the JSON object. For more details, run the `roxctl image scan --help` command. |
