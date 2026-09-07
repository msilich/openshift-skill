<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The OpenShift Container Platform control plane includes a built-in OAuth server. You can obtain OAuth access tokens to authenticate to the OpenShift Container Platform API. After you create your hosted cluster, you can configure OAuth by specifying an identity provider.

# Configuring the OAuth server for a hosted cluster by using the CLI

You can configure the internal OAuth server for your hosted cluster by using the command-line interface (CLI).

You can configure OAuth for the following supported identity providers:

- `oidc`

- `htpasswd`

- `keystone`

- `ldap`

- `basic-authentication`

- `request-header`

- `github`

- `gitlab`

- `google`

Adding any identity provider in the OAuth configuration removes the default `kubeadmin` user provider.

> [!NOTE]
> When you configure identity providers, you must configure at least one `NodePool` replica in your hosted cluster in advance. Traffic for DNS resolution is sent through the worker nodes. You do not need to configure the `NodePool` replicas in advance for the `htpasswd` and `request-header` identity providers.

<div>

<div class="title">

Prerequisites

</div>

- You created your hosted cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `HostedCluster` custom resource (CR) on the management cluster by running the following command:

    ``` terminal
    $ oc edit hostedcluster <hosted_cluster_name> -n <hosted_cluster_namespace>
    ```

2.  Add the OAuth configuration in the `HostedCluster` CR by using the following example:

    ``` yaml
    apiVersion: hypershift.openshift.io/v1alpha1
    kind: HostedCluster
    metadata:
      name: <hosted_cluster_name>
      namespace: <hosted_cluster_namespace>
    spec:
      configuration:
        oauth:
          identityProviders:
          - openID:
              claims:
                email:
                  - <email_address>
                name:
                  - <display_name>
                preferredUsername:
                  - <preferred_username>
              clientID: <client_id>
              clientSecret:
                name: <client_id_secret_name>
              issuer: https://example.com/identity
            mappingMethod: lookup
            name: IAM
            type: OpenID
    ```

    - `metadata.name` specifies your hosted cluster name.

    - `metadata.namespace` specifies your hosted cluster namespace.

    - `spec.configuration.oauth.identityProviders.openID` is a provider name that is prefixed to the value of the identity claim to form an identity name. The provider name is also used to build the redirect URL.

    - `spec.configuration.oauth.identityProviders.openID.claims.email` defines a list of attributes to use as the email address.

    - `spec.configuration.oauth.identityProviders.openID.claims.name` defines a list of attributes to use as a display name.

    - `spec.configuration.oauth.identityProviders.openID.claims.preferredUsername` defines a list of attributes to use as a preferred user name.

    - `spec.configuration.oauth.identityProviders.openID.clientID` defines the ID of a client registered with the OpenID provider. You must allow the client to redirect to the `https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>` URL.

    - `spec.configuration.oauth.identityProviders.openID.clientSecret.name` defines a secret of a client registered with the OpenID provider.

    - `spec.configuration.oauth.identityProviders.openID.issuer` specifies the Issuer Identifier described in the OpenID spec. You must use `https` without query or fragment component. For more information about Issuer Identifiers, see "Issuer Identifier".

    - `spec.configuration.oauth.identityProviders.mappingMethod` defines a mapping method that controls how mappings are established between identities of this provider and `User` objects.

3.  Save the file to apply the changes.

</div>

# Configuring the OAuth server for a hosted cluster by using the web console

You can configure the internal OAuth server for your hosted cluster by using the OpenShift Container Platform web console.

You can configure OAuth for the following supported identity providers:

- `oidc`

- `htpasswd`

- `keystone`

- `ldap`

- `basic-authentication`

- `request-header`

- `github`

- `gitlab`

- `google`

Adding any identity provider in the OAuth configuration removes the default `kubeadmin` user provider.

> [!NOTE]
> When you configure identity providers, you must configure at least one `NodePool` replica in your hosted cluster in advance. Traffic for DNS resolution is sent through the worker nodes. You do not need to configure the `NodePool` replicas in advance for the `htpasswd` and `request-header` identity providers.

<div>

<div class="title">

Prerequisites

</div>

- You logged in as a user with `cluster-admin` privileges.

- You created your hosted cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to **Home** → **API Explorer**.

2.  Use the **Filter by kind** box to search for your `HostedCluster` resource.

3.  Click the `HostedCluster` resource that you want to edit.

4.  Click the **Instances** tab.

5.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to your hosted cluster name entry and click **Edit HostedCluster**.

