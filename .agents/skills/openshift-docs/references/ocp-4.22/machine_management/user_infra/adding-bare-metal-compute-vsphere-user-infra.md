<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To support workloads requiring direct hardware access, extend your existing VMware vSphere cluster by adding bare-metal compute machines. This creates a hybrid architecture that combines a virtualized control plane with the performance of physical hardware.

This procedure supports clusters installed using installer-provisioned infrastructure, user-provisioned infrastructure, or the Assisted Installer.

> [!IMPORTANT]
> Bare-metal nodes on vSphere clusters is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

> [!IMPORTANT]
> Bare-metal compute machines added to a vSphere cluster are unmanaged by the Machine API. You cannot use compute machine sets or the cluster autoscaler to manage these compute machines. Lifecycle tasks such as provisioning and replacement must be performed manually.

# Prerequisites

- You have an existing OpenShift Container Platform cluster installed on vSphere.

- You have bare-metal hardware with network connectivity to the existing cluster’s machine network.

- You have configured the network for the new bare-metal compute machines, including:

  - DHCP: Persistent IP addresses and hostname reservations.

  - DNS: Forward and reverse DNS resolution for the new hostnames.

- You have obtained the Red Hat Enterprise Linux CoreOS (RHCOS) ISO image that matches your cluster version. You can download this from the **Cluster Details** page on the Red Hat Hybrid Cloud Console or extract it from the cluster payload.

> [!WARNING]
> To use this feature, you must explicitly disable the native vSphere Container Storage Interface (CSI) driver for the entire cluster. This means existing vSphere virtual machines will lose the ability to provision or attach vSphere volumes. You must ensure that all workloads (virtual and physical) are migrated to an alternative storage solution before proceeding.

<div>

<div class="title">

Additional resources

</div>

