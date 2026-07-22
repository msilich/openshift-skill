<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

> [!IMPORTANT]
> All cluster nodes must have the same release version in order for this Operator to function properly. As an example, for nodes running RHCOS, all nodes must have the same RHCOS version.

# Installing the File Integrity Operator using the web console

<div>

<div class="title">

Prerequisites

</div>

- You must have `admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, navigate to **Ecosystem** → **Software Catalog**.

2.  Search for the File Integrity Operator, then click **Install**.

3.  Keep the default selection of **Installation mode** and **namespace** to ensure that the Operator will be installed to the `openshift-file-integrity` namespace.

4.  Click **Install**.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

To confirm that the installation is successful:

</div>

1.  Navigate to the **Ecosystem** → **Installed Operators** page.

2.  Check that the Operator is installed in the `openshift-file-integrity` namespace and its status is `Succeeded`.

If the Operator is not installed successfully:

1.  Navigate to the **Ecosystem** → **Installed Operators** page and inspect the `Status` column for any errors or failures.

2.  Navigate to the **Workloads** → **Pods** page and check the logs in any pods in the `openshift-file-integrity` project that are reporting issues.

# Installing the File Integrity Operator using the CLI

<div>

<div class="title">

Prerequisites

</div>

- You must have `admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Namespace` object YAML file by running:

    ``` terminal
    $ oc create -f <file-name>.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      labels:
        openshift.io/cluster-monitoring: "true"
        pod-security.kubernetes.io/enforce: privileged
      name: openshift-file-integrity
    ```

    </div>

    - In OpenShift Container Platform 4.17, the pod security label must be set to `privileged` at the namespace level.

2.  Create the `OperatorGroup` object YAML file:

    ``` terminal
    $ oc create -f <file-name>.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    apiVersion: operators.coreos.com/v1
    kind: OperatorGroup
    metadata:
      name: file-integrity-operator
      namespace: openshift-file-integrity
    spec:
      targetNamespaces:
      - openshift-file-integrity
    ```

    </div>

3.  Create the `Subscription` object YAML file:

    ``` terminal
    $ oc create -f <file-name>.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: file-integrity-operator
      namespace: openshift-file-integrity
    spec:
      channel: "stable"
      installPlanApproval: Automatic
      name: file-integrity-operator
      source: redhat-operators
      sourceNamespace: openshift-marketplace
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify the installation succeeded by inspecting the CSV file:

    ``` terminal
    $ oc get csv -n openshift-file-integrity
    ```

2.  Verify that the File Integrity Operator is up and running:

    ``` terminal
    $ oc get deploy -n openshift-file-integrity
    ```

</div>

# Additional resources

- [Using Operator Lifecycle Manager in disconnected environments](../../disconnected/using-olm.md#olm-restricted-networks)
