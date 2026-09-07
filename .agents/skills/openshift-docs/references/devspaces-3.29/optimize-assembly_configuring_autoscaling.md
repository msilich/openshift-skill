> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-assembly_configuring_autoscaling). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Scale the platform automatically

Scale OpenShift Dev Spaces container replicas and cluster nodes automatically so that the platform grows and shrinks with developer demand.

- **[Scale OpenShift Dev Spaces for high availability](optimize-proc_configuring_number_of_replicas.md)**  
  Scale OpenShift Dev Spaces for high availability by defining a Kubernetes `HorizontalPodAutoscaler` (HPA) resource for OpenShift Dev Spaces operands. The HPA dynamically adjusts the number of replicas based on specified metrics.
- **[Prevent workspace failures during node scaling](optimize-proc_configuring_machine_autoscaling.md)**  
  Prevent workspace failures during node scaling by configuring OpenShift Dev Spaces startup timeouts and pod annotations to work with the cluster autoscaler.
