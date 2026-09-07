<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the CLI tool to manage Red Hat OpenShift Pipelines from a terminal. The following section describes how to install the CLI tool on different platforms.

You can also find the URL to the latest binaries from the OpenShift Container Platform web console by clicking the **?** icon in the upper-right corner and selecting **Command Line Tools**.

> [!NOTE]
> Both the archives and the RPMs contain the following executables:
>
> - `tkn`
>
> - `tkn-pac`
>
> - `opc`

> [!IMPORTANT]
> Running Red Hat OpenShift Pipelines with the `opc` CLI tool is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Installing the Red Hat OpenShift Pipelines CLI on Linux

For Linux distributions, you can download the CLI as a `tar.gz` archive.

<div>

<div class="title">

Procedure

</div>

1.  Download the relevant CLI tool.

    - [Linux (x86_64, amd64)](https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.18.0/tkn-linux-amd64.tar.gz)

    - [Linux on IBM Z® and IBM® LinuxONE (s390x)](https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.18.0/tkn-linux-s390x.tar.gz)

    - [Linux on IBM Power® (ppc64le)](https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.18.0/tkn-linux-ppc64le.tar.gz)

    - [Linux on ARM (aarch64, arm64)](https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.18.0/tkn-linux-arm64.tar.gz)

</div>

1.  Unpack the archive:

    ``` terminal
    $ tar xvzf <file>
    ```

2.  Add the location of your `tkn`, `tkn-pac`, and `opc` files to your `PATH` environment variable.

3.  To check your `PATH`, run the following command:

    ``` terminal
    $ echo $PATH
    ```

# Installing the Red Hat OpenShift Pipelines CLI on Linux using an RPM

For Red Hat Enterprise Linux (RHEL) version 8, you can install the Red Hat OpenShift Pipelines CLI as an RPM.

<div>

<div class="title">

Prerequisites

</div>

- You have an active OpenShift Container Platform subscription on your Red Hat account.

- You have root or sudo privileges on your local system.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Register with Red Hat Subscription Manager:

    ``` terminal
    # subscription-manager register
    ```

2.  Pull the latest subscription data:

    ``` terminal
    # subscription-manager refresh
    ```

3.  List the available subscriptions:

    ``` terminal
    # subscription-manager list --available --matches '*pipelines*'
    ```

4.  In the output for the previous command, find the pool ID for your OpenShift Container Platform subscription and attach the subscription to the registered system:

    ``` terminal
    # subscription-manager attach --pool=<pool_id>
    ```

5.  Enable the repositories required by Red Hat OpenShift Pipelines:

    - Linux (x86_64, amd64)

      ``` terminal
      # subscription-manager repos --enable="pipelines-1.18-for-rhel-8-x86_64-rpms"
      ```

    - Linux on IBM Z® and IBM® LinuxONE (s390x)

      ``` terminal
      # subscription-manager repos --enable="pipelines-1.18-for-rhel-8-s390x-rpms"
      ```

    - Linux on IBM Power® (ppc64le)

      ``` terminal
      # subscription-manager repos --enable="pipelines-1.18-for-rhel-8-ppc64le-rpms"
      ```

    - Linux on ARM (aarch64, arm64)

      ``` terminal
      # subscription-manager repos --enable="pipelines-1.18-for-rhel-8-aarch64-rpms"
      ```

6.  Install the `openshift-pipelines-client` package:

    ``` terminal
    # yum install openshift-pipelines-client
    ```

</div>

After you install the CLI, it is available using the `tkn` command:

``` terminal
$ tkn version
```

# Installing the Red Hat OpenShift Pipelines CLI on Windows

For Windows, you can download the CLI as a `zip` archive.

<div>

<div class="title">

Procedure

</div>

1.  Download the [CLI tool](https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.18.0/tkn-windows-amd64.zip).

2.  Extract the archive with a ZIP program.

3.  Add the location of your `tkn`, `tkn-pac`, and `opc` files to your `PATH` environment variable.

4.  To check your `PATH`, run the following command:

    ``` terminal
    C:\> path
    ```

</div>

# Installing the Red Hat OpenShift Pipelines CLI on macOS

For macOS, you can download the CLI as a `tar.gz` archive.

<div>

<div class="title">

Procedure

</div>

1.  Download the relevant CLI tool.

    - [macOS](https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.18.0/tkn-macos-amd64.tar.gz)

    - [macOS on ARM](https://mirror.openshift.com/pub/openshift-v4/clients/pipelines/1.18.0/tkn-macos-arm64.tar.gz)

2.  Unpack and extract the archive.

3.  Add the location of your `tkn`, `tkn-pac`, and `opc` files to your `PATH` environment variable.

4.  To check your `PATH`, run the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>
