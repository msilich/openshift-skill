<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use the Node Feature Discovery (NFD) Operator to detect and expose hardware features and system configuration as node-level information.

# About the Node Feature Discovery Operator

You can use the Node Feature Discovery Operator (NFD) to detect hardware features and system configuration on cluster nodes, labeling them with attributes such as PCI cards, kernel version, and CPU capabilities. These labels enable workload scheduling based on hardware requirements.

The NFD Operator can be found on the OperatorHub by searching for “Node Feature Discovery”.

# Installing the Node Feature Discovery Operator

As a cluster administrator, you can install the NFD Operator by using the OpenShift Container Platform CLI or the web console. The Node Feature Discovery (NFD) Operator orchestrates all resources needed to run the NFD daemon set.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster.

- You installed the OpenShift CLI (`oc`).

- You are logged in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

- **Method 1:** Install the NFD Operator by using the CLI:

  1.  Create the following `Namespace` custom resource (CR) that defines the `openshift-nfd` namespace, and then save the YAML in the `nfd-namespace.yaml` file. Set `cluster-monitoring` to `"true"`.

      ``` yaml
      apiVersion: v1
      kind: Namespace
      metadata:
        name: openshift-nfd
        labels:
          name: openshift-nfd
          openshift.io/cluster-monitoring: "true"
      ```

  2.  Create the namespace by running the following command:

      ``` terminal
      $ oc create -f nfd-namespace.yaml
      ```

  3.  Create the following `OperatorGroup` CR and save the YAML in the `nfd-operatorgroup.yaml` file:

      ``` yaml
      apiVersion: operators.coreos.com/v1
      kind: OperatorGroup
      metadata:
        generateName: openshift-nfd-
        name: openshift-nfd
        namespace: openshift-nfd
      spec:
        targetNamespaces:
        - openshift-nfd
      ```

  4.  Create the `OperatorGroup` CR by running the following command:

      ``` terminal
      $ oc create -f nfd-operatorgroup.yaml
      ```

  5.  Create the following `Subscription` CR and save the YAML in the `nfd-sub.yaml` file:

      <div class="formalpara">

      <div class="title">

      Example Subscription

      </div>

      ``` yaml
      apiVersion: operators.coreos.com/v1alpha1
      kind: Subscription
      metadata:
        name: nfd
        namespace: openshift-nfd
      spec:
        channel: "stable"
        installPlanApproval: Automatic
        name: nfd
        source: redhat-operators
        sourceNamespace: openshift-marketplace
      ```

      </div>

  6.  Create the subscription object by running the following command:

      ``` terminal
      $ oc create -f nfd-sub.yaml
      ```

  7.  Change to the `openshift-nfd` project:

      ``` terminal
      $ oc project openshift-nfd
      ```

- **Method 2:** Install the NFD Operator by using the web console:

  1.  In the OpenShift Container Platform web console, click **Ecosystem** → **Software Catalog**.

  2.  Choose **Node Feature Discovery** from the list of available Operators, and then click **Install**.

  3.  On the **Install Operator** page, select **A specific namespace on the cluster**, and then click **Install**. You do not need to create a namespace because it is created for you.

</div>

<div>

<div class="title">

Verification

</div>

- To verify a CLI installation, run the following command and confirm that the output shows a `Running` status:

  ``` terminal
  $ oc get pods
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                                      READY   STATUS    RESTARTS   AGE
  nfd-controller-manager-7f86ccfb58-vgr4x   2/2     Running   0          10m
  ```

  </div>

- To verify a web console installation, navigate to the **Ecosystem** → **Installed Operators** page and ensure that **Node Feature Discovery** is listed in the **openshift-nfd** project with a **Status** of `InstallSucceeded`.

  > [!NOTE]
  > During installation an Operator might display a **Failed** status. If the installation later succeeds with an `InstallSucceeded` message, you can ignore the **Failed** message.

</div>

<div class="formalpara">

<div class="title">

Troubleshooting

</div>

If the Operator does not appear as installed, troubleshoot further:

</div>

