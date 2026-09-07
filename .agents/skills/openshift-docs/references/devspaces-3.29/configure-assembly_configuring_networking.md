> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-assembly_configuring_networking). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set up network access for workspaces

Set up network policies, TLS certificates, custom hostnames, and proxy settings so that OpenShift Dev Spaces workspaces communicate securely within your network environment.

By default, OpenShift Dev Spaces auto-detects the cluster domain, generates a self-signed TLS certificate, and allows all workspace pods to communicate freely across namespaces. The procedures in this section override those defaults to match your organization's network requirements.

## What you can configure

- **TLS certificates:** Import your corporate CA chain so the server, dashboard, and workspaces trust connections to proxies, identity providers, and Git hosts. You can also deploy with your own self-signed certificate instead of the auto-generated one.
- **Custom hostnames and domains:** Replace the default cluster-assigned URLs with corporate DNS names for the dashboard and workspace endpoints. Use router sharding when Dev Spaces shares an ingress controller with other applications.
- **Proxy routing:** Route all outbound traffic through an HTTP/HTTPS proxy. Dev Spaces propagates proxy settings to server components and workspace containers through environment variables.
- **Network isolation:** Apply OpenShift NetworkPolicy resources to restrict pod-to-pod traffic between user namespaces. By default, any pod can reach any other pod across namespaces.

## When to configure networking

Configure these settings after installation and before onboarding developers. TLS and proxy settings affect all workspaces; changes require a workspace restart to take effect in existing sessions.

- **[Restrict network traffic between workspaces](configure-proc_configuring_network_policies.md)**  
  Restrict traffic between workspace Pods in different user projects by configuring network policies for multitenant isolation. By default, all Pods in an OpenShift cluster can communicate across namespaces.
- **[Use a custom hostname for the dashboard](configure-proc_configuring_devspaces_hostname.md)**  
  Use a custom hostname for the OpenShift Dev Spaces dashboard instead of the default cluster-assigned URL to align with corporate DNS standards and branding requirements.
- **[Deploy with a self-signed TLS certificate](configure-proc_deploy_with_self_signed_tls_certificate.md)**  
  Deploy OpenShift Dev Spaces with a custom self-signed TLS certificate instead of the automatically generated one. By default, `dsc` creates an OpenShift Job to generate a self-signed certificate automatically.
- **[Trust custom TLS certificates for external services](configure-proc_importing_untrusted_tls_certificates.md)**  
  Trust custom TLS certificate authority (CA) chains for external services in OpenShift Dev Spaces. This enables the server, dashboard, and workspaces to establish trusted encrypted connections to proxies, identity providers, and Git servers.
- **[Route workspace traffic through a shared ingress controller](configure-proc_configuring_openshift_route_for_router_sharding.md)**  
  Route OpenShift Dev Spaces traffic to the correct ingress controller by configuring labels, annotations, and domains for OpenShift Route when using Router Sharding on an OpenShift cluster.
- **[Set a custom domain for workspace URLs](configure-proc_configuring_workspace_endpoints_base_domain.md)**  
  Set a custom base domain for workspace endpoints to align URLs with your organization’s DNS naming conventions. By default, the OpenShift Dev Spaces Operator detects the base domain automatically.
- **[Route traffic through a proxy](configure-proc_configuring_proxy.md)**  
  Route Red Hat OpenShift Dev Spaces traffic through a proxy by creating a Kubernetes Secret for proxy credentials and setting the proxy configuration in the `CheCluster` custom resource. The proxy settings are propagated to the operands and workspaces through environment variables.

**Related concepts**  

- [Control where workspace data is stored](configure-assembly_configuring_storage.md "Control storage classes, strategies, and volume sizes so that workspace data persists reliably and meets your organization’s capacity and performance requirements.")
