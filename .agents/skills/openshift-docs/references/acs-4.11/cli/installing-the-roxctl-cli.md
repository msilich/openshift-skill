<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

`roxctl` is a command-line interface (CLI) for running commands on Red Hat Advanced Cluster Security for Kubernetes (RHACS). You can install the `roxctl` CLI by downloading the binary or you can run the `roxctl` CLI from a container image.

<a id="installing-the-roxctl-cli-by-downloading-the-binary_installing-roxctl-cli"></a>

# Installing the roxctl CLI by downloading the binary

You can install the `roxctl` CLI to interact with RHACS from a command-line interface. You can install `roxctl` on Linux, Windows, or macOS.

<a id="installing-cli-on-linux_installing-roxctl-cli"></a>

## Installing the roxctl CLI on Linux

You can install the `roxctl` CLI binary on Linux by using the following procedure.

> [!NOTE]
> `roxctl` CLI for Linux is available for `amd64`, `arm64`, `ppc64le`, and `s390x` architectures.

<div>

<div class="title">

Procedure

</div>

1.  Find the `roxctl` architecture for the target operating system:

    ``` terminal
    $ arch="$(uname -m | sed "s/x86_64//")"; arch="${arch:+-$arch}"
    ```

2.  Download the `roxctl` CLI:

    ``` terminal
    $ curl -L -f -o roxctl "https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Linux/roxctl${arch}"
    ```

3.  Make the `roxctl` binary executable:

    ``` terminal
    $ chmod +x roxctl
    ```

4.  Place the `roxctl` binary in a directory that is on your `PATH`:

    To check your `PATH`, run the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="installing-cli-on-macos_installing-roxctl-cli"></a>

## Installing the roxctl CLI on macOS

You can install the `roxctl` CLI binary on macOS by using the following procedure.

> [!NOTE]
> `roxctl` CLI for macOS is available for `amd64` and `arm64` architectures.

<div>

<div class="title">

Procedure

</div>

1.  Find the `roxctl` architecture for the target operating system:

    ``` terminal
    $ arch="$(uname -m | sed "s/x86_64//")"; arch="${arch:+-$arch}"
    ```

2.  Download the `roxctl` CLI:

    ``` terminal
    $ curl -L -f -o roxctl "https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Darwin/roxctl${arch}"
    ```

3.  Remove all extended attributes from the binary:

    ``` terminal
    $ xattr -c roxctl
    ```

4.  Make the `roxctl` binary executable:

    ``` terminal
    $ chmod +x roxctl
    ```

5.  Place the `roxctl` binary in a directory that is on your `PATH`:

    To check your `PATH`, run the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="installing-cli-on-windows_installing-roxctl-cli"></a>

## Installing the roxctl CLI on Windows

You can install the `roxctl` CLI binary on Windows by using the following procedure.

> [!NOTE]
> `roxctl` CLI for Windows is available for the `amd64` architecture.

<div>

<div class="title">

Procedure

</div>

- Download the `roxctl` CLI:

  ``` terminal
  $ curl -f -O https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Windows/roxctl.exe
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="run-roxctl-from-container_installing-roxctl-cli"></a>

# Running the roxctl CLI from a container

The `roxctl` client is the default entry point in the RHACS `roxctl` image. To run the `roxctl` client in a container image:

<div>

<div class="title">

Prerequisites

</div>

- You must first generate an authentication token from the RHACS portal.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the `registry.redhat.io` registry.

    ``` terminal
    $ docker login registry.redhat.io
    ```

2.  Pull the latest container image for the `roxctl` CLI.

    ``` terminal
    $ docker pull registry.redhat.io/advanced-cluster-security/rhacs-roxctl-rhel9:4.11.3
    ```

    After you install the CLI, you can run it by using the following command:

    ``` terminal
    $ docker run -e ROX_API_TOKEN=$ROX_API_TOKEN \
      -it registry.redhat.io/advanced-cluster-security/rhacs-roxctl-rhel9:4.11.3 \
      -e $ROX_CENTRAL_ADDRESS <command>
    ```

</div>

<div class="informalexample">

In Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service), when using `roxctl` commands that require the Central address, use the **Central instance address** as displayed in the **Instance Details** section of the Red Hat Hybrid Cloud Console. For example, use `acs-ABCD12345.acs.rhcloud.com` instead of `acs-data-ABCD12345.acs.rhcloud.com`.

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed.

  ``` terminal
  $ docker run -it registry.redhat.io/advanced-cluster-security/rhacs-roxctl-rhel9:4.11.3 version
  ```

</div>
