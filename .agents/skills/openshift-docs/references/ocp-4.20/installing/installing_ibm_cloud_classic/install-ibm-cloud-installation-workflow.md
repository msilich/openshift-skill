<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Preparing the provisioner node on IBM Cloud® Bare Metal (Classic) infrastructure

Perform the following steps to prepare the provisioner node.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the provisioner node via `ssh`.

2.  Create a non-root user (`kni`) and provide that user with `sudo` privileges:

    ``` terminal
    # useradd kni
    ```

    ``` terminal
    # passwd kni
    ```

    ``` terminal
    # echo "kni ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/kni
    ```

    ``` terminal
    # chmod 0440 /etc/sudoers.d/kni
    ```

3.  Create an `ssh` key for the new user:

    ``` terminal
    # su - kni -c "ssh-keygen -f /home/kni/.ssh/id_rsa -N ''"
    ```

4.  Log in as the new user on the provisioner node:

    ``` terminal
    # su - kni
    ```

5.  Use Red Hat Subscription Manager to register the provisioner node:

    ``` terminal
    $ sudo subscription-manager register --username=<user> --password=<pass> --auto-attach
    ```

    ``` terminal
    $ sudo subscription-manager repos --enable=rhel-8-for-x86_64-appstream-rpms \
                                      --enable=rhel-8-for-x86_64-baseos-rpms
    ```

    > [!NOTE]
    > For more information about Red Hat Subscription Manager, see [Registering a RHEL system with command-line tools](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_rhel_system_registration/basic-reg-rhel-cli).

6.  Install the following packages:

    ``` terminal
    $ sudo dnf install -y libvirt qemu-kvm mkisofs python3-devel jq ipmitool
    ```

7.  Modify the user to add the `libvirt` group to the newly created user:

    ``` terminal
    $ sudo usermod --append --groups libvirt kni
    ```

8.  Start `firewalld`:

    ``` terminal
    $ sudo systemctl start firewalld
    ```

9.  Enable `firewalld`:

    ``` terminal
    $ sudo systemctl enable firewalld
    ```

10. Start the `http` service:

    ``` terminal
    $ sudo firewall-cmd --zone=public --add-service=http --permanent
    ```

    ``` terminal
    $ sudo firewall-cmd --reload
    ```

11. Start and enable the `libvirtd` service:

    ``` terminal
    $ sudo systemctl enable libvirtd --now
    ```

12. Set the ID of the provisioner node:

    ``` terminal
    $ PRVN_HOST_ID=<ID>
    ```

    You can view the ID with the following `ibmcloud` command:

    ``` terminal
    $ ibmcloud sl hardware list
    ```

13. Set the ID of the public subnet:

    ``` terminal
    $ PUBLICSUBNETID=<ID>
    ```

    You can view the ID with the following `ibmcloud` command:

    ``` terminal
    $ ibmcloud sl subnet list
    ```

14. Set the ID of the private subnet:

    ``` terminal
    $ PRIVSUBNETID=<ID>
    ```

    You can view the ID with the following `ibmcloud` command:

    ``` terminal
    $ ibmcloud sl subnet list
    ```

15. Set the provisioner node public IP address:

    ``` terminal
    $ PRVN_PUB_IP=$(ibmcloud sl hardware detail $PRVN_HOST_ID --output JSON | jq .primaryIpAddress -r)
    ```

16. Set the CIDR for the public network:

    ``` terminal
    $ PUBLICCIDR=$(ibmcloud sl subnet detail $PUBLICSUBNETID --output JSON | jq .cidr)
    ```

17. Set the IP address and CIDR for the public network:

    ``` terminal
    $ PUB_IP_CIDR=$PRVN_PUB_IP/$PUBLICCIDR
    ```

18. Set the gateway for the public network:

    ``` terminal
    $ PUB_GATEWAY=$(ibmcloud sl subnet detail $PUBLICSUBNETID --output JSON | jq .gateway -r)
    ```

