<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use a *node selector* to specify a map of key/value pairs that you define by using custom labels on nodes and selectors specified in pods. For the pod to be eligible to run on a node, the pod must have the same key/value node selector as the label on the node.

# About node selectors

You can use node selectors on pods and labels on nodes to control where the pod is scheduled. With node selectors, OpenShift Container Platform schedules the pods on nodes that contain matching labels.

You can use a node selector to place specific pods on specific nodes, cluster-wide node selectors to place new pods on specific nodes anywhere in the cluster, and project node selectors to place new pods in a project on specific nodes.

For example, as a cluster administrator, you can create an infrastructure where application developers can deploy pods only onto the nodes closest to their geographical location by including a node selector in every pod they create. In this example, the cluster consists of five data centers spread across two regions. In the U.S., label the nodes as `us-east`, `us-central`, or `us-west`. In the Asia-Pacific region (APAC), label the nodes as `apac-east` or `apac-west`. The developers can add a node selector to the pods they create to ensure the pods get scheduled on those nodes.

A pod is not scheduled if the `Pod` object contains a node selector, but no node has a matching label.

> [!IMPORTANT]
> If you are using node selectors and node affinity in the same pod configuration, the following rules control pod placement onto nodes:
>
> - If you configure both `nodeSelector` and `nodeAffinity`, both conditions must be satisfied for the pod to be scheduled onto a candidate node.
>
> - If you specify multiple `nodeSelectorTerms` associated with `nodeAffinity` types, then the pod can be scheduled onto a node if one of the `nodeSelectorTerms` is satisfied.
>
> - If you specify multiple `matchExpressions` associated with `nodeSelectorTerms`, then the pod can be scheduled onto a node only if all `matchExpressions` are satisfied.

Node selectors on specific pods and nodes
You can control which node a specific pod is scheduled on by using node selectors and labels.

To use node selectors and labels, first label the node to avoid pods being descheduled, then add the node selector to the pod.

> [!NOTE]
> You cannot add a node selector directly to an existing scheduled pod. You must label the object that controls the pod, such as deployment config.

For example, the following `Node` object has the `region: east` label:

<div class="formalpara">

<div class="title">

Sample `Node` object with a label

</div>

``` yaml
kind: Node
apiVersion: v1
metadata:
  name: ip-10-0-131-14.ec2.internal
  selfLink: /api/v1/nodes/ip-10-0-131-14.ec2.internal
  uid: 7bc2580a-8b8e-11e9-8e01-021ab4174c74
  resourceVersion: '478704'
  creationTimestamp: '2019-06-10T14:46:08Z'
  labels:
    kubernetes.io/os: linux
    topology.kubernetes.io/zone: us-east-1a
    node.openshift.io/os_version: '4.5'
    node-role.kubernetes.io/worker: ''
    topology.kubernetes.io/region: us-east-1
    node.openshift.io/os_id: rhcos
    node.kubernetes.io/instance-type: m4.large
    kubernetes.io/hostname: ip-10-0-131-14
    kubernetes.io/arch: amd64
    region: east
    type: user-node
#...
```

</div>

In this example, the `region: east` and `type: user-node` labels must match the pod node selector.

A pod has the `type: user-node,region: east` node selector:

<div class="formalpara">

<div class="title">

Sample `Pod` object with node selectors

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: s1
#...
spec:
  nodeSelector:
    region: east
    type: user-node
#...
```

</div>

where:

`spec.nodeSelector`
Specifies the node selectors to match the node label. The node must have a label for each node selector.

When you create the pod using the example pod spec, it can be scheduled on the example node.

Default cluster-wide node selectors
With default cluster-wide node selectors, when you create a pod in that cluster, OpenShift Container Platform adds the default node selectors to the pod and schedules the pod on nodes with matching labels.

For example, the following `Scheduler` object has the default cluster-wide `region=east` and `type=user-node` node selectors:

<div class="formalpara">

<div class="title">

Example Scheduler Operator Custom Resource

</div>

``` yaml
apiVersion: config.openshift.io/v1
kind: Scheduler
metadata:
  name: cluster
#...
spec:
  defaultNodeSelector: type=user-node,region=east
