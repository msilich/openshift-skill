<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure RHACS to use the Compliance Operator for compliance reporting and remediation with OpenShift Container Platform clusters. The RHACS Compliance Dashboard displays results from the Compliance Operator.

<a id="compliance-operator-rhacs-overview_compliance-operator-rhacs"></a>

# Compliance Operator overview

The default compliance profiles in RHACS only scan user workloads. The Compliance Operator adds compliance profiles suitable for the rest of the OpenShift Container Platform infrastructure, providing a complete environment scanning solution.

> [!NOTE]
> You must install the Compliance Operator on the cluster where you install Central and on each secured cluster that you want reviewed for compliance.

The Compliance Operator automates the review of many technical implementations and compares them with certain aspects of industry standards, benchmarks, and baselines.

The Compliance Operator is not an auditor. To comply or certify to these various standards, you must engage an authorized auditor such as a Qualified Security Assessor (QSA), Joint Authorization Board (JAB), or other industry-recognized regulatory authority to assess your environment.

The Compliance Operator makes recommendations based on generally available information and practices that relate to such standards and can assist with remediation, but actual compliance is your responsibility. You must work with an authorized auditor to achieve compliance with a standard.

<a id="compliance-operator-install_compliance-operator-rhacs"></a>

# Installing the Compliance Operator

Install the Compliance Operator by using the Software Catalog.

<div>

<div class="title">

Procedure

</div>

1.  In the web console, go to the **Ecosystem** → **Software Catalog** page.

2.  Enter **compliance operator** into the **Filter by keyword** box to find the Compliance Operator.

3.  Select the **Compliance Operator** to view the details page.

4.  Read the information about the Operator, and then click **Install**.

    <div class="important">

    <div class="title">

    </div>

    - If you use the compliance feature, you can schedule your scan by using RHACS to create a compliance scan schedule.

      For more information about scheduling a compliance scan by using the compliance feature, see "Customizing and automating your compliance scans".

    - If you create a scan schedule, you do *not* need to create the `ScanSettingBinding` on the Compliance Operator.

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Understanding the Compliance Operator](https://access.redhat.com/documentation/en-us/openshift_container_platform/latest/html/security_and_compliance/compliance-operator#understanding-compliance-operator)

- [Compliance Operator scans](https://access.redhat.com/documentation/en-us/openshift_container_platform/latest/html/security_and_compliance/compliance-operator#compliance-operator-scans)

- [Compliance Operator release notes](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.21/html/security_and_compliance/compliance-operator#compliance-operator-release-notes)

- [Assessing the profile compliance across clusters](manage-compliance/using-openshift-compliance.md#assessing-the-profile-compliance-across-clusters_using-openshift-compliance)

- [Customizing and automating your compliance scans](manage-compliance/using-openshift-compliance.md#customizing-and-automating-your-compliance-scans_using-openshift-compliance)

</div>
