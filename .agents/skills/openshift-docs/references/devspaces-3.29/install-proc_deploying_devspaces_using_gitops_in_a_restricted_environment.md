> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-proc_deploying_devspaces_using_gitops_in_a_restricted_environment). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy with GitOps in an air-gapped environment

Deploy OpenShift Dev Spaces in a restricted network through OpenShift GitOps (Argo CD) by mirroring the required container images to a private registry and storing the deployment manifests in an internal Git repository.

## Before you begin

- You have an OpenShift cluster with at least 64 GB of disk space.
- You have an OpenShift cluster ready to operate on a restricted network. See [About disconnected installation mirroring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/installing-mirroring-disconnected-about) and [Using Operator Lifecycle Manager on restricted networks](https://docs.openshift.com/container-platform/4.22/operators/admin/olm-restricted-networks.html).
- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have an active `oc registry` session to the `registry.redhat.io` Red Hat Ecosystem Catalog. See [Red Hat Container Registry authentication](https://access.redhat.com/RegistryAuthentication).
- You have `opm` installed. See [Installing the `opm` CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/opm/cli-opm-install.html).
- You have `jq` installed. See [Downloading `jq`](https://stedolan.github.io/jq/download/).
- You have `podman` installed. See [Podman Installation Instructions](https://podman.io/docs/installation).
- You have `skopeo` version 1.6 or higher installed. See [Installing Skopeo](https://github.com/containers/skopeo/blob/main/install.md).
- You have an active `skopeo` session with administrative access to the private Docker registry. See [Authenticating to a registry](https://github.com/containers/skopeo#authenticating-to-a-registry) and [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/installing-mirroring-disconnected-about).
- You have `dsc` for OpenShift Dev Spaces version 3.29 installed. See [Installing the dsc management tool](plan-proc_installing_the_dsc_management_tool.md).
- You have the OpenShift GitOps operator installed on the cluster. See [Installing OpenShift GitOps](https://docs.openshift.com/gitops/latest/installing_gitops/installing-openshift-gitops.html).
- You have an internal Git repository accessible from the cluster.

## About this task

In a disconnected environment, the cluster cannot pull images from public registries or sync from external Git repositories. You mirror the required images to an internal registry, store the OpenShift Dev Spaces manifests in an internal Git repository, and let Argo CD reconcile the deployment from inside the network.

## Procedure

1.  Download and execute the mirroring script to install a custom Operator catalog and mirror the related images: [prepare-restricted-environment.sh](https://raw.githubusercontent.com/eclipse-che/che-docs/main/modules/administration-guide/attachments/restricted-environment/prepare-restricted-environment.sh).

    ``` bash
    $ bash prepare-restricted-environment.sh \
      --devworkspace_operator_index registry.redhat.io/redhat/redhat-operator-index:v4.22\
      --devworkspace_operator_version "v0.41.0" \
      --prod_operator_index "registry.redhat.io/redhat/redhat-operator-index:v4.22" \
      --prod_operator_package_name "devspaces" \
      --prod_operator_bundle_name "devspacesoperator" \
      --prod_operator_version "v3.29.0" \
      --my_registry "<my_registry>"
    ```

    where:

    ` `*`<my_registry>`*` `  
    The private Docker registry where the images will be mirrored

2.  In your internal Git repository, create a directory for the OpenShift Dev Spaces manifests with three files: the Operator subscription, the `CheCluster` custom resource, and a Kustomize configuration.

    **Repository structure**

    ``` plaintext
    <your-gitops-repo>/
    └── devspaces/
        ├── subscription.yaml
        ├── checluster.yaml
        └── kustomization.yaml
    ```

3.  Create the `subscription.yaml` file with the namespace and Operator subscription pointing to the disconnected catalog source:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: openshift-devspaces
    ---
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: devspaces
      namespace: openshift-operators
    spec:
      channel: stable
      installPlanApproval: Automatic
      name: devspaces
      source: devspaces-disconnected-install
      sourceNamespace: openshift-marketplace
    ```

    The `source` field points to the disconnected catalog source created by the mirroring script in the prerequisites.

4.  Create the `checluster.yaml` file with the OpenShift Dev Spaces instance configuration pointing to your private registry:

    ``` yaml
    apiVersion: org.eclipse.che/v2
    kind: CheCluster
    metadata:
      name: devspaces
      namespace: openshift-devspaces
    spec:
      components:
        cheServer:
          debug: false
          logLevel: INFO
        metrics:
          enable: true
        pluginRegistry:
          openVSXURL: ""
      containerRegistry:
        hostname: <your-private-registry>
        organization: <your-registry-organization>
      devEnvironments:
        startTimeoutSeconds: 600
        defaultEditor: che-incubator/che-code/latest
        defaultNamespace:
          autoProvision: true
          template: <username>-devspaces
        storage:
          pvcStrategy: per-user
    ```

    `containerRegistry.hostname`  
    The hostname of your private container registry that holds the mirrored images.

    `containerRegistry.organization`  
    The organization or project path in your private registry.

    `pluginRegistry.openVSXURL`  
    Set to an empty string to disable external Open VSX access. Use an internal Open VSX instance if IDE extensions are required.

    `startTimeoutSeconds`  
    Increased to 600 seconds to allow for slower image pulls from internal registries.

5.  Create the `kustomization.yaml` file:

    ``` yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization

    resources:
      - subscription.yaml
      - checluster.yaml
    ```

6.  Commit and push the files to your internal Git repository.

7.  Grant the Argo CD service account the permissions required to create namespaces and install Operators:

    ``` bash
    $ oc apply -f - <<EOF
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: openshift-gitops-devspaces-installer
    rules:
      - apiGroups: [""]
        resources: ["namespaces"]
        verbs: ["get", "list", "create", "update", "patch"]
      - apiGroups: ["operators.coreos.com"]
        resources: ["subscriptions", "operatorgroups"]
        verbs: ["get", "list", "create", "update", "patch", "delete"]
      - apiGroups: ["org.eclipse.che"]
        resources: ["checlusters"]
        verbs: ["get", "list", "create", "update", "patch", "delete"]
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: openshift-gitops-devspaces-installer
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: openshift-gitops-devspaces-installer
    subjects:
      - kind: ServiceAccount
        name: openshift-gitops-argocd-application-controller
        namespace: openshift-gitops
    EOF
    ```

8.  Create the Argo CD `Application` resource that points to your internal Git repository:

    ``` bash
    $ oc apply -f - <<EOF
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: devspaces
      namespace: openshift-gitops
    spec:
      project: default
      source:
        repoURL: <your-internal-git-repo-url>
        targetRevision: main
        path: devspaces
      destination:
        server: https://kubernetes.default.svc
      syncPolicy:
        automated:
          selfHeal: true
          prune: true
        retry:
          limit: 10
          backoff:
            duration: 30s
            factor: 2
            maxDuration: 5m
        syncOptions:
          - CreateNamespace=true
          - ServerSideApply=true
          - SkipDryRunOnMissingResource=true
    EOF
    ```

9.  Wait for Argo CD to sync the resources. In a restricted environment, the Operator installation takes longer because images are pulled from the internal registry.

## Results

1.  Verify that the Argo CD Application reports `Synced` and `Healthy`:

    ``` bash
    $ oc get application devspaces -n openshift-gitops \
        -o jsonpath='{.status.sync.status}{" "}{.status.health.status}'
    ```

    Expected output: `Synced Healthy`

2.  Verify that the `CheCluster` is active:

    ``` bash
    $ oc get checluster devspaces -n openshift-devspaces \
        -o jsonpath='{.status.chePhase}'
    ```

    Expected output: `Active`

3.  Retrieve the OpenShift Dev Spaces dashboard URL and open it in a browser:

    ``` bash
    $ oc get checluster devspaces -n openshift-devspaces \
        -o jsonpath='{.status.cheURL}'
    ```

- **Image pull errors**: Verify that all required images are mirrored to your private registry and that the `ImageContentSourcePolicy` or `ImageDigestMirrorSet` is configured correctly.
- **Sync fails with "CheCluster CRD not found"**: Verify that the Argo CD Application includes `SkipDryRunOnMissingResource=true` in the `syncOptions`.
- **Operator reports "OwnNamespace InstallModeType not supported"**: The Subscription must target the `openshift-operators` namespace. Do not place the Subscription in the `openshift-devspaces` namespace.
- **Network policies block workspace traffic**: Allow incoming traffic from the `openshift-devspaces` namespace to user namespaces. See [Restrict network traffic between workspaces](configure-proc_configuring_network_policies.md).

**Related tasks**  

- [Deploy using GitOps and Argo CD](install-proc_deploying_devspaces_using_gitops.md "Deploy OpenShift Dev Spaces declaratively through OpenShift GitOps (Argo CD) so that every configuration change is tracked in Git, auditable, and automatically reconciled on the cluster.")

**Related information**  

- [Installing OpenShift GitOps](https://docs.openshift.com/gitops/latest/installing_gitops/installing-openshift-gitops.html)
- [About disconnected installation mirroring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/disconnected_environments/installing-mirroring-disconnected-about)
