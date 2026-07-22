<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure the registry of a cluster that runs on your own Red Hat OpenStack Platform (RHOSP) infrastructure.

# Configuring Image Registry Operator redirects

By disabling redirects, you can configure the Image Registry Operator to control whether clients such as OpenShift Container Platform cluster builds or external systems like developer machines are redirected to pull images directly from Red Hat OpenStack Platform (RHOSP) Swift storage. This configuration is optional and depends on whether the clients trust the storage’s SSL/TLS certificates.

> [!NOTE]
> In situations where clients to not trust the storage certificate, setting the `disableRedirect` option can be set to `true` proxies traffic through the image registry. Consequently, however, the image registry might require more resources, especially network bandwidth, to handle the increased load.
>
> Alternatively, if clients trust the storage certificate, the registry can allow redirects. This reduces resource demand on the registry itself.
>
> Some users might prefer to configure their clients to trust their self-signed certificate authorities (CAs) instead of disabling redirects. If you are using a self-signed CA, you must decide between trusting the custom CAs or disabling redirects.

<div>

<div class="title">

Procedure

</div>

- To ensures that the image registry proxies traffic instead of relying on Swift storage, change the value of the `spec.disableRedirect` field in the `config.imageregistry` object to `true` by running the following command:

  ``` terminal
  $ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"disableRedirect":true}}'
  ```

</div>

# Configuring a secret for the Image Registry Operator

In addition to the `configs.imageregistry.operator.openshift.io` and ConfigMap resources, configuration is provided to the Operator by a separate secret resource located within the `openshift-image-registry` namespace.

The `image-registry-private-configuration-user` secret provides credentials needed for storage access and management. It overrides the default credentials used by the Operator, if default credentials were found.

For Swift on Red Hat OpenStack Platform (RHOSP) storage, the secret is expected to contain the following two keys:

- `REGISTRY_STORAGE_SWIFT_USERNAME`

- `REGISTRY_STORAGE_SWIFT_PASSWORD`

<div>

<div class="title">

Procedure

</div>

- Create an OpenShift Container Platform secret that contains the required keys.

  ``` terminal
  $ oc create secret generic image-registry-private-configuration-user --from-literal=REGISTRY_STORAGE_SWIFT_USERNAME=<username> --from-literal=REGISTRY_STORAGE_SWIFT_PASSWORD=<password> -n openshift-image-registry
  ```

</div>

# Registry storage for RHOSP with user-provisioned infrastructure

If the Registry Operator cannot create a Swift bucket, you must set up the storage medium manually and configure the settings in the registry custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- A cluster on Red Hat OpenStack Platform (RHOSP) with user-provisioned infrastructure.

- To configure registry storage for RHOSP, you need to provide Registry Operator cloud credentials.

- For Swift on RHOSP storage, the secret is expected to contain the following two keys:

  - `REGISTRY_STORAGE_SWIFT_USERNAME`

  - `REGISTRY_STORAGE_SWIFT_PASSWORD`

</div>

<div>

<div class="title">

Procedure

</div>

- Fill in the storage configuration in `configs.imageregistry.operator.openshift.io/cluster`:

  ``` terminal
  $ oc edit configs.imageregistry.operator.openshift.io/cluster
  ```

  <div class="formalpara">

  <div class="title">

  Example configuration

  </div>

  ``` yaml
  apiVersion: imageregistry.operator.openshift.io/v1
  kind: Config
  metadata:
    name: cluster
  spec:
    storage:
      swift:
        container: <container_id>
  ```

  </div>

</div>

# Image Registry Operator configuration parameters for RHOSP Swift

The following parameters are available for you to configure your Red Hat OpenStack Platform (RHOSP) Swift registry storage.

| Parameter | Description |
|----|----|
| `authURL` | Defines the URL for obtaining the authentication token. This value is optional. |
| `authVersion` | Specifies the Auth version of RHOSP, for example, `authVersion: "3"`. This value is optional. |
| `container` | Defines the name of a Swift container for storing registry data. This value is optional. |
| `domain` | Specifies the RHOSP domain name for the Identity v3 API. This value is optional. |
| `domainID` | Specifies the RHOSP domain ID for the Identity v3 API. This value is optional. |
| `tenant` | Defines the RHOSP tenant name to be used by the registry. This value is optional. |
| `tenantID` | Defines the RHOSP tenant ID to be used by the registry. This value is optional. |
| `regionName` | Defines the RHOSP region in which the container exists. This value is optional. |
