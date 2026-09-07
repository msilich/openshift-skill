<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use the Argo CD Image Updater to automatically update container image versions for workloads managed by Argo CD. The Image Updater monitors container registries for new image versions and updates Argo CD applications when new versions are found that match user-defined constraints.

# About Argo CD Image Updater

Argo CD Image Updater automatically updates container image versions for workloads managed by Argo CD. It monitors container registries for new image tags that match configured version constraints and updates applications through Argo CD.

In the Red Hat OpenShift GitOps Operator, Argo CD Image Updater is provided as a productized controller that you enable through the Argo CD custom resource.

The Argo CD Image Updater controller runs a reconciliation loop that continuously watches configured Argo CD applications and queries container registries for newer image versions. When a qualifying new version is discovered, the controller instructs Argo CD to update the application. You define which images to track and what version constraints to enforce by creating `ImageUpdater` custom resources.

Depending on the Argo CD application sync policy, updated images are either deployed automatically or marked as out of sync for manual approval.

The Image Updater provides the following capabilities:

**Image selection and update behavior**

- Semantic version constraints, newest-build strategy, alphabetical sorting, and SHA256 digest tracking

- Tag filtering using regular expressions and glob patterns

**Application support**

- Helm and Kustomize applications

**Persistence and Git workflows**

- Direct API write-back to Argo CD Application resources

- Git commits to configuration repositories

- Pull requests and merge requests for approval workflows

**Registry integration**

- Docker Hub, Red Hat Quay, GitHub Container Registry, GitLab Container Registry, Google Container Registry, Azure Container Registry, JFrog Artifactory, and Docker Registry v2 API-compatible registries

- Authentication using Kubernetes secrets, pull secrets, environment variables, and external scripts

- Webhooks for immediate updates from Docker Hub, GitHub Container Registry, Quay, and Harbor

**Observability**

- Status conditions (`Ready`, `Reconciling`, `Error`)

- Matched application and image counts

- Update history

Argo CD Image Updater has the following limitations:

- Applications must be managed by Argo CD. Standalone Kubernetes workloads are not supported.

- Only Kustomize-rendered and Helm-rendered manifests are supported. Helm charts must expose image tag parameters for the Argo CD Image Updater controller to modify.

- Image pull secrets must exist in the same cluster where the Argo CD Image Updater controller runs.

# Enabling Argo CD Image Updater

You can enable the Argo CD Image Updater controller for an Argo CD instance by configuring the Argo CD custom resource (CR). The Argo CD Image Updater controller is namespace-scoped by default, watching only the namespace in which it is installed.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with `cluster-admin` privileges and are logged in to the web console.

- You have installed the Red Hat OpenShift GitOps Operator on your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the **Operators** → **Installed Operators** page.

2.  From the list of **Installed Operators**, select the Red Hat OpenShift GitOps Operator, and then click on the **Argo CD** tab.

3.  Select the Argo CD instance name for which you want to enable Argo CD Image Updater. For example, `openshift-gitops`.

