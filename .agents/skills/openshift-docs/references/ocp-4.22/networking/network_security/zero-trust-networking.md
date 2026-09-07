<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Zero trust is an approach to designing security architectures based on the premise that every interaction begins in an untrusted state. This contrasts with traditional architectures, which might determine trustworthiness based on whether communication starts inside a firewall. More specifically, zero trust attempts to close gaps in security architectures that rely on implicit trust models and one-time authentication.

OpenShift Container Platform can add some zero trust networking capabilities to containers running on the platform without requiring changes to the containers or the software running in them. There are also several products that Red Hat offers that can further augment the zero trust networking capabilities of containers. If you have the ability to change the software running in the containers, then there are other projects that Red Hat supports that can add further capabilities.

Explore the following targeted capabilities of zero trust networking.

# Root of trust

Public certificates and private keys are critical to zero trust networking. These are used to identify components to one another, authenticate, and to secure traffic. The certificates are signed by other certificates, and there is a chain of trust to a root certificate authority (CA). Everything participating in the network needs to ultimately have the public key for a root CA so that it can validate the chain of trust. For public-facing things, these are usually the set of root CAs that are globally known, and whose keys are distributed with operating systems, web browsers, and so on. However, it is possible to run a private CA for a cluster or a corporation if the certificate of the private CA is distributed to all parties.

Leverage:

