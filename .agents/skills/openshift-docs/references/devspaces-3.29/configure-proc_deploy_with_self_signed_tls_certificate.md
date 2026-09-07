> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_deploy_with_self_signed_tls_certificate). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy with a self-signed TLS certificate

Deploy OpenShift Dev Spaces with a custom self-signed TLS certificate instead of the automatically generated one. By default, `dsc` creates an OpenShift Job to generate a self-signed certificate automatically.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- Generated certificate and private key files.

## Procedure

1.  Pre-create a project for OpenShift Dev Spaces:

    ``` bash
    $ oc create project openshift-devspaces
    ```

2.  Create a `che-tls` secret, replacing *\<key_file\>* with the path to your private key in PEM format and *\<cert_file\>* with the path to your public key certificate in PEM format:

    ``` bash
    $ oc create secret tls che-tls \
    --key <key_file> \
    --cert <cert_file> \
    -n openshift-devspaces
    ```

3.  Add the required labels to the secret:

    ``` bash
    $ oc label secret che-tls app.kubernetes.io/part-of=che.eclipse.org -n openshift-devspaces
    ```

4.  Create a `self-signed-certificate` secret, replacing *\<certificate_chain_of_trust_file\>* with the path to your certificate chain of trust in PEM format:

    ``` bash
    $ oc create secret generic self-signed-certificate \
    --from-file=ca.crt=<certificate_chain_of_trust_file> \
    -n openshift-devspaces
    ```

5.  Add the required labels to the secret:

    ``` bash
    $ oc label secret self-signed-certificate app.kubernetes.io/part-of=che.eclipse.org -n openshift-devspaces
    ```

**Related information**  

- [Deploy OpenShift Dev Spaces on OpenShift using CLI](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/install_openshift_dev_spaces/index#proc_installing-devspaces-on-openshift-using-cli_installation_guide)
