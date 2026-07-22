<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If a cluster-wide egress proxy is configured in OpenShift Container Platform, the Operator Lifecycle Manager (OLM) automatically configures Operators that it manages with the cluster-wide proxy. OLM automatically updates all of the Operator deployments with the `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` environment variables.

# Configuring the egress proxy for the External Secrets Operator for Red Hat OpenShift

The egress proxy can be configured in the `ExternalSecretsConfig` or the `ExternalSecretsManager` custom resource (CR). The Operator and the operand make use of the OpenShift Container Platform supported certificate authority (CA) bundle for the proxy validations.

The Operator can automatically create and manage a `NetworkPolicy` such as `eso-sys-allow-proxy-egress`, that allows all `external-secrets` pods to reach the proxy server. You control this behavior by using the `networkPolicyProvisioning` field. The field can be set in either the `ExternalSecretsConfig` CR or the `ExternalSecretsManager` CR, and can be configured independently of proxy URL fields. For example, when the proxy is provided by Operator Lifecycle Manager (OLM) environment variables at the cluster level, you can set only `networkPolicyProvisioning` in either CR without specifying any proxy URLs.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have created the `ExternalSecretsConfig` custom CR.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To set the proxy in the `ExternalSecretsConfig` resource, perform the following steps:

    1.  Edit the `ExternalSecretsConfig` resource by running the following command:

        ``` terminal
        $ oc edit externalsecretsconfigs.operator.openshift.io cluster
        ```

    2.  Edit the `spec.appConfig.proxy` section to set the proxy values as follows:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: ExternalSecretsConfig
        ...
        spec:
          appConfig:
            proxy:
              httpProxy: <http_proxy>
              httpsProxy: <https_proxy>
              noProxy: <no_proxy>
              networkPolicyProvisioning: Managed
        ```

        where:

        `spec.appConfig.proxy.httpProxy`
        Specifies the proxy URL for the HTTP requests.

        `spec.appConfig.proxy.httpsProxy`
        Specifies the proxy URL for the HTTPS requests.

        `spec.appConfig.proxy.noProxy`
        Specifies a comma-separated list of hostnames, CIDRs, IPs or a combination of these, for which the proxy should not be used.

        `spec.appConfig.proxy.networkPolicyProvisioning`
        Specifies whether the Operator automatically creates and manages the `eso-sys-allow-proxy-egress` `NetworkPolicy`. Accepted values are `Managed`, which is the default, and `Unmanaged`. When set to `Managed`, the Operator creates the policy based on the proxy URL port and deletes it when the proxy is removed. When set to `Unmanaged`, the Operator does not create or delete the policy and you are responsible for managing proxy egress traffic.

2.  To set the proxy in the `ExternalSecretsManager` CR, perform the following steps:

    1.  Edit the `ExternalSecretsManager` CR by running the following command:

        ``` terminal
        $ oc edit externalsecretsmanagers.operator.openshift.io cluster
        ```

    2.  Edit the `spec.globalConfig.proxy` section to set the proxy values as follows:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: ExternalSecretsManager
        ...
        spec:
          globalConfig:
            proxy:
              httpProxy: <http_proxy>
              httpsProxy: <https_proxy>
              noProxy: <no_proxy>
              networkPolicyProvisioning: Managed
        ```

        where:

        `spec.appConfig.proxy.httpProxy`
        Specifies the proxy URL for the HTTP requests.

        `spec.appConfig.proxy.httpsProxy`
        Specifies the proxy URL for the HTTPS requests.

        `spec.appConfig.proxy.noProxy`
        Specifies a comma-separated list of hostnames, CIDRs, IPs or a combination of these, for which the proxy should not be used.

        `spec.appConfig.proxy.networkPolicyProvisioning`
        Specifies whether the Operator automatically creates and manages the `eso-sys-allow-proxy-egress` `NetworkPolicy`. The values are\`Managed\`, which is the default, and `Unmanaged`.

        > [!NOTE]
        > When `networkPolicyProvisioning` is set in both the `ExternalSecretsConfig` CR and the `ExternalSecretsManager` CR, the value in the `ExternalSecretsConfig` CR takes precedence.

3.  If the proxy is configured at the cluster level through OLM environment variables and you only want to control `NetworkPolicy` provisioning without specifying proxy URLs in a CR, set only the `networkPolicyProvisioning` field in either CR as follows:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ExternalSecretsConfig
    ...
    spec:
      applicationConfig:
        proxy:
          networkPolicyProvisioning: Unmanaged
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the proxy egress `NetworkPolicy` was created by running the following command:

    ``` terminal
    $ oc get networkpolicy eso-sys-allow-proxy-egress -n external-secrets -o yaml
    ```

    The policy should show an egress rule allowing transmission control protocol (TCP) traffic on the port derived from the configured proxy URL.

2.  Verify that the proxy configuration is applied to the `external-secrets` deployment by running the following command:

    ``` terminal
    $ oc set env deployment/external-secrets -n external-secrets --list | grep -i proxy
    ```

</div>

# Additional resources

- [Configuring proxy support in Operator Lifecycle Manager](../../operators/admin/olm-configuring-proxy-support.md#olm-configuring-proxy-support)
