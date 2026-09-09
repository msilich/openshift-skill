<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure endpoints for Red Hat Advanced Cluster Security for Kubernetes (RHACS) by using a YAML configuration file.

<a id="configure-endpoints-overview_configure-endpoints"></a>

# Configuring endpoints overview

You can use a YAML configuration file to define endpoints and customize their settings for Red Hat Advanced Cluster Security for Kubernetes.

You can use a YAML configuration file to configure exposed endpoints. You can use this configuration file to define one or more endpoints for Red Hat Advanced Cluster Security for Kubernetes and customize the TLS settings for each endpoint, or disable the TLS for specific endpoints. You can also define if the endpoints require client authentication, and which client certificates to accept.

<a id="custom-yaml-configuration_configure-endpoints"></a>

# Custom YAML configuration

Red Hat Advanced Cluster Security for Kubernetes uses the YAML configuration as a `ConfigMap`, making configurations easier to change and manage.

When you use the custom YAML configuration file, you can configure the following for each endpoint:

- The protocols to use, such as `HTTP`, `gRPC`, or both.

- Enable or disable TLS.

- Specify server certificates.

- Client Certificate Authorities (CA) to trust for client authentication.

- Specify if the endpoints require client certificate authentication (`mTLS`).

You can use the configuration file to specify endpoints either during the installation or on an existing instance of Red Hat Advanced Cluster Security for Kubernetes. However, if you expose any additional ports other than the default port `8443`, you must create network policies that allow traffic on those additional ports.

The following is a sample `endpoints.yaml` configuration file for Red Hat Advanced Cluster Security for Kubernetes:

``` yaml
# Sample endpoints.yaml configuration for Central.
#
# # CAREFUL: If the following line is uncommented, do not expose the default endpoint on port 8443 by default.
# #          This will break normal operation.
# disableDefault: true # if true, do not serve on :8443
endpoints:
  # Serve plaintext HTTP only on port 8080
  - listen: ":8080"
    # Backend protocols, possible values are 'http' and 'grpc'. If unset or empty, assume both.
    protocols:
      - http
    tls:
      # Disable TLS. If this is not specified, assume TLS is enabled.
      disable: true
  # Serve HTTP and  gRPC for sensors only on port 8444
  - listen: ":8444"
    tls:
      # Which TLS certificates to serve, possible values are 'service' (For  service certificates that Red Hat Advanced Cluster Security for Kubernetes generates)
      # and 'default' (user-configured default TLS certificate). If unset or empty, assume both.
      serverCerts:
        - default
        - service
      # Client authentication settings.
      clientAuth:
        # Enforce TLS client authentication. If unset, do not enforce, only request certificates
        # opportunistically.
        required: true
        # Which TLS client CAs to serve, possible values are 'service' (CA for service
        # certificates that Red Hat Advanced Cluster Security for Kubernetes generates) and 'user' (CAs for PKI auth providers). If unset or empty, assume both.
        certAuthorities:
        # if not set, assume ["user", "service"]
          - service
```

where:

`disableDefault`  
Specifies whether to disable exposure on the default port number `8443`. If you do not specify a value, it defaults to `false`; changing it to `true` might break existing functionality.

`endpoints`  
Specifies a list of additional endpoints for exposing Central.

`endpoints.listen`  
Specifies the address and port number on which to listen. You must specify this value if you are using `endpoints`. You can use the format `port`, `:port`, or `address:port` to specify values. For example,

- `8080` or `:8080` - listen on port `8080` on all interfaces.

- `0.0.0.0:8080` - listen on port `8080` on all IPv4 (not IPv6) interfaces.

- `127.0.0.1:8080` - listen on port `8080` on the local loopback device only.

`endpoints.protocols`  
Specifies the protocols to use for the specified endpoint. Acceptable values are `http` and `grpc`. If you do not specify a value, Central listens to both HTTP and gRPC traffic on the specified port. If you want to expose an endpoint only for the RHACS portal, use `http`. However, you cannot use the endpoint for service-to-service communication or for the `roxctl` CLI, because these clients require both gRPC and HTTP. To enable both HTTP and gRPC protocols for the endpoint, you must not specify a value for this key. If you want to restrict an endpoint to Red Hat Advanced Cluster Security for Kubernetes services only, use the **clientAuth** option.

`endpoints.tls`  
Specifies the TLS settings for the endpoint. If you do not specify a value, Red Hat Advanced Cluster Security for Kubernetes enables TLS with the default settings for all the following nested keys.

`endpoints.tls.disable`  
Specifies whether to disable TLS on the specified endpoint. If you do not specify a value, it defaults to `false`. When you set it to `true`, you cannot specify values for `serverCerts` and `clientAuth`.

