> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_proxy). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Route traffic through a proxy

Route Red Hat OpenShift Dev Spaces traffic through a proxy by creating a Kubernetes Secret for proxy credentials and setting the proxy configuration in the `CheCluster` custom resource. The proxy settings are propagated to the operands and workspaces through environment variables.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have the proxy server URL, port, and (if the proxy requires authentication) the username and password.

## About this task

On an OpenShift cluster, you do not need to configure proxy settings. OpenShift Dev Spaces Operator automatically uses the OpenShift cluster-wide proxy configuration. However, you can override the proxy settings by specifying them in the `CheCluster` custom resource.

## Procedure

1.  Optional: Create a Secret in the openshift-devspaces namespace that contains a user and password for a proxy server. The secret must have the `app.kubernetes.io/part-of=che.eclipse.org` label. Skip this step if the proxy server does not require authentication.

    ``` bash
    oc apply -f - <<EOF
    kind: Secret
    apiVersion: v1
    metadata:
      name: devspaces-proxy-credentials
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
    type: Opaque
    stringData:
      user: <user>
      password: <password>
    EOF
    ```

    where:

    ` `*`<user>`*` `  
    The username for the proxy server.

    ` `*`<password>`*` `  
    The password for the proxy server.

2.  Configure the proxy or override the cluster-wide proxy configuration for an OpenShift cluster by setting the following properties in the CheCluster custom resource:

    ``` bash
    oc patch checluster/devspaces \
        --namespace openshift-devspaces \
        --type='merge' -p \
    '{"spec":
        {"components":
            {"cheServer":
                {"proxy":
                    {"credentialsSecretName" : "<secretName>",
                     "nonProxyHosts"         : ["<host_1>"],
                     "port"                  : "<port>",
                     "url"                   : "<protocol>://<domain>"}}}}}'
    ```

    where:

    ` `*`<secretName>`*` `  
    The credentials secret name created in the previous step.

    ` `*`<host_1>`*` `  
    The list of hosts that can be reached directly, without using the proxy. Use the following form `.<DOMAIN>` to specify a wildcard domain. OpenShift Dev Spaces Operator automatically adds .svc and Kubernetes service host to the list of non-proxy hosts. In OpenShift, OpenShift Dev Spaces Operator combines the non-proxy host list from the cluster-wide proxy configuration with the custom resource. In some proxy configurations, `localhost` may not translate to `127.0.0.1`. Both `localhost` and `127.0.0.1` should be specified in this situation.

    ` `*`<port>`*` `  
    The port of the proxy server.

    *`<protocol>`*`://`*`<domain>`*  
    Protocol and domain of the proxy server.

## Results

1.  Start a workspace.
2.  Verify that the workspace pod contains `HTTP_PROXY`, `HTTPS_PROXY`, `http_proxy`, and `https_proxy` environment variables, each set to *`<protocol>`*`://`*`<user>`*`:`*`<password>`*`@`*`<domain>`*`:`*`<port>`*.
3.  Verify that the workspace pod contains `NO_PROXY` and `no_proxy` environment variables, each set to a comma-separated list of non-proxy hosts.

**Related information**  

- [Configuring the cluster-wide proxy on OpenShift](https://docs.openshift.com/container-platform/4.22/networking/enable-cluster-wide-proxy.html)
