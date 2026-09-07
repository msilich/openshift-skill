<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To protect sensitive data and meet security compliance requirements, you must secure your Gateway API application traffic. You can secure 'HTTPRoute' custom resources (CRs) by either applying edge or re-encrypt Transport Layer Security (TLS) termination. Choose your method based on your security architecture and performance needs.

# HTTPRoute Transport Layer Security (TLS) configuration

To balance security compliance and application performance, you can configure edge or re-encrypt TLS termination on your gateway listeners.

Edge termination
Edge termination encrypts client traffic to the gateway but allows unencrypted traffic to pass to your internal services. This configuration is ideal for encrypting user logins while trading internal encryption for faster application performance.

Re-encrypt termination
Re-encrypt termination encrypts traffic from the client to the gateway, and then re-encrypts it to the destination service. This mode allows the gateway to inspect payloads to efficiently route traffic or block unauthorized access without eliminating backend encryption.

> [!IMPORTANT]
> OpenShift Container Platform does not support passthrough termination for Gateway API. Passthrough termination provides direct traffic encryption from the client to the service, and is only supported in traditional OpenShift Container Platform routes.

# Securing client connections with edge TLS termination

To secure traffic from clients to your gateway, configure a listener with the `Terminate` TLS mode and a `certificateRef` to an OpenShift Container Platform secret.

This configuration terminates encryption at the gateway for `HTTPRoute` custom resource (CR) traffic that targets the listener, and forwards unencrypted traffic to the destination service. You must have both an `HTTPRoute` CR and a gateway listener configured with intersecting hostnames for edge termination to successfully connect.

<div>

<div class="title">

Prerequisites

</div>

- You created an `HTTPRoute` CR that references your gateway. The hostnames defined in this route must match or intersect with the hostnames you plan to configure on your gateway listeners.

- You created a `Secret` resource containing your TLS certificate and key in the same namespace as your gateway or in a namespace permitted by a `ReferenceGrant` CR.

</div>

> [!IMPORTANT]
> The configuration examples in this procedure use `openshift-default` as the `gatewayClassName` value. When creating your `Gateway` CR, ensure that the `gatewayClassName` field aligns with the `GatewayClass` CR in your cluster configuration.

<div>

<div class="title">

Procedure

</div>

- Create and apply a `Gateway` CR file configured for your domain requirements by using one of the following examples:

  - To secure multiple domains, configure separate listeners for each domain with their respective certificates as shown in the following example:

    ``` yaml
    apiVersion: gateway.networking.k8s.io/v1
    kind: Gateway
    metadata:
      name: tls-basic
      namespace: openshift-ingress
    spec:
      gatewayClassName: openshift-default
      listeners:
      - name: app1-https
        protocol: HTTPS
        port: 443
        hostname: app1.example.com
        tls:
          mode: Terminate
          certificateRefs:
          - kind: Secret
            group: ""
            name: app1-example-com-cert
      - name: app2-https
        protocol: HTTPS
        port: 443
        hostname: app2.example.com
        tls:
          mode: Terminate
          certificateRefs:
          - kind: Secret
            group: ""
            name: app2-example-com-cert
    ```

  - To secure wildcard domains, configure a single listener with a wildcard certificate:

    ``` yaml
    apiVersion: gateway.networking.k8s.io/v1
    kind: Gateway
    metadata:
      name: wildcard-gateway
      namespace: openshift-ingress
    spec:
      gatewayClassName: openshift-default
      listeners:
      - name: wildcard-https
        protocol: HTTPS
        port: 443
        hostname: "+++*+++.example.com"
        tls:
          mode: Terminate
          certificateRefs:
          - kind: Secret
            group: ""
            name: wildcard-cert
    ```

    You can configure both specific domain listeners and wildcard listeners on the same `Gateway` CR. Specific matches happen before wildcard matches, so a request to `app1.example.com` uses the specific certificate rather than the wildcard certificate.

  - To secure all domains, configure a listener that listens for all routes regardless of hostname as shown in the following example:

    ``` yaml
    apiVersion: gateway.networking.k8s.io/v1
    kind: Gateway
    metadata:
      name: default-gateway
      namespace: openshift-ingress
    spec:
      gatewayClassName: openshift-default
      listeners:
      - name: all-https
        protocol: HTTPS
        port: 443
        tls:
          mode: Terminate
          certificateRefs:
          - kind: Secret
            group: ""
            name: default-cert
    ```

  - To use a `Secret` object in a different namespace, configure your listener and create a corresponding `ReferenceGrant` CR as shown in the following example:

    ``` yaml
    apiVersion: gateway.networking.k8s.io/v1
    kind: Gateway
    metadata:
      name: cross-namespace-example
      namespace: example-ns1
    spec:
      gatewayClassName: openshift-default
      listeners:
      - name: https
        protocol: HTTPS
        port: 443
        hostname: "+++*+++.example.com"
        tls:
          mode: Terminate
          certificateRefs:
          - kind: Secret
            group: ""
            name: wildcard-cert
            namespace: example-ns2
    ---
    apiVersion: gateway.networking.k8s.io/v1beta1
    kind: ReferenceGrant
    metadata:
      name: allow-ns1-reference
      namespace: example-ns2
    spec:
      from:
      - group: gateway.networking.k8s.io
        kind: Gateway
        namespace: example-ns1
      to:
      - group: ""
        kind: Secret
    ```

    Unlike standard OpenShift Container Platform routes that use namespace-wide annotations for cross-namespace permissions, Gateway API uses the `ReferenceGrant` CR to authorize access. This `ReferenceGrant` CR gives access from the `Gateway` CR in one namespace to the `Secret` object in another namespace.

