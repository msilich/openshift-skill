> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/plan-proc_installing_the_dsc_management_tool). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Set up the dsc command-line tool

Set up `dsc` on Linux, macOS, or Windows so that you can deploy, update, and manage OpenShift Dev Spaces from the command line.

## Before you begin

- You have a Linux or macOS workstation. Note

  For installing `dsc` on Windows, see the following pages:

  - <https://developers.redhat.com/products/openshift-dev-spaces/download>
  - <https://github.com/redhat-developer/devspaces-chectl>

## Procedure

1.  Download the archive from <https://developers.redhat.com/products/openshift-dev-spaces/download> to a directory such as `$HOME`.
2.  Run `tar xvzf` on the archive to extract the `/dsc` directory.
3.  Add the extracted `/dsc/bin` subdirectory to `$PATH`.

## Results

- Run `dsc` to view information about it.

  ``` bash
  $ dsc
  ```

**Related information**  

- [dsc reference documentation](https://github.com/redhat-developer/devspaces-chectl)