#...
```

</div>

A node in that cluster has the `type=user-node,region=east` labels:

<div class="formalpara">

<div class="title">

Example `Node` object

</div>

``` yaml
apiVersion: v1
kind: Node
metadata:
  name: ci-ln-qg1il3k-f76d1-hlmhl-worker-b-df2s4
#...
  labels:
    region: east
    type: user-node
#...
```

</div>

<div class="formalpara">

<div class="title">

Example `Pod` object with a node selector

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: s1
#...
spec:
  nodeSelector:
    region: east
#...
```

</div>

When you create the pod using the example pod spec in the example cluster, the pod is created with the cluster-wide node selector and is scheduled on the labeled node:

<div class="formalpara">

<div class="title">

Example pod list with the pod on the labeled node

</div>

``` terminal
NAME     READY   STATUS    RESTARTS   AGE   IP           NODE                                       NOMINATED NODE   READINESS GATES
pod-s1   1/1     Running   0          20s   10.131.2.6   ci-ln-qg1il3k-f76d1-hlmhl-worker-b-df2s4   <none>           <none>
```

</div>

> [!NOTE]
> If the project where you create the pod has a project node selector, that selector takes preference over a cluster-wide node selector. Your pod is not created or scheduled if the pod does not have the project node selector.

<!-- -->

Project node selectors
With project node selectors, when you create a pod in this project, OpenShift Container Platform adds the node selectors to the pod and schedules the pods on a node with matching labels. If there is a cluster-wide default node selector, a project node selector takes preference.

For example, the following project has the `region=east` node selector:

<div class="formalpara">

<div class="title">

Example `Namespace` object

</div>

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  name: east-region
  annotations:
    openshift.io/node-selector: "region=east"
#...
```

</div>

The following node has the `type=user-node,region=east` labels:

<div class="formalpara">

<div class="title">

Example `Node` object

</div>

``` yaml
apiVersion: v1
kind: Node
metadata:
  name: ci-ln-qg1il3k-f76d1-hlmhl-worker-b-df2s4
#...
  labels:
    region: east
    type: user-node
#...
```

</div>

When you create the pod using the example pod spec in this example project, the pod is created with the project node selectors and is scheduled on the labeled node:

<div class="formalpara">

<div class="title">

Example `Pod` object

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  namespace: east-region
#...
spec:
  nodeSelector:
    region: east
    type: user-node
#...
```

</div>

<div class="formalpara">

<div class="title">

Example pod list with the pod on the labeled node

</div>

``` terminal
NAME     READY   STATUS    RESTARTS   AGE   IP           NODE                                       NOMINATED NODE   READINESS GATES
pod-s1   1/1     Running   0          20s   10.131.2.6   ci-ln-qg1il3k-f76d1-hlmhl-worker-b-df2s4   <none>           <none>
```

</div>

A pod in the project is not created or scheduled if the pod contains different node selectors. For example, if you deploy the following pod into the example project, it is not created:

<div class="formalpara">

<div class="title">

Example `Pod` object with an invalid node selector

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: west-region
#...
spec:
  nodeSelector:
    region: west
#...
```

</div>

# Using node selectors to control pod placement

You can use node selectors on pods and labels on nodes to control where the pod is scheduled. With node selectors, OpenShift Container Platform schedules the pods on nodes that contain matching labels.

You add labels to a node, a compute machine set, or a machine config. Adding the label to the compute machine set ensures that if the node or machine goes down, new nodes have the label. Labels added to a node or machine config do not persist if the node or machine goes down.

To add node selectors to an existing pod, add a node selector to the controlling object for that pod, such as a `ReplicaSet` object, `DaemonSet` object, `StatefulSet` object, `Deployment` object, or `DeploymentConfig` object. Any existing pods under that controlling object are recreated on a node with a matching label. If you are creating a new pod, you can add the node selector directly to the pod spec. If the pod does not have a controlling object, you must delete the pod, edit the pod spec, and recreate the pod.

> [!NOTE]
> You cannot add a node selector directly to an existing scheduled pod.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

To add a node selector to existing pods, determine the controlling object for that pod. For example, the `router-default-66d5cf9464-m2g75` pod is controlled by the `router-default-66d5cf9464` replica set:

</div>

``` terminal
$ oc describe pod router-default-66d5cf9464-7pwkc
```

The output appears similar to the following example:

``` terminal
kind: Pod
apiVersion: v1
metadata:
# ...
Name:               router-default-66d5cf9464-7pwkc
Namespace:          openshift-ingress
# ...
Controlled By:      ReplicaSet/router-default-66d5cf9464
# ...
```

The web console lists the controlling object under `ownerReferences` in the pod YAML:

``` terminal
apiVersion: v1
kind: Pod
metadata:
  name: router-default-66d5cf9464-7pwkc
