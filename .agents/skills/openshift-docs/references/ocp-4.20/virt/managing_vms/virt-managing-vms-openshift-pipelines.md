<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat OpenShift Pipelines is a Kubernetes-native CI/CD framework that allows developers to design and run each step of the CI/CD pipeline in its own container.

By using OpenShift Pipelines tasks and the example pipeline, you can do the following:

- Create and manage virtual machines (VMs), persistent volume claims (PVCs), data volumes, and data sources.

- Run commands in VMs.

- Manipulate disk images with `libguestfs` tools.

The tasks are located in the task catalog (ArtifactHub).

The example Windows pipeline is located in the pipeline catalog (ArtifactHub).

# Prerequisites

- You have access to an OpenShift Container Platform cluster with `cluster-admin` permissions.

- You have installed the OpenShift CLI (`oc`).

- You have installed OpenShift Pipelines.

# Supported virtual machine tasks

Automate virtual machine (VM) provisioning and management in your CI/CD workflows with OpenShift Pipelines tasks designed for virtualization. These tasks allow you to manage VMs and their disks as part of your automated deployment pipelines, streamlining VM lifecycle management.

| Task | Description |
|----|----|
| `create-vm-from-manifest` | Create a virtual machine from a provided manifest or with `virtctl`. |
| `create-vm-from-template` | Create a virtual machine from a template. |
| `copy-template` | Copy a virtual machine template. |
| `modify-vm-template` | Modify a virtual machine template. |
| `modify-data-object` | Create or delete data volumes or data sources. |
| `cleanup-vm` | Run a script or a command in a virtual machine and stop or delete the virtual machine afterward. |
| `disk-virt-customize` | Use the `virt-customize` tool to run a customization script on a target PVC. |
| `disk-virt-sysprep` | Use the `virt-sysprep` tool to run a sysprep script on a target PVC. |
| `wait-for-vmi-status` | Wait for a specific status of a virtual machine instance and fail or succeed based on the status. |

Supported virtual machine tasks

> [!NOTE]
> Virtual machine creation in pipelines now utilizes `ClusterInstanceType` and `ClusterPreference` instead of template-based tasks, which have been deprecated. The `create-vm-from-template`, `copy-template`, and `modify-vm-template` commands remain available but are not used in default pipeline tasks.

# Windows EFI installer pipeline

You can run the Windows EFI installer pipeline by using the web console or CLI.

The Windows EFI installer pipeline installs Windows 10, Windows 11, or Windows Server 2022 into a new data volume from a Windows installation image (ISO file). A custom answer file is used to run the installation process.

> [!NOTE]
> The Windows EFI installer pipeline uses a config map file with `sysprep` predefined by OpenShift Container Platform and suitable for Microsoft ISO files. For ISO files pertaining to different Windows editions, it may be necessary to create a new config map file with a system-specific `sysprep` definition.

## Running the example pipelines using the web console

You can run the example pipelines from the **Pipelines** menu in the web console.

<div>

<div class="title">

Procedure

</div>

1.  Click **Pipelines** → **Pipelines** in the side menu.

2.  Select a pipeline to open the **Pipeline details** page.

3.  From the **Actions** list, select **Start**. The **Start Pipeline** dialog is displayed.

4.  Keep the default values for the parameters and then click **Start** to run the pipeline. The **Details** tab tracks the progress of each task and displays the pipeline status.

</div>

## Running the example pipelines using the CLI

Use a `PipelineRun` resource to run the example pipelines. A `PipelineRun` object is the running instance of a pipeline. It instantiates a pipeline for execution with specific inputs, outputs, and execution parameters on a cluster. It also creates a `TaskRun` object for each task in the pipeline.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  To run the Microsoft Windows 11 installer pipeline, create the following `PipelineRun` manifest:

    ``` yaml
    apiVersion: tekton.dev/v1
    kind: PipelineRun
    metadata:
      generateName: windows11-installer-run-
      labels:
        pipelinerun: windows11-installer-run
    spec:
        params:
        -   name: winImageDownloadURL
            value: <windows_image_download_url>
        -   name: acceptEula
            value: false
        pipelineRef:
            params:
            -   name: catalog
                value: redhat-pipelines
            -   name: type
                value: artifact
            -   name: kind
                value: pipeline
            -   name: name
                value: windows-efi-installer
            -   name: version
                value: 4.17
            resolver: hub
        taskRunSpecs:
        -   pipelineTaskName: modify-windows-iso-file
            PodTemplate:
                securityContext:
                    fsGroup: 107
                    runAsUser: 107
    ```

    - For `<windows_image_download_url>`, specify the URL for the Windows 11 64-bit ISO file. The product’s language must be English (United States).

    - Example `PipelineRun` objects have a special parameter, `acceptEula`. By setting this parameter, you are agreeing to the applicable Microsoft user license agreements for each deployment or installation of the Microsoft products. If you set it to false, the pipeline exits at the first task.

2.  Apply the `PipelineRun` manifest:

    ``` terminal
    $ oc apply -f windows11-customize-run.yaml
    ```

</div>

# Removing deprecated or unused resources

You can clean up deprecated or unused resources associated with the Red Hat OpenShift Pipelines Operator.

<div>

<div class="title">

Procedure

</div>

- Remove any remaining OpenShift Pipelines resources from the cluster by running the following command:

  ``` terminal
  $ oc delete clusterroles,rolebindings,serviceaccounts,configmaps,pipelines,tasks \
    --selector 'app.kubernetes.io/managed-by=ssp-operator' \
    --selector 'app.kubernetes.io/component in (tektonPipelines,tektonTasks)' \
    --selector 'app.kubernetes.io/name in (tekton-pipelines,tekton-tasks)' \
    --ignore-not-found \
    --all-namespaces
  ```

  If the Red Hat OpenShift Pipelines Operator custom resource definitions (CRDs) have already been removed, the command may return an error. You can safely ignore this, as all other matching resources will still be deleted.

</div>

# Additional resources

- [Understanding OpenShift Pipelines](https://docs.openshift.com/pipelines/latest/about/understanding-openshift-pipelines.html)

- [Task catalog (ArtifactHub)](https://artifacthub.io/packages/search?repo=redhat-tekton-tasks&sort=relevance&page=1)

- [Windows EFI installer pipeline (ArtifactHub)](https://artifacthub.io/packages/tekton-pipeline/redhat-pipelines/windows-efi-installer)

- [Installing OpenShift Pipelines](https://docs.openshift.com/pipelines/latest/install_config/installing-pipelines.html)

- [Creating CI/CD solutions for applications using Red Hat OpenShift Pipelines](https://docs.openshift.com/pipelines/latest/create/creating-applications-with-cicd-pipelines.html)

- [Creating a Windows VM](../creating_vms_advanced/virt-creating-vms-uploading-images.md#virt-creating-windows-vm_virt-creating-vms-uploading-images)
