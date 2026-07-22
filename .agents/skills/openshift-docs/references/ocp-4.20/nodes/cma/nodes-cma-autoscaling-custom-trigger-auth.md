<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

A trigger authentication allows you to include authentication information in a scaled object or a scaled job that can be used by the associated containers. You can use trigger authentications to pass OpenShift Container Platform secrets, platform-native pod authentication mechanisms, environment variables, and so on.

You define a `TriggerAuthentication` object in the same namespace as the object that you want to scale. That trigger authentication can be used only by objects in that namespace.

Alternatively, to share credentials between objects in multiple namespaces, you can create a `ClusterTriggerAuthentication` object that can be used across all namespaces.

Trigger authentications and cluster trigger authentication use the same configuration. However, a cluster trigger authentication requires an additional `kind` parameter in the authentication reference of the scaled object.

<div class="formalpara">

<div class="title">

Example trigger authentication that uses a bound service account token

</div>

``` yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: secret-triggerauthentication
  namespace: my-namespace
spec:
  boundServiceAccountToken:
    - parameter: bearerToken
      serviceAccountName: thanos
```

</div>

- Specifies the namespace of the object you want to scale.

- Specifies that this trigger authentication uses a bound service account token for authorization when connecting to the metrics endpoint.

- Specifies the name of the service account to use.

<div class="formalpara">

<div class="title">

Example cluster trigger authentication that uses a bound service account token

</div>

``` yaml
kind: ClusterTriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: bound-service-account-token-triggerauthentication
spec:
  boundServiceAccountToken:
    - parameter: bearerToken
      serviceAccountName: thanos
```

</div>

- Specifies the namespace of the object you want to scale.

- Specifies that this cluster trigger authentication uses a bound service account token for authorization when connecting to the metrics endpoint.

- Specifies the name of the service account to use.

<div class="formalpara">

<div class="title">

Example trigger authentication that uses a secret for Basic authentication

</div>

``` yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: secret-triggerauthentication
  namespace: my-namespace
spec:
  secretTargetRef:
  - parameter: username
    name: my-basic-secret
    key: username
  - parameter: password
    name: my-basic-secret
    key: password
```

</div>

- Specifies the namespace of the object you want to scale.

- Specifies that this trigger authentication uses a secret for authorization when connecting to the metrics endpoint.

- Specifies the authentication parameter to supply by using the secret.

- Specifies the name of the secret to use. See the following example secret for Basic authentication.

- Specifies the key in the secret to use with the specified parameter.

<div class="formalpara">

<div class="title">

Example secret for Basic authentication

</div>

``` yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-basic-secret
  namespace: default
data:
  username: "dXNlcm5hbWU="
  password: "cGFzc3dvcmQ="
```

</div>

- User name and password to supply to the trigger authentication. The values in the `data` stanza must be base-64 encoded.

<div class="formalpara">

<div class="title">

Example trigger authentication that uses a secret for CA details

</div>

``` yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: secret-triggerauthentication
  namespace: my-namespace
spec:
  secretTargetRef:
    - parameter: key
      name: my-secret
      key: client-key.pem
    - parameter: ca
      name: my-secret
      key: ca-cert.pem
```

</div>

- Specifies the namespace of the object you want to scale.

- Specifies that this trigger authentication uses a secret for authorization when connecting to the metrics endpoint.

- Specifies the type of authentication to use.

- Specifies the name of the secret to use.

- Specifies the key in the secret to use with the specified parameter.

- Specifies the authentication parameter for a custom CA when connecting to the metrics endpoint.

- Specifies the name of the secret to use. See the following example secret with certificate authority (CA) details.

- Specifies the key in the secret to use with the specified parameter.

<div class="formalpara">

<div class="title">

Example secret with certificate authority (CA) details

</div>

``` yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
  namespace: my-namespace
data:
  ca-cert.pem: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0...
  client-cert.pem: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0...
  client-key.pem: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0t...
```

</div>

- Specifies the TLS CA Certificate for authentication of the metrics endpoint. The value must be base-64 encoded.

- Specifies the TLS certificates and key for TLS client authentication. The values must be base-64 encoded.

<div class="formalpara">

<div class="title">

Example trigger authentication that uses a bearer token

</div>

``` yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: token-triggerauthentication
  namespace: my-namespace
spec:
  secretTargetRef:
  - parameter: bearerToken
    name: my-secret
    key: bearerToken
```

</div>

- Specifies the namespace of the object you want to scale.

- Specifies that this trigger authentication uses a secret for authorization when connecting to the metrics endpoint.

- Specifies the type of authentication to use.

- Specifies the name of the secret to use. See the following example secret for a bearer token.

- Specifies the key in the token to use with the specified parameter.

<div class="formalpara">

<div class="title">

Example secret for a bearer token

</div>

``` yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
  namespace: my-namespace
data:
  bearerToken: "<bearer_token>"
```

</div>

- Specifies a bearer token to use with bearer authentication. The value must be base-64 encoded.

<div class="formalpara">

<div class="title">

Example trigger authentication that uses an environment variable

</div>

``` yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: env-var-triggerauthentication
  namespace: my-namespace
spec:
  env:
  - parameter: access_key
    name: ACCESS_KEY
    containerName: my-container
```

</div>

- Specifies the namespace of the object you want to scale.

- Specifies that this trigger authentication uses environment variables for authorization when connecting to the metrics endpoint.

