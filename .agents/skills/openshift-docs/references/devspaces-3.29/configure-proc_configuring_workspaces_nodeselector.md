> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_workspaces_nodeselector). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Control which nodes run workspaces

Control which nodes run OpenShift Dev Spaces workspace Pods by setting `nodeSelector` and tolerations for compliance, hardware affinity, or zone isolation.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- The target nodes are labeled or tainted according to the scheduling rules you want to apply.

## Procedure

1.  Set `nodeSelector` in the `CheCluster` Custom Resource to schedule workspace Pods on specific nodes:

    ``` yaml
    spec:
      devEnvironments:
        nodeSelector:
          <key>: <value>
    ```

    This section must contain a set of `key=value` pairs for each node label to form the `nodeSelector` rule.

2.  Set `tolerations` in the `CheCluster` Custom Resource to allow workspace Pods to be scheduled on tainted nodes. Tolerations work in the opposite way to `nodeSelector`. Instead of specifying which nodes the Pod is scheduled on, you specify which nodes the Pod cannot be scheduled on.

    ``` yaml
    spec:
      devEnvironments:
        tolerations:
          - effect: NoSchedule
            key: <key>
            value: <value>
            operator: Equal
    ```

    Important

    `nodeSelector` must be configured during OpenShift Dev Spaces installation. This prevents existing workspaces from failing to run due to volumes affinity conflict caused by existing workspace PVC and Pod being scheduled in different zones.

    On large, multizone clusters, Pods and PVCs can be scheduled in different zones. To avoid this, create an additional `StorageClass` object (pay attention to the `allowedTopologies` field) to coordinate the PVC creation process.

    Pass the name of this newly created `StorageClass` to OpenShift Dev Spaces through the `CheCluster` Custom Resource.

## Results

- Verify the `nodeSelector` or `tolerations` configuration in the `CheCluster` Custom Resource:

  ``` bash
  oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.spec.devEnvironments.nodeSelector}'
  ```

**Related information**  

- [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [Built-in node labels](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#built-in-node-labels)
- [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration)
- [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
- [Use a custom storage provisioner](configure-proc_configuring_storage_classes.md)
- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
