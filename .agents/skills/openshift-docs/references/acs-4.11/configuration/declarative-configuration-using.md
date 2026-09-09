<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With declarative configuration, you can update configurations by storing them in files in repositories and apply them to the system. Declarative configuration is useful, for example, if you are using a GitOps workflow. You can currently use declarative configuration in Red Hat Advanced Cluster Security for Kubernetes (RHACS) for authentication and authorization resources such as authentication providers, roles, permission sets, and access scopes.

<a id="declarative-configuration-overview_declarative-configuration-using"></a>

# Declarative configuration overview

With declarative configuration, you can update configurations by storing them in files in repositories and apply them to the system by using config maps or secrets.

To use declarative configuration, you create YAML files that contain configuration information about authentication and authorization resources. You add these files, or configurations, to RHACS by using a mount point during Central installation. See the installation documentation in the "Additional resources" section for more information about configuring mount points when installing RHACS.

You store the configuration files used with declarative configuration in config maps or secrets, depending on the type of resource. Store configurations for authentication providers in a secret for greater security. You can store other configurations in config maps.

A single config map or secret can contain more than one configuration of many resource types. This configuration limits the number of volume mounts for the Central instance.

<a id="restrictions-declarative-config-resources_declarative-configuration-using"></a>

# Restrictions for resources created from declarative configuration

Resources created from declarative configuration have specific restrictions regarding references, naming, and modification.

Because resources can reference other resources (for example, a role can reference both a permission set and access scope), the following restrictions for references apply:

- A declarative configuration can only reference a resource that is either also created declaratively or a system RHACS resource; for example, a resource such as the `Admin` or `Analyst` system role or permission set.

- All references between resources use names to identify the resource; therefore, all names within the same resource type must be unique.

- You can only change or delete resources created from declarative configuration by altering the declarative configuration files. You cannot change these resources by using the RHACS portal or the API.

<a id="declarative-configuration-resource-create_declarative-configuration-using"></a>

# Creating declarative configurations

Use `roxctl` to create the YAML files that store the configurations, create a config map from the files, and apply the config map.

> [!NOTE]
> For OpenShift Container Platform, use `oc` instead of `kubectl`.

<div>

<div class="title">

Prerequisites

</div>

- You have added the mount for the config map or secret during the installation of Central. In this example, the config map has the name "declarative-configs". See the installation documentation for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the permission set by entering the following command. This example creates a permission set named "restricted" and saves it as the `permission-set.yaml` file. It sets read and write access for the `Administration` resource and read access to the Access resource.

    ``` terminal
    $ roxctl declarative-config create permission-set \
    --name="restricted" \
    --description="Restriction permission set that only allows \
    access to Administration and Access resources" \
    --resource-with-access=Administration=READ_WRITE_ACCESS \
    --resource-with-access=Access=READ_ACCESS > permission-set.yaml
    ```

2.  Create the role that allows access to the `Administration` and `Access` resources by entering the following command. This example creates a role named "restricted" and saves it as the `role.yaml` file.

    ``` terminal
    $ roxctl declarative-config create role \
    --name="restricted" \
    --description="Restricted role that only allows access to Administration and Access" \
    --permission-set="restricted" \
    --access-scope="Unrestricted" > role.yaml
    ```

3.  Create a config map from the two YAML files that you created in the earlier steps by entering the following command. This example creates the `declarative-configurations` config map.

    ``` terminal
    $ kubectl create configmap declarative-configurations \
    --from-file permission-set.yaml --from-file role.yaml \
    -o yaml --namespace=stackrox > declarative-configs.yaml
    ```

4.  Apply the config map by entering the following command:

    ``` terminal
    $ kubectl apply -f declarative-configs.yaml
    ```

    After you apply the config map, Central extracts the configuration information and creates the resources.

    > [!NOTE]
    > Although the watch interval is 5 seconds, as described in the following paragraph, there can be a delay in propagating changes from the config map to the Central mount.

    You can configure the following intervals to specify how declarative configurations interact with Central:

    - Configuration watch interval: The interval for Central to check for changes is every 5 seconds. You can configure this interval by using the `ROX_DECLARATIVE_CONFIG_WATCH_INTERVAL` environment variable.

    - Reconciliation interval: By default, declarative configuration reconciliation with Central occurs every 20 seconds. You can configure this interval by using the `ROX_DECLARATIVE_CONFIG_RECONCILE_INTERVAL` environment variable.

      After creating authentication and authorization resources by using declarative configuration, you can view them in the **Access Control** page in the RHACS web portal. The **Origin** field indicates `Declarative` if you created the resource by using declarative configuration.

      > [!NOTE]
      > You cannot edit resources created from declarative configurations in the RHACS web portal. You must edit the configuration files directly to make changes to these resources.

      You can view the status of declarative configurations by navigating to **Platform Configuration** → **System Health** and scrolling to the **Declarative configuration** section.

