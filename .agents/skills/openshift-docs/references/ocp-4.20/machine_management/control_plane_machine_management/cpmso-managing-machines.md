<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Control plane machine sets automate several essential aspects of control plane management to reduce operational overhead and ensure consistency.

# Updating the control plane configuration

Update the control plane machine set specification to modify control plane machine configuration and trigger automatic or manual replacements.

The Control Plane Machine Set Operator monitors the control plane machines and compares their configuration with the specification in the control plane machine set CR. When there is a discrepancy between the specification in the CR and the configuration of a control plane machine, the Operator marks that control plane machine for replacement.

> [!NOTE]
> For more information about the parameters in the CR, see "Control plane machine set configuration".

<div>

<div class="title">

Prerequisites

</div>

- Your cluster has an activated and functioning Control Plane Machine Set Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit your control plane machine set CR by running the following command:

    ``` terminal
    $ oc edit controlplanemachineset.machine.openshift.io cluster \
      -n openshift-machine-api
    ```

2.  Change the values of any fields that you want to update in your cluster configuration.

3.  Save your changes.

</div>

<div>

<div class="title">

Next steps

</div>

- For clusters that use the default `RollingUpdate` update strategy, the control plane machine set propagates changes to your control plane configuration automatically.

- For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

</div>

## Automatic updates to the control plane configuration

The `RollingUpdate` update strategy automatically propagates changes to your control plane configuration to minimize manual intervention.

This update strategy is the default configuration for the control plane machine set.

For clusters that use the `RollingUpdate` update strategy, the Operator creates a replacement control plane machine with the configuration that is specified in the CR. When the replacement control plane machine is ready, the Operator deletes the control plane machine that is marked for replacement. The replacement machine then joins the control plane.

If multiple control plane machines are marked for replacement, the Operator protects etcd health during replacement by repeating this replacement process one machine at a time until it has replaced each machine.

## Manual updates to the control plane configuration

Use the `OnDelete` update strategy to test configuration changes on individual control plane machines before applying them cluster-wide. Manually replacing machines allows you to test changes to your configuration on a single machine before applying the changes more broadly.

For clusters that are configured to use the `OnDelete` update strategy, the Operator creates a replacement control plane machine when you delete an existing machine. When the replacement control plane machine is ready, the etcd Operator allows the existing machine to be deleted. The replacement machine then joins the control plane.

If multiple control plane machines are deleted, the Operator creates all of the required replacement machines simultaneously. The Operator maintains etcd health by preventing more than one machine being removed from the control plane at once.

# Replacing a control plane machine

Replace a control plane machine to apply updated configurations or recover from hardware issues while maintaining cluster stability. The control plane machine set replaces the deleted machine with one using the specification in the control plane machine set custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- If your cluster runs on Red Hat OpenStack Platform (RHOSP) and you need to evacuate a compute server, such as for an upgrade, you must disable the RHOSP compute node that the machine runs on by running the following command:

  ``` terminal
  $ openstack compute service set <target_node_host_name> nova-compute --disable
  ```

  For more information, see [Preparing to migrate](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/17.1/html/configuring_the_compute_service_for_instance_creation/assembly_migrating-virtual-machine-instances-between-compute-nodes_migrating-instances#proc_preparing-to-migrate_migrating-instances) in the RHOSP documentation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  List the control plane machines in your cluster by running the following command:

    ``` terminal
    $ oc get machines \
      -l machine.openshift.io/cluster-api-machine-role==master \
      -n openshift-machine-api
    ```

2.  Delete a control plane machine by running the following command:

    ``` terminal
    $ oc delete machine \
      -n openshift-machine-api \
      <control_plane_machine_name>
    ```

    where `<control_plane_machine_name>` specifies the name of the control plane machine to delete.

    > [!NOTE]
    > If you delete multiple control plane machines, the control plane machine set replaces them according to the configured update strategy:
    >
    > - For clusters that use the default `RollingUpdate` update strategy, the Operator replaces one machine at a time until each machine is replaced.
    >
    > - For clusters that are configured to use the `OnDelete` update strategy, the Operator creates all of the required replacement machines simultaneously.
    >
    > Both strategies maintain etcd health during control plane machine replacement.

</div>

# Additional resources

- [Control plane machine set configuration](cpmso-configuration.md#cpmso-configuration)

- [Provider-specific configuration options](cpmso-configuration.md#cpmso-config-provider-specific_cpmso-configuration)
