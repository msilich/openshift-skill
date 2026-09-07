> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_workspace_endpoints_base_domain). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set a custom domain for workspace URLs

Set a custom base domain for workspace endpoints to align URLs with your organization’s DNS naming conventions. By default, the OpenShift Dev Spaces Operator detects the base domain automatically.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have a DNS domain name configured to resolve to the cluster ingress where workspace routes will be served.

## Procedure

1.  Set the `CHE_INFRA_OPENSHIFT_ROUTE_HOST_DOMAIN__SUFFIX` field in the `CheCluster` Custom Resource:

    ``` yaml
    spec:
      components:
        cheServer:
          extraProperties:
            CHE_INFRA_OPENSHIFT_ROUTE_HOST_DOMAIN__SUFFIX: "<base_domain>"
    ```

    where:

    ` `*`<base_domain>`*` `  
    The workspace endpoints base domain, for example, `my-devspaces.example.com`.

2.  Apply the change:

    ``` bash
    oc patch checluster/devspaces \
        --namespace openshift-devspaces \
        --type='merge' -p \
    '{"spec":
        {"components":
            {"cheServer":
                {"extraProperties":
                    {"CHE_INFRA_OPENSHIFT_ROUTE_HOST_DOMAIN__SUFFIX": "my-devspaces.example.com"}}}}}'
    ```

## Results

- Verify the `CHE_INFRA_OPENSHIFT_ROUTE_HOST_DOMAIN__SUFFIX` value in the `CheCluster` Custom Resource:

  ``` bash
  oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.spec.components.cheServer.extraProperties.CHE_INFRA_OPENSHIFT_ROUTE_HOST_DOMAIN__SUFFIX}'
  ```

**Related information**  

- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
