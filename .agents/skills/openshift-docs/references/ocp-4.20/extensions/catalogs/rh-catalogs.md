<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat provides several Operator catalogs that are included with OpenShift Container Platform by default.

# About Red Hat-provided Operator catalogs

The Red Hat-provided catalog sources are installed by default in the `openshift-marketplace` namespace, which makes the catalogs available cluster-wide in all namespaces.

The following Operator catalogs are distributed by Red Hat:

| Catalog | Index image | Description |
|----|----|----|
| `redhat-operators` | `registry.redhat.io/redhat/redhat-operator-index:v4.17` | Red Hat products packaged and shipped by Red Hat. Supported by Red Hat. |
| `certified-operators` | `registry.redhat.io/redhat/certified-operator-index:v4.17` | Products from leading independent software vendors (ISVs). Red Hat partners with ISVs to package and ship. Supported by the ISV. |
| `community-operators` | `registry.redhat.io/redhat/community-operator-index:v4.17` | Software maintained by relevant representatives in the [redhat-openshift-ecosystem/community-operators-prod/operators](https://github.com/redhat-openshift-ecosystem/community-operators-prod/tree/main/operators) GitHub repository. No official support. |

During a cluster upgrade, the index image tag for the default Red Hat-provided catalog sources are updated automatically by the Cluster Version Operator (CVO) so that Operator Lifecycle Manager (OLM) pulls the updated version of the catalog. For example during an upgrade from OpenShift Container Platform 4.8 to 4.9, the `spec.image` field in the `CatalogSource` object for the `redhat-operators` catalog is updated from:

``` terminal
registry.redhat.io/redhat/redhat-operator-index:v4.8
```

to:

``` terminal
registry.redhat.io/redhat/redhat-operator-index:v4.9
```
