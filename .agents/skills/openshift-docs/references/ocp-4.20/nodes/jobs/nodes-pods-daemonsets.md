<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Daemon sets ensure that pods run on all or specific nodes in a cluster, enabling cluster-wide services such as logging agents, monitoring tools, and shared storage that must be present on every node.

As an administrator, you can create and use daemon sets to run replicas of a pod on specific or all nodes in an OpenShift Container Platform cluster.

A daemon set ensures that all (or some) nodes run a copy of a pod. As nodes are added to the cluster, pods are added to the cluster. As nodes are removed from the cluster, those pods are removed through garbage collection. Deleting a daemon set will clean up the pods it created.

You can use daemon sets to create shared storage, run a logging pod on every node in your cluster, or deploy a monitoring agent on every node.

For security reasons, the cluster administrators and the project administrators can create daemon sets.

For more information on daemon sets, see the [Kubernetes documentation](http://kubernetes.io/docs/admin/daemons/).

> [!IMPORTANT]
> Daemon set scheduling is incompatible with project’s default node selector. If you fail to disable it, the daemon set gets restricted by merging with the default node selector. This results in frequent pod recreates on the nodes that got unselected by the merged node selector, which in turn puts unwanted load on the cluster.

# Scheduled by default scheduler

A daemon set ensures that all eligible nodes run a copy of a pod. Normally, the node that a pod runs on is selected by the Kubernetes scheduler. However, daemon set pods are created and scheduled by the daemon set controller. That introduces the following issues:

- Inconsistent pod behavior: Normal pods waiting to be scheduled are created and in Pending state, but daemon set pods are not created in `Pending` state. This is confusing to the user.

- Pod preemption is handled by default scheduler. When preemption is enabled, the daemon set controller will make scheduling decisions without considering pod priority and preemption.

The **ScheduleDaemonSetPods** feature, enabled by default in OpenShift Container Platform, lets you schedule daemon sets using the default scheduler instead of the daemon set controller, by adding the `NodeAffinity` term to the daemon set pods, instead of the `spec.nodeName` term. The default scheduler is then used to bind the pod to the target host. If node affinity of the daemon set pod already exists, it is replaced. The daemon set controller only performs these operations when creating or modifying daemon set pods, and no changes are made to the `spec.template` of the daemon set.

``` yaml
kind: Pod
apiVersion: v1
metadata:
  name: hello-node-6fbccf8d9-9tmzr
#...
spec:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchFields:
        - key: metadata.name
          operator: In
          values:
          - target-host-name
#...
```

In addition, a `node.kubernetes.io/unschedulable:NoSchedule` toleration is added automatically to daemon set pods. The default scheduler ignores unschedulable Nodes when scheduling daemon set pods.

# Creating daemonsets

Create a daemon set to automatically deploy and maintain pod replicas across selected nodes in your cluster, using node selectors to control placement.

When creating daemon sets, the `nodeSelector` field is used to indicate the nodes on which the daemon set should deploy replicas.

<div class="important">

<div class="title">

</div>

- If you update a daemon set pod template, the existing pod replicas are not affected.

- If you delete a daemon set and then create a new daemon set with a different template but the same label selector, it recognizes any existing pod replicas as having matching labels and thus does not update them or create new replicas despite a mismatch in the pod template.

- If you change node labels, the daemon set adds pods to nodes that match the new labels and deletes pods from nodes that do not match the new labels.

To update a daemon set, force new pod replicas to be created by deleting the old replicas or nodes.

</div>

<div>

<div class="title">

Prerequisites

</div>

- Before you start using daemon sets, disable the default project-wide node selector in your namespace, by setting the namespace annotation `openshift.io/node-selector` to an empty string:

  ``` terminal
  $ oc patch namespace myproject -p \
      '{"metadata": {"annotations": {"openshift.io/node-selector": ""}}}'
  ```

  > [!TIP]
  > You can alternatively apply the following YAML to disable the default project-wide node selector for a namespace:
  >
  > ``` yaml
  > apiVersion: v1
  > kind: Namespace
  > metadata:
  >   name: <namespace>
  >   annotations:
  >     openshift.io/node-selector: ''
  > #...
  > ```

- If you are creating a new project, overwrite the default node selector:

  ``` terminal
  $ oc adm new-project <name> --node-selector=""
  ```

</div>

<div>

<div class="title">

Procedure

</div>

1.  Define the daemon set yaml file:

    ``` yaml
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: hello-daemonset
    spec:
      selector:
          matchLabels:
            name: hello-daemonset
      template:
        metadata:
          labels:
            name: hello-daemonset
        spec:
          nodeSelector:
            role: worker
          containers:
          - image: openshift/hello-openshift
            imagePullPolicy: Always
            name: registry
            ports:
            - containerPort: 80
              protocol: TCP
            resources: {}
            terminationMessagePath: /dev/termination-log
          serviceAccount: default
          terminationGracePeriodSeconds: 10
    #...
    ```

    where:

    `spec.selector.matchLabels.name`
    Specifies the label selector that determines which pods belong to the daemon set.

    `spec.template.metadata.labels.name`
    Specifies the pod template’s label selector. Must match the label selector above.

    `spec.template.spec.nodeSelector`
    Specifies the node selector that determines on which nodes pod replicas should be deployed. A matching label must be present on the node.

2.  Create the daemon set object by running the following command:

    ``` terminal
    $ oc create -f daemonset.yaml
    ```

3.  To verify that the pods were created, and that each node has a pod replica:

    1.  Find the daemonset pods by entering the following command:

        ``` terminal
        $ oc get pods
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        hello-daemonset-cx6md   1/1       Running   0          2m
        hello-daemonset-e3md9   1/1       Running   0          2m
        ```

        </div>

    2.  View the pods to verify the pod has been placed onto the node by entering the following command:

        ``` terminal
        $ oc describe pod/hello-daemonset-cx6md|grep Node
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Node:        openshift-node01.hostname.com/10.14.20.134
        ```

        </div>

        ``` terminal
        $ oc describe pod/hello-daemonset-e3md9|grep Node
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Node:        openshift-node02.hostname.com/10.14.20.137
        ```

        </div>

</div>
