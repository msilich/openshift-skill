<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To disconnect a pod from specific network configurations in OpenShift Container Platform, you can remove the pod from a secondary network. Delete the pod to remove its connection to the secondary network.

# Removing a pod from a secondary network

To disconnect a pod from specific network configurations in OpenShift Container Platform, you can remove the pod from a secondary network. Delete the pod using the `oc delete pod` command to remove its connection to the secondary network.

<div>

<div class="title">

Prerequisites

</div>

- A secondary network is attached to the pod.

- Install the OpenShift CLI (`oc`).

- Log in to the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

- Delete the pod by entering the following command:

  ``` terminal
  $ oc delete pod <name> -n <namespace>
  ```

  where:

  `<name>`
  Specifies the name of the pod.

  `<namespace>`
  Specifies the namespace that contains the pod.

</div>