19. Set the private IP address of the provisioner node:

    ``` terminal
    $ PRVN_PRIV_IP=$(ibmcloud sl hardware detail $PRVN_HOST_ID --output JSON | \
                     jq .primaryBackendIpAddress -r)
    ```

20. Set the CIDR for the private network:

    ``` terminal
    $ PRIVCIDR=$(ibmcloud sl subnet detail $PRIVSUBNETID --output JSON | jq .cidr)
    ```

21. Set the IP address and CIDR for the private network:

    ``` terminal
    $ PRIV_IP_CIDR=$PRVN_PRIV_IP/$PRIVCIDR
    ```

22. Set the gateway for the private network:

    ``` terminal
    $ PRIV_GATEWAY=$(ibmcloud sl subnet detail $PRIVSUBNETID --output JSON | jq .gateway -r)
    ```

23. Set up the bridges for the `baremetal` and `provisioning` networks:

    ``` terminal
    $ sudo nohup bash -c "
        nmcli --get-values UUID con show | xargs -n 1 nmcli con delete
        nmcli connection add ifname provisioning type bridge con-name provisioning
        nmcli con add type bridge-slave ifname eth1 master provisioning
        nmcli connection add ifname baremetal type bridge con-name baremetal
        nmcli con add type bridge-slave ifname eth2 master baremetal
        nmcli connection modify baremetal ipv4.addresses $PUB_IP_CIDR ipv4.method manual ipv4.gateway $PUB_GATEWAY
        nmcli connection modify provisioning ipv4.addresses 172.22.0.1/24,$PRIV_IP_CIDR ipv4.method manual
        nmcli connection modify provisioning +ipv4.routes \"10.0.0.0/8 $PRIV_GATEWAY\"
        nmcli con down baremetal
        nmcli con up baremetal
        nmcli con down provisioning
        nmcli con up provisioning
        init 6
    "
    ```

    > [!NOTE]
    > For `eth1` and `eth2`, substitute the appropriate interface name, as needed.

24. If required, SSH back into the `provisioner` node:

    ``` terminal
    # ssh kni@provisioner.<cluster-name>.<domain>
    ```

25. Verify the connection bridges have been properly created:

    ``` terminal
    $ sudo nmcli con show
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME               UUID                                  TYPE      DEVICE
    baremetal          4d5133a5-8351-4bb9-bfd4-3af264801530  bridge    baremetal
    provisioning       43942805-017f-4d7d-a2c2-7cb3324482ed  bridge    provisioning
    virbr0             d9bca40f-eee1-410b-8879-a2d4bb0465e7  bridge    virbr0
    bridge-slave-eth1  76a8ed50-c7e5-4999-b4f6-6d9014dd0812  ethernet  eth1
    bridge-slave-eth2  f31c3353-54b7-48de-893a-02d2b34c4736  ethernet  eth2
    ```

    </div>

