<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Red Hat OpenShift GitOps **Environments** page in the **Developer** perspective of the OpenShift Container Platform web console shows a list of the successful deployments of the application environments, along with links to the revision for each deployment.

The **Application environments** page in the **Developer** perspective of the OpenShift Container Platform web console displays the health status of application resources, such as routes, synchronization status, deployment configurations, and deployment history.

# Settings for environment labels and annotations

Configure specific labels and annotations in your application and namespace manifests to enable environment monitoring in the OpenShift Container Platform web console. These settings allow the GitOps Operator to identify and track your application environments.

**Environment labels**

The environment application manifest must include the `labels.openshift.gitops/environment` and `destination.namespace` fields. The value of the `openshift.gitops/environment` label must match both the `destination.namespace` value and the application manifest name.

Example environment application manifest specification:

``` yaml
spec:
  labels:
    openshift.gitops/environment: <environment_name>
  destination:
    namespace: <environment_name>
# ...
```

Example of an environment application manifest:

``` yaml
apiVersion: argoproj.io/v1beta1
kind: Application
metadata:
  name: dev-env
  namespace: openshift-gitops
spec:
  labels:
    openshift.gitops/environment: dev-env
  destination:
    namespace: dev-env
# ...
```

where:

`metadata.name`
Specifies the name of the environment application manifest. This value must match the `openshift.gitops/environment` label value and the `destination.namespace` value.

**Environment annotations**

The environment namespace manifest must include the `annotations.app.openshift.io/vcs-uri` and `annotations.app.openshift.io/vcs-ref` fields to specify the version control source repository of the application. The namespace name must match the environment name that the application manifest defines.

Example environment namespace manifest specification:

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    app.openshift.io/vcs-uri: <application_source_url>
    app.openshift.io/vcs-ref: <branch_reference>
  name: <environment_name>
# ...
```

where:

metadata.name
Specifies the name of the environment namespace. This value must match the environment name defined in the application manifest.

Example of an environment namespace manifest:

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    app.openshift.io/vcs-uri: https://example.com/<your_domain>/<your_gitops.git>
    app.openshift.io/vcs-ref: main
  labels:
    argocd.argoproj.io/managed-by: openshift-gitops
  name: dev-env
# ...
```

# Checking health information

Check the health status and deployment history of your GitOps-managed applications using the GitOps environments monitoring interface in the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator from **OperatorHub**.

- Your applications are managed and synchronized by Argo CD.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, navigate to the **Developer** perspective and click **Environments**. The **Environments** page shows the list of applications along with their **Environment status**.

2.  Hover over the icons under the **Environment status** column to see the synchronization status of all the environments.

3.  Click the application name from the list to view the details of a specific application.

4.  In the **Application environments** page, view the Resources section under the **Overview** tab to check the resource health status:

    - A broken heart icon indicates that resource issues have degraded the application’s performance.

    - A yellow yield sign icon indicates that resource issues have delayed the health status data.

5.  Optional: In the **Application environments** page, click the **Deployment History** tab to view the deployment history. The page displays details such as `Last deployment`, `Description (commit message)`, `Environment`, `Author`, and `Revision`.

</div>
