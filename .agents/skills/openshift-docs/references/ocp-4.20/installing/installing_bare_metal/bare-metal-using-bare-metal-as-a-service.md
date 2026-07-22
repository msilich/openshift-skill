<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can provision and manage bare-metal hosts by using the Metal<sup>3</sup> API and the Bare Metal Operator (BMO). These hosts, external to the OpenShift Container Platform cluster, can run workloads that might not be suitable for containerization or virtualization, such as legacy applications or applications that require direct hardware access.

Red Hat Bare Metal as a Service for OpenShift has the following capabilities:

- Provisioning of bare-metal hosts, including initial configuration.

- Lifecycle management such as power management, firmware updates, and decommissioning by using the BMO.

As standalone systems, these hosts operate independently of the OpenShift Container Platform cluster and support diverse workloads by integrating bare metal resources with containerized and virtualized applications. Red Hat Bare Metal as a Service for OpenShift can run other operating systems, but only Red Hat Enterprise Linux (RHEL) and CentOS Stream 9 were tested.

> [!IMPORTANT]
> Red Hat Bare Metal as a Service for OpenShift is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Prerequisites for using Red Hat Bare Metal as a Service for OpenShift

Red Hat Bare Metal as a Service for OpenShift lets you apply cloud-native management practices to bare-metal infrastructure, enabling automated provisioning and lifecycle management for workloads that require physical hardware. To use the Red Hat Bare Metal as a Service for OpenShift Technology Preview, complete the following prerequisites:

BareMetalHost Configuration
All bare-metal hosts must use a Baseboard Management Controller (BMC) configured with the Redfish protocol and virtual media (`redfish-virtualmedia`) driver. Each bare-metal host requires a boot interface with a MAC address configured to receive an IP address lease.

Network Requirements
A DHCP server, separate from the OpenShift Container Platform and Metal<sup>3</sup> infrastructure, must be operational on the same Layer 2 network as the bare-metal hosts. The DHCP server must be configured to match the MAC addresses of the boot interfaces on the bare-metal hosts, enabling IP address assignment for communication with Metal<sup>3</sup> components.

Cluster Privileges
You must have `cluster-admin` privileges on the OpenShift Container Platform cluster to perform configuration tasks.

Web server with images
Red Hat Bare Metal as a Service for OpenShift does not provide images for deployment on hardware. You must configure a web server with the images and checksums you want to use. The `image` field of the `BareMetalHost` spec references these images during deployment. Ensure that the bare-metal hosts can reach the web server URL. The following is an example of an image and checksum you might include:

- `http://example.com/rhel9.qcow2`

- `http://example.com/rhel9.qcow2.sha512sum`

- `http://example.com/stream9.qcow2`

- `http://example.com/stream9.qcow2.sha512sum`

These prerequisites ensure that you can provision and manage bare-metal hosts effectively.

# Using the Bare Metal Operator to manage resources across all namespaces

For the Bare Metal Operator (BMO) to manage `BareMetalHost` resources across all namespaces in your OpenShift Container Platform cluster, you must configure the Operator to watch all namespaces. This configuration is important to avoid mixing non-OpenShift Container Platform workloads with other components in the same namespace.

<div>

<div class="title">

Prerequisites

</div>

