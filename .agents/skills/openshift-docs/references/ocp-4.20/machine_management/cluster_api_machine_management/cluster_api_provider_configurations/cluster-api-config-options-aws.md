<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can change the configuration of your Amazon Web Services (AWS) Cluster API machines by updating values in the Cluster API custom resource manifests.

> [!IMPORTANT]
> Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The YAML file examples show configurations for an Amazon Web Services cluster.

You can enable features by updating values in the Cluster API custom resource manifests.

# Sample YAML for a Cluster API machine template resource on Amazon Web Services

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines.

``` yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      iamInstanceProfile: # ...
      instanceType: m5.large
      ignition:
        storageType: UnencryptedUserData
        version: "3.4"
      ami:
        id: # ...
      subnet:
        filters:
        - name: tag:Name
          values:
          - # ...
      additionalSecurityGroups:
      - filters:
        - name: tag:Name
          values:
          - # ...
```

where:

`kind`
Specifies the machine template kind. This value must match the value for your platform.

`metadata.name`
Specifies a name for the machine template.

`spec.template.spec`
Specifies the details for your environment. The values here are examples.

# Sample YAML for a Cluster API compute machine set resource on Amazon Web Services

The compute machine set resource defines additional properties of the machines that the resource creates. The compute machine set also references the cluster resource and machine template when creating machines.

``` yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: AWSMachineTemplate
        name: <template_name>
```

where:

`metadata.name`
Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.

`metadata.labels.cluster.x-k8s.io/cluster-name`
Specifies the cluster ID as the name of the cluster.

`spec.clusterName`
Specifies the cluster ID as the name of the cluster.

`spec.template.spec.infrastructureRef.kind`
Specifies the machine template kind. This value must match the value for your platform.

`spec.template.spec.infrastructureRef.name`
Specifies the machine template name.

## Elastic Fabric Adapter instances and placement group options

You can deploy compute machines on Elastic Fabric Adapter (EFA) instances within an existing AWS placement group.

EFA instances do not require placement groups, and you can use placement groups for purposes other than configuring an EFA. The following example uses an EFA and placement group together to demonstrate a configuration that can improve network performance for machines within the specified placement group.

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

<div class="formalpara">

<div class="title">

Sample EFA instance and placement group configuration

</div>

``` yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceType: <supported_instance_type>
      networkInterfaceType: efa
      placementGroupName: <placement_group>
      placementGroupPartition: <placement_group_partition_number>
# ...
```

</div>

where:

`spec.template.spec.instanceType`
Specifies an instance type that supports EFAs. For more information, see "Supported instance types".

`spec.template.spec.networkInterfaceType`
Specifies the `efa` network interface type.

`spec.template.spec.placementGroupName`
Specifies the name of the existing AWS placement group to deploy machines in.

`spec.template.spec.placementGroupPartition`
Specifies the partition number of the existing AWS placement group where you want your machines deployed. Setting a value for the parameter is optional.

> [!NOTE]
> Ensure that the rules and limitations for the type of placement group that you create are compatible with your intended use case. For more information, see "Placement groups for your Amazon EC2 instances".

<div>

<div class="title">

Additional resources

</div>

