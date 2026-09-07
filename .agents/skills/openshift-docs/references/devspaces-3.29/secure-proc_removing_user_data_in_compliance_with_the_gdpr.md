> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/secure-proc_removing_user_data_in_compliance_with_the_gdpr). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Remove user data for GDPR compliance

Remove a user’s data from OpenShift Container Platform when a developer leaves your organization, to comply with the [General Data Protection Regulation (GDPR)](https://gdpr.eu/). The process for other Kubernetes infrastructures might vary.

## Before you begin

- You have an active `oc` session with administrative permissions for the OpenShift Container Platform cluster. See [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

Warning

Removing user data as follows is irreversible. All removed data is deleted and unrecoverable.

## Procedure

1.  List all the users in the OpenShift cluster using the following command:

    ``` bash
    $ oc get users
    ```

2.  Delete the user entry: Important

    If the user has any associated resources (such as projects, roles, or service accounts), you must delete those first before deleting the user.

    ``` bash
    $ oc delete user <username>
    ```

## Results

- Verify the user no longer appears in the cluster:

  ``` bash
  $ oc get users
  ```

**Related information**  

- [Using the Dev Spaces server API](configure-proc_using_devspaces_server_api.md)
- [Configure project name](configure-proc_configuring_project_name.md)
- [Uninstalling OpenShift Dev Spaces](install-proc_uninstalling_dev_spaces.md)
