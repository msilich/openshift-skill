> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-assembly_connecting_package_registries). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Resolve dependencies in restricted environments

Resolve build dependencies in restricted or air-gapped environments by connecting OpenShift Dev Spaces workspaces to your organization’s internal package registries for Maven, Gradle, npm, Python, Go, and NuGet.

Configure each language ecosystem by mounting ConfigMaps or Secrets with the appropriate configuration files into workspaces.

- **[Set up Maven to use your internal registry](integrate-proc_enabling_maven_artifact_repositories.md)**  
  Set up Maven so that Java workspaces can resolve dependencies from your internal Nexus or Artifactory server. .Prerequisites
- **[Set up Gradle to use your internal registry](integrate-proc_enabling_gradle_artifact_repositories.md)**  
  Set up Gradle so that Gradle workspaces can download plugins and dependencies from your internal registry. .Prerequisites
- **[Set up npm to use your internal registry](integrate-proc_enabling_npm_artifact_repositories.md)**  
  Set up npm so that Node.js workspaces can install packages from your internal npm registry. .Prerequisites
- **[Set up Python to use your internal registry](integrate-proc_enabling_python_artifact_repositories.md)**  
  Set up pip to use an internal PyPI mirror by mounting a `pip.conf` file into your workspaces. .Prerequisites
- **[Set up Go to use your internal registry](integrate-proc_enabling_go_artifact_repositories.md)**  
  Set up Go to use a module proxy by setting environment variables in your workspaces. .Prerequisites
- **[Set up NuGet to use your internal registry](integrate-proc_enabling_nuget_artifact_repositories.md)**  
  Set up NuGet so that .NET workspaces can restore packages from your internal NuGet feed. .Prerequisites

**Related information**  

- [Trust custom TLS certificates for external services](configure-proc_importing_untrusted_tls_certificates.md)