4.  Click the **YAML** tab, and then edit and set the `spec.imageUpdater.enabled` parameter to `true`:

    **Example:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
      namespace: openshift-gitops
    spec:
      imageUpdater:
        enabled: true
    ```

5.  Click **Save**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the Image Updater controller pod is running:

    ``` terminal
    $ oc get pods -n openshift-gitops | grep image-updater
    ```

    **Example output:**

    ``` terminal
    openshift-gitops-argocd-image-updater-7d9f8c5b6-xk2lm 1/1 Running 0 2m
    ```

2.  Verify that the Image Updater controller has the necessary RBAC permissions:

    ``` terminal
    $ oc get clusterrole argocd-image-updater
    ```

</div>

# Configuring the Image Updater to watch multiple namespaces

By default, the Argo CD Image Updater controller watches only the namespace in which it is installed. To configure the Argo CD Image Updater controller to watch additional namespaces, set the `IMAGE_UPDATER_WATCH_NAMESPACES` environment variable to a comma-separated list of namespaces.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with `cluster-admin` privileges and are logged in to the web console.

- You have enabled the Argo CD Image Updater feature.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console:

    1.  Click **Operators** → **OperatorHub**, if your version of OpenShift Container Platform is 4.19 or earlier.

    2.  Click **Ecosystem** → **Software Catalog**, if your version of OpenShift Container Platform is 4.20 or later.

    3.  Type `openshift-gitops` in the **Filter by keyword** box.

2.  From the list of **Installed Operators**, select the Red Hat OpenShift GitOps Operator, and then click the **Argo CD** tab.

3.  Select your Argo CD instance.

4.  Click the **YAML** tab, and configure the `IMAGE_UPDATER_WATCH_NAMESPACES` environment variable:

    **Example:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
      namespace: openshift-gitops
    spec:
      imageUpdater:
        enabled: true
        env:
          - name: IMAGE_UPDATER_LOGLEVEL
            value: info
          - name: IMAGE_UPDATER_WATCH_NAMESPACES
            value: "openshift-gitops,team-a,team-b"
        resources:
          limits:
            cpu: 500m
            memory: 1024Mi
          requests:
            cpu: 250m
            memory: 512Mi
    ```

    where:

    `spec.imageUpdater.enabled`
    Enables the Image Updater controller.

    `spec.imageUpdater.env`
    Defines environment variables for the Image Updater controller.

    `IMAGE_UPDATER_LOGLEVEL`
    Sets the log level for the Argo CD Image Updater controller. Valid values are `debug`, `info`, `warn`, and `error`.

    `IMAGE_UPDATER_WATCH_NAMESPACES`
    Specifies a comma-separated list of namespaces that the Argo CD Image Updater controller watches for `ImageUpdater` custom resources and Argo CD Applications.

    `spec.imageUpdater.resources`
    Defines resource requests and limits for the Image Updater controller.

5.  Click **Save**.

</div>

# Understanding the ImageUpdater custom resource

To configure the Argo CD Image Updater to track and update images for an Argo CD application, you create an `ImageUpdater` custom resource (CR). The `ImageUpdater` CR specifies which Argo CD applications to monitor, which images to track, the update strategy to use, and how to write back image updates.

The `ImageUpdater` CR must reside in the same namespace as the Argo CD applications it references. The controller uses `metadata.namespace` to determine the namespace in which to search for matching applications.

The following example shows a basic `ImageUpdater` CR that matches applications whose names start with `my-app-` and tracks the `nginx` image with a version constraint of `~1.26`, which restricts updates to patch versions within the 1.26 minor release (for example, 1.26.0, 1.26.1, 1.26.2):

<div class="formalpara">

<div class="title">

Example basic ImageUpdater CR

</div>

``` yaml
apiVersion: argocd-image-updater.argoproj.io/v1alpha1
kind: ImageUpdater
metadata:
  name: my-image-updater
  namespace: openshift-gitops
spec:
  applicationRefs:
    - namePattern: "my-app-*"
      images:
        - alias: "nginx"
          imageName: "nginx:~1.26"
```

</div>

> [!IMPORTANT]
> Version constraints prevent Argo CD Image Updater from introducing breaking changes. Without a constraint, Argo CD Image Updater could update to any newer version, potentially causing compatibility issues.

> [!IMPORTANT]
> Multiple `ImageUpdater` CRs must not target the same application. If two or more CRs match the same application, they will continuously overwrite each other’s changes, causing the image version to thrash between updates. Ensure that each application is targeted by only one `ImageUpdater` CR.

# Selecting applications for image updates

The `applicationRefs` field in the `ImageUpdater` custom resource determines which Argo CD applications the Argo CD Image Updater controller monitors. Applications can be selected by name pattern, by label, or by a combination of both.

You can use glob patterns to match application names. The `namePattern` field supports glob-based selection. An exact name matches a single application, while wildcards match multiple applications.

**Example: Using a name pattern with wildcards:**

``` yaml
spec:
  applicationRefs:
    - namePattern: "frontend-*"
      images:
        - alias: "nginx"
          imageName: "nginx:~1.26"
```

You can select applications based on their Kubernetes labels. The `labelSelectors` field selects applications by their Kubernetes labels, supporting both `matchLabels` for key-value pairs and `matchExpressions` for operator-based conditions.

