<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `argocd.argoproj.io/managed-by-url` annotation to specify which Argo CD instance manages an Application resource. This configuration ensures that application links in the user interface resolve to the correct instance in multi-instance environments.

# Overview of the managed-by-url annotation

The `argocd.argoproj.io/managed-by-url` annotation allows an Application resource to specify which Argo CD instance manages it. This annotation ensures application links in the user interface point to the correct managing instance.

When you use multiple Argo CD instances with the app-of-apps pattern:

- A primary Argo CD instance creates a parent Application.

- The parent Application deploys child Applications that a secondary Argo CD instance manages.

- Without the annotation, clicking on child Applications in the primary instance’s user interface attempts to open them in the primary instance, which is incorrect.

- With the annotation, child Applications correctly open in the secondary instance.

The `managed-by-url` annotation ensures application links redirect to the correct Argo CD instance.

> [!NOTE]
> This annotation is particularly useful in multitenant setups where different teams have their own Argo CD instances, or in hub-and-spoke architectures where a central instance manages multiple edge instances.

# Configuring the managed-by-url annotation

You can configure the `argocd.argoproj.io/managed-by-url` annotation to direct application links to the correct Argo CD instance in multi-instance environments.

<div>

<div class="title">

Prerequisites

</div>

- You have access to multiple Argo CD instances.

- You are using a GitOps workflow with Application resources.

- You have permissions to create and modify Application manifests.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a parent Application in the primary Argo CD instance:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: parent-app
      namespace: argocd
    spec:
      project: default
      source:
        repoURL: https://github.com/YOUR-ORG/my-apps-repo.git
        targetRevision: main
        path: path-to-child-app
      destination:
        server: https://kubernetes.default.svc
        namespace: namespace-b
      syncPolicy:
        automated:
          selfHeal: true
          prune: true
    ```

    The parent Application deploys child Applications from the specified repository.

2.  Add the `managed-by-url` annotation to the child Application definition in your Git repository. Replace `https://secondary-argocd.example.com` with the actual URL of your secondary Argo CD instance:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: child-app
      namespace: namespace-b
      annotations:
        argocd.argoproj.io/managed-by-url: "https://secondary-argocd.example.com"
    spec:
      project: default
      source:
        repoURL: https://github.com/YOUR-ORG/my-apps-repo.git
        targetRevision: main
        path: path-to-child-app
      destination:
        server: https://kubernetes.default.svc
        namespace: namespace-b
      syncPolicy:
        automated:
          selfHeal: true
          prune: true
    ```

    The annotation defines the Argo CD instance that manages the child Application.

3.  Apply or sync the parent Application.

</div>

<div>

<div class="title">

Verification

</div>

1.  Log in to the primary Argo CD instance.

2.  Navigate to the `parent-app` Application.

3.  Select the `child-app` resource from the resource tree.

4.  Verify that the link opens in the correct Argo CD instance at the URL specified in the annotation.

</div>

# Managed-by-url annotation reference

The `argocd.argoproj.io/managed-by-url` annotation specifies the Argo CD instance URL that manages an Application resource.

| Field      | Value                               |
|------------|-------------------------------------|
| Annotation | `argocd.argoproj.io/managed-by-url` |
| Target     | Application                         |
| Value      | Valid HTTP(S) URL                   |
| Required   | No                                  |

The annotation value must be a valid HTTP or HTTPS URL.

The following are the examples of valid annotation values:

- `https://argocd.example.com`

- `https://argocd.example.com:8080`

- `http://localhost:8080`

The following are the examples of invalid annotation values:

- `argocd.example.com` - Missing protocol

- `javascript:alert(1)` - Invalid protocol

Invalid values prevent Argo CD from creating or updating the Application.

Argo CD determines application links as follows:

- Without the annotation, Argo CD uses the current instance URL.

- With the annotation, Argo CD uses the specified URL.

- With an invalid value, Argo CD falls back to the current instance and logs a warning.

> [!WARNING]
> Ensure that the specified URL is accessible from user browsers. Configure DNS or network access as required for internal deployments.

# Troubleshooting the managed-by-url annotation

Use the following guidelines to troubleshoot issues with the `argocd.argoproj.io/managed-by-url` annotation.

If links point to the wrong instance, check if the annotation is present:

``` terminal
$ kubectl get application <child-app-name> -n <namespace> \
  -o jsonpath='{.metadata.annotations.argocd\.argoproj\.io/managed-by-url}'
```

where:

`<child-app-name>`
Specifies the name of the child Argo CD Application whose annotation you want to retrieve.

`<namespace>`
Specifies the namespace in which the child Application resource exists.

Expected output:

``` terminal
http://localhost:8081
```

The output displays a complete URL such as `http://localhost:8081` or your configured URL such as `https://secondary-argocd.example.com`.

If the annotation is present but links do not work:

- Verify that the URL is reachable from your browser.

- Check the browser console for errors.

- Ensure that the URL includes the correct protocol (`http://` or `https://`).

If Application creation fails with an "invalid managed-by URL" error, verify the following:

- Verify that the URL includes a protocol (`https://` or `http://`).

- Check for typos in the URL.

- Ensure the URL uses only valid characters.

- Avoid unsupported schemes such as `javascript:`.

If nested Applications are not working in app-of-apps patterns, ensure the following:

1.  The child Application YAML in Git includes the annotation.

2.  The parent Application synced successfully.

3.  The child Application exists in the cluster.

Verify that the child Application exists:

``` terminal
$ kubectl get application <child-app-name> -n <namespace>
```

where:

`<child-app-name>`
Specifies the name of the child Application resource to verify.

`<namespace>`
Specifies the namespace where the child Application is expected to exist.

If the child Application does not exist, check the parent Application sync status and logs.

# Additional resources

- [Application deletion, Argo CD upstream documentation](https://argo-cd.readthedocs.io/en/stable/user-guide/app_deletion/)
