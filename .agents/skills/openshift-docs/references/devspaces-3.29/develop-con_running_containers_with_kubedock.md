> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-con_running_containers_with_kubedock). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How kubedock works

Kubedock is a minimal container engine implementation that gives you a Podman-/docker-like experience inside an OpenShift Dev Spaces workspace.

Kubedock is especially useful when dealing with ad-hoc, ephemeral, and testing containers, such as in the use cases listed below:

- Executing application tests which rely on the Testcontainers framework.
- Using Quarkus Dev Services.
- Running a container stored in remote container registry, for local development purposes

For more information about these frameworks, see Additional resources.

Important

The image you want to use with kubedock must be compliant with OpenShift Container Platform image creation guidelines. Otherwise, running the image with kubedock results in a failure even if the same image runs locally without issues.

<span id="con_running-containers-with-kubedock_devspaces___supported_commands"></span>

## [Supported commands](develop-con_running_containers_with_kubedock.md#con_running-containers-with-kubedock_devspaces___supported_commands)

After enabling the kubedock environment variable, kubedock runs the following `podman` commands:

- `podman run`
- `podman ps`
- `podman exec`
- `podman cp`
- `podman logs`
- `podman inspect`
- `podman kill`
- `podman rm`
- `podman wait`
- `podman stop`
- `podman start`

Other commands such as `podman build` are started by the local Podman.

Important

Using `podman` commands with kubedock has the following limitations:

- The `podman build -t <image> . && podman run <image>` command fails. Use `podman build -t <image> . && podman push <image> && podman run <image>` instead.
- The `podman generate kube` command is not supported.
- `--env` option causes the `podman run` command to fail.

To enable and use kubedock in your workspace, see Additional resources.

**Related tasks**  

- [Enable kubedock in a workspace](develop-proc_enabling_kubedock.md "Enable kubedock in an OpenShift Dev Spaces workspace by adding environment variables to the devfile.")
- [Use Kubedock in a workspace](develop-proc_using_kubedock_in_workspace.md "Use Kubedock to run containers in your workspace when Docker-in-Docker or privileged containers are not available.")

**Related information**  

- [Kubedock GitHub repository](https://github.com/joyrex2001/kubedock)
- [Testcontainers](https://testcontainers.com/)
- [Quarkus Dev Services](https://quarkus.io/guides/dev-services)
- [OpenShift Container Platform image creation guidelines](https://docs.openshift.com/container-platform/4.22/openshift_images/create-images.html#images-create-guide-openshift_create-images)