**Example: Using label selectors:**

``` yaml
spec:
  applicationRefs:
    - labelSelectors:
        matchLabels:
          tier: "frontend"
        matchExpressions:
          - key: env
            operator: In
            values:
              - staging
              - production
      images:
        - alias: "nginx"
          imageName: "nginx:~1.26"
```

You can combine name patterns and label selectors for more precise application selection. For example, to match only applications whose names start with `web-` and that have a `tier: "frontend"` label:

**Example: Combining name pattern and label selectors:**

``` yaml
spec:
  applicationRefs:
    - namePattern: "web-*"
      labelSelectors:
        matchLabels:
          tier: "frontend"
      images:
        - alias: "nginx"
          imageName: "nginx:~1.26"
```

Applications can provide image configuration through annotations as an alternative to CR-based configuration. When working with ApplicationSets that generate many Applications, each Application can provide its own image configuration through annotations instead of defining images in the `ImageUpdater` CR. Set `useAnnotations: true` on an `applicationRef` to enable this.

**Example: Using annotations for image configuration:**

``` yaml
spec:
  applicationRefs:
    - namePattern: "generated-app-*"
      useAnnotations: true
```

When `useAnnotations` is enabled, the controller reads image configuration from the `argocd-image-updater.argoproj.io/image-list` annotation on each matching `Application` resource.

For that `applicationRef`, any image configuration defined in the CR is ignored. Only the `namePattern` and `labelSelectors` fields remain effective.

**Example: Using annotations for image configuration:**

``` yaml
spec:
  applicationRefs:
    - namePattern: "*"
      labelSelectors:
        matchLabels:
          image-updater: my-image-updater
      useAnnotations: true
```

> [!NOTE]
> Using `useAnnotations: true` with `namePattern: "*"` and no label selectors will attempt to process all Applications in the namespace, which may impact performance.

# Update strategies

The Argo CD Image Updater supports four strategies for determining which image version to update to. Configure the strategy using the `commonUpdateSettings.updateStrategy` field.

| Strategy | Description |
|----|----|
| `semver` (default) | Updates to the highest version matching a semantic version constraint. Use this strategy when images follow semantic versioning. |
| `newest-build` | Updates to the image tag with the most recent creation timestamp, regardless of version numbering. |
| `alphabetical` | Updates to the last tag when sorted alphabetically. |
| `digest` | Tracks a mutable tag (such as `latest`) by its SHA256 digest, updating when the digest changes. |

Update strategies

**Example: Using the newest-build strategy with a tag filter:**

``` yaml
spec:
  applicationRefs:
    - namePattern: "my-app"
      images:
        - alias: "myimage"
          imageName: "myorg/myimage"
          commonUpdateSettings:
            updateStrategy: "newest-build"
            allowTags: "regexp:^v1\\.0\\.0-[0-9a-zA-Z]+$"
```

You can control which image tags are eligible for updates using the following parameters:

`allowTags`
Specifies a match function applied to every tag. Supports `regexp:<expression>` for regular expression matching and `any` (the default) to match all tags.

`ignoreTags`
Specifies a comma-separated list of glob patterns for tags to exclude from consideration.

**Example: Tag filtering with allowTags and ignoreTags:**

``` yaml
spec:
  applicationRefs:
    - namePattern: "my-app"
      images:
        - alias: "myimage"
          imageName: "myorg/myimage"
          commonUpdateSettings:
            allowTags: "regexp:^v[0-9]+\\.[0-9]+\\.[0-9]+$"
            ignoreTags: "*-rc*"
```

This example allows only tags matching a specific semantic version pattern and ignores release candidate tags.

# Write-back methods

The Argo CD Image Updater supports three methods for writing back image updates to your applications: Argo CD API method, Git method, and pull request or merge request method.

The Argo CD API method is the default write-back method and requires no additional configuration. It updates the Argo CD Application resource directly via the Kubernetes API. No additional configuration is required. This method is best suited for applications created imperatively through the Argo CD Web UI or CLI.

> [!NOTE]
> If the Application is managed in Git, syncing from Git will overwrite the Argo CD Image Updater’s changes.

