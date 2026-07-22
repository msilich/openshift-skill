<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To use RHACM in a disconnected environment, create a mirror registry that mirrors the OpenShift Container Platform release images and Operator Lifecycle Manager (OLM) catalog that contains the required Operator images. OLM manages, installs, and upgrades Operators and their dependencies in the cluster. You can also use a disconnected mirror host to serve the RHCOS ISO and RootFS disk images that are used to provision the bare-metal hosts.

# Telco RAN DU 4.17 validated software components

The Red Hat telco RAN DU 4.17 solution has been validated using the following Red Hat software products for OpenShift Container Platform managed clusters.

| Component                                | Software version |
|------------------------------------------|------------------|
| Managed cluster version                  | 4.19             |
| Cluster Logging Operator                 | 6.2              |
| Local Storage Operator                   | 4.20             |
| OpenShift API for Data Protection (OADP) | 1.5              |
| PTP Operator                             | 4.20             |
| SR-IOV Operator                          | 4.20             |
| SRIOV-FEC Operator                       | 2.11             |
| Lifecycle Agent                          | 4.20             |

Telco RAN DU managed cluster validated software components

# Recommended hub cluster specifications and managed cluster limits for GitOps ZTP

With GitOps Zero Touch Provisioning (ZTP), you can manage thousands of clusters in geographically dispersed regions and networks. The Red Hat Performance and Scale lab successfully created and managed 3500 virtual single-node OpenShift clusters with a reduced DU profile from a single Red Hat Advanced Cluster Management (RHACM) hub cluster in a lab environment.

In real-world situations, the scaling limits for the number of clusters that you can manage will vary depending on various factors affecting the hub cluster. For example:

Hub cluster resources
Available hub cluster host resources (CPU, memory, storage) are an important factor in determining how many clusters the hub cluster can manage. The more resources allocated to the hub cluster, the more managed clusters it can accommodate.

Hub cluster storage
The hub cluster host storage IOPS rating and whether the hub cluster hosts use NVMe storage can affect hub cluster performance and the number of clusters it can manage.

Network bandwidth and latency
Slow or high-latency network connections between the hub cluster and managed clusters can impact how the hub cluster manages multiple clusters.

Managed cluster size and complexity
The size and complexity of the managed clusters also affects the capacity of the hub cluster. Larger managed clusters with more nodes, namespaces, and resources require additional processing and management resources. Similarly, clusters with complex configurations such as the RAN DU profile or diverse workloads can require more resources from the hub cluster.

Number of managed policies
The number of policies managed by the hub cluster scaled over the number of managed clusters bound to those policies is an important factor that determines how many clusters can be managed.

Monitoring and management workloads
RHACM continuously monitors and manages the managed clusters. The number and complexity of monitoring and management workloads running on the hub cluster can affect its capacity. Intensive monitoring or frequent reconciliation operations can require additional resources, potentially limiting the number of manageable clusters.

RHACM version and configuration
Different versions of RHACM can have varying performance characteristics and resource requirements. Additionally, the configuration settings of RHACM, such as the number of concurrent reconciliations or the frequency of health checks, can affect the managed cluster capacity of the hub cluster.

Use the following representative configuration and network specifications to develop your own Hub cluster and network specifications.

> [!IMPORTANT]
> The following guidelines are based on internal lab benchmark testing only and do not represent complete bare-metal host specifications.

<table style="width:90%;">
<caption>Representative three-node hub cluster machine specifications</caption>
<colgroup>
<col style="width: 45%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Requirement</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Server hardware</p></td>
<td style="text-align: left;"><p>3 x Dell PowerEdge R650 rack servers</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>NVMe hard disks</p></td>
<td style="text-align: left;"><ul>
<li><p>50 GB disk for <code>/var/lib/etcd</code></p></li>
<li><p>2.9 TB disk for <code>/var/lib/containers</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>SSD hard disks</p></td>
<td style="text-align: left;"><ul>
<li><p>1 SSD split into 15 200GB thin-provisioned logical volumes provisioned as <code>PV</code> CRs</p></li>
<li><p>1 SSD serving as an extra large <code>PV</code> resource</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Number of applied DU profile policies</p></td>
<td style="text-align: left;"><p>5</p></td>
</tr>
</tbody>
</table>

> [!IMPORTANT]
> The following network specifications are representative of a typical real-world RAN network and were applied to the scale lab environment during testing.

| Specification                 | Description       |
|-------------------------------|-------------------|
| Round-trip time (RTT) latency | 50 ms             |
| Packet loss                   | 0.02% packet loss |
| Network bandwidth limit       | 20 Mbps           |

Simulated lab environment network specifications

<div>

<div class="title">

Additional resources

</div>

