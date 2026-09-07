> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-proc_enabling_devspaces_metrics). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Enable OpenShift Dev Spaces server metrics

Enable the OpenShift Dev Spaces JVM metrics endpoint on port `8087` of the `che-host` Service to support performance monitoring and capacity planning.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

Edit the `CheCluster` Custom Resource on the cluster:

``` bash
$ oc edit checluster/devspaces -n openshift-devspaces
```

``` yaml
spec:
  components:
    metrics:
      enable: <boolean>
```

where:

` `*`<boolean>`*` `  
`true` to enable, `false` to disable.

## Results

- Verify the metrics endpoint is accessible:

  ``` bash
  oc get service che-host -n openshift-devspaces -o jsonpath='{.spec.ports[?(@.port==8087)]}'
  ```

**Related concepts**  

- [What OpenShift Dev Spaces server metrics reveal](observe-con_monitoring_devspaces.md "The OpenShift Dev Spaces server exposes JVM metrics such as memory usage and class loading on port 8087 on the /metrics endpoint. Monitoring these metrics helps administrators identify performance bottlenecks and plan server capacity.")

**Related tasks**  

- [Verify OpenShift Dev Spaces Server metrics collection with Prometheus](observe-proc_collecting_devspaces_metrics_with_prometheus.md "Verify that OpenShift Dev Spaces Server JVM metrics are available in Prometheus. The OpenShift Dev Spaces Operator automatically creates and reconciles the required Prometheus resources (ServiceMonitor, Role, and RoleBinding) and configures namespace labeling.")
