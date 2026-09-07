> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_openshift_route_for_router_sharding). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Route workspace traffic through a shared ingress controller

Route OpenShift Dev Spaces traffic to the correct ingress controller by configuring labels, annotations, and domains for OpenShift Route when using Router Sharding on an OpenShift cluster.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have the `dsc` management tool installed. See [Installing the dsc management tool](plan-proc_installing_the_dsc_management_tool.md).

## Procedure

Edit the `CheCluster` Custom Resource on the cluster:

``` bash
$ oc edit checluster/devspaces -n openshift-devspaces
```

``` yaml
spec:
  networking:
    labels: <labels>
    domain: <domain>
    annotations: <annotations>
```

where:

` `*`<labels>`*` `  
An unstructured key value map of labels that the target ingress controller uses to filter the set of Routes to service.

` `*`<domain>`*` `  
The DNS name serviced by the target ingress controller.

` `*`<annotations>`*` `  
An unstructured key value map stored with a resource.

## Results

- Verify that OpenShift Dev Spaces routes have the configured labels and annotations:

  ``` bash
  oc get routes -n openshift-devspaces -o yaml
  ```

**Related information**  

- [Router Sharding](https://docs.openshift.com/container-platform/4.22/networking/ingress-operator.html#nw-ingress-sharding_configuring-ingress)
- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
