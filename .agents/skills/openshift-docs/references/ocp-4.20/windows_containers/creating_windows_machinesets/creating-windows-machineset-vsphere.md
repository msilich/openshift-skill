<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use a `MachineSet` custom resource (CR) to add a Windows compute node to your VMware vSphere cluster, where you can run Windows container workloads.

For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines. For more information about machine sets, see "Overview of machine management" in the *Additional resources* section.

# Prerequisites

- You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).

- You are using a supported Windows Server as the operating system image.

- You must prepare your vSphere environment for Windows container workloads by creating the vSphere Windows VM golden image. See "Creating the vSphere Windows VM golden image" in this section.

- You must enable communication with the internal API server for the WMCO. See "Enabling communication with the internal API server for the WMCO on vSphere" in this section.

# Creating the vSphere Windows VM golden image

You must prepare your vSphere environment for Windows container workloads by creating the vSphere Windows VM golden image.

<div>

<div class="title">

Prerequisites

</div>

- You have created a private/public key pair, which is used to configure key-based authentication in the OpenSSH server. The private key must be configured in the Windows Machine Config Operator (WMCO) namespace so that the WMCO can communicate with the Windows VM.

  If you created the key pair on a Red Hat Enterprise Linux (RHEL) system, before you can use the public key on a Windows system, make sure the public key is saved using ASCII encoding. For example, the following PowerShell command copies a public key, encoding it for the ASCII character set:

  ``` terminal
  C:\> echo "ssh-rsa <ssh_pub_key>" | Out-File <ssh_key_path> -Encoding ascii
  ```

  where:

  `<ssh_pub_key>`
  Specifies the SSH public key used to access the cluster.

  `<ssh_key_path>`
  Specifies the path to the SSH public key.

  See the "Configuring a secret for the Windows Machine Config Operator" section for more details.

</div>

> [!NOTE]
> You must use [Microsoft PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell) commands in several cases when creating your Windows VM. PowerShell commands in this guide are distinguished by the `PS C:\>` prefix.

<div>

<div class="title">

Procedure

</div>

1.  Select a compatible Windows Server version. Currently, the Windows Machine Config Operator (WMCO) stable version supports Windows Server 2022 Long-Term Servicing Channel with the OS-level container networking patch [KB5012637](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d).

