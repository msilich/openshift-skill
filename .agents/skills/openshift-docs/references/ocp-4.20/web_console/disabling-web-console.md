<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can disable the OpenShift Container Platform web console.

# Prerequisites

- Deploy an OpenShift Container Platform cluster.

# Disabling the web console

You can disable the web console by editing the `consoles.operator.openshift.io` resource.

<div>

<div class="title">

Procedure

</div>

- Edit the `consoles.operator.openshift.io` resource:

  ``` terminal
  $ oc edit consoles.operator.openshift.io cluster
  ```

  The following example displays the parameters from this resource that you can modify:

  ``` yaml
  apiVersion: operator.openshift.io/v1
  kind: Console
  metadata:
    name: cluster
  spec:
    managementState: Removed
  ```

  where:

  `spec.managementState.Removed`
  Set the `managementState` parameter value to `Removed` to disable the web console. The other valid values for this parameter are `Managed`, which enables the console under the cluster’s control, and `Unmanaged`, which means that you are taking control of web console management.

</div>
