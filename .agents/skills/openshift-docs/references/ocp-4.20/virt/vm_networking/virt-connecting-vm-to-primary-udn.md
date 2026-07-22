<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can connect a virtual machine (VM) to a user-defined network (UDN) on the VM’s primary interface. The primary UDN replaces the default pod network in your specified namespace. You can define the primary UDN per project, where each project can use its specific subnet and topology.

OpenShift Virtualization supports the namespace-scoped `UserDefinedNetwork` and the cluster-scoped `ClusterUserDefinedNetwork` custom resource definitions (CRD).

Cluster administrators can configure a primary `UserDefinedNetwork` CRD to create a tenant network that isolates the tenant namespace from other namespaces without requiring network policies. Additionally, cluster administrators can use the `ClusterUserDefinedNetwork` CRD to create a shared OVN network across multiple namespaces.

> [!NOTE]
> You must add the `k8s.ovn.org/primary-user-defined-network` label when you create a namespace that is to be used with user-defined networks.

With the layer 2 topology, OVN-Kubernetes creates an overlay network between nodes. You can use this overlay network to connect VMs on different nodes without having to configure any additional physical networking infrastructure.

The layer 2 topology enables seamless migration of VMs without the need for Network Address Translation (NAT) because persistent IP addresses are preserved across cluster nodes during live migration.

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

## Attaching a virtual machine to the primary user-defined network by using the web console

You can connect a virtual machine (VM) to the primary user-defined network (UDN) by using the OpenShift Container Platform web console. VMs that are created in a namespace where the primary UDN is configured are automatically attached to the UDN with the Layer 2 bridge network binding plugin.

To attach a VM to the primary UDN by using the Plug a Simple Socket Transport (passt) binding, enable the plugin and configure the VM network interface in the web console.

> [!IMPORTANT]
> Using the passt binding plugin to attach a VM to the primary UDN is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Follow these steps to enable the passt network binding plugin Technology Preview feature:

    1.  From the **Virtualization** perspective, click **Overview**.

    2.  On the **Virtualization** page, click the **Settings** tab.

    3.  Click **Preview features** and set **Enable Passt binding for primary user-defined networks** to on.

2.  From the **Virtualization** perspective, click **VirtualMachines**.

3.  Select a VM to open the **VirtualMachine details** page.

4.  Click the **Configuration** tab.

5.  Click **Network**.

6.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) on the **Network interfaces** page and select **Edit**.

7.  In the **Edit network interface** dialog, select the default pod network attachment from the **Network** list.

8.  Expand **Advanced** and then select the **Passt** binding.

9.  Click **Save**.

10. If your VM is running, restart it for the changes to take effect.

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
                - name: udn-l2-net
                  binding:
                    name: l2bridge
    # ...
          networks:
          - name: udn-l2-net
            pod: {}
    # ...
    ```

    - `metadata.namespace` specifies the namespace in which the VM is located. This value must match the namespace in which the UDN is defined.

    - `spec.template.spec.domain.devices.interfaces.name` specifies the name of the user-defined network interface.

    - `spec.template.spec.domain.devices.interfaces.binding.name` specifies the name of the binding plugin that is used to connect the interface to the VM. The possible values are `l2bridge` and `passt`. The default value is `l2bridge`.

    - `spec.template.spec.networks.name` specifies the name of the network. This must match the value of the `spec.template.spec.domain.devices.interfaces.name` field.

2.  Optional: If you are using the Plug a Simple Socket Transport (passt) network binding plugin, set the `hco.kubevirt.io/deployPasstNetworkBinding` annotation to `true` in the `HyperConverged` custom resource (CR) by running the following command:

    ``` terminal
    $ oc annotate hco kubevirt-hyperconverged -n kubevirt-hyperconverged hco.kubevirt.io/deployPasstNetworkBinding=true --overwrite
    ```

3.  Apply the `VirtualMachine` manifest by running the following command:

    ``` terminal
    $ oc apply -f <filename>.yaml
    ```

</div>

# Additional resources

- [About user-defined networks](../../networking/multiple_networks/primary_networks/about-user-defined-networks.md#about-user-defined-networks)