- OpenShift Container Platform: OpenShift creates a [cluster CA at installation](../../security/certificate_types_descriptions/bootstrap-certificates.md#cert-types-bootstrap-certificates) that is used to secure the cluster resources. However, OpenShift Container Platform can also create and sign [certificates for services](../../security/certificates/service-serving-certificate.md#add-service-serving) in the cluster, and can inject the cluster CA bundle into a pod if requested. [Service certificates](../../security/certificate_types_descriptions/service-ca-certificates.md#cert-types-service-ca-certificates) created and signed by OpenShift Container Platform have a 26-month time to live (TTL) and are rotated automatically at 13 months. They can also be rotated manually if necessary.

- [OpenShift cert-manager Operator](../../security/cert_manager_operator/index.md#cert-manager-operator-about): cert-manager allows you to request keys that are signed by an external root of trust. There are many configurable issuers to integrate with external issuers, along with ways to run with a delegated signing certificate. The cert-manager API can be used by other software in zero trust networking to request the necessary certificates (for example, Red Hat OpenShift Service Mesh), or can be used directly by customer software.

# Traffic authentication and encryption

Ensure that all traffic on the wire is encrypted and the endpoints are identifiable. An example of this is Mutual TLS, or mTLS, which is a method for mutual authentication.

Leverage:

- OpenShift Container Platform: With transparent [pod-to-pod IPsec](configuring-ipsec-ovn.md#pod-to-pod-ipsec_configuring-ipsec-ovn), the source and destination of the traffic can be identified by the IP address. There is the capability for egress traffic to be [encrypted using IPsec](configuring-ipsec-ovn.md#nw-ovn-ipsec-north-south-enable_configuring-ipsec-ovn). By using the [egress IP](../ovn_kubernetes_network_provider/configuring-egress-ips-ovn.md#configuring-egress-ips-ovn) feature, the source IP address of the traffic can be used to identify the source of the traffic inside the cluster.

- [Red Hat OpenShift Service Mesh](../../service_mesh/v2x/ossm-about.md#ossm-about): Provides powerful [mTLS capabilities](../../service_mesh/v2x/ossm-security.md#ossm-security-mtls_ossm-security) that can transparently augment traffic leaving a pod to provide authentication and encryption.

- [OpenShift cert-manager Operator](../../security/cert_manager_operator/index.md#cert-manager-operator-about): Use custom resource definitions (CRDs) to request certificates that can be mounted for your programs to use for SSL/TLS protocols.

# Identification and authentication

After you have the ability to mint certificates using a CA, you can use it to establish trust relationships by verification of the identity of the other end of a connection — either a user or a client machine. This also requires management of certificate lifecycles to limit use if compromised.

Leverage:

- OpenShift Container Platform: Cluster-signed [service certificates](../../security/certificates/service-serving-certificate.md#add-service-serving) to ensure that a client is talking to a trusted endpoint. This requires that the service uses SSL/TLS and that the client uses the [cluster CA](../../security/certificates/service-serving-certificate.md#add-service-certificate-configmap_service-serving-certificate). The client identity must be provided using some other means.

- [Red Hat Single Sign-On](../../security/container_security/security-platform.md#security-platform-red-hat-sso_security-platform): Provides request authentication integration with enterprise user directories or third-party identity providers.

- [Red Hat OpenShift Service Mesh](../../service_mesh/v2x/ossm-about.md#ossm-about): [Transparent upgrade](../../service_mesh/v2x/ossm-architecture.md#ossm-architecture) of connections to mTLS, auto-rotation, custom certificate expiration, and request authentication with JSON web token (JWT).

- [OpenShift cert-manager Operator](../../security/cert_manager_operator/index.md#cert-manager-operator-about): Creation and management of certificates for use by your application. Certificates can be controlled by CRDs and mounted as secrets, or your application can be changed to interact directly with the cert-manager API.

# Inter-service authorization

It is critical to be able to control access to services based on the identity of the requester. This is done by the platform and does not require each application to implement it. That allows better auditing and inspection of the policies.

Leverage:

- OpenShift Container Platform: Can enforce isolation in the networking layer of the platform using the Kubernetes [`NetworkPolicy`](network_policy/about-network-policy.md#about-network-policy) and [`AdminNetworkPolicy`](AdminNetworkPolicy/ovn-k-anp.md#ovn-k-anp) objects.

- [Red Hat OpenShift Service Mesh](../../service_mesh/v2x/ossm-about.md#ossm-about): Sophisticated L4 and L7 [control of traffic](../../service_mesh/v2x/ossm-security.md#ossm-security) using standard Istio objects and using mTLS to identify the source and destination of traffic and then apply policies based on that information.

# Transaction-level verification

In addition to the ability to identify and authenticate connections, it is also useful to control access to individual transactions. This can include rate-limiting by source, observability, and semantic validation that a transaction is well formed.

Leverage:

- [Red Hat OpenShift Service Mesh](../../service_mesh/v2x/ossm-about.md#ossm-about): Perform L7 inspection of requests, rejecting malformed HTTP requests, transaction-level [observability and reporting](../../service_mesh/v2x/ossm-architecture.md#understanding-kiali). Service Mesh can also provide [request-based authentication](../../service_mesh/v2x/ossm-security.md#restrict-access-with-json-web-token) using JWT.

# Risk assessment

As the number of security policies in a cluster increase, visualization of what the policies allow and deny becomes increasingly important. These tools make it easier to create, visualize, and manage cluster security policies.

Leverage:

- [Red Hat OpenShift Service Mesh](../../service_mesh/v2x/ossm-about.md#ossm-about): Create and visualize Kubernetes `NetworkPolicy` and `AdminNetworkPolicy`, and OpenShift Networking `EgressFirewall` objects using the [OpenShift web console](../../web_console/web-console-overview.md#web-console-overview).

- [Red Hat Advanced Cluster Security for Kubernetes](https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security-kubernetes): Advanced [visualization of objects](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_security_for_kubernetes/4.3/html/operating/index).

# Site-wide policy enforcement and distribution

After deploying applications on a cluster, it becomes challenging to manage all of the objects that make up the security rules. It becomes critical to be able to apply site-wide policies and audit the deployed objects for compliance with the policies. This should allow for delegation of some permissions to users and cluster administrators within defined bounds, and should allow for exceptions to the policies if necessary.

Leverage:

- [Red Hat OpenShift Service Mesh](../../service_mesh/v2x/ossm-about.md#ossm-about): RBAC to [control policy object](../../security/container_security/security-platform.md#security-platform-multi-tenancy_security-platform)s and delegate control.

- [Red Hat Advanced Cluster Security for Kubernetes](https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security-kubernetes): [Policy enforcement](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_security_for_kubernetes/4.1/html/operating/manage-security-policies#doc-wrapper) engine.

- [Red Hat Advanced Cluster Management (RHACM) for Kubernetes](https://www.redhat.com/en/technologies/management/advanced-cluster-management): Centralized policy control.

# Observability for constant, and retrospective, evaluation

After you have a running cluster, you want to be able to observe the traffic and verify that the traffic comports with the defined rules. This is important for intrusion detection, forensics, and is helpful for operational load management.

Leverage:

- [Network Observability Operator](../../observability/network_observability/installing-operators.md#installing-network-observability-operators): Allows for inspection, monitoring, and alerting on network connections to pods and nodes in the cluster.

- [Red Hat Advanced Cluster Management (RHACM) for Kubernetes](https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security-kubernetes): Monitors, collects, and evaluates system-level events such as process execution, network connections and flows, and privilege escalation. It can determine a baseline for a cluster, and then detect anomalous activity and alert you about it.

- [Red Hat OpenShift Service Mesh](../../service_mesh/v2x/ossm-about.md#ossm-about): Can [monitor traffic](../../service_mesh/v2x/ossm-architecture.md#ossm-kiali-overview_ossm-architecture) entering and leaving a pod.

- [Red Hat OpenShift Distributed Tracing Platform](../../service_mesh/v2x/ossm-architecture.md#understanding-distributed-tracing): For suitably instrumented applications, you can see all traffic associated with a particular action as it splits into sub-requests to microservices. This allows you to identify bottlenecks within a distributed application.

# Endpoint security

It is important to be able to trust that the software running the services in your cluster has not been compromised. For example, you might need to ensure that certified images are run on trusted hardware, and have policies to only allow connections to or from an endpoint based on endpoint characteristics.

Leverage:

- OpenShift Container Platform: Secureboot can ensure that the nodes in the cluster are running trusted software, so the platform itself (including the container runtime) have not been tampered with. You can configure OpenShift Container Platform to only run images that have been [signed by certain signatures](../../security/container_security/security-container-signature.md#security-container-signature).

- [Red Hat Trusted Artifact Signer](https://catalog.redhat.com/software/container-stacks/detail/6525b71aa53de2eb01ac9628): This can be used in a trusted build chain and produce signed container images.

# Extending trust outside of the cluster

You might want to extend trust outside of the cluster by allowing a cluster to mint CAs for a subdomain. Alternatively, you might want to attest to workload identity in the cluster to a remote endpoint.

Leverage:

- [OpenShift cert-manager Operator](../../security/cert_manager_operator/index.md#cert-manager-operator-about): You can use cert-manager to manage delegated CAs so that you can distribute trust across different clusters, or through your organization.

- [Red Hat OpenShift Service Mesh](../../service_mesh/v2x/ossm-about.md#ossm-about): Can use SPIFFE to provide remote attestation of workloads to endpoints running in remote or local clusters.
