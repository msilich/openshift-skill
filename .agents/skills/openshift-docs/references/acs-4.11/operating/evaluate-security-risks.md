<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes assesses risk across your entire environment and ranks your running deployments according to their security risk. It also provides details about vulnerabilities, configurations, and runtime activities that require immediate attention.

<a id="risk-view-details_evaluate-security-risks"></a>

# Viewing deployments at risk

The **Risk** view lists all deployments from all clusters, sorted by a multi-factor risk metric based on policy violations, image contents, deployment configuration, and other similar factors. Deployments at the top of the list present the most risk.

The **Risk** view shows list of deployments with following attributes for each row:

- **Name**: The name of the deployment.

- **Created**: The creation time of the deployment.

- **Cluster**: The name of the cluster where the deployment is running.

- **Namespace**: The namespace in which the deployment exists.

- **Priority**: A priority ranking based on severity and risk metrics.

In the **Risk** view, you can complete these actions:

- Select a column heading to sort the violations in ascending or descending order.

- Use the filter bar to filter violations. For example, you can use the `Process Name:<name>` query in the filter bar to find deployments that have the specified process.

- Create a new policy based on the filtered criteria.

To view more details about the risks for a deployment, select a deployment in the **Risk** view.

<a id="risk-view-deployment_evaluate-security-risks"></a>

## Viewing risk information for a deployment

When you select a deployment in the **Risk** view, the **Deployment risk** page provides information about risk factors for that deployment. You can select from the following tabs:

- Risk indicators

- Deployment details

- Process discovery

<a id="risk-indicators-tab_evaluate-security-risks"></a>

## Risk indicators tab

The **Risk indicators** tab explains the discovered risks.

The **Risk indicators** tab includes the following sections:

- **Policy Violations**: The names of the policies that are violated for the selected deployment.

- **Suspicious Process Executions**: Suspicious processes, arguments, and container names that the process ran in.

- **Image Vulnerabilities**: Images including total CVEs with their CVSS scores.

- **Service Configurations**: Aspects of the configurations that are often problematic, such as read-write (RW) capability, whether capabilities are dropped, and the presence of privileged containers.

- **Service Reachability**: Container ports exposed inside or outside the cluster.

- **Components Useful for Attackers**: Discovered software tools that are often used by attackers.

- **Number of Components in Image**: The number of packages found in each image.

- **Image Freshness**: Image names and age, for example, `285 days old`.

- **RBAC Configuration**: The level of permissions granted to the deployment in Kubernetes role-based access control (RBAC).

> [!NOTE]
> Not all sections are visible in the **Risk indicators** tab. Red Hat Advanced Cluster Security for Kubernetes displays only relevant sections that affect the selected deployment.

<a id="risk-deployment-details_evaluate-security-risks"></a>

## Deployment details tab

The sections in the **Deployment details** tab of the **Deployment risk** page give you more information so you can make appropriate decisions on how to address the discovered risk.

You can click the arrows to expand the different sections in the page and view more information.

<a id="risk-deployment-details-overview_evaluate-security-risks"></a>

### Overview section

The **Overview** section in the **Deployment details** tab shows details about the following items:

- **Deployment ID**: An alphanumeric identifier for the deployment.

- **Deployment Name**: Name of the deployment.

- **Deployment Type**: The type of deployment, for example, `Deployment` or `DaemonSet`.

- **Namespace**: The Kubernetes or OpenShift Container Platform namespace in which the deployment exists.

- **Replicas**: The number of pods deployed for this deployment.

- **Labels**: The key-value labels attached to the Kubernetes or OpenShift Container Platform application.

- **Annotations**: The Kubernetes annotations for the deployment.

- **Created**: The time and date when the deployment was created.

- **Cluster**: The name of the cluster where the deployment is running.

- **Service Account**: Represents an identity for processes that run in a pod. When a process is authenticated through a service account, it can contact the Kubernetes API server and access cluster resources. If a pod does not have an assigned service account, it gets the default service account.

- **Port configuration**: Information about the ports that are configured in the deployment.

<a id="risk-deployment-details-container-configuration_evaluate-security-risks"></a>

### Container configuration section

The container configuration section in the **Deployment details** tab shows details about the following items:

- **Image Name**: The name of the image that is deployed.

- **Resources**

  - **CPU Request (cores)**: The number of CPUs requested by the container.

  - **CPU Limit (cores)**: The maximum number of CPUs the container can use.

  - **Memory Request (MB)**: The memory size requested by the container.

  - **Memory Limit (MB)**: The maximum amount of memory the container can use without being killed.

