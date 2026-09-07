<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can connect a virtual machine (VM) to a user-defined network (UDN) on the VM’s primary interface. The primary UDN replaces the default pod network in your specified namespace. You can define the primary UDN per project, where each project can use its specific subnet and topology.

OpenShift Virtualization supports the namespace-scoped `UserDefinedNetwork` and the cluster-scoped `ClusterUserDefinedNetwork` custom resource definitions (CRD).

> [!NOTE]
> You must add the `k8s.ovn.org/primary-user-defined-network` label when you create a namespace that is to be used with user-defined networks.

Cluster administrators can configure a primary `UserDefinedNetwork` CRD to create a tenant network that isolates the tenant namespace from other namespaces without requiring network policies. Additionally, cluster administrators can use the `ClusterUserDefinedNetwork` CRD to create a shared OVN network across multiple namespaces.

With the layer 2 topology, OVN-Kubernetes creates an overlay network between nodes. You can use this overlay network to connect VMs on different nodes without having to configure any additional physical networking infrastructure.

The layer 2 topology enables seamless migration of VMs without the need for Network Address Translation (NAT) because persistent IP addresses are preserved across cluster nodes during live migration.

> [!NOTE]
> You can use the Ethernet Virtual Private Network’s (EVPN) Border Gateway Protocol (BGP) control plane to extend layer 2 connectivity between VMs running on different OpenShift Container Platform clusters. BGP EVPN support for primary cluster-scoped UDNs enables deeper integration with data center networks for your virtualized workloads. For more information, see "About BGP EVPN for primary cluster user-defined networks" in the Additional resources section.

You must consider the following limitations before implementing a primary UDN:

- You cannot use the `virtctl ssh` command to configure SSH access to a VM.

- You cannot use the `oc port-forward` command to forward ports to a VM.

- You cannot use headless services to access a VM.

# Create a primary user-defined network by using the web console

You can use the OpenShift Container Platform web console to create a primary namespace-scoped `UserDefinedNetwork` (UDN) or a cluster-scoped `ClusterUserDefinedNetwork` custom resource definition (CRD).

The UDN serves as the default primary network for pods and VMs that you create in namespaces associated with the network.

After you define the custom primary overlay network, you can create namespaces that are associated with the cluster-scoped UDN.

## Creating a namespace for user-defined networks by using the web console

You can create a namespace to be used with primary user-defined networks (UDNs) by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- Log in to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the **Administrator** perspective, click **Administration** → **Namespaces**.

2.  Click **Create Namespace**.

3.  In the **Name** field, specify a name for the namespace. The name must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character.

4.  In the **Labels** field, add the `k8s.ovn.org/primary-user-defined-network` label.

5.  Optional: If the namespace is to be used with an existing cluster-scoped UDN, add the appropriate labels as defined in the `spec.namespaceSelector` field in the `ClusterUserDefinedNetwork` custom resource.

6.  Optional: Specify a default network policy.

7.  Click **Create** to create the namespace.

</div>

## Creating a primary namespace-scoped user-defined network by using the web console

You can create an isolated primary network in your project namespace by creating a `UserDefinedNetwork` custom resource in the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

- You have created a namespace and applied the `k8s.ovn.org/primary-user-defined-network` label. For more information, see "Creating a namespace for user-defined networks by using the web console".

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the **Administrator** perspective, click **Networking** → **UserDefinedNetworks**.

2.  Click **Create UserDefinedNetwork**.

3.  From the **Project name** list, select the namespace that you previously created.

4.  Specify a value in the **Subnet** field.

5.  Click **Create**. The user-defined network serves as the default primary network for pods and virtual machines that you create in this namespace.

</div>

## Creating a cluster-scoped network to connect pods directly to an external network

You can connect one or more projects to a physical network for direct layer 2 access to data center resources through a `ClusterUserDefinedNetwork` custom resource in the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, go to **Virtualization** → **Networking**.

2.  Click **Virtual machine networks** in the navigation pane.

3.  Click **Create**. The **Create virtual machine network** wizard is displayed.

4.  Give details about the network on the **Network definition** page:

    1.  Enter a name for the network in the **Name** field.

    2.  Select a physical network through an `OpenvSwitch` bridge from the **Select physical network** list.

    3.  Enter the maximum transmission unit (MTU).

        > [!NOTE]
        > An MTU, measured in bytes, is the largest allowable size of a data packet. Ensure that all underlying physical network equipment supports this MTU, or higher.

    4.  Optional: Select the **VLAN ID** checkbox to enter VLAN tagging information. If you tag traffic with a VLAN ID, you must configure your physical switch with a VLAN trunk that includes the VLAN ID that you choose.

5.  Click **Next**.

6.  Select the projects that the network should be made available to on the **Project mapping** page. By default, all projects have access to the network.

7.  Click **Create**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Navigate to the **Virtualization** → **Virtual machine networks** page.

