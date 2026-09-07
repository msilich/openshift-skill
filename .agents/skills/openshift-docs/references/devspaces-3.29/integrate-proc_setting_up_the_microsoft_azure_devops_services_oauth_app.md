> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_setting_up_the_microsoft_azure_devops_services_oauth_app). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create a Microsoft Entra ID application for OpenShift Dev Spaces

Create a Microsoft Entra ID OAuth application so that OpenShift Dev Spaces can authenticate your developers and provide credential-free access to Azure DevOps repositories. .Prerequisites

## About this task

- You are logged in to [Microsoft Azure DevOps Services](https://azure.microsoft.com/en-us/products/devops/).
- `Third-party application access via OAuth` is enabled for your Azure DevOps organization. See [Change application connection & security policies for your organization](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/change-application-access-policies?view=azure-devops).

## Procedure

1.  Register an application in Microsoft Entra ID. See [Register an application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).
2.  Add the **Authorization callback URL**`https://`*`<openshift_dev_spaces_fqdn>`*`/api/oauth/callback` to your application. See [Add a redirect URI](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri).
3.  Add a client secret to your application. See [Add credentials](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=client-secret).
4.  Add the Azure DevOps `vso.code_write` permission to the client application. See [Add permissions to access your web API](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#add-permissions-to-access-your-web-api).
5.  Connect your Azure DevOps organization to Microsoft Entra ID. See [Connect your organization to Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/connect-organization-to-azure-ad?view=azure-devops#connect-your-organization-to-microsoft-entra-id-1).

**Related information**  

- [Authorize access to REST APIs with OAuth 2.0](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops)
- [Change application connection & security policies for your organization](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/change-application-access-policies?view=azure-devops)
