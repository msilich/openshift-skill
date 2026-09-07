> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-con_troubleshooting_platform). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# When something goes wrong with the platform

OpenShift Dev Spaces Cloud Development Environments can encounter startup failures, network errors, and authentication problems caused by platform-level configuration issues. Start by checking logs in the OpenShift console, then use the symptom-based sections in this guide to diagnose and resolve the issue.

The first step for any infrastructure problem is to check the Cloud Development Environment logs in the OpenShift console. Logs from the OpenShift Dev Spaces server, the Dev Workspace Operator, and workspace Pods reveal scheduling, networking, and authentication errors.

<span id="con_troubleshooting-platform_devspaces__entry__1"></span><span id="con_troubleshooting-platform_devspaces__entry__2"></span>

| Symptom | Description |
|----|----|
| Need to check logs | View logs from the CLI or the OpenShift console to identify server and operator errors. |
| Cloud Development Environment fails to start | Diagnose pod scheduling, image pull, DevWorkspace, and resource quota errors from the dashboard or operator logs. |
| Cloud Development Environment is slow | Pre-pull images, tune storage strategy, install offline, and reduce public endpoints to improve startup time. |
| Network connectivity issues | Diagnose WebSocket failures, proxy configuration problems, and DNS resolution errors. |
| OAuth or Git authentication errors | Verify callback URLs, Secret labels, GitLab scopes, and Bitbucket public keys. |

Table 1. What problem are you experiencing?

**Related information**  

- [Troubleshoot workspaces](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/troubleshoot_workspaces/index#troubleshoot-workspaces_troubleshoot_workspaces)
