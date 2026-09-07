> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/plan-assembly_requirements). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Plan deployment resources

Plan the platform support, cluster capacity, scalability limits, and management tooling your team needs before you install OpenShift Dev Spaces.

- **[Supported platforms and architectures](plan-supported_platforms_ref.md)**  
  Confirm that your target cluster runs a supported OpenShift version and CPU architecture before starting the installation.
- **[Size your cluster for OpenShift Dev Spaces](plan-proc_calculating_resource_requirements.md)**  
  Size your cluster by calculating the CPU and memory requirements for the OpenShift Dev Spaces Operator, Dev Workspace Controller, and user workspaces so that your cluster can handle the expected number of concurrent users.
- **[Scalability limits and multi-cluster deployments](plan-con_running_at_scale.md)**  
  Scaling cloud development environments to thousands of concurrent workspaces strains etcd, Operator memory, and worker nodes. Review bottlenecks, tested maximums, and multi-cluster deployment patterns.
- **[Set up the dsc command-line tool](plan-proc_installing_the_dsc_management_tool.md)**  
  Set up `dsc` on Linux, macOS, or Windows so that you can deploy, update, and manage OpenShift Dev Spaces from the command line.