6.  Add the OAuth configuration in the YAML file:

    ``` yaml
    apiVersion: hypershift.openshift.io/v1alpha1
    kind: HostedCluster
    metadata:
      #...
    spec:
      configuration:
        oauth:
          identityProviders:
          - openID:
              claims:
                email:
                  - <email_address>
                name:
                  - <display_name>
                preferredUsername:
                  - <preferred_username>
              clientID: <client_id>
              clientSecret:
                name: <client_id_secret_name>
              issuer: https://example.com/identity
            mappingMethod: lookup
            name: IAM
            type: OpenID
    ```

    - `spec.configuration.oauth.identityProviders.openID` specifies the provider name that is prefixed to the value of the identity claim to form an identity name. The provider name is also used to build the redirect URL.

    - `spec.configuration.oauth.identityProviders.openID.claims.email` defines a list of attributes to use as the email address.

    - `spec.configuration.oauth.identityProviders.openID.claims.name` defines a list of attributes to use as a display name.

    - `spec.configuration.oauth.identityProviders.openID.claims.preferredUsername` defines a list of attributes to use as a preferred user name.

    - `spec.configuration.oauth.identityProviders.openID.clientID` defines the ID of a client registered with the OpenID provider. You must allow the client to redirect to the `https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>` URL.

    - `spec.configuration.oauth.identityProviders.openID.clientSecret.name` defines a secret of a client registered with the OpenID provider.

    - `spec.configuration.oauth.identityProviders.openID.issuer` specifies the Issuer Identifier described in the OpenID spec. You must use `https` without query or fragment component. For more information, see "Issuer Identifier".

    - `spec.configuration.oauth.identityProviders.mappingMethod` defines a mapping method that controls how mappings are established between identities of this provider and `User` objects.

7.  Click **Save**.

</div>

# IAM roles assigned by using the CCO in a hosted cluster on AWS

You can assign components Identity and Access Management (IAM) roles that provide short-term, limited-privilege security credentials by using the Cloud Credential Operator (CCO) in hosted clusters on Amazon Web Services (AWS).

By default, the CCO runs in a hosted control plane.

> [!NOTE]
> The CCO supports a manual mode only for hosted clusters on AWS. By default, hosted clusters are configured in a manual mode. The management cluster might use modes other than manual.

## Enabling Operators to support CCO-based workflows with AWS STS

As an Operator author designing your project to run on Operator Lifecycle Manager (OLM), you can enable your Operator to authenticate against AWS on STS-enabled OpenShift Container Platform clusters by customizing your project to support the Cloud Credential Operator (CCO).

With this method, the Operator is responsible for and requires RBAC permissions for creating the `CredentialsRequest` object and reading the resulting `Secret` object.

> [!NOTE]
> By default, pods related to the Operator deployment mount a `serviceAccountToken` volume so that the service account token can be referenced in the resulting `Secret` object.

<div>

<div class="title">

Prerequisites

</div>

- OpenShift Container Platform 4.14 or later

- Cluster in STS mode

- OLM-based Operator project

</div>

<div>

<div class="title">

Procedure

</div>

1.  Update your Operator project’s `ClusterServiceVersion` (CSV) object:

    1.  Ensure your Operator has RBAC permission to create `CredentialsRequests` objects:

        <div class="formalpara">

        <div class="title">

        Example `clusterPermissions` list

        </div>

        ``` yaml
        # ...
        install:
          spec:
            clusterPermissions:
            - rules:
              - apiGroups:
                - "cloudcredential.openshift.io"
                resources:
                - credentialsrequests
                verbs:
                - create
                - delete
                - get
                - list
                - patch
                - update
                - watch
        ```

        </div>

    2.  Add the following annotation to claim support for this method of CCO-based workflow with AWS STS:

        ``` yaml
        # ...
        metadata:
         annotations:
           features.operators.openshift.io/token-auth-aws: "true"
        ```