- [Elastic Fabric Adapter (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html)

- [Placement groups for your Amazon EC2 instances (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#limitations-placement-groups)

- [Supported instance types (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types)

</div>

## Amazon EC2 Instance Metadata Service configuration options

You can restrict the version of the Amazon EC2 Instance Metadata Service (IMDS) that machines on Amazon Web Services (AWS) clusters use. Machines can require the use of IMDSv2, or allow the use of IMDSv1 in addition to IMDSv2.

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

> [!IMPORTANT]
> Before creating machines that require IMDSv2, ensure that any workloads that interact with the IMDS support IMDSv2.

<div class="formalpara">

<div class="title">

Sample IMDS configuration

</div>

``` yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceMetadataOptions:
        httpEndpoint: enabled
        httpPutResponseHopLimit: 1
        httpTokens: optional
        instanceMetadataTags: disabled
# ...
```

</div>

where:

`spec.template.spec.instanceMetadataOptions.httpPutResponseHopLimit`
Specifies the number of network hops allowed for IMDSv2 calls. If no value is specified, this parameter is set to `1` by default.

`spec.template.spec.instanceMetadataOptions.httpTokens`
Specifies whether to require the use of IMDSv2. If no value is specified, this parameter is set to `optional` by default. The following values are valid:

- `optional`: Allow the use of both IMDSv1 and IMDSv2.

- `required`: Require IMDSv2.

> [!NOTE]
> The Machine API does not support the `httpEndpoint`, `httpPutResponseHopLimit`, and `instanceMetadataTags` fields. If you migrate a Cluster API machine template that uses this feature to a Machine API compute machine set, any Machine API machines that it creates will not have these fields and the underlying instances will not use these settings. Any existing machines that the migrated machine set manages will retain these fields and the underlying instances will continue to use these settings.

Requiring the use of IMDSv2 might cause timeouts. For more information, including mitigation strategies, see "Instance metadata access considerations".

<div>

<div class="title">

Additional resources

</div>

- [IMDSv2 (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

- [Instance metadata access considerations (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html#imds-considerations)

</div>

## Dedicated Instance configuration options

You can deploy machines that are backed by Dedicated Instances on Amazon Web Services (AWS) clusters.

Dedicated Instances run in a virtual private cloud (VPC) on hardware that is dedicated to a single customer. These Amazon EC2 instances are physically isolated at the host hardware level. The isolation of Dedicated Instances occurs even if the instances belong to different AWS accounts that are linked to a single payer account. However, other instances that are not dedicated can share hardware with Dedicated Instances if they belong to the same AWS account.

OpenShift Container Platform supports instances with public or dedicated tenancy.

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

<div class="formalpara">

<div class="title">

Sample Dedicated Instances configuration

</div>

``` yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      tenancy: dedicated
# ...
```

</div>

The `tenancy` field specifies using instances with dedicated tenancy that run on single-tenant hardware. If you do not specify the `dedicated` value, instances with public tenancy that run on shared hardware are used by default.

## Non-guaranteed Spot Instances and hourly cost limits

You can deploy machines as non-guaranteed Spot Instances on Amazon Web Services (AWS). Spot Instances use spare AWS EC2 capacity and are less expensive than On-Demand Instances. You can use Spot Instances for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads.

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

> [!IMPORTANT]
> AWS EC2 can reclaim the capacity for a Spot Instance at any time.

<div class="formalpara">

<div class="title">

Sample Spot Instance configuration

</div>

``` yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      spotMarketOptions:
        maxPrice: <price_per_hour>
# ...
```

</div>

where:

`spec.template.spec.spotMarketOptions`
Specifies the use of Spot Instances.

`spec.template.spec.spotMarketOptions.maxPrice`
Optional parameter. Specifies an hourly cost limit in US dollars for the Spot Instance. For example, setting the `<price_per_hour>` value to `2.50` limits the cost of the Spot Instance to USD 2.50 per hour. When this value is not set, the maximum price charges up to the On-Demand Instance price.

> [!WARNING]
> Setting a specific `maxPrice: <price_per_hour>` value might increase the frequency of interruptions compared to using the default On-Demand Instance price. Red Hat recommends to use the default On-Demand Instance price and to not set the maximum price for Spot Instances.

Interruptions can occur when using Spot Instances for the following reasons:

- The instance price exceeds your maximum price

- The demand for Spot Instances increases

- The supply of Spot Instances decreases

AWS gives a two-minute warning to the user when an interruption occurs. OpenShift Container Platform begins to remove the workloads from the affected instances when AWS issues the termination warning.

When AWS terminates an instance, a termination handler running on the Spot Instance node deletes the machine resource. To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a Spot Instance.

## Capacity Reservation configuration options

OpenShift Container Platform version 4.17 and later supports Capacity Reservations on Amazon Web Services clusters, including On-Demand Capacity Reservations and Capacity Blocks for ML.

You can deploy machines on any available resources that match the parameters of a capacity request that you define. These parameters specify the instance type, region, and number of instances that you want to reserve. If your Capacity Reservation can accommodate the capacity request, the deployment succeeds.

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

<div class="formalpara">

<div class="title">

Sample Capacity Reservation configuration

</div>

``` yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      capacityReservationId: <capacity_reservation>
      capacityReservationPreference: <reservation_preference>
      marketType: <market_type>
# ...
```

</div>

where:

`spec.template.spec.capacityReservationId`
Specifies the ID of the Capacity Block for ML or On-Demand Capacity Reservation that you want to deploy machines on.

`spec.template.spec.capacityReservationPreference`
Specifies your preferred capacity reservation behavior. The following values are valid:

`CapacityReservationsOnly`
Use this option to require a matching capacity reservation. If no matching capacity reservation is available, the instance fails to launch.

`Open`
Use this option to allow using an open capacity reservation that matches the availability zone and instance type.

`None`
Use this option to prohibit using a capacity reservation. You might use this option to help keep capacity reservations available for workloads that you want to use them.

`spec.template.spec.marketType`
Specifies the market type to use. The following values are valid:

`CapacityBlock`
Use this market type with Capacity Blocks for ML.

`OnDemand`
Use this market type with On-Demand Capacity Reservations.

`Spot`
Use this market type with Spot Instances. This option is not compatible with Capacity Reservations.

For more information, including limitations and suggested use cases for this offering, see On-Demand Capacity Reservations and Capacity Blocks for ML (AWS documentation).

<div>

<div class="title">

Additional resources

</div>

- [On-Demand Capacity Reservations and Capacity Blocks for ML (AWS documentation)](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html)

</div>

## GPU-enabled machine options

You can deploy GPU-enabled compute machines on Amazon Web Services (AWS).

The following sample configuration uses an AWS G4dn instance type, which includes an NVIDIA Tesla T4 Tensor Core GPU, as an example.

For more information about supported instance types, see the following pages in the NVIDIA documentation:

- NVIDIA GPU Operator Community support matrix

- NVIDIA AI Enterprise support matrix

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file and a machine set YAML file that references the machine template when it deploys machines.

<div class="formalpara">

<div class="title">

Sample GPU-enabled machine template configuration

</div>

``` yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceType: g4dn.xlarge
# ...
```

</div>

- The `spec.template.spec.instanceType` field specifies a G4dn instance type.

<div class="formalpara">

<div class="title">

Sample GPU-enabled machine set configuration

</div>

``` yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <cluster_name>-gpu-<region>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <cluster_name>-gpu-<region>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <cluster_name>-gpu-<region>
        node-role.kubernetes.io/<role>: ""
# ...
```

</div>

where:

`metadate.name`
Specifies a name that includes the `gpu` role. The name includes the cluster ID as a prefix and the region as a suffix.

`spec.selector.matchLabels.cluster.x-k8s.io/set-name`
Specifies a selector label that matches the machine set name.

`spec.template.metadata.labels.cluster.x-k8s.io/set-name`
Specifies a template label that matches the machine set name.

<div>

<div class="title">

Additional resources

</div>

- [AWS G4dn instance type](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing)

- [NVIDIA GPU Operator Community support matrix (NVIDIA documentation)](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/platform-support.html)

- [NVIDIA AI Enterprise support matrix (NVIDIA documentation)](https://docs.nvidia.com/ai-enterprise/latest/product-support-matrix/index.html)

</div>