- **Mounts**

  - **Name**: The name of the mount.

  - **Source**: The path from where the data for the mount comes.

  - **Destination**: The path to which the data for the mount goes.

  - **Type**: The type of the mount.

- **Secrets**: The names of Kubernetes secrets used in the deployment, and basic details for secret values that are X.509 certificates.

<a id="risk-deployment-details-security-context_evaluate-security-risks"></a>

### Security context section

The **Security Context** section in the **Deployment details** tab shows the following details about the security context:

- **Privileged**: Lists `true` if the container is privileged.

<a id="process-discovery-tab_evaluate-security-risks"></a>

## Process discovery tab

The **Process Discovery** tab provides a comprehensive list of all binaries that have been executed in a container in your environment for a deployment that you have selected.

You can view information about processes and add or remove processes from the baseline. This page provides the following information and options:

- **Event Timeline**: Displays the number of policy violations, process activities, restarts and terminations, and a link to a graphical representation of that information.

- **History of Running Processes**: Displays a list of processes by name of the binary that was executed and the container in the deployment in which the process executed. Click a process to expand and show additional information such as the following fields:

  - **Arguments**: The specific arguments that were passed with the binary.

  - **Time**: The date and time of the most recent time the binary was executed in a given container.

  - **Pod ID**: The identifier of the pod that includes the container.

  - **UID**: The Linux user identity under which the process executed.

- **Spec Container Baselines**: Used to create baselines that you can use to allow or deny new processes when RHACS discovers them.

<a id="process-discovery-event-timeline_evaluate-security-risks"></a>

### Event timeline section

The **Event Timeline** section in the **Process Discovery** tab provides an overview of events for the selected deployment. It shows the number of policy violations, process activities, and container termination or restart events.

You can select **Event Timeline** to view more details.

The **Event Timeline** shows events for all pods for the selected deployment.

Red Hat Advanced Cluster Security for Kubernetes categorizes the events on the timeline as the following types:

- Process activities

- Policy violations

- Container restarts

- Container terminations

The events appear as icons on a timeline. To see more details about an event, hover over the event icon. The details appear in a tooltip.

- Click **Show Legend** to see which icon corresponds to which type of event.

- Select **Export** → **Download PDF** or **Export** → **Download CSV** to download the event timeline information.

- Select **Show All** and choose the filter to restrict which type of events are visible on the timeline.

- You can expand the display to show events separately for each container in the selected pod.

All events in the timeline are also visible in the minimap control at the bottom. The minimap controls the number of events visible in the event timeline. You can change the events shown in the timeline by modifying the highlighted area on the minimap. To do this, decrease the highlighted area from left or right sides (or both), and then drag the highlighted area.

<div class="note">

<div class="title">

</div>

- When containers restart, Red Hat Advanced Cluster Security for Kubernetes (RHACS) does the following:

  - Shows information about container termination and restart events for up to 10 inactive container instances for each container in a pod. For example, for a pod with two containers `app` and `sidecar`, RHACS keeps activity for up to 10 `app` instances and up to 10 `sidecar` instances.

  - Does not track process activities associated with the previous instances of the container.

- RHACS only shows the most recent execution of each (process name, process arguments, UID) tuple for each pod.

- RHACS shows events only for the active pods.

- RHACS adjusts the reported timestamps based on time reported by Kubernetes and Collector. Kubernetes timestamps use second-based precision, and it rounds off the time to the nearest second. However, Collector uses more precise timestamps. For example, if Kubernetes reports the container start time as `10:54:48`, and the Collector reports a process in that container started at `10:54:47.5349823`, RHACS adjusts the container start time to `10:54:47.5349823`.

</div>

<a id="use-process-baselines_evaluate-security-risks"></a>

### Using process baselines

You can minimize risk by using process baselining for infrastructure security. With this approach, Red Hat Advanced Cluster Security for Kubernetes (RHACS) first discovers existing processes and creates a baseline. Then it operates in the default deny-all mode and only allows processes listed in the baseline to run.

Process baselines  
When you install RHACS, there is no default process baseline. As RHACS discovers deployments, it creates a process baseline for every container type in a deployment. Then it adds all discovered processes to their own process baselines.

Process baseline states  
During the process discovery phase, all baselines are in an unlocked state.

In an **unlocked** state:

