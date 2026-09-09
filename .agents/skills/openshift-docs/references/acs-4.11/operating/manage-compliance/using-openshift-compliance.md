<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can assess compliance across your entire OpenShift cluster fleet and ensure consistent adherence to the security policies of your organization. If you have Red Hat OpenShift clusters with the Compliance Operator installed, you can manage, view, and schedule Compliance Operator scans in RHACS by using the **Compliance** pages in the RHACS portal. The coverage page shows you the scan results associated with a benchmark and profile in a single interface.

> [!NOTE]
> To access the Compliance menu and API, a user must have at least read permissions for the `Compliance` resource and read permissions for the `Cluster` resource. Additionally, to use email notifiers in the scan schedule configuration, the user requires read permissions for the `Integration` resource.

You can create and manage compliance scan schedules on the schedules page that meet your operational needs. You can only have one schedule that scans the same profile on the same cluster.

By viewing and filtering the scan results on the coverage page, you can monitor the compliance status across all clusters.

<a id="customizing-and-automating-your-compliance-scans_using-openshift-compliance"></a>

# Customizing and automating your compliance scans

By creating a compliance scan schedule, you can customize and automate your compliance scans to align with your operational requirements.

> [!NOTE]
> You can only have one schedule that scans the same profile on the same cluster. This means that you cannot create multiple scan schedules for the same profile on a single cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Compliance Operator version 1.6.0 or later.

  For more information about how to install the Compliance Operator, see "Using the Compliance Operator with Red Hat Advanced Cluster Security for Kubernetes".

  <div class="note">

  <div class="title">

  </div>

  - Currently, the compliance feature and the Compliance Operator evaluate only infrastructure and platform compliance.

  - To use the compliance feature, you must run the Compliance Operator on a Red Hat OpenShift cluster.

  </div>

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Compliance → OpenShift Schedules**.

2.  Click **Create scan schedule**.

3.  In the **Create scan schedule** page, provide the following information:

    - **Name**: Enter a name to identify different compliance scans.

    - **Description**: Specify the reason for each compliance scan.

    - **Schedule**: Adjust the scan schedule to fit your required schedule:

      - **Frequency**: From the drop-down list, select how often you want to run the scan. If you do not select a frequency, `Daily` is selected automatically.

        The following values are associated with how often you want to perform the scan:

        - `Daily`

        - `Weekly`

        - `Monthly`

      - **On day(s)**: From the list, select one or more days of the week on which you want to perform the scan.

        The following values are associated with the days of the week on which you want to perform the scan:

        - `Monday`

        - `Tuesday`

        - `Wednesday`

        - `Thursday`

        - `Friday`

        - `Saturday`

        - `Sunday`

        - `The first of the month`

        - `The middle of the month`

          > [!NOTE]
          > These values are only applicable if you specify the frequency of scan as `Weekly` or `Monthly`.

      - **Time**: Start to type the time in `hh:mm` at which you want to run the scan. From the list that is displayed, select a time.

4.  Click **Next**.

5.  Select one or more healthy clusters that you want to include in the scan.

6.  Click **Next**.

7.  Select one or more profiles that you want to include in the scan. The **Type** column shows the profile type as **Built-in** or **Tailored**. You can include both built-in and tailored profiles in the same scan schedule.

8.  Click **Next**.

