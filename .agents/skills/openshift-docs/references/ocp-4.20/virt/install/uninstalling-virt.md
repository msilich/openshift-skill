<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can uninstall OpenShift Virtualization by using the web console or the command-line interface (CLI) to delete OpenShift Virtualization workloads, the Operator, and its resources.

To uninstall OpenShift Virtualization, perform the following tasks:

1.  Delete the `HyperConverged` CR.

2.  Delete the OpenShift Virtualization Operator.

3.  Delete the `openshift-cnv` namespace.

4.  Delete the OpenShift Virtualization custom resource definitions (CRDs).

# Prerequisites

- Delete all virtual machine instances. You cannot uninstall OpenShift Virtualization while its workloads remain on the cluster.

# Deleting the HyperConverged custom resource

To uninstall OpenShift Virtualization, you first delete the `HyperConverged` custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the **Ecosystem** → **Installed Operators** page.

2.  Select the OpenShift Virtualization Operator.

3.  Click the **OpenShift Virtualization Deployment** tab.

4.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) beside `kubevirt-hyperconverged` and select **Delete HyperConverged**.

5.  Click **Delete** in the confirmation window.

</div>

# Deleting Operators from a cluster using the web console

Cluster administrators can delete installed Operators from a selected namespace by using the web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform cluster web console using an account with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the **Ecosystem** → **Installed Operators** page.

2.  Scroll or enter a keyword into the **Filter by name** field to find the Operator that you want to remove. Then, click on it.

3.  On the right side of the **Operator Details** page, select **Uninstall Operator** from the **Actions** list.

    An **Uninstall Operator?** dialog box is displayed.

4.  Select **Uninstall** to remove the Operator, Operator deployments, and pods. Following this action, the Operator stops running and no longer receives updates.

    > [!NOTE]
    > This action does not remove resources managed by the Operator, including custom resource definitions (CRDs) and custom resources (CRs). Dashboards and navigation items enabled by the web console and off-cluster resources that continue to run might need manual clean up. To remove these after uninstalling the Operator, you might need to manually delete the Operator CRDs.

</div>

# Deleting a namespace using the web console

You can delete a namespace by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Administration** → **Namespaces**.

2.  Locate the namespace that you want to delete in the list of namespaces.

3.  On the far right side of the namespace listing, select **Delete Namespace** from the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=).

4.  When the **Delete Namespace** pane opens, enter the name of the namespace that you want to delete in the field.

5.  Click **Delete**.

</div>

# Deleting OpenShift Virtualization custom resource definitions

You can delete the OpenShift Virtualization custom resource definitions (CRDs) by using the web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Administration** → **CustomResourceDefinitions**.

2.  Select the **Label** filter and enter `operators.coreos.com/kubevirt-hyperconverged.openshift-cnv` in the **Search** field to display the OpenShift Virtualization CRDs.

3.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) beside each CRD and select **Delete CustomResourceDefinition**.

</div>

# Uninstalling OpenShift Virtualization by using the CLI

You can uninstall OpenShift Virtualization by using the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

- You have installed the OpenShift CLI (`oc`).

- You have deleted all virtual machines and virtual machine instances. You cannot uninstall OpenShift Virtualization while its workloads remain on the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Delete the `HyperConverged` custom resource:

    ``` terminal
    $ oc delete HyperConverged kubevirt-hyperconverged -n openshift-cnv
    ```

2.  Delete the OpenShift Virtualization Operator subscription:

    ``` terminal
    $ oc delete subscription hco-operatorhub -n openshift-cnv
    ```

3.  Delete the OpenShift Virtualization `ClusterServiceVersion` resource:

    ``` terminal
    $ oc delete csv -n openshift-cnv -l operators.coreos.com/kubevirt-hyperconverged.openshift-cnv
    ```

4.  Delete the OpenShift Virtualization namespace:

    ``` terminal
    $ oc delete namespace openshift-cnv
    ```

5.  List the OpenShift Virtualization custom resource definitions (CRDs) by running the `oc delete crd` command with the `dry-run` option:

    ``` terminal
    $ oc delete crd --dry-run=client -l operators.coreos.com/kubevirt-hyperconverged.openshift-cnv
    ```

    Example output:

        customresourcedefinition.apiextensions.k8s.io "cdis.cdi.kubevirt.io" deleted (dry run)
        customresourcedefinition.apiextensions.k8s.io "hostpathprovisioners.hostpathprovisioner.kubevirt.io" deleted (dry run)
        customresourcedefinition.apiextensions.k8s.io "hyperconvergeds.hco.kubevirt.io" deleted (dry run)
        customresourcedefinition.apiextensions.k8s.io "kubevirts.kubevirt.io" deleted (dry run)
        customresourcedefinition.apiextensions.k8s.io "networkaddonsconfigs.networkaddonsoperator.network.kubevirt.io" deleted (dry run)
        customresourcedefinition.apiextensions.k8s.io "ssps.ssp.kubevirt.io" deleted (dry run)
        customresourcedefinition.apiextensions.k8s.io "tektontasks.tektontasks.kubevirt.io" deleted (dry run)

6.  Delete the CRDs by running the `oc delete crd` command without the `dry-run` option:

    ``` terminal
    $ oc delete crd -l operators.coreos.com/kubevirt-hyperconverged.openshift-cnv
    ```

</div>

# Additional resources

- [Deleting the `HyperConverged` custom resource](uninstalling-virt.md#virt-deleting-deployment-custom-resource_uninstalling-virt)

- [Deleting Operators from a cluster using the web console](uninstalling-virt.md#olm-deleting-operators-from-a-cluster-using-web-console_uninstalling-virt)

- [Deleting a namespace using the web console](uninstalling-virt.md#deleting-a-namespace-using-the-web-console_uninstalling-virt)

- [Deleting OpenShift Virtualization custom resource definitions](uninstalling-virt.md#virt-deleting-virt-crds-web_uninstalling-virt)

- [Deleting a virtual machine using the web console](../managing_vms/virt-delete-vms.md#virt-delete-vm-web_virt-delete-vms)

- [Deleting a standalone virtual machine instance using the CLI](../managing_vms/virt-manage-vmis.md#virt-deleting-vmis-cli_virt-manage-vmis)
