<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In OpenShift Container Platform with OVN-Kubernetes, you can disable IP multicast on a per-project basis so pods no longer receive multicast traffic.

# Disabling multicast between pods

To disable multicast between pods in a project, you can remove the `k8s.ovn.org/multicast-enabled` annotation from the namespace by using the `oc annotate` command or a namespace manifest.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- You must log in to the cluster with a user that has the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Disable multicast by running the following command:

  ``` terminal
  $ oc annotate namespace <namespace> \
      k8s.ovn.org/multicast-enabled-
  ```

  For `<namespace>`, specify the namespace for the project you want to disable multicast for.

  > [!TIP]
  > You can alternatively apply the following YAML to delete the annotation:
  >
  > ``` yaml
  > apiVersion: v1
  > kind: Namespace
  > metadata:
  >   name: <namespace>
  >   annotations:
  >     k8s.ovn.org/multicast-enabled: null
  > ```

</div>
