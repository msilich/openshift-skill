<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Web terminal and network policies

The web terminal might fail to start if the cluster has network policies configured. To start a web terminal instance, the Web Terminal Operator must communicate with the web terminal’s pod to verify it is running, and the OpenShift Container Platform web console needs to send information to automatically log in to the cluster within the terminal. If either step fails, the web terminal fails to start and the terminal panel is in a loading state until a `context deadline exceeded error` occurs.

To avoid this issue, ensure that the network policies for namespaces that are used for terminals allow ingress from the `openshift-console` and `openshift-operators` namespaces.

The following samples show `NetworkPolicy` objects for allowing ingress from the `openshift-console` and `openshift-operators` namespaces.

<div class="formalpara">

<div class="title">

Allowing ingress from the `openshift-console` namespace

</div>

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-openshift-console
spec:
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-console
  podSelector: {}
  policyTypes:
  - Ingress
```

</div>

<div class="formalpara">

<div class="title">

Allowing ingress from the `openshift-operators` namespace

</div>

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-from-openshift-operators
spec:
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: openshift-operators
  podSelector: {}
  policyTypes:
  - Ingress
```

</div>
