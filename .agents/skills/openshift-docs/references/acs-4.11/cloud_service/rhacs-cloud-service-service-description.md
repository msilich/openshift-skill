<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

<a id="introduction-to-rhacs_access-policy-service-description"></a>

# Introduction to RHACS

Red Hat Advanced Cluster Security for Kubernetes (RHACS) is an enterprise-ready, Kubernetes-native container security solution that helps you build, deploy, and run cloud-native applications more securely.

Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service) provides Kubernetes-native security as a service. With RHACS Cloud Service, Red Hat maintains, upgrades, and manages your Central services.

Central services include the user interface (UI), data storage, RHACS application programming interface (API), and image scanning capabilities. You deploy your Central service through the [Red Hat Hybrid Cloud Console.](https://console.redhat.com/) When you create a new ACS instance, Red Hat creates your individual control plane for RHACS.

RHACS Cloud Service allows you to secure self-managed clusters that communicate with a Central instance. The clusters you secure, called Secured Clusters, are managed by you, and not by Red Hat. Secured Cluster services include optional vulnerability scanning services, admission control services, and data collection services used for runtime monitoring and compliance. You install Secured Cluster services on any OpenShift or Kubernetes cluster you want to secure.

<a id="architecture_access-policy-service-description"></a>

# Architecture

RHACS Cloud Service is hosted on Amazon Web Services (AWS) over two regions, eu-west-1 and us-east-1, and uses the network access points provided by the cloud provider. Each tenant from RHACS Cloud Service uses highly-available egress proxies and is spread over 3 availability zones. For more information about RHACS Cloud Service system architecture and components, see [Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service) architecture](acscs-architecture.md#acscs-architecture-overview_acscs-architecture).

<a id="billing_access-policy-service-description"></a>

# Billing

Customers can purchase a RHACS Cloud Service subscription on the Amazon Web Services (AWS) marketplace. The service cost is charged hourly per secured core, or vCPU of a node belonging to a secured cluster.

<div class="example">

<div class="title">

Subscription cost example

</div>

If you have established a connection to two secured clusters, each with 5 identical nodes with 8 vCPUs (such as Amazon EC2 m7g.2xlarge), the total number of secured cores is 80 (2 x 5 x 8 = 80).

</div>

<a id="security-and-compliance_access-policy-service-description"></a>

# Security and compliance

All RHACS Cloud Service data in the Central instance is encrypted in transit and at rest. The data is stored in secure storage with full replication and high availability together with regularly-scheduled backups. RHACS Cloud Service is available through cloud data centers that ensure optimal performance and the ability to meet data residency requirements.

<a id="cloud-info-security_access-policy-service-description"></a>

## Information security guidelines, roles, and responsibilities

Red Hat’s information security guidelines, aligned with the [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework), are approved by executive management. Red Hat maintains a dedicated team of globally-distributed certified information security professionals. See the following resources:

- [FIRST: RH-ISIRT team](https://www.first.org/members/teams/rh-isirt)

- [TF-CSIRT: RH-ISIRT team](https://www.trusted-introducer.org/directory/teams/rh-isirt.html)

Red Hat has strict internal policies and practices to protect our customers and their businesses. These policies and practices are confidential. In addition, we comply with all applicable laws and regulations, including those related to data privacy.

Red Hat’s information security roles and responsibilities are not managed by third parties.

Red Hat maintains an ISO 27001 certification for our corporate information security management system (ISMS), which governs how all of our people work, corporate endpoint devices, and authentication and authorization practices. We have taken a standardized approach to this through the implementation of the Red Hat Enterprise Security Standard (ESS) to all infrastructure, products, services and technology that Red Hat employs. A copy of the ESS is available upon request.

RHACS Cloud Service runs on an instance of OpenShift Dedicated hosted on Amazon Web Services (AWS). OpenShift Dedicated is compliant with ISO 27001, ISO 27017, ISO 27018, PCI DSS, SOC 2 Type 2, and HIPAA. Strong processes and security controls are aligned with industry standards to manage information security.

RHACS Cloud Service follows the same security principles, guidelines, processes and controls defined for OpenShift Dedicated. These certifications demonstrate how our services platform, associated operations, and management practices align with core security requirements. We meet many of these requirements by following solid Secure Software Development Framework (SSDF) practices as defined by NIST, including build pipeline security. Implementation of SSDF controls are implemented via our Secure Software Management Lifecycle (SSML) for all products and services.

Red Hat’s proven and experienced global site reliability engineering (SRE) team is available 24x7 and proactively manages the cluster life cycle, infrastructure configuration, scaling, maintenance, security patching, and incident response as it relates to the hosted components of RHACS Cloud Service. The Red Hat SRE team is responsible for managing HA, uptime, backups, restore, and security for the RHACS Cloud Service control plane. RHACS Cloud Service comes with a 99.95% availability SLA and 24x7 RH SRE support by phone or chat.

You are responsible for use of the product, including implementation of policies, vulnerability management, and deployment of secured cluster components within your OpenShift Container Platform environments. The Red Hat SRE team manages the control plane that contains tenant data in line with the compliance frameworks noted previously, including:

- All Red Hat SRE access the data plane clusters through the backplane which enables audited access to the cluster

- Red Hat SRE only deploys images from the Red Hat registry. All content posted to the Red Hat registry goes through rigorous checks. These images are the same images available to self-managed customers.

- Each tenant has their own individual mTLS CA, which encrypts data in-transit, enabling multi-tenant isolation. Additional isolation is provided via SELinux controls namespaces and network policies.

- Each tenant has their own instance of the RDS database.

All Red Hat SREs and developers go through rigorous Secure Development Lifecycle training.

For more information, see the following resources:

- [Red Hat Site Reliability Engineering (SRE) services](https://www.redhat.com/en/resources/site-reliability-engineering-services-datasheet)

- [Red Hat OpenShift Dedicated](https://www.redhat.com/en/resources/openshift-dedicated-datasheet)

- [An Overview of Red Hat’s Secure Development Lifecycle (SDL) practices](https://access.redhat.com/articles/red_hat_sdl)

<a id="sdlc-security_access-policy-service-description"></a>

## Systems development lifecycle security

Red Hat follows secure development lifecycle practices. Red Hat Product Security practices are aligned with the Open Web Application Security Project (OWASP) and ISO12207:2017 wherever it is feasible. Red Hat covers OWASP project recommendations along with other secure software development practices to increase the general security posture of our products. OWASP project analysis is included in Red Hat’s automated scanning, security testing, and threat models, as the OWASP project is built based on selected CWE weaknesses. Red Hat monitors weaknesses in our products to address issues before they are exploited and become vulnerabilities.

For more information, see the following resources:

- [Red Hat Software Development Life Cycle practices](https://access.redhat.com/security_testing_sdl_practice)

- [Security by design: Security principles and threat modeling](https://www.redhat.com/en/blog/security-design-security-principles-and-threat-modeling)

Applications are scanned regularly and the container scan results of the product are available publicly. For example, on the Red Hat Ecosystem Catalog site, you can select a component image such as `rhacs-main` and click the **Security** tab to see the health index and the status of security updates.

As part of Red Hat’s policy, a support policy and maintenance plan is issued for any third-party components we depend on that go to end-of-life.

<a id="access-control_access-policy-service-description"></a>

# Access control

User accounts are managed with role-based access control (RBAC). See [Managing RBAC in Red Hat Advanced Cluster Security for Kubernetes](../operating/manage-user-access/manage-role-based-access-control-3630.md) for more information. Red Hat site reliability engineers (SREs) have access to Central instances. Access is controlled with OpenShift RBAC. Credentials are instantly revoked upon termination.

<a id="authentication-provider_access-policy-service-description"></a>

## Authentication provider

When you create a Central instance using [Red Hat Hybrid Cloud Console](https://console.redhat.com/), authentication for the cluster administrator is configured as part of the process. Customers must manage all access to the Central instance as part of their integrated solution. For more information about the available authentication methods, see [Understanding authentication providers](../operating/manage-user-access/understanding-authentication-providers.md).

The default identity provider in RHACS Cloud Service is Red Hat Single Sign-On (SSO). Authorization rules are set up to provide administrator access to the user who created the RHACS Cloud Service and to users who are marked as organization administrators in Red Hat SSO. The `admin` login is disabled for RHACS Cloud Service by default and can only be enabled temporarily by SREs. For more information about authentication using Red Hat SSO, see [Default access to the ACS Console](getting-started-rhacs-cloud-ocp.md#default-access-acs-console_getting-started-rhacs-cloud-ocp).

<a id="passwords_access-policy-service-description"></a>

## Password management

Red Hat’s password policy requires the use of a complex password. Passwords must contain at least 14 characters and at least three of the following character classes:

- Base 10 digits (0 to 9)

- Upper case characters (A to Z)

- Lower case characters (a to z)

- Punctuation, spaces, and other characters

Most systems require two-factor authentication.

Red Hat follows best password practices according to [NIST guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html).

<a id="remote-access_access-policy-service-description"></a>

## Remote access

Access for remote support and troubleshooting is strictly controlled through implementation of the following guidelines:

- Strong two-factor authentication for VPN access

- A segregated network with management and administrative networks requiring additional authentication through a bastion host

- All access and management is performed over encrypted sessions

Our customer support team offers Bomgar as a remote access solution for troubleshooting. Bomgar sessions are optional, must be initiated by the customer, and can be monitored and controlled.

To prevent information leakage, logs are shipped to SRE through our security information and event management (SIEM) application, Splunk.

<a id="access-restriction_access-policy-service-description"></a>

## Central access restriction by IP addresses and CIDR ranges

Restricting access to Central ensures that only traffic from trusted IP addresses can reach the security policy enforcement point, thereby strengthening the overall security posture.

To request restricted access to Central, go to the [Red Hat Customer Portal](https://access.redhat.com/support) page. From the Customer Portal, submit a support case requesting the restriction of access to Central. Be sure to provide the list of trusted IP addresses and CIDR ranges. The maximum number of IP addresses and CIDR ranges is 55.

<a id="cloud-svc-compliance_access-policy-service-description"></a>

# Compliance

RHACS Cloud Service is certified across key global standards, ensuring top-tier security, compliance, and data protection for your business.

The following table outlines certifications for RHACS Cloud Service.

| Compliance         | RHACS Cloud Service on Kubernetes |
|--------------------|-----------------------------------|
| ISO/IEC 27001:2022 | Yes                               |
| ISO/IEC 27017:2015 | Yes                               |
| ISO/IEC 27018:2019 | Yes                               |
| PCI DSS 4.0        | Yes                               |
| SOC 2 Type 2       | Yes                               |
| SOC 2 Type 3       | Yes                               |

Security and control certifications for RHACS Cloud Service

<a id="data-protection_access-policy-service-description"></a>

# Data protection

Red Hat provides data protection by using various methods, such as logging, access control, and encryption.

<a id="data-storage-media-protection_access-policy-service-description"></a>

## Data storage media protection

To protect our data and client data from risk of theft or destruction, Red Hat employs the following methods:

- access logging

- automated account termination procedures

- application of the principle of least privilege

Data is encrypted in transit and at rest using strong data encryption following NIST guidelines and Federal Information Processing Standards (FIPS) where possible and practical. This includes backup systems.

RHACS Cloud Service encrypts data at rest within the Amazon Relational Database Service (RDS) database by using AWS-managed Key Management Services (KMS) keys. All data between the application and the database, together with data exchange between the systems, are encrypted in transit.

<a id="data-retention-destruction_access-policy-service-description"></a>

### Data retention and destruction

Records, including those containing personal data, are retained as required by law. Records not required by law or a reasonable business need are securely removed. Secure data destruction requirements are included in operating procedures, using military grade tools. In addition, staff have access to secure document destruction facilities.

<a id="encryption_access-policy-service-description"></a>

### Encryption

Red Hat uses [AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) which are rotated by AWS each year. For information on the use of keys, see [AWS KMS key management](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.Keys.html). For more information about RDS, see [Amazon RDS Security](https://aws.amazon.com/rds/features/security).

<a id="multi-tenancy_access-policy-service-description"></a>

### Multi-tenancy

RHACS Cloud Service isolates tenants by namespace on OpenShift Container Platform. SELinux provides additional isolation. Each customer has a unique RDS instance.

<a id="data-ownership_access-policy-service-description"></a>

### Data ownership

Customer data is stored in an encrypted RDS database not available on the public internet. Only Site Reliability Engineers (SREs) have access to it, and the access is audited.

Every RHACS Cloud Service system comes integrated with Red Hat external SSO. Authorization rules are set up to provide administrator access to the user created the Cloud Service and to users who are marked as organization administrators in Red Hat SSO. The admin login is disabled for RHACS Cloud Service by default and can only be temporarily enabled by SREs.

Red Hat collects information about the number of secured clusters connected to RHACS Cloud Service and the usage of features. Metadata generated by the application and stored in the RDS database is owned by the customer. Red Hat only accesses data for troubleshooting purposes and with customer permission. Red Hat access requires audited privilege escalation.

Upon contract termination, Red Hat can perform a secure disk wipe upon request. However, we are unable to physically destroy media (cloud providers such as AWS do not provide this option).

To secure data in case of a breach, you can perform the following actions:

- Disconnect all secured clusters from RHACS Cloud Service immediately using the cluster management page.

- Immediately disable access to the RHACS Cloud Service by using the Access Control page.

- Immediately delete your RHACS instance, which also deletes the RDS instance.

Any AWS RDS (data store) specific access modifications would be implemented by the RHACS Cloud Service SRE engineers.

<a id="metrics-and-logging_access-policy-service-description"></a>

# Metrics and Logging

<a id="service-metrics_access-policy-service-description"></a>

## Service metrics

Service metrics are internal only. Red Hat provides and maintains the service at the agreed upon level. Service metrics are accessible only to authorized Red Hat personnel. For more information, see [PRODUCT APPENDIX 4 RED HAT ONLINE SERVICES](https://www.redhat.com/licenses/Appendix_4_Red_Hat_Online_Services_20221213.pdf).

<a id="customer-metrics_access-policy-service-description"></a>

## Customer metrics

Core usage capacity metrics are available either through [Subscription Watch](https://access.redhat.com/articles/subscription-watch) or the [Subscriptions page](https://console.redhat.com/beta/application-services/subscriptions/acs).

<a id="service-logging_access-policy-service-description"></a>

## Service logging

System logs for all components of the Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service) are internal and available only to Red Hat personnel. Red Hat does not provide user access to component logs. For more information, see [PRODUCT APPENDIX 4 RED HAT ONLINE SERVICES](https://www.redhat.com/licenses/Appendix_4_Red_Hat_Online_Services_20221213.pdf).

<a id="updates-and-upgrades_access-policy-service-description"></a>

# Updates and Upgrades

Red Hat makes a commercially reasonable effort to notify customers prior to updates and upgrades that impact service. The decision regarding the need for a Service update to the Central instance and its timing is the sole responsibility of Red Hat.

Customers have no control over when a Central service update occurs. For more information, see [PRODUCT APPENDIX 4 RED HAT ONLINE SERVICES](https://www.redhat.com/licenses/Appendix_4_Red_Hat_Online_Services_20221213.pdf). Upgrades to the version of Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service) are considered part of the service update. Upgrades are transparent to the customer and no connection to any update site is required.

Customers are responsible for timely RHACS Secured Cluster services upgrades that are required to maintain compatibility with RHACS Cloud Service.

Red Hat recommends enabling automatic upgrades for Secured Clusters that are connected to RHACS Cloud Service.

See the [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053) for more information about upgrade versions.

<a id="availability_access-policy-service-description"></a>

# Availability

Availability and disaster avoidance are extremely important aspects of any security platform. Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service) provides numerous protections against failures at multiple levels. To account for possible cloud provider failures, Red Hat established multiple availability zones.

<a id="backup-disaster-recovery_access-policy-service-description"></a>

## Backup and disaster recovery

The RHACS Cloud Service Disaster Recovery strategy includes backups of database and any customization. This also applies to customer data stored in the Central database. Recovery time varies based on the number of appliances and database sizes; however, because the appliances can be clustered and distributed, the RTO can be reduced upfront with proper architecture planning.

All snapshots are created using the appropriate cloud provider snapshot APIs, encrypted and then uploaded to secure object storage, which for Amazon Web Services (AWS) is an S3 bucket.

- Red Hat does not commit to a Recovery Point Objective (RPO) or Recovery Time Objective (RTO). For more information, see [PRODUCT APPENDIX 4 RED HAT ONLINE SERVICES](https://www.redhat.com/licenses/Appendix_4_Red_Hat_Online_Services_20221213.pdf).

- Site Reliability Engineering performs backups only as a precautionary measure. They are stored in the same region as the cluster.

- Customers should deploy multiple availability zone Secured Clusters with workloads that follow Kubernetes best practices to ensure high availability within a region.

Disaster recovery plans are exercised annually at a minimum. A Business Continuity Management standard and guideline is in place so that the BC lifecycle is consistently followed throughout the organization. This policy includes a requirement for testing at least annually, or with major change of functional plans. Review sessions are required to be conducted after any plan exercise or activation, and plan updates are made as needed.

Red Hat has generator backup systems. Our IT production systems are hosted in a Tier 3 data center facility that has recurring testing to ensure redundancy is operational. They are audited yearly to validate compliance.

<a id="cloud-getting-support_access-policy-service-description"></a>

# Getting support for RHACS Cloud Service

If you experience difficulty with a procedure described in this documentation, or with RHACS Cloud Service in general, visit the [Red Hat Customer Portal](https://access.redhat.com/support).

From the Customer Portal, you can perform the following actions:

- Search or browse through the Red Hat Knowledgebase of articles and solutions relating to Red Hat products.

- Submit a support case to Red Hat Support.

- Access other product documentation.

To identify issues with your cluster, you can use Insights in RHACS Cloud Service. Insights provides details about issues and, if available, information on how to solve a problem.

<a id="cloud-service-removal_access-policy-service-description"></a>

# Service removal

You can delete RHACS Cloud Service using the default delete operations from the [Red Hat Hybrid Cloud Console](https://console.redhat.com/). Deleting the RHACS Cloud Service Central instance automatically removes all RHACS components. Deleting is not reversible.

<a id="pricing_access-policy-service-description"></a>

# Pricing

For information about subscription fees, see [PRODUCT APPENDIX 4 RED HAT ONLINE SERVICES](https://www.redhat.com/licenses/Appendix_4_Red_Hat_Online_Services_20221213.pdf).

<a id="service-level-agreement_access-policy-service-description"></a>

# Service Level Agreement

For more information about the Service Level Agreements (SLAs) offered for Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service), see [PRODUCT APPENDIX 4 RED HAT ONLINE SERVICES](https://www.redhat.com/licenses/Appendix_4_Red_Hat_Online_Services_20221213.pdf).
