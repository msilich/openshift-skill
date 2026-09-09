<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) creates an administrator account, `admin`, during the installation process that can be used to log in with a user name and password. The password is dynamically generated unless specifically overridden and is unique to your RHACS instance.

In production environments, it is highly recommended to create an authentication provider and remove the `admin` user.

<a id="remove_admin-user_remove-admin-user"></a>

# Removing the admin user after installation

After an authentication provider has been successfully created, it is strongly recommended to remove the `admin` user.

Removing the `admin` user is dependent on the installation method of the RHACS portal.

<div class="formalpara">

<div class="title">

Procedure

</div>

Perform one of the following procedures:

</div>

- For Operator installations, set `central.adminPasswordGenerationDisabled` to `true` in your `Central` custom resource.

- For Helm installations:

  1.  In your `Central` Helm configuration, set `central.adminPassword.generate` to `false`.

  2.  Follow the steps to change the configuration. See "Changing configuration options after deployment" for more information.

- For `roxctl` installations:

  1.  When generating the manifest, set `Disable password generation` to `false`.

  2.  Follow the steps to install Central by using `roxctl` to apply the changes. See "Install Central using the roxctl CLI" for more information.

<div>

<div class="title">

Additional resources

</div>

- [Changing configuration options after deploying the central-services Helm chart (OpenShift Container Platform)](../../installing/installing_ocp/install-central-ocp.md#change-config-options-after-deployment-central-services_install-central-ocp)

- [Changing configuration options after deploying the central-services Helm chart (Kubernetes)](../../installing/installing_other/install-central-other.md#change-config-options-after-deployment-central-services_install-central-other)

- [Install Central using the roxctl CLI](../../installing/installing_ocp/install-central-ocp.md)

</div>

After applying the configuration changes, you cannot log in as an `admin` user.

> [!NOTE]
> You can add the `admin` user again as a fallback by reverting the configuration changes. When enabling the `admin` user again, a new password is generated.
