> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/upgrade-proc_verify_upgrade_completed). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Verify the upgrade completed successfully

Verify that all OpenShift Dev Spaces components are running the new version and that the platform is functional so that you can confirm the upgrade succeeded before notifying developers.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Verify that the OpenShift Dev Spaces Operator CSV shows the expected version and `Succeeded` phase:

    ``` bash
    $ oc get csv -n openshift-devspaces -o custom-columns='NAME:.metadata.name,PHASE:.status.phase,VERSION:.spec.version'
    ```

    Expected output:

    ``` shell-session
    NAME                        PHASE       VERSION
    devspacesoperator.v3.29.0   Succeeded   3.29.0
    ```

2.  Verify that the `CheCluster` custom resource reports `Active` phase and the correct version:

    ``` bash
    $ oc get checluster devspaces -n openshift-devspaces -o jsonpath='Phase: {.status.chePhase}, Version: {.status.cheVersion}'
    ```

    Expected output:

    ``` shell-session
    Phase: Active, Version: 3.29.0
    ```

3.  Verify that all OpenShift Dev Spaces pods in the `openshift-devspaces` namespace are running and ready:

    ``` bash
    $ oc get pods -n openshift-devspaces
    ```

    All pods should show `Running` status with all containers ready.

4.  Verify that the OpenShift Dev Spaces dashboard is accessible:

    ``` bash
    $ oc get checluster devspaces -n openshift-devspaces -o jsonpath='{.status.cheURL}'
    ```

    Open the returned URL in a browser and confirm the login page loads.

5.  Verify that the Dev Workspace Operator is running the expected version:

    ``` bash
    $ oc get csv -n openshift-operators -o custom-columns='NAME:.metadata.name,PHASE:.status.phase' | grep devworkspace
    ```

    The Dev Workspace Operator CSV should show `Succeeded` phase.

6.  Start a test workspace from the OpenShift Dev Spaces dashboard to confirm that workspaces function correctly after the upgrade.

**Related information**  

- [OpenShift Dev Spaces 3.29 release notes](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/release_notes/)
- [Troubleshoot the OpenShift Dev Spaces platform](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/troubleshoot_platform/index#troubleshoot-platform_troubleshoot_platform)