The Git method provides persistent storage by committing changes to the application’s Git repository. The Argo CD Image Updater controller fetches the remote repository, checks out the target branch, creates or updates a parameter override file, and commits and pushes the change.

**Example: Git write-back method:**

``` yaml
spec:
  applicationRefs:
    - namePattern: "my-app"
      images:
        - alias: "nginx"
          imageName: "nginx:~1.26"
  writeBackConfig:
    method: "git"
    gitConfig:
      repository: "https://github.com/myorg/my-app-config.git"
      branch: "main"
```

To use credentials other than the ones configured in Argo CD, reference a Kubernetes secret:

**Example: Git write-back with custom credentials:**

``` yaml
spec:
  writeBackConfig:
    method: "git:secret:openshift-gitops/git-creds"
    gitConfig:
      branch: "main"
```

The Git method supports multiple write-back targets. By default, it creates or updates an `.argocd-source-<appName>.yaml` file in the application path. For Kustomization applications, you can set the `writeBackTarget` to `kustomization` to commit changes as a `kustomize edit set image` operation. For Helm applications, you can specify a Helm values file path using `writeBackTarget: "helmvalues:/helm/config/values.yaml"` to update the values file directly.

**Example: Kustomization write-back target:**

``` yaml
spec:
  writeBackConfig:
    method: "git"
    gitConfig:
      branch: "main"
      writeBackTarget: "kustomization"
```

**Example: Helm values file write-back target:**

``` yaml
spec:
  writeBackConfig:
    method: "git"
    gitConfig:
      branch: "main"
      writeBackTarget: "helmvalues:/helm/config/values.yaml"
```

The pull request or merge request method creates PRs or MRs for review instead of directly committing to the target branch. The PR/MR method extends the Git method by pushing changes to an auto-generated branch and opening a pull request or merge request instead of pushing directly to the target branch. This method is ideal when the target branch is protected or when image updates should go through a review workflow.

The Image Updater pushes the commit to a branch named `image-updater-<namespace>-<appName>-<sha256>` and opens a pull or merge request from that branch into the configured base branch. If a PR already exists for the same branch pair, no duplicate is created.

**Example: GitHub pull request:**

``` yaml
spec:
  writeBackConfig:
    method: "git:secret:openshift-gitops/git-creds"
    gitConfig:
      repository: "https://github.com/example/example.git"
      branch: "main"
      pullRequest:
        github: {}
```

**Example: GitLab merge request:**

``` yaml
spec:
  writeBackConfig:
    method: "git:secret:openshift-gitops/gitlab-creds"
    gitConfig:
      repository: "https://gitlab.com/org/repo.git"
      branch: "main"
      pullRequest:
        gitlab: {}
```

> [!IMPORTANT]
> PR creation requires credentials with a bearer token, such as a personal access token (PAT) or GitHub App credentials. SSH keys cannot be used for PR creation because they do not provide the HTTP token needed to call the SCM API.

# Configuring images for Helm applications

For Helm charts that use non-standard parameter names for image references, configure the `manifestTargets.helm` field in the `ImageUpdater` custom resource to explicitly map the image parameters.

<div>

<div class="title">

Procedure

</div>

1.  Configure the `name` field to specify the Helm parameter for the image repository and the `tag` field to specify the Helm parameter for the image tag:

    **Example: Mapping Helm parameters for image repository and tag:**

    ``` yaml
    spec:
      applicationRefs:
        - namePattern: "my-app"
          images:
            - alias: "myimage"
              imageName: "myorg/myimage"
              manifestTargets:
                helm:
                  name: "image.repository"
                  tag: "image.tag"
    ```

2.  If the Helm chart uses a single parameter for the full image reference (for example, `image: myorg/myimage:v1.0.0`), use the `spec` field to specify the Helm parameter.

    **Example: Mapping a single Helm parameter for full image reference:**

    ``` yaml
    spec:
      applicationRefs:
        - namePattern: "my-app"
          images:
            - alias: "myimage"
              imageName: "myorg/myimage"
              manifestTargets:
                helm:
                  spec: "image.fullRef"
    ```

</div>

