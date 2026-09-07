<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can remove a Windows node by deleting its host Windows machine.

# Deleting a specific machine

To remove a machine from your cluster, or restart a machine that is part of a machine set, you can use the OpenShift CLI (`oc`) to delete a specific machine.

> [!IMPORTANT]
> Do not delete a control plane machine unless your cluster uses a control plane machine set. If the machine that you delete belongs to a machine set, a new machine is immediately created to satisfy the specified number of replicas.

<div>

<div class="title">

Prerequisites

</div>

- Install an OpenShift Container Platform cluster.

- Install the OpenShift CLI (`oc`).

- Log in to `oc` as a user with `cluster-admin` permission.

</div>

<div>

<div class="title">

Procedure

</div>

1.  View the machines that are in the cluster by running the following command:

    ``` terminal
    $ oc get machine -n openshift-machine-api
    ```

    The command output contains a list of machines in the `<clusterid>-<role>-<cloud_region>` format.

2.  Identify the machine that you want to delete.

3.  Delete the machine by running the following command:

    ``` terminal
    $ oc delete machine <machine> -n openshift-machine-api
    ```

    Replace `<machine>` with the name of the machine.

    > [!IMPORTANT]
    > By default, the machine controller tries to drain the node that is backed by the machine until it succeeds. In some situations, such as with a misconfigured pod disruption budget, the drain operation might not be able to succeed. If the drain operation fails, the machine controller cannot proceed removing the machine.
    >
    > You can skip draining the node by annotating `machine.openshift.io/exclude-node-draining` in a specific machine.

</div>
