<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Encrypt and decrypt etcd data in OpenShift Container Platform to protect sensitive cluster resources such as secrets, config maps, and OAuth tokens.

# etcd encryption

By default, etcd data is not encrypted in OpenShift Container Platform. You can enable etcd encryption for your cluster to provide an additional layer of data security. For example, it can help protect the loss of sensitive data if an etcd backup is exposed to the incorrect parties.

When you enable etcd encryption, the following OpenShift API server and Kubernetes API server resources are encrypted:

- Secrets

- Config maps

- Routes

- OAuth access tokens

- OAuth authorize tokens

When you enable etcd encryption, encryption keys are created. You must have these keys to restore from an etcd backup.

> [!NOTE]
> etcd encryption only encrypts values, not keys. Resource types, namespaces, and object names are unencrypted.
>
> If etcd encryption is enabled during a backup, the `static_kuberesources_<datetimestamp>.tar.gz` file contains the encryption keys for the etcd snapshot. For security reasons, store this file separately from the etcd snapshot. However, this file is required to restore a previous state of etcd from the respective etcd snapshot.

# Supported encryption types

OpenShift Container Platform supports AES-CBC and AES-GCM encryption types to protect etcd data at rest.

The following encryption types are supported for encrypting etcd data in OpenShift Container Platform:

AES-CBC
Uses AES-CBC with PKCS#7 padding and a 32-byte key to perform the encryption.

AES-GCM
Uses AES-GCM with a random nonce and a 32-byte key to perform the encryption.

The etcd encryption keys are rotated every 7 days. Up to 10 historical encryption keys are preserved after rotation to help decrypt older backups and provide an extra layer of data recovery safety.

# Enabling etcd encryption

Enable etcd encryption to protect sensitive cluster resources such as secrets, config maps, routes, and OAuth tokens at rest.

> [!WARNING]
> Do not back up etcd resources until the initial encryption process is completed. If the encryption process is not completed, the backup might be only partially encrypted.
>
> After you enable etcd encryption, several changes can occur:
>
> - The etcd encryption might affect the memory consumption of a few resources.
>
> - You might notice a transient effect on backup performance because the leader must serve the backup.
>
> - A disk I/O can affect the node that receives the backup state.

You can encrypt the etcd database in either AES-GCM or AES-CBC encryption.

> [!NOTE]
> To migrate your etcd database from one encryption type to the other, you can modify the API server’s `spec.encryption.type` field. Migration of the etcd data to the new encryption type occurs automatically.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Modify the `APIServer` object:

    ``` terminal
    $ oc edit apiserver
    ```

2.  Set the `spec.encryption.type` field to `aesgcm` or `aescbc`:

    ``` yaml
    spec:
      encryption:
        type: aesgcm
    ```

    - The `aesgcm` value specifies AES-GCM encryption. Alternatively, set the `type` field to `aescbc` for AES-CBC encryption.

3.  Save the file to apply the changes.

    The encryption process starts. It can take 20 minutes or longer for this process to complete, depending on the size of the etcd database.

</div>

<div>

<div class="title">

Verification

</div>

- Review the `Encrypted` status condition for the OpenShift API server to verify that its resources were successfully encrypted:

  ``` terminal
  $ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{"\n"}{"\n"}'
  ```

  The output shows `EncryptionCompleted` upon successful encryption:

  ``` terminal
  EncryptionCompleted
  All resources encrypted: routes.route.openshift.io
  ```

  If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again.

- Review the `Encrypted` status condition for the Kubernetes API server to verify that its resources were successfully encrypted:

  ``` terminal
  $ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{"\n"}{"\n"}'
  ```

  The output shows `EncryptionCompleted` upon successful encryption:

  ``` terminal
  EncryptionCompleted
  All resources encrypted: secrets, configmaps
  ```

  If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again.

- Review the `Encrypted` status condition for the OpenShift OAuth API server to verify that its resources were successfully encrypted:

  ``` terminal
  $ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{"\n"}{"\n"}'
  ```

  The output shows `EncryptionCompleted` upon successful encryption:

  ``` terminal
  EncryptionCompleted
  All resources encrypted: oauthaccesstokens.oauth.openshift.io, oauthauthorizetokens.oauth.openshift.io
  ```

  If the output shows `EncryptionInProgress`, encryption is still in progress. Wait a few minutes and try again.

</div>

# Disabling etcd encryption

Disable etcd encryption when you no longer need to encrypt sensitive cluster resources at rest.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Modify the `APIServer` object:

    ``` terminal
    $ oc edit apiserver
    ```

2.  Set the `encryption` field type to `identity`:

    ``` yaml
    spec:
      encryption:
        type: identity
    ```

    The `identity` value specifies that no encryption is performed. This is the default value.

3.  Save the file to apply the changes.

    The decryption process starts. It can take 20 minutes or longer for this process to complete, depending on the size of your cluster.

</div>

<div>

<div class="title">

Verification

</div>

- Review the `Encrypted` status condition for the OpenShift API server to verify that its resources were successfully decrypted:

  ``` terminal
  $ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{"\n"}{"\n"}'
  ```

  The output shows `DecryptionCompleted` upon successful decryption:

  ``` terminal
  DecryptionCompleted
  Encryption mode set to identity and everything is decrypted
  ```

  If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again.

- Review the `Encrypted` status condition for the Kubernetes API server to verify that its resources were successfully decrypted:

  ``` terminal
  $ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{"\n"}{"\n"}'
  ```

  The output shows `DecryptionCompleted` upon successful decryption:

  ``` terminal
  DecryptionCompleted
  Encryption mode set to identity and everything is decrypted
  ```

  If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again.

- Review the `Encrypted` status condition for the OpenShift OAuth API server to verify that its resources were successfully decrypted:

  ``` terminal
  $ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{"\n"}{"\n"}'
  ```

  The output shows `DecryptionCompleted` upon successful decryption:

  ``` terminal
  DecryptionCompleted
  Encryption mode set to identity and everything is decrypted
  ```

  If the output shows `DecryptionInProgress`, decryption is still in progress. Wait a few minutes and try again.

</div>
