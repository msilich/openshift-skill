<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To uninstall the SR-IOV Network Operator, you must delete any running SR-IOV workloads, uninstall the Operator, and delete the webhooks that the Operator used.

# Uninstalling the SR-IOV Network Operator

You can remove the SR-IOV Network Operator from your cluster by uninstalling the Operator. This ensures that the Operator and its associated resources are deleted when you no longer need to manage SR-IOV network devices.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

- You have the SR-IOV Network Operator installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Delete all SR-IOV custom resources (CRs):

    ``` terminal
    $ oc delete sriovnetwork -n openshift-sriov-network-operator --all
    ```

    ``` terminal
    $ oc delete sriovnetworknodepolicy -n openshift-sriov-network-operator --all
    ```

    ``` terminal
    $ oc delete sriovibnetwork -n openshift-sriov-network-operator --all
    ```

    ``` terminal
    $ oc delete sriovoperatorconfigs -n openshift-sriov-network-operator --all
    ```

2.  Follow the instructions in the "Deleting Operators from a cluster" section to remove the SR-IOV Network Operator from your cluster.

3.  Delete the SR-IOV custom resource definitions that remain in the cluster after the SR-IOV Network Operator is uninstalled:

    ``` terminal
    $ oc delete crd sriovibnetworks.sriovnetwork.openshift.io
    ```

    ``` terminal
    $ oc delete crd sriovnetworknodepolicies.sriovnetwork.openshift.io
    ```

    ``` terminal
    $ oc delete crd sriovnetworknodestates.sriovnetwork.openshift.io
    ```

    ``` terminal
    $ oc delete crd sriovnetworkpoolconfigs.sriovnetwork.openshift.io
    ```

    ``` terminal
    $ oc delete crd sriovnetworks.sriovnetwork.openshift.io
    ```

    ``` terminal
    $ oc delete crd sriovoperatorconfigs.sriovnetwork.openshift.io
    ```

4.  Delete the SR-IOV Network Operator namespace:

    ``` terminal
    $ oc delete namespace openshift-sriov-network-operator
    ```

</div>

# Additional resources

- [Deleting Operators from a cluster](../../../operators/admin/olm-deleting-operators-from-cluster.md#olm-deleting-operators-from-a-cluster)