9.  Optional: To configure email delivery destinations for manually triggered reports, perform the following steps:

    > [!NOTE]
    > You can add one or more delivery destinations.

    1.  Expand **Add delivery destination**.

    2.  In the **Delivery destination** page, provide the following information:

        - **Email notifier**: Select an email notifier from the drop-down list.

          Optional: To configure the setting for a new email notifier integration, perform the following steps:

          1.  From **Select a notifier** drop-down list, click **Create email notifier**.

          2.  In the **Create email notifier** page, provide the following information:

              - **Integration name**: Enter a unique name for the email notifier. This name helps you identify and manage this specific email notifier configuration.

              - **Email server**: Specify the address of the SMTP server that you want to use to send the emails.

              - **Username**: Enter the username that is required for authentication with the SMTP server. This is often the email address used for sending the emails.

              - **Password**: Enter the password associated with the SMTP username. This password is used for authentication with the SMTP server.

              - **From**: This address usually represents the sender of the emails and is visible to the recipients. This is optional.

              - **Sender**: Enter the name of the sender, which is displayed together with the *From* email address. This name helps recipients identify who sent the email.

              - **Default recipient**: Enter the default email address that should receive the notifications if no specific recipient is specified. This ensures that there is always a recipient for the emails.

              - **Annotation key for recipient**: Specify the annotation key to define a recipient that you want to notify about the policy violations related to a specific deployment or namespace. This is optional.

              - Optional: Select the **Enable unauthenticated SMTP** checkbox, if your SMTP server does not require authentication. This is not recommended due to security reasons.

              - Optional: Select the **Disable TLS certificate validation (insecure)** checkbox, if you want to disable TLS certificate validation. This is not recommended due to security reasons.

              - Optional: In the **Use STARTTLS (requires TLS to be disabled)** field, select the type of STARTTLS for securing the connection to the SMTP server from the drop-down list.

                > [!IMPORTANT]
                > To use this option, you must disable TLS certificate validation.

                The following values are associated with the type of STARTTLS for securing the connection to the SMTP server:

                - `Disabled`

                  Data is not encrypted.

                - `Plain`

                  Encodes username and password in base64.

                - `Login`

                  Sends username and password as separate base64-encoded strings for added security.

          3.  Click **Save integration**.

        - **Distribution list**: Enter one or more comma-separated email addresses of the recipients who should receive the report.

        - **Email template**: The default template is automatically applied.

          Optional: To customize the email subject and body as needed, perform the following steps:

          1.  Click the pencil icon.

          2.  In the **Edit email template** page, provide the following information:

              - **Email subject**: Enter the desired subject line for the email. This subject is displayed in the recipient’s inbox and should clearly indicate the purpose of the email.

              - **Email body**: Compose the text of the email. This is the main content of the email and can include text, placeholders for dynamic content and any formatting necessary to get your message across effectively.

          3.  Click **Apply**.

10. Click **Next**.

11. Review your scan configuration, and then click **Save**.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the RHACS portal, click **Compliance → OpenShift Schedules**.

2.  Select the compliance scan that you have created.

3.  In the **Clusters** section, verify that the operator status is healthy.

4.  Optional: To edit the scan schedule, perform the following steps:

    1.  From the **Actions** drop-down list, which is in the upper right of the page, select **Edit scan schedule**.

    2.  Make your changes.

    3.  Click **Save**.

5.  Optional: To manually send a scan report:

    <div class="note">

    <div class="title">

    </div>

    - You can only send a scan report manually if you have configured an email delivery destination.

    - Compliance reporting is only available for clusters running Compliance Operator version 1.6.0 or later.

    </div>

    - From the **Actions** drop-down list, which is in the upper right of the page, select **Send report**.

      You receive a confirmation that you have requested to send a report.

6.  Optional: To download a scan report, perform the following steps:

    > [!NOTE]
    > Compliance reporting is only available for clusters running Compliance Operator version 1.6.0 or later.

    1.  From the **Actions** drop-down list, which is in the upper right of the page, select **Generate download**.

        You receive a confirmation that the report generation has started.

    2.  Click the **All report jobs** tab.

    3.  Optional: Set **View only my jobs** to on.

    4.  Locate the report job that you created.

    5.  Wait until the download is complete, and then click **Ready for download**.

    6.  Optional: To delete the report job, click the overflow menu ![kebab](../../images/kebab.png) and then select **Delete download**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Using the Compliance Operator with Red Hat Advanced Cluster Security for Kubernetes](../compliance-operator-rhacs.md)

</div>

<a id="analyzing-compliance-scan-schedules_using-openshift-compliance"></a>

## Analyzing compliance scan schedules

By viewing the **Schedules** page, you can analyze the various attributes of the compliance scan schedule that you created.

<div>

<div class="title">

Prerequisites

</div>

- You have created a compliance scan schedule.

  For more information about how to create a compliance scan schedule, see "Customizing and automating your compliance scans".

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Compliance → OpenShift Schedules**.

2.  Optional: To sort the compliance scan schedules in ascending or descending order, select the **Name** column heading.

3.  Select the compliance scan that you have created.

4.  Optional: To sort the cluster health information in ascending or descending order, select a column heading in the **Clusters** section.