1.  Navigate to the **Ecosystem** → **Installed Operators** page and inspect the **Operator Subscriptions** and **Install Plans** tabs for any failure or errors under **Status**.

2.  Navigate to the **Workloads** → **Pods** page and check the logs for pods in the `openshift-nfd` project.

# NFD Operator overview

The Node Feature Discovery (NFD) Operator orchestrates all resources needed to run the NFD daemon set. You create a `NodeFeatureDiscovery` custom resource (CR), and the Operator creates the operand components in the selected namespace.

As a cluster administrator, you can create a `NodeFeatureDiscovery` CR by using the OpenShift CLI (`oc`) or the web console.

> [!NOTE]
> Starting with version 4.12, the `operand.image` field in the `NodeFeatureDiscovery` CR is mandatory. If the NFD Operator is deployed by using Operator Lifecycle Manager (OLM), OLM automatically sets the `operand.image` field. If you create the `NodeFeatureDiscovery` CR by using the OpenShift Container Platform CLI or the OpenShift Container Platform web console, you must set the `operand.image` field explicitly.

## Creating a NodeFeatureDiscovery CR by using the CLI

Create a `NodeFeatureDiscovery` CR instance by using the OpenShift CLI (`oc`) to deploy the NFD operand and enable hardware feature detection on your cluster nodes.

> [!NOTE]
> The `spec.operand.image` setting requires a `-rhel9` image to be defined for use with OpenShift Container Platform releases 4.13 and later.

The following example shows the use of `-rhel9` to acquire the correct image.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster.

- You installed the OpenShift CLI (`oc`).

- You logged in as a user with `cluster-admin` privileges.

- You installed the NFD Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `NodeFeatureDiscovery` CR:

    <div class="formalpara">

    <div class="title">

    Example `NodeFeatureDiscovery` CR

    </div>

    ``` yaml
    apiVersion: nfd.openshift.io/v1
    kind: NodeFeatureDiscovery
    metadata:
      name: nfd-instance
      namespace: openshift-nfd
    spec:
      instance: "" # instance is empty by default
      topologyupdater: false # False by default
      operand:
        image: registry.redhat.io/openshift4/ose-node-feature-discovery-rhel9:v4.22
        imagePullPolicy: Always
      workerConfig:
        configData: |
          core:
          #  labelWhiteList:
          #  noPublish: false
            sleepInterval: 60s
          #  sources: [all]
          #  klog:
          #    addDirHeader: false
          #    alsologtostderr: false
          #    logBacktraceAt:
          #    logtostderr: true
          #    skipHeaders: false
          #    stderrthreshold: 2
          #    v: 0
          #    vmodule:
          ##   NOTE: the following options are not dynamically run-time configurable
          ##         and require a nfd-worker restart to take effect after being changed
          #    logDir:
          #    logFile:
          #    logFileMaxSize: 1800
          #    skipLogHeaders: false
          sources:
            cpu:
              cpuid:
          #     NOTE: whitelist has priority over blacklist
                attributeBlacklist:
                  - "BMI1"
                  - "BMI2"
                  - "CLMUL"
                  - "CMOV"
                  - "CX16"
                  - "ERMS"
                  - "F16C"
                  - "HTT"
                  - "LZCNT"
                  - "MMX"
                  - "MMXEXT"
                  - "NX"
                  - "POPCNT"
                  - "RDRAND"
                  - "RDSEED"
                  - "RDTSCP"
                  - "SGX"
                  - "SSE"
                  - "SSE2"
                  - "SSE3"
                  - "SSE4.1"
                  - "SSE4.2"
                  - "SSSE3"
                attributeWhitelist:
            kernel:
              kconfigFile: "/path/to/kconfig"
              configOpts:
                - "NO_HZ"
                - "X86"
                - "DMI"
            pci:
              deviceClassWhitelist:
                - "0200"
                - "03"
                - "12"
              deviceLabelFields:
                - "class"
      customConfig:
        configData: |
              - name: "more.kernel.features"
                matchOn:
                - loadedKMod: ["example_kmod3"]
    ```

    </div>

    where:

    `operand.image`
    Specifies the required operand image.

