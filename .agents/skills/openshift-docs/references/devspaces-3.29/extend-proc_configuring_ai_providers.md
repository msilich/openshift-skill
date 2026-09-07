> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_configuring_ai_providers). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Register an AI provider

Register one or more AI providers in OpenShift Dev Spaces so that developers can select and use AI coding assistants when creating workspaces.

## Before you begin

- An active `oc` session with administrative permissions to the destination OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- The devspaces-operator is installed and a `devspaces` custom resource exists in the `openshift-devspaces` namespace.

## About this task

Important

The AI provider feature is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see <https://access.redhat.com/support/offerings/techpreview/>.

The AI tool registry is stored in a OpenShift `ConfigMap` with specific labels. When the ConfigMap exists and contains at least one provider with a matching tool, the AI Selector widget is displayed on the dashboard. When the ConfigMap is absent or empty, the widget is hidden.

## Procedure

1.  Optional: Build and push a custom AI tool injector image.

    The injector image is a container that carries the AI tool binary. During workspace startup, OpenShift Dev Spaces runs it as an init container to copy the binary into a shared volume. The following minimal `Dockerfile` is based on the [OpenCode injector image](https://github.com/che-incubator/che-ai-tool-images/blob/main/dockerfiles/opencode/Dockerfile):

    ``` plaintext
    FROM alpine:3.21 AS builder

    ARG OPENCODE_VERSION=v1.2.27
    ARG TARGETARCH

    RUN apk add --no-cache curl tar gzip

    RUN set -e && \
        case "${TARGETARCH}" in \
          amd64) ARCH="x64" ;; \
          arm64) ARCH="arm64" ;; \
          *) echo "Unsupported architecture: ${TARGETARCH}" && exit 1 ;; \
        esac && \
        curl -fsSL -o /tmp/opencode.tar.gz \
          "https://github.com/anomalyco/opencode/releases/download/${OPENCODE_VERSION}/opencode-linux-${ARCH}.tar.gz" && \
        tar -xzf /tmp/opencode.tar.gz -C /tmp && \
        mv /tmp/opencode /usr/local/bin/opencode && \
        chmod +x /usr/local/bin/opencode

    FROM registry.access.redhat.com/ubi10/ubi-minimal:10.0

    COPY --from=builder /usr/local/bin/opencode /usr/local/bin/opencode-bin

    RUN printf '#!/bin/sh\n\
    SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"\n\
    OC_HOME="/tmp/opencode-home"\n\
    mkdir -p "$OC_HOME/.config" "$OC_HOME/.local/share"\n\
    export XDG_CONFIG_HOME="${XDG_CONFIG_HOME:-$OC_HOME/.config}"\n\
    export XDG_DATA_HOME="${XDG_DATA_HOME:-$OC_HOME/.local/share}"\n\
    exec "$SCRIPT_DIR/opencode-bin" "$@"\n' > /usr/local/bin/opencode && \
        chmod +x /usr/local/bin/opencode

    LABEL org.opencontainers.image.description="OpenCode CLI tool for DevWorkspace injection" \
          org.opencontainers.image.source="https://github.com/che-incubator/che-ai-tool-images.git"
    ```

    Key design points:

    - **Multi-stage build**: the `builder` stage downloads the architecture-specific binary; the minimal runtime stage keeps the final image small.
    - **Wrapper script**: redirects `XDG_CONFIG_HOME`, `XDG_DATA_HOME`, and related variables to writable paths under `/tmp`, allowing the tool to run as an arbitrary UID on OpenShift.
    - **Multi-arch**: pass `--platform linux/amd64,linux/arm64` to `podman build` to produce a multi-arch image.

    Build and push the image:

    ``` bash
    $ {docker-cli} build --platform linux/amd64,linux/arm64 \
        -t <your-registry>/<your-org>/opencode:next \
        --push .
    ```

    See [che-incubator/che-ai-tool-images](https://github.com/che-incubator/che-ai-tool-images) for maintained injector image examples.

2.  Create a `registry.json` file that defines providers, tools, and optional defaults:

    ``` plaintext
    {
      "providers": [
        {
          "id": "opencodeai/opencode",
          "name": "OpenCode",
          "publisher": "opencode.ai",
          "description": "Open-source terminal AI coding agent supporting 75+ LLM providers.",
          "docsUrl": "https://opencode.ai",
          "icon": "https://example.com/opencode-icon.svg"
        }
      ],
      "tools": [
        {
          "providerId": "opencodeai/opencode",
          "tag": "next",
          "name": "OpenCode",
          "url": "https://opencode.ai",
          "binary": "opencode",
          "pattern": "init",
          "injectorImage": "<your-registry>/<your-org>/opencode:next",
          "envVarName": "OPENAI_API_KEY"
        }
      ],
      "defaultAiProviders": ["opencodeai/opencode"]
    }
    ```

    The following table describes the key fields:

    <span id="proc_configuring-ai-providers_devspaces__entry__1"></span><span id="proc_configuring-ai-providers_devspaces__entry__2"></span>

    | Field | Description |
    |----|----|
    | `id` | Unique provider identifier in *`<vendor>`*`/`*`<product>`* format. |
    | `providerId` | Links the tool to its provider by `id`. |
    | `tag` | Version tag. When multiple tools share the same `providerId`, the dashboard selects by priority: `next` \> `latest` \> highest semver. |
    | `binary` | Binary name that must be available in `PATH` inside the workspace after injection. |
    | `pattern` | Injection pattern: `init` copies a single binary into the shared volume; `bundle` copies a full runtime directory and creates a symlink. |
    | `injectorImage` | Container image that carries the tool binary. Run as an init container at workspace start. |
    | `envVarName` | Environment variable name for the API key. The dashboard creates a OpenShift Secret using this name as the data key. |
    | `defaultAiProviders` | Optional. Provider IDs pre-selected in the AI Selector widget for new workspaces. |

3.  Create the `ConfigMap` in the `openshift-devspaces` namespace with the required labels:

    ``` bash
    $ oc create configmap ai-tool-registry \
      --from-file=registry.json=registry.json \
      -n openshift-devspaces \
      --dry-run=client -o yaml | \
      oc label --local -f - \
        app.kubernetes.io/component=ai-tool-registry \
        app.kubernetes.io/part-of=che.eclipse.org \
        -o yaml | \
      oc apply -f -
    ```

## Results

1.  Open the OpenShift Dev Spaces dashboard.
2.  Navigate to **Create Workspace**.
3.  Verify that an **AI Provider** section is visible, listing the providers you configured.

Note

To disable the AI Selector widget, delete the `ai-tool-registry` ConfigMap. Users will no longer see the AI Provider section on the **Create Workspace** page. Existing API key Secrets in user namespaces are not deleted automatically.

When you update the registry (for example, to remove a tool or change the injector image tag), existing workspaces are updated automatically before their next start. The dashboard removes stale tool injectors and replaces outdated image tags without user intervention.

**Related reference**  

- [AI provider API key secret reference](extend-ref_ai_provider_api_key_secret_reference.md "Each user’s AI provider API key is stored as a OpenShift Opaque Secret in the user’s personal project. The Dev Workspace Controller automatically mounts matching Secrets as environment variables into all workspace containers.")

**Related information**  

- [Use AI assistants in workspaces](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop_tools/index#using-ai-assistants-in-workspaces_develop_tools)
