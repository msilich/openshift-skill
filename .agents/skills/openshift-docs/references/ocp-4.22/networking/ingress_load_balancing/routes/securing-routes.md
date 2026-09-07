<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To secure application traffic, you can configure routes to serve custom certificates to clients by using edge, passthrough, or re-encrypt TLS termination, aand manage externally provided certificates. Additionally, you can enforce strict security protocols by securing a route with HTTP strict transport security (HSTS).

# Creating an edge route with a custom certificate

To secure traffic by using a custom certificate, configure a route with edge TLS termination by running the `oc create route` command. This configuration terminates encryption at the Ingress Controller before forwarding traffic to the destination pod.

The route specifies the TLS certificate and key that the Ingress Controller uses for the route.

The procedure creates a `Route` resource with a custom certificate and edge TLS termination. The procedure assumes that the certificate/key pair are in the `tls.crt` and `tls.key` files in the current working directory. You may also specify a CA certificate if needed to complete the certificate chain. Substitute the actual path names for `tls.crt`, `tls.key`, and (optionally) `ca.crt`. Substitute the name of the service that you want to expose for `frontend`. Substitute the appropriate hostname for `www.example.com`.

<div>

<div class="title">

Prerequisites

</div>

- You must have a certificate/key pair in PEM-encoded files, where the certificate is valid for the route host.

- You might have a separate CA certificate in a PEM-encoded file that completes the certificate chain.

- You must have a service that you want to expose.

</div>

> [!NOTE]
> Password protected key files are not supported. To remove a passphrase from a key file, use the following command:
>
> ``` terminal
> $ openssl rsa -in password_protected_tls.key -out tls.key
> ```

<div>

<div class="title">

Procedure

</div>

- Create a secure `Route` resource using edge TLS termination and a custom certificate.

  ``` terminal
  $ oc create route edge --service=frontend --cert=tls.crt --key=tls.key --ca-cert=ca.crt --hostname=www.example.com
  ```

  If you examine the resulting `Route` resource, the resource should have a configuration similar to the following example:

  <div class="formalpara">

  <div class="title">

  YAML Definition of the Secure Route

  </div>

  ``` yaml
  apiVersion: route.openshift.io/v1
  kind: Route
  metadata:
    name: frontend
  spec:
    host: www.example.com
    to:
      kind: Service
      name: frontend
    tls:
      termination: edge
      key: |-
        -----BEGIN PRIVATE KEY-----
        [...]
        -----END PRIVATE KEY-----
      certificate: |-
        -----BEGIN CERTIFICATE-----
        [...]
        -----END CERTIFICATE-----
      caCertificate: |-
        -----BEGIN CERTIFICATE-----
        [...]
        -----END CERTIFICATE-----
  # ...
  ```

  </div>

  See `oc create route edge --help` for more options.

</div>

# Creating a re-encrypt route with a custom certificate

To secure traffic by using a custom certificate, configure a route with re-encrypt TLS termination by running the `oc create route` command. This configuration enables the Ingress Controller to decrypt traffic, and then re-encrypt traffic before forwarding the traffic to the destination pod.

The procedure creates a `Route` resource with a custom certificate and reencrypt TLS termination. The procedure assumes that the certificate/key pair are in the `tls.crt` and `tls.key` files in the current working directory. You must also specify a destination CA certificate to enable the Ingress Controller to trust the service’s certificate. You may also specify a CA certificate if needed to complete the certificate chain. Substitute the actual path names for `tls.crt`, `tls.key`, `cacert.crt`, and (optionally) `ca.crt`. Substitute the name of the `Service` resource that you want to expose for `frontend`. Substitute the appropriate hostname for `www.example.com`.

<div>

<div class="title">

Prerequisites

</div>

- You must have a certificate/key pair in PEM-encoded files, where the certificate is valid for the route host.

- You may have a separate CA certificate in a PEM-encoded file that completes the certificate chain.

- You must have a separate destination CA certificate in a PEM-encoded file.

- You must have a service that you want to expose.

</div>

> [!NOTE]
> Password protected key files are not supported. To remove a passphrase from a key file, use the following command:
>
> ``` terminal
> $ openssl rsa -in password_protected_tls.key -out tls.key
> ```

<div>

<div class="title">

Procedure

</div>

