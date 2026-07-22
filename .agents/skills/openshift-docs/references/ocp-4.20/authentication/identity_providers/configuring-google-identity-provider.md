<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure the `google` identity provider using the [Google OpenID Connect integration](https://developers.google.com/identity/protocols/OpenIDConnect).

# About identity providers in OpenShift Container Platform

You can configure identity providers by creating a custom resource (CR) that describes the provider and adding it to the cluster. Identity providers enable user authentication in OpenShift Container Platform beyond the default `kubeadmin` user.

> [!NOTE]
> OpenShift Container Platform user names containing `/`, `:`, and `%` are not supported.

# About Google authentication

Using Google as an identity provider allows any Google user to authenticate to your server. You can limit authentication to members of a specific hosted domain with the `hostedDomain` configuration attribute.

> [!NOTE]
> Using Google as an identity provider requires users to get a token using `<namespace_route>/oauth/token/request` to use with command-line tools.

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

# Sample Google CR

The following custom resource (CR) shows the parameters and acceptable values for a Google identity provider.

<div class="formalpara">

<div class="title">

Google CR

</div>

``` yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: googleidp
    mappingMethod: claim
    type: Google
    google:
      clientID: {...}
      clientSecret:
        name: google-secret
      hostedDomain: "example.com"
```

</div>

- This provider name is prefixed to the Google numeric user ID to form an identity name. It is also used to build the redirect URL.

- Controls how mappings are established between this provider’s identities and `User` objects.

- The client ID of a [registered Google project](https://console.developers.google.com/). The project must be configured with a redirect URI of `https://oauth-openshift.apps.<cluster-name>.<cluster-domain>/oauth2callback/<idp-provider-name>`.

- Reference to an OpenShift Container Platform `Secret` object containing the client secret issued by Google.

- A [hosted domain](https://developers.google.com/identity/protocols/OpenIDConnect#hd-param) used to restrict sign-in accounts. Optional if the `lookup` `mappingMethod` is used. If empty, any Google account is allowed to authenticate.

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
