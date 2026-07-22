<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To ensure OpenShift Container Platform can successfully install and run the cluster in Amazon Web Services (AWS), you must configure an AWS account with the correct identity and permissions before you start the installation.

# Configuring Route 53

To install OpenShift Container Platform, the Amazon Web Services (AWS) account you use must have a dedicated public hosted zone in your Route 53 service. This zone must be authoritative for the domain. The Route 53 service provides cluster DNS resolution and name lookup for external connections to the cluster.

<div>

<div class="title">

Procedure

</div>

1.  Identify your domain, or subdomain, and registrar. You can transfer an existing domain and registrar or obtain a new one through AWS or another source.

    > [!NOTE]
    > If you purchase a new domain through AWS, it takes time for the relevant DNS changes to propagate. For more information about purchasing domains through AWS, see [Registering Domain Names Using Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html) in the AWS documentation.

2.  If you are using an existing domain and registrar, migrate its DNS to AWS. See [Making Amazon Route 53 the DNS Service for an Existing Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html) in the AWS documentation.

3.  Create a public hosted zone for your domain or subdomain. See [Creating a Public Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html) in the AWS documentation.

    Use an appropriate root domain, such as `openshiftcorp.com`, or subdomain, such as `clusters.openshiftcorp.com`.

4.  Extract the new authoritative name servers from the hosted zone records. See [Getting the Name Servers for a Public Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/GetInfoAboutHostedZone.html) in the AWS documentation.

