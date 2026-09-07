> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_disabling_ai_providers). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Disable AI coding assistants

Disable AI coding assistants by deleting the `ai-tool-registry` ConfigMap. The AI Provider section on the **Create Workspace** page is hidden when the ConfigMap is absent.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Delete the `ai-tool-registry` ConfigMap:

    ``` bash
    $ oc delete configmap ai-tool-registry -n openshift-devspaces
    ```

2.  Verify that the AI provider registry is empty:

    ``` bash
    $ oc exec deploy/devspaces-dashboard -n openshift-devspaces \
        -- curl -s http://localhost:8080/dashboard/api/ai-registry
    ```

    Expected output:

    ``` plaintext
    {"providers":[],"tools":[],"defaultAiProviders":[]}
    ```

## Results

- Open the OpenShift Dev Spaces dashboard and navigate to **Create Workspace**. Verify that the **AI Provider** section is no longer visible.

Note

Deleting the ConfigMap does not remove existing API key Secrets from user namespaces. Users who previously stored API keys retain those Secrets until they manually delete them or an administrator removes them.

**Related tasks**  

- [Register an AI provider](extend-proc_configuring_ai_providers.md "Register one or more AI providers in OpenShift Dev Spaces so that developers can select and use AI coding assistants when creating workspaces.")

**Related reference**  

- [AI provider API key secret reference](extend-ref_ai_provider_api_key_secret_reference.md "Each user’s AI provider API key is stored as a OpenShift Opaque Secret in the user’s personal project. The Dev Workspace Controller automatically mounts matching Secrets as environment variables into all workspace containers.")
