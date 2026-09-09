<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure policies in Red Hat Advanced Cluster Security (RHACS) to detect and alert on sensitive file accesses or operations for containerized workloads or cluster nodes. Define criteria to identify high risk accesses of sensitive files, such as opening a file for writing, file deletion, or permission changes. You can configure the system to send notifications when this activity occurs, and set enforcement actions to automatically block noncompliant workloads.

> [!IMPORTANT]
> File activity monitoring is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> Policy criteria might change in future releases as this feature approaches General Availability. If you test this feature in Technology Preview, you might need to perform manual updates before you upgrade. Follow the instructions in the relevant KCS article to maintain your configurations in future versions.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<a id="detection-of-unauthorized-file-modifications_file-activity-monitoring"></a>

# Detection of unauthorized file modifications

Protect your infrastructure by configuring RHACS policies that monitor sensitive file activity. Policies can check custom file paths identified with wildcard patterns. The unified file path criterion that replaces separate effective path and actual path fields enables you to define flexible monitoring rules. These flexible rules can match your specific security and compliance requirements, from individual critical files to entire directory trees. You can detect unauthorized modifications and host breakouts even when attackers try to obscure their targets by using symbolic links or volume mounts.

When creating policies for unauthorized file modifications, you specify file paths by using glob pattern syntax. For example, you add `/etc/*.conf` or `/var/log/app/**/*.log` in a single file path field during policy creation. The file activity monitoring system evaluates violations against both the effective path, which is how the process views the file inside the container, and the actual path, which is the true location on the host filesystem. This dual matching ensures comprehensive detection while violation records display both path values for forensic investigation.

You can combine file path patterns with process filtering criteria to create precise policies that reduce false positives from legitimate system operations. Process filters suppress violations when expected processes such as package managers, Operators, or the Machine Config Operator modify monitored files during upgrades or maintenance windows.

> [!IMPORTANT]
> To use file activity monitoring, you must have enabled **File Activity Monitoring** within the **per Node Configuration** section during secured cluster configuration.
>
> For more information, see "Creating and modifying security policies".

<a id="about-dynamic-path-support-for-file-activity-monitoring_file-activity-monitoring"></a>

## Dynamic path support for file activity monitoring

RHACS 4.11 enhances the Technology Preview file activity monitoring feature with dynamic path support and process-based filtering. You can now define custom file paths by using wildcard patterns instead of being limited to four fixed critical paths. The unified file path criterion simplifies policy creation by replacing separate effective path and actual path fields, while violation records continue to display both values for forensic analysis.

You can use process filtering to suppress alerts from legitimate system operations such as OpenShift upgrades and package installations. You can configure policies with process name, process ancestor, process arguments, and process UID criteria to reduce false positives while maintaining comprehensive file integrity monitoring coverage.

RHACS file activity monitoring includes the following changes and enhancements:

- Node violations are now visible in the RHACS portal **Violations** page, improving investigation workflows for security teams.

- File rename operations are detectable as a distinct file operation type.

- File activity violations are supported in the Splunk Technology Add-on 3.0.0 alert data feed. For more information, see "Using the Red Hat Advanced Cluster Security for Kubernetes add-on".

If you are upgrading from RHACS 4.10 with file activity monitoring enabled, you must migrate existing policies to the 4.11 unified file path model. Any policies that use separate effective path and actual path fields are not automatically converted. For migration guidance, see "Migrate file activity monitoring policies from 4.10 to 4.11".

<div>

<div class="title">

Additional resources

</div>

