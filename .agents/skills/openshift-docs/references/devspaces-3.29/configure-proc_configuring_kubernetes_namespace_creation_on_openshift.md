> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_kubernetes_namespace_creation_on_openshift). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Use Kubernetes namespaces instead of OpenShift projects

Use standard Kubernetes namespaces directly on OpenShift Container Platform instead of using the ProjectRequest API to bypass cluster-specific Project Templates.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

By default, on OpenShift Container Platform clusters, OpenShift Dev Spaces uses the ProjectRequest API to create projects. This triggers cluster-specific [Project Templates](https://docs.openshift.com/container-platform/4.22/applications/projects/configuring-project-creation.html), which can apply additional resources or policies.

On OpenShift Container Platform, you can bypass Project Templates and create standard Kubernetes namespaces directly. For example, this is useful when Project Templates introduce unwanted side effects.

## Procedure

Set the `createKubernetesNamespaces` field to `true`:

``` plaintext
oc patch checluster devspaces \
  --namespace openshift-devspaces \
  --type merge \
  --patch '{
    "spec": {
      "devEnvironments": {
        "defaultNamespace": {
          "createKubernetesNamespaces": true
        }
      }
    }
  }'
```

Note

This setting applies only to OpenShift Container Platform clusters. On Kubernetes clusters, namespaces are always created directly regardless of this setting.

## Results

- Verify the configuration:

  ``` plaintext
  oc get checluster devspaces \
    --namespace openshift-devspaces \
    --output jsonpath='{.spec.devEnvironments.defaultNamespace.createKubernetesNamespaces}'
  ```

  The command returns `true`.

**Related tasks**  

- [Set the workspace namespace naming convention](configure-proc_configuring_project_name.md "Set the project name template that OpenShift Dev Spaces uses when creating workspace projects to enforce naming conventions and organizational compliance.")
- [Synchronize resources across user namespaces](configure-proc_configuring_a_user_namespace.md "Synchronize ConfigMaps, Secrets, PersistentVolumeClaims, and other Kubernetes objects from the openshift-devspaces namespace to user-specific namespaces to provide consistent workspace configurations.")

**Related information**  

- [Configuring OpenShift project creation](https://docs.openshift.com/container-platform/4.22/applications/projects/configuring-project-creation.html)