`endpoints.tls.serverCerts`  
Specifies a list of sources from which to configure server TLS certificates. The `serverCerts` list is order-dependent, it means that the first item in the list determines the certificate that Central uses by default, when there is no matching Server Name indication (SNI). You can use this to specify many certificates and Central automatically selects the right certificate based on SNI. Acceptable values are:

- `default`: use the already configured custom TLS certificate if it exists.

- `service`: use the internal service certificate that Red Hat Advanced Cluster Security for Kubernetes generates.

`endpoints.tls.clientAuth`  
Specifies whether to configure the behavior of the TLS-enabled endpoint’s client certificate authentication.

`endpoints.tls.clientAuth.required`  
Specifies whether to only allow clients with a valid client certificate. If you do not specify a value, it defaults to `false`. You can use `true` in conjunction with a the `certAuthorities` setting of `service` to only allow Red Hat Advanced Cluster Security for Kubernetes services to connect to this endpoint.

`endpoints.tls.clientAuth.certAuthorities`  
Specifies a list of CAs to verify client certificates. The default value is `["service", "user"]`. The `certAuthorities` list is order-independent, it means that the position of the items in this list does not matter. Also, setting it as empty list `[]` disables client certificate authentication for the endpoint, which is different from leaving this value unset. Acceptable values are:

- `service`: CA for service certificates that Red Hat Advanced Cluster Security for Kubernetes generates.

- `user`: CAs configured by PKI authentication providers.

<a id="configure-endpoints-new-install_configure-endpoints"></a>

# Configuring endpoints during a new installation

When you install Red Hat Advanced Cluster Security for Kubernetes by using the `roxctl` CLI, it creates a folder named `central-bundle`, which contains the necessary YAML manifests and scripts to deploy Central.

> [!NOTE]
> If you expose any additional ports other than the default port `8443`, you must create network policies that allow traffic on those additional ports.

<div>

<div class="title">

Procedure

</div>

1.  After you generate the `central-bundle`, open the `./central-bundle/central/02-endpoints-config.yaml` file.

2.  In this file, add your custom YAML configuration under the `data:` section of the key `endpoints.yaml`. Maintain a 4 space indentation for the YAML configuration.

3.  Continue the installation instructions as usual. Red Hat Advanced Cluster Security for Kubernetes uses the specified configuration.

</div>

<a id="configure-endpoints-existing_configure-endpoints"></a>

# Configuring endpoints for an existing instance

You can configure endpoints for an existing instance of Red Hat Advanced Cluster Security for Kubernetes.

> [!NOTE]
> If you expose any additional ports other than the default port `8443`, you must create network policies that allow traffic on those additional ports.

<div>

<div class="title">

Procedure

</div>

1.  Download the existing config map:

    ``` terminal
    $ oc -n stackrox get cm/central-endpoints -o go-template='{{index .data "endpoints.yaml"}}'  > <directory_path>/central_endpoints.yaml
    ```

2.  In the downloaded `central_endpoints.yaml` file, specify your custom YAML configuration.

3.  Upload and apply the modified `central_endpoints.yaml` configuration file:

    ``` terminal
    $ oc -n stackrox create cm central-endpoints --from-file=endpoints.yaml=<directory-path>/central-endpoints.yaml -o yaml --dry-run | \
    oc label -f - --local -o yaml app.kubernetes.io/name=stackrox | \
    oc apply -f -
    ```

4.  Restart Central.

</div>

<a id="restart-central_configure-endpoints"></a>

## Restarting the Central container

You can restart the Central container by deleting the Central pod.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

- To delete the Central pod, run the following command:

  ``` terminal
  $ oc -n stackrox delete pod -lapp=central
  ```

</div>

<a id="enable-traffic-flow-through-custom-ports_configure-endpoints"></a>

# Enabling traffic flow through custom ports

If you are exposing a port to another service running in the same cluster or to an ingress controller, allow traffic only from the services in your cluster or from the proxy of the ingress controller. Otherwise, if you are exposing a port by using a load balancer service, you might want to allow traffic from all sources, including external sources. Use the procedure listed in this section to allow traffic from all sources.

<div>

<div class="title">

Procedure

</div>

1.  Clone the `allow-ext-to-central` Kubernetes network policy:

    ``` terminal
    $ oc -n stackrox get networkpolicy.networking.k8s.io/allow-ext-to-central -o yaml > <directory_path>/allow-ext-to-central-custom-port.yaml
    ```

2.  Use it as a reference to create your network policy, and in that policy, specify the port number you want to expose. Make sure to change the name of your network policy in the `metadata` section of the YAML file, so that it does not interfere with the built-in `allow-ext-to-central` policy.

</div>