# ...
  ownerReferences:
    - apiVersion: apps/v1
      kind: ReplicaSet
      name: router-default-66d5cf9464
      uid: d81dd094-da26-11e9-a48a-128e7edf0312
      controller: true
      blockOwnerDeletion: true
# ...
```

<div>

<div class="title">

Procedure

</div>

1.  Add labels to a node by using a compute machine set or editing the node directly:

    - Use a `MachineSet` object to add labels to nodes managed by the compute machine set when a node is created:

      1.  Run the following command to add labels to a `MachineSet` object:

          ``` terminal
          $ oc patch MachineSet <name> --type='json' -p='[{"op":"add","path":"/spec/template/spec/metadata/labels", "value":{"<key>"="<value>","<key>"="<value>"}}]'  -n openshift-machine-api
          ```

          For example:

          ``` terminal
          $ oc patch MachineSet abc612-msrtw-worker-us-east-1c  --type='json' -p='[{"op":"add","path":"/spec/template/spec/metadata/labels", "value":{"type":"user-node","region":"east"}}]'  -n openshift-machine-api
          ```

          > [!TIP]
          > You can alternatively apply the following YAML to add labels to a compute machine set:
          >
          > ``` yaml
          > apiVersion: machine.openshift.io/v1beta1
          > kind: MachineSet
          > metadata:
          >   name: xf2bd-infra-us-east-2a
          >   namespace: openshift-machine-api
          > spec:
          >   template:
          >     spec:
          >       metadata:
          >         labels:
          >           region: "east"
          >           type: "user-node"
          > # ...
          > ```

      2.  Verify that the labels are added to the `MachineSet` object by using the `oc edit` command:

          For example:

          ``` terminal
          $ oc edit MachineSet abc612-msrtw-worker-us-east-1c -n openshift-machine-api
          ```

          The output appears similar to the following example:

          ``` yaml
          apiVersion: machine.openshift.io/v1beta1
          kind: MachineSet

          # ...

          spec:
          # ...
            template:
              metadata:
          # ...
              spec:
                metadata:
                  labels:
                    region: east
                    type: user-node
          # ...
          ```

    - Add labels directly to a node:

      1.  Edit the `Node` object for the node:

          ``` terminal
          $ oc label nodes <name> <key>=<value>
          ```

          For example, to label a node:

          ``` terminal
          $ oc label nodes ip-10-0-142-25.ec2.internal type=user-node region=east
          ```

          > [!TIP]
          > You can alternatively apply the following YAML to add labels to a node:
          >
          > ``` yaml
          > kind: Node
          > apiVersion: v1
          > metadata:
          >   name: hello-node-6fbccf8d9
          >   labels:
          >     type: "user-node"
          >     region: "east"
          > # ...
          > ```

      2.  Verify that the labels are added to the node:

          ``` terminal
          $ oc get nodes -l type=user-node,region=east
          ```

          <div class="formalpara">

          <div class="title">

          Example output

          </div>

          ``` terminal
          NAME                          STATUS   ROLES    AGE   VERSION
          ip-10-0-142-25.ec2.internal   Ready    worker   17m   v1.33.4
          ```

          </div>

2.  Add the matching node selector to a pod:

    - To add a node selector to existing and future pods, add a node selector to the controlling object for the pods:

      <div class="formalpara">

      <div class="title">

      Example `ReplicaSet` object with labels

      </div>

      ``` yaml
      kind: ReplicaSet
      apiVersion: apps/v1
      metadata:
        name: hello-node-6fbccf8d9
      # ...
      spec:
      # ...
        template:
          metadata:
            creationTimestamp: null
            labels:
              ingresscontroller.operator.openshift.io/deployment-ingresscontroller: default
              pod-template-hash: 66d5cf9464
          spec:
            nodeSelector:
              kubernetes.io/os: linux
              node-role.kubernetes.io/worker: ''
              type: user-node
      # ...
      ```

      </div>

      where:

      `spec.template.spec.nodeSelector`
      Specifies the node selectors .

    - To add a node selector to a specific, new pod, add the selector to the `Pod` object directly:

      <div class="formalpara">

      <div class="title">

      Example `Pod` object with a node selector

      </div>

      ``` yaml
      apiVersion: v1
      kind: Pod
      metadata:
        name: hello-node-6fbccf8d9
      # ...
      spec:
        nodeSelector:
          region: east
          type: user-node
      # ...
      ```

      </div>

      > [!NOTE]
      > You cannot add a node selector directly to an existing scheduled pod.

</div>

# Creating default cluster-wide node selectors

You can use default cluster-wide node selectors on pods together with labels on nodes to constrain all pods created in a cluster to specific nodes.

With cluster-wide node selectors, when you create a pod in that cluster, OpenShift Container Platform adds the default node selectors to the pod and schedules the pod on nodes with matching labels.

You configure cluster-wide node selectors by editing the Scheduler Operator custom resource (CR). You add labels to a node, a compute machine set, or a machine config. Adding the label to the compute machine set ensures that if the node or machine goes down, new nodes have the label. Labels added to a node or machine config do not persist if the node or machine goes down.

> [!NOTE]
> You can add additional key/value pairs to a pod. But you cannot add a different value for a default key.

The following procedure adds a default cluster-wide node selector.

<div>

<div class="title">

Procedure

</div>

1.  Edit the Scheduler Operator CR to add the default cluster-wide node selectors:

    ``` terminal
    $ oc edit scheduler cluster
    ```

    <div class="formalpara">

    <div class="title">

    Example Scheduler Operator CR with a node selector

    </div>

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Scheduler
    metadata:
      name: cluster
    ...
    spec:
      defaultNodeSelector: type=user-node,region=east
      mastersSchedulable: false
    ```

    </div>

    where:

    `spec.defaultNodeSelector`
    Specifies a node selector with the appropriate `<key>:<value>` pairs.

    After making this change, wait for the pods in the `openshift-kube-apiserver` project to redeploy. This can take several minutes. The default cluster-wide node selector does not take effect until the pods redeploy.

