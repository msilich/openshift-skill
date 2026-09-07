<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can remove the CLI Manager Operator from OpenShift Container Platform by uninstalling the CLI Manager Operator and removing its related resources.

> [!IMPORTANT]
> Using the CLI Manager Operator to install and manage plugins for the OpenShift CLI is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Uninstalling the CLI Manager Operator

You can uninstall the CLI Manager Operator by using the web console.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.

- You have access to the OpenShift Container Platform web console.

- The CLI Manager Operator is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Uninstall the CLI Manager Operator by completing the following steps:

    1.  Navigate to **Ecosystem** → **Installed Operators**.

    2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the **CLI Manager Operator** entry and click **Uninstall Operator**.

    3.  In the confirmation dialog, click **Uninstall**.

</div>

# Removing CLI Manager Operator resources

Optionally, after you uninstall the CLI Manager Operator, you can remove its related resources from your cluster.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.

- You have access to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Remove the `openshift-cli-manager-operator` namespace:

    1.  Navigate to **Administration** → **Namespaces**.

    2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the **openshift-cli-manager-operator** entry and select **Delete Namespace**.

    3.  In the confirmation dialog, enter `openshift-cli-manager-operator` in the field and click **Delete**.

</div>
