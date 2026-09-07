> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_enabling_nuget_artifact_repositories). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set up NuGet to use your internal registry

Set up NuGet so that .NET workspaces can restore packages from your internal NuGet feed. .Prerequisites

## About this task

- You are not running any NuGet workspace. Warning

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
    The Base64-encoded content of your NuGet artifact repository’s public TLS certificate, with line wrapping disabled.

2.  Apply the Secret to your project:

    ``` bash
    $ oc apply -f tls-cer.yaml -n <your_namespace>
    ```

3.  Create a ConfigMap to set the `SSL_CERT_FILE` environment variable to the path of the TLS certificate:

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
      SSL_CERT_FILE: /home/user/certs/tls.cer
    ```

4.  Create a ConfigMap for the `nuget.config` file:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: init-nuget
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /projects
      labels:
        controller.devfile.io/mount-to-devworkspace: 'true'
        controller.devfile.io/watch-configmap: 'true'
    data:
      nuget.config: |
        <?xml version="1.0" encoding="UTF-8"?>
        <configuration>
          <packageSources>
            <add key="nexus2" value="https://<nuget_artifact_repository_route>/repository/nuget-group/"/>
          </packageSources>
          <packageSourceCredentials>
            <nexus2>
                <add key="Username" value="admin" />
                <add key="Password" value="passwd" />
            </nexus2>
          </packageSourceCredentials>
        </configuration>
    ```

    where:

    ` `*`<nuget_artifact_repository_route>`*` `  
    The hostname and path of your internal NuGet artifact repository.

5.  Apply both ConfigMaps to your project:

    ``` bash
    $ oc apply -f disconnected-env.yaml -n <your_namespace>
    $ oc apply -f init-nuget.yaml -n <your_namespace>
    ```

6.  Start a NuGet workspace.

## Results

1.  Open a terminal in your workspace.

2.  Verify the NuGet source configuration:

    ``` bash
    $ dotnet nuget list source
    ```

    The output includes the artifact repository URL from your `nuget.config` ConfigMap.

3.  Restore packages to verify artifact resolution from the mirror:

    ``` bash
    $ dotnet restore
    ```

**Related tasks**  

- [Set up Maven to use your internal registry](integrate-proc_enabling_maven_artifact_repositories.md "Set up Maven so that Java workspaces can resolve dependencies from your internal Nexus or Artifactory server. .Prerequisites")
- [Set up Gradle to use your internal registry](integrate-proc_enabling_gradle_artifact_repositories.md "Set up Gradle so that Gradle workspaces can download plugins and dependencies from your internal registry. .Prerequisites")
- [Set up npm to use your internal registry](integrate-proc_enabling_npm_artifact_repositories.md "Set up npm so that Node.js workspaces can install packages from your internal npm registry. .Prerequisites")
