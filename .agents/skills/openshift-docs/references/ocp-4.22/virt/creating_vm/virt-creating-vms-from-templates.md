<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can create, customize, and manage the virtual machine (VM) templates that you use to create VMs. To create a VM from a template, use the web console creation wizard.

# About VM templates

VM templates define a reusable VM configuration. You can create a VM from a template to deploy a standardized VM quickly.

Speed up creation with boot sources
You can speed up VM creation by using templates that have an available boot source. A template with a boot source displays the **Available boot source** label if it does not have a custom label.

A template without a boot source displays the **Boot source required** label.

Customize before starting the VM
You can customize the disk source and VM parameters before you start the VM.

> [!NOTE]
> If you copy a VM template with all its labels and annotations, your version of the template is marked as deprecated when a new version of the Scheduling, Scale, and Performance (SSP) Operator is deployed. You can remove this designation. See "Removing a deprecated designation from a customized VM template by using the web console".

Single-node OpenShift
Due to differences in storage behavior, some templates are incompatible with single-node OpenShift. To ensure compatibility, do not set the `evictionStrategy` field for templates or VMs that use data volumes or storage profiles.

# Creating a custom VM template in the web console

You can create a virtual machine template by editing a YAML file example in the OpenShift Container Platform web console.

<div>

<div class="title">

Procedure

</div>

1.  In the web console, click **Virtualization** → **Templates** in the side menu.

2.  Optional: Use the **Project** drop-down menu to change the project associated with the new template. All templates are saved to the `openshift` project by default.

3.  Click **Create Template**.

4.  Specify the template parameters by editing the YAML file.

5.  Click **Create**.

    The template is displayed on the **Templates** page.

6.  Optional: Click **Download** to download and save the YAML file.

</div>

# Enabling dedicated resources for a virtual machine template

You can enable dedicated resources for a virtual machine (VM) template in the OpenShift Container Platform web console. VMs that are created from this template will be scheduled with dedicated resources.

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, click **Virtualization** → **Templates** in the side menu.

2.  Select the template that you want to edit to open the **Template details** page.

3.  On the **Scheduling** tab, click the edit icon beside **Dedicated Resources**.

4.  Select **Schedule this workload with dedicated resources (guaranteed policy)**.

5.  Click **Save**.

</div>

# Removing a deprecated designation from a customized VM template by using the web console

You can customize an existing virtual machine (VM) template before you start the VM, by modifying the VM or template parameters, such as data sources, cloud-init, or SSH keys.

> [!NOTE]
> If you customize a template by copying it and including all of its labels and annotations, the customized template is marked as deprecated when a new version of the Scheduling, Scale, and Performance (SSP) Operator is deployed. You can remove the deprecated designation from the customized template.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Virtualization** → **Templates** in the web console.

2.  From the list of VM templates, click the template marked as deprecated.

3.  Click **Edit** next to the pencil icon beside **Labels**.

4.  Remove the following two labels:

    - `template.kubevirt.io/type: "base"`

    - `template.kubevirt.io/version: "version"`

5.  Click **Save**.

6.  Click the pencil icon beside the number of existing **Annotations**.

7.  Remove the following annotation:

    - `template.kubevirt.io/deprecated`

8.  Click **Save**.

</div>

# Additional resources

- [Creating a VM from a template by using the web console](virt-creating-vms-web.md#virt-creating-vm-from-template-web_virt-creating-vms-web)

- [Managing automatic boot source updates](../storage/virt-automatic-bootsource-updates.md#virt-automatic-bootsource-updates)