2.  Create the `NodeFeatureDiscovery` CR by running the following command:

    ``` terminal
    $ oc apply -f <filename>
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check that the `NodeFeatureDiscovery` CR was created by running the following command:

    ``` terminal
    $ oc get pods
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                      READY   STATUS    RESTARTS   AGE
    nfd-controller-manager-7f86ccfb58-vgr4x   2/2     Running   0          11m
    nfd-master-hcn64                          1/1     Running   0          60s
    nfd-master-lnnxx                          1/1     Running   0          60s
    nfd-master-mp6hr                          1/1     Running   0          60s
    nfd-worker-vgcz9                          1/1     Running   0          60s
    nfd-worker-xqbws                          1/1     Running   0          60s
    ```

    </div>

    A successful deployment shows a `Running` status.

</div>

## Creating a NodeFeatureDiscovery CR by using the CLI in a disconnected environment

Create a `NodeFeatureDiscovery` CR instance in a disconnected environment by using the OpenShift CLI (`oc`) and a mirror registry to deploy the NFD operand without direct internet access.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster.

- You installed the OpenShift CLI (`oc`).

- You logged in as a user with `cluster-admin` privileges.

- You installed the NFD Operator.

- You have access to a mirror registry with the required images.

- You installed the `skopeo` CLI tool.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Determine the digest of the registry image:

    1.  Run the following command:

        ``` terminal
        $ skopeo inspect docker://registry.redhat.io/openshift4/ose-node-feature-discovery:<openshift_version>
        ```

        <div class="formalpara">

        <div class="title">

        Example command

        </div>

        ``` terminal
        $ skopeo inspect docker://registry.redhat.io/openshift4/ose-node-feature-discovery:v4.12
        ```

        </div>

    2.  Inspect the output to identify the image digest:

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        {
          ...
          "Digest": "sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
          ...
        }
        ```

        </div>

2.  Use the `skopeo` CLI tool to copy the image from `registry.redhat.io` to your mirror registry, by running the following command:

    ``` terminal
    $ skopeo copy docker://registry.redhat.io/openshift4/ose-node-feature-discovery@<image_digest> docker://<mirror_registry>/openshift4/ose-node-feature-discovery@<image_digest>
    ```

    <div class="formalpara">

    <div class="title">

    Example command

    </div>

    ``` terminal
    $ skopeo copy docker://registry.redhat.io/openshift4/ose-node-feature-discovery@sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef docker://<your_mirror_registry>/openshift4/ose-node-feature-discovery@sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
    ```

    </div>

3.  Create a `NodeFeatureDiscovery` CR:

    <div class="formalpara">

    <div class="title">

    Example `NodeFeatureDiscovery` CR

    </div>

    ``` yaml
    apiVersion: nfd.openshift.io/v1
    kind: NodeFeatureDiscovery
    metadata:
      name: nfd-instance
    spec:
      operand:
        image: <mirror_registry>/openshift4/ose-node-feature-discovery@<image_digest>
        imagePullPolicy: Always
      workerConfig:
        configData: |
          core:
          #  labelWhiteList:
          #  noPublish: false
            sleepInterval: 60s
          #  sources: [all]
          #  klog:
          #    addDirHeader: false
          #    alsologtostderr: false
          #    logBacktraceAt:
          #    logtostderr: true
          #    skipHeaders: false
          #    stderrthreshold: 2
          #    v: 0
          #    vmodule:
          ##   NOTE: the following options are not dynamically run-time configurable
          ##         and require a nfd-worker restart to take effect after being changed
          #    logDir:
          #    logFile:
          #    logFileMaxSize: 1800
          #    skipLogHeaders: false
          sources:
            cpu:
              cpuid:
          #     NOTE: whitelist has priority over blacklist
                attributeBlacklist:
                  - "BMI1"
                  - "BMI2"
                  - "CLMUL"
                  - "CMOV"
                  - "CX16"
                  - "ERMS"
                  - "F16C"
                  - "HTT"
                  - "LZCNT"
                  - "MMX"
                  - "MMXEXT"
                  - "NX"
                  - "POPCNT"
                  - "RDRAND"
                  - "RDSEED"
                  - "RDTSCP"
                  - "SGX"
                  - "SSE"
                  - "SSE2"
                  - "SSE3"
                  - "SSE4.1"
                  - "SSE4.2"
                  - "SSSE3"
                attributeWhitelist:
            kernel:
              kconfigFile: "/path/to/kconfig"
              configOpts:
                - "NO_HZ"
                - "X86"
                - "DMI"
            pci:
              deviceClassWhitelist:
                - "0200"
                - "03"
                - "12"
              deviceLabelFields:
                - "class"
      customConfig:
        configData: |
              - name: "more.kernel.features"
                matchOn:
                - loadedKMod: ["example_kmod3"]
    ```

    </div>

    where:

    `operand.image`
    Specifies the required operand image.

