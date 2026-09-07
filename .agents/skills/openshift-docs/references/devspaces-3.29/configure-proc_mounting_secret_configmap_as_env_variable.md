> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_mounting_secret_configmap_as_env_variable). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Inject environment variables from Secrets and ConfigMaps

Inject configuration values from an OpenShift Secret or a ConfigMap as environment variables in an OpenShift Dev Spaces container, such as credentials, API keys, or feature flags, without modifying the container image.

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

2.  Configure the annotation values. Annotations must indicate that the given object is mounted as an environment variable:
    - `che.eclipse.org/mount-as: env` - Mounts an object as an environment variable.

    - `che.eclipse.org/env-name: `*`<FOO_ENV>`* - Provides the environment variable name, which is required to mount an object key value.

      For a Secret:

      ``` yaml
      apiVersion: v1
      kind: Secret
      metadata:
        name: custom-settings
        annotations:
          che.eclipse.org/env-name: FOO_ENV
          che.eclipse.org/mount-as: env
        labels:
          app.kubernetes.io/part-of: che.eclipse.org
          app.kubernetes.io/component: devspaces-secret
      stringData:
        mykey: myvalue
      ```

      For a ConfigMap:

      ``` yaml
      apiVersion: v1
      kind: ConfigMap
      metadata:
        name: custom-settings
        annotations:
          che.eclipse.org/env-name: FOO_ENV
          che.eclipse.org/mount-as: env
        labels:
          app.kubernetes.io/part-of: che.eclipse.org
          app.kubernetes.io/component: devspaces-configmap
      data:
        mykey: myvalue
      ```

3.  If the object provides more than one data item, provide the environment variable name for each data key by using the `che.eclipse.org/`*`<key>`*`_env-name` annotation format.

    For a Secret:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: custom-settings
      annotations:
        che.eclipse.org/mount-as: env
        che.eclipse.org/mykey_env-name: FOO_ENV
        che.eclipse.org/otherkey_env-name: OTHER_ENV
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: devspaces-secret
    stringData:
      mykey: <data_content_here>
      otherkey: <data_content_here>
    ```

    For a ConfigMap:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: custom-settings
      annotations:
        che.eclipse.org/mount-as: env
        che.eclipse.org/mykey_env-name: FOO_ENV
        che.eclipse.org/otherkey_env-name: OTHER_ENV
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
        app.kubernetes.io/component: devspaces-configmap
    data:
      mykey: <data content here>
      otherkey: <data content here>
    ```

    The maximum length of annotation names in an OpenShift object is 63 characters, where 9 characters are reserved for a prefix that ends with `/`. This restricts the maximum length of the key that can be used for the object.

## Results

- Verify that the environment variable is set in the target container:

  ``` bash
  oc exec -n openshift-devspaces deploy/<DEPLOYMENT_NAME> -- env | grep <ENV_NAME>
  ```

  For a single-key object, both the `env-name` value and the data key name become environment variables. For a multi-key object, only the per-key `env-name` values are provisioned.

  Important

  If you update the Secret or ConfigMap data, re-create the object entirely to make the changes visible in the OpenShift Dev Spaces container.

**Related tasks**  

- [Edit the central configuration from the command line](configure-proc_using_cli_to_configure_checluster.md "Edit the CheCluster Custom Resource YAML file to customize the behavior of a running OpenShift Dev Spaces instance for your environment.")

**Related information**  

- [Configuring the CheCluster Custom Resource during installation](install-proc_using_dsc_to_configure_checluster_during_installation.md)
