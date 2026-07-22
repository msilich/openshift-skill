<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure the `github` identity provider to validate user names and passwords against GitHub or GitHub Enterprise’s OAuth authentication server. OAuth facilitates a token exchange flow between OpenShift Container Platform and GitHub or GitHub Enterprise.

You can use the GitHub integration to connect to either GitHub or GitHub Enterprise. For GitHub Enterprise integrations, you must provide the `hostname` of your instance and can optionally provide a `ca` certificate bundle to use in requests to the server.

> [!NOTE]
> The following steps apply to both GitHub and GitHub Enterprise unless noted.

# About identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform user names containing `/`, `:`, and `%` are not supported.

# About GitHub authentication

Configuring [GitHub authentication](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/authorizing-oauth-apps) allows users to log in to OpenShift Container Platform with their GitHub credentials. To prevent anyone with any GitHub user ID from logging in to your OpenShift Container Platform cluster, you can restrict access to only those in specific GitHub organizations.

# Registering a GitHub application

To use GitHub or GitHub Enterprise as an identity provider, you must register an application to use.

<div>

<div class="title">

Procedure

</div>

1.  Register an application on GitHub:

    - For GitHub, click [**Settings**](https://github.com/settings/profile) → [**Developer settings**](https://github.com/settings/apps) → [**OAuth Apps**](https://github.com/settings/developers) → [**Register a new OAuth application**](https://github.com/settings/applications/new).

    - For GitHub Enterprise, go to your GitHub Enterprise home page and then click **Settings → Developer settings → Register a new application**.

2.  Enter an application name, for example `My OpenShift Install`.

3.  Enter a homepage URL, such as `https://oauth-openshift.apps.<cluster-name>.<cluster-domain>`.

4.  Optional: Enter an application description.

5.  Enter the authorization callback URL, where the end of the URL contains the identity provider `name`:

        https://oauth-openshift.apps.<cluster-name>.<cluster-domain>/oauth2callback/<idp-provider-name>

    For example:

        https://oauth-openshift.apps.openshift-cluster.example.com/oauth2callback/github

6.  Click **Register application**. GitHub provides a client ID and a client secret. You need these values to complete the identity provider configuration.

</div>

# Creating the secret

Identity providers use OpenShift Container Platform `Secret` objects in the `openshift-config` namespace to contain the client secret, client certificates, and keys.

<div>

<div class="title">

Procedure

</div>

- Create a `Secret` object containing a string by using the following command:

  ``` terminal
  $ oc create secret generic <secret_name> --from-literal=clientSecret=<secret> -n openshift-config
  ```

  > [!TIP]
  > You can alternatively apply the following YAML to create the secret:
  >
  > ``` yaml
  > apiVersion: v1
  > kind: Secret
  > metadata:
  >   name: <secret_name>
  >   namespace: openshift-config
  > type: Opaque
  > data:
  >   clientSecret: <base64_encoded_client_secret>
  > ```

- You can define a `Secret` object containing the contents of a file by using the following command:

  ``` terminal
  $ oc create secret generic <secret_name> --from-file=<path_to_file> -n openshift-config
  ```

</div>

# Creating a config map

Identity providers use OpenShift Container Platform `ConfigMap` objects in the `openshift-config` namespace to contain the certificate authority bundle. These are primarily used to contain certificate bundles needed by the identity provider.

> [!NOTE]
> This procedure is only required for GitHub Enterprise.

<div>

<div class="title">

Procedure

</div>

- Define an OpenShift Container Platform `ConfigMap` object containing the certificate authority by using the following command. The certificate authority must be stored in the `ca.crt` key of the `ConfigMap` object.

  ``` terminal
  $ oc create configmap ca-config-map --from-file=ca.crt=/path/to/ca -n openshift-config
  ```

  > [!TIP]
  > You can alternatively apply the following YAML to create the config map:
  >
  > ``` yaml
  > apiVersion: v1
  > kind: ConfigMap
  > metadata:
  >   name: ca-config-map
  >   namespace: openshift-config
  > data:
  >   ca.crt: |
  >     <CA_certificate_PEM>
  > ```

</div>

# Sample GitHub CR

The following custom resource (CR) shows the parameters and acceptable values for a GitHub identity provider.

<div class="formalpara">

<div class="title">

GitHub CR

</div>

``` yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: githubidp
    mappingMethod: claim
    type: GitHub
    github:
      ca:
        name: ca-config-map
      clientID: {...}
      clientSecret:
        name: github-secret
      hostname: ...
      organizations:
      - myorganization1
      - myorganization2
      teams:
      - myorganization1/team-a
      - myorganization2/team-b
```

</div>

- This provider name is prefixed to the GitHub numeric user ID to form an identity name. It is also used to build the callback URL.

- Controls how mappings are established between this provider’s identities and `User` objects.

- Optional: Reference to an OpenShift Container Platform `ConfigMap` object containing the PEM-encoded certificate authority bundle to use in validating server certificates for the configured URL. Only for use in GitHub Enterprise with a non-publicly trusted root certificate.

- The client ID of a [registered GitHub OAuth application](https://github.com/settings/applications/new). The application must be configured with a callback URL of `https://oauth-openshift.apps.<cluster-name>.<cluster-domain>/oauth2callback/<idp-provider-name>`.

- Reference to an OpenShift Container Platform `Secret` object containing the client secret issued by GitHub.

- For GitHub Enterprise, you must provide the hostname of your instance, such as `example.com`. This value must match the GitHub Enterprise `hostname` value in in the `/setup/settings` file and cannot include a port number. If this value is not set, then either `teams` or `organizations` must be defined. For GitHub, omit this parameter.

- The list of organizations. Either the `organizations` or `teams` field must be set unless the `hostname` field is set, or if `mappingMethod` is set to `lookup`. Cannot be used in combination with the `teams` field.

- The list of teams. Either the `teams` or `organizations` field must be set unless the `hostname` field is set, or if `mappingMethod` is set to `lookup`. Cannot be used in combination with the `organizations` field.

> [!NOTE]
> If `organizations` or `teams` is specified, only GitHub users that are members of at least one of the listed organizations will be allowed to log in. If the GitHub OAuth application configured in `clientID` is not owned by the organization, an organization owner must grant third-party access to use this option. This can be done during the first GitHub login by the organization’s administrator, or from the GitHub organization settings.

<div>

<div class="title">

Additional resources

</div>

- See [Identity provider parameters](../understanding-identity-provider.md#identity-provider-parameters_understanding-identity-provider) for information on parameters, such as `mappingMethod`, that are common to all identity providers.

</div>

# Adding an identity provider to your cluster

After you install your cluster, add an identity provider to it so your users can authenticate.

<div>

<div class="title">

Prerequisites

</div>

- Create an OpenShift Container Platform cluster.

- Create the custom resource (CR) for your identity providers.

- You must be logged in as an administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Apply the defined CR:

    ``` terminal
    $ oc apply -f </path/to/CR>
    ```

    > [!NOTE]
    > If a CR does not exist, `oc apply` creates a new CR and might trigger the following warning: `Warning: oc apply should be used on resources created by either oc create --save-config or oc apply`. In this case you can safely ignore this warning.

2.  Obtain a token from the OAuth server.

    As long as the `kubeadmin` user has been removed, the `oc login` command provides instructions on how to access a web page where you can retrieve the token.

    You can also access this page from the web console by navigating to **(?) Help** → **Command Line Tools** → **Copy Login Command**.

3.  Log in to the cluster, passing in the token to authenticate.

    ``` terminal
    $ oc login --token=<token>
    ```

    > [!NOTE]
    > This identity provider does not support logging in with a user name and password.

4.  Confirm that the user logged in successfully, and display the user name.

    ``` terminal
    $ oc whoami
    ```

</div>