2.  Click the **OVN localnet** tab.

3.  Verify that your new network is displayed in the list.

</div>

## Creating a primary cluster-scoped user-defined network by using the web console

You can connect multiple namespaces to the same primary user-defined network (UDN) by creating a `ClusterUserDefinedNetwork` custom resource in the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From the **Administrator** perspective, click **Networking** → **UserDefinedNetworks**.

2.  From the **Create** list, select **ClusterUserDefinedNetwork**.

3.  In the **Name** field, specify a name for the cluster-scoped UDN.

4.  Specify a value in the **Subnet** field.

5.  In the **Project(s) Match Labels** field, add the appropriate labels to select namespaces that the cluster UDN applies to.

6.  Click **Create**. The cluster-scoped UDN serves as the default primary network for pods and virtual machines located in namespaces that contain the labels that you specified in step 5.

</div>

# Create a primary user-defined network by using the CLI

You can create a primary `UserDefinedNetwork` or `ClusterUserDefinedNetwork` custom resource definition (CRD) by using the OpenShift CLI (`oc`). After you define the custom primary overlay network, you can create namespaces that are associated with the cluster-scoped UDN.

## Creating a namespace for user-defined networks by using the CLI

You can create a namespace to be used with primary user-defined networks (UDNs) by using the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with `cluster-admin` permissions.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Namespace` object as a YAML file similar to the following example:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: my-namespace
      labels:
        k8s.ovn.org/primary-user-defined-network: ""
    # ...
    ```

    The `k8s.ovn.org/primary-user-defined-network` label is required for the namespace to be associated with a UDN. If the namespace is to be used with an existing cluster UDN, you must also add the appropriate labels that are defined in the `spec.namespaceSelector` field of the `ClusterUserDefinedNetwork` custom resource.

2.  Apply the `Namespace` manifest by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

</div>

## Creating a primary namespace-scoped user-defined network by using the CLI

You can create an isolated primary network in your project namespace by using the CLI. You must use the OVN-Kubernetes layer 2 topology and enable persistent IP address allocation in the user-defined network (UDN) configuration to ensure VM live migration support.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have created a namespace and applied the `k8s.ovn.org/primary-user-defined-network` label.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `UserDefinedNetwork` object to specify the custom network configuration.

    Example `UserDefinedNetwork` manifest:

    ``` yaml
    apiVersion: k8s.ovn.org/v1
    kind: UserDefinedNetwork
    metadata:
      name: udn-l2-net
      namespace: my-namespace
    spec:
      topology: Layer2
      layer2:
        role: Primary
        subnets:
          - "10.0.0.0/24"
          - "2001:db8::/60"
        ipam:
          lifecycle: Persistent
    ```

    - `metadata.name` specifies the name of the `UserDefinedNetwork` custom resource.

    - `metadata.namespace` specifies the namespace in which the VM is located. The namespace must have the `k8s.ovn.org/primary-user-defined-network` label. The namespace must not be `default`, an `openshift-*` namespace, or match any global namespaces that are defined by the Cluster Network Operator (CNO).

    - `spec.topology` specifies the topological configuration of the network. The required value is `Layer2`. A `Layer2` topology creates a logical switch that is shared by all nodes.

    - `spec.layer2.role` specifies whether the UDN is primary or secondary. The `Primary` role means that the UDN acts as the primary network for the VM and all default traffic passes through this network.

    - `spec.layer2.ipam.lifecycle` specifies that virtual workloads have consistent IP addresses across reboots and migration. The `spec.layer2.subnets` field is required when `ipam.lifecycle: Persistent` is specified.

2.  Apply the `UserDefinedNetwork` manifest by running the following command:

    ``` terminal
    $ oc apply -f --validate=true <filename>.yaml
    ```

</div>

## Creating a primary cluster-scoped user-defined network by using the CLI

You can connect multiple namespaces to the same primary user-defined network (UDN) to achieve native tenant isolation by using the CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with `cluster-admin` privileges.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `ClusterUserDefinedNetwork` object to specify the custom network configuration.

    Example `ClusterUserDefinedNetwork` manifest:

    ``` yaml
    apiVersion: k8s.ovn.org/v1
    kind: ClusterUserDefinedNetwork
    metadata:
      name: cudn-l2-net
    spec:
      namespaceSelector:
        matchExpressions:
        - key: kubernetes.io/metadata.name
          operator: In
          values: ["red-namespace", "blue-namespace"]
      network:
        topology: Layer2
        layer2:
          role: Primary
          ipam:
            lifecycle: Persistent
          subnets:
            - 203.203.0.0/16
    ```

    - `metadata.name` specifies the name of the `ClusterUserDefinedNetwork` custom resource.

    - `spec.namespaceSelector` specifies the set of namespaces that the cluster UDN applies to. The namespace selector must not point to `default`, an `openshift-*` namespace, or any global namespaces that are defined by the Cluster Network Operator (CNO).

    - `spec.namespaceSelector.matchExpressions` specifies the type of selector. In this example, the `matchExpressions` selector selects objects that have the label `kubernetes.io/metadata.name` with the value `red-namespace` or `blue-namespace`.

    - `spec.namespaceSelector.matchExpressions.operator` specifies the type of operator. Possible values are `In`, `NotIn`, and `Exists`.

    - `spec.network.topology` specifies the topological configuration of the network. The required value is `Layer2`. A `Layer2` topology creates a logical switch that is shared by all nodes.

    - `spec.network.layer2.role` specifies whether the UDN is primary or secondary. The `Primary` role means that the UDN acts as the primary network for the VM and all default traffic passes through this network.

