<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After installing OpenShift Container Platform, you can further expand and customize your cluster to your requirements, including storage configuration.

By default, containers operate by using the ephemeral storage or transient local storage. The ephemeral storage has a lifetime limitation. To store the data for a long time, you must configure persistent storage. You can configure storage by using one of the following methods:

Dynamic provisioning
You can dynamically provision storage on-demand by defining and creating storage classes that control different levels of storage, including storage access.

Static provisioning
You can use Kubernetes persistent volumes to make existing storage available to a cluster. Static provisioning can support various device configurations and mount options.

# Dynamic provisioning

Dynamic Provisioning allows you to create storage volumes on-demand, eliminating the need for cluster administrators to pre-provision storage. See [Dynamic provisioning](../storage/dynamic-provisioning.md#dynamic-provisioning).

# Recommended configurable storage technology

Review the recommended and configurable storage technologies for the given OpenShift Container Platform cluster application.

| Storage type          | Block            | File             | Object           |
|-----------------------|------------------|------------------|------------------|
| ROX                   | Yes              | Yes              | Yes              |
| RWX                   | No               | Yes              | Yes              |
| Registry              | Configurable     | Configurable     | Recommended      |
| Scaled registry       | Not configurable | Configurable     | Recommended      |
| Metrics               | Recommended      | Configurable     | Not configurable |
| Elasticsearch Logging | Recommended      | Configurable     | Not supported    |
| Loki Logging          | Not configurable | Not configurable | Recommended      |
| Apps                  | Recommended      | Recommended      | Not configurable |

Recommended and configurable storage technology

where:

`ROX`
Specifies `ReadOnlyMany` access mode.

`ROX.Yes`
Specifies that this access mode

`RWX`
Specifies `ReadWriteMany` access mode.

`Metrics`
Specifies Prometheus as the underlying technology used for metrics.

`Metrics.Configurable`
For metrics, using file storage with the `ReadWriteMany` (RWX) access mode is unreliable. If you use file storage, do not configure the RWX access mode on any persistent volume claims (PVCs) that are configured for use with metrics.

`Elasticsearch Logging.Configurable`
For logging, review the recommended storage solution in Configuring persistent storage for the log store section. Using NFS storage as a persistent volume or through NAS, such as Gluster, can corrupt the data. Therefore, NFS is not supported for Elasticsearch storage and LokiStack log store in OpenShift Container Platform Logging. You must use one persistent volume type per log store.

`Apps.Not configurable`
Specifies that object storage is not consumed through PVs or PVCs of OpenShift Container Platform. Apps must integrate with the object storage REST API.

> [!NOTE]
> A scaled registry is an OpenShift image registry where two or more pod replicas are running.

# Deploy Red Hat OpenShift Data Foundation

Red Hat OpenShift Data Foundation is a provider of agnostic persistent storage for OpenShift Container Platform supporting file, block, and object storage, either in-house or in hybrid clouds. As a Red Hat storage solution, Red Hat OpenShift Data Foundation is completely integrated with OpenShift Container Platform for deployment, management, and monitoring. For more information, see the [Red Hat OpenShift Data Foundation documentation](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation).

> [!IMPORTANT]
> OpenShift Data Foundation on top of Red Hat Hyperconverged Infrastructure (RHHI) for Virtualization, which uses hyperconverged nodes that host virtual machines installed with OpenShift Container Platform, is not a supported configuration. For more information about supported platforms, see the [Red Hat OpenShift Data Foundation Supportability and Interoperability Guide](https://access.redhat.com/articles/4731161).

| If you are looking for Red Hat OpenShift Data Foundation information about…​ | See the following Red Hat OpenShift Data Foundation documentation: |
|----|----|
| What’s new, known issues, notable bug fixes, and Technology Previews | [OpenShift Data Foundation 4.12 Release Notes](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/4.12_release_notes) |
| Supported workloads, layouts, hardware and software requirements, sizing and scaling recommendations | [Planning your OpenShift Data Foundation 4.12 deployment](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/planning_your_deployment) |
| Instructions on deploying OpenShift Data Foundation to use an external Red Hat Ceph Storage cluster | [Deploying OpenShift Data Foundation 4.12 in external mode](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/deploying_openshift_data_foundation_in_external_mode) |
| Instructions on deploying OpenShift Data Foundation to local storage on bare metal infrastructure | [Deploying OpenShift Data Foundation 4.12 using bare metal infrastructure](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/deploying_openshift_data_foundation_using_bare_metal_infrastructure) |
| Instructions on deploying OpenShift Data Foundation on Red Hat OpenShift Container Platform VMware vSphere clusters | [Deploying OpenShift Data Foundation 4.12 on VMware vSphere](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/deploying_openshift_data_foundation_on_vmware_vsphere) |
| Instructions on deploying OpenShift Data Foundation using Amazon Web Services for local or cloud storage | [Deploying OpenShift Data Foundation 4.12 using Amazon Web Services](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/deploying_openshift_data_foundation_using_amazon_web_services) |
| Instructions on deploying and managing OpenShift Data Foundation on existing Red Hat OpenShift Container Platform Google Cloud clusters | [Deploying and managing OpenShift Data Foundation 4.12 using Google Cloud](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/deploying_and_managing_openshift_data_foundation_using_google_cloud) |
| Instructions on deploying and managing OpenShift Data Foundation on existing Red Hat OpenShift Container Platform Azure clusters | [Deploying and managing OpenShift Data Foundation 4.12 using Microsoft Azure](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/deploying_openshift_data_foundation_using_microsoft_azure/index) |
| Instructions on deploying OpenShift Data Foundation to use local storage on IBM Power® infrastructure | [Deploying OpenShift Data Foundation on IBM Power®](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html-single/deploying_openshift_data_foundation_using_ibm_power/index) |
| Instructions on deploying OpenShift Data Foundation to use local storage on IBM Z® infrastructure | [Deploying OpenShift Data Foundation on IBM Z® infrastructure](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/deploying_openshift_data_foundation_using_ibm_z_infrastructure/index) |
| Allocating storage to core services and hosted applications in Red Hat OpenShift Data Foundation, including snapshot and clone | [Managing and allocating resources](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/managing_and_allocating_storage_resources) |
| Managing storage resources across a hybrid cloud or multicloud environment using the Multicloud Object Gateway (NooBaa) | [Managing hybrid and multicloud resources](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/managing_hybrid_and_multicloud_resources) |
| Safely replacing storage devices for Red Hat OpenShift Data Foundation | [Replacing devices](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/replacing_devices) |
| Safely replacing a node in a Red Hat OpenShift Data Foundation cluster | [Replacing nodes](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/replacing_nodes) |
| Scaling operations in Red Hat OpenShift Data Foundation | [Scaling storage](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/scaling_storage) |
| Monitoring a Red Hat OpenShift Data Foundation 4.12 cluster | [Monitoring Red Hat OpenShift Data Foundation 4.12](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/monitoring_openshift_data_foundation) |
| Resolve issues encountered during operations | [Troubleshooting OpenShift Data Foundation 4.12](https://access.redhat.com/documentation/en-us/red_hat_openshift_data_foundation/4.12/html/troubleshooting_openshift_data_foundation) |
| Migrating your OpenShift Container Platform cluster from version 3 to version 4 | [Migration](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.12/html/migrating_from_version_3_to_4/index) |
