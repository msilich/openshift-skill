<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To allow external clients to connect securely to applications under the .apps subdomain in OpenShift Container Platform, you can replace the default wildcard ingress certificate with one issued by a trusted public CA.

# Understanding the default ingress certificate

You can replace the default ingress certificate with a certificate from a public CA so that external clients connect securely to your applications.

The default ingress certificate in OpenShift Container Platform is a wildcard certificate that the Ingress Operator issues from an internal CA for the web console, CLI, and applications under the `.apps` subdomain.

# Replacing the default ingress certificate

To secure the web console, CLI, and all applications under the `.apps` subdomain in OpenShift Container Platform, you can replace the default ingress certificate by creating a TLS secret with your wildcard certificate and updating the Ingress Controller and cluster proxy configuration.

> [!NOTE]
> Before using the procedure, ensure you understand the following Ingress Controller behaviors:
>
> - When certificates are renewed or rotated by using external certificate management tools, only the contents of the secret, such as the certificate and key, are updated. The secret name remains unchanged. Kubelet automatically propagates these updates to the mounted volume, allowing the router to detect the file changes and hot-reload the new certificate and key. As a result, no rolling update of the router deployment is triggered or required.
>
> - For secret renewal or rotation, the cert-manager Operator changes the secret content, such as a cert/key pair, but does not change the secret name. This happens because kubelet automatically propagates changes to the secret in the volume mount. The router pod detects the file change and then hot reloads the new cert/key pair. Updating the secret content does not trigger rolling update.

<div>

<div class="title">

Prerequisites

</div>

- You must have a wildcard certificate for the fully qualified `.apps` subdomain and its corresponding private key. Each should be in a separate PEM format file.

- The private key must be unencrypted. If your key is encrypted, decrypt it before importing it into OpenShift Container Platform.

- The certificate must include the `subjectAltName` extension showing `*.apps.<clustername>.<domain>`.

- The certificate file can contain one or more certificates in a chain. The file must list the wildcard certificate as the first certificate, followed by other intermediate certificates, and then ending with the root CA certificate.

- Copy the root CA certificate into an additional PEM format file.

- Verify that all certificates which include `-----END CERTIFICATE-----` also end with one carriage return after that line.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a config map that includes only the root CA certificate that is used to sign the wildcard certificate:

    ``` terminal
    $ oc create configmap custom-ca \
         --from-file=ca-bundle.crt=</path/to/example-ca.crt> \
         -n openshift-config
    ```

    where

    `</path/to/example-ca.crt>`
    The path to the root CA certificate file on your local file system. For example, `/etc/pki/ca-trust/source/anchors`.

2.  Update the cluster-wide proxy configuration with the newly created config map:

    ``` terminal
    $ oc patch proxy/cluster \
         --type=merge \
         --patch='{"spec":{"trustedCA":{"name":"custom-ca"}}}'
    ```

    > [!NOTE]
    > If you update only the trusted CA for your cluster, the MCO updates the `/etc/pki/ca-trust/source/anchors/openshift-config-user-ca-bundle.crt` file and the Machine Config Controller (MCC) applies the trusted CA update to each node so that a node reboot is not required. However, with these changes, the Machine Config Daemon (MCD) restarts critical services on each node, such as kubelet and CRI-O. These service restarts cause each node to briefly enter the `NotReady` state until the service is fully restarted.
    >
    > If you change any other parameter in the `openshift-config-user-ca-bundle.crt` file, such as `noproxy`, the MCO reboots each node in your cluster.

3.  Create a secret that contains the wildcard certificate chain and key:

    ``` terminal
    $ oc create secret tls <secret> \
         --cert=</path/to/cert.crt> \
         --key=</path/to/cert.key> \
         -n openshift-ingress
    ```

    where:

    `<secret>`
    Specifies the name of the secret that will contain the certificate chain and private key.

    `</path/to/cert.crt>`
    Specifies the path to the certificate chain on your local file system.

    `</path/to/cert.key>`
    Specifies the path to the private key associated with this certificate.

4.  Update the Ingress Controller configuration with the newly created secret:

    ``` terminal
    $ oc patch ingresscontroller.operator default \
         --type=merge -p \
         '{"spec":{"defaultCertificate": {"name": "<secret>"}}}' \
         -n openshift-ingress-operator
    ```

    - `<secret>`:: Specifies the name used for the secret. Replace `<secret>` with the name used for the secret.

</div>

# Additional resources

- [Replacing the CA Bundle certificate](updating-ca-bundle.md#ca-bundle-understanding_updating-ca-bundle)

- [Proxy certificate customization](../certificate_types_descriptions/proxy-certificates.md#customization)
