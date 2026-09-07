> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_adding_try_in_web_ide_github_action). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Add the action to a GitHub repository workflow

Add the Try in Web IDE GitHub action to a GitHub repository workflow so that contributors can quickly open pull requests in a ready-to-use cloud workspace.

## Before you begin

- You have a GitHub repository.
- You have a devfile in the root of the GitHub repository.

## Procedure

1.  In the GitHub repository, create a `.github/workflows` directory if it does not exist already.

2.  Create an `example.yml` file in the `.github/workflows` directory with the following content:

    ``` yaml
    name: Try in Web IDE example

    on:
      pull_request_target:
        types: [opened]

    jobs:
      add-link:
        runs-on: ubuntu-20.04
        steps:
          - name: Web IDE Pull Request Check
            id: try-in-web-ide
            uses: redhat-actions/try-in-web-ide@v1
            with:
              # GitHub action inputs

              # required
              github_token: ${{ secrets.GITHUB_TOKEN }}

              # optional - defaults to true
              add_comment: true

              # optional - defaults to true
              add_status: true
    ```

    This code snippet creates a workflow named `Try in Web IDE example`, with a job that runs the `v1` version of the `redhat-actions/try-in-web-ide` community action. The workflow is triggered on the [`pull_request_target` event](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows), on the `opened` activity type.

3.  Optional: Configure the activity types from the `on.pull_request_target.types` field to customize when the workflow triggers. Activity types such as `reopened` and `synchronize` can be useful.

    For example:

    ``` yaml
    on:
      pull_request_target:
        types: [opened, synchronize]
    ```

4.  Optional: Configure the `add_comment` and `add_status` GitHub action inputs within `example.yml`. These inputs customize whether comments and status checks are added.

**Related concepts**  

- [Try in Web IDE GitHub action](develop-con_try_in_web_ide_github_action.md "The Try in Web IDE GitHub action adds a factory URL to pull requests, enabling reviewers to quickly test changes in a Red Hat OpenShift Dev Spaces workspace.")
