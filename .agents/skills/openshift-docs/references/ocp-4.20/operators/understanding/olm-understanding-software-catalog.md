<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# About the software catalog

The *software catalog* is the web console interface in OpenShift Container Platform that cluster administrators use to discover and install Operators. With one click, an Operator can be pulled from its off-cluster source, installed and subscribed on the cluster, and made ready for engineering teams to self-service manage the product across deployment environments using Operator Lifecycle Manager (OLM).

Cluster administrators can choose from catalogs grouped into the following categories:

| Category | Description |
|----|----|
| Red Hat Operators | Red Hat products packaged and shipped by Red Hat. Supported by Red Hat. |
| Certified Operators | Products from leading independent software vendors (ISVs). Red Hat partners with ISVs to package and ship. Supported by the ISV. |
| Community Operators | Optionally-visible software maintained by relevant representatives in the [redhat-openshift-ecosystem/community-operators-prod/operators](https://github.com/redhat-openshift-ecosystem/community-operators-prod/tree/main/operators) GitHub repository. No official support. |
| Custom Operators | Operators you add to the cluster yourself. If you have not added any custom Operators, the **Custom** category does not appear in the web console software catalog. |

Operators in the software catalog are packaged to run on OLM. This includes a YAML file called a cluster service version (CSV) containing all of the CRDs, RBAC rules, deployments, and container images required to install and securely run the Operator. It also contains user-visible information like a description of its features and supported Kubernetes versions.

# Software catalog architecture

The software catalog UI component is driven by the Marketplace Operator by default on OpenShift Container Platform in the `openshift-marketplace` namespace.

## OperatorHub custom resource

The Marketplace Operator manages an `OperatorHub` custom resource (CR) named `cluster` that manages the default `CatalogSource` objects provided with the software catalog. You can modify this resource to enable or disable the default catalogs, which is useful when configuring OpenShift Container Platform in restricted network environments.

<div class="formalpara">

<div class="title">

Example `OperatorHub` custom resource

</div>

``` yaml
apiVersion: config.openshift.io/v1
kind: OperatorHub
metadata:
  name: cluster
spec:
  disableAllDefaultSources: true
  sources: [
    {
      name: "community-operators",
      disabled: false
    }
  ]
```

</div>

- `disableAllDefaultSources` is an override that controls availability of all default catalogs that are configured by default during an OpenShift Container Platform installation.

- Disable default catalogs individually by changing the `disabled` parameter value per source.

# Additional resources

- [Catalog source](olm/olm-understanding-olm.md#olm-catalogsource_olm-understanding-olm)

- [Operator installation and upgrade workflow in OLM](olm/olm-workflow.md#olm-upgrades_olm-workflow)

- [Red Hat Partner Connect](https://connect.redhat.com)
