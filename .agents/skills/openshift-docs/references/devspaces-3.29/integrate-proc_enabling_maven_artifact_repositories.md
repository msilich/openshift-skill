> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_enabling_maven_artifact_repositories). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set up Maven to use your internal registry

Set up Maven so that Java workspaces can resolve dependencies from your internal Nexus or Artifactory server. .Prerequisites

## About this task

- You are not running any Maven workspace.
- You know your user namespace, which is *`<username>`*`-devspaces` where *`<username>`* is your OpenShift Dev Spaces username.

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
    The Base64-encoded content of your Maven artifact repository’s public TLS certificate, with line wrapping disabled.

2.  Apply the Secret to the *`<username>`*`-devspaces` namespace:

    ``` bash
    $ oc apply -f tls-cer.yaml -n <username>-devspaces
    ```

3.  Create a ConfigMap for the `settings.xml` file:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: settings-xml
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /home/user/.m2
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
    data:
      settings.xml: |
        <settings xmlns="http://maven.apache.org/SETTINGS/1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 https://maven.apache.org/xsd/settings-1.0.0.xsd">
          <localRepository/>
          <interactiveMode/>
          <offline/>
          <pluginGroups/>
          <servers/>
          <mirrors>
            <mirror>
              <id>redhat-ga-mirror</id>
              <name>Red Hat GA</name>
              <url>https://<maven_artifact_repository_route>/repository/redhat-ga/</url>
              <mirrorOf>redhat-ga</mirrorOf>
            </mirror>
            <mirror>
              <id>maven-central-mirror</id>
              <name>Maven Central</name>
              <url>https://<maven_artifact_repository_route>/repository/maven-central/</url>
              <mirrorOf>maven-central</mirrorOf>
            </mirror>
            <mirror>
              <id>jboss-public-repository-mirror</id>
              <name>JBoss Public Maven Repository</name>
              <url>https://<maven_artifact_repository_route>/repository/jboss-public/</url>
              <mirrorOf>jboss-public-repository</mirrorOf>
            </mirror>
          </mirrors>
          <proxies/>
          <profiles/>
          <activeProfiles/>
        </settings>
    ```

    where:

    ` `*`<maven_artifact_repository_route>`*` `  
    The hostname and path of your internal Maven artifact repository.

4.  Optional: When using JBoss EAP-based devfiles, create a second `settings-xml` ConfigMap with a different name and the `/home/jboss/.m2` mount path. Use the same content as step 3.

5.  Create a ConfigMap for the TrustStore initialization script that matches your Java version:

    For Java 8:

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
      init-java8-truststore.sh: |
        #!/usr/bin/env bash

        keytool -importcert -noprompt -file /home/user/certs/tls.cer -trustcacerts -keystore ~/.java/current/jre/lib/security/cacerts -storepass changeit
    ```

    For Java 11:

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
      init-java11-truststore.sh: |
        #!/usr/bin/env bash

        keytool -importcert -noprompt -file /home/user/certs/tls.cer -cacerts -storepass changeit
    ```

6.  Apply the Secret, `settings.xml` ConfigMap, and TrustStore ConfigMap to the *`<username>`*`-devspaces` namespace:

    ``` bash
    $ oc apply -f tls-cer.yaml -n <username>-devspaces
    $ oc apply -f settings-xml.yaml -n <username>-devspaces
    $ oc apply -f init-truststore.yaml -n <username>-devspaces
    ```

7.  Start a Maven workspace.

8.  Open a new terminal in the `tools` container.

9.  Run `~/init-truststore.sh`.

## Results

1.  In the workspace terminal, verify the Maven mirror configuration:

    ``` bash
    $ mvn help:effective-settings
    ```

    The output includes the mirror URLs from your `settings.xml` ConfigMap.

2.  Build a Maven project to verify artifact resolution from the mirror:

    ``` bash
    $ mvn package
    ```

**Related tasks**  

- [Set up Gradle to use your internal registry](integrate-proc_enabling_gradle_artifact_repositories.md "Set up Gradle so that Gradle workspaces can download plugins and dependencies from your internal registry. .Prerequisites")
- [Set up npm to use your internal registry](integrate-proc_enabling_npm_artifact_repositories.md "Set up npm so that Node.js workspaces can install packages from your internal npm registry. .Prerequisites")
- [Set up Python to use your internal registry](integrate-proc_enabling_python_artifact_repositories.md "Set up pip to use an internal PyPI mirror by mounting a pip.conf file into your workspaces. .Prerequisites")
