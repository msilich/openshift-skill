> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/upgrade-proc_specifying_update_approval_strategy). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Choose how updates are applied

Choose between automatic and manual update approval for the Red Hat OpenShift Dev Spaces Operator so that you control when new versions are installed on your cluster.

## Before you begin

- You have an OpenShift web console session as a cluster administrator. See [Accessing the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/web-console).
- You have an instance of OpenShift Dev Spaces installed by using Red Hat Ecosystem Catalog.

## About this task

The Red Hat OpenShift Dev Spaces Operator supports two upgrade strategies:

`Automatic`  
The Operator installs new updates when they become available.

`Manual`  
New updates need to be manually approved before installation begins.

## Procedure

1.  In the OpenShift web console, navigate to Operators<span class="abbr" title="and then"> \> </span>Installed Operators.
2.  Click **Red Hat OpenShift Dev Spaces** in the list of installed Operators.
3.  Navigate to the **Subscription** tab.
4.  Configure the **Update approval** strategy to `Automatic` or `Manual`.

**Related information**  

- [Changing the update channel for an Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/administrator-tasks#olm-changing-update-channel_olm-upgrading-operators)
