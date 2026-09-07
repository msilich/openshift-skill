> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_requesting_persistent_storage_in_a_devfile). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Request persistent storage in a devfile

When a workspace requires its own persistent storage, request a PersistentVolume (PV) in the devfile, and OpenShift Dev Spaces automatically manages the necessary PersistentVolumeClaims.

## Before you begin

- You have not started the workspace.

## Procedure

1.  Add a `volume` component in the devfile:

    ``` yaml
    ...
    components:
      ...
      - name: <chosen_volume_name>
        volume:
          size: <requested_volume_size>G
      ...
    ```

2.  Add a `volumeMount` for the relevant `container` in the devfile:

    ``` yaml
    ...
    components:
      - name: ...
        container:
          ...
          volumeMounts:
            - name: <chosen_volume_name_from_previous_step>
              path: <path_where_to_mount_the_PV>
          ...
    ```

    For example, when a workspace is started with the following devfile, the `cache` PV is provisioned to the `golang` container in the `/.cache` container path:

    ``` yaml
    schemaVersion: 2.1.0
    metadata:
      name: mydevfile
    components:
      - name: golang
        container:
          image: golang
          memoryLimit: 512Mi
          mountSources: true
          command: ['sleep', 'infinity']
          volumeMounts:
            - name: cache
              path: /.cache
      - name: cache
        volume:
          size: 2Gi
    ```

**Related concepts**  

- [Share preconfigured workspace links with your team](develop-assembly_optional_parameters_for_urls.md "Share preconfigured workspace links with your team by appending optional parameters to the URL that starts a new workspace so you can control the IDE, storage, resource limits, and devfile configuration without editing files.")

**Related tasks**  

- [Request persistent storage in a PVC](develop-proc_requesting_persistent_storage_with_pvc.md "Request persistent storage by applying a PersistentVolumeClaim (PVC) to provision a PersistentVolume (PV) for your workspaces, so that data persists beyond workspace restarts and can be shared across workspaces.")
