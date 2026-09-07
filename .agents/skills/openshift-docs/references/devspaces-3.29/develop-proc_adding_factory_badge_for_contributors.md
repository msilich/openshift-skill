> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_adding_factory_badge_for_contributors). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Add a factory badge for first-time contributors

Add a badge with a link to your OpenShift Dev Spaces instance to enable first-time contributors to start a workspace with a project.

## Before you begin

- You have a running OpenShift Dev Spaces instance.
- You have a project repository hosted on a Git provider.

## About this task

<figure>
<br />
<img src="assets/98236222890cf3182590.svg" alt="Factory badge" /><br />

<figcaption>Figure 1. Factory badge</figcaption>
</figure>

## Procedure

Substitute your OpenShift Dev Spaces URL (`https://`*`<openshift_dev_spaces_fqdn>`*) and repository URL (*`<your_repository_url>`*), and add the link to your repository in the project `README.md` file.

``` plaintext
[![Contribute](https://www.eclipse.org/che/contribute.svg)](https://<openshift_dev_spaces_fqdn>/#https://<your_repository_url>)
```

## Results

- The `README.md` file in your Git provider web interface displays the ![Factory badge](assets/98236222890cf3182590.svg) factory badge. Click the badge to open a workspace with your project in your OpenShift Dev Spaces instance.

**Related concepts**  

- [Try in Web IDE GitHub action](develop-con_try_in_web_ide_github_action.md "The Try in Web IDE GitHub action adds a factory URL to pull requests, enabling reviewers to quickly test changes in a Red Hat OpenShift Dev Spaces workspace.")

**Related tasks**  

- [Review pull and merge requests](develop-proc_reviewing_pull_and_merge_requests.md "Review pull and merge requests in a Red Hat OpenShift Dev Spaces-supported web IDE with a ready-to-use workspace to run a linter, unit tests, the build, and more.")
- [Add the action to a GitHub repository workflow](develop-proc_adding_try_in_web_ide_github_action.md "Add the Try in Web IDE GitHub action to a GitHub repository workflow so that contributors can quickly open pull requests in a ready-to-use cloud workspace.")
