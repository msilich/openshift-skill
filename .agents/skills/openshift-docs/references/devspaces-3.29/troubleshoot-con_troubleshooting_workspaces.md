> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-con_troubleshooting_workspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# When something goes wrong with your workspace

OpenShift Dev Spaces Cloud Development Environments can encounter startup failures, runtime errors, and IDE issues. Start by checking logs, then use the symptom-based sections in this guide to diagnose and resolve the issue.

The first step for any problem is to check the Cloud Development Environment logs. Logs capture IDE extension activity, container events, and process errors that point to the root cause.

<span id="con_troubleshooting-workspaces_devspaces__entry__1"></span><span id="con_troubleshooting-workspaces_devspaces__entry__2"></span>

| Symptom | Description |
|----|----|
| Need to check logs | View logs from the CLI or the editor to identify errors and warnings. |
| Cloud Development Environment is slow | Tune CPU and memory resource limits in your devfile to improve runtime performance. |
| Webview or editor UI errors | Fix service worker errors in private browsing windows. |
| Devfile syntax or validation errors | Diagnose component failures, lifecycle command problems, and volume or endpoint misconfigurations. |

Table 1. What problem are you experiencing?

**Related information**  

- [Troubleshoot the OpenShift Dev Spaces platform](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/troubleshoot_platform/index#troubleshoot-platform_troubleshoot_platform)
