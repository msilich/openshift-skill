> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-proc_viewing_workspace_logs_in_cli). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# View workspace logs in CLI

View OpenShift Dev Spaces workspace logs from the OpenShift command-line interface (CLI) to troubleshoot startup failures and runtime errors.

## Before you begin

- You have the OpenShift Dev Spaces workspace *\<workspace_name\>* running.
- You have an OpenShift CLI session with access to the OpenShift project *\<namespace_name\>* containing this workspace.

## Procedure

Get the logs from the pod running the *\<workspace_name\>* workspace in the *\<namespace_name\>* project:

``` bash
$ oc logs --follow --namespace='<workspace_namespace>' \
  --selector='controller.devfile.io/devworkspace_name=<workspace_name>'
```

## Results

- The terminal displays workspace container logs including startup events and runtime output.
