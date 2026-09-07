> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_git_with_self_signed_certificates). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Trust self-signed Git server certificates

Trust self-signed certificates from Git providers by configuring OpenShift Dev Spaces so that workspaces can clone and push to repositories secured by internal certificate authorities.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have Git version 2 or later installed.

## Procedure

1.  Create a new **ConfigMap** with details about the Git server:

    ``` bash
    $ oc create configmap che-git-self-signed-cert \
      --from-file=ca.crt=<path_to_certificate> \
      --from-literal=githost=<git_server_url> -n openshift-devspaces
    ```

    where:

    `--from-file`  
    Path to the self-signed certificate.

    `--from-literal`  
    Optional parameter to specify the Git server URL for example `https://git.example.com:8443`. When omitted, the self-signed certificate is used for all repositories over HTTPS.

    Note

    - Certificate files are typically stored as Base64 ASCII files, such as. `.pem`, `.crt`, `.ca-bundle`. All `ConfigMaps` that hold certificate files should use the Base64 ASCII certificate rather than the binary data certificate.
    - A certificate chain of trust is required. If the `ca.crt` is signed by a certificate authority (CA), the CA certificate must be included in the `ca.crt` file.

2.  Add the required labels to the ConfigMap:

    ``` bash
    $ oc label configmap che-git-self-signed-cert \
      app.kubernetes.io/part-of=che.eclipse.org -n openshift-devspaces
    ```

3.  Edit the `CheCluster` Custom Resource on the cluster:

    ``` bash
    $ oc edit checluster/devspaces -n openshift-devspaces
    ```

    ``` yaml
    spec:
      devEnvironments:
        trustedCerts:
          gitTrustedCertsConfigMapName: che-git-self-signed-cert
    ```

## Results

- Create and start a new workspace. Every container used by the workspace mounts a special volume that contains a file with the self-signed certificate. The container's `/etc/gitconfig` file contains information about the Git server host (its URL) and the path to the certificate in the `http` section (see Git documentation about [git-config](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslCAInfo)).

  For example:

  ``` plaintext
  [http "https://10.33.177.118:3000"]
  sslCAInfo = /etc/config/che-git-tls-creds/certificate
  ```

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
- [Trust custom TLS certificates for external services](configure-proc_importing_untrusted_tls_certificates.md)
