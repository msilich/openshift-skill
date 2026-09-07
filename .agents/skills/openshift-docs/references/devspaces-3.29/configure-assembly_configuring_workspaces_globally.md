> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-assembly_configuring_workspaces_globally). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set workspace policies for all users

Set workspace limits, Git certificate trust, node scheduling, allowed URLs, and container capabilities that apply to every developer on the platform.

Workspace policies are cluster-wide settings in the CheCluster custom resource that override individual developer preferences. They take effect immediately for new workspaces and on next restart for running workspaces.

## What you can control

- **Resource limits:** Cap the number of workspaces each developer can keep, and limit how many workspaces can run simultaneously across the cluster. These policies prevent resource exhaustion on shared infrastructure.
- **Security and trust:** Inject self-signed Git server certificates so workspaces can clone from enterprise Git hosts over TLS. Restrict which repository URLs are allowed to create workspaces, blocking untrusted sources. Grant container capabilities for nested container builds when required.
- **Scheduling and placement:** Control which nodes run workspace pods using node selectors and tolerations. Use this to isolate developer workloads on dedicated nodes or specific availability zones.

## Where policies are defined

All workspace policies are fields in the `CheCluster` custom resource under `spec.devEnvironments`. Changes applied with `oc patch` or through the OpenShift web console take effect without restarting the Dev Spaces server.

- **[Limit the number of workspaces that a user can keep](configure-proc_limiting_workspaces_per_user.md)**  
  Limit the number of workspaces a user can keep in the dashboard to reduce demand on the cluster. By default, users can keep an unlimited number of workspaces.
- **[Limit the number of workspaces that all users can run simultaneously](configure-proc_limiting_workspaces_per_cluster.md)**  
  Limit the number of concurrently running workspaces across the cluster to manage resource consumption. By default, all users can run an unlimited number of workspaces.
- **[Enable users to run multiple workspaces simultaneously](configure-proc_enabling_multiple_workspaces_simultaneously.md)**  
  Enable users to run multiple workspaces simultaneously so that they can work on several projects without stopping active sessions. By default, a user can run only one workspace at a time.
- **[Trust self-signed Git server certificates](configure-proc_git_with_self_signed_certificates.md)**  
  Trust self-signed certificates from Git providers by configuring OpenShift Dev Spaces so that workspaces can clone and push to repositories secured by internal certificate authorities.
- **[Control which nodes run workspaces](configure-proc_configuring_workspaces_nodeselector.md)**  
  Control which nodes run OpenShift Dev Spaces workspace Pods by setting `nodeSelector` and tolerations for compliance, hardware affinity, or zone isolation.
- **[Restrict which URLs can create workspaces](configure-proc_configuring_allowed_urls_for_cde.md)**  
  Restrict Cloud Development Environment (CDE) initiation to authorized source URLs, protecting your infrastructure from untrusted deployments.
- **[Run nested containers in workspaces](configure-proc_enabling_container_run_capabilities.md)**  
  Run nested containers in OpenShift Dev Spaces workspaces using tools like Podman. This feature uses Linux kernel user namespaces for isolation, so that users can build and run container images within their workspaces.

**Related information**  

- [Set up network access for workspaces](configure-assembly_configuring_networking.md)
- [Control where workspace data is stored](configure-assembly_configuring_storage.md)
