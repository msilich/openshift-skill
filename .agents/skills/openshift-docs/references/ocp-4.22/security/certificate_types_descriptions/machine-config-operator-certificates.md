<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Understand Machine Config Operator (MCO) certificates used to secure node connections to the Machine Config Server (MCS) during cluster provisioning, including their lifecycle, rotation, and support boundaries.

# Machine Config Operator certificates overview

Learn how Machine Config Operator (MCO) certificates secure node connections to the Machine Config Server (MCS) during cluster provisioning, so you can plan for certificate maintenance and for troubleshooting node provisioning issues.

This certificate authority (CA) is used to secure connections from nodes to the MCS during initial provisioning.

There are two certificates:

- A self-signed CA, the `machine-config-server-ca` config map (MCS CA).

- A derived certificate, the `machine-config-server-tls` secret (MCS certificate).

## Provisioning details

OpenShift Container Platform installations that use Red Hat Enterprise Linux CoreOS (RHCOS) are installed by using Ignition. This process is split into two parts:

- An Ignition config is created that references a URL for the full configuration served by the MCS.

- For user-provisioned infrastructure installation methods, the Ignition config manifests as a `worker.ign` file created by the `openshift-install` command. For installer-provisioned infrastructure installation methods that use the Machine API Operator, this configuration appears as the `worker-user-data` secret.

> [!IMPORTANT]
> Currently, there is no supported way to block or restrict the machine config server endpoint. The machine config server must be exposed to the network so that newly-provisioned machines, which have no existing configuration or state, are able to fetch their configuration. In this model, the root of trust is the certificate signing requests (CSR) endpoint, which is where the kubelet sends its certificate signing request for approval to join the cluster. Because of this, machine configs should not be used to distribute sensitive information, such as secrets and certificates.
>
> To ensure that the machine config server endpoints, ports 22623 and 22624, are secured in bare metal scenarios, customers must configure proper network policies.

## Provisioning chain of trust

The MCS CA is injected into the Ignition configuration under the `security.tls.certificateAuthorities` configuration field. The MCS then provides the complete configuration using the MCS certificate presented by the web server.

The client validates that the MCS certificate presented by the server has a chain of trust to an authority it recognizes. In this case, the MCS CA is that authority, and it signs the MCS certificate. This ensures that the client is accessing the correct server. The client in this case is Ignition running on a machine in the initial RAM filesystem (initramfs).

# Machine Config Operator certificates reference

Use this reference to locate Machine Config Operator (MCO) certificate key material, rotation requirements, and support boundaries, so you can plan for certificate maintenance and for scheduling rotation before certificates expire.

## Key material inside a cluster

The following objects are stored in the `openshift-machine-config-operator` namespace:

- The Machine Config Server (MCS) certificate authority (CA) bundle is stored as the `machine-config-server-ca` config map. The MCS CA bundle stores all valid CAs for the `MachineConfigServer` TLS certificate.

- The MCS CA signing key is stored as the `machine-config-server-ca` secret. The MCS CA signing key is used to sign the `MachineConfigServer` TLS certificate.

- The MCS certificate is stored as the `machine-config-server-tls` secret, which contains the `MachineConfigServer` TLS certificate and key.

The `machine-config-server-ca` config map is used in the following ways:

- The certificate controller updates the `*-user-data` secrets in the `openshift-machine-api` namespace any time the `machine-config-server-ca` configmap is updated.

- The Machine Config Operator renders the `master-user-data-managed` and `worker-user-data-managed` secrets from the `machine-config-server-ca` configmap.

## Management

At this time, directly modifying either of these certificates is not supported.

## Expiration

The MCS CA and MCS certificate are valid for 10 years and are automatically rotated by the MCO at 8 years.

The issued serving certificates are valid for 10 years.

> [!NOTE]
> This automatic certificate rotation applies only to clusters that use machine sets. For clusters that do not use machine sets, such as vSphere user-provisioned infrastructure clusters, you are required to manually rotate these certificates. For more information on manual certificate rotation, see the Red Hat Knowledgebase article *Regenerating CA certificates for the Machine Config Server*.

## Customization

You cannot customize the MCO certificates.

<div>

<div class="title">

Additional resources

</div>

- [About the Machine Config Operator](../../machine_configuration/index.md#about-machine-config-operator_machine-config-overview)

- [About the OVN-Kubernetes network plugin](../../networking/ovn_kubernetes_network_provider/about-ovn-kubernetes.md#about-ovn-kubernetes)

- [Regenerating CA certificates for the Machine Config Server](https://access.redhat.com/articles/regenerating_cluster_certificates#regenerating-ca-certificates-for-the-machine-config-server-5)

</div>
