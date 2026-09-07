> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_enabling_npm_artifact_repositories). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set up npm to use your internal registry

Set up npm so that Node.js workspaces can install packages from your internal npm registry. .Prerequisites

## About this task

- You are not running any npm workspace. Warning

  Applying a ConfigMap that sets environment variables might cause a workspace boot loop.

  If you encounter this behavior, remove the `ConfigMap` and edit the devfile directly.

## Procedure

1.  Create a Secret to store the TLS certificate:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: tls-cer
      annotations:
        controller.devfile.io/mount-path: /public-certs
        controller.devfile.io/mount-as: file
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-secret: 'true'
    data:
      nexus.cer: >-
        <Base64_encoded_content_of_public_cert>
    ```

    where:

    ` `*`<Base64_encoded_content_of_public_cert>`*` `  
    The Base64-encoded content of your npm artifact repository’s public TLS certificate, with line wrapping disabled.

2.  Apply the Secret to your project:

    ``` bash
    $ oc apply -f tls-cer.yaml -n <your_namespace>
    ```

3.  Create a ConfigMap to set the `NPM_CONFIG_REGISTRY` environment variable:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: disconnected-env
      annotations:
        controller.devfile.io/mount-as: env
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
    data:
      NPM_CONFIG_REGISTRY: >-
        https://<npm_artifact_repository_route>/repository/npm-all/
    ```

    where:

    ` `*`<npm_artifact_repository_route>`*` `  
    The hostname and path of your internal npm artifact repository.

4.  Apply the ConfigMap to your project:

    ``` bash
    $ oc apply -f disconnected-env.yaml -n <your_namespace>
    ```

5.  Start a npm workspace.

6.  Configure the workspace to trust the self-signed certificate by using one of the following options:
    1.  Set the `NODE_EXTRA_CA_CERTS` environment variable to the path of the TLS certificate:

        ``` bash
        $ export NODE_EXTRA_CA_CERTS=/public-certs/nexus.cer
        $ npm install
        ```

    2.  Alternatively, disable self-signed certificate validation:

        ``` bash
        $ npm config set strict-ssl false
        ```

        Warning

        Disabling SSL/TLS bypasses the validation of your self-signed certificates. For a more secure solution, use `NODE_EXTRA_CA_CERTS` (sub-step a).

## Results

1.  Open a terminal in your workspace.

2.  Verify the npm registry configuration:

    ``` bash
    $ npm config get registry
    ```

    The output shows the artifact repository URL from your ConfigMap.

3.  Install a package to verify artifact resolution from the mirror:

    ``` bash
    $ npm install express
    ```

**Related tasks**  

- [Set up Maven to use your internal registry](integrate-proc_enabling_maven_artifact_repositories.md "Set up Maven so that Java workspaces can resolve dependencies from your internal Nexus or Artifactory server. .Prerequisites")
- [Set up Gradle to use your internal registry](integrate-proc_enabling_gradle_artifact_repositories.md "Set up Gradle so that Gradle workspaces can download plugins and dependencies from your internal registry. .Prerequisites")
- [Set up Python to use your internal registry](integrate-proc_enabling_python_artifact_repositories.md "Set up pip to use an internal PyPI mirror by mounting a pip.conf file into your workspaces. .Prerequisites")
