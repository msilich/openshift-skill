<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you begin an installation on infrastructure that you provision, be sure that your AWS environment meets the following installation requirements.

For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

# Required machines for cluster installation

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails.

The smallest OpenShift Container Platform clusters require the following hosts:

> [!IMPORTANT]
> For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

| Hosts | Description |
|----|----|
| One temporary bootstrap machine | The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster. |
| Three control plane machines | The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane. |
| At least two compute machines, which are also known as worker machines. | The workloads requested by OpenShift Container Platform users run on the compute machines. |

Minimum required hosts

> [!IMPORTANT]
> To maintain high availability of your cluster, use separate physical hosts for these cluster machines.

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. However, the compute machines can choose between Red Hat Enterprise Linux CoreOS (RHCOS), Red Hat Enterprise Linux (RHEL) 8.6 and later.

Note that RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.2 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits).

## Minimum resource requirements for cluster installation

Each created cluster must meet minimum requirements so that the cluster runs as expected.

| Machine | Operating System | vCPU <sup>\[1\]</sup> | Virtual RAM | Storage | Input/Output Per Second (IOPS)<sup>\[2\]</sup> |
|----|----|----|----|----|----|
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Minimum resource requirements

1.  One vCPU is equivalent to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.

2.  OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.

3.  As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Use of RHEL 7 compute machines is deprecated and has been removed in OpenShift Container Platform 4.10 and later.

> [!NOTE]
> For OpenShift Container Platform version 4.19, RHCOS is based on RHEL version 9.6, which updates the micro-architecture requirements. The following list contains the minimum instruction set architectures (ISA) that each architecture requires:
>
> - x86-64 architecture requires x86-64-v2 ISA
>
> - ARM64 architecture requires ARMv8.0-A ISA
>
> - IBM Power architecture requires Power 9 ISA
>
> - s390x architecture requires z14 ISA
>
> For more information, see "Architectures".

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

<div>

<div class="title">

Additional resources

</div>