4.  Create the `NodeFeatureDiscovery` CR by running the following command:

    ``` terminal
    $ oc apply -f <filename>
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check the status of the `NodeFeatureDiscovery` CR by running the following command:

    ``` terminal
    $ oc get nodefeaturediscovery nfd-instance -o yaml
    ```

2.  Check that the pods are running without `ImagePullBackOff` errors by running the following command:

    ``` terminal
    $ oc get pods -n <nfd_namespace>
    ```

</div>

## Creating a NodeFeatureDiscovery CR by using the web console

Create a `NodeFeatureDiscovery` CR by using the OpenShift Container Platform web console to deploy the NFD operand and enable hardware feature detection on your cluster nodes.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster.

- You logged in as a user with `cluster-admin` privileges.

- You installed the NFD Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the **Ecosystem** → **Installed Operators** page.

2.  In the **Node Feature Discovery** section, under **Provided APIs**, click **Create instance**.

3.  Edit the values of the `NodeFeatureDiscovery` CR.

4.  Click **Create**.

    > [!NOTE]
    > Starting with version 4.12, the `operand.image` field in the `NodeFeatureDiscovery` CR is mandatory. If the NFD Operator is deployed by using Operator Lifecycle Manager (OLM), OLM automatically sets the `operand.image` field. If you create the `NodeFeatureDiscovery` CR by using the OpenShift Container Platform CLI or the OpenShift Container Platform web console, you must set the `operand.image` field explicitly.

</div>

# NFD core configuration parameters

The following core configuration parameters control Node Feature Discovery (NFD) feature detection intervals, label filtering, and publishing behavior across all feature sources.

`core.sleepInterval`
Specifies the interval between consecutive passes of feature detection or re-detection, and therefore also the interval between node re-labeling. A non-positive value implies an infinite sleep interval; no re-detection or re-labeling is done. This value is overridden by the deprecated `--sleep-interval` command-line flag, if specified. The default value is `60s`.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
core:
  sleepInterval: 60s
```

</div>

`core.sources`
Specifies the list of enabled feature sources. A special value `all` enables all feature sources. This value is overridden by the deprecated `--sources` command-line flag, if specified. Default: `[all]`.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
core:
  sources:
    - system
    - custom
```

</div>

`core.labelWhiteList`
Specifies a regular expression for filtering feature labels based on the label name. Non-matching labels are not published. The regular expression is only matched against the basename part of the label, the part of the name after '/'. The label prefix, or namespace, is omitted. This value is overridden by the deprecated `--label-whitelist` command-line flag, if specified. Default: `null`.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
core:
  labelWhiteList: '^cpu-cpuid'
```

</div>

`core.noPublish`
Setting `core.noPublish` to `true` disables all communication with the `nfd-master`. It is effectively a dry run flag; `nfd-worker` runs feature detection normally, but no labeling requests are sent to `nfd-master`. This value is overridden by the `--no-publish` command-line flag, if specified. The default value is `false`.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
core:
  noPublish: true
