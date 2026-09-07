<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use the Operator Framework packaging format to bundle and publish Operator metadata for Operator Lifecycle Manager (OLM) in OpenShift Container Platform. The format covers bundle images, dependencies, and file-based catalog schemas.

# Bundle format

The bundle format is an Operator Framework packaging format that simplifies distributing Operator metadata to catalogs. An Operator bundle is a single Operator version shipped as a non-runnable container image that stores Kubernetes manifests and metadata.

Storage and distribution of the bundle image is managed using existing container tools like `podman` and `docker` and container registries such as Quay.

Operator metadata can include:

- Information that identifies the Operator, for example its name and version.

- Additional information that drives the UI, for example its icon and some example custom resources (CRs).

- Required and provided APIs.

- Related images.

When loading manifests into the Operator Registry database, the following requirements are validated:

- The bundle must have at least one channel defined in the annotations.

- Every bundle has exactly one cluster service version (CSV).

- If a CSV owns a custom resource definition (CRD), that CRD must exist in the bundle.

## Manifests

Bundle manifests are Kubernetes objects in an Operator bundle that define the deployment and role based access control (RBAC) model for an Operator. A bundle includes one cluster service version (CSV) and typically the custom resource definitions (CRDs) for APIs owned by that CSV in its `/manifests` directory.

<div class="formalpara">

<div class="title">

Example bundle format layout

</div>

``` terminal
etcd
├── manifests
│   ├── etcdcluster.crd.yaml
│   └── etcdoperator.clusterserviceversion.yaml
│   └── secret.yaml
│   └── configmap.yaml
└── metadata
    └── annotations.yaml
    └── dependencies.yaml
```

</div>

### Additional supported Kubernetes objects

Operator bundles can optionally include additional Kubernetes object types in the `/manifests` directory for deployment with a cluster service version (CSV). When included, Operator Lifecycle Manager (OLM) creates and manages the lifecycle of these objects alongside the CSV.

The following optional object types are supported:

- `ClusterRole`

- `ClusterRoleBinding`

- `ConfigMap`

- `ConsoleCLIDownload`

- `ConsoleLink`

- `ConsoleQuickStart`

- `ConsoleYamlSample`

- `PodDisruptionBudget`

- `PriorityClass`

- `PrometheusRule`

- `Role`

- `RoleBinding`

- `Secret`

- `Service`

- `ServiceAccount`

- `ServiceMonitor`

- `VerticalPodAutoscaler`

OLM manages the lifecycle of these optional objects as follows:

- When the CSV is deleted, OLM deletes the optional object.

- When the CSV is upgraded:

  - If the name of the optional object is the same, OLM updates it in place.

  - If the name of the optional object has changed between versions, OLM deletes and recreates it.

## Annotations

Operator bundle annotations in the `metadata/annotations.yaml` file define aggregate metadata that describes how a bundle is indexed. These annotations specify media type, manifest paths, package name, channels, and the default channel for catalog registration.

A bundle includes an `annotations.yaml` file in its `/metadata` directory:

<div class="formalpara">

<div class="title">

Example `annotations.yaml`

</div>

``` yaml
annotations:
  operators.operatorframework.io.bundle.mediatype.v1: "registry+v1"
  operators.operatorframework.io.bundle.manifests.v1: "manifests/"
  operators.operatorframework.io.bundle.metadata.v1: "metadata/"
  operators.operatorframework.io.bundle.package.v1: "test-operator"
  operators.operatorframework.io.bundle.channels.v1: "beta,stable"
  operators.operatorframework.io.bundle.channel.default.v1: "stable"
```

</div>

where:

`annotations.operators.operatorframework.io.bundle.mediatype.v1`
Specifies the media type or format of the Operator bundle. The `registry+v1` format means it contains a CSV and its associated Kubernetes objects.

`annotations.operators.operatorframework.io.bundle.manifests.v1`
Specifies the path in the image to the directory that contains the Operator manifests. This label is reserved for future use and currently defaults to `manifests/`. The value `manifests.v1` implies that the bundle contains Operator manifests.