- [Creating and managing single-node OpenShift clusters with RHACM](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.7/html/install/installing#single-node)

</div>

# Installing GitOps ZTP in a disconnected environment

Use Red Hat Advanced Cluster Management (RHACM), Red Hat OpenShift GitOps, and Topology Aware Lifecycle Manager (TALM) on the hub cluster in the disconnected environment to manage the deployment of multiple managed clusters.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift Container Platform CLI (`oc`).

- You have logged in as a user with `cluster-admin` privileges.

- You have configured a disconnected mirror registry for use in the cluster.

  > [!NOTE]
  > The disconnected mirror registry that you create must contain a version of TALM backup and pre-cache images that matches the version of TALM running in the hub cluster. The spoke cluster must be able to resolve these images in the disconnected mirror registry.

</div>

<div>

<div class="title">

Procedure

</div>

- Install RHACM in the hub cluster. See [Installing RHACM in a disconnected environment](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.13/html/install/installing#install-on-disconnected-networks).

- Install GitOps and TALM in the hub cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing OpenShift GitOps](https://docs.openshift.com/gitops/latest/installing_gitops/installing-openshift-gitops.html#installing-openshift-gitops)

- [Installing TALM](cnf-talm-for-cluster-upgrades.md#installing-topology-aware-lifecycle-manager-using-cli_cnf-topology-aware-lifecycle-manager)

- [Mirroring an Operator catalog](../disconnected/using-olm.md#olm-mirror-catalog_olm-restricted-networks)

</div>

# Adding RHCOS ISO and RootFS images to the disconnected mirror host

Before you begin installing clusters in the disconnected environment with Red Hat Advanced Cluster Management (RHACM), you must first host Red Hat Enterprise Linux CoreOS (RHCOS) images for it to use. Use a disconnected mirror to host the RHCOS images.

<div>

<div class="title">

Prerequisites

</div>

- Deploy and configure an HTTP server to host the RHCOS image resources on the network. You must be able to access the HTTP server from your computer, and from the machines that you create.

</div>

> [!IMPORTANT]
> The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the version that you install. Use the image versions that match your OpenShift Container Platform version if they are available. You require ISO and RootFS images to install RHCOS on the hosts. RHCOS QCOW2 images are not supported for this installation type.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the mirror host.

2.  Obtain the RHCOS ISO and RootFS images from [mirror.openshift.com](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/), for example:

    1.  Export the required image names and OpenShift Container Platform version as environment variables:

        ``` terminal
        $ export ISO_IMAGE_NAME=<iso_image_name>
        ```

        ``` terminal
        $ export ROOTFS_IMAGE_NAME=<rootfs_image_name>
        ```

        ``` terminal
        $ export OCP_VERSION=<ocp_version>
        ```

        where:

        `<iso_image_name>`
        ISO image name, for example, `rhcos-4.17.1-x86_64-live.x86_64.iso`

        `<rootfs_image_name>`
        RootFS image name, for example, `rhcos-4.17.1-x86_64-live-rootfs.x86_64.img`

        `<ocp_version>`
        OpenShift Container Platform version, for example, `4.17.1`

    2.  Download the required images:

        ``` terminal
        $ sudo wget https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/4.17/${OCP_VERSION}/${ISO_IMAGE_NAME} -O /var/www/html/${ISO_IMAGE_NAME}
        ```

        ``` terminal
        $ sudo wget https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/4.17/${OCP_VERSION}/${ROOTFS_IMAGE_NAME} -O /var/www/html/${ROOTFS_IMAGE_NAME}
        ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the images downloaded successfully and are being served on the disconnected mirror host, for example:

  ``` terminal
  $ wget http://$(hostname)/${ISO_IMAGE_NAME}
  ```

  Example output:

  ``` terminal
  Saving to: rhcos-4.17.1-x86_64-live.x86_64.iso
  rhcos-4.17.1-x86_64-live.x86_64.iso-  11%[====>    ]  10.01M  4.71MB/s
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a mirror registry](../disconnected/installing-mirroring-creating-registry.md#installing-mirroring-creating-registry)

- [Mirroring images for a disconnected installation](../disconnected/installing-mirroring-installation-images.md#installing-mirroring-installation-images)

</div>

# Enabling the assisted service

Red Hat Advanced Cluster Management (RHACM) uses the assisted service to deploy OpenShift Container Platform clusters. The assisted service is deployed automatically when you enable the MultiClusterHub Operator on Red Hat Advanced Cluster Management (RHACM). After that, you need to configure the `Provisioning` resource to watch all namespaces and to update the `AgentServiceConfig` custom resource (CR) with references to the ISO and RootFS images that are hosted on the mirror registry HTTP server.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in to the hub cluster as a user with `cluster-admin` privileges.

- You have RHACM with `MultiClusterHub` enabled.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable the `Provisioning` resource to watch all namespaces and configure mirrors for disconnected environments. For more information, see [Enabling the central infrastructure management service](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.9/html/clusters/cluster_mce_overview#enable-cim).

2.  Open the `AgentServiceConfig` CR to update the `spec.osImages` field by running the following command:

    ``` terminal
    $ oc edit AgentServiceConfig
    ```

3.  Update the `spec.osImages` field in the `AgentServiceConfig` CR:

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: AgentServiceConfig
    metadata:
     name: agent
    spec:
    # ...
      osImages:
        - cpuArchitecture: x86_64
          openshiftVersion: "4.17"
          rootFSUrl: https://<host>/<path>/rhcos-live-rootfs.x86_64.img
          url: https://<host>/<path>/rhcos-live.x86_64.iso
    ```

    where:

    `<host>`
    Specifies the fully qualified domain name (FQDN) for the target mirror registry HTTP server.

    `<path>`
    Specifies the path to the image on the target mirror registry.

4.  Save and quit the editor to apply the changes.

</div>

# Configuring the hub cluster to use a disconnected mirror registry

You can configure the hub cluster to use a disconnected mirror registry for a disconnected environment.

<div>

<div class="title">

Prerequisites

</div>

- You have a disconnected hub cluster installation with Red Hat Advanced Cluster Management (RHACM) 2.13 installed.

- You have hosted the `rootfs` and `iso` images on an HTTP server. See the *Additional resources* section for guidance about *Mirroring the OpenShift Container Platform image repository*.

</div>

> [!WARNING]
> If you enable TLS for the HTTP server, you must confirm the root certificate is signed by an authority trusted by the client and verify the trusted certificate chain between your OpenShift Container Platform hub and managed clusters and the HTTP server. Using a server configured with an untrusted certificate prevents the images from being downloaded to the image creation service. Using untrusted HTTPS servers is not supported.

<div>

<div class="title">

Procedure

</div>

1.  Create a `ConfigMap` containing the mirror registry config:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: assisted-installer-mirror-config
      namespace: multicluster-engine
      labels:
        app: assisted-service
    data:
      ca-bundle.crt: |
        -----BEGIN CERTIFICATE-----
        <certificate_contents>
        -----END CERTIFICATE-----

      registries.conf: |
        unqualified-search-registries = ["registry.access.redhat.com", "docker.io"]

        [[registry]]
           prefix = ""
           location = "quay.io/example-repository"
           mirror-by-digest-only = true

           [[registry.mirror]]
           location = "mirror1.registry.corp.com:5000/example-repository"
    ```

    where:

    `namespace: multicluster-engine`
    The `ConfigMap` namespace must be set to `multicluster-engine`.

    `ca-bundle.crt`
    The mirror registry’s certificate that is used when creating the mirror registry.

    `registries.conf`
    The configuration file for the mirror registry. The mirror registry configuration adds mirror information to the `/etc/containers/registries.conf` file in the discovery image. The mirror information is stored in the `imageContentSources` section of the `install-config.yaml` file when the information is passed to the installation program. The Assisted Service pod that runs on the hub cluster fetches the container images from the configured mirror registry.

    `location = "quay.io/example-repository"`
    The URL of the mirror registry. You must use the URL from the `imageContentSources` section by running the `oc adm release mirror` command when you configure the mirror registry. For more information, see the *Mirroring the OpenShift Container Platform image repository* section.

    `location = "mirror1.registry.corp.com:5000/example-repository"`
    The registries defined in the `registries.conf` file must be scoped by repository, not by registry. In this example, both the `quay.io/example-repository` and the `mirror1.registry.corp.com:5000/example-repository` repositories are scoped by the `example-repository` repository.

    This updates `mirrorRegistryRef` in the `AgentServiceConfig` custom resource, as shown in this example output:

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: AgentServiceConfig
    metadata:
      name: agent
      namespace: multicluster-engine
    spec:
      databaseStorage:
        volumeName: <db_pv_name>
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: <db_storage_size>
      filesystemStorage:
        volumeName: <fs_pv_name>
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: <fs_storage_size>
      mirrorRegistryRef:
        name: assisted-installer-mirror-config
      osImages:
        - openshiftVersion: <ocp_version>
          url: <iso_url>
    ```

    where:

    `namespace: multicluster-engine`
    Set the `AgentServiceConfig` namespace to `multicluster-engine` to match the `ConfigMap` namespace.

    `assisted-installer-mirror-config`
    Set `mirrorRegistryRef.name` to match the definition specified in the related `ConfigMap` CR.

    `<ocp_version>`
    Set the OpenShift Container Platform version to either the x.y or x.y.z format.

    `<iso_url>`
    Set the URL for the ISO hosted on the `httpd` server.

    > [!IMPORTANT]
    > A valid NTP server is required during cluster installation. Ensure that a suitable NTP server is available and can be reached from the installed clusters through the disconnected network.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Mirroring the OpenShift Container Platform repository](../disconnected/installing-mirroring-installation-images.md#installation-mirror-repository_installing-mirroring-installation-images)

</div>

# Configuring the hub cluster to use unauthenticated registries

You can configure the hub cluster to use unauthenticated registries. Unauthenticated registries does not require authentication to access and download images.

<div>

<div class="title">

Prerequisites

</div>

- You have installed and configured a hub cluster and installed Red Hat Advanced Cluster Management (RHACM) on the hub cluster.

- You have installed the OpenShift Container Platform CLI (oc).

- You have logged in as a user with `cluster-admin` privileges.

- You have configured an unauthenticated registry for use with the hub cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Update the `AgentServiceConfig` custom resource (CR) by running the following command:

    ``` terminal
    $ oc edit AgentServiceConfig agent
    ```

2.  Add the `unauthenticatedRegistries` field in the CR:

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: AgentServiceConfig
    metadata:
      name: agent
    spec:
      unauthenticatedRegistries:
      - example.registry.com
      - example.registry2.com
      ...
    ```

    Unauthenticated registries are listed under `spec.unauthenticatedRegistries` in the `AgentServiceConfig` resource. Any registry on this list is not required to have an entry in the pull secret used for the spoke cluster installation. `assisted-service` validates the pull secret by making sure it contains the authentication information for every image registry used for installation.

    > [!NOTE]
    > Mirror registries are automatically added to the ignore list and do not need to be added under `spec.unauthenticatedRegistries`. Specifying the `PUBLIC_CONTAINER_REGISTRIES` environment variable in the `ConfigMap` overrides the default values with the specified value. The `PUBLIC_CONTAINER_REGISTRIES` defaults are [quay.io](https://quay.io) and [registry.svc.ci.openshift.org](https://registry.svc.ci.openshift.org).

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

Verify that you can access the newly added registry from the hub cluster by running the following commands:

</div>

1.  Open a debug shell prompt to the hub cluster:

    ``` terminal
    $ oc debug node/<node_name>
    ```

2.  Test access to the unauthenticated registry by running the following command:

    ``` terminal
    sh-4.4# podman login -u kubeadmin -p $(oc whoami -t) <unauthenticated_registry>
    ```

    where:

    \<unauthenticated_registry\>
    Is the new registry, for example, `unauthenticated-image-registry.openshift-image-registry.svc:5000`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Login Succeeded!
    ```

    </div>

# Configuring the hub cluster with ArgoCD

You can configure the hub cluster with a set of ArgoCD applications that generate the required installation and policy custom resources (CRs) for each site with GitOps Zero Touch Provisioning (ZTP).

> [!NOTE]
> Red Hat Advanced Cluster Management (RHACM) uses `SiteConfig` CRs to generate the Day 1 managed cluster installation CRs for ArgoCD. Each ArgoCD application can manage a maximum of 300 `SiteConfig` CRs.

<div>

<div class="title">

Prerequisites

</div>

- You have a OpenShift Container Platform hub cluster with Red Hat Advanced Cluster Management (RHACM) and Red Hat OpenShift GitOps installed.

- You have extracted the reference deployment from the GitOps ZTP plugin container as described in the "Preparing the GitOps ZTP site configuration repository" section. Extracting the reference deployment creates the `out/argocd/deployment` directory referenced in the following procedure.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Prepare the ArgoCD pipeline configuration:

    1.  Create a Git repository with the directory structure similar to the example directory. For more information, see "Preparing the GitOps ZTP site configuration repository".

    2.  Configure access to the repository using the ArgoCD UI. Under **Settings** configure the following:

        - **Repositories** - Add the connection information. The URL must end in `.git`, for example, `https://repo.example.com/repo.git` and credentials.

        - **Certificates** - Add the public certificate for the repository, if needed.

    3.  Modify the two ArgoCD applications, `out/argocd/deployment/clusters-app.yaml` and `out/argocd/deployment/policies-app.yaml`, based on your Git repository:

        - Update the URL to point to the Git repository. The URL ends with `.git`, for example, `https://repo.example.com/repo.git`.

        - The `targetRevision` indicates which Git repository branch to monitor.

        - `path` specifies the path to the `SiteConfig` and `PolicyGenerator` or `PolicyGentemplate` CRs, respectively.

</div>

1.  To install the GitOps ZTP plugin, patch the ArgoCD instance in the hub cluster with the relevant multicluster engine (MCE) subscription image. Customize the patch file that you previously extracted into the `out/argocd/deployment/` directory for your environment.

    1.  Select the `multicluster-operators-subscription` image that matches your RHACM version.

        - For RHACM 2.8 and 2.9, use the `registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel8:v<rhacm_version>` image.

        - For RHACM 2.10 and later, use the `registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel9:v<rhacm_version>` image.

        > [!IMPORTANT]
        > The version of the `multicluster-operators-subscription` image must match the RHACM version. Beginning with the MCE 2.10 release, RHEL 9 is the base image for `multicluster-operators-subscription` images.
        >
        > Click `[Expand for Operator list]` in the "Platform Aligned Operators" table in [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators) to view the complete supported Operators matrix for OpenShift Container Platform.

    2.  Modify the `out/argocd/deployment/argocd-openshift-gitops-patch.json` file with the `multicluster-operators-subscription` image that matches your RHACM version:

        ``` json
        {
          "args": [
            "-c",
            "mkdir -p /.config/kustomize/plugin/policy.open-cluster-management.io/v1/policygenerator && cp /policy-generator/PolicyGenerator-not-fips-compliant /.config/kustomize/plugin/policy.open-cluster-management.io/v1/policygenerator/PolicyGenerator"
          ],
          "command": [
            "/bin/bash"
          ],
          "image": "registry.redhat.io/rhacm2/multicluster-operators-subscription-rhel9:v2.10",
          "name": "policy-generator-install",
          "imagePullPolicy": "Always",
          "volumeMounts": [
            {
              "mountPath": "/.config",
              "name": "kustomize"
            }
          ]
        }
        ```

        - Optional: For RHEL 9 images, in the `args` field, change the executable path from `/policy-generator/PolicyGenerator-not-fips-compliant` to match the required universal executable for your ArgoCD version.

        - Match the `multicluster-operators-subscription` image to your RHACM version. In disconnected environments, replace the URL with the disconnected registry equivalent for your environment.

    3.  Patch the ArgoCD instance. Run the following command:

        ``` terminal
        $ oc patch argocd openshift-gitops \
        -n openshift-gitops --type=merge \
        --patch-file out/argocd/deployment/argocd-openshift-gitops-patch.json
        ```

2.  In RHACM 2.7 and later, the multicluster engine enables the `cluster-proxy-addon` feature by default. Apply the following patch to disable the `cluster-proxy-addon` feature and remove the relevant hub cluster and managed pods that are responsible for this add-on. Run the following command:

    ``` terminal
    $ oc patch multiclusterengines.multicluster.openshift.io multiclusterengine --type=merge --patch-file out/argocd/deployment/disable-cluster-proxy-addon.json
    ```

3.  Apply the pipeline configuration to your hub cluster by running the following command:

    ``` terminal
    $ oc apply -k out/argocd/deployment
    ```

4.  Optional: If you have existing ArgoCD applications, verify that the `PrunePropagationPolicy=background` policy is set in the `Application` resource by running the following command:

    ``` terminal
    $ oc -n openshift-gitops get applications.argoproj.io  \
    clusters -o jsonpath='{.spec.syncPolicy.syncOptions}' |jq
    ```

    Example output for an existing policy:

    ``` terminal
    [
      "CreateNamespace=true",
      "PrunePropagationPolicy=background",
      "RespectIgnoreDifferences=true"
    ]
    ```

    1.  If the `spec.syncPolicy.syncOption` field does not contain a `PrunePropagationPolicy` parameter or `PrunePropagationPolicy` is set to the `foreground` value, set the policy to `background` in the `Application` resource. See the following example:

        ``` yaml
        kind: Application
        spec:
          syncPolicy:
            syncOptions:
            - PrunePropagationPolicy=background
        ```

    Setting the `background` deletion policy ensures that the `ManagedCluster` CR and all its associated resources are deleted.

# Preparing the GitOps ZTP site configuration repository

Before you can use the GitOps Zero Touch Provisioning (ZTP) pipeline, you need to prepare the Git repository to host the site configuration data.

<div>

<div class="title">

Prerequisites

</div>

- You have configured the hub cluster GitOps applications for generating the required installation and policy custom resources (CRs).

- You have deployed the managed clusters using GitOps ZTP.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a directory structure with separate paths for the `SiteConfig` and `PolicyGenerator` or `PolicyGentemplate` CRs.

    > [!NOTE]
    > Keep `SiteConfig` and `PolicyGenerator` or `PolicyGentemplate` CRs in separate directories. Both the `SiteConfig` and `PolicyGenerator` or `PolicyGentemplate` directories must contain a `kustomization.yaml` file that explicitly includes the files in that directory.

2.  Export the `argocd` directory from the `ztp-site-generate` container image using the following commands:

    ``` terminal
    $ podman pull registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.17
    ```

    ``` terminal
    $ mkdir -p ./out
    ```

    ``` terminal
    $ podman run --log-driver=none --rm registry.redhat.io/openshift4/ztp-site-generate-rhel8:v4.17 extract /home/ztp --tar | tar x -C ./out
    ```

3.  Check that the `out` directory contains the following subdirectories:

    - `out/extra-manifest` contains the source CR files that `SiteConfig` uses to generate extra manifest `configMap`.

    - `out/source-crs` contains the source CR files that `PolicyGenerator` uses to generate the Red Hat Advanced Cluster Management (RHACM) policies.

    - `out/argocd/deployment` contains patches and YAML files to apply on the hub cluster for use in the next step of this procedure.

    - `out/argocd/example` contains the examples for `SiteConfig` and `PolicyGenerator` or `PolicyGentemplate` files that represent the recommended configuration.

4.  Copy the `out/source-crs` folder and contents to the `PolicyGenerator` or `PolicyGentemplate` directory.

5.  The out/extra-manifests directory contains the reference manifests for a RAN DU cluster. Copy the `out/extra-manifests` directory into the `SiteConfig` folder. This directory should contain CRs from the `ztp-site-generate` container only. Do not add user-provided CRs here. If you want to work with user-provided CRs you must create another directory for that content. For example:

    ``` text
    example/
      ├── acmpolicygenerator
      │   ├── kustomization.yaml
      │   └── source-crs/
      ├── policygentemplates
      │   ├── kustomization.yaml
      │   └── source-crs/
      └── siteconfig
            ├── extra-manifests
            └── kustomization.yaml
    ```

    > [!NOTE]
    > Using `PolicyGenTemplate` CRs to manage and deploy policies to manage clusters will be deprecated in a future OpenShift Container Platform release. Equivalent and improved functionality is available by using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.

6.  Commit the directory structure and the `kustomization.yaml` files and push to your Git repository. The initial push to Git should include the `kustomization.yaml` files.

    You can use the directory structure under `out/argocd/example` as a reference for the structure and content of your Git repository. That structure includes `SiteConfig` and `PolicyGenerator` or `PolicyGentemplate` reference CRs for single-node, three-node, and standard clusters. Remove references to cluster types that you are not using.

    For all cluster types, you must:

    - Add the `source-crs` subdirectory to the `acmpolicygenerator` or `policygentemplates` directory.

    - Add the `extra-manifests` directory to the `siteconfig` directory.

      The following example describes a set of CRs for a network of single-node clusters:

      ``` text
      example/
        ├── acmpolicygenerator
        │   ├── acm-common-ranGen.yaml
        │   ├── acm-example-sno-site.yaml
        │   ├── acm-group-du-sno-ranGen.yaml
        │   ├── group-du-sno-validator-ranGen.yaml
        │   ├── kustomization.yaml
        │   ├── source-crs/
        │   └── ns.yaml
        └── siteconfig
              ├── example-sno.yaml
              ├── extra-manifests/
              ├── custom-manifests/
              ├── KlusterletAddonConfigOverride.yaml
              └── kustomization.yaml
      ```

      where:

      `extra-manifests/`
      Contains reference manifests from the `ztp-container`.

      `custom-manifests/`
      Contains custom manifests.

</div>

> [!IMPORTANT]
> Using `PolicyGenTemplate` CRs to manage and deploy policies to managed clusters will be deprecated in an upcoming OpenShift Container Platform release. Equivalent and improved functionality is available using Red Hat Advanced Cluster Management (RHACM) and `PolicyGenerator` CRs.
>
> For more information about `PolicyGenerator` resources, see the RHACM [Integrating Policy Generator](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.13/html-single/governance/index#integrate-policy-generator) documentation.

<div>

<div class="title">

Additional resources

</div>

- [Configuring managed cluster policies by using PolicyGenerator resources](policygenerator_for_ztp/ztp-configuring-managed-clusters-policygenerator.md#ztp-configuring-managed-clusters-policygenerator)

- [Comparing RHACM PolicyGenerator and PolicyGenTemplate resource patching](policygenerator_for_ztp/ztp-configuring-managed-clusters-policygenerator.md#ztp-comparing-pgt-and-rhacm-pg-patching-strategies_ztp-configuring-managed-clusters-policygenerator)

</div>

# Preparing the GitOps ZTP site configuration repository for version independence

You can use GitOps ZTP to manage source custom resources (CRs) for managed clusters that are running different versions of OpenShift Container Platform. This means that the version of OpenShift Container Platform running on the hub cluster can be independent of the version running on the managed clusters.

> [!NOTE]
> The following procedure assumes you are using `PolicyGenerator` resources instead of `PolicyGentemplate` resources for cluster policies management.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a directory structure with separate paths for the `SiteConfig` and `PolicyGenerator` CRs.

2.  Within the `PolicyGenerator` directory, create a directory for each OpenShift Container Platform version you want to make available. For each version, create the following resources:

    - `kustomization.yaml` file that explicitly includes the files in that directory

    - `source-crs` directory to contain reference CR configuration files from the `ztp-site-generate` container

      If you want to work with user-provided CRs, you must create a separate directory for them.

3.  In the `/siteconfig` directory, create a subdirectory for each OpenShift Container Platform version you want to make available. For each version, create at least one directory for reference CRs to be copied from the container. There is no restriction on the naming of directories or on the number of reference directories. If you want to work with custom manifests, you must create a separate directory for them.

    The following example describes a structure using user-provided manifests and CRs for different versions of OpenShift Container Platform:

    ``` text
    ├── acmpolicygenerator
    │   ├── kustomization.yaml
    │   ├── version_4.13
    │   │   ├── common-ranGen.yaml
    │   │   ├── group-du-sno-ranGen.yaml
    │   │   ├── group-du-sno-validator-ranGen.yaml
    │   │   ├── helix56-v413.yaml
    │   │   ├── kustomization.yaml
    │   │   ├── ns.yaml
    │   │   └── source-crs/
    │   │      └── reference-crs/
    │   │      └── custom-crs/
    │   └── version_4.14
    │       ├── common-ranGen.yaml
    │       ├── group-du-sno-ranGen.yaml
    │       ├── group-du-sno-validator-ranGen.yaml
    │       ├── helix56-v414.yaml
    │       ├── kustomization.yaml
    │       ├── ns.yaml
    │       └── source-crs/
    │         └── reference-crs/
    │         └── custom-crs/
    └── siteconfig
        ├── kustomization.yaml
        ├── version_4.13
        │   ├── helix56-v413.yaml
        │   ├── kustomization.yaml
        │   ├── extra-manifest/
        │   └── custom-manifest/
        └── version_4.14
            ├── helix57-v414.yaml
            ├── kustomization.yaml
            ├── extra-manifest/
            └── custom-manifest/
    ```

    where:

    `kustomization.yaml` (top-level)
    Create a top-level `kustomization` YAML file.

    `version_4.13`, `version_4.14`
    Create the version-specific directories within the custom `/acmpolicygenerator` directory.

    `kustomization.yaml` (per-version)
    Create a `kustomization.yaml` file for each version.

    `source-crs/`
    Create a `source-crs` directory for each version to contain reference CRs from the `ztp-site-generate` container.

    `reference-crs/`
    Create the `reference-crs` directory for policy CRs that are extracted from the ZTP container.

    `custom-crs/`
    Optional: Create a `custom-crs` directory for user-provided CRs.

    `extra-manifest/`
    Create a directory within the custom `/siteconfig` directory to contain extra manifests from the `ztp-site-generate` container.

    `custom-manifest/`
    Create a folder to hold user-provided manifests.

    > [!NOTE]
    > In the previous example, each version subdirectory in the custom `/siteconfig` directory contains two further subdirectories, one containing the reference manifests copied from the container, the other for custom manifests that you provide. The names assigned to those directories are examples. If you use user-provided CRs, the last directory listed under `extraManifests.searchPaths` in the `SiteConfig` CR must be the directory containing user-provided CRs.

4.  Edit the `SiteConfig` CR to include the search paths of any directories you have created. The first directory that is listed under `extraManifests.searchPaths` must be the directory containing the reference manifests. Consider the order in which the directories are listed. In cases where directories contain files with the same name, the file in the final directory takes precedence.

    Example `SiteConfig` CR:

    ``` yaml
    extraManifests:
        searchPaths:
        - extra-manifest/
        - custom-manifest/
    ```

    where:

    `extra-manifest/`
    The directory containing the reference manifests must be listed first under `extraManifests.searchPaths`.

    `custom-manifest/`
    If you are using user-provided CRs, the last directory listed under `extraManifests.searchPaths` in the `SiteConfig` CR must be the directory containing those user-provided CRs.

5.  Edit the top-level `kustomization.yaml` file to control which OpenShift Container Platform versions are active. The following is an example of a `kustomization.yaml` file at the top level:

    ``` yaml
    resources:
    - version_4.13
    #- version_4.14
    ```

    where:

    `version_4.13`
    Activate version 4.13.

    `#- version_4.14`
    Use comments to deactivate a version.

</div>

# Configuring the hub cluster for backup and restore

You can use GitOps ZTP to configure a set of policies to back up `BareMetalHost` resources. This allows you to recover data from a failed hub cluster and deploy a replacement cluster using Red Hat Advanced Cluster Management (RHACM).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a policy to add the `cluster.open-cluster-management.io/backup=cluster-activation` label to all `BareMetalHost` resources that have the `infraenvs.agent-install.openshift.io` label. Save the policy as `BareMetalHostBackupPolicy.yaml`.

    The following example adds the `cluster.open-cluster-management.io/backup` label to all `BareMetalHost` resources that have the `infraenvs.agent-install.openshift.io` label:

    <div class="formalpara">

    <div class="title">

    Example Policy

    </div>

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: bmh-cluster-activation-label
      annotations:
        policy.open-cluster-management.io/description: Policy used to add the cluster.open-cluster-management.io/backup=cluster-activation label to all BareMetalHost resources
    spec:
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: set-bmh-backup-label
            spec:
              object-templates-raw: |
                {{- /* Set cluster-activation label on all BMH resources */ -}}
                {{- $infra_label := "infraenvs.agent-install.openshift.io" }}
                {{- range $bmh := (lookup "metal3.io/v1alpha1" "BareMetalHost" "" "" $infra_label).items }}
                    - complianceType: musthave
                      objectDefinition:
                        kind: BareMetalHost
                        apiVersion: metal3.io/v1alpha1
                        metadata:
                          name: {{ $bmh.metadata.name }}
                          namespace: {{ $bmh.metadata.namespace }}
                          labels:
                            cluster.open-cluster-management.io/backup: cluster-activation
                {{- end }}
              remediationAction: enforce
              severity: high
    ---
    apiVersion: cluster.open-cluster-management.io/v1beta1
    kind: Placement
    metadata:
      name: bmh-cluster-activation-label-pr
    spec:
      predicates:
        - requiredClusterSelector:
            labelSelector:
              matchExpressions:
                - key: name
                  operator: In
                  values:
                    - local-cluster
    ---
    apiVersion: policy.open-cluster-management.io/v1
    kind: PlacementBinding
    metadata:
      name: bmh-cluster-activation-label-binding
    placementRef:
      name: bmh-cluster-activation-label-pr
      apiGroup: cluster.open-cluster-management.io
      kind: Placement
    subjects:
      - name: bmh-cluster-activation-label
        apiGroup: policy.open-cluster-management.io
        kind: Policy
    ---
    apiVersion: cluster.open-cluster-management.io/v1beta2
    kind: ManagedClusterSetBinding
    metadata:
      name: default
      namespace: default
    spec:
      clusterSet: default
    ```

    </div>

    If you apply the `cluster.open-cluster-management.io/backup: cluster-activation` label to `BareMetalHost` resources, the RHACM cluster backs up those resources. You can restore the `BareMetalHost` resources if the active cluster becomes unavailable, when restoring the hub activation resources.

2.  Apply the policy by running the following command:

    ``` terminal
    $ oc apply -f BareMetalHostBackupPolicy.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Find all `BareMetalHost` resources with the label `infraenvs.agent-install.openshift.io` by running the following command:

    ``` terminal
    $ oc get BareMetalHost -A -l infraenvs.agent-install.openshift.io
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    NAMESPACE      NAME             STATE   CONSUMER   ONLINE   ERROR   AGE
    baremetal-ns   baremetal-name                      false            50s
    ```

    </div>

2.  Verify that the policy has applied the label `cluster.open-cluster-management.io/backup=cluster-activation` to all these resources, by running the following command:

    ``` terminal
    $ oc get BareMetalHost -A -l infraenvs.agent-install.openshift.io,cluster.open-cluster-management.io/backup=cluster-activation
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    NAMESPACE      NAME             STATE   CONSUMER   ONLINE   ERROR   AGE
    baremetal-ns   baremetal-name                      false            50s
    ```

    </div>

    The output must show the same list as in the previous step, which listed all `BareMetalHost` resources with the label `infraenvs.agent-install.openshift.io`. This confirms that all the `BareMetalHost` resources with the `infraenvs.agent-install.openshift.io` label also have the `cluster.open-cluster-management.io/backup: cluster-activation` label.

    The following example shows a `BareMetalHost` resource with the `infraenvs.agent-install.openshift.io` label. The resource must also have the `cluster.open-cluster-management.io/backup: cluster-activation` label, which was added by the policy created in step 1.

    ``` yaml
    apiVersion: metal3.io/v1alpha1
    kind: BareMetalHost
    metadata:
      labels:
        cluster.open-cluster-management.io/backup: cluster-activation
        infraenvs.agent-install.openshift.io: value
      name: baremetal-name
      namespace: baremetal-ns
    ```

</div>

You can now use Red Hat Advanced Cluster Management to restore a managed cluster.

> [!IMPORTANT]
> When you restore `BareMetalHost` resources as part of restoring the cluster activation data, you must restore the `BareMetalHost` status. The following RHACM `Restore` resource example restores activation resources, including `BareMetalHost`, and also restores the status for the `BareMetalHost` resources:
>
> ``` yaml
> apiVersion: cluster.open-cluster-management.io/v1beta1
> kind: Restore
> metadata:
>   name: restore-acm-bmh
>   namespace: open-cluster-management-backup
> spec:
>   cleanupBeforeRestore: CleanupRestored
>   veleroManagedClustersBackupName: latest
>   veleroCredentialsBackupName: latest
>   veleroResourcesBackupName: latest
>   restoreStatus:
>     includedResources:
>       - BareMetalHosts
> ```
>
> - Set `veleroManagedClustersBackupName: latest` to restore activation resources.
>
> - Restores the status for `BareMetalHost` resources.

<div>

<div class="title">

Additional resources

</div>

- [Restoring managed cluster activation data](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/latest/html/business_continuity/business-cont-overview#managed-cluster-activation-data)

- [Active-passive configuration](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/latest/html/business_continuity/business-cont-overview#active-passive-config)

- [Restoring activation resources](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/latest/html/business_continuity/business-cont-overview#restore-activation-resources)

</div>