- Create a secure `Route` resource using reencrypt TLS termination and a custom certificate:

  ``` terminal
  $ oc create route reencrypt --service=frontend --cert=tls.crt --key=tls.key --dest-ca-cert=destca.crt --ca-cert=ca.crt --hostname=www.example.com
  ```

  If you examine the resulting `Route` resource, the resource should have a configuration similar to the following example:

  <div class="formalpara">

  <div class="title">

  YAML Definition of the Secure Route

  </div>

  ``` yaml
  apiVersion: route.openshift.io/v1
  kind: Route
  metadata:
    name: frontend
  spec:
    host: www.example.com
    to:
      kind: Service
      name: frontend
    tls:
      termination: reencrypt
      key: |-
        -----BEGIN PRIVATE KEY-----
        [...]
        -----END PRIVATE KEY-----
      certificate: |-
        -----BEGIN CERTIFICATE-----
        [...]
        -----END CERTIFICATE-----
      caCertificate: |-
        -----BEGIN CERTIFICATE-----
        [...]
        -----END CERTIFICATE-----
      destinationCACertificate: |-
        -----BEGIN CERTIFICATE-----
        [...]
        -----END CERTIFICATE-----
  # ...
  ```

  </div>

  See `oc create route reencrypt --help` for more options.

</div>

# Creating a passthrough route

To send encrypted traffic directly to the destination without decryption at the router, configure a route with passthrough termination by running the `oc create route` command. This configuration requires no key or certificate on the route, as the destination pod handles TLS termination.

<div>

<div class="title">

Prerequisites

</div>

- You must have a service that you want to expose.

</div>

<div>

<div class="title">

Procedure

</div>

- Create a `Route` resource:

  ``` terminal
  $ oc create route passthrough route-passthrough-secured --service=frontend --port=8080
  ```

  If you examine the resulting `Route` resource, it should look similar to the following:

  <div class="formalpara">

  <div class="title">

  A Secured Route Using Passthrough Termination

  </div>

  ``` yaml
  apiVersion: route.openshift.io/v1
  kind: Route
  metadata:
    name: route-passthrough-secured
  spec:
    host: www.example.com
    port:
      targetPort: 8080
    tls:
      termination: passthrough
      insecureEdgeTerminationPolicy: None
    to:
      kind: Service
      name: frontend
  ```

  </div>

  where:

  `metadata.name`
  Specifies the name of the object, which is limited to 63 characters.

  `tls.termination`
  Specifies the `termination` field is set to `passthrough`. This is the only required `tls` field.

  `tls.insecureEdgeTerminationPolicy`
  Specifies the type of edge termination policy. Optional parameter. The only valid values are `None`, `Redirect`, or empty for disabled.

  The destination pod is responsible for serving certificates for the traffic at the endpoint. This is currently the only method that can support requiring client certificates, also known as two-way authentication.

</div>

# Creating a route with externally managed certificates

You can configure OpenShift Container Platform routes with third-party certificate management solutions by using the `.spec.tls.externalCertificate` field of the route API. You can reference externally managed TLS certificates via secrets, eliminating the need for manual certificate management.

By using the externally managed certificate, you can reduce errors to ensure a smoother rollout of certificate updates and enable the OpenShift Container Platform router to serve renewed certificates promptly. You can use externally managed certificates with both edge routes and re-encrypt routes.

<div>

<div class="title">

Prerequisites

</div>

- You must have a secret containing a valid certificate or key pair in PEM-encoded format of type `kubernetes.io/tls`, which includes both `tls.key` and `tls.crt` keys. Example command: `$ oc create secret tls myapp-tls --cert=server.crt --key=server.key`.

  > [!IMPORTANT]
  > Note the following considerations for externally managed certificates:
  >
  > - When using `externalCertificate`, the router does not automatically pull a CA bundle from the secret. If your route requires a specific `tls.caCertificate` (for example, for client authentication or re-encryption), you must either provide it manually in the `Route` spec or bundle the full certificate chain directly into the `tls.crt` entry of the secret.
  >
  > - The Ingress Controller uses `SubjectAccessReview` to load external certificates. This means the ability of the router to serve the certificate is tied to the route creator’s permissions on that secret. If the user’s permissions are revoked, the router will eventually lose its lease on that certificate, and the route status will reflect a validation failure.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `role` object in the same namespace as the secret to allow the router service account read access by running the following command:

    ``` terminal
    $ oc create role secret-reader --verb=get,list,watch --resource=secrets --resource-name=<secret-name> \
    --namespace=<current-namespace>
    ```

    Where:

    `<secret-name>`
    Specifies the actual name of your secret.

    `<current-namespace>`
    Specifies the namespace where both your secret and route reside.

