<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Install the Helm CLI to manage software packages on your OpenShift Container Platform cluster from a local workstation.

In OpenShift Container Platform 4.22, you can use the Helm v3 CLI or the Helm v4 CLI. You can keep using the Helm v3 CLI in OpenShift Container Platform 5.0, but you must move to Helm v4 before you upgrade to a later OpenShift Container Platform release.

You can find the URL to the latest binaries in the OpenShift Container Platform web console by clicking the help icon (**?**) and selecting **Command Line Tools**.

Replace `<version>` in the curl commands with a Helm version that is compatible with your OpenShift Container Platform cluster version. Use the exact version folder name from the Helm CLI download directory. To find a compatible version, and for information about moving from Helm v3 to Helm v4, see the Red Hat Knowledgebase article "Helm CLI for Red Hat OpenShift compatibility matrix."

The following are the procedures to install the Helm CLI on Linux, Windows, and macOS. Complete the procedure for your operating system.

# On Linux

1.  Download the Helm binary by running the command for your system architecture:

    - Linux (x86_64, amd64)

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/cgw/helm/<version>/helm-linux-amd64 -o /usr/local/bin/helm
      ```

    - Linux on IBM Z® and IBM® LinuxONE (s390x)

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/cgw/helm/<version>/helm-linux-s390x -o /usr/local/bin/helm
      ```

    - Linux on IBM Power® (ppc64le)

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/cgw/helm/<version>/helm-linux-ppc64le -o /usr/local/bin/helm
      ```

    - Linux on ARM (arm64)

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/cgw/helm/<version>/helm-linux-arm64 -o /usr/local/bin/helm
      ```

2.  Make the binary file executable:

    ``` terminal
    # chmod +x /usr/local/bin/helm
    ```

3.  Check the installed version:

    ``` terminal
    $ helm version
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    version.BuildInfo{Version:"v4.3.0", GitCommit:"c34fd182358aabf30e6c6c5e9bb2733da4d6b9da", GitTreeState:"clean", GoVersion:"go1.26.7 (Red Hat 1.26.7-1.el9_8)", KubeClientVersion:"v1.37"}
    ```

    </div>

# On Windows

1.  Go to the Helm CLI download directory, open the folder for your Helm version, and download `helm-windows-amd64.exe`.

2.  Click **Search** and type `env` or `environment`.

3.  Select **Edit environment variables for your account**.

4.  Select **Path** from the **Variable** section and click **Edit**.

5.  Click **New** and type the path to the directory with the exe file into the field or click **Browse** and select the directory, and click **OK**.

# On macOS

1.  Download the Helm binary by running the command for your system architecture:

    - For macOS on Intel (x86_64):

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/cgw/helm/<version>/helm-darwin-amd64 -o /usr/local/bin/helm
      ```

    - For macOS on ARM (Apple Silicon):

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/cgw/helm/<version>/helm-darwin-arm64 -o /usr/local/bin/helm
      ```

2.  Make the binary file executable:

    ``` terminal
    # chmod +x /usr/local/bin/helm
    ```

3.  Check the installed version:

    ``` terminal
    $ helm version
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    version.BuildInfo{Version:"v4.3.0", GitCommit:"c34fd182358aabf30e6c6c5e9bb2733da4d6b9da", GitTreeState:"clean", GoVersion:"go1.26.7 (Red Hat 1.26.7-1.el9_8)", KubeClientVersion:"v1.37"}
    ```

    </div>

# Additional resources

- [Helm CLI for Red Hat OpenShift compatibility matrix](https://access.redhat.com/articles/7145580)

- [Helm CLI download directory](https://mirror.openshift.com/pub/cgw/helm/)
