<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Network-Bound Disk Encryption (NBDE) must be enabled when a cluster node is installed. However, you can change the disk encryption policy at any time after it was initialized at installation.

# Installation scenarios

Consider the following recommendations when planning Tang server installations:

- Small environments can use a single set of key material, even when using multiple Tang servers:

  - Key rotations are easier.

  - Tang servers can scale easily to permit high availability.

- Large environments can benefit from multiple sets of key material:

  - Physically diverse installations do not require the copying and synchronizing of key material between geographic regions.

  - Key rotations are more complex in large environments.

  - Node installation and rekeying require network connectivity to all Tang servers.

  - A small increase in network traffic can occur due to a booting node querying all Tang servers during decryption. Note that while only one Clevis client query must succeed, Clevis queries all Tang servers.

- Further complexity:

  - Additional manual reconfiguration can permit the Shamir’s secret sharing (sss) of `any N of M servers online` in order to decrypt the disk partition. Decrypting disks in this scenario requires multiple sets of key material, and manual management of Tang servers and nodes with Clevis clients after the initial installation.

- High level recommendations:

  - For a single RAN deployment, a limited set of Tang servers can run in the corresponding domain controller (DC).

  - For multiple RAN deployments, you must decide whether to run Tang servers in each corresponding DC or whether a global Tang environment better suits the other needs and requirements of the system.

# Installing a Tang server

To deploy one or more Tang servers, you can choose from the following options depending on your scenario:

1.  [Deploying a Tang server using the NBDE Tang Server Operator](../nbde_tang_server_operator/nbde-tang-server-operator-configuring-managing.md#deploying-nbde-tang-server_configuring-and-managing-nbde-tang-server-operator)

2.  [Deploying a Tang server with SELinux in enforcing mode on RHEL systems](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening#deploying-a-tang-server-with-selinux-in-enforcing-mode_configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption)

3.  [Configuring a Tang server in the RHEL web console](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening#configuring-automated-unlocking-using-a-tang-key-in-the-web-console_configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption)

4.  [Deploying Tang as a container](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening#proc_deploying-tang-as-a-container_configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption)

5.  [Using the nbde_server System Role for setting up multiple Tang servers](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening#using-the-nbde_server-system-role-for-setting-up-multiple-tang-servers_configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption)

## Compute requirements

The computational requirements for the Tang server are very low. Any typical server grade configuration that you would use to deploy a server into production can provision sufficient compute capacity.

High availability considerations are solely for availability and not additional compute power to satisfy client demands.

## Automatic start at boot

Due to the sensitive nature of the key material the Tang server uses, you should keep in mind that the overhead of manual intervention during the Tang server’s boot sequence can be beneficial.

By default, if a Tang server starts and does not have key material present in the expected local volume, it will create fresh material and serve it. You can avoid this default behavior by either starting with pre-existing key material or aborting the startup and waiting for manual intervention.

## HTTP versus HTTPS

Traffic to the Tang server can be encrypted (HTTPS) or plain text (HTTP). There are no significant security advantages of encrypting this traffic, and leaving it decrypted removes any complexity or failure conditions related to Transport Layer Security (TLS) certificate checking in the node running a Clevis client.

While it is possible to perform passive monitoring of unencrypted traffic between the node’s Clevis client and the Tang server, the ability to use this traffic to determine the key material is at best a future theoretical concern. Any such traffic analysis would require large quantities of captured data. Key rotation would immediately invalidate it. Finally, any threat actor able to perform passive monitoring has already obtained the necessary network access to perform manual connections to the Tang server and can perform the simpler manual decryption of captured Clevis headers.

However, because other network policies in place at the installation site might require traffic encryption regardless of application, consider leaving this decision to the cluster administrator.

<div>

<div class="title">

Additional resources

</div>

- [Configuring automated unlocking of encrypted volumes using policy-based decryption](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening)

- [Official Tang server container](https://catalog.redhat.com/software/containers/detail/5fbc405674aa0cc23b445f8f?container-tabs=overview&gti-tabs=registry-tokens)

- [Encrypting and mirroring disks during installation](../../installing/install_config/installing-customizing.md#installation-special-config-storage_installing-customizing)

</div>