# Configuring images for Kustomize applications

When replacing one image with another, for example, switching registries, use the `manifestTargets.kustomize.name` field to identify the original image in the kustomization.

<div>

<div class="title">

Procedure

</div>

1.  Configure the `manifestTargets.kustomize.name` field to specify the original image name that should be replaced. The `imageName` field specifies the new image to use, and the `name` field under `kustomize` specifies the original image name to replace in the kustomization:

    **Example: Replacing an image for Kustomize applications:**

    ``` yaml
    spec:
      applicationRefs:
        - namePattern: "my-app"
          images:
            - alias: "argocd"
              imageName: "ghcr.io/argoproj/argocd:latest"
              manifestTargets:
                kustomize:
                  name: "quay.io/argoproj/argocd"
    ```

</div>

# Configuring container registries

The Argo CD Image Updater works with most container registries that implement the Docker Registry v2 API out of the box. For custom or private registries, you can configure registry settings in the `argocd-image-updater-config` ConfigMap.

The Image Updater works with the following container registries out of the box:

- Docker Hub (docker.io)

- Red Hat Quay (quay.io)

- GitHub Container Registry (ghcr.io)

- GitLab Container Registry (registry.gitlab.com)

- Google Container Registry (gcr.io)

- Azure Container Registry (azurecr.io)

- JFrog Artifactory

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with `cluster-admin` privileges.

- You have installed the Red Hat OpenShift GitOps Operator on your cluster.

- You have enabled the Argo CD Image Updater.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create or edit the `argocd-image-updater-config` config map in the namespace where your Argo CD instance is installed. Configure the registry with a descriptive name, the registry prefix that matches the beginning of image names, the API URL for the registry, credentials for authentication, and whether this registry should be used as the default for images without a registry prefix:

    <div class="formalpara">

    <div class="title">

    Example: Custom registry configuration

    </div>

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: argocd-image-updater-config
      namespace: openshift-gitops
    data:
      registries.conf: |
        registries:
        - name: My Private Registry
          prefix: myregistry.example.com
          api_url: https://myregistry.example.com
          credentials: secret:openshift-gitops/registry-creds#creds
          default: false
    ```

    </div>

2.  Apply the config map:

    ``` terminal
    $ oc apply -f argocd-image-updater-config.yaml
    ```

</div>

# Configuring pull secrets for image registries

Per-image pull secrets authenticate with private container registries. The `pullSecret` field supports the following formats:

**Pull secret formats:**

| Format | Description |
|----|----|
| `secret:<namespace>/<secret_name>#<field>` | Reads credentials from a specific field in a Kubernetes secret. The value must be in `<username>:<password>` format. |
| `pullsecret:<namespace>/<secret_name>` | Uses a Docker-style pull secret (`.dockerconfigjson`). |
| `env:<variable_name>` | Reads credentials from an environment variable. The value must be in `<username>:<password>` format. |
| `ext:<path_to_script>` | Executes a script that outputs `<username>:<password>` to stdout. |

<div>

<div class="title">

Procedure

</div>

1.  Configure the `pullSecret` field in your `ImageUpdater` custom resource to specify the authentication credentials:

    **Example: Using a pull secret**

    ``` yaml
    spec:
      applicationRefs:
        - namePattern: "my-app"
          images:
            - alias: "myimage"
              imageName: "myregistry.example.com/myorg/myimage:~1.0"
              pullSecret: "pullsecret:openshift-gitops/myregistry-pull-secret"
    ```

</div>

# Configuring webhooks for immediate image updates

By default, the Argo CD Image Updater discovers new image versions by periodically polling container registries. You can also configure webhooks so that registries push notifications to the Image Updater immediately when a new image is available, eliminating the delay between image publication and update.

| Registry                              | `type` query parameter value |
|---------------------------------------|------------------------------|
| Docker Hub                            | `docker.io`                  |
| GitHub Container Registry (GHCR)      | `ghcr.io`                    |
| Harbor                                | `harbor`                     |
| Quay                                  | `quay.io`                    |
| Aliyun ACR                            | `aliyun-acr`                 |
| AWS ECR (via EventBridge CloudEvents) | `cloudevents`                |

