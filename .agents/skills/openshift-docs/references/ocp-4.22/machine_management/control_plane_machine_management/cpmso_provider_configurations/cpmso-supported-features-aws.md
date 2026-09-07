<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

# Restricting the API server to private for an Amazon Web Services cluster

If the security posture of your organization does not allow clusters to use an open API endpoint, you can restrict the API server to use only internal load balancers. To implement this API server restriction, use the Amazon Web Services (AWS) console and OpenShift CLI (`oc`) to delete the external load balancer components.

<div>

<div class="title">

Prerequisites

</div>

- You have installed an OpenShift Container Platform cluster on AWS.

- You have access to the AWS console as a user with administrator privileges.

- You have access to the OpenShift CLI (`oc`) as a user with administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the AWS console as a user with administrator privileges.

2.  Delete the external load balancer.

    > [!NOTE]
    > The API DNS entry in the private zone already points to the internal load balancer, which uses an identical configuration, so you do not need to modify the internal load balancer.

3.  Delete the `api.<cluster_name>.<domain_name>` DNS entry in the public zone.

    where `<cluster_name>` is the name of the cluster and `<domain_name>` is the base domain for the cluster.

4.  To remove the external load balancers, log in to the OpenShift CLI (`oc`) as a user with administrator privileges.

5.  Edit the `ControlPlaneMachineSet` CR by running the following command:

    ``` terminal
    $ oc edit controlplanemachineset.machine.openshift.io cluster \
      -n openshift-machine-api
    ```

6.  Remove the external load balancers by deleting the corresponding lines in the control plane machine set custom resource (CR).

    In the `spec.template.spec.providerSpec.value.loadBalancers` section of the CR, the `name` value for the external load balancer ends in `-ext`. Delete the line with the external load balancer `name` value and the line with the external load balancer `type` value that accompanies it.

    ``` yaml
    apiVersion: machine.openshift.io/v1
    kind: ControlPlaneMachineSet
    metadata:
      name: cluster
      namespace: openshift-machine-api
    spec:
    # ...
      template:
    # ...
          spec:
            providerSpec:
              value:
                loadBalancers:
                - name: <cluster_id>-ext
                  type: network
                - name: <cluster_id>-int
                  type: network
    # ...
    ```

