<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If you are using Jira, you can forward alerts from Red Hat Advanced Cluster Security for Kubernetes to Jira.

<a id="jira-integration-workflow-overview_integrate-with-jira"></a>

# Jira integration workflow

The Red Hat Advanced Cluster Security for Kubernetes integration with Jira follows a three-step workflow to enable alert forwarding.

The following steps represent a high-level workflow for integrating Red Hat Advanced Cluster Security for Kubernetes with Jira:

1.  Setup a user in Jira.

2.  Use the Jira URL, username, and password to integrate Jira with Red Hat Advanced Cluster Security for Kubernetes.

3.  Identify policies for which you want to send notifications, and update the notification settings for those policies.

<a id="configure-jira_integrate-with-jira"></a>

# Configuring Jira

Start by creating a new user, and assign appropriate roles and permissions.

<div>

<div class="title">

Prerequisites

</div>

- You need a Jira account with permissions to create and edit issues in the project with which you are integrating.

</div>

<div>

<div class="title">

Procedure

</div>

- Create a user in Jira which have access to the projects for which you want to create issues:

  - To create a new user, see the "Create, edit, or remove a user" topic in the Jira documentation.

  - To give users access to project roles and applications, see the "Assign users to groups, project roles, and applications" topic in the Jira documentation.

    > [!NOTE]
    > If you are using Jira Software Cloud, after you create the user, you must create a token for the user:
    >
    > 1.  Go to API tokens, to generate a new token.
    >
    > 2.  Use the token as password when you configure Red Hat Advanced Cluster Security for Kubernetes.

</div>

<div>

<div class="title">

Additional resources

</div>