2.  Update your Operator project code:

    1.  Get the role ARN from the environment variable set on the pod by the `Subscription` object. For example:

        ``` go
        // Get ENV var
        roleARN := os.Getenv("ROLEARN")
        setupLog.Info("getting role ARN", "role ARN = ", roleARN)
        webIdentityTokenPath := "/var/run/secrets/openshift/serviceaccount/token"
        ```

    2.  Ensure you have a `CredentialsRequest` object ready to be patched and applied. For example:

        <div class="formalpara">

        <div class="title">

        Example `CredentialsRequest` object creation

        </div>

        ``` go
        import (
           minterv1 "github.com/openshift/cloud-credential-operator/pkg/apis/cloudcredential/v1"
           corev1 "k8s.io/api/core/v1"
           metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
        )

        var in = minterv1.AWSProviderSpec{
           StatementEntries: []minterv1.StatementEntry{
              {
                 Action: []string{
                    "s3:*",
                 },
                 Effect:   "Allow",
                 Resource: "arn:aws:s3:*:*:*",
              },
           },
            STSIAMRoleARN: "<role_arn>",
        }

        var codec = minterv1.Codec
        var ProviderSpec, _ = codec.EncodeProviderSpec(in.DeepCopyObject())

        const (
           name      = "<credential_request_name>"
           namespace = "<namespace_name>"
        )

        var CredentialsRequestTemplate = &minterv1.CredentialsRequest{
           ObjectMeta: metav1.ObjectMeta{
               Name:      name,
               Namespace: "openshift-cloud-credential-operator",
           },
           Spec: minterv1.CredentialsRequestSpec{
              ProviderSpec: ProviderSpec,
              SecretRef: corev1.ObjectReference{
                 Name:      "<secret_name>",
                 Namespace: namespace,
              },
              ServiceAccountNames: []string{
                 "<service_account_name>",
              },
              CloudTokenPath:   "",
           },
        }
        ```

        </div>

        Alternatively, if you are starting from a `CredentialsRequest` object in YAML form (for example, as part of your Operator project code), you can handle it differently:

        <div class="formalpara">

        <div class="title">

        Example `CredentialsRequest` object creation in YAML form

        </div>

        ``` go
        // CredentialsRequest is a struct that represents a request for credentials
        type CredentialsRequest struct {
          APIVersion string `yaml:"apiVersion"`
          Kind       string `yaml:"kind"`
          Metadata   struct {
             Name      string `yaml:"name"`
             Namespace string `yaml:"namespace"`
          } `yaml:"metadata"`
          Spec struct {
             SecretRef struct {
                Name      string `yaml:"name"`
                Namespace string `yaml:"namespace"`
             } `yaml:"secretRef"`
             ProviderSpec struct {
                APIVersion     string `yaml:"apiVersion"`
                Kind           string `yaml:"kind"`
                StatementEntries []struct {
                   Effect   string   `yaml:"effect"`
                   Action   []string `yaml:"action"`
                   Resource string   `yaml:"resource"`
                } `yaml:"statementEntries"`
                STSIAMRoleARN   string `yaml:"stsIAMRoleARN"`
             } `yaml:"providerSpec"`

             // added new field
              CloudTokenPath   string `yaml:"cloudTokenPath"`
          } `yaml:"spec"`
        }

        // ConsumeCredsRequestAddingTokenInfo is a function that takes a YAML filename and two strings as arguments
        // It unmarshals the YAML file to a CredentialsRequest object and adds the token information.
        func ConsumeCredsRequestAddingTokenInfo(fileName, tokenString, tokenPath string) (*CredentialsRequest, error) {
          // open a file containing YAML form of a CredentialsRequest
          file, err := os.Open(fileName)
          if err != nil {
             return nil, err
          }
          defer file.Close()

          // create a new CredentialsRequest object
          cr := &CredentialsRequest{}

          // decode the yaml file to the object
          decoder := yaml.NewDecoder(file)
          err = decoder.Decode(cr)
          if err != nil {
             return nil, err
          }

          // assign the string to the existing field in the object
          cr.Spec.CloudTokenPath = tokenPath

          // return the modified object
          return cr, nil
        }
        ```

        </div>

        > [!NOTE]
        > Adding a `CredentialsRequest` object to the Operator bundle is not currently supported.

    3.  Add the role ARN and web identity token path to the credentials request and apply it during Operator initialization:

        <div class="formalpara">

        <div class="title">

        Example applying `CredentialsRequest` object during Operator initialization

        </div>

        ``` go
        // apply CredentialsRequest on install
        credReq := credreq.CredentialsRequestTemplate
        credReq.Spec.CloudTokenPath = webIdentityTokenPath

        c := mgr.GetClient()
        if err := c.Create(context.TODO(), credReq); err != nil {
           if !errors.IsAlreadyExists(err) {
              setupLog.Error(err, "unable to create CredRequest")
              os.Exit(1)
           }
        }
        ```

        </div>

    4.  Ensure your Operator can wait for a `Secret` object to show up from the CCO, as shown in the following example, which is called along with the other items you are reconciling in your Operator:

        <div class="formalpara">

        <div class="title">

        Example wait for `Secret` object

        </div>

        ``` go
        // WaitForSecret is a function that takes a Kubernetes client, a namespace, and a v1 "k8s.io/api/core/v1" name as arguments
        // It waits until the secret object with the given name exists in the given namespace
        // It returns the secret object or an error if the timeout is exceeded
        func WaitForSecret(client kubernetes.Interface, namespace, name string) (*v1.Secret, error) {
          // set a timeout of 10 minutes
          timeout := time.After(10 * time.Minute)

          // set a polling interval of 10 seconds
          ticker := time.NewTicker(10 * time.Second)

          // loop until the timeout or the secret is found
          for {
             select {
             case <-timeout:
                // timeout is exceeded, return an error
                return nil, fmt.Errorf("timed out waiting for secret %s in namespace %s", name, namespace)
                   // add to this error with a pointer to instructions for following a manual path to a Secret that will work on STS
             case <-ticker.C:
                // polling interval is reached, try to get the secret
                secret, err := client.CoreV1().Secrets(namespace).Get(context.Background(), name, metav1.GetOptions{})
                if err != nil {
                   if errors.IsNotFound(err) {
                      // secret does not exist yet, continue waiting
                      continue
                   } else {
                      // some other error occurred, return it
                      return nil, err
                   }
                } else {
                   // secret is found, return it
                   return secret, nil
                }
             }
          }
        }
        ```

        </div>

        The `timeout` value is based on an estimate of how fast the CCO might detect an added `CredentialsRequest` object and generate a `Secret` object. You might consider lowering the time or creating custom feedback for cluster administrators that could be wondering why the Operator is not yet accessing the cloud resources.

    5.  Set up the AWS configuration by reading the secret created by the CCO from the credentials request and creating the AWS config file containing the data from that secret:

        <div class="formalpara">

        <div class="title">

        Example AWS configuration creation

        </div>

        ``` go
        func SharedCredentialsFileFromSecret(secret *corev1.Secret) (string, error) {
           var data []byte
           switch {
           case len(secret.Data["credentials"]) > 0:
               data = secret.Data["credentials"]
           default:
               return "", errors.New("invalid secret for aws credentials")
           }

           f, err := ioutil.TempFile("", "aws-shared-credentials")
           if err != nil {
               return "", errors.Wrap(err, "failed to create file for shared credentials")
           }
           defer f.Close()
           if _, err := f.Write(data); err != nil {
               return "", errors.Wrapf(err, "failed to write credentials to %s", f.Name())
           }
           return f.Name(), nil
        }
        ```

        </div>

        > [!IMPORTANT]
        > The secret is assumed to exist, but your Operator code should wait and retry when using this secret to give time to the CCO to create the secret.
        >
        > Additionally, the wait period should eventually time out and warn users that the OpenShift Container Platform cluster version, and therefore the CCO, might be an earlier version that does not support the `CredentialsRequest` object workflow with STS detection. In such cases, instruct users that they must add a secret by using another method.

    6.  Configure the AWS SDK session, for example:

        <div class="formalpara">

        <div class="title">

        Example AWS SDK session configuration

        </div>

        ``` go
        sharedCredentialsFile, err := SharedCredentialsFileFromSecret(secret)
        if err != nil {
           // handle error
        }
        options := session.Options{
           SharedConfigState: session.SharedConfigEnable,
           SharedConfigFiles: []string{sharedCredentialsFile},
        }
        ```

        </div>

