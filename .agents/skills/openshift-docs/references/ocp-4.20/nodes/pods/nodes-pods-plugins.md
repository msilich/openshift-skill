<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Device plugins allow you to use a particular device type (GPU, InfiniBand, or other similar computing resources that require vendor-specific initialization and setup) in your OpenShift Container Platform pod without needing to write custom code.

# Understanding device plugins

A device plugin is a gRPC service running on nodes that manages specific hardware resources through an extension mechanism, enabling containers to consume these devices.

> [!IMPORTANT]
> OpenShift Container Platform supports the device plugin API, but the device plugin Containers are supported by individual vendors.

A device plugin is a gRPC service running on the nodes (external to the `kubelet`) that is responsible for managing specific hardware resources. Any device plugin must support following remote procedure calls (RPCs):

``` golang
service DevicePlugin {
      // GetDevicePluginOptions returns options to be communicated with Device
      // Manager
      rpc GetDevicePluginOptions(Empty) returns (DevicePluginOptions) {}

      // ListAndWatch returns a stream of List of Devices
      // Whenever a Device state change or a Device disappears, ListAndWatch
      // returns the new list
      rpc ListAndWatch(Empty) returns (stream ListAndWatchResponse) {}

      // Allocate is called during container creation so that the Device
      // Plug-in can run device specific operations and instruct Kubelet
      // of the steps to make the Device available in the container
      rpc Allocate(AllocateRequest) returns (AllocateResponse) {}

      // PreStartcontainer is called, if indicated by Device Plug-in during
      // registration phase, before each container start. Device plug-in
      // can run device specific operations such as resetting the device
      // before making devices available to the container
      rpc PreStartcontainer(PreStartcontainerRequest) returns (PreStartcontainerResponse) {}
}
```

## Example device plugins

- [Nvidia GPU device plugin for COS-based operating system](https://github.com/GoogleCloudPlatform/Container-engine-accelerators/tree/master/cmd/nvidia_gpu)

- [Nvidia official GPU device plugin](https://github.com/NVIDIA/k8s-device-plugin)

- [Solarflare device plugin](https://github.com/vikaschoudhary16/sfc-device-plugin)

- [KubeVirt device plugins: vfio and kvm](https://github.com/kubevirt/kubernetes-device-plugins)

- [Kubernetes device plugin for IBM® Crypto Express (CEX) cards](https://github.com/ibm-s390-cloud/k8s-cex-dev-plugin)

> [!NOTE]
> For easy device plugin reference implementation, there is a stub device plugin in the Device Manager code: ***vendor/k8s.io/kubernetes/pkg/kubelet/cm/deviceplugin/device_plugin_stub.go***.

## Methods for deploying a device plugin

- Daemon sets are the recommended approach for device plugin deployments.

- Upon start, the device plugin will try to create a UNIX domain socket at ***/var/lib/kubelet/device-plugin/*** on the node to serve RPCs from Device Manager.

- Since device plugins must manage hardware resources, access to the host file system, as well as socket creation, they must be run in a privileged security context.

- More specific details regarding deployment steps can be found with each device plugin implementation.

# Understanding the Device Manager

Device Manager advertises specialized node hardware resources through device plugins, enabling pods to consume hardware devices without requiring upstream code changes.

You can advertise specialized hardware without requiring any upstream code changes.

> [!IMPORTANT]
> OpenShift Container Platform supports the device plugin API, but the device plugin Containers are supported by individual vendors.

Device Manager advertises devices as **Extended Resources**. User pods can consume devices, advertised by Device Manager, using the same **Limit/Request** mechanism, which is used for requesting any other **Extended Resource**.

Upon start, the device plugin registers itself with Device Manager invoking `Register` on the ***/var/lib/kubelet/device-plugins/kubelet.sock*** and starts a gRPC service at ***/var/lib/kubelet/device-plugins/\<plugin\>.sock*** for serving Device Manager requests.

Device Manager, while processing a new registration request, invokes `ListAndWatch` remote procedure call (RPC) at the device plugin service. In response, Device Manager gets a list of **Device** objects from the plugin over a gRPC stream. Device Manager will keep watching on the stream for new updates from the plugin. On the plugin side, the plugin will also keep the stream open and whenever there is a change in the state of any of the devices, a new device list is sent to the Device Manager over the same streaming connection.

While handling a new pod admission request, Kubelet passes requested `Extended Resources` to the Device Manager for device allocation. Device Manager checks in its database to verify if a corresponding plugin exists or not. If the plugin exists and there are free allocatable devices as well as per local cache, `Allocate` RPC is invoked at that particular device plugin.

Additionally, device plugins can also perform several other device-specific operations, such as driver installation, device initialization, and device resets. These functionalities vary from implementation to implementation.

# Enabling Device Manager

Enable Device Manager to allow device plugins to advertise specialized node hardware resources and make them available to pods without requiring code changes.

Device Manager provides a mechanism for advertising specialized node hardware resources with the help of plugins known as device plugins.

<div>

<div class="title">

Procedure

</div>

1.  Obtain the label associated with the static `MachineConfigPool` CRD for the type of node you want to configure by entering the following command. Perform one of the following steps:

    1.  View the machine config:

        ``` terminal
        # oc describe machineconfig <name>
        ```

        For example:

        ``` terminal
        # oc describe machineconfig 00-worker
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Name:         00-worker
        Namespace:
        Labels:       machineconfiguration.openshift.io/role=worker
        ```

        </div>

        `machineconfiguration.openshift.io` is the label required for the Device Manager.

2.  Create a custom resource (CR) for your configuration change.

    <div class="formalpara">

    <div class="title">

    Sample configuration for a Device Manager CR

    </div>

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: KubeletConfig
    metadata:
      name: devicemgr
    spec:
      machineConfigPoolSelector:
        matchLabels:
           machineconfiguration.openshift.io: devicemgr
      kubeletConfig:
        feature-gates:
          - DevicePlugins=true
    ```

    </div>

    where:

    `metadata.name`
    Specifies a name to assign to the CR.

    `spec.machineConfigPoolSelector.matchLabels`
    Specifies the label from the Machine Config Pool.

    `spec.kubeletConfig.feature-gates`
    Specifies the `DevicePlugins` feature gate. Set to `true`.

3.  Create the Device Manager:

    ``` terminal
    $ oc create -f devicemgr.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    kubeletconfig.machineconfiguration.openshift.io/devicemgr created
    ```

    </div>

4.  Ensure that Device Manager was actually enabled by confirming that ***/var/lib/kubelet/device-plugins/kubelet.sock*** is created on the node. This is the UNIX domain socket on which the Device Manager gRPC server listens for new plugin registrations. This sock file is created when the Kubelet is started only if Device Manager is enabled.

</div>
