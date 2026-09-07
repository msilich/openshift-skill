<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can identify and resolve OpenShift Container Platform cluster issues by using diagnostic tools, support procedures, and remote health monitoring.

# Get support

Visit the Red Hat Customer Portal to review knowledge base articles, submit a support case, and review additional product documentation and resources.

# Remote health monitoring issues

Use the Telemetry Client and the Insights Operator to collect cluster telemetry and configuration data. The Red Hat support team uses this diagnostic information to proactively identify and resolve potential infrastructure issues.

Red Hat uses this data to understand and resolve issues in a *connected cluster*. Similar to connected clusters, you can use remote health monitoring in a restricted network. OpenShift Container Platform collects data and monitors health using the following:

- **Telemetry**: The Telemetry Client gathers and uploads the metrics values to Red Hat every four minutes and thirty seconds. Red Hat uses this data to:

  - Monitor the clusters.

  - Roll out OpenShift Container Platform upgrades.

  - Improve the upgrade experience.

- **Insights Operator**: By default, OpenShift Container Platform installs and enables the Insights Operator, which reports configuration and component failure status every two hours. The Insights Operator helps to:

  - Identify potential cluster issues proactively.

  - Provide a solution and preventive action in Red Hat OpenShift Cluster Manager.

You can review telemetry information.

If you have enabled remote health reporting, you can use Red Hat Lightspeed to identify issues with your cluster. You can optionally disable remote health reporting.

# Cluster data collection

Diagnostic tools and system logs provide the critical debugging information that the Red Hat Support team requires to troubleshoot and resolve cluster issues.

A cluster administrator can use the following to gather data about your cluster:

- **must-gather tool**: Use the `must-gather` tool to collect information about your cluster and to debug the issues.

- **sosreport**: Use the `sosreport` tool to collect configuration details, system information, and diagnostic data for debugging purposes.

- **Cluster ID**: Obtain the unique identifier for your cluster, when providing information to Red Hat Support.

- **Bootstrap node journal logs**: Gather `bootkube.service` `journald` unit logs and container logs from the bootstrap node to troubleshoot bootstrap-related issues.

- **Cluster node journal logs**: Gather `journald` unit logs and logs within `/var/log` on individual cluster nodes to troubleshoot node-related issues.

- **Network trace**: Provide a network packet trace from a specific OpenShift Container Platform cluster node or a container to Red Hat Support to help troubleshoot network-related issues.

# Issue resolution

As an administrator, you can minimize the downtime for OpenShift Container Platform by monitoring system health and applying specific troubleshooting procedures.

You can troubleshoot these components by using the following procedures:

- **Installation issues**: OpenShift Container Platform installation proceeds through various stages. You can perform the following:

  - Monitor the installation stages.

  - Determine at which stage installation issues occur.

  - Investigate multiple installation issues.

  - Gather logs from a failed installation.

- **Node issues**: A cluster administrator can verify and troubleshoot node-related issues by reviewing the status, resource usage, and configuration of a node. You can query the following:

  - Kubelet’s status on a node.

  - Cluster node journal logs.

- **Crio issues**: A cluster administrator can verify CRI-O container runtime engine status on each cluster node. If you experience container runtime issues, perform the following:

  - Gather CRI-O journald unit logs.

  - Cleaning CRI-O storage.

- **Operating system issues**: OpenShift Container Platform runs on Red Hat Enterprise Linux CoreOS. If you experience operating system issues, you can investigate kernel crash procedures. Ensure the following:

  - Enable kdump.

  - Test the kdump configuration.

  - Analyze a core dump.

- **Network issues**: To troubleshoot Open vSwitch issues, a cluster administrator can perform the following:

  - Configure the Open vSwitch log level temporarily.

  - Configure the Open vSwitch log level permanently.

  - Display Open vSwitch logs.

- **Operator issues**: A cluster administrator can do the following to resolve Operator issues:

  - Verify Operator subscription status.

  - Check Operator pod health.

  - Gather Operator logs.

- **Pod issues**: A cluster administrator can troubleshoot pod-related issues by reviewing the status of a pod and completing the following:

  - Review pod and container logs.

  - Start debug pods with root access.

- **Source-to-image issues**: A cluster administrator can observe the S2I stages to determine where in the S2I process a failure occurred. Gather the following to resolve Source-to-Image (S2I) issues:

  - Source-to-Image diagnostic data.

  - Application diagnostic data to investigate application failure.

- **Storage issues**: A multi-attach storage error occurs when the mounting volume on a new node is not possible because the failed node cannot unmount the attached volume. A cluster administrator can do the following to resolve multi-attach storage issues:

  - Enable multiple attachments by using RWX volumes.

  - Recover or delete the failed node when using an RWO volume.

- **Monitoring issues**: A cluster administrator can follow the procedures on the troubleshooting page for monitoring. If the metrics for your user-defined projects are unavailable or if Prometheus is consuming a lot of disk space, check the following:

  - Investigate why user-defined metrics are unavailable.

  - Determine why Prometheus is consuming a lot of disk space.

- **OpenShift CLI (`oc`) issues**: Investigate OpenShift CLI (`oc`) issues by increasing the log level.

# Additional resources

- [Getting support](getting-support.md#getting-support)

- [About remote health monitoring](remote_health_monitoring/about-remote-health-monitoring.md#about-remote-health-monitoring)

- [Using remote health monitoring in a restricted network](remote_health_monitoring/remote-health-reporting-from-restricted-network.md#remote-health-reporting-from-restricted-network)

- [Troubleshooting installations](troubleshooting/troubleshooting-installations.md#troubleshooting-installations)

- [Troubleshooting CRI-O issues](troubleshooting/troubleshooting-crio-issues.md#troubleshooting-crio-issues)

- [Troubleshooting operating system issues](troubleshooting/troubleshooting-operating-system-issues.md#troubleshooting-operating-system-issues)

- [Troubleshooting network issues](troubleshooting/troubleshooting-network-issues.md#troubleshooting-network-issues)

- [Using Red Hat Lightspeed to identify issues with your cluster](remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.md#using-insights-to-identify-issues-with-your-cluster)

- [Showing data collected by remote health monitoring](remote_health_monitoring/showing-data-collected-by-remote-health-monitoring.md#showing-data-collected-by-remote-health-monitoring)

- [Gathering data about your cluster](gathering-cluster-data.md#gathering-cluster-data)

- [Verifying node health](troubleshooting/verifying-node-health.md#verifying-node-health)

- [Troubleshooting Operator issues](troubleshooting/troubleshooting-operator-issues.md#troubleshooting-operator-issues)

- [Investigating pod issues](troubleshooting/investigating-pod-issues.md#investigating-pod-issues)

- [Troubleshooting Source-to-Image](troubleshooting/troubleshooting-s2i.md#troubleshooting-s2i)

- [Troubleshooting storage issues](troubleshooting/troubleshooting-storage-issues.md#troubleshooting-storage-issues)

- [Investigating monitoring issues](troubleshooting/investigating-monitoring-issues.md#investigating-monitoring-issues)

- [Diagnosing OpenShift CLI issues](troubleshooting/diagnosing-oc-issues.md#diagnosing-oc-issues)