2.  Create a new VM in the vSphere client using the VM golden image with a compatible Windows Server version. For more information about compatible versions, see the "Windows Machine Config Operator prerequisites" section of the "Red Hat OpenShift support for Windows Containers release notes."

    > [!IMPORTANT]
    > The virtual hardware version for your VM must meet the infrastructure requirements for OpenShift Container Platform. For more information, see the "VMware vSphere infrastructure requirements" section in the OpenShift Container Platform documentation. Also, you can refer to VMware’s documentation on [virtual machine hardware versions](https://kb.vmware.com/s/article/1003746).

3.  Install and configure VMware Tools version 11.0.6 or greater on the Windows VM. See the [VMware Tools documentation](https://docs.vmware.com/en/VMware-Tools/index.html) for more information.

4.  After installing VMware Tools on the Windows VM, verify the following:

    1.  The `C:\ProgramData\VMware\VMware Tools\tools.conf` file exists with the following entry:

        ``` ini
        exclude-nics=
        ```

        If the `tools.conf` file does not exist, create it with the `exclude-nics` option uncommented and set as an empty value.

        This entry ensures the cloned vNIC generated on the Windows VM by the hybrid-overlay is not ignored.

    2.  The Windows VM has a valid IP address in vCenter:

        ``` terminal
        C:\> ipconfig
        ```

    3.  The VMTools Windows service is running:

        ``` posh
        PS C:\> Get-Service -Name VMTools | Select Status, StartType
        ```

5.  Install and configure the OpenSSH Server on the Windows VM. See Microsoft’s documentation on [installing OpenSSH](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse) for more details.

6.  Set up SSH access for an administrative user. See Microsoft’s documentation on the [Administrative user](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement#administrative-user) to do this.

    > [!IMPORTANT]
    > The public key used in the instructions must correspond to the private key you create later in the WMCO namespace that holds your secret. See the "Configuring a secret for the Windows Machine Config Operator" section for more details.

7.  You must create a new firewall rule in the Windows VM that allows incoming connections for container logs. Run the following PowerShell command to create the firewall rule on TCP port 10250:

    ``` posh
    PS C:\> New-NetFirewallRule -DisplayName "ContainerLogsPort" -LocalPort 10250 -Enabled True -Direction Inbound -Protocol TCP -Action Allow -EdgeTraversalPolicy Allow
    ```

8.  Clone the Windows VM so it is a reusable image. Follow the VMware documentation on how to [clone an existing virtual machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-1E185A80-0B97-4B46-A32B-3EF8F309BEED.html) for more details.

9.  In the cloned Windows VM, run the [Windows Sysprep tool](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation):

    ``` terminal
    C:\> C:\Windows\System32\Sysprep\sysprep.exe /generalize /oobe /shutdown /unattend:<path_to_unattend.xml>
    ```

    Replace `<path_to_unattend.xml>` with the path to your `unattend.xml` file.

    > [!NOTE]
    > There is a limit on how many times you can run the `sysprep` command on a Windows image. Consult Microsoft’s [documentation](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation#limits-on-how-many-times-you-can-run-sysprep) for more information.

    An example `unattend.xml` is provided, which maintains all the changes needed for the WMCO. You must modify this example; it cannot be used directly.

    <div class="formalpara">

    <div class="title">

    Example `unattend.xml`

    </div>

    ``` xml
    <?xml version="1.0" encoding="UTF-8"?>
    <unattend xmlns="urn:schemas-microsoft-com:unattend">
       <settings pass="specialize">
          <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-International-Core" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
             <InputLocale>0409:00000409</InputLocale>
             <SystemLocale>en-US</SystemLocale>
             <UILanguage>en-US</UILanguage>
             <UILanguageFallback>en-US</UILanguageFallback>
             <UserLocale>en-US</UserLocale>
          </component>
          <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-Security-SPP-UX" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
             <SkipAutoActivation>true</SkipAutoActivation>
          </component>
          <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-SQMApi" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
             <CEIPEnabled>0</CEIPEnabled>
          </component>
          <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
             <ComputerName>winhost</ComputerName>
          </component>
       </settings>
       <settings pass="oobeSystem">
          <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
             <AutoLogon>
                <Enabled>false</Enabled>
             </AutoLogon>
             <OOBE>
                <HideEULAPage>true</HideEULAPage>
                <HideLocalAccountScreen>true</HideLocalAccountScreen>
                <HideOEMRegistrationScreen>true</HideOEMRegistrationScreen>
                <HideOnlineAccountScreens>true</HideOnlineAccountScreens>
                <HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>
                <NetworkLocation>Work</NetworkLocation>
                <ProtectYourPC>1</ProtectYourPC>
                <SkipMachineOOBE>true</SkipMachineOOBE>
                <SkipUserOOBE>true</SkipUserOOBE>
             </OOBE>
             <RegisteredOrganization>Organization</RegisteredOrganization>
             <RegisteredOwner>Owner</RegisteredOwner>
             <DisableAutoDaylightTimeSet>false</DisableAutoDaylightTimeSet>
             <TimeZone>Eastern Standard Time</TimeZone>
             <UserAccounts>
                <AdministratorPassword>
                   <Value>MyPassword</Value>
                   <PlainText>true</PlainText>
                </AdministratorPassword>
             </UserAccounts>
          </component>
       </settings>
    </unattend>
    ```

    </div>

    where:

    `<ComputerName>`
    Replace the `winhost` placeholder with a computer name, which must follow the Kubernetes' names specification. These specifications also apply to Guest OS customization performed on the resulting template while creating new VMs. For more information, see "Object Names and IDs specification (Kubernetes documentation)" in the *Additional resources* section.

    `<AutoLogon>.<Enabled>`
    When `false`, automatic logon is disabled to avoid the security issue of leaving an open terminal with Administrator privileges at boot. This is the default value and must not be changed.

    `<UserAccounts>.<AdministratorPassword>.<Value>`
    Replace the `MyPassword` placeholder with the password for the Administrator account. This prevents the built-in Administrator account from having a blank password by default. Follow Microsoft’s best practices for choosing a password. For more information on Microsoft’s best practices, see "Password must meet complexity requirements (Microsoft documentation)" in the *Additional resources* section.

    After the Sysprep tool has completed, the Windows VM will power off. You must not use or power on this VM anymore.

10. Convert the Windows VM to a template in vCenter. For more information, see "vSphere Virtual Machine Administration (vSphere documentation)" in the *Additional resources* section.

</div>

# Enabling communication with the internal API server for the WMCO on vSphere

You must enable communication with the internal API server so that your Windows virtual machine (VM) can download the Ignition config files, and the kubelet on the configured VM can only communicate with the internal API server.

The Windows Machine Config Operator (WMCO) can download the Ignition config files from the internal API server endpoint only after communication with the server is enabled.

<div>

<div class="title">

Prerequisites

</div>

- You have installed a cluster on vSphere.

</div>

<div>

<div class="title">

Procedure

</div>

- Add a new DNS entry for `api-int.<cluster_name>.<base_domain>` that points to the external API server URL `api.<cluster_name>.<base_domain>`. This can be a CNAME or an additional A record.

  > [!NOTE]
  > The external API endpoint was already created as part of the initial cluster installation on vSphere.

</div>

# Sample YAML for a Windows MachineSet object on vSphere

You can define a Windows `MachineSet` object running on VMware vSphere by creating a YAML file similar to the following example, which the Windows Machine Config Operator (WMCO) can react upon.

``` yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <windows_machine_set_name>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <windows_machine_set_name>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <windows_machine_set_name>
        machine.openshift.io/os-id: Windows
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: ""
      providerSpec:
        value:
          apiVersion: vsphereprovider.openshift.io/v1beta1
          credentialsSecret:
            name: vsphere-cloud-credentials
          diskGiB: 128
          kind: VSphereMachineProviderSpec
          memoryMiB: 16384
          network:
            devices:
            - networkName: "<vm_network_name>"
          numCPUs: 4
          numCoresPerSocket: 1
          snapshot: ""
          template: <windows_vm_template_name>
          userDataSecret:
            name: windows-user-data
          workspace:
             datacenter: <vcenter_data_center_name>
             datastore: <vcenter_datastore_name>
             folder: <vcenter_vm_folder_path>
             resourcePool: <vsphere_resource_pool>
             server: <vcenter_server_ip>
```

where:

`metadata.labels`
For the `machine.openshift.io/cluster-api-cluster` label, replace `<infrastructure_id>` with the infrastructure ID. You can obtain the infrastructure ID by running the following command: Specify the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You can obtain the infrastructure ID by running the following command:

``` terminal
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```

`metadata.name`
Replace the infrastructure ID, worker label, and zone.

`spec.selector.matchLabels`
Replace the parameters for the following labels:

- `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.

- `machine.openshift.io/cluster-api-machineset`. Specify the Windows compute machine set name. The compute machine set name cannot be more than 9 characters long, due to the way machine names are generated in vSphere.

`spec.template.metadata.labels`
Replace the parameters for the following labels:

- `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.

- `machine.openshift.io/cluster-api-machineset`. Specify the Windows compute machine set name. The compute machine set name cannot be more than 9 characters long, due to the way machine names are generated in vSphere.

- `machine.openshift.io/os-id: Windows`. When set to `Windows`, configures the compute machine set as a Windows machine.

`spec.template.spec.metadata.labels`
When set to `node-role.kubernetes.io/worker`, configures the node as a compute machine.

`spec.template.spec.providerSpec`
Specify the following parameters:

- `value.diskGiB`. Specifies the size of the vSphere Virtual Machine Disk (VMDK).

  > [!NOTE]
  > This parameter does not set the size of the Windows partition. You can resize the Windows partition by using the `unattend.xml` file or by creating the vSphere Windows virtual machine (VM) golden image with the required disk size.

- `value.network.devices.networkName`. Specifies the vSphere VM network to deploy the compute machine set to. This VM network must be where other Linux compute machines reside in the cluster.

- `value.template`. Specifies the full path of the Windows vSphere VM template to use, such as `golden-images/windows-server-template`. The name must be unique.

  > [!IMPORTANT]
  > Do not specify the original VM template. The VM template must remain off and must be cloned for new Windows machines. Starting the VM template configures the VM template as a VM on the platform, which prevents it from being used as a template that compute machine sets can apply configurations to.

- `value.userDataSecret.name`. The `windows-user-data` is created by the WMCO when the first Windows machine is configured. After that, the `windows-user-data` is available for all subsequent compute machine sets to consume.

- `value.workspace.datacenter`. Specifies the vCenter data center to deploy the compute machine set on.

- `value.workspace.datastore`. Specifies the vCenter datastore to deploy the compute machine set on.

- `value.workspace.folder`. Specifies the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`.

- `value.workspace.resourcePool`. Specifies the vSphere resource pool for your Windows VMs. This parameter is optional.

- `value.workspace.server`. Specifies the vCenter server IP or fully qualified domain name. This parameter is optional.

# Creating a compute machine set

To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

<div>

<div class="title">

Prerequisites

</div>

- Deploy an OpenShift Container Platform cluster.

- Install the OpenShift CLI (`oc`).

- Log in to `oc` as a user with `cluster-admin` permission.

- In disconnected environments, the image specified in the `MachineSet` custom resource (CR) must have the [OpenSSH server v0.0.1.0 installed](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell#install-openssh-for-windows).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`.

    Ensure that you set the `<clusterID>` and `<role>` parameter values.

2.  Optional: If you are not sure which value to set for a specific field, you can check an existing compute machine set from your cluster.

    1.  To list the compute machine sets in your cluster, run the following command:

        ``` terminal
        $ oc get machinesets -n openshift-machine-api
        ```

        The following is example output:

        ``` terminal
        NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
        agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
        agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
        agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
        agl030519-vplxk-worker-us-east-1d   0         0                             55m
        agl030519-vplxk-worker-us-east-1e   0         0                             55m
        agl030519-vplxk-worker-us-east-1f   0         0                             55m
        ```

    2.  To view values of a specific compute machine set custom resource (CR), run the following command:

        ``` terminal
        $ oc get machineset <machineset_name> \
          -n openshift-machine-api -o yaml
        ```

        The following is example output:

        ``` yaml
        apiVersion: machine.openshift.io/v1beta1
        kind: MachineSet
        metadata:
          labels:
            machine.openshift.io/cluster-api-cluster: <infrastructure_id>
          name: <infrastructure_id>-<role>
          namespace: openshift-machine-api
        spec:
          replicas: 1
          selector:
            matchLabels:
              machine.openshift.io/cluster-api-cluster: <infrastructure_id>
              machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
          template:
            metadata:
              labels:
                machine.openshift.io/cluster-api-cluster: <infrastructure_id>
                machine.openshift.io/cluster-api-machine-role: <role>
                machine.openshift.io/cluster-api-machine-type: <role>
                machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
            spec:
              providerSpec:
                ...
        ```

        where:

        `metadata.labels.machine.openshift.io/cluster-api-cluster`
        Specifies the cluster infrastructure ID.

        `metadata.labels.name`
        Specifies a default node label.

        > [!NOTE]
        > For clusters that have user-provisioned infrastructure, a compute machine set can only create `worker` and `infra` type machines.

        `spec.template.metadata.spec.providerSpec`
        Specifies the values of the compute machine set CR. The values are platform-specific. For more information about `<providerSpec>` parameters in the CR, see the sample compute machine set CR configuration for your provider.

3.  Create a `MachineSet` CR by running the following command:

    ``` terminal
    $ oc create -f <file_name>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- View the list of compute machine sets by running the following command:

  ``` terminal
  $ oc get machineset -n openshift-machine-api
  ```

  The following is example output:

  ``` terminal
  NAME                                       DESIRED   CURRENT   READY   AVAILABLE   AGE
  agl030519-vplxk-windows-worker-us-east-1a  1         1         1       1           11m
  agl030519-vplxk-worker-us-east-1a          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1b          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1c          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1d          0         0                             55m
  agl030519-vplxk-worker-us-east-1e          0         0                             55m
  agl030519-vplxk-worker-us-east-1f          0         0                             55m
  ```

  When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again.

</div>

# Additional resources

- [Configuring a secret for the Windows Machine Config Operator](../enabling-windows-container-workloads.md#configuring-secret-for-wmco_enabling-windows-container-workloads)

- [VMware vSphere infrastructure requirements](../../installing/installing_vsphere/ipi/ipi-vsphere-installation-reqs.md#installation-vsphere-infrastructure_ipi-vsphere-installation-reqs)

- [Overview of machine management](../../machine_management/index.md#overview-of-machine-management)

- [Object Names and IDs specification (Kubernetes documentation)](https://kubernetes.io/docs/concepts/overview/working-with-objects/names)

- [Password must meet complexity requirements (Microsoft documentation)](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements)

- [vSphere Virtual Machine Administration (vSphere documentation)](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration.html)
