> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-ref_url_parameter_for_a_memory_limit). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# URL parameter for a memory limit

The `memoryLimit` URL parameter specifies or overrides the container memory limit when starting a new workspace from a devfile URL. Use this parameter to allocate enough memory for resource-intensive development tasks.

The URL parameter for the memory limit is `memoryLimit=`:

``` plaintext
https://<openshift_dev_spaces_fqdn>#<git_repository_url>?memoryLimit=<container_memory_limit>
```

You can specify the memory limit in bytes, or use a suffix such as `Mi` for mebibytes or `Gi` for gibibytes.

## Example

`https://`*`<openshift_dev_spaces_fqdn>`*`#https://github.com/eclipse-che/che-docs?memoryLimit=4Gi`

Important

When you specify the `memoryLimit` parameter, it overrides the memory limit defined for the first container of the devfile.

The sum of the limits from the target devfile and from the editor definition is applied to the workspace pod `spec.containers[0].resources.limits.memory`.

**Related information**  

- [Limiting resources usage](https://devfile.io/docs/2.3.0/limiting-resources-usage)
- [Editor definition samples](https://github.com/devfile/devworkspace-operator/tree/main/samples/editors)
