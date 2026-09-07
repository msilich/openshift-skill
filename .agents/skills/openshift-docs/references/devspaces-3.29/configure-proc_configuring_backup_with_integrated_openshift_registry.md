> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_backup_with_integrated_openshift_registry). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Configure backup with the integrated OpenShift registry

Configure the Dev Workspace backup job to use the integrated OpenShift Container Platform container registry. This option requires no additional authentication configuration.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have the [integrated container registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/registry/setting-up-and-configuring-the-registry) enabled on the cluster.

## Procedure

1.  Configure the `DevWorkspaceOperatorConfig` resource to enable the backup job:

    ``` yaml
    apiVersion: controller.devfile.io/v1alpha1
    kind: DevWorkspaceOperatorConfig
    metadata:
      name: devworkspace-operator-config
      namespace: openshift-operators
    config:
      workspace:
        backupCronJob:
          enable: true
          registry:
            path: <integrated_registry_url>
          oras:
            extraArgs: '--insecure'
          schedule: '0 */4 * * *'
        imagePullPolicy: Always
    ```

    where:

    `openshift-operators`  
    The default installation namespace for the Dev Workspace Operator on OpenShift. If the Dev Workspace Operator is installed in a different namespace, use that namespace instead.

    ` `*`<integrated_registry_url>`*` `  
    The URL to the OpenShift Container Platform integrated registry for your cluster.

    `--insecure`  
    The `--insecure` flag may be required depending on the integrated registry’s routing configuration.

2.  Get the default path to the integrated registry:

    ``` bash
    echo "$(oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}')"
    ```

## Results

- After the backup job completes, verify that the backup archives are available in the integrated registry. Check the Dev Workspace project for a repository with a matching Dev Workspace name.

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

- [Configure backup with a regular OCI-compatible registry](configure-proc_configuring_backup_with_regular_oci_registry.md "Configure the Dev Workspace backup job to use a regular OCI-compatible registry for backups. Provide registry credentials through a Kubernetes Secret in the Operator project or in each Dev Workspace project.")

**Related information**  

- [Setting up and configuring the OpenShift Container Platform registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/registry/setting-up-and-configuring-the-registry)