- When RHACS discovers a new process, it adds that process to the process baseline.

- Processes do not show up as risks and do not trigger any violations.

After an hour from when RHACS receives the first process indicator from a container in a deployment, it finishes the process discovery phase. For information about how to configure the duration of the discovery phase, see "Configuring the observation period for the process baseline".

At this point:

- RHACS stops adding processes to the process baselines.

- New processes that are not in the process baseline show up as risks, but they do not by default trigger any violations.

To generate violations, you must either manually lock the process baseline, or enable process baseline auto-lock feature.

For more information about manually locking and unlocking process baselines, see "Locking and unlocking the process baselines".

For more information about automatically locking process baselines, see "Configuring auto-lock for process baselines".

In a **locked** state:

- RHACS stops adding processes to the process baselines.

- New processes that are not in the process baseline trigger violations.

Independent of the locked or unlocked baseline state, you can always add or remove processes from the baseline.

> [!NOTE]
> For a deployment, if each pod has more than one container in it, RHACS creates a process baseline for each container type. For such a deployment, if some baselines are locked and some are unlocked, the baseline status for that deployment shows up as **Mixed**.

<a id="configuring-process-baseline-generation-duration_evaluate-security-risks"></a>

### Configuring the observation period for the process baseline

You can configure the observation period for the process baseline by setting the `ROX_BASELINE_GENERATION_DURATION` environment variable.

<div>

<div class="title">

Procedure

</div>

- Set the `ROX_BASELINE_GENERATION_DURATION` environment variable by running the following command:

  ``` terminal
  $ oc -n stackrox set env deploy/central \
    ROX_BASELINE_GENERATION_DURATION=<value>
  ```

  - `oc`: If you use Kubernetes, enter `kubectl`.

  - `<value>`: Use time units, for example: `300ms`, `-1.5h`, or `2h45m`. Valid time units are:

    - `ns`

    - `us` or `µs`

    - `ms`

    - `s`

    - `m`

    - `h`

</div>

<a id="view-process-baselines_evaluate-security-risks"></a>

### Viewing the process baselines

You can view process baselines from the **Risk** view.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, select **Risk** from the navigation menu.

2.  Select a deployment from the list of deployments in the default **Risk** view.

3.  In the **Deployment Risk** page, select the **Process discovery** tab.

4.  The process baselines are visible under the **Spec Container Baselines** section.

</div>

<a id="add-process-to-baseline_evaluate-security-risks"></a>

### Adding a process to the baseline

You can manually add a process to the baseline, for example, to add a safe process that was not running when the baseline was created.

<div>

<div class="title">

Procedure

</div>

1.  In the Red Hat Advanced Cluster Security for Kubernetes (RHACS) portal, select **Risk** from the navigation menu.

2.  Select a deployment from the list of deployments in the default **Risk** view.

3.  Select the **Process discovery** tab.

    - In the **History of Running Processes** list, click the plus sign to add a process to the process baseline. You can only add a process that is not already in the baseline.

</div>

<a id="remove-process-from-baseline_evaluate-security-risks"></a>

### Removing a process from the baseline

You can remove a process from the baseline so that it is not considered when the system evaluates the baseline.

<div>

<div class="title">

Procedure

</div>

1.  In the Red Hat Advanced Cluster Security for Kubernetes (RHACS) portal, select **Risk** from the navigation menu.

2.  Select a deployment from the list of deployments in the default **Risk** view.

3.  Select the **Process discovery** tab.

4.  Under the **Spec Container baselines** section, click the **Remove** icon for the process you want to remove from the process baseline.

</div>

<a id="lock-and-unlock-process-baselines_evaluate-security-risks"></a>

### Locking and unlocking the process baselines

You can **Lock** the baseline to trigger violations for all processes not listed in the baseline and **Unlock** the baseline to stop triggering violations.

<div>

<div class="title">

Procedure

</div>

1.  In the Red Hat Advanced Cluster Security for Kubernetes (RHACS) portal, select **Risk** from the navigation menu.

2.  Select a deployment from the list of deployments in the default **Risk** view.

3.  Select the **Process Discovery** tab.

4.  Under the **Spec Container baselines** section:

    - Click the **Lock** icon to trigger violations for processes that are not in the baseline.

    - Click the **Unlock** icon to stop triggering violations for processes that are not in the baseline.

</div>

<a id="auto-lock-process-baselines_evaluate-security-risks"></a>

### Configuring auto-lock for process baselines