5.  Optional: To view the status of the one or more requested jobs from different users:

    1.  Click the **All report jobs** tab.

    2.  You can find the status of the one or more report jobs in the **Status** column.

    3.  Optional: Choose the appropriate method to re-organize the information in the **All report jobs** section:

        - To sort the jobs in ascending or descending order, select the **Completed** column heading.

        - To filter the jobs based on the report run states, select one or more states from the **Filter by report run states** drop-down list.

          The following values are associated with the report run states:

          - `Waiting`

          - `Preparing`

          - `Report ready for download`

          - `Partial report ready for download`

          - `Report successfully sent`

          - `Partial report successfully sent`

          - `Report failed to generate`

        - To view only the jobs that you created, set **View only my jobs** to on.

    4.  Optional: To view the job details associated with a report job, perform the following steps:

        1.  Locate the report job for which you want to view the job details.

        2.  To view the job details, expand the report job.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Customizing and automating your compliance scans](using-openshift-compliance.md#customizing-and-automating-your-compliance-scans_using-openshift-compliance)

</div>

<a id="schedules-page-overview_using-openshift-compliance"></a>

## OpenShift Schedules page overview

The **OpenShift Schedules** page lists all the scan schedules and organizes information into the following groups:

Name  
The unique identifier or title given to each scan schedule.

Schedule  
Indicates the frequency and timing of the scan.

Last scanned  
Indicates the date and time of the most recent scan for that schedule.

Clusters  
Lists the clusters included in the scan schedule.

Profiles  
Identifies the one or more profiles applied in the compliance scan.

My last job status  
Shows the status of your job.

The following values are associated with the job status:

`Waiting`  
The report job is in the queue.

`Preparing`  
The report job is being processed.

`Report ready for download`  
The report is ready and available for download.

`Partial report ready for download`  
A report is partially complete and ready for download.

`Report successfully sent`  
The report was successfully emailed.

`Partial report successfully sent`  
A report is partially complete and was successfully emailed.

`Report failed to generate`  
There was an issue with the report job. Hover to view the error message.

`None`  
There are no recent jobs available.

To view the configuration details and report job status associated with a compliance scan, select the compliance scan you created.

<a id="configuration-details-tab_using-openshift-compliance"></a>

### Configuration details tab

The **Configuration details** tab displays information about the scan schedule information such as the essential parameters, cluster status, associated profiles, and email delivery destinations.

<a id="_parameters_section"></a>

#### Parameters section

The **Parameters** section organizes information into the following groups:

Name  
The unique identifier for the compliance scan.

Description  
Specifies additional information about the compliance scan.

Schedule  
Specifies when the compliance scans should run.

Last scanned  
The timestamp of the last compliance scan performed.

Last updated  
The last date and time that the compliance scan data was modified.

<a id="_clusters_section"></a>

#### Clusters section

The **Clusters** section organizes information into the following groups:

Cluster  
Lists the one or more clusters associated with a compliance scan.

Operator status  
Indicates the current health or operational status of the Operator.

<a id="_profiles_section"></a>

#### Profiles section

The **Profiles** section lists the one or more profiles associated with a compliance scan.

<a id="_delivery_destinations_section"></a>

#### Delivery destinations section

The **Delivery destinations** section organizes information into the following groups:

Email notifier  
Specifies the email notification system or tool set up to distribute reports or alerts.

Distribution list  
Lists the recipients who should receive the notifications or reports.

Email template  
Specifies the email format used for the notifications. You can use the default or customize the email subject and body as needed.

<a id="all-report-jobs-tab_using-openshift-compliance"></a>

### All report jobs tab

The **All report jobs** tab shows the current status and requester for each report job, with completed jobs indicated in the row expansion section.

The report jobs are organized into the following groups:

Completed  
Indicates which report jobs have been finished.

Status  
Displays the current state of each report job.

The following values are associated with the report job status:

`Waiting`  
The report job is in the queue.

`Preparing`  
The report job is being processed.

`Report ready for download`  
The report is ready and available for download.

`Partial report ready for download`  
A report is partially complete and ready for download.

`Report successfully sent`  
The report was successfully emailed.

`Partial report successfully sent`  
A report is partially complete and was successfully emailed.

`Report failed to generate`  
There was an issue with the report job. Hover to view the error message.

`None`  
There are no recent jobs available.

Requester  
Identifies the user or system account that initiated the report job.

<a id="assessing-the-profile-compliance-across-clusters_using-openshift-compliance"></a>

# Assessing the profile compliance across clusters

By viewing the **Coverage** page, you can assess the profile compliance for nodes and platform resources across clusters.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Compliance Operator version 1.6.0 or later.

  For more information about how to install the Compliance Operator, see "Using the Compliance Operator with Red Hat Advanced Cluster Security for Kubernetes".

  <div class="note">

  <div class="title">

  </div>

  - Currently, the compliance feature and the Compliance Operator evaluate only infrastructure and platform compliance.

  - The compliance feature requires the Compliance Operator to be running and does *not* support Amazon Elastic Kubernetes Service (EKS).

  </div>

- You have created a compliance scan schedule.

  For more information about how to create a compliance scan schedule, see "Customizing and automating your compliance scans".

</div>

<div>

<div class="title">

Procedure

</div>

- In the RHACS portal, click **Compliance → OpenShift Coverage**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Using the Compliance Operator with Red Hat Advanced Cluster Security for Kubernetes](../compliance-operator-rhacs.md)