- [Architectures (RHEL documentation)](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.2_release_notes/index#architectures)

</div>

<div>

<div class="title">

Additional resources

</div>

- [Optimizing storage](../../../scalability_and_performance/optimization/optimizing-storage.md#optimizing-storage)

</div>

## Tested instance types for AWS

The following Amazon Web Services (AWS) instance types have been tested with OpenShift Container Platform.

> [!NOTE]
> Use the machine types included in the following charts for your AWS instances. If you use an instance type that is not listed in the chart, ensure that the instance size you use matches the minimum resource requirements that are listed in the section named "Minimum resource requirements for cluster installation".

<div class="example">

<div class="title">

Machine types based on 64-bit x86 architecture

</div>

<https://raw.githubusercontent.com/openshift/installer/release-4.20/docs/user/aws/tested_instance_types_x86_64.md>

</div>

## Tested instance types for AWS on 64-bit ARM infrastructures

The following Amazon Web Services (AWS) 64-bit ARM instance types have been tested with OpenShift Container Platform.

> [!NOTE]
> Use the machine types included in the following charts for your AWS ARM instances. If you use an instance type that is not listed in the chart, ensure that the instance size you use matches the minimum resource requirements that are listed in "Minimum resource requirements for cluster installation".

<div class="example">

<div class="title">

Machine types based on 64-bit ARM architecture

</div>

<https://raw.githubusercontent.com/openshift/installer/release-4.20/docs/user/aws/tested_instance_types_aarch64.md>

</div>

# Certificate signing requests management

On user-provisioned infrastructure, you must provide a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that is requested by using kubelet credentials because it cannot confirm that the correct machine issued the request. You must determine and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

# Required AWS infrastructure components

To install OpenShift Container Platform on user-provisioned infrastructure in Amazon Web Services (AWS), you must manually create both the machines and their supporting infrastructure.

For more information about the integration testing for different platforms, see the [OpenShift Container Platform 4.x Tested Integrations](https://access.redhat.com/articles/4128421) page.

By using the provided CloudFormation templates, you can create stacks of AWS resources that represent the following components:

- An AWS Virtual Private Cloud (VPC)

- Networking and load balancing components

- Security groups and roles

- An OpenShift Container Platform bootstrap node

- OpenShift Container Platform control plane nodes

- An OpenShift Container Platform compute node

Alternatively, you can manually create the components or you can reuse existing infrastructure that meets the cluster requirements. Review the CloudFormation templates for more details about how the components interrelate.

## Other infrastructure components

- A VPC

- DNS entries

- Load balancers (classic or network) and listeners

- A public and a private Route 53 zone

- Security groups

- IAM roles

- S3 buckets

If you are working in a disconnected environment, you are unable to reach the public IP addresses for EC2, ELB, and S3 endpoints. Depending on the level to which you want to restrict internet traffic during the installation, the following configuration options are available:

### Option 1: Create VPC endpoints

Create a VPC endpoint and attach it to the subnets that the clusters are using. Name the endpoints as follows:

- `ec2.<aws_region>.amazonaws.com`

- `elasticloadbalancing.<aws_region>.amazonaws.com`

- `s3.<aws_region>.amazonaws.com`

With this option, network traffic remains private between your VPC and the required AWS services.

### Option 2: Create a proxy without VPC endpoints

As part of the installation process, you can configure an HTTP or HTTPS proxy. With this option, internet traffic goes through the proxy to reach the required AWS services.

### Option 3: Create a proxy with VPC endpoints

As part of the installation process, you can configure an HTTP or HTTPS proxy with VPC endpoints. Create a VPC endpoint and attach it to the subnets that the clusters are using. Name the endpoints as follows:

- `ec2.<aws_region>.amazonaws.com`

- `elasticloadbalancing.<aws_region>.amazonaws.com`

- `s3.<aws_region>.amazonaws.com`

When configuring the proxy in the `install-config.yaml` file, add these endpoints to the `noProxy` field. With this option, the proxy prevents the cluster from accessing the internet directly. However, network traffic remains private between your VPC and the required AWS services.

<div class="formalpara">

<div class="title">

Required VPC components

</div>

You must provide a suitable VPC and subnets that allow communication to your machines.

</div>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 46%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Component</th>
<th style="text-align: left;">AWS type</th>
<th colspan="2" style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>VPC</p></td>
<td style="text-align: left;"><ul>
<li><p><code>AWS::EC2::VPC</code></p></li>
<li><p><code>AWS::EC2::VPCEndpoint</code></p></li>
</ul></td>
<td colspan="2" style="text-align: left;"><p>You must provide a public VPC for the cluster to use. The VPC uses an endpoint that references the route tables for each subnet to improve communication with the registry that is hosted in S3.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Public subnets</p></td>
<td style="text-align: left;"><ul>
<li><p><code>AWS::EC2::Subnet</code></p></li>
<li><p><code>AWS::EC2::SubnetNetworkAclAssociation</code></p></li>
</ul></td>
<td colspan="2" style="text-align: left;"><p>Your VPC must have public subnets for between 1 and 3 availability zones and associate them with appropriate Ingress rules.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Internet gateway</p></td>
<td style="text-align: left;"><ul>
<li><p><code>AWS::EC2::InternetGateway</code></p></li>
<li><p><code>AWS::EC2::VPCGatewayAttachment</code></p></li>
<li><p><code>AWS::EC2::RouteTable</code></p></li>
<li><p><code>AWS::EC2::Route</code></p></li>
<li><p><code>AWS::EC2::SubnetRouteTableAssociation</code></p></li>
<li><p><code>AWS::EC2::NatGateway</code></p></li>
<li><p><code>AWS::EC2::EIP</code></p></li>
</ul></td>
<td colspan="2" style="text-align: left;"><p>You must have a public internet gateway, with public routes, attached to the VPC. In the provided templates, each public subnet has a NAT gateway with an EIP address. These NAT gateways allow cluster resources, like private subnet instances, to reach the internet and are not required for some restricted network or proxy scenarios.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Network access control</p></td>
<td style="text-align: left;"><ul>
<li><p><code>AWS::EC2::NetworkAcl</code></p></li>
<li><p><code>AWS::EC2::NetworkAclEntry</code></p></li>
</ul></td>
<td colspan="2" style="text-align: left;"><p>You must allow the VPC to access the following ports:</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>Port</strong></p></td>
<td style="text-align: left;"><p><strong>Reason</strong></p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>80</code></p></td>
<td style="text-align: left;"><p>Inbound HTTP traffic</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>443</code></p></td>
<td style="text-align: left;"><p>Inbound HTTPS traffic</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>22</code></p></td>
<td style="text-align: left;"><p>Inbound SSH traffic</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>1024</code> - <code>65535</code></p></td>
<td style="text-align: left;"><p>Inbound ephemeral traffic</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>0</code> - <code>65535</code></p></td>
<td style="text-align: left;"><p>Outbound ephemeral traffic</p></td>
<td></td>
<td></td>
</tr>
<tr>
<td style="text-align: left;"><p>Private subnets</p></td>
<td style="text-align: left;"><ul>
<li><p><code>AWS::EC2::Subnet</code></p></li>
<li><p><code>AWS::EC2::RouteTable</code></p></li>
<li><p><code>AWS::EC2::SubnetRouteTableAssociation</code></p></li>
</ul></td>
<td colspan="2" style="text-align: left;"><p>Your VPC can have private subnets. The provided CloudFormation templates can create private subnets for between 1 and 3 availability zones. If you use private subnets, you must provide appropriate routes and tables for them.</p></td>
</tr>
</tbody>
</table>

<div class="formalpara">

<div class="title">

Required DNS and load balancing components

</div>

Your DNS and load balancer configuration needs to use a public hosted zone and can use a private hosted zone similar to the one that the installation program uses if it provisions the cluster’s infrastructure. You must create a DNS entry that resolves to your load balancer. An entry for `api.<cluster_name>.<domain>` must point to the external load balancer, and an entry for `api-int.<cluster_name>.<domain>` must point to the internal load balancer.

</div>

The cluster also requires load balancers and listeners for port 6443, which are required for the Kubernetes API and its extensions, and port 22623, which are required for the Ignition config files for new machines. The targets will be the control plane nodes. Port 6443 must be accessible to both clients external to the cluster and nodes within the cluster. Port 22623 must be accessible to nodes within the cluster.

| Component | AWS type | Description |
|----|----|----|
| DNS | `AWS::Route53::HostedZone` | The hosted zone for your internal DNS. |
| Public load balancer | `AWS::ElasticLoadBalancingV2::LoadBalancer` | The load balancer for your public subnets. |
| External API server record | `AWS::Route53::RecordSetGroup` | Alias records for the external API server. |
| External listener | `AWS::ElasticLoadBalancingV2::Listener` | A listener on port 6443 for the external load balancer. |
| External target group | `AWS::ElasticLoadBalancingV2::TargetGroup` | The target group for the external load balancer. |
| Private load balancer | `AWS::ElasticLoadBalancingV2::LoadBalancer` | The load balancer for your private subnets. |
| Internal API server record | `AWS::Route53::RecordSetGroup` | Alias records for the internal API server. |
| Internal listener | `AWS::ElasticLoadBalancingV2::Listener` | A listener on port 22623 for the internal load balancer. |
| Internal target group | `AWS::ElasticLoadBalancingV2::TargetGroup` | The target group for the internal load balancer. |
| Internal listener | `AWS::ElasticLoadBalancingV2::Listener` | A listener on port 6443 for the internal load balancer. |
| Internal target group | `AWS::ElasticLoadBalancingV2::TargetGroup` | The target group for the internal load balancer. |

<div class="formalpara">

<div class="title">

Security groups

</div>

The control plane and worker machines require access to the following ports:

</div>

| Group                    | Type                      | IP Protocol | Port range |
|--------------------------|---------------------------|-------------|------------|
| `MasterSecurityGroup`    | `AWS::EC2::SecurityGroup` | `icmp`      | `0`        |
| `tcp`                    | `22`                      |             |            |
| `tcp`                    | `6443`                    |             |            |
| `tcp`                    | `22623`                   |             |            |
| `WorkerSecurityGroup`    | `AWS::EC2::SecurityGroup` | `icmp`      | `0`        |
| `tcp`                    | `22`                      |             |            |
| `BootstrapSecurityGroup` | `AWS::EC2::SecurityGroup` | `tcp`       | `22`       |
| `tcp`                    | `19531`                   |             |            |

<div class="formalpara">

<div class="title">

Control plane Ingress

</div>

The control plane machines require the following Ingress groups. Each Ingress group is a `AWS::EC2::SecurityGroupIngress` resource.

</div>

| Ingress group | Description | IP protocol | Port range |
|----|----|----|----|
| `MasterIngressEtcd` | etcd | `tcp` | `2379`- `2380` |
| `MasterIngressVxlan` | Vxlan packets | `udp` | `6081` |
| `MasterIngressWorkerVxlan` | Vxlan packets | `udp` | `6081` |
| `MasterIngressInternal` | Internal cluster communication and Kubernetes proxy metrics | `tcp` | `9000` - `9999` |
| `MasterIngressWorkerInternal` | Internal cluster communication | `tcp` | `9000` - `9999` |
| `MasterIngressKube` | Kubernetes kubelet, scheduler and controller manager | `tcp` | `10250` - `10259` |
| `MasterIngressWorkerKube` | Kubernetes kubelet, scheduler and controller manager | `tcp` | `10250` - `10259` |
| `MasterIngressIngressServices` | Kubernetes Ingress services | `tcp` | `30000` - `32767` |
| `MasterIngressWorkerIngressServices` | Kubernetes Ingress services | `tcp` | `30000` - `32767` |
| `MasterIngressGeneve` | Geneve packets | `udp` | `6081` |
| `MasterIngressWorkerGeneve` | Geneve packets | `udp` | `6081` |
| `MasterIngressIpsecIke` | IPsec IKE packets | `udp` | `500` |
| `MasterIngressWorkerIpsecIke` | IPsec IKE packets | `udp` | `500` |
| `MasterIngressIpsecNat` | IPsec NAT-T packets | `udp` | `4500` |
| `MasterIngressWorkerIpsecNat` | IPsec NAT-T packets | `udp` | `4500` |
| `MasterIngressIpsecEsp` | IPsec ESP packets | `50` | `All` |
| `MasterIngressWorkerIpsecEsp` | IPsec ESP packets | `50` | `All` |
| `MasterIngressInternalUDP` | Internal cluster communication | `udp` | `9000` - `9999` |
| `MasterIngressWorkerInternalUDP` | Internal cluster communication | `udp` | `9000` - `9999` |
| `MasterIngressIngressServicesUDP` | Kubernetes Ingress services | `udp` | `30000` - `32767` |
| `MasterIngressWorkerIngressServicesUDP` | Kubernetes Ingress services | `udp` | `30000` - `32767` |

<div class="formalpara">

<div class="title">

Worker Ingress

</div>

The worker machines require the following Ingress groups. Each Ingress group is a `AWS::EC2::SecurityGroupIngress` resource.

</div>

| Ingress group | Description | IP protocol | Port range |
|----|----|----|----|
| `WorkerIngressVxlan` | Vxlan packets | `udp` | `6081` |
| `WorkerIngressWorkerVxlan` | Vxlan packets | `udp` | `6081` |
| `WorkerIngressInternal` | Internal cluster communication | `tcp` | `9000` - `9999` |
| `WorkerIngressWorkerInternal` | Internal cluster communication | `tcp` | `9000` - `9999` |
| `WorkerIngressKube` | Kubernetes kubelet, scheduler, and controller manager | `tcp` | `10250` |
| `WorkerIngressWorkerKube` | Kubernetes kubelet, scheduler, and controller manager | `tcp` | `10250` |
| `WorkerIngressIngressServices` | Kubernetes Ingress services | `tcp` | `30000` - `32767` |
| `WorkerIngressWorkerIngressServices` | Kubernetes Ingress services | `tcp` | `30000` - `32767` |
| `WorkerIngressGeneve` | Geneve packets | `udp` | `6081` |
| `WorkerIngressMasterGeneve` | Geneve packets | `udp` | `6081` |
| `WorkerIngressIpsecIke` | IPsec IKE packets | `udp` | `500` |
| `WorkerIngressMasterIpsecIke` | IPsec IKE packets | `udp` | `500` |
| `WorkerIngressIpsecNat` | IPsec NAT-T packets | `udp` | `4500` |
| `WorkerIngressMasterIpsecNat` | IPsec NAT-T packets | `udp` | `4500` |
| `WorkerIngressIpsecEsp` | IPsec ESP packets | `50` | `All` |
| `WorkerIngressMasterIpsecEsp` | IPsec ESP packets | `50` | `All` |
| `WorkerIngressInternalUDP` | Internal cluster communication | `udp` | `9000` - `9999` |
| `WorkerIngressMasterInternalUDP` | Internal cluster communication | `udp` | `9000` - `9999` |
| `WorkerIngressIngressServicesUDP` | Kubernetes Ingress services | `udp` | `30000` - `32767` |
| `WorkerIngressMasterIngressServicesUDP` | Kubernetes Ingress services | `udp` | `30000` - `32767` |

<div class="formalpara">

<div class="title">

Roles and instance profiles

</div>

You must grant the machines permissions in AWS. The provided CloudFormation templates grant the machines `Allow` permissions for the following `AWS::IAM::Role` objects and provide a `AWS::IAM::InstanceProfile` for each set of roles. If you do not use the templates, you can grant the machines the following broad permissions or the following individual permissions.

</div>

| Role      | Effect                   | Action          | Resource |
|-----------|--------------------------|-----------------|----------|
| Master    | `Allow`                  | `ec2:*`         | `*`      |
| `Allow`   | `elasticloadbalancing:*` | `*`             |          |
| `Allow`   | `iam:PassRole`           | `*`             |          |
| `Allow`   | `s3:GetObject`           | `*`             |          |
| Worker    | `Allow`                  | `ec2:Describe*` | `*`      |
| Bootstrap | `Allow`                  | `ec2:Describe*` | `*`      |
| `Allow`   | `ec2:AttachVolume`       | `*`             |          |
| `Allow`   | `ec2:DetachVolume`       | `*`             |          |

## Cluster machines

You need `AWS::EC2::Instance` objects for the following machines:

- A bootstrap machine. This machine is required during installation, but you can remove it after your cluster deploys.

- Three control plane machines. The control plane machines are not governed by a control plane machine set.

- Compute machines. You must create at least two compute machines, which are also known as worker machines, during installation. These machines are not governed by a compute machine set.

# Required AWS permissions for the IAM user

To deploy all components of an OpenShift Container Platform cluster, you must grant the all the required permissions to the IAM user that you create in Amazon Web Services (AWS).

> [!NOTE]
> Your IAM user must have the permission `tag:GetResources` in the region `us-east-1` to delete the base cluster resources. As part of the AWS API requirement, the OpenShift Container Platform installation program performs various actions in this region.

When you attach the `AdministratorAccess` policy to the IAM user that you create in Amazon Web Services (AWS), you grant that user all of the required permissions. To deploy all components of an OpenShift Container Platform cluster, the IAM user requires the following permissions:

<div class="example">

<div class="title">

Required EC2 permissions for installation

</div>

- `ec2:AttachNetworkInterface`

- `ec2:AuthorizeSecurityGroupEgress`

- `ec2:AuthorizeSecurityGroupIngress`

- `ec2:CopyImage`

- `ec2:CreateNetworkInterface`

- `ec2:CreateSecurityGroup`

- `ec2:CreateTags`

- `ec2:CreateVolume`

- `ec2:DeleteSecurityGroup`

- `ec2:DeleteSnapshot`

- `ec2:DeleteTags`

- `ec2:DeregisterImage`

- `ec2:DescribeAccountAttributes`

- `ec2:DescribeAddresses`

- `ec2:DescribeAvailabilityZones`

- `ec2:DescribeDhcpOptions`

- `ec2:DescribeImages`

- `ec2:DescribeInstanceAttribute`

- `ec2:DescribeInstanceCreditSpecifications`

- `ec2:DescribeInstances`

- `ec2:DescribeInstanceTypes`

- `ec2:DescribeInstanceTypeOfferings`

- `ec2:DescribeInternetGateways`

- `ec2:DescribeKeyPairs`

- `ec2:DescribeNatGateways`

- `ec2:DescribeNetworkAcls`

- `ec2:DescribeNetworkInterfaces`

- `ec2:DescribePrefixLists`

- `ec2:DescribePublicIpv4Pools` (only required if `publicIpv4Pool` is specified in `install-config.yaml`)

- `ec2:DescribeRegions`

- `ec2:DescribeRouteTables`

- `ec2:DescribeSecurityGroupRules`

- `ec2:DescribeSecurityGroups`

- `ec2:DescribeSubnets`

- `ec2:DescribeTags`

- `ec2:DescribeVolumes`

- `ec2:DescribeVpcAttribute`

- `ec2:DescribeVpcClassicLink`

- `ec2:DescribeVpcClassicLinkDnsSupport`

- `ec2:DescribeVpcEndpoints`

- `ec2:DescribeVpcs`

- `ec2:DisassociateAddress` (only required if `publicIpv4Pool` is specified in `install-config.yaml`)

- `ec2:GetEbsDefaultKmsKeyId`

- `ec2:ModifyInstanceAttribute`

- `ec2:ModifyNetworkInterfaceAttribute`

- `ec2:RevokeSecurityGroupEgress`

- `ec2:RevokeSecurityGroupIngress`

- `ec2:RunInstances`

- `ec2:TerminateInstances`

</div>

<div class="example">

<div class="title">

Required permissions for creating network resources during installation

</div>

- `ec2:AllocateAddress`

- `ec2:AssociateAddress`

- `ec2:AssociateDhcpOptions`

- `ec2:AssociateRouteTable`

- `ec2:AttachInternetGateway`

- `ec2:CreateDhcpOptions`

- `ec2:CreateInternetGateway`

- `ec2:CreateNatGateway`

- `ec2:CreateRoute`

- `ec2:CreateRouteTable`

- `ec2:CreateSubnet`

- `ec2:CreateVpc`

- `ec2:CreateVpcEndpoint`

- `ec2:ModifySubnetAttribute`

- `ec2:ModifyVpcAttribute`

> [!NOTE]
> If you use an existing Virtual Private Cloud (VPC), your account does not require these permissions for creating network resources.

</div>

<div class="example">

<div class="title">

Required Elastic Load Balancing permissions (ELB) for installation

</div>

- `elasticloadbalancing:AddTags`

- `elasticloadbalancing:ApplySecurityGroupsToLoadBalancer`

- `elasticloadbalancing:AttachLoadBalancerToSubnets`

- `elasticloadbalancing:ConfigureHealthCheck`

- `elasticloadbalancing:CreateListener`

- `elasticloadbalancing:CreateLoadBalancer`

- `elasticloadbalancing:CreateLoadBalancerListeners`

- `elasticloadbalancing:CreateTargetGroup`

- `elasticloadbalancing:DeleteLoadBalancer`

- `elasticloadbalancing:DeregisterInstancesFromLoadBalancer`

- `elasticloadbalancing:DeregisterTargets`

- `elasticloadbalancing:DescribeInstanceHealth`

- `elasticloadbalancing:DescribeListeners`

- `elasticloadbalancing:DescribeLoadBalancerAttributes`

- `elasticloadbalancing:DescribeLoadBalancers`

- `elasticloadbalancing:DescribeTags`

- `elasticloadbalancing:DescribeTargetGroupAttributes`

- `elasticloadbalancing:DescribeTargetHealth`

- `elasticloadbalancing:ModifyLoadBalancerAttributes`

- `elasticloadbalancing:ModifyTargetGroup`

- `elasticloadbalancing:ModifyTargetGroupAttributes`

- `elasticloadbalancing:RegisterInstancesWithLoadBalancer`

- `elasticloadbalancing:RegisterTargets`

- `elasticloadbalancing:SetLoadBalancerPoliciesOfListener`

- `elasticloadbalancing:SetSecurityGroups`

> [!IMPORTANT]
> OpenShift Container Platform uses both the ELB and ELBv2 API services to provision load balancers. The permission list shows permissions required by both services. A known issue exists in the AWS web console where both services use the same `elasticloadbalancing` action prefix but do not recognize the same actions. You can ignore the warnings about the service not recognizing certain `elasticloadbalancing` actions.

</div>

<div class="example">

<div class="title">

Required IAM permissions for installation

</div>

- `iam:AddRoleToInstanceProfile`

- `iam:CreateInstanceProfile`

- `iam:CreateRole`

- `iam:DeleteInstanceProfile`

- `iam:DeleteRole`

- `iam:DeleteRolePolicy`

- `iam:GetInstanceProfile`

- `iam:GetRole`

- `iam:GetRolePolicy`

- `iam:GetUser`

- `iam:ListInstanceProfilesForRole`

- `iam:ListRoles`

- `iam:ListUsers`

- `iam:PassRole`

- `iam:PutRolePolicy`

- `iam:RemoveRoleFromInstanceProfile`

- `iam:SimulatePrincipalPolicy`

- `iam:TagInstanceProfile`

- `iam:TagRole`

<div class="note">

<div class="title">

</div>

- If you specify an existing IAM role in the `install-config.yaml` file, the following IAM permissions are not required: `iam:CreateRole`,`iam:DeleteRole`, `iam:DeleteRolePolicy`, and `iam:PutRolePolicy`.

- If you have not created a load balancer in your AWS account, the IAM user also requires the `iam:CreateServiceLinkedRole` permission.

</div>

</div>

<div class="example">

<div class="title">

Required Route 53 permissions for installation

</div>

- `route53:ChangeResourceRecordSets`

- `route53:ChangeTagsForResource`

- `route53:CreateHostedZone`

- `route53:DeleteHostedZone`

- `route53:GetChange`

- `route53:GetHostedZone`

- `route53:ListHostedZones`

- `route53:ListHostedZonesByName`

- `route53:ListResourceRecordSets`

- `route53:ListTagsForResource`

- `route53:UpdateHostedZoneComment`

</div>

<div class="example">

<div class="title">

Required Amazon Simple Storage Service (S3) permissions for installation

</div>

- `s3:CreateBucket`

- `s3:DeleteBucket`

- `s3:GetAccelerateConfiguration`

- `s3:GetBucketAcl`

- `s3:GetBucketCors`

- `s3:GetBucketLocation`

- `s3:GetBucketLogging`

- `s3:GetBucketObjectLockConfiguration`

- `s3:GetBucketPolicy`

- `s3:GetBucketRequestPayment`

- `s3:GetBucketTagging`

- `s3:GetBucketVersioning`

- `s3:GetBucketWebsite`

- `s3:GetEncryptionConfiguration`

- `s3:GetLifecycleConfiguration`

- `s3:GetReplicationConfiguration`

- `s3:ListBucket`

- `s3:PutBucketAcl`

- `s3:PutBucketPolicy`

- `s3:PutBucketTagging`

- `s3:PutEncryptionConfiguration`

</div>

<div class="example">

<div class="title">

S3 permissions that cluster Operators require

</div>

- `s3:DeleteObject`

- `s3:GetObject`

- `s3:GetObjectAcl`

- `s3:GetObjectTagging`

- `s3:GetObjectVersion`

- `s3:PutObject`

- `s3:PutObjectAcl`

- `s3:PutObjectTagging`

</div>

<div class="example">

<div class="title">

Required permissions to delete base cluster resources

</div>

- `autoscaling:DescribeAutoScalingGroups`

- `ec2:DeleteNetworkInterface`

- `ec2:DeletePlacementGroup`

- `ec2:DeleteVolume`

- `elasticloadbalancing:DeleteTargetGroup`

- `elasticloadbalancing:DescribeTargetGroups`

- `iam:DeleteAccessKey`

- `iam:DeleteUser`

- `iam:DeleteUserPolicy`

- `iam:ListAttachedRolePolicies`

- `iam:ListInstanceProfiles`

- `iam:ListRolePolicies`

- `iam:ListUserPolicies`

- `s3:DeleteObject`

- `s3:ListBucketVersions`

- `tag:GetResources`

</div>

<div class="example">

<div class="title">

Required permissions to delete network resources

</div>

- `ec2:DeleteDhcpOptions`

- `ec2:DeleteInternetGateway`

- `ec2:DeleteNatGateway`

- `ec2:DeleteRoute`

- `ec2:DeleteRouteTable`

- `ec2:DeleteSubnet`

- `ec2:DeleteVpc`

- `ec2:DeleteVpcEndpoints`

- `ec2:DetachInternetGateway`

- `ec2:DisassociateRouteTable`

- `ec2:ReleaseAddress`

- `ec2:ReplaceRouteTableAssociation`

> [!NOTE]
> If you use an existing VPC, your account does not require these permissions to delete network resources. Instead, your account only requires the `tag:UntagResources` permission to delete network resources.

</div>

<div class="example">

<div class="title">

Optional permissions for installing a cluster with a custom Key Management Service (KMS) key

</div>

- `kms:CreateGrant`

- `kms:Decrypt`

- `kms:DescribeKey`

- `kms:Encrypt`

- `kms:GenerateDataKey`

- `kms:GenerateDataKeyWithoutPlainText`

- `kms:ListGrants`

- `kms:RevokeGrant`

> [!NOTE]
> If you provide an Amazon Machine Image (AMI) that is encrypted with a customer-managed key, you must provide the `kms:ReEncrypt*` permissions in addition to these permissions.

</div>

<div class="example">

<div class="title">

Required permissions to delete a cluster with shared instance roles

</div>

- `iam:UntagRole`

</div>

<div class="example">

<div class="title">

Required permissions to delete a cluster with shared instance profiles

</div>

- `tag:UntagResources`

</div>

<div class="example">

<div class="title">

Additional IAM and S3 permissions that are required to create manifests

</div>

- `iam:GetUserPolicy`

- `iam:ListAccessKeys`

- `iam:PutUserPolicy`

- `iam:TagUser`

- `s3:AbortMultipartUpload`

- `s3:GetBucketPublicAccessBlock`

- `s3:ListBucket`

- `s3:ListBucketMultipartUploads`

- `s3:PutBucketPublicAccessBlock`

- `s3:PutLifecycleConfiguration`

> [!NOTE]
> If you are managing your cloud provider credentials with mint mode, the IAM user also requires the `iam:CreateAccessKey` and `iam:CreateUser` permissions.

</div>

<div class="example">

<div class="title">

Optional permissions for instance and quota checks for installation

</div>

- `servicequotas:ListAWSDefaultServiceQuotas`

</div>

<div class="example">

<div class="title">

Optional permissions for the cluster owner account when installing a cluster on a shared VPC

</div>

- `sts:AssumeRole`

</div>

<div class="example">

<div class="title">

Required permissions for enabling Bring your own public IPv4 addresses (BYOIP) feature for installation

</div>

- `ec2:DescribePublicIpv4Pools`

- `ec2:DisassociateAddress`

</div>

# Obtaining an AWS Marketplace image

If you are deploying an OpenShift Container Platform cluster using an AWS Marketplace image, you must first subscribe through AWS. Subscribing to the offer provides you with the AMI ID that the installation program uses to deploy compute nodes.

> [!NOTE]
> You should only modify the RHCOS image for compute machines to use an AWS Marketplace image. Control plane machines and infrastructure nodes do not require an OpenShift Container Platform subscription and use the public RHCOS default image by default, which does not incur subscription costs on your AWS bill. Therefore, you should not modify the cluster default boot image or the control plane boot images. Applying the AWS Marketplace image to them will incur additional licensing costs that cannot be recovered.

<div>

<div class="title">

Prerequisites

</div>

- You have an AWS account to purchase the offer. This account does not have to be the same account that is used to install the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Complete the OpenShift Container Platform subscription from the [AWS Marketplace](https://aws.amazon.com/marketplace/fulfillment?productId=59ead7de-2540-4653-a8b0-fa7926d5c845).

</div>