2.  Add labels to a node by using a compute machine set or editing the node directly:

    - Use a compute machine set to add labels to nodes managed by the compute machine set when a node is created:

      1.  Run the following command to add labels to a `MachineSet` object:

          ``` terminal
          $ oc patch MachineSet <name> --type='json' -p='[{"op":"add","path":"/spec/template/spec/metadata/labels", "value":{"<key>"="<value>","<key>"="<value>"}}]'  -n openshift-machine-api
          ```

          Add a `<key>/<value>` pair for each label.

          For example:

          ``` terminal
          $ oc patch MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c --type='json' -p='[{"op":"add","path":"/spec/template/spec/metadata/labels", "value":{"type":"user-node","region":"east"}}]'  -n openshift-machine-api
          ```

          > [!TIP]
          > You can alternatively apply the following YAML to add labels to a compute machine set:
          >
          > ``` yaml
          > apiVersion: machine.openshift.io/v1beta1
          > kind: MachineSet
          > metadata:
          >   name: <machineset>
          >   namespace: openshift-machine-api
          > spec:
          >   template:
          >     spec:
          >       metadata:
          >         labels:
          >           region: "east"
          >           type: "user-node"
          > ```

      2.  Verify that the labels are added to the `MachineSet` object by using the `oc edit` command:

          For example:

          ``` terminal
          $ oc edit MachineSet abc612-msrtw-worker-us-east-1c -n openshift-machine-api
          ```

          <div class="formalpara">

          <div class="title">

          Example `MachineSet` object

          </div>

          ``` yaml
          apiVersion: machine.openshift.io/v1beta1
          kind: MachineSet
            ...
          spec:
            ...
            template:
              metadata:
            ...
              spec:
                metadata:
                  labels:
                    region: east
                    type: user-node
            ...
          ```

          </div>

      3.  Redeploy the nodes associated with that compute machine set by scaling down to `0` and scaling up the nodes:

          For example:

          ``` terminal
          $ oc scale --replicas=0 MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c -n openshift-machine-api
          ```

          ``` terminal
          $ oc scale --replicas=1 MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c -n openshift-machine-api
          ```

      4.  When the nodes are ready and available, verify that the label is added to the nodes by using the `oc get` command:

          ``` terminal
          $ oc get nodes -l <key>=<value>
          ```

          For example:

          ``` terminal
          $ oc get nodes -l type=user-node
          ```

          <div class="formalpara">

          <div class="title">

          Example output

          </div>

          ``` terminal
          NAME                                       STATUS   ROLES    AGE   VERSION
          ci-ln-l8nry52-f76d1-hl7m7-worker-c-vmqzp   Ready    worker   61s   v1.33.4
          ```

          </div>

    - Add labels directly to a node:

      1.  Edit the `Node` object for the node:

          ``` terminal
          $ oc label nodes <name> <key>=<value>
          ```

          For example, to label a node:

          ``` terminal
          $ oc label nodes ci-ln-l8nry52-f76d1-hl7m7-worker-b-tgq49 type=user-node region=east
          ```

          > [!TIP]
          > You can alternatively apply the following YAML to add labels to a node:
          >
          > ``` yaml
          > kind: Node
          > apiVersion: v1
          > metadata:
          >   name: <node_name>
          >   labels:
          >     type: "user-node"
          >     region: "east"
          > ```

      2.  Verify that the labels are added to the node using the `oc get` command:

          ``` terminal
          $ oc get nodes -l <key>=<value>,<key>=<value>
          ```

          For example:

          ``` terminal
          $ oc get nodes -l type=user-node,region=east
          ```

          <div class="formalpara">

          <div class="title">

          Example output

          </div>

          ``` terminal
          NAME                                       STATUS   ROLES    AGE   VERSION
          ci-ln-l8nry52-f76d1-hl7m7-worker-b-tgq49   Ready    worker   17m   v1.33.4
          ```

          </div>