</div>

<div>

<div class="title">

Verification

</div>

- Check the listener conditions to verify that the `Gateway` CR is successfully configured and listening on port 443. The following example checks the `tls-basic` sample gateway:

  ``` terminal
  $ oc get gateway tls-basic -n openshift-ingress -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` yaml
  status:
    listeners:
    - attachedRoutes: 1
      conditions:
      - lastTransitionTime: "2026-06-24T15:00:00Z"
        message: "The listener is valid"
        observedGeneration: 1
        reason: Accepted
        status: "True"
        type: Accepted
      - lastTransitionTime: "2026-06-24T15:00:00Z"
        message: "The listener is ready to accept traffic"
        observedGeneration: 1
        reason: Programmed
        status: "True"
        type: Programmed
      name: app1-https
      supportedKinds:
      - group: gateway.networking.k8s.io
        kind: HTTPRoute
  ```

  </div>

</div>

# About backend TLS validation

To ensure secure end-to-end encryption, you can use a `BackendTLSPolicy` custom resource (CR) to validate your backend certificates. This validation ensures that your `Gateway` CR securely connects to the correct destination pod.

To use re-encrypt termination in Gateway API, you must combine listener edge termination with a `BackendTLSPolicy` CR attached to the service.

> [!IMPORTANT]
> Re-encrypt for `HTTPRoutes` CRs requires a listener configured with edge termination on the `Gateway` CR and a `BackendTLSPolicy` CR that targets the service.

A `BackendTLSPolicy` CR describes up to 16 targets in the `targetRefs` parameter. The policy also determines how the backend certificate should be validated.

The `BackendTLSPolicy` CR specifies two options to validate backend certificates for a TLS connection. You must configure only one of the following options per policy:

`caCertificateRefs`
Use this option for explicit certificate authority (CA) certificates. The `caCertificateRefs` parameter can refer to up to eight PEM-encoded TLS certificates configured within a config map. The config map must reside in the same namespace as the `BackendTLSPolicy` CR. Cross-namespace references with a `ReferenceGrant` CR are not supported.

`wellKnownCACertificates`
Use this option for trusted system certificates.

The policy also specifies a Server Name Indication (SNI) `hostname` parameter that must match the certificate served by the destination pod unless you also specify a Subject Alternative Name (SAN) `subjectAltNames` parameter. You can specify up to five values in the `subjectAltNames` parameter.

You can use either SNIs or SANs depending on the certificate served by the targeted backend pods. If the pod certificate uses SANs, the `BackendTLSPolicy` CR must have at least one matching value in the `subjectAltNames` parameter to successfully connect using TLS. Each entry in the `subjectAltNames` parameter must include a `type` parameter. You can set the `type` value to either `"hostname"` or Uniform Resource Identifier (`"URI"`). You can specify the SAN itself as a domain name, URI, or a combination of both.

> [!IMPORTANT]
> Gateway API does not automatically evaluate the value of the `hostname` parameter as a SAN. If your certificate requires the hostname to be validated as a SAN, you must explicitly add it as a value in the `subjectAltNames` parameter.

# Configuring re-encrypt termination with a BackendTLSPolicy

To meet strict security requirements, use re-encrypt TLS termination to encrypt traffic from the gateway to your backend services. This ensures end-to-end encryption while allowing gateway payload inspection to route traffic efficiently.

<div>

<div class="title">

Prerequisites

</div>

- You created an edge-terminated listener on your gateway.

- You created an `HTTPRoute` custom resource (CR).

- You created a target backend service.

- If you are using explicit CA certificates, you created a `ConfigMap` object containing the public CA certificate that signed the certificate of your backend service.

</div>

> [!IMPORTANT]
> Re-encrypt for `HTTPRoutes` CRs requires a listener configured with edge termination on the `Gateway` CR and a `BackendTLSPolicy` CR that targets the service.

> [!NOTE]
> The `BackendTLSPolicy` CR must reside in the same namespace as your `HTTPRoute` CR unless you configure a `ReferenceGrant` CR. The `HTTPRoute` CR does not need to reside in the same namespace as your `Gateway` CR, provided the `Gateway` CR is configured to allow routes from other namespaces. Additionally, if you choose to specify a `hostname` parameter in the policy, its value must match the hostname configured in your `HTTPRoute` CR.

<div>

<div class="title">

Procedure

</div>

1.  Create a `BackendTLSPolicy` CR that targets your backend service. Use one of the following configuration options:

    - To use system certificates for re-encrypt termination, set the `wellKnownCACertificates` parameter to the `"System"` value as shown in the following example:

      ``` yaml
      apiVersion: gateway.networking.k8s.io/v1
      kind: BackendTLSPolicy
      metadata:
        name: tls-upstream-dev
        namespace: my-application
      spec:
        targetRefs:
          - kind: Service
            name: dev
            group: ""
        validation:
          wellKnownCACertificates: "System"
          hostname: dev.example.com
      ```

    - To use explicit CA certificates for re-encrypt termination, configure the CR to use your pre-existing `ConfigMap` object, such as `auth-cert` in the following example:

      ``` yaml
      apiVersion: gateway.networking.k8s.io/v1
      kind: BackendTLSPolicy
      metadata:
        name: tls-upstream-auth
        namespace: my-application
      spec:
        targetRefs:
          - kind: Service
            name: auth
            group: ""
        validation:
          caCertificateRefs:
            - kind: ConfigMap
              name: auth-cert
              group: ""
          hostname: "authentication.example.com"
          subjectAltNames:
          - type: "URI"
            uri: "spiffe://authorization.example.com/identity"
      ```

    - To configure re-encrypt termination for a target service that exposes multiple ports and requires different policies, explicitly specify the port name using the `sectionName` parameter. The following example demonstrates this setup within your `targetRefs` configuration:

      > [!IMPORTANT]
      > If you omit the `sectionName` parameter when multiple references target the same service, the `BackendTLSPolicy` CR fails validation or results in a `Conflicted` status.

      ``` yaml
      apiVersion: gateway.networking.k8s.io/v1
      kind: BackendTLSPolicy
      metadata:
        name: tls-upstream-multi-port
        namespace: my-application
      spec:
        targetRefs:
          - kind: Service
            name: my-service
            group: ""
            sectionName: https
        validation:
          wellKnownCACertificates: "System"
          hostname: my-service.example.com
      ```

2.  Apply the policy to your cluster by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `BackendTLSPolicy` CR was accepted by the implementation controller by checking its status. The following example checks the `tls-upstream-dev` sample policy:

  ``` terminal
  $ oc get backendtlspolicy tls-upstream-dev -n my-application -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` yaml
  status:
    conditions:
    - lastTransitionTime: "2026-06-05T20:56:41Z"
      message: Configuration is valid
      observedGeneration: 1
      reason: Accepted
      status: "True"
      type: Accepted
  ```

  </div>

</div>

<div>

<div class="title">

Troubleshooting

</div>

- If the `Accepted` status is set to `False`, check the `reason` parameter. Implementation-specific values, such as `InvalidCACertificateRef` or `Pending`, indicate why the re-encryption failed.

</div>

# Additional resources

- [Routing HTTP requests to services](routing-http-requests-to-services.md#routing-http-requests-to-services)

- [Securing routes](../routes/securing-routes.md#securing-routes)
