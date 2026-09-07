<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use infrastructure nodes to isolate infrastructure workloads for two primary purposes:

- To prevent billing costs associated with the number of subscriptions

- To separate maintenance and management

With GitOps control plane workloads, you can securely and declaratively isolate the infrastructure workloads by creating multiple isolated Argo CD instances in a cluster, with full control over what an Argo CD instance is capable of. In addition, you can manage these Argo CD instances declaratively across multiple developer namespaces. By using taints, you can ensure that only infrastructure components run on these nodes.

# Moving GitOps control plane workloads to infrastructure nodes

You can move the GitOps control plane workloads installed by the Red Hat OpenShift GitOps to the infrastructure nodes. The following are the control plane workloads that you can move:

- `cluster deployment` (backend service)

- `openshift-gitops-applicationset-controller deployment`

- `openshift-gitops-dex-server deployment`

- `openshift-gitops-redis deployment`

- `openshift-gitops-redis-ha-haproxy deployment`

- `openshift-gitops-repo-server deployment`

- `openshift-gitops-server deployment`

- `openshift-gitops-application-controller statefulset`

- `openshift-gitops-redis-server statefulset`

<div>

<div class="title">

Procedure

</div>

1.  Label existing nodes as infrastructure by running the following command:

    ``` terminal
    $ oc label node <node-name> node-role.kubernetes.io/infra=
    ```

2.  Edit the `GitOpsService` custom resource (CR) to add the infrastructure node selector:

    ``` terminal
    $ oc edit gitopsservice -n openshift-gitops
    ```

3.  In the `GitOpsService` CR file, add `runOnInfra` field to the `spec` section and set it to `true`. This field moves the control plane workloads in `openshift-gitops` namespace to the infrastructure nodes:

    ``` yaml
    apiVersion: pipelines.openshift.io/v1alpha1
    kind: GitopsService
    metadata:
      name: cluster
    spec:
      runOnInfra: true
    ```

4.  Optional: Apply taints and isolate the workloads on infrastructure nodes and prevent other workloads from scheduling on these nodes.

    ``` terminal
    $ oc adm taint nodes -l node-role.kubernetes.io/infra
    infra=reserved:NoSchedule infra=reserved:NoExecute
    ```

5.  Optional: If you apply taints to the nodes, you can add tolerations in the `GitOpsService` CR:

    ``` yaml
    spec:
      runOnInfra: true
      tolerations:
      - effect: NoSchedule
        key: infra
        value: reserved
      - effect: NoExecute
        key: infra
        value: reserved
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the workloads are scheduled on infrastructure nodes in the Red Hat OpenShift GitOps namespace, click any of the pod names and ensure that the **Node selector** and **Tolerations** have been added.

  > [!NOTE]
  > Any manually added **Node selectors** and **Tolerations** in the default Argo CD CR will be overwritten by the toggle and the tolerations in the `GitOpsService` CR.

</div>

# Moving the GitOps Operator pod to infrastructure nodes

You can move the GitOps Operator pod to the infrastructure nodes.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have access to the cluster with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Label an existing node as infrastructure node by running the following command:

    ``` terminal
    $ oc label node <node_name> node-role.kubernetes.io/infra=
    ```

    where:

    `<node_name>`
    Specifies the name of the node you want to label as infrastructure node.

    **Example output:**

    ``` terminal
    node/<node_name> labeled
    ```

2.  Edit the Red Hat OpenShift GitOps `Subscription` resource by running the following command:

    ``` terminal
    $ oc -n openshift-gitops-operator edit subscription openshift-gitops-operator
    ```

3.  Add `nodeSelector` and `tolerations` to the `spec.config` field in the `Subscription` resource:

    **Example Subscription:**

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: openshift-gitops-operator
      namespace: openshift-gitops-operator
    spec:
      config:
        nodeSelector:
          node-role.kubernetes.io/infra: ""
        tolerations:
        - key: node-role.kubernetes.io/infra
          operator: Exists
          effect: NoSchedule
    ```

    where:

    `<metadata.name>`
    Specifies that the operator pod should only be scheduled on nodes with the `node-role.kubernetes.io/infra` label.

    `<metadata.namespace>`
    Allows the operator pod to tolerate taints on infrastructure nodes so it can run there.

    **Example output:**

    ``` terminal
    subscription.operators.coreos.com/openshift-gitops-operator edited
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the GitOps Operator pod is running on the infrastructure node by running the following command:

  ``` terminal
  $ oc -n openshift-gitops-operator get po -owide
  ```

  **Example output:**

  ``` terminal
  NAME                                                            READY   STATUS    RESTARTS   AGE   IP              NODE            NOMINATED NODE   READINESS GATES
  openshift-gitops-operator-controller-manager-abcd               2/2     Running   0          11m   94.142.44.126   <node_name>     <none>           <none>
  ```

  Ensure that the listed `<node_name>` is the node with the `node-role.kubernetes.io/infra` label.

</div>

# Additional resources

- [Controlling pod placement using node taints](https://docs.openshift.com/container-platform/latest/nodes/scheduling/nodes-scheduler-taints-tolerations.html#nodes-scheduler-taints-tolerations)

- [Creating infrastructure machine sets](https://docs.openshift.com/container-platform/latest/machine_management/creating-infrastructure-machinesets.html#creating-infrastructure-machinesets)
