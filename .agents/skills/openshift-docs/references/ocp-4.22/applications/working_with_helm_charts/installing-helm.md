<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Install the Helm CLI to manage software packages on your OpenShift Container Platform cluster from a local workstation.

You can also find the URL to the latest binaries from the OpenShift Container Platform web console by clicking the **?** icon in the upper-right corner and selecting **Command Line Tools**.

# On Linux

1.  Download the Helm binary:

    - Linux (x86_64, amd64)

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-amd64 -o /usr/local/bin/helm
      ```

    - Linux on IBM Z® and IBM® LinuxONE (s390x)

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-s390x -o /usr/local/bin/helm
      ```

    - Linux on IBM Power® (ppc64le)

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-ppc64le -o /usr/local/bin/helm
      ```

    - Linux on ARM (arm64)

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-arm64 -o /usr/local/bin/helm
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
    version.BuildInfo{Version:"v3.0", GitCommit:"b31719aab7963acf4887a1c1e6d5e53378e34d93", GitTreeState:"clean", GoVersion:"go1.13.4"}
    ```

    </div>

# On Windows

1.  Download the Helm binary: [`.exe` file](https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-windows-amd64.exe).

2.  Click **Search** and type `env` or `environment`.

3.  Select **Edit environment variables for your account**.

4.  Select **Path** from the **Variable** section and click **Edit**.

5.  Click **New** and type the path to the directory with the exe file into the field or click **Browse** and select the directory, and click **OK**.

# On macOS

1.  Download the Helm binary:

    - For macOS on Intel (x86_64):

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-darwin-amd64 -o /usr/local/bin/helm
      ```

    - For macOS on ARM (Apple Silicon):

      ``` terminal
      # curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-darwin-arm64 -o /usr/local/bin/helm
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
    version.BuildInfo{Version:"v3.0", GitCommit:"b31719aab7963acf4887a1c1e6d5e53378e34d93", GitTreeState:"clean", GoVersion:"go1.13.4"}
    ```

    </div>
