<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can secure a route with HTTP strict transport security (HSTS).

# HTTP Strict Transport Security

To enhance security and optimize website performance, use the HTTP Strict Transport Security (HSTS) policy. This mechanism signals browsers to use only HTTPS traffic on the route host, eliminating the need for HTTP redirects and speeding up user interactions.

When HSTS policy is enforced, HSTS adds a Strict Transport Security header to HTTP and HTTPS responses from the site. You can use the `insecureEdgeTerminationPolicy` value in a route to redirect HTTP to HTTPS. When HSTS is enforced, the client changes all requests from the HTTP URL to HTTPS before the request is sent, eliminating the need for a redirect.

Cluster administrators can configure HSTS to do the following:

- Enable HSTS per-route

- Disable HSTS per-route

- Enforce HSTS per-domain, for a set of domains, or use namespace labels in combination with domains

> [!IMPORTANT]
> HSTS works only with secure routes, either edge-terminated or re-encrypt. The configuration is ineffective on HTTP or passthrough routes.

## Enabling HTTP Strict Transport Security per-route

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

## Disabling HTTP Strict Transport Security per-route

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
