> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/integrate-proc_creating_workspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create a workspace from the command line

Create a workspace from the command line by applying a `DevWorkspace` custom resource to the cluster. Use this method when your workflow does not permit the OpenShift Dev Spaces dashboard.

## Before you begin

- You have an active `oc` session with permissions to create `DevWorkspace` resources in your project on the cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

- You know your OpenShift Dev Spaces user namespace on the cluster. The user namespace is created automatically when the user first accesses the OpenShift Dev Spaces dashboard. To retrieve it, visit `https://`*`<openshift_dev_spaces_fqdn>`*`/api/kubernetes/namespace` and find the `name` value.

- You are in your OpenShift Dev Spaces user namespace on the cluster. On OpenShift, use `oc` to [display your current namespace or switch to a namespace](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/developer-cli-commands.html#oc-project).

  To create workspaces for other users, create the `DevWorkspace` custom resource in the target user namespace. This namespace must be provisioned by OpenShift Dev Spaces or by the administrator. See [Configuring a user namespace](configure-proc_configuring_a_user_namespace.md).

## About this task

Creating workspaces through the OpenShift Dev Spaces dashboard provides better user experience and configuration benefits compared to using the command line:

- As a user, you are automatically logged in to the cluster.
- OpenShift clients work automatically.
- OpenShift Dev Spaces and its components automatically convert the target Git repository's devfile into the `DevWorkspace` and `DevWorkspaceTemplate` custom resources on the cluster.
- Access to the workspace is secured by default with the `routingClass: che` in the `DevWorkspace` of the workspace.
- Recognition of the `DevWorkspaceOperatorConfig` configuration is managed by OpenShift Dev Spaces.
- Recognition of configurations in `spec.devEnvironments` specified in the `CheCluster` custom resource including:
  - Persistent storage strategy is specified with `devEnvironments.storage`.
  - Default IDE is specified with `devEnvironments.defaultEditor`.
  - Default plugins are specified with `devEnvironments.defaultPlugins`.
  - Container build configuration is specified with `devEnvironments.containerBuildConfiguration`.
  - Available AI providers are configured through an `ai-tool-registry` ConfigMap in the `openshift-devspaces` namespace.

## Procedure

1.  Copy the contents of the target Git repository's devfile to prepare the `DevWorkspace` custom resource.

    For example:

    ``` yaml
    components:
      - name: tooling-container
        container:
          image: quay.io/devfile/universal-developer-image:ubi9-latest
    ```

    For more details, see the [devfile v2 documentation](https://devfile.io/docs/2.2.0/what-is-a-devfile).

2.  Create a `DevWorkspace` custom resource, pasting the devfile contents from the previous step under the `spec.template` field.

    For example:

    ``` yaml
    kind: DevWorkspace
    apiVersion: workspace.devfile.io/v1alpha2
    metadata:
      name: my-devworkspace
      namespace: user1-dev
    spec:
      routingClass: che
      started: true
      contributions:
        - name: ide
          uri: http://devspaces-dashboard.openshift-devspaces.svc.cluster.local:8080/dashboard/api/editors/devfile?che-editor=che-incubator/che-code/latest
      template:
        projects:
          - name: my-project-name
            git:
              remotes:
                origin: https://github.com/eclipse-che/che-docs
        components:
          - name: tooling-container
            container:
              image: quay.io/devfile/universal-developer-image:ubi9-latest
              env:
                - name: CHE_DASHBOARD_URL
                  value: https://<openshift_dev_spaces_fqdn>/dashboard/
    ```

    where:

    name  
    Name of the `DevWorkspace` custom resource. This is the name of the new workspace.

    namespace  
    User namespace, which is the target project for the new workspace.

    started  
    Determines whether the workspace must be started when the `DevWorkspace` custom resource is created.

    contributions  
    URL reference to the [Microsoft Visual Studio Code - Open Source](https://github.com/microsoft/vscode) IDE devfile.

    projects  
    Details about the Git repository to clone into the workspace when it starts.

    components  
    List of components such as workspace containers and volume components.

    CHE_DASHBOARD_URL  
    URL to OpenShift Dev Spaces dashboard.

3.  Apply the `DevWorkspace` custom resource to the cluster.

    ``` bash
    $ oc apply -f <devworkspace>.yaml
    ```

## Results

1.  Verify that the workspace is starting by checking the **PHASE** status of the `DevWorkspace`.

    ``` bash
    $ oc get devworkspaces -n <user_project> --watch
    ```

    Example output:

    ``` shell-session
    NAMESPACE        NAME                  DEVWORKSPACE ID             PHASE      INFO
    user1-dev        my-devworkspace       workspacedf64e4a492cd4701   Starting   Waiting for workspace deployment
    ```

2.  When the workspace has successfully started, its **PHASE** status changes to **Running** in the output of the `oc get devworkspaces` command.

    Example output:

    ``` shell-session
    NAMESPACE            NAME                  DEVWORKSPACE ID             PHASE      INFO
    user1-dev            my-devworkspace       workspacedf64e4a492cd4701   Running    https://url-to-workspace.com
    ```

    You can then open the workspace by using one of these options:

    - Visit the URL provided in the **INFO** section of the output of the `oc get devworkspaces` command.
    - Open the workspace from the OpenShift Dev Spaces dashboard.

**Related concepts**  

- [How workspaces connect to OpenShift](integrate-con_integrating_with_openshift.md "OpenShift Dev Spaces workspaces connect to OpenShift through automatic token injection, the OpenShift CLI, and console navigation.")
- [How OpenShift Dev Spaces appears in the OpenShift console](integrate-con_navigating_devspaces_from_openshift_developer_perspective.md "OpenShift Dev Spaces appears in the OpenShift console through a ConsoleLink Custom Resource that adds an interactive link to the Red Hat Applications menu. When the OpenShift Dev Spaces Operator is deployed into OpenShift Container Platform 4.2 and later, it creates a ConsoleLink Custom Resource (CR). This adds an interactive link to the Red Hat Applications menu for accessing the OpenShift Dev Spaces installation. To access the menu, click the three-by-three matrix icon on the main screen of the OpenShift web console. The OpenShift Dev Spaces Console Link creates a new workspace or redirects you to an existing one. For step-by-step instructions, see Additional resources.")

**Related tasks**  

- [List workspaces from the command line](integrate-proc_listing_all_workspaces.md "List workspaces from the command line to check their status, identify stopped or failed workspaces, and monitor resource usage across your OpenShift Dev Spaces environment. .Prerequisites")
