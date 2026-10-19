<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The compliance feature ensures that your Kubernetes clusters adhere to industry standards and regulatory requirements through automated compliance checks.

<a id="openshift-infrastructure-compliance_compliance-feature-overview"></a>

# OpenShift infrastructure compliance

OpenShift infrastructure compliance, formerly known as Compliance 2.0, summarizes compliance information in a single interface after scheduled scans by using the Compliance Operator.

<div class="important">

<div class="title">

</div>

- If you have Red Hat OpenShift clusters with the Compliance Operator installed, you can create and manage compliance scan schedules directly in RHACS on the schedules page. The coverage page shows you the scan results associated with a benchmark and profile in a single interface.

- You can now use the new OpenShift infrastructure compliance feature to assess compliance across your entire OpenShift cluster fleet and ensure consistent adherence to the security policies of your organization. RHACS now generates reports even if some clusters in a scheduled scan fail, so that you can keep visibility into the compliance status of successfully scanned clusters without data gaps.

  For more information, see "Using OpenShift compliance".

</div>

RHACS also supports tailored profiles from the Compliance Operator, so that you can customize existing benchmarks to match the requirements of your organization. You can schedule scans that use these profiles directly from the RHACS portal.

For more information, see "Understanding tailored profiles in compliance scans".

> [!NOTE]
> To access the Compliance menu and API, a user must have at least read permissions for the `Compliance` resource and read permissions for the `Cluster` resource. Additionally, to use email notifiers in the scan schedule configuration, the user requires read permissions for the `Integration` resource.

<div>

<div class="title">

Additional resources

</div>

- [Using OpenShift compliance](using-openshift-compliance.md)

- [Understanding tailored profiles in compliance scans](using-openshift-compliance.md#understanding-tailored-profiles-in-compliance-scans_using-openshift-compliance)

</div>

<a id="dashboard_compliance-feature-overview"></a>

# Dashboard (deprecated)

The compliance dashboard, formerly known as Compliance 1.0, summarizes compliance information from all clusters and covers workload and infrastructure compliance. The dashboard is deprecated in RHACS 4.8 and will be removed in a future release.

> [!IMPORTANT]
> By running a compliance scan in RHACS, you can monitor the entire Kubernetes infrastructure and workloads and ensure that they meet the required standards. You can use the compliance dashboard for filtering and detailed reporting.

<a id="compliance-assessment-and-reporting-by-using-rhacs_compliance-feature-overview"></a>

# Compliance assessment and reporting by using RHACS

On the dashboard page, you can assess and report on the compliance of your containerized infrastructure and workloads with the applicable technical controls from a range of security and regulatory frameworks.

You can run compliance scans based on the following industry standards:

- **Center for Internet Security (CIS) Benchmarks** for **Kubernetes**

- **Health Insurance Portability and Accountability Act** (HIPAA)

- **National Institute of Standards and Technology (NIST) Special Publication 800-190**

- **NIST Special Publication 800-53**

- **Payment Card Industry Data Security Standard** (PCI DSS)

- **OpenShift Compliance Operator Profiles**

  The Compliance Operator evaluates the compliance of both the OpenShift Container Platform Kubernetes API resources and the nodes running the cluster. There are several profiles available as part of the Compliance Operator installation.

  For more information about the available profiles, see "Supported compliance profiles".

By scanning your environment based on these standards, you can:

- Evaluate your infrastructure for regulatory compliance.

- Harden your Kubernetes orchestrator.

- Understand and manage the overall security posture of your environment.

- Get a detailed overview of the compliance status of clusters, namespaces, and nodes.

<div>

<div class="title">

Additional resources

</div>

- [Supported compliance profiles](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html-single/security_and_compliance/index#compliance-operator-supported-profiles)

</div>

<a id="workload-compliance-for-non-openshift-clusters_compliance-feature-overview"></a>

# Workload compliance for non-OpenShift clusters

For non-OpenShift clusters, Red Hat Advanced Cluster Security for Kubernetes (RHACS) provides workload compliance through standard and custom security policies rather than through the default compliance profiles that earlier releases provided.

RHACS previously provided default compliance profiles to scan user workloads on non-OpenShift clusters. RHACS no longer includes this functionality.

You can use standard RHACS security policies to replace most of the checks that earlier compliance scans performed. Tag specific security policies with the relevant compliance benchmark controls. The RHACS policy engine then continuously evaluates your workloads against these tagged policies and reports a pass or fail result.

<div>

<div class="title">

Additional resources

</div>

- [About security policies](../manage_security_policies/about-security-policies.md)

</div>
