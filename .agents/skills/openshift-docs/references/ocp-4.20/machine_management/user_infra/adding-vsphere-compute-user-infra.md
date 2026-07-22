<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can add more compute machines to your OpenShift Container Platform cluster on VMware vSphere manually.

> [!NOTE]
> You can also [use compute machine sets](../creating_machinesets/creating-machineset-vsphere.md#creating-machineset-vsphere) to automate the creation of additional VMware vSphere compute machines for your cluster.

# Prerequisites

- You [installed a cluster on vSphere](../../installing/installing_vsphere/upi/installing-vsphere.md#installing-vsphere).

- You have installation media and Red Hat Enterprise Linux CoreOS (RHCOS) images that you used to create your cluster. If you do not have these files, you must obtain them by following the instructions in the [installation procedure](../../installing/installing_vsphere/upi/installing-vsphere.md#installing-vsphere).

> [!IMPORTANT]
> If you do not have access to the Red Hat Enterprise Linux CoreOS (RHCOS) images that were used to create your cluster, you can add more compute machines to your OpenShift Container Platform cluster with newer versions of Red Hat Enterprise Linux CoreOS (RHCOS) images. For instructions, see [Adding new nodes to UPI cluster fails after upgrading to OpenShift 4.6+](https://access.redhat.com/solutions/5514051).

# Adding more compute machines to a cluster in vSphere

You can add more compute machines to a user-provisioned OpenShift Container Platform cluster on VMware vSphere.

After your vSphere template deploys in your OpenShift Container Platform cluster, you can deploy a virtual machine (VM) for a machine in that cluster.

<div>

<div class="title">

Prerequisites

</div>

- Obtain the base64-encoded Ignition file for your compute machines.

- You have access to the vSphere template that you created for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Right-click the template’s name and click **Clone** → **Clone to Virtual Machine**.

2.  On the **Select a name and folder** tab, specify a name for the VM. You might include the machine type in the name, such as `compute-1`.

    > [!NOTE]
    > Ensure that all virtual machine names across a vSphere installation are unique.

3.  On the **Select a name and folder** tab, select the name of the folder that you created for the cluster.

4.  On the **Select a compute resource** tab, select the name of a host in your data center.

5.  On the **Select storage** tab, select storage for your configuration and disk files.

6.  On the **Select clone options** tab, select **Customize this virtual machine’s hardware**.

7.  On the **Customize hardware** tab, click **Advanced Parameters**.

    - Add the following configuration parameter names and values by specifying data in the **Attribute** and **Values** fields. Ensure that you select the **Add** button for each parameter that you create.

      - `guestinfo.ignition.config.data`: Paste the contents of the base64-encoded compute Ignition config file for this machine type.

      - `guestinfo.ignition.config.data.encoding`: Specify `base64`.

      - `disk.EnableUUID`: Specify `TRUE`.

8.  In the **Virtual Hardware** panel of the **Customize hardware** tab, modify the specified values as required. Ensure that the amount of RAM, CPU, and disk storage meets the minimum requirements for the machine type. If many networks exist, select **Add New Device** \> **Network Adapter**, and then enter your network information in the fields provided by the **New Network** menu item.

9.  Complete the remaining configuration steps. On clicking the **Finish** button, you have completed the cloning operation.

10. From the **Virtual Machines** tab, right-click on your VM and then select **Power** → **Power On**.

</div>

<div>

<div class="title">

Next steps

</div>

- Continue to create more compute machines for your cluster.

</div>

# Approving the certificate signing requests for your machines

When you add machines to a cluster, two pending certificate signing requests (CSRs) are generated for each machine that you added. You must confirm that these CSRs are approved or, if necessary, approve them yourself. The client requests must be approved first, followed by the server requests.

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
    master-0  Ready     master  63m  v1.33.4
    master-1  Ready     master  63m  v1.33.4
    master-2  Ready     master  64m  v1.33.4
    ```

    </div>

    The output lists all of the machines that you created.

    > [!NOTE]
    > The preceding output might not include the compute nodes until some CSRs are approved.

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
    > You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates will rotate, and more than two certificates will be present for each node. You must approve all of these certificates. After the client CSR is approved, the Kubelet creates a secondary CSR for the serving certificate, which requires manual approval. The subsequent serving certificate renewal requests are then automatically approved by the `machine-approver` if the Kubelet requests a new certificate with identical parameters.

    > [!NOTE]
    > For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If a request is not approved, then the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because a serving certificate is required when the API server connects to the kubelet. Any operation that contacts the Kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the CSR was submitted by the `node-bootstrapper` service account in the `system:node` or `system:admin` groups, and confirm the identity of the node.

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
      > Some Operators might not become available until some CSRs are approved.

4.  Now that your client requests are approved, you must review the server requests for each machine that you added to the cluster:

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

6.  After all client and server CSRs have been approved, the machines have the `Ready` status. Verify this by running the following command:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME      STATUS    ROLES   AGE  VERSION
    master-0  Ready     master  73m  v1.33.4
    master-1  Ready     master  73m  v1.33.4
    master-2  Ready     master  74m  v1.33.4
    worker-0  Ready     worker  11m  v1.33.4
    worker-1  Ready     worker  11m  v1.33.4
    ```

    </div>

    > [!NOTE]
    > You might need to wait a few minutes after approval of the server CSRs for the machines to transition to the `Ready` status.

</div>
