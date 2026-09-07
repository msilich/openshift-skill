> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_mounting_secret_configmap_as_subpath). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Add individual files without replacing directories

Add individual files from an OpenShift Secret or a ConfigMap to a target directory without replacing existing contents. Use a subPath mount when the target directory already contains files that must be preserved.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have a running instance of Red Hat OpenShift Dev Spaces.

## Procedure

1.  Create a new OpenShift Secret or a ConfigMap in the OpenShift project where OpenShift Dev Spaces is deployed with the required labels:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: custom-settings
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: <DEPLOYMENT_NAME>-<OBJECT_KIND>
    ...
    ```

    where:

    `kind`  
    `Secret` for a Secret or `ConfigMap` for a ConfigMap.

    `<DEPLOYMENT_NAME>`  
    Target deployment: `devspaces`, `devspaces-dashboard`, `devfile-registry`, or `plugin-registry`.

    `<OBJECT_KIND>`  
    `secret` for a Secret or `configmap` for a ConfigMap.

2.  Configure the annotation values. Annotations must indicate that the given object is mounted as a subPath:
    - `che.eclipse.org/mount-as: subpath` - Mounts an object as a subPath.

    - `che.eclipse.org/mount-path: `*`<TARGET_PATH>`* - To provide a required mount path.

      For a Secret:

      ``` yaml
      apiVersion: v1
      kind: Secret
      metadata:
        name: custom-data
        annotations:
          che.eclipse.org/mount-as: subpath
          che.eclipse.org/mount-path: /data
        labels:
          app.kubernetes.io/part-of: che.eclipse.org
          app.kubernetes.io/component: devspaces-secret
      ...
      ```

      For a ConfigMap:

      ``` yaml
      apiVersion: v1
      kind: ConfigMap
      metadata:
        name: custom-data
        annotations:
          che.eclipse.org/mount-as: subpath
          che.eclipse.org/mount-path: /data
        labels:
          app.kubernetes.io/part-of: che.eclipse.org
          app.kubernetes.io/component: devspaces-configmap
      ...
      ```

3.  Add data items to the object. Each item name must match the file name mounted into the container.

    For a Secret:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: custom-data
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: devspaces-secret
      annotations:
        che.eclipse.org/mount-as: subpath
        che.eclipse.org/mount-path: /data
    data:
      ca.crt: <base64 encoded data content here>
    ```

    For a ConfigMap:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: custom-data
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: devspaces-configmap
      annotations:
        che.eclipse.org/mount-as: subpath
        che.eclipse.org/mount-path: /data
    data:
      ca.crt: <data content here>
    ```

## Results

- Verify that the file is mounted in the target container:

  ``` bash
  oc exec -n openshift-devspaces deploy/<DEPLOYMENT_NAME> -- ls <TARGET_PATH>/<FILE_NAME>
  ```

  Each data item name in the object corresponds to a file name at the mount path. For example, a data item named `ca.crt` with a mount path of `/data` results in a file at `/data/ca.crt`.

  Important

  If you update the Secret or ConfigMap data, re-create the object entirely to make the changes visible in the OpenShift Dev Spaces container.

**Related tasks**  

- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md "Edit the CheCluster Custom Resource YAML file to customize the behavior of a running OpenShift Dev Spaces instance for your environment.")

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
