> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/whats_new-ref_new_features). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# New features and enhancements

The following release notes detail the new features and enhancements for the Red Hat OpenShift Dev Spaces 3.29 general availability release.

## OpenShift Dev Spaces now supports clusters with external authentication

Before this update, the OpenShift Dev Spaces Operator did not support OpenShift clusters configured with Bring Your Own (BYO) external authentication. Clusters that replaced the built-in OpenShift OAuth server with external corporate OIDC identity providers (IdPs) could not run OpenShift Dev Spaces.

With this update, OpenShift Dev Spaces supports BYO external authentication. Administrators can configure their OpenShift cluster to use an external OIDC identity provider as the authentication source and deploy OpenShift Dev Spaces on these clusters.

For instructions, see [Deploy using an external identity provider](install-proc_installing_dev_spaces_on_openshift_with_keycloak_as_oidc.md) in the Install guide.

**Additional resources**

- [CRW-9763](https://redhat.atlassian.net/browse/CRW-9763)

## Users can now stop workspace creation from the Workspace Creation page

Before this update, there was no mechanism to halt workspace starting from the Workspace Creation page. With this update, a stop mechanism is available. As a result, users have better control over the workspace creation process.

**Additional resources**

- [CRW-10282](https://redhat.atlassian.net/browse/CRW-10282)

## Session timeout warning before OAuth session expires

To prevent data loss from silent session expiration, the Dashboard now warns users before their OAuth session expires. A modal appears 60 seconds before session expiry with a live countdown, offering options to extend the session or sign out immediately.

**Additional resources**

- [CRW-10290](https://redhat.atlassian.net/browse/CRW-10290)

## Streamlined GitHub Copilot Chat authentication

To simplify the setup experience for AI-powered code assistance, OpenShift Dev Spaces now automatically detects when GitHub Copilot Chat is not authenticated and triggers the Device Authentication flow. Previously, users had to manually run the Device Authentication command to authenticate GitHub Copilot Chat in their workspace.

**Additional resources**

- [CRW-10918](https://redhat.atlassian.net/browse/CRW-10918)

## Visual Studio Code - Open Source updated to version 1.116.0

To provide access to the newest development capabilities, Visual Studio Code - Open Source ("Code - OSS") has been updated to version 1.116.0. This update includes GitHub Copilot Chat as a built-in feature, the latest performance improvements, and security patches from the upstream project.

**Additional resources**

- [CRW-10936](https://redhat.atlassian.net/browse/CRW-10936)

## Updated Node.js versions in the Universal Developer Image

To support modern JavaScript development, the Universal Developer Image now includes Node.js 22 (v22.22.3) as the default version. Existing Node.js versions have been updated to the latest patch releases:

- Node.js 22 (v22.22.3) — default version
- Node.js 20 updated to v20.20.2
- Node.js 18 updated to v18.20.8

**Additional resources**

- [CRW-11418](https://redhat.atlassian.net/browse/CRW-11418)

## Automated Prometheus resource setup for metrics collection

To simplify monitoring configuration, OpenShift Dev Spaces now automatically sets up the required Prometheus resources for metrics collection, removing the need for manual configuration. The operator creates:

- ServiceMonitor objects for both the server and the DevWorkspace Operator
- RBAC (Role + RoleBinding) granting the prometheus-k8s service account access to scrape metrics endpoints
- The `openshift.io/cluster-monitoring: "true"` label on the operator namespace, enabling the built-in monitoring stack to discover the ServiceMonitors automatically

**Additional resources**

- [CRW-11425](https://redhat.atlassian.net/browse/CRW-11425)

## URI handler for establishing local-to-remote SSH connections

To streamline the local-to-remote connection process, OpenShift Dev Spaces now automatically opens a `vscode://redhat.devspaces-remote-ssh` URI that is handled by an active Code-based editor with the Dev Spaces Local/Remote Support - SSH extension installed.

**Additional resources**

- [CRW-11426](https://redhat.atlassian.net/browse/CRW-11426)

## Simplified cluster authentication for the Gateway plugin

To reduce friction when connecting to a cluster, the Gateway plugin now offers new authentication methods and a redesigned UI to easily switch between them.

**Additional resources**

- [CRW-11427](https://redhat.atlassian.net/browse/CRW-11427)

## Restrict workspace override fields and improve stability with DevWorkspace Operator 0.42.0

DevWorkspace Operator 0.42.0 introduces configurable field-level restrictions for container and pod overrides, along with fixes for OpenShift registry RoleBinding accumulation, nested project cloning, PVC cleanup pod security context, init-persistent-home memory limits, and ephemeral workspace home volumes.

**Configurable field-level restrictions for container and pod overrides**

Cluster administrators can define deny rules in `DevWorkspaceOperatorConfig` to block specific fields or field values from being set via the `container-overrides` and `pod-overrides` DevWorkspace attributes. Restrictions are specified using the new `config.overrides.restrictedContainerOverrideFields` and `config.overrides.restrictedPodOverrideFields` fields.

On Kubernetes, a set of security-sensitive fields are denied out of the box including privileged containers, running as root, host networking, and `hostPath` volumes, matching the restrictions that OpenShift enforces natively via SCCs. These defaults can be adjusted from the global `DevWorkspaceOperatorConfig` object.

**Additional fixes in DWO 0.42.0:**

- OpenShift registry image-puller RoleBindings no longer accumulate deleted workspace ServiceAccounts, preventing etcd rejections in high-churn namespaces.
- Project cloning no longer fails when a nested `clonePath` is used and intermediate parent directories do not exist.
- PVC cleanup Job pods inherit the workspace `podSecurityContext` to match workspace deployment behavior.
- The default `init-persistent-home` container memory limit is increased from 128Mi to 256Mi and the request from 64Mi to 128Mi to prevent OOM failures with large developer images.
- Ephemeral workspaces mount an `emptyDir` home volume when a custom `init-persistent-home` init container is configured and `persistUserHome` is enabled.

**Additional resources**

- [CRW-11514](https://redhat.atlassian.net/browse/CRW-11514)
