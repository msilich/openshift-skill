> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-proc_finding_the_fqdn). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Get the dashboard URL to share with your team

Get the OpenShift Dev Spaces dashboard URL from the `CheCluster` custom resource so that you can open the dashboard in a browser or share the endpoint with your development team.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

Tip

You can find the FQDN for your organization’s OpenShift Dev Spaces instance in the **Administrator** view of the OpenShift web console as follows. Go to **Operators** **Installed Operators** **Red Hat OpenShift Dev Spaces instance Specification** **devspaces** **Red Hat OpenShift Dev Spaces URL**.

## Procedure

Retrieve the OpenShift Dev Spaces URL from the `CheCluster` custom resource:

``` bash
oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.status.cheURL}'
```

## Results

- Open the returned URL in a web browser and verify that the OpenShift Dev Spaces dashboard loads.

**Related tasks**  

- [Deploy using the CLI](install-proc_installing_dev_spaces_using_cli.md "Deploy OpenShift Dev Spaces from the command line using the dsc management tool so that you have full control over configuration options and can automate the installation.")
- [Deploy using the web console](install-proc_installing_dev_spaces_using_web_console.md "Deploy OpenShift Dev Spaces through the OpenShift web console using the standard OperatorHub workflow so that you can install without command-line access.")
- [Deploy in an air-gapped environment](install-proc_installing_dev_spaces_in_a_restricted_environment_on_openshift.md "Deploy OpenShift Dev Spaces on an OpenShift cluster with no internet access by mirroring the required container images and Operator catalogs to a private registry.")
