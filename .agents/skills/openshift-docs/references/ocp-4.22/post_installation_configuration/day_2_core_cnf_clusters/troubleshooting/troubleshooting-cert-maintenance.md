<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Certificate maintenance is required for continuous cluster authentication. As a cluster administrator, you must manually renew certain certificates, while others are automatically renewed by the cluster.

Learn about certificates in OpenShift Container Platform and how to maintain them by using the following resources:

- [Which OpenShift certificates do rotate automatically and which do not in Openshift 4.x?](https://access.redhat.com/solutions/5018231)

- [Checking etcd certificate expiry in OpenShift 4](https://access.redhat.com/solutions/7000968)

# Certificates manually managed by the administrator

The following certificates must be renewed by a cluster administrator:

- Proxy certificates

- User-provisioned certificates for the API server

## Managing proxy certificates

Proxy certificates allow users to specify one or more custom certificate authority (CA) certificates that are used by platform components when making egress connections.

> [!NOTE]
> Certain CAs set expiration dates and you might need to renew these certificates every two years.

If you did not originally set the requested certificates, you can determine the certificate expiration in several ways. Most Cloud-native Network Functions (CNFs) use certificates that are not specifically designed for browser-based connectivity. Therefore, you need to pull the certificate from the `ConfigMap` object of your deployment.

<div>

<div class="title">

Procedure

</div>

- To get the expiration date, run the following command against the certificate file:

  ``` terminal
  $ openssl x509 -enddate -noout -in <cert_file_name>.pem
  ```

  For more information about determining how and when to renew your proxy certificates, see "Proxy certificates" in *Security and compliance*.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Proxy certificates](../../../security/certificate_types_descriptions/proxy-certificates.md#proxy-certificates)

</div>

## User-provisioned API server certificates

The API server is accessible by clients that are external to the cluster at `api.<cluster_name>.<base_domain>`. You might want clients to access the API server at a different hostname or without the need to distribute the cluster-managed certificate authority (CA) certificates to the clients. You must set a custom default certificate to be used by the API server when serving content.

For more information, see "User-provided certificates for the API server" in *Security and compliance*

<div>

<div class="title">

Additional resources

</div>

- [User-provisioned certificates for the API server](../../../security/certificate_types_descriptions/user-provided-certificates-for-api-server.md#cert-types-user-provided-certificates-for-the-api-server)

</div>

# Certificates managed by the cluster

You only need to check cluster-managed certificates if you detect an issue in the logs. The following certificates are automatically managed by the cluster:

- Service CA certificates

- Node certificates

- Bootstrap certificates

- etcd certificates

- OLM certificates

- Machine Config Operator certificates

- Monitoring and cluster logging Operator component certificates

- Control plane certificates

- Ingress certificates

<div>

<div class="title">

Additional resources

</div>

- [Service CA certificates](../../../security/certificate_types_descriptions/service-ca-certificates.md#cert-types-service-ca-certificates_cert-types-service-ca-certificates)

- [Node certificates](../../../security/certificate_types_descriptions/node-certificates.md#cert-types-node-certificates_cert-types-node-certificates)

- [Bootstrap certificates](../../../security/certificate_types_descriptions/bootstrap-certificates.md#cert-types-bootstrap-certificates_cert-types-bootstrap-certificates)

- [etcd certificates](../../../security/certificate_types_descriptions/etcd-certificates.md#cert-types-etcd-certificates-cert-types-etcd-certificates)

- [OLM certificates](../../../security/certificate_types_descriptions/olm-certificates.md#cert-types-olm-certificates_cert-types-olm-certificates)

- [Machine Config Operator certificates](../../../security/certificate_types_descriptions/machine-config-operator-certificates.md#cert-types-machine-config-operator-certificates_cert-types-machine-config-operator-certificates)

- [Monitoring and cluster logging Operator component certificates](../../../security/certificate_types_descriptions/monitoring-and-cluster-logging-operator-component-certificates.md#cert-types-monitoring-and-cluster-logging-operator-component-certificates_cert-types-monitoring-and-cluster-logging-operator-component-certificates)

- [Control plane certificates](../../../security/certificate_types_descriptions/control-plane-certificates.md#cert-types-control-plane-certificates_cert-types-control-plane-certificates)

- [Ingress certificates](../../../security/certificate_types_descriptions/ingress-certificates.md#cert-types-ingress-certificates_cert-types-ingress-certificates)

</div>

## Certificates managed by etcd

The etcd certificates are used for encrypted communication between etcd member peers as well as encrypted client traffic. The certificates are renewed automatically within the cluster provided that communication between all nodes and all services is current. Therefore, if your cluster might lose communication between components during a specific period of time, which is close to the end of the etcd certificate lifetime, it is recommended to renew the certificate in advance. For example, communication can be lost during an upgrade due to nodes rebooting at different times.

- You can manually renew etcd certificates by running the following command:

  ``` terminal
  $ for each in $(oc get secret -n openshift-etcd | grep "kubernetes.io/tls" | grep -e \
  "etcd-peer\|etcd-serving" | awk '{print $1}'); do oc get secret $each -n openshift-etcd -o \
  jsonpath="{.data.tls\.crt}" | base64 -d | openssl x509 -noout -enddate; done
  ```

For more information about updating etcd certificates, see [Checking etcd certificate expiry in OpenShift 4](https://access.redhat.com/solutions/7000968). For more information about etcd certificates, see "etcd certificates" in *Security and compliance*.

<div>

<div class="title">

Additional resources

</div>

- [etcd certificates](../../../security/certificate_types_descriptions/etcd-certificates.md#cert-types-etcd-certificates_cert-types-etcd-certificates)

</div>

## Node certificates

Node certificates are self-signed certificates, which means that they are signed by the cluster and they originate from an internal certificate authority (CA) that is generated by the bootstrap process.

After the cluster is installed, the cluster automatically renews the node certificates.

For more information, see "Node certificates" in *Security and compliance*.

<div>

<div class="title">

Additional resources

</div>

- [Node certificates](../../../security/certificate_types_descriptions/node-certificates.md#cert-types-node-certificates_cert-types-node-certificates)

</div>

## Service CA certificates

The `service-ca` is an Operator that creates a self-signed certificate authority (CA) when an OpenShift Container Platform cluster is deployed. This allows user to add certificates to their deployments without manually creating them. Service CA certificates are self-signed certificates.

For more information, see "Service CA certificates" in *Security and compliance*.

<div>

<div class="title">

Additional resources

</div>

- [Service CA certificates](../../../security/certificate_types_descriptions/service-ca-certificates.md#cert-types-service-ca-certificates_cert-types-service-ca-certificates)

</div>
