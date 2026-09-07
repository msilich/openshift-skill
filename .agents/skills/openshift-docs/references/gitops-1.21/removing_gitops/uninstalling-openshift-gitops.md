<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Uninstalling the Red Hat OpenShift GitOps Operator is a two-step process:

1.  Delete the Argo CD instances from the `openshift-gitops` namespace and any other namespaces where they were created.

2.  Uninstall the Red Hat OpenShift GitOps Operator.

Uninstalling only the Operator will not remove the Argo CD instances created.

# Deleting the Argo CD instances

Delete the Argo CD instances added to the namespace of the GitOps Operator.

<div>

<div class="title">

Procedure

</div>

1.  In the terminal, run the following command:

    ``` terminal
    $ oc delete gitopsservice cluster -n openshift-gitops
    ```

    > [!NOTE]
    > You cannot delete an Argo CD instance from the web console UI.

    After the command runs successfully, the Argo CD instances will be deleted from the `openshift-gitops` namespace.

2.  Delete any other Argo CD instances from other namespaces using the same command:

    ``` terminal
    $ oc delete gitopsservice cluster -n <namespace>
    ```

</div>

# Uninstalling the GitOps Operator

You can uninstall the Red Hat OpenShift GitOps Operator from the OperatorHub by using the web console.

<div>

<div class="title">

Procedure

</div>

1.  From the **Operators** → **OperatorHub** page, use the **Filter by keyword** box to search for `Red Hat OpenShift GitOps` tile.

2.  Click the **Red Hat OpenShift GitOps** tile. The Operator tile indicates it is installed.

3.  In the **Red Hat OpenShift GitOps** descriptor page, click **Uninstall**.

</div>

# Additional resources

- [Deleting Operators from a cluster](https://docs.openshift.com/container-platform/latest/operators/admin/olm-deleting-operators-from-cluster.html#olm-deleting-operators-from-a-cluster)
