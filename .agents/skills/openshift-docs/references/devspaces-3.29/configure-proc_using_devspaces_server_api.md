> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_using_devspaces_server_api). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Use the server API

Use the Swagger web user interface to explore and interact with the OpenShift Dev Spaces server and dashboard APIs for programmatic integration and automation.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

Navigate to the Swagger API web user interface:

- `https://`*`<openshift_dev_spaces_fqdn>`*`/swagger` (OpenShift Dev Spaces server)

- `https://`*`<openshift_dev_spaces_fqdn>`*`/dashboard/swagger` (OpenShift Dev Spaces dashboard) Important

  DevWorkspace is a Kubernetes object and manipulations should happen on the Kubernetes API level.

**Related information**  

- [How workspaces connect to OpenShift](integrate-con_integrating_with_openshift.md)
- [Swagger](https://swagger.io/)