Supported webhook registries

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with `cluster-admin` privileges.

- You have installed the Red Hat OpenShift GitOps Operator on your cluster.

- You have enabled the Argo CD Image Updater.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the `ENABLE_WEBHOOK` and `WEBHOOK_PORT` environment variables in the Argo CD CR:

    <div class="formalpara">

    <div class="title">

    Example: Enabling the webhook server

    </div>

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
      namespace: openshift-gitops
    spec:
      imageUpdater:
        enabled: true
        env:
          - name: ENABLE_WEBHOOK
            value: "true"
          - name: WEBHOOK_PORT
            value: "8082"
    ```

    </div>

2.  Apply the changes:

    ``` terminal
    $ oc apply -f argocd.yaml
    ```

    The webhook server exposes two endpoints:

    - `/webhook` — receives and processes registry notifications

    - `/healthz` — health check endpoint for liveness probes

      Registry webhook URLs include a `type` query parameter that identifies the registry. For example: `https://image-updater.example.com/webhook?type=docker.io`.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify the webhook server is running:

    ``` terminal
    $ oc logs -n openshift-gitops deployment/openshift-gitops-argocd-image-updater | grep webhook
    ```

    **Example output:**

    ``` terminal
    INFO  Starting webhook server on port 8082
    INFO  Webhook TLS enabled: true
    ```

</div>

## Configuring webhook secrets

Webhook secrets validate incoming notifications and prevent unauthorized triggers. Configure the secret for each registry using environment variables in the Argo CD CR, replacing `<YOUR_SECRET>` with your actual webhook secret.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with `cluster-admin` privileges.

- You have installed the Red Hat OpenShift GitOps Operator on your cluster.

- You have enabled the Argo CD Image Updater.

