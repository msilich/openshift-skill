<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Install the RHACS Operator on your secured clusters.

<a id="install-acs-operator-cloud_cloud-install-operator"></a>

# Installing the RHACS Operator for RHACS Cloud Service

Using the Software Catalog provided with OpenShift Container Platform is the easiest way to install the RHACS Operator.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster using an account with Operator installation permissions.

- You must be using OpenShift Container Platform 4.12 or later. For information about supported platforms and architecture, see the "Red Hat Advanced Cluster Security for Kubernetes Support Matrix".

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the web console, go to the **Ecosystem** → **Software Catalog** page.

2.  If Red Hat Advanced Cluster Security for Kubernetes is not displayed, enter **Advanced Cluster Security** into the **Filter by keyword** box to find the Red Hat Advanced Cluster Security for Kubernetes Operator. You might have to select a project first.

3.  Select the **Red Hat Advanced Cluster Security for Kubernetes Operator** to view the details page.

4.  Read the information about the Operator, and then click **Install**.

5.  On the **Install Operator** page:

    - Keep the default value for **Installation mode** as **All namespaces on the cluster**.

    - Select a specific namespace in which to install the Operator for the **Installed namespace** field. Install the Red Hat Advanced Cluster Security for Kubernetes Operator in the **rhacs-operator** namespace.

    - Select automatic or manual updates for **Update approval**.

      If you select automatic updates, when a new version of the Operator is available, Operator Lifecycle Manager (OLM) automatically upgrades the running instance of your Operator.

      If you select manual updates, when a newer version of the Operator is available, OLM creates an update request. As a cluster administrator, you must manually approve the update request to update the Operator to the latest version.

      Red Hat recommends enabling automatic upgrades for Operator in RHACS Cloud Service. See the "Red Hat Advanced Cluster Security for Kubernetes Support Matrix" for more information.

6.  Click **Install**.

</div>

<div>

<div class="title">

Verification

</div>

- After the installation completes, go to **Ecosystem** → **Installed Operators** to verify that the Red Hat Advanced Cluster Security for Kubernetes Operator shows the status of **Succeeded**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

</div>

<a id="configuring-the-rhacs-operator-for-infrastructure-nodes_cloud-install-operator"></a>

## Configuring the RHACS Operator for infrastructure nodes

To deploy the Red Hat Advanced Cluster Security for Kubernetes (RHACS) Operator on infrastructure nodes, you can change its subscription YAML to include `nodeSelector` and `tolerations` to ensure that infrastructure nodes schedule Operator pods correctly.

<div>

<div class="title">

Procedure

</div>

1.  Configure the RHACS Operator with the necessary `nodeSelector` and `tolerations` for infrastructure nodes before you apply the Operator Lifecycle Manager (OLM) subscription by using the following content, for example:

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      labels:
        operators.coreos.com/rhacs-operator.rhacs-operator: ""
      name: rhacs-operator
      namespace: rhacs-operator
    spec:
      channel: stable
      config:
        nodeSelector:
          node-role.kubernetes.io/infra: "" #
        tolerations:
          - effect: NoSchedule
            key: node-role.kubernetes.io/infra #
            operator: Exists
      installPlanApproval: Automatic
      name: rhacs-operator
      source: redhat-operators
      sourceNamespace: openshift-marketplace
    ```

    where:

    `spec.config.nodeSelector.node-role.kubernetes.io/infra`  
    Specifies the `nodeSelector` key and value to instruct the Kubernetes scheduler to place the Operator pods on nodes that have the label `node-role.kubernetes.io/infra: ""`.

    `spec.config.tolerations.key`  
    Specifies the `tolerations` entry, which allows nodes with a taint matching the `node-role.kubernetes.io/infra` key to schedule the Operator pods. This is necessary as infrastructure nodes typically have a taint to prevent them from scheduling non-infrastructure workloads.

2.  Save the YAML file and apply it by using the OpenShift CLI (`oc`).

    When you apply the YAML file, you update the subscription for the RHACS Operator. This action configures which nodes can schedule the RHACS Operator pods. The `rhacs-operator` namespace is the designated location for the RHACS Operator.

</div>

<a id="next-steps-cloud-install-operator_cloud-install-operator"></a>

# Next steps

After installing the RHACS Operator, you install secured cluster resources on each Red Hat OpenShift cluster.

On each Red Hat OpenShift cluster, install secured cluster resources in the `stackrox` project.

<div>

<div class="title">

Additional resources

</div>

- [Installing secured cluster resources](install-secured-cluster-cloud-ocp.md)

</div>
