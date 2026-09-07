<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Kernel Module Management (KMM) Operator deploys out-of-tree kernel modules and device plugins on OpenShift Container Platform clusters. You can use KMM to build, load, and manage kernel modules across cluster lifecycle stages.

# About the Kernel Module Management Operator

The Kernel Module Management (KMM) Operator on OpenShift Container Platform manages the full lifecycle of out-of-tree kernel modules and device plugins, from build and signing through deployment. You can use `Module` custom resources (CRs)to define module loaders, device plugins, and version-specific build instructions across kernel upgrades.

# Installing the Kernel Module Management Operator

As a cluster administrator, you can install the Kernel Module Management (KMM) Operator on OpenShift Container Platform by using the OpenShift CLI or web console.

The KMM Operator is supported on OpenShift Container Platform 4.12 and later. Installing KMM on version 4.11 does not require specific additional steps. For details on installing KMM on version 4.10 and earlier, see the section "Installing the Kernel Module Management Operator on earlier versions of OpenShift Container Platform".

## Installing the Kernel Module Management Operator using the web console

To install the Kernel Module Management (KMM)Operator on OpenShift Container Platform, you can use the web console **Software Catalog** to deploy it into the `openshift-kmm` namespace.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Install the Kernel Module Management Operator:

    1.  In the OpenShift Container Platform web console, click **Ecosystem** → **Software Catalog**.

    2.  Select **Kernel Module Management Operator** from the list of available Operators, and then click **Install**.

    3.  From the **Installed Namespace** list, select the `openshift-kmm` namespace.

    4.  Click **Install**.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

To verify that KMM Operator installed successfully:

</div>

1.  Navigate to the **Ecosystem** → **Installed Operators** page.

2.  Ensure that **Kernel Module Management Operator** is listed in the **openshift-kmm** project with a **Status** of **InstallSucceeded**.

    > [!NOTE]
    > During installation, an Operator might display a **Failed** status. If the installation later succeeds with an **InstallSucceeded** message, you can ignore the **Failed** message.

<div>

<div class="title">

Troubleshooting

</div>

1.  To troubleshoot issues with Operator installation:

    1.  Navigate to the **Ecosystem** → **Installed Operators** page and inspect the **Operator Subscriptions** and **Install Plans** tabs for any failure or errors under **Status**.

    2.  Navigate to the **Workloads** → **Pods** page and check the logs for pods in the `openshift-kmm` project.

</div>

## Installing the Kernel Module Management Operator by using the CLI

To install the Kernel Module Management (KMM) Operator on OpenShift Container Platform, you can create `Namespace`, `OperatorGroup`, and `Subscription` resources by using the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have a running OpenShift Container Platform cluster.

- You installed the OpenShift CLI (`oc`).

- You are logged into the OpenShift CLI as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Install KMM in the `openshift-kmm` namespace:

    1.  Create the following `Namespace` CR and save the YAML file, for example, `kmm-namespace.yaml`:

        ``` yaml
        apiVersion: v1
        kind: Namespace
        metadata:
          name: openshift-kmm
        ```

    2.  Create the following `OperatorGroup` CR and save the YAML file, for example, `kmm-op-group.yaml`:

        ``` yaml
        apiVersion: operators.coreos.com/v1
        kind: OperatorGroup
        metadata:
          name: kernel-module-management
          namespace: openshift-kmm
        ```

    3.  Create the following `Subscription` CR and save the YAML file, for example, `kmm-sub.yaml`:

        ``` yaml
        apiVersion: operators.coreos.com/v1alpha1
        kind: Subscription
        metadata:
          name: kernel-module-management
          namespace: openshift-kmm
        spec:
          channel: stable
          installPlanApproval: Automatic
          name: kernel-module-management
          source: redhat-operators
          sourceNamespace: openshift-marketplace
        ```

    4.  Create the subscription object by running the following command:

        ``` terminal
        $ oc create -f kmm-sub.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the Operator deployment is successful, run the following command:

  ``` terminal
  $ oc get -n openshift-kmm deployments.apps kmm-operator-controller
  ```

  Example output:

  ``` terminal
  NAME                              READY UP-TO-DATE  AVAILABLE AGE
  kmm-operator-controller           1/1   1           1         97s
  ```

  The Operator is available.

</div>

## Installing the Kernel Module Management Operator on earlier versions of OpenShift Container Platform

As a cluster administrator, you can install the Kernel Module Management (KMM) Operator by using the OpenShift CLI.

The KMM Operator is supported on OpenShift Container Platform 4.12 and later. For version 4.10 and earlier, you must create a new `SecurityContextConstraint` object and bind it to the Operator’s `ServiceAccount`.

<div>

<div class="title">

Prerequisites

</div>

- You have a running OpenShift Container Platform cluster.

- You installed the OpenShift CLI (`oc`).

- You are logged into the OpenShift CLI as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Install KMM in the `openshift-kmm` namespace:

    1.  Create the following `Namespace` CR and save the YAML file, for example, `kmm-namespace.yaml` file:

        ``` yaml
        apiVersion: v1
        kind: Namespace
        metadata:
          name: openshift-kmm
        ```

    2.  Create the following `SecurityContextConstraint` object and save the YAML file, for example, `kmm-security-constraint.yaml`:

        ``` yaml
        allowHostDirVolumePlugin: false
        allowHostIPC: false
        allowHostNetwork: false
        allowHostPID: false
        allowHostPorts: false
        allowPrivilegeEscalation: false
        allowPrivilegedContainer: false
        allowedCapabilities:
          - NET_BIND_SERVICE
        apiVersion: security.openshift.io/v1
        defaultAddCapabilities: null
        fsGroup:
          type: MustRunAs
        groups: []
        kind: SecurityContextConstraints
        metadata:
          name: restricted-v2
        priority: null
        readOnlyRootFilesystem: false
        requiredDropCapabilities:
          - ALL
        runAsUser:
          type: MustRunAsRange
        seLinuxContext:
          type: MustRunAs
        seccompProfiles:
          - runtime/default
        supplementalGroups:
          type: RunAsAny
        users: []
        volumes:
          - configMap
          - downwardAPI
          - emptyDir
          - persistentVolumeClaim
          - projected
          - secret
        ```

    3.  Bind the `SecurityContextConstraint` object to the Operator’s `ServiceAccount` by running the following commands:

        ``` terminal
        $ oc apply -f kmm-security-constraint.yaml
        ```

        ``` terminal
        $ oc adm policy add-scc-to-user kmm-security-constraint -z kmm-operator-controller -n openshift-kmm
        ```

    4.  Create the following `OperatorGroup` CR and save the YAML file, for example, `kmm-op-group.yaml`:

        ``` yaml
        apiVersion: operators.coreos.com/v1
        kind: OperatorGroup
        metadata:
          name: kernel-module-management
          namespace: openshift-kmm
        ```

    5.  Create the following `Subscription` CR and save the YAML file, for example, `kmm-sub.yaml`:

        ``` yaml
        apiVersion: operators.coreos.com/v1alpha1
        kind: Subscription
        metadata:
          name: kernel-module-management
          namespace: openshift-kmm
        spec:
          channel: stable
          installPlanApproval: Automatic
          name: kernel-module-management
          source: redhat-operators
          sourceNamespace: openshift-marketplace
        ```

    6.  Create the subscription object by running the following command:

        ``` terminal
        $ oc create -f kmm-sub.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the Operator deployment is successful, run the following command:

  ``` terminal
  $ oc get -n openshift-kmm deployments.apps kmm-operator-controller
  ```

  Example output:

  ``` terminal
  NAME                              READY UP-TO-DATE  AVAILABLE AGE
  kmm-operator-controller           1/1   1           1         97s
  ```

  The Operator is available.

</div>

# Configuring the Kernel Module Management Operator

To adapt the Kernel Module Management (KMM) Operator to your OpenShift Container Platform environment, you can create a `ConfigMap` with custom settings and restart the controller.

<div>

<div class="title">

Procedure

</div>

