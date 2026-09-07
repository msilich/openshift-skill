> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/get_started-assembly_start_your_first_workspace). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create your first cloud workspace

When you receive the OpenShift Dev Spaces URL from your administrator, create a cloud workspace to start coding on your project without installing any tools locally. OpenShift Dev Spaces clones your repository, provisions development tools, and opens the IDE in your browser.

- **[Your first-day experience](get_started-con_your_first_workspace.md)**  
  OpenShift Dev Spaces creates a cloud development environment (CDE) for your project. The dashboard and CLI refer to each CDE as a **workspace**. Each cloud development environment runs as an OpenShift `DevWorkspace` custom resource on your cluster. You go from login to coding in about three minutes.
- **[Open your project in a cloud development environment](get_started-proc_starting_a_workspace_from_a_git_repository_url.md)**  
  Open your team’s Git repository in a cloud development environment so that you can start coding without installing tools, cloning repositories, or configuring your local environment. OpenShift Dev Spaces handles all of this automatically.
- **[Manage your cloud development environments](get_started-ref_basic_actions_on_a_workspace.md)**  
  Stop, restart, and delete cloud development environments from the OpenShift Dev Spaces dashboard to control resource usage and keep your environment organized. Access the **Workspaces** page at `https://`*`<openshift_dev_spaces_fqdn>`*`/dashboard/#/workspaces`.

**Related concepts**  

- [Connect to your Git repositories](get_started-assembly_authenticate_to_git_servers.md "Connect to your Git provider to push code, clone private repositories, and collaborate with your team from OpenShift Dev Spaces workspaces. Your administrator configures OAuth at the platform level for credential-free access, or you can use a personal access token when OAuth is not available.")

**Related information**  

- [Develop with OpenShift Dev Spaces](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop/index#develop_develop)
