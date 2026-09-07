> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-assembly_configuring_server_components). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Connect server components to enterprise systems

Connect OpenShift Dev Spaces server components to enterprise systems by injecting OpenShift Secrets and ConfigMaps into containers. Mount configuration files, credentials, and environment variables without modifying container images.

You can mount Secrets and ConfigMaps as files, as subpath volumes, or as environment variables. Each method requires specific annotations and labels on the OpenShift resource.

- **[Inject files from Secrets and ConfigMaps into containers](configure-proc_mounting_secret_configmap_as_file.md)**  
  Inject an OpenShift Secret or a ConfigMap as a file into an OpenShift Dev Spaces container to provide configuration files, certificates, or credentials without embedding them in the container image.
- **[Add individual files without replacing directories](configure-proc_mounting_secret_configmap_as_subpath.md)**  
  Add individual files from an OpenShift Secret or a ConfigMap to a target directory without replacing existing contents. Use a subPath mount when the target directory already contains files that must be preserved.
- **[Inject environment variables from Secrets and ConfigMaps](configure-proc_mounting_secret_configmap_as_env_variable.md)**  
  Inject configuration values from an OpenShift Secret or a ConfigMap as environment variables in an OpenShift Dev Spaces container, such as credentials, API keys, or feature flags, without modifying the container image.
- **[Fine-tune the server](configure-con_advanced_configuration_devspaces_server.md)**  
  Fine-tune the OpenShift Dev Spaces server by setting environment variables or overriding properties that are not exposed through the standard `CheCluster` Custom Resource fields.

**Related concepts**  

- [Customize the central configuration](configure-assembly_configuring_the_checluster_custom_resource.md "Customize OpenShift Dev Spaces behavior by editing the CheCluster Custom Resource (CR), the single configuration object that defines how your instance runs.")