5.  Update the registrar records for the AWS Route 53 name servers that your domain uses. For example, if you registered your domain to a Route 53 service in a different accounts, see the following topic in the AWS documentation: [Adding or Changing Name Servers or Glue Records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-name-servers-glue-records.html#domain-name-servers-glue-records-procedure).

6.  If you are using a subdomain, add its delegation records to the parent domain. This gives Amazon Route 53 responsibility for the subdomain. Follow the delegation procedure outlined by the DNS provider of the parent domain. See [Creating a subdomain that uses Amazon Route 53 as the DNS service without migrating the parent domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingNewSubdomain.html) in the AWS documentation for an example high level procedure.

</div>

## Ingress Operator endpoint configuration for AWS Route 53

Configure Ingress Operator endpoints for OpenShift Container Platform clusters in Amazon Web Services (AWS) GovCloud (US) regions. Verifying these settings helps to ensure that your cluster connects to the correct API endpoints.

If you install in either AWS GovCloud (US) US-West or US-East region, the Ingress Operator uses `us-gov-west-1` region for Route53 and tagging API clients.

The Ingress Operator uses `https://tagging.us-gov-west-1.amazonaws.com` as the tagging API endpoint if a tagging custom endpoint is configured that includes the string 'us-gov-east-1'.

For more information on AWS GovCloud (US) endpoints, see the [Service Endpoints](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-govcloud-endpoints.html) in the AWS documentation about GovCloud (US).

> [!IMPORTANT]
> Private, disconnected installations are not supported for AWS GovCloud when you install in the `us-gov-east-1` region.

<div class="formalpara">

<div class="title">

Example Route 53 configuration

</div>

``` yaml
platform:
  aws:
    region: us-gov-west-1
    serviceEndpoints:
    - name: ec2
      url: https://ec2.us-gov-west-1.amazonaws.com
    - name: elasticloadbalancing
      url: https://elasticloadbalancing.us-gov-west-1.amazonaws.com
    - name: route53
      url: https://route53.us-gov.amazonaws.com
    - name: tagging
      url: https://tagging.us-gov-west-1.amazonaws.com
```

</div>

where:

`https://route53.us-gov.amazonaws.com`
Defaults to `https://route53.us-gov.amazonaws.com` for both AWS GovCloud (US) regions.

`https://tagging.us-gov-west-1.amazonaws.com`
Only the US-West region has endpoints for tagging. Omit this parameter if your cluster is in another region.

# AWS account limits

The OpenShift Container Platform cluster uses several Amazon Web Services (AWS) components, and the default [Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) affect your ability to install OpenShift Container Platform clusters.

If you use certain cluster configurations, deploy your cluster in certain AWS regions, or run multiple clusters from your account, you might need to request additional resources for your AWS account.

The following table summarizes the AWS components whose limits can impact your ability to install and run OpenShift Container Platform clusters.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Component</th>
<th style="text-align: left;">Number of clusters available by default</th>
<th style="text-align: left;">Default AWS limit</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Instance Limits</p></td>
<td style="text-align: left;"><p>Varies</p></td>
<td style="text-align: left;"><p>Varies</p></td>
<td style="text-align: left;"><p>By default, each cluster creates the following instances:</p>
<ul>
<li><p>One bootstrap machine, which is removed after installation</p></li>
<li><p>Three control plane nodes</p></li>
<li><p>Three worker nodes</p></li>
</ul>
<p>These instance type counts are within a new account’s default limit. To deploy more worker nodes, enable autoscaling, deploy large workloads, or use a different instance type, review your account limits to ensure that your cluster can deploy the machines that you need.</p>
<p>In most regions, the worker machines use an <code>m6i.large</code> instance and the bootstrap and control plane machines use <code>m6i.xlarge</code> instances. In some regions, including all regions that do not support these instance types, <code>m5.large</code> and <code>m5.xlarge</code> instances are used instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Elastic IPs (EIPs)</p></td>
<td style="text-align: left;"><p>0 to 1</p></td>
<td style="text-align: left;"><p>5 EIPs per account</p></td>
<td style="text-align: left;"><p>To provision the cluster in a highly available configuration, the installation program creates a public and private subnet for each <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html">availability zone within a region</a>. Each private subnet requires a <a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html">NAT Gateway</a>, and each NAT gateway requires a separate <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html">elastic IP</a>. Review the <a href="https://aws.amazon.com/about-aws/global-infrastructure/">AWS region map</a> to determine how many availability zones are in each region. To take advantage of the default high availability, install the cluster in a region with at least three availability zones. To install a cluster in a region with more than five availability zones, you must increase the EIP limit.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>To use the <code>us-east-1</code> region, you must increase the EIP limit for your account.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p>Virtual Private Clouds (VPCs)</p></td>
<td style="text-align: left;"><p>5</p></td>
<td style="text-align: left;"><p>5 VPCs per region</p></td>
<td style="text-align: left;"><p>Each cluster creates its own VPC.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Elastic Load Balancing (ELB/NLB)</p></td>
<td style="text-align: left;"><p>3</p></td>
<td style="text-align: left;"><p>20 per region</p></td>
<td style="text-align: left;"><p>By default, each cluster creates internal and external network load balancers for the master API server and a single Classic Load Balancer for the router. Deploying more Kubernetes <code>Service</code> objects with type <code>LoadBalancer</code> will create additional <a href="https://aws.amazon.com/elasticloadbalancing/">load balancers</a>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>NAT Gateways</p></td>
<td style="text-align: left;"><p>5</p></td>
<td style="text-align: left;"><p>5 per availability zone</p></td>
<td style="text-align: left;"><p>The cluster deploys one NAT gateway in each availability zone.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Elastic Network Interfaces (ENIs)</p></td>
<td style="text-align: left;"><p>At least 12</p></td>
<td style="text-align: left;"><p>350 per region</p></td>
<td style="text-align: left;"><p>The default installation creates 21 ENIs and an ENI for each availability zone in your region. For example, the <code>us-east-1</code> region contains six availability zones, so a cluster that is deployed in that zone uses 27 ENIs. Review the <a href="https://aws.amazon.com/about-aws/global-infrastructure/">AWS region map</a> to determine how many availability zones are in each region.</p>
<p>Additional ENIs are created for additional machines and ELB load balancers that are created by cluster usage and deployed workloads.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>VPC Gateway</p></td>
<td style="text-align: left;"><p>20</p></td>
<td style="text-align: left;"><p>20 per account</p></td>
<td style="text-align: left;"><p>Each cluster creates a single VPC Gateway for S3 access.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>S3 buckets</p></td>
<td style="text-align: left;"><p>99</p></td>
<td style="text-align: left;"><p>100 buckets per account</p></td>
<td style="text-align: left;"><p>Because the installation process creates a temporary bucket and the registry component in each cluster creates a bucket, you can create only 99 OpenShift Container Platform clusters per AWS account.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Security Groups</p></td>
<td style="text-align: left;"><p>250</p></td>
<td style="text-align: left;"><p>2,500 per account</p></td>
<td style="text-align: left;"><p>Each cluster creates 10 distinct security groups.</p></td>
</tr>
</tbody>
</table>

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

# Creating an IAM user

Before you install OpenShift Container Platform, you must create a secondary IAM administrative user and assign permissions to create the cluster.

Each Amazon Web Services (AWS) account contains a root user account that is based on the email address you used to create the account.

> [!IMPORTANT]
> This is a highly-privileged account, and it is recommended to use it for only initial account and billing configuration, creating an initial set of users, and securing the account.

As you complete the [Creating an IAM User in Your AWS Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) procedure in the Amazon Web Services (AWS) documentation, set the following options:

<div>

<div class="title">

Procedure

</div>

1.  Specify the IAM user name and select `Programmatic access`.

2.  Attach the `AdministratorAccess` policy to ensure that the account has sufficient permission to create the cluster. This policy provides the cluster with the ability to grant credentials to each OpenShift Container Platform component. The cluster grants the components only the credentials that they require.

    > [!NOTE]
    > While it is possible to create a policy that grants the all of the required AWS permissions and attach it to the user, this is not the preferred option. The cluster will not have the ability to grant additional credentials to individual components, so the same credentials are used by all components.

3.  Optional: Add metadata to the user by attaching tags.

4.  Confirm that the user name that you specified is granted the `AdministratorAccess` policy.

5.  Record the access key ID and secret access key values. You must use these values when you configure your local machine to run the installation program.

    > [!IMPORTANT]
    > You cannot use a temporary session token that you generated while using a multi-factor authentication device to authenticate to AWS when you deploy a cluster. The cluster continues to use your current AWS credentials to create AWS resources for the entire life of the cluster, so you must use key-based, long-term credentials.

</div>

# IAM Policies and AWS authentication

You can specify your own IAM roles if required. By default, the installation program creates instance profiles for the bootstrap, control plane, and compute instances with the necessary permissions for the cluster to operate.

> [!NOTE]
> To enable pulling images from the Amazon Elastic Container Registry (ECR) as a postinstallation task in a single-node OpenShift cluster, you must add the `AmazonEC2ContainerRegistryReadOnly` policy to the IAM role associated with the cluster’s control plane role.

However, you can create your own IAM roles and specify them as part of the installation process. You might need to specify your own roles to deploy the cluster or to manage the cluster after installation. For example:

- Your organization’s security policies require that you use a more restrictive set of permissions to install the cluster.

- After the installation, the cluster is configured with an Operator that requires access to additional services.

If you choose to specify your own IAM roles, you can take the following steps:

- Begin with the default policies and adapt as required. For more information, see "Default permissions for IAM instance profiles".

- To create a policy template that is based on the cluster’s activity, see "Using AWS IAM Analyzer to create policy templates".

## Default permissions for IAM instance profiles

To ensure your cluster operates with the correct security permissions in OpenShift Container Platform, review the default IAM instance profiles created by the installation program.

By default, the installation program creates IAM instance profiles for the bootstrap, control plane, and compute instances with the necessary permissions for the cluster to operate.

The following lists specify the default permissions for control plane and compute machines:

<div>

<div class="title">

Default IAM role permissions for control plane instance profiles

</div>

- `ec2:AttachVolume`

- `ec2:AuthorizeSecurityGroupIngress`

- `ec2:CreateSecurityGroup`

- `ec2:CreateTags`

- `ec2:CreateVolume`

- `ec2:DeleteSecurityGroup`

- `ec2:DeleteVolume`

- `ec2:Describe*`

- `ec2:DetachVolume`

- `ec2:ModifyInstanceAttribute`

- `ec2:ModifyVolume`

- `ec2:RevokeSecurityGroupIngress`

- `elasticloadbalancing:AddTags`

- `elasticloadbalancing:AttachLoadBalancerToSubnets`

- `elasticloadbalancing:ApplySecurityGroupsToLoadBalancer`

- `elasticloadbalancing:CreateListener`

- `elasticloadbalancing:CreateLoadBalancer`

- `elasticloadbalancing:CreateLoadBalancerPolicy`

- `elasticloadbalancing:CreateLoadBalancerListeners`

- `elasticloadbalancing:CreateTargetGroup`

- `elasticloadbalancing:ConfigureHealthCheck`

- `elasticloadbalancing:DeleteListener`

- `elasticloadbalancing:DeleteLoadBalancer`

- `elasticloadbalancing:DeleteLoadBalancerListeners`

- `elasticloadbalancing:DeleteTargetGroup`

- `elasticloadbalancing:DeregisterInstancesFromLoadBalancer`

- `elasticloadbalancing:DeregisterTargets`

- `elasticloadbalancing:Describe*`

- `elasticloadbalancing:DetachLoadBalancerFromSubnets`

- `elasticloadbalancing:ModifyListener`

- `elasticloadbalancing:ModifyLoadBalancerAttributes`

- `elasticloadbalancing:ModifyTargetGroup`

- `elasticloadbalancing:ModifyTargetGroupAttributes`

- `elasticloadbalancing:RegisterInstancesWithLoadBalancer`

- `elasticloadbalancing:RegisterTargets`

- `elasticloadbalancing:SetLoadBalancerPoliciesForBackendServer`

- `elasticloadbalancing:SetLoadBalancerPoliciesOfListener`

- `kms:DescribeKey`

</div>

<div>

<div class="title">

Default IAM role permissions for compute instance profiles

</div>

- `ec2:DescribeInstances`

- `ec2:DescribeRegions`

</div>

## Specifying an existing IAM role

Instead of allowing the installation program to create IAM instance profiles with the default permissions, you can use the `install-config.yaml` file to specify an existing IAM role for control plane and compute instances.

<div>

<div class="title">

Prerequisites

</div>

- You have an existing `install-config.yaml` file.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Update `compute.platform.aws.iamRole` with an existing role for the compute machines.

    <div class="formalpara">

    <div class="title">

    Sample `install-config.yaml` file with an IAM role for compute instances

    </div>

    ``` yaml
    compute:
    - hyperthreading: Enabled
      name: worker
      platform:
        aws:
          iamRole: ExampleRole
    ```

    </div>

2.  Update `controlPlane.platform.aws.iamRole` with an existing role for the control plane machines.

    <div class="formalpara">

    <div class="title">

    Sample `install-config.yaml` file with an IAM role for control plane instances

    </div>

    ``` yaml
    controlPlane:
      hyperthreading: Enabled
      name: master
      platform:
        aws:
          iamRole: ExampleRole
    ```

    </div>

3.  Save the file and reference it when installing the OpenShift Container Platform cluster.

    > [!NOTE]
    > To change or update an IAM account after the cluster has been installed, see [RHOCP 4 AWS cloud-credentials access key is expired](https://access.redhat.com/solutions/4284011) (Red Hat Knowledgebase).

</div>

<div>

<div class="title">

Additional resources

</div>

- [Deploying the cluster](ipi/installing-aws-customizations.md#installation-launching-installer_installing-aws-customizations)

</div>

## Using AWS IAM Analyzer to create policy templates

To reduce security risk, you can use AWS IAM Access Analyzer and CloudTrail to generate and apply minimal, fine-grained IAM policies for cluster control plane and compute instance profiles.

The minimal set of permissions that the control plane and compute instance profiles require depends on how the cluster is configured for its daily operation.

One way to determine which permissions the cluster instances require is to use the AWS Identity and Access Management Access Analyzer (IAM Access Analyzer) to create a policy template:

- A policy template contains the permissions the cluster has used over a specified period of time.

- You can then use the template to create policies with fine-grained permissions.

<div>

<div class="title">

Procedure

</div>

1.  Ensure that CloudTrail is enabled. CloudTrail records all of the actions and events in your AWS account, including the API calls that are required to create a policy template. For more information, see the AWS documentation for [working with CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-getting-started.html).

2.  Create an instance profile for control plane instances and an instance profile for compute instances. Be sure to assign each role a permissive policy, such as PowerUserAccess. For more information, see the AWS documentation for [creating instance profile roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).

3.  Install the cluster in a development environment and configure it as required. Be sure to deploy all of applications the cluster will host in a production environment.

4.  Test the cluster thoroughly. Testing the cluster ensures that all of the required API calls are logged.

5.  Use the IAM Access Analyzer to create a policy template for each instance profile. For more information, see the AWS documentation for [generating policies based on the CloudTrail logs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html).

6.  Create and add a fine-grained policy to each instance profile.

7.  Remove the permissive policy from each instance profile.

8.  Deploy a production cluster using the existing instance profiles with the new policies.

    > [!NOTE]
    > You can add [IAM Conditions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) to your policy to make it more restrictive and compliant with your organization security requirements.

</div>

# Supported AWS Marketplace regions

Installing an OpenShift Container Platform cluster using an AWS Marketplace image is available to customers who purchase the offer in North America.

While the offer must be purchased in North America, you can deploy the cluster to any of the following supported paritions:

- Public

- GovCloud

> [!NOTE]
> Deploying a OpenShift Container Platform cluster using an AWS Marketplace image is not supported for the AWS secret regions or China regions.

# Supported AWS regions

You can deploy an OpenShift Container Platform cluster to the following regions.

> [!NOTE]
> Your IAM user must have the permission `tag:GetResources` in the region `us-east-1` to delete the base cluster resources. As part of the AWS API requirement, the OpenShift Container Platform installation program performs various actions in this region.

## AWS public regions

The following AWS public regions are supported:

- `af-south-1` (Cape Town)

- `ap-east-1` (Hong Kong)

- `ap-east-2` (Taipei)

- `ap-northeast-1` (Tokyo)

- `ap-northeast-2` (Seoul)

- `ap-northeast-3` (Osaka)

- `ap-south-1` (Mumbai)

- `ap-south-2` (Hyderabad)

- `ap-southeast-1` (Singapore)

- `ap-southeast-2` (Sydney)

- `ap-southeast-3` (Jakarta)

- `ap-southeast-4` (Melbourne)

- `ap-southeast-5` (Malaysia)

- `ap-southeast-7` (Thailand)

- `ca-central-1` (Central Canada)

- `ca-west-1` (Calgary)

- `eu-central-1` (Frankfurt)

- `eu-central-2` (Zurich)

- `eu-north-1` (Stockholm)

- `eu-south-1` (Milan)

- `eu-south-2` (Spain)

- `eu-west-1` (Ireland)

- `eu-west-2` (London)

- `eu-west-3` (Paris)

- `il-central-1` (Tel Aviv)

- `me-central-1` (UAE)

- `me-south-1` (Bahrain)

- `mx-central-1` (Central Mexico)

- `sa-east-1` (São Paulo)

- `us-east-1` (N. Virginia)

- `us-east-2` (Ohio)

- `us-west-1` (N. California)

- `us-west-2` (Oregon)

## AWS GovCloud regions

The following AWS GovCloud regions are supported:

- `us-gov-west-1`

- `us-gov-east-1`

## AWS SC2S and C2S secret regions

The following AWS secret regions are supported:

- `us-isob-east-1` Secret Commercial Cloud Services (SC2S)

- `us-iso-east-1` Commercial Cloud Services (C2S)

## AWS China regions

The following AWS China regions are supported:

- `cn-north-1` (Beijing)

- `cn-northwest-1` (Ningxia)

<div>

<div class="title">

Additional resources

</div>

- [Quickly install a cluster](ipi/installing-aws-default.md#installing-aws-default)

- [Install a cluster with cloud customizations on installer-provisioned infrastructure](ipi/installing-aws-customizations.md#installing-aws-customizations)

- [Installing a cluster on user-provisioned infrastructure in AWS by using CloudFormation templates](upi/installing-aws-user-infra.md#installing-aws-user-infra)

</div>
