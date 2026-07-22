<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Keep a stable network across your OpenShift nodes, AWS Simple Storage Service (S3) storage, and cloud environments. Meeting these recommended network settings helps you ensure successful OpenShift API for Data Protection (OADP) backup and restore operations, even when using remote AWS S3 buckets.

# OADP network requirements

For a supported experience with OpenShift API for Data Protection (OADP), you should have a stable and resilient network across OpenShift nodes, AWS Simple Storage Service (S3)-compatible object storage, and in supported cloud environments that meet OpenShift network requirements.

For deployments that use remote S3 buckets located off-cluster with suboptimal data paths, such as high-latency or geographically distant locations, successful backup and restore operations require specific configurations. Ensure your network settings meet the following minimum requirements:

- Bandwidth (network upload speed to object storage): Greater than 2 Mbps for small backups and 10-100 Mbps depending on the data volume for larger backups.

- Packet loss: 1%

- Packet corruption: 1%

- Latency: 100 ms

Ensure that your OpenShift Container Platform network performs optimally and meets OpenShift Container Platform network requirements.

> [!IMPORTANT]
> Although Red Hat provides support for standard backup and restore failures, it does not provide support for failures caused by network settings that do not meet the recommended thresholds.

# Additional resources

- [Configuring network settings](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/configuring_network_settings/index)

- [About installing OADP](../installing/about-installing-oadp.md#about-installing-oadp)

- [Troubleshooting](../troubleshooting/troubleshooting.md#troubleshooting)
