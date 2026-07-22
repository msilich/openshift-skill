<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Container Platform runs on RHCOS. You can follow these procedures to troubleshoot problems related to the operating system.

# Investigating kernel crashes

The `kdump` service, included in the `kexec-tools` package, provides a crash-dumping mechanism. You can use this service to save the contents of a system’s memory for later analysis.

## Enabling kdump

RHCOS ships with the `kexec-tools` package, but manual configuration is required to enable the `kdump` service.

<div class="formalpara">

<div class="title">

Procedure

</div>

Perform the following steps to enable kdump on RHCOS.

</div>

1.  To reserve memory for the crash kernel during the first kernel booting, provide kernel arguments by entering the following command:

    ``` terminal
    # rpm-ostree kargs --append='crashkernel=256M'
    ```

    > [!NOTE]
    > For the `ppc64le` platform, the recommended value for `crashkernel` is `crashkernel=2G-4G:384M,4G-16G:512M,16G-64G:1G,64G-128G:2G,128G-:4G`.

2.  Optional: To write the crash dump over the network or to some other location, rather than to the default local `/var/crash` location, edit the `/etc/kdump.conf` configuration file.

    > [!NOTE]
    > If your node uses LUKS-encrypted devices, you must use network dumps as kdump does not support saving crash dumps to LUKS-encrypted devices.

    For details on configuring the `kdump` service, see the comments in `/etc/sysconfig/kdump`, `/etc/kdump.conf`, and the `kdump.conf` manual page. Also refer to the [RHEL kdump documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_monitoring_and_updating_the_kernel/configuring-kdump-on-the-command-line_managing-monitoring-and-updating-the-kernel#configuring-the-kdump-target_configuring-kdump-on-the-command-line) for further information on configuring the dump target.

    > [!IMPORTANT]
    > If you have multipathing enabled on your primary disk, the dump target must be either an NFS or SSH server and you must exclude the multipath module from your `/etc/kdump.conf` configuration file.

3.  Enable the `kdump` systemd service.

    ``` terminal
    # systemctl enable kdump.service
    ```

4.  Reboot your system.

    ``` terminal
    # systemctl reboot
    ```

5.  Ensure that kdump has loaded a crash kernel by checking that the `kdump.service` systemd service has started and exited successfully and that the command, `cat /sys/kernel/kexec_crash_loaded`, prints the value `1`.

## Enabling kdump on day-1

The `kdump` service is intended to be enabled per node to debug kernel problems. Because there are costs to having kdump enabled, and these costs accumulate with each additional kdump-enabled node, it is recommended that the `kdump` service only be enabled on each node as needed. Potential costs of enabling the `kdump` service on each node include:

- Less available RAM due to memory being reserved for the crash kernel.

- Node unavailability while the kernel is dumping the core.

- Additional storage space being used to store the crash dumps.

If you are aware of the downsides and trade-offs of having the `kdump` service enabled, it is possible to enable kdump in a cluster-wide fashion. Although machine-specific machine configs are not yet supported, you can use a `systemd` unit in a `MachineConfig` object as a day-1 customization and have kdump enabled on all nodes in the cluster. You can create a `MachineConfig` object and inject that object into the set of manifest files used by Ignition during cluster setup.

> [!IMPORTANT]
> Architecture-specific kernel arguments must be considered when enabling kdump.
>
> For the ppc64le platform:
>
> - Use the following recommended value for the `crashkernel` parameter:
>
>   `crashkernel=2G-4G:384M,4G-16G:512M,16G-64G:1G,64G-128G:2G,128G-:4G`
>
> - In the `KDUMP_COMMANDLINE_APPEND` setting, replace `nr_cpus=1` with `maxcpus=1` because the `nr_cpus` parameter is not supported on this platform. Ensure that these adjustments are applied when configuring kdump on ppc64le systems.

> [!NOTE]
> See "Customizing nodes" in the *Installing → Installation configuration* section for more information and examples on how to use Ignition configs.

<div>

<div class="title">

Procedure

</div>

1.  Create a Butane config file, `99-worker-kdump.bu`, that configures and enables kdump. This creates a `MachineConfig` object for cluster-wide configuration:

    > [!NOTE]
    > The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.17.0`. See "Creating machine configs with Butane" for information about Butane.

    ``` yaml
    variant: openshift
    version: 4.17.0
    metadata:
      name: 99-worker-kdump
      labels:
        machineconfiguration.openshift.io/role: worker
    openshift:
      kernel_arguments:
        - crashkernel=256M
    storage:
      files:
        - path: /etc/kdump.conf
          mode: 0644
          overwrite: true
          contents:
            inline: |
              path /var/crash
              core_collector makedumpfile -l --message-level 7 -d 31

        - path: /etc/sysconfig/kdump
          mode: 0644
          overwrite: true
          contents:
            inline: |
              KDUMP_COMMANDLINE_REMOVE="hugepages hugepagesz slub_debug quiet log_buf_len swiotlb"
              KDUMP_COMMANDLINE_APPEND="irqpoll nr_cpus=1 reset_devices cgroup_disable=memory mce=off numa=off udev.children-max=2 panic=10 rootflags=nofail acpi_no_memhotplug transparent_hugepage=never nokaslr novmcoredd hest_disable"
              KEXEC_ARGS="-s"
              KDUMP_IMG="vmlinuz"

    systemd:
      units:
        - name: kdump.service
          enabled: true
    ```

    where
    - Replace `worker` with `master` in both locations when creating a `MachineConfig` object for control plane nodes.

    - Provide kernel arguments to reserve memory for the crash kernel. You can add other kernel arguments if necessary. For the `ppc64le` platform, the recommended value for `crashkernel` is `crashkernel=2G-4G:384M,4G-16G:512M,16G-64G:1G,64G-128G:2G,128G-:4G`.

    - If you want to change the contents of `/etc/kdump.conf` from the default, include this section and modify the `inline` subsection accordingly.

    - If you want to change the contents of `/etc/sysconfig/kdump` from the default, include this section and modify the `inline` subsection accordingly.

    - For the `ppc64le` platform, replace `nr_cpus=1` with `maxcpus=1`, which is not supported on this platform.

      > [!NOTE]
      > To export the dumps to NFS targets, some kernel modules must be explicitly added to the configuration file:
      >
      > <div class="formalpara">
      >
      > <div class="title">
      >
      > Example `/etc/kdump.conf` file
      >
      > </div>
      >
      > ``` text
      > nfs server.example.com:/export/cores
      > core_collector makedumpfile -l --message-level 7 -d 31
      > extra_bins /sbin/mount.nfs
      > extra_modules nfs nfsv3 nfs_layout_nfsv41_files blocklayoutdriver nfs_layout_flexfiles nfs_layout_nfsv41_files
      > ```
      >
      > </div>

2.  Use Butane to generate a machine config YAML file, `99-worker-kdump.yaml`, containing the configuration to be delivered to the nodes:

    ``` terminal
    $ butane 99-worker-kdump.bu -o 99-worker-kdump.yaml
    ```

3.  Put the YAML file into the `<installation_directory>/manifests/` directory during cluster setup. You can also create this `MachineConfig` object after cluster setup with the YAML file:

    ``` terminal
    $ oc create -f 99-worker-kdump.yaml
    ```

</div>

## Testing and analyzing kdump

After configuring kdump, you can test the configuration and analyze core dumps using the RHEL documentation.

See the [Testing the kdump configuration](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_monitoring_and_updating_the_kernel/configuring-kdump-on-the-command-line_managing-monitoring-and-updating-the-kernel#testing-the-kdump-configuration_configuring-kdump-on-the-command-line) section in the RHEL documentation for kdump.

See the [Analyzing a core dump](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_monitoring_and_updating_the_kernel/analyzing-a-core-dump_managing-monitoring-and-updating-the-kernel) section in the RHEL documentation for kdump.

> [!NOTE]
> It is recommended to perform vmcore analysis on a separate RHEL system.

## Additional resources

- [Setting up kdump in RHEL](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_monitoring_and_updating_the_kernel/configuring-kdump-on-the-command-line_managing-monitoring-and-updating-the-kernel)

- [Linux kernel documentation for kdump](https://www.kernel.org/doc/html/latest/admin-guide/kdump/kdump.html)

- kdump.conf(5) — a manual page for the `/etc/kdump.conf` configuration file containing the full documentation of available options

- kexec(8) — a manual page for the `kexec` package

- [Red Hat Knowledgebase article](https://access.redhat.com/site/solutions/6038) regarding kexec and kdump

# Debugging Ignition failures

If a machine cannot be provisioned, Ignition fails and RHCOS will boot into the emergency shell. Use the following procedure to get debugging information.

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to show which service units failed:

    ``` terminal
    $ systemctl --failed
    ```

2.  Optional: Run the following command on an individual service unit to find out more information:

    ``` terminal
    $ journalctl -u <unit>.service
    ```

</div>