</div>

# Creating project-wide node selectors

You can use node selectors in a project together with labels on nodes to constrain all pods created in that project to the labeled nodes.

When you create a pod in this project, OpenShift Container Platform adds the node selectors to the pods in the project and schedules the pods on a node with matching labels in the project. If there is a cluster-wide default node selector, a project node selector takes preference.

You add node selectors to a project by editing the `Namespace` object to add the `openshift.io/node-selector` parameter. You add labels to a node, a compute machine set, or a machine config. Adding the label to the compute machine set ensures that if the node or machine goes down, new nodes have the label. Labels added to a node or machine config do not persist if the node or machine goes down.

A pod is not scheduled if the `Pod` object contains a node selector, but no project has a matching node selector. When you create a pod from that spec, you receive an error similar to the following message:

``` terminal
Error from server (Forbidden): error when creating "pod.yaml": pods "pod-4" is forbidden: pod node label selector conflicts with its project node label selector
```

> [!NOTE]
> You can add additional key/value pairs to a pod. But you cannot add a different value for a project key.

The following procedure adds a default project node selector.

<div>

<div class="title">

Procedure

</div>

1.  Create a namespace or edit an existing namespace to add the `openshift.io/node-selector` parameter:

    ``` terminal
    $ oc edit namespace <name>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      annotations:
        openshift.io/node-selector: "type=user-node,region=east"
        openshift.io/description: ""
        openshift.io/display-name: ""
        openshift.io/requester: kube:admin
        openshift.io/sa.scc.mcs: s0:c30,c5
        openshift.io/sa.scc.supplemental-groups: 1000880000/10000
        openshift.io/sa.scc.uid-range: 1000880000/10000
      creationTimestamp: "2021-05-10T12:35:04Z"
      labels:
        kubernetes.io/metadata.name: demo
      name: demo
      resourceVersion: "145537"
      uid: 3f8786e3-1fcb-42e3-a0e3-e2ac54d15001
    spec:
      finalizers:
      - kubernetes
    ```

    </div>

    Add the `openshift.io/node-selector` annotation with the appropriate `<key>:<value>` pairs.

