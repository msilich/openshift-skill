<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure automatic or manual DNS record management for Gateway API resources to provide predictable network addresses for incoming traffic.

# DNS management requirements for Gateway API

The Ingress Operator manages DNS records for Gateway API resources when deployed in the `openshift-ingress` namespace. This automatic management applies only when specific namespace and domain conditions are met.

The Ingress Operator creates DNS records from hostnames specified in `spec.listeners[*].hostname` on the `Gateway` resource. The Operator does not create DNS records from hostnames specified only on route resources. Listeners without a hostname do not receive an automatically managed DNS record.

To enable automatic DNS record creation and lifecycle management for Gateway API resources, ensure you meet the following criteria:

- You ensured that the cluster DNS configuration defines at least one managed public or private DNS zone.

- You created the `Gateway` custom resource (CR) in the `openshift-ingress` namespace.

- You ensured that the listener hostnames must fall under the cluster base domain. To inspect the base domain of your cluster, enter the following command:

  ``` terminal
  $ oc get dns.config.openshift.io cluster -o jsonpath='{.spec.baseDomain}'
  ```

- You ensured that another Gateway does not use the listener hostname; otherwise, the Gateway reports `DNSReady=False` and does not publish a DNS record.

If you create the `Gateway` object in any other namespace, note the following limitations:

- The Ingress Operator does not provision or manage DNS records for the Gateway.

- You must manually configure and manage DNS records for all hostnames associated with that Gateway.

# Automatic DNS management

When you deploy a `Gateway` object in the `openshift-ingress` namespace to use automatic DNS management, you must configure listener route attachment rules to support multi-namespace deployments.

> [!NOTE]
> Setting the `spec.listeners[*].allowedRoutes.namespaces.from` field to `Same` on a Gateway in the `openshift-ingress` namespace restricts route attachment to that namespace. If you do not set that field, the Gateway defaults to this same behavior and only accepts route attachments from its own namespace. If you deploy `HTTPRoute`, `GRPCRoute` or `TLSRoute` objects in user namespaces, you cannot attach routes to the Gateway.

The following example creates a Gateway in the `openshift-ingress` namespace with a listener hostname under the cluster base domain, enabling automatic DNS management. The example also sets the `allowedRoutes.namespaces.from` field to `Selector` to allow route attachment from labeled application namespaces.

``` yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: managed-dns-gateway
  namespace: openshift-ingress
spec:
  gatewayClassName: openshift-gateway-manager
  listeners:
  - name: https
    hostname: "*.gwapi.<domain>"
    port: 443
    protocol: HTTPS
    tls:
      mode: Terminate
      certificateRefs:
      - name: gwapi-wildcard
    allowedRoutes:
      namespaces:
        from: Selector
        selector:
          matchLabels:
            gateway-access: "true"
```

where:

`metadata.namespace`
Deploying in `openshift-ingress` enables automatic DNS record management by the Ingress Operator.

`spec.listeners.hostname`
Replace `<domain>` with your cluster base domain. You can run the following command to get your domain name:

``` terminal
$ oc get dns.config.openshift.io cluster -o jsonpath='{.spec.baseDomain}'
```

`spec.listeners.allowedRoutes.namespaces.from`
Configured to `Selector` (or `All`) so route resources in designated application namespaces can attach. `Same` is not supported for cross-namespace application routes.

When you deploy a `Gateway` in the `openshift-ingress` namespace, the Ingress Operator automatically provisions DNS records for each listener hostname. You can verify that DNS is configured correctly by checking the `DNSReady` condition on the `Gateway` resource:

``` terminal
$ oc -n openshift-ingress get gateway managed-dns-gateway -o jsonpath='{.status.conditions[?(@.type=="DNSReady")]}' | jq
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` json
{
  "lastTransitionTime": "2025-01-15T12:00:00Z",
  "message": "All the listeners have DNS ready",
  "reason": "AllListenersReady",
  "status": "True",
  "type": "DNSReady"
}
```

</div>

If `DNSReady` is `False`, inspect the listener-level conditions for specific failure reasons. For more information, see "Verifying Gateway infrastructure status".

# Additional resources

- [Provisioning your own DNS records](../../../installing/installing_gcp/installing-gcp-customizations.md#installation-gcp-provisioning-own-dns-records_installing-gcp-customizations)