</div>

<a id="declarative-configuration-examples_declarative-configuration-using"></a>

# Declarative configuration examples

You can create declarative configurations by using the following examples as a guide. Use the `roxctl declarative-config lint` command to verify that your configurations are valid.

<a id="declarative-config-example-auth-provider_declarative-configuration-using"></a>

## Declarative configuration authentication provider example

Example YAML configuration for creating an authentication provider by using declarative configuration.

``` yaml
name: A sample auth provider
minimumRole: Analyst
uiEndpoint: central.custom-domain.com:443
extraUIEndpoints:
    - central-alt.custom-domain.com:443
groups:
    - key: email
      value: example@example.com
      role: Admin
    - key: groups
      value: reviewers
      role: Analyst
requiredAttributes:
    - key: org_id
      value: "12345"
claimMappings:
    - path: org_id
      value: my_org_id
oidc:
    issuer: sample.issuer.com
    mode: auto
    clientID: CLIENT_ID
    clientSecret: CLIENT_SECRET
clientSecret: CLIENT_SECRET
iap:
    audience: audience
saml:
    spIssuer: sample.issuer.com
    metadataURL: sample.provider.com/metadata
saml:
    spIssuer: sample.issuer.com
    cert: |
    ssoURL: saml.provider.com
    idpIssuer: idp.issuer.com
userpki:
    certificateAuthorities: |
    certificate
openshift:
    enable: true
```

where:

`minimumRole`  
Specifies the minimum role that the system assigns by default to any user logging in. If left blank, the value is `None`.

`uiEndpoint`  
Specifies the user interface endpoint of your Central instance.

`extraUIEndpoints`  
Specifies whether your Central instance exposes different endpoints.

`groups`  
Specifies the specific roles to map users based on their attributes.

`groups.key`  
Specifies the key that can be any claim the authentication provider returns.

`groups.role`  
Specifies the role that the system gives to the users. You can use a default role or a declaratively-created role.

`requiredAttributes`  
Specifies whether the authentication provider requires the returned attributes, for example, if the audience limits to a specific organization or group. This is optional.

`claimMappings`  
Specifies whether to map the claims the identity provider returns to custom claims. This is optional.

`oidc`  
Specifies whether to configure the system to use OpenID Connect (OIDC) as an authentication method.

`oidc.issuer`  
Specifies the expected issuer for the token.

`oidc.mode`  
Specifies the OIDC callback mode. Possible values are `auto`, `post`, `query`, and `fragment`. The preferred value is `auto`.

`iap`  
Specifies whether to configure the system to use Google Identity-Aware Proxy (IAP) as an authentication method.

`saml`  
Specifies whether to configure the system to use Security Assertion Markup Language (SAML) 2.0 dynamic or static configuration as an authentication method.

`saml.cert`  
Specifies the certificate in Privacy Enhanced Mail (PEM) format.

`userpki.certificateAuthorities`  
Specifies whether to configure the system for authentication with user certificates.

`userpki.certificate`  
Specifies the certificate in PEM format.

`openshift`  
Specifies whether to configure the system for OpenShift Auth authentication providers.

<a id="declarative-config-example-short-lived-token_declarative-configuration-using"></a>

## Declarative configuration short-lived token example

Example YAML configuration for creating a short-lived token configuration by using declarative configuration.

``` yaml
issuer: https://token.actions.githubusercontent.com
type: GITHUB_ACTION
tokenExpirationDuration: 20m
mappings:
  - key: sub
    value: repos:stackrox:stackrox
    role: Analyst
```

where:

`issuer`  
Specifies the expected issuer for the token to exchange against a short-lived one.

`type`  
Specifies the configuration type. See "Configuring short-lived access" and "Integrating RHACS using short-lived access tokens" for more information.

`tokenExpirationDuration`  
Specifies the token lifetime in the **XhYmZs** format. The lifetime cannot be longer than 24 hours.

