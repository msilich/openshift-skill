<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Security overview

It is important to understand how to properly secure various aspects of your OpenShift Container Platform cluster.

## Container security

A good starting point to understanding OpenShift Container Platform security is to review the concepts in [Understanding container security](container_security/security-understanding.md#security-understanding). This and subsequent sections provide a high-level walkthrough of the container security measures available in OpenShift Container Platform, including solutions for the host layer, the container and orchestration layer, and the build and application layer. These sections also include information on the following topics:

- Why container security is important and how it compares with existing security standards.

- Which container security measures are provided by the host (RHCOS and RHEL) layer and which are provided by OpenShift Container Platform.

- How to evaluate your container content and sources for vulnerabilities.

- How to design your build and deployment process to proactively check container content.

- How to control access to containers through authentication and authorization.

- How networking and attached storage are secured in OpenShift Container Platform.

- Containerized solutions for API management and SSO.

## Auditing

OpenShift Container Platform auditing provides a security-relevant chronological set of records documenting the sequence of activities that have affected the system by individual users, administrators, or other components of the system. Administrators can [configure the audit log policy](audit-log-policy-config.md#audit-log-policy-config) and [view audit logs](audit-log-view.md#audit-log-view).

## Certificates

Certificates are used by various components to validate access to the cluster. Administrators can [replace the default ingress certificate](certificates/replacing-default-ingress-certificate.md#replacing-default-ingress), [add API server certificates](certificates/api-server.md#api-server-certificates), or [add a service certificate](certificates/service-serving-certificate.md#add-service-serving).

You can also review more details about the types of certificates used by the cluster:

- [User-provided certificates for the API server](certificate_types_descriptions/user-provided-certificates-for-api-server.md#cert-types-user-provided-certificates-for-the-api-server)

- [Proxy certificates](certificate_types_descriptions/proxy-certificates.md#proxy-certificates)

- [Service CA certificates](certificate_types_descriptions/service-ca-certificates.md#cert-types-service-ca-certificates)

- [Node certificates](certificate_types_descriptions/node-certificates.md#cert-types-node-certificates)

- [Bootstrap certificates](certificate_types_descriptions/bootstrap-certificates.md#cert-types-bootstrap-certificates)

- [etcd certificates](certificate_types_descriptions/etcd-certificates.md#cert-types-etcd-certificates)

- [OLM certificates](certificate_types_descriptions/olm-certificates.md#cert-types-olm-certificates)

- [Aggregated API client certificates](certificate_types_descriptions/aggregated-api-client-certificates.md#cert-types-aggregated-api-client-certificates)

- [Machine Config Operator certificates](certificate_types_descriptions/machine-config-operator-certificates.md#cert-types-machine-config-operator-certificates)

- [User-provided certificates for default ingress](certificate_types_descriptions/user-provided-certificates-for-default-ingress.md#cert-types-user-provided-certificates-for-default-ingress)

- [Ingress certificates](certificate_types_descriptions/ingress-certificates.md#cert-types-ingress-certificates)

- [Monitoring and cluster logging Operator component certificates](certificate_types_descriptions/monitoring-and-cluster-logging-operator-component-certificates.md#cert-types-monitoring-and-cluster-logging-operator-component-certificates)

- [Control plane certificates](certificate_types_descriptions/control-plane-certificates.md#cert-types-control-plane-certificates)

## Encrypting data

You can [enable etcd encryption](../etcd/etcd-encrypt.md#etcd-encrypt) for your cluster to provide an additional layer of data security. For example, it can help protect the loss of sensitive data if an etcd backup is exposed to the incorrect parties.

## Vulnerability scanning

Administrators can use the Red Hat Quay Container Security Operator to run [vulnerability scans](pod-vulnerability-scan.md#pod-vulnerability-scan) and review information about detected vulnerabilities.

# Compliance overview

For many OpenShift Container Platform customers, regulatory readiness, or compliance, on some level is required before any systems can be put into production. That regulatory readiness can be imposed by national standards, industry standards, or the organization’s corporate governance framework.

## Compliance checking

Administrators can use the [Compliance Operator](compliance_operator/co-concepts/compliance-operator-understanding.md#understanding-compliance-operator) to run compliance scans and recommend remediations for any issues found. The [`oc-compliance` plugin](compliance_operator/co-scans/oc-compliance-plug-in-using.md#using-oc-compliance-plug-in) is an OpenShift CLI (`oc`) plugin that provides a set of utilities to easily interact with the Compliance Operator.

## File integrity checking

Administrators can use the [File Integrity Operator](file_integrity_operator/file-integrity-operator-understanding.md#understanding-file-integrity-operator) to continually run file integrity checks on cluster nodes and provide a log of files that have been modified.

# Additional resources

- [Understanding authentication](../authentication/understanding-authentication.md#understanding-authentication)

- [Configuring the internal OAuth server](../authentication/configuring-internal-oauth.md#configuring-internal-oauth)

- [Understanding identity provider configuration](../authentication/understanding-identity-provider.md#understanding-identity-provider)

- [Using RBAC to define and apply permissions](../authentication/using-rbac.md#using-rbac)

- [Managing security context constraints](../authentication/managing-security-context-constraints.md#managing-pod-security-policies)
