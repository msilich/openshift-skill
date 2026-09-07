<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use `skip-node` annotation to prevent the `node-labeller` from reconciling a node.

# Using skip-node annotation

If you want the `node-labeller` to skip a node, annotate that node by using the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Annotate the node that you want to skip by running the following command:

  ``` terminal
  $ oc annotate node <node_name> node-labeller.kubevirt.io/skip-node=true
  ```

  Replace `<node_name>` with the name of the relevant node to skip.

  Reconciliation resumes on the next cycle after the node annotation is removed or set to false.

</div>

# Additional resources

- [Managing node labeling for obsolete CPU models](virt-managing-node-labeling-obsolete-cpu-models.md#virt-managing-node-labeling-obsolete-cpu-models)
