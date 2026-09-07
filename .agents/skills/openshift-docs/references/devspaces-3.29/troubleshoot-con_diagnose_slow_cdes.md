> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/troubleshoot-con_diagnose_slow_cdes). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Diagnose slow Cloud Development Environments

Diagnose slow Cloud Development Environment startup by pre-pulling images, tuning storage strategy, installing offline, and reducing public endpoints.

<span id="con_diagnose-slow-cdes_devspaces___reduce_workspace_start_time"></span>

## [Reduce workspace start time](troubleshoot-con_diagnose_slow_cdes.md#con_diagnose-slow-cdes_devspaces___reduce_workspace_start_time)

Cache images with Image Puller  
When starting a workspace, OpenShift pulls the images from the registry. A workspace can include many containers meaning that OpenShift pulls Pod’s images (one per container). Depending on the size of the image and the bandwidth, it can take a long time.

Image Puller is a tool that can cache images on each of OpenShift nodes. As such, pre-pulling images can improve start times.

Choose a faster storage type  
Every workspace has a shared volume attached. This volume stores the project files, so that when restarting a workspace, changes are still available. Depending on the storage, attach time can take up to a few minutes, and I/O can be slow.

Install in offline mode  
Components of OpenShift Dev Spaces are OCI images. Configure Red Hat OpenShift Dev Spaces in offline mode to reduce any extra download at runtime because everything needs to be available from the beginning.

Reduce the number of public endpoints  
For each endpoint, OpenShift is creating OpenShift Route objects. Depending on the underlying configuration, this creation can be slow.

To avoid this problem, reduce the exposure. For example, Microsoft Visual Code - Open Source has three optional routes. These routes automatically detect a new port listening inside containers and redirect traffic for processes using a local IP address (`127.0.0.1`).

By reducing the number of endpoints and checking endpoints of all plugins, workspace start can be faster.

**Related information**  

- [Speed up workspace starts with image caching](optimize-assembly_caching_images_for_faster_workspace_start.md)
- [Install OpenShift Dev Spaces in a restricted environment](install-proc_installing_dev_spaces_in_a_restricted_environment_on_openshift.md)
- [Diagnose slow workspaces](troubleshoot-con_diagnose_slow_workspaces.md)
