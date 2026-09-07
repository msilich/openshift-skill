> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_importing_untrusted_tls_certificates). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Trust custom TLS certificates for external services

Trust custom TLS certificate authority (CA) chains for external services in OpenShift Dev Spaces. This enables the server, dashboard, and workspaces to establish trusted encrypted connections to proxies, identity providers, and Git servers.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have the `openshift-devspaces` project created.
- You have the root CA and intermediate certificates for each CA chain to import, in [PEM](https://wiki.openssl.org/index.php/PEM) format, in a `ca-cert-for-devspaces-`*`<count>`*`.pem` file.

## About this task

OpenShift Dev Spaces uses labeled ConfigMaps in OpenShift Dev Spaces project as sources for TLS certificates. The ConfigMaps can have an arbitrary amount of keys with an arbitrary amount of certificates each. All certificates are mounted into:

- `/public-certs` location of OpenShift Dev Spaces server and dashboard pods
- `/etc/pki/ca-trust/extracted/pem` locations of workspaces pods

Configure the `CheCluster` Custom Resource to disable CA bundle mounting at `/etc/pki/ca-trust/extracted/pem`. The certificates are instead mounted at `/public-certs` to keep the behavior from the previous version.

Note

Configure the `CheCluster` Custom Resource to disable the mounting of the CA bundle under the path `/etc/pki/ca-trust/extracted/pem`. Certificates are mounted under the path `/public-certs` in this case.

``` yaml
spec:
  devEnvironments:
    trustedCerts:
      disableWorkspaceCaBundleMount: true
```

Important

On an OpenShift cluster, OpenShift Dev Spaces operator automatically adds Red Hat Enterprise Linux CoreOS (RHCOS) trust bundle into mounted certificates.

## Procedure

1.  Concatenate all CA chains PEM files to import, into the `custom-ca-certificates.pem` file, and remove the return character that is incompatible with the Java truststore.

    ``` bash
    $ cat ca-cert-for-devspaces-*.pem | tr -d '\r' > custom-ca-certificates.pem
    ```

2.  Create the `custom-ca-certificates` ConfigMap with the required TLS certificates:

    ``` bash
    $ oc create configmap custom-ca-certificates \
        --from-file=custom-ca-certificates.pem \
        --namespace=openshift-devspaces
    ```

3.  Label the `custom-ca-certificates` ConfigMap:

    ``` bash
    $ oc label configmap custom-ca-certificates \
        app.kubernetes.io/component=ca-bundle \
        app.kubernetes.io/part-of=che.eclipse.org \
        --namespace=openshift-devspaces
    ```

4.  Deploy OpenShift Dev Spaces if it has not been deployed before. Otherwise, wait until the rollout of OpenShift Dev Spaces components finishes.

5.  Restart running workspaces for the changes to take effect.

## Results

1.  Verify that the ConfigMap contains your custom CA certificates. This command returns CA bundle certificates in PEM format:

    ``` bash
    oc get configmap \
        --namespace=openshift-devspaces \
        --output='jsonpath={.items[0:].data.custom-ca-certificates\.pem}' \
        --selector=app.kubernetes.io/component=ca-bundle,app.kubernetes.io/part-of=che.eclipse.org
    ```

2.  Verify in the OpenShift Dev Spaces server logs that the imported certificates count is not null:

    ``` bash
    oc logs deploy/devspaces --namespace=openshift-devspaces \
        | grep tls-ca-bundle.pem
    ```

3.  Start a workspace, get the project name in which it has been created: *\<workspace_namespace\>*, and wait for the workspace to be started.

4.  Verify that the `ca-certs-merged` ConfigMap contains your custom CA certificates. This command returns OpenShift Dev Spaces CA bundle certificates in PEM format:

    ``` bash
    oc get configmap ca-certs-merged \
        --namespace=<workspace_namespace> \
        --output='jsonpath={.data.tls-ca-bundle\.pem}'
    ```

5.  Verify that the workspace pod mounts the `ca-certs-merged` ConfigMap:

    ``` bash
    oc get pod \
        --namespace=<workspace_namespace> \
        --selector='controller.devfile.io/devworkspace_name=<workspace_name>' \
        --output='jsonpath={.items[0:].spec.volumes[0:].configMap.name}' \
        | grep ca-certs-merged
    ```

6.  Get the workspace pod name *\<workspace_pod_name\>*:

    ``` bash
    oc get pod \
        --namespace=<workspace_namespace> \
        --selector='controller.devfile.io/devworkspace_name=<workspace_name>' \
        --output='jsonpath={.items[0:].metadata.name}'
    ```

7.  Verify that the workspace container has your custom CA certificates. This command returns OpenShift Dev Spaces CA bundle certificates in PEM format:

    ``` bash
    oc exec <workspace_pod_name> \
        --namespace=<workspace_namespace> \
        -- cat /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
    ```

    Or if `disableWorkspaceCaBundleMount` set to `true`:

    ``` bash
    oc exec <workspace_pod_name> \
        --namespace=<workspace_namespace> \
        -- cat /public-certs/tls-ca-bundle.pem
    ```

**Related information**  

- [Trust self-signed Git server certificates](configure-proc_git_with_self_signed_certificates.md)