</div>

## Verifying the CCO installation in a hosted cluster on AWS

You can verify that the Cloud Credential Operator (CCO) is running correctly in your hosted control plane.

<div>

<div class="title">

Prerequisites

</div>

- You configured the hosted cluster on Amazon Web Services (AWS).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the CCO is configured in a manual mode in your hosted cluster by running the following command:

    ``` terminal
    $ oc get cloudcredentials <hosted_cluster_name> \
      -n <hosted_cluster_namespace> \
      -o=jsonpath={.spec.credentialsMode}
    ```

    <div class="formalpara">

    <div class="title">

    Expected output

    </div>

    ``` terminal
    Manual
    ```

    </div>

2.  Verify that the value for the `serviceAccountIssuer` resource is not empty by running the following command:

    ``` terminal
    $ oc get authentication cluster --kubeconfig <hosted_cluster_name>.kubeconfig \
      -o jsonpath --template '{.spec.serviceAccountIssuer }'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    https://aos-hypershift-ci-oidc-29999.s3.us-east-2.amazonaws.com/hypershift-ci-29999
    ```

    </div>

</div>

# Additional resources

- [Issuer Identifier](https://openid.net/specs/openid-connect-core-1_0.html#IssuerIdentifier)

- [Understanding identity provider configuration](../authentication/understanding-identity-provider.md#understanding-identity-provider)

- [Cluster Operators reference page for the Cloud Credential Operator](../operators/operator-reference.md#cloud-credential-operator_operator-reference)
