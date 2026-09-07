> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-con_diagnose_slow_workspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Diagnose slow workspaces

Diagnose slow workspace runtime performance by tuning CPU and memory resource limits in your devfile.

<span id="con_diagnose-slow-workspaces_devspaces___improve_workspace_runtime_performance"></span>

## [Improve workspace runtime performance](troubleshoot-con_diagnose_slow_workspaces.md#con_diagnose-slow-workspaces_devspaces___improve_workspace_runtime_performance)

Provide enough CPU resources  
Plugins consume CPU resources. For example, when a plugin provides IntelliSense features, adding more CPU resources can improve performance.

Ensure the CPU settings in the devfile definition, `devfile.yaml`, are correct:

``` yaml
components:
  - name: tools
    container:
      image: quay.io/devfile/universal-developer-image:ubi8-latest
      cpuLimit: 4000m
      cpuRequest: 1000m
```

cpuLimit  
Specifies the CPU limit.

cpuRequest  
Specifies the CPU request.

Provide enough memory  
Plug-ins consume CPU and memory resources. For example, when a plugin provides IntelliSense features, collecting data can consume all the memory allocated to the container.

Providing more memory to the container can increase performance. Ensure that memory settings in the devfile definition `devfile.yaml` file are correct.

``` yaml
components:
  - name: tools
    container:
      image: quay.io/devfile/universal-developer-image:ubi8-latest
      memoryLimit: 6G
      memoryRequest: 512Mi
```

memoryLimit  
Specifies the memory limit.

memoryRequest  
Specifies the memory request.

**Related information**  

- [Diagnose slow Cloud Development Environments](troubleshoot-con_diagnose_slow_cdes.md)
