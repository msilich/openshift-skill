> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_reviewing_pull_and_merge_requests). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Review pull and merge requests

Review pull and merge requests in a Red Hat OpenShift Dev Spaces-supported web IDE with a ready-to-use workspace to run a linter, unit tests, the build, and more.

## Before you begin

- You have access to the repository hosted by your Git provider.
- You have access to an OpenShift Dev Spaces instance.

## Procedure

1.  Open the feature branch to review in OpenShift Dev Spaces. A clone of the branch opens in a workspace with tools for debugging and testing.
2.  Check the pull or merge request changes.
3.  Run your desired debugging and testing tools:
    - Run a linter.
    - Run unit tests.
    - Run the build.
    - Run the application to check for problems.
4.  Navigate to the UI of your Git provider to leave a comment and pull or merge your assigned request.

## Results

- Optional: Open a second workspace using the main branch of the repository to reproduce a problem.

**Related concepts**  

- [Try in Web IDE GitHub action](develop-con_try_in_web_ide_github_action.md "The Try in Web IDE GitHub action adds a factory URL to pull requests, enabling reviewers to quickly test changes in a Red Hat OpenShift Dev Spaces workspace.")

**Related tasks**  

- [Add a factory badge for first-time contributors](develop-proc_adding_factory_badge_for_contributors.md "Add a badge with a link to your OpenShift Dev Spaces instance to enable first-time contributors to start a workspace with a project.")
- [Add the action to a GitHub repository workflow](develop-proc_adding_try_in_web_ide_github_action.md "Add the Try in Web IDE GitHub action to a GitHub repository workflow so that contributors can quickly open pull requests in a ready-to-use cloud workspace.")