- To modify any setting, create a `ConfigMap` with the name `kmm-operator-manager-config` in the Operator namespace with the relevant data and restart the controller using the following command:

  ``` terminal
  $ oc rollout restart -n "$namespace" deployment/kmm-operator-controller
  ```

  The value of `$namespace` depends on your installation method. For example:

  ``` yaml
  apiVersion: v1
  data:
    controller_config.yaml: |
      worker:
        firmwareHostPath: /example/different/firmware/path
  kind: ConfigMap
  metadata:
    name: kmm-operator-manager-config
    namespace: openshift-kmm
  ```

  > [!NOTE]
  > If you want to configure `KMM Hub`, create the `ConfigMap` using the name `kmm-operator-hub-manager-config` in the KMM Hub controller’s namespace.

  <table>
  <caption>Operator configuration parameters</caption>
  <colgroup>
  <col style="width: 20%" />
  <col style="width: 80%" />
  </colgroup>
  <thead>
  <tr>
  <th style="text-align: left;">Parameter</th>
  <th style="text-align: left;">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td style="text-align: left;"><p><code>healthProbeBindAddress</code></p></td>
  <td style="text-align: left;"><p>Defines the address on which the Operator monitors for kubelet health probes. The recommended value is <code>:8081</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>job.gcDelay</code></p></td>
  <td style="text-align: left;"><p>Defines the duration for which successful build pods should be preserved before they are deleted. For information about the valid values for this setting, see <a href="https://pkg.go.dev/time#ParseDuration">ParseDuration</a>. The default value is <code>0s</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>leaderElection.enabled</code></p></td>
  <td style="text-align: left;"><p>Determines whether leader election is used to ensure that only one replica of the KMM Operator is running at any time. For more information, see <a href="https://kubernetes.io/docs/concepts/architecture/leases/">Leases</a>. The default value is <code>true</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>leaderElection.resourceID</code></p></td>
  <td style="text-align: left;"><p>Determines the name of the resource that leader election uses for holding the leader lock. The default value for KMM is <code>kmm.sigs.x-k8s.io</code>. The default value for KMM-hub is <code>kmm-hub.sigs.x-k8s.io</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>metrics.bindAddress</code></p></td>
  <td style="text-align: left;"><p>Determines the bind address for the metrics server. Set this to "0" to disable the metrics server. The default value is <code>0.0.0.0:8443</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>metrics.disableHTTP2</code></p></td>
  <td style="text-align: left;"><p>If <code>true</code>, disables HTTP/2 for the metrics server as a mitigation for <a href="https://access.redhat.com/security/cve/cve-2023-44487">CVE-2023-44487</a>. The default value is <code>true</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>metrics.enableAuthnAuthz</code></p></td>
  <td style="text-align: left;"><p>Determines if metrics are authenticated using <code>TokenReviews</code> and authorized using <code>SubjectAccessReviews</code> with the kube-apiserver.</p>
  <p>For authentication and authorization, the controller needs a <code>ClusterRole</code> with the following rules:</p>
  <ul>
  <li><p><code>apiGroups: authentication.k8s.io, resources: tokenreviews, verbs: create</code></p></li>
  <li><p><code>apiGroups: authorization.k8s.io, resources: subjectaccessreviews, verbs: create</code></p></li>
  </ul>
  <p>To scrape metrics, for example, using Prometheus, the client needs a <code>ClusterRole</code> with the following rule:</p>
  <ul>
  <li><p><code>nonResourceURLs: "/metrics", verbs: get</code></p></li>
  </ul>
  <p>The default value is <code>true</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>metrics.secureServing</code></p></td>
  <td style="text-align: left;"><p>Determines whether the metrics are served over HTTPS instead of HTTP. The default value is <code>true</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>webhook.disableHTTP2</code></p></td>
  <td style="text-align: left;"><p>If <code>true</code>, disables HTTP/2 for the webhook server, as a mitigation for <a href="https://access.redhat.com/security/cve/cve-2023-44487">CVE-2023-44487</a>. The default value is <code>true</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>webhook.port</code></p></td>
  <td style="text-align: left;"><p>Defines the port on which the Operator monitors webhook requests. The default value is <code>9443</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>worker.runAsUser</code></p></td>
  <td style="text-align: left;"><p>Determines the value of the <code>runAsUser</code> field of the worker container’s security context. For more information, see <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/">SecurityContext</a>. The default value is <code>9443</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>worker.seLinuxType</code></p></td>
  <td style="text-align: left;"><p>Determines the value of the <code>seLinuxOptions.type</code> field of the worker container’s security context. For more information, see <a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/">SecurityContext</a>. The default value is <code>spc_t</code>.</p></td>
  </tr>
  <tr>
  <td style="text-align: left;"><p><code>worker.firmwareHostPath</code></p></td>
  <td style="text-align: left;"><p>If set, the value of this field is written by the worker container into the /sys/module/firmware_class/parameters/path file on the node. For more information see <a href="https://openshift-kmm.netlify.app/documentation/firmwares/#setting-the-kernels-firmware-search-path">Setting the kernel’s firmware search path</a>. The default value is <code>/var/lib/firmware</code>.</p></td>
  </tr>
  </tbody>
  </table>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing the Kernel Module Management Operator](kmm-kernel-module-management.md#kmm-install_kernel-module-management-operator)

</div>

## Unloading the kernel module

To unload a kernel module deployed with KMM on OpenShift Container Platform, you can delete the corresponding `Module` resource. KMM creates worker pods that run `modprobe -r` on eligible nodes.

You must unload the kernel modules when moving to a newer version or if they introduce some undesirable side effect on the node.

<div>

<div class="title">

Procedure

</div>

- To unload a module loaded with KMM from nodes, delete the corresponding `Module` resource. KMM then creates worker pods, where required, to run `modprobe -r` and unload the kernel module from the nodes.

  > [!WARNING]
  > When unloading worker pods, KMM needs all the resources it uses when loading the kernel module. This includes the `ServiceAccount` referenced in the `Module` as well as any RBAC defined to allow privileged KMM worker Pods to run. It also includes any pull secret referenced in `.spec.imageRepoSecret`.
  >
  > To avoid situations where KMM is unable to unload the kernel module from nodes, make sure those resources are not deleted while the `Module` resource is still present in the cluster in any state, including `Terminating`. KMM includes a validating admission webhook that rejects the deletion of namespaces that contain at least one `Module` resource.

</div>

## Setting the kernel firmware search path

To configure where KMM worker pods search for firmware on OpenShift Container Platform nodes, you can set the `worker.setFirmwareClassPath` parameter in the Operator configuration.

The Linux kernel accepts the `firmware_class.path` parameter as a search path for firmware, as explained in [Firmware search paths](https://www.kernel.org/doc/html/latest/driver-api/firmware/fw_search_path.html).

<div>

<div class="title">

Procedure

</div>

- To define a firmware search path, set `worker.setFirmwareClassPath` to `/var/lib/firmware` in the Operator configuration.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring the Kernel Module Management Operator](kmm-kernel-module-management.md#kmm-configuring-kmmo_kernel-module-management-operator)

</div>

# Uninstalling the Kernel Module Management Operator

You can uninstall the Kernel Module Management (KMM) Operator from OpenShift Container Platform by using CLI or uninstalling the Operator.

## Uninstalling a Red Hat catalog installation

To uninstall a Kernel Module Management (KMM) Operator installation from the Red Hat catalog on OpenShift Container Platform, you can remove the Operator from **Installed Operators** in the web console.

<div>

<div class="title">

Procedure

</div>

- Use the OpenShift console under **Operators** -→ **Installed Operators** to locate and uninstall the Operator.

  > [!NOTE]
  > Alternatively, you can delete the `Subscription` resource in the KMM namespace.

</div>

## Uninstalling a CLI installation

To uninstall a Kernel Module Management (KMM) Operator CLI installation from OpenShift Container Platform, you can run `oc delete -k` against the upstream configuration manifest.

<div>

<div class="title">

Procedure

</div>

- Run the following command to uninstall the KMM Operator:

  ``` terminal
  $ oc delete -k https://github.com/rh-ecosystem-edge/kernel-module-management/config/default
  ```

  > [!NOTE]
  > Using this command deletes the `Module` CRD and all `Module` instances in the cluster.

</div>

# Kernel module deployment

Kernel Module Management (KMM) monitors `Node` and `Module` resources on OpenShift Container Platform to load or unload kernel modules on eligible nodes. KMM creates worker pods on target nodes to reconcile the desired module state.

To be eligible for a module, a node must contain the following:

- Labels that match the module’s `.spec.selector` field.

- A kernel version matching one of the items in the module’s `.spec.moduleLoader.container.kernelMappings` field.

- If ordered upgrade (`ordered_upgrade.md`) is configured in the module, a label that matches its `.spec.moduleLoader.container.version` field.

When KMM reconciles nodes with the desired state as configured in the `Module` resource, it creates worker pods on the target nodes to run the necessary action. The KMM Operator monitors the outcome of the pods and records the information. The Operator uses this information to label the `Node` objects when the module is successfully loaded, and to run the device plugin, if configured.

Worker pods run the KMM `worker` binary that performs the following tasks:

- Pulls the kmod image configured in the `Module` resource. Kmod images are standard OCI images that contain `.ko` files.

- Extracts the image in the pod’s filesystem.

- Runs `modprobe` with the specified arguments to perform the necessary action.

## The Module custom resource definition

The `Module` custom resource (CR) in OpenShift Container Platform represents a kernel module that can be loaded on all or select nodes in the cluster, through a kmod image. A `Module` CR specifies one or more kernel versions with which it is compatible, and a node selector.

The compatible versions for a `Module` resource are listed under `.spec.moduleLoader.container.kernelMappings`. A kernel mapping can either match a `literal` version, or use `regexp` to match many of them at the same time.

The reconciliation loop for the `Module` resource runs the following steps:

1.  List all nodes matching `.spec.selector`.

2.  Build a set of all kernel versions running on those nodes.

3.  For each kernel version:

    1.  Go through `.spec.moduleLoader.container.kernelMappings` and find the appropriate container image name. If the kernel mapping has `build` or `sign` defined and the container image does not already exist, run the build, the signing pod, or both, as needed.

    2.  Create a worker pod to pull the container image determined in the previous step and run `modprobe`.

    3.  If `.spec.devicePlugin` is defined, create a device plugin daemon set using the configuration specified under `.spec.devicePlugin.container`.

4.  Run `garbage-collect` on:

    1.  Obsolete device plugin `DaemonSets` that do not target any node.

    2.  Successful build pods.

    3.  Successful signing pods.

## Set soft dependencies between kernel modules

Soft dependencies require kernel modules to load in a specific order even when they do not share symbols. You can declare these dependencies in the `Module` CR with the `modulesLoadingOrder` field.

The `depmod` utility does not recognize soft dependencies, and soft dependencies do not appear in the files it produces. For example, if `mod_a` has a soft dependency on `mod_b`, `modprobe mod_a` will not load `mod_b`.

``` yaml
# ...
spec:
  moduleLoader:
    container:
      modprobe:
        moduleName: mod_a
        dirName: /opt
        firmwarePath: /firmware
        parameters:
          - param=1
        modulesLoadingOrder:
          - mod_a
          - mod_b
```

In the configuration above, the worker pod will first try to unload the in-tree `mod_b` before loading `mod_a` from the kmod image. When the worker pod is terminated and `mod_a` is unloaded, `mod_b` will not be loaded again.

> [!NOTE]
> The first value in the list, to be loaded last, must be equivalent to the `moduleName`.

# Security and permissions

KMM security and permissions govern how privileged workloads load kernel modules on OpenShift Container Platform nodes. Review `ServiceAccount`, `SecurityContextConstraint`, and pod security requirements before deploying `Module` resources.

> [!IMPORTANT]
> Loading kernel modules is a highly sensitive operation. After they are loaded, kernel modules have all possible permissions to do any kind of operation on the node.

## ServiceAccounts and SecurityContextConstraints

Kernel Module Management (KMM) creates a privileged workload to load the kernel modules on nodes. That workload needs `ServiceAccounts` allowed to use the `privileged` `SecurityContextConstraint` (SCC) resource.

The authorization model for that workload depends on the namespace of the `Module` resource, as well as its spec.

- If the `.spec.moduleLoader.serviceAccountName` or `.spec.devicePlugin.serviceAccountName` fields are set, they are always used.

- If those fields are not set, then:

  - If the `Module` resource is created in the Operator’s namespace (`openshift-kmm` by default), then KMM uses its default, powerful `ServiceAccounts` to run the worker and device plugin pods.

  - If the `Module` resource is created in any other namespace, then KMM runs the pods with the namespace’s `default` `ServiceAccount`. The `Module` resource cannot run a privileged workload unless you manually enable it to use the `privileged` SCC.

> [!IMPORTANT]
> `openshift-kmm` is a trusted namespace.
>
> When setting up RBAC permissions, remember that any user or `ServiceAccount` creating a `Module` resource in the `openshift-kmm` namespace results in KMM automatically running privileged workloads on potentially all nodes in the cluster.

To allow any `ServiceAccount` to use the `privileged` SCC and run worker or device plugin pods, you can use the `oc adm policy` command, as in the following example:

``` terminal
$ oc adm policy add-scc-to-user privileged -z "${serviceAccountName}" [ -n "${namespace}" ]
```

## Pod security standards

OpenShift runs a synchronization mechanism that sets the namespace Pod Security level automatically based on the security contexts in use. No action is needed.

<div>

<div class="title">

Additional resources

</div>

- [Understanding and managing pod security admission](../authentication/understanding-and-managing-pod-security-admission.md#understanding-and-managing-pod-security-admission)

</div>

# Replacing in-tree modules with out-of-tree modules

You can use Kernel Module Management (KMM) to build kernel modules that can be loaded or unloaded into the kernel on demand. These modules extend the functionality of the kernel without the need to reboot the system. Modules can be configured as built-in or dynamically loaded.

Dynamically loaded modules include in-tree modules and out-of-tree (OOT) modules. In-tree modules are internal to the Linux kernel tree, that is, they are already part of the kernel. Out-of-tree modules are external to the Linux kernel tree. They are generally written for development and testing purposes, such as testing the new version of a kernel module that is shipped in-tree, or to deal with incompatibilities.

Some modules that are loaded by KMM could replace in-tree modules that are already loaded on the node. To unload in-tree modules before loading your module, set the value of the `.spec.moduleLoader.container.inTreeModulesToRemove` field to the modules that you want to unload. The following example demonstrates module replacement for all kernel mappings:

``` yaml
# ...
spec:
  moduleLoader:
    container:
      modprobe:
        moduleName: mod_a

      inTreeModulesToRemove: [mod_a, mod_b]
```

In this example, the `moduleLoader` pod uses `inTreeModulesToRemove` to unload the in-tree `mod_a` and `mod_b` before loading `mod_a` from the `moduleLoader` image. When the `` moduleLoader`pod is terminated and `mod_a `` is unloaded, `mod_b` is not loaded again.

The following is an example for module replacement for specific kernel mappings:

``` yaml
# ...
spec:
  moduleLoader:
    container:
      kernelMappings:
        - literal: 6.0.15-300.fc37.x86_64
          containerImage: "some.registry/org/my-kmod:${KERNEL_FULL_VERSION}"
          inTreeModulesToRemove: [<module_name>, <module_name>]
```

<div>

<div class="title">

Additional resources

</div>

- [Building a linux kernel module](https://fastbitlab.com/building-a-linux-kernel-module/)

</div>

## Example Module CR

Use this annotated `Module` custom resource example as a reference when you configure kernel module loading, device plugins, builds, and signing in OpenShift Container Platform.

``` yaml
apiVersion: kmm.sigs.x-k8s.io/v1beta1
kind: Module
metadata:
  name: <my_kmod>
spec:
  moduleLoader:
    container:
      modprobe:
        moduleName: <my_kmod>
        dirName: /opt
        firmwarePath: /firmware
        parameters:
          - param=1
      kernelMappings:
        - literal: 6.0.15-300.fc37.x86_64
          containerImage: some.registry/org/my-kmod:6.0.15-300.fc37.x86_64
        - regexp: '^.+\fc37\.x86_64$'
          containerImage: "some.other.registry/org/<my_kmod>:${KERNEL_FULL_VERSION}"
        - regexp: '^.+$'
          containerImage: "some.registry/org/<my_kmod>:${KERNEL_FULL_VERSION}"
          build:
            buildArgs:
              - name: ARG_NAME
                value: <some_value>
            secrets:
              - name: <some_kubernetes_secret>
            baseImageRegistryTLS:
              insecure: false
              insecureSkipTLSVerify: false
            dockerfileConfigMap:
              name: <my_kmod_dockerfile>
          sign:
            certSecret:
              name: <cert_secret>
            keySecret:
              name: <key_secret>
            filesToSign:
              - /opt/lib/modules/${KERNEL_FULL_VERSION}/<my_kmod>.ko
          registryTLS:
            insecure: false
            insecureSkipTLSVerify: false
    serviceAccountName: <sa_module_loader>
  devicePlugin:
    container:
      image: some.registry/org/device-plugin:latest
      env:
        - name: MY_DEVICE_PLUGIN_ENV_VAR
          value: SOME_VALUE
      volumeMounts:
        - mountPath: /some/mountPath
          name: <device_plugin_volume>
    volumes:
      - name: <device_plugin_volume>
        configMap:
          name: <some_configmap>
    serviceAccountName: <sa_device_plugin>
  imageRepoSecret:
    name: <secret_name>
  selector:
    node-role.kubernetes.io/worker: ""
```

where:

`spec.moduleLoader.container.modprobe.moduleName`
Specifies the name of the module to load. This parameter is required.

`spec.moduleLoader.container.modprobe.dirName`
Specifies the directory name to use for the module. This parameter is optional.

`spec.moduleLoader.container.modprobe.firmwarePath`
Specifies the path to the firmware to use for the module. This field is optional. Copies the contents of this path into the path specified in `worker.setFirmwareClassPath` (which is preset to `/var/lib/firmware`) of the `kmm-operator-manager-config` config map. This action occurs before `modprobe` is called to insert the kernel module.

`spec.moduleLoader.container.modprobe.parameters`
Specifies the parameters to pass to the module. This parameter is optional.

`spec.moduleLoader.container.kernelMappings`
Specifies at least one kernel item. This parameter is required.

`spec.moduleLoader.container.kernelMappings.regexp`
Specifies a tag or digest. Foreach node running a kernel matching the regular expression, KMM checks if you have included a tag or a digest. If you have not specified a tag or digest in the container image, then the validation webhook returns an error and does not apply the module.

`spec.moduleLoader.container.kernelMappings.regexp`
Specifies that for any other kernel, build the image using the Dockerfile in the `my-kmod` ConfigMap.

`spec.moduleLoader.container.kernelMappings.containerImage`
Specifies the container image that holds the customer’s kmods. This container should contain the `cp` binary.

`spec.moduleLoader.container.kernelMappings.build.buildArgs`
Specifies an optional field.

`spec.moduleLoader.container.kernelMappings.build.secrets`
Specifies that a value for `some-kubernetes-secret` can be obtained from the build environment at `/run/secrets/some-kubernetes-secret`. This field is optional.

`spec.moduleLoader.container.kernelMappings.build.baseImageRegistryTLS`
This fied has no effect. When building kmod images or signing kmods within a kmod image, you might sometimes need to pull base images from a registry that serves a certificate signed by an untrusted Certificate Authority (CA). In order for KMM to trust that CA, it must also trust the new CA by replacing the cluster’s CA bundle. See "Replacing the CA Bundle certificate" to learn how to replace the cluster’s CA bundle.

`spec.moduleLoader.container.kernelMappings.build.baseImageRegistryTLS.insecureSkipTLSVerify`
Specifies to an optional parameter; avoid using it. If set to `true`, the build skips any TLS server certificate validation when pulling the image in the Dockerfile `FROM` instruction using plain HTTP. This parameter is optional.

`spec.moduleLoader.container.kernelMappings.build.dockerfileConfigMap`
Specifies the `dockerfileConfigMap` parameter. This parameter is required.

`spec.moduleLoader.container.kernelMappings.sign.certSecret`
Specifies the `certSecret` parameter. This parameter is required.

`spec.moduleLoader.container.kernelMappings.sign.keySecret`
Specifies the `keySecret` parameter. This parameter is required.

`spec.moduleLoader.container.kernelMappings.registryTLS`
Specifies an optional parameter; avoid using it. If set to `true`, KMM is allowed to check if the container image already exists using plain HTTP.

`spec.moduleLoader.container.kernelMappings.registryTLS.insecure`
Specifies a optional parameter; avoid using it. If set to `true`, KMM skips any TLS server certificate validation when checking if the container image already exists.

`spec.moduleLoader.serviceAccountName`
Specifies the `serviceAccountName` parameter. This parameter is optional.

`spec.devicePlugin`
Specifies the `devicePlugin` parameter. This parameter is optional.

`spec.devicePlugin.container.image`
Specifies the `image` parameter. This parameter is required if the device plugin section is present.

`spec.devicePlugin.container.volumeMounts`
Specifies the `volumeMounts` parameter. This parameter is optional.

`spec.devicePlugin.volumes`
Specifies the `volumes` parameter. This parameter is optional.

`spec.devicePlugin.serviceAccountName`
Specifies the `serviceAccountName` parameter. This parameter is optional.

`spec.imageRepoSecret`
Specifies the `imageRepoSecret` parameter. This parameter is used to pull module loader and device plugin images.

<div>

<div class="title">

Additional resources

</div>

- [Replacing the CA Bundle certificate](../security/certificates/updating-ca-bundle.md#ca-bundle-replacing_updating-ca-bundle)

</div>

# Using in-tree modules with the device plugin

You can configure a KMM `Module` custom resource on OpenShift Container Platform to use an in-tree kernel module and run only the device plugin. Omit the `moduleLoader` section and specify only `devicePlugin` in the CR.

<div class="example">

<div class="title">

Example `Module` CR

</div>

``` yaml
apiVersion: kmm.sigs.x-k8s.io/v1beta1
kind: Module
metadata:
  name: my-kmod
spec:
  selector:
    node-role.kubernetes.io/worker: ""
  devicePlugin:
    container:
      image: some.registry/org/my-device-plugin:latest
```

</div>

# Symbolic links for in-tree dependencies

Symbolic links let kmod images reference in-tree kernel module dependencies on OpenShift Container Platform without copying them. KMM mounts `/usr/lib/modules` so `depmod` and `modprobe` can resolve those dependencies at build and runtime.

By creating a symlink from `/opt/usr/lib/modules/<kernel_version>/<symlink_name>` to `/usr/lib/modules/<kernel_version>`, `depmod` can use the in-tree kmods on the building node’s filesystem to resolve dependencies.

At runtime, the worker pod extracts the entire image, including the `<symlink_name>` symbolic link. That symbolic link points to `/usr/lib/modules/<kernel_version>` in the worker pod, which is mounted from the node’s filesystem. `modprobe` can then follow that link and load the in-tree dependencies as needed.

In the following example, `host` is the symbolic link name under `/opt/usr/lib/modules/<kernel_version>`:

``` dockerfile
ARG DTK_AUTO

FROM ${DTK_AUTO} as builder

#
# Build steps
#

FROM ubi9/ubi

ARG KERNEL_FULL_VERSION

RUN dnf update && dnf install -y kmod

COPY --from=builder /usr/src/kernel-module-management/ci/kmm-kmod/kmm_ci_a.ko /opt/lib/modules/${KERNEL_FULL_VERSION}/
COPY --from=builder /usr/src/kernel-module-management/ci/kmm-kmod/kmm_ci_b.ko /opt/lib/modules/${KERNEL_FULL_VERSION}/

# Create the symbolic link
RUN ln -s /lib/modules/${KERNEL_FULL_VERSION} /opt/lib/modules/${KERNEL_FULL_VERSION}/host

RUN depmod -b /opt ${KERNEL_FULL_VERSION}
```

> [!NOTE]
> `depmod` generates dependency files based on the kernel modules present on the node that runs the kmod image build.
>
> On the node on which KMM loads the kernel modules, `modprobe` expects the files to be present under `/usr/lib/modules/<kernel_version>`, and the same filesystem layout. It is highly recommended that the build and the target nodes share the same operating system and release.

# Creating a kmod image

A kmod image is a standard OCI container image that holds `.ko` kernel module files for use with Kernel Module Management (KMM) on OpenShift Container Platform. You must place `.ko` files under a path that matches `<prefix>/lib/modules/[kernel-version]/`.

Keep the following in mind when working with the `.ko` files:

- In most cases, `<prefix>` should be equal to `/opt`. This is the `Module` CRD’s default value.

- `kernel-version` must not be empty and must be equal to the kernel version the kernel modules were built for.

In addition to the `.ko` files, the kmod image also requires the `cp` binary to be present because the `.ko` files are copied from this image to the image-loader worker pod created by the Operator. This is a minimal requirement and no other binary tool is required in the image.

## Running depmod

Run the `depmod` utlity at the end of the build process to generate `modules.dep` and `.map` files. This is especially useful if your kmod image contains several kernel modules and if one of the modules depends on another module.

If you are building your image on OpenShift Container Platform, consider using the Driver Toolkit (DTK). For further information, see [How to use entitled image builds to build DriverContainers with UBI on OpenShift](https://cloud.redhat.com/blog/how-to-use-entitled-image-builds-to-build-drivercontainers-with-ubi-on-openshift).

> [!NOTE]
> You must have a Red Hat subscription to download the `kernel-devel` package.

<div>

<div class="title">

Procedure

</div>

- Generate `modules.dep` and `.map` files for a specific kernel version by running the following command:

  ``` terminal
  $ depmod -b /opt ${KERNEL_FULL_VERSION}+`.
  ```

  The following example Dockerfile shows how to run `depmod` at the end of the build:

  ``` yaml
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: kmm-ci-dockerfile
  data:
    dockerfile: |
      ARG DTK_AUTO
      FROM ${DTK_AUTO} as builder
      ARG KERNEL_FULL_VERSION
      WORKDIR /usr/src
      RUN ["git", "clone", "https://github.com/rh-ecosystem-edge/kernel-module-management.git"]
      WORKDIR /usr/src/kernel-module-management/ci/kmm-kmod
      RUN KERNEL_SRC_DIR=/lib/modules/${KERNEL_FULL_VERSION}/build make all
      FROM registry.redhat.io/ubi9/ubi-minimal
      ARG KERNEL_FULL_VERSION
      RUN microdnf install kmod
      COPY --from=builder /usr/src/kernel-module-management/ci/kmm-kmod/kmm_ci_a.ko /opt/lib/modules/${KERNEL_FULL_VERSION}/
      COPY --from=builder /usr/src/kernel-module-management/ci/kmm-kmod/kmm_ci_b.ko /opt/lib/modules/${KERNEL_FULL_VERSION}/
      RUN depmod -b /opt ${KERNEL_FULL_VERSION}
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Driver Toolkit](psap-driver-toolkit.md#driver-toolkit)

</div>

## Building in the cluster

Kernel Module Management (KMM) can build kmod container images in the cluster on OpenShift Container Platform when the image does not already exist in the registry. You configure in-cluster builds through the `build` section of a kernel mapping in the `Module` CR.

- Provide build instructions using the `build` section of a kernel mapping.

- Copy the Dockerfile for your container image into a `ConfigMap` resource, under the `dockerfile` key.

- Ensure that the `ConfigMap` is located in the same namespace as the `Module`.

KMM checks if the image name specified in the `containerImage` field exists. If it does, the build is skipped.

Otherwise, KMM creates a `Build` resource to build your image. After the image is built, KMM proceeds with the `Module` reconciliation. See the following example.

``` yaml
# ...
- regexp: '^.+$'
  containerImage: "some.registry/org/<my_kmod>:${KERNEL_FULL_VERSION}"
  build:
    buildArgs:
      - name: ARG_NAME
        value: <some_value>
    secrets:
      - name: <some_kubernetes_secret>
    baseImageRegistryTLS:
      insecure: false
      insecureSkipTLSVerify: false
    dockerfileConfigMap:
      name: <my_kmod_dockerfile>
  registryTLS:
    insecure: false
    insecureSkipTLSVerify: false
```

where:

`spec.moduleLoader.container.kernelMappings.build.buildArgs`
Specifies build arguments. This field is optional.

`spec.moduleLoader.container.kernelMappings.build.secrets`
Specifies secrets. This field is optional.

`spec.moduleLoader.container.kernelMappings.build.secrets.name`
Specifies that the secret will be mounted in the file path of the build pod as `/run/secrets/some-kubernetes-secret`.

`spec.moduleLoader.container.kernelMappings.build.baseImageRegistryTLS.insecure`
Specifies an optional parameter; avoid using this parameter. If set to `true`, the build will be allowed to pull the image in the Dockerfile `FROM` instruction using plain HTTP.

`spec.moduleLoader.container.kernelMappings.build.baseImageRegistryTLS.insecureSkipTLSVerify`
Specifies an optional parameter; avoid using this parameter. If set to `true`, the build will skip any TLS server certificate validation when pulling the image in the Dockerfile `FROM` instruction using plain HTTP.

`spec.moduleLoader.container.kernelMappings.build.dockerfileConfigMap`
Specifies the Dockerfile ConfigMap. This field is required.

`spec.moduleLoader.container.kernelMappings.registryTLS.insecure`
Specifies an optional parameter; avoid using this parameter. If set to `true`, KMM will be allowed to check if the container image already exists using plain HTTP.

`spec.moduleLoader.container.kernelMappings.registryTLS.insecureSkipTLSVerify`
Specifies an optional parameter; avoid using this parameter. If set to `true`, KMM will skip any TLS server certificate validation when checking if the container image already exists.

Successful build pods are garbage collected immediately, unless the `job.gcDelay` parameter is set in the Operator configuration. Failed build pods are always preserved and must be deleted manually by the administrator for the build to be restarted.

<div>

<div class="title">

Additional resources

</div>

- [Build configuration resources](../cicd/builds/build-configuration.md#build-configuration)

- [Preflight validation for Kernel Module Management (KMM) Modules](../updating/preparing_for_updates/kmm-preflight-validation.md)

</div>

## Using the Driver Toolkit

To build kernel module loader images in OpenShift Container Platform, you can use the Driver Toolkit (DTK) as the first stage of a multi-stage Dockerfile. DTK provides kernel headers and build tools matched to the cluster OpenShift Container Platform version.

<div>

<div class="title">

Procedure

</div>

1.  Build the kernel modules.

2.  Copy the `.ko` files into a smaller end-user image such as [`ubi-minimal`](https://catalog.redhat.com/software/containers/ubi9/ubi-minimal).

3.  To leverage DTK in your in-cluster build, use the `DTK_AUTO` build argument. The value is automatically set by KMM when creating the `Build` resource. See the following example.

    ``` dockerfile
    ARG DTK_AUTO
    FROM ${DTK_AUTO} as builder
    ARG KERNEL_FULL_VERSION
    WORKDIR /usr/src
    RUN ["git", "clone", "https://github.com/rh-ecosystem-edge/kernel-module-management.git"]
    WORKDIR /usr/src/kernel-module-management/ci/kmm-kmod
    RUN KERNEL_SRC_DIR=/lib/modules/${KERNEL_FULL_VERSION}/build make all
    FROM ubi9/ubi-minimal
    ARG KERNEL_FULL_VERSION
    RUN microdnf install kmod
    COPY --from=builder /usr/src/kernel-module-management/ci/kmm-kmod/kmm_ci_a.ko /opt/lib/modules/${KERNEL_FULL_VERSION}/
    COPY --from=builder /usr/src/kernel-module-management/ci/kmm-kmod/kmm_ci_b.ko /opt/lib/modules/${KERNEL_FULL_VERSION}/
    RUN depmod -b /opt ${KERNEL_FULL_VERSION}
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Driver Toolkit](psap-driver-toolkit.md#driver-toolkit)

</div>

# Using signing with Kernel Module Management (KMM)

On Secure Boot-enabled OpenShift Container Platform systems, out-of-tree kernel modules must be signed with keys enrolled in the Machine Owner’s Key (MOK) database. For kernel modules built out of tree, KMM supports signing kmods through the `sign` section of the kernel mapping in a `Module` custom resource.

For more details on using Secure Boot, see "Generating a public and private key pair".

## Prerequisites

- A public private key pair in the correct (DER) format.

- At least one secure-boot enabled node with the public key enrolled in its MOK database.

- Either a pre-built driver container image, or the source code and Dockerfile needed to build one in-cluster.

<div>

<div class="title">

Additional resources

</div>

- [Generating a public and private key pair](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot_managing-monitoring-and-updating-the-kernel#generating-a-public-and-private-key-pair_signing-a-kernel-and-modules-for-secure-boot)

</div>

# Adding the keys for secureboot

To sign kernel modules with Kernel Module Management (KMM) on OpenShift Container Platform, you can add Secure Boot certificate and private key files as Kubernetes secrets.

For details on how to create these, see [Generating a public and private key pair](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot_managing-monitoring-and-updating-the-kernel#generating-a-public-and-private-key-pair_signing-a-kernel-and-modules-for-secure-boot).

For details on how to extract the public and private key pair, see [Signing kernel modules with the private key](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot_managing-monitoring-and-updating-the-kernel#signing-kernel-modules-with-the-private-key_signing-a-kernel-and-modules-for-secure-boot). Use steps 1 through 4 to extract the keys into files.

<div>

<div class="title">

Procedure

</div>

1.  Create the `sb_cert.cer` file that contains the certificate and the `sb_cert.priv` file that contains the private key:

    ``` terminal
    $ openssl req -x509 -new -nodes -utf8 -sha256 -days 36500 -batch -config configuration_file.config -outform DER -out my_signing_key_pub.der -keyout my_signing_key.priv
    ```

2.  Add the files by using one of the following methods:

    - Add the files as [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) directly:

      ``` terminal
      $ oc create secret generic my-signing-key --from-file=key=<my_signing_key.priv>
      ```

      ``` terminal
      $ oc create secret generic my-signing-key-pub --from-file=cert=<my_signing_key_pub.der>
      ```

    - Add the files by base64 encoding them:

      ``` terminal
      $ cat sb_cert.priv | base64 -w 0 > my_signing_key2.base64
      ```

      ``` terminal
      $ cat sb_cert.cer | base64 -w 0 > my_signing_key_pub.base64
      ```

3.  Add the encoded text to a YAML file:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: my-signing-key-pub
      namespace: default
    type: Opaque
    data:
      cert: <base64_encoded_secureboot_public_key>

    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: my-signing-key
      namespace: default
    type: Opaque
    data:
      key: <base64_encoded_secureboot_private_key>
    ```

    Replace `default` with a valid namespace.

4.  Apply the YAML file:

    ``` terminal
    $ oc apply -f <yaml_filename>
    ```

</div>

## Checking the keys

To verify that your secure boot signing keys are configured correctly in OpenShift Container Platform, you can inspect the public certificate and private key secrets with the OpenShift CLI.

<div>

<div class="title">

Procedure

</div>

1.  Check to ensure the public key secret is set correctly:

    ``` terminal
    $ oc get secret -o yaml <certificate secret name> | awk '/cert/{print $2; exit}' | base64 -d  | openssl x509 -inform der -text
    ```

    This should display a certificate with a Serial Number, Issuer, Subject, and more.

2.  Check to ensure the private key secret is set correctly:

    ``` terminal
    $ oc get secret -o yaml <private key secret name> | awk '/key/{print $2; exit}' | base64 -d
    ```

    This should display the key enclosed in the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines.

</div>

# Signing kmods in a pre-built image

To sign kernel modules in a vendor-supplied or externally built image on OpenShift Container Platform, you can configure a `Module` custom resource with unsigned and signed container image references and key secrets.

The following YAML file adds the public/private key-pair as secrets with the required key names - `key` for the private key, `cert` for the public key. The cluster then pulls down the `unsignedImage` image, opens it, signs the kernel modules listed in `filesToSign`, adds them back, and pushes the resulting image as `containerImage`.

KMM then loads the signed kmods onto all the nodes with that match the selector. The kmods are successfully loaded on any nodes that have the public key in their MOK database, and any nodes that are not secure-boot enabled, which will ignore the signature.

<div>

<div class="title">

Prerequisites

</div>

- The `keySecret` and `certSecret` secrets have been created in the same namespace as the rest of the resources.

</div>

<div>

<div class="title">

Procedure

</div>

- Apply the YAML file:

  ``` yaml
  ---
  apiVersion: kmm.sigs.x-k8s.io/v1beta1
  kind: Module
  metadata:
    name: example-module
  spec:
    moduleLoader:
      serviceAccountName: default
      container:
        modprobe:
          moduleName: '<module_name>'
        kernelMappings:
          # the kmods will be deployed on all nodes in the cluster with a kernel that matches the regexp
          - regexp: '^.*\.x86_64$'
            # the container to produce containing the signed kmods
            containerImage: <container_image_name>
            sign:
              # the image containing the unsigned kmods (we need this because we are not building the kmods within the cluster)
              unsignedImage: <unsigned_image_name>
              keySecret: # a secret holding the private secureboot key with the key 'key'
                name: <private_key_secret_name>
              certSecret: # a secret holding the public secureboot key with the key 'cert'
                name: <certificate_secret_name>
              filesToSign: # full path within the unsignedImage container to the kmod(s) to sign
                - /opt/lib/modules/4.18.0-348.2.1.el8_5.x86_64/kmm_ci_a.ko
    imageRepoSecret:
      # the name of a secret containing credentials to pull unsignedImage and push containerImage to the registry
      name: repo-pull-secret
    selector:
      kubernetes.io/arch: amd64
  ```

  where:

  `<module_name>`
  Specifies the name of the kmod to load.

  `<container_image_name>`
  Specifies the name of the container image. For example, `quay.io/myuser/my-driver:<kernelversion`.

  `<unsigned_image_name>`
  Specifies the name of the unsigned image. For example, `quay.io/myuser/my-driver:<kernelversion`.

</div>

# Specifying files to sign

You can specify full paths or wildcard and glob patterns to sign kernel module (`.ko`) files in specific directories.

Kernel Module Management (KMM) provides support for wildcard and glob pattern support for the `sign.filesToSign` field in the `Module` CR for signing kernel modules. In addition to using a full path to explicit files, you can use any glob patterns supported by the Bash shell to specify the files to sign.

The `DirName` value from `moduleLoader.container.modprobe` is propagated into the sign image. The validation webhook also verifies that all `filesToSign` entries fall under the configured `DirName`.

All paths in `filesToSign` must be under the directory defined by `DirName` in the same `moduleLoader.container.modprobe` (default `/opt`).

The KMM Operator loads the signed kmods onto all of the nodes that match the selector. The kmods should be successfully loaded on any nodes that have the public key in their Machine Owner Key (MOK) database and on any nodes that are not secure-boot enabled (which will just ignore the signature). They should fail to load on any that have secure-boot enabled but do not have that key in their MOK database.

## Defining full paths

You can define one or more absolute paths to kernel module `.ko` files inside the image.

The following example shows full path usage in the `sign.filesToSign` field:

``` yaml
sign:
  certSecret:
    name: <cert_secret>
  keySecret:
    name: <key_secret>
  filesToSign:
    - /opt/lib/modules/${KERNEL_FULL_VERSION}/<my-kmod>.ko
    - /opt/lib/modules/${KERNEL_FULL_VERSION}/<my_kmod1>.ko
    - /opt/lib/modules/${KERNEL_FULL_VERSION}/<my_kmod2>.ko
```

## Using wildcard and glob patterns

You can use wildcard and any glob expression supported by the Ash shell in the `sign.filesToSign` field. The shell expands each entry at sign time, so you can match multiple modules with a single entry.

- The following example signs all `.ko` files in that directory:

  ``` yaml
  sign:
    certSecret:
      name: <cert_secret>
    keySecret:
      name: <key_secret>
    filesToSign:
      - /opt/lib/modules/${KERNEL_FULL_VERSION}/*.ko
  ```

- The following example signs all modules matching that pattern, for example, `kmm_ci_a.ko`, `kmm_ci_b.ko`, and so on:

  ``` yaml
  sign:
    certSecret:
      name: <cert_secret>
    keySecret:
      name: <key_secret>
    filesToSign:
      - /opt/lib/modules/${KERNEL_FULL_VERSION}/kmm_ci_?.ko
  ```

- The following example signs `driver-a.ko`, `driver-b.ko`, or `driver-c.ko`:

  ``` yaml
  sign:
    certSecret:
      name: <cert_secret>
    keySecret:
      name: <key_secret>
    filesToSign:
      - /opt/lib/modules/${KERNEL_FULL_VERSION}/driver-[abc].ko
  ```

- The following example signs `mod-0.ko` through `mod-9.ko`:

  ``` yaml
  sign:
    certSecret:
      name: <cert_secret>
    keySecret:
      name: <key_secret>
    filesToSign:
      - /opt/lib/modules/${KERNEL_FULL_VERSION}/mod-[0-9].ko
  ```

# Building and signing a kmod image

To build and sign a kmod image from source code on OpenShift Container Platform, you can apply a `Module` custom resource that builds an unsigned image and then signs it with your key and certificate secrets.

The following YAML file builds a new container image using the source code from the repository. The image produced is saved back in the registry with a temporary name, and this temporary image is then signed using the parameters in the `sign` section.

The temporary image name is based on the final image name and is set to be `<containerImage>:<tag>-<namespace>_<module name>_kmm_unsigned`.

For example, using the following YAML file, Kernel Module Management (KMM) builds an image named `example.org/repository/minimal-driver:final-default_example-module_kmm_unsigned` containing the build with unsigned kmods and pushes it to the registry. Then it creates a second image named `example.org/repository/minimal-driver:final` that contains the signed kmods. It is this second image that is pulled by the worker pods and contains the kmods to be loaded on the cluster nodes.

After it is signed, you can safely delete the temporary image from the registry. It will be rebuilt, if needed.

<div>

<div class="title">

Prerequisites

</div>

- The `keySecret` and `certSecret` secrets have been created in the same namespace as the rest of the resources.

</div>

<div>

<div class="title">

Procedure

</div>

- Apply the YAML file:

  ``` yaml
  ---
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: example-module-dockerfile
    namespace: <namespace>
  data:
    dockerfile: |
      ARG DTK_AUTO
      ARG KERNEL_VERSION
      FROM ${DTK_AUTO} as builder
      WORKDIR /build/
      RUN git clone -b main --single-branch https://github.com/rh-ecosystem-edge/kernel-module-management.git
      WORKDIR kernel-module-management/ci/kmm-kmod/
      RUN make
      FROM registry.access.redhat.com/ubi9/ubi:latest
      ARG KERNEL_VERSION
      RUN yum -y install kmod && yum clean all
      RUN mkdir -p /opt/lib/modules/${KERNEL_VERSION}
      COPY --from=builder /build/kernel-module-management/ci/kmm-kmod/*.ko /opt/lib/modules/${KERNEL_VERSION}/
      RUN /usr/sbin/depmod -b /opt
  ---
  apiVersion: kmm.sigs.x-k8s.io/v1beta1
  kind: Module
  metadata:
    name: example-module
    namespace: <namespace>
  spec:
    moduleLoader:
      serviceAccountName: default
      container:
        modprobe:
          moduleName: simple_kmod
        kernelMappings:
          - regexp: '^.*\.x86_64$'
            containerImage: <final_driver_container_name>
            build:
              dockerfileConfigMap:
                name: example-module-dockerfile
            sign:
              keySecret:
                name: <private_key_secret_name>
              certSecret:
                name: <certificate_secret_name>
              filesToSign:
                - /opt/lib/modules/4.18.0-348.2.1.el8_5.x86_64/kmm_ci_a.ko
    imageRepoSecret:
      name: repo-pull-secret
    selector: # top-level selector
      kubernetes.io/arch: amd64
  ```

  where:

  `metadata.namespace`
  Specifies the namespace where the module will be deployed.

  `spec.moduleLoader.serviceAccountName`
  Specifies the service account that will be used to run the module. The default service account does not have the required permissions to run a module that is privileged. For information on creating a service account, see "Creating service accounts".

  `spec.imageRepoSecret`
  Specifies that it is used as `imagePullSecrets` in the `DaemonSet` object and to pull and push for the build and sign features.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating service accounts](../authentication/understanding-and-creating-service-accounts.md#service-accounts-managing_understanding-service-accounts).

</div>

# Using tolerations for kernel module scheduling

You can configure user-defined tolerations in the ModuleSpec resource to ensure Kernel Module Management (KMM) housekeeping pods can run on cordoned or tainted nodes during driver and kernel module upgrades.

When you taint a node to evacuate workload pods prior to an upgrade, setting matching tolerations in the ModuleSpec allows KMM housekeeping pods to deploy and execute driver maintenance without being blocked by node taints.

# Applying tolerations to kernel module pods

Kernel module pods in OpenShift Container Platform can tolerate node taints so KMM schedules them on designated nodes. You can configure toleration parameters in the `Module` custom resource to match taint effects, keys, and values on target nodes.

Taints and tolerations consist of `effect`, `key`, and `value` parameters. Tolerations include additional `operator` and `tolerationSeconds` parameters.

`effect`
Indicates the taint effect to match. If left empty, all taint effects are matched. When you set `effect`, valid values are: `NoSchedule`, `PreferNoSchedule`, or `NoExecute`.

`key`
The taint key that the toleration applies to. If left empty, all taint keys are matched. If the `key` is empty, you must set the `operator` parameter to `Exists`. This combination matches all values and all keys.

`value`
The taint value the toleration matches to. If the `operator` parameter is `Exists`, the value must be empty, otherwise use a regular string.

`operator`
Represents a relationship of a key to the value. Valid `operator` parameters are `Exists` and `Equal`. The default value is `Equal`. `Exists` is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.

`tolerationSeconds`
Represents the period of time the toleration (which must be of effect `NoExecute`, otherwise this field is ignored) tolerates the taint. By default, it is not set and the taint is tolerated forever without eviction. Zero and negative values are treated as `0` and immediately evicted by the system.

Toleration values must match the taint that is added to the nodes. A toleration matches a taint:

- If the `operator` parameter is set to `Equal`:

  - the `key` parameters are the same;

  - the `value` parameters are the same;

  - the `effect` parameters are the same.

- If the `operator` parameter is set to `Exists`:

  - the `key` parameters are the same;

  - the `effect` parameters are the same.

<div class="example">

<div class="title">

Example taint in a node specification

</div>

``` yaml
apiVersion: v1
kind: Node
metadata:
  name: <my_node>
#...
spec:
  taints:
  - effect: NoSchedule
    key: key1
    value: value1
#...
```

</div>

<div class="example">

<div class="title">

Example toleration in a module specification

</div>

``` yaml
apiVersion: kmm.sigs.x-k8s.io/v1beta1
kind: Module
metadata:
  name: <my_kmod>
spec:
  ...
  tolerations:
    effect: NoSchedule
    key: key1
    operator: Equal
    tolerationSeconds: 36000
    value: value1
```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Understanding taints and tolerations](https://docs.openshift.com/container-platform/4.17/nodes/scheduling/nodes-scheduler-taints-tolerations.html#nodes-scheduler-taints-tolerations-about_nodes-scheduler-taints-tolerations)

</div>

# KMM hub and spoke

In RHACM hub-and-spoke deployments, the KMM-Hub controller offloads kernel module building and signing to the hub cluster. Administrators can use the `ManagedClusterModule` custom resource (CR) to load modules on spoke clusters while preserving resources on managed nodes.

In hub and spoke setups, spokes are focused, resource-constrained clusters that are centrally managed by a hub cluster. Spokes run the single-cluster edition of KMM, with those resource-intensive features disabled. To adapt KMM to this environment, you should reduce the workload running on the spokes to the minimum, while the hub takes care of the expensive tasks.

Building kernel module images and signing the `.ko` files, should run on the hub. The scheduling of the Module Loader and Device Plugin `DaemonSets` can only happen on the spokes.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Advanced Cluster Management (RHACM)](https://www.redhat.com/en/technologies/management/advanced-cluster-management)

</div>

## KMM-Hub

KMM-Hub is a hub-cluster edition of Kernel Module Management for OpenShift Container Platform multi-cluster deployments. It monitors spoke kernel versions, runs image builds and kmod signing on the hub, and delivers trimmed `Module` resources to spokes through RHACM.

> [!NOTE]
> KMM-Hub cannot be used to load kernel modules on the hub cluster. Install the regular edition of KMM to load kernel modules.

<div>

<div class="title">

Additional resources

</div>

- [Installing KMM](https://openshift-kmm.netlify.app/documentation/install/)

</div>

## Installing KMM-Hub

To deploy KMM-Hub for multi-cluster kernel module management on OpenShift Container Platform, you can install it with Operator Lifecycle Manager (OLM) or by creating KMM resources manually.

<div>

<div class="title">

Additional resources

</div>

- [KMM Operator bundle](https://catalog.redhat.com/software/containers/kmm/kernel-module-management-hub-operator-bundle/63d84cc33862da54bb19b8c6?architecture=amd64&image=654273ac86f7e537ae452f6ehttps://catalog.redhat.com/software/containers/kmm/kernel-module-management-hub-operator-bundle/63d84cc33862da54bb19b8c6?architecture=amd64&image=654273ac86f7e537ae452f6e)

</div>

### Installing KMM-Hub using the Operator Lifecycle Manager

To install KMM-Hub on OpenShift Container Platform using Operator Lifecycle Manager, you can use the **Operators** section of the OpenShift web console.

<div>

<div class="title">

Procedure

</div>

- Use the **Operators** section of the OpenShift console to install KMM-Hub.

</div>

### Installing KMM-Hub by creating KMM resources

To install KMM-Hub programmatically on OpenShift Container Platform, you can create `Namespace`, `OperatorGroup`, and `Subscription` resources.

<div>

<div class="title">

Procedure

</div>

- If you want to install KMM-Hub programmatically, you can use the following resources to create the `Namespace`, `OperatorGroup` and `Subscription` resources:

  ``` yaml
  ---
  apiVersion: v1
  kind: Namespace
  metadata:
    name: openshift-kmm-hub
  ---
  apiVersion: operators.coreos.com/v1
  kind: OperatorGroup
  metadata:
    name: kernel-module-management-hub
    namespace: openshift-kmm-hub
  ---
  apiVersion: operators.coreos.com/v1alpha1
  kind: Subscription
  metadata:
    name: kernel-module-management-hub
    namespace: openshift-kmm-hub
  spec:
    channel: stable
    installPlanApproval: Automatic
    name: kernel-module-management-hub
    source: redhat-operators
    sourceNamespace: openshift-marketplace
  ```

</div>

## Using the `ManagedClusterModule` CRD

To deploy kernel modules on spoke clusters with KMM-Hub on OpenShift Container Platform, you can configure a cluster-scoped `ManagedClusterModule` custom resource that wraps a `Module` spec and selects target clusters.

This CRD is cluster-scoped, wraps a `Module` spec and adds the following additional fields:

``` yaml
apiVersion: hub.kmm.sigs.x-k8s.io/v1beta1
kind: ManagedClusterModule
metadata:
  name: <my-mcm>
  # No namespace, because this resource is cluster-scoped.
spec:
  moduleSpec:
    selector:
      node-wants-my-mcm: 'true'

  spokeNamespace: <some-namespace>

  selector:
    wants-my-mcm: 'true'
```

where:

`spec.moduleSpec`
Specifies the `moduleLoader` and `devicePlugin` sections, similar to a `Module` resource.

`spec.moduleSpec.selector`
Specifies nodes within the `ManagedCluster`.

`spec.spokeNamespace`
Specifies in which namespace the `Module` should be created.

`spec.selector`
Specifies `ManagedCluster` objects.

If build or signing instructions are present in `.spec.moduleSpec`, those pods are run on the hub cluster in the operator’s namespace.

When the `.spec.selector matches` one or more `ManagedCluster` resources, then KMM-Hub creates a `ManifestWork` resource in the corresponding namespace(s). `ManifestWork` contains a trimmed-down `Module` resource, with kernel mappings preserved but all `build` and `sign` subsections are removed. `containerImage` fields that contain image names ending with a tag are replaced with their digest equivalent.

## Running KMM on the spoke

To run Kernel Module Management (KMM) on spoke clusters in OpenShift Container Platform, you can install it with a RHACM `Policy` object. After installation, create a `ManagedClusterModule` object from the hub to deploy kernel modules.

You can install KMM on the spokes cluster through a RHACM `Policy` object. In addition to installing KMM from the software catalog and running it in a lightweight spoke mode, the `Policy` configures additional RBAC required for the RHACM agent to be able to manage `Module` resources.

<div>

<div class="title">

Procedure

</div>

- Use the following RHACM policy to install KMM on spoke clusters:

      ---
      apiVersion: policy.open-cluster-management.io/v1
      kind: Policy
      metadata:
        name: install-kmm
      spec:
        remediationAction: enforce
        disabled: false
        policy-templates:
          - objectDefinition:
              apiVersion: policy.open-cluster-management.io/v1
              kind: ConfigurationPolicy
              metadata:
                name: install-kmm
              spec:
                severity: high
                object-templates:
                - complianceType: mustonlyhave
                  objectDefinition:
                    apiVersion: v1
                    kind: Namespace
                    metadata:
                      name: openshift-kmm
                - complianceType: mustonlyhave
                  objectDefinition:
                    apiVersion: operators.coreos.com/v1
                    kind: OperatorGroup
                    metadata:
                      name: kmm
                      namespace: openshift-kmm
                    spec:
                      upgradeStrategy: Default
                - complianceType: mustonlyhave
                  objectDefinition:
                    apiVersion: operators.coreos.com/v1alpha1
                    kind: Subscription
                    metadata:
                      name: kernel-module-management
                      namespace: openshift-kmm
                    spec:
                      channel: stable
                      config:
                        env:
                          - name: KMM_MANAGED
                            value: "1"
                      installPlanApproval: Automatic
                      name: kernel-module-management
                      source: redhat-operators
                      sourceNamespace: openshift-marketplace
                - complianceType: mustonlyhave
                  objectDefinition:
                    apiVersion: rbac.authorization.k8s.io/v1
                    kind: ClusterRole
                    metadata:
                      name: kmm-module-manager
                    rules:
                      - apiGroups: [kmm.sigs.x-k8s.io]
                        resources: [modules]
                        verbs: [create, delete, get, list, patch, update, watch]
                - complianceType: mustonlyhave
                  objectDefinition:
                    apiVersion: rbac.authorization.k8s.io/v1
                    kind: ClusterRoleBinding
                    metadata:
                      name: klusterlet-kmm
                    subjects:
                    - kind: ServiceAccount
                      name: klusterlet-work-sa
                      namespace: open-cluster-management-agent
                    roleRef:
                      kind: ClusterRole
                      name: kmm-module-manager
                      apiGroup: rbac.authorization.k8s.io
      ---
      apiVersion: apps.open-cluster-management.io/v1
      kind: PlacementRule
      metadata:
        name: all-managed-clusters
      spec:
        clusterSelector:
          matchExpressions: []
      ---
      apiVersion: policy.open-cluster-management.io/v1
      kind: PlacementBinding
      metadata:
        name: install-kmm
      placementRef:
        apiGroup: apps.open-cluster-management.io
        kind: PlacementRule
        name: all-managed-clusters
      subjects:
        - apiGroup: policy.open-cluster-management.io
          kind: Policy
          name: install-kmm

  where:

  `spec.policy-templates.objectDefinition.spec.object-templates.objectDefinition.spec.config.env.name`
  Specifies the environment variable name on the `Subscription` object entry. This variable is required when running KMM on a spoke cluster.

  `spec.clusterSelector`
  Specifies that on the `PlacementRule` object entry, this field can be customized to target select clusters only.

</div>

# Customizing upgrades for kernel modules

The Kernel Module Management (KMM) Operator periodically upgrades `Module` resources in the cluster, typically during a cluster upgrade.

Use this procedure to upgrade the kernel module while running maintenance operations on the node, including rebooting the node, if needed. To minimize the impact on the workloads running in the cluster, run the kernel upgrade process sequentially, one node at a time.

> [!NOTE]
> This procedure requires knowledge of the workload using the kernel module and must be managed by the cluster administrator.

<div>

<div class="title">

Prerequisites

</div>

- Before upgrading, set the `kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>=$moduleVersion` label on all the nodes that are used by the kernel module.

- End all user application workloads on the node or move them to another node.

- Unload the currently loaded kernel module.

- Ensure that the user workload (the application running in the cluster that is accessing kernel module) is not running on the node before the kernel module unloads and that the workload is back running on the node after the new kernel module version has been loaded.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Ensure that the device plugin managed by KMM on the node is unloaded.

2.  Update the following fields in the `Module` custom resource (CR):

    - `containerImage` (to the appropriate kernel version)

    - `version`

      The update should be atomic; that is, both the `containerImage` and `version` fields must be updated simultaneously.

3.  End any workload using the kernel module on the node being upgraded.

4.  Remove the `kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>` label on the node. Run the following command to unload the kernel module from the node:

    ``` terminal
    $ oc label node/<node_name> kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>-
    ```

5.  If required, as the cluster administrator, perform any additional maintenance required on the node for the kernel module upgrade.

    If no additional upgrading is needed, you can skip Steps 3 through 6 by updating the `kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>` label value to the new `$moduleVersion` as set in the `Module`.

6.  Run the following command to add the `kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>=$moduleVersion` label to the node. The `$moduleVersion` must be equal to the new value of the `version` field in the `Module` CR.

    ``` terminal
    $ oc label node/<node_name> kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>=<desired_version>
    ```

    > [!NOTE]
    > Because of Kubernetes limitations in label names, the combined length of `Module` name and namespace must not exceed 39 characters.

    The Operator labels the node with a `version.ready` label to indicate that the new version of the kernel module is loaded and is ready to be used:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    `kmm.node.kubernetes.io/<module-namespace>.<module-name>.version.ready=<module-version>`
    ```

    </div>

7.  Restore any workload that leverages the kernel module on the node.

8.  Reload the device plugin managed by KMM on the node.

</div>

# Day 1 kernel module loading

Day 1 kernel module loading lets you insert kernel modules during Linux `systemd` initialization on OpenShift Container Platform, before the standard KMM Day 2 loading and a complete initialization of a Linux (RHCOS) server. You can use the Machine Config Operator (MCO) when a module must load earlier than full node initialization.

<div>

<div class="title">

Additional resources

</div>

- [Machine Config Operator](../machine_configuration/index.md#machine-config-index)

</div>

## Day 1 supported use cases

Day 1 supported use cases define when OpenShift Container Platform can load out-of-tree (OOT) kernel modules before NetworkManager starts. This functionality does not support loading modules during the `initramfs` stage.

The following are the conditions needed for Day 1 functionality:

- The kernel module is not loaded in the kernel.

- The in-tree kernel module is loaded into the kernel, but can be unloaded and replaced by the OOT kernel module. This means that the in-tree module is not referenced by any other kernel modules.

- In order for Day 1 functionlity to work, the node must have a functional network interface, that is, an in-tree kernel driver for that interface. The OOT kernel module can be a network driver that will replace the functional network driver.

## OOT kernel module loading flow

To load an out-of-tree kernel module during OpenShift Container Platform node boot, you can apply a `MachineConfig` through the Machine Config Operator (MCO). MCO reboots nodes and deploys `systemd` services that pull the kernel module image and swap in-tree modules for OOT modules.

<div>

<div class="title">

Procedure

</div>

1.  Apply a `MachineConfig` resource to the existing running cluster. In order to identify the necessary nodes that need to be updated, you must create an appropriate `MachineConfigPool` resource.

2.  MCO applies the reboots node by node. On any rebooted node, two new `systemd` services are deployed: `pull` service and `load` service.

3.  The `load` service is configured to run prior to the `NetworkConfiguration` service. The service tries to pull a predefined kernel module image and then, using that image, to unload an in-tree module and load an OOT kernel module.

4.  The `pull` service is configured to run after NetworkManager service. The service checks if the preconfigured kernel module image is located on the node’s filesystem. If it is, the service exists normally, and the server continues with the boot process. If not, it pulls the image onto the node and reboots the node afterwards.

</div>

## The kernel module image

Day 1 kernel module loading in OpenShift Container Platform uses Driver Toolkit-based container images shared with Day 2 KMM builds. These images must contain your out-of-tree kernel modules so the Machine Config Operator can pull and load them during node boot.

The out-of-tree kernel module should be located under `/opt/lib/modules/${kernelVersion}`.

<div>

<div class="title">

Additional resources

</div>

- [Driver Toolkit](psap-driver-toolkit.md#driver-toolkit)

</div>

## In-tree module replacement

Day 1 kernel module loading in OpenShift Container Platform replaces in-tree kernel modules with out-of-tree (OOT) versions when present. If the in-tree module is not loaded, KMM loads the OOT module without affecting the flow.

## MCO yaml creation

Kernel Module Management (KMM) exposes a `ProduceMachineConfig` API that generates Machine Config Operator (MCO) YAML for Day 1 out-of-tree kernel module loading on OpenShift Container Platform. You apply the returned manifest to target nodes in a specified `MachineConfigPool` object.

``` console
ProduceMachineConfig(machineConfigName, machineConfigPoolRef, kernelModuleImage, kernelModuleName string) (string, error)
```

The returned output is a string representation of the MCO YAML manifest to be applied. It is up to the customer to apply this YAML.

The parameters are:

`machineConfigName`
The name of the MCO YAML manifest. This parameter is set as the `name` parameter of the metadata of the MCO YAML manifest.

`machineConfigPoolRef`
The `MachineConfigPool` name used to identify the targeted nodes.

`kernelModuleImage`
The name of the container image that includes the OOT kernel module.

`kernelModuleName`
The name of the OOT kernel module. This parameter is used both to unload the in-tree kernel module (if loaded into the kernel) and to load the OOT kernel module.

The API is located under `pkg/mcproducer` package of the KMM source code. The KMM operator does not need to be running to use the Day 1 functionality. You only need to import the `pkg/mcproducer` package into their operator/utility code, call the API, and apply the produced MCO YAML to the cluster.

## The MachineConfigPool

A `MachineConfigPool` objectidentifies a collection of OpenShift Container Platform nodes affected by Machine Config Operator changes.

``` yaml
kind: MachineConfigPool
metadata:
  name: sfc
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker, sfc]}
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/sfc: ""
  paused: false
  maxUnavailable: 1
```

where:

`spec.machineConfigSelector`
Specifies labels that match in the MachineConfig.

`spec.nodeSelector`
Specifies labels that match on the node.

There are predefined `MachineConfigPools` in the OCP cluster:

- `worker`: Targets all worker nodes in the cluster

- `master`: Targets all master nodes in the cluster

Define the following `MachineConfig` to target the master `MachineConfigPool`:

``` yaml
metadata:
  labels:
    machineconfiguration.opensfhit.io/role: master
```

Define the following `MachineConfig` to target the worker `MachineConfigPool`:

``` yaml
metadata:
  labels:
    machineconfiguration.opensfhit.io/role: worker
```

<div>

<div class="title">

Additional resources

</div>

- [About MachineConfigPool](https://www.redhat.com/en/blog/openshift-container-platform-4-how-does-machine-config-pool-work)

</div>

# Managing Day 1 kmod images

Kmod images using the Day 1 utility can be managed by the KMM Operator for full lifecycle management.

In cases where a kmod was installed using the Day 1 utility and a `MachineConfig` is present in the cluster you can create a `Module` in the cluster targetting the same kmod and kernel as the `MachineConfig`. The KMM Operator attempts to load the kmod, but nothing will happen since it is already loaded in the kernel. Future upgrades can be done like Day 2 operations by updating the `Module` CR in the cluster.

The problem with this approach is if a sudden node reboot occurs, the node is rebooted with the kmod from the `MachineConfig` and not the kmod from the `Module` if a kmod upgrade was performed.

Using a `BootMachineConfig` (BMC) CRD can mitigate this issue. When a Day 1 kmod is transitioned to the KMM Operator using a `Module`, a BMC needs to be created in the cluster to address the sudden reboot issues by ensuring that the `MachineConfig` is updated with the correct values without triggering a node reboot.

The following example shows a typical `BootMachineConfig` CRD:

``` yaml
apiVersion: kmm.sigs.x-k8s.io/v1beta1
 kind: BootModuleConfig
 metadata:
  name: example-bmc
  namespace: openshift-machine-config-operator
 spec:
  machineConfigName: worker-kmod-config
  machineConfigPoolName: worker
  kernelModuleImage: quay.io/example/kmod
  kernelModuleName: my_module
  inTreeModulesToRemove:
    - intree_module_1
    - intree_module_2
  firmwareFilesPath: /firmware
  workerImage: quay.io/<USER>/kernel-module-management-worker:latest
 status:
  conditions: []
```

`machineConfigName`
The `machineConfig` that is targeted by the BMC.

`machineConfigPoolName`
The `machineConfig` pool that is linked to the targeted `machineConfig`.

`kernelModuleImage`
The kernel module container image that contains the kernel module `.ko` file without the tag. The pull service determines the kernel version of the node and then uses this value as a tag for the kernel module image. Before upgrading the cluster, all you need to do is to create a kernel module image with the appropriate tag, without any need to update the Day 1 `machineConfig`. When the node is rebooted, the pull service pulls the correct image.

`kernelModuleName`
The name of the kernel module to be loaded (the name of the `.ko` file without the `.ko`).

`inTreeModulesToRemove`
An optional list of the in-tree kernel module to remove prior to loading the OOT kernel module.

`firmwareFilesPath`
An optional path of the firmware files in the kernel module container image.

`workerImage`
An optional KMM worker image. If not specified, the current worker image is used.

# Debugging and troubleshooting

Unsigned or incorrectly signed kmods in KMM driver containers on OpenShift Container Platform can cause `PostStartHookError` or `CrashLoopBackOff` states. You can verify signing issues by running `oc describe` on the container and checking for a `Required key not available` error.

The following message appears in this scenario:

``` terminal
modprobe: ERROR: could not insert '<your_kmod_name>': Required key not available
```

# KMM firmware support

KMM firmware support copying firmware files from the kmod image to a node on OpenShift Container Platform before loading a kernel module.

The contents of `.spec.moduleLoader.container.modprobe.firmwarePath` are copied into the `/var/lib/firmware` path on the node before running the `modprobe` command to insert the kernel module.

All files and empty directories are removed from that location before running the `modprobe -r` command to unload the kernel module, when the pod is terminated.

## Configuring the lookup path on nodes

To add `/var/lib/firmware` to the kernel firmware lookup path on OpenShift Container Platform nodes, you can create a `MachineConfig` custom resource that sets the `firmware_class.path` kernel argument.

On OpenShift Container Platform nodes, the set of default lookup paths for firmwares does not include the `/var/lib/firmware` path.

<div>

<div class="title">

Procedure

</div>

1.  Use the Machine Config Operator to create a `MachineConfig` custom resource (CR) that contains the `/var/lib/firmware` path:

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfig
    metadata:
      labels:
        machineconfiguration.openshift.io/role: worker
      name: 99-worker-kernel-args-firmware-path
    spec:
      kernelArguments:
        - 'firmware_class.path=/var/lib/firmware'
    ```

    You can configure the label based on your needs. In the case of single-node OpenShift, use either `control-pane` or `master` objects.

2.  By applying the `MachineConfig` CR, the nodes are automatically rebooted.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Machine Config Operator](../machine_configuration/index.md#machine-config-operator_machine-config-overview)

</div>

## Building a kmod image

To build a kmod image with firmware support in OpenShift Container Platform, you can include the binary firmware in the builder image alongside the kernel module.

<div>

<div class="title">

Procedure

</div>

- In addition to building the kernel module itself, include the binary firmware in the builder image:

  ``` dockerfile
  FROM registry.redhat.io/ubi9/ubi-minimal as builder

  # Build the kmod

  RUN ["mkdir", "/firmware"]
  RUN ["curl", "-o", "/firmware/firmware.bin", "https://artifacts.example.com/firmware.bin"]

  FROM registry.redhat.io/ubi9/ubi-minimal

  # Copy the kmod, install modprobe, run depmod

  COPY --from=builder /firmware /firmware
  ```

</div>

## Tuning the Module resource

To configure firmware file paths for kernel modules on OpenShift Container Platform, you can set `.spec.moduleLoader.container.modprobe.firmwarePath` in the `Module` CR.

<div>

<div class="title">

Procedure

</div>

- Set `.spec.moduleLoader.container.modprobe.firmwarePath` in the `Module` custom resource (CR):

  ``` yaml
  apiVersion: kmm.sigs.x-k8s.io/v1beta1
  kind: Module
  metadata:
    name: my-kmod
  spec:
    moduleLoader:
      container:
        modprobe:
          moduleName: my-kmod  # Required

          firmwarePath: /firmware
  ```

  where:

  `spec.moduleLoader.container.modprobe.firmwarePath`
  Specifies that `/firmware/*` is copied into the files path `/var/lib/firmware/` on the node. This parameter is optional.

</div>

# Day 0 through Day 2 kmod installation

You can install some kernel modules (kmods) during Day 0 through Day 2 operations without Kernel Module Management (KMM). You can use these stages to plan kmod transitions to KMM.

Use the following criteria to determine suitable kmod installations.

Day 0
The most basic kmods that are required for a node to become `Ready` in the cluster. Examples of these types of kmods include:

- A storage driver that is required to mount the rootFS as part of the boot process

- A network driver that is required for the machine to access `machine-config-server` on the bootstrap node to pull the ignition and join the cluster

Day 1
Kmods that are not required for a node to become `Ready` in the cluster but cannot be unloaded when the node is `Ready`.

An example of this type of kmod is an out-of-tree (OOT) network driver that replaces an outdated in-tree driver to exploit the full potential of the NIC while `NetworkManager` depends on it. When the node is `Ready`, you cannot unload the driver because of the `NetworkManager` dependency.

Day 2
Kmods that can be dynamically loaded to the kernel or removed from it without interfering with the cluster infrastructure, for example, connectivity.

Examples of these types of kmods include:

- GPU operators

- Secondary network adapters

- field-programmable gate arrays (FPGAs)

## Layering background

Layering applies Day 0 kernel modules through the Machine Config Operator (MCO) on OpenShift Container Platform, so cluster upgrades do not trigger node upgrades for those modules. You recompile the driver only when you add new features, because the node operating system stays the same.

## Lifecycle management

KMM lifecycle management on OpenShift Container Platform lets you upgrade kmods from Day 0 through Day 2 without rebooting nodes when the driver supports it.

> [!NOTE]
> This will not work if the upgrade requires a node reboot, for example, when rebuilding `initramfs` files is needed.

Use one of the following options for lifecycle management.

### Treat the kmod as an in-tree driver

Use this method when you want to upgrade the kmods. In this case, treat the kmod as an in-tree driver and create a `Module` in the cluster with the `inTreeRemoval` field to unload the old version of the driver.

Note the following characteristics of treating the kmod as an in-tree driver:

- Downtime might occur as KMM tries to unload and load the kmod on all the selected nodes simultaneously.

- This works if removing the driver makes the node lose connectivity because KMM uses a single pod to unload and load the driver.

### Use ordered upgrade

You can use ordered upgrade (ordered_upgrade.md) to create a versioned `Module` in the cluster representing the kmods with no effect, because the kmods are already loaded.

Note the following characteristics of using ordered upgrade:

- There is no cluster downtime because you control the pace of the upgrade and how many nodes are upgraded at the same time; therefore, an upgrade with no downtime is possible.

- This method will not work if unloading the driver results in losing connection to the node, because KMM creates two different worker pods for unloading and another for loading. These pods will not be scheduled.

# Troubleshooting KMM

When troubleshooting KMM on OpenShift Container Platform, you can monitor Operator logs to identify the failure stage and gather diagnostic data for that stage.

## Reading Operator logs

KMM and KMM-Hub Operator logs on OpenShift Container Platform provide diagnostic information for troubleshooting installation and runtime issues. You can read them with the `oc logs` command against the controller and webhook server deployments.

Example command for KMM controller
``` terminal
$ oc logs -fn openshift-kmm deployments/kmm-operator-controller
```

Example command for KMM webhook server
``` terminal
$ oc logs -fn openshift-kmm deployments/kmm-operator-webhook-server
```

Example command for KMM-Hub controller
``` terminal
$ oc logs -fn openshift-kmm-hub deployments/kmm-operator-hub-controller
```

Example command for KMM-Hub webhook server
``` terminal
$ oc logs -fn openshift-kmm deployments/kmm-operator-hub-webhook-server
```

## Observing events

You can observe Kernel Module Management (KMM) events on OpenShift Container Platform to monitor kmod image builds, signing, and module load or unload operations. Events attach to `Module` and `Node` objects and appear in `oc describe` output.

### Build & sign

KMM publishes events whenever it starts a kmod image build or observes its outcome. These events are attached to `Module` objects and are available at the end of the output of `oc describe module` command, as in the following example:

``` terminal
$ oc describe modules.kmm.sigs.x-k8s.io kmm-ci-a
[...]
Events:
  Type    Reason          Age                From  Message
  ----    ------          ----               ----  -------
  Normal  BuildCreated    2m29s              kmm   Build created for kernel 6.6.2-201.fc39.x86_64
  Normal  BuildSucceeded  63s                kmm   Build job succeeded for kernel 6.6.2-201.fc39.x86_64
  Normal  SignCreated     64s (x2 over 64s)  kmm   Sign created for kernel 6.6.2-201.fc39.x86_64
  Normal  SignSucceeded   57s                kmm   Sign job succeeded for kernel 6.6.2-201.fc39.x86_64
```

### Module load or unload

KMM publishes events whenever it successfully loads or unloads a kernel module on a node. These events are attached to `Node` objects and are available at the end of the output of `oc describe node` command, as in the following example:

``` terminal
$ oc describe node my-node
[...]
Events:
  Type    Reason          Age    From  Message
  ----    ------          ----   ----  -------
[...]
  Normal  ModuleLoaded    4m17s  kmm   Module default/kmm-ci-a loaded into the kernel
  Normal  ModuleUnloaded  2s     kmm   Module default/kmm-ci-a unloaded from the kernel
```

## Using the must-gather tool

To collect Kernel Module Management debugging data for Red Hat Support on OpenShift Container Platform, you can run the `oc adm must-gather` command with KMM-specific arguments.

<div>

<div class="title">

Additional resources

</div>

- [About the must-gather tool](../support/gathering-cluster-data.md#about-must-gather_gathering-cluster-data)

</div>

### Gathering data for KMM

To troubleshoot Kernel Module Management (KMM) on OpenShift Container Platform, you can gather Operator data with the `must-gather` tool and review controller manager logs.

<div>

<div class="title">

Procedure

</div>

1.  Gather the data for the KMM Operator controller manager:

    1.  Set the `MUST_GATHER_IMAGE` variable:

        ``` terminal
        $ export MUST_GATHER_IMAGE=$(oc get deployment -n openshift-kmm kmm-operator-controller -ojsonpath='{.spec.template.spec.containers[?(@.name=="manager")].env[?(@.name=="RELATED_IMAGE_MUST_GATHER")].value}')
        ```

        ``` terminal
        $ oc adm must-gather --image="${MUST_GATHER_IMAGE}" -- /usr/bin/gather
        ```

        > [!NOTE]
        > Use the `-n <namespace>` switch to specify a namespace if you installed KMM in a custom namespace.

    2.  Run the `must-gather` tool:

        ``` terminal
        $ oc adm must-gather --image="${MUST_GATHER_IMAGE}" -- /usr/bin/gather
        ```

2.  View the Operator logs:

    ``` terminal
    $ oc logs -fn openshift-kmm deployments/kmm-operator-controller
    ```

    Example output:

    ``` terminal
    I0228 09:36:37.352405       1 request.go:682] Waited for 1.001998746s due to client-side throttling, not priority and fairness, request: GET:https://172.30.0.1:443/apis/machine.openshift.io/v1beta1?timeout=32s
    I0228 09:36:40.767060       1 listener.go:44] kmm/controller-runtime/metrics "msg"="Metrics server is starting to listen" "addr"="127.0.0.1:8080"
    I0228 09:36:40.769483       1 main.go:234] kmm/setup "msg"="starting manager"
    I0228 09:36:40.769907       1 internal.go:366] kmm "msg"="Starting server" "addr"={"IP":"127.0.0.1","Port":8080,"Zone":""} "kind"="metrics" "path"="/metrics"
    I0228 09:36:40.770025       1 internal.go:366] kmm "msg"="Starting server" "addr"={"IP":"::","Port":8081,"Zone":""} "kind"="health probe"
    I0228 09:36:40.770128       1 leaderelection.go:248] attempting to acquire leader lease openshift-kmm/kmm.sigs.x-k8s.io...
    I0228 09:36:40.784396       1 leaderelection.go:258] successfully acquired lease openshift-kmm/kmm.sigs.x-k8s.io
    I0228 09:36:40.784876       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module" "source"="kind source: *v1beta1.Module"
    I0228 09:36:40.784925       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module" "source"="kind source: *v1.DaemonSet"
    I0228 09:36:40.784968       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module" "source"="kind source: *v1.Build"
    I0228 09:36:40.785001       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module" "source"="kind source: *v1.Job"
    I0228 09:36:40.785025       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module" "source"="kind source: *v1.Node"
    I0228 09:36:40.785039       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="Module" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="Module"
    I0228 09:36:40.785458       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="PodNodeModule" "controllerGroup"="" "controllerKind"="Pod" "source"="kind source: *v1.Pod"
    I0228 09:36:40.786947       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="PreflightValidation" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidation" "source"="kind source: *v1beta1.PreflightValidation"
    I0228 09:36:40.787406       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="PreflightValidation" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidation" "source"="kind source: *v1.Build"
    I0228 09:36:40.787474       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="PreflightValidation" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidation" "source"="kind source: *v1.Job"
    I0228 09:36:40.787488       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="PreflightValidation" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidation" "source"="kind source: *v1beta1.Module"
    I0228 09:36:40.787603       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="NodeKernel" "controllerGroup"="" "controllerKind"="Node" "source"="kind source: *v1.Node"
    I0228 09:36:40.787634       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="NodeKernel" "controllerGroup"="" "controllerKind"="Node"
    I0228 09:36:40.787680       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="PreflightValidation" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidation"
    I0228 09:36:40.785607       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream" "source"="kind source: *v1.ImageStream"
    I0228 09:36:40.787822       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="preflightvalidationocp" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidationOCP" "source"="kind source: *v1beta1.PreflightValidationOCP"
    I0228 09:36:40.787853       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream"
    I0228 09:36:40.787879       1 controller.go:185] kmm "msg"="Starting EventSource" "controller"="preflightvalidationocp" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidationOCP" "source"="kind source: *v1beta1.PreflightValidation"
    I0228 09:36:40.787905       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="preflightvalidationocp" "controllerGroup"="kmm.sigs.x-k8s.io" "controllerKind"="PreflightValidationOCP"
    I0228 09:36:40.786489       1 controller.go:193] kmm "msg"="Starting Controller" "controller"="PodNodeModule" "controllerGroup"="" "controllerKind"="Pod"
    ```

</div>

### Gathering data for KMM-Hub

To collect diagnostic data for the KMM-Hub Operator on OpenShift Container Platform, you can run the `must-gather` tool with the hub controller image and review Operator logs.

<div>

<div class="title">

Procedure

</div>

1.  Gather the data for the KMM Operator hub controller manager:

    1.  Set the `MUST_GATHER_IMAGE` variable:

        ``` terminal
        $ export MUST_GATHER_IMAGE=$(oc get deployment -n openshift-kmm-hub kmm-operator-hub-controller -ojsonpath='{.spec.template.spec.containers[?(@.name=="manager")].env[?(@.name=="RELATED_IMAGE_MUST_GATHER")].value}')
        ```

        ``` terminal
        $ oc adm must-gather --image="${MUST_GATHER_IMAGE}" -- /usr/bin/gather -u
        ```

        > [!NOTE]
        > Use the `-n <namespace>` switch to specify a namespace if you installed KMM in a custom namespace.

    2.  Run the `must-gather` tool:

        ``` terminal
        $ oc adm must-gather --image="${MUST_GATHER_IMAGE}" -- /usr/bin/gather -u
        ```

2.  View the Operator logs:

    ``` terminal
    $ oc logs -fn openshift-kmm-hub deployments/kmm-operator-hub-controller
    ```

    Example output:

    ``` terminal
    I0417 11:34:08.807472       1 request.go:682] Waited for 1.023403273s due to client-side throttling, not priority and fairness, request: GET:https://172.30.0.1:443/apis/tuned.openshift.io/v1?timeout=32s
    I0417 11:34:12.373413       1 listener.go:44] kmm-hub/controller-runtime/metrics "msg"="Metrics server is starting to listen" "addr"="127.0.0.1:8080"
    I0417 11:34:12.376253       1 main.go:150] kmm-hub/setup "msg"="Adding controller" "name"="ManagedClusterModule"
    I0417 11:34:12.376621       1 main.go:186] kmm-hub/setup "msg"="starting manager"
    I0417 11:34:12.377690       1 leaderelection.go:248] attempting to acquire leader lease openshift-kmm-hub/kmm-hub.sigs.x-k8s.io...
    I0417 11:34:12.378078       1 internal.go:366] kmm-hub "msg"="Starting server" "addr"={"IP":"127.0.0.1","Port":8080,"Zone":""} "kind"="metrics" "path"="/metrics"
    I0417 11:34:12.378222       1 internal.go:366] kmm-hub "msg"="Starting server" "addr"={"IP":"::","Port":8081,"Zone":""} "kind"="health probe"
    I0417 11:34:12.395703       1 leaderelection.go:258] successfully acquired lease openshift-kmm-hub/kmm-hub.sigs.x-k8s.io
    I0417 11:34:12.396334       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "source"="kind source: *v1beta1.ManagedClusterModule"
    I0417 11:34:12.396403       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "source"="kind source: *v1.ManifestWork"
    I0417 11:34:12.396430       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "source"="kind source: *v1.Build"
    I0417 11:34:12.396469       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "source"="kind source: *v1.Job"
    I0417 11:34:12.396522       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "source"="kind source: *v1.ManagedCluster"
    I0417 11:34:12.396543       1 controller.go:193] kmm-hub "msg"="Starting Controller" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule"
    I0417 11:34:12.397175       1 controller.go:185] kmm-hub "msg"="Starting EventSource" "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream" "source"="kind source: *v1.ImageStream"
    I0417 11:34:12.397221       1 controller.go:193] kmm-hub "msg"="Starting Controller" "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream"
    I0417 11:34:12.498335       1 filter.go:196] kmm-hub "msg"="Listing all ManagedClusterModules" "managedcluster"="local-cluster"
    I0417 11:34:12.498570       1 filter.go:205] kmm-hub "msg"="Listed ManagedClusterModules" "count"=0 "managedcluster"="local-cluster"
    I0417 11:34:12.498629       1 filter.go:238] kmm-hub "msg"="Adding reconciliation requests" "count"=0 "managedcluster"="local-cluster"
    I0417 11:34:12.498687       1 filter.go:196] kmm-hub "msg"="Listing all ManagedClusterModules" "managedcluster"="sno1-0"
    I0417 11:34:12.498750       1 filter.go:205] kmm-hub "msg"="Listed ManagedClusterModules" "count"=0 "managedcluster"="sno1-0"
    I0417 11:34:12.498801       1 filter.go:238] kmm-hub "msg"="Adding reconciliation requests" "count"=0 "managedcluster"="sno1-0"
    I0417 11:34:12.501947       1 controller.go:227] kmm-hub "msg"="Starting workers" "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream" "worker count"=1
    I0417 11:34:12.501948       1 controller.go:227] kmm-hub "msg"="Starting workers" "controller"="ManagedClusterModule" "controllerGroup"="hub.kmm.sigs.x-k8s.io" "controllerKind"="ManagedClusterModule" "worker count"=1
    I0417 11:34:12.502285       1 imagestream_reconciler.go:50] kmm-hub "msg"="registered imagestream info mapping" "ImageStream"={"name":"driver-toolkit","namespace":"openshift"} "controller"="imagestream" "controllerGroup"="image.openshift.io" "controllerKind"="ImageStream" "dtkImage"="quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:df42b4785a7a662b30da53bdb0d206120cf4d24b45674227b16051ba4b7c3934" "name"="driver-toolkit" "namespace"="openshift" "osImageVersion"="412.86.202302211547-0" "reconcileID"="e709ff0a-5664-4007-8270-49b5dff8bae9"
    ```

</div>