2.  Create a `rolebinding` object in the same namespace as the secret and bind the router service account to the newly created role by running the following command:

    ``` terminal
    $ oc create rolebinding secret-reader-binding --role=secret-reader --serviceaccount=openshift-ingress:router --namespace=<current-namespace>
    ```

    Where:

    `<current-namespace>`
    Specifies the namespace where both your secret and route reside.

3.  Create a YAML file that defines the `route` and specifies the secret containing your certificate using the following example.

    <div class="formalpara">

    <div class="title">

    YAML definition of the secure route

    </div>

    ``` yaml
    apiVersion: route.openshift.io/v1
    kind: Route
    metadata:
      name: myedge
      namespace: test
    spec:
      host: myedge-test.apps.example.com
      tls:
        externalCertificate:
          name: <secret-name>
        termination: edge
        [...]
    [...]
    ```

    </div>

    Where:

    `<secret-name>`
    Specifies the actual name of your secret.

4.  Create a `route` resource by running the following command:

    ``` terminal
    $ oc apply -f <route.yaml>
    ```

    Where:

    `<route.yaml>`
    Specifies the generated YAML filename.

    If the secret exists and has a certificate/key pair, the router will serve the generated certificate if all prerequisites are met.

    > [!NOTE]
    > If `.spec.tls.externalCertificate` is not provided, the router uses default generated certificates.
    >
    > You cannot provide the `.spec.tls.certificate` field or the `.spec.tls.key` field when using the `.spec.tls.externalCertificate` field.

</div>

<div class="formalpara">

<div class="title">

Troubleshooting

</div>

If your route is not serving the externally managed certificate, check the route’s status conditions by running the following command:

</div>

``` terminal
$ oc describe route <route-name> -n <route-namespace>
```

Look for the following specific failure reasons in the output to diagnose the issue without needing to consult the router logs:

- `ExternalCertificateGetFailed`: Indicates an RBAC or `SubjectAccessReview` issue. Verify that the route creator has the correct permissions to read the secret and that the `RoleBinding` is properly configured.

- `ExternalCertificateValidationFailed`: Indicates that the secret exists but is the wrong type. Ensure the secret was explicitly created as type `kubernetes.io/tls` and contains both the `tls.key` and `tls.crt` keys.

# HTTP Strict Transport Security

To enhance security and optimize website performance, use the HTTP Strict Transport Security (HSTS) policy. This mechanism signals browsers to use only HTTPS traffic on the route host, eliminating the need for HTTP redirects and speeding up user interactions.

When HSTS policy is enforced, HSTS adds a Strict Transport Security header to HTTP and HTTPS responses from the site. You can use the `insecureEdgeTerminationPolicy` value in a route to redirect HTTP to HTTPS. When HSTS is enforced, the client changes all requests from the HTTP URL to HTTPS before the request is sent, eliminating the need for a redirect.

Cluster administrators can configure HSTS to do the following:

- Enable HSTS per-route

- Disable HSTS per-route

- Enforce HSTS per-domain, for a set of domains, or use namespace labels in combination with domains

> [!IMPORTANT]
> HSTS works only with secure routes, either edge-terminated or re-encrypt. The configuration is ineffective on HTTP or passthrough routes.

## Enable HTTP Strict Transport Security per-route

