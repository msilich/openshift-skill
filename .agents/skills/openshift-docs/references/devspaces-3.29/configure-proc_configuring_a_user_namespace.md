> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_a_user_namespace). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Synchronize resources across user namespaces

Synchronize `ConfigMaps`, `Secrets`, `PersistentVolumeClaims`, and other Kubernetes objects from the `openshift-devspaces` namespace to user-specific namespaces to provide consistent workspace configurations.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

Warning

Applying or modifying a `Secret` or `ConfigMap` with the `controller.devfile.io/mount-to-devworkspace: 'true'` label restarts all running workspaces in the project.

To mount the `Secret` or `ConfigMap` only at workspace start and prevent automatic restarts, add the `controller.devfile.io/mount-on-start: 'true'` annotation.

## About this task

If you make changes to a Kubernetes resource in the openshift-devspaces namespace, OpenShift Dev Spaces immediately synchronizes the changes across all user namespaces. In reverse, if a Kubernetes resource is modified in a user namespace, OpenShift Dev Spaces immediately reverts the changes.

## Procedure

1.  Create the following `ConfigMap` to mount it into every workspace:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: devspaces-user-configmap
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: workspaces-config
    data:
      ...
    ```

    Optional: Use annotations to configure how the ConfigMap is mounted.

    <span id="proc_configuring-a-user-namespace_devspaces__entry__1"></span><span id="proc_configuring-a-user-namespace_devspaces__entry__2"></span>

    | Annotation | Description |
    |----|----|
    | `che.eclipse.org/sync-retain-on-delete:` | When set to `"true"`, the ConfigMap is retained in a user namespace after being deleted from `openshift-devspaces` namespace. |
    | `controller.devfile.io/mount-on-start:` | When set to `"true"`, the ConfigMap is mounted only at workspace start. This prevents workspace restarts when the ConfigMap is created. |
    | `controller.devfile.io/mount-to-devworkspace-include:` | Specifies a comma-separated list of `Dev Workspace` name patterns. When set, the ConfigMap is mounted only to workspaces whose names match at least one pattern. Patterns support exact match, prefix (name\*), suffix (\*name), contains (\*name\*). |
    | `controller.devfile.io/mount-to-devworkspace-exclude:` | Specifies a comma-separated list of `Dev Workspace` name patterns. When set, the ConfigMap is mounted to all workspaces except those whose names match a pattern. Patterns support exact match, prefix (name\*), suffix (\*name), contains (\*name\*). |

    Table 1. Optional annotations

    Note

    When both annotations `controller.devfile.io/mount-to-devworkspace-include` and `controller.devfile.io/mount-to-devworkspace-exclude` are set, the resource is mounted only to workspaces that match the include pattern and do not match the exclude pattern.

    For other labels and annotations, see the [mounting volumes, configmaps, and secrets](https://github.com/devfile/devworkspace-operator/blob/main/docs/additional-configuration.adoc#automatically-mounting-volumes-configmaps-and-secrets).

    For example, to mount a default SSH configuration into every workspace, create a ConfigMap:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: ssh-config-configmap
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/component: workspaces-config
        app.kubernetes.io/part-of: che.eclipse.org
      annotations:
        controller.devfile.io/mount-as: subpath
        controller.devfile.io/mount-path: /etc/ssh/ssh_config.d/
    data:
      ssh.conf: <ssh_config_content>
    ```

    The ConfigMap propagates the SSH configuration as an extension by using `Include /etc/ssh/ssh_config.d/*.conf`. For details, see [Include definition](https://man.openbsd.org/ssh_config#Include).

2.  Create the following `Secret` to mount it into every workspace:

    ``` yaml
    kind: Secret
    apiVersion: v1
    metadata:
      name: devspaces-user-secret
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: workspaces-config
    stringData:
        ...
    ```

    Optional: Use annotations to configure how the Secret is mounted.

    <span id="proc_configuring-a-user-namespace_devspaces__entry__11"></span><span id="proc_configuring-a-user-namespace_devspaces__entry__12"></span>

    | Annotation | Description |
    |----|----|
    | `che.eclipse.org/sync-retain-on-delete:` | When set to `"true"`, the Secret is retained in a user namespace after being deleted from `openshift-devspaces` namespace. |
    | `controller.devfile.io/mount-on-start:` | When set to `"true"`, the Secret is mounted only at workspace start. This prevents workspace restarts when the Secret is created. |
    | `controller.devfile.io/mount-to-devworkspace-include:` | Specifies a comma-separated list of `Dev Workspace` name patterns. When set, the Secret is mounted only to workspaces whose names match at least one pattern. Patterns support exact match, prefix (name\*), suffix (\*name), contains (\*name\*). |
    | `controller.devfile.io/mount-to-devworkspace-exclude:` | Specifies a comma-separated list of `Dev Workspace` name patterns. When set, the Secret is mounted to all workspaces except those whose names match a pattern. Patterns support exact match, prefix (name\*), suffix (\*name), contains (\*name\*). |

    Table 2. Optional annotations

    Note

    When both annotations `controller.devfile.io/mount-to-devworkspace-include` and `controller.devfile.io/mount-to-devworkspace-exclude` are set, the resource is mounted only to workspaces that match the include pattern and do not match the exclude pattern.

    For other labels and annotations, see the [mounting volumes, configmaps, and secrets](https://github.com/devfile/devworkspace-operator/blob/main/docs/additional-configuration.adoc#automatically-mounting-volumes-configmaps-and-secrets).

3.  Create the following `PersistentVolumeClaim` for every user project:

    ``` yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: devspaces-user-pvc
      namespace: openshift-devspaces
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: workspaces-config
    spec:
      ...
    ```

    Optional: Use annotations to configure how the `PersistentVolumeClaim` is mounted.

    Note

    The `PersistentVolumeClaim` is not deleted in a user namespace by default if the one from `openshift-devspaces` is deleted.

    <span id="proc_configuring-a-user-namespace_devspaces__entry__21"></span><span id="proc_configuring-a-user-namespace_devspaces__entry__22"></span>

    | Annotation | Description |
    |----|----|
    | `che.eclipse.org/sync-retain-on-delete:` | When set to `"false"`, the `PersistentVolumeClaim` is deleted in a user namespace when it is deleted from `openshift-devspaces` namespace. |
    | `controller.devfile.io/mount-on-start:` | When set to `"true"`, the `PersistentVolumeClaim` is mounted only at workspace start. This prevents workspace restarts when the `PersistentVolumeClaim` is created. |
    | `controller.devfile.io/mount-to-devworkspace-include:` | Specifies a comma-separated list of `Dev Workspace` name patterns. When set, the `PersistentVolumeClaim` is mounted only to workspaces whose names match at least one pattern. Patterns support exact match, prefix (name\*), suffix (\*name), contains (\*name\*). |
    | `controller.devfile.io/mount-to-devworkspace-exclude:` | Specifies a comma-separated list of `Dev Workspace` name patterns. When set, the `PersistentVolumeClaim` is mounted to all workspaces except those whose names match a pattern. Patterns support exact match, prefix (name\*), suffix (\*name), contains (\*name\*). |

    Table 3. Optional annotations

    Note

    When both annotations `controller.devfile.io/mount-to-devworkspace-include` and `controller.devfile.io/mount-to-devworkspace-exclude` are set, the resource is mounted only to workspaces that match the include pattern and do not match the exclude pattern.

    For other labels and annotations, see the [mounting volumes, configmaps, and secrets](https://github.com/devfile/devworkspace-operator/blob/main/docs/additional-configuration.adoc#automatically-mounting-volumes-configmaps-and-secrets).

4.  Optional: To use the OpenShift Kubernetes Engine, create a `Template` object to replicate all resources defined within the template across each user project.

    Aside from the previously mentioned `ConfigMap`, `Secret`, and `PersistentVolumeClaim`, `Template` objects can include:

    - `LimitRange`

    - `NetworkPolicy`

    - `ResourceQuota`

    - `Role`

    - `RoleBinding`

      ``` yaml
      apiVersion: template.openshift.io/v1
      kind: Template
      metadata:
        name: devspaces-user-namespace-configurator
        namespace: openshift-devspaces
        labels:
          app.kubernetes.io/part-of: che.eclipse.org
          app.kubernetes.io/component: workspaces-config
      objects:
        ...
      parameters:
      - name: PROJECT_NAME
      - name: PROJECT_ADMIN_USER
      ```

      The `parameters` are optional and define which parameters can be used. Currently, only `PROJECT_NAME` and `PROJECT_ADMIN_USER` are supported. `PROJECT_NAME` is the name of the OpenShift Dev Spaces namespace, while `PROJECT_ADMIN_USER` is the OpenShift Dev Spaces user of the namespace.

      The namespace name in objects is replaced with the user’s namespace name during synchronization.

      For example, a Template that replicates `ResourceQuota`, `LimitRange`, `Role`, and `RoleBinding` objects:

      ``` yaml
      apiVersion: template.openshift.io/v1
      kind: Template
      metadata:
        name: devspaces-user-namespace-configurator
        namespace: openshift-devspaces
        labels:
          app.kubernetes.io/part-of: che.eclipse.org
          app.kubernetes.io/component: workspaces-config
      objects:
      - apiVersion: v1
        kind: ResourceQuota
        metadata:
          name: devspaces-user-resource-quota
        spec:
          ...
      - apiVersion: v1
        kind: LimitRange
        metadata:
          name: devspaces-user-resource-constraint
        spec:
          ...
      - apiVersion: rbac.authorization.k8s.io/v1
        kind: Role
        metadata:
          name: devspaces-user-roles
        rules:
          ...
      - apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: devspaces-user-rolebinding
        roleRef:
          apiGroup: rbac.authorization.k8s.io
          kind: Role
          name: devspaces-user-roles
        subjects:
        - kind: User
          apiGroup: rbac.authorization.k8s.io
          name: ${PROJECT_ADMIN_USER}
      parameters:
      - name: PROJECT_ADMIN_USER
      ```

      Note

      Creating Template Kubernetes resources is supported only on OpenShift.

## Results

- Verify that the Kubernetes objects are synchronized to a user project:

  ``` bash
  $ oc get configmaps,secrets -n <user_namespace> -l app.kubernetes.io/part-of=che.eclipse.org
  ```

**Related information**  

- [Mounting ConfigMaps](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop/index#mounting-configmaps_develop)
- [Mounting Secrets](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/develop/index#mounting-secrets_develop)
- [Requesting persistent storage for workspaces](develop-con_requesting_persistent_storage_for_workspaces.md)
- [Automatically mounting volumes, configmaps, and secrets](https://github.com/devfile/devworkspace-operator/blob/main/docs/additional-configuration.adoc#automatically-mounting-volumes-configmaps-and-secrets)
- [OpenShift API reference for](https://docs.openshift.com/container-platform/4.22/rest_api/template_apis/template-template-openshift-io-v1.html)
- [Configuring OpenShift project creation](https://docs.openshift.com/container-platform/4.22/applications/projects/configuring-project-creation.html)
