<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Delete certificates and secrets from installed secrets management Operators using the External Secrets Management Console Plug-in in the OpenShift Container Platform web console.

> [!IMPORTANT]
> External Secrets Management Console Plug-in is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Deleting certificates and secrets by using External Secrets Management Console Plug-in

You can delete certificates and secrets from installed secrets management Operators across your clusters by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform cluster as a user with the `cluster-admin` role.

- You have installed the External Secrets Management Console Plug-in.

- You have installed at least one secrets management Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Navigate to **Plugins** → **Secrets Management**.

3.  Click ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) for the custom resource that you want to delete, and then click **Delete**.

4.  Enter the name of the custom resource.

5.  Click **Delete**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Navigate to **Ecosystem** → **Installed Operators**.

2.  Select the secrets management Operator whose custom resource you deleted.

3.  Verify that the deleted custom resource no longer appears in the Operator details view.

</div>
