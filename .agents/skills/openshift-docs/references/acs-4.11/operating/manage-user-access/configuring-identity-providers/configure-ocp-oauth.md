<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Container Platform includes a built-in OAuth server that you can use as an authentication provider for Red Hat Advanced Cluster Security for Kubernetes (RHACS).

<a id="configure-ocp-oauth-identity-provider_configure-ocp-oauth"></a>

# Configuring OpenShift Container Platform OAuth server as an identity provider

To integrate the built-in OpenShift Container Platform OAuth server as an identity provider for RHACS, use the instructions in this section.

<div>

<div class="title">

Prerequisites

</div>

- You must have the `Access` permission to configure identity providers in RHACS.

- You must have already configured users and groups in OpenShift Container Platform OAuth server through an identity provider. For information about the identity provider requirements, see [Understanding identity provider configuration](https://docs.openshift.com/container-platform/4.9/authentication/understanding-identity-provider.html).

</div>

> [!NOTE]
> The following procedure configures only a single main route named `central` for the OpenShift Container Platform OAuth server.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Access Control**.

2.  Click **Create auth provider** and select **OpenShift Auth** from the drop-down list.

3.  Enter a name for the authentication provider in the **Name** field.

4.  Assign a **Minimum access role** for users that access RHACS using the selected identity provider. A user must have the permissions granted to this role or a role with higher permissions to log in to RHACS.

    > [!TIP]
    > For security, Red Hat recommends first setting the **Minimum access role** to **None** while you complete setup. Later, you can return to the **Access Control** page to set up more tailored access rules based on user metadata from your identity provider.

5.  Optional: To add access rules for users and groups accessing RHACS, click **Add new rule** in the **Rules** section, then enter the rule information and click **Save**. You will need attributes for the user or group so that you can configure access.

    > [!TIP]
    > Group mappings are more robust because groups are usually associated with teams or permissions sets and require modification less often than users.

    To get user information in OpenShift Container Platform, you can use one of the following methods:

    - Click **User Management** → **Users** → **\<username**\> → **YAML**.

    - Access the `k8s/cluster/user.openshift.io~v1~User/<username>/yaml` file and note the values for `name`, `uid` (`userid` in RHACS), and `groups`.

    - Use the OpenShift Container Platform API as described in the *OpenShift Container Platform API reference*.

    The following configuration example describes how to configure rules for an **Admin** role with the following attributes:

    - `name`: `administrator`

    - `groups`: `["system:authenticated", "system:authenticated:oauth", "myAdministratorsGroup"]`

    - `uid`: `12345-00aa-1234-123b-123fcdef1234`

    You can add a rule for this administrator role using one of the following steps:

    - To configure a rule for a name, select `name` from the **Key** drop-down list, enter `administrator` in the **Value** field, then select **Administrator** under **Role**.

    - To configure a rule for a group, select `groups` from the **Key** drop-down list, enter `myAdministratorsGroup` in the **Value** field, then select **Admin** under **Role**.

    - To configure a rule for a user name, select `userid` from the **Key** drop-down list, enter `12345-00aa-1234-123b-123fcdef1234` in the **Value** field, then select **Admin** under **Role**.

</div>

<div class="important">

<div class="title">

</div>

- If you use a custom TLS certificate for OpenShift Container Platform OAuth server, you must add the root certificate of the CA to Red Hat Advanced Cluster Security for Kubernetes as a trusted root CA. Otherwise, Central cannot connect to the OpenShift Container Platform OAuth server.

- To enable the OpenShift Container Platform OAuth server integration when installing Red Hat Advanced Cluster Security for Kubernetes using the `roxctl` CLI, set the `ROX_ENABLE_OPENSHIFT_AUTH` environment variable to `true` in Central:

  ``` terminal
  $ oc -n stackrox set env deploy/central ROX_ENABLE_OPENSHIFT_AUTH=true
  ```

- For access rules, the OpenShift Container Platform OAuth server does not return the key `Email`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring an LDAP identity provider](https://docs.openshift.com/container-platform/4.12/authentication/identity_providers/configuring-ldap-identity-provider.html)

- [Adding trusted certificate authorities](../../../configuration/add-trusted-ca.md)

</div>

<a id="create-additional-routes-ocp-oauth_configure-ocp-oauth"></a>

# Creating additional routes for OpenShift Container Platform OAuth server

When you configure OpenShift Container Platform OAuth server as an identity provider by using Red Hat Advanced Cluster Security for Kubernetes portal, RHACS configures only a single route for the OAuth server. However, you can create additional routes by specifying them as annotations in the Central custom resource.

<div>

<div class="title">

Prerequisites

</div>

- You must have configured [Service accounts as OAuth clients](https://docs.openshift.com/container-platform/4.12/authentication/using-service-accounts-as-oauth-client.html#service-accounts-as-oauth-clients_using-service-accounts-as-oauth-client) for your OpenShift Container Platform OAuth server.

</div>

<div>

<div class="title">

Procedure

</div>

- If you installed RHACS using the RHACS Operator:

  1.  Create a `CENTRAL_ADDITIONAL_ROUTES` environment variable that contains a patch for the Central custom resource:

      ``` terminal
      $ CENTRAL_ADDITIONAL_ROUTES='
      spec:
        central:
          exposure:
            loadBalancer:
              enabled: false
              port: 443
            nodePort:
              enabled: false
            route:
              enabled: true
          persistence:
            persistentVolumeClaim:
              claimName: stackrox-db
        customize:
          annotations:
            serviceaccounts.openshift.io/oauth-redirecturi.main: sso/providers/openshift/callback
            serviceaccounts.openshift.io/oauth-redirectreference.main: "{\"kind\":\"OAuthRedirectReference\",\"apiVersion\":\"v1\",\"reference\":{\"kind\":\"Route\",\"name\":\"central\"}}"
            serviceaccounts.openshift.io/oauth-redirecturi.second: sso/providers/openshift/callback
            serviceaccounts.openshift.io/oauth-redirectreference.second: "{\"kind\":\"OAuthRedirectReference\",\"apiVersion\":\"v1\",\"reference\":{\"kind\":\"Route\",\"name\":\"second-central\"}}"
      '
      ```

      where:

      `spec.customize.annotations.serviceaccounts.openshift.io/oauth-redirecturi.main`  
      Specifies the redirect URI for setting the main route.

      `spec.customize.annotations.serviceaccounts.openshift.io/oauth-redirectreference.main`  
      Specifies the redirect URI reference for the main route.

      `spec.customize.annotations.serviceaccounts.openshift.io/oauth-redirecturi.second`  
      Specifies the redirect for setting the second route.

      `spec.customize.annotations.serviceaccounts.openshift.io/oauth-redirectreference.second`  
      Specifies the redirect reference for the second route.

  2.  Apply the `CENTRAL_ADDITIONAL_ROUTES` patch to the Central custom resource:

      ``` terminal
      $ oc patch centrals.platform.stackrox.io \
        -n <namespace> \
        <custom-resource> \
        --patch "$CENTRAL_ADDITIONAL_ROUTES" \
        --type=merge
      ```

      where:

      `<namespace>`  
      Specifies the name of the project that contains the Central custom resource.

      `<custom-resource>`  
      Specifies the name of the Central custom resource.

- Or, if you installed RHACS using Helm:

  1.  Add the following annotations to your `values-public.yaml` file:

      ``` yaml
      customize:
        central:
          annotations:
            serviceaccounts.openshift.io/oauth-redirecturi.main: sso/providers/openshift/callback
            serviceaccounts.openshift.io/oauth-redirectreference.main: "{\"kind\":\"OAuthRedirectReference\",\"apiVersion\":\"v1\",\"reference\":{\"kind\":\"Route\",\"name\":\"central\"}}"
            serviceaccounts.openshift.io/oauth-redirecturi.second: sso/providers/openshift/callback
            serviceaccounts.openshift.io/oauth-redirectreference.second: "{\"kind\":\"OAuthRedirectReference\",\"apiVersion\":\"v1\",\"reference\":{\"kind\":\"Route\",\"name\":\"second-central\"}}"
      ```

      where:

      `customize.central.annotations.serviceaccounts.openshift.io/oauth-redirecturi.main`  
      Specifies the redirect for setting the main route.

      `customize.central.annotations.serviceaccounts.openshift.io/oauth-redirectreference.main`  
      Specifies the redirect reference for the main route.

      `customize.central.annotations.serviceaccounts.openshift.io/oauth-redirecturi.second`  
      Specifies the redirect for setting the second route.

      `customize.central.annotations.serviceaccounts.openshift.io/oauth-redirectreference.second`  
      Specifies the redirect reference for the second route.

  2.  Apply the custom annotations to the Central custom resource by using `helm upgrade`:

      ``` terminal
      $ helm upgrade -n stackrox \
        stackrox-central-services rhacs/central-services \
        -f <path_to_values_public.yaml>
      ```

      where:

      `<path_to_values_public.yaml>`  
      Specifies the path of the `values-public.yaml` configuration file.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Service accounts as OAuth clients](https://docs.openshift.com/container-platform/4.12/authentication/using-service-accounts-as-oauth-client.html#service-accounts-as-oauth-clients_using-service-accounts-as-oauth-client)

- [Redirect URIs for service accounts as OAuth clients](https://docs.openshift.com/container-platform/4.12/authentication/using-service-accounts-as-oauth-client.html#redirect-uris-for-service-accounts_using-service-accounts-as-oauth-client)

</div>
