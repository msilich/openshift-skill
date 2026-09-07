<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To control network traffic flow, you can configure Gateway API listeners to define the designated port, protocol, and hostname for your gateway. By configuring listeners, you can specify secure TLS connections, dictate how traffic is terminated, and restrict which application routes are permitted to attach to the gateway.

To successfully manage your incoming traffic with gateway listeners, complete the following tasks:

- Configure listener routing and security settings to define the ports, protocols, hostnames, and TLS certificates for your incoming traffic.

- Understand listener routing conflicts by applying conflict management rules to ensure overlapping hostnames or ports are routed correctly.

- Troubleshoot listener connections by monitoring listener status conditions to identify and resolve configuration errors.

# Configure listener routing and security settings

To ensure that your applications receive only authenticated and authorized traffic, you must specify the allowed protocols and ports for your gateway. If you are routing secure traffic, you must also configure TLS settings. You can define these parameters by configuring the `spec.listeners` field in your `Gateway` custom resource (CR).

> [!IMPORTANT]
> If your gateway is accessible from other namespaces, always configure the `spec.listeners[].allowedRoutes[].namespaces.selector` field with a selector for the permitted namespaces. By specifying a namespace selector, you prevent possible misuse or hijacking of the gateway from other namespaces.
>
> If nothing is listed in the `spec.listeners[].allowedRoutes[]` field, the gateway is accessible only from the same namespace.

<div>

<div class="title">

Procedure

</div>

1.  Create or edit a `Gateway` YAML file to include your listener configuration.

    The following example demonstrates a `Gateway` CR with two listeners, one for HTTP and one for HTTPS. For detailed descriptions of the listener fields, see "Gateway listener configuration reference".

    ``` yaml
    kind: Gateway
    apiVersion: gateway.networking.k8s.io/v1
    metadata:
      name: <example_gateway>
      namespace: openshift-ingress
    spec:
      gatewayClassName: openshift-default
      listeners:
      - protocol: HTTP
        port: 80
        name: http
        hostname: "*.<example_domain.tld>"
        allowedRoutes:
          namespaces:
            from: Selector
            selector:
              matchLabels:
                env: "dev"
      - protocol: HTTPS
        port: 443
        name: https
        hostname: "*.<example_domain.tld>"
        tls:
          mode: Terminate
          certificateRefs:
            - name: <listener_cert>
              kind: Secret
        allowedRoutes:
          namespaces:
            from: Selector
            selector:
              matchLabels:
                env: "dev"
    ```

    \+ With this configuration, only `HTTPRoute` resources in namespaces that have the `env: "dev"` label can attach to these listeners.

2.  Apply the `Gateway` CR by running the following command:

    ``` terminal
    $ oc apply -f <gateway_cr>.yaml
    ```

</div>

## Gateway listener configuration reference

When configuring the `spec.listeners` field in your `Gateway` custom resource (CR), you can define network protocols, ports, hostnames, TLS termination, and route attachment policies.

You can customize your gateway listener configuration using the following fields:

`spec.listeners`
Defines the list of listeners for the gateway. You can customize this field with settings for port, protocol, TLS, hostnames, and allowed routes.

`listeners.protocol` and `listeners.port`
Defines the network port and protocol. For example, `protocol: HTTP` accepts HTTP traffic on port `80`, and `protocol: HTTPS` accepts HTTPS traffic on port `443`.

`listeners.hostname`
Defines the hostnames that the listener matches for incoming requests. For example, it can match only requests for hostnames ending in `<example_domain.tld>` (such as `www.<example_domain.tld>`). Always set a hostname on each listener, unless you are defining a catch-all route. If no hostname is specified, any route that can attach to the listener can claim arbitrary hostnames.

`listeners.tls`
Specifies the TLS settings for secure communication, including the mode (currently, only `Terminate` is supported on OpenShift Container Platform) and the Kubernetes secret containing the certificate keypair. For example, TLS is terminated at the gateway using a certificate stored in a Kubernetes `Secret` called `<listener_cert>`. You must ensure that the specified Kubernetes secret exists before you create the `Gateway` CR.