You can configure Red Hat Advanced Cluster Security for Kubernetes (RHACS) to automatically lock process baselines when they leave the observation period. You must enable auto-lock feature in both Central and in the secured cluster.

Follow these guidelines when using auto-lock:

- The feature is enabled in Central by default and disabled in the secured clusters by default. Therefore, enabling the feature does not require restarting Central. However, changing the state of the feature in Central does require a restart of Central.

- The feature is only enabled for process baselines for secured clusters where the feature is enabled.

- Disabling the feature after it has been enabled does not unlock process baselines that have been locked by the feature.

- Enabling the feature does not lock process baselines that left the observation period before the feature was enabled.

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, go to the RHACS Operator page.

2.  In the top navigation menu, select **Secured Cluster**.

3.  Click the instance name, for example, **stackrox-secured-cluster-services**.

4.  Use one of the following methods to change the setting:

    - In the **Form view**, under **Process baselines settings** → **Auto Lock**, select **Enabled** or **Disabled**.

    - Click **YAML** to open the YAML editor and locate the `spec.processBaselines.autoLock` attribute. Change to `Enabled` or `Disabled`.

5.  Click **Save.**

6.  To enable or disable the feature in Central, set the `ROX_AUTO_LOCK_PROCESS_BASELINES` environment variable. The default value is `true`.

</div>

<a id="auto-lock-process-baselines-known-limitations_evaluate-security-risks"></a>

### Auto-lock process baselines known limitations

Central, Central DB, and Sensor consume more CPU and memory resources when process baseline auto-lock is enabled. This can lead to CPU throttling and pods crashing due to running out of memory.

The following results were obtained from tests with 1,000 deployments in which 5,000 process were spawned every 30 seconds (166.67 processes per second). The test was run with the feature enabled and disabled. Resource usage was compared between the two tests. For the tests the process baseline generation duration was set to three minutes and the rate of process creation did not change after the baseline generation period ended.

- Sensor used 24 Mb more memory.

- The difference in Sensor memory usage did not appear to increase with time.

- Sensor CPU usage increased by 0.14 CPUs.

- Central used 175 Mb more memory.

- The rate of increase of Central memory usage was 65 Kb per second greater with auto-lock enabled.

- Central CPU usage increased by 0.12 CPUs.

- Central DB used 296 Mb more memory with auto-lock enabled.

- The difference in Central DB memory usage did not appear to increase over time.

- Central DB CPU usage was low and increased by 0.03 CPUs.

<a id="bulk-locking-and-unlocking-process-baselines_evaluate-security-risks"></a>

### Bulk locking and unlocking process baselines

You can lock or unlock all process baselines in a cluster by using API endpoints. You can specify an optional set of namespaces to limit the action to just those namespaces.

Use the following API endpoints to lock and unlock the process baseline:

- `/v1/processbaselines/bulk/lock`

- `/v1/processbaselines/bulk/unlock`

The following example shows the input for the endpoints:

``` json
{
        "cluster_id": "aeaaaaaa-0000-0000-0000-000000000000",
        "namespaces": [
                        "stackrox",
                        "gmp-system"
                      ]
}
```

These endpoints return a success message or an error.

<a id="create-policy-from-risk-view_evaluate-security-risks"></a>

# Creating a security policy from the risk view

You can generate a new security policy directly from the **Risk** view in the RHACS portal to address specific security concerns. Use this method to create a policy based on the local page filtering criteria you apply to your risk data, ensuring the policy targets the specific risks you are analyzing.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Risk**.

2.  Apply the local page filtering criteria that you want to create a policy for. For example, you can filter by using criteria such as a specific CVE, a cluster, a deployment, an image, or various other criteria.

3.  Click **Create policy** and complete the required fields to create a new policy. For the steps to create a policy, see "Creating a security policy from the system policies view".

</div>

