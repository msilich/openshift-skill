<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As a cluster administrator, you can delete a network policy from a namespace.

# Deleting a network policy using the CLI

You can delete a network policy in a namespace.

> [!NOTE]
> If you log in with `cluster-admin` privileges, you can delete network policies in any namespace in the cluster.

> [!NOTE]
> If you log in with `cluster-admin` privileges, you can delete network policies in any namespace in the cluster. In the web console, you can delete policies directly in YAML or by using the **Actions** menu.

<div>

<div class="title">

Prerequisites

</div>

- Your cluster uses a network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes network plugin, with `mode: NetworkPolicy` set.

- You installed the OpenShift CLI (`oc`).

- You logged in to the cluster with a user with `admin` privileges.

- You are working in the namespace where the network policy exists.

</div>

<div>

<div class="title">

Procedure

</div>

- To delete a network policy object, enter the following command. Successful output lists the name of the policy object and the `deleted` status.

  ``` terminal
  $ oc delete networkpolicy <policy_name> -n <namespace>
  ```

  where:

  `<policy_name>`
  Specifies the name of the network policy.

  `<namespace>`
  Optional parameter. If you defined the object in a different namespace than the current namespace, the parameter specifices the namespace.

</div>
