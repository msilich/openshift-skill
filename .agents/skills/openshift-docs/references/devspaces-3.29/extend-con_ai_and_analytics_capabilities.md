> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-con_ai_and_analytics_capabilities). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# What you can add to your platform

OpenShift Dev Spaces creates a Cloud Development Environment (CDE) for every project. The dashboard and CLI refer to each CDE as a **workspace**. Beyond the default tooling, you can add AI coding assistants and build custom analytics plugins.

As a Platform administrator, you can register AI coding assistants so that developers can select an AI provider when creating workspaces. The AI tool binary is injected into the workspace at startup via an init container.

As a Developer, you can build a custom telemetry plugin that collects workspace activity events and sends them to your organization’s analytics backend. The plugin extends the `AbstractAnalyticsManager` class from the DevWorkspace Telemetry SDK.

<span id="con_ai-and-analytics-capabilities_devspaces__entry__1"></span><span id="con_ai-and-analytics-capabilities_devspaces__entry__2"></span>

| Goal | Description |
|----|----|
| Register AI coding assistants | Configure AI providers so that developers can select them when creating workspaces. Store API keys in OpenShift Secrets that are automatically mounted into workspace containers. |
| Build a custom telemetry plugin | Create a backend that receives workspace events (start, stop, activity) and forwards them to your analytics system. |

Table 1. What do you need to add?

For information about how developers use AI assistants in workspaces, see Additional resources.

**Related information**  

- [Customize workspace tooling](extend-con_extending_devspaces.md)
- [Use AI assistants in workspaces](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop_tools/index#using-ai-assistants-in-workspaces_develop_tools)
