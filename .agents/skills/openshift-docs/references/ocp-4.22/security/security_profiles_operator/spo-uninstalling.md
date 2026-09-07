<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can remove the Security Profiles Operator from your cluster by using the OpenShift Container Platform web console.

# Uninstall the Security Profiles Operator by using the web console

To remove the Security Profiles Operator, you must first delete the `seccomp` and SELinux profiles. After the profiles are removed, you can then remove the Operator and its namespace by deleting the **openshift-security-profiles** project.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the web console as a user with `cluster-admin` privileges.

- The Security Profiles Operator is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the **Ecosystem** → **Installed Operators** page.

2.  Delete all `seccomp` profiles, SELinux profiles, and webhook configurations.

3.  Switch to the **Administration** → **Ecosystem** → **Installed Operators** page.

4.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) on the **Security Profiles Operator** entry.

5.  Select **Uninstall Operator**.

6.  Switch to the **Home** → **Projects** page.

7.  Search for `security profiles`.

8.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the **openshift-security-profiles** project.

9.  Select **Delete Project**.

    1.  Enter `openshift-security-profiles` in the dialog box.

    2.  Click **Delete**.

10. Delete the `MutatingWebhookConfiguration` object by running the following command:

    ``` terminal
    $ oc delete MutatingWebhookConfiguration spo-mutating-webhook-configuration
    ```

</div>
