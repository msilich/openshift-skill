# Platform health

Read [System health](../../openshift-docs/references/acs-4.11/operating/use-system-health-dashboard.md)
and its component status sections, then [Collector logs and pod status](../../openshift-docs/references/acs-4.11/troubleshooting/retrieving-and-analyzing-the-collector-logs-and-pod-status.md).
See [source provenance](sources.md) and follow [execution](execution.md).

Establish which Central owns the secured cluster ID. Correlate that registration
with approved deployment inventory, Sensor configuration metadata and the target
OpenShift API endpoint. Do not dump Secrets or whole environment configurations.
If evidence conflicts, stop cross-plane conclusions until the mapping is resolved.

Read the Operator/CR conditions, workload readiness, bounded events and relevant
container logs. Trace Central -> Sensor connection -> Collector/node collection
and Scanner services according to the actual deployment topology. Distinguish
unreachable components, unhealthy components and missing permissions to observe
them. A healthy pod does not prove ingestion or current scans.

For Operator deployments inspect the served Central and SecuredCluster schemas
through openshift-api. Read [Central configuration options](../../openshift-docs/references/acs-4.11/installing/installing_ocp/install-central-config-options-ocp.md)
and [secured cluster configuration options](../../openshift-docs/references/acs-4.11/installing/installing_ocp/install-secured-cluster-config-options-ocp.md),
selecting the fields relevant to the symptom. Change the owning CR/Git source,
not reconciled Deployments. Do not assume an API group or field from memory.

For TLS failures compare the configured hostname, chain, expiry and trust on each
side without exposing private keys. Read [trusted CAs](../../openshift-docs/references/acs-4.11/configuration/add-trusted-ca.md)
and [internal certificate rotation](../../openshift-docs/references/acs-4.11/configuration/internal-certificate-authority-rotation-for-rhacs.md)
before a high-risk certificate change. Never disable TLS verification as a repair.
After approval verify reconnection, ingestion and the original failed operation.
