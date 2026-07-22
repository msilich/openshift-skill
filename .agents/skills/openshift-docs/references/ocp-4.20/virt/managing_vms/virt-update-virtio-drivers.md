<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Update VirtIO drivers in guest operating systems. Using the latest VirtIO drivers increases performance and stability.

# Enable automatic updates for Red Hat virtio-win drivers

If the Windows Update service (WUS) is restricted to allow only drivers explicitly signed and published by Microsoft, you must manually configure automatic Red Hat `virtio-win` driver updates. Otherwise, automatic updates are disabled.

<div>

<div class="title">

Prerequisites

</div>

- The cluster must have internet connectivity. Disconnected clusters cannot reach the WUS.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Import the Red Hat Release Certificate into the Trusted Publishers store.

    Example command:

    ``` powershell
    Import-Certificate -FilePath "redhat-driver-cert.cer" -CertStoreLocation Cert:\LocalMachine\TrustedPublisher
    ```

2.  In the Group Policy Management Console (GPMC):

    1.  Set the `Allow signed updates from an intranet Microsoft update service location` policy to `Enabled`.

        If a driver is signed by a certificate in the Trusted Publishers store, it is now accepted, even if it didn’t come from Microsoft directly.

    2.  Set the `Do not include drivers with Windows Updates` policy to `Disabled`.

</div>

# Update VirtIO drivers on a Windows VM

You can update the VirtIO drivers on a Windows virtual machine (VM) by using the Windows Update service (WUS).

> [!IMPORTANT]
> If you restrict the WUS to only allow drivers explicitly signed and published by Microsoft, automatic Red Hat `virtio-win` driver updates are disabled. For information about enabling automatic Red Hat VirtIO driver updates, see "Enable automatic updates for Red Hat virtio-win drivers".

<div>

<div class="title">

Prerequisites

</div>

- The cluster must have internet connectivity. Disconnected clusters cannot reach the WUS.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the Windows Guest operating system, click the **Windows** key and select **Settings**.

2.  Navigate to **Windows Update** → **Advanced Options** → **Optional Updates**.

3.  Install all updates from **Red Hat, Inc.**.

4.  Reboot the VM.

</div>

<div>

<div class="title">

Verification

</div>

1.  On the Windows VM, navigate to the **Device Manager**.

2.  Select a device.

3.  Select the **Driver** tab.

4.  Click **Driver Details** and confirm that the `virtio` driver details displays the correct version.

</div>

# Additional resources

- [Allow signed updates from an intranet Microsoft update service location](https://learn.microsoft.com/en-us/windows/deployment/update/waas-wu-settings#allow-signed-updates-from-an-intranet-microsoft-update-service-location)

- [Do not include drivers with Windows Updates](https://learn.microsoft.com/en-us/windows/deployment/update/waas-wu-settings#do-not-include-drivers-with-windows-updates)
