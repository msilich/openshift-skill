<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The `opm` command-line interface (CLI) is a tool for creating and maintaining Operator catalogs.

<div class="formalpara">

<div class="title">

`opm` CLI syntax

</div>

``` terminal
$ opm <command> [<subcommand>] [<argument>] [<flags>]
```

</div>

> [!WARNING]
> The `opm` CLI is not forward compatible. The version of the `opm` CLI used to generate catalog content must be earlier than or equal to the version used to serve the content on a cluster.

| Flag | Description |
|----|----|
| `-skip-tls-verify` | Skip TLS certificate verification for container image registries while pulling bundles or indexes. |
| `--use-http` | When you pull bundles, use plain HTTP for container image registries. |

Global flags

> [!IMPORTANT]
> The SQLite-based catalog format, including the related CLI commands, is a deprecated feature. Deprecated functionality is still included in OpenShift Container Platform and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments.
>
> For the most recent list of major functionality that has been deprecated or removed within OpenShift Container Platform, refer to the *Deprecated and removed features* section of the OpenShift Container Platform release notes.

# generate

Generate various artifacts for declarative config indexes.

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm generate <subcommand> [<flags>]
```

</div>

| Subcommand   | Description                                           |
|--------------|-------------------------------------------------------|
| `dockerfile` | Generate a Dockerfile for a declarative config index. |

`generate` subcommands

| Flags          | Description        |
|----------------|--------------------|
| `-h`, `--help` | Help for generate. |

`generate` flags

## dockerfile

Generate a Dockerfile for a declarative config index.

> [!IMPORTANT]
> This command creates a Dockerfile in the same directory as the `<dcRootDir>` (named `<dcDirName>.Dockerfile`) that is used to build the index. If a Dockerfile with the same name already exists, this command fails.
>
> When specifying extra labels, if duplicate keys exist, only the last value of each duplicate key gets added to the generated Dockerfile.

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm generate dockerfile <dcRootDir> [<flags>]
```

</div>

| Flag | Description |
|----|----|
| `-i,` `--binary-image` (string) | Image in which to build catalog. The default value is `quay.io/operator-framework/opm:latest`. |
| `-l`, `--extra-labels` (string) | Extra labels to include in the generated Dockerfile. Labels have the form `key=value`. |
| `-h`, `--help` | Help for Dockerfile. |

`generate dockerfile` flags

> [!NOTE]
> To build with the official Red Hat image, use the `registry.redhat.io/openshift4/ose-operator-registry-rhel9:v4.17` value with the `-i` flag.

# index

Generate Operator index for SQLite database format container images from pre-existing Operator bundles.

> [!IMPORTANT]
> As of OpenShift Container Platform 4.11, the default Red Hat-provided Operator catalog releases in the file-based catalog format. The default Red Hat-provided Operator catalogs for OpenShift Container Platform 4.6 through 4.10 released in the deprecated SQLite database format.
>
> The `opm` subcommands, flags, and functionality related to the SQLite database format are also deprecated and will be removed in a future release. The features are still supported and must be used for catalogs that use the deprecated SQLite database format.
>
> Many of the `opm` subcommands and flags for working with the SQLite database format, such as `opm index prune`, do not work with the file-based catalog format.
>
> For more information about working with file-based catalogs, see "Additional resources".

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm index <subcommand> [<flags>]
```

</div>

| Subcommand | Description |
|----|----|
| `add` | Add Operator bundles to an index. |
| `prune` | Prune an index of all but specified packages. |
| `prune-stranded` | Prune an index of stranded bundles, which are bundles that are not associated with a particular image. |
| `rm` | Delete an entire Operator from an index. |

`index` subcommands

## add

Add Operator bundles to an index.

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm index add [<flags>]
```

</div>

| Flag | Description |
|----|----|
| `-i`, `--binary-image` | Container image for on-image `opm` command |
| `-u`, `--build-tool` (string) | Tool to build container images: `podman` (the default value) or `docker`. Overrides part of the `--container-tool` flag. |
| `-b`, `--bundles` (strings) | Comma-separated list of bundles to add. |
| `-c`, `--container-tool` (string) | Tool to interact with container images, such as for saving and building: `docker` or `podman`. |
| `-f`, `--from-index` (string) | Previous index to add to. |
| `--generate` | If enabled, only creates the Dockerfile and saves it to local disk. |
| `--mode` (string) | Graph update mode that defines how channel graphs are updated: `replaces` (the default value), `semver`, or `semver-skippatch`. |
| `-d`, `--out-dockerfile` (string) | Optional: If generating the Dockerfile, specify a file name. |
| `--permissive` | Allow registry load errors. |
| `-p`, `--pull-tool` (string) | Tool to pull container images: `none` (the default value), `docker`, or `podman`. Overrides part of the `--container-tool` flag. |
| `-t`, `--tag` (string) | Custom tag for container image being built. |

`index add` flags

## prune

Prune an index of all but specified packages.

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm index prune [<flags>]
```

</div>

| Flag | Description |
|----|----|
| `-i`, `--binary-image` | Container image for on-image `opm` command |
| `-c`, `--container-tool` (string) | Tool to interact with container images, such as for saving and building: `docker` or `podman`. |
| `-f`, `--from-index` (string) | Index to prune. |
| `--generate` | If enabled, only creates the Dockerfile and saves it to local disk. |
| `-d`, `--out-dockerfile` (string) | Optional: If generating the Dockerfile, specify a file name. |
| `-p`, `--packages` (strings) | Comma-separated list of packages to keep. |
| `--permissive` | Allow registry load errors. |
| `-t`, `--tag` (string) | Custom tag for container image being built. |

`index prune` flags

## prune-stranded

Prune an index of stranded bundles, which are bundles that are not associated with a particular image.

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm index prune-stranded [<flags>]
```

