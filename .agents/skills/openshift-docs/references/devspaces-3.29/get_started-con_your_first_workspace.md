> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/get_started-con_your_first_workspace). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Your first-day experience

OpenShift Dev Spaces creates a cloud development environment (CDE) for your project. The dashboard and CLI refer to each CDE as a **workspace**. Each cloud development environment runs as an OpenShift `DevWorkspace` custom resource on your cluster. You go from login to coding in about three minutes.

<span id="con_your-first-workspace_devspaces___from_url_to_code_in_four_steps"></span>

## [From URL to code in four steps](get_started-con_your_first_workspace.md#con_your-first-workspace_devspaces___from_url_to_code_in_four_steps)

When your administrator shares the OpenShift Dev Spaces dashboard URL, you go from login to coding in four steps:

1.  **Authenticate with OpenShift** — OpenShift Dev Spaces redirects you to the OpenShift OAuth login page. Enter your OpenShift credentials and authorize OpenShift Dev Spaces to access your account.
2.  **Create Workspace page** — After authentication, you land on the Create Workspace page. The page has two main sections:
    - **Git Repo URL** — A field where you paste the HTTPS or SSH URL of your Git repository.
    - **Select a Sample** — Pre-configured samples for languages and frameworks such as Java, Node.js, Python, and Go. Use these to explore OpenShift Dev Spaces without connecting your own repository.
3.  **Start your cloud development environment** — When you enter a Git URL and click **Create & Open**, OpenShift Dev Spaces asks you to confirm that you trust the repository authors, then provisions the cloud development environment.
4.  **IDE loads in your browser** — The default IDE, Microsoft Visual Studio Code - Open Source, opens in your browser tab with the repository already cloned.

<span id="con_your-first-workspace_devspaces___why_the_first_start_takes_longer"></span>

## [Why the first start takes longer](get_started-con_your_first_workspace.md#con_your-first-workspace_devspaces___why_the_first_start_takes_longer)

The first cloud development environment start takes approximately 2-3 minutes because OpenShift Dev Spaces pulls container images to the cluster node. The starting page displays real-time progress, including:

- Volume provisioning for persistent storage
- Container image pulls for the development tools and IDE
- Initialization of the project clone, home directory, and IDE server

Subsequent starts are faster because OpenShift caches the container images on the node. If your administrator has deployed the Image Puller, images are pre-cached across all nodes for near-instant starts.

Note

Administrators can reduce first-start times by pre-caching container images on cluster nodes.

<span id="con_your-first-workspace_devspaces___what_you_can_do_in_a_cloud_development_environment"></span>

## [What you can do in a cloud development environment](get_started-con_your_first_workspace.md#con_your-first-workspace_devspaces___what_you_can_do_in_a_cloud_development_environment)

A running cloud development environment provides:

Terminal  
A `bash` terminal in the IDE with your project directory as the working directory. The terminal prompt shows the current Git branch.

Git integration  
Your repository is cloned into the cloud development environment filesystem. If your administrator has configured OAuth for your Git provider, you can push commits without re-entering credentials.

Development tools  
The Universal Developer Image (UDI) includes compilers, runtimes, and build tools for common languages. Your project’s `devfile.yaml` can define additional tools and commands.

CDE URL  
Each cloud development environment has a unique URL in the format `https://`*`<openshift_dev_spaces_fqdn>`*`/`*`<user_name>`*`/`*`<workspace_name>`*`/`. Bookmark this URL to return to a running cloud development environment.

<span id="con_your-first-workspace_devspaces___troubleshoot_common_issues"></span>

## [Troubleshoot common issues](get_started-con_your_first_workspace.md#con_your-first-workspace_devspaces___troubleshoot_common_issues)

Cloud development environment fails to start with `OOMKilled` or `FailedScheduling`  
Your namespace exceeded its resource quota, or the cloud development environment requested more memory or CPU than the cluster allows. Contact your administrator to adjust resource limits.

Git push returns `401 Unauthorized` or `403 Forbidden`  
OAuth is not configured for your Git provider, or your token has expired. Configure authentication to resolve this issue.

Blank IDE with a `Could not register service workers` error  
This error occurs in Google Chrome Incognito mode or Mozilla Firefox Private Browsing mode. Use a regular browser window instead.

**Related concepts**  

- [Git server authentication from a workspace](get_started-con_authenticating_to_a_git_server_from_a_workspace.md "When you clone a private repository or push code from a cloud development environment, OpenShift Dev Spaces needs credentials to access your Git provider. Authentication can be configured at the platform level by your administrator or individually with a personal access token.")

**Related information**  

- [Speed up workspace starts with image caching](optimize-assembly_caching_images_for_faster_workspace_start.md)
