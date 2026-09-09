<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can create and manage policies as code by saving policies as Kubernetes custom resources (CRs) and applying them to clusters by using a Kubernetes-native continuous delivery (CD) tool such as Argo CD.

<a id="policy-as-code-about_managing-policies-as-code"></a>

# Managing polices as code

You can create and manage policies as code by saving policies as Kubernetes custom resources (CRs) and applying them to clusters by using a Kubernetes-native continuous delivery (CD) tool such as Argo CD.

Policy as code is useful for Kubernetes security architects who want to author policies in YAML or JSON instead of using the RHACS portal. GitOps administrators who already manage Kubernetes configurations by using a GitOps workflow can also find it useful.

RHACS provides the ability to use default policies or create custom policies for your system. With the policy as code feature, you can create custom policies locally by downloading them and modifying them, or by creating them from empty files. To author policies locally, you create CRs that represent the desired state of the policies. You then use a continuous delivery tool such as Argo CD to track, manage, and apply policies to your clusters that are running RHACS. After you create or update CRs and use the CI/CD tool to apply them, the policies stored in the RHACS database are created or updated.

With this feature, RHACS installs a new Kubernetes controller in the namespace where Central is installed, typically the `stackrox` namespace. With an Argo CD workflow, you configure Argo CD to apply policy as code resources to the same namespace in which RHACS is installed. After you configure this connection, the controller in RHACS receives information from the Kubernetes API about new, updated, or deleted policies that are managed as individual Kubernetes CR files. RHACS reconciles the policy CR to the policy stored in the RHACS database.

With a GitOps workflow that does not use Argo CD, you configure your GitOps repository to connect to Central in RHACS through the RHACS API. A CR is not used.

<a id="policy-as-code-drift_managing-policies-as-code"></a>

## About policy drift

Because policies can be edited, deleted, and created in the RHACS portal and also externally, sometimes *policy drift* can occur. Drift occurs when the version of a policy in Central in RHACS does not match the version of the policy in Kubernetes.

Drift can occur when a change is applied to an externally-managed policy by using the RHACS portal or the API instead of by modifying its Kubernetes custom resource. RHACS does not prevent drift, but it is not recommended. Drift is automatically resolved within ten hours after it was introduced.

<a id="policy-as-code-create-portal_managing-policies-as-code"></a>

## Creating policies in code by using the RHACS portal

You can create new policies in code by using the RHACS portal to save existing policies as YAML files.

<div>

<div class="title">

Prerequisites

</div>

- You must have RHACS release 4.6 or later installed.

- If you installed RHACS by using the manifest installation method, also called the `roxctl` method, you must manually apply the `config.stackrox.io` CRD that is located in the .zip file at `helm/chart/crds/config.stackrox.io_securitypolicies.yaml` by using the following command:

  ``` terminal
  $ kubectl create -f helm/chart/crds/config.stackrox.io_securitypolicies.yaml
  ```

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

To create a new policy in code by using the RHACS portal to create the CR:

</div>

1.  In the **Policy Management** page, create a new policy or clone a default policy.

    > [!NOTE]
    > You must clone a default policy before you can save it as a CR.

2.  In the row listing the policy, click the overflow menu, ![kebab](../../images/kebab.png), and then select **Save as Custom Resource**. To save multiple policies at one time, you can select them and click **Bulk actions** → **Save as Custom Resources**.

3.  After editing your policy, you can apply the saved CR by doing one of the following:

    - Use the `oc apply` or `kubectl apply` command to apply the CR directly to the Kubernetes namespace where Central is installed.

    - Use Argo CD or your GitOps tool to push the CR to the Kubernetes namespace where Central is installed.

<a id="policy-as-code-create-cr_managing-policies-as-code"></a>

## Creating policies in code by constructing a CR

You can create new policies in code by constructing a CR for the policy.

1.  Use an editor to construct a CR for the policy with the following attributes:

    ``` yaml
    kind: SecurityPolicy
    apiVersion: config.stackrox.io/v1alpha1
    metadata:
      name: short-name
    spec:
      policyName: A longer form name
    # ...
    ```

    > [!TIP]
    > Use online documentation, for example, by entering the `kubectl explain securitypolicy.spec` command, to understand the fields available for defining a policy specification.

2.  Apply the saved CR by doing one of the following:

    - Use the `oc apply` or `kubectl apply` command to apply the CR directly to the Kubernetes namespace where Central is installed.

    - Use Argo CD or your GitOps tool to push the CR to the Kubernetes namespace where Central is installed.

<a id="policy-as-code-disable_managing-policies-as-code"></a>

## Disabling the policy as code feature

The policy as code feature is automatically enabled when you install RHACS, but you can disable it.

> [!NOTE]
> For OpenShift Container Platform, use `oc` instead of `kubectl`.

<div class="formalpara">

<div class="title">

Procedure

</div>

To disable the policy as code feature, complete one of the following tasks, depending on the method you used to install RHACS:

</div>

- If you installed RHACS by using the Operator, set the `spec.configAsCode.configAsCodeComponent` field to `Disabled`.

- If you installed RHACS by using Helm charts, set the `configAsCode.enabled` field in the `values.yaml` file to `false`.

- If you installed RHACS by using the manifest installation method, also known as the `roxctl` method, delete the `config-controller` deployment by running the following command:

  ``` terminal
  $ kubectl -n stackrox delete deployment config-controller
  ```
