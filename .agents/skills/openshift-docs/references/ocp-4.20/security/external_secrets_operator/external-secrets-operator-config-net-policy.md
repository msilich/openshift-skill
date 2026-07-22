<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The External Secrets Operator for Red Hat OpenShift for OpenShift Container Platform includes pre-defined `NetworkPolicies` for security that rejects all egress traffic and allows traffic towards services that are required for the operand functionality. You must configure additional custom policies to allow the `external-secrets` controller to egress traffic towards external providers. These configurable policies are set through the `ExternalSecretsConfig` custom resource to establish the egress allow policy.

# Adding a custom network policy to allow egress to all external providers

You must configure custom policies through the `ExternalSecretsConfig` custom resource to allow all egress to all external providers.

<div>

<div class="title">

Prerequisites

</div>

- An `ExternalSecretsConfig` must be predefined.

- You must be able to define specific egress rules, including destination ports and protocols.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `ExternalSecretsConfig` CR by running the following command:

    ``` terminal
    $ oc edit externalsecretsconfigs.operator.openshift.io cluster
    ```

2.  Set the policy by editing the `networkPolicies` section:

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ExternalSecretsConfig
    metadata:
      name: cluster
    spec:
      controllerConfig:
        networkPolicies:
          - name: allow-external-secrets-egress
            componentName: CoreController
            egress: # Allow all egress traffic
    ```

</div>

# Adding a custom network policy to allow egress to a specific provider

You must configure custom policies through the `ExternalSecretsConfig` custom resource to allow all egress to a specific provider.

<div>

<div class="title">

Prerequisites

</div>

- An `ExternalSecretsConfig` must be predefined.

- You must be able to define specific egress rules, including destination ports and protocols

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `ExternalSecretsConfig` CR by running the following command:

    ``` terminal
    $ oc edit externalsecretsconfigs.operator.openshift.io cluster
    ```

2.  Set the policy by editing the `networkPolicies` section. The following example shows how to allow egress to Amazon Web Services (AWS) endpoints.

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: ExternalSecretsConfig
    metadata:
      name: cluster
    spec:
      controllerConfig:
        networkPolicies:
          - componentName: ExternalSecretsCoreController
            egress:
              # Allow egress to Kubernetes API server, AWS endpoints, and DNS
              - ports:
                  - port: 443   # HTTPS (AWS Secrets Manager)
                    protocol: TCP
          - name: allow-external-secrets-egress
    ```

    where:

    componentName
    Specifies the name for the core controller which is `ExternalSecretsCoreController`. Egress rules must specify the required ports, such as Transmission Control Protocol (TCP) port 443, for services such as the AWS Secrets Manager.

</div>

# Default ingress and egress rules

The ingress and egress rules are necessary to build a secure setup where every component acts with the least amount of privilege necessary. These rules protect your cluster by strictly blocking unnecessary traffic and only allowing the outbound connections needed to fetch secrets. They also permit the specific inbound connections required to validate webhooks and observe system performance.

The following table summarizes the specific ports and protocols used by each component.

| Component | Ingress ports | Egress ports | Description |
|----|----|----|----|
| `external-secrets` | 8080 | 6443 | Allows retrieving metrics and interacting with the API server |
| `external-secrets-webhook` | 8080/10250 | 6443 | Allows retrieving metrics, handling webhook requests, and interacting with the API server |
| `external-secrets-cert-controller` | 8080 | 6443 | Allows retrieving metrics and interacting with the API server |
| `external-secrets-bitwarden-server` | 9998 | 6443 | Handles Bitwarden server connections and interacts with the API server |
| `external-secrets-allow-dns` |  | 5353 | Enables DNS lookups to find external secret providers. |
