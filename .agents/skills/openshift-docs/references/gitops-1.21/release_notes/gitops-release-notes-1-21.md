<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Release notes contain information about new and deprecated features, breaking changes, fixed issues, and known issues. The following release notes apply to the most recent OpenShift GitOps releases on OpenShift Container Platform.

Red Hat OpenShift GitOps is a declarative way to implement continuous deployment for cloud native applications. Red Hat OpenShift GitOps ensures consistency in applications when you deploy them to different clusters in different environments, such as development, staging, and production. Red Hat OpenShift GitOps helps you automate the following tasks:

- Ensure that the clusters have similar states for configuration, monitoring, and storage.

- Recover or recreate clusters from a known state.

- Apply or revert configuration changes to multiple OpenShift Container Platform clusters.

- Associate templated configuration with different environments.

- Promote applications across clusters, from staging to production.

For an overview of Red Hat OpenShift GitOps, see [About Red Hat OpenShift GitOps](../understanding_openshift_gitops/about-redhat-openshift-gitops.md#about-redhat-openshift-gitops).

> [!NOTE]
> For additional information about the OpenShift GitOps lifecycle and supported platforms, refer to the [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators) and [Red Hat OpenShift Container Platform Life Cycle Policy](https://access.redhat.com/support/policy/updates/openshift).

# Compatibility and support matrix

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use.

> [!IMPORTANT]
> Technology Preview features in this table is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

In the table, features are marked with the following statuses:

- **TP**: *Technology Preview*

- **GA**: *General Availability*

- **NA**: *Not Applicable*

<div class="important">

<div class="title">

</div>

- In OpenShift Container Platform 4.13, the `stable` channel has been removed. Before upgrading to OpenShift Container Platform 4.13, if you are already on the `stable` channel, choose the appropriate channel and switch to it.

- The maintenance support for OpenShift Container Platform 4.12 on IBM Power has ended from 17 July 2024. If you are using Red Hat OpenShift GitOps on OpenShift Container Platform 4.12, upgrade to OpenShift Container Platform 4.13 or later.

</div>

| GitOps | Argo CD CLI | Helm | Kustomize | Argo CD | Argo Rollouts | Dex | Argo CD Agent | Argo CD Image Updater | OpenShift Container Platform |
|----|----|----|----|----|----|----|----|----|----|
| 1.21.0 | 3.4.3 GA | 3.19.4 GA | 5.8.1 GA | 3.4.3 GA | 1.9.0 GA | 2.45.0 GA | 0.9.0 GA | 1.2.1 GA | 4.14, 4.16-4.22 |
| 1.20.0 | 3.3.2 TP | 3.19.4 GA | 5.8.1 GA | 3.3.2 GA | 1.8.4 GA | 2.43.1 GA | 0.7.0 GA | 1.1.2 TP | 4.14, 4.16-4.21 |
| 1.19.0 | 3.1.9 TP | 3.18.4 GA | 5.7.0 GA | 3.1.9 GA | 1.8.3 GA | 2.43.0 GA | 0.5.3 GA | 1.0.4 TP | 4.14, 4.16-4.21 |

GitOps and component versions

<div class="important">

<div class="title">

</div>

- Starting from Red Hat OpenShift GitOps 1.18, support is no longer provided for Keycloak-based authentication. As an alternative, you can migrate to Dex or configure a self-managed Red Hat Build of Keycloak (RHBK) instance.

</div>

## Technology Preview features

The features mentioned in the following table are currently in Technology Preview (TP). These experimental features are not intended for production use.

| Feature | TP in Red Hat OpenShift GitOps versions | GA in Red Hat OpenShift GitOps versions |
|----|----|----|
| Argo CD Agent | 1.17.0 | 1.19.0 |
| Argo CD Image Updater | 1.18.0 | 1.21.0 |
| The GitOps `argocd` CLI tool | 1.12.0 | 1.21.0 |
| Argo CD application sets in non-control plane namespaces | 1.12.0 | NA |
| The `round-robin` cluster sharding algorithm | 1.10.0 | NA |
| Dynamic scaling of shards | 1.10.0 | NA |
| Argo Rollouts | 1.9.0 | 1.13.0 |
| ApplicationSet Progressive Sync Strategy | 1.8.0 | NA |
| Multiple sources for an application | 1.8.0 | 1.15.0 |
| Argo CD applications in non-control plane namespaces | 1.7.0 | 1.13.0 |
| The Red Hat OpenShift GitOps **Environments** page in the **Developer** perspective of the OpenShift Container Platform web console | 1.1.0 | NA |

Technology Preview tracker

> [!NOTE]
> The `ApplicationSet Progressive Sync Strategy` feature name aligns with the upstream naming convention and replaces the earlier name, `ApplicationSet Progressive Rollout Strategy`, used in previous Red Hat OpenShift GitOps versions. The functionality remains unchanged.

# Release notes for Red Hat OpenShift GitOps 1.21.4

Red Hat OpenShift GitOps 1.21.4 is now available on OpenShift Container Platform 4.18, 4.19, 4.20, 4.21, and 4.22.

## Errata updates

RHSA-2026:63142 - Red Hat OpenShift GitOps 1.21.4 enhancement update advisory
Issued: 2026-09-03

The list of enhancements that are included in this release is documented in the following advisory:

- [RHSA-2026:63142](https://access.redhat.com/errata/RHSA-2026:63142)

If you have installed the Red Hat OpenShift GitOps Operator in the default namespace, run the following command to view the container images in this release:

``` terminal
$ oc describe deployment gitops-operator-controller-manager -n openshift-gitops-operator
```

## Fixed issues

OpenShift login succeeds when NamespaceManagement CR targets an unauthorized namespace
Before this update, OpenShift login to Argo CD failed with an `unauthorized_client` error when a `NamespaceManagement` custom resource (CR) existed for a namespace that Argo CD was not configured to manage. With this update, OpenShift login succeeds even when a `NamespaceManagement` CR targets a namespace that Argo CD is not allowed to manage.

[GITOPS-10477](https://redhat.atlassian.net/browse/GITOPS-10477)

# Release notes for Red Hat OpenShift GitOps 1.21.3

Red Hat OpenShift GitOps 1.21.3 is now available on OpenShift Container Platform 4.18, 4.19, 4.20, 4.21, and 4.22.

## Errata updates

RHBA-2026:54873 - Red Hat OpenShift GitOps 1.21.3 enhancement update advisory
Issued: 2026-08-14

The list of enhancements that are included in this release is documented in the following advisory:

- [RHBA-2026:54873](https://access.redhat.com/errata/RHBA-2026:54873)

If you have installed the Red Hat OpenShift GitOps Operator in the default namespace, run the following command to view the container images in this release:

``` terminal
$ oc describe deployment gitops-operator-controller-manager -n openshift-gitops-operator
```

## Fixed issues

Redis container image updated to the latest version
Before this update, the Red Hat OpenShift GitOps Operator used an outdated Redis container image that contained multiple known issues. With this update, the Operator uses the latest Redis container image, which includes security patches and dependency updates.

[GITOPS-10464](https://redhat.atlassian.net/browse/GITOPS-10464)

# Release notes for Red Hat OpenShift GitOps 1.21.2

Red Hat OpenShift GitOps 1.21.2 is now available on OpenShift Container Platform 4.18, 4.19, 4.20, 4.21, and 4.22.

## Errata updates

RHBA-2026:52859 - Red Hat OpenShift GitOps 1.21.2 enhancement update advisory
Issued: 2026-08-10

The list of enhancements that are included in this release is documented in the following advisory:

- [RHBA-2026:52859](https://access.redhat.com/errata/RHBA-2026:52859)

If you have installed the Red Hat OpenShift GitOps Operator in the default namespace, run the following command to view the container images in this release:

``` terminal
$ oc describe deployment gitops-operator-controller-manager -n openshift-gitops-operator
```

## Fixed issues

Custom `GODEBUG` environment variable values on FIPS-enabled clusters
Before this update, running the Red Hat OpenShift GitOps Operator on a FIPS-enabled cluster prevented setting custom `GODEBUG` environment variable values because the Operator used `GODEBUG` internally to enable FIPS at runtime. With this update, it is possible to set custom values for the `GODEBUG` environment variable.

> [!NOTE]
> When overriding `GODEBUG`, ensure your custom string retains the required FIPS runtime flags, such as `fips140=on`, to maintain FIPS compliance.

[GITOPS-10507](https://redhat.atlassian.net/browse/GITOPS-10507)

`ignoreDifferences` rules for individual array elements
Before this update, `ignoreDifferences` rules could not be applied to individual array elements in resources managed by Argo CD. With this update, Argo CD respects `ignoreDifferences` configurations for matching elements within resource arrays.

[GITOPS-7994](https://redhat.atlassian.net/browse/GITOPS-7994)

`aggregationRule` removal during `ServerSideApply` for `ClusterRole` resources
Before this update, when managing `ClusterRole` resources by using Argo CD and applying custom labels, conflicting field ownership could cause the `aggregationRule` field to be removed when using `ServerSideApply`. With this update, the `aggregationRule` field is preserved during `ServerSideApply`, preventing its removal.

[GITOPS-7957](https://redhat.atlassian.net/browse/GITOPS-7957)

Source namespace role reconciliation failure for terminating namespaces
Before this update, when `spec.sourceNamespaces` included a namespace in the `Terminating` state, the Operator attempted to create or update roles in that namespace. Because Kubernetes rejects resource creation in a terminating namespace, the Argo CD reconciliation failed and prevented the remaining source namespaces from being reconciled. With this update, the Operator skips source namespaces with a `DeletionTimestamp` during role reconciliation, consistent with the existing behavior for managed namespaces.

[GITOPS-10508](https://redhat.atlassian.net/browse/GITOPS-10508)

## Known issues

Kustomize 5.8.x namespace propagation issue for Helm-generated resources
In Red Hat OpenShift GitOps 1.21, the bundled Kustomize versions 5.8.0 and 5.8.1 contain an upstream issue that prevents namespace propagation for Helm-generated resources. If your applications rely on Kustomize to set `metadata.namespace` for resources generated from Helm charts, the generated resources do not include a namespace. As a result, application synchronization fails with an `InvalidSpecError`.

As a workaround, configure the Argo CD custom resource (CR) to use Kustomize v5.7.1, which is not affected by this issue.

1.  Add the Kustomize v5.7.1 binary to the `repo-server` pod by configuring the `spec.repo.initContainers`, `spec.repo.volumes`, and `spec.repo.volumeMounts` fields in the Argo CD CR.

2.  Add the custom Kustomize version to the Argo CD CR by configuring the `spec.kustomizeVersions` field:

    ``` yaml
       spec:
        kustomizeVersions:
        - version: v5.7.1
          path: /custom-tools/kustomize_5_7_1
    ```

3.  Set `kustomize.version: v5.7.1` in the affected `Application` resources to use the custom Kustomize version.

    [GITOPS-10444](https://redhat.atlassian.net/browse/GITOPS-10444)

# Release notes for Red Hat OpenShift GitOps 1.21.1

Red Hat OpenShift GitOps 1.21.1 is available on OpenShift Container Platform 4.18, 4.19, 4.20, 4.21, and 4.22.

## Errata updates

RHSA-2026:35995 - Red Hat OpenShift GitOps 1.21.1 enhancement update advisory
Issued: 2026-07-06

The list of enhancements that are included in this release is documented in the following advisory:

- [RHSA-2026:35995](https://access.redhat.com/errata/RHSA-2026:35995)

If you have installed the Red Hat OpenShift GitOps Operator in the default namespace, run the following command to view the container images in this release:

``` terminal
$ oc describe deployment gitops-operator-controller-manager -n openshift-gitops-operator
```

## Fixed issues

Redis HA replication failure resolved
Before this update, when Redis `ha.enabled` is `true`, Redis HA replicas started without `masterauth` in their configuration, causing every replication attempt to fail with `NOAUTH Authentication required`. With `min-replicas-to-write 1` set in `redis.conf`, the master then rejected all writes with `NOREPLICAS Not enough good replicas to write`, making the Argo CD UI and all write operations fail. With this update, the Red Hat OpenShift GitOps Operator sets `masterauth` in `redis.conf` during startup of pods. As a result, Redis replicas do not show any `NOAUTH Authentication required` errors and Argo CD UI functionality works without any issues.

[GITOPS-10178](https://redhat.atlassian.net/browse/GITOPS-10178)

Prometheus metrics scraping fixed for Red Hat OpenShift GitOps Operator
Before this update, Prometheus Operator made HTTPS calls to scrape the metrics, but after removing `kube-rbac-proxy`, Red Hat OpenShift GitOps Operator HTTPS handling was misconfigured, causing `targetDown` alerts in the OpenShift Container Platform web console. With this update, the issue is fixed by properly handling HTTPS connections for Red Hat OpenShift GitOps Operator to scrape the metrics. As a result, there are no `targetDown` alerts firing in the OpenShift Container Platform web console.

[GITOPS-10273](https://redhat.atlassian.net/browse/GITOPS-10273)

Argo CD Image Updater goroutine leak fixed
Before this update, when running Argo CD Image Updater with `git` write-back method under heavy load, especially with a large number of applications and short poll intervals, the Image Updater experienced goroutine thread leaks. This caused subsequent Git operations to fail with `error: cannot fork() for remote-https: Resource temporarily unavailable`. With this update, the `argocd-image-updater-controller` reuses a shared informer factory and avoids unnecessary creation of goroutines without leaks. As a result, Git operations work reliably under heavy load.

[GITOPS-9938](https://redhat.atlassian.net/browse/GITOPS-9938)

Self-hosted Quay registry URL handling fixed in Image Updater
Before this update, when using a self-hosted Quay container registry, the Image Updater incorrectly used the public Quay registry URL (`quay.io`) rather than the configured URL for the self-hosted registry. With this update, the Image Updater correctly extracts the configured registry URL and uses it when processing webhook events from the source registry. As a result, self-hosted Quay registries work correctly with Image Updater.

[GITOPS-9971](https://redhat.atlassian.net/browse/GITOPS-9971)

Web terminal permissions fixed
Before this update, permissions were missing to access the web terminal from the Argo CD UI. With this update, the issue is fixed by providing the necessary permissions for accessing the web terminal from the Argo CD UI. As a result, users can access the web-based terminal from the Argo CD UI when `spec.webTerminalEnabled` is `true`.

[GITOPS-10083](https://redhat.atlassian.net/browse/GITOPS-10083)

# Release notes for Red Hat OpenShift GitOps 1.21.0

Red Hat OpenShift GitOps 1.21.0 is available on OpenShift Container Platform 4.14, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21, and 4.22.

## Errata updates

RHEA-2026:28967 - Red Hat OpenShift GitOps 1.21.0 enhancement update advisory
Issued: 2026-06-24

The enhancements included in this release are documented in the following advisory:

- [RHEA-2026:28967](https://access.redhat.com/errata/RHEA-2026:28967)

If you installed the Red Hat OpenShift GitOps Operator in the default namespace, run the following command to view the container images in this release:

``` terminal
$ oc describe deployment gitops-operator-controller-manager -n openshift-gitops-operator
```

## New features

Argo CD Image Updater (General Availability)
With this update, Argo CD Image Updater is generally available. It updates container images automatically for Kubernetes workloads managed by Argo CD. It tracks image versions in applications. You can define these versions in `ImageUpdater` custom resources (CR). It updates images using parameter overrides through the Argo CD API or the Git write-back method. The Image Updater supports applications built with Kustomize or Helm.

[GITOPS-9754](https://redhat.atlassian.net/browse/GITOPS-9754)

Argo CD CLI (General Availability)
With this update, the Argo CD CLI is generally available. It provides a stable command-line interface for managing Argo CD applications and related resources. Use the CLI to perform common GitOps operations.

[GITOPS-9379](https://redhat.atlassian.net/browse/GITOPS-9379)

GitOps Console Plugin resource pages (Technology Preview)
With this update, the GitOps Console Plugin adds Technology Preview support for Argo CD and Argo Rollouts. You can view Applications, ApplicationSets, AppProjects, and Rollouts directly from the OpenShift Container Platform. This feature requires OpenShift Container Platform 4.19 or later.

This feature includes:

- List and details pages for Argo CD and Argo Rollouts resources

- Filters for health and sync status

- Visual views for Applications and ApplicationSets

- Rollout topology in the OpenShift Console Topology view

- YAML templates for creating resources

- Links between the OpenShift Console and the Argo CD UI

- Views for sync history, events, resources, generators, revisions, and project policies

  These updates help you manage GitOps resources from a single interface and reduce the need to switch between tools.

  > [!IMPORTANT]
  > The GitOps Console Plugin resource pages feature is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
  >
  > For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

  [GITOPS-9196](https://redhat.atlassian.net/browse/GITOPS-9196)

Hybrid architecture for Argo CD Agent (Technology Preview)
With this update, you can run Argo CD Agent with your existing Argo CD deployment. This enables gradual adoption of the agent pull model without replacing the existing push-based architecture. Traditional applications continue to use the Application Controller on the control plane. Agent applications are synced to the workload clusters via the agent pull model. Both appear in the same UI. Label selectors and the `argocd.argoproj.io/skip-reconcile` annotation enforce isolation between them.

> [!IMPORTANT]
> The Argo CD Agent hybrid architecture feature is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

[GITOPS-9022](https://redhat.atlassian.net/browse/GITOPS-9022)

Declarative management for Git webhook secrets
With this update, the Argo CD Operator supports declarative management of Git webhook secrets through the `spec.webhookSecrets` field in the Argo CD custom resource (CR). You can configure webhook secrets for GitHub, GitLab, Bitbucket Cloud, Bitbucket Server, Gogs, and Azure DevOps directly within the CR. This feature allows you to reference external Kubernetes secrets containing webhook credentials rather than manually editing the operator-managed `argocd-secret` configuration.

This enhancement enables full integration with external secret management tools, such as the External Secrets Operator or Sealed Secrets, allowing webhook secrets to be managed alongside Argo CD configurations in a version-controlled, declarative workflow. This prevents the storage of sensitive tokens in GitOps repositories and eliminates manual updates to operator-managed resources, reducing reconciliation conflicts. This feature is fully backward compatible, and existing manual configurations continue to function without modification.

[GITOPS-8222](https://redhat.atlassian.net/browse/GITOPS-8222)

Pull Request workflow support for Image Updater
With this update, Argo CD Image Updater adds a Pull Request workflow for the Git write-back method. Before this update, image update commits were pushed directly to the tracking branch, which did not work with protected branches and skipped review processes. The Image Updater can now open a pull request to the base branch instead of pushing directly, allowing image updates to go through a review and approval workflow.

[GITOPS-9143](https://redhat.atlassian.net/browse/GITOPS-9143)

Namespace-scoped operation for Image Updater
With this update, Argo CD Image Updater defaults to namespace-scoped operation. Before this update, the Image Updater required cluster-wide RBAC permissions by default. This was restrictive in multitenant environments where cluster-scoped access is limited. By default, the controller watches only the namespace where it is installed and includes namespace-scoped Role and RoleBinding manifests. This default behavior is configurable. You can configure the controller to watch a specific set of namespaces or the entire cluster by adjusting the RBAC configuration.

[GITOPS-9134](https://redhat.atlassian.net/browse/GITOPS-9134)

TLS encryption for Image Updater webhook server
With this update, the Argo CD Image Updater webhook server runs with TLS enabled by default. Before this update, the webhook server accepted registry notifications over plain HTTP. It had no TLS encryption or configuration options. This allowed webhook payloads to transmit in cleartext. This included shared secrets used for payload validation. The webhook server now uses TLS 1.3 for both the minimum and maximum protocol versions by default. These TLS options are configurable. This ensures secure transmission of webhook notifications from container registries.

[GITOPS-9133](https://redhat.atlassian.net/browse/GITOPS-9133)

Alibaba Cloud Container Registry webhook support for Image Updater
With this update, Argo CD Image Updater adds native webhook support for Alibaba Cloud Container Registry (ACR). Before this update, the Image Updater had no webhook support for ACR and required polling to detect new image versions. A dedicated Aliyun ACR webhook handler enables the controller to respond to push events in real time.

[GITOPS-9701](https://redhat.atlassian.net/browse/GITOPS-9701)

Image Updater status subresource for monitoring and observability
With this update, each `ImageUpdater` CR maintains a status subresource that reflects the overall state of the resource. This includes the number of matched applications, managed images, timestamps, conditions, and a list of image updates from the most recent update cycle. You can check the state of your `ImageUpdater` resources with CLI commands:

``` terminal
$ oc get imageupdater -n openshift-gitops
```

You can also view the complete status by examining the `ImageUpdater` CR in the cluster.

[GITOPS-7316](https://redhat.atlassian.net/browse/GITOPS-7316)

ServiceMonitor resources for Argo CD Agent
With this update, ServiceMonitor resources are available for Argo CD Agent Principal and Agent components. This enables Prometheus to scrape metrics through Monitoring. Metrics now appear in Console dashboards.

[GITOPS-9595](https://redhat.atlassian.net/browse/GITOPS-9595)

End-to-end TLS encryption for Redis traffic in Argo CD Agent and Principal
With this update, the Argo CD Agent and Principal components support end-to-end TLS encryption for Redis traffic. The Redis proxy accepts TLS connections from Argo CD components like `argocd-server` and `argocd-repo-server`. It uses TLS when connecting to the local `argocd-redis` instance. Configure this feature using new CLI flags and environment variables. These include `--redis-tls-enabled`, proxy server certificate, and key paths, or related Kubernetes secrets. You can configure the upstream CA using a file path, a Kubernetes secret, or an insecure mode for testing only. The Kubernetes and Helm installation manifests include optional Redis TLS settings. TLS is disabled by default. The `principal.redis.tls.enabled` and `agent.redis.tls.enabled` fields default to `false`. This ensures that existing deployments continue to work until you enable the feature and provide certificates.

[GITOPS-8090](https://redhat.atlassian.net/browse/GITOPS-8090)

Repository credential sync for Argo CD Agent
With this update, Argo CD Agent syncs credentials to managed agents. It supports per-repository secrets and URL-prefix templates. Both are scoped by AppProject.

[GITOPS-9390](https://redhat.atlassian.net/browse/GITOPS-9390)

Redis credentials distribution using volume mounts
With this update, username and password for the operator-managed Redis or Redis HA are injected using volume mounts. This security hardening reduces the risk of accidental credential exposure.

[GITOPS-7368](https://redhat.atlassian.net/browse/GITOPS-7368)

Per-component Prometheus metrics configuration
With this update, you can configure the `interval` and `scrapeTimeout` fields for Argo CD component ServiceMonitors. This gives you control over metric collection intervals and timeouts for each Argo CD component.

[GITOPS-9633](https://redhat.atlassian.net/browse/GITOPS-9633)

Automatic cleanup of legacy KAM resources
With this update, Red Hat OpenShift GitOps cleans up old KAM (Application Manager CLI) resources automatically. Before this update, you had to remove KAM components manually when upgrading from older versions. These resources often stayed in clusters after upgrades. This caused stale deployments, wasted resources, and security scan alerts. The Red Hat OpenShift GitOps Operator removes these resources automatically.

[GITOPS-9217](https://redhat.atlassian.net/browse/GITOPS-9217)

## Fixed issues

Dex service account authentication security tokens
Before this update, the Dex service account used non-expiring security tokens. This created security risks from long-lived credentials. With this update, the service account uses expiring tokens. This improves authentication security for the Dex server in Red Hat OpenShift GitOps.

[GITOPS-9426](https://redhat.atlassian.net/browse/GITOPS-9426)

SSH handshake timeout errors with GitHub App authentication behind firewalls
Before this update, users with GitHub App authentication behind restrictive firewalls saw vague timeout errors. This happened because Post-Quantum Cryptography (PQC) algorithms generate larger SSH handshake packets. Some firewalls silently drop these packets. PQC algorithms are enabled by default starting in Argo CD 2.4.12. Suricata 7, which AWS Network Firewall uses, drops such large SSH packets. With this update, individual timeouts are used. Error messages now explicitly identify SSH handshake timeouts instead of generic timeout errors. This helps cluster operators quickly isolate and debug network path issues.

To avoid timeout errors when using GitHub App authentication behind network firewalls, disable the PQC algorithm for SSH handshake.

[GITOPS-8739](https://redhat.atlassian.net/browse/GITOPS-8739)

AppProject routing for destination-based mapping
Before this update, the principal required the agent name to match both `.spec.destinations[].name` and `.spec.sourceNamespaces` in an AppProject when using destination-based mapping. This was inconsistent with how Applications are routed in destination-based mapping. With this update, the principal checks only `.spec.destinations[].name` for routing when destination-based mapping is enabled. AppProjects are now correctly distributed to managed agents based solely on the destination name.

[GITOPS-9790](https://redhat.atlassian.net/browse/GITOPS-9790)

GitOps Operator annotation copying behavior fixed
Before this update, the Red Hat OpenShift GitOps Operator copied all annotations from the Argo CD custom resource (CR) onto operator-managed RBAC resources, such as RoleBindings, ClusterRoles, and ClusterRoleBindings. When the Argo CD CR was managed by a central Argo CD instance, copied tracking annotations such as `argocd.argoproj.io/tracking-id` and `argocd.argoproj.io/installation-id` could cause the central instance to incorrectly claim ownership of those resources and mark them for pruning.

With this update, the Red Hat OpenShift GitOps Operator applies only its default annotations to the resources it creates and no longer copies annotations from the Argo CD CR. As a result, this change prevents accidental pruning of newly created operator-managed RBAC resources.

For existing RoleBindings and ClusterRoleBindings that already contain these tracking annotations, the annotations must be removed, or the resources must be deleted so that the Operator can recreate them after the upgrade.

[GITOPS-9568](https://redhat.atlassian.net/browse/GITOPS-9568)

## Known issues

Web-based CLI terminal does not work without additional RBAC permissions
When the web-based CLI terminal feature is enabled by setting the `spec.webTerminalEnabled` field, the **Terminal** tab appears on the application details page for a pod, but command input does not work. The `openshift-gitops-argocd-server` service account does not have permission to create `pods/exec` resources, which the web terminal requires to attach to running pods and execute commands.

To work around this issue, create a `ClusterRole` and `ClusterRoleBinding` that grants the Argo CD server service account `pods/exec` access.

**Example:**

``` yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: terminal-tmp
rules:
  - verbs:
      - create
    apiGroups:
      - ''
    resources:
      - pods/exec
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: terminal-tmp
subjects:
  - kind: ServiceAccount
    name: openshift-gitops-argocd-server
    namespace: openshift-gitops
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: terminal-tmp
```

Apply the manifest with `oc apply -f`. If your Argo CD instance is not the default deployment in `openshift-gitops`, update the service account name and namespace in the `ClusterRoleBinding` accordingly.

[GITOPS-9631](https://redhat.atlassian.net/browse/GITOPS-9631)

Goroutine leak in Image Updater with Git write-back method
With this update, the Argo CD Image Updater might have a goroutine leak when using the `git` write-back method under heavy load. This happens when you have many applications and short poll intervals. The leak causes Git operations to fail with this error: `error: cannot fork() for remote-https: Resource temporarily unavailable`.

To mitigate this issue, apply one of the following workarounds:

- Increase the reconciliation interval to slow the leak by setting the environment variable in the ArgoCD custom resource:

  ``` yaml
  spec:
    imageUpdater:
      env:
        - name: IMAGE_UPDATER_INTERVAL
          value: 15m
  ```

- Implement a periodic restart of the deployment:

  ``` terminal
  $ oc rollout restart deployment/argocd-image-updater-controller
  ```

- Increase pod PID limits.

  [GITOPS-9959](https://redhat.atlassian.net/browse/GITOPS-9959)

Redis HA mode replication failure due to missing `masterauth` directive
The `argocd-redis-ha-configmap` is updated to switch the Redis authentication mechanism from `requirepass` to ACL file-based authentication. However, Redis HA mode does not work correctly because the new `redis.conf` template is missing the `masterauth` directive. As a result, Redis HA replicas start without `masterauth` in their configuration, causing replication attempts to fail with the `NOAUTH Authentication required` error.

This issue occurs only when `ha.enabled: true` in the Argo CD CR. Instances with `ha.enabled: false` are unaffected because single-instance Redis does not use replication and therefore does not require `masterauth`.

This issue will be fixed in the next Red Hat OpenShift GitOps z-stream release.

[GITOPS-10178](https://redhat.atlassian.net/browse/GITOPS-10178)

## Breaking changes

ApplicationSet tokenRef strict mode enabled by default
With this update, the Red Hat OpenShift GitOps Operator enables ApplicationSet `tokenRef` strict mode by default. This happens when `.spec.applicationSet.sourceNamespaces` on the Argo CD custom resource includes at least one cluster namespace. This change affects ApplicationSet SCM Provider and Pull Request generators. Secrets used by these generators through `tokenRef` must have this label: `argocd.argoproj.io/secret-type: scm-creds`.

If you use SCM Provider or Pull Request generators with unlabeled secrets, do one of the following before upgrading:

- Recommended: Label your secrets with `argocd.argoproj.io/secret-type: scm-creds`

- Not recommended for production environments: Temporarily disable strict mode by setting the following configuration in the ArgoCD custom resource:

  ``` yaml
  spec:
    cmdParams:
      applicationsetcontroller.enable.tokenref.strict.mode: "false"
  ```

  [GITOPS-8628](https://redhat.atlassian.net/browse/GITOPS-8628)

ImageUpdater spec.namespace field removed
With this update, the `spec.namespace` field has been removed from the ImageUpdater API. Any CR that includes `spec.namespace` will fail validation. The controller uses the ImageUpdater CR’s `metadata.namespace` to determine which namespace to search for applications.

[GITOPS-9135](https://redhat.atlassian.net/browse/GITOPS-9135)

## Deprecated and removed features

Deprecated logformat field for ApplicationSet and Notifications components
With this update, the `logformat` field name is now consistent across Argo CD components. Before this update, the `applicationSet` and `notifications` components used the lowercase `logformat` field. Components such as `server`, `repo-server`, and `application-controller` used the camelCase `logFormat` field.

Use the camelCase `logFormat` field for `applicationSet` and `notifications`. The lowercase `logformat` field is deprecated but still works for backward compatibility. The Red Hat OpenShift GitOps Operator uses the lowercase `logformat` field if the camelCase `logFormat` field is not set. You can update your custom resource specifications to use the camelCase `logFormat` field. The deprecated lowercase `logformat` field might be removed in a future release.

[GITOPS-9119](https://redhat.atlassian.net/browse/GITOPS-9119)

Deprecated dynamic shard scaling feature
With this update, the dynamic shard scaling feature in the Red Hat OpenShift GitOps Operator is deprecated. This includes the `.spec.controller.sharding.dynamicScalingEnabled` field in the Argo CD custom resource. For more information about sharding clusters, see the Additional resources section.

[GITOPS-9478](https://redhat.atlassian.net/browse/GITOPS-9478)

Migrated kube-rbac-proxy dependency
With this update, the deprecated `kube-rbac-proxy` image is no longer used. The Red Hat OpenShift GitOps Operator uses the `WithAuthenticationAndAuthorization` function from `controller-runtime` for authentication and authorization. As a result, Operator deployments now run with a single container instead of two.

[GITOPS-9236](https://redhat.atlassian.net/browse/GITOPS-9236)

# Additional resources

- [Using Argo CD Image Updater](../argocd_instance/using-argo-cd-image-updater.md#using-argo-cd-image-updater)

- [Working with the GitOps Console plugin](../argocd_applications/working-with-gitops-console-plugin.md#working-with-gitops-console-plugin)

- [Configuring webhook secrets for Git providers](../argocd_instance/configure-webhook-secrets-git-providers.md#configure-webhook-secrets-git-providers)

- [ApplicationSet tokenRef strict mode](../argocd_application_sets/managing-app-sets-in-non-control-plane-namespaces.md#gitops-applicationset-tokenref-strict-mode_managing-app-sets-in-non-control-plane-namespaces)

- [OpenTelemetry Tracing - Argo CD Agent upstream documentation](https://argocd-agent.readthedocs.io/latest/operations/tracing/)

- [Hybrid Architecture - Argo CD Agent upstream documentation](https://argocd-agent.readthedocs.io/latest/user-guide/hybrid-architecture/)

- [Download argocd, argocd-agentctl, Argo Rollouts kubectl plugin binaries](https://developers.redhat.com/content-gateway/rest/browse/pub/cgw/openshift-gitops/)

- [Sharding clusters across Argo CD Application Controller replicas](../declarative_clusterconfig/sharding-clusters-across-argo-cd-application-controller-replicas.md#sharding-clusters-across-argo-cd-application-controller-replicas)