```

</div>

# NFD core klog configuration parameters

The following `core.klog` configuration parameters control Node Feature Discovery (NFD) logging behavior, including log verbosity, output destinations, and file rotation, to support debugging and operational monitoring.

The logger options can also be specified using command-line flags, which take precedence over any corresponding config file options.

`core.klog.addDirHeader`
If set to `true`, adds the file directory to the header of the log messages. Default: `false`. Runtime configurable: yes.

`core.klog.alsologtostderr`
Log to standard error and files. Default: `false`. Runtime configurable: yes.

`core.klog.logBacktraceAt`
When logging hits line `file:N`, emit a stack trace. Default: empty. Runtime configurable: yes.

`core.klog.logDir`
If non-empty, write log files in this directory. Default: empty. Runtime configurable: no.

`core.klog.logFile`
If not empty, use this log file. Default: empty. Runtime configurable: no.

`core.klog.logFileMaxSize`
Defines the maximum size a log file can grow to. Unit is megabytes. If the value is `0`, the maximum file size is unlimited. Default: `1800`. Runtime configurable: no.

`core.klog.logtostderr`
Log to standard error instead of files. Default: `true`. Runtime configurable: yes.

`core.klog.skipHeaders`
If set to `true`, avoid header prefixes in the log messages. Default: `false`. Runtime configurable: yes.

`core.klog.skipLogHeaders`
If set to `true`, avoid headers when opening log files. Default: `false`. Runtime configurable: no.

`core.klog.stderrthreshold`
Logs at or above this threshold go to stderr. Default: `2`. Runtime configurable: yes.

`core.klog.v`
Specifies the number for the log level verbosity. Default: `0`. Runtime configurable: yes.

`core.klog.vmodule`
Specifies a comma-separated list of `pattern=N` settings for file-filtered logging. Default: empty. Runtime configurable: yes.

# NFD sources configuration parameters

The following source configuration parameters control which CPU, kernel, PCI, USB, and custom hardware attributes Node Feature Discovery (NFD) detects and publishes as node labels.

`sources.cpu.cpuid.attributeBlacklist`
Prevents publishing `cpuid` features listed in this option. This value is overridden by `sources.cpu.cpuid.attributeWhitelist`, if specified. Default: `[BMI1, BMI2, CLMUL, CMOV, CX16, ERMS, F16C, HTT, LZCNT, MMX, MMXEXT, NX, POPCNT, RDRAND, RDSEED, RDTSCP, SGX, SGXLC, SSE, SSE2, SSE3, SSE4.1, SSE4.2, SSSE3]`.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
sources:
  cpu:
    cpuid:
      attributeBlacklist: [MMX, MMXEXT]
```

</div>

`sources.cpu.cpuid.attributeWhitelist`
Publishes only the `cpuid` features listed in this option. Takes precedence over `sources.cpu.cpuid.attributeBlacklist`. Default: empty.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
sources:
  cpu:
    cpuid:
      attributeWhitelist: [AVX512BW, AVX512CD, AVX512DQ, AVX512F, AVX512VL]
```

</div>

`sources.kernel.kconfigFile`
Specifies the path of the kernel config file. If empty, NFD runs a search in the well-known standard locations. Default: empty.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
sources:
  kernel:
    kconfigFile: "/path/to/kconfig"
```

</div>

`sources.kernel.configOpts`
Specifies kernel configuration options to publish as feature labels. Default: `[NO_HZ, NO_HZ_IDLE, NO_HZ_FULL, PREEMPT]`.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
sources:
  kernel:
    configOpts: [NO_HZ, X86, DMI]
```

</div>

`sources.pci.deviceClassWhitelist`
Specifies a list of [PCI device class IDs](https://pci-ids.ucw.cz/read/PD) for which to publish a label. It can be specified as a main class only (for example, `03`) or full class-subclass combination (for example `0300`). The former implies that all subclasses are accepted. The format of the labels can be further configured with `deviceLabelFields`. Default: `["03", "0b40", "12"]`.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
sources:
  pci:
    deviceClassWhitelist: ["0200", "03"]
```

</div>

`sources.pci.deviceLabelFields`
Specifies the set of PCI ID fields to use when constructing the name of the feature label. Valid fields are `class`, `vendor`, `device`, `subsystem_vendor` and `subsystem_device`. Default: `[class, vendor]`.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
sources:
  pci:
    deviceLabelFields: [class, vendor, device]
