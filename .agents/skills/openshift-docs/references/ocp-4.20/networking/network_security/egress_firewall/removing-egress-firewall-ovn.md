<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As a cluster administrator, you can remove an egress firewall from a project to remove all restrictions on network traffic from the project that leaves the OpenShift Container Platform cluster.

# Removing an EgressFirewall CR

As a cluster administrator, you can remove an egress firewall from a project.

<div>

<div class="title">

Prerequisites

</div>

- A cluster using the OVN-Kubernetes network plugin.

- Install the OpenShift CLI (`oc`).

- You must log in to the cluster as a cluster administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Find the name of the `EgressFirewall` CR for the project. Replace `<project>` with the name of the project.

    ``` terminal
    $ oc get egressfirewall -n <project>
    ```

2.  Delete the `EgressFirewall` CR by entering the following command. Replace `<project>` with the name of the project and `<name>` with the name of the object.

    ``` terminal
    $ oc delete -n <project> egressfirewall <name>
    ```

</div>
