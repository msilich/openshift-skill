<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You must configure the proxy settings for secured cluster services within the Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service) environment to establish a connection between the Secured Cluster and the specified proxy server. This ensures reliable data collection and transmission.

<a id="specifying-the-environment-variables-in-the-securedcluster-cr_configure-secured-cluster-proxy"></a>

# Specifying the environment variables in the SecuredCluster CR

To configure an egress proxy, you can either use the cluster-wide Red Hat OpenShift proxy or specify the `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` environment variables within the SecuredCluster Custom Resource (CR) configuration file to ensure proper use of the proxy and bypass for internal requests within the specified domain.

The proxy configuration applies to all running services: Sensor, Collector, Admission Controller and Scanner.

<div>

<div class="title">

Procedure

</div>

- Specify the `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` environment variables under the customize specification in the SecuredCluster CR configuration file:

  For example:

  ``` yaml
  # proxy collector
  customize:
    envVars:
      - name: HTTP_PROXY
        value: http://egress-proxy.stackrox.svc:xxxx
      - name: HTTPS_PROXY
        value: http://egress-proxy.stackrox.svc:xxxx
      - name: NO_PROXY
        value: .stackrox.svc
  ```

  where:

  `customize.envVars.value.name:<HTTP_PROXY>`  
  Specifies the value of the `HTTP_PROXY` variable. This is the proxy server used for HTTP connections.

  `customize.envVars.value.name:<HTTPS_PROXY>`  
  Specifies the value of the `HTTPS_PROXY` variable. This is the proxy server used for HTTPS connections.

  `customize.envVars.value.name:<NO_PROXY>`  
  Specifies the value of the `NO_PROXY` variable. This variable defines which hostnames or IP addresses bypass the proxy server.

</div>
