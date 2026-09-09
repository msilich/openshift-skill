<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Enable an unencrypted HTTP server to expose the RHACS portal through ingress controllers, Layer 7 load balancers, Istio, or other solutions.

<a id="expose-portal-http-overview_expose-portal-over-http"></a>

# HTTP portal exposure overview

You can configure Red Hat Advanced Cluster Security for Kubernetes to expose the RHACS portal over HTTP for use with ingress controllers, Layer 7 load balancers, or Istio that prefer unencrypted HTTP back ends.

If you use an ingress controller, Istio, or a Layer 7 load balancer that prefers unencrypted HTTP back ends, you can configure Red Hat Advanced Cluster Security for Kubernetes to expose the RHACS portal over HTTP. Doing this makes the RHACS portal available over a plain text back end.

> [!IMPORTANT]
> To expose the RHACS portal over HTTP, you must be using an ingress controller, a Layer 7 load balancer, or Istio to encrypt external traffic with HTTPS. It is insecure to expose the RHACS portal directly to external clients by using plain HTTP.

You can expose the RHACS portal over HTTP during installation or on an existing deployment.

<a id="expose-portal-http-prerequisites_expose-portal-over-http"></a>

# Prerequisites

You must use an endpoint specification to configure HTTP endpoints for the RHACS portal.

- To specify an HTTP endpoint you must use an `<endpoints_spec>`. It is a comma-separated list of single endpoint specifications in the form of `<type>@<addr>:<port>`, where:

  - `type` is `grpc` or `http`. Using `http` as type works in most use cases. For advanced use cases, you can either use `grpc` or omit its value. If you omit the value for `type`, you can configure two endpoints in your proxy, one for gRPC and the other for HTTP. Both these endpoints point to the same exposed HTTP port on Central. However, most proxies do not support carrying both gRPC and HTTP traffic on the same external port.

  - `addr` is the IP address to expose Central on. You can omit this, or use `localhost` or `127.0.0.1` if you need an HTTP endpoint which is only accessible by using port-forwarding.

  - `port` is the port to expose Central on.

  - The following are several valid `<endpoints_spec>` values:

    - `8080`

    - `http@8080`

    - `:8081`

    - `grpc@:8081`

    - `localhost:8080`

    - `http@localhost:8080`

    - `http@8080,grpc@8081`

    - `8080, grpc@:8081, http@0.0.0.0:8082`

<a id="expose-portal-http-during-installation_expose-portal-over-http"></a>

# Exposing the RHACS portal over HTTP during the installation

If you are installing Red Hat Advanced Cluster Security for Kubernetes by using the `roxctl` CLI, use the `--plaintext-endpoints` option with the `roxctl central generate interactive` command to enable the HTTP server during the installation.

<div>

<div class="title">

Procedure

</div>

- Run the following command to specify an HTTP endpoint during the interactive installation process:

  ``` terminal
  $ roxctl central generate interactive \
    --plaintext-endpoints=<endpoints_spec>
  ```

  where:

  \<endpoints_spec\>  
  Specifies the endpoints in the form of `<type>@<addr>:<port>`. See the Prerequisites section for details.

</div>

<a id="expose-portal-http-existing-deployment_expose-portal-over-http"></a>

# Exposing the RHACS portal over HTTP for an existing deployment

You can enable the HTTP server on an existing Red Hat Advanced Cluster Security for Kubernetes deployment.

<div>

<div class="title">

Procedure

</div>

1.  Create a patch and define a `ROX_PLAINTEXT_ENDPOINTS` environment variable:

    ``` terminal
    $ CENTRAL_PLAINTEXT_PATCH='
    spec:
      template:
        spec:
          containers:
          - name: central
            env:
            - name: ROX_PLAINTEXT_ENDPOINTS
              value: <endpoints_spec>
    '
    ```

    where:

    \<endpoints_spec\>  
    Specifies the endpoints in the form of `<type>@<addr>:<port>`. See the Prerequisites section for details.

2.  Add the `ROX_PLAINTEXT_ENDPOINTS` environment variable to the Central deployment:

    ``` terminal
    $ oc -n stackrox patch deploy/central -p "$CENTRAL_PLAINTEXT_PATCH"
    ```

</div>
