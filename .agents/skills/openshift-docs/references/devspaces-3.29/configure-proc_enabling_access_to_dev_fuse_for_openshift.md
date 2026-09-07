> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_enabling_access_to_dev_fuse_for_openshift). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Enable `/dev/fuse` access on OpenShift 4.14 and earlier

Enable `/dev/fuse` access for workspace containers on OpenShift versions older than 4.15, so that workspaces can use the fuse-overlayfs storage driver for Podman and Buildah.

## Before you begin

- You have the [Butane](https://docs.openshift.com/container-platform/4.22/installing/install_config/installing-customizing.html#installation-special-config-butane-install_installing-customizing) tool (`butane`) installed.

<!-- -->

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

Note

For OpenShift 4.15 and later, `/dev/fuse` is available by default and no additional configuration is needed. See [Release Notes](https://docs.openshift.com/container-platform/4.15/release_notes/ocp-4-15-release-notes.html#ocp-4-15-nodes-dev-fuse).

Warning

Creating `MachineConfig` resources on an OpenShift cluster is a potentially dangerous task, as you are making advanced, system-level changes to the cluster.

View the [MachineConfig documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/machine-config-index#about-machine-config-operator_machine-config-overview) for more details and possible risks.

## Procedure

1.  Set the environment variable based on the type of your OpenShift cluster: a single node cluster, or a multi node cluster with separate control plane and worker nodes.
    - For a single node cluster, set:

      ``` bash
      $ NODE_ROLE=master
      ```

    - For a multi node cluster, set:

      ``` bash
      $ NODE_ROLE=worker
      ```

2.  Set the environment variable for the OpenShift Butane config version. This variable is the major and minor version of the OpenShift cluster. For example, `4.12.0`, `4.13.0`, or `4.14.0`.

    ``` bash
    $ VERSION=4.12.0
    ```

3.  Create a `MachineConfig` resource that creates a drop-in CRI-O configuration file named `99-podman-fuse` in the `NODE_ROLE` nodes. This configuration file makes access to the `/dev/fuse` device possible for certain pods.

    ``` bash
    cat << EOF | butane | oc apply -f -
    variant: openshift
    version: ${VERSION}
    metadata:
      labels:
        machineconfiguration.openshift.io/role: ${NODE_ROLE}
      name: 99-podman-dev-fuse-${NODE_ROLE}
    storage:
      files:
      - path: /etc/crio/crio.conf.d/99-podman-fuse
        mode: 0644
        overwrite: true
        contents:
          inline: |
            [crio.runtime.workloads.podman-fuse]
            activation_annotation = "io.openshift.podman-fuse"
            allowed_annotations = [
              "io.kubernetes.cri-o.Devices"
            ]
            [crio.runtime]
            allowed_devices = ["/dev/fuse"]
    EOF
    ```

    where:

    `/etc/crio/crio.conf.d/99-podman-fuse`  
    The absolute file path to the new drop-in configuration file for CRI-O.

    `contents`  
    The content of the new drop-in configuration file.

    `[crio.runtime.workloads.podman-fuse]`  
    Define a `podman-fuse` workload.

    `activation_annotation`  
    The pod annotation that activates the `podman-fuse` workload settings.

    `allowed_annotations`  
    List of annotations the `podman-fuse` workload is allowed to process.

    `allowed_devices`  
    List of devices on the host that a user can specify with the `io.kubernetes.cri-o.Devices` annotation.

4.  After applying the `MachineConfig` resource, scheduling is temporarily disabled for each node with the `worker` role as changes are applied. View the nodes' statuses.

    ``` bash
    $ oc get nodes
    ```

    Example output:

    ``` shell-session
    NAME                           STATUS                     ROLES    AGE   VERSION
    ip-10-0-136-161.ec2.internal   Ready                      worker   28m   v1.27.9
    ip-10-0-136-243.ec2.internal   Ready                      master   34m   v1.27.9
    ip-10-0-141-105.ec2.internal   Ready,SchedulingDisabled   worker   28m   v1.27.9
    ip-10-0-142-249.ec2.internal   Ready                      master   34m   v1.27.9
    ip-10-0-153-11.ec2.internal    Ready                      worker   28m   v1.27.9
    ip-10-0-153-150.ec2.internal   Ready                      master   34m   v1.27.9
    ```

5.  After all nodes with the `worker` role have a status `Ready`, `/dev/fuse` is available to any pod with the following annotations.

    ``` yaml
    io.openshift.podman-fuse: ''
    io.kubernetes.cri-o.Devices: /dev/fuse
    ```

## Results

1.  Get the name of a node with a `worker` role:

    ``` bash
    $ oc get nodes
    ```

2.  Open an `oc debug` session to a worker node.

    ``` bash
    $ oc debug node/<nodename>
    ```

3.  Verify that a new CRI-O config file named `99-podman-fuse` exists.

    ``` shell-session
    sh-4.4# stat /host/etc/crio/crio.conf.d/99-podman-fuse
    ```

**Related concepts**  

- [When to enable fuse-overlayfs](configure-con_configuring_fuse_overlayfs.md "Use the fuse-overlayfs storage driver for Podman and Buildah in the Universal Developer Image (UDI) instead of the default vfs driver, which does not provide copy-on-write support.")

**Related tasks**  

- [Enable fuse-overlayfs for all workspaces](configure-proc_enabling_fuse_for_all_workspaces.md "Enable fuse-overlayfs for all workspaces to use the overlay storage driver.")

**Related information**  

- [Using the fuse-overlayfs storage driver](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop/index#using-the-fuse-overlay-storage-driver_develop)
