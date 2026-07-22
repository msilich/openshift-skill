<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can update a cluster in a disconnected environment without using the OpenShift Update Service.

Use the following procedures to update a cluster in a disconnected environment without access to the OpenShift Update Service.

# Prerequisites for a cluster update

You must meet several prerequisites before updating a cluster in a disconnected environment.

The following prerequisites must be met:

- You must have the `oc` command-line interface (CLI) tool installed.

- You must provision a local container image registry with the container images for your update, as described in "Mirroring OpenShift Container Platform images".

- You must have access to the cluster as a user with `admin` privileges. See "Using RBAC to define and apply permissions".

- You must have a recent etcd backup in case your update fails and you must restore your cluster to a previous state. For more information, see "Backing up etcd" and "Restoring to a previous cluster state".

- You have updated all Operators previously installed through Operator Lifecycle Manager (OLM) to a version that is compatible with your target release. Updating the Operators ensures they have a valid update path when the default catalog sources switch from the current minor version to the next during a cluster update. See "Updating installed Operators" for more information on how to check compatibility and, if necessary, update the installed Operators.

- You must ensure that all machine config pools (MCPs) are running and not paused. Nodes associated with a paused MCP are skipped during the update process. You can pause the MCPs if you are performing a canary rollout update strategy.

- If your cluster uses manually maintained credentials, update the cloud provider resources for the new release. For more information, including how to determine if this is a requirement for your cluster, see "Preparing to update a cluster with manually maintained credentials".

- If you run an Operator or you have configured any application with the pod disruption budget, you might experience an interruption during the update process. If `minAvailable` is set to 1 in `PodDisruptionBudget`, the nodes are drained to apply pending machine configs which might block the eviction process. If several nodes are rebooted, all the pods might run on only one node, and the `PodDisruptionBudget` field can prevent the node drain.

> [!NOTE]
> If you run an Operator or you have configured any application with the pod disruption budget, you might experience an interruption during the update process. If `minAvailable` is set to 1 in `PodDisruptionBudget`, the nodes are drained to apply pending machine configs which might block the eviction process. If several nodes are rebooted, all the pods might run on only one node, and the `PodDisruptionBudget` field can prevent the node drain.

<div>

<div class="title">

Additional resources

</div>