`annotations.operators.operatorframework.io.bundle.metadata.v1`
Specifies the path in the image to the directory that contains metadata files about the bundle. This label is reserved for future use and currently defaults to `metadata/`. The value `metadata.v1` implies that this bundle has Operator metadata.

`annotations.operators.operatorframework.io.bundle.package.v1`
Specifies the package name of the bundle.

`annotations.operators.operatorframework.io.bundle.channels.v1`
Specifies the list of channels the bundle is subscribing to when added into an Operator Registry.

`annotations.operators.operatorframework.io.bundle.channel.default.v1`
Specifies the default channel an Operator should be subscribed to when installed from a registry.

> [!NOTE]
> In case of a mismatch, the `annotations.yaml` file is authoritative because the on-cluster Operator Registry that relies on these annotations only has access to this file.

## Dependencies

Operator dependencies define relationships between Operators that Operator Lifecycle Manager (OLM) must resolve during installation on OpenShift Container Platform. You can list these dependencies in the optional `dependencies.yaml` file in a bundle’s `metadata/` folder.

The dependency list contains a `type` field for each item to specify what kind of dependency this is. The following types of Operator dependencies are supported:

`olm.package`
This type indicates a dependency for a specific Operator version. The dependency information must include the package name and the version of the package in semver format. For example, you can specify an exact version such as `0.5.2` or a range of versions such as `>0.5.1`.

`olm.gvk`
With this type, the author can specify a dependency with group/version/kind (GVK) information, similar to existing CRD and API-based usage in a CSV. This is a path to enable Operator authors to consolidate all dependencies, API or explicit versions, to be in the same place.

`olm.constraint`
This type declares generic constraints on arbitrary Operator properties.

In the following example, dependencies are specified for a Prometheus Operator and etcd CRDs:

<div class="formalpara">

<div class="title">

Example `dependencies.yaml` file

</div>

