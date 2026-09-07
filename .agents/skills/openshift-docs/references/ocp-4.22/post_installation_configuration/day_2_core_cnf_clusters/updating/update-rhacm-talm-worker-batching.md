<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure worker node batching to control how many worker nodes update simultaneously and how workloads tolerate disruption during cluster updates by using `MachineConfigPool` and `PodDisruptionBudget` resources.

# Configuring worker node batching by using machine config pools

You can configure the `MachineConfigPool` resource to control how many worker nodes update simultaneously during a cluster update. Adjusting the `maxUnavailable` setting balances update speed against workload availability.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the target cluster with cluster-admin privileges.

- The `oc` CLI tool is installed and configured.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check the current `maxUnavailable` setting for the worker `MachineConfigPool` resource by running the following command:

    ``` terminal
    $ oc get mcp worker -o jsonpath='{.spec.maxUnavailable}'
    ```

2.  Set the required `maxUnavailable` value in the worker `MachineConfigPool` resource by running the following command:

    ``` terminal
    $ oc patch mcp worker --type merge -p '{"spec":{"maxUnavailable":"<max_unavailable>"}}'
    ```

    where `<max_unavailable>` is one of the following values:

    - An integer, for example `1`, to specify the exact number of nodes that can be unavailable during the update.

    - A percentage, for example `"50%"`, to specify the proportion of nodes that can be unavailable.

    > [!NOTE]
    > The default `maxUnavailable` value is 1 worker node or 33% of worker nodes, whichever is smaller. Setting a higher value accelerates updates but increases the number of nodes unavailable at any given time. Consult your application teams to find the appropriate value for your workloads.

3.  Verify the updated setting by running the following command:

    ``` terminal
    $ oc get mcp worker -o yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `MachineConfigPool` resource reflects the updated `maxUnavailable` value by running the following command:

  ``` terminal
  $ oc get mcp worker -o jsonpath='{.spec.maxUnavailable}'
  ```

</div>

# Configuring worker node batching by using pod disruption budgets

You can configure `PodDisruptionBudget` resources to control how your workloads tolerate node draining during cluster updates. Pod disruption budgets ensure that a minimum number of pod replicas remain available during worker node updates.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the target cluster with cluster-admin privileges.

- The `oc` CLI tool is installed and configured.

- You have identified critical workloads that run with replicas.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `PodDisruptionBudget` resource for each critical workload:

    ``` yaml
    apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: <pdb_name>
      namespace: <namespace>
    spec:
      maxUnavailable: 1
      selector:
        matchLabels:
          app: <app_label>
    ```

    where:

    - `<pdb_name>`: Specifies a name for the `PodDisruptionBudget` resource, for example `cnf-workload-pdb`.

    - `<namespace>`: Specifies the namespace where the workload runs, for example `cnf-workload`.

    - `maxUnavailable`: Specifies the maximum number of pods that can be unavailable during a disruption. Set this value to at least `1` to allow node draining to proceed.

    - `<app_label>`: Specifies the label selector that matches the pods for this workload.

2.  Apply the `PodDisruptionBudget` resource by running the following command:

    ``` terminal
    $ oc apply -f <pdb_filename>.yaml
    ```

3.  Verify that the pod disruption budget allows at least one disruption by running the following command:

    ``` terminal
    $ oc get pdb <pdb_name> -n <namespace>
    ```

    The following example shows the output:

    ``` terminal
    NAME               MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
    cnf-workload-pdb   N/A             1                 1                     30s
    ```

    > [!IMPORTANT]
    > Ensure the `ALLOWED DISRUPTIONS` column shows a value greater than 0. If this value is 0, the pod disruption budget blocks node draining and updates stall. Do not set `minAvailable` to 100% of replicas, as this prevents any disruption.

4.  Repeat steps 1-3 for all critical workloads in your cluster.

5.  Verify all pod disruption budgets across the cluster by running the following command:

    ``` terminal
    $ oc get pdb -A
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that no pod disruption budgets are blocking disruptions by running the following command:

  ``` terminal
  $ oc get pdb -A -o jsonpath='{range .items[?(@.status.disruptionsAllowed==0)]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
  ```

  This command must produce no output. If the output lists any pod disruption budgets, adjust their configuration before updating.

</div>

# Additional resources

- [Configuring application pods before updating your OpenShift Container Platform cluster](update-cnf-update-prep.md#update-cnf-update-prep)

- [Kubernetes PodDisruptionBudget documentation](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)

- [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)
