> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-con_setting_up_development_tools). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# What development tools you can configure

OpenShift Dev Spaces supports multiple IDEs and AI coding assistants that you can configure for your Cloud Development Environments. Choose between Visual Studio Code - Open Source and JetBrains IntelliJ IDEA, define a common IDE for your team’s repositories, and select AI providers.

**IDE options**

OpenShift Dev Spaces supports Visual Studio Code - Open Source as the default editor. You can also connect JetBrains IntelliJ IDEA Ultimate Edition through JetBrains Gateway or JetBrains Toolbox. To standardize the IDE across your team, add a `che-editor.yaml` file to your Git repository.

**AI coding assistants**

Your administrator registers AI providers in the OpenShift Dev Spaces configuration. You select a provider when creating a Cloud Development Environment, configure your API key as a OpenShift Secret, and the AI tool binaries are injected into your workspace. GitHub Copilot Chat is available as a VS Code extension. For information about how administrators register AI providers, see Additional resources.

<span id="con_setting-up-development-tools_devspaces__entry__1"></span><span id="con_setting-up-development-tools_devspaces__entry__2"></span>

| Goal | Description |
|----|----|
| Choose and configure your IDE | Connect Visual Studio Code or JetBrains IntelliJ IDEA, define a common IDE for your team, and automate extension installation. |
| Use AI coding assistants | Select an AI provider, configure your API key, set up GitHub Copilot Chat, and switch between tools. |

Table 1. What do you need to set up?

**Related information**  

- [Develop with OpenShift Dev Spaces](develop-con_developing_with_devspaces.md)
- [Register AI coding assistants](extend-assembly_configuring_ai_providers.md)