`listeners.allowedRoutes`
Controls which route resources can attach to this listener. If you omit this field, or set `namespaces.from: Same`, only routes in the same namespace as the `Gateway` can attach. To allow routes from other namespaces, set `namespaces.from: Selector` and a label selector for trusted namespaces. For example, an HTTP listener might allow `HTTPRoute` resources only from namespaces that have the `env: "dev"` label. Do not set `namespaces.from: All`; that setting allows routes from every namespace and can enable hostname or domain hijacking.

# Understand listener routing conflicts

When you configure a `Gateway` custom resource (CR) with multiple listeners, you must establish clear rules for overlapping hostnames and ports to ensure your traffic does not get misrouted. To avoid ambiguity, the Gateway API uses specific conflict management rules.

If your listener configurations violate these rules, the affected listener receives a `Conflicted` status condition and cannot route traffic correctly.

To resolve or prevent routing conflicts, ensure that your listeners adhere to the following rules:

- Distinct ports: A gateway can have distinct listeners that use the exact same hostname, provided their network ports are distinct.

- Distinct hostnames: A gateway can have distinct listeners that use the exact same protocol and port, provided their hostnames are different.

- Specificity precedence: If one listener uses a wildcard domain (for example, `*.<example_domain.tld>`) and another listener uses a more specific endpoint for that exact same domain (for example, `<www.example_domain.tld>`), the more specific entry takes precedence.

  This specificity rule also applies to multiple wildcard domains. For example, `*.<example_domain.tld>` takes precedence over `*.<tld>`. This ensures that traffic intended for a specific subdomain is accurately routed to its dedicated listener, even if a broader wildcard listener exists.

  > [!NOTE]
  > In the Gateway API, wildcards match one or more complete DNS labels. For example, `*.<example.com>` matches `<www.example.com>` and `<sub.domain.example.com>`, but does not match the root domain `<example.com>`.

# Troubleshoot listener connections using status conditions

When a listener is not routing traffic as expected, you can review its `status` conditions to quickly diagnose and fix the configuration error. The listener `status` condition gives insight into its current state and any underlying issues preventing it from accepting traffic.

<div>

<div class="title">

Procedure

</div>

1.  Check the `status` conditions of your `Gateway` custom resource (CR) by running the following command:

    ``` terminal
    $ oc describe gateway <gateway_cr> -n <namespace>
    ```

    - `<gateway_cr>`: Specify the name of your gateway.

    - `<namespace>`: Specify the namespace where the gateway resides.

      For details on how to interpret the output and resolve common errors, see [Gateway listener troubleshooting reference](#gateway-listener-troubleshooting-reference_controlling-incoming-traffic-gateway-listeners).

</div>

## Gateway listener troubleshooting reference

When you troubleshoot your gateway listeners, you can review the status conditions in the `Gateway` custom resource (CR) output to identify configuration errors or conflicts.

The following table describes common listener conditions and how to resolve them:

| Condition | Description |
|----|----|
| `Ready` | Indicates that the listener is configured correctly and is actively listening for traffic. |
| `Conflicted` | Signifies an ambiguity or conflict in the listener’s configuration with another listener on the same gateway. If a listener is conflicted, review your listener configurations against the conflict management rules to identify and resolve the ambiguity. |
| `Programmed` | Denotes that the underlying infrastructure, such as a load balancer or proxy, has successfully been programmed with the listener’s configuration. |
| `Accepted` | Indicates that the gateway has accepted the listener’s configuration. This is usually an early step in the listener’s lifecycle. |
| `Invalid` | Means the listener’s configuration itself contains errors or is malformed, preventing it from being processed. An invalid status indicates errors in your YAML configuration. Check your configuration for typos, incorrect syntax, or missing required fields. |

Gateway listener status conditions

# Additional resources

- [Gateway API documentation: Protocol-specific distinctiveness rules](https://gateway-api.sigs.k8s.io/concepts/api-overview/#distinctiveness)

- [Gateway API documentation: Hostnames](https://gateway-api.sigs.k8s.io/concepts/hostnames/)
