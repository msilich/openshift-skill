<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Install the External Secrets Management Console Plug-in from the OpenShift Container Platform web console **Software Catalog** to manage certificates and secrets across installed secrets management Operators.

> [!IMPORTANT]
> External Secrets Management Console Plug-in is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Installing the External Secrets Management Console Plug-in

You can use the web console to install the External Secrets Management Console Plug-in.

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

2.  Navigate to **Ecosystem** → **Software Catalog**.

3.  Enter **External Secrets Management Console** into the filter box.

4.  Select **External Secrets Management Console**.

5.  Select the External Secrets Management Console Plug-in version from the **Version** drop-down list, and click **Install**.

6.  On the **Install Operator** page:

    1.  Update the **Update channel**, if necessary. The channel defaults to **tech-preview-v1**.

    2.  Select an **Update approval** strategy.

        - The **Automatic** strategy allows the Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.

        - The **Manual** strategy requires a user with appropriate credentials to approve the Operator update.

    3.  Click **Install**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that **External Secrets Management Console Plug-in** is available under **Plugins**.

2.  Verify that all the installed secrets management Operators are listed when you click **External Secrets Management Console Plug-in**.

</div>
