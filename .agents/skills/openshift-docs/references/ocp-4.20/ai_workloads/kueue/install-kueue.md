<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can install Red Hat build of Kueue by using the Red Hat Build of Kueue Operator in OperatorHub.

# Compatible environments

Before you install Red Hat build of Kueue, review this section to ensure that your cluster meets the requirements.

## Supported architectures

Red Hat build of Kueue version 1.1 and later is supported on the following architectures:

- ARM64

- 64-bit x86

- ppc64le (IBM Power®)

- s390x (IBM Z®)

## Supported platforms

Red Hat build of Kueue version 1.1 and later is supported on the following platforms:

- OpenShift Container Platform

- Hosted control planes for OpenShift Container Platform

> [!IMPORTANT]
> Currently, Red Hat build of Kueue is not supported on Red Hat build of MicroShift (MicroShift).

# Installing the Red Hat Build of Kueue Operator

You can install the Red Hat Build of Kueue Operator on a OpenShift Container Platform cluster by using the OperatorHub in the web console.

<div>

<div class="title">

Prerequisites

</div>

- You have administrator permissions on a OpenShift Container Platform cluster.

- You have access to the OpenShift Container Platform web console.

- You have installed and configured the cert-manager Operator for Red Hat OpenShift for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, click **Operators** → **OperatorHub**.

2.  Choose **Red Hat Build of Kueue Operator** from the list of available Operators, and click **Install**.

3.  Select **Enable Operator recommended cluster monitoring on this Namespace**.

    This option sets the `openshift.io/cluster-monitoring: "true"` label in the Namespace object. You must select this option to ensure that cluster monitoring scrapes the `openshift-kueue-operator` namespace.

4.  Click **Install**.

    > [!NOTE]
    > Alternatively, if you are creating the `Namespace` object by using YAML, ensure that you include the `openshift.io/cluster-monitoring: "true"` label:
    >
    > \+
    >
    > ``` yaml
    > apiVersion: v1
    > kind: Namespace
    > metadata:
    >   labels:
    >     openshift.io/cluster-monitoring: "true"
    >   name: openshift-kueue-operator
    > ```

</div>

<div>

<div class="title">

Verification

</div>

- Go to **Operators** → **Installed Operators** and confirm that the **Red Hat Build of Kueue Operator** is listed with **Status** as **Succeeded**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing the cert-manager Operator for Red Hat OpenShift](../../security/cert_manager_operator/cert-manager-operator-install.md#installing-the-cert-manager-operator-for-red-hat-openshift)

</div>

# Upgrading Red Hat build of Kueue

If you have previously installed Red Hat build of Kueue, you must manually upgrade your deployment to the latest version to use the latest bug fixes and feature enhancements.

<div>

<div class="title">

Prerequisites

</div>

- You have installed a previous version of Red Hat build of Kueue.

- You are logged in to the OpenShift Container Platform web console with cluster administrator permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, click **Operators** → **Installed Operators**, then select **Red Hat build of Kueue** from the list.

2.  From the **Actions** drop-down menu, select **Uninstall Operator**.

3.  The **Uninstall Operator?** dialog box opens. Click **Uninstall**.

    > [!IMPORTANT]
    > Selecting the **Delete all operand instances for this operator** checkbox before clicking **Uninstall** deletes all existing resources from the cluster, including:
    >
    > - The `Kueue` CR
    >
    > - Any cluster queues, local queues, or resource flavors that you have created
    >
    > Leave this box unchecked when upgrading your cluster to retain your created resources.

4.  In the OpenShift Container Platform web console, click **Operators** → **OperatorHub**.

5.  Choose **Red Hat Build of Kueue Operator** from the list of available Operators, and click **Install**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Go to **Operators** → **Installed Operators**.

2.  Confirm that the **Red Hat Build of Kueue Operator** is listed with **Status** as **Succeeded**.

3.  Confirm that the version shown under the Operator name in the list is the latest version.

</div>

# Creating a Kueue custom resource

After you have installed the Red Hat Build of Kueue Operator, you must create a `Kueue` custom resource (CR) to configure your installation.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

Ensure that you have completed the following prerequisites:

</div>

- The Red Hat build of Kueue Operator is installed on your cluster.

- You have cluster administrator permissions and the `kueue-batch-admin-role` role.

- You have access to the OpenShift Container Platform web console.

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, click **Operators** → **Installed Operators**.

2.  In the **Provided APIs** table column, click **Kueue**. This takes you to the **Kueue** tab of the **Operator details** page.

3.  Click **Create Kueue**. This takes you to the **Create Kueue** YAML view.

4.  Enter the details for your `Kueue` CR.

    <div class="formalpara">

    <div class="title">

    Example `Kueue` CR

    </div>

    ``` yaml
    apiVersion: kueue.openshift.io/v1
    kind: Kueue
    metadata:
      labels:
        app.kubernetes.io/name: kueue-operator
        app.kubernetes.io/managed-by: kustomize
      name: cluster
      namespace: openshift-kueue-operator
    spec:
      managementState: Managed
      config:
        integrations:
          frameworks:
          - BatchJob
        preemption:
          preemptionPolicy: Classical
    # ...
    ```

    </div>

    - The name of the `Kueue` CR must be `cluster`.

    - If you want to configure Red Hat build of Kueue for use with other workload types, add those types here. The default configuration is `BatchJob`. Additional types are `Pod`, `Deployment`, and `StatefulSet`.

    - Optional: If you want to configure fair sharing for Red Hat build of Kueue, set the `preemptionPolicy` value to `FairSharing`. The default setting in the `Kueue` CR is `Classical` preemption.

5.  Click **Create**.

</div>

<div>

<div class="title">

Verification

</div>

- After you create the `Kueue` CR, the web console brings you to the **Operator details** page, where you can see the CR in the list of **Kueues**.

- Optional: If you have the OpenShift CLI (`oc`) installed, you can run the following command and observe the output to confirm that your `Kueue` CR has been created successfully:

  ``` terminal
  $ oc get kueue
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME         AGE
  cluster     4m
  ```

  </div>

</div>

# Labeling namespaces to allow Red Hat build of Kueue to manage jobs

The Red Hat build of Kueue Operator uses an opt-in webhook mechanism to ensure that policies are only enforced for the jobs and namespaces that it is expected to target.

You must label the namespaces where you want Red Hat build of Kueue to manage jobs with the `kueue.openshift.io/managed=true` label.

<div>

<div class="title">

Prerequisites

</div>

- You have cluster administrator permissions.

- The Red Hat build of Kueue Operator is installed on your cluster, and you have created a `Kueue` custom resource (CR).

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Add the `kueue.openshift.io/managed=true` label to a namespace by running the following command:

  ``` terminal
  $ oc label namespace <namespace> kueue.openshift.io/managed=true
  ```

</div>

When you add this label, you instruct the Red Hat build of Kueue Operator that the namespace is managed by its webhook admission controllers. As a result, any Red Hat build of Kueue resources within that namespace are properly validated and mutated.