```

</div>

With the example config above, NFD would publish labels such as `feature.node.kubernetes.io/pci-<class_id>_<vendor_id>_<device_id>.present=true`.

`sources.usb.deviceClassWhitelist`
Specifies a list of USB [device class](https://www.usb.org/defined-class-codes) IDs for which to publish a feature label. The format of the labels can be further configured with `deviceLabelFields`. Default: `["0e", "ef", "fe", "ff"]`.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
sources:
  usb:
    deviceClassWhitelist: ["ef", "ff"]
```

</div>

`sources.usb.deviceLabelFields`
Specifies the set of USB ID fields from which to compose the name of the feature label. Valid fields are `class`, `vendor`, and `device`. Default: `[class, vendor, device]`.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
sources:
  pci:
    deviceLabelFields: [class, vendor]
```

</div>

With the example config above, NFD would publish labels such as `feature.node.kubernetes.io/usb-<class_id>_<vendor_id>.present=true`.

`sources.custom`
Specifies the list of rules to process in the custom feature source to create user-specific labels. Default: empty.

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
sources:
  custom:
  - name: "my.custom.feature"
    matchOn:
    - loadedKMod: ["e1000e"]
    - pciId:
        class: ["0200"]
        vendor: ["8086"]
```

</div>

# Configure Node Feature Discovery worker and controller pod scheduling

You can control where Node Feature Discovery (NFD) worker and controller pods are scheduled by configuring node selectors and tolerations in the `NodeFeatureDiscovery` custom resource.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster.

- You have installed the OpenShift CLI (`oc`).

- You have logged in as a user with `cluster-admin` privileges.

- You have installed the NFD Operator.

</div>

> [!NOTE]
> If you specify `workerNodeSelector` without the required `workerTolerations`, NFD worker pods are not scheduled on tainted nodes, even when the nodes match the configured node selector.

<div>

<div class="title">

Procedure

</div>

1.  Label the target node with the label you use in the `workerNodeSelector` field by entering the following command:

    ``` terminal
    $ oc label node <node_name> special-node=true
    ```

2.  Edit the `NodeFeatureDiscovery` custom resource by entering the following command:

    ``` terminal
    $ oc edit NodeFeatureDiscovery nfd-instance -n openshift-nfd
    ```

3.  Configure the scheduling options:

    ``` yaml
    apiVersion: nfd.openshift.io/v1
    kind: NodeFeatureDiscovery
    metadata:
      name: nfd-instance
      namespace: openshift-nfd
    spec:
      enableTaints: false
      instance: ""
      operand:
        imagePullPolicy: IfNotPresent
        servicePort: 12000
        workerNodeSelector:
          special-node: "true"
        workerTolerations:
          - key: "node-role.kubernetes.io/ai"
            operator: "Exists"
            effect: "NoSchedule"
          - key: "node-role.kubernetes.io/ai"
            operator: "Exists"
            effect: "NoExecute"
        masterTolerations:
          - key: "node-role.kubernetes.io/master"
            operator: "Exists"
            effect: "NoSchedule"
          - key: "node-role.kubernetes.io/control-plane"
            operator: "Exists"
            effect: "NoSchedule"
      prunerOnDelete: false
      topologyUpdater: false
    ```

    where:

    `spec.operand.workerNodeSelector`
    Controls where the NFD worker DaemonSet is scheduled. Configure this field under `spec.operand`.

    `spec.operand.workerTolerations`
    Allows the NFD worker pods to tolerate taints applied to the selected nodes. Configure this field under `spec.operand`.

    `spec.operand.masterTolerations`
    Allows NFD controller pods to tolerate taints on control plane nodes. The tolerations must match the node taints for the controller pods to schedule successfully.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the NFD worker pods are scheduled on the expected nodes by entering the following command:

    ``` terminal
    $ oc get pods -n openshift-nfd -o wide
    ```

2.  Verify the node labels by entering the following command:

    ``` terminal
    $ oc get nodes --show-labels
    ```