`mappings`  
Specifies the roles to which the system maps users, based on their attributes.

`mappings.key`  
Specifies that the key can be any claim the issuer returns.

`mappings.role`  
Specifies the role that the system gives to the users. You can use a default role or a declaratively-created one.

<div>

<div class="title">

Additional resources

</div>

- [Configuring short-lived access](../operating/manage-user-access/configure-short-lived-access.md#configure-short-lived-access_configure-short-lived-access)

- [Integrating RHACS using short-lived tokens](../integration/integrate-using-short-lived-tokens.md)

</div>

<a id="declarative-config-example-permission-set_declarative-configuration-using"></a>

## Declarative configuration permission set example

Example YAML configuration for creating a permission set by using declarative configuration.

``` yaml
name: A sample permission set
description: A sample permission set created declaratively
resources:
- resource: Integration
  access: READ_ACCESS
- resource: Administration
  access: READ_WRITE_ACCESS
```

where:

`resources.resource`  
Specifies a full list of supported resources. For more information, go to **Access Control** → **Permission Sets**.

`resources.access`  
Specifies that the access can be either `READ_ACCESS` or `READ_WRITE_ACCESS`.

<a id="declarative-config-example-access-scope_declarative-configuration-using"></a>

## Declarative configuration access scope example

Example YAML configuration for creating an access scope by using declarative configuration.

``` yaml
name: A sample access scope
description: A sample access scope created declaratively
rules:
    included:
        - cluster: secured-cluster-A
          namespaces:
            - namespaceA
        - cluster: secured-cluster-B
    clusterLabelSelectors:
        - requirements:
          - key: kubernetes.io/metadata.name
            operator: IN
            values:
            - production
            - staging
            - environment
```

where:

`rules.included.cluster`  
Specifies a cluster where the access scope includes only specific namespaces.

`rules.included.cluster`  
Specifies a cluster where the access scope includes all namespaces.

`rules.clusterLabelSelectors.requirements.operator`  
Specifies the Operator to use for the label selection. Valid values are `IN`, `NOT_IN`, `EXISTS`, and `NOT_EXISTS`.

<a id="declarative-config-example-role_declarative-configuration-using"></a>

## Declarative configuration role example

Example YAML configuration for creating a role by using declarative configuration.

``` yaml
name: A sample role
description: A sample role created declaratively
permissionSet: A sample permission set
accessScope: Unrestricted
```

where:

`permissionSet`  
Specifies the name of the permission set; can be either one of the system permission sets or a declaratively-created permission set.

`accessScope`  
Specifies the name of the access scope; can be either one of the system access scopes or a declaratively-created access scope.

<a id="declarative-configuration-troubleshooting_declarative-configuration-using"></a>

# Troubleshooting declarative configuration

You can use the error messages displayed in the **Declarative configuration** section of the **Platform Configuration** → **System Health** page to help in troubleshooting. The `roxctl declarative-config` command also includes a `lint` option to validate the configuration file and help you detect errors.

The error messages displayed in the **Declarative configuration** section of the **Platform Configuration** → **System Health** page give information about issues with declarative configurations. The following conditions can cause problems with declarative configurations:

- The format of the configuration file is not in valid YAML.

- The configuration file has invalid values, such as invalid access within a permission set.

- Invalid storage constraints exist, such as resource names are not unique or the configuration has invalid references to a resource.

To validate configuration files, check for errors in configuration files, and make sure that there are no invalid storage constraints when creating and updating configuration files, use the `roxctl declarative-config lint` command.

To troubleshoot a storage constraint during deletion, check if the system marked the resource as `Declarative Orphaned`. This indicates that someone deleted the declarative configuration that a resource referenced (for example, if someone deleted the declarative configuration for a permission set that a role referenced). To correct this error, edit the resource to point to a new permission set, or restore the deleted declarative configuration.

<a id="additional-resources_declarative-configuration-using"></a>

# Additional resources

- [Install Central using Helm charts with customizations (Red Hat OpenShift)](../installing/installing_ocp/install-central-ocp.md)

- [Install Central using Helm charts with customizations (other Kubernetes platforms)](../installing/installing_other/install-central-other.md)

- [Configuring short-lived access](../operating/manage-user-access/configure-short-lived-access.md#configure-short-lived-access_configure-short-lived-access)

- [Integrating RHACS using short-lived tokens](../integration/integrate-using-short-lived-tokens.md)