- [Customizing and automating your compliance scans](using-openshift-compliance.md#customizing-and-automating-your-compliance-scans_using-openshift-compliance)

</div>

<a id="coverage-page-overview_using-openshift-compliance"></a>

## OpenShift Coverage page overview

When you view the **Coverage** page and apply a filter to a schedule, all results are filtered accordingly. This filter remains active for all coverage pages until you delete it. You can always view the results based on a single profile.

You can select profiles grouped according to their associated benchmarks by using the toggle group. Tailored profiles appear under a dedicated **Tailored Profiles** tab.

You calculate the compliance percentage based on the number of passed checks in relation to the total number of checks.

> [!NOTE]
> The **Coverage** page now only shows the results of the last scan. If the last scan fails, the Red Hat Advanced Cluster Security for Kubernetes (RHACS) deletes the previous results and you cannot see any information for this scan on the **Coverage** page.

The **Checks** view lists the profile checks and enables you to easily navigate and understand your compliance status.

The profile check information is organized into the following groups:

Check  
The name of the profile check.

Controls  
Shows the various controls associated with each check.

Fail status  
Shows the checks that have failed and require your attention.

Pass status  
Shows the checks that have been successfully passed.

Manual status  
Shows the checks that require a manual review because additional organizational or technical knowledge is required that you cannot automate.

Other status  
Shows the checks with a status other than pass or fail, such as warnings or informational statuses.

Compliance  
Shows the overall compliance status and helps you to ensure that your environment meets the required standards.

> [!NOTE]
> A profile might show different numbers of checks across clusters. This can happen for the following reasons:
>
> - Clusters run different versions of the Compliance Operator. Compliance Operator releases can add or remove rules, which changes the number of checks for a given profile.
>
> - A tailored profile has a different definition on each cluster.
>
> You can expect this behavior. Each cluster’s check results reflect the actual profile definition on that cluster. For more information, see "Understanding tailored profiles in compliance scans".

The **Clusters** view lists the clusters and enables you to effectively monitor and manage your clusters.

The cluster information is organized into the following groups:

Cluster  
The name of the cluster.

Last scanned  
Indicates when the individual clusters were last scanned.

Fail status  
Shows the clusters whose scan has failed and which require your attention.

Pass status  
Shows the clusters that have successfully passed all checks.

Manual status  
Shows the checks that require a manual review because additional organizational or technical knowledge is required that you cannot automate.

Other status  
Shows the clusters that have a status other than pass or fail, such as warnings or informational alerts.

Compliance  
Shows the overall compliance status of your clusters and helps you to ensure that they meet the required standards.

<div>

<div class="title">

Additional resources

</div>

- [Understanding tailored profiles in compliance scans](using-openshift-compliance.md#understanding-tailored-profiles-in-compliance-scans_using-openshift-compliance)

</div>

<a id="monitoring-and-analyzing-the-health-of-your-clusters_using-openshift-compliance"></a>

## Monitoring and analyzing the health of your clusters

By viewing the status of a profile check, you can efficiently monitor and analyze the health of your clusters.

> [!IMPORTANT]
> Wait until the Compliance Operator returns the scan results. It might take a few minutes.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Compliance → OpenShift Coverage**.

2.  Select a cluster to view the details of the individual scans.

3.  Optional: Choose the appropriate method to re-organize the information in the **Coverage** page.

    - To filter the scan results based on a scan schedule, from the drop-down list, select the scan schedule. If you do not select a particular scan schedule, **All scan schedules** is selected automatically.

    - To filter the scan results based on an entity and its attributes, do any of the following tasks:

      > [!IMPORTANT]
      > To select multiple entities and attributes, click the right arrow icon to add another search criteria.

      - To filter the scan results based on a profile check, enter the name of the profile check in the search bar to view the status.

      - To filter the scan results based on cluster attributes, from the drop-down list, select **Cluster**, and then select an attribute. Enter the details of the cluster attribute in the search bar to view the status.

        The following values are associated with the attributes of a cluster:

        - `ID`

        - `Name`

        - `Label`

        - `Type`

        - `Platform Type`

4.  Optional: From the **Compliance status** drop-down list, select one or more statuses by using which you want to filter the scan details.

    The following values are associated with how you want to filter the scan details:

    - `Pass`

    - `Fail`

    - `Error`

    - `Info`

    - `Manual`

    - `Not Applicable`

    - `Inconsistent`

</div>

<a id="compliance-scan-status-overview_using-openshift-compliance"></a>

## Compliance scan status overview

By understanding the compliance scan status, you can manage the overall security posture of your environment.

| Status | Description |
|----|----|
| `Fail` | The compliance check failed. |
| `Pass` | The compliance check passed. |
| `Not Applicable` | Skipped the compliance check because it was not applicable. |
| `Info` | The compliance check gathered data, but RHACS could not make a pass or fail determination. |
| `Error` | The compliance check failed due to a technical issue. |
| `Manual` | Manual intervention is required to ensure compliance. |
| `Inconsistent` | The compliance scan data is inconsistent, and requires closer inspection and targeted resolution. |

<a id="understanding-tailored-profiles-in-compliance-scans_using-openshift-compliance"></a>

# Understanding tailored profiles in compliance scans

Tailored profiles are custom compliance profiles that you create in the Compliance Operator and use in Red Hat Advanced Cluster Security for Kubernetes (RHACS). Tailored profiles build on standard compliance profiles provided by the Compliance Operator, such as Center for Internet Security (CIS), National Institute of Standards and Technology (NIST), Payment Card Industry Data Security Standard (PCI-DSS), and Security Technical Implementation Guide (STIG) benchmarks. You can use tailored profiles to extend existing benchmarks and customize the combination of rules that you are using.

You create tailored profiles at the cluster level by using `TailoredProfile` custom resources (CRs), then use RHACS to schedule and manage scans across multiple clusters.

> [!NOTE]
> RHACS does not currently create, copy, or synchronize tailored profiles between clusters. You must create the `TailoredProfile` CR on each cluster where you want to run the profile.

<a id="supported-tailored-profile-types_using-openshift-compliance"></a>

## Supported tailored profile types

RHACS supports all `TailoredProfile` CR configurations available in the Compliance Operator.

| Type | Description |
|----|----|
| Profile extension | Profiles that extend a single standard profile by using the `extends` field |
| Disabled rules | Profiles that exclude specific compliance checks by using the `disableRules` field |
| Enabled rules | Profiles that explicitly enable compliance checks by using the `enableRules` field |
| Manual rules | Profiles that mark specific checks as requiring manual verification by using the `manualRules` field |
| Modified values | Profiles that override default values for compliance checks by using the `setValues` field |
| Custom rules | Profiles that include organization-specific checks by using the Compliance Operator `CustomRule` object |
| Profile combination | Profiles that combine checks from more than one standard profile by using `extends` entries or rule combinations |

Tailored profile types

<a id="tailored-profile-workflow_using-openshift-compliance"></a>

## Tailored profile workflow

Tailored profiles integrate with RHACS through the following workflow:

1.  You create `TailoredProfile` CRs in the Compliance Operator on each target cluster. The `TailoredProfile` resource specifies which standard profile to extend, which rules to enable or disable, and any custom values to apply.

2.  RHACS automatically discovers tailored profiles available on secured clusters. Tailored profiles appear in the RHACS compliance interface with standard profiles.

3.  From the RHACS portal, you select tailored profiles and schedule scans across one or more clusters. RHACS creates the necessary `ScanSettingBinding` resources on target clusters to start the scans.

4.  RHACS collects scan results from all clusters and aggregates them in the **Coverage** dashboard. Results from tailored profiles appear in a dedicated **Tailored Profiles** tab, separate from standard profile results.

<div>

<div class="title">

Additional resources

</div>

- [Creating a new tailored profile](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html-single/security_and_compliance/index#compliance-new-tailored-profiles_compliance-tailor)

- [Adding custom labels and annotations to a `CustomRule` object](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/security_and_compliance/compliance-operator#compliance-operator-checkresult-custom-metadata-configure-customrules_compliance-operator-checkresult-metadata)

</div>

<a id="tailored-profiles-appearance_using-openshift-compliance"></a>

## How tailored profiles appear in RHACS

Tailored profiles behave like built-in profiles in most respects, with the following differences:

Scan schedules  
When you create or edit a scan schedule, the profile selection table includes a **Type** column that displays **Built-in** for built-in profiles and **Tailored** for tailored profiles. You can select both types together in the same scan schedule.

CSV reports  
In downloaded CSV compliance reports, the **Profile type** column displays **Tailored Profile** instead of **Profile**. The **Control Reference** column displays **N/A** for tailored profiles because tailored profile names do not map to a known compliance standard.

Coverage page  
On the **Coverage** page, tailored profiles appear under a dedicated **Tailored Profiles** tab.

> [!NOTE]
> Tailored profiles with the same name can produce different check counts across clusters. Because each cluster manages its own tailored profile as a Kubernetes resource, they can differ in several ways:
>
> - Different sets of enabled or disabled rules.
>
> - Extending different base profiles.
>
> - Extending the same base profile but on clusters running different Compliance Operator versions, which can cause the base profile itself to contain different rules.
>
> You can expect this behavior. Each cluster’s check results reflect the actual tailored profile definition on that cluster.

<a id="rhacs-compliance-tailored-profile-troubleshooting_using-openshift-compliance"></a>

## Troubleshooting tailored profiles in RHACS

If tailored profiles do not appear in RHACS, check the status of the tailored profile.

<div>

<div class="title">

Procedure

</div>

- Check the status of the tailored profile:

  ``` terminal
  $ oc get tailoredprofile <profile_name> -n openshift-compliance -o yaml
  ```

  Look for the `status.state` field. A ready profile shows `status.state: READY`.

</div>

<a id="rhacs-compliance-tailored-profile-requirements_using-openshift-compliance"></a>

## Tailored profile requirements and support

Tailored profiles in Red Hat Advanced Cluster Security for Kubernetes (RHACS) have specific version requirements and naming conventions. Understanding these requirements helps you plan your compliance scanning strategy across multiple clusters and OpenShift Container Platform versions.

Tailored profiles are supported in RHACS version 4.11 and later. For information about Compliance Operator and OpenShift Container Platform version support, see the Compliance Operator release notes.

Compliance benchmark content can change between Compliance Operator versions. The same tailored profile might produce different results on clusters running different versions of the Operator. This is a known limitation related to upstream compliance content changes, not a RHACS limitation.

For details about compliance content changes, see the Compliance Operator release notes.

<div>

<div class="title">

Additional resources

</div>

- [Creating tailored profiles in the Compliance Operator](https://docs.openshift.com/container-platform/latest/security/compliance_operator/co-scans/compliance-operator-tailor.html)

- [Understanding the Compliance Operator](https://docs.openshift.com/container-platform/latest/security/compliance_operator/co-concepts/compliance-operator-understanding.html)

- [Understanding compliance scan results](https://docs.openshift.com/container-platform/latest/security/compliance_operator/co-scans/compliance-scans.html)

- [Troubleshooting the Compliance Operator](https://docs.openshift.com/container-platform/latest/security/compliance_operator/co-scans/compliance-operator-troubleshooting.html)

</div>
