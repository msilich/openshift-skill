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

# Assigning machines to placement groups for Elastic Fabric Adapter instances by using machine sets

You can configure a machine set to deploy machines on Elastic Fabric Adapter (EFA) instances within an existing Amazon Web Services (AWS) placement group.

[EFA](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) instances do not require placement groups, and you can use placement groups for purposes other than configuring an EFA. This example uses both to demonstrate a configuration that can improve network performance for machines within the specified placement group.

<div>

<div class="title">

Prerequisites

</div>

- You created a placement group in the AWS console.

  > [!NOTE]
  > Ensure that the [rules and limitations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#limitations-placement-groups) for the type of placement group that you create are compatible with your intended use case. The control plane machine set spreads the control plane machines across multiple failure domains when possible. To use placement groups for the control plane, you must use a placement group type that can span multiple Availability Zones.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In a text editor, open the YAML file for an existing machine set or create a new one.

2.  Edit the following lines under the `providerSpec` field:

</div>

``` yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    spec:
      providerSpec:
        value:
          instanceType: <supported_instance_type>
          networkInterfaceType: EFA
          placement:
            availabilityZone: <zone>
            region: <region>
          placementGroupName: <placement_group>
          placementGroupPartition: <placement_group_partition_number>
# ...
```

where:

`spec.template.spec.providerSpec.value.instanceType`
Specifies an instance type that [supports EFAs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types).

`spec.template.spec.providerSpec.value.networkInterfaceType`
Specifies the `EFA` network interface type.

`spec.template.spec.providerSpec.value.placement.availabilityZone`
Specifies the zone, for example, `us-east-1a`.

`spec.template.spec.providerSpec.value.placement.region`
Specifies the region, for example, `us-east-1`.

`spec.template.spec.providerSpec.value.placementGroupName`
Specifies the name of the existing AWS placement group to deploy machines in.

`spec.template.spec.providerSpec.value.placementGroupPartition`
Specifies the partition number of the existing AWS placement group to deploy machines in. This value is optional.

<div>

<div class="title">

Verification

</div>

- In the AWS console, find a machine that the machine set created and verify the following in the machine properties:

  - The placement group field has the value that you specified for the `placementGroupName` parameter in the machine set.

  - The partition number field has the value that you specified for the `placementGroupPartition` parameter in the machine set.

  - The interface type field indicates that it uses an EFA.

</div>

# Machine set options for the Amazon EC2 Instance Metadata Service

You can use machine sets to create machines that use a specific version of the Amazon EC2 Instance Metadata Service (IMDS).

Machine sets can create machines that allow the use of both IMDSv1 and IMDSv2 or machines that require the use of IMDSv2.

> [!NOTE]
> To use IMDSv2 on Amazon Web Services (AWS) clusters that were created with OpenShift Container Platform version 4.6 or earlier, you must update your boot image. For more information, see "Boot image management".

> [!IMPORTANT]
> Before configuring a machine set to create machines that require IMDSv2, ensure that any workloads that interact with the AWS metadata service support IMDSv2.

<div>

<div class="title">

Additional resources

</div>

- [Boot image management](../../../machine_configuration/mco-update-boot-images.md#mco-update-boot-images)

</div>

## Configuring IMDS by using machine sets

You can specify whether to require the use of IMDSv2 by adding or editing the value of `metadataServiceOptions.authentication` in the machine set YAML file for your machines.

<div>

<div class="title">

Prerequisites

</div>

- To use IMDSv2, your Amazon Web Services (AWS) cluster must have been created with OpenShift Container Platform version 4.7 or later.

</div>

<div>

<div class="title">

Procedure

</div>

- Add or edit the following lines under the `providerSpec` field:

  ``` yaml
  providerSpec:
    value:
      metadataServiceOptions:
        authentication: Required
  ```

  where:

  `providerSpec.value.metadataServiceOptions.authentication`
  Specifies whether to require IMDSv2. To require IMDSv2, set the parameter value to `Required`. To allow the use of both IMDSv1 and IMDSv2, set the parameter value to `Optional`. If you do not specify a value, both IMDSv1 and IMDSv2 are allowed.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Use the Instance Metadata Service to access instance metadata (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

</div>

# Machine sets that deploy machines as Dedicated Instances

You can create a machine set running on Amazon Web Services (AWS) that deploys machines as Dedicated Instances. Dedicated Instances run in a virtual private cloud (VPC) on hardware that is dedicated to a single customer.

These Amazon EC2 instances are physically isolated at the host hardware level. The isolation of Dedicated Instances occurs even if the instances belong to different AWS accounts that are linked to a single payer account. However, other instances that are not dedicated can share hardware with Dedicated Instances if they belong to the same AWS account.

Instances with either public or dedicated tenancy are supported by the Machine API. Instances with public tenancy run on shared hardware. Public tenancy is the default tenancy. Instances with dedicated tenancy run on single-tenant hardware.

## Creating Dedicated Instances by using machine sets

You can run a machine that is backed by a Dedicated Instance by using Machine API integration. Set the `tenancy` field in your machine set YAML file to launch a Dedicated Instance on Amazon Web Services (AWS).

<div>

<div class="title">

Procedure

</div>

- Specify a dedicated tenancy under the `providerSpec` field:

  ``` yaml
  providerSpec:
    placement:
      tenancy: dedicated
  ```

</div>

# Configuring Capacity Reservations by using machine sets

OpenShift Container Platform version 4.17 and later supports Capacity Reservations on Amazon Web Services clusters, including On-Demand Capacity Reservations and Capacity Blocks for ML.

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define.

These parameters specify the instance type, region, and number of instances that you want to reserve. If your Capacity Reservation can accommodate the capacity request, the deployment succeeds.

For more information, including limitations and suggested use cases for this Amazon Web Services offering, see [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) in the AWS documentation.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You installed the OpenShift CLI (`oc`).

- You purchased an On-Demand Capacity Reservation or Capacity Block for ML. For more information, see [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) in the AWS documentation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In a text editor, open the YAML file for an existing machine set or create a new one.

2.  Edit the following section under the `providerSpec` field:

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
