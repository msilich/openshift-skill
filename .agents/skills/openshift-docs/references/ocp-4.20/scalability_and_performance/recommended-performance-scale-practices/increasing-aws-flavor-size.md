<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If the control plane machines in an Amazon Web Services (AWS) cluster require more resources, you can select a larger AWS instance type for the control plane machines to use.

> [!NOTE]
> The procedure for clusters that use a control plane machine set is different from the procedure for clusters that do not use a control plane machine set.
>
> If you are uncertain about the state of the `ControlPlaneMachineSet` CR in your cluster, you can verify the CR status.

# Additional resources

- [Verify the CR status](../../machine_management/control_plane_machine_management/cpmso-getting-started.md#cpmso-checking-status_cpmso-getting-started)

# Changing the Amazon Web Services instance type by using a control plane machine set

You can change the Amazon Web Services (AWS) instance type that your control plane machines use by updating the specification in the control plane machine set custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- Your AWS cluster uses a control plane machine set.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the following line under the `providerSpec` field:

    ``` yaml
    providerSpec:
      value:
        ...
        instanceType: <compatible_aws_instance_type>
    ```

    - `<compatible_aws_instance_type>`: Specifies a larger AWS instance type with the same base as the previous selection. For example, you can change `m6i.xlarge` to `m6i.2xlarge` or `m6i.4xlarge`.

2.  Save your changes.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Managing control plane machines with control plane machine sets](../../machine_management/control_plane_machine_management/cpmso-managing-machines.md#cpmso-managing-machines)

</div>

# Changing the Amazon Web Services instance type by using the AWS console

You can change the Amazon Web Services (AWS) instance type that your control plane machines use by updating the instance type in the AWS console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the AWS console with the permissions required to modify the EC2 Instance for your cluster.

- You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Open the AWS console and fetch the instances for the control plane machines.

2.  Choose one control plane machine instance.

    1.  For the selected control plane machine, back up the etcd data by creating an etcd snapshot. For more information, see "Backing up etcd".

    2.  In the AWS console, stop the control plane machine instance.

    3.  Select the stopped instance, and click **Actions** → **Instance Settings** → **Change instance type**.

    4.  Change the instance to a larger type, ensuring that the type is the same base as the previous selection, and apply changes. For example, you can change `m6i.xlarge` to `m6i.2xlarge` or `m6i.4xlarge`.

    5.  Start the instance.

    6.  If your OpenShift Container Platform cluster has a corresponding `Machine` object for the instance, update the instance type of the object to match the instance type set in the AWS console.

3.  Repeat this process for each control plane machine.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Backing up etcd](../../backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.md#backing-up-etcd)

- [AWS documentation about changing the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)

</div>
