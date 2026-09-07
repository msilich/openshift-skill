> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-ref_ai_provider_api_key_secret_reference). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# AI provider API key secret reference

Each user’s AI provider API key is stored as a OpenShift `Opaque` Secret in the user’s personal project. The Dev Workspace Controller automatically mounts matching Secrets as environment variables into all workspace containers.

<span id="ref_ai-provider-api-key-secret-reference_devspaces___what_the_secret_contains"></span>

## [What the Secret contains](extend-ref_ai_provider_api_key_secret_reference.md#ref_ai-provider-api-key-secret-reference_devspaces___what_the_secret_contains)

``` yaml
apiVersion: v1
kind: Secret
metadata:
  name: ai-provider-openai-api-key
  namespace: <user-namespace>
  labels:
    controller.devfile.io/mount-to-devworkspace: 'true'
    controller.devfile.io/watch-secret: 'true'
    che.eclipse.org/ai-provider-id: opencodeai-opencode
  annotations:
    controller.devfile.io/mount-as: env
type: Opaque
data:
  OPENAI_API_KEY: <base64-encoded-api-key>
```

`name`  
Secret name is derived as `ai-provider-` + `envVarName.toLowerCase().replace(/_/g, '-')`. For `OPENAI_API_KEY` the name is `ai-provider-openai-api-key`.

`mount-to-devworkspace: 'true'`  
Instructs the DevWorkspace Controller to mount this Secret into all `DevWorkspace` containers in the namespace.

`watch-secret: 'true'`  
Instructs the DevWorkspace Controller to watch for Secret changes and re-mount without a workspace restart.

`ai-provider-id`  
Sanitized provider ID (characters other than letters, digits, dots, underscores, and dashes are replaced with dashes). Identifies which AI provider this Secret belongs to. Used by the OpenShift Dev Spaces dashboard to detect existing keys.

`mount-as: env`  
Mounts the Secret data keys as environment variables (not as files).

`OPENAI_API_KEY`  
The data key is the environment variable name. The value is base64-encoded. The variable is injected directly into all workspace containers.

<span id="ref_ai-provider-api-key-secret-reference_devspaces___required_labels_and_annotations"></span>

## [Required labels and annotations](extend-ref_ai_provider_api_key_secret_reference.md#ref_ai-provider-api-key-secret-reference_devspaces___required_labels_and_annotations)

<span id="ref_ai-provider-api-key-secret-reference_devspaces___required_labels_and_annotations__entry__1"></span><span id="ref_ai-provider-api-key-secret-reference_devspaces___required_labels_and_annotations__entry__2"></span><span id="ref_ai-provider-api-key-secret-reference_devspaces___required_labels_and_annotations__entry__3"></span>

| Label / Annotation | Value | Purpose |
|----|----|----|
| `controller.devfile.io/mount-to-devworkspace` | `'true'` | Causes the DevWorkspace Controller to mount this Secret into every `DevWorkspace` in the namespace. |
| `controller.devfile.io/watch-secret` | `'true'` | The DevWorkspace Controller re-mounts the Secret when its data changes, without requiring a workspace restart. |
| `controller.devfile.io/mount-as` | `env` | Each data key in the Secret becomes an environment variable with the key as the variable name and the decoded value as the variable value. |
| `che.eclipse.org/ai-provider-id` | Sanitized provider ID (for example, `opencodeai-opencode`). Characters other than letters, digits, dots, underscores, and dashes are replaced with dashes. | Used by the OpenShift Dev Spaces dashboard to identify and list AI provider key Secrets when rendering the AI Selector widget. |

<span id="ref_ai-provider-api-key-secret-reference_devspaces___how_to_name_your_secret"></span>

## [How to name your Secret](extend-ref_ai_provider_api_key_secret_reference.md#ref_ai-provider-api-key-secret-reference_devspaces___how_to_name_your_secret)

Secret names follow the pattern:

``` plaintext
ai-provider-<envVarName-lowercased-underscores-as-dashes>
```

Example:

<span id="ref_ai-provider-api-key-secret-reference_devspaces___how_to_name_your_secret__entry__1"></span><span id="ref_ai-provider-api-key-secret-reference_devspaces___how_to_name_your_secret__entry__2"></span>

| `envVarName`     | Secret name                  |
|------------------|------------------------------|
| `OPENAI_API_KEY` | `ai-provider-openai-api-key` |

<span id="ref_ai-provider-api-key-secret-reference_devspaces___create_the_secret_manually"></span>

## [Create the Secret manually](extend-ref_ai_provider_api_key_secret_reference.md#ref_ai-provider-api-key-secret-reference_devspaces___create_the_secret_manually)

Advanced users can create AI provider key Secrets manually using `oc` instead of the dashboard UI. Use the same labels and annotations as shown in the schema above:

``` bash
$ oc apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: ai-provider-openai-api-key
  namespace: <user-namespace>
  labels:
    controller.devfile.io/mount-to-devworkspace: 'true'
    controller.devfile.io/watch-secret: 'true'
    che.eclipse.org/ai-provider-id: opencodeai-opencode
  annotations:
    controller.devfile.io/mount-as: env
type: Opaque
data:
  OPENAI_API_KEY: <base64-encoded-api-key>
EOF
```

**Related tasks**  

- [Register an AI provider](extend-proc_configuring_ai_providers.md "Register one or more AI providers in OpenShift Dev Spaces so that developers can select and use AI coding assistants when creating workspaces.")

**Related information**  

- [Mount Secrets](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop/index#mounting-secrets_develop)
- [Devfile documentation](https://devfile.io/docs/2.2.0/what-is-a-devfile)
