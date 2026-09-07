<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the GitOps `argocd` CLI tool to configure and manage Red Hat OpenShift GitOps and Argo CD resources from the command line. You can install it on Linux, macOS, and Windows.

> [!NOTE]
> Both the compressed archives and the RPMs contain the `argocd` executable binary file. If you have an active OpenShift Container Platform subscription on your Red Hat account, install the CLI tool as an RPM by using a package manager, such as `yum` or `dnf`.

# Installing the Red Hat OpenShift GitOps CLI on Linux

For Linux distributions, you can download the GitOps `argocd` CLI as a `tar.gz` archive.

<div>

<div class="title">

Procedure

</div>

1.  Download the latest version of the CLI tool from the [content gateway](https://developers.redhat.com/content-gateway/rest/browse/pub/openshift-v4/clients/openshift-gitops/latest/) for your operating system and architecture.

    | Operating system | Architecture | Tarball |
    |----|----|----|
    | Linux | x86_64, amd64 | `argocd-linux-amd64.tar.gz` |
    | Linux on IBM zSystems and IBM® LinuxONE | s390x | `argocd-linux-s390x.tar.gz` |
    | Linux on IBM Power | ppc64le | `argocd-linux-ppc64le.tar.gz` |
    | Linux on ARM | aarch64, arm64 | `argocd-linux-arm64.tar.gz` |

    > [!NOTE]
    > Newer versions of the CLI tool are compatible with the older versions of Red Hat OpenShift GitOps server, but not vice versa.

2.  Extract the archive by running the following command:

    ``` terminal
    $ tar xvzf <file>
    ```

3.  Move the binary to a directory on your `PATH` environment variable by running the following command:

    ``` terminal
    $ sudo mv argocd /usr/local/bin/argocd
    ```

4.  Make the file executable by running the following command:

    ``` terminal
    $ sudo chmod +x /usr/local/bin/argocd
    ```

5.  After you install the GitOps `argocd` CLI, verify that it is available by running the following command:

    ``` terminal
    $ argocd version --client
    ```

    **Example output:**

    ``` terminal
    argocd: v2.9.5+f943664
      BuildDate: 2024-02-15T05:19:27Z
      GitCommit: f9436641a616d277ab1f98694e5ce4c986d4ea05
      GitTreeState: clean
      GoVersion: go1.20.10
      Compiler: gc
      Platform: linux/amd64
      ExtraBuildInfo: openshift-gitops-version: 1.19.0, release: 0015022024
    ```

    where:

    `ExtraBuildInfo: openshift-gitops-version`
    Specifies the build information of Red Hat OpenShift GitOps built by Red Hat.

</div>

# Installing the Red Hat OpenShift GitOps CLI on Linux using an RPM

For Red Hat Enterprise Linux (RHEL) version 8 or later, you can install the GitOps `argocd` CLI as an RPM by using a package manager, such as `yum` or `dnf`. This allows the GitOps `argocd` CLI version to be automatically managed by the system. For example, using a command such as `dnf upgrade` upgrades all packages, including `argocd`, if a new version is available.

<div>

<div class="title">

Prerequisites

</div>

- You have an active OpenShift Container Platform subscription on your Red Hat account.

- You have root or `sudo` privileges on your local system.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Register with Red Hat Subscription Manager by running the following command:

    ``` terminal
    # subscription-manager register
    ```

2.  Pull the latest subscription data by running the following command:

    ``` terminal
    # subscription-manager refresh
    ```

3.  List the available subscriptions by running the following command:

    ``` terminal
    # subscription-manager list --available --matches '*gitops*'
    ```

4.  In the output for the previous command, find the pool ID for your OpenShift Container Platform subscription, and attach the subscription to the registered system by running the following command:

    ``` terminal
    # subscription-manager attach --pool=<pool_id>
    ```

5.  Enable the repositories required by Red Hat OpenShift GitOps for RHEL version 8 or later by running the following command:

    - Linux (x86_64, amd64)

      ``` terminal
      # subscription-manager repos --enable="gitops-<gitops_version>-for-rhel-<rhel_version>-x86_64-rpms"
      ```

      **Example command:**

      ``` terminal
      # subscription-manager repos --enable="gitops-1.21-for-rhel-8-x86_64-rpms"
      ```

    - Linux on IBM zSystems and IBM® LinuxONE (s390x)

      ``` terminal
      # subscription-manager repos --enable="gitops-<gitops_version>-for-rhel-<rhel_version>-s390x-rpms"
      ```

      **Example command:**

      ``` terminal
      # subscription-manager repos --enable="gitops-1.21-for-rhel-8-s390x-rpms"
      ```

    - Linux on IBM Power (ppc64le)

      ``` terminal
      # subscription-manager repos --enable="gitops-<gitops_version>-for-rhel-<rhel_version>-ppc64le-rpms"
      ```

      **Example command:**

      ``` terminal
      # subscription-manager repos --enable="gitops-1.21-for-rhel-8-ppc64le-rpms"
      ```

    - Linux on ARM (aarch64, arm64)

      ``` terminal
      # subscription-manager repos --enable="gitops-<gitops_version>-for-rhel-<rhel_version>-aarch64-rpms"
      ```

      **Example command:**

      ``` terminal
      # subscription-manager repos --enable="gitops-1.21-for-rhel-8-aarch64-rpms"
      ```

6.  Install the `openshift-gitops-argocd-cli` package by running the following command:

    ``` terminal
    # yum install openshift-gitops-argocd-cli
    ```

7.  After you install the GitOps `argocd` CLI, verify that it is available by running the following command:

    ``` terminal
    $ argocd version --client
    ```

    **Example output:**

    ``` terminal
    argocd: v2.9.5+f943664
      BuildDate: 2024-02-15T05:19:27Z
      GitCommit: f9436641a616d277ab1f98694e5ce4c986d4ea05
      GitTreeState: clean
      GoVersion: go1.20.10
      Compiler: gc
      Platform: linux/amd64
      ExtraBuildInfo: openshift-gitops-version: 1.19.0, release: 0015022024
    ```

    where:

    `ExtraBuildInfo: openshift-gitops-version`
    Specifies the build information of Red Hat OpenShift GitOps built by Red Hat.

</div>

# Installing the Red Hat OpenShift GitOps CLI on Windows

For Windows, you can download the GitOps `argocd` CLI as a compressed `zip` archive.

<div>

<div class="title">

Procedure

</div>

1.  Download the latest version of the CLI tool from the [content gateway](https://developers.redhat.com/content-gateway/rest/browse/pub/openshift-v4/clients/openshift-gitops/latest/) for your operating system and architecture.

    | Operating system | Architecture | Archive                    |
    |------------------|--------------|----------------------------|
    | Windows          | x86_64       | `argocd-windows-amd64.zip` |

    > [!NOTE]
    > Newer versions of the CLI tool are compatible with the older versions of Red Hat OpenShift GitOps server, but not vice versa.

2.  Extract the archive with a ZIP program.

3.  Move the binary to a directory on your `PATH` environment variable by running the following command:

    ``` terminal
    C:\> move argocd.exe <directory>
    ```

4.  After you install the GitOps `argocd` CLI, verify that it is available by running the following command:

    ``` terminal
    $ argocd version --client
    ```

    **Example output:**

    ``` terminal
    argocd: v2.9.5+f943664
      BuildDate: 2024-02-15T05:19:27Z
      GitCommit: f9436641a616d277ab1f98694e5ce4c986d4ea05
      GitTreeState: clean
      GoVersion: go1.20.10
      Compiler: gc
      Platform: windows/amd64
      ExtraBuildInfo: openshift-gitops-version: 1.19.0, release: 0015022024
    ```

    where:

    `ExtraBuildInfo: openshift-gitops-version`
    Specifies the build information of Red Hat OpenShift GitOps built by Red Hat.

</div>

# Installing the Red Hat OpenShift GitOps CLI on macOS

For macOS, you can download the GitOps `argocd` CLI as a `tar.gz` archive.

<div>

<div class="title">

Procedure

</div>

1.  Download the latest version of the CLI tool from the [content gateway](https://developers.redhat.com/content-gateway/rest/browse/pub/openshift-v4/clients/openshift-gitops/latest/) for your operating system and architecture.

    | Operating system | Architecture | Tarball                     |
    |------------------|--------------|-----------------------------|
    | macOS on Intel   | x86_64       | `argocd-macos-amd64.tar.gz` |
    | macOS on ARM     | arm64        | `argocd-macos-arm64.tar.gz` |

    > [!NOTE]
    > Newer versions of the CLI tool are compatible with the older versions of Red Hat OpenShift GitOps server, but not vice versa.

2.  Extract the archive by running the following command:

    ``` terminal
    $ tar xvzf <file>
    ```

3.  Move the binary to a directory on your `PATH` environment variable by running the following command:

    ``` terminal
    $ sudo mv argocd /usr/local/bin/argocd
    ```

4.  Make the file executable by running the following command:

    ``` terminal
    $ sudo chmod +x /usr/local/bin/argocd
    ```

5.  After you install the GitOps `argocd` CLI, verify that it is available by running the following command:

    ``` terminal
    $ argocd version --client
    ```

    **Example output:**

    ``` terminal
    argocd: v2.9.5+f943664
      BuildDate: 2024-02-15T05:19:27Z
      GitCommit: f9436641a616d277ab1f98694e5ce4c986d4ea05
      GitTreeState: clean
      GoVersion: go1.20.10
      Compiler: gc
      Platform: darwin/amd64
      ExtraBuildInfo: openshift-gitops-version: 1.19.0, release: 0015022024
    ```

    where:

    `ExtraBuildInfo: openshift-gitops-version`
    Specifies the build information of Red Hat OpenShift GitOps built by Red Hat.

</div>

# Additional resources

- [Configuring the GitOps CLI](../gitops_cli_argocd/configuring-argocd-gitops-cli.md#configuring-argocd-gitops-cli)

- [Logging in to the Argo CD server in the default mode](../gitops_cli_argocd/logging-in-to-argocd-server-in-default-mode.md#logging-in-to-argocd-server-in-default-mode)

- [Basic GitOps argocd commands](../gitops_cli_argocd/argocd-gitops-cli-reference.md#argocd-gitops-cli-reference)

- [Installing Red Hat OpenShift GitOps](installing-openshift-gitops.md#installing-openshift-gitops)

- [Setting up a new Argo CD instance](../argocd_instance/setting-up-argocd-instance.md#setting-up-argocd-instance)
