<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can extract the `cluster-compare` plugin from a container image in the Red Hat container catalog and use it as a plugin to the `oc` command.

# Installing the cluster-compare plugin

Install the `cluster-compare` plugin to compare a reference configuration with a cluster configuration from a live cluster or `must-gather` data.

<div>

<div class="title">

Prerequisites

</div>

1.  You have installed the OpenShift CLI (`oc`).

2.  You installed `podman`.

3.  You have access to the Red Hat container catalog.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the Red Hat container catalog by running the following command:

    ``` terminal
    $ podman login registry.redhat.io
    ```

2.  Create a container for the `cluster-compare` image by running the following command:

    ``` terminal
    $ podman create --name cca registry.redhat.io/openshift4/kube-compare-artifacts-rhel9:latest
    ```

3.  Copy the `cluster-compare` plugin to a directory that is included in your `PATH` environment variable by running the following command:

    ``` terminal
    $ podman cp cca:/usr/share/openshift/<arch>/kube-compare.<rhel_version> <directory_on_path>/kubectl-cluster_compare
    ```

    - `arch` is the architecture for your machine. Valid values are:

      - `linux_amd64`

      - `linux_arm64`

      - `linux_ppc64le`

      - `linux_s390x`

    - `<rhel_version>` is the version of RHEL on your machine. Valid values are `rhel8` or `rhel9`.

    - `<directory_on_path>` is the path to a directory included in your `PATH` environment variable.

</div>

<div>

<div class="title">

Verification

</div>

- View the help for the plugin by running the following command:

  ``` terminal
  $ oc cluster-compare -h
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Compare a known valid reference configuration and a set of specific cluster configuration CRs.

  ...

  Usage:
    compare -r <Reference File>

  Examples:
    # Compare a known valid reference configuration with a live cluster:
    kubectl cluster-compare -r ./reference/metadata.yaml

   ...
  ```

  </div>

</div>

# Additional resources

- [Extending the OpenShift CLI with plugins](../../cli_reference/openshift_cli/extending-cli-plugins.md#cli-extend-plugins)
