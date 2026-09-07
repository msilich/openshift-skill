<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Review user-provided TLS certificates for the API server in OpenShift Container Platform to understand their purpose, location, management, and expiration for external client access.

# Purpose

The API server is accessible by clients external to the cluster at `api.<cluster_name>.<base_domain>`. You might want clients to access the API server at a different hostname or without the need to distribute the cluster-managed certificate authority (CA) certificates to the clients. The administrator must set a custom default certificate to be used by the API server when serving content.

# Location

The user-provided certificates must be provided in a `kubernetes.io/tls` type `Secret` in the `openshift-config` namespace. Update the API server cluster configuration, the `apiserver/cluster` resource, to enable the use of the user-provided certificate.

# Management

User-provided certificates are managed by the user.

# Expiration

API server client certificate expiration is less than five minutes.

# Customization

Update the secret containing the user-managed certificate as needed.

# Additional resources

- [Adding API server certificates](../certificates/api-server.md#api-server-certificates)