3.  Verify the node taints by entering the following command:

    ``` terminal
    $ oc get node <node_name> -o jsonpath='{.spec.taints}'
    ```

    After verification, NFD worker pods should appear on nodes with the `special-node=true` label, or with the label you configured in `workerNodeSelector`. Controller pods should remain `Running` in the `openshift-nfd` namespace.

</div>

# About the NodeFeatureRule custom resource

A `NodeFeatureRule` custom resource provides a flexible, rule-based method to create vendor- or application-specific labels and optionally taints on nodes based on detected hardware features and system configuration.

# Using the NodeFeatureRule custom resource

Create a `NodeFeatureRule` object to apply custom labels to nodes based on detected features, enabling targeted workload scheduling and hardware-specific configuration.

<div>

<div class="title">

Procedure

</div>

1.  Create a custom resource file named `nodefeaturerule.yaml` that contains the following text:

    ``` yaml
    apiVersion: nfd.openshift.io/v1
    kind: NodeFeatureRule
    metadata:
      name: example-rule
    spec:
      rules:
        - name: "example rule"
          labels:
            "example-custom-feature": "true"
          # Label is created if all of the rules below match
          matchFeatures:
            # Match if "veth" kernel module is loaded
            - feature: kernel.loadedmodule
              matchExpressions:
                veth: {op: Exists}
            # Match if any PCI device with vendor 8086 exists in the system
            - feature: pci.device
              matchExpressions:
                vendor: {op: In, value: ["8086"]}
    ```

    This custom resource specifies that labeling occurs when the `veth` module is loaded and a PCI device with vendor code `8086` exists in the cluster.

2.  Apply the `nodefeaturerule.yaml` file to your cluster by running the following command:

    ``` terminal
    $ oc apply -f https://raw.githubusercontent.com/kubernetes-sigs/node-feature-discovery/v0.13.6/examples/nodefeaturerule.yaml
    ```

    The example applies the feature label on nodes where the `veth` module is loaded and a PCI device with vendor code `8086` exists.

    > [!NOTE]
    > A relabeling delay of up to 1 minute might occur.

</div>

# Using the NFD Topology Updater

Enable the NFD Topology Updater to detect allocated resources on worker nodes and report per-zone resource availability. This information helps the scheduler make topology-aware placement decisions for workloads that require specific NUMA node configurations.

The NFD Topology Updater runs as a daemon on each worker node, examining the allocated resources and creating per-zone resource availability information. It communicates with nfd-master to create or update `NodeResourceTopology` custom resources with the resource topology of each zone, such as NUMA nodes.

<div>

<div class="title">

Procedure

</div>

- To enable the Topology Updater workers in NFD, set the `topologyupdater` variable to `true` in the `NodeFeatureDiscovery` CR, as described in the section **Using the Node Feature Discovery Operator**.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

When run with NFD Topology Updater, NFD creates `NodeResourceTopology` custom resource instances corresponding to the node resource hardware topology, such as:

</div>

``` yaml
apiVersion: topology.node.k8s.io/v1alpha1
kind: NodeResourceTopology
metadata:
  name: node1
topologyPolicies: ["SingleNUMANodeContainerLevel"]
zones:
  - name: node-0
    type: Node
    resources:
      - name: cpu
        capacity: 20
        allocatable: 16
        available: 10
      - name: vendor/nic1
        capacity: 3
        allocatable: 3
        available: 3
  - name: node-1
    type: Node
    resources:
      - name: cpu
        capacity: 30
        allocatable: 30
        available: 15
      - name: vendor/nic2
        capacity: 6
        allocatable: 6
        available: 6
  - name: node-2
    type: Node
    resources:
      - name: cpu
        capacity: 30
        allocatable: 30
        available: 15
      - name: vendor/nic1
        capacity: 3
        allocatable: 3
        available: 3
```

## NFD Topology Updater command-line flags

You can use the NFD Topology Updater command-line flags to control TLS authentication, resource detection intervals, and connection settings for communicating node resource topology to nfd-master.

To view available flags, run the `nfd-topology-updater -help` command. For example, in a Podman container, run the following command:

``` terminal
$ podman run gcr.io/k8s-staging-nfd/node-feature-discovery:master nfd-topology-updater -help
```

`-ca-file`
Specifies the TLS root certificate for verifying the authenticity of nfd-master. The `-ca-file` flag is one of three flags, together with `-cert-file` and `-key-file`, that controls mutual TLS authentication on the NFD Topology Updater. Default: empty.

> [!IMPORTANT]
> The `-ca-file` flag must be specified together with the `-cert-file` and `-key-file` flags.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ nfd-topology-updater -ca-file=/opt/nfd/ca.crt -cert-file=/opt/nfd/updater.crt -key-file=/opt/nfd/updater.key
```

</div>

`-cert-file`
Specifies the TLS certificate presented for authenticating outgoing requests. The `-cert-file` flag is one of three flags, together with `-ca-file` and `-key-file`, that controls mutual TLS authentication on the NFD Topology Updater. Default: empty.

> [!IMPORTANT]
> The `-cert-file` flag must be specified together with the `-ca-file` and `-key-file` flags.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ nfd-topology-updater -cert-file=/opt/nfd/updater.crt -key-file=/opt/nfd/updater.key -ca-file=/opt/nfd/ca.crt
```

</div>

`-h`, `-help`
Print usage and exit.

`-key-file`
Specifies the private key corresponding to the given certificate file, or `-cert-file`, that is used for authenticating outgoing requests. The `-key-file` flag is one of three flags, together with `-ca-file` and `-cert-file`, that controls mutual TLS authentication on the NFD Topology Updater. Default: empty.

> [!IMPORTANT]
> The `-key-file` flag must be specified together with the `-ca-file` and `-cert-file` flags.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ nfd-topology-updater -key-file=/opt/nfd/updater.key -cert-file=/opt/nfd/updater.crt -ca-file=/opt/nfd/ca.crt
```

</div>

`-kubelet-config-file`
Specifies the path to the kubelet’s configuration file. Default: `/host-var/lib/kubelet/config.yaml`.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ nfd-topology-updater -kubelet-config-file=/var/lib/kubelet/config.yaml
```

</div>

`-no-publish`
Disables all communication with the nfd-master, making it a dry run flag for nfd-topology-updater. NFD Topology Updater runs resource hardware topology detection normally, but no CR requests are sent to nfd-master. Default: `false`.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ nfd-topology-updater -no-publish
```

</div>

`-oneshot`
Causes the NFD Topology Updater to exit after one pass of resource hardware topology detection. Default: `false`.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ nfd-topology-updater -oneshot -no-publish
```

</div>

`-podresources-socket`
Specifies the path to the UNIX socket where kubelet exports a gRPC service to enable discovery of in-use CPUs and devices, and to provide metadata for them. Default: `/host-var/lib/kubelet/pod-resources/kubelet.sock`.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ nfd-topology-updater -podresources-socket=/var/lib/kubelet/pod-resources/kubelet.sock
```

</div>

`-server`
Specifies the address of the nfd-master endpoint to connect to. Default: `localhost:8080`.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ nfd-topology-updater -server=nfd-master.nfd.svc.cluster.local:443
```

</div>

`-server-name-override`
Specifies the common name (CN) which to expect from the nfd-master TLS certificate. This flag is mostly intended for development and debugging purposes. Default: empty.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ nfd-topology-updater -server-name-override=localhost
```

</div>

`-sleep-interval`
Specifies the interval between resource hardware topology re-examination and custom resource updates. A non-positive value implies infinite sleep interval and no re-detection is done. Default: `60s`.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ nfd-topology-updater -sleep-interval=1h
```

</div>

`-version`
Print version and exit.

`-watch-namespace`
Specifies the namespace to ensure that resource hardware topology examination only happens for the pods running in the specified namespace. Pods that are not running in the specified namespace are not considered during resource accounting. This is particularly useful for testing and debugging purposes. A `*` value means that all of the pods across all namespaces are considered during the accounting process. Default: `*`.

<div class="formalpara">

<div class="title">

Example

</div>

``` terminal
$ nfd-topology-updater -watch-namespace=rte
```

</div>