2.  Apply the `ClusterUserDefinedNetwork` manifest by running the following command:

    ``` terminal
    $ oc apply -f --validate=true <filename>.yaml
    ```

</div>

# Attach a virtual machine to the primary user-defined network

You can connect a virtual machine (VM) to the primary user-defined network (UDN) by requesting the pod network attachment and configuring the interface binding.

OpenShift Virtualization supports the following network binding plugins to connect the network interface to the VM:

Layer 2 bridge
The Layer 2 bridge binding creates a direct Layer 2 connection between the VM’s virtual interface and the virtual switch of the UDN.

Passt
The Plug a Simple Socket Transport (passt) binding provides a user-space networking solution that integrates seamlessly with the pod network, providing better integration with the OpenShift Container Platform networking ecosystem.

Passt binding has the following benefits:

- You can define readiness and liveness HTTP probes to configure VM health checks.

- You can use Red Hat Advanced Cluster Security to monitor TCP traffic within the cluster with detailed insights.

> [!IMPORTANT]
> Using the passt binding plugin to attach a VM to the primary UDN is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

## Creating a virtual machine in a namespace with a primary user-defined network by using the web console

You can create a virtual machine (VM) in a namespace that is configured to use a primary user-defined network (UDN) by using the OpenShift Container Platform web console.

By default, the VM automatically connects to the primary UDN using the Layer 2 bridge (`l2bridge`) network binding plugin.

> [!NOTE]
> When creating the virtual machine, verify that the default network interface type is automatically set to `L2 bridge` and the network attachment is configured for the `pod` network.

<div>

<div class="title">

Prerequisites

</div>

- You have a namespace configured and labeled for a primary user-defined network.

- You are logged in to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Click **Virtualization** → **VirtualMachines**.

2.  Select the UDN-configured namespace from the **Project** drop-down list.

3.  Click **Create** → **With Wizard**.

4.  Configure the VM specifications in the wizard and click **Create VirtualMachine**.

</div>

## Attaching a virtual machine to the primary user-defined network by using the CLI

You can connect a virtual machine (VM) to the primary user-defined network (UDN) by using the OpenShift CLI (`oc`).

> [!IMPORTANT]
> Using the passt binding plugin to attach a VM to the primary UDN is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `VirtualMachine` manifest to add the UDN interface details, as in the following example:

    Example `VirtualMachine` manifest:

    ``` yaml
    apiVersion: kubevirt.io/v1
    kind: VirtualMachine
    metadata:
      name: example-vm
      namespace: my-namespace
    spec:
      template:
        spec:
          domain:
            devices:
              interfaces:
                - name: default
                  binding:
                    name: l2bridge
    # ...
          networks:
          - name: default
            pod: {}
    # ...
    ```

    - `metadata.namespace` specifies the namespace in which the VM is located. This value must match the namespace in which the UDN is defined.

    - `spec.template.spec.domain.devices.interfaces.name` specifies the name of the user-defined network interface.

    - `spec.template.spec.domain.devices.interfaces.binding.name` specifies the name of the binding plugin that is used to connect the interface to the VM. The possible values are `l2bridge` and `passt`. The default value is `l2bridge`.

    - `spec.template.spec.networks.name` specifies the name of the network. This must match the value of the `spec.template.spec.domain.devices.interfaces.name` field.

2.  Optional: If you are using the Plug a Simple Socket Transport (passt) network binding plugin, set the `hco.kubevirt.io/deployPasstNetworkBinding` annotation to `true` in the `HyperConverged` custom resource (CR) by running the following command:

    ``` terminal
    $ oc annotate hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv hco.kubevirt.io/deployPasstNetworkBinding=true --overwrite
    ```

3.  Apply the `VirtualMachine` manifest by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

</div>

# Additional resources

- [About user-defined networks](../../networking/multiple_networks/primary_networks/about-user-defined-networks.md#about-user-defined-networks)

- [About BGP EVPN for primary cluster user-defined networks](../../networking/advanced_networking/bgp_evpn_udn/about-bgp-evpn-user-defined-networks.md#about-bgp-evpn-user-defined-networks)
