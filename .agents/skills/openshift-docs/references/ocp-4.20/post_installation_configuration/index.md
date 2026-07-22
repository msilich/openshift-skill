<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After installing OpenShift Container Platform, a cluster administrator can configure and customize the following components:

- Machine

- Bare metal

- Cluster

- Node

- Network

- Storage

- Users

- Alerts and notifications

# Postinstallation configuration tasks

You can perform the postinstallation configuration tasks to configure your environment to meet your needs.

The following lists details these configurations:

- [Configure operating system features](../machine_configuration/index.md#machine-config-overview): The Machine Config Operator (MCO) manages `MachineConfig` objects. By using the MCO, you can configure nodes and custom resources.

- [Configure cluster features](cluster-tasks.md#post-install-cluster-tasks). You can modify the following features of an OpenShift Container Platform cluster:

  - Image registry

  - Networking configuration

  - Image build behavior

  - Identity provider

  - The etcd configuration

  - Machine set creation to handle the workloads

  - Cloud provider credential management

- [Configuring a private cluster](configuring-private-cluster.md#configuring-private-cluster): By default, the installation program provisions OpenShift Container Platform by using a publicly accessible DNS and endpoints. To make your cluster accessible only from within an internal network, configure the following components to make them private:

  - DNS

  - Ingress Controller

  - API server

- [Perform node operations](node-tasks.md#post-install-node-tasks): By default, OpenShift Container Platform uses Red Hat Enterprise Linux CoreOS (RHCOS) compute machines. You can perform the following node operations:

  - Add and remove compute machines.

  - Add and remove taints and tolerations.

  - Configure the maximum number of pods per node.

  - Enable Device Manager.

- [Configure users](preparing-for-users.md#post-install-preparing-for-users): Users can authenticate themselves to the API by using OAuth access tokens. You can configure OAuth to perform the following tasks:

  - Specify an identity provider.

  - Use role-based access control to define and grant permissions to users.

  - Install an Operator from the software catalog.

- [Configuring alert notifications](configuring-alert-notifications.md#configuring-alert-notifications): By default, firing alerts are displayed on the Alerting UI of the web console. You can also configure OpenShift Container Platform to send alert notifications to external systems.