1.  Additional resources

    - [Creating a security policy from the system policies view ](manage_security_policies/custom-security-policies.md#create-policy-from-system-policies-view_custom-security-policies)

<a id="understanding-filtering-to-policy-mapping_evaluate-security-risks"></a>

## Filtering criteria and policies

Use the filtering criteria in the **Risk** view to define the policy scope and rules when you create a policy.

When you create new security policies from the **Risk** view, based on the filtering criteria you use, not all criteria are directly applied to the new policy.

Red Hat Advanced Cluster Security for Kubernetes (RHACS) converts the **Cluster**, **Namespace**, and **Deployment** filters to corresponding policy resources.

- When converting **Risk** view filters to policy resources, RHACS distinguishes between name-based and label-based filtering.

- Cluster name filters convert to cluster ID scopes, while cluster label filters convert to cluster label scopes.

- Namespace name filters convert to namespace name scopes, and namespace label filters convert to namespace label scopes.

These conversions preserve the filtering semantics when creating policies from Risk view.

> [!NOTE]
> Cluster label and namespace label scopes are only created when the secured cluster runs RHACS 4.11 or later. For secured clusters running earlier versions, RHACS drops label-based filters during policy creation.

<a id="local-page-filtering_evaluate-security-risks"></a>

### Local page filtering

Local page filtering on the **Risk** view combines the search terms by using the following methods:

- RHACS combines the search terms within the same category with an `OR` operator. For example, if the search query is `Cluster:A,B`, the filter matches deployments in `cluster A` or `cluster B`.

- RHACS combines the search terms from different categories with an `AND` operator. For example, if the search query is `Cluster:A+Namespace:Z`, the filter matches deployments in `cluster A` and in `namespace Z`.

- When you add multiple scopes to a policy, the policy matches violations from any of the scopes. For example, if you search for `(Cluster A OR Cluster B) AND (Namespace Z)` it results in two policy resources, `(Cluster=A AND Namespace=Z)` OR `(Cluster=B AND Namespace=Z)`.

- RHACS drops or modifies filters that do not directly map to policy criteria and reports the dropped filters.

The following table lists how the filtering search attributes map to the policy criteria:

| Search attribute | Policy criteria |
|----|----|
| Add Capabilities | Add Capabilities |
| Annotation | Disallowed Annotation |
| CPU Cores Limit | Container CPU Limit |
| CPU Cores Request | Container CPU Request |
| CVE | CVE |
| CVE Published On | Dropped |
| CVE Snoozed | Dropped |
| CVSS | CVSS |
| Cluster (by name) | Converted to cluster ID scope |
| Cluster Label | Converted to cluster label scope (RHACS 4.11+) |
| Component | Image Component (name) |
| Component Version | Image Component (version) |
| Deployment | Converted to scope |
| Deployment Type | Dropped |
| Dockerfile Instruction Keyword | Dockerfile Line (key) |
| Dockerfile Instruction Value | Dockerfile Line (value) |
| Drop Capabilities | Dropped |
| Environment Key | Environment Variable (key) |
| Environment Value | Environment Variable (value) |
| Environment Variable Source | Environment Variable (source) |
| Exposed Node Port | Dropped |
| Exposing Service | Dropped |
| Exposing Service Port | Dropped |
| Exposure Level | Port Exposure |
| External Hostname | Dropped |
| External IP | Dropped |
| Image | Dropped |
| Image Command | Dropped |
| Image Created Time | Days since image was created |
| Image Entrypoint | Dropped |
| Image Label | Disallowed Image Label |
| Image operating system | Image operating system |
| Image Pull Secret | Dropped |
| Image Registry | Image Registry |
| Image Remote | Image Remote |
| Image Scan Time | Days since image was last scanned |
| Image Tag | Image Tag |
| Image Top CVSS | Dropped |
| Image User | Dropped |
| Image Volumes | Dropped |
| Deployment Label | Converted to deployment label scope |
| Max Exposure Level | Dropped |
| Memory Limit (MB) | Container Memory Limit |
| Memory Request (MB) | Container Memory Request |
| Namespace (by name) | Converted to namespace name scope |
| Namespace Label | Converted to namespace label scope (RHACS 4.11 and later) |
| Namespace ID | Dropped |
| Pod Label | Dropped |
| Port | Port |
| Port Protocol | Protocol |
| Priority | Dropped |
| Privileged | Privileged |
| Process Ancestor | Process Ancestor |
| Process Arguments | Process Arguments |
| Process Name | Process Name |
| Process Path | Dropped |
| Process Tag | Dropped |
| Process UID | Process UID |
| Read Only Root Filesystem | Read-Only Root Filesystem |
| Secret | Dropped |
| Secret Path | Dropped |
| Service Account | Dropped |
| Service Account Permission Level | Minimum RBAC Permission Level |
| Toleration Key | Dropped |
| Toleration Value | Dropped |
| Volume Destination | Volume Destination |
| Volume Name | Volume Name |
| Volume ReadOnly | Writable Volume |
| Volume Source | Volume Source |
| Volume Type | Volume Type |
