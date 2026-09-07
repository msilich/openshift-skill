> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_enabling_container_run_capabilities). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Run nested containers in workspaces

Run nested containers in OpenShift Dev Spaces workspaces using tools like Podman. This feature uses Linux kernel user namespaces for isolation, so that users can build and run container images within their workspaces.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have an instance of OpenShift Dev Spaces running in OpenShift.

## About this task

Important

Previously created workspaces cannot be started after enabling this feature. Users must create new workspaces.

Important

- This feature is available on OpenShift 4.20 and later versions.

## Procedure

Configure the `CheCluster` custom resource to enable container run capabilities:

``` bash
oc patch checluster/devspaces -n openshift-devspaces \
  --type='merge' -p \
  '{"spec":{"devEnvironments":{"disableContainerRunCapabilities":false}}}'
```

## Results

- Create a new workspace and verify that Podman is available:

  ``` bash
  podman run --rm hello-world
  ```

**Related information**  

- [Linux user namespace support](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/containers-using-userns_nodes-containers-using)
