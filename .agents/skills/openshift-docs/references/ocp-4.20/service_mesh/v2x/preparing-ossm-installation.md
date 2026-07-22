<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you can install Red Hat OpenShift Service Mesh, you must subscribe to OpenShift Container Platform and install OpenShift Container Platform in a supported configuration.

# Prerequisites

- Maintain an active OpenShift Container Platform subscription on your Red Hat account. If you do not have a subscription, contact your sales representative for more information.

- Review the [OpenShift Container Platform 4.17 overview](../../architecture/architecture-installation.md#installation-overview_architecture-installation).

- Install OpenShift Container Platform 4.17. If you are installing Red Hat OpenShift Service Mesh on a [restricted network](../../installing/overview/installing-preparing.md#supported-installation-methods-for-different-platforms), follow the instructions for your chosen OpenShift Container Platform infrastructure.

  - [Install OpenShift Container Platform 4.17 on AWS](../../installing/installing_aws/ipi/installing-aws-default.md#installing-aws-default)

  - [Install OpenShift Container Platform 4.17 on AWS with user-provisioned infrastructure](../../installing/installing_aws/upi/installing-aws-user-infra.md#installing-aws-user-infra)

  - [Install OpenShift Container Platform 4.17 on bare metal](../../installing/installing_bare_metal/upi/installing-bare-metal.md#installing-bare-metal)

  - [Install OpenShift Container Platform 4.17 on vSphere](../../installing/installing_vsphere/upi/installing-vsphere.md#installing-vsphere)

  - [Install OpenShift Container Platform 4.17 on IBM Z® and IBM® LinuxONE](../../installing/installing_ibm_z/upi/installing-ibm-z.md#installing-ibm-z)

  - [Install OpenShift Container Platform 4.17 on IBM Power®](../../installing/installing_ibm_power/installing-ibm-power.md#installing-ibm-power)

- Install the version of the OpenShift Container Platform command-line utility (the `oc` client tool) that matches your OpenShift Container Platform version and add it to your path.

  - If you are using OpenShift Container Platform 4.17, see [About the OpenShift CLI](../../cli_reference/openshift_cli/getting-started-cli.md#cli-about-cli_cli-developer-commands).

For additional information about Red Hat OpenShift Service Mesh lifecycle and supported platforms, refer to the [Support Policy](https://access.redhat.com/support/policy/updates/openshift#ossm).

# Supported configurations

The following configurations are supported for the current release of Red Hat OpenShift Service Mesh.

## Supported platforms

The Red Hat OpenShift Service Mesh Operator supports multiple versions of the `ServiceMeshControlPlane` resource. Version 2.6 Service Mesh control planes are supported on the following platform versions:

- Red Hat OpenShift Container Platform version 4.10 or later

- Red Hat OpenShift Dedicated version 4

- Azure Red Hat OpenShift (ARO) version 4

- Red Hat OpenShift Service on AWS

- Red Hat OpenShift Service on AWS classic architecture

## Unsupported configurations

Explicitly unsupported cases include:

- OpenShift Online is not supported for Red Hat OpenShift Service Mesh.

- Red Hat OpenShift Service Mesh does not support the management of microservices outside the cluster where Service Mesh is running.

## Supported network configurations

Red Hat OpenShift Service Mesh supports the following network configurations.

- OpenShift-SDN

- OVN-Kubernetes is available on all supported versions of OpenShift Container Platform.

- Third-Party Container Network Interface (CNI) plugins that have been certified on OpenShift Container Platform and passed Service Mesh conformance testing. See [Certified OpenShift CNI Plug-ins](https://access.redhat.com/articles/5436171) for more information.

## Supported configurations for Service Mesh

- This release of Red Hat OpenShift Service Mesh is only available on OpenShift Container Platform x86_64, IBM Z®, and IBM Power®.

  - IBM Z® is only supported on OpenShift Container Platform 4.10 and later.

  - IBM Power® is only supported on OpenShift Container Platform 4.10 and later.

- Configurations where all Service Mesh components are contained within a single OpenShift Container Platform cluster.

- Configurations that do not integrate external services such as virtual machines.

- Red Hat OpenShift Service Mesh does not support `EnvoyFilter` configuration except where explicitly documented.

## Supported configurations for Kiali

- The Kiali console is only supported on the two most recent releases of the Google Chrome, Microsoft Edge, Mozilla Firefox, or Apple Safari browsers.

- The `openshift` authentication strategy is the only supported authentication configuration when Kiali is deployed with Red Hat OpenShift Service Mesh (OSSM). The `openshift` strategy controls access based on the individual’s role-based access control (RBAC) roles of the OpenShift Container Platform.

## Supported configurations for Distributed Tracing

- Jaeger agent as a sidecar is the only supported configuration for Jaeger. Jaeger as a daemonset is not supported for multitenant installations or OpenShift Dedicated.

## Supported WebAssembly module

- 3scale WebAssembly is the only provided WebAssembly module. You can create custom WebAssembly modules.

# Next steps

- [Install Red Hat OpenShift Service Mesh](installing-ossm.md#installing-ossm) in your OpenShift Container Platform environment.
