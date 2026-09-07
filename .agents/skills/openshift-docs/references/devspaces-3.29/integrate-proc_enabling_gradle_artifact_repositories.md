> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_enabling_gradle_artifact_repositories). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set up Gradle to use your internal registry

Set up Gradle so that Gradle workspaces can download plugins and dependencies from your internal registry. .Prerequisites

## About this task

- You are not running any Gradle workspace.

## Procedure

1.  Create a Secret to store the TLS certificate:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: tls-cer
      annotations:
        controller.devfile.io/mount-path: /home/user/certs
        controller.devfile.io/mount-as: file
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-secret: 'true'
    data:
      tls.cer: >-
        <Base64_encoded_content_of_public_cert>
    ```

    where:

    ` `*`<Base64_encoded_content_of_public_cert>`*` `  
    The Base64-encoded content of your Gradle artifact repository’s public TLS certificate, with line wrapping disabled.

2.  Create a ConfigMap for the TrustStore initialization script:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: init-truststore
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /home/user/
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
    data:
      init-truststore.sh: |
        #!/usr/bin/env bash

        keytool -importcert -noprompt -file /home/user/certs/tls.cer -cacerts -storepass changeit
    ```

3.  Create a ConfigMap for the Gradle init script:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: init-gradle
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /home/user/.gradle
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
    data:
      init.gradle: |
        allprojects {
          repositories {
            mavenLocal ()
            maven {
              url "https://<gradle_artifact_repository_route>/repository/maven-public/"
              credentials {
                username "admin"
                password "passwd"
              }
            }
          }
        }
    ```

    where:

    ` `*`<gradle_artifact_repository_route>`*` `  
    The hostname and path of your internal Gradle artifact repository.

4.  Apply the Secret and both ConfigMaps to your project:

    ``` bash
    $ oc apply -f tls-cer.yaml -n <your_namespace>
    $ oc apply -f init-truststore.yaml -n <your_namespace>
    $ oc apply -f init-gradle.yaml -n <your_namespace>
    ```

5.  Start a Gradle workspace.

6.  Open a new terminal in the `tools` container.

7.  Run `~/init-truststore.sh`.

## Results

1.  In the workspace terminal, build a Gradle project to verify artifact resolution from the mirror:

    ``` bash
    $ gradle build
    ```

**Related tasks**  

- [Set up Maven to use your internal registry](integrate-proc_enabling_maven_artifact_repositories.md "Set up Maven so that Java workspaces can resolve dependencies from your internal Nexus or Artifactory server. .Prerequisites")
- [Set up npm to use your internal registry](integrate-proc_enabling_npm_artifact_repositories.md "Set up npm so that Node.js workspaces can install packages from your internal npm registry. .Prerequisites")
- [Set up Python to use your internal registry](integrate-proc_enabling_python_artifact_repositories.md "Set up pip to use an internal PyPI mirror by mounting a pip.conf file into your workspaces. .Prerequisites")