- You have configured webhooks for Argo CD Image Updater.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure webhook secrets for your registries in the Argo CD CR:

    **Example: Configuring webhook secrets:**

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
      namespace: openshift-gitops
    spec:
      imageUpdater:
        enabled: true
        env:
          - name: ENABLE_WEBHOOK
            value: "true"
          - name: DOCKER_WEBHOOK_SECRET
            value: <YOUR_SECRET>
          - name: GHCR_WEBHOOK_SECRET
            value: <YOUR_SECRET>
          - name: HARBOR_WEBHOOK_SECRET
            value: <YOUR_SECRET>
          - name: QUAY_WEBHOOK_SECRET
            value: <YOUR_SECRET>
    ```

2.  Apply the changes:

    ``` terminal
    $ oc apply -f argocd.yaml
    ```

    > [!NOTE]
    > GitHub Container Registry and Harbor have built-in secret validation. Configure the secret in the registry’s webhook settings as documented by those registries. For Docker Hub and Quay, append `&secret=<YOUR_SECRET>` to the webhook URL.

</div>

## Configuring TLS for webhooks

The webhook server uses TLS 1.3 by default for secure communication. It loads certificates from the `argocd-image-updater-tls` Secret, or generates a self-signed certificate if none is provided.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with `cluster-admin` privileges.

- You have installed the Red Hat OpenShift GitOps Operator on your cluster.

- You have enabled the Argo CD Image Updater.

- You have configured webhooks for Argo CD Image Updater.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To disable TLS, set the `DISABLE_TLS` environment variable to `true` in the Argo CD CR:

    **Example: Disabling TLS for webhooks:**

    ``` yaml
    spec:
      imageUpdater:
        enabled: true
        env:
          - name: ENABLE_WEBHOOK
            value: "true"
          - name: DISABLE_TLS
            value: "true"
    ```

</div>

## Configuring rate limiting for webhooks

Rate limiting on the `/webhook` endpoint prevents resource overload from high-volume notifications. The `WEBHOOK_RATELIMIT_ALLOWED` environment variable controls the maximum requests allowed (default: `0` for disabled). When the limit is exceeded, requests are queued rather than rejected.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster with `cluster-admin` privileges.

- You have installed the Red Hat OpenShift GitOps Operator on your cluster.

- You have enabled the Argo CD Image Updater.

- You have configured webhooks for Argo CD Image Updater.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the `WEBHOOK_RATELIMIT_ALLOWED` environment variable in the Argo CD CR:

    **Example: Configuring webhook rate limiting:**

    ``` yaml
    spec:
      imageUpdater:
        enabled: true
        env:
          - name: ENABLE_WEBHOOK
            value: "true"
          - name: WEBHOOK_RATELIMIT_ALLOWED
            value: "100"
    ```

</div>

# Monitoring Image Updater status

The `ImageUpdater` custom resource exposes a status subresource with standard Kubernetes conditions that provide information about the operational state of the Argo CD Image Updater controller.

<div>

<div class="title">

Prerequisites

</div>

- You have created an `ImageUpdater` custom resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To inspect the status of an `ImageUpdater` CR, run the following command:

    ``` terminal
    $ oc get imageupdater my-image-updater -o yaml
    ```

    **Example output:**

    ``` yaml
    status:
      conditions:
      - lastTransitionTime: "2026-06-03T10:00:00Z"
        message: Image Updater is operating normally
        reason: ReconciliationSucceeded
        status: "True"
        type: Ready
      - lastTransitionTime: "2026-06-03T10:00:00Z"
        message: Actively processing updates
        reason: ProcessingUpdates
        status: "True"
        type: Reconciling
      matchedApplications: 3
      matchedImages: 5
      lastUpdateHistory:
      - timestamp: "2026-06-03T09:55:00Z"
        application: my-app-1
        image: nginx:1.26.1
        previousVersion: 1.26.0
    ```

    The Argo CD Image Updater controller reports its operational state using standard Kubernetes conditions. The `ImageUpdater` CR status includes the following standard Kubernetes conditions:

    `Ready`
    Indicates that the Argo CD Image Updater controller is operating normally.

    `Reconciling`
    Indicates that the Argo CD Image Updater controller is actively processing updates.

    `Error`
    Indicates that an error has occurred during reconciliation. Check the condition message for details.

</div>

# Complete ImageUpdater example

The following example shows a complete `ImageUpdater` custom resource that tracks two images for a Helm-based application, uses semantic versioning constraints, and writes back updates as pull requests to a GitHub repository. This example demonstrates tracking a frontend image with patch version updates within 2.0, a backend image with minor and patch updates within 1.x using semantic versioning strategy, pull secret authentication, and Git write-back with GitHub pull request creation.

**Example: Complete ImageUpdater CR:**

``` yaml
apiVersion: argocd-image-updater.argoproj.io/v1alpha1
kind: ImageUpdater
metadata:
  name: my-app-updater
  namespace: openshift-gitops
spec:
  applicationRefs:
    - namePattern: "my-app"
      images:
        - alias: "frontend"
          imageName: "myorg/frontend:~2.0"
          manifestTargets:
            helm:
              name: "frontend.image.repository"
              tag: "frontend.image.tag"
        - alias: "backend"
          imageName: "myorg/backend:^1.5"
          commonUpdateSettings:
            updateStrategy: "semver"
            allowTags: "regexp:^v[0-9]+\\.[0-9]+\\.[0-9]+$"
          manifestTargets:
            helm:
              name: "backend.image.repository"
              tag: "backend.image.tag"
          pullSecret: "pullsecret:openshift-gitops/myregistry-pull-secret"
  writeBackConfig:
    method: "git:secret:openshift-gitops/git-creds"
    gitConfig:
      repository: "https://github.com/myorg/my-app-config.git"
      branch: "main"
      pullRequest:
        github: {}
```

# Additional resources

- [Argo CD Image Updater upstream documentation](https://argocd-image-updater.readthedocs.io/en/stable/)

- [Image Updater in the Argo CD Operator documentation](https://argocd-operator.readthedocs.io/en/latest/usage/image-updater/)

- [Argo CD Image Updater GitHub repository](https://github.com/argoproj-labs/argocd-image-updater)

- [Installing a user-defined Argo CD instance](setting-up-argocd-instance.md#gitops-argo-cd-installation_setting-up-argocd-instance)

- [Argo CD custom resource and component properties](argo-cd-cr-component-properties.md#argo-cd-cr-component-properties)
