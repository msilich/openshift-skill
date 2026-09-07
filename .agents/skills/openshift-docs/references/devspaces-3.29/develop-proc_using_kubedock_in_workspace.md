> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_using_kubedock_in_workspace). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Use Kubedock in a workspace

Use Kubedock to run containers in your workspace when Docker-in-Docker or privileged containers are not available.

## Before you begin

- You have a running OpenShift Dev Spaces workspace.
- You have the Kubedock command-line interface (CLI) (`kubedock`) available in your workspace. It is included in the Universal Developer Image (UDI).

## Procedure

1.  Set the `DOCKER_HOST` environment variable to point to the Kubedock server:

    ``` bash
    export DOCKER_HOST=tcp://127.0.0.1:2475
    ```

2.  Start the Kubedock server in the background:

    ``` bash
    kubedock server --port-forward &
    ```

3.  Use standard Docker commands that Kubedock handles:

    ``` bash
    docker run --rm hello-world
    ```

## Results

- The container runs successfully and outputs its message.

**Related concepts**  

- [How kubedock works](develop-con_running_containers_with_kubedock.md "Kubedock is a minimal container engine implementation that gives you a Podman-/docker-like experience inside an OpenShift Dev Spaces workspace.")

**Related information**  

- [Kubedock GitHub repository](https://github.com/joyrex2001/kubedock)
