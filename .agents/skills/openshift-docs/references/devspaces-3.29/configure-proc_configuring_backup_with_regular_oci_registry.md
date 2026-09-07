> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_backup_with_regular_oci_registry). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Configure backup with a regular OCI-compatible registry

Configure the Dev Workspace backup job to use a regular OCI-compatible registry for backups. Provide registry credentials through a Kubernetes Secret in the Operator project or in each Dev Workspace project.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have credentials for an OCI-compatible registry such as [Quay.io](https://quay.io).

## About this task

A Secret in the Dev Workspace project enables using different registry accounts per project with more granular access control.

## Procedure

1.  Configure the `DevWorkspaceOperatorConfig` resource to enable the backup job:

    ``` yaml
    kind: DevWorkspaceOperatorConfig
    apiVersion: controller.devfile.io/v1alpha1
    metadata:
      name: devworkspace-operator-config
      namespace: openshift-operators
    config:
      workspace:
        backupCronJob:
          enable: true
          registry:
            authSecret: devworkspace-backup-registry-auth
            path: <registry_url>
          schedule: '0 */4 * * *'
        imagePullPolicy: Always
    ```

    where:

    `openshift-operators`  
    The default installation namespace for the Dev Workspace Operator on OpenShift. If the Dev Workspace Operator is installed in a different namespace, use that namespace instead.

    ` `*`<registry_url>`*` `  
    The OCI registry URL. For example: `quay.io/my-company-org`.

    The `authSecret` must be named `devworkspace-backup-registry-auth`. It must reference a Kubernetes Secret of type `kubernetes.io/dockerconfigjson` that contains credentials to access the registry. Create the Secret in the installation project for the Dev Workspace Operator.

2.  Create the registry credentials Secret:

    ``` bash
    oc create secret docker-registry devworkspace-backup-registry-auth --from-file=config.json -n openshift-operators
    ```

3.  Add the required label to the Secret for the Dev Workspace Operator to recognize it:

    ``` bash
    oc label secret devworkspace-backup-registry-auth controller.devfile.io/watch-secret=true -n openshift-operators
    ```

    Warning

    The Dev Workspace Operator copies the `devworkspace-backup-registry-auth` Secret to each Dev Workspace project so that backups from user workspaces can be pushed to the registry. To use different credentials per project, create a `devworkspace-backup-registry-auth` Secret with user-specific credentials in each Dev Workspace project instead.

## Results

- After the backup job completes, verify that the backup archives are available in the OCI registry under the expected path.

Note

If the installation project for the Dev Workspace Operator is not `openshift-operators`, you must define it as an environment variable for the Red Hat OpenShift Dev Spaces dashboard in the `CheCluster` Custom Resource.

``` yaml
apiVersion: org.eclipse.che/v2
kind: CheCluster
spec:
  components:
    dashboard:
      deployment:
        containers:
          - env:
              - name: DWO_NAMESPACE
                value: <operator_install_namespace>
            name: che-dashboard
```

where:

` `*`<operator_install_namespace>`*` `  
The project where the Dev Workspace Operator is installed. The default installation project for the Dev Workspace Operator on OpenShift is `openshift-operators`.

For more information, see [Dev Workspace Operator](discover-con_devworkspace_operator.md).

**Related tasks**  

- [Configure backup with the integrated OpenShift registry](configure-proc_configuring_backup_with_integrated_openshift_registry.md "Configure the Dev Workspace backup job to use the integrated OpenShift Container Platform container registry. This option requires no additional authentication configuration.")
