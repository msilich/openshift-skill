<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As an administrator, you can expose a set of host and virtual machine (VM) metrics to a guest VM by enabling the `downwardMetrics` feature gate and configuring a downward metrics device. You can view these metrics by using the command line or the `vm-dump-metrics` tool.

> [!NOTE]
> On Red Hat Enterprise Linux (RHEL) 9, use the command line to view downward metrics.
>
> The `vm-dump-metrics` tool is not supported on the Red Hat Enterprise Linux (RHEL) 9 platform.

# Enabling or disabling the downward metrics feature gate in a YAML file

To expose downward metrics for a host virtual machine, you can enable the `downwardMetrics` feature gate by editing a YAML file.

<div>

<div class="title">

Prerequisites

</div>

- You must have administrator privileges to enable the feature gate.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Open the HyperConverged custom resource (CR) in your default editor by running the following command:

    ``` terminal
    $ oc edit hyperconverged kubevirt-hyperconverged -n openshift-cnv
    ```

2.  Choose to enable or disable the downwardMetrics feature gate as follows:

    - To enable the `downwardMetrics` feature gate, add and then set `spec.featureGates.downwardMetrics` to `true`. For example:

      ``` yaml
      apiVersion: hco.kubevirt.io/v1beta1
      kind: HyperConverged
      metadata:
        name: kubevirt-hyperconverged
        namespace: openshift-cnv
      spec:
          featureGates:
            downwardMetrics: true
      # ...
      ```

    - To disable the `downwardMetrics` feature gate, set `spec.featureGates.downwardMetrics` to `false`. For example:

      ``` yaml
      apiVersion: hco.kubevirt.io/v1beta1
      kind: HyperConverged
      metadata:
        name: kubevirt-hyperconverged
        namespace: openshift-cnv
      spec:
          featureGates:
            downwardMetrics: false
      # ...
      ```

</div>

# Enabling or disabling the downward metrics feature gate from the CLI

To expose downward metrics for a host virtual machine, you can enable the `downwardMetrics` feature gate by using the command line.

<div>

<div class="title">

Prerequisites

</div>

- You must have administrator privileges to enable the feature gate.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Choose to enable or disable the `downwardMetrics` feature gate as follows:

  - Enable the `downwardMetrics` feature gate by running the command shown in the following example:

    ``` terminal
    $ oc patch hco kubevirt-hyperconverged -n openshift-cnv \
      --type json -p '[{"op": "replace", "path": \
      "/spec/featureGates/downwardMetrics", \
      "value": true}]'
    ```

  - Disable the `downwardMetrics` feature gate by running the command shown in the following example:

    ``` terminal
    $ oc patch hco kubevirt-hyperconverged -n openshift-cnv \
      --type json -p '[{"op": "replace", "path": \
      "/spec/featureGates/downwardMetrics", \
      "value": false}]'
    ```

</div>

# Configuring a downward metrics device

You can enable the capturing of downward metrics for a host VM by creating a configuration file that includes a `downwardMetrics` device. Adding this device establishes that the metrics are exposed through a `virtio-serial` port.

<div>

<div class="title">

Prerequisites

</div>

- You must first enable the `downwardMetrics` feature gate.

</div>

<div>

<div class="title">

Procedure

</div>

- Edit or create a YAML file that includes a `downwardMetrics` device, as shown in the following example:

  ``` yaml
  apiVersion: kubevirt.io/v1
  kind: VirtualMachine
  metadata:
    name: fedora
    namespace: default
  spec:
    dataVolumeTemplates:
      - metadata:
          name: fedora-volume
        spec:
          sourceRef:
            kind: DataSource
            name: fedora
            namespace: openshift-virtualization-os-images
          storage:
            resources: {}
    instancetype:
      name: u1.medium
    runStrategy: Always
    template:
      metadata:
        labels:
          app.kubernetes.io/name: headless
      spec:
        domain:
          devices:
            downwardMetrics: {}
        subdomain: headless
        volumes:
          - dataVolume:
              name: fedora-volume
            name: rootdisk
          - cloudInitNoCloud:
              userData: |
                #cloud-config
                chpasswd:
                  expire: false
                password: '<password>'
                user: fedora
            name: cloudinitdisk
  ```

  - The `downwardMetrics` device.

  - The password for the `fedora` user.

</div>

# Viewing downward metrics by using the CLI

You can view downward metrics by entering a command from inside a guest virtual machine (VM).

<div>

<div class="title">

Procedure

</div>

- Run the following commands:

  ``` terminal
  $ sudo sh -c 'printf "GET /metrics/XML\n\n" > /dev/virtio-ports/org.github.vhostmd.1'
  ```

  ``` terminal
  $ sudo cat /dev/virtio-ports/org.github.vhostmd.1
  ```

</div>

# Additional resources

- [Viewing downward metrics by using the command line](virt-exposing-downward-metrics.md#virt-viewing-downward-metrics-cli_virt-exposing-downward-metrics)
