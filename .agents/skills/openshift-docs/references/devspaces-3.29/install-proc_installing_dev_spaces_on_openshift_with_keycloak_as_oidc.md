> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-proc_installing_dev_spaces_on_openshift_with_keycloak_as_oidc). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy using an external identity provider

Deploy OpenShift Dev Spaces with Keycloak as the OIDC provider so that you can manage user authentication through your organization’s existing identity infrastructure instead of OpenShift OAuth.

## Before you begin

- An active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- Keycloak configured as an external identity provider for OpenShift. See [Enabling direct authentication with an external OIDC identity provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/external-auth).

## Procedure

1.  Create a `devspaces` client in the Keycloak Admin Console:
    1.  Within the realm used for OpenShift authentication, select **Clients** on the left side of the navigation bar.
    2.  Select the **Create client** button.
    3.  On the **General Settings** page:
        1.  Enter `devspaces` in the **Client ID** field.
        2.  Optional: Enter a **Name** and **Description** for the OAuth client.
        3.  Click **Next**.
    4.  On the **Capability config** page:
        1.  Toggle **Client authentication** to **On**.
        2.  Click **Next**.
    5.  On the **Login settings** page:
        1.  Enter the OpenShift Dev Spaces redirect URL in the **Valid redirect URIs** field. Note

            Run the following command to obtain the Red Hat OpenShift Dev Spaces redirect URL:

            ``` bash
            echo "$(
              oc whoami --show-console |
              sed 's|console-openshift-console|red-hat-openshift-devspaces|g'
            )/oauth/callback"
            ```

        2.  Click **Save**.
    6.  Navigate to the **Credentials** tab of the newly created client and copy the **Client secret** value for use when applying the OAuth client secret.

2.  Add the `devspaces` client to the audiences list in the OpenShift authentication configuration:

    ``` bash
    oc patch authentication.config/cluster \
      --type='json' \
      -p='[
        {
          "op": "add",
          "path": "/spec/oidcProviders/0/issuer/audiences/-",
          "value": "devspaces"
        }
      ]'
    ```

    Note

    If you have multiple OIDC providers configured, adjust the array index in the path (currently `0`) to match your Keycloak provider’s position in the configuration.

3.  Wait for the `kube-apiserver` cluster Operator to roll out the configuration changes:

    ``` bash
    watch oc get co kube-apiserver
    ```

4.  Create a project for OpenShift Dev Spaces:

    ``` bash
    oc create project openshift-devspaces
    ```

5.  Create a Secret for OAuth authentication:

    ``` yaml
    oc apply -f - <<EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: devspaces-oidc-client-secret
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
    stringData:
      oAuthSecret: <client_secret>
    EOF
    ```

    where:

    ` `*`<client_secret>`*` `  
    The client secret value from the `devspaces` client credentials tab in Keycloak.

6.  Prepare the `CheCluster` patch:

    ``` yaml
    cat > che-patch.yaml <<EOF
    kind: CheCluster
    apiVersion: org.eclipse.che/v2
    spec:
      networking:
        auth:
          oAuthClientName: devspaces
          oAuthSecret: devspaces-oidc-client-secret
          gateway:
            oAuthProxy:
              cookieExpireSeconds: 300
            deployment:
              containers:
                - name: oauth-proxy
                  env:
                    - name: OAUTH2_PROXY_BACKEND_LOGOUT_URL
                      value: "<issuer_url>/protocol/openid-connect/logout?id_token_hint={id_token}"
    EOF
    ```

    where:

    ` `*`<issuer_url>`*` `  
    The Keycloak OIDC issuer URL for your realm.

7.  Create the OpenShift Dev Spaces instance with `dsc`:

    ``` bash
    dsc server:deploy \
      --platform openshift \
      --che-operator-cr-patch-yaml che-patch.yaml
    ```

## Results

1.  Verify the OpenShift Dev Spaces instance status:

    ``` bash
    dsc server:status
    ```

2.  Navigate to the OpenShift Dev Spaces cluster instance:

    ``` bash
    dsc dashboard:open
    ```

3.  Log in to the OpenShift Dev Spaces instance.

**Related information**  

- [Enabling direct authentication with an external OIDC identity provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/external-auth)