``` yaml
dependencies:
  - type: olm.package
    value:
      packageName: prometheus
      version: ">0.27.0"
  - type: olm.gvk
    value:
      group: etcd.database.coreos.com
      kind: EtcdCluster
      version: v1beta2
```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Operator Lifecycle Manager dependency resolution](olm/olm-understanding-dependency-resolution.md#olm-understanding-dependency-resolution)

</div>

## About the opm CLI

The `opm` CLI is an Operator Framework tool for creating and maintaining Operator catalogs from bundle images in OpenShift Container Platform. You can use it to build catalog container images that Operator Lifecycle Manager (OLM) references through catalog sources.

A catalog contains a database of pointers to Operator manifest content that can be queried through an included API that is served when the container image is run. On OpenShift Container Platform, Operator Lifecycle Manager (OLM) can reference the image in a catalog source, defined by a `CatalogSource` object, which polls the image at regular intervals to enable frequent updates to installed Operators on the cluster.

- See [CLI tools](../../cli_reference/opm/cli-opm-install.md#cli-opm-install) for steps on installing the `opm` CLI.

# Introduction to file-based catalogs

File-based catalogs are the latest plain text (JSON or YAML) catalog format for Operator Lifecycle Manager (OLM). This format enables catalog editing, composability, and extensibility while remaining compatible with earlier SQLite-based catalogs.

Editing
With file-based catalogs, users interacting with the contents of a catalog are able to make direct changes to the format and verify that their changes are valid. Because this format is plain text JSON or YAML, catalog maintainers can easily manipulate catalog metadata by hand or with widely known and supported JSON or YAML tooling, such as the `jq` CLI.

This editability enables the following features and user-defined extensions:

- Promoting an existing bundle to a new channel

- Changing the default channel of a package

- Custom algorithms for adding, updating, and removing upgrade paths

Composability
File-based catalogs are stored in an arbitrary directory hierarchy, which enables catalog composition. For example, consider two separate file-based catalog directories: `catalogA` and `catalogB`. A catalog maintainer can create a new combined catalog by making a new directory `catalogC` and copying `catalogA` and `catalogB` into it.

This composability enables decentralized catalogs. The format permits Operator authors to maintain Operator-specific catalogs, and it permits maintainers to trivially build a catalog composed of individual Operator catalogs. File-based catalogs can be composed by combining multiple other catalogs, by extracting subsets of one catalog, or a combination of both of these.

> [!NOTE]
> Duplicate packages and duplicate bundles within a package are not permitted. The `opm validate` command returns an error if any duplicates are found.

Because Operator authors are most familiar with their Operator, its dependencies, and its upgrade compatibility, they are able to maintain their own Operator-specific catalog and have direct control over its contents. With file-based catalogs, Operator authors own the task of building and maintaining their packages in a catalog. Composite catalog maintainers, however, only own the task of curating the packages in their catalog and publishing the catalog to users.

Extensibility
The file-based catalog specification is a low-level representation of a catalog. While it can be maintained directly in its low-level form, catalog maintainers can build interesting extensions on top that can be used by their own custom tooling to make any number of mutations.

For example, a tool could translate a high-level API, such as `(mode=semver)`, down to the low-level, file-based catalog format for upgrade paths. Or a catalog maintainer might need to customize all of the bundle metadata by adding a new property to bundles that meet a certain criteria.

While this extensibility allows for additional official tooling to be developed on top of the low-level APIs for future OpenShift Container Platform releases, the major benefit is that catalog maintainers have this capability as well.

> [!IMPORTANT]
> As of OpenShift Container Platform 4.11, the default Red Hat-provided Operator catalog releases in the file-based catalog format. The default Red Hat-provided Operator catalogs for OpenShift Container Platform 4.6 through 4.10 released in the deprecated SQLite database format.
>
> The `opm` subcommands, flags, and functionality related to the SQLite database format are also deprecated and will be removed in a future release. The features are still supported and must be used for catalogs that use the deprecated SQLite database format.
>
> Many of the `opm` subcommands and flags for working with the SQLite database format, such as `opm index prune`, do not work with the file-based catalog format.

<div>

<div class="title">

Additional resources

</div>

- [Managing custom catalogs](../admin/olm-managing-custom-catalogs.md#olm-managing-custom-catalogs-fb)

- [Mirroring images for a disconnected installation using the oc-mirror plugin](../../disconnected/installing-mirroring-disconnected.md#installing-mirroring-disconnected)

</div>

## Directory structure

File-based catalogs can be stored and loaded from directory-based file systems. The `opm` CLI loads the catalog by walking the root directory and recursing into subdirectories. The CLI attempts to load every file it finds and fails if any errors occur.

Non-catalog files can be ignored using `.indexignore` files, which have the same rules for patterns and precedence as `.gitignore` files.

<div class="formalpara">

<div class="title">

Example `.indexignore` file

</div>

``` terminal
# Ignore everything except non-object .json and .yaml files
**/*
!*.json
!*.yaml
**/objects/*.json
**/objects/*.yaml
```

</div>

Catalog maintainers have the flexibility to choose their layout, but it is recommended to store each package’s file-based catalog blobs in separate subdirectories. Each individual file can be either JSON or YAML; it is not necessary for every file in a catalog to use the same format.

<div class="formalpara">

<div class="title">

Basic recommended structure

</div>

``` terminal
catalog
├── packageA
│   └── index.yaml
├── packageB
│   ├── .indexignore
│   ├── index.yaml
│   └── objects
│       └── packageB.v0.1.0.clusterserviceversion.yaml
└── packageC
    └── index.json
    └── deprecations.yaml
```

</div>

This recommended structure has the property that each subdirectory in the directory hierarchy is a self-contained catalog, which makes catalog composition, discovery, and navigation trivial file system operations. The catalog can also be included in a parent catalog by copying it into the parent catalog’s root directory.

## Schemas

File-based catalogs on OpenShift Container Platform use a CUE-based format with schemas that define catalog structure for Operator Lifecycle Manager (OLM). Each Operator package requires one `olm.package` blob, at least one `olm.channel` blob, and one or more `olm.bundle` blobs.

<div class="formalpara">

<div class="title">

`_Meta` schema

</div>

``` go
_Meta: {
  // schema is required and must be a non-empty string
  schema: string & !=""

  // package is optional, but if it's defined, it must be a non-empty string
  package?: string & !=""

  // properties is optional, but if it's defined, it must be a list of 0 or more properties
  properties?: [... #Property]
}

#Property: {
  // type is required
  type: string & !=""

  // value is required, and it must not be null
  value: !=null
}
```

</div>

> [!NOTE]
> No CUE schemas listed in this specification should be considered exhaustive. The `opm validate` command has additional validations that are difficult or impossible to express concisely in CUE.

> [!NOTE]
> All `olm.*` schemas are reserved for OLM-defined schemas. Custom schemas must use a unique prefix, such as a domain that you own.

### olm.package schema

The `olm.package` schema specifies package-level metadata for Operators in file-based catalogs, including name, default channel, and icon. Use this schema reference when you build or validate Operator package definitions for Operator Lifecycle Manager (OLM).

<div class="example">

<div class="title">

`olm.package` schema

</div>

``` go
#Package: {
  schema: "olm.package"

  // Package name
  name: string & !=""

  // A description of the package
  description?: string

  // The package's default channel
  defaultChannel: string & !=""

  // An optional icon
  icon?: {
    base64data: string
    mediatype:  string
  }
}
```

</div>

### olm.channel schema

The `olm.channel` schema defines a channel within a package, the bundle entries that are members of the channel, and the upgrade paths for those bundles.

If a bundle entry represents an edge in multiple `olm.channel` blobs, it can only appear once per channel.

It is valid for an entry’s `replaces` value to reference another bundle name that cannot be found in this catalog or another catalog. However, all other channel invariants must hold true, such as a channel not having multiple heads.

<div class="example">

<div class="title">

`olm.channel` schema

</div>

``` go
#Channel: {
  schema: "olm.channel"
  package: string & !=""
  name: string & !=""
  entries: [...#ChannelEntry]
}

#ChannelEntry: {
  // name is required. It is the name of an `olm.bundle` that
  // is present in the channel.
  name: string & !=""

  // replaces is optional. It is the name of bundle that is replaced
  // by this entry. It does not have to be present in the entry list.
  replaces?: string & !=""

  // skips is optional. It is a list of bundle names that are skipped by
  // this entry. The skipped bundles do not have to be present in the
  // entry list.
  skips?: [...string & !=""]

  // skipRange is optional. It is the semver range of bundle versions
  // that are skipped by this entry.
  skipRange?: string & !=""
}
```

</div>

> [!WARNING]
> When using the `skipRange` field, the skipped Operator versions are pruned from the update graph and are longer installable by users with the `spec.startingCSV` property of `Subscription` objects.
>
> You can update an Operator incrementally while keeping previously installed versions available to users for future installation by using both the `skipRange` and `replaces` field. Ensure that the `replaces` field points to the immediate previous version of the Operator version in question.

<div>

<div class="title">

Additional resources

</div>

- [CUE language specification](https://cuelang.org/docs/references/spec/)

</div>

### olm.bundle schema

The `olm.bundle` schema defines the structure of bundle entries stored in an Operator catalog index. It specifies required fields such as package name, bundle name, image reference, and optional properties and related images.

<div class="example">

<div class="title">

`olm.bundle` schema

</div>

``` go
#Bundle: {
  schema: "olm.bundle"
  package: string & !=""
  name: string & !=""
  image: string & !=""
  properties: [...#Property]
  relatedImages?: [...#RelatedImage]
}

#Property: {
  // type is required
  type: string & !=""

  // value is required, and it must not be null
  value: !=null
}

#RelatedImage: {
  // image is the image reference
  image: string & !=""

  // name is an optional descriptive name for an image that
  // helps identify its purpose in the context of the bundle
  name?: string & !=""
}
```

</div>

### olm.deprecations schema

The optional `olm.deprecations` schema defines deprecation information for packages, bundles, and channels in an Operator catalog. When you define this schema, the web console displays warning badges and deprecation messages in the software catalog.

An `olm.deprecations` schema entry contains one or more of the following `reference` types, which indicates the deprecation scope. After the Operator is installed, any specified messages can be viewed as status conditions on the related `Subscription` object.

| Type          | Scope                         | Status condition    |
|---------------|-------------------------------|---------------------|
| `olm.package` | Represents the entire package | `PackageDeprecated` |
| `olm.channel` | Represents one channel        | `ChannelDeprecated` |
| `olm.bundle`  | Represents one bundle version | `BundleDeprecated`  |

Deprecation `reference` types

Each `reference` type has their own requirements, as detailed in the following example.

<div class="formalpara">

<div class="title">

Example `olm.deprecations` schema with each `reference` type

</div>

``` yaml
schema: olm.deprecations
package: my-operator
entries:
  - reference:
      schema: olm.package
    message: |
    The 'my-operator' package is end of life. Please use the
    'my-operator-new' package for support.
  - reference:
      schema: olm.channel
      name: alpha
    message: |
    The 'alpha' channel is no longer supported. Please switch to the
    'stable' channel.
  - reference:
      schema: olm.bundle
      name: my-operator.v1.68.0
    message: |
    my-operator.v1.68.0 is deprecated. Uninstall my-operator.v1.68.0 and
    install my-operator.v1.72.0 for support.
```

</div>

- Each deprecation schema must have a `package` value, and that package reference must be unique across the catalog. There must not be an associated `name` field.

- The `olm.package` schema must not include a `name` field, because it is determined by the `package` field defined earlier in the schema.

- All `message` fields, for any `reference` type, must be a non-zero length and represented as an opaque text blob.

- The `name` field for the `olm.channel` schema is required.

- The `name` field for the `olm.bundle` schema is required.

> [!NOTE]
> The deprecation feature does not consider overlapping deprecation, for example package versus channel versus bundle.

Operator authors can save `olm.deprecations` schema entries as a `deprecations.yaml` file in the same directory as the package’s `index.yaml` file:

<div class="formalpara">

<div class="title">

Example directory structure for a catalog with deprecations

</div>

``` terminal
my-catalog
└── my-operator
    ├── index.yaml
    └── deprecations.yaml
```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Updating or filtering a file-based catalog image](../admin/olm-managing-custom-catalogs.md#olm-filtering-fbc_olm-managing-custom-catalogs)

</div>

## Properties

Properties are arbitrary pieces of metadata that can be attached to file-based catalog schemas. The `type` field is a string that effectively specifies the semantic and syntactic meaning of the `value` field. The value can be any arbitrary JSON or YAML.

OLM defines a handful of property types, again using the reserved `olm.*` prefix.

### olm.package property

The `olm.package` property defines the package name and version. This is a required property on bundles, and there must be exactly one of these properties. The `packageName` field must match the bundle’s first-class `package` field, and the `version` field must be a valid semantic version.

<div class="formalpara">

<div class="title">

`olm.package` property

</div>

``` go
#PropertyPackage: {
  type: "olm.package"
  value: {
    packageName: string & !=""
    version: string & !=""
  }
}
```

</div>

### olm.gvk property

The `olm.gvk` property defines the group/version/kind (GVK) of a Kubernetes API that is provided by this bundle. This property is used by OLM to resolve a bundle with this property as a dependency for other bundles that list the same GVK as a required API. The GVK must adhere to Kubernetes GVK validations.

<div class="formalpara">

<div class="title">

`olm.gvk` property

</div>

``` go
#PropertyGVK: {
  type: "olm.gvk"
  value: {
    group: string & !=""
    version: string & !=""
    kind: string & !=""
  }
}
```

</div>

### olm.package.required

The `olm.package.required` property defines the package name and version range of another package that this bundle requires. For every required package property a bundle lists, OLM ensures there is an Operator installed on the cluster for the listed package and in the required version range. The `versionRange` field must be a valid semantic version (semver) range.

<div class="formalpara">

<div class="title">

`olm.package.required` property

</div>

``` go
#PropertyPackageRequired: {
  type: "olm.package.required"
  value: {
    packageName: string & !=""
    versionRange: string & !=""
  }
}
```

</div>

### olm.gvk.required

The `olm.gvk.required` property defines the group/version/kind (GVK) of a Kubernetes API that this bundle requires. For every required GVK property a bundle lists, OLM ensures there is an Operator installed on the cluster that provides it. The GVK must adhere to Kubernetes GVK validations.

<div class="formalpara">

<div class="title">

`olm.gvk.required` property

</div>

``` terminal
#PropertyGVKRequired: {
  type: "olm.gvk.required"
  value: {
    group: string & !=""
    version: string & !=""
    kind: string & !=""
  }
}
```

</div>

## Example catalog

With file-based catalogs, catalog maintainers can focus on Operator curation and compatibility.

Because Operator authors have already produced Operator-specific catalogs for their Operators, catalog maintainers can build their catalog by rendering each Operator catalog into a subdirectory of the catalog’s root directory.

There are many possible ways to build a file-based catalog; the following steps outline a simple approach:

1.  Maintain a single configuration file for the catalog, containing image references for each Operator in the catalog:

    <div class="formalpara">

    <div class="title">

    Example catalog configuration file

    </div>

    ``` yaml
    name: community-operators
    repo: quay.io/community-operators/catalog
    tag: latest
    references:
    - name: etcd-operator
      image: quay.io/etcd-operator/index@sha256:5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03
    - name: prometheus-operator
      image: quay.io/prometheus-operator/index@sha256:e258d248fda94c63753607f7c4494ee0fcbe92f1a76bfdac795c9d84101eb317
    ```

    </div>

2.  Run a script that parses the configuration file and creates a new catalog from its references:

    <div class="formalpara">

    <div class="title">

    Example script

    </div>

    ``` sh
    name=$(yq eval '.name' catalog.yaml)
    mkdir "$name"
    yq eval '.name + "/" + .references[].name' catalog.yaml | xargs mkdir
    for l in $(yq e '.name as $catalog | .references[] | .image + "|" + $catalog + "/" + .name + "/index.yaml"' catalog.yaml); do
      image=$(echo $l | cut -d'|' -f1)
      file=$(echo $l | cut -d'|' -f2)
      opm render "$image" > "$file"
    done
    opm generate dockerfile "$name"
    indexImage=$(yq eval '.repo + ":" + .tag' catalog.yaml)
    docker build -t "$indexImage" -f "$name.Dockerfile" .
    docker push "$indexImage"
    ```

    </div>

## Guidelines

Follow the guidelines to maintain file-based Operator catalogs. Treat bundle images and metadata as immutable. Store catalog metadata in source control as the source of truth.

### Immutable bundles

The general advice with Operator Lifecycle Manager (OLM) is that bundle images and their metadata should be treated as immutable.

If a broken bundle has been pushed to a catalog, you must assume that at least one of your users has upgraded to that bundle. Based on that assumption, you must release another bundle with an upgrade path from the broken bundle to ensure users with the broken bundle installed receive an upgrade. OLM will not reinstall an installed bundle if the contents of that bundle are updated in the catalog.

However, there are some cases where a change in the catalog metadata is preferred:

- Channel promotion: If you already released a bundle and later decide that you want to add it to another channel, you can add an entry for your bundle in another `olm.channel` blob.

- New upgrade paths: If you release a new `1.2.z` bundle version, for example `1.2.4`, but `1.3.0` is already released, you can update the catalog metadata for `1.3.0` to skip `1.2.4`.

### Source control

Catalog metadata should be stored in source control and treated as the source of truth. Updates to catalog images should include the following steps:

1.  Update the source-controlled catalog directory with a new commit.

2.  Build and push the catalog image. Use a consistent tagging taxonomy, such as `:latest` or `:<target_cluster_version>`, so that users can receive updates to a catalog as they become available.

> [!NOTE]
> For more information about creating file-based catalogs by using the `opm` CLI, see "Creating a file-based catalog image".

<div>

<div class="title">

Additional resources

</div>

- [Managing custom catalogs](../admin/olm-managing-custom-catalogs.md#olm-creating-fb-catalog-image_olm-managing-custom-catalogs)

- [CLI tools](../../cli_reference/opm/cli-opm-ref.md#cli-opm-ref)

</div>

## Automation

Operator authors and catalog maintainers can automate file-based catalog maintenance with CI/CD workflows.

Catalog maintainers can use GitOps automation to accomplish the following example tasks:

- Check that pull request (PR) authors are permitted to make the requested changes, for example by updating their package’s image reference.

- Check that the catalog updates pass the `opm validate` command.

- Check that the updated bundle or catalog image references exist, the catalog images run successfully in a cluster, and Operators from that package can be successfully installed.

- Automatically merge PRs that pass the previous checks.

- Automatically rebuild and republish the catalog image.
