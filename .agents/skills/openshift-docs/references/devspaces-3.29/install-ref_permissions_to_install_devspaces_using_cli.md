> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-ref_permissions_to_install_devspaces_using_cli). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Permissions required for CLI installation

Apply this `ClusterRole` to the installer’s service account or user to grant the minimum permissions required for a `dsc`-based installation of OpenShift Dev Spaces.

The following YAML defines the minimal set of permissions for installing OpenShift Dev Spaces on an OpenShift cluster using `dsc`:

``` yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: devspaces-install-dsc
rules:
- apiGroups: ["org.eclipse.che"]
  resources: ["checlusters"]
  verbs: ["*"]
- apiGroups: ["project.openshift.io"]
  resources: ["projects"]
  verbs: ["get", "list"]
- apiGroups: [""]
  resources: ["namespaces"]
  verbs: ["get", "list", "create"]
- apiGroups: [""]
  resources: ["pods", "configmaps"]
  verbs: ["get", "list"]
- apiGroups: ["route.openshift.io"]
  resources: ["routes"]
  verbs: ["get", "list"]
  # OLM resources permissions
- apiGroups: ["operators.coreos.com"]
  resources: ["catalogsources", "subscriptions"]
  verbs: ["create", "get", "list", "watch"]
- apiGroups: ["operators.coreos.com"]
  resources: ["operatorgroups", "clusterserviceversions"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["operators.coreos.com"]
  resources: ["installplans"]
  verbs: ["patch", "get", "list", "watch"]
- apiGroups: ["packages.operators.coreos.com"]
  resources: ["packagemanifests"]
  verbs: ["get", "list"]
```

**Related information**  

- [command](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/developer-cli-commands.html#oc-apply)
- [command](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/administrator-cli-commands.html#oc-adm-policy-add-cluster-role-to-user)
