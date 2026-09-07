> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/discover-con_what_problems_devspaces_solves). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# What problems does OpenShift Dev Spaces solve?

OpenShift Dev Spaces solves six common development workflow problems by providing ready-to-code cloud workspaces from Git repositories. Developers open a URL and start coding within minutes.

<span id="con_what-problems-devspaces-solves_devspaces___environment_inconsistency"></span>

## [Environment inconsistency](discover-con_what_problems_devspaces_solves.md#con_what-problems-devspaces-solves_devspaces___environment_inconsistency)

When every developer configures their own local environment, differences in OS versions, tool versions, and dependencies cause "works on my machine" failures. OpenShift Dev Spaces uses devfiles, declarative YAML files that define the exact tools, runtimes, and dependencies for a project. Every developer who opens the same repository gets an identical environment.

<span id="con_what-problems-devspaces-solves_devspaces___slow_developer_onboarding"></span>

## [Slow developer onboarding](discover-con_what_problems_devspaces_solves.md#con_what-problems-devspaces-solves_devspaces___slow_developer_onboarding)

New team members must install tools, clone repositories, configure credentials, and troubleshoot build failures before writing their first line of code. With OpenShift Dev Spaces, a new developer opens the dashboard URL, pastes the team’s repository link, and has a fully configured workspace within minutes.

<span id="con_what-problems-devspaces-solves_devspaces___security_and_credential_management"></span>

## [Security and credential management](discover-con_what_problems_devspaces_solves.md#con_what-problems-devspaces-solves_devspaces___security_and_credential_management)

Local development environments store credentials on individual laptops. OpenShift Dev Spaces centralizes credential management through OAuth integration with Git providers and OpenShift RBAC. Developer tokens are stored as OpenShift Secrets on the cluster, not on individual machines.

<span id="con_what-problems-devspaces-solves_devspaces___environment_drift_over_time"></span>

## [Environment drift over time](discover-con_what_problems_devspaces_solves.md#con_what-problems-devspaces-solves_devspaces___environment_drift_over_time)

Even teams that start with consistent environments drift as developers install different extensions, update tools independently, or modify configurations. OpenShift Dev Spaces rebuilds the workspace container from the devfile on each start, so the base toolchain is always consistent. The `/home/user` directory persists across restarts by default, preserving personal preferences and shell history without affecting the standardized tools and runtimes.

<span id="con_what-problems-devspaces-solves_devspaces___resource_constraints_on_developer_laptops"></span>

## [Resource constraints on developer laptops](discover-con_what_problems_devspaces_solves.md#con_what-problems-devspaces-solves_devspaces___resource_constraints_on_developer_laptops)

Complex projects with multiple microservices, databases, and build tools can overwhelm laptop hardware. OpenShift Dev Spaces runs workspaces on cluster infrastructure with configurable CPU, memory, and storage limits. Developers get the resources they need without upgrading their hardware.

<span id="con_what-problems-devspaces-solves_devspaces___compliance_in_regulated_environments"></span>

## [Compliance in regulated environments](discover-con_what_problems_devspaces_solves.md#con_what-problems-devspaces-solves_devspaces___compliance_in_regulated_environments)

Organizations in regulated industries need to control where code is developed and how it is accessed. OpenShift Dev Spaces runs entirely within your OpenShift cluster and supports air-gapped environments with no internet access. In air-gapped deployments, all workspace traffic stays within your network boundary.