To enforce secure HTTPS connections for specific applications, enable HTTP Strict Transport Security (HSTS) on a per-route basis. Applying the `haproxy.router.openshift.io/hsts_header` annotation to edge and re-encrypt routes ensures that browsers reject unencrypted traffic.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster with a user with administrator privileges for the project.

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- To enable HSTS on a route, add the `haproxy.router.openshift.io/hsts_header` value to the edge-terminated or re-encrypt route. You can use the `oc annotate` tool to do this by running the following command. To properly run the command, ensure that the semicolon (`;`) in the `haproxy.router.openshift.io/hsts_header` route annotation is also surrounded by double quotation marks (`""`).

  <div class="formalpara">

  <div class="title">

  Example `annotate` command that sets the maximum age to `31536000` ms (approximately 8.5 hours)

  </div>

  ``` terminal
  $ oc annotate route <route_name> -n <namespace> --overwrite=true "haproxy.router.openshift.io/hsts_header=max-age=31536000;\
  includeSubDomains;preload"
  ```

  </div>

  <div class="formalpara">

  <div class="title">

  Example route configured with an annotation

  </div>

  ``` yaml
  apiVersion: route.openshift.io/v1
  kind: Route
  metadata:
    annotations:
      haproxy.router.openshift.io/hsts_header: max-age=31536000;includeSubDomains;preload
  # ...
  spec:
    host: def.abc.com
    tls:
      termination: "reencrypt"
      ...
    wildcardPolicy: "Subdomain"
  # ...
  ```

  </div>

  where:

  `max-age`
  Specifies the measurement of the length of time, in seconds, for the HSTS policy. If set to `0`, it negates the policy.

  `includeSubDomains`
  Specifies that all subdomains of the host must have the same HSTS policy as the host. Optional parameter.

  `preload`
  Specifies that the site is included in the HSTS preload list when `max-age` is greater than `0`. For example, sites such as Google can construct a list of sites that have `preload` set. Browsers can then use these lists to determine which sites they can communicate with over HTTPS, even before they have interacted with the site. Without `preload` set, browsers must have interacted with the site over HTTPS, at least once, to get the header. Optional parameter.

</div>

## Disable HTTP Strict Transport Security per-route

To allow unencrypted connections or troubleshoot access issues, disable HTTP Strict Transport Security (HSTS) for a specific route. Setting the `max-age` route annotation to `0` instructs browsers to stop enforcing HTTPS requirements on the route host.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster with a user with administrator privileges for the project.

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- To disable HSTS, enter the following to set the `max-age` value in the route annotation to `0`:

  ``` terminal
  $ oc annotate route <route_name> -n <namespace> --overwrite=true "haproxy.router.openshift.io/hsts_header"="max-age=0"
  ```

  > [!TIP]
  > You can alternatively apply the following YAML to create the config map for disabling HSTS per-route:
  >
  > ``` yaml
  > kind: Route
  > apiVersion: route.openshift.io/v1
  > metadata:
  >   annotations:
  >     haproxy.router.openshift.io/hsts_header: max-age=0
  > ```

- To disable HSTS for every route in a namespace, enter the following command:

  ``` terminal
  $ oc annotate route --all -n <namespace> --overwrite=true "haproxy.router.openshift.io/hsts_header"="max-age=0"
  ```

</div>

<div>

<div class="title">

Verification

</div>

- To query the annotation for all routes, enter the following command:

  ``` terminal
  $ oc get route  --all-namespaces -o go-template='{{range .items}}{{if .metadata.annotations}}{{$a := index .metadata.annotations "haproxy.router.openshift.io/hsts_header"}}{{$n := .metadata.name}}{{with $a}}Name: {{$n}} HSTS: {{$a}}{{"\n"}}{{else}}{{""}}{{end}}{{end}}{{end}}'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Name: routename HSTS: max-age=0
  ```

  </div>

</div>

## Enforcing HTTP Strict Transport Security per-domain

To enforce HTTP Strict Transport Security (HSTS) per-domain for secure routes, add a `requiredHSTSPolicies` record to the Ingress spec to capture the configuration of the HSTS policy.

If you configure a `requiredHSTSPolicy` to enforce HSTS, then any newly created route must be configured with a compliant HSTS policy annotation.

> [!NOTE]
> To handle upgraded clusters with non-compliant HSTS routes, you can update the manifests at the source and apply the updates.

> [!NOTE]
> You cannot use `oc expose route` or `oc create route` commands to add a route in a domain that enforces HSTS, because the API for these commands does not accept annotations.

