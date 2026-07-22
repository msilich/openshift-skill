<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure the `gitlab` identity provider using [GitLab.com](https://gitlab.com/) or any other GitLab instance as an identity provider.

# About identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform user names containing `/`, `:`, and `%` are not supported.

# About GitLab authentication

Configuring GitLab authentication allows users to log in to OpenShift Container Platform with their GitLab credentials.

If you use GitLab version 7.7.0 to 11.0, you connect using the [OAuth integration](https://docs.gitlab.com/ce/integration/oauth_provider.html). If you use GitLab version 11.1 or later, you can use [OpenID Connect](https://docs.gitlab.com/ce/integration/openid_connect_provider.html) (OIDC) to connect instead of OAuth.

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

# Sample GitLab CR

The following custom resource (CR) shows the parameters and acceptable values for a GitLab identity provider.

<div class="formalpara">

<div class="title">

GitLab CR

</div>

``` yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: gitlabidp
    mappingMethod: claim
    type: GitLab
    gitlab:
      clientID: {...}
      clientSecret:
        name: gitlab-secret
      url: https://gitlab.com
      ca:
        name: ca-config-map
```

</div>

- This provider name is prefixed to the GitLab numeric user ID to form an identity name. It is also used to build the callback URL.

- Controls how mappings are established between this provider’s identities and `User` objects.

- The client ID of a [registered GitLab OAuth application](https://docs.gitlab.com/ce/api/oauth2.html). The application must be configured with a callback URL of `https://oauth-openshift.apps.<cluster-name>.<cluster-domain>/oauth2callback/<idp-provider-name>`.

- Reference to an OpenShift Container Platform `Secret` object containing the client secret issued by GitLab.

- The host URL of a GitLab provider. This could either be `https://gitlab.com/` or any other self hosted instance of GitLab.

- Optional: Reference to an OpenShift Container Platform `ConfigMap` object containing the PEM-encoded certificate authority bundle to use in validating server certificates for the configured URL.

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

2.  Log in to the cluster as a user from your identity provider, entering the password when prompted.

    ``` terminal
    $ oc login -u <username>
    ```

3.  Confirm that the user logged in successfully, and display the user name.

    ``` terminal
    $ oc whoami
    ```

</div>
