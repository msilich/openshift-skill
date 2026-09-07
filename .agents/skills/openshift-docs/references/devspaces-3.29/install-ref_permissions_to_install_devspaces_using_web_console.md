> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-ref_permissions_to_install_devspaces_using_web_console). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Permissions required for web console installation

Install OpenShift Dev Spaces through the OpenShift web console with a specific set of cluster permissions. Apply this `ClusterRole` to the installer’s service account or user to grant the minimum required permissions for web console installation.

The following YAML defines the minimal set of permissions for installing OpenShift Dev Spaces on an OpenShift cluster using the web console:

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: devspaces-install-web-console
rules:
- apiGroups: ["org.eclipse.che"]
  resources: ["checlusters"]
  verbs: ["*"]
- apiGroups: [""]
  resources: ["namespaces"]
  verbs: ["get", "list", "create"]
- apiGroups: ["project.openshift.io"]
  resources: ["projects"]
  verbs: ["get", "list", "create"]
  # OLM resources permissions
- apiGroups: ["operators.coreos.com"]
  resources: ["subscriptions"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: ["operators.coreos.com"]
  resources: ["operatorgroups"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["operators.coreos.com"]
  resources: ["clusterserviceversions", "catalogsources", "installplans"]
  verbs: ["get", "list", "watch", "delete"]
- apiGroups: ["packages.operators.coreos.com"]
  resources: ["packagemanifests", "packagemanifests/icon"]
  verbs: ["get", "list", "watch"]
  # Workaround related to viewing operators in OperatorHub
- apiGroups: ["operator.openshift.io"]
  resources: ["cloudcredentials"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["config.openshift.io"]
  resources: ["infrastructures", "authentications"]
  verbs: ["get", "list", "watch"]
```

**Related information**  

- [command](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/developer-cli-commands.html#oc-apply)
- [command](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/administrator-cli-commands.html#oc-adm-policy-add-cluster-role-to-user)