</div>

| Flag | Description |
|----|----|
| `-i`, `--binary-image` | Container image for on-image `opm` command |
| `-c`, `--container-tool` (string) | Tool to interact with container images, such as for saving and building: `docker` or `podman`. |
| `-f`, `--from-index` (string) | Index to prune. |
| `--generate` | If enabled, only creates the Dockerfile and saves it to local disk. |
| `-d`, `--out-dockerfile` (string) | Optional: If generating the Dockerfile, specify a file name. |
| `-p`, `--packages` (strings) | Comma-separated list of packages to keep. |
| `--permissive` | Allow registry load errors. |
| `-t`, `--tag` (string) | Custom tag for container image being built. |

`index prune-stranded` flags

## rm

Delete an entire Operator from an index.

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm index rm [<flags>]
```

</div>

| Flag | Description |
|----|----|
| `-i`, `--binary-image` | Container image for on-image `opm` command |
| `-u`, `--build-tool` (string) | Tool to build container images: `podman` (the default value) or `docker`. Overrides part of the `--container-tool` flag. |
| `-c`, `--container-tool` (string) | Tool to interact with container images, such as for saving and building: `docker` or `podman`. |
| `-f`, `--from-index` (string) | Previous index to delete from. |
| `--generate` | If enabled, only creates the Dockerfile and saves it to local disk. |
| `-o`, `--operators` (strings) | Comma-separated list of Operators to delete. |
| `-d`, `--out-dockerfile` (string) | Optional: If generating the Dockerfile, specify a file name. |
| `-p`, `--packages` (strings) | Comma-separated list of packages to keep. |
| `--permissive` | Allow registry load errors. |
| `-p`, `--pull-tool` (string) | Tool to pull container images: `none` (the default value), `docker`, or `podman`. Overrides part of the `--container-tool` flag. |
| `-t`, `--tag` (string) | Custom tag for container image being built. |

`index rm` flags

<div>

<div class="title">

Additional resources

</div>

- [Operator Framework packaging format](../../operators/understanding/olm-packaging-format.md#olm-file-based-catalogs_olm-packaging-format)

- [Managing custom catalogs](../../operators/admin/olm-managing-custom-catalogs.md#olm-managing-custom-catalogs-fb)

- [Mirroring images for a disconnected installation using the oc-mirror plugin](../../disconnected/installing-mirroring-disconnected.md#installing-mirroring-disconnected)

</div>

# init

Generate an `olm.package` declarative config blob.

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm init <package_name> [<flags>]
```

</div>

| Flag | Description |
|----|----|
| `-c`, `--default-channel` (string) | The channel that subscriptions will default to if unspecified. |
| `-d`, `--description` (string) | Path to the Operator’s `README.md` or other documentation. |
| `-i`, `--icon` (string) | Path to package’s icon. |
| `-o`, `--output` (string) | Output format: `json` (the default value) or `yaml`. |

`init` flags

# migrate

Migrate a SQLite database format index image or database file to a file-based catalog.

> [!IMPORTANT]
> The SQLite-based catalog format, including the related CLI commands, is a deprecated feature. Deprecated functionality is still included in OpenShift Container Platform and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments.
>
> For the most recent list of major functionality that has been deprecated or removed within OpenShift Container Platform, refer to the *Deprecated and removed features* section of the OpenShift Container Platform release notes.

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm migrate <index_ref> <output_dir> [<flags>]
```

</div>

| Flag | Description |
|----|----|
| `-o`, `--output` (string) | Output format: `json` (the default value) or `yaml`. |

`migrate` flags

# render

Generate a declarative config blob from the provided index images, bundle images, and SQLite database files.

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm render <index_image | bundle_image | sqlite_file> [<flags>]
```

</div>

| Flag | Description |
|----|----|
| `-o`, `--output` (string) | Output format: `json` (the default value) or `yaml`. |

`render` flags

# serve

Serve declarative configs via a GRPC server.

> [!NOTE]
> The declarative config directory is loaded by the `serve` command at startup. Changes made to the declarative config after this command starts are not reflected in the served content.

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm serve <source_path> [<flags>]
```

</div>

| Flag | Description |
|----|----|
| `--cache-dir` (string) | If this flag is set, it syncs and persists the server cache directory. |
| `--cache-enforce-integrity` | Exits with an error if the cache is not present or is invalidated. The default value is `true` when the `--cache-dir` flag is set and the `--cache-only` flag is `false`. Otherwise, the default is `false`. |
| `--cache-only` | Syncs the serve cache and exits without serving. |
| `--debug` | Enables debug logging. |
| `h`, `--help` | Help for serve. |
| `-p`, `--port` (string) | The port number for the service. The default value is `50051`. |
| `--pprof-addr` (string) | The address of the startup profiling endpoint. The format is `Addr:Port`. |
| `-t`, `--termination-log` (string) | The path to a container termination log file. The default value is `/dev/termination-log`. |

`serve` flags

# validate

Validate the declarative config JSON file(s) in a given directory.

<div class="formalpara">

<div class="title">

Command syntax

</div>

``` terminal
$ opm validate <directory> [<flags>]
```

</div>
