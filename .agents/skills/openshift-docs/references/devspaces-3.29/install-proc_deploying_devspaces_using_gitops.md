> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-proc_deploying_devspaces_using_gitops). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy using GitOps and Argo CD

Deploy OpenShift Dev Spaces declaratively through OpenShift GitOps (Argo CD) so that every configuration change is tracked in Git, auditable, and automatically reconciled on the cluster.

## Before you begin

- You have an OpenShift Container Platform 4.22 or later cluster with cluster-admin access.
- You have the OpenShift GitOps operator installed on the cluster. See [Installing OpenShift GitOps](https://docs.openshift.com/gitops/latest/installing_gitops/installing-openshift-gitops.html).
- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have a Git repository accessible from the cluster (GitHub, GitLab, Bitbucket, or an internal Git server).

## About this task

With this method, you store the Operator subscription and `CheCluster` configuration in a Git repository. Argo CD monitors the repository and applies changes to the cluster automatically. You manage OpenShift Dev Spaces through Git commits instead of direct cluster commands.

## Procedure

1.  In your Git repository, create a directory for the OpenShift Dev Spaces manifests. The directory contains three files: the Operator subscription, the `CheCluster` custom resource, and a Kustomize configuration.

    **Repository structure**

    ``` plaintext
    <your-gitops-repo>/
    └── devspaces/
        ├── subscription.yaml
        ├── checluster.yaml
        └── kustomization.yaml
    ```

2.  Create the `subscription.yaml` file with the namespace and Operator subscription:

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
      source: redhat-operators
      sourceNamespace: openshift-marketplace
    ```

3.  Create the `checluster.yaml` file with the OpenShift Dev Spaces instance configuration:

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
          openVSXURL: https://open-vsx.org
      devEnvironments:
        startTimeoutSeconds: 300
        defaultEditor: che-incubator/che-code/latest
        defaultNamespace:
          autoProvision: true
          template: <username>-devspaces
        storage:
          pvcStrategy: per-user
    ```

4.  Create the `kustomization.yaml` file:

    ``` yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization

    resources:
      - subscription.yaml
      - checluster.yaml
    ```

5.  Commit and push the files to your Git repository.

6.  Grant the Argo CD service account the permissions required to create namespaces and install Operators:

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

7.  Create the Argo CD `Application` resource that points to your Git repository:

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
        repoURL: <your-git-repo-url>
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

    `SkipDryRunOnMissingResource`  
    Required because the `CheCluster` custom resource definition (CRD) does not exist until the Operator installs it. This option tells Argo CD to skip validation for unknown resource types and apply them directly.

    `selfHeal`  
    Reverts manual changes on the cluster to match the Git repository state.

8.  Wait for Argo CD to sync the resources. The Operator installs first, registers the `CheCluster` CRD, and then Argo CD applies the `CheCluster` custom resource.

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

- **Sync fails with "CheCluster CRD not found"**: Verify that the Argo CD Application includes `SkipDryRunOnMissingResource=true` in the `syncOptions`.

- **Operator reports "OwnNamespace InstallModeType not supported"**: The Subscription must target the `openshift-operators` namespace (AllNamespaces mode). Do not place the Subscription in the `openshift-devspaces` namespace.

- **Sync retries but CheCluster is not created**: The Operator may still be installing. Wait for the ClusterServiceVersion to reach `Succeeded`:

  ``` bash
  $ oc get csv -n openshift-operators | grep devspaces
  ```

**Related information**  

- [Installing OpenShift GitOps](https://docs.openshift.com/gitops/latest/installing_gitops/installing-openshift-gitops.html)
- [Argo CD sync options](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/)
- [Configure the CheCluster custom resource](configure-assembly_configuring_the_checluster_custom_resource.md)
