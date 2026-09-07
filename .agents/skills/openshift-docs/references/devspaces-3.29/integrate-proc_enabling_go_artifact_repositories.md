> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_enabling_go_artifact_repositories). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set up Go to use your internal registry

Set up Go to use a module proxy by setting environment variables in your workspaces. .Prerequisites

## About this task

- You have an active `oc` session with your project. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You know the URL of your Go module proxy.

## Procedure

1.  Create a Secret to store the TLS certificate:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: tls-cert
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-secret: 'true'
      annotations:
        controller.devfile.io/mount-path: /home/user/certs
        controller.devfile.io/mount-as: file
    type: Opaque
    data:
      tls.cer: >-
        <Base64_encoded_TLS_certificate>
    ```

    where:

    ` `*`<Base64_encoded_TLS_certificate>`*` `  
    The Base64-encoded content of your Go module proxy’s TLS certificate.

2.  Apply the Secret to your project:

    ``` bash
    $ oc apply -f tls-cert.yaml -n <your_namespace>
    ```

3.  Create a ConfigMap with Go environment variables: Warning

    Applying a ConfigMap that sets environment variables might cause a workspace boot loop. If you encounter this behavior, remove the `ConfigMap` and edit the devfile directly.

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: go-config
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
      annotations:
        controller.devfile.io/mount-as: env
    data:
      GOPROXY: <your_go_proxy_url>
      GONOSUMDB: "*"
      GOPRIVATE: "<your_private_modules>"
      SSL_CERT_FILE: /home/user/certs/tls.cer
    ```

    where:

    ` `*`<your_go_proxy_url>`*` `  
    The URL of your internal Go module proxy.

    ` `*`<your_private_modules>`*` `  
    A comma-separated list of Go module path prefixes for private modules that bypass the proxy and checksum database.

4.  Apply the ConfigMap to your project:

    ``` bash
    $ oc apply -f go-config.yaml -n <your_namespace>
    ```

5.  Start or restart your workspace.

## Results

1.  Open a terminal in your workspace.

2.  Verify the Go configuration:

    ``` bash
    $ go env GOPROXY
    ```

3.  Download a Go module to verify the configuration:

    ``` bash
    $ go get github.com/gin-gonic/gin
    ```

**Related tasks**  

- [Set up Maven to use your internal registry](integrate-proc_enabling_maven_artifact_repositories.md "Set up Maven so that Java workspaces can resolve dependencies from your internal Nexus or Artifactory server. .Prerequisites")
- [Set up Gradle to use your internal registry](integrate-proc_enabling_gradle_artifact_repositories.md "Set up Gradle so that Gradle workspaces can download plugins and dependencies from your internal registry. .Prerequisites")
- [Set up npm to use your internal registry](integrate-proc_enabling_npm_artifact_repositories.md "Set up npm so that Node.js workspaces can install packages from your internal npm registry. .Prerequisites")