- If you are using user-provisioned installation and the Provisioning CR does not exist, you must create it manually. For instructions, see [Configuring a provisioning resource to scale user-provisioned clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html-single/installing_on_bare_metal/index#scaling-a-user-provisioned-cluster-with-the-bare-metal-operator). For installer-provisioned installations, the installation program creates the Provisioning custom resource (CR) automatically.

</div>

<div>

<div class="title">

Procedure

</div>

- Patch the provisioning configuration to enable watching all namespaces by running the following command:

  ``` terminal
  $ oc patch provisioning/provisioning-configuration \
    --type merge -p '{"spec": {"watchAllNamespaces": true}}'
  ```

  The BMO applies this change automatically.

</div>

# Setting up a dedicated namespace

To prevent accidental interference between Red Hat Bare Metal as a Service for OpenShift workloads and the OpenShift Container Platform infrastructure, set up a dedicated namespace. Repeat this procedure for every project where you intend to use Red Hat Bare Metal as a Service for OpenShift.

<div>

<div class="title">

Prerequisites

</div>

- You have [configured an identify provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html-single/authentication_and_authorization/index#configuring-identity-providers).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure a `bmadmin` user in the identity provider and create a secret in OpenShift:

    1.  Create the `bmadmin` user in the identity provider. For example, if using the `htpasswd` identity provider, run the following command:

        ``` terminal
        $ htpasswd -c -B -b ./users_htpasswd <username> <password>
        ```

        \<username\>
        The user name for the identity provider. Replace `<username>` with your preferred user name. This example uses `bmadmin`.

        \<password\>
        The password for the user. Replace `<password>` with a secure password.

    2.  Create a secret in the `openshift-config` namespace to store the identity provider configuration by running the following command:

        ``` terminal
        $ oc create secret generic <identity_provider_arguments> -n openshift-config
        ```

        For example, when using the `htpasswd` identity provider, run the following command:

        ``` terminal
        $ oc create secret generic htpass-secret --from-file=htpasswd=users_htpasswd -n openshift-config
        ```

        \<identity_provider_arguments\>
        The arguments specific to the identity provider secret. Replace `<identity_provider_arguments>` with the appropriate arguments for your identity provider.

2.  Configure OAuth to use the identity provider:

    1.  Edit the OAuth resource by running the following command:

        ``` terminal
        $ oc edit oauth cluster
        ```

        The editor opens and displays the Oauth resource.

    2.  Add the identity provider configuration to the `spec.identityProviders` list:

        <table>
        <caption>Identity provider configuration examples</caption>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr>
        <th style="text-align: left;">Type</th>
        <th style="text-align: left;">Example</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td style="text-align: left;"><p>htpasswd</p></td>
        <td style="text-align: left;"><div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co"># ...</span></span>
        <span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="fu">name</span><span class="kw">:</span><span class="at"> my_bmaas_provider</span></span>
        <span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">mappingMethod</span><span class="kw">:</span><span class="at"> claim</span></span>
        <span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">type</span><span class="kw">:</span><span class="at"> htpasswd</span></span>
        <span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">htpasswd</span><span class="kw">:</span></span>
        <span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">fileData</span><span class="kw">:</span></span>
        <span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">name</span><span class="kw">:</span><span class="at"> &lt;secret&gt;</span></span>
        <span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="co"># ...</span></span></code></pre></div></td>
        </tr>
        <tr>
        <td style="text-align: left;"><p>LDAP</p></td>
        <td style="text-align: left;"><div class="sourceCode" id="cb2"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co"># ...</span></span>
        <span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="fu">name</span><span class="kw">:</span><span class="at"> my_bmaas_provider</span></span>
        <span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">mappingMethod</span><span class="kw">:</span><span class="at"> claim</span></span>
        <span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">type</span><span class="kw">:</span><span class="at"> ldap</span></span>
        <span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">ldap</span><span class="kw">:</span></span>
        <span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">attributes</span><span class="kw">:</span></span>
        <span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">id</span><span class="kw">:</span></span>
        <span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> dn</span></span>
        <span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">email</span><span class="kw">:</span></span>
        <span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> mail</span></span>
        <span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">name</span><span class="kw">:</span></span>
        <span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> cn</span></span>
        <span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">preferredUsername</span><span class="kw">:</span></span>
        <span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> uid</span></span>
        <span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a><span class="co"># ...</span></span></code></pre></div></td>
        </tr>
        <tr>
        <td style="text-align: left;"><p>GitHub</p></td>
        <td style="text-align: left;"><div class="sourceCode" id="cb3"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="co"># ...</span></span>
        <span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="fu">name</span><span class="kw">:</span><span class="at"> my_bmaas_provider</span></span>
        <span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">mappingMethod</span><span class="kw">:</span><span class="at"> claim</span></span>
        <span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">type</span><span class="kw">:</span><span class="at"> GitHub</span></span>
        <span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">github</span><span class="kw">:</span></span>
        <span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">ca</span><span class="kw">:</span></span>
        <span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a><span class="at">        </span><span class="fu">name</span><span class="kw">:</span><span class="at"> ca-config-map</span></span>
        <span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">clientID</span><span class="kw">:</span><span class="at"> </span><span class="kw">{</span><span class="at">...</span><span class="kw">}</span></span>
        <span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">clientSecret</span><span class="kw">:</span></span>
        <span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a><span class="at">        </span><span class="fu">name</span><span class="kw">:</span><span class="at"> github-secret</span></span>
        <span id="cb3-11"><a href="#cb3-11" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">hostname</span><span class="kw">:</span><span class="at"> ...</span></span>
        <span id="cb3-12"><a href="#cb3-12" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">organizations</span><span class="kw">:</span></span>
        <span id="cb3-13"><a href="#cb3-13" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> myorganization1</span></span>
        <span id="cb3-14"><a href="#cb3-14" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> myorganization2</span></span>
        <span id="cb3-15"><a href="#cb3-15" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">teams</span><span class="kw">:</span></span>
        <span id="cb3-16"><a href="#cb3-16" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> myorganization1/team-a</span></span>
        <span id="cb3-17"><a href="#cb3-17" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> myorganization2/team-b</span></span>
        <span id="cb3-18"><a href="#cb3-18" aria-hidden="true" tabindex="-1"></a><span class="co"># ...</span></span></code></pre></div></td>
        </tr>
        </tbody>
        </table>

        For more information about identify providers, see [Authentication and authorization](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html-single/authentication_and_authorization/index).

    3.  Save and exit the editor.

3.  Create a `bmadmin` user by running the following command:

    ``` terminal
    $ oc create user <username>
    ```

    \<username\>
    The user name. Replace `<username>` with your username. The following examples use `bmadmin` as the username.

4.  Create a dedicated `bmaas` namespace for Red Hat Bare Metal as a Service for OpenShift hosts by running the following command:

    ``` terminal
    $ oc new-project <namespace>
    ```

    `<namespace>`
    Replace \<namespace\> with the namespace name that you want to use. This example uses `bmaas`.

5.  Assign the `edit` role to the `bmadmin` user in the `bmaas` namespace by running the following command:

    ``` terminal
    $ oc adm policy add-role-to-user edit <username> -n bmaas
    ```

6.  Clone the `baremetal-operator` repository to obtain the role-based access control (RBAC) role definitions by running the following command:

    ``` terminal
    $ git clone -b release-4.17 https://github.com/openshift/baremetal-operator.git
    ```

7.  For each role you want to add, apply the appropriate RBAC role YAML file from the repository by running the following command:

    ``` terminal
    $ oc apply -f baremetal-operator/config/base/rbac/<role_filename>.yaml
    ```

8.  Assign the custom RBAC roles to the `bmadmin` user in the `bmaas` namespace by running the following command:

    ``` terminal
    $ oc adm policy add-role-to-user <role_name> bmadmin -n bmaas
    ```

9.  Login as the `bmadmin` user by running the following command:

    ``` terminal
    $ oc login <api_server_url>:6443
    ```

    `<api_server_url>`
    The URL to the Kubernetes API.

</div>

# Creating a BMC secret

To deploy a bare-metal host, you must create a secret to access the baseboard management controller (BMC). This means you can remotely provision or manage the physical hardware.

<div>

<div class="title">

Procedure

</div>

1.  Create a BMC secret file by running the following command:

    ``` terminal
    $ vim bmaas-<name>-bmc-secret.yaml
    ```

    Replace `<name>` with the name of the bare-metal host.

2.  Edit the secret:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: bmaas-<name>-bmc-secret
      namespace: bmaas
    type: Opaque
    data:
      username: <base64_of_uid>
      password: <base64_of_pwd>
    ```

    \<base64_of_uid\>
    Replace `<base64_of_uid>` with the BMC user name as a Base64-encoded string.

    \<base64_of_pwd\>
    Replace `<base64_of_pwd>` with the BMC password as a Base64-encoded string.

3.  Apply the BMC secret by running the following command:

    ``` terminal
    $ oc apply -f bmaas-<name>-bmc-secret.yaml
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [About BMC addressing](ipi/ipi-install-installation-workflow.md#bmc-addressing_ipi-install-installation-workflow)

</div>

# Creating a bare-metal host resource

To deploy a bare-metal host, you must create a `BareMetalHost` resource.

<div>

<div class="title">

Procedure

</div>

1.  Create a `BareMetalHost` custom resource (CR) file by running the following command:

    ``` terminal
    $ vim bmaas-<name>-bmh.yaml
    ```

    \<name\>
    Replace `<name>` with the name of the bare-metal host.

2.  Edit the CR:

    ``` yaml
    apiVersion: metal3.io/v1alpha1
    kind: BareMetalHost
    metadata:
      name: bmaas-<name>
      namespace:  bmaas
    spec:
      online: true
      bootMACAddress: <mac_addr>
      bmc:
        address: redfish-virtualmedia+<address>/redfish/v1/Systems/System.Embedded.1
        credentialsName: bmaas-<num>-bmc-secret
    ```

    \<mac_addr\>
    Replace `<mac_addr>` with the MAC address of the first NIC on the bare-metal host.

    \<address\>
    Replace `<address>` with IP address or FQDN of the host.

3.  Apply the CR by running the following command:

    ``` terminal
    $ oc apply -f bmaas-<name>-bmh.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Check the `BareMetalHost` state by running the following command:

  ``` terminal
  $ oc get baremetalhost -n bmaas
  ```

  The state progresses from **registering**, to **inspecting**, and finally to **available**.

</div>

# Configuring users for Red Hat Bare Metal as a Service for OpenShift hosts

Configure bare-metal host users and add them to a Kubernetes secret. Then, create and apply the secret to customize the host. With configured users you can access or manage the bare-metal host after it is provisioned.

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `<hostname>-user-data.yaml`, where `<hostname>` is the name of the bare-metal host, with the following content:

    ``` yaml
    users:
      - name: <name>
        sudo: [<sudo_config>]
        ssh_authorized_keys:
          - <key_type>
          <key>
        shell: <shell_path>
        groups: [<groups>]
        lock_passwd: true|false
    ```

    `users.name`
    The user name.

    `users.sudo`
    The sudo configuration for the user.

    `users.ssh_authorized_keys.<key_type>`
    The SSH key type.

    `users.ssh_authorized_keys.<key>`
    The public SSH key to use when accessing this host as the `<name>` user.

    `users.shell`
    The shell to use when accessing the host.

    `users.groups`
    The groups the user belongs to.

    `users.lock_passwd`
    Whether the user password is locked. If `true`, the user cannot log in by using the password, but can still use SSH.

    <div class="formalpara">

    <div class="title">

    Example user

    </div>

    ``` yaml
    users:
      - name: sysadmin
        sudo: ["ALL=(ALL) NOPASSWD:ALL"]
        ssh_authorized_keys:
          - ssh-rsa AAAAB3NzaC1yc2E... sysadmin@workstation.example.com
        shell: /bin/bash
        groups: [adm, sudo]
        lock_passwd: true
    ```

    </div>

2.  Create a secret from the `<hostname>-user-data.yaml` file by running the following command:

    ``` terminal
    $ oc create secret generic <hostname>-user-data \
      --from-file=userData=<hostname>-user-data.yaml -n bmaas
    ```

    `<hostname>`
    The name of the bare-metal host.

3.  Configure the `BareMetalHost` to use the `<hostname>-user-data.yaml` file by running the following command:

    ``` terminal
    $ oc patch baremetalhost <hostname> -n bmaas \
         --type merge -p '{"spec":{"userData":{"name":"<hostname>-user-data"}}}'
    ```

    `<hostname>`
    The name of the bare-metal host.

</div>

# Configuring the networkData parameter in the BareMetalHost resource

The `networkData` field in the `BareMetalHost` custom resource (CR) allows you to control the network configuration of the bare-metal host at creation time. For most operating systems, this is achieved using a configuration file encapsulated in a Kubernetes secret. Then, the `cloud-init` service uses it to customize services.

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `network-data.yaml` with the following content:

    ``` yaml
    links:
      - id: <interface_id>
        type: phy
        ethernet_mac_address: <mac_address>
    networks:
      - id: <interface_id>
        link: <interface_id>
        type: ipv4_dhcp
    services:
      - type: dns
        address: <dns_server>
    ```

    `<interface_id>`
    The ID of the network interface, such as `enp2s0`.

    `<mac_address>`
    The MAC address of the network interface.

    `<dns_server>`
    The IP address of the DNS server.

2.  Create a secret from the `networkData` file by running the following command:

    ``` terminal
    $ oc create secret generic <hostname>-network-data \
      --from-file=networkData=network-data.yaml -n bmaas
    ```

    `<hostname>`
    The hostname of the bare-metal host.

3.  Configure the `BareMetalHost` to use the `networkData` file by running the following command:

    ``` terminal
    $ oc patch baremetalhost <hostname> -n bmaas \
      --type merge -p '{"spec":{"networkData":{"name":"<hostname>-network-data"}}}'
    ```

</div>

# Deploying an image to the bare-metal host

To deploy the image to the host, update the `image` field in the `spec` section of the `BareMetalHost` resource. Once you update the `image` field, provisioning begins immediately. Deploying an image transforms bare hardware into a functional system ready to run your workloads, in an automated and repeatable way.

<div>

<div class="title">

Procedure

</div>

- Update the `image` field in the `BareMetalHost` CR by running the following command:

  ``` terminal
  $ oc patch baremetalhost <hostname> \
    --type merge -p '{"spec": {"image": {"url": "<image_url>", "checksum": "<checksum_url>", "checksumType": "auto"}}}'
  ```

  `<hostname>`
  The name of your `BareMetalHost` resource.

  `<image_url>`
  The URL of the image to deploy.

  `<checksum_url>`
  The URL of the checksum file for the image.

</div>