- Specify the parameter to set with this variable.

- Specify the name of the environment variable.

- Optional: Specify a container that requires authentication. The container must be in the same resource as referenced by `scaleTargetRef` in the scaled object.

<div class="formalpara">

<div class="title">

Example trigger authentication that uses pod authentication providers

</div>

``` yaml
kind: TriggerAuthentication
apiVersion: keda.sh/v1alpha1
metadata:
  name: pod-id-triggerauthentication
  namespace: my-namespace
spec:
  podIdentity:
    provider: aws-eks
```

</div>

- Specifies the namespace of the object you want to scale.

- Specifies that this trigger authentication uses a platform-native pod authentication when connecting to the metrics endpoint.

- Specifies a pod identity. Supported values are `none`, `azure`, `gcp`, `aws-eks`, or `aws-kiam`. The default is `none`.

<div>

<div class="title">

Additional resources

</div>

- [Understanding and creating service accounts](../../authentication/understanding-and-creating-service-accounts.md#understanding-service-accounts)

- [Providing sensitive data to pods](../pods/nodes-pods-secrets.md#nodes-pods-secrets).

</div>

# Using trigger authentications

You use trigger authentications and cluster trigger authentications by using a custom resource to create the authentication, then add a reference to a scaled object or scaled job.

<div>

<div class="title">

Prerequisites

</div>

- The Custom Metrics Autoscaler Operator must be installed.

- If you are using a bound service account token, the service account must exist.

- If you are using a bound service account token, a role-based access control (RBAC) object that enables the Custom Metrics Autoscaler Operator to request service account tokens from the service account must exist.

  ``` yaml
  apiVersion: rbac.authorization.k8s.io/v1
  kind: Role
  metadata:
    name: keda-operator-token-creator
    namespace: <namespace_name>
  rules:
  - apiGroups:
    - ""
    resources:
    - serviceaccounts/token
    verbs:
    - create
    resourceNames:
    - thanos
  ---
  apiVersion: rbac.authorization.k8s.io/v1
  kind: RoleBinding
  metadata:
    name: keda-operator-token-creator-binding
    namespace: <namespace_name>
  roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: Role
    name: keda-operator-token-creator
  subjects:
  - kind: ServiceAccount
    name: keda-operator
    namespace: openshift-keda
  ```

  - Specifies the namespace of the service account.

  - Specifies the name of the service account.

  - Specifies the namespace of the service account.

- If you are using a secret, the `Secret` object must exist.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `TriggerAuthentication` or `ClusterTriggerAuthentication` object.

    1.  Create a YAML file that defines the object:

        <div class="formalpara">

        <div class="title">

        Example trigger authentication with a bound service account token

        </div>

        ``` yaml
        kind: TriggerAuthentication
        apiVersion: keda.sh/v1alpha1
        metadata:
          name: prom-triggerauthentication
          namespace: my-namespace
          spec:
          boundServiceAccountToken:
            - parameter: token
              serviceAccountName: thanos
        ```

        </div>

        - Specifies the namespace of the object you want to scale.

        - Specifies that this trigger authentication uses a bound service account token for authorization when connecting to the metrics endpoint.

        - Specifies the name of the service account to use.

    2.  Create the `TriggerAuthentication` object:

        ``` terminal
        $ oc create -f <filename>.yaml
        ```

2.  Create or edit a `ScaledObject` YAML file that uses the trigger authentication:

    1.  Create a YAML file that defines the object by running the following command:

        <div class="formalpara">

        <div class="title">

        Example scaled object with a trigger authentication

        </div>

        ``` yaml
        apiVersion: keda.sh/v1alpha1
        kind: ScaledObject
        metadata:
          name: scaledobject
          namespace: my-namespace
        spec:
          scaleTargetRef:
            name: example-deployment
          maxReplicaCount: 100
          minReplicaCount: 0
          pollingInterval: 30
          triggers:
          - type: prometheus
            metadata:
              serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
              namespace: kedatest # replace <NAMESPACE>
              metricName: http_requests_total
              threshold: '5'
              query: sum(rate(http_requests_total{job="test-app"}[1m]))
              authModes: "basic"
            authenticationRef:
              name: prom-triggerauthentication
              kind: TriggerAuthentication
        ```

        </div>

        - Specify the name of your trigger authentication object.

        - Specify `TriggerAuthentication`. `TriggerAuthentication` is the default.

          <div class="formalpara">

          <div class="title">

          Example scaled object with a cluster trigger authentication

          </div>

          ``` yaml
          apiVersion: keda.sh/v1alpha1
          kind: ScaledObject
          metadata:
            name: scaledobject
            namespace: my-namespace
          spec:
            scaleTargetRef:
              name: example-deployment
            maxReplicaCount: 100
            minReplicaCount: 0
            pollingInterval: 30
            triggers:
            - type: prometheus
              metadata:
                serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
                namespace: kedatest # replace <NAMESPACE>
                metricName: http_requests_total
                threshold: '5'
                query: sum(rate(http_requests_total{job="test-app"}[1m]))
                authModes: "basic"
              authenticationRef:
                name: prom-cluster-triggerauthentication
                kind: ClusterTriggerAuthentication
          ```

          </div>

        - Specify the name of your trigger authentication object.

        - Specify `ClusterTriggerAuthentication`.

    2.  Create the scaled object by running the following command:

        ``` terminal
        $ oc apply -f <filename>
        ```

</div>