2.  Add labels to a node by using a compute machine set or editing the node directly:

    - Use a `MachineSet` object to add labels to nodes managed by the compute machine set when a node is created:

      1.  Run the following command to add labels to a `MachineSet` object:

          ``` terminal
          $ oc patch MachineSet <name> --type='json' -p='[{"op":"add","path":"/spec/template/spec/metadata/labels", "value":{"<key>"="<value>","<key>"="<value>"}}]'  -n openshift-machine-api
          ```

          For example:

          ``` terminal
          $ oc patch MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c --type='json' -p='[{"op":"add","path":"/spec/template/spec/metadata/labels", "value":{"type":"user-node","region":"east"}}]'  -n openshift-machine-api
          ```

          > [!TIP]
          > You can alternatively apply the following YAML to add labels to a compute machine set:
          >
          > ``` yaml
          > apiVersion: machine.openshift.io/v1beta1
          > kind: MachineSet
          > metadata:
          >   name: <machineset>
          >   namespace: openshift-machine-api
          > spec:
          >   template:
          >     spec:
          >       metadata:
          >         labels:
          >           region: "east"
          >           type: "user-node"
          > ```

      2.  Verify that the labels are added to the `MachineSet` object by using the `oc edit` command:

          For example:

          ``` terminal
          $ oc edit MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c -n openshift-machine-api
          ```

          <div class="formalpara">

          <div class="title">

          Example output

          </div>

          ``` yaml
          apiVersion: machine.openshift.io/v1beta1
          kind: MachineSet
          metadata:
          ...
          spec:
          ...
            template:
              metadata:
          ...
              spec:
                metadata:
                  labels:
                    region: east
                    type: user-node
          ```

          </div>

      3.  Redeploy the nodes associated with that compute machine set:

          For example:

          ``` terminal
          $ oc scale --replicas=0 MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c -n openshift-machine-api
          ```

          ``` terminal
          $ oc scale --replicas=1 MachineSet ci-ln-l8nry52-f76d1-hl7m7-worker-c -n openshift-machine-api
          ```

      4.  When the nodes are ready and available, verify that the label is added to the nodes by using the `oc get` command:

          ``` terminal
          $ oc get nodes -l <key>=<value>
          ```

          For example:

          ``` terminal
          $ oc get nodes -l type=user-node,region=east
          ```

          <div class="formalpara">

          <div class="title">

          Example output

          </div>

          ``` terminal
          NAME                                       STATUS   ROLES    AGE   VERSION
          ci-ln-l8nry52-f76d1-hl7m7-worker-c-vmqzp   Ready    worker   61s   v1.33.4
          ```

          </div>

    - Add labels directly to a node:

      1.  Edit the `Node` object to add labels:

          ``` terminal
          $ oc label <resource> <name> <key>=<value>
          ```

          For example, to label a node:

          ``` terminal
          $ oc label nodes ci-ln-l8nry52-f76d1-hl7m7-worker-c-tgq49 type=user-node region=east
          ```

          > [!TIP]
          > You can alternatively apply the following YAML to add labels to a node:
          >
          > ``` yaml
          > kind: Node
          > apiVersion: v1
          > metadata:
          >   name: <node_name>
          >   labels:
          >     type: "user-node"
          >     region: "east"
          > ```

      2.  Verify that the labels are added to the `Node` object using the `oc get` command:

          ``` terminal
          $ oc get nodes -l <key>=<value>
          ```

          For example:

          ``` terminal
          $ oc get nodes -l type=user-node,region=east
          ```

          <div class="formalpara">

          <div class="title">

          Example output

          </div>

          ``` terminal
          NAME                                       STATUS   ROLES    AGE   VERSION
          ci-ln-l8nry52-f76d1-hl7m7-worker-b-tgq49   Ready    worker   17m   v1.33.4
          ```

          </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a project with a node selector and toleration](nodes-scheduler-taints-tolerations.md#nodes-scheduler-taints-tolerations-projects_nodes-scheduler-taints-tolerations)

</div>
