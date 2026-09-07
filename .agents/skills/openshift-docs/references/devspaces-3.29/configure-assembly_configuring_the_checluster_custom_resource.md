> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-assembly_configuring_the_checluster_custom_resource). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Customize the central configuration

Customize OpenShift Dev Spaces behavior by editing the `CheCluster` Custom Resource (CR), the single configuration object that defines how your instance runs.

The `CheCluster` CR is the central configuration object for OpenShift Dev Spaces. You can set fields during installation with `dsc` flags or modify them at any time afterward with `oc`. For instructions on configuring the CheCluster during installation, see Additional resources.

- **[How the central configuration works](configure-con_understanding_the_checluster_custom_resource.md)**  
  Understand how OpenShift Dev Spaces behavior is controlled through the `CheCluster` Custom Resource, the single configuration object parameterized by the Red Hat OpenShift Dev Spaces Operator.
- **[Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)**  
  Edit the `CheCluster` Custom Resource YAML file to customize the behavior of a running OpenShift Dev Spaces instance for your environment.

**Related information**  

- [Configure the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
