<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can learn how Operator Lifecycle Manager (OLM) components interact to manage Operators in OpenShift Container Platform. The architecture includes the OLM Operator, Catalog Operator, and Catalog Registry.

# CRDs

Operator Lifecycle Manager (OLM) and the Catalog Operator manage the following custom resource definitions (CRDs) that form the basis of the Operator Framework.

| Resource | Short name | Owner | Description |
|----|----|----|----|
| `ClusterServiceVersion` (CSV) | `csv` | OLM | Application metadata: name, version, icon, required resources, installation, and so on. |
| `InstallPlan` | `ip` | Catalog | Calculated list of resources to be created to automatically install or upgrade a CSV. |
| `CatalogSource` | `catsrc` | Catalog | A repository of CSVs, CRDs, and packages that define an application. |
| `Subscription` | `sub` | Catalog | Used to keep CSVs up to date by tracking a channel in a package. |
| `OperatorGroup` | `og` | OLM | Configures all Operators deployed in the same namespace as the `OperatorGroup` object to watch for their custom resource (CR) in a list of namespaces or cluster-wide. |

CRDs managed by OLM and Catalog Operators

Each of these Operators is also responsible for creating the following resources:

| Resource                           | Owner   |
|------------------------------------|---------|
| `Deployments`                      | OLM     |
| `ServiceAccounts`                  |         |
| `(Cluster)Roles`                   |         |
| `(Cluster)RoleBindings`            |         |
| `CustomResourceDefinitions` (CRDs) | Catalog |
| `ClusterServiceVersions`           |         |

Resources created by OLM and Catalog Operators

# OLM Operator

The OLM Operator deploys applications defined by cluster service versions (CSVs) after their required resources are present in the cluster. It watches CSVs in a namespace, verifies requirements, and runs the install strategy when conditions are met.

The OLM Operator is not concerned with the creation of the required resources; you can choose to manually create these resources using the CLI or using the Catalog Operator. This separation of concern allows users incremental buy-in in terms of how much of the OLM framework they choose to leverage for their application.

The OLM Operator uses the following workflow:

1.  Watch for cluster service versions (CSVs) in a namespace and check that requirements are met.

2.  If requirements are met, run the install strategy for the CSV.

    > [!NOTE]
    > A CSV must be an active member of an Operator group for the install strategy to run.

# Catalog Operator

The Catalog Operator in OpenShift Container Platform resolves and installs cluster service versions (CSVs) and their required resources from catalog sources. It watches subscriptions and catalog sources to create install plans and upgrade packages in channels.

To track a package in a channel, you can create a `Subscription` object configuring the desired package, channel, and the `CatalogSource` object you want to use for pulling updates. When updates are found, an appropriate `InstallPlan` object is written into the namespace on behalf of the user.

The Catalog Operator uses the following workflow:

1.  Connect to each catalog source in the cluster.

2.  Watch for unresolved install plans created by a user, and if found:

    1.  Find the CSV matching the name requested and add the CSV as a resolved resource.

    2.  For each managed or required CRD, add the CRD as a resolved resource.

    3.  For each required CRD, find the CSV that manages it.

3.  Watch for resolved install plans and create all of the discovered resources for it, if approved by a user or automatically.

4.  Watch for catalog sources and subscriptions and create install plans based on them.

# Catalog Registry

The Catalog Registry stores cluster service versions (CSVs), custom resource definitions (CRDs), and metadata about packages and channels for Operator installation in OpenShift Container Platform. Package manifests link package identities to CSVs so the Catalog Operator can step through channel upgrade paths.

A *package manifest* is an entry in the Catalog Registry that associates a package identity with sets of CSVs. Within a package, channels point to a particular CSV. Because CSVs explicitly reference the CSV that they replace, a package manifest provides the Catalog Operator with all of the information that is required to update a CSV to the latest version in a channel, stepping through each intermediate version.
