<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When using the static CPU Manager policy, you can explicitly define a list of CPUs that are reserved for critical system processes on specific nodes. Reserving CPUs for critical system processes can help ensure cluster stability.

For example, on a system with 24 CPUs, you could reserve CPUs numbered 0 - 3 for the control plane allowing the compute nodes to use CPUs 4 - 23.

# Reserving CPUs for nodes

You can explicitly define a list of CPUs that are reserved for critical system processes on specific nodes by creating a `KubeletConfig` custom resource (CR) to define the `reservedSystemCPUs` parameter. Reserving CPUs for critical system processes can help ensure cluster stability.

This list supersedes the CPUs that might be reserved by using the `systemReserved` parameter.

For more information on the `systemReserved` parameter, see "Allocating resources for nodes in an OpenShift Container Platform cluster".

<div>

<div class="title">

Prerequisites

</div>

1.  You have the label associated with the machine config pool (MCP) for the type of node you want to configure:

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file for the `KubeletConfig` CR:

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: KubeletConfig
    metadata:
      name: set-reserved-cpus
    spec:
      kubeletConfig:
        reservedSystemCPUs: "0,1,2,3"
      machineConfigPoolSelector:
        matchLabels:
          pools.operator.machineconfiguration.openshift.io/worker: ""
    #...
    ```

    where:

    `metadata.name`
    Specifies a name for the CR.

    `spec.kubeletConfig.reservedSystemCPUs`
    Specifies the core IDs of the CPUs you want to reserve for the nodes associated with the MCP.

    `spec.machineConfigPoolSelector.matchLabels`
    Specifies the label from the MCP.

2.  Create the CR object:

    ``` terminal
    $ oc create -f <file_name>.yaml
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Setting up CPU Manager](../../scalability_and_performance/using-cpu-manager.md#setting_up_cpu_manager_using-cpu-manager-and-topology-manager)

- [Allocating resources for nodes in an OpenShift Container Platform cluster](nodes-nodes-resources-configuring.md#nodes-nodes-resources-configuring-about_nodes-nodes-resources-configuring)

</div>