> [!IMPORTANT]
> HSTS cannot be applied to insecure, or non-TLS routes, even if HSTS is requested for all routes globally.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the cluster with a user with administrator privileges for the project.

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the Ingress configuration YAML by running the following command and updating fields as needed:

    ``` terminal
    $ oc edit ingresses.config.openshift.io/cluster
    ```

    <div class="formalpara">

    <div class="title">

    Example HSTS policy

    </div>

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Ingress
    metadata:
      name: cluster
    spec:
      domain: 'hello-openshift-default.apps.username.devcluster.openshift.com'
      requiredHSTSPolicies:
      - domainPatterns:
        - '*hello-openshift-default.apps.username.devcluster.openshift.com'
        - '*hello-openshift-default2.apps.username.devcluster.openshift.com'
        namespaceSelector:
          matchLabels:
            myPolicy: strict
        maxAge:
          smallestMaxAge: 1
          largestMaxAge: 31536000
        preloadPolicy: RequirePreload
        includeSubDomainsPolicy: RequireIncludeSubDomains
      - domainPatterns:
        - 'abc.example.com'
        - '*xyz.example.com'
        namespaceSelector:
          matchLabels: {}
        maxAge: {}
        preloadPolicy: NoOpinion
        includeSubDomainsPolicy: RequireNoIncludeSubDomains
    ```

    </div>

    - Required. `requiredHSTSPolicies` are validated in order, and the first matching `domainPatterns` applies.

    - Required. You must specify at least one `domainPatterns` hostname. Any number of domains can be listed. You can include multiple sections of enforcing options for different `domainPatterns`.

    - Optional. If you include `namespaceSelector`, it must match the labels of the project where the routes reside, to enforce the set HSTS policy on the routes. Routes that only match the `namespaceSelector` and not the `domainPatterns` are not validated.

    - Required. `max-age` measures the length of time, in seconds, that the HSTS policy is in effect. This policy setting allows for a smallest and largest `max-age` to be enforced.

      - The `largestMaxAge` value must be between `0` and `2147483647`. It can be left unspecified, which means no upper limit is enforced.

      - The `smallestMaxAge` value must be between `0` and `2147483647`. Enter `0` to disable HSTS for troubleshooting, otherwise enter `1` if you never want HSTS to be disabled. It can be left unspecified, which means no lower limit is enforced.

    - Optional. Including `preload` in `haproxy.router.openshift.io/hsts_header` allows external services to include this site in their HSTS preload lists. Browsers can then use these lists to determine which sites they can communicate with over HTTPS, before they have interacted with the site. Without `preload` set, browsers need to interact at least once with the site to get the header. `preload` can be set with one of the following:

      - `RequirePreload`: `preload` is required by the `RequiredHSTSPolicy`.

      - `RequireNoPreload`: `preload` is forbidden by the `RequiredHSTSPolicy`.

      - `NoOpinion`: `preload` does not matter to the `RequiredHSTSPolicy`.

    - Optional. `includeSubDomainsPolicy` can be set with one of the following:

      - `RequireIncludeSubDomains`: `includeSubDomains` is required by the `RequiredHSTSPolicy`.

      - `RequireNoIncludeSubDomains`: `includeSubDomains` is forbidden by the `RequiredHSTSPolicy`.

      - `NoOpinion`: `includeSubDomains` does not matter to the `RequiredHSTSPolicy`.

2.  You can apply HSTS to all routes in the cluster or in a particular namespace by entering the `oc annotate command`.

    - To apply HSTS to all routes in the cluster, enter the `oc annotate command`. For example:

      ``` terminal
      $ oc annotate route --all --all-namespaces --overwrite=true "haproxy.router.openshift.io/hsts_header"="max-age=31536000"
      ```

    - To apply HSTS to all routes in a particular namespace, enter the `oc annotate command`. For example:

      ``` terminal
      $ oc annotate route --all -n my-namespace --overwrite=true "haproxy.router.openshift.io/hsts_header"="max-age=31536000"
      ```

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

You can review the HSTS policy you configured. For example:

</div>

- To review the `maxAge` set for required HSTS policies, enter the following command:

  ``` terminal
  $ oc get clusteroperator/ingress -n openshift-ingress-operator -o jsonpath='{range .spec.requiredHSTSPolicies[*]}{.spec.requiredHSTSPolicies.maxAgePolicy.largestMaxAge}{"\n"}{end}'
  ```

- To review the HSTS annotations on all routes, enter the following command:

  ``` terminal
  $ oc get route  --all-namespaces -o go-template='{{range .items}}{{if .metadata.annotations}}{{$a := index .metadata.annotations "haproxy.router.openshift.io/hsts_header"}}{{$n := .metadata.name}}{{with $a}}Name: {{$n}} HSTS: {{$a}}{{"\n"}}{{else}}{{""}}{{end}}{{end}}{{end}}'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Name: <_routename_> HSTS: max-age=31536000;preload;includeSubDomains
  ```

  </div>
