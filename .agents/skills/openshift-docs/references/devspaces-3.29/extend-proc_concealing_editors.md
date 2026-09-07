> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_concealing_editors). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Hide editors from the dashboard

Hide selected OpenShift Dev Spaces editors from the Dashboard UI, for example IntelliJ IDEA Ultimate, and have only Visual Studio Code - Open Source visible.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have `jq` installed. See [Downloading `jq`](https://stedolan.github.io/jq/download/).

## Procedure

1.  Determine the IDs of the available editors. An editor ID has the following format: `publisher/name/version`.

    ``` bash
    oc exec deploy/devspaces-dashboard -n openshift-devspaces  \
        -- curl -s http://localhost:8080/dashboard/api/editors | jq -r '[.[] | "\(.metadata.attributes.publisher)/\(.metadata.name)/\(.metadata.attributes.version)"]'
    ```

2.  Edit the `CheCluster` Custom Resource on the cluster:

    ``` bash
    $ oc edit checluster/devspaces -n openshift-devspaces
    ```

    ``` yaml
    spec:
      components:
        dashboard:
          deployment:
            containers:
            - env:
              - name: CHE_HIDE_EDITORS_BY_ID
                value: 'che-incubator/che-webstorm-server/latest, che-incubator/che-webstorm-server/next'
    ```

    where:

    value  
    A string containing comma-separated IDs of editors to hide.

## Results

- In the OpenShift Dev Spaces Dashboard, go to **Create Workspace** and verify that the concealed editors are no longer visible.

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md)
- [Editor definition samples](https://github.com/devfile/devworkspace-operator/tree/main/samples/editors)
