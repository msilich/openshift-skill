<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

RHCOS was created and tuned to be deployed in OpenShift Container Platform with few if any changes needed to RHCOS nodes. Every organization adopting OpenShift Container Platform has its own requirements for system hardening. As a RHEL system with OpenShift-specific modifications and features added (such as Ignition, ostree, and a read-only `/usr` to provide limited immutability), RHCOS can be hardened just as you would any RHEL system. Differences lie in the ways you manage the hardening.

A key feature of OpenShift Container Platform and its Kubernetes engine is to be able to quickly scale applications and infrastructure up and down as needed. Unless it is unavoidable, you do not want to make direct changes to RHCOS by logging into a host and adding software or changing settings. You want to have the OpenShift Container Platform installer and control plane manage changes to RHCOS so new nodes can be spun up without manual intervention.

So, if you are setting out to harden RHCOS nodes in OpenShift Container Platform to meet your security needs, you should consider both what to harden and how to go about doing that hardening.

# Choosing what to harden in RHCOS

For information on how to approach security for any RHEL system, see the [RHEL 9 Security Hardening](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/security_hardening/index#scanning-container-and-container-images-for-vulnerabilities_scanning-the-system-for-security-compliance-and-vulnerabilities) guide.

Use this guide to learn how to approach cryptography, evaluate vulnerabilities, and assess threats to various services. Likewise, you can learn how to scan for compliance standards, check file integrity, perform auditing, and encrypt storage devices.

With the knowledge of what features you want to harden, you can then decide how to harden them in RHCOS.

# Choosing how to harden RHCOS

Direct modification of RHCOS systems in OpenShift Container Platform is discouraged. Instead, you should think of modifying systems in pools of nodes, such as worker nodes and control plane nodes. When a new node is needed, in non-bare metal installs, you can request a new node of the type you want and it will be created from an RHCOS image plus the modifications you created earlier.

There are opportunities for modifying RHCOS before installation, during installation, and after the cluster is up and running.

## Hardening before installation

For bare metal installations, you can add hardening features to RHCOS before beginning the OpenShift Container Platform installation. For example, you can add kernel options when you boot the RHCOS installer to turn security features on or off, such as various SELinux booleans or low-level settings, such as symmetric multithreading.

> [!WARNING]
> Disabling SELinux on RHCOS nodes is not supported.

Although bare metal RHCOS installations are more difficult, they offer the opportunity of getting operating system changes in place before starting the OpenShift Container Platform installation. This can be important when you need to ensure that certain features, such as disk encryption or special networking settings, be set up at the earliest possible moment.

## Hardening during installation

You can interrupt the OpenShift Container Platform installation process and change Ignition configs. Through Ignition configs, you can add your own files and systemd services to the RHCOS nodes. You can also make some basic security-related changes to the `install-config.yaml` file used for installation. Contents added in this way are available at each node’s first boot.

## Hardening after the cluster is running

After the OpenShift Container Platform cluster is up and running, there are several ways to apply hardening features to RHCOS:

- Daemon set: If you need a service to run on every node, you can add that service with a [Kubernetes `DaemonSet` object](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/).

- Machine config: `MachineConfig` objects contain a subset of Ignition configs in the same format. By applying machine configs to all worker or control plane nodes, you can ensure that the next node of the same type that is added to the cluster has the same changes applied.

All of the features noted here are described in the OpenShift Container Platform product documentation.

<div>

<div class="title">

Additional resources

</div>

- [OpenShift Security Guide](https://access.redhat.com/articles/5059881)

- [Choosing how to configure RHCOS](../../architecture/architecture-rhcos.md#rhcos-deployed_architecture-rhcos)

- [Modifying Nodes](../../nodes/nodes/nodes-nodes-managing.md#nodes-nodes-managing)

- [Manually creating the installation configuration file](../../installing/installing_bare_metal/upi/installing-bare-metal.md#installation-initializing-manual_installing-bare-metal)

- [Creating the Kubernetes manifest and Ignition config files](../../installing/installing_bare_metal/upi/installing-bare-metal.md#installation-user-infra-generate-k8s-manifest-ignition_installing-bare-metal)

- [Installing RHCOS by using an ISO image](../../installing/installing_bare_metal/upi/installing-bare-metal.md#installation-user-infra-machines-iso_installing-bare-metal)

- [Customizing nodes](../../installing/install_config/installing-customizing.md#installing-customizing)

- [Adding kernel arguments to nodes](../../nodes/nodes/nodes-nodes-managing.md#nodes-nodes-kernel-arguments_nodes-nodes-managing)

- [Optional configuration parameters](../../installing/installing_aws/installation-config-parameters-aws.md#installation-configuration-parameters-optional_installation-config-parameters-aws)

- [Support for FIPS cryptography](../../installing/overview/installing-fips.md#installing-fips)

- [RHEL core crypto components](https://access.redhat.com/articles/3359851)

</div>
