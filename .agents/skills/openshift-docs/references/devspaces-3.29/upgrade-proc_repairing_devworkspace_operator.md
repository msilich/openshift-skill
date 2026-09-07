> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/upgrade-proc_repairing_devworkspace_operator). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Fix a duplicate Dev Workspace Operator after a cluster upgrade

Fix a duplicate Dev Workspace Operator installation that can occur when an [OLM](https://docs.openshift.com/container-platform/4.22/operators/understanding/olm/olm-understanding-olm.html) restart or OpenShift cluster upgrade leaves multiple Operator entries in a **Replacing** or **Pending** loop.

## Before you begin

- You have an active `oc` session as a cluster administrator to the destination OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You see multiple entries for the Dev Workspace Operator on the **Installed Operators** page of the OpenShift web console. Alternatively, you see one entry that is stuck in a loop of **Replacing** and **Pending**.

## Procedure

1.  Delete the `devworkspace-controller` namespace that contains the failing pod.

2.  Update `DevWorkspace` and `DevWorkspaceTemplate` Custom Resource Definitions (CRD) by setting the conversion strategy to `None` and removing the entire `webhook` section:

    ``` yaml
    spec:
      ...
      conversion:
        strategy: None
    status:
    ...
    ```

    Tip

    You can find and edit the `DevWorkspace` and `DevWorkspaceTemplate` CRDs in the **Administrator** perspective of the OpenShift web console by searching for `DevWorkspace` in Administration<span class="abbr" title="and then"> \> </span>CustomResourceDefinitions.

    Note

    The `DevWorkspaceOperatorConfig` and `DevWorkspaceRouting` CRDs have the conversion strategy set to `None` by default.

3.  Remove the Dev Workspace Operator subscription:

    ``` bash
    $ oc delete sub devworkspace-operator \
    -n <devworkspace_operator_namespace>
    ```

    where:

    ` `*`<devworkspace_operator_namespace>`*` `  
    The project where the Dev Workspace Operator is installed. For OpenShift Dev Spaces 3.29, this is typically `openshift-devspaces`. For standalone Dev Workspace Operator installations, this is `openshift-operators`.

4.  Get the Dev Workspace Operator CSVs in the *\<devworkspace_operator.vX.Y.Z\>* format:

    ``` bash
    $ oc get csv | grep devworkspace
    ```

5.  Remove each Dev Workspace Operator CSV:

    ``` bash
    $ oc delete csv <devworkspace_operator.vX.Y.Z> \
    -n <devworkspace_operator_namespace>
    ```

6.  Re-create the Dev Workspace Operator subscription:

    ``` bash
    $ cat <<EOF | oc apply -f -
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: devworkspace-operator
      namespace: openshift-operators
    spec:
      channel: fast
      name: devworkspace-operator
      source: redhat-operators
      sourceNamespace: openshift-marketplace
      installPlanApproval: Automatic
      startingCSV: devworkspace-operator.v0.41.0
    EOF
    ```

    `installPlanApproval`  
    `Automatic` or `Manual`.

    Important

    For `installPlanApproval: Manual`, in the **Administrator** perspective of the OpenShift web console, go to Operators<span class="abbr" title="and then"> \> </span>Installed Operators and select the following for the **Dev Workspace Operator**: Upgrade available<span class="abbr" title="and then"> \> </span>Preview InstallPlan<span class="abbr" title="and then"> \> </span>Approve.

## Results

- In the **Administrator** perspective of the OpenShift web console, go to Operators<span class="abbr" title="and then"> \> </span>Installed Operators and verify the **Succeeded** status of the **Dev Workspace Operator**.

**Related tasks**  

- [Choose how updates are applied](upgrade-proc_specifying_update_approval_strategy.md "Choose between automatic and manual update approval for the Red Hat OpenShift Dev Spaces Operator so that you control when new versions are installed on your cluster.")
- [Approve a pending update in the web console](upgrade-proc_upgrading_using_web_console.md "Approve a pending OpenShift Dev Spaces Operator update in the OpenShift web console so that your deployment receives the latest bug fixes, security patches, and features at the time you choose.")

**Related information**  

- [Installing the dsc management tool](plan-proc_installing_the_dsc_management_tool.md)
