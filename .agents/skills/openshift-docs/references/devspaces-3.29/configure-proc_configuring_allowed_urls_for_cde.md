> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_allowed_urls_for_cde). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Restrict which URLs can create workspaces

Restrict Cloud Development Environment (CDE) initiation to authorized source URLs, protecting your infrastructure from untrusted deployments.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

Patch the `CheCluster` Custom Resource to configure the allowed source URLs:

``` bash
oc patch checluster/devspaces \
    --namespace openshift-devspaces \
    --type='merge' \
    -p \
'{
   "spec": {
     "devEnvironments": {
       "allowedSources": {
         "urls": ["<url_1>", "<url_2>"]
       }
     }
   }
 }'
```

where:

`urls`  
The array of approved URLs for starting CDEs. Wildcards `*` are supported. For example, `https://example.com/\*` allows CDEs from any path within `example.com`.

## Results

- In the OpenShift Dev Spaces Dashboard, start a workspace from an allowed URL and verify that it starts successfully.
- Attempt to start a workspace from a URL that is not in the allowed list and verify that it is rejected.

**Related information**  

- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
