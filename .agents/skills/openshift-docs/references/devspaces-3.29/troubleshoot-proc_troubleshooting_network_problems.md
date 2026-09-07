> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-proc_troubleshooting_network_problems). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Troubleshoot network problems

Troubleshoot OpenShift Dev Spaces network connectivity issues including WebSocket failures, proxy configuration problems, and Domain Name System (DNS) resolution errors.

## Before you begin

- You have an active workspace URL or the OpenShift Dev Spaces dashboard URL.

## Procedure

1.  Verify that the browser supports WebSocket connections by opening the browser developer tools (F12), navigating to the **Console** tab, and running:

    ``` plaintext
    var ws = new WebSocket('wss://echo.websocket.org');
    ws.onopen = function() { console.log('WebSocket OK'); ws.close(); };
    ws.onerror = function() { console.log('WebSocket FAILED'); };
    ```

    If the output is `WebSocket FAILED`, WebSocket connections are blocked. Contact your network administrator to allow WSS connections on port 443.

2.  Verify that firewall rules allow WebSocket Secure (WSS) connections on port 443 to the OpenShift Dev Spaces hostname.

3.  If your network uses a proxy server, verify that the proxy allows WebSocket upgrade requests. Some proxies block HTTP upgrade headers by default.

4.  Verify DNS resolution from a workspace terminal:

    ``` bash
    nslookup <devspaces_hostname>
    ```

    If the DNS lookup fails, the workspace Pod cannot resolve the OpenShift Dev Spaces hostname. Verify the cluster DNS configuration and any custom DNS settings in the workspace namespace.

5.  If you encounter `x509: certificate signed by unknown authority` errors when connecting to an HTTPS endpoint from inside a workspace, the workspace does not trust the TLS certificate.

    Contact your administrator to import the required Certificate Authority (CA) certificates.

## Results

- Open a workspace and verify that the IDE loads without connection errors.
- Verify that Git operations (clone, push, pull) complete without network timeouts.

**Related concepts**  

- [Diagnose slow Cloud Development Environments](troubleshoot-con_diagnose_slow_cdes.md "Diagnose slow Cloud Development Environment startup by pre-pulling images, tuning storage strategy, installing offline, and reducing public endpoints.")

**Related tasks**  

- [View workspace logs in CLI](troubleshoot-proc_viewing_workspace_logs_in_cli.md "View OpenShift Dev Spaces workspace logs from the OpenShift command-line interface (CLI) to troubleshoot startup failures and runtime errors.")

**Related information**  

- [Fix webview loading errors in private browsing](troubleshoot-con_troubleshooting_webview_loading_error.md)
