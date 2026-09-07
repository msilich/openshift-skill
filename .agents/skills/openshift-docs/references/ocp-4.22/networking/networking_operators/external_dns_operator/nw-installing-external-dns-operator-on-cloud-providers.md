<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To manage DNS records on your cloud infrastructure, install the External DNS Operator. This Operator supports deployment on major cloud providers, including Amazon Web Services (AWS), Microsoft Azure, and Google Cloud.

# Installing the External DNS Operator with the Software Catalog

You can install the External DNS Operator by using the OpenShift Container Platform Software Catalog. You can then manage the Operator lifecycle directly from the web console.

<div>

<div class="title">

Procedure

</div>

1.  Click **Ecosystem** → **Software Catalog** in the OpenShift Container Platform web console.

2.  Click **External DNS Operator**. You can use the **Filter by keyword** text box or the filter list to search for External DNS Operator from the list of Operators.

3.  Select the `external-dns-operator` namespace.

4.  On the **External DNS Operator** page, click **Install**.

5.  On the **Install Operator** page, ensure that you selected the following options:

    1.  Update the channel as **stable-v1**.

    2.  Installation mode as **A specific name on the cluster**.

    3.  Installed namespace as `external-dns-operator`. If namespace `external-dns-operator` does not exist, the Operator gets created during the Operator installation.

    4.  Select **Approval Strategy** as **Automatic** or **Manual**. The Approval Strategy defaults to **Automatic**.

    5.  Click **Install**.

        If you select **Automatic** updates, the Operator Lifecycle Manager (OLM) automatically upgrades the running instance of your Operator without any intervention.

        If you select **Manual** updates, the OLM creates an update request. As a cluster administrator, you must then manually approve that update request to have the Operator updated to the new version.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the External DNS Operator shows the **Status** as **Succeeded** on the **Installed Operators** dashboard.

</div>

# Installing the External DNS Operator by using the CLI

You can use the OpenShift CLI (`oc`) to install the External DNS Operator. The Operator manages the installation process directly from your terminal without you having to use the web console.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Namespace` object:

    1.  Create a YAML file that defines the `Namespace` object:

        <div class="formalpara">

        <div class="title">

        Example `namespace.yaml` file

        </div>

        ``` yaml
        apiVersion: v1
        kind: Namespace
        metadata:
          name: external-dns-operator
        # ...
        ```

        </div>

    2.  Create the `Namespace` object by running the following command:

        ``` terminal
        $ oc apply -f namespace.yaml
        ```

2.  Create an `OperatorGroup` object:

    1.  Create a YAML file that defines the `OperatorGroup` object:

        <div class="formalpara">

        <div class="title">

        Example `operatorgroup.yaml` file

        </div>

        ``` yaml
        apiVersion: operators.coreos.com/v1
        kind: OperatorGroup
        metadata:
          name: external-dns-operator
          namespace: external-dns-operator
        spec:
          upgradeStrategy: Default
          targetNamespaces:
          - external-dns-operator
        # ...
        ```

        </div>

    2.  Create the `OperatorGroup` object by running the following command:

        ``` terminal
        $ oc apply -f operatorgroup.yaml
        ```

3.  Create a `Subscription` object:

    1.  Create a YAML file that defines the `Subscription` object:

        <div class="formalpara">

        <div class="title">

        Example `subscription.yaml` file

        </div>

        ``` yaml
        apiVersion: operators.coreos.com/v1alpha1
        kind: Subscription
        metadata:
          name: external-dns-operator
          namespace: external-dns-operator
        spec:
          channel: stable-v1
          installPlanApproval: Automatic
          name: external-dns-operator
          source: redhat-operators
          sourceNamespace: openshift-marketplace
        # ...
        ```

        </div>

    2.  Create the `Subscription` object by running the following command:

        ``` terminal
        $ oc apply -f subscription.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Get the name of the install plan from the subscription by running the following command:

    ``` terminal
    $ oc -n external-dns-operator \
      get subscription external-dns-operator \
      --template='{{.status.installplan.name}}{{"\n"}}'
    ```

2.  Verify that the status of the install plan is `Complete` by running the following command:

    ``` terminal
    $ oc -n external-dns-operator \
      get ip <install_plan_name> \
      --template='{{.status.phase}}{{"\n"}}'
    ```

3.  Verify that the status of the `external-dns-operator` pod is `Running` by running the following command:

    ``` terminal
    $ oc -n external-dns-operator get pod
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                     READY   STATUS    RESTARTS   AGE
    external-dns-operator-5584585fd7-5lwqm   2/2     Running   0          11m
    ```

    </div>

4.  Verify that the catalog source of the subscription is `redhat-operators` by running the following command:

    ``` terminal
    $ oc -n external-dns-operator get subscription
    ```

5.  Check the `external-dns-operator` version by running the following command:

    ``` terminal
    $ oc -n external-dns-operator get csv
    ```

</div>