7.  Save your changes and exit the object specification.

    When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring the Ingress Controller endpoint publishing scope to Internal](../../../networking/ingress_load_balancing/configuring_ingress_cluster_traffic/nw-configuring-ingress-controller-endpoint-publishing-strategy.md#nw-ingresscontroller-change-internal_nw-configuring-ingress-controller-endpoint-publishing-strategy)

</div>

# Changing the Amazon Web Services instance type by using a control plane machine set

If you need more resources for your control plane machines, you can change the Amazon Web Services (AWS) instance type that they use. To change the instance type, you update the instance type value in the control plane machine set custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift CLI (`oc`) as a user with administrator privileges.

- Your AWS cluster uses a control plane machine set.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit your control plane machine set CR by running the following command:

    ``` terminal
    $ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
    ```

2.  Update the CR to implement your configuration changes:

    ``` yaml
    apiVersion: machine.openshift.io/v1
    kind: ControlPlaneMachineSet
    # ...
    spec:
      template:
        machines_v1beta1_machine_openshift_io:
          spec:
            providerSpec:
              value:
                instanceType: <compatible_aws_instance_type>
    ```

    where `<compatible_aws_instance_type>` specifies a larger AWS instance type with the same base. For example, you can change this value from `m6i.xlarge` to `m6i.2xlarge` or `m6i.4xlarge`.

3.  Save your changes and exit the object specification.

    When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

    - For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.

    - For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

</div>

# Assigning machines to placement groups for Elastic Fabric Adapter instances by using machine sets

You can configure a machine set to deploy machines on Elastic Fabric Adapter (EFA) instances within an existing Amazon Web Services (AWS) placement group.

[EFA](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) instances do not require placement groups, and you can use placement groups for purposes other than configuring an EFA. This example uses both to demonstrate a configuration that can improve network performance for machines within the specified placement group.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift CLI (`oc`) as a user with administrator privileges.

- You created a placement group in the AWS console.

  > [!NOTE]
  > Ensure that the [rules and limitations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#limitations-placement-groups) for the type of placement group that you create are compatible with your intended use case. The control plane machine set spreads the control plane machines across multiple failure domains when possible. To use placement groups for the control plane, you must use a placement group type that can span multiple Availability Zones.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit your control plane machine set custom resource (CR) by running the following command:

    ``` terminal
    $ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
    ```

2.  Update the CR to implement your configuration changes:

    ``` yaml
    apiVersion: machine.openshift.io/v1
    kind: ControlPlaneMachineSet
    # ...
    spec:
      template:
        machines_v1beta1_machine_openshift_io:
          spec:
            providerSpec:
              value:
                instanceType: <supported_instance_type>
                networkInterfaceType: <interface_type>
                placement:
                  availabilityZone: <zone>
                  region: <region>
                placementGroupName: <placement_group>
                placementGroupPartition: <placement_group_partition_number>
    ```

    where:

    `<supported_instance_type>`
    Specifies an instance type that [supports EFAs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types).

    `<interface_type>`
    Specifies the network interface type. To use an EFA, set this value to `EFA`.

    `<zone>`
    Specifies the zone; for example, `us-east-1a`.

    `<region>`
    Specifies the region; for example, `us-east-1`.

    `<placement_group>`
    Specifies the name of the existing AWS placement group to deploy machines in.

    `<placement_group_partition_number>`
    Specifies the partition number of the existing AWS placement group to deploy machines in. This parameter is optional.

3.  Save your changes and exit the object specification.

    When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

    - For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.

    - For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

</div>

<div>

<div class="title">

Verification

</div>

- In the AWS console, find a machine that the machine set created and verify the following in the machine properties:

  - The placement group field has the value that you specified for the `placementGroupName` parameter in the machine set.

  - If you specified a partition number, the partition number field has the value that you specified for the `placementGroupPartition` parameter in the machine set.

  - The interface type field indicates that it uses an EFA.

</div>

# Configuring the AWS EC2 Instance Metadata Service by using machine sets

You can use machine sets to create machines that use the version of the Amazon EC2 Instance Metadata Service (IMDS) that meets the security requirements of your organization.

Machine sets can create machines that allow the use of both IMDSv1 and [IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) or machines that require the use of IMDSv2.

You can specify whether to require the use of IMDSv2 by adding or editing the value of `metadataServiceOptions.authentication` in the machine set.

> [!IMPORTANT]
> Before configuring a machine set to create machines that require IMDSv2, ensure that any workloads that interact with the AWS metadata service support IMDSv2.

<div>

<div class="title">

Prerequisites

</div>

- To use IMDSv2, your AWS cluster must have been created with OpenShift Container Platform version 4.7 or later.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit your control plane machine set custom resource (CR) by running the following command:

    ``` terminal
    $ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
    ```

2.  Update the CR to implement your configuration changes:

    ``` yaml
    apiVersion: machine.openshift.io/v1
    kind: ControlPlaneMachineSet
    # ...
    spec:
      template:
        machines_v1beta1_machine_openshift_io:
          spec:
            providerSpec:
              value:
                imetadataServiceOptions:
                  authentication: Required
    ```

    To require IMDSv2, set the `metadataServiceOptions.authentication` parameter value to `Required`. To allow the use of both IMDSv1 and IMDSv2, set the parameter value to `Optional`. If you do not specify a value, machines that the machine set creates allow the use of both IMDSv1 and IMDSv2.

3.  Save your changes and exit the object specification.

    When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

    - For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.

    - For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Boot image management](../../../machine_configuration/mco-update-boot-images.md#mco-update-boot-images)

</div>

# Configuring storage throughput for gp3 drives

You can improve performance for high traffic services by increasing the throughput of gp3 storage volumes in an AWS cluster. You can configure the storage throughput by editing your compute or control plane machine set.

<div>

<div class="title">

Prerequisites

</div>

- You use gp3 storage volume(s).

</div>

<div>

<div class="title">

Procedure

</div>

- Add or edit the following lines under the `providerSpec` field in your compute or control plane machine set:

  ``` yaml
  providerSpec:
    value:
      blockDevices:
        - ebs:
            throughputMib: <throughput_value>
  ```

  where:

  `<throughput_value>`
  Specifies a value in MiB per second between 125 and 2,000. You can only edit this value on gp3 volumes. The default value is `125`.

</div>

# Creating Dedicated Instances by using machine sets

You can configure a machine set to deploy machines as Dedicated Instances that run in a virtual private cloud (VPC) on hardware that only a single customer can use. To change use Dedicated Instances, you update the placement tenancy value in the machine set custom resource (CR).

Amazon Web Services (AWS) Dedicated Instances are EC2 instances that are physically isolated at the host hardware level. This isolation applies to instances that a single payer account owns even if the instances belong to different AWS accounts.

Public tenancy is the default tenancy. Instances with public tenancy run on shared hardware and can share hardware with Dedicated Instances that belong to the same AWS account.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift CLI (`oc`) as a user with administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit your control plane machine set custom resource (CR) by running the following command:

    ``` terminal
    $ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
    ```

2.  Update the CR to implement your configuration changes:

    ``` yaml
    apiVersion: machine.openshift.io/v1
    kind: ControlPlaneMachineSet
    # ...
    spec:
      template:
        machines_v1beta1_machine_openshift_io:
          spec:
            providerSpec:
              value:
                placement:
                  tenancy: dedicated
    ```

    To use Dedicated Instances, set the `placement.tenancy` parameter value to `dedicated`.

3.  Save your changes and exit the object specification.

    When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

    - For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.

    - For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

</div>

# Configuring Capacity Reservations by using machine sets

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define by using Capacity Reservations on Amazon Web Services clusters, including On-Demand Capacity Reservations and Capacity Blocks for ML.

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define.

These parameters specify the instance type, region, and number of instances that you want to reserve. If your Capacity Reservation can accommodate the capacity request, the deployment succeeds.

For more information, including limitations and suggested use cases for this Amazon Web Services offering, see [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) in the AWS documentation.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You installed the OpenShift CLI (`oc`).

- You have purchased an On-Demand Capacity Reservation or Capacity Block for ML. For more information, see [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) in the AWS documentation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit your control plane machine set custom resource (CR) by running the following command:

    ``` terminal
    $ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
    ```

2.  Update the CR to implement your configuration changes:

    <div class="formalpara">

    <div class="title">

    Sample configuration

    </div>

    ``` yaml
    apiVersion: machine.openshift.io/v1
    kind: ControlPlaneMachineSet
    # ...
    spec:
      template:
        machines_v1beta1_machine_openshift_io:
          spec:
            providerSpec:
              value:
                capacityReservationId: <capacity_reservation>
                marketType: <market_type>
    # ...
    ```

    </div>

    where:

    `<capacity_reservation>`
    Specifies the ID of the Capacity Block for ML or On-Demand Capacity Reservation that you want the machine set to deploy machines on.

    `<market_type>`
    Specifies the market type to use. The following values are valid:

    `CapacityBlock`
    Use this market type with Capacity Blocks for ML.

    `OnDemand`
    Use this market type with On-Demand Capacity Reservations.

3.  Save your changes and exit the object specification.

    When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

    - For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.

    - For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

</div>

<div>

<div class="title">

Verification

</div>

- To verify machine deployment, list the machines that the machine set created by running the following command:

  ``` terminal
  $ oc get machine \
    -n openshift-machine-api \
    -l machine.openshift.io/cluster-api-machine-role=master
  ```

  In the output, verify that the characteristics of the listed machines match the parameters of your Capacity Reservation.

</div>

# Additional resources

- [Updating the control plane configuration](../cpmso-managing-machines.md#cpmso-feat-config-update_cpmso-managing-machines)

- [Control plane configuration options for Amazon Web Services](cpmso-config-options-aws.md#cpmso-config-options-aws)