- [Using the Red Hat Advanced Cluster Security for Kubernetes add-on](../../integration/integrate-with-splunk.md#integrate-splunk-add-on)

- [Migrate file activity monitoring policies from 4.10 to 4.11](configuring-file-activity-monitoring.md#migrate-file-activity-monitoring-policies-from-410-to-411_file-activity-monitoring)

</div>

<a id="file-activity-monitoring-limitations_file-activity-monitoring"></a>

## Known limitations

The following are the known limitations of the file activity monitoring feature:

Architecture support  
This feature supports only x86 architecture in RHACS 4.11. On hybrid clusters with multiple architectures, file activity monitoring operates only on x86 nodes. ARM, Power, and Z architecture nodes do not report file activity violations. Future general availability releases might expand architecture support.

Wildcard pattern performance constraints  
Patterns exceeding this limit are rejected during policy creation. Under sustained load of 100 file operations per second, the file activity monitoring collector consumes approximately 5% CPU and 200 MB RAM. Exceeding these thresholds might result in missed violations or delayed violation reporting.

Hosted control plane compatibility  
File activity monitoring operates on OpenShift cluster worker nodes regardless of whether the control plane is hosted externally (for example, Red Hat Advanced Cluster Security for Kubernetes (RHACS) on Hosted Control Planes). The feature does not monitor control plane file activity, only workloads and system processes running on managed worker nodes. Worker node architecture must be x86 for file activity monitoring to function.

Splunk Technology Add-on integration  
File activity violation data requires Splunk Technology Add-on 3.0.0 or later. Earlier versions of the Splunk TA do not support the file activity input type. For more information, see "Install and configure the Splunk add-on".

<a id="create-file-activity-monitoring-policy_file-activity-monitoring"></a>

# Create a file activity monitoring policy

You can create file activity monitoring policies to detect unauthorized file modifications and host breakouts. Use glob syntax wildcard patterns in your policies to match multiple files or directories with a single pattern, enabling comprehensive monitoring coverage without creating individual policies for each file path.

<div>

<div class="title">

Prerequisites

</div>

- RHACS 4.11 or later is installed.

- You have identified which files and directories require monitoring based on security policy and compliance requirements.

- You understand glob pattern syntax and wildcard matching behavior.

- The file activity monitoring setting is enabled in the **Per Node Settings** section during secured cluster configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, navigate to **Platform Configuration** → **Policy Management**.

2.  Click **Create policy**.

3.  In the **Policy name** field, enter a descriptive name for the policy purpose.

4.  Select the policy severity.

5.  In the **Categories** section, select **File Activity Monitoring**.

6.  Select the **Runtime** lifecycle stage.

7.  Select the event source:

    - **Deployment**: Select this option to monitor file activity initiated by Kubernetes workloads, such as pods, jobs, or deployments. This source identifies when containers try to change their own files or the underlying host system.

    - **Node**: Select this option to monitor sensitive file activity from processes running directly on the host, such as SSH sessions, systemd services, or standalone scripts.

8.  In the **Policy rules** section, add the policy fields that you want to use. For this policy, select **File activity** → **File path**.

    > [!NOTE]
    > The events and violations will show the actual path and effective path, where appropriate. However, the single file path field checks both of these fields.

9.  Enter a file path pattern with optional wildcard characters in glob syntax, as shown in the following examples:

    - For exact path matching, enter the full path without wildcards.

      - Example: `/etc/ssh/sshd_config`

    - To match all files in a directory, use a single asterisk.

      - Example: `/etc/*.conf`

    - To match files at any depth in a directory tree, use double asterisks.

      - Example: `/var/log/app/*/.log`

    - To match specific user directories, combine path segments with wildcards.

      - Example: `/home/*/.ssh/authorized_keys`

10. Optional: From **File operation**, select one or more operations to monitor:

    - **Open (writable)** - Detects files opened for writing.

    - **Create** - Detects new file creation.

    - **Rename** - Detects file rename operations. Provides the file that was moved and the location where the file was moved to.

    - **Delete (Unlink)** - Detects file deletion.

    - **Change permissions** - Detects permission modifications.

    - **Change ownership** - Detects ownership changes.

11. Optional: For node policies, you can create a policy that alerts on file activity from specific processes. For example, you can combine file activity and process filtering to suppress violations from legitimate system operations. For more information, see "Filter file activity by process".

12. Click **Save**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Trigger a test file operation that matches your configured pattern to verify the policy functions correctly.

2.  Navigate to **Violations** in the RHACS portal.

3.  If you configured a policy for deployment policies:

    1.  Select the **User Workloads** tab.

    2.  Verify that a violation was created with the expected file path that matches your wildcard pattern.

4.  If you configured a policy for node file activity monitoring:

    1.  Select the **Nodes** tab.

    2.  Verify that a violation record is displayed with the expected file path that matches your configured wildcard pattern.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating and modifying security policies](custom-security-policies.md)

</div>

<a id="process-filtering-for-file-activity-policies_file-activity-monitoring"></a>

# Process filtering for file activity policies

File activity monitoring policies support process-based filtering to reduce false positive alerts from legitimate system operations. You can configure policies to suppress violations when specific processes, process ancestors, process UIDs, or process arguments match expected patterns during maintenance windows or system upgrades. This capability enables you to maintain comprehensive file integrity monitoring coverage while minimizing alert fatigue from authorized changes.

Process filtering works by adding process criteria to file activity policies with the file path and file operation criteria. When a file operation occurs, RHACS evaluates all configured criteria. If the operation matches the file criteria but the initiating process matches the exclusion filter, no violation is generated.

<a id="available-process-filtering-criteria_file-activity-monitoring"></a>

## Available process filtering criteria

RHACS supports four process-based criteria for file activity policy filtering:

**Process name**  
Filters based on the executable name of the process that performed the file operation. Use this criterion to exclude known system components such as `rpm`, `dpkg`, or operator binaries.

**Process ancestor**  
Filters based on parent or ancestor processes in the process tree. Use this criterion to exclude all operations initiated by specific management frameworks, such as the Machine Config Operator (MCO) on OpenShift clusters.

**Process arguments**  
Filters based on command-line arguments passed to the process. Use this criterion to distinguish between different invocations of the same binary, such as excluding `systemctl daemon-reload` while monitoring other `systemctl` operations.

**Process UID**  
Filters based on the numeric user ID of the process. Use this criterion to allow privileged system maintenance (UID 0) while detecting unprivileged user attempts to modify protected files.

<a id="common-use-cases-for-process-filtering_file-activity-monitoring"></a>

## Common use cases for process filtering

**Suppress OpenShift upgrade activity**  
During OpenShift cluster upgrades, the MCO modifies system configuration files as part of normal upgrade procedures. You can filter violations by adding a process ancestor criterion matching the MCO binary to prevent alert storms during planned maintenance.

**Exclude package manager operations**  
System administrators regularly install and update packages by using `yum`, `dnf`, or `rpm` on cluster nodes. You can filter violations by adding a process name criterion matching the package management tools to allow these expected modifications while detecting unauthorized changes.

**Allow Operator-initiated changes**  
Kubernetes operators frequently update application configuration files as part of their reconciliation loops. You can filter violations by adding process name or process ancestor criteria matching the Operator binary to distinguish between automated configuration management and potential security incidents.

**Detect privilege escalation attempts**  
You can monitor sensitive files for modifications while excluding expected system daemon activity by combining file path patterns with process UID filters. For example, monitor `/etc/sudoers` modifications and exclude UID 0 operations to detect unprivileged who are attempting privilege escalation.

<a id="combining-file-path-and-process-filters_file-activity-monitoring"></a>

## Combining file path and process filters

Process filtering becomes most effective when combined with targeted file path patterns and specific file operation selections. This layered approach creates precise policies that balance security coverage with operational noise reduction.

For example, you can create a policy that performs the following tasks:

- Monitors all configuration files matching `/etc/*.conf`

- Triggers on change permissions and change ownership operations

- Excludes operations initiated by the Machine Config Operator

This policy detects unauthorized permission changes while ignoring legitimate system maintenance, reducing false positives without sacrificing security visibility.

> [!NOTE]
> Process filtering criteria use the same matching logic as other RHACS policy criteria. You can configure multiple process filters in a single policy, and all configured criteria must match for a violation to be suppressed.

<a id="create-file-activity-policies-with-process-filters_file-activity-monitoring"></a>

## Create file activity policies with process filters

You can create file activity monitoring policies that combine file path patterns, file operation selections, and process filtering criteria to achieve precise security coverage with minimal false positives. With this layered approach, you can monitor sensitive files while suppressing violations from expected system maintenance and Operator activity.

<div>

<div class="title">

Prerequisites

</div>

- RHACS 4.11 or later is installed.

- You understand which files require monitoring based on security and compliance requirements.

- You understand which processes initiate legitimate modifications to monitored files.

- The file activity monitoring setting is enabled in the **Per Node Settings** section during secured cluster configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, navigate to **Platform Configuration** → **Policy Management**.

2.  Click **Create policy**.

3.  In the **Policy name** field, enter a descriptive name for the policy purpose.

4.  Select the policy severity.

5.  In the **Categories** section, select **File Activity Monitoring**.

6.  Select the **Runtime** lifecycle stage.

7.  Select the **Node** event source.

8.  In the **Policy rules** section, add the policy fields that you want to use. For this policy, select **File activity** → **File path**.

9.  In the **File path** field, enter a wildcard pattern matching the files you want to monitor. For example, enter `/etc/*.conf` to match all configuration files in the `/etc/` directory.

10. In **File operation**, select the operations you want to alert on that indicate security risks. For example, select **Change permissions** and **Change ownership** to detect unauthorized attempts to escalate privileges or modify file access controls.

11. Configure the process activity filtering by selecting one or more criteria. In the criterion value field, enter the process identifier to exclude. For example, select **Process ancestor** and enter `machine-config-daemon` to suppress violations during OpenShift cluster upgrades. You can configure the following criteria:

    - **Process name**: Filters by executable name

    - **Process ancestor**: Filters by parent process

    - **Process arguments**: Filters by command-line arguments

    - **Process UID**: Filters by user ID

12. Optional: Add additional process filtering criteria to create more precise exclusion rules. For example, add a **Process name** criterion with value `rpm` and add another **Process name** criterion with value `dnf` to suppress violations from both Red Hat Package Manager and Dandified YUM operations.

13. Click **Save**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Trigger a file operation from an unfiltered process that matches your configured file criteria, for example:

    ``` terminal
    $ touch /etc/test.conf && chmod 777 /etc/test.conf
    ```

2.  Navigate to **Violations** in the RHACS portal.

3.  Verify that a violation record is displayed with the file path and operation details.

4.  Trigger a file operation from a filtered process to verify the process filter is working.

    For example, to simulate package installation:

    ``` terminal
    # rpm -i example-package.rpm
    ```

5.  Navigate to **Violations** in the RHACS portal.

6.  Verify that no violation is displayed for the filtered process operation.

</div>

<a id="create-file-activity-policies-process-filters-examples_file-activity-monitoring"></a>

### Policies with process filter examples

You can combine file path, operations, and process name criteria to create file activity monitoring policies that provide alerts with fewer false positives.

The following example policy configurations show common file activity monitoring scenarios with process filtering:

Monitor SSH authorized keys changes excluding system daemons  
- File path: `/home/*/.ssh/authorized_keys`

- File operations: Create, Delete (unlink), Change permissions

- Process name: `sshd` (negated to exclude SSH daemon)

- Event source: Node

This policy detects unauthorized SSH key additions while allowing SSH daemon operations.

Monitor application log rotation excluding system log managers  
- File path: `/var/log/app/*/.log`

- File operations: Rename, Delete (unlink)

- Process ancestor: `logrotate`

- Event source: Deployment

This policy detects unauthorized log file deletion or tampering while allowing scheduled log rotation.

Monitor container configuration files excluding Operator updates  
- File path: `/opt/app/config/*.yaml`

- File operations: Open (writable), Create, Delete (unlink)

- Process name: `app-operator`

- Event source: Deployment

This policy detects unauthorized configuration changes while allowing the application Operator to manage configuration files.

<a id="migrate-file-activity-monitoring-policies-from-410-to-411_file-activity-monitoring"></a>

# Migrate file activity monitoring policies from 4.10 to 4.11

You can migrate file activity monitoring policies from RHACS release 4.10 to release 4.11. To migrate, re-create policies by using the unified file path criterion with wildcard patterns.

The underlying policy data model changed in release 4.11 to support custom paths and process filtering, requiring manual migration from the fixed four-path model used in release 4.10. To use your existing policies, you must complete these steps before upgrading to release 4.11.

<div>

<div class="title">

Prerequisites

</div>

- You understand which files and operations that your 4.10 policies monitored.

- You understand glob pattern syntax for creating wildcard patterns.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Inventory your existing 4.10 file activity policies:

    1.  In the RHACS portal, navigate to **Platform Configuration** → **Policy Management**.

    2.  Filter policies by the **File Activity Monitoring** category.

    3.  For each file activity policy, record:

        - The effective path or actual path values configured

        - The file operation selections, such as Open, Create, Delete, Change permissions, or Change ownership

        - The event source selection (Deployment or Node)

        - Any observed false positive patterns during 4.10 usage

2.  Map 4.10 fixed paths to 4.11 wildcard patterns. Review each monitored path and determine whether you can expand coverage using wildcard patterns:

    - For paths monitoring specific files, use the exact path without wildcards.

    - For paths monitoring configuration directories, consider patterns such as `/etc/*.conf` to match all configuration files.

    - For paths monitoring application logs, consider recursive patterns such as `/var/log/app/*/.log` to match logs at any depth.

3.  Create new 4.11 file activity policies:

    1.  Click **Create policy**.

    2.  In the **Policy name** field, enter a name for the migrated policy purpose.

    3.  Verify that the correct severity is selected.

    4.  In the **Categories** section, select **File Activity Monitoring**.

    5.  Verify that the correct **lifecycle stage** is selected.

    6.  Select the same **Event source** value configured in your 4.10 policy.

    7.  In the **Policy rules** section, add a **File path** criterion with the correct wildcard pattern.

    8.  Select the same **File operation** values configured in your 4.10 policy.

    9.  Optional: Add process filtering criteria to suppress false positives observed during 4.10 usage:

        - To exclude Machine Config Operator activity during OpenShift upgrades, add a **Process ancestor** criterion with value `machine-config-daemon`.

        - To exclude package manager operations, add a **Process name** criterion with value `rpm` or `dnf`.

        - To exclude operator-initiated changes, add a **Process name** criterion matching the operator binary.

    10. Click **Save**.

4.  Test your migrated policies:

    1.  Trigger a file operation that should generate a violation based on your policy configuration.

    2.  Navigate to **Violations** in the RHACS portal.

    3.  Verify that the new 4.11 policy generates violations with expected path values.

    4.  Trigger a file operation that matches your process filter criteria.

    5.  Verify that no violation is displayed for filtered processes, confirming that process filters suppress expected activity.

5.  Disable or delete 4.10 policies:

    1.  After verifying that 4.11 policies provide equal or better security coverage, disable your 4.10 file activity policies by setting them to **Disabled**.

    2.  Optional: Delete 4.10 policies after a suitable observation period confirms that 4.11 policies meet your monitoring requirements.

</div>

<div>

<div class="title">

Verification

</div>

1.  Navigate to **Violations** in the RHACS portal.

2.  Verify that file activity violations appear for unauthorized modifications while expected system operations do not trigger violations.

3.  Compare the volume of violations from 4.11 policies to 4.10 baseline levels.

4.  Verify that wildcard patterns detect file operations across multiple files as intended.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Respond to violations](../respond-to-violations.md)

</div>
