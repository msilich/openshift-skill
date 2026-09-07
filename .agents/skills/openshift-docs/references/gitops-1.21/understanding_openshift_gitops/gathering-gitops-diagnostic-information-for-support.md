<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When you open a support case, you must provide debugging information about your cluster to the Red Hat Support team. You can use the `must-gather` tool to collect diagnostic information for project-level resources, cluster-level resources, and Red Hat OpenShift GitOps components.

> [!NOTE]
> For prompt support, provide diagnostic information for both OpenShift Container Platform and Red Hat OpenShift GitOps.

# About the must-gather tool

The `oc adm must-gather` CLI command collects the information from your cluster that is most likely needed for debugging issues, including:

- Resource definitions

- Service logs

By default, the `oc adm must-gather` command uses the default plugin image and writes into `./must-gather.local`.

Alternatively, you can collect specific information by running the command with the appropriate arguments as described in the following sections:

- To collect data related to one or more specific features, use the `--image` argument with an image, as listed in a following section.

  **Example command:**

<!-- -->

    $ oc adm must-gather --image=registry.redhat.io/openshift-gitops-1/must-gather-rhel9:v1.20.0

- To collect the audit logs, use the `-- /usr/bin/gather_audit_logs` argument, as described in a following section.

  **Example command:**

  ``` terminal
  $ oc adm must-gather -- /usr/bin/gather_audit_logs
  ```

  > [!NOTE]
  > Audit logs are not collected as part of the default set of information to reduce the size of the files.

When you run `oc adm must-gather`, a new pod with a random name is created in a new project on the cluster. The data is collected on that pod and saved in a new directory that starts with `must-gather.local`. This directory is created in the current working directory.

**Example pod:**

``` terminal
NAMESPACE                      NAME                 READY   STATUS      RESTARTS      AGE
...
openshift-must-gather-5drcj    must-gather-bklx4    2/2     Running     0             72s
openshift-must-gather-5drcj    must-gather-s8sdh    2/2     Running     0             72s
...
```

Optionally, you can run the `oc adm must-gather` command in a specific namespace by using the `--run-namespace` option.

**Example command:**

``` terminal
$ oc adm must-gather --image=registry.redhat.io/openshift-gitops-1/must-gather-rhel9:v1.20.0
```

> [!NOTE]
> For versions of Red Hat OpenShift GitOps earlier than v1.20.0, the GitOps components use container images based on RHEL 8, for example, `registry.redhat.io/openshift-gitops-1/must-gather-rhel8`. When collecting debugging information using the must-gather tool, ensure that you reference the RHEL 8 based GitOps must-gather image that matches the installed GitOps version.

# Collecting debugging data for Red Hat OpenShift GitOps

Use the `oc adm must-gather` CLI command to collect the following details about the cluster that is associated with Red Hat OpenShift GitOps:

- The subscription and namespace of the Red Hat OpenShift GitOps Operator.

- The namespaces where ArgoCD objects are available and the objects in those namespaces, such as `ArgoCD`, `Applications`, `ApplicationSets`, `AppProjects`, and `configmaps`.

- A list of the namespaces that are managed by the Red Hat OpenShift GitOps Operator, and resources from those namespaces.

- All GitOps-related custom resource objects and definitions.

- Operator and Argo CD logs.

- Warning and error-level events.

> [!NOTE]
> For versions of Red Hat OpenShift GitOps earlier than v1.20.0, the GitOps components use container images based on RHEL 8, for example, `registry.redhat.io/openshift-gitops-1/must-gather-rhel8`. When collecting debugging information using the must-gather tool, ensure that you reference the RHEL 8 based GitOps must-gather image that matches the installed GitOps version.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the OpenShift Container Platform CLI (`oc`).

- You have installed the Red Hat OpenShift GitOps Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the directory where you want to store the debugging information.

2.  Run the `oc adm must-gather` command with the Red Hat OpenShift GitOps `must-gather` image:

    ``` terminal
    $ oc adm must-gather --image=registry.redhat.io/openshift-gitops-1/must-gather-rhel8:<image_version_tag>
    ```

    where:

    `<image_version_tag>`
    Specifies the must-gather image version tag for GitOps.

    **Example command:**

    ``` terminal
    $ oc adm must-gather --image=registry.redhat.io/openshift-gitops-1/must-gather-rhel9:v1.20.0
    ```

    The `must-gather` tool creates a new directory that starts with `./must-gather.local` in the current directory. For example, `./must-gather.local.4157245944708210399`.

3.  Create a compressed file from the directory that was just created. For example, on a computer that uses a Linux operating system, run the following command:

    ``` terminal
    $ tar -cvaf must-gather.tar.gz must-gather.local.4157245944708210399
    ```

    where:

    `<must-gather-local.4157245944708210399>`
    Specifies the actual directory name.

4.  Attach the compressed file to your support case on the [Red Hat Customer Portal](https://access.redhat.com/).

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the compressed file exists in your current directory:

    ``` terminal
    $ ls -lh must-gather.tar.gz
    ```

    **Example output:**

    ``` terminal
    -rw-r--r--. 1 user user 2.5M Mar 17 18:30 must-gather.tar.gz
    ```

</div>

# Additional resources

- [Gathering data about specific features](https://docs.openshift.com/container-platform/latest/support/gathering-cluster-data.html#gathering-data-specific-features_gathering-cluster-data)