- [Disabling and enabling storage on vSphere](../../storage/container_storage_interface/persistent-storage-csi-vsphere.md#persistent-storage-csi-vsphere-disable-storage-procedure_persistent-storage-csi-vsphere)

</div>

# Creating RHCOS machines using an ISO image

To add bare-metal compute machines to your VMware vSphere cluster, you must manually provision them using an RHCOS ISO image and the `coreos-installer` utility.

> [!IMPORTANT]
> Bare-metal nodes on vSphere clusters is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the RHCOS ISO image that matches your cluster version.

- You have an HTTP server accessible to the bare-metal machine to host the Ignition config file.

- You have disabled the vSphere CSI driver.

- The OpenShift CLI (`oc`) is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Extract the Ignition config file for the worker node type from the cluster by running the following command:

    ``` terminal
    $ oc extract -n openshift-machine-api secret/worker-user-data-managed --keys=userData --to=- > worker.ign
    ```

2.  Upload the `worker.ign` Ignition config file to your HTTP server. Record the URL of this file.

3.  Validate that the Ignition file is accessible from the network. The following example uses `curl` to verify the file presence:

    ``` terminal
    $ curl -I http://<http_server>/worker.ign
    ```

4.  Boot the bare-metal machine using the RHCOS ISO image.

5.  From the installation console, run the `coreos-installer` command:

    ``` terminal
    $ sudo coreos-installer install /dev/sda \
        --ignition-url=http://<http_server>/worker.ign \
        --insecure-ignition \
        --platform=metal
    ```

    where:

    `/dev/sda`
    Specifies the target install device for your hardware.

    `<http_server>`
    Specifies the address of your web server.

6.  Reboot the machine:

    ``` terminal
    $ reboot
    ```

7.  Monitor the boot process. After the machine reboots, it attempts to join the cluster and generates certificate signing requests (CSRs).

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the new compute machine has joined the cluster and is in the `Ready` state:

  ``` terminal
  $ oc get nodes
  ```

</div>

# Approving the certificate signing requests for your machines

To allow newly added machines to join your OpenShift Container Platform cluster, confirm that the cluster approves pending certificate signing requests (CSRs), or approve them yourself. Approve client requests first, then server requests.

<div>

<div class="title">

Prerequisites

</div>

- You added machines to your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Confirm that the cluster recognizes the machines:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME      STATUS    ROLES   AGE  VERSION
    master-0  Ready     master  63m  v1.35.4
    master-1  Ready     master  63m  v1.35.4
    master-2  Ready     master  64m  v1.35.4
    ```

    </div>

    The output lists all of the machines that you created.

    > [!NOTE]
    > The preceding output might not include the compute nodes until you approve some CSRs.

2.  Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster:

    ``` terminal
    $ oc get csr
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        AGE     REQUESTOR                                                                   CONDITION
    csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
    csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
    ...
    ```

    </div>

    In this example, two machines are joining the cluster. You might see more approved CSRs in the list.

3.  If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines:

    > [!NOTE]
    > You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates rotate, and more than two certificates are present for each node. You must approve all of these certificates. After you approve the client CSR, the kubelet creates a secondary CSR for the serving certificate, which requires manual approval. The `machine-approver` then automatically approves later serving certificate renewal requests if the kubelet requests a new certificate with the same parameters.

    > [!NOTE]
    > For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If you do not approve a request, the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because the API server requires a serving certificate when it connects to the kubelet. Any operation that contacts the kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the `node-bootstrapper` service account in the `system:node` or `system:admin` groups submitted the CSR, and confirm the identity of the node.

    - To approve them individually, run the following command for each valid CSR:

      ``` terminal
      $ oc adm certificate approve <csr_name>
      ```

      where:

      `<csr_name>`
      Specifies the name of a CSR from the list of current CSRs.

    - To approve all pending CSRs, run the following command:

      ``` terminal
      $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
      ```

      > [!NOTE]
      > Some Operators might not become available until you approve some CSRs. Each node submits two CSRs, so you might need to run the command to approve CSRs many times.

4.  After you approve your client requests, review the server requests for each machine that you added to the cluster:

    ``` terminal
    $ oc get csr
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        AGE     REQUESTOR                                                                   CONDITION
    csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
    csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
    ...
    ```

    </div>

5.  If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines:

    - To approve them individually, run the following command for each valid CSR:

      ``` terminal
      $ oc adm certificate approve <csr_name>
      ```

      where:

      `<csr_name>`
      Specifies the name of a CSR from the list of current CSRs.

    - To approve all pending CSRs, run the following command:

      ``` terminal
      $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
      ```

6.  After you approve all client and server CSRs, the machines have the `Ready` status. Verify this by running the following command:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME      STATUS    ROLES   AGE  VERSION
    master-0  Ready     master  73m  v1.35.4
    master-1  Ready     master  73m  v1.35.4
    master-2  Ready     master  74m  v1.35.4
    worker-0  Ready     worker  11m  v1.35.4
    worker-1  Ready     worker  11m  v1.35.4
    ```

    </div>

    > [!NOTE]
    > You might need to wait a few minutes after approval of the server CSRs for the machines to change to the `Ready` status.

</div>

# Remove the cloud provider uninitialized taint from bare-metal nodes

After a bare-metal node joins a VMware vSphere cluster, the vSphere Cloud Controller Manager (CCM) cannot remove the `node.cloudprovider.kubernetes.io/uninitialized` taint automatically. You must manually remove this taint so that workloads can be scheduled on the node.

The vSphere CCM attempts to initialize each node by searching vCenter for a matching virtual machine. Because a bare-metal node is physical hardware and not a VM in vCenter, the CCM cannot find a match and never removes the taint automatically.

> [!NOTE]
> The CCM logs errors similar to `No VM found` for bare-metal nodes. These errors are expected and do not indicate a problem with the node or the cluster.

<div>

<div class="title">

Prerequisites

</div>

- The bare-metal node has joined the cluster and its certificate signing requests (CSRs) have been approved.

- You have installed the OpenShift CLI (`oc`).

- You have cluster administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

- Remove the `node.cloudprovider.kubernetes.io/uninitialized` taint from each bare-metal node by running the following command:

  ``` terminal
  $ oc adm taint nodes <node_name> node.cloudprovider.kubernetes.io/uninitialized:NoSchedule-
  ```

  Replace `<node_name>` with the name of the bare-metal node as shown in the output of `oc get nodes`.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the taint has been removed by running the following command and confirming that `node.cloudprovider.kubernetes.io/uninitialized` does not appear in the output:

  ``` terminal
  $ oc describe node <node_name> | grep Taint
  ```

  Replace `<node_name>` with the name of the bare-metal node as shown in the output of `oc get nodes`.

</div>
