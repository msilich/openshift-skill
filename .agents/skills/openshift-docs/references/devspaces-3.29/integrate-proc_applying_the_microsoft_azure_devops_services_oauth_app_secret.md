> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_applying_the_microsoft_azure_devops_services_oauth_app_secret). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Connect OpenShift Dev Spaces to your Microsoft Entra ID application

Connect OpenShift Dev Spaces to your Microsoft Entra ID application so that developers can access Azure DevOps repositories from workspaces without re-entering credentials. .Prerequisites

## About this task

- You have configured the Microsoft Entra ID OAuth App.
- You have the following values, which were generated when configuring the Microsoft Entra ID OAuth App:
  - **Application (client) ID**
  - **Directory (tenant) ID**
  - **Client Secret**

<!-- -->

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Prepare the Secret:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: azure-devops-oauth-config
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: oauth-scm-configuration
      annotations:
        che.eclipse.org/oauth-scm-server: azure-devops
    type: Opaque
    stringData:
      tenant-id: <Microsoft_Entra_ID_Tenant_ID>
      id: <Microsoft_Entra_ID_App_ID>
      secret: <Microsoft_Entra_ID_Client_Secret>
    ```

    where:

    `namespace`  
    The OpenShift Dev Spaces namespace. The default is `openshift-devspaces`.

    `tenant-id`  
    The Microsoft Entra ID **Directory (tenant) ID**.

    `id`  
    The Microsoft Entra ID **Application (client) ID**.

    `secret`  
    The Microsoft Entra ID **Client Secret**.

2.  Apply the Secret:

    ``` bash
    $ oc apply -f - <<EOF
    <Secret_prepared_in_the_previous_step>
    EOF
    ```

## Results

- Verify that the output displays `secret/azure-devops-oauth-config created`.

- Verify that the rollout of the OpenShift Dev Spaces server components is complete:

  ``` bash
  $ oc rollout status deployment/devspaces -n openshift-devspaces
  ```

**Related tasks**  

- [Create a Microsoft Entra ID application for OpenShift Dev Spaces](integrate-proc_setting_up_the_microsoft_azure_devops_services_oauth_app.md "Create a Microsoft Entra ID OAuth application so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to Azure DevOps repositories. .Prerequisites")
- [Create a GitHub OAuth application for OpenShift Dev Spaces](integrate-proc_setting_up_the_github_oauth_app.md "Create an OAuth 2.0 application on GitHub so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitHub repositories. .Prerequisites")
- [Create a GitLab OAuth application for OpenShift Dev Spaces](integrate-proc_setting_up_the_gitlab_authorized_application.md "Create an OAuth 2.0 authorized application on your GitLab instance so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to GitLab repositories. .Prerequisites")
