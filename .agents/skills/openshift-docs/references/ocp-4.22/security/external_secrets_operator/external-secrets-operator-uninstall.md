<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can remove the External Secrets Operator for Red Hat OpenShift from OpenShift Container Platform by uninstalling the Operator and removing its related resources.

# Uninstalling the External Secrets Operator for Red Hat OpenShift using the web console

You can uninstall the External Secrets Operator for Red Hat OpenShift from your cluster using the OpenShift Container Platform web console. Uninstalling the Operator does not automatically delete the `ExternalSecrets` custom resources or the running `external-secrets` application workload. These resources remain in the cluster to prevent accidental data loss and must be removed manually if they are no longer needed.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

- The External Secrets Operator is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Uninstall the External Secrets Operator for Red Hat OpenShift using the following steps:

    1.  Navigate to **Ecosystem** → **Installed Operators**.

    2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the **External Secrets Operator for Red Hat OpenShift** entry and click **Uninstall Operator**.

    3.  In the confirmation dialog, click **Uninstall**.

</div>

# Removing External Secrets Operator for Red Hat OpenShift resources by using the web console

After you have uninstalled the External Secrets Operator for Red Hat OpenShift, you can optionally eliminate its associated resources from your cluster.

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

2.  Remove the deployments of the `external-secrets` application components in the `external-secrets` namespace:

    1.  Click the **Project** drop-down menu to see a list of all available projects, and select the **external-secrets** project.

    2.  Navigate to **Workloads** → **Deployments**.

    3.  Select the deployment that you want to delete.

    4.  Click the **Actions** drop-down menu, and select **Delete Deployment** to see a confirmation dialog box.

    5.  Click **Delete** to delete the deployment.

3.  Remove the custom resource definitions (CRDs) that were installed by the External Secrets Operator using the following steps:

    1.  Navigate to **Administration** → **CustomResourceDefinitions**.

    2.  Choose `external-secrets.io/component: controller` from the suggestions in the **Label** field to filter the CRDs.

    3.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to each of the following CRDs, and select **Delete Custom Resource Definition**:

        - ACRAccessToken

        - ClusterExternalSecret

        - ClusterGenerator

        - ClusterPushSecret

        - ClusterSecretStore

        - ECRAuthorizationToken

        - ExternalSecret

        - GCRAccessToken

        - GeneratorState

        - GithubAccessToken

        - Grafana

        - MFA

        - Password

        - PushSecret

        - QuayAccessToken

        - SecretStore

        - SSHKey

        - STSSessionToken

        - UUID

        - VaultDynamicSecret

        - Webhook

4.  Remove the `external-secrets-operator` namespace using the following steps:

    1.  Navigate to **Administration** → **Namespaces**.

    2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the **External Secrets Operator** and select **Delete Namespace**.

    3.  In the confirmation dialog, enter `external-secrets-operator` in the field and click **Delete**.

</div>

# Removing External Secrets Operator for Red Hat OpenShift resources by using the CLI

After you have uninstalled the External Secrets Operator for Red Hat OpenShift, you can optionally eliminate its associated resources from your cluster by using the command-line interface (CLI).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Delete the deployments of the `external-secrets` application components in the `external-secrets` namespace by running the following command:

    ``` terminal
    $ oc delete deployment -n external-secrets -l app=external-secrets
    ```

2.  Delete the custom resource definitions (CRDs) that were installed by the External Secrets Operator by running the following command:

    ``` terminal
    $ oc delete customresourcedefinitions.apiextensions.k8s.io -l external-secrets.io/component=controller
    ```

3.  Delete the `external-secrets-operator` namespace by running the following command:

    ``` terminal
    $ oc delete project external-secrets-operator
    ```

</div>