26. Create a `pull-secret.txt` file:

    ``` terminal
    $ vim pull-secret.txt
    ```

    In a web browser, navigate to [Install on Bare Metal with user-provisioned infrastructure](https://console.redhat.com/openshift/install/metal/user-provisioned). In step 1, click **Download pull secret**. Paste the contents into the `pull-secret.txt` file and save the contents in the `kni` user’s home directory.

</div>

# Configuring the public subnet

All of the OpenShift Container Platform cluster nodes must be on the public subnet. IBM Cloud® Bare Metal (Classic) does not provide a DHCP server on the subnet. Set it up separately on the provisioner node.

You must reset the BASH variables defined when preparing the provisioner node. Rebooting the provisioner node after preparing it will delete the BASH variables previously set.

<div>

<div class="title">

Procedure

</div>

1.  Install `dnsmasq`:

    ``` terminal
    $ sudo dnf install dnsmasq
    ```

2.  Open the `dnsmasq` configuration file:

    ``` terminal
    $ sudo vi /etc/dnsmasq.conf
    ```

3.  Add the following configuration to the `dnsmasq` configuration file:

    ``` text
    interface=baremetal
    except-interface=lo
    bind-dynamic
    log-dhcp

    dhcp-range=<ip_addr>,<ip_addr>,<pub_cidr>
    dhcp-option=baremetal,121,0.0.0.0/0,<pub_gateway>,<prvn_priv_ip>,<prvn_pub_ip>

    dhcp-hostsfile=/var/lib/dnsmasq/dnsmasq.hostsfile
    ```

    - Set the DHCP range. Replace both instances of `<ip_addr>` with one unused IP address from the public subnet so that the `dhcp-range` for the `baremetal` network begins and ends with the same the IP address. Replace `<pub_cidr>` with the CIDR of the public subnet.

    - Set the DHCP option. Replace `<pub_gateway>` with the IP address of the gateway for the `baremetal` network. Replace `<prvn_priv_ip>` with the IP address of the provisioner node’s private IP address on the `provisioning` network. Replace `<prvn_pub_ip>` with the IP address of the provisioner node’s public IP address on the `baremetal` network.

      To retrieve the value for `<pub_cidr>`, execute:

      ``` terminal
      $ ibmcloud sl subnet detail <publicsubnetid> --output JSON | jq .cidr
      ```

      Replace `<publicsubnetid>` with the ID of the public subnet.

      To retrieve the value for `<pub_gateway>`, execute:

      ``` terminal
      $ ibmcloud sl subnet detail <publicsubnetid> --output JSON | jq .gateway -r
      ```

      Replace `<publicsubnetid>` with the ID of the public subnet.

      To retrieve the value for `<prvn_priv_ip>`, execute:

      ``` terminal
      $ ibmcloud  sl hardware detail <id> --output JSON | \
                  jq .primaryBackendIpAddress -r
      ```

      Replace `<id>` with the ID of the provisioner node.

      To retrieve the value for `<prvn_pub_ip>`, execute:

      ``` terminal
      $ ibmcloud sl hardware detail <id> --output JSON | jq .primaryIpAddress -r
      ```

      Replace `<id>` with the ID of the provisioner node.

4.  Obtain the list of hardware for the cluster:

    ``` terminal
    $ ibmcloud sl hardware list
    ```

5.  Obtain the MAC addresses and IP addresses for each node:

    ``` terminal
    $ ibmcloud sl hardware detail <id> --output JSON | \
      jq '.networkComponents[] | \
      "\(.primaryIpAddress) \(.macAddress)"' | grep -v null
    ```

    Replace `<id>` with the ID of the node.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    "10.196.130.144 00:e0:ed:6a:ca:b4"
    "141.125.65.215 00:e0:ed:6a:ca:b5"
    ```

    </div>

    Make a note of the MAC address and IP address of the public network. Make a separate note of the MAC address of the private network, which you will use later in the `install-config.yaml` file. Repeat this procedure for each node until you have all the public MAC and IP addresses for the public `baremetal` network, and the MAC addresses of the private `provisioning` network.

6.  Add the MAC and IP address pair of the public `baremetal` network for each node into the `dnsmasq.hostsfile` file:

    ``` terminal
    $ sudo vim /var/lib/dnsmasq/dnsmasq.hostsfile
    ```

    <div class="formalpara">

    <div class="title">

    Example input

    </div>

    ``` text
    00:e0:ed:6a:ca:b5,141.125.65.215,master-0
    <mac>,<ip>,master-1
    <mac>,<ip>,master-2
    <mac>,<ip>,worker-0
    <mac>,<ip>,worker-1
    ...
    ```

    </div>

    Replace `<mac>,<ip>` with the public MAC address and public IP address of the corresponding node name.

7.  Start `dnsmasq`:

    ``` terminal
    $ sudo systemctl start dnsmasq
    ```

8.  Enable `dnsmasq` so that it starts when booting the node:

    ``` terminal
    $ sudo systemctl enable dnsmasq
    ```

9.  Verify `dnsmasq` is running:

    ``` terminal
    $ sudo systemctl status dnsmasq
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    ● dnsmasq.service - DNS caching server.
    Loaded: loaded (/usr/lib/systemd/system/dnsmasq.service; enabled; vendor preset: disabled)
    Active: active (running) since Tue 2021-10-05 05:04:14 CDT; 49s ago
    Main PID: 3101 (dnsmasq)
    Tasks: 1 (limit: 204038)
    Memory: 732.0K
    CGroup: /system.slice/dnsmasq.service
    └─3101 /usr/sbin/dnsmasq -k
    ```

    </div>

10. Open ports `53` and `67` with UDP protocol:

    ``` terminal
    $ sudo firewall-cmd --add-port 53/udp --permanent
    ```

    ``` terminal
    $ sudo firewall-cmd --add-port 67/udp --permanent
    ```

11. Add `provisioning` to the external zone with masquerade:

    ``` terminal
    $ sudo firewall-cmd --change-zone=provisioning --zone=external --permanent
    ```

    This step ensures network address translation for IPMI calls to the management subnet.

12. Reload the `firewalld` configuration:

    ``` terminal
    $ sudo firewall-cmd --reload
    ```

</div>

# Retrieving the OpenShift Container Platform installer

Use the `stable-4.x` version of the installation program and your selected architecture to deploy the generally available stable version of OpenShift Container Platform:

``` terminal
$ export VERSION=stable-4.17
```

``` terminal
$ export RELEASE_ARCH=<architecture>
```

``` terminal
$ export RELEASE_IMAGE=$(curl -s https://mirror.openshift.com/pub/openshift-v4/$RELEASE_ARCH/clients/ocp/$VERSION/release.txt | grep 'Pull From: quay.io' | awk -F ' ' '{print $3}')
```

# Extracting the OpenShift Container Platform installer

After retrieving the installer, the next step is to extract it.

<div>

<div class="title">

Procedure

</div>

1.  Set the environment variables:

    ``` terminal
    $ export cmd=openshift-baremetal-install
    ```

    ``` terminal
    $ export pullsecret_file=~/pull-secret.txt
    ```

    ``` terminal
    $ export extract_dir=$(pwd)
    ```

2.  Get the `oc` binary:

    ``` terminal
    $ curl -s https://mirror.openshift.com/pub/openshift-v4/clients/ocp/$VERSION/openshift-client-linux.tar.gz | tar zxvf - oc
    ```

3.  Extract the installer:

    ``` terminal
    $ sudo cp oc /usr/local/bin
    ```

    ``` terminal
    $ oc adm release extract --registry-config "${pullsecret_file}" --command=$cmd --to "${extract_dir}" ${RELEASE_IMAGE}
    ```

    ``` terminal
    $ sudo cp openshift-baremetal-install /usr/local/bin
    ```

</div>

# Configuring the install-config.yaml file

The `install-config.yaml` file requires some additional details. Most of the information is teaching the installer and the resulting cluster enough about the available IBM Cloud® Bare Metal (Classic) hardware so that it is able to fully manage it. The material difference between installing on bare metal and installing on IBM Cloud® Bare Metal (Classic) is that you must explicitly set the privilege level for IPMI in the BMC section of the `install-config.yaml` file.

<div>

<div class="title">

Procedure

</div>

1.  Configure `install-config.yaml`. Change the appropriate variables to match the environment, including `pullSecret` and `sshKey`.

    ``` yaml
    apiVersion: v1
    baseDomain: <domain>
    metadata:
      name: <cluster_name>
    networking:
      machineNetwork:
      - cidr: <public-cidr>
      networkType: OVNKubernetes
    compute:
    - name: worker
      replicas: 2
    controlPlane:
      name: master
      replicas: 3
      platform:
        baremetal: {}
    platform:
      baremetal:
        apiVIP: <api_ip>
        ingressVIP: <wildcard_ip>
        provisioningNetworkInterface: <NIC1>
        provisioningNetworkCIDR: <CIDR>
        hosts:
          - name: openshift-master-0
            role: master
            bmc:
              address: ipmi://10.196.130.145?privilegelevel=OPERATOR
              username: root
              password: <password>
            bootMACAddress: 00:e0:ed:6a:ca:b4
            rootDeviceHints:
              deviceName: "/dev/sda"
          - name: openshift-worker-0
            role: worker
            bmc:
              address: ipmi://<out-of-band-ip>?privilegelevel=OPERATOR
              username: <user>
              password: <password>
            bootMACAddress: <NIC1_mac_address>
            rootDeviceHints:
              deviceName: "/dev/sda"
    pullSecret: '<pull_secret>'
    sshKey: '<ssh_pub_key>'
    ```

    - The `bmc.address` provides a `privilegelevel` configuration setting with the value set to `OPERATOR`. This is required for IBM Cloud® Bare Metal (Classic) infrastructure.

    - Add the MAC address of the private `provisioning` network NIC for the corresponding node.

      > [!NOTE]
      > You can use the `ibmcloud` command-line utility to retrieve the password.
      >
      > ``` terminal
      > $ ibmcloud sl hardware detail <id> --output JSON | \
      >   jq '"(.networkManagementIpAddress) (.remoteManagementAccounts[0].password)"'
      > ```
      >
      > Replace `<id>` with the ID of the node.

2.  Create a directory to store the cluster configuration:

    ``` terminal
    $ mkdir ~/clusterconfigs
    ```

3.  Copy the `install-config.yaml` file into the directory:

    ``` terminal
    $ cp install-config.yaml ~/clusterconfigs
    ```

4.  Ensure all bare metal nodes are powered off prior to installing the OpenShift Container Platform cluster:

    ``` terminal
    $ ipmitool -I lanplus -U <user> -P <password> -H <management_server_ip> power off
    ```

5.  Remove old bootstrap resources if any are left over from a previous deployment attempt:

    ``` bash
    for i in $(sudo virsh list | tail -n +3 | grep bootstrap | awk {'print $2'});
    do
      sudo virsh destroy $i;
      sudo virsh undefine $i;
      sudo virsh vol-delete $i --pool $i;
      sudo virsh vol-delete $i.ign --pool $i;
      sudo virsh pool-destroy $i;
      sudo virsh pool-undefine $i;
    done
    ```

</div>

# Additional `install-config` parameters

See the following tables for the required parameters, the `hosts` parameter, and the `bmc` parameter for the `install-config.yaml` file.

<table>
<caption>Required parameters</caption>
<colgroup>
<col style="width: 40%" />
<col style="width: 10%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameters</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>baseDomain</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The domain name for the cluster. For example, <code>example.com</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bootMode</code></p></td>
<td style="text-align: left;"><p><code>UEFI</code></p></td>
<td style="text-align: left;"><p>The boot mode for a node. Options are <code>legacy</code>, <code>UEFI</code>, and <code>UEFISecureBoot</code>. If <code>bootMode</code> is not set, Ironic sets it while inspecting the node.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>For hardware that implements <code>BootMode</code> read-only, such as HP or Cisco, do not leave this parameter blank. You must manually set the system to UEFI mode before installation and explicitly set this parameter to UEFI.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    bootstrapExternalStaticDNS</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The static network DNS of the bootstrap node. You must set this value when deploying a cluster with static IP addresses when there is no Dynamic Host Configuration Protocol (DHCP) server on the bare-metal network. If you do not set this value, the installation program will use the value from <code>bootstrapExternalStaticGateway</code>, which causes problems when the IP address values of the gateway and DNS are different.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    bootstrapExternalStaticIP</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The static IP address for the bootstrap VM. You must set this value when deploying a cluster with static IP addresses when there is no DHCP server on the bare-metal network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    bootstrapExternalStaticGateway</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The static IP address of the gateway for the bootstrap VM. You must set this value when deploying a cluster with static IP addresses when there is no DHCP server on the bare-metal network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>sshKey</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The <code>sshKey</code> configuration setting has the key in the <code>~/.ssh/id_rsa.pub</code> file required to access the control plane nodes and compute nodes. Typically, this key is from the <code>provisioner</code> node.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>pullSecret</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The <code>pullSecret</code> configuration setting has a copy of the pull secret downloaded from the <a href="https://console.redhat.com/openshift/install/metal/user-provisioned">Install OpenShift on Bare Metal</a> page when preparing the provisioner node.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>metadata:
    name:</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The name of the OpenShift Container Platform cluster. For example, <code>openshift</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>networking:
    machineNetwork:
    - cidr:</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The public CIDR (Classless Inter-Domain Routing) of the external network. For example, <code>10.0.0.0/24</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
  - name: worker</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The OpenShift Container Platform cluster requires you to provide a name for compute nodes even if there are zero nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>compute:
    replicas: 2</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Replicas sets the number of compute nodes in the OpenShift Container Platform cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
    name: master</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The OpenShift Container Platform cluster requires a name for control plane nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>controlPlane:
    replicas: 3</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Replicas sets the number of control plane nodes included as part of the OpenShift Container Platform cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>arbiter:
    name: arbiter</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The OpenShift Container Platform cluster requires a name for arbiter nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>arbiter:
    replicas: 1</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The <code>replicas</code> parameter sets the number of arbiter nodes for the OpenShift Container Platform cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provisioningNetworkInterface</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The name of the network interface on nodes connected to the provisioning network. For OpenShift Container Platform 4.9 and later releases, use the <code>bootMACAddress</code> configuration setting to enable Ironic to identify the IP address of the NIC instead of using the <code>provisioningNetworkInterface</code> configuration setting to identify the name of the NIC.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>defaultMachinePlatform</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The default configuration used for machine pools without a platform configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>apiVIPs</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>(Optional) The virtual IP address for Kubernetes API communication.</p>
<p>You must either provide this setting in the <code>install-config.yaml</code> file as a reserved IP from the <code>MachineNetwork</code> parameter or preconfigured in the DNS so that the default name resolves correctly. Use the virtual IP address and not the FQDN when adding a value to the <code>apiVIPs</code> configuration setting in the <code>install-config.yaml</code> file. For dual-stack networking, the primary IP address can be either an IPv4 network or an IPv6 network. If not set, the installation program uses <code>api.&lt;cluster_name&gt;.&lt;base_domain&gt;</code> to derive the IP address from the DNS.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Before OpenShift Container Platform 4.12, the cluster installation program only accepted an IPv4 address or an IPv6 address for the <code>apiVIP</code> configuration setting. From OpenShift Container Platform 4.12 or later, the <code>apiVIP</code> configuration setting is deprecated. Instead, use a list format for the <code>apiVIPs</code> configuration setting to specify an IPv4 address, an IPv6 address or both IP address formats.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>disableCertificateVerification</code></p></td>
<td style="text-align: left;"><p><code>False</code></p></td>
<td style="text-align: left;"><p><code>redfish</code> and <code>redfish-virtualmedia</code> need this parameter to manage BMC addresses. The value should be <code>True</code> when using a self-signed certificate for BMC addresses.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ingressVIPs</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>(Optional) The virtual IP address for ingress traffic.</p>
<p>You must either provide this setting in the <code>install-config.yaml</code> file as a reserved IP from the <code>MachineNetwork</code> parameter or preconfigured in the DNS so that the default name resolves correctly. Use the virtual IP address and not the FQDN when adding a value to the <code>ingressVIPs</code> configuration setting in the <code>install-config.yaml</code> file. For dual-stack networking, the primary IP address can be either an IPv4 network or an IPv6 network. If not set, the installation program uses <code>test.apps.&lt;cluster_name&gt;.&lt;base_domain&gt;</code> to derive the IP address from the DNS.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Before OpenShift Container Platform 4.12, the cluster installation program only accepted an IPv4 address or an IPv6 address for the <code>ingressVIP</code> configuration setting. In OpenShift Container Platform 4.12 and later, the <code>ingressVIP</code> configuration setting is deprecated. Instead, use a list format for the <code>ingressVIPs</code> configuration setting to specify an IPv4 addresses, an IPv6 addresses or both IP address formats.</p>
</div></td>
</tr>
</tbody>
</table>

<table>
<caption>Optional Parameters</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameters</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>platform:
  baremetal:
    additionalNTPServers:
    - &lt;ip_address_or_domain_name&gt;</code></pre></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>An optional list of additional NTP servers to add to each host. You can use an IP address or a domain name to specify each NTP server. Additional NTP servers are user-defined NTP servers that enable preinstallation clock synchronization when the cluster host clocks are out of synchronization.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provisioningDHCPRange</code></p></td>
<td style="text-align: left;"><p><code>172.22.0.10,172.22.0.100</code></p></td>
<td style="text-align: left;"><p>Defines the IP range for nodes on the provisioning network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provisioningNetworkCIDR</code></p></td>
<td style="text-align: left;"><p><code>172.22.0.0/24</code></p></td>
<td style="text-align: left;"><p>The CIDR for the network to use for provisioning. The installation program requires this option when not using the default address range on the provisioning network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>clusterProvisioningIP</code></p></td>
<td style="text-align: left;"><p>The third IP address of the <code>provisioningNetworkCIDR</code>.</p></td>
<td style="text-align: left;"><p>The IP address within the cluster where the provisioning services run. Defaults to the third IP address of the provisioning subnet. For example, <code>172.22.0.3</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bootstrapProvisioningIP</code></p></td>
<td style="text-align: left;"><p>The second IP address of the <code>provisioningNetworkCIDR</code>.</p></td>
<td style="text-align: left;"><p>The IP address on the bootstrap VM where the provisioning services run while the installation program is deploying the control plane (master) nodes. Defaults to the second IP address of the provisioning subnet. For example, <code>172.22.0.2</code> or <code>2620:52:0:1307::2</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>externalBridge</code></p></td>
<td style="text-align: left;"><p><code>baremetal</code></p></td>
<td style="text-align: left;"><p>The name of the bare-metal bridge of the hypervisor attached to the bare-metal network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provisioningBridge</code></p></td>
<td style="text-align: left;"><p><code>provisioning</code></p></td>
<td style="text-align: left;"><p>The name of the provisioning bridge on the <code>provisioner</code> host attached to the provisioning network.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>architecture</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Defines the host architecture for your cluster. Valid values are <code>amd64</code> or <code>arm64</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>defaultMachinePlatform</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The default configuration used for machine pools without a platform configuration.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bootstrapOSImage</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>A URL to override the default operating system image for the bootstrap node. The URL must contain a SHA-256 hash of the image. For example: <code>https://mirror.openshift.com/rhcos-&lt;version&gt;-qemu.qcow2.gz?sha256=&lt;uncompressed_sha256&gt;;</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>provisioningNetwork</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The <code>provisioningNetwork</code> configuration setting determines whether the cluster uses the provisioning network. If it does, the configuration setting also determines if the cluster manages the network.</p>
<p><code>Disabled</code>: Set this parameter to <code>Disabled</code> to disable the requirement for a provisioning network. When set to <code>Disabled</code>, you must only use virtual media based provisioning, or start the cluster by using the Assisted Installer. If set to <code>Disabled</code> and using power management, BMCs must be accessible from the bare-metal network. If set to <code>Disabled</code>, you must provide two IP addresses on the bare-metal network that the installation program uses for the provisioning services.</p>
<p><code>Managed</code>: Set this parameter to <code>Managed</code>, which is the default, to fully manage the provisioning network, including DHCP, TFTP, and so on.</p>
<p><code>Unmanaged</code>: Set this parameter to <code>Unmanaged</code> to enable the provisioning network but take care of manual configuration of DHCP. Virtual media provisioning is recommended but PXE is still available if required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpProxy</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Set this parameter to the appropriate HTTP proxy used within your environment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>httpsProxy</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Set this parameter to the appropriate HTTPS proxy used within your environment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>noProxy</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Set this parameter to the appropriate list of exclusions for proxy usage within your environment.</p></td>
</tr>
</tbody>
</table>

## Hosts

The `hosts` parameter is a list of separate bare metal assets used to build the cluster.

<table>
<caption>Hosts</caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 20%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Default</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The name of the <code>BareMetalHost</code> resource to associate with the details. For example, <code>openshift-master-0</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>role</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The role of the bare-metal node. Either <code>master</code> (control plane node) or <code>worker</code> (compute node).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bmc</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Connection details for the baseboard management controller. See the BMC addressing section for additional details.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bootMACAddress</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>The MAC address of the NIC that the host uses for the provisioning network. Ironic retrieves the IP address using the <code>bootMACAddress</code> configuration setting. Then, it binds to the host.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>You must provide a valid MAC address from the host if you disabled the provisioning network.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>networkConfig</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Set this optional parameter to configure the network interface of a host. See "(Optional) Configuring host network interfaces" for additional details.</p></td>
</tr>
</tbody>
</table>

# Root device hints

The `rootDeviceHints` parameter enables the installer to provision the Red Hat Enterprise Linux CoreOS (RHCOS) image to a particular device. The installer examines the devices in the order it discovers them, and compares the discovered values with the hint values. The installer uses the first discovered device that matches the hint value. The configuration can combine multiple hints, but a device must match all hints for the installer to select it.

<table>
<caption>Subfields</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Subfield</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>deviceName</code></p></td>
<td style="text-align: left;"><p>A string containing a Linux device name such as <code>/dev/vda</code> or <code>/dev/disk/by-path/</code>.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>It is recommended to use the <code>/dev/disk/by-path/&lt;device_path&gt;</code> link to the storage location.</p>
</div>
<p>The hint must match the actual value exactly.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hctl</code></p></td>
<td style="text-align: left;"><p>A string containing a SCSI bus address like <code>0:0:0:0</code>. The hint must match the actual value exactly.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>model</code></p></td>
<td style="text-align: left;"><p>A string containing a vendor-specific device identifier. The hint can be a substring of the actual value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>vendor</code></p></td>
<td style="text-align: left;"><p>A string containing the name of the vendor or manufacturer of the device. The hint can be a sub-string of the actual value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>serialNumber</code></p></td>
<td style="text-align: left;"><p>A string containing the device serial number. The hint must match the actual value exactly.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minSizeGigabytes</code></p></td>
<td style="text-align: left;"><p>An integer representing the minimum size of the device in gigabytes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>wwn</code></p></td>
<td style="text-align: left;"><p>A string containing the unique storage identifier. The hint must match the actual value exactly.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>wwnWithExtension</code></p></td>
<td style="text-align: left;"><p>A string containing the unique storage identifier with the vendor extension appended. The hint must match the actual value exactly.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>wwnVendorExtension</code></p></td>
<td style="text-align: left;"><p>A string containing the unique vendor storage identifier. The hint must match the actual value exactly.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rotational</code></p></td>
<td style="text-align: left;"><p>A boolean indicating whether the device should be a rotating disk (true) or not (false).</p></td>
</tr>
</tbody>
</table>

<div class="formalpara">

<div class="title">

Example usage

</div>

``` yaml
     - name: master-0
       role: master
       bmc:
         address: ipmi://10.10.0.3:6203
         username: admin
         password: redhat
       bootMACAddress: de:ad:be:ef:00:40
       rootDeviceHints:
         deviceName: "/dev/sda"
```

</div>

# Creating the OpenShift Container Platform manifests

1.  Create the OpenShift Container Platform manifests.

    ``` terminal
    $ ./openshift-baremetal-install --dir ~/clusterconfigs create manifests
    ```

    ``` terminal
    INFO Consuming Install Config from target directory
    WARNING Making control-plane schedulable by setting MastersSchedulable to true for Scheduler cluster settings
    WARNING Discarding the OpenShift Manifest that was provided in the target directory because its dependencies are dirty and it needs to be regenerated
    ```

# Deploying the cluster via the OpenShift Container Platform installer

Run the OpenShift Container Platform installer:

``` terminal
$ ./openshift-baremetal-install --dir ~/clusterconfigs --log-level debug create cluster
```

# Following the progress of the installation

During the deployment process, you can check the installation’s overall status by issuing the `tail` command to the `.openshift_install.log` log file in the install directory folder:

``` terminal
$ tail -f /path/to/install-dir/.openshift_install.log
```
