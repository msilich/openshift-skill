<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If your network configuration restricts outbound traffic through proxies, you can configure proxy settings in Red Hat Advanced Cluster Security for Kubernetes to route traffic through a proxy.

<a id="configure-proxy-overview_configure-proxy"></a>

# Proxy configuration overview

When you use a proxy with Red Hat Advanced Cluster Security for Kubernetes, the proxy configuration affects how traffic flows between components and external services.

When you use a proxy with Red Hat Advanced Cluster Security for Kubernetes:

- All outgoing HTTP, HTTPS, and other TCP traffic from Central and Scanner goes through the proxy.

- Traffic between Central and Scanner does not go through the proxy.

- The proxy configuration does not affect the other Red Hat Advanced Cluster Security for Kubernetes components.

- When you are not using the offline mode, and a Collector running in a secured cluster needs to download an additional eBPF probe at runtime:

  - The collector attempts to download them by contacting Sensor.

  - The Sensor then forwards this request to Central.

  - Central uses the proxy to locate the module or probe at `https://collector-modules.stackrox.io`.

<a id="configure-proxy-on-an-existing-deployment_configure-proxy"></a>

# Configuring a proxy on an existing deployment

To configure a proxy in an existing deployment, you must export the `proxy-config` secret as a YAML file, update your proxy configuration in that file, and upload it as a secret.

> [!NOTE]
> If you have configured a global proxy on your OpenShift Container Platform cluster, the Operator Lifecycle Manager (OLM) automatically configures Operators that it manages with the cluster-wide proxy. However, you can also configure installed Operators to override the global proxy or inject a custom certificate authority (CA) certificate.
>
> For more information, see "Configuring proxy support in Operator Lifecycle Manager".

<div>

<div class="title">

Procedure

</div>

1.  Save the existing secret as a YAML file:

    ``` terminal
    $ oc -n stackrox get secret proxy-config \
      -o go-template='{{index .data "config.yaml" | \
      base64decode}}{{"\n"}}' > /tmp/proxy-config.yaml
    ```

2.  Edit the fields you want to change in the YAML configuration file, for example:

    ``` yaml
        # # NOTE: Both central and scanner should be restarted if this secret is changed.
        # # While it is possible that some components will pick up the new proxy configuration
        # # without a restart, it cannot be guaranteed that this will apply to every possible
        # # integration etc.
        # url: http://proxy.name:port
        # username: username
        # password: password
        # # If the following value is set to true, the proxy wil NOT be excluded for the default hosts:
        # # - *.stackrox, *.stackrox.svc
        # # - localhost, localhost.localdomain, 127.0.0.0/8, ::1
        # # - *.local
        # omitDefaultExcludes: false
        # excludes:  # hostnames (may include * components) for which you do not
        # # want to use a proxy, like in-cluster repositories.
        # - some.domain
        # # The following configuration sections allow specifying a different proxy to be used for HTTP(S) connections.
        # # If they are omitted, the above configuration is used for HTTP(S) connections as well as TCP connections.
        # # If only the `http` section is given, it will be used for HTTPS connections as well.
        # # Note: in most cases, a single, global proxy configuration is sufficient.
        # http:
        #   url: http://http-proxy.name:port
        #   username: username
        #   password: password
        # https:
        #   url: http://https-proxy.name:port
        #   username: username
        #   password: password
    ```

3.  After you save the changes, run the following command to replace the secret:

    ``` terminal
    $ oc -n stackrox create secret generic proxy-config \
      --from-file=config.yaml=/tmp/proxy-config.yaml -o yaml --dry-run | \
      oc label -f - --local -o yaml app.kubernetes.io/name=stackrox | \
      oc apply -f -
    ```

    <div class="important">

    <div class="title">

    </div>

    - You must wait for at least 1 minute, until OpenShift Container Platform propagates your changes to Central and Scanner.

    - If you see any issues with outgoing connections after changing the proxy configuration, you must restart your Central and Scanner pods.

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring proxy support in Operator Lifecycle Manager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/operators/administrator-tasks#olm-configuring-proxy-support)

</div>

<a id="configure-proxy-during-installation_configure-proxy"></a>

# Configuring a proxy during installation

When you are installing Red Hat Advanced Cluster Security for Kubernetes by using the `roxctl` command-line interface (CLI) or Helm, you can specify your proxy configuration during the installation.

When you run the installation program by using the `roxctl central generate` command, the installation program generates the secrets and deployment configuration files for your environment. You can configure a proxy by editing the generated configuration secret (YAML) file. Currently, you cannot configure proxies by using the `roxctl` CLI. Central and Scanner share the configuration, which Kubernetes stores in a secret.

<div>

<div class="title">

Procedure

</div>

1.  Open the configuration file `central/proxy-config-secret.yaml` from your deployment bundle directory.

    > [!NOTE]
    > If you are using Helm the configuration file is at `central/templates/proxy-config-secret.yaml`.

2.  Edit the fields you want to change in the configuration file:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      namespace: stackrox
      name: proxy-config
    type: Opaque
    stringData:
      config.yaml: |-
        # # NOTE: Both central and scanner should be restarted if this secret is changed.
        # # While it is possible that some components will pick up the new proxy configuration
        # # without a restart, it cannot be guaranteed that this will apply to every possible
        # # integration etc.
        # url: http://proxy.name:port
        # username: username
        # password: password
        # # If the following value is set to true, the proxy wil NOT be excluded for the default hosts:
        # # - *.stackrox, *.stackrox.svc
        # # - localhost, localhost.localdomain, 127.0.0.0/8, ::1
        # # - *.local
        # omitDefaultExcludes: false
        # excludes:  # hostnames (may include * components) for which you do not
        # # want to use a proxy, like in-cluster repositories.
        # - some.domain
        # # The following configuration sections allow specifying a different proxy to be used for HTTP(S) connections.
        # # If they are omitted, the above configuration is used for HTTP(S) connections as well as TCP connections.
        # # If only the `http` section is given, it will be used for HTTPS connections as well.
        # # Note: in most cases, a single, global proxy configuration is sufficient.
        # http:
        #   url: http://http-proxy.name:port
        #   username: username
        #   password: password
        # https:
        #   url: http://https-proxy.name:port
        #   username: username
        #   password: password
    ```

    where:

    `username` and `password`  
    (Optional) Specifies the username and password. These fields are optional at the beginning and in the `http` and `https` sections.

    `url`  
    Specifies the URL of the proxy. Supports the following URL schemes:

    - `http://` for an HTTP proxy

    - `https://` for a TLS-enabled HTTP proxy

    - `socks5://` for a SOCKS5 proxy

    `excludes`  
    Specifies a list of DNS names, with or without `*` wildcards, IP addresses, or IP blocks in CIDR notation, for example, `10.0.0.0/8`. The values in this list apply to all outgoing connections, regardless of protocol.

    `|-`  
    Specifies the start of the configuration data when inserted into the `stringData` section.

    <div class="note">

    <div class="title">

    </div>

    - When you first open the file, the `#` sign at the beginning of each line comments out all values. Lines starting with double hash signs `# #` contain explanation of the configuration keys.

    - Make sure that when you edit the fields, you keep an indentation level of two spaces relative to the `config.yaml: |-` line.

    </div>

3.  After editing the configuration file, you can proceed with your usual installation. The updated configuration instructs Red Hat Advanced Cluster Security for Kubernetes to use the proxy running on the provided address and the port number.

</div>
