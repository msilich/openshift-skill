<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure the `github` identity provider so users can log in to OpenShift Container Platform with GitHub or GitHub Enterprise accounts through OAuth. Use this integration when you want cluster users to authenticate with existing GitHub credentials instead of managing separate cluster passwords.

You can use the GitHub integration to connect to either GitHub or GitHub Enterprise. For GitHub Enterprise integrations, you must provide the `hostname` of your instance and can optionally provide a `ca` certificate bundle to use in requests to the server.

> [!NOTE]
> The following steps apply to both GitHub and GitHub Enterprise unless noted.

# Identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform usernames containing `/`, `:`, and `%` are not supported.

# About GitHub authentication

Configure GitHub authentication so users can log in with GitHub or GitHub Enterprise credentials. Separate OpenShift Container Platform user accounts are not required.

To prevent anyone with any GitHub user ID from logging in to your OpenShift Container Platform cluster, you can restrict access to only those in specific GitHub organizations.

# Registering a GitHub application

Register an OAuth application on GitHub or GitHub Enterprise to obtain the client ID and client secret for the identity provider configuration.

<div>

<div class="title">

Procedure

</div>

1.  Start the registration process by navigating to the appropriate page in GitHub or GitHub Enterprise:

    - For GitHub, click your profile picture in the upper right corner and select **Settings** → **Developer settings** → **OAuth Apps**.

    - For GitHub Enterprise, go to your GitHub Enterprise home page and then select **Settings → Developer settings → Register a new application**.

2.  Click **New OAuth app**.

3.  Enter an application name, for example `My OpenShift Install`.

4.  Enter a homepage URL, such as `https://oauth-openshift.apps.<cluster-name>.<cluster-domain>`.

5.  Optional: Enter an application description.

6.  Enter the authorization callback URL, where the end of the URL contains the identity provider `name`:

        https://oauth-openshift.apps.<cluster-name>.<cluster-domain>/oauth2callback/<idp-provider-name>

    For example:

        https://oauth-openshift.apps.openshift-cluster.example.com/oauth2callback/github

7.  Click **Register application**. GitHub provides a client ID and a client secret. You need these values to complete the identity provider configuration.

</div>

# Creating the secret

Create a `Secret` object in the `openshift-config` namespace to store the client secret for your identity provider. The identity provider custom resource (CR) references this secret during configuration.

<div>

<div class="title">

Procedure

</div>

1.  Create a `Secret` object containing the client secret by running the following command:

    ``` terminal
    $ oc create secret generic <secret_name> --from-literal=clientSecret=<secret> -n openshift-config
    ```

2.  Optional: Apply the following YAML to create the secret:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: <secret_name>
      namespace: openshift-config
    type: Opaque
    data:
      clientSecret: <base64_encoded_client_secret>
    ```

3.  Create a `Secret` object from a file by running the following command:

    ``` terminal
    $ oc create secret generic <secret_name> --from-file=<path_to_file> -n openshift-config
    ```

</div>

# Creating a ConfigMap

Create a `ConfigMap` object in the `openshift-config` namespace that contains the certificate authority bundle for the identity provider. OpenShift Container Platform uses this bundle to validate Transport Layer Security (TLS) connections to the identity provider.

> [!NOTE]
> This procedure is required only for GitHub Enterprise.

<div>

<div class="title">

Procedure

</div>

1.  Define an OpenShift Container Platform `ConfigMap` object containing the CA by running the following command:

    ``` terminal
    $ oc create configmap ca-config-map --from-file=ca.crt=/path/to/ca -n openshift-config
    ```

2.  Optional: Apply the following YAML to create the config map:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: ca-config-map
      namespace: openshift-config
    data:
      ca.crt: |
        <CA_certificate_PEM>
    ```

    The CA must be stored in the `ca.crt` key of the `ConfigMap` object.

</div>

# Sample GitHub CR

Review the custom resource fields and acceptable values for configuring a GitHub identity provider in OpenShift Container Platform. Use these definitions to set client credentials and access restrictions before applying the configuration to the cluster.

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

where:

`spec.identityProviders.name`
Specifies the provider name, which is prefixed to the GitHub numeric user ID to form an identity name. It is also used to build the callback URL.

`spec.identityProviders.mappingMethod`
Specifies how mappings are established between identities from this provider and `User` objects.

`spec.identityProviders.github.ca`
Specifies an optional reference to an OpenShift Container Platform `ConfigMap` object containing the PEM-encoded certificate authority bundle to use in validating server certificates for the configured URL. Only for use in GitHub Enterprise with a non-publicly trusted root certificate.

`spec.identityProviders.github.clientID`
Specifies the client ID issued when you register a GitHub OAuth application. The application must be configured with a callback URL of `https://oauth-openshift.apps.<cluster-name>.<cluster-domain>/oauth2callback/<idp-provider-name>`.

`spec.identityProviders.github.clientSecret`
Specifies a reference to an OpenShift Container Platform `Secret` object containing the client secret issued by GitHub.

`spec.identityProviders.github.hostname`
Specifies the hostname of your GitHub Enterprise instance, such as `example.com`. This value must match the GitHub Enterprise `hostname` value in the `/setup/settings` file and cannot include a port number. If this value is not set, then either `teams` or `organizations` must be defined. For GitHub, omit this parameter.

`spec.identityProviders.github.organizations`
Specifies the list of organizations. Either the `organizations` or `teams` field must be set unless the `hostname` field is set, or if `mappingMethod` is set to `lookup`. Cannot be used in combination with the `teams` field.

`spec.identityProviders.github.teams`
Specifies the list of teams. Either the `teams` or `organizations` field must be set unless the `hostname` field is set, or if `mappingMethod` is set to `lookup`. Cannot be used in combination with the `organizations` field.

> [!NOTE]
> If `organizations` or `teams` is specified, only GitHub users that are members of at least one of the listed organizations are allowed to log in. If the GitHub OAuth application configured in `clientID` is not owned by the organization, an organization owner must grant third-party access to use this option. This can be done during the first GitHub login by the administrator of the organization, or from the GitHub organization settings.

<div>

<div class="title">

Additional resources

</div>

- [Identity provider parameters](../understanding-identity-provider.md#identity-provider-parameters_understanding-identity-provider)

</div>

# Adding an identity provider to your cluster

Apply the identity provider custom resource (CR) to your cluster after you define it. With this configuration, you can authenticate with the configured identity provider.

<div>

<div class="title">

Prerequisites

</div>

- You have access to a OpenShift Container Platform cluster.

- You have created the CR for your identity providers.

- You are logged in as an administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Apply the defined CR by running the following command:

    ``` terminal
    $ oc apply -f </path/to/CR>
    ```

    > [!NOTE]
    > If a CR does not exist, `oc apply` creates a new CR and might trigger the following warning: `Warning: oc apply should be used on resources created by either oc create --save-config or oc apply`. In this case you can safely ignore this warning.

2.  Obtain a token from the OAuth server.

    As long as the `kubeadmin` user has been removed, the `oc login` command provides instructions on how to access a web page where you can retrieve the token.

    You can also access this page from the web console by navigating to **(?) Help** → **Command Line Tools** → **Copy Login Command**.

3.  Log in to the cluster by running the following command, passing in the token to authenticate:

    ``` terminal
    $ oc login --token=<token>
    ```

</div>

This identity provider does not support logging in with a username and password.

1.  Confirm that the user logged in successfully and that the username displays by running the following command:

    ``` terminal
    $ oc whoami
    ```

<div>

<div class="title">

Additional resources

</div>

- [GitHub authentication (GitHub documentation)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/authorizing-oauth-apps)

</div>
