> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-con_troubleshooting_webview_loading_error). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Fix webview loading errors in private browsing

If you use Microsoft Visual Studio Code - Open Source in a private browsing window, you might encounter an error message. The error is: **Error loading webview: Error: Could not register service workers**.

This is a known issue affecting the following browsers:

- Google Chrome in Incognito mode
- Mozilla Firefox in Private Browsing mode

<span id="con_troubleshooting-webview-loading-error_devspaces__entry__1"></span><span id="con_troubleshooting-webview-loading-error_devspaces__entry__2"></span>

| Browser | Workarounds |
|----|----|
| Google Chrome | Go to **Settings** **Privacy and security** **Cookies and other site data** **Allow all cookies**. |
| Mozilla Firefox | Webviews are not supported in Private Browsing mode. See the Mozilla bug report for details. |

Table 1. Dealing with the webview error in a private browsing window

**Related information**  

- [Mozilla Bug 1320796: Service workers are not available in Private Browsing mode](https://bugzilla.mozilla.org/show_bug.cgi?id=1320796)
