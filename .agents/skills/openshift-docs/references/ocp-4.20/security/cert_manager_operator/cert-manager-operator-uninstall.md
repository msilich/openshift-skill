<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can remove the cert-manager Operator for Red Hat OpenShift from OpenShift Container Platform by uninstalling the Operator and removing its related resources.

# Uninstalling the cert-manager Operator for Red Hat OpenShift

You can uninstall the cert-manager Operator for Red Hat OpenShift by using the web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

- The cert-manager Operator for Red Hat OpenShift is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Uninstall the cert-manager Operator for Red Hat OpenShift Operator.

    1.  Navigate to **Ecosystem** → **Installed Operators**.

    2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the **cert-manager Operator for Red Hat OpenShift** entry and click **Uninstall Operator**.

    3.  In the confirmation dialog, click **Uninstall**.

</div>

# Removing cert-manager Operator for Red Hat OpenShift resources

Once you have uninstalled the cert-manager Operator for Red Hat OpenShift, you have the option to eliminate its associated resources from your cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Remove the deployments of the cert-manager components, such as `cert-manager`, `cainjector`, and `webhook`, present in the `cert-manager` namespace.

    1.  Click the **Project** drop-down menu to see a list of all available projects, and select the **cert-manager** project.

    2.  Navigate to **Workloads** → **Deployments**.

    3.  Select the deployment that you want to delete.

    4.  Click the **Actions** drop-down menu, and select **Delete Deployment** to see a confirmation dialog box.

    5.  Click **Delete** to delete the deployment.

    6.  Alternatively, delete deployments of the cert-manager components such as `cert-manager`, `cainjector` and `webhook` present in the `cert-manager` namespace by using the command-line interface (CLI).

        ``` terminal
        $ oc delete deployment -n cert-manager -l app.kubernetes.io/instance=cert-manager
        ```

3.  Optional: Remove the custom resource definitions (CRDs) that were installed by the cert-manager Operator for Red Hat OpenShift:

    1.  Remove the finalizers from the `CertManager` custom resource (CR) by running the following command:

        ``` terminal
        $ oc patch certmanagers.operator cluster --type=merge -p='{"metadata":{"finalizers":null}}'
        ```

    2.  Navigate to **Administration** → **CustomResourceDefinitions**.

    3.  Enter `certmanager` in the **Name** field to filter the CRDs.

    4.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to each of the following CRDs, and select **Delete Custom Resource Definition**:

        - `Certificate`

        - `CertificateRequest`

        - `CertManager` (`operator.openshift.io`)

        - `Challenge`

        - `ClusterIssuer`

        - `Issuer`

        - `Order`

4.  Optional: Remove the `cert-manager-operator` namespace.

    1.  Navigate to **Administration** → **Namespaces**.

    2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the **cert-manager-operator** and select **Delete Namespace**.

    3.  In the confirmation dialog, enter `cert-manager-operator` in the field and click **Delete**.

</div>
