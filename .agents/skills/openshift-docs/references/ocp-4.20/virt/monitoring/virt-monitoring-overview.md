<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Monitor the health of your cluster and virtual machines (VMs) to have a unified operational view of your environment. This ensures high availability and optimal resource performance.

You can monitor the health of your cluster and VMs with the following tools:

Monitoring OpenShift Virtualization VM health status
View the overall health of your OpenShift Virtualization environment in the web console by navigating to the **Home** → **Overview** page in the OpenShift Container Platform web console. The **Status** card displays the overall health of OpenShift Virtualization based on the alerts and conditions.

[OpenShift Container Platform cluster checkup framework](virt-running-cluster-checkups.md#virt-running-cluster-checkups)
Run automated tests with the OpenShift Container Platform cluster checkup framework to ensure that your cluster, including cluster storage, is optimally configured for OpenShift Virtualization.

[Prometheus queries for virtual resources](virt-prometheus-queries.md#virt-prometheus-queries)
Query vCPU, network, storage, and guest memory swapping usage and live migration progress.

[VM custom metrics](virt-exposing-custom-metrics-for-vms.md#virt-exposing-custom-metrics-for-vms)
Configure the `node-exporter` service to expose internal VM metrics and processes.

[VM health checks](virt-monitoring-vm-health.md#virt-monitoring-vm-health)
Configure readiness, liveness, and guest agent ping probes and a watchdog for VMs.

[Runbooks](virt-runbooks.md#virt-runbooks)
Diagnose and resolve issues that trigger OpenShift Virtualization [alerts](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/monitoring_key_concepts/key-concepts#about-managing-alerts_key-concepts) in the OpenShift Container Platform web console.
