<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can restore kubelet certificates on your OpenShift Container Platform cluster by approving pending certificate signing requests (CSRs) after control plane certificates expire. Approved CSRs return nodes to a healthy state.

# Recovering from expired control plane certificates

You can restore kubelet certificates by manually approving pending `node-bootstrapper` certificate signing requests (CSRs) and, on user-provisioned installations, kubelet serving CSRs. Approved CSRs return nodes to a healthy state after control plane certificates expire.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have access to the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the list of current CSRs by running the following command:

    ``` terminal
    $ oc get csr
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        AGE    SIGNERNAME                                    REQUESTOR                                                                   CONDITION
    csr-2s94x   8m3s   kubernetes.io/kubelet-serving                 system:node:<node_name>                                                     Pending
    csr-4bd6t   8m3s   kubernetes.io/kubelet-serving                 system:node:<node_name>                                                     Pending
    csr-4hl85   13m    kubernetes.io/kube-apiserver-client-kubelet   system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
    csr-zhhhp   3m8s   kubernetes.io/kube-apiserver-client-kubelet   system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
    ...
    ```

    </div>

    In the example output, CSRs with a `SIGNERNAME` of `kubernetes.io/kubelet-serving` are kubelet serving CSRs. You see this CSR type on user-provisioned installations. CSRs with a `SIGNERNAME` of `kubernetes.io/kube-apiserver-client-kubelet` and a `node-bootstrapper` requestor are `node-bootstrapper` CSRs that you must approve to restore kubelet certificates.

2.  Review the details of a CSR to verify that it is valid by running the following command:

    ``` terminal
    $ oc describe csr <csr_name>
    ```

    `<csr_name>` is the name of a CSR from the list of current CSRs.

3.  Approve each valid `node-bootstrapper` CSR by running the following command:

    ``` terminal
    $ oc adm certificate approve <csr_name>
    ```

4.  For user-provisioned installations, approve each valid kubelet serving CSR by running the following command:

    ``` terminal
    $ oc adm certificate approve <csr_name>
    ```

</div>