- [API Tokens](https://id.atlassian.com/manage-profile/security/api-tokens)

- [Create, edit, or remove a user](https://confluence.atlassian.com/adminjiraserver/create-edit-or-remove-a-user-938847025.html)

- [Assign users to groups, project roles, and applications](https://confluence.atlassian.com/adminjiraserver/assign-users-to-groups-project-roles-and-applications-938847026.html)

</div>

<a id="jira-configuring-acs_integrate-with-jira"></a>

# Configuring Red Hat Advanced Cluster Security for Kubernetes

Create a new integration in Red Hat Advanced Cluster Security for Kubernetes by using the Jira server URL and user credentials.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Notifier Integrations** section and select **Jira Software**.

3.  Click **New integration**.

4.  Enter a name for **Integration name**.

5.  Enter the user credentials in the **Username** and **Password or API token** fields.

6.  For **Issue type**, enter a valid Jira Issue Type, for example **Task**, **Sub-task**, or **Bug**.

7.  Enter the Jira server URL in the **Jira URL** field.

8.  Enter the key of the project in which you want to create issues in the **Default project** field.

9.  Optional: Use the **Annotation key for project** field to create issues in different Jira projects by completing the following steps. You can use annotations to dynamically create issues.

    1.  Add an annotation similar to the following example in your namespace or deployment YAML file, where `jira/project-key` is the annotation key that you specify in your Jira integration. You can create an annotation for the deployment or the namespace.

        ``` yaml
        annotations:
        # ...
          jira/project-key: <jira_project_key>
        # ...
        ```

    2.  Use the annotation key `jira/project-key` in the **Annotation key for project** field.

10. If you use custom priorities in your Jira project, use the **Priority Mapping** toggle to configure custom priorities.

11. If you use mandatory custom fields in your Jira project, enter them as JSON values in the **Default Fields JSON** field. For example:

    ``` json
    {
      "customfield_10004": 3,
      "customfield_20005": "Alerts",
    }
    ```

12. Select **Test** to test that the integration with Jira is working.

13. Select **Create** to generate the configuration.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Jira Issue Types](https://confluence.atlassian.com/adminjiracloud/issue-types-844500742.html)

</div>

<a id="create-issues-in-different-jira-projects_integrate-with-jira"></a>

## Creating issues in different Jira projects

You can configure Red Hat Advanced Cluster Security for Kubernetes to create issues in different Jira projects so that they directly go to the correct team. After completing the configuration, if a deployment has an annotation in the YAML file, RHACS creates issues in the project specified for that annotation. Otherwise, RHACS creates issues in the default project.

<div>

<div class="title">

Prerequisites

</div>

- You must have an account with access to each project that you want to send the alerts to.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add an annotation similar to the following example in your namespace or deployment YAML file:

    ``` yaml
    annotations:
    # ...
      jira/project-key: <jira_project_key>
    # ...
    ```

2.  Use the annotation key `jira/project-key` in the **Annotation key for project** field when you configure Red Hat Advanced Cluster Security for Kubernetes.

</div>

<a id="configure-custom-priorities-in-jira_integrate-with-jira"></a>

## Configuring custom priorities in Jira

If you are using custom priorities in your Jira project, you can configure them in Red Hat Advanced Cluster Security for Kubernetes.

<div>

<div class="title">

Procedure

</div>

1.  While configuring Jira integration in Red Hat Advanced Cluster Security for Kubernetes, turn on the **Priority Mapping** toggle. Red Hat Advanced Cluster Security for Kubernetes gets the JIRA project schema, and auto fills the values for the **CRITICAL_SEVERITY**, **HIGH_SEVERITY**, **MEDIUM_SEVERITY**, and **LOW_SEVERITY** fields.

2.  Verify or update the priority values based on your JIRA project configuration.

3.  Select **Test** to test that the integration with Jira is working.

4.  Select **Create** to generate the configuration.

</div>

<a id="configure-policy-notifications_integrate-with-jira"></a>

# Configuring policy notifications

Enable alert notifications for system policies.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Select one or more policies for which you want to send alerts.

3.  Under **Bulk actions**, select **Enable notification**.

4.  In the **Enable notification** window, select the **Jira** notifier.

    > [!NOTE]
    > If you have not configured any other integrations, the system displays a message that no notifiers exist.

5.  Click **Enable**.

    <div class="note">

    <div class="title">

    </div>

    - Red Hat Advanced Cluster Security for Kubernetes sends notifications on an opt-in basis. To receive notifications, you must first assign a notifier to the policy.

    - Notifications are only sent once for a given alert. If you have assigned a notifier to a policy, you will not receive a notification unless a violation generates a new alert.

    - Red Hat Advanced Cluster Security for Kubernetes creates a new alert for the following scenarios:

      - A policy violation occurs for the first time in a deployment.

      - A runtime-phase policy violation occurs in a deployment after you resolved the earlier runtime alert for a policy in that deployment.

    </div>

</div>

<a id="troubleshoot-jira-integration_integrate-with-jira"></a>

# Troubleshooting Jira integration

If you are using custom priorities or mandatory custom fields in your Jira project, you might get an error when you try to integrate Red Hat Advanced Cluster Security for Kubernetes with Jira Software. This error might be because of the mismatch between the severity and the priority field values.

If you do not know the custom priority values in your JIRA project, use the `roxctl` CLI to enable debug logging for JIRA integration.

<div>

<div class="title">

Procedure

</div>

1.  To get the custom priority values from your JIRA project, run the following command to turn on debug logging for JIRA integration:

    ``` terminal
    $ roxctl -e "$ROX_CENTRAL_ADDRESS" central debug log --level Debug --modules notifiers/jira
    ```

2.  Follow the instructions to configure Red Hat Advanced Cluster Security for Kubernetes for Jira integration. When you test the integration, even if the integration test fails, the generated log includes your JIRA project schema and the custom priorities.

3.  To save the debugging information as a compressed `.zip` file, run the following command:

    ``` terminal
    $ roxctl -e "$ROX_CENTRAL_ADDRESS" central debug dump
    ```

4.  Extract the `.zip` file to retrieve the custom priority values in use in your JIRA project.

5.  To turn off debug logging, run the following command:

    ``` terminal
    $ roxctl -e "$ROX_CENTRAL_ADDRESS" central debug log --level Info
    ```

6.  Configure Red Hat Advanced Cluster Security for Kubernetes for Jira integration again and use the priority values to configure custom priorities.

</div>
