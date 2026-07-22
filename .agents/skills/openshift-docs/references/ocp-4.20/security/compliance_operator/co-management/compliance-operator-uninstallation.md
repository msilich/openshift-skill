<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can remove the OpenShift Compliance Operator from your cluster by using the OpenShift Container Platform web console or the CLI.

# Uninstalling the OpenShift Compliance Operator from OpenShift Container Platform using the web console

To remove the Compliance Operator, you must first delete the objects in the namespace. After the objects are removed, you can remove the Operator and its namespace by deleting the **openshift-compliance** project.

<div>

<div class="title">

Prerequisites

</div>

- Access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

- The OpenShift Compliance Operator must be installed.

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

To remove the Compliance Operator by using the OpenShift Container Platform web console:

</div>

1.  Go to the **Ecosystem** → **Installed Operators** → **Compliance Operator** page.

    1.  Click **All instances**.

    2.  In **All namespaces**, click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) and delete all ScanSettingBinding, ComplainceSuite, ComplianceScan, and ProfileBundle objects.

2.  Switch to the **Administration** → **Ecosystem** → **Installed Operators** page.

3.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) on the **Compliance Operator** entry and select **Uninstall Operator**.

4.  Switch to the **Home** → **Projects** page.

5.  Search for 'compliance'.

6.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the **openshift-compliance** project, and select **Delete Project**.

    1.  Confirm the deletion by typing `openshift-compliance` in the dialog box, and click **Delete**.

# Uninstalling the OpenShift Compliance Operator from OpenShift Container Platform using the CLI

To remove the Compliance Operator, you must first delete the objects in the namespace. After the objects are removed, you can remove the Operator and its namespace by deleting the **openshift-compliance** project.

<div>

<div class="title">

Prerequisites

</div>

- Access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

- The OpenShift Compliance Operator must be installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Delete all objects in the namespace.

    1.  Delete the `ScanSettingBinding` objects:

        ``` terminal
        $ oc delete ssb --all -n openshift-compliance
        ```

    2.  Delete the `ScanSetting` objects:

        ``` terminal
        $ oc delete ss --all -n openshift-compliance
        ```

    3.  Delete the `ComplianceSuite` objects:

        ``` terminal
        $ oc delete suite --all -n openshift-compliance
        ```

    4.  Delete the `ComplianceScan` objects:

        ``` terminal
        $ oc delete scan --all -n openshift-compliance
        ```

    5.  Delete the `ProfileBundle` objects:

        ``` terminal
        $ oc delete profilebundle.compliance --all -n openshift-compliance
        ```

2.  Delete the Subscription object:

    ``` terminal
    $ oc delete sub --all -n openshift-compliance
    ```

3.  Delete the CSV object:

    ``` terminal
    $ oc delete csv --all -n openshift-compliance
    ```

4.  Delete the project:

    ``` terminal
    $ oc delete project openshift-compliance
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    project.project.openshift.io "openshift-compliance" deleted
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Confirm the namespace is deleted:

    ``` terminal
    $ oc get project/openshift-compliance
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Error from server (NotFound): namespaces "openshift-compliance" not found
    ```

    </div>

</div>