- [Mirroring OpenShift Container Platform images](mirroring-image-repository.md#mirroring-ocp-image-repository)

- [Using RBAC to define and apply permissions](../../authentication/using-rbac.md#using-rbac)

- [Backing up etcd](../../backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.md#backup-etcd)

- [Restoring to a previous cluster state](../../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md#dr-restoring-cluster-state)

- [Updating installed Operators](../../operators/admin/olm-upgrading-operators.md#olm-upgrading-operators)

- [Preparing to update a cluster with manually maintained credentials](../../updating/preparing_for_updates/preparing-manual-creds-update.md#preparing-manual-creds-update)

</div>

# Pausing a MachineHealthCheck resource

During the update process, nodes in the cluster might become temporarily unavailable. For worker nodes, the `MachineHealthCheck` resources might identify such nodes as unhealthy and reboot them. To avoid rebooting worker nodes, you must pause all the `MachineHealthCheck` resources before updating the cluster.

> [!NOTE]
> Some `MachineHealthCheck` resources might not need to be paused. If your `MachineHealthCheck` resource relies on unrecoverable conditions, pausing that MHC is unnecessary.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  List all of the available `MachineHealthCheck` resources that you want to pause by running the following command:

    ``` terminal
    $ oc get machinehealthcheck -n openshift-machine-api
    ```

2.  For each `MachineHealthCheck` resource, pause the machine health check by running the following command:

    ``` terminal
    $ oc -n openshift-machine-api annotate mhc <mhc_name> cluster.x-k8s.io/paused=""
    ```

    The annotated `MachineHealthCheck` resource resembles the following YAML file:

    ``` yaml
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineHealthCheck
    metadata:
      name: example
      namespace: openshift-machine-api
      annotations:
        cluster.x-k8s.io/paused: ""
    spec:
      selector:
        matchLabels:
          role: worker
      unhealthyConditions:
      - type:    "Ready"
        status:  "Unknown"
        timeout: "300s"
      - type:    "Ready"
        status:  "False"
        timeout: "300s"
      maxUnhealthy: "40%"
    status:
      currentHealthy: 5
      expectedMachines: 5
    ```

    > [!IMPORTANT]
    > Resume the machine health checks after updating the cluster. To resume the check, remove the pause annotation from the `MachineHealthCheck` resource by running the following command:
    >
    > ``` terminal
    > $ oc -n openshift-machine-api annotate mhc <mhc-name> cluster.x-k8s.io/paused-
    > ```

</div>

# Retrieving a release image digest

In order to update a cluster in a disconnected environment using the `oc adm upgrade` command with the `--to-image` option, you must reference the sha256 digest that corresponds to your targeted release image.

<div>

<div class="title">

Procedure

</div>

1.  Run the following command on a device that is connected to the internet:

    ``` terminal
    $ oc adm release info -o 'jsonpath={"\n"}' quay.io/openshift-release-dev/ocp-release:${OCP_RELEASE_VERSION}-${ARCHITECTURE}
    ```

    For `{OCP_RELEASE_VERSION}`, specify the version of OpenShift Container Platform to which you want to update, such as `4.10.16`.

    For `{ARCHITECTURE}`, specify the architecture of the cluster, such as `x86_64`, `aarch64`, `s390x`, or `ppc64le`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    sha256:a8bfba3b6dddd1a2fbbead7dac65fe4fb8335089e4e7cae327f3bad334add31d
    ```

    </div>

2.  Copy the sha256 digest for use when updating your cluster.

</div>

# Updating the disconnected cluster

Update the disconnected cluster to the OpenShift Container Platform version that you downloaded the release images for.

> [!NOTE]
> If you have a local OpenShift Update Service, you can update by using the connected web console or CLI instructions instead of this procedure.

<div>

<div class="title">

Prerequisites

</div>

- You mirrored the images for the new release to your registry.

- You applied the release image signature ConfigMap for the new release to your cluster.

  > [!NOTE]
  > The release image signature config map allows the Cluster Version Operator (CVO) to ensure the integrity of release images by verifying that the actual image signatures match the expected signatures.

- You obtained the sha256 digest for your targeted release image.

- You installed the OpenShift CLI (`oc`).

- You paused all `MachineHealthCheck` resources.

</div>

<div>

<div class="title">

Procedure

</div>

- Update the cluster:

  ``` terminal
  $ oc adm upgrade --allow-explicit-upgrade --to-image <defined_registry>/<defined_repository>@<digest>
  ```

  Where:

  `<defined_registry>`
  Specifies the name of the mirror registry you mirrored your images to.

  `<defined_repository>`
  Specifies the name of the image repository you want to use on the mirror registry.

  `<digest>`
  Specifies the sha256 digest for the targeted release image, for example, `sha256:81154f5c03294534e1eaf0319bef7a601134f891689ccede5d705ef659aa8c92`.

  <div class="note">

  <div class="title">

  </div>

  - See "Mirroring OpenShift Container Platform images" to review how your mirror registry and repository names are defined.

  - If you used an `ImageContentSourcePolicy` or `ImageDigestMirrorSet`, you can use the canonical registry and repository names instead of the names you defined. The canonical registry name is `quay.io` and the canonical repository name is `openshift-release-dev/ocp-release`.

  - You can only configure global pull secrets for clusters that have an `ImageContentSourcePolicy`, `ImageDigestMirrorSet`, or `ImageTagMirrorSet` object. You cannot add a pull secret to a project.

  </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Mirroring OpenShift Container Platform images](mirroring-image-repository.md#mirroring-ocp-image-repository)

</div>

# Understanding image registry repository mirroring

You must mirror images to update clusters in disconnected environments.

By setting up container registry repository mirroring, you can perform the following tasks:

- Configure your OpenShift Container Platform cluster to redirect requests to pull images from a repository on a source image registry and have it resolved by a repository on a mirrored image registry.

- Identify multiple mirrored repositories for each target repository, to make sure that if one mirror is down, another can be used.

Repository mirroring in OpenShift Container Platform includes the following attributes:

- Image pulls are resilient to registry downtimes.

- Clusters in disconnected environments can pull images from critical locations, such as `quay.io`, and have registries behind a company firewall provide the requested images.

- A particular order of registries is tried when an image pull request is made, with the permanent registry typically being the last one tried.

- The mirror information you enter is added to the `/etc/containers/registries.conf` file on every node in the OpenShift Container Platform cluster.

- When a node makes a request for an image from the source repository, it tries each mirrored repository in turn until it finds the requested content. If all mirrors fail, the cluster tries the source repository. If successful, the image is pulled to the node.

You can set up repository mirroring in the following ways:

- At OpenShift Container Platform installation:

  By pulling container images needed by OpenShift Container Platform and then bringing those images behind your company’s firewall, you can install OpenShift Container Platform into a data center that is in a disconnected environment.

- After OpenShift Container Platform installation:

  If you did not configure mirroring during OpenShift Container Platform installation, you can do so postinstallation by using any of the following custom resource (CR) objects:

  - `ImageDigestMirrorSet` (IDMS). This object allows you to pull images from a mirrored registry by using digest specifications. The IDMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails.

  - `ImageTagMirrorSet` (ITMS). This object allows you to pull images from a mirrored registry by using image tags. The ITMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails.

  - `ImageContentSourcePolicy` (ICSP). This object allows you to pull images from a mirrored registry by using digest specifications. The ICSP CR always falls back to the source registry if the mirrors do not work.

    > [!IMPORTANT]
    > Using an `ImageContentSourcePolicy` (ICSP) object to configure repository mirroring is a deprecated feature. Deprecated functionality is still included in OpenShift Container Platform and continues to be supported. It will be removed in a future release and is not recommended for new deployments.
    >
    > If you have existing YAML files that you used to create `ImageContentSourcePolicy` objects, you can use the `oc adm migrate icsp` command to convert those files to a `ImageDigestMirrorSet` YAML files. For more information, see "Converting ImageContentSourcePolicy (ICSP) files for image registry repository mirroring".

Each of these custom resource objects identify the following information:

- The source of the container image repository you want to mirror.

- A separate entry for each mirror repository you want to offer the content

Note the following actions and how they affect node drain behavior:

- If you create an IDMS or ICSP CR object, the MCO does not drain or reboot the node.

- If you create an ITMS CR object, the MCO drains and reboots the node.

- If you delete an ITMS, IDMS, or ICSP CR object, the MCO drains and reboots the node.

- If you modify an ITMS, IDMS, or ICSP CR object, the MCO drains and reboots the node.

  <div class="important">

  <div class="title">

  </div>

  - When the MCO detects any of the following changes, it applies the update without draining or rebooting the node:

    - Changes to the SSH key in the `spec.config.passwd.users.sshAuthorizedKeys` parameter of a machine config.

    - Changes to the global pull secret or pull secret in the `openshift-config` namespace.

    - Automatic rotation of the `/etc/kubernetes/kubelet-ca.crt` certificate authority (CA) by the Kubernetes API Server Operator.

  - When the MCO detects changes to the `/etc/containers/registries.conf` file, such as editing an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object, it drains the corresponding nodes, applies the changes, and uncordons the nodes. The node drain does not happen for the following changes:

    - The addition of a registry with the `pull-from-mirror = "digest-only"` parameter set for each mirror.

    - The addition of a mirror with the `pull-from-mirror = "digest-only"` parameter set in a registry.

    - The addition of items to the `unqualified-search-registries` list.

  </div>

For new clusters, you can use IDMS, ITMS, and ICSP CRs objects as needed. However, using IDMS and ITMS is recommended.

If you upgraded a cluster, any existing ICSP objects remain stable, and both IDMS and ICSP objects are supported. Workloads that use ICSP objects continue to function as expected. However, if you want to take advantage of the fallback policies introduced in the IDMS CRs, you can migrate current workloads to IDMS objects by using the `oc adm migrate icsp` command as shown in the **Converting ImageContentSourcePolicy (ICSP) files for image registry repository mirroring** section that follows. Migrating to IDMS objects does not require a cluster reboot.

> [!NOTE]
> If your cluster uses an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object to configure repository mirroring, you can use only global pull secrets for mirrored registries. You cannot add a pull secret to a project.

## Configuring image registry repository mirroring

You can create postinstallation mirror configuration custom resources (CR) to redirect image pull requests from a source image registry to a mirrored image registry.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure mirrored repositories, by either:

    - Setting up a mirrored repository with Red Hat Quay. You can copy images from one repository to another and also automatically sync those repositories repeatedly over time by using Red Hat Quay.

      - [Red Hat Quay Repository Mirroring](https://docs.redhat.com/en/documentation/red_hat_quay/3/html/manage_red_hat_quay/arch-mirroring-intro#enabling-repository-mirroring-quay)

    - Using a tool such as `skopeo` to copy images manually from the source repository to the mirrored repository.

      For example, after installing the skopeo RPM package on a {op-system-base-full system}, use the `skopeo` command as shown in the following example:

      ``` terminal
      $ skopeo copy --all \
      docker://registry.access.redhat.com/ubi9/ubi-minimal:latest@sha256:5cf... \
      docker://example.io/example/ubi-minimal
      ```

      In this example, you have a container image registry named `example.io` and image repository named `example`. You want to copy the `ubi9/ubi-minimal` image from `registry.access.redhat.com` to `example.io`. After you create the mirrored registry, you can configure your OpenShift Container Platform cluster to redirect requests made to the source repository to the mirrored repository.

2.  Create a postinstallation mirror configuration custom resource (CR), by using one of the following examples:

    - Create an `ImageDigestMirrorSet` or `ImageTagMirrorSet` CR, as needed, replacing the source and mirrors with your own registry and repository pairs and images:

      ``` yaml
      apiVersion: config.openshift.io/v1
      kind: ImageDigestMirrorSet
      metadata:
        name: ubi9repo
      spec:
        imageDigestMirrors:
        - mirrors:
          - example.io/example/ubi-minimal
          - example.com/example2/ubi-minimal
          source: registry.access.redhat.com/ubi9/ubi-minimal
          mirrorSourcePolicy: AllowContactingSource
        - mirrors:
          - mirror.example.com/redhat
          source: registry.example.com/redhat
          mirrorSourcePolicy: AllowContactingSource
        - mirrors:
          - mirror.example.com
          source: registry.example.com
          mirrorSourcePolicy: AllowContactingSource
        - mirrors:
          - mirror.example.net/image
          source: registry.example.com/example/myimage
          mirrorSourcePolicy: AllowContactingSource
        - mirrors:
          - mirror.example.net
          source: registry.example.com/example
          mirrorSourcePolicy: AllowContactingSource
        - mirrors:
          - mirror.example.net/registry-example-com
          source: registry.example.com
          mirrorSourcePolicy: AllowContactingSource
      ```

    - Create an `ImageContentSourcePolicy` custom resource, replacing the source and mirrors with your own registry and repository pairs and images:

      ``` yaml
      apiVersion: operator.openshift.io/v1alpha1
      kind: ImageContentSourcePolicy
      metadata:
        name: mirror-ocp
      spec:
        repositoryDigestMirrors:
        - mirrors:
          - mirror.registry.com:443/ocp/release
          source: quay.io/openshift-release-dev/ocp-release
        - mirrors:
          - mirror.registry.com:443/ocp/release
          source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
      ```

      where:

      `- mirror.registry.com:443/ocp/release`
      Specifies the name of the mirror image registry and repository.

      `source: quay.io/openshift-release-dev/ocp-release`
      Specifies the online registry and repository containing the content that is mirrored.

3.  Create the new object by running the following command:

    ``` terminal
    $ oc create -f registryrepomirror.yaml
    ```

    After the object is created, the Machine Config Operator (MCO) drains the nodes for `ImageTagMirrorSet` objects only. The MCO does not drain the nodes for `ImageDigestMirrorSet` and `ImageContentSourcePolicy` objects.

4.  To check that the mirrored configuration settings are applied, do the following on one of the nodes.

    1.  List your nodes:

        ``` terminal
        $ oc get node
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                           STATUS                     ROLES    AGE  VERSION
        worker-1.compute.local         Ready                      worker   7m   v1.35.4
        master-1.compute.local         Ready                      master   11m  v1.35.4
        master-2.compute.local         Ready                      master   11m  v1.35.4
        worker-2.compute.local         Ready                      worker   7m   v1.35.4
        worker-3.compute.local         Ready                      worker   7m   v1.35.4
        master-3.compute.local         Ready                      master   11m  v1.35.4
        ```

        </div>

    2.  Start the debugging process to access the node:

        ``` terminal
        $ oc debug node/worker-1.compute.local
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        Starting pod/worker-1.compute.local-debug ...
        To use host binaries, run `chroot /host`
        ```

        </div>

    3.  Change your root directory to `/host`:

        ``` terminal
        sh-4.2# chroot /host
        ```

    4.  Check the `/etc/containers/registries.conf` file to make sure the changes were made:

        ``` terminal
        sh-4.2# cat /etc/containers/registries.conf
        ```

        The following output represents a `registries.conf` file where postinstallation mirror configuration CRs are applied.

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]
        short-name-mode = ""

        [[registry]]
          prefix = ""
          location = "registry.access.redhat.com/ubi9/ubi-minimal"

          [[registry.mirror]]
            location = "example.io/example/ubi-minimal"
            pull-from-mirror = "digest-only"

          [[registry.mirror]]
            location = "example.com/example/ubi-minimal"
            pull-from-mirror = "digest-only"

        [[registry]]
          prefix = ""
          location = "registry.example.com"

          [[registry.mirror]]
            location = "mirror.example.net/registry-example-com"
            pull-from-mirror = "digest-only"

        [[registry]]
          prefix = ""
          location = "registry.example.com/example"

          [[registry.mirror]]
            location = "mirror.example.net"
            pull-from-mirror = "digest-only"

        [[registry]]
          prefix = ""
          location = "registry.example.com/example/myimage"

          [[registry.mirror]]
            location = "mirror.example.net/image"
            pull-from-mirror = "digest-only"

        [[registry]]
          prefix = ""
          location = "registry.example.com"

          [[registry.mirror]]
            location = "mirror.example.com"
            pull-from-mirror = "digest-only"

        [[registry]]
          prefix = ""
          location = "registry.example.com/redhat"

          [[registry.mirror]]
            location = "mirror.example.com/redhat"
            pull-from-mirror = "digest-only"
        [[registry]]
          prefix = ""
          location = "registry.access.redhat.com/ubi9/ubi-minimal"
          blocked = true

          [[registry.mirror]]
            location = "example.io/example/ubi-minimal-tag"
            pull-from-mirror = "tag-only"
        ```

        </div>

        where: `[[registry]].location = "registry.access.redhat.com/ubi9/ubi-minimal"`:: The repository listed in a pull spec. `[[registry.mirror]].location = "example.io/example/ubi-minimal"`:: Indicates the mirror for that repository. `[[registry.mirror]].pull-from-mirror = "digest-only"`:: Means that the image pull from the mirror is a digest reference image. `[[registry]].blocked = true`:: Indicates that the `NeverContactSource` parameter is set for this repository. `[[registry.mirror]].pull-from-mirror = "tag-only"`:: Indicates that the image pull from the mirror is a tag reference image.

    5.  Pull an image to the node from the source and check if it is resolved by the mirror.

        ``` terminal
        sh-4.2# podman pull --log-level=debug registry.access.redhat.com/ubi9/ubi-minimal@sha256:5cf...
        ```

</div>

<div class="formalpara">

<div class="title">

Troubleshooting

</div>

If the repository mirroring procedure does not work as described, use the following information about how repository mirroring works to help troubleshoot the problem:

</div>

- The first working mirror is used to supply the pulled image.

- The main registry is only used if no other mirror works.

- From the system context, the `Insecure` flags are used as fallback.

- The format of the `/etc/containers/registries.conf` file has changed recently. It is now version 2 and in TOML format.

## Converting ImageContentSourcePolicy (ICSP) files for image registry repository mirroring

You can convert existing `ImageContentSourcePolicy` (ICSP) files to `ImageDigestMirrorSet` files to configure image registry repository mirroring.

Using an `ImageContentSourcePolicy` (ICSP) object to configure repository mirroring is a deprecated feature.

This functionality is still included in OpenShift Container Platform and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments.

ICSP objects are being replaced by `ImageDigestMirrorSet` and `ImageTagMirrorSet` objects to configure repository mirroring. If you have existing YAML files that you used to create `ImageContentSourcePolicy` objects, you can use the `oc adm migrate icsp` command to convert those files to an `ImageDigestMirrorSet` YAML file. The command updates the API to the current version, changes the `kind` value to `ImageDigestMirrorSet`, and changes `spec.repositoryDigestMirrors` to `spec.imageDigestMirrors`. The rest of the file is not changed.

Because the migration does not change the `registries.conf` file, the cluster does not need to reboot.

For more information about `ImageDigestMirrorSet` or `ImageTagMirrorSet` objects, see "Configuring image registry repository mirroring" in the previous section.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

- Ensure that you have `ImageContentSourcePolicy` objects on your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Use the following command to convert one or more `ImageContentSourcePolicy` YAML files to an `ImageDigestMirrorSet` YAML file:

    ``` terminal
    $ oc adm migrate icsp <file_name>.yaml <file_name>.yaml <file_name>.yaml --dest-dir <path_to_the_directory>
    ```

    where:

    `<file_name>`
    Specifies the name of the source `ImageContentSourcePolicy` YAML. You can list multiple file names.

    `--dest-dir`
    Optional: Specifies a directory for the output `ImageDigestMirrorSet` YAML. If unset, the file is written to the current directory.

    For example, the following command converts the `icsp.yaml` and `icsp-2.yaml` file and saves the new YAML files to the `idms-files` directory.

    ``` terminal
    $ oc adm migrate icsp icsp.yaml icsp-2.yaml --dest-dir idms-files
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    wrote ImageDigestMirrorSet to idms-files/imagedigestmirrorset_ubi8repo.5911620242173376087.yaml
    wrote ImageDigestMirrorSet to idms-files/imagedigestmirrorset_ubi9repo.6456931852378115011.yaml
    ```

    </div>

2.  Create the CR object by running the following command:

    ``` terminal
    $ oc create -f <path_to_the_directory>/<file-name>.yaml
    ```

    where:

    `<path_to_the_directory>`
    Specifies the path to the directory, if you used the `--dest-dir` flag.

    `<file_name>`
    Specifies the name of the `ImageDigestMirrorSet` YAML.

3.  Remove the ICSP objects after the IDMS objects are rolled out.

</div>

# Widening the scope of the mirror image catalog to reduce the frequency of cluster node reboots

You can scope the mirrored image catalog at the repository level or the wider registry level. A widely scoped `ImageContentSourcePolicy` resource reduces the number of times the nodes need to reboot in response to changes to the resource.

To widen the scope of the mirror image catalog in the `ImageContentSourcePolicy` resource, perform the following procedure.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift Container Platform CLI `oc`.

- Log in as a user with `cluster-admin` privileges.

- Configure a mirrored image catalog for use in your disconnected cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the following command, specifying values for `<local_registry>`, `<pull_spec>`, and `<pull_secret_file>`:

    ``` terminal
    $ oc adm catalog mirror <local_registry>/<pull_spec> <local_registry> -a <pull_secret_file> --icsp-scope=registry
    ```

    where:

    \<local_registry\>
    is the local registry you have configured for your disconnected cluster, for example, `local.registry:5000`.

    \<pull_spec\>
    is the pull specification as configured in your disconnected registry, for example, `redhat/redhat-operator-index:v4.17`

    \<pull_secret_file\>
    is the `registry.redhat.io` pull secret in `.json` file format. You can download the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret).

    The `oc adm catalog mirror` command creates a `/redhat-operator-index-manifests` directory and generates `imageContentSourcePolicy.yaml`, `catalogSource.yaml`, and `mapping.txt` files.

2.  Apply the new `ImageContentSourcePolicy` resource to the cluster:

    ``` terminal
    $ oc apply -f imageContentSourcePolicy.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that `oc apply` successfully applied the change to `ImageContentSourcePolicy`:

  ``` terminal
  $ oc get ImageContentSourcePolicy -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` yaml
  apiVersion: v1
  items:
  - apiVersion: operator.openshift.io/v1alpha1
    kind: ImageContentSourcePolicy
    metadata:
      annotations:
        kubectl.kubernetes.io/last-applied-configuration: |
          {"apiVersion":"operator.openshift.io/v1alpha1","kind":"ImageContentSourcePolicy","metadata":{"annotations":{},"name":"redhat-operator-index"},"spec":{"repositoryDigestMirrors":[{"mirrors":["local.registry:5000"],"source":"registry.redhat.io"}]}}
  ...
  ```

  </div>

</div>

After you update the `ImageContentSourcePolicy` resource, OpenShift Container Platform deploys the new settings to each node and the cluster starts using the mirrored repository for requests to the source repository.

# Additional resources

- [Using Operator Lifecycle Manager in disconnected environments](../using-olm.md#olm-restricted-networks)

- [Machine Config Overview](../../machine_configuration/index.md#machine-config-overview)
